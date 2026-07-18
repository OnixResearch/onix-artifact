# Agent Notes

`artifact-auth-core` and `artifact-auth-ed25519` are authority-free `#![no_std]` plus `alloc` functional cores. They must not read files, inspect environment state, spawn processes, print, consult clocks, generate or store keys, use network I/O, discover trust, or depend on product repositories.

Consumers own measurement, payload canonicalization, signing, private material, currentness collection, authorization, lifecycle, build, transport, registry, runtime, and release policy.

Use BLAKE3 for repository-owned identities. Preserve algorithm labels for interoperability references. Add positive and negative tests together.

Primary checks:

```console
cargo test --workspace
cargo check -p artifact-auth-core --no-default-features --target wasm32-unknown-unknown
cargo check -p artifact-auth-ed25519 --no-default-features --target wasm32-unknown-unknown
cargo clippy --workspace --all-targets -- -D warnings
nix flake check -L
```
