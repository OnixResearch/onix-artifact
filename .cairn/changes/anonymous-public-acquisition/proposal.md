## Why

The repository is prepared for public release from GitHub. The Cairn flake input was acquired over GitHub SSH, and the locked Cairn tool carried SSH and internal-gateway locators for its own source inputs, so a clean clone depended on maintainer credentials or services that an anonymous reader does not have. The README also asserted a compatibility projection that no longer resolves and linked sources that are not anonymously reachable. The repository had no security policy.

## What Changes

- Pin the Cairn flake input and Cairn's own source inputs to anonymous public HTTPS locators at the same revisions, preserving revision and narHash identity.
- Correct README distribution, compatibility-source, validation and reference statements; add status, requirements, quick start, security and non-claim sections.
- Add `SECURITY.md` pointing at GitHub private vulnerability reporting and describing the bounded scope.
- Add missing package descriptions and ignore local scratch directories.
- Do not change mechanism code, license terms, grants, immutable evidence or published source identities.

## Impact

- **Files:** CI-facing flake inputs and lock, README, SECURITY, crate manifests, ignore rules, and two documentation statements plus one negative-test literal.
- **Consumers:** No change. All recorded revisions and package identities remain identical.
- **Owner:** Artifact maintainers own the public locators and release documentation. Consumer repositories retain their own pins and migration decisions.
- **Testing:** Formatting, workspace tests, Clippy, no-std host/Wasm/thumb checks, Nickel typechecks and generated projections, Cairn validation and gates, the flake check, and anonymous acquisition checks with SSH, credentials, prompts and personal configuration disabled. These checks do not establish cryptographic, consumer or release correctness.
