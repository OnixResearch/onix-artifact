# artifact-auth

Run `cargo test --workspace` first. It checks the product-neutral boundary for canonical artifact statements, Ed25519 verification, key-currentness observations, distinct-key thresholds, and bounded authentication decisions.

## Start here

1. Run the workspace tests. Budget **1–3 minutes** with a warm build cache.
2. Choose [`artifact-auth-core`](#artifact-auth-core) for statement and policy logic, or [`artifact-auth-ed25519`](#artifact-auth-ed25519) for signature verification.
3. Read the [claim boundary](#claim-boundary) before using a passing decision as evidence.
4. Compare compatibility-sensitive work against the frozen [baseline vectors](docs/baseline-vectors.md).

**Success:** the relevant validation commands exit with status `0`, and the consumer keeps authority decisions outside this repository.

## What this repository owns

| Area | Repository-owned behavior |
|---|---|
| Statements | Versioned typed statements and injective, length-delimited canonical preimages |
| Identity | Full BLAKE3 public-key identities and explicitly labeled interoperability references |
| Verification | Pure Ed25519 verification over exact canonical statement bytes |
| Policy inputs | Explicit key-purpose, generation, currentness, and distinct-key threshold observations |
| Authority | None; consumers retain trust, authorization, signing, lifecycle, and release decisions |

### `artifact-auth-core`

`artifact-auth-core` is `#![no_std]` plus `alloc`. Its functional core:

- validates typed references and statements;
- constructs canonical statement preimages;
- computes BLAKE3 identities; and
- evaluates explicitly supplied trusted-key and currentness observations.

It performs no I/O and owns no authority.

### `artifact-auth-ed25519`

`artifact-auth-ed25519` is a pure verifier. It accepts core-produced canonical statement bytes plus explicitly supplied public-key and signature bytes.

It does not expose signing or private-key APIs.

## Consumer responsibilities

Consumers retain:

- measurement and payload canonicalization;
- signing and private material;
- trust-root selection and currentness collection;
- authorization, lifecycle, build, and release decisions; and
- transport, registry, and runtime behavior.

## Statement contract

A signer-specific `artifact-auth.statement.v1` binds:

- domain, purpose, and compatibility profile;
- producer and key labels plus the full BLAKE3 public-key identity;
- one typed subject reference;
- sorted, unique typed parent references; and
- one typed verifier-context reference.

The canonical preimage is a versioned, length-delimited byte encoding. JSON, Preserves, OCI, Radicle, and product receipt formats are compatibility projections—not alternate canonical encodings.

Stack-owned references use BLAKE3. Protocol-required SHA-256 references remain explicitly labeled interoperability values.

## Claim boundary

<!-- r[verify artifact_auth.claims.bounded] r[verify artifact_auth.conformance.consumers] -->

A passing decision proves only both of these facts:

1. Supplied public-key material verified each exact canonical statement.
2. Supplied key-purpose, generation, currentness, and threshold observations satisfied the selected bounded policy.

A passing decision does **not** prove artifact truth, verifier correctness, producer authorization, trust-root correctness, revocation freshness, provenance correctness, lifecycle conformance, build correctness, semantic equivalence, deployment safety, or release eligibility.

## Validation

Run the smallest group that covers your change.

### Fast feedback — budget 1–3 minutes with a warm cache

```console
cargo fmt --check
cargo test --workspace
```

### `no_std` boundary — budget 1–3 minutes after dependencies are built

```console
cargo check -p artifact-auth-core --no-default-features --target wasm32-unknown-unknown
cargo check -p artifact-auth-ed25519 --no-default-features --target wasm32-unknown-unknown
```

### Full repository gate — budget 5–30 minutes depending on the Nix cache

```console
cargo clippy --workspace --all-targets -- -D warnings
nickel typecheck config/repository.ncl
nickel typecheck release/profile.ncl
nix flake check -L
```

**Done means:** every command in the selected group exits with status `0`.

## Distribution

Distribution uses immutable Git revisions and Nix inputs. Both packages set `publish = false`; crates.io is not a release channel.

## Design lineage

The implementation combines:

- Cairn's typed-observation boundary;
- Mantle's canonical normalization and distinct-full-key threshold behavior; and
- Molten's purpose, generation, and currentness model.

Valence remains the owner of Evidence IR and Radicle authorization semantics. Exact legacy bytes and identities are frozen in [`docs/baseline-vectors.md`](docs/baseline-vectors.md).

## License

The repository and both packages are available under `MIT OR Apache-2.0`.

Mantle-derived design and implementation material is included under the owner authorization recorded in [`provenance/SOURCE_GRANT.md`](provenance/SOURCE_GRANT.md). Exact source identities are listed in [`docs/source-inventory.md`](docs/source-inventory.md).

## References

These fixed revisions informed the extraction. They remain consumer references and do not transfer product authority into this repository.

- [Cairn authenticated inputs at `cc4639be24475d80844b091cdec605eb2fef9ff0`](https://github.com/OnixResearch/cairn/blob/cc4639be24475d80844b091cdec605eb2fef9ff0/crates/cairn-core/src/verified/authenticated_inputs.rs)
- Mantle at `26c6880c08cd730c9e9420f92ea91a87212e492d`: [OCI trust](https://github.com/OnixResearch/mantle/blob/26c6880c08cd730c9e9420f92ea91a87212e492d/src/oci_registry.rs) and [action-result core](https://github.com/OnixResearch/mantle/blob/26c6880c08cd730c9e9420f92ea91a87212e492d/crates/crunch-action-result-core/src/lib.rs)
- [Molten cryptographic identity at `70590459a218dc8e66948ab6f305a7c54142b710`](https://github.com/brittonr/aspen/blob/70590459a218dc8e66948ab6f305a7c54142b710/crates/molten-core/src/fabric_crypto_identity/model.rs)
- [Valence Radicle evidence at `8eccac35fcd8aae8ef64b3d1021e7f1a53656180`](https://github.com/OnixResearch/valence/blob/8eccac35fcd8aae8ef64b3d1021e7f1a53656180/crates/valence-core/src/cob_evidence.rs)
- [nickel-export](https://github.com/OnixResearch/nickel-export) and [host-control](https://github.com/OnixResearch/host-control) — independent-repository and authority-boundary references.
