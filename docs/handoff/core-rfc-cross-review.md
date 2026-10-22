# RFC-0001–0005 Cross-Review

**Status:** Working review record; the RFCs remain Draft.
**Date:** 2026-10-19

This record captures the cross-RFC rules aligned in RFC-0001 through RFC-0005 and the work still required before implementation or production reliance. The binding candidate details live in the RFCs themselves; this document is a navigation and review aid.

## Draft rules aligned

| Concern | Aligned rule | Primary specification |
|---|---|---|
| Canonical JSON | Use RFC 8785 JCS over UTF-8; reject duplicate keys and non-I-JSON values; do not normalize Unicode. Amounts and integers outside safe binary64 precision are schema-validated decimal strings. | [RFC-0004](../rfc/0004-envelope-canonical-encoding-and-object-ids.md) |
| Crypto encodings | Ed25519; public key is 32-byte unpadded base64url, signature is 64-byte unpadded base64url, SHA-256 hash is 64 lowercase hex characters. | [RFC-0004](../rfc/0004-envelope-canonical-encoding-and-object-ids.md) |
| IDs | Use fixed type prefixes and domain-separated SHA-256 over immutable canonical preimages that exclude the ID field. Object IDs exclude projection metadata. | [RFC-0004](../rfc/0004-envelope-canonical-encoding-and-object-ids.md) |
| Wire payload | `payloadBytes` is an unpadded base64url string; the decoded bytes must be valid UTF-8, parse without duplicate keys, and equal their JCS canonical re-encoding byte-for-byte. | [RFC-0004](../rfc/0004-envelope-canonical-encoding-and-object-ids.md) |
| Validation and mutation | Validate envelope structure, canonical bytes, hash, IDs, author, signature, schema, sequencing, permissions and module transition before state mutation. Local record and projection updates must recover atomically from failure. | [RFC-0002](../rfc/0002-node-architecture.md), [RFC-0004](../rfc/0004-envelope-canonical-encoding-and-object-ids.md), [RFC-0005](../rfc/0005-object-event-semantics-and-state-resolution.md) |
| Concurrent state events | Preserve both valid competing branches and stop projection at their common ancestor. Never choose a business outcome by event ID, timestamp or arrival order. A unique authorized resolution must name the conflict; concurrent resolutions leave it unresolved. | [RFC-0005](../rfc/0005-object-event-semantics-and-state-resolution.md) |
| Local projection and finality | `applied` is a deterministic, revisable local projection over currently known events, not global finality. Modules must define finality before an irreversible external effect. | [RFC-0005](../rfc/0005-object-event-semantics-and-state-resolution.md) |
| Workflow payment | `payout_authorized` records approval under policy. `paid` requires confirmed settlement under RFC-0008; a PR merge or provider callback alone is not payment proof. | [RFC-0003](../rfc/0003-development-workflow-module.md), [RFC-0014](../rfc/0014-treasury-agent-and-release-authorization.md) |
| Object metadata | `updatedAt` is derived projection metadata, not part of an immutable signed creation record. State changes are represented through events. | [RFC-0001](../rfc/0001-protocol-core.md), [RFC-0005](../rfc/0005-object-event-semantics-and-state-resolution.md) |
| Node profiles | Desktop Standard is the first implementation target; the architecture supports Light, Standard, and Service profiles from the start. Storage and service roles differ by profile, but accepted records use the same validation rules and profile/capability claims do not establish trust. | [RFC-0002](../rfc/0002-node-architecture.md) §4 and §16, [ADR-0003](../decisions/ADR-0003-heterogeneous-nodes-and-network-validation.md) |
| Resource bounds | Draft direction is class-specific hard protocol ceilings plus lower operator-local caps; capability negotiation may select smaller chunks but never raise a ceiling. Numeric limits await the ADR-0009 benchmark plan. | [RFC-0002](../rfc/0002-node-architecture.md) §16.5, [ADR-0009](../decisions/ADR-0009-resource-aware-capacity-and-deployment.md) |
| Non-financial conflict authority | Mutual party agreement may resolve cooperatively; otherwise the Draft baseline is a predeclared Space-local 2-of-3 resolver panel. Mediation is advisory, and state resolution cannot moderate identities or authorize money movement. | [RFC-0005](../rfc/0005-object-event-semantics-and-state-resolution.md) §9.6–9.7 |
| Durable state and recovery | Admission, event classification, and projection/head update form one recoverable commit; rebuild uses admitted immutable records and atomically swaps a complete projection generation. Crash/fault verification remains pending. | [RFC-0002](../rfc/0002-node-architecture.md) §6.5.1, [RFC-0005](../rfc/0005-object-event-semantics-and-state-resolution.md) §11 |

## Still blocking implementation readiness

1. Review and exercise the [RFC-0004 known-answer fixtures](../rfc/vectors/rfc-0004.json) in independent implementations; add boundary cases as gaps are found.
2. Exercise the [RFC-0005 state-machine fixtures](../rfc/vectors/rfc-0005.json) against independent projection implementations, especially all event delivery permutations.
3. Cross-review the proposed RFC-0005 2-of-3 resolver baseline: define the approval event/schema, roster rotation and key-loss behavior, conflict/appeal interaction, and exact module scope before implementation.
4. Inventory payload classes and run ADR-0009's reproducible Light/Standard/Service benchmark plan; then choose and version numeric envelope, payload, attachment-chunk, batch, parser, CPU, memory, and replay limits.
5. Verify RFC-0002 §6.5.1 admission, transaction, crash-recovery, quarantine, and atomic projection-generation behavior under injected failures; projection rebuild must remain possible from admitted records.
6. Complete RFC-0003 states and event schemas, distinguishing claim requests, assignment, validation, payout authorization, settlement confirmation, cancellation, and disputes.
7. Define RFC-0008 settlement confirmation and RFC-0013 disputes/finality before any real payout. RFC-0014 remains gated by these specifications.
8. Independently review cryptographic and security choices and adversarial interoperability results before marking these drafts Accepted.

## Exit criteria

RFC-0001–0005 remain Draft until all of the following are available:

- conformance vectors pass in at least two independent implementations;
- the authority and conflict rules are auditable and have no implicit hash-based winner;
- size/resource limits, validation-before-mutation, and crash recovery are specified and verified;
- a documented security review has no unresolved launch-blocking finding;
- RFC-0003 payment states point to a specified settlement and dispute finality model.

