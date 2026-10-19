# ADR-0003 - Heterogeneous Nodes and Network Validation

**Status:** Proposed
**Date:** 2026-10-18
**Decision Type:** Protocol Architecture
**Amends:** ADR-0001 (desktop-first MVP), RFC-0002 §4.3

---

## Context

ADR-0001 and RFC-0002 define a desktop full node as the only node type of the MVP and explicitly exclude mobile nodes and light clients.

The target network is broader. It must run across the world, on:

* a phone, possibly offline for hours, on mobile data, behind carrier NAT;
* a weak machine (old laptop, Raspberry Pi, mini PC) with little storage and an unstable home connection;
* a strong server with a public IP, large disks and plenty of bandwidth.

All of them must take part in the same network, and stronger machines should contribute more without the network depending on them.

The operator also wants the network to validate everything, without a central authority, in the spirit of Bisq.

---

## Decision

### 1. One protocol, several node profiles

Every node speaks the same protocol and validates everything it accepts. Nodes differ in **what they store and serve**, not in what they trust.

| Profile | Typical device | Stores | Serves |
|---|---|---|---|
| **Light** | Phone, browser | Own identities and keys, own spaces, data it asked for | Nothing to others; connects through relays |
| **Standard** | Desktop, mini PC, Raspberry Pi | Full history of spaces it participates in, plus a configurable share of other spaces | DHT routing, replicas, mailbox for its identities |
| **Service** | Server with public IP | Large replica share, indexes, archives | Search indexing, relay (NAT traversal), bootstrap, archival, mailbox for light nodes |

A node measures its own resources (storage, memory, CPU, bandwidth, uptime, reachability) and takes on roles automatically, within limits set by its operator. A phone never becomes a relay; a server that stays reachable for weeks can volunteer as indexer and relay.

Service nodes are an optimisation, never an authority: anything they serve is signed by its author and verified by the receiver, and a light node queries several service nodes so that one cannot hide data.

### 2. "The network validates everything" without a blockchain

Most Alkaest facts do not need global agreement. They need to be **authentic, ordered within their space and reproducible**:

| Layer | What is checked | Who checks |
|---|---|---|
| Envelope | Signature, canonical encoding, schema (RFC-0004) | Every node, for everything it accepts, including light nodes |
| Space state | Deterministic replay of the space's event log (RFC-0005): permissions, ordering, state transitions | Every node that replicates the space |
| Derived facts | Reputation, search ranking: recomputed from signed evidence with deterministic rules | Any node that wants to; results are verifiable, not trusted |
| Global uniqueness / value | Things that cannot be double-spent (balances, escrow, names) | Deferred; anchored to an external settlement layer when needed (see ADR-0004) |

Each space keeps a hash-linked, signed event log. Logs can be periodically **anchored** to Bitcoin (for example with OpenTimestamps) so that history cannot be rewritten later, without running a chain.

This avoids building a blockchain, which would force every node, including phones, to agree on every fact in the world.

### 3. Privacy by architecture

Personal data stays on the node that owns it. The network carries signed, pseudonymous facts: provider listings are public business data; customers appear as per-space pseudonyms; queries can be routed through relays or Tor so that searching does not reveal who searches.

### 4. MVP scope

The first implementation still builds the **Standard** profile on a desktop (ADR-0001 stands for the implementation order). What changes is that the architecture must not assume every node is a full desktop node:

* node APIs and sync are designed for partial replication from day one;
* capability advertisement and role selection exist in the protocol, even if only one role is implemented first;
* the light profile is the second implementation target, not a someday item.

### 5. Reference technology (proposed)

* Node core in **Rust**: runs on phones (via UniFFI), ARM boards and servers with one codebase and a small footprint.
* **libp2p**: QUIC and TCP transports, Kademlia DHT for discovery, gossipsub for propagation, AutoNAT, hole punching and circuit relay v2 for nodes behind NAT. An optional Tor transport, as in Bisq.
* Storage: SQLite for light and standard nodes, an embedded key-value store (RocksDB) for service nodes.
* Integrations such as Alkaest Chatbot stay outside the node and talk to its local API (RFC-0002 §5.2).

---

## Consequences

Positive:

* The same network works for a barber's phone, a home mini PC and a data-center server.
* Trust does not depend on big nodes; they only make the network faster.
* No blockchain to bootstrap, secure or pay for before there is a reason to move value.

Negative:

* Partial replication and multi-source queries are harder to build than "everyone stores everything".
* Sybil resistance (fake identities inflating reputation) is not solved by signatures alone; it must be addressed in the reputation RFC (RFC-0006), for example by weighting evidence by the counterparty's own history and age.
* A Rust node core means the Java chatbot integrates through an API, not by sharing code.

---

## Follow-up

* Update RFC-0002 with node profiles and capability advertisement (done alongside this ADR).
* RFC-0006 (reputation proofs) must define verifiable recomputation and Sybil weighting.
* RFC-0009 (node API) must expose partial replication and capability queries.
