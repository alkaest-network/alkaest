# Vision

## Purpose

Alkaest is a decentralized coordination protocol for work.
It is designed to let individuals, teams, and organizations coordinate work without depending on any single centralized intermediary, while preserving trust through cryptographic identity, verifiable history, and portable reputation.

The first concrete domain is open-source development coordination.
The longer-term ambition is broader: design, automation, maintenance, delivery, and other service markets where reputation can function as a primary credential.

---

## Core principles

### Decentralized coordination

Work coordination should not depend on a central authority.
Protocol participants operate nodes that discover, evaluate, and synchronize work.
Alkaest does not assume that every useful coordinator must disappear: teams and independent operators may organize demand, split scopes, and bring contributors together, while the protocol keeps the work, rules, evidence, and settlement portable rather than dependent on one platform.

### Verifiable reputation

Reputation should come from evidence, not from subjective ratings or platform-owned profiles. Any consequential production use is gated on an anti-self-dealing, Sybil/collusion, and appeal model in RFC-0006; see the [reputation integrity threat model](../research/reputation-integrity-threat-model.md).

### Identity sovereignty

Users should control their own cryptographic identities and keep ownership of their history over time.

### Reputation as evidence

Reputation should emerge from completed work, validated outcomes, dispute outcomes, and other provable protocol events.

### Reputation decay

Older work should matter less than recent work so that reputation stays current.

### Domain context

Reputation is domain-specific.
Credibility in one kind of work does not automatically transfer to another.

### Progressive market entry

The system should help newcomers grow through smaller tasks while reducing incentives for senior participants to dominate trivial work.

---

## Conceptual model

The project currently revolves around four core ideas:

- Node
- Identity
- Task
- Reputation

### Node

A node is the runtime that executes the protocol.
In the MVP, each developer runs a local Standard node on their own machine (ADR-0003).

Nodes may eventually support:

- individual operators
- companies
- autonomous agents

For the MVP, the important point is simpler: the node is the protocol boundary.

### Identity

An identity represents an economic participant in the protocol.
Identities are cryptographic and self-controlled.
Reputation belongs to the identity, not to a particular device.

Nodes may eventually manage multiple identities for distinct work contexts without merging their reputational histories.

### Task

Tasks are units of work coordinated through the protocol.
The initial use case focuses on open-source development work, but the model is intended to grow into other domains over time.

### Reputation

Reputation is not just a single score.
It is better understood as a ledger of contribution evidence that can be interpreted per domain and over time.

---

## Reputation direction

The reputation model is intended to support:

- contribution proofs tied to real work
- reputation wallets as collections of contribution evidence
- domain-specific reputation profiles
- time-based decay
- negative signals such as abandonment, fraud, and dispute losses
- anti-farming protections such as validator diversity and diminishing returns on trivial work

The exact machine-readable proof and scoring model belongs in RFC-0006, which is not yet written. Until its launch gates are met, payment, task completion, merge, or agent acceptance alone must not be represented as mature reputation.

---

## Work progression

Task complexity should matter.

- low-complexity work should not generate outsized reputation
- well-matched work should produce the best progression
- stretch work may produce larger gains, but with more risk

This is meant to create a healthier reputation ladder over time.

---

## AI-assisted operation

Nodes may use AI agents to help with:

- analyzing tasks
- estimating fit
- estimating completion probability
- recommending work

An AI model's output is never protocol authority by itself. A separately identified agent may act only through capabilities explicitly granted by a signed Space policy; the treasury agent's bounded authority and restrictions are defined by ADR-0007/RFC-0014.

---

## Economic trust direction

The broader concept includes an economic security layer with:

- reward escrow
- requester bonds
- worker bonds
- validator compensation
- mediator incentives

The settlement model remains undecided until RFC-0008 and RFC-0013 define it; the Bitcoin treasury/audit direction does not itself specify escrow or dispute outcomes.

The broader concept also leaves room for:

- validation tiers based on task complexity
- Bitcoin settlement and audit anchoring for treasury activity (ADR-0007); ordinary protocol validation remains based on signed event logs
- optional identity assurance levels for higher-trust work

---

## Initial use case

The first practical wedge is open-source software development.

Alkaest should help projects:

- publish work
- coordinate contributors
- attach evidence to completed work
- validate outcomes
- build verifiable contributor reputation

GitHub may be used as an integration surface, but it is not the protocol itself.

The first project intended to use this model is Alkaest itself.
In other words, the network should bootstrap by coordinating the development of the Alkaest project through its own issue flow.

That implies an early operating plan where:

- the `alkaest-network` project becomes the first project coordinated through the protocol
- issues in `alkaest-network` become the first funded work items
- donations intended for Alkaest are distributed across those issues
- contributors to Alkaest become the first developers paid through the network

After the treasury workflow is activated, every change to Alkaest code and maintained project artifacts—including tests, dependencies, configuration, documentation, release assets, and visual identity—must reference a `WorkItem` or signed maintenance decision. The treasury agent may open and fund issues within a signed budget policy, then verify the exact delivery against rules fixed before work begins. Routine, uncontested work can be paid automatically after required independent review, merge, and CI/security checks pass. Exceptions and disputes require independent review.

Bitcoin provides the public settlement rail for donations and payouts and a periodic anchor for the signed treasury log. Full code, issue contents, personal data, and workflow payloads remain off-chain. The protocol's ordinary event validation stays peer-to-peer and does not depend on Bitcoin consensus (ADR-0003, ADR-0007).

The intended initial compensation asset for Alkaest contributors is BTC. A contributor may independently use Bisq to seek a BTC-to-fiat trade; fiat moves directly between the trading peers using an external payment method. Bisq is optional and separate from Alkaest, which does not guarantee a conversion offer, price, liquidity, or timing. RFC-0008 must still define the supported settlement rail, fees, and price denomination. See [Bitcoin payouts and optional Bisq conversion](../research/bitcoin-payouts-and-bisq-conversion.md).

This self-hosting path is important because it forces the protocol to prove its value on a real project before expanding to other teams.

The longer-term protocol direction also anticipates:

- validation by qualified participants
- dispute resolution for contested work outcomes
- evidence-driven reputation growth over time

## Market participation over time

Alkaest's adoption can begin with people and teams who already know how to find demand, scope it, and coordinate delivery. They can use the network to turn opportunities into funded WorkItems and bring together the contributors needed to complete them. This gives the first users a practical reason to participate and creates real examples of demand, delivery, payment, and evidence.

As the network becomes easier to discover and use, individual contributors should be able to install an Alkaest client or run a node, find suitable WorkItems, and participate directly. The transition is about adding a direct path, not requiring every project to use the same commercial arrangement: coordinators remain useful where they add scoping, trust, or delivery capacity, while contributors gain the option to find and take work without depending on a private marketplace account.

The protocol should support both paths with the same primitives. Work ownership, subcontracted scope, contributor roles, budgets, acceptance criteria, and payment splits must be explicit before work starts. Alkaest should not infer employment status or legal relationships from protocol roles; those depend on the parties and applicable law. The roadmap treats discovery, direct participation, and operator diversity as adoption milestones, not assumptions for the MVP.

---

## Commercial bootstrap path

Alkaest also has a near-term commercial bootstrap path through Alkaest Chatbot.

Alkaest Chatbot is a WhatsApp scheduling assistant for local service providers such as barbershops, dentists, doctors, salons, and clinics.
It can start as a centralized product because its immediate purpose is revenue, real customer learning, and operational proof.

The strategic sequence is:

```text
Alkaest Chatbot -> Private Service-Network Backend Pilot -> Discovery Frontend -> Alkaest Network
```

In this path:

- the chatbot helps providers manage appointment scheduling through WhatsApp
- before a protocol-facing discovery or reputation frontend, the chatbot can write provider-authorized scheduling events to private Spaces and validate them on an isolated multi-node network
- after that backend gate, a discovery number can let customers search for professionals already in the provider base
- appointment completion and customer feedback remain separate evidence claims; any reputation interpretation stays gated on RFC-0006
- provider profiles and service catalogs can later map to Alkaest Spaces, Identities, Objects, Events, Messages, Decisions, and Evidence

This path does not change the protocol core.
The core must remain generic enough to support multiple coordination domains.

Service scheduling is described by Draft RFC-0007. Its backend integration must still pass privacy, consent, deterministic replay, and multi-node validation before protocol-facing service/reputation screens are introduced. This path does not permit covert collection: customers and providers must be told how their data is used, and feedback must remain optional.

## Independent professional operating layer

The long-term product may give an independent professional more than a way to receive bookings: it can help them run and grow their own business. With the professional's permission, Alkaest could connect selected open-source tools for scheduling, customer management, invoicing, bookkeeping, and business operations through replaceable adapters. The professional chooses which tools and records to connect, can inspect what is used, and can export or disconnect their data.

Reports could combine operational facts such as revenue, expenses, booking patterns, cancellations, and workload. Later, with enough history and clear uncertainty, the product could offer decision support such as identifying a lower-demand period that may be suitable for time off. These are recommendations for the professional to review, not promises of financial outcomes or automatic business decisions. The system should explain the data and assumptions behind each insight and work when a user declines an integration.

This product layer should strengthen, not replace, the professional's own identity and business records. It belongs in modular applications and integrations over the Alkaest protocol, not as a universal business suite hard-coded into protocol core.

## Autonomous operations for physical assets

In a distant future, Alkaest could coordinate the operation of a physical asset such as a rental home. With the owner's explicit policy and connected systems (potentially including a home-automation platform such as Home Assistant), an agent could publish availability, answer booking requests, coordinate check-in and check-out, schedule approved cleaning, detect maintenance needs, request quotes, and assign repair WorkItems to qualified professionals. A guest could book through Alkaest, receive the necessary instructions, and trigger a bounded operational workflow without the owner manually coordinating each routine step.

This is a long-term scenario, not a current product capability or a promise of fully autonomous property management. The owner remains the principal and sets revocable limits for price, dates, access, spending, vendors, and actions. Guest consent and privacy apply to sensors, cameras, occupancy data, and messages. Agents must not silently expand permissions or make high-impact commitments outside policy. Access control, safety-critical devices, emergencies, legal obligations, unusual damage, disputes, and expenses above a preapproved cap require an explicit escalation path and, where appropriate, human decision. Every booking, instruction, authorization, sensor-derived claim, contractor assignment, approval, and payment-related decision needs attributable evidence and an appealable record.

The protocol should coordinate signed, scoped work and decisions; it should not directly become the home-control system, custody authority, property manager, or legal intermediary. Device and property integrations remain replaceable adapters, and tenant isolation is required if the hosted product serves multiple owners, properties, guests, or vendors.

## Open-source project ecosystem

Alkaest should make it practical for independent open-source projects to create their own Spaces, bring contributors together, fund work, and govern project decisions under rules they publish. A project may use DAO-like practices—transparent proposals, signed decisions, visible budgets, and replaceable roles—without requiring a transferable token or inheriting one global treasury/governance model.

Projects should be able to join, leave, or fork while keeping their own authority boundaries and portable records. Shared tooling and integrations can lower the cost of joining Alkaest, while each project remains responsible for its own governance and legal organization. The protocol supplies coordination primitives; it does not declare every Space a legal DAO or decide its legal status.

---

## Long-term vision

Over time, Alkaest aims to become a universal coordination layer for work.

Potential future domains include:

- software development
- design
- infrastructure automation
- home services
- delivery
- technical consulting
- rental-property operations coordinated with home-automation and local-service integrations

The long-term idea is that reputation becomes a portable, evidence-based credential for participating in these markets.

---

## Status

This vision is intentionally conceptual.
The implementation path should continue to move from vision into precise RFCs, starting with protocol correctness, node architecture, and the first workflow module. The [roadmap](roadmap.md) defines the sequence and security gates.
The first workflow should eventually be strong enough to coordinate Alkaest's own development.
