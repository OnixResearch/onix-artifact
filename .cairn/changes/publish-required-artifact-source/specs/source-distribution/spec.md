## ADDED Requirements

### Requirement: Existing unified identity and governance are preserved

r[artifact_workspace.distribution.existing_identity] Required anonymous-source publication MUST operate only on the existing unified Artifact identity `rad:z25ySMy8Hh3HpsxP5zcYoYgaMBi99` under an explicit operator request, after native proposal/design/tasks admission, without creating an identity or changing its delegate set, threshold, default-branch meaning, source objects or licenses.

#### Scenario: Required existing identity is published

r[artifact_workspace.distribution.existing_identity.scenario.publish]
- GIVEN the operator explicitly authorized publication of this required dependency, the existing identity has one delegate and threshold one, and the current operator is that delegate
- WHEN the admitted publication operation runs
- THEN native readback MUST show public visibility for the same RID with unchanged delegates and threshold.

#### Scenario: Unrelated identity or governance mutation is rejected

r[artifact_workspace.distribution.existing_identity.scenario.boundary]
- GIVEN an operation would create a RID, use the frozen compatibility identity, alter delegates or threshold, or publish an unrelated repository
- WHEN publication authority is evaluated
- THEN that operation MUST remain outside this change and MUST NOT satisfy required-source admission.

### Requirement: Native publication surface is reviewed before mutation

r[artifact_workspace.distribution.exposure] Before changing visibility, maintainers MUST review intended native refs and reachable history with a redacting secret scanner and bounded manual license and exposure review, retain the exact review scope, and stop on a confirmed unresolved operational-secret, privacy or redistribution restriction.

#### Scenario: Bounded review records limitations

r[artifact_workspace.distribution.exposure.scenario.review]
- GIVEN native publication may expose more than the selected runtime package trees
- WHEN source review completes
- THEN its evidence MUST distinguish exact source objects, current checkout files, advertised refs, reachable history and unreviewed surfaces
- AND deterministic example keys MUST NOT be misrepresented as operational credentials or scanner results as security certification.

### Requirement: Both exact source revisions are anonymously acquired

r[artifact_workspace.distribution.anonymous_exact] Source admission MUST prove actual fresh credential-free HTTP Git acquisition and exact commit readback for both `e41340bec587b6d049b5cc518ec7db925dde84be` and `c932138d880ddf4c2967f4c024b489b5c0022bf1` from observed projections of the unified workspace, with user/system configuration, credentials, prompts and SSH disabled.

#### Scenario: Exact anonymous readback succeeds

r[artifact_workspace.distribution.anonymous_exact.scenario.success]
- GIVEN the required source object is served by an existing canonical HTTP projection or declared mirror
- WHEN a fresh repository fetches that exact revision without credentials
- THEN the fetched commit and commit type MUST match the requested identity
- AND evidence MUST record the endpoint, revision, command outcome and source boundary without claiming indefinite availability or downstream correctness.

#### Scenario: Locator or cached object is insufficient

r[artifact_workspace.distribution.anonymous_exact.scenario.failure]
- GIVEN an endpoint fails, requires credentials, serves another object, or is only a plausible HTTPS URL or existing local cache
- WHEN anonymous source admission runs
- THEN that observation MUST NOT count as a passing acquisition
- AND no alternative RID, floating ref or sibling working tree MAY replace the exact source requirement.
