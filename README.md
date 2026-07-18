# artifact-auth

`artifact-auth` is the independent, product-neutral boundary for versioned artifact statements, canonical preimages, full public-key identities, pure Ed25519 verification, explicit key-currentness observations, distinct-key thresholds, and bounded authentication decisions.

## Architecture

- `artifact-auth-core` is `#![no_std]` plus `alloc`. It validates typed references and statements, constructs an injective length-delimited preimage, computes BLAKE3 identities, and evaluates explicit trusted-key/currentness observations. It performs no I/O and owns no authority.
- `artifact-auth-ed25519` is a pure verifier over core-produced canonical statement bytes and explicitly supplied public-key/signature bytes. It does not expose signing or private-key APIs.
- Consumers retain measurement, payload canonicalization, signing, private material, trust-root selection, currentness collection, authorization, lifecycle, build, transport, registry, runtime, and release decisions.

The implementation synthesizes Cairn's typed-observation boundary, Mantle's canonical normalization and distinct-full-key threshold behavior, and Molten's purpose/generation/currentness model. Valence remains the owner of Evidence IR and Radicle authorization semantics.

## Statement contract

A signer-specific `artifact-auth.statement.v1` binds:

- domain, purpose, and compatibility profile;
- producer and key labels;
- the full BLAKE3 public-key identity;
- one typed subject reference;
- sorted unique typed parent references; and
- one typed verifier-context reference.

The canonical preimage is a versioned, length-delimited byte encoding. JSON, Preserves, OCI, Radicle, and product receipt formats are compatibility projections, not alternate canonical encodings.

Stack-owned references use BLAKE3. Protocol-required SHA-256 references remain explicitly labeled interoperability values.

## Claim boundary

<!-- r[verify artifact_auth.claims.bounded] r[verify artifact_auth.conformance.consumers] -->

A passing decision proves only that supplied public-key material verified each exact canonical statement and that supplied key-purpose, generation, currentness, and threshold observations satisfied the selected bounded policy.

It does not prove artifact truth, verifier correctness, producer authorization, trust-root correctness, revocation freshness, provenance correctness, lifecycle conformance, build correctness, semantic equivalence, deployment safety, or release eligibility.

## Validation

```console
cargo fmt --check
cargo test --workspace
cargo check -p artifact-auth-core --no-default-features --target wasm32-unknown-unknown
cargo check -p artifact-auth-ed25519 --no-default-features --target wasm32-unknown-unknown
cargo clippy --workspace --all-targets -- -D warnings
nickel typecheck config/repository.ncl
nickel typecheck release/profile.ncl
nix flake check -L
```

Distribution is through immutable Git revisions and Nix inputs. Both packages set `publish = false`; crates.io is not a release channel.

## License

The repository and both packages are available under `MIT OR Apache-2.0`. Mantle-derived design and implementation material is included under the owner authorization recorded in [`provenance/SOURCE_GRANT.md`](provenance/SOURCE_GRANT.md), with exact source identities in [`docs/source-inventory.md`](docs/source-inventory.md).

## References

These fixed revisions informed the extraction. They remain consumer references and do not transfer product authority into this repository.

- [Cairn authenticated inputs at `cc4639be24475d80844b091cdec605eb2fef9ff0`](https://github.com/OnixResearch/cairn/blob/cc4639be24475d80844b091cdec605eb2fef9ff0/crates/cairn-core/src/verified/authenticated_inputs.rs)
- [Mantle OCI trust at `26c6880c08cd730c9e9420f92ea91a87212e492d`](https://github.com/OnixResearch/mantle/blob/26c6880c08cd730c9e9420f92ea91a87212e492d/src/oci_registry.rs)
- [Mantle action-result core at `26c6880c08cd730c9e9420f92ea91a87212e492d`](https://github.com/OnixResearch/mantle/blob/26c6880c08cd730c9e9420f92ea91a87212e492d/crates/crunch-action-result-core/src/lib.rs)
- [Molten cryptographic identity at `70590459a218dc8e66948ab6f305a7c54142b710`](https://github.com/brittonr/aspen/blob/70590459a218dc8e66948ab6f305a7c54142b710/crates/molten-core/src/fabric_crypto_identity/model.rs)
- [Valence Radicle evidence at `8eccac35fcd8aae8ef64b3d1021e7f1a53656180`](https://github.com/OnixResearch/valence/blob/8eccac35fcd8aae8ef64b3d1021e7f1a53656180/crates/valence-core/src/cob_evidence.rs)
- [nickel-export](https://github.com/OnixResearch/nickel-export) and [host-control](https://github.com/OnixResearch/host-control) — independent-repository and authority-boundary references.
