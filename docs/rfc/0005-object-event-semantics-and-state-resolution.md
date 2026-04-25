# RFC-0005 — Object/Event Semantics and State Resolution

**Status:** Draft
**Author:** modern_alchemist
**Date:** 2026
**Category:** Protocol Specification

---

# 1. Abstract

This RFC defines how Alkaest objects and events produce deterministic state.

It specifies:

* the role of Objects versus Events
* the lifecycle of mutable protocol state
* event sequencing expectations
* object version progression
* pending, applied, rejected, and conflicting event handling
* deterministic projection rebuild rules

The goal is that honest nodes receiving the same valid envelopes eventually compute the same object state and the same query projections.

---

# 2. Goals

This RFC defines:

* what state is immutable and what is event-derived
* how objects are created and evolved
* how events are ordered for a target object
* how nodes handle out-of-order and conflicting events
* how projections are rebuilt deterministically

This RFC does not define:

* module-specific business rules in full detail
* final dispute procedures
* reputation issuance rules
* settlement mechanics
* transport-level replication flows

Those remain the responsibility of other RFCs.

---

# 3. Context

RFC-0001 introduces:

* Object
* Event
* Relation
* Decision
* Envelope

RFC-0002 requires the node runtime to:

* validate envelopes
* process events
* rebuild projections

RFC-0003 defines a workflow module whose `WorkItem` status and payout eligibility depend on event-driven transitions.

RFC-0004 makes envelopes, payload bytes, hashes, signatures, and identifiers deterministic.

This RFC defines how those deterministic envelopes become deterministic state.

---

# 4. Core Model

## 4.1 Objects are stable anchors

An `Object` is the stable anchor for a unit of protocol state.

The object creation payload defines:

* identity of the object
* object type
* schema
* initial metadata
* initial immutable fields

## 4.2 Events express state transitions

An `Event` represents a proposed state transition affecting an existing object.

State that changes over time SHOULD be expressed through events rather than by rewriting the original object creation payload.

## 4.3 Projections are derived state

Queryable state is not authoritative by itself.
Authoritative state is:

* the created object
* the accepted event history for that object

Projections are deterministic read models built from that history.

---

# 5. Object Semantics

## 5.1 Object creation

An object becomes known to the protocol when an `object.created` event or equivalent creation envelope is accepted according to the module rules.

For MVP purposes, an object has:

* one creation record
* zero or more subsequent events

## 5.2 Immutable versus mutable fields

The following SHOULD be treated as immutable after object creation:

* `id`
* `spaceId`
* `objectType`
* `schemaId`
* `ownerIdentityId`
* creation timestamp

Mutable state SHOULD be represented through events and projections, not by mutating these fields directly.

## 5.3 Object base state

Each object has a base state composed of:

* its creation payload
* initial version `0`
* no applied events yet

---

# 6. Event Semantics

## 6.1 Event purpose

An event is a typed transition proposed against a target object.

Each event MUST identify:

* `targetObjectId`
* `eventType`
* `actorIdentityId`
* `createdAt`

## 6.2 Event sequencing fields

To support deterministic state resolution, event payloads affecting mutable object state MUST include these sequencing fields:

```text
EventSequencing
- targetVersion
- prevEventId
```

### targetVersion

`targetVersion` is the object version that will exist if the event is applied.

### prevEventId

`prevEventId` references the last applied event the actor believes this new event extends.

For the first state-changing event after creation, `prevEventId` is `null` and `targetVersion` is `1`.

## 6.3 Event classes

Events fall into three practical classes:

* state-changing events
* evidence or commentary events
* authoritative resolution events

### state-changing events

These advance object state and normally increment the object version.

Examples:

* `work_item.assigned`
* `work_item.accepted`
* `work_item.closed`

### evidence or commentary events

These attach supporting information but do not necessarily change the core lifecycle state.

Examples:

* `work_item.evidence_added`
* reviewer notes
* external reference attachments

### authoritative resolution events

These resolve ambiguity or conflict and are intended to become the canonical next state.

Examples:

* dispute closure
* authoritative approval
* administrative cancellation

---

# 7. Object Version Model

## 7.1 Version progression

Each object has a monotonically increasing integer version.

Rules:

* object creation starts at version `0`
* each applied state-changing event increments the version by `1`
* evidence-only events MAY reference the current version without incrementing it if module rules allow

## 7.2 Applied head

Each object has one current applied head:

```text
ObjectHead
- objectId
- currentVersion
- lastAppliedEventId
```

This head is what later events must extend unless they are purely informational and explicitly defined as non-version-advancing by their module.

---

# 8. Event Admission States

After envelope validation from RFC-0004, a node classifies an event envelope into one of these local processing states:

* `pending`
* `applied`
* `rejected`
* `conflicting`

## 8.1 Pending

An event is `pending` when:

* its target object is known
* the envelope is valid
* the required prior state is not yet locally available

Examples:

* missing `prevEventId`
* target version gap
* dependent object not yet materialized

## 8.2 Applied

An event is `applied` when:

* its envelope is valid
* module-level validation passes
* its sequencing fields match the current applied head
* it wins any deterministic conflict comparison required by this RFC

## 8.3 Rejected

An event is `rejected` when:

* schema validation fails
* permission validation fails
* module transition rules fail
* the event references impossible state
* the payload is well-formed but semantically invalid

Rejected events may be retained for audit or debugging, but they MUST NOT affect projections.

## 8.4 Conflicting

An event is `conflicting` when:

* its envelope is valid
* its module semantics are individually valid
* but another event already occupies the same next-state slot deterministically

Conflicting events are not applied to the canonical projection state unless a later resolution event or rule reintroduces them.

---

# 9. State Resolution Rules

## 9.1 Normal application rule

A state-changing event is eligible for application when all of the following are true:

* `targetObjectId` exists
* `targetVersion == currentVersion + 1`
* `prevEventId == lastAppliedEventId`
* module transition rules allow `eventType` from the current projected state
* permission checks succeed

## 9.2 Out-of-order delivery

If a valid event references a `prevEventId` not yet known locally, it MUST remain `pending` until:

* the predecessor arrives and is applied
* the predecessor is rejected
* the event is superseded by deterministic conflict handling

## 9.3 Version gap rule

If an event references `targetVersion > currentVersion + 1`, it MUST remain `pending`.
Nodes MUST NOT skip versions to apply it early.

## 9.4 Stale event rule

If an event references:

* a `targetVersion` already passed, or
* a `prevEventId` that is no longer the applied head

then the event becomes `conflicting` unless a module-specific rule explicitly classifies it as `rejected`.

## 9.5 Conflict slot

For each object version step, only one state-changing event may become the canonical applied event.

If multiple valid candidate events compete for the same slot, nodes MUST choose a deterministic winner.

## 9.6 Deterministic conflict winner

The default MVP winner rule is:

1. Prefer an authoritative resolution event over a normal state-changing event if both target the same next slot and are otherwise valid.
2. If candidate classes are equal, choose the candidate with the lexicographically smallest `eventId`.

All other candidates for that slot become `conflicting`.

This rule is intentionally simple and exists to ensure convergence before richer conflict markets or governance rules exist.

---

# 10. Module Transition Validation

RFC-0005 defines the generic resolution framework.
Each module still defines which transitions are legal.

For example, the workflow module from RFC-0003 may allow:

```text
funded -> open
open -> assigned
assigned -> in_progress
in_progress -> submitted
submitted -> accepted
accepted -> paid
paid -> closed
```

and reject illegal transitions such as:

```text
draft -> paid
closed -> assigned
accepted -> open
```

Module transition validation MUST run before an event can become `applied`.

---

# 11. Projection Rebuild Algorithm

Nodes MUST be able to rebuild projections from stored protocol records alone.

Recommended rebuild algorithm per object:

1. Load the object creation record.
2. Initialize the projection state from the object creation payload.
3. Gather all valid event envelopes targeting that object.
4. Partition them into state-changing and non-state-changing classes where module rules require.
5. Repeatedly apply the eligible next event according to the resolution rules in this RFC.
6. Mark unresolved future events as `pending`.
7. Mark losing same-slot events as `conflicting`.
8. Mark invalid events as `rejected`.
9. Build derived query projections from the resulting canonical object state.

This algorithm MUST produce the same applied head when the input envelope set is the same.

---

# 12. Deterministic Ordering for Projection Work

When multiple candidate envelopes are otherwise ready for the same processing step, nodes SHOULD sort them by:

1. `targetVersion`
2. `createdAt`
3. `eventId`

The tie-breaker on `eventId` ensures stable ordering even if timestamps are equal.

Ordering alone does not decide validity.
It only ensures that deterministic processing does not depend on local arrival order.

---

# 13. Event Replay Semantics

## 13.1 Replay requirement

Nodes MUST be able to replay event history after restart or projection rebuild.

## 13.2 Replay safety

Replay MUST be idempotent.
Applying the same valid event history multiple times must produce the same canonical state.

## 13.3 Duplicate envelopes

If the same envelope is received multiple times, the node MUST deduplicate by `envelopeId`.
Duplicate receipt MUST NOT create duplicate state transitions.

---

# 14. Relations, Messages, and Decisions

Not every protocol entity needs the same state progression model.

## 14.1 Relations

Relations are usually immutable assertions once created.
If a relation needs lifecycle state, it SHOULD be modeled as an object with events rather than as repeated mutation of the relation itself.

## 14.2 Messages

Messages are append-only communication records.
They normally do not require version progression after creation.

## 14.3 Decisions

Decisions are authoritative records.
They are usually immutable once created, though they may target mutable objects and thereby affect projection outcomes.

---

# 15. Example: WorkItem Assignment Conflict

Two contributors race for the same funded `WorkItem`.

Events received:

* `evt_a`: `work_item.assigned`, `targetVersion=2`, `prevEventId=evt_funded`
* `evt_b`: `work_item.assigned`, `targetVersion=2`, `prevEventId=evt_funded`

If both events are individually valid and no authoritative resolution event exists:

* sort by deterministic winner rule
* apply the winner
* mark the loser as `conflicting`

All honest nodes with the same event set will therefore converge on the same assignee projection.

---

# 16. Error and Audit Visibility

Nodes SHOULD expose local visibility into:

* pending events
* rejected events
* conflicting events
* current applied head per object

This is important for debugging workflow issues and explaining why some validly signed events did not become canonical state.

---

# 17. Implementation Guidance

Implementations SHOULD keep separate stores or indexes for:

* raw admitted envelopes
* canonical applied object state
* pending event queues
* rejected and conflicting audit records

Because the project follows TDD, implementations of this RFC should begin with:

* event ordering tests
* pending-to-applied transition tests
* deterministic conflict winner tests
* projection rebuild tests
* duplicate envelope replay tests

---

# 18. Future Work

Later RFCs may refine or replace parts of this model with:

* richer authority and permission rules
* dispute-aware conflict resolution
* module-specific conflict policies
* CRDT-style object classes for selected data types
* multi-head merge semantics

Those possibilities remain open, but they are not required for the MVP.

---

# 19. Summary

This RFC defines how Alkaest turns immutable records into deterministic mutable state.

The MVP model is:

* objects are stable anchors
* events drive state transitions
* projections are derived
* one canonical applied event occupies each version slot
* pending, rejected, and conflicting events remain visible but do not silently alter canonical state

With RFC-0005 in place, the protocol has a workable foundation for building consistent full-node behavior on top of RFC-0004's deterministic envelopes.
