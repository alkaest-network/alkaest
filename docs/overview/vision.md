# Vision

## Purpose

Alkaest is a decentralized coordination protocol for work.
It is designed to let individuals, teams, and organizations coordinate work without relying on centralized intermediaries, while preserving trust through cryptographic identity, verifiable history, and portable reputation.

The first concrete domain is open-source development coordination.
The longer-term ambition is broader: design, automation, maintenance, delivery, and other service markets where reputation can function as a primary credential.

---

## Core principles

### Decentralized coordination

Work coordination should not depend on a central authority.
Protocol participants operate nodes that discover, evaluate, and synchronize work.

### Verifiable reputation

Reputation should come from evidence, not from subjective ratings or platform-owned profiles.

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
In the MVP, each developer runs a local full node on their own machine.

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

The exact machine-readable scoring model still belongs in later RFCs.

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

In the current direction, agents are assistants to node operators rather than new sources of protocol authority.

---

## Economic trust direction

The broader concept includes an economic security layer with:

- reward escrow
- requester bonds
- worker bonds
- validator compensation
- mediator incentives

The exact settlement model is still undecided.
Those details should be defined through later RFCs rather than treated as settled design.

The broader concept also leaves room for:

- validation tiers based on task complexity
- optional blockchain anchoring for auditability
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

This self-hosting path is important because it forces the protocol to prove its value on a real project before expanding to other teams.

The longer-term protocol direction also anticipates:

- validation by qualified participants
- dispute resolution for contested work outcomes
- evidence-driven reputation growth over time

---

## Commercial bootstrap path

Alkaest also has a near-term commercial bootstrap path through Alkaest Chatbot.

Alkaest Chatbot is a WhatsApp scheduling assistant for local service providers such as barbershops, dentists, doctors, salons, and clinics.
It can start as a centralized product because its immediate purpose is revenue, real customer learning, and operational proof.

The strategic sequence is:

```text
Alkaest Chatbot -> WhatsApp Discovery Number -> Alkaest Network
```

In this path:

- the chatbot helps providers manage appointment scheduling through WhatsApp
- a later discovery number lets customers search for professionals already in the provider base
- appointment, cancellation, completion, and provider reliability records become candidates for future protocol Evidence
- provider profiles and service catalogs can later map to Alkaest Spaces, Identities, Objects, Events, Messages, Decisions, and Evidence

This path does not change the protocol core.
The core must remain generic enough to support multiple coordination domains.

Service scheduling should become a future domain module after the chatbot product proves which records, workflows, privacy constraints, and reputation signals matter in practice.

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

The long-term idea is that reputation becomes a portable, evidence-based credential for participating in these markets.

---

## Status

This vision is intentionally conceptual.
The implementation path should continue to move from vision into precise RFCs, starting with the protocol core, node architecture, and first workflow module.
The first workflow should be strong enough to coordinate Alkaest's own development.
