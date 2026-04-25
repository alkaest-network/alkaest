# ADR-0001 — Desktop-First MVP

**Status:** Accepted
**Date:** 2026-03-16
**Decision Type:** Product and Architecture

---

## Context

Alkaest is a protocol-first project.
The repository currently defines:

* a generic protocol core
* a local node architecture
* a first development workflow module
* a self-hosting plan where Alkaest coordinates the development of Alkaest

At this stage, the project needs a clear MVP execution model.
Without that clarity, the architecture could drift toward supporting:

* mobile-first clients
* light-client sync
* hosted multi-tenant nodes
* broad consumer experiences

too early, before the protocol and workflow are proven on a real project.

The project also intends to bootstrap on the `alkaest-network` project itself, with donations to Alkaest being allocated across Alkaest issues and paid to Alkaest contributors.
That bootstrap path favors a developer-centric environment over a consumer-first one.

---

## Decision

Alkaest will pursue a **desktop-first MVP**.

For the MVP:

* each developer is expected to run a local full node
* the primary user environment is the developer workstation
* the first workflow is open-source development coordination
* the first project on the network is expected to be Alkaest itself
* GitHub is treated as an integration layer, not as the protocol

The MVP will optimize for:

* protocol correctness
* local node operation
* issue-based development workflow
* evidence and validation capture
* funded contributor coordination for `alkaest-network`

The MVP will not optimize for:

* mobile-first experiences
* light-client-first architecture
* partial replication as a first-class requirement
* hosted custodial operation as the main product model
* generalized non-developer consumer onboarding

---

## Why this decision was made

### 1. The first real users are developers

The first people expected to use Alkaest are the developers building Alkaest.
A desktop-first MVP matches that user base directly.

### 2. Local full nodes reduce ambiguity

A local full node is simpler to reason about than a light-client or hosted-node model.
It reduces early complexity around:

* trust boundaries
* partial synchronization
* remote signing
* offline subset storage
* delegated infrastructure custody

### 3. Self-hosting needs operational simplicity

Because the first project on the network is Alkaest itself, the first workflow needs to be practical, not abstract.
A desktop-first environment gives contributors a direct path from:

* issue selection
* local development
* evidence creation
* validation
* payout eligibility

### 4. It preserves the protocol-first approach

A desktop-first node model reinforces the idea that the node is the protocol boundary.
That aligns with the current RFC direction much better than starting from a thin client or hosted platform pattern.

### 5. It keeps future options open

Choosing desktop-first for the MVP does not prevent future support for:

* mobile clients
* light nodes
* selective sync
* managed node hosting

It simply prevents those concerns from distorting the first implementation.

---

## Consequences

### Positive consequences

* The first implementation target is clearer.
* RFCs can optimize for local full-node behavior.
* Developer workflow integration becomes the main product path.
* The protocol can prove itself on a real project before expanding scope.
* Documentation can distinguish more clearly between MVP and future architecture.

### Negative consequences

* Early UX may be less accessible to non-technical participants.
* Mobile and consumer use cases are explicitly delayed.
* Some future architectural concerns will need revisiting later.

### Constraints introduced

* MVP docs should avoid introducing light-client requirements unless explicitly marked as future work.
* Workflow design should assume a developer workstation environment.
* Integration design should prioritize GitHub and developer tooling before broader platform integrations.

---

## Alternatives considered

### Mobile-first MVP

Rejected because it introduces selective sync, embedded wallet behavior, and device constraints too early.

### Hosted-node MVP

Rejected as the default model because it weakens the node-first and self-sovereign posture of the protocol before it is proven.

### Dual desktop and mobile MVP

Rejected because it expands scope without first proving the core workflow on a single strong environment.

---

## Relationship to current RFCs

This decision supports:

* [RFC-0001 Protocol Core](/Users/nivaldojunior/Documents/Alkaest/alkaest/docs/rfc/0001-protocol-core.md)
* [RFC-0002 Node Architecture](/Users/nivaldojunior/Documents/Alkaest/alkaest/docs/rfc/0002-node-architecture.md)
* [RFC-0003 Development Workflow Module](/Users/nivaldojunior/Documents/Alkaest/alkaest/docs/rfc/0003-development-workflow-module.md)
* [RFC-0004 Envelope, Canonical Encoding, and Object IDs](/Users/nivaldojunior/Documents/Alkaest/alkaest/docs/rfc/0004-envelope-canonical-encoding-and-object-ids.md)

This ADR should be treated as a product-direction constraint when writing future RFCs.

---

## Follow-up implications

This decision implies that upcoming work should continue to prioritize:

* RFC-0005 state resolution for full nodes
* `.alkaest/project.yaml` for project integration
* donation-to-issue allocation rules for `alkaest-network`
* diagrams and workflows aimed at desktop developer usage

---

## Summary

Alkaest will start as a desktop-first, local-full-node protocol for coordinating open-source development work.
The first project on the network is expected to be Alkaest itself.

This ADR keeps the MVP narrow enough to build, test, and validate on a real project before taking on mobile, light-client, or broader consumer complexity.
