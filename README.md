# Artifact

Product-neutral `no_std + alloc` cores for artifact authentication, transfer geometry, and versioned binding/reachability mechanics.

The workspace shares a Rust toolchain, license, lint policy, dependency resolution, lifecycle, and release checks. Workspace membership does not make its mechanisms semantically interchangeable and does not transfer consumer authority into these crates.

## Start here

1. Run `nix develop -c cargo test --workspace`.
2. Choose the narrow package matching the mechanism you need.
3. Read that package's claim boundary before writing an adapter.
4. Pin an immutable Git revision; never depend on a sibling path from a product repository.

## Packages

| Package | Status | Owns | Does not own |
|---|---|---|---|
| `artifact-auth-core` | Implemented | Canonical signed statements, typed references, explicit currentness/threshold observations, bounded authentication decisions | Trust discovery, signing, authorization, storage, lifecycle, release |
| `artifact-auth-ed25519` | Implemented | Pure Ed25519 verification over exact core-produced canonical bytes | Private keys, signing, trust, revocation collection, authorization |
| `artifact-transfer-core` | Implemented | Fixed, FastCDC-bound, and external ordered-part geometry; checked coverage/offsets; explicit BLAKE3/SHA-256 tags | Wire manifests, chunking/hashing bytes, transport, storage, integrity claims |
| `artifact-binding-core` | Implemented | Checked successor binding, one-snapshot resolution, deterministic reachability, stable pin paths, conservative retirement | Artifact identity, compatibility truth, persistence, atomic swaps, deployment, GC, deletion authority |

## Workspace invariants

<!-- r[impl artifact_workspace.substrate.uniform] r[impl artifact_workspace.dependencies.narrow] -->

- Every reusable core remains `#![no_std]` plus `alloc` and receives already-loaded values.
- `artifact-auth-ed25519` may depend on `artifact-auth-core`; the other cores remain independent unless a later reviewed Cairn change proves a narrower dependency.
- No umbrella crate re-exports the packages and no universal `ArtifactRef` erases algorithm, schema, or consumer semantics.
- Consumers retain canonical product formats, compatibility policy, authority, persistence, transport, evidence, deployment, retention, and release decisions.
- Positive and negative tests travel together, including malformed input, bounds, overflow, stale observations, and authority-widening cases.

## Authentication boundary

A passing authentication decision proves only that supplied public-key material verified exact canonical statements and that supplied purpose, generation, currentness, trust, and threshold observations satisfied the selected bounded policy.

It does not prove artifact truth, producer authorization, trust-root correctness, revocation freshness, provenance, build correctness, deployment safety, or release eligibility. See [`docs/security.md`](docs/security.md), [`docs/baseline-vectors.md`](docs/baseline-vectors.md), and [`docs/consumer-mappings.md`](docs/consumer-mappings.md).

## Transfer boundary

<!-- r[impl artifact_transfer.claims.bounded] -->

A passing geometry decision proves only that supplied ordered lengths cover a declared byte count under an explicit mechanism, bounds, and empty-artifact policy. It does not prove chunk bytes, hashes, external ordering, reconstruction, transfer completion, or integrity.

The extraction decision and disposable pilots remain available under [`docs/transfer/`](docs/transfer/).

## Binding boundary

<!-- r[impl artifact_binding.core.boundary] -->

The binding core classifies only caller-supplied binding, graph, root, attribution, and completeness facts. Incomplete root inventories cannot produce a definitive retired result. Retirement evidence never grants cleanup or deletion authority.

See the [design](docs/binding/design.md), [adoption guide](docs/binding/adoption.md), and [disposable pilots](docs/binding/pilot.md).

## Publication incubation

The durable one-file publication candidate remains a disposable fixture. It is not a workspace package and does not change Mantle or OnixOS dependencies.

See the [candidate API](docs/publication/API.md), [source inventory](docs/publication/SOURCE-INVENTORY.md), [pilot mappings](docs/publication/PILOTS.md), and [extraction decision](docs/publication/DECISION.md).

## Distribution and compatibility

<!-- r[impl artifact_workspace.provenance.imports] r[impl artifact_workspace.migration.receiver_local] -->

Packages are distributed from immutable Git revisions and set `publish = false`; crates.io is not a release channel. Product repositories must align Cargo and Nix to the same reviewed source identity.

The standalone `artifact-auth`, `artifact-transfer`, and `artifact-binding` repositories are deprecated. Keep their immutable revisions only for source history and rollback. All active development and new consumer pins must use this workspace.

Historical `artifact-auth` revision `799459346d5416fbd7b9f55840a7371441b55afa` remains a valid compatibility source for existing Molten, Mantle, and Valence pins. Moving a consumer to this workspace requires a repo-local Cairn change, exact source/package/license checks, generated Cargo/Nix locks, focused positive and negative tests, and rollback evidence.

The unified workspace's existing canonical identity is
`rad:z25ySMy8Hh3HpsxP5zcYoYgaMBi99`. It is now public natively, with its existing
single delegate, threshold one, default branch and native `main` preserved.
Reviewed consumer revisions `e41340bec587b6d049b5cc518ec7db925dde84be` and
`c932138d880ddf4c2967f4c024b489b5c0022bf1` are signed on dedicated
`consumer-pins/<full-revision>` refs. The exact command observations are in
[`native-publication-and-acquisition.json`](.cairn/changes/publish-required-artifact-source/evidence/native-publication-and-acquisition.json).
Native publication does not establish a working anonymous HTTPS Git input:
post-publication exact fetches returned HTTP 500 from the Garden projection and
repository-not-found from the Onix projection. Neither attempted endpoint is
admitted for downstream cutover; exact anonymous acquisition remains open.

## Validation

Fast feedback:

```console
nix develop -c cargo fmt --all -- --check
nix develop -c cargo test --workspace
nix develop -c cargo clippy --workspace --all-targets -- -D warnings
```

Core boundaries:

```console
nix develop -c cargo check -p artifact-auth-core --no-default-features --target wasm32-unknown-unknown
nix develop -c cargo check -p artifact-auth-ed25519 --no-default-features --target wasm32-unknown-unknown
nix develop -c cargo check -p artifact-transfer-core --no-default-features --target wasm32-unknown-unknown
nix develop -c cargo check -p artifact-binding-core --no-default-features --target wasm32-unknown-unknown
nix develop -c cargo check -p artifact-binding-core --no-default-features --target thumbv7em-none-eabi
nix develop -c cargo test --manifest-path fixtures/publication-candidate/Cargo.toml
```

Full repository gate:

```console
nickel typecheck config/repository.ncl
nickel typecheck release/profile.ncl
nix run --inputs-from . cairn#cairn -- validate --root . --policy cairn-policy/generated/cairn-policy.json
nix flake check path:$PWD -L
```

Native lifecycle content is `.cairn/`; the immutable tool input is Cairn
`1cacafebbff7b2716a953961a1ebf52bafb352e7`, acquired through authorized Git SSH.
The pinned tool selects `.cairn/` without relocating lifecycle content or changing
the checked-in gate policy. SSH acquisition requires an authorized GitHub key;
it does not establish anonymous source availability. The exact 156-file prepared
cohort passed the x86_64-linux owner flake checks, native validation and gates,
and an isolated incomplete-release-inventory rejection. Commands, original
output and source identities are retained in
[`owner-acceptance-v1`](.cairn/archive/1970-01-01-align-source-package-inventory/evidence/owner-acceptance-v1/complete.json).
The flake check explicitly omitted aarch64-linux. Separate Cargo metadata and
source-member observations are in
[`package-metadata-v1`](.cairn/archive/1970-01-01-align-source-package-inventory/evidence/package-metadata-v1/complete.json):
all four packages resolve to AGPL-3.0-or-later, disable crates.io publication,
and include LICENSE and LICENSE-AGPL. These observations do not establish
consumer migration, anonymous acquisition or release eligibility. Native sync
accepted the complete source-package inventory, and native archive moved the
change to the tool-selected `1970-01-01-align-source-package-inventory` path.
Terminal command receipts and post-archive validation are retained in
[`native-terminal-v1`](.cairn/archive/1970-01-01-align-source-package-inventory/evidence/native-terminal-v1/complete.json).
The archive path is the native tool output, not a claim about execution date.

### Frozen Radicle compatibility source

Historical revision `799459346d5416fbd7b9f55840a7371441b55afa` is served unchanged at `https://git.onix.computer/z4JGYYW7WsesXUq7MXVdx16Fawu2f.git`. Its typed publication receipt is [`evidence/radicle/publication-v1.ncl`](evidence/radicle/publication-v1.ncl). This compatibility publication does not replace the unified `artifact` workspace or claim current-package equivalence.

## License

<!-- r[verify artifact_workspace.substrate.uniform] r[verify artifact_workspace.claims.bounded] -->

All repository-owned packages and new owned source, contracts, schemas, fixtures, templates, documentation and policy are offered under `AGPL-3.0-or-later`; see [`LICENSE`](LICENSE) and [`LICENSE-AGPL`](LICENSE-AGPL).

The authorization and exact imported source revisions are recorded in [`provenance/SOURCE_GRANT.md`](provenance/SOURCE_GRANT.md) and [`docs/source-inventory.md`](docs/source-inventory.md). Prior MIT/Apache grants remain effective for previously granted material, including byte-identical content. Retained permissive texts do not grant permissive terms for new contributions. Immutable baselines, historical receipts and third-party dependencies retain their recorded terms. This source preparation does not publish a revision or migrate consumer pins.

## References

- [Deprecated artifact-auth history](https://github.com/OnixResearch/artifact-auth) — immutable authentication source and compatibility revisions.
- [Deprecated artifact-transfer history](https://github.com/OnixResearch/artifact-transfer) — immutable transfer-geometry source and disposable consumer evidence imported at revision `507b10823c4513064710a70fe565f9a1ee592985`.
- [`../artifact-binding/`](../artifact-binding/) — deprecated local design history with no publication source.
- [PsychoLlama/ambient](https://github.com/PsychoLlama/ambient) — non-normative design reference for immutable implementations, explicit late binding, semantic handler identity, and generation retirement tracing.
- [Molten](https://github.com/brittonr/aspen), [Mantle](https://github.com/OnixResearch/mantle), [Valence](https://github.com/OnixResearch/valence), and [OnixOS](https://github.com/onixcomputer/onix-modules) — consumers and pilots that retain product authority.
