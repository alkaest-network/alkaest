# Paid Work Pilot Cross-Review

**Date:** 2026-10-19  
**Scope:** Paid-work pilot Draft requirements in RFC-0003/RFC-0014 against RFC-0004/0005 and Draft RFC-0008/RFC-0013.

This is a documentation cross-review, not protocol acceptance, implementation verification, or authorization to use real funds. At the time of the original review, RFC-0008 and RFC-0013 were not written. Follow-up: both now exist as drafts. RFC-0008 defines an on-chain BTC settlement interface; RFC-0013 defines a conservative validation/dispute lifecycle. Their open script/key, timeout/refund, chain-proof, destination-control, selection, appeal, and authority decisions remain launch blockers.

## Cross-review findings

| Topic | Cross-review result | Follow-up |
|---|---|---|
| Event signatures and mutual consent | RFC-0004 envelopes have one author/signature. A single `terms_amended` event cannot prove the requester proposed terms and the assignee accepted them. | RFC-0003 now distinguishes signed `terms_amendment_proposed` and `terms_amendment_accepted` events, the latter referencing the exact proposal/digest. |
| Event ordering and concurrent amendments | RFC-0005 requires state-changing events to extend `targetVersion`/`prevEventId`. Competing valid events remain conflicting at their common ancestor until an authorized resolution; arrival order does not choose a winner. | Amendments and assignment release are separate events. Concurrent proposal/acceptance/release races must be explicit in future conformance scenarios. Do not infer acceptance from time or GitHub state. |
| Assignment and reassignment | RFC-0005 can represent assignment/release as state transitions, but RFC-0003 needs module authority and preconditions. | RFC-0003 now proposes one active assignee, fixed deadlines, and explicit release/expiry before reassignment. Exact deadline semantics, authority during maintainer unavailability, and stalled/conflicting branches remain unresolved. |
| WorkItem lifecycle and role boundaries | A lifecycle needs deterministic guards for claim, assignment consent, work, review, payout, cancellation, and closure; provider observations must not acquire protocol authority. | RFC-0003 now has a transition table, separate assignment offer/acceptance, role permissions, funding/settlement projections, and provenance-labeled evidence. These remain draft rules: resolve expiry authority/time semantics, project integration, adapter trust, event schemas, and cross-RFC conformance before implementation. |
| Validation and dispute event mapping | RFC-0003 and RFC-0013 had overlapping submission/validation event names; RFC-0003 also named funding broadcast/failure events absent from RFC-0008's settlement vocabulary. | The drafts now share `work_item.submitted` and `work_item.validation_attested`; RFC-0013 explicitly reuses the RFC-0003 submission event. RFC-0008 now defines funding broadcast/failure records. Canonical payload schemas, actor authority, and compatibility vectors still need review. RFC-0003 also blocks payout and closure while an RFC-0013 case is unresolved; the case remains a separate object. |
| Reviewer independence | RFC-0003/RFC-0014 can require reviewer identities distinct from requester, funding authority, and assignee. Neither RFC-0004 nor RFC-0005 proves these are different people or detects hidden related identities. | Treat this as visible role separation only, never Sybil resistance. Define declared/protocol-visible conflicts and escalation; validate stronger reviewer rules with RFC-0006/0013. |
| Payout destination | RFC-0004 can sign a contributor-authored instruction, and RFC-0005 can order it, but neither defines payment-address proof, confidentiality, escrow outputs, fees, refunds, or finality. | RFC-0003/RFC-0014 now prohibit destination selection from issue/PR text, AI output, or adapter callbacks. RFC-0008 must define proof of control, address changes, output validation, privacy, and settlement finality before this is implementable. |
| Disputes and appeals | RFC-0005 has generic authoritative conflict resolution, but this does not define mediation eligibility, impartiality, evidentiary procedure, outcomes, or appeal finality. | A disputed task must block routine release. RFC-0013 must specify the independent decision and appeal process; do not treat a generic conflict-resolution event as a mediator verdict. |
| Escrow and partial payment | RFC-0003/RFC-0014 require funding before assignment and allow only predeclared, separately funded milestones for partial payout. | RFC-0008 must define reservation, cooperative release/refund, fees, timeout/refund behavior, transaction validation, and how milestone escrows map to the WorkItem. No real-money pilot before then. |

## Changes made from this review

- Replaced the single amendment event proposal with a signed proposal event plus a separate assignee acceptance event, consistent with the single-author envelope model.
- Added the new amendment event names to RFC-0003 and made explicit that an unaccepted amendment cannot affect eligibility.
- Recorded that event branches do not resolve by arrival order and that conflicting economic state blocks release.
- Updated the open questions, current state, and next-task list to identify which work depends on RFC-0008's and RFC-0013's open design gates.

## Follow-up after RFC-0008 draft

- RFC-0003 now has separate `fundingStatus` and `settlementStatus` projections. Allocation, escrow confirmation, payout authorization, broadcast, observation, settlement, refund, and reorganization are separate events/states; `paid` follows only verified settlement.
- RFC-0003 now specifies a WorkItem transition table, role separation, and evidence/validation records bound to term versions and immutable revisions. A validation `pass` is distinct from the authorized acceptance event; `payout_authorized` remains distinct from confirmed `paid`. The state table and event schemas still require review against RFC-0004/0005/0008/0013/0014, including project adapters and expiry authority.
- RFC-0008 defines the initial on-chain BTC `regtest` interface and explicit transaction/output validation requirements. RFC-0013 separates mediation/adjudication from settlement authorization and leaves disputed spending disabled. Neither provides a finalized script/key profile, destination-control proof, timeout/refund path, production chain-observation rule, or secure mediator-selection policy.
- RFC-0014's release diagram now shows broadcast, chain observation, confirmation, and reorganization/hold states. The cross-RFC event schema and vectors still need review before implementation.

## Remaining decisions

1. Define timestamp trust, deadline grace, expiry evidence, and conflict behavior in RFC-0004/0005 and RFC-0003. A timestamp passing locally must not silently release an assignment.
2. Define maintainer authority and succession for releasing assignments, especially if the assignee is unavailable or disputes expiry.
3. Specify hidden-relationship limitations and reviewer/mediator role separation without overstating identity assurance.
4. Cross-review Draft RFC-0008 with RFC-0003/RFC-0014 and resolve its settlement launch gates; keep RFC-0013 mediation and appeal mechanics as an explicit dependency.
5. Cross-review RFC-0013 for independent validation, mediation, appeal, and finality, consistent with the unresolved event branches in RFC-0005.
6. Only after these specifications stabilize, define conformance vectors and tests. No real payment or external-project pilot is authorized.

## Source documents

- [RFC-0003 Development Workflow Module](../rfc/0003-development-workflow-module.md)
- [RFC-0004 Envelope Encoding and Object IDs](../rfc/0004-envelope-canonical-encoding-and-object-ids.md)
- [RFC-0005 Object Event Semantics and State Resolution](../rfc/0005-object-event-semantics-and-state-resolution.md)
- [RFC-0014 Treasury Agent and Release Authorization](../rfc/0014-treasury-agent-and-release-authorization.md)
- [Alkaest paid work pilot design](../research/alkaest-paid-work-pilot-design.md)
- [RFC-0008 Bitcoin Escrow and Settlement](../rfc/0008-bitcoin-escrow-and-settlement.md) and [RFC-0013 Validation, Dispute Resolution, and Appeals](../rfc/0013-validation-dispute-resolution-and-appeals.md) are Drafts; neither authorizes real funds.
