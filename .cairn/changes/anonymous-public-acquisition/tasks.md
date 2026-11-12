## Implementation

- [x] [serial] Replace the Cairn SSH input and Cairn's SSH/internal-gateway source inputs with anonymous public HTTPS locators at the same revisions, relock, and confirm unchanged revisions and narHashes. r[artifact_workspace.distribution.anonymous_sources]
- [x] [serial] Correct README, release and adoption statements, add `SECURITY.md`, and add missing package descriptions and ignore rules. r[artifact_workspace.distribution.anonymous_sources]
- [x] [serial] Replace the unreachable repository literal in the publication negative test with a clearly reserved example host. r[artifact_workspace.distribution.anonymous_sources]

## Verification

- [ ] [serial] Run the repository formatting, test, Clippy, no-std, Nickel, Cairn and flake checks once after the edits. r[artifact_workspace.distribution.anonymous_sources]
- [ ] [serial] Prove anonymous acquisition from a fresh clone with SSH, credentials, prompts and personal configuration disabled, for `cargo fetch --locked` and every locked flake input URL. r[artifact_workspace.distribution.anonymous_sources]
