## Why

Lattice's required Cairn and Mantle producers need the unified Artifact workspace at exact revisions `e41340bec587b6d049b5cc518ec7db925dde84be` and `c932138d880ddf4c2967f4c024b489b5c0022bf1`. Its existing canonical identity `rad:z25ySMy8Hh3HpsxP5zcYoYgaMBi99` is private, and actual anonymous acquisition currently fails. Publishing the unrelated frozen compatibility identity cannot satisfy either source requirement.

## What Changes

- Publish only the existing unified Artifact identity under the operator's explicit required-dependency authorization, after bounded source/history exposure review and owning admission gates.
- Preserve its current single delegate, threshold one, source objects, package licenses, and default branch; do not create an identity, change governance, or substitute source revisions.
- Verify both exact objects through an actual credential-free HTTP Git projection and record scoped acquisition and publication facts.

## Impact

- **Consumers:** Cairn's authentication source and Mantle's Artifact source retain exact object/package identities while removing a credential prerequisite.
- **Files:** This lifecycle package, source-distribution evidence and the existing distribution documentation; no mechanism implementation changes.
- **Owner:** Artifact maintainers own native identity and publication evidence. Cairn, Mantle and Lattice maintainers own their independent exact-source cutovers and generated locks.
- **Testing:** Native proposal/design/tasks admission; redacted tracked/history exposure review for the published refs; native identity/delegate/threshold readback; fresh anonymous exact-object acquisition and commit readback. These observations do not establish behavioral or security correctness.
