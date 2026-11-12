## ADDED Requirements

### Requirement: Public source acquisition is credential-free

r[artifact_workspace.distribution.anonymous_sources] Every flake input and Cargo Git dependency MUST resolve from an anonymous HTTPS locator to a public repository at the same pinned revision. A clean clone MUST build the Rust workspace and run its Nickel checks without GitHub SSH credentials, personal agent or host configuration, or project-internal gateways. Public release documentation and the security policy MUST describe the repository as it is reachable from GitHub.

#### Scenario: Clean clone resolves over HTTPS

r[artifact_workspace.distribution.anonymous_sources.scenario.https]
- GIVEN a fresh clone of the published revision and an environment with SSH, credentials and interactive prompts disabled
- WHEN the workspace build, Nickel checks and `cargo fetch --locked` run
- THEN every flake input and Cargo Git dependency resolves from a public HTTPS locator at its recorded revision.

#### Scenario: Credential or internal locator is rejected

r[artifact_workspace.distribution.anonymous_sources.scenario.boundary]
- GIVEN a flake input or Cargo dependency requires GitHub SSH, a private gateway, or an unpinned revision
- WHEN public source admission is evaluated
- THEN that locator MUST NOT count as a valid public build source
- AND no alternative source identity MAY replace the recorded revision.
