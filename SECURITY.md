# Security policy

## Supported revisions

Security fixes are made against the current default branch. Reviewed release
tags may receive fixes when their release notes explicitly say so; no other
long-term-support promise is implied.

## Report a vulnerability

Use GitHub private vulnerability reporting for this repository:

<https://github.com/OnixResearch/onix-artifact/security/advisories/new>

Do not include vulnerability details in a public issue, discussion, commit, or
pull request. Include the affected revision and package, the reachable surface,
reproduction steps, expected impact, and any known mitigations in the private
report. Do not include unrelated credentials, personal data, or production
evidence.

Repository administrators must keep private vulnerability reporting enabled
before treating the repository as publicly supported. If the private reporting
interface is unavailable, a public issue may report only that the private
channel is unavailable; it must not contain vulnerability details.

## Scope

A report may concern the Rust cores, their canonical statement and digest
encodings, Ed25519 verification, chunk-geometry bounds, binding/reachability
classification, package boundaries, or the build and release tooling checked
into this repository.

A passing authentication, geometry, binding, or repository check is not a
security proof. Each result remains limited to the supplied values, the selected
policy, and the non-claims documented in `README.md` and `docs/security.md`. The
cores do not own signing, key storage, trust discovery, persistence, transport,
deployment, retention, or release authority.
