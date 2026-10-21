<!-- SPDX-License-Identifier: AGPL-3.0-or-later -->
# Complete source inventory design

## Context

`Cargo.toml` already declares authentication core, Ed25519 verification, transfer and binding packages. The source catalog is reviewable Nickel policy; both JSON files are generated artifacts. The historical catalog omitted binding despite its presence in the immutable source tree.

## Decision

Keep the existing closed package/dependency contract. Admit the existing binding package as independent, without changing the sole allowed authentication-to-core edge. Compare sorted package names loaded from every declared Cargo member manifest with both generated inventory lists in the existing `nickel-contracts` gate. Export freshness and the existing positive and negative Nickel fixtures remain required.

This applies the established complete-workspace admission rule; no alternative source registry, consumer-only allowlist, compatibility shim or runtime behavior is introduced. The prospective AGPL-3.0-or-later grant is governed by `adopt-owned-source-agpl`; prior grants, immutable imports and third-party terms remain unchanged.

### Decision: Select the native lifecycle tool without changing policy

The old Cairn `cf5c4a5c10361ca20a13addf14954407d6857028` scans `cairn/`, while Artifact stores native lifecycle content in `.cairn/`. Select immutable Cairn `1cacafebbff7b2716a953961a1ebf52bafb352e7` through authorized Git SSH and regenerate the lock with Nix. Its native layout maps specs, changes and archive to `.cairn/`. Do not move lifecycle directories, use a sibling tool checkout, weaken coverage, or change the gate policy. Authorized acquisition is not anonymous acquisition.

## Verification

Regenerate through Nickel, run the real Nix gate and existing workspace/core checks, and exercise the gate on an isolated missing-member release profile. The positive source must admit all four packages; incomplete inventory and forbidden cross-mechanism dependencies must fail. Retain exact inputs, commands and outcomes. Native Cairn gates, sync/archive, and post-archive validation are separate observations from build or release authority.

The default traceability profile intentionally reads accepted requirements only
from `.cairn/specs`; active change deltas do not become accepted by passing
structural validation. Until separately authorized native sync, the inventory
gate links to the existing accepted uniform-substrate and narrow-dependency
requirements. The new source-inventory requirement remains in this active delta,
not an invented accepted declaration or an out-of-profile source reference.

Default evidence roots omit the Rust crate trees. Declare verification links at
the actual Nix runners: `cargo-test` runs authentication canonicalization,
Ed25519 signature rejection, explicit policy/non-claim, geometry and digest tests;
`binding-core` runs compatibility and retirement-attribution tests alongside its
existing binding checks. These links name existing verification mechanisms, not
passing observations. Print the coverage JSON directly so failed checks retain
their missing/dangling IDs in the owner log. Gate policy and evidence roots remain
unchanged, and no acceptance checkbox is completed by these declarations.

## Boundaries

Metadata agreement proves source-package inventory consistency only. It does not prove semantic correctness, trust, authorization, successful downstream adoption, anonymous acquisition or release eligibility. Preserve historical publication receipts and the existing Radicle identity; no source publication is performed by this preparation.
