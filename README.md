# Alkaest

Alkaest is a decentralized protocol for coordinating work through verifiable reputation, cryptographic identities, and local user-run nodes.

[Contribute to Alkaest](contribute.html) · [Contribution guidelines](CONTRIBUTING.md) · [Open issues](https://github.com/alkaest-network/alkaest/issues)

[Documentation index](docs/README.md) · [Roadmap and launch gates](docs/overview/roadmap.md) · [Current state](docs/handoff/current-state.md)

[Alkaest visual identity](docs/brand/visual-identity.md)

The project is protocol-first and currently focused on a desktop-first MVP for open-source development coordination.
The long-term goal is a broader coordination layer for work where domain-specific reputation may become a portable, evidence-based credential. Reputation is under design and is not a production guarantee.
Longer term, Alkaest may also give independent professionals an opt-in operating dashboard over interoperable open-source tools and help independent projects coordinate their own budgets and DAO-like governance. These are expansion directions, not current product capabilities.

Interested in contributing? Start with the [contribution guide](CONTRIBUTING.md), read the [Code of Conduct](CODE_OF_CONDUCT.md), and browse [open issues](https://github.com/alkaest-network/alkaest/issues).

## What Alkaest is trying to build

Alkaest aims to make it possible for people and organizations to coordinate work without relying on centralized platforms as the source of truth.

In practical terms, that means:

- participants run their own local nodes
- identities are cryptographic and self-controlled
- work history is represented by verifiable evidence
- reputation is built from outcomes, not platform-owned profiles
- workflow integrations such as GitHub stay outside the protocol core

## Current direction

The protocol repository is separate from the node, app, and other component repositories. See the [repository map and access notes](CONTRIBUTING.md#choose-a-repository) before starting implementation work.

The repository currently defines the early architecture and planning layers. The [documentation index](docs/README.md) lists every document with its maturity.

Overview:

- [Vision](docs/overview/vision.md)
- [Glossary](docs/overview/glossary.md)
- [Roadmap](docs/overview/roadmap.md)
- [Chatbot-to-Network Strategy](docs/overview/chatbot-to-network-strategy.md)
- [Chatbot-to-Network Diagram](docs/diagrams/chatbot-to-network.md)
- [Alkaest Search](docs/overview/alkaest-search.md)
- [Network Rollout Plan](docs/overview/network-rollout-plan.md)

Protocol specifications (all Draft):

- [RFC-0001 Protocol Core](docs/rfc/0001-protocol-core.md)
- [RFC-0002 Node Architecture](docs/rfc/0002-node-architecture.md)
- [RFC-0003 Development Workflow Module](docs/rfc/0003-development-workflow-module.md)
- [RFC-0004 Envelope, Canonical Encoding, and Object IDs](docs/rfc/0004-envelope-canonical-encoding-and-object-ids.md)
- [RFC-0005 Object/Event Semantics and State Resolution](docs/rfc/0005-object-event-semantics-and-state-resolution.md)
- RFC-0006 Reputation Proofs and Integrity (planned, not yet written)
- [RFC-0007 Service Scheduling Module](docs/rfc/0007-service-scheduling-module.md)
- [RFC-0008 Bitcoin Escrow and Settlement](docs/rfc/0008-bitcoin-escrow-and-settlement.md)
- [RFC-0009 Node API and SDK Contract](docs/rfc/0009-node-api-and-sdk-contract.md)
- [RFC-0013 Validation, Dispute Resolution, and Appeals](docs/rfc/0013-validation-dispute-resolution-and-appeals.md)
- [RFC-0014 Treasury Agent and Release Authorization](docs/rfc/0014-treasury-agent-and-release-authorization.md)

Architecture decisions ([decision index](docs/decisions/README.md)):

- [ADR-0001 Desktop-First MVP](docs/decisions/ADR-0001-desktop-first-mvp.md)
- [ADR-0002 Chatbot Commercial Wedge](docs/decisions/ADR-0002-chatbot-commercial-wedge.md)
- [ADR-0003 Heterogeneous Nodes and Network Validation](docs/decisions/ADR-0003-heterogeneous-nodes-and-network-validation.md)
- [ADR-0004 Token and Settlement Direction](docs/decisions/ADR-0004-token-and-settlement-direction.md)
- [ADR-0005 Cross-Platform App and Deployment Modes](docs/decisions/ADR-0005-cross-platform-app-and-deployment-modes.md)
- [ADR-0006 Self-Funding Treasury, Task Bounties with Random Mediation, and the Maintainer Agent](docs/decisions/ADR-0006-self-funding-treasury-and-maintainer-agent.md)
- [ADR-0007 Autonomous Treasury and Bitcoin Audit Trail](docs/decisions/ADR-0007-autonomous-treasury-and-bitcoin-audit.md)
- [ADR-0008 Token Design Before Issuance](docs/decisions/ADR-0008-token-design-before-issuance.md)
- [ADR-0009 Resource-Aware Node Capacity and Deployment (Proposed)](docs/decisions/ADR-0009-resource-aware-capacity-and-deployment.md)

Selected research:

- [Bisq DAO and Alkaest Token Research](docs/research/bisq-dao-and-alkaest-token.md)
- [Reputation Integrity Threat Model](docs/research/reputation-integrity-threat-model.md)
- [Bisq May 2026 Incident and Alkaest Mitigations](docs/research/bisq-may-2026-incident-and-alkaest-mitigations.md)

## Commercial bootstrap path

Alkaest also has a near-term commercial wedge: Alkaest Chatbot.

The chatbot is a WhatsApp scheduling assistant for local service providers such as barbershops, dentists, doctors, salons, and clinics.
Its job is to generate revenue, validate real coordination needs, and create operational evidence before the decentralized network is ready.
Production messaging should use the official WhatsApp Business Platform API. Provider billing is usage-based, with WhatsApp/provider charges and Alkaest's variable service costs shown separately; exact rates and WABA ownership remain open.

The intended sequence is:

- start with Alkaest Chatbot as a practical scheduling product
- grow a base of paying providers
- integrate the chatbot with provider-private Alkaest Spaces behind the existing interface and validate the backend on an isolated, multi-node test network
- only after the backend passes its privacy, determinism, and replication gates, add a public discovery experience
- introduce any reputation interface only after the anti-manipulation and privacy launch gates of RFC-0006 (planned, not yet written)

Service completion, customer feedback, and reputation are distinct. Completion recorded by a provider is not independent proof of quality; a WhatsApp rating relayed by the integration is not a cryptographic customer signature. Feedback is optional and disclosed, while free-text comments remain private by default.

The protocol core should remain generic.
It should not become WhatsApp-specific, Google Calendar-specific, or scheduling-only.

## First network project

The first project intended to live on the Alkaest network is Alkaest itself.

That means the protocol should bootstrap on a real open-source project before trying to generalize outward.
In practice, the plan is that:

- the `alkaest-network` project is the first project coordinated through Alkaest
- issues in `alkaest-network` become the first real work items on the network
- money donated to Alkaest is routed into those issues
- developers contributing to Alkaest are paid through the same issue-based coordination flow the protocol is meant to support

This gives the network an initial self-hosting path: Alkaest helps fund and coordinate the development of Alkaest.

The initial candidate backlog includes professional brand identity work and bounded Flutter app tasks; these are not promised or funded bounties. The founder sets initial priorities and budget boundaries. The Brain then selects which eligible issue to open and proposes its BTC bounty using provenance-labeled metrics, reports, contributor feedback, complaints, permitted quotes/rates, and a deterministic verified treasury balance. A signed policy gate enforces the reserve and spending limits; uncertain or unsupported decisions are deferred or escalated. See [ADR-0007](docs/decisions/ADR-0007-autonomous-treasury-and-bitcoin-audit.md) and [RFC-0014](docs/rfc/0014-treasury-agent-and-release-authorization.md).

The intended initial payment asset for contributors is BTC through Alkaest's funded-work flow. A contributor may choose to use Bisq separately to seek a peer-to-peer BTC-to-fiat trade; Alkaest does not process or guarantee that conversion. The settlement rail and fee/quote rules remain subject to RFC-0008 and the treasury launch gates. See [Bitcoin payout and Bisq conversion research](docs/research/bitcoin-payouts-and-bisq-conversion.md).

## Inspiration from Bisq 2

Alkaest is strongly inspired by the architectural direction of Bisq 2, especially its node-first approach where users run the application locally and participate directly in a peer-to-peer network rather than depending on a central operator.

That inspiration shows up in a few ways:

- the local node is the primary protocol boundary
- the network is peer-to-peer instead of platform-centric
- external services are treated as integrations, not authorities
- the product is designed around user sovereignty and local control

The key difference is scope.
Bisq 2 is focused on peer-to-peer exchange protocols, while Alkaest is exploring peer-to-peer coordination of work, evidence, validation, settlement, and reputation.

Helpful Bisq 2 references:

- [Bisq 2 beta announcement](https://bisq.network/bisq-2)
- [Bisq Easy overview](https://bisq.network/bisq-easy)
- [Bisq 2 mobile architecture notes](https://bisq.wiki/Bisq_2_mobile)

## Origin

[WHITEPAPER.md](WHITEPAPER.md) is the conceptual origin document written before the current architecture was defined.
It captures the initial ideas and motivations behind Alkaest.
The `docs/` folder is the living specification that has evolved from it.

## Status

This repository contains early protocol research, RFCs, diagrams, and planning documents.

Implementation should stay exploratory until the protocol core, workflow module, and state rules are specified more precisely.
The clearest first real-world target is to fund Alkaest development itself through issue-based coordination on the network.
