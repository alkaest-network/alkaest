# Alkaest

Alkaest is a decentralized protocol for coordinating work through verifiable reputation, cryptographic identities, and local user-run nodes.

The project is protocol-first and currently focused on a desktop-first MVP for open-source development coordination.
The long-term goal is a broader coordination layer for work where reputation becomes a portable, evidence-based credential.

## What Alkaest is trying to build

Alkaest aims to make it possible for people and organizations to coordinate work without relying on centralized platforms as the source of truth.

In practical terms, that means:

- participants run their own local nodes
- identities are cryptographic and self-controlled
- work history is represented by verifiable evidence
- reputation is built from outcomes, not platform-owned profiles
- workflow integrations such as GitHub stay outside the protocol core

## Current direction

The repository currently defines the early architecture and planning layers:

- [Vision](docs/overview/vision.md)
- [Glossary](docs/overview/glossary.md)
- [Roadmap](docs/overview/roadmap.md)
- [Chatbot-to-Network Strategy](docs/overview/chatbot-to-network-strategy.md)
- [Chatbot-to-Network Diagram](docs/diagrams/chatbot-to-network.md)
- [RFC-0001 Protocol Core](docs/rfc/0001-protocol-core.md)
- [RFC-0002 Node Architecture](docs/rfc/0002-node-architecture.md)

## Commercial bootstrap path

Alkaest also has a near-term commercial wedge: Alkaest Chatbot.

The chatbot is a WhatsApp scheduling assistant for local service providers such as barbershops, dentists, doctors, salons, and clinics.
Its job is to generate revenue, validate real coordination needs, and create operational evidence before the decentralized network is ready.

The intended sequence is:

- start with Alkaest Chatbot as a practical scheduling product
- grow a base of paying providers
- add a public WhatsApp discovery number where people can search for professionals already in that provider base
- progressively map proven scheduling, discovery, and reputation concepts into the Alkaest protocol

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
