## Context

The workspace is public on GitHub and on Radicle. `flake.nix` previously pinned Cairn with `git+ssh://git@github.com/OnixResearch/cairn.git`, and the locked Cairn revision declared its own inputs as GitHub SSH locators plus a `git.onix.computer` gateway. Anonymous `nix flake check` and `nix develop` therefore depended on a maintainer GitHub key and an internal service. The published GitHub repository, Mantle, bounded-exec and the recorded Cairn revision are publicly fetchable over HTTPS at the same object identities.

## Decisions

### Decision: Override acquisition locators without changing source identity

**Choice:** Keep Cairn at revision `1cacafebbff7b2716a953961a1ebf52bafb352e7` and declare anonymous HTTPS overrides for Cairn's `artifact`, `mantle-build-contract` and `bounded-exec` inputs at their existing revisions. Relock with Nix and confirm every `narHash` is unchanged.

**Rationale:** Source identity and acquisition transport are separate concerns. Replacing SSH or internal-gateway locators with public HTTPS at the same revision preserves the exact content and dependency graph while removing the credential and service prerequisites. Updating the Cairn revision itself would change the lifecycle tool and is outside this release-preparation change.

### Decision: Correct public documentation instead of deleting history

**Choice:** Rewrite the README distribution, validation, compatibility-source and reference statements so they describe the reachable public source, and keep historical receipts, evidence and prior grants untouched. Add `SECURITY.md` using the house private-reporting policy.

**Rationale:** A reader arriving from GitHub needs an accurate acquisition path and a private reporting channel. Immutable receipts remain the record of what was observed at publication time; prose that repeats an obsolete projection as a current instruction is corrected rather than erased. The `git.onix.computer` projection recorded in `evidence/radicle/publication-v1.ncl` is hash-bound and stays as a historical receipt with an explicit availability limit.

## Risks / Trade-offs

- The public GitHub repositories are external services; a future rename or removal would break the locators. The lock still pins every revision and narHash, so a mismatch fails closed.
- Overriding a tool's own inputs couples this repository's lock to those public repositories. The revisions are unchanged, and the Cairn tool remains the reviewed `1cacafe` revision.
- Documentation accuracy and anonymous acquisition checks do not prove cryptographic correctness, consumer behavior or release eligibility.
