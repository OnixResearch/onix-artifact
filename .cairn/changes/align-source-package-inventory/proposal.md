<!-- SPDX-License-Identifier: AGPL-3.0-or-later -->
# Align the complete source-package inventory

## Why

The immutable source cohort contains four Cargo workspace packages but its historical Nickel repository catalog and exported release profile listed only three. Valence's full-source admission correctly rejects that mismatch. A consumer must not hide a declared package or weaken admission to use the authentication crates.

## What Changes

- Include the already-declared `artifact-binding-core` package and its empty cross-package dependency set in the closed Nickel inventory.
- Regenerate `config/repository.json` and `release/profile.json` from their Nickel sources.
- Make the existing Nickel gate reject disagreement between Cargo workspace package names, repository metadata and release metadata.
- Keep the forbidden cross-mechanism dependency fixture complete and add a missing-package negative fixture.
- Select the immutable authorized-SSH Cairn tool revision that reads native `.cairn/` content; preserve lifecycle paths and the checked-in gate policy.

## Non-goals

No Rust API, package dependency, authority, authentication behavior, cryptographic profile or trust-root changes. The separate owner AGPL change governs the prospective package grant without rewriting historical licenses. This does not complete the separate anonymous-acquisition work or prove consumer migration.

## Impact

Current consumer: Valence's exact full-source Artifact admission, followed by Mantle's unified authentication cohort. Maintenance owner: Artifact's existing Nickel and Nix checks. Consumers pin the final immutable revision and independently rerun their own admission and behavior checks; historical source revisions remain valid rollback identities, not evidence of inventory coherence.
