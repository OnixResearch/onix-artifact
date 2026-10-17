<!-- SPDX-License-Identifier: AGPL-3.0-or-later -->
# Complete source-package inventory

## ADDED Requirements

### Requirement: Source-package inventory is complete

r[artifact_workspace.source_inventory.complete] Artifact MUST declare every Cargo workspace package exactly once in its repository and release package inventories. The release dependency inventory MUST retain the closed admitted cross-package edges. Generated metadata MUST be exported from Nickel, and the owner gate MUST reject disagreement with the package names in the declared member manifests. The immutable Cairn tool input MUST read native `.cairn/` content without moving lifecycle directories or weakening gate policy. This establishes inventory consistency only and MUST NOT grant consumer migration, authority, semantic correctness or release eligibility.

#### Scenario: Complete immutable source cohort

- GIVEN the four declared authentication, verifier, transfer and binding packages
- WHEN repository/release projections and owner source admission are checked
- THEN all four package names agree and the declared independent binding package is retained

#### Scenario: A source package is hidden

- GIVEN a declared Cargo member is omitted from a repository or release inventory
- WHEN the owner gate evaluates the source cohort
- THEN admission fails rather than narrowing the source set to the consumer's selected crates

#### Scenario: A cross-mechanism dependency is introduced

- GIVEN a complete package inventory but an authentication dependency is added to transfer or binding
- WHEN the closed dependency contract is evaluated
- THEN the negative fixture is rejected without relying on an unrelated missing-package failure

#### Scenario: Native lifecycle content is selected

- GIVEN the checked-in `.cairn/` lifecycle and unchanged gate policy
- WHEN the immutable pinned Cairn tool runs native checks
- THEN it reads `.cairn/specs`, `.cairn/changes` and `.cairn/archive`, not an empty legacy `cairn/` tree
