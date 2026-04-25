# Roadmap

## Purpose

This roadmap connects the current vision to an implementable protocol.
It captures the main planning gaps, the recommended RFC sequence, and the founder-level decisions that still need to be made.

---

## What is already defined

### Strongest current material

- Vision and principles in [vision.md](/Users/nivaldojunior/Documents/Alkaest/alkaest/docs/overview/vision.md)
- Shared terminology in [glossary.md](/Users/nivaldojunior/Documents/Alkaest/alkaest/docs/overview/glossary.md)
- Core protocol shell in [0001-protocol-core.md](/Users/nivaldojunior/Documents/Alkaest/alkaest/docs/rfc/0001-protocol-core.md)
- Desktop-first node architecture in [0002-node-architecture.md](/Users/nivaldojunior/Documents/Alkaest/alkaest/docs/rfc/0002-node-architecture.md)

### Still mostly conceptual

- Reputation scoring and proof issuance
- Marketplace workflow semantics
- Service scheduling workflow semantics
- Economic settlement and bonds
- Validator and mediator incentives
- AI-assisted task matching
- donation-to-issue allocation for the first self-hosted project

### Not yet defined enough to build against

- canonical encoding and hash rules
- deterministic event ordering and merge behavior
- workflow object schemas
- validation evidence model
- node API contract
- integration configuration
- governance and versioning

---

## Main gaps

### 1. Core protocol versus workflow boundary

The project still needs a crisp line between:

- generic protocol primitives
- open-source development workflow behavior
- future marketplace and economic modules

Recommendation:
Keep the core protocol generic and push workflow-specific behavior into module RFCs.

### 2. Envelope and encoding rules

RFC-0001 defines the envelope concept, but the project still lacks exact rules for:

- canonical serialization
- hashing
- signatures
- ID derivation
- validation procedure

Without this, implementations cannot converge reliably.

### 3. Event semantics and deterministic state

The project needs explicit rules for:

- valid event ordering
- replay behavior
- conflict handling
- invalid transition handling
- projection determinism

This is a protocol blocker for implementation.

### 4. Workflow module definition

The first domain is open-source development coordination, but the concrete workflow is still underspecified.

The system still needs a module RFC that defines:

- task or `WorkItem` schemas
- claiming or assignment behavior
- evidence submission
- validation checkpoints
- project integration configuration
- funding flows from donated money into issue-level work items

The first reference workflow should be for Alkaest itself, with the `alkaest-network` project acting as the first project coordinated through the network.

### 5. Reputation model

The vision depends on portable, evidence-based reputation, but the exact rules are still open:

- contribution proof schema
- scoring model
- decay model
- domain boundaries
- negative signals
- anti-farming limits

### 6. Settlement and trust layer

The broader concept includes escrow, bonds, validation, and dispute resolution, but these are not yet defined precisely enough to implement.

### 7. Chatbot-to-network bridge

Alkaest Chatbot introduces a practical commercial wedge that is not yet represented in the protocol roadmap.

The project needs to define how centralized chatbot records can later map into protocol-native concepts without making the core protocol scheduling-specific.

Important bridge concepts:

- establishments as future Spaces
- business owners and professionals as future Identities or Members
- services as Objects
- appointments as booking or WorkItem-like Objects
- booking and cancellation changes as Events
- admin commands as Decisions or privileged Events
- completed appointments as Evidence
- provider reliability as future reputation input

This should become a future service scheduling workflow module after enough operational learning exists.

### 8. Security and trust assumptions

The project still needs a more explicit treatment of:

- sybil resistance
- colluding validators
- spam and griefing
- malicious evidence submission
- replay and signature abuse
- mailbox abuse
- appointment privacy and consent for service-domain evidence

### 9. Future node profiles

The MVP is full-node-first, but the longer-term architecture still needs a place for:

- light clients
- selective sync
- embedded or mobile nodes
- trust assumptions for partial replication

This should remain future work until the full-node model is stable.

### 10. Node API and integrations

The node-first model is established, but the practical interface still needs:

- command definitions
- query contracts
- stream semantics
- local auth rules
- integration configuration shape

---

## Recommended RFC sequence

### Phase 1: Stabilize the protocol foundation

#### RFC-0003: Development Workflow Module

Define:

- `WorkItem` lifecycle
- evidence attachment points
- project integration expectations
- GitHub mapping boundaries
- first practical workflow for open-source development
- how donations to Alkaest become funded issues for Alkaest contributors

Why now:
It is the first real domain and the next planned RFC in the current repo process.

#### RFC-0004: Envelope, Canonical Encoding, and Object IDs

Define:

- canonical serialization
- hash rules
- signature rules
- object and envelope ID derivation
- envelope validation flow

Why now:
Everything replicated on the network depends on deterministic encoding.

#### RFC-0005: Object/Event Semantics and State Resolution

Define:

- event ordering
- object versioning
- replay rules
- deterministic projections
- invalid-state handling

Why now:
Nodes need consistent state convergence before implementation gets too deep.

### Phase 2: Define the trust and market layer

#### RFC-0006: Reputation Proofs and Scoring

Define:

- contribution proof schema
- domain scoring
- decay
- negative signals
- anti-farming rules

#### RFC-0007: Validation and Dispute Resolution

Define:

- validator eligibility
- validation evidence
- dispute triggers
- mediator selection
- finality

#### RFC-0008: Escrow, Bonds, and Settlement

Define:

- reward escrow
- bond rules
- fee routing
- payout outcomes
- slash conditions

#### Future RFC: Service Scheduling Workflow Module

Define:

- provider spaces
- professional membership
- service catalog objects
- appointment or booking lifecycle
- customer and provider messages
- admin decisions
- appointment completion evidence
- cancellation and no-show evidence
- privacy boundaries for appointment-derived records
- mapping from Alkaest Chatbot records into protocol objects and events

Why later:
The chatbot should first prove the operational workflow with real clients.
The protocol should standardize durable concepts after the product has evidence, not before.

### Phase 3: Make the ecosystem usable

#### RFC-0009: Node API and SDK Contract

Define:

- commands
- queries
- streams
- auth model
- error model
- idempotency expectations

#### RFC-0010: Attachments, Privacy, and Data Availability

Define:

- blob storage expectations
- encryption boundaries
- integrity guarantees
- retention

#### RFC-0011: Permissions and Capability Model

Define:

- space-level permissions
- module-specific capabilities
- role interpretation rules

#### RFC-0012: Governance and Versioning

Define:

- protocol upgrade process
- schema evolution strategy
- standard module process
- RFC acceptance expectations

---

## Decisions that still need explicit answers

### What is the practical MVP deliverable?

The project should make this explicit:

- a protocol plus reference node
- a developer workflow app backed by the node
- a project coordination system for open-source maintainers
- a self-hosted coordination flow for the Alkaest project itself

Recommendation:
Pick one crisp MVP outcome and use it to evaluate every RFC.

### What is the first settlement model?

The current concept mentions crypto payments and escrow, but the first implementation still needs a simpler decision:

- manual settlement
- signed off-protocol settlement records
- escrow-ready protocol records without on-chain execution
- full on-chain settlement

This should be decided in the context of the first real funding flow:
donations to Alkaest being allocated across `alkaest-network` issues and paid out to Alkaest contributors.

### How open is the first validation model?

The project still needs to decide whether MVP validation is:

- project-declared and curated
- open to any qualified participant
- hybrid

### How much protocol responsibility should AI agents have?

Recommendation:
Keep agents advisory and node-local first.
Do not treat them as separate trust roots in the MVP.

### How does Alkaest Chatbot influence the protocol roadmap?

Recommendation:
Treat Alkaest Chatbot as a commercial bootstrap product and future domain-learning source.
Do not let WhatsApp, Baileys, Google Calendar, or appointment scheduling leak into the protocol core.

The protocol should later define service scheduling through a module RFC once the chatbot has proven:

- provider profile requirements
- service catalog requirements
- booking lifecycle requirements
- privacy constraints
- useful reputation evidence
- discovery behavior through the WhatsApp admin number

### Will identity assurance be part of the first workflow?

The long-term concept includes optional assurance tiers, but the MVP still needs a simpler answer:

- no assurance layer initially
- project-defined optional assurance metadata
- first-class assurance requirements in the workflow module

### Should blockchain anchoring exist in the first protocol versions?

The concept is compatible with future anchoring, but the project still needs to decide whether early RFCs should:

- ignore anchoring completely
- reserve fields for future anchoring
- define checkpoint structures early without requiring implementation

---

## Immediate next work

1. Refine RFC-0005 against RFC-0001 through RFC-0004.
2. Define how donations to Alkaest are represented and allocated to `alkaest-network` issues.
3. Define `.alkaest/project.yaml` for project integration.
4. Write RFC-0006 Reputation Proofs and Scoring.
5. Map Alkaest Chatbot records to future protocol Evidence and service scheduling objects.
6. Add more diagrams for workflow state, evidence flow, funding flow, validation flow, and chatbot-to-network progression.

---

## Exit criteria for planning maturity

Planning is likely strong enough to support serious implementation when these are all true:

- workflow objects and transitions are explicit
- envelopes are deterministic
- state convergence rules are explicit
- evidence and validation are machine-readable
- settlement outcomes are representable
- node API contracts are stable enough for one client implementation
