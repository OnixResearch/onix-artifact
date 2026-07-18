{
  description = "Product-neutral artifact authentication statements and policy decisions";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    rust-overlay = {
      url = "github:oxalica/rust-overlay";
      inputs.nixpkgs.follows = "nixpkgs";
    };
    cairn = {
      url = "github:OnixResearch/cairn/cf5c4a5c10361ca20a13addf14954407d6857028";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs =
    {
      self,
      nixpkgs,
      rust-overlay,
      cairn,
    }:
    let
      systems = [
        "x86_64-linux"
        "aarch64-linux"
      ];
      eachSystem = function: nixpkgs.lib.genAttrs systems (system: function system);
    in
    {
      packages = eachSystem (
        system:
        let
          pkgs = import nixpkgs {
            inherit system;
            overlays = [ (import rust-overlay) ];
          };
          toolchain = pkgs.rust-bin.fromRustupToolchainFile ./rust-toolchain.toml;
          rustPlatform = pkgs.makeRustPlatform {
            cargo = toolchain;
            rustc = toolchain;
          };
        in
        {
          artifact-auth = rustPlatform.buildRustPackage {
            pname = "artifact-auth";
            version = "0.1.0";
            src = self;
            cargoLock.lockFile = ./Cargo.lock;
            cargoBuildFlags = [ "--workspace" ];
            cargoTestFlags = [ "--workspace" ];
            installPhase = ''
              mkdir -p "$out/share/artifact-auth" "$out/share/doc/artifact-auth" "$out/share/licenses/artifact-auth"
              cp config/repository.json "$out/share/artifact-auth/repository.json"
              cp release/profile.json "$out/share/artifact-auth/release-profile.json"
              cp README.md docs/*.md "$out/share/doc/artifact-auth/"
              cp LICENSE LICENSE-MIT LICENSE-APACHE NOTICE "$out/share/licenses/artifact-auth/"
            '';
          };
          default = self.packages.${system}.artifact-auth;
        }
      );

      checks = eachSystem (
        system:
        let
          pkgs = import nixpkgs {
            inherit system;
            overlays = [ (import rust-overlay) ];
          };
          toolchain = pkgs.rust-bin.fromRustupToolchainFile ./rust-toolchain.toml;
          rustPlatform = pkgs.makeRustPlatform {
            cargo = toolchain;
            rustc = toolchain;
          };
          noStdCheck =
            name: package: target:
            rustPlatform.buildRustPackage {
              pname = name;
              version = "0.1.0";
              src = self;
              cargoLock.lockFile = ./Cargo.lock;
              cargoBuildFlags = [
                "-p"
                package
                "--no-default-features"
              ]
              ++ pkgs.lib.optionals (target != null) [
                "--target"
                target
              ];
              doCheck = false;
              installPhase = ''
                touch "$out"
              '';
            };
        in
        {
          cargo-test = rustPlatform.buildRustPackage {
            pname = "artifact-auth-tests";
            version = "0.1.0";
            src = self;
            cargoLock.lockFile = ./Cargo.lock;
            cargoBuildFlags = [ "--workspace" ];
            cargoTestFlags = [ "--workspace" ];
          };

          cargo-clippy = rustPlatform.buildRustPackage {
            pname = "artifact-auth-clippy";
            version = "0.1.0";
            src = self;
            cargoLock.lockFile = ./Cargo.lock;
            buildPhase = ''
              cargo clippy --workspace --all-targets --offline -- -D warnings
            '';
            doCheck = false;
            installPhase = ''
              touch "$out"
            '';
          };

          cargo-format =
            pkgs.runCommand "artifact-auth-format"
              {
                nativeBuildInputs = [ toolchain ];
                src = self;
              }
              ''
                set -eu
                cd "$src"
                cargo fmt --all -- --check
                touch "$out"
              '';

          core-no-std-host = noStdCheck "artifact-auth-core-no-std-host" "artifact-auth-core" null;
          core-no-std-wasm =
            noStdCheck "artifact-auth-core-no-std-wasm" "artifact-auth-core"
              "wasm32-unknown-unknown";
          ed25519-no-std-host = noStdCheck "artifact-auth-ed25519-no-std-host" "artifact-auth-ed25519" null;
          ed25519-no-std-wasm =
            noStdCheck "artifact-auth-ed25519-no-std-wasm" "artifact-auth-ed25519"
              "wasm32-unknown-unknown";

          nickel-contracts =
            pkgs.runCommand "artifact-auth-nickel-contracts"
              {
                nativeBuildInputs = [ pkgs.nickel ];
                src = self;
              }
              ''
                set -eu
                cd "$src"
                nickel typecheck config/repository.ncl
                nickel typecheck release/profile.ncl
                nickel export --format json config/repository.ncl > "$TMPDIR/repository.json"
                nickel export --format json release/profile.ncl > "$TMPDIR/profile.json"
                cmp "$TMPDIR/repository.json" config/repository.json
                cmp "$TMPDIR/profile.json" release/profile.json
                touch "$out"
              '';

          # r[verify artifact_auth.core.authority_free]
          # r[verify artifact_auth.conformance.consumers]
          cairn-validation =
            pkgs.runCommand "artifact-auth-cairn-validation"
              {
                nativeBuildInputs = [ cairn.packages.${system}.cairn ];
                src = self;
              }
              ''
                set -eu
                cairn policy export \
                  --source "$src/cairn-policy/default.ncl" \
                  --output "$TMPDIR/cairn-policy.json"
                cmp "$TMPDIR/cairn-policy.json" "$src/cairn-policy/generated/cairn-policy.json"
                cairn validate --root "$src"
                cairn traceability coverage --root "$src" --json > "$TMPDIR/traceability.json"
                touch "$out"
              '';

          # r[verify artifact_auth.core.authority_free]
          authority-audit =
            pkgs.runCommand "artifact-auth-authority-audit"
              {
                nativeBuildInputs = [ pkgs.gnugrep ];
                src = self;
              }
              ''
                set -eu
                if grep -R -E 'std::fs|std::env|std::process|std::time|std::net|tokio::|async |println!|eprintln!|pub fn sign|pub struct SigningKey|pub struct SecretKey|rand::' "$src/crates" --include='*.rs'; then
                  echo "forbidden authority or private-key dependency found" >&2
                  exit 1
                fi
                touch "$out"
              '';
        }
      );

      devShells = eachSystem (
        system:
        let
          pkgs = import nixpkgs {
            inherit system;
            overlays = [ (import rust-overlay) ];
          };
          toolchain = pkgs.rust-bin.fromRustupToolchainFile ./rust-toolchain.toml;
        in
        {
          default = pkgs.mkShell {
            packages = [
              toolchain
              pkgs.nickel
              pkgs.nixfmt
            ];
          };
        }
      );
    };
}
