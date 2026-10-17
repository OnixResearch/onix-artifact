<!-- SPDX-License-Identifier: AGPL-3.0-or-later -->
## Phase 1: Complete the declared inventory

- [x] [serial] Align the closed Nickel package/dependency inventories with all existing Cargo members and regenerate both JSON projections. r[artifact_workspace.source_inventory.complete]
- [x] [serial] Reject source/repository/release package disagreement in the existing gate; retain meaningful missing-member and forbidden-dependency negative fixtures. r[artifact_workspace.source_inventory.complete]
- [x] [serial] Generate the immutable compatible Cairn SSH lock without moving `.cairn/` or changing the gate policy. r[artifact_workspace.source_inventory.complete]

## Phase 2: Verify and publish the exact cohort

- [x] [serial] Run the required owner checks and an isolated positive/negative source-inventory gate smoke; retain exact commands, source identities and bounded non-claims. r[artifact_workspace.source_inventory.complete]
- [ ] [serial] Commit the verified implementation and prepare complete native gate/sync evidence for the separately executed terminal archive/publication operation. r[artifact_workspace.source_inventory.complete]
