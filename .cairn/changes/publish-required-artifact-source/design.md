## Context

The existing unified Artifact identity is private with one delegate and threshold one. Read-only native inspection showed the current operator DID equals that delegate. Cairn requires `e41340bec587b6d049b5cc518ec7db925dde84be`; Mantle requires `c932138d880ddf4c2967f4c024b489b5c0022bf1`. These are separate immutable objects. The previously published `z4JGYYW7WsesXUq7MXVdx16Fawu2f` compatibility identity covers another historical revision and is not a substitute.

## Decisions

### Decision: Publish the existing identity without expanding authority

**Choice:** Use the native existing-RID publication operation only after the owning admission gates and bounded exposure review. Preserve delegates, threshold, branch meaning, source objects, and licenses. This package is authorized by the operator's explicit required-dependency publication request, not by a structural gate or an assistant completion claim.

**Rationale:** Source identity and acquisition transport are separate. Reusing the canonical identity preserves ownership and consumer exact pins; an unrelated identity or a local checkout would not prove anonymous public acquisition.

The observed native `main` is `eb85ddcd9d5c782044a81ed980c1824438bb46c1`, which is not an ancestor of either required source. The required `e41340bec587b6d049b5cc518ec7db925dde84be` is an ancestor of `c932138d880ddf4c2967f4c024b489b5c0022bf1`. Preserve native `main` and the default branch rather than force-updating them. Publish only the reviewed exact source commits on dedicated `consumer-pins/<full-revision>` refs under the existing delegate; those refs describe immutable consumer inputs, not a replacement release or main branch.

### Decision: Admit an acquisition endpoint only after exact anonymous readback

**Choice:** An existing canonical HTTP projection or declared mirror must serve each requested Git commit into a fresh repository with user/system Git configuration, credentials, prompts and SSH disabled. Read back the exact commit and its type. Preserve negative observations and unavailable routes; do not label an HTTPS locator successful merely because it is well formed.

**Rationale:** Operator caches and successful credentialed builds cannot establish an outside user's acquisition path. The repeatable capability is exact anonymous source admission for current Cairn/Mantle consumers, maintained by Artifact's existing owner.

## Risks / Trade-offs

- Making an existing identity public may expose its advertised refs and reachable history, not merely the two selected runtime crates. Review that native publication surface before mutation; report residual scope explicitly.
- A redacting scanner and manual review are bounded observations, not proof that no secret or privacy issue exists. Stop on a confirmed unresolved exposure or redistribution restriction.
- Publication does not prove indefinite availability, seed trust, source or downstream correctness, consumer lock freshness, release eligibility, or authority to publish any other repository.
