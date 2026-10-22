# ADR-0003 - Heterogeneous Nodes and Network Validation

**Status:** Accepted direction; reference technology choices remain proposed
**Date:** 2026-10-18
**Decision Type:** Protocol Architecture
**Amends:** ADR-0001 (desktop-first MVP), RFC-0002 §4.3

---

## Context

Earlier versions of ADR-0001 and RFC-0002 focused on a desktop full node as the only MVP node type and deferred mobile/light profiles. This ADR supersedes that full-node-only assumption while preserving desktop as the first implementation target; RFC-0002 now specifies the three profiles and their shared validation boundary.

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

### 2. Protocol validation without a chain; treasury audit on Bitcoin

Most Alkaest facts do not need global agreement. They need to be **authentic, ordered within their space and reproducible**:

| Layer | What is checked | Who checks |
|---|---|---|
| Envelope | Signature, canonical encoding, schema (RFC-0004) | Every node, for everything it accepts, including light nodes |
| Space state | Deterministic replay of the space's event log (RFC-0005): permissions, ordering, state transitions | Every node that replicates the space |
| Derived facts | Reputation, search ranking: recomputed from signed evidence with deterministic rules | Any node that wants to; results are verifiable, not trusted |
| Global uniqueness / value | Things that cannot be double-spent (balances, escrow, names) | Deferred; anchored to an external settlement layer when needed (see ADR-0004) |

Signatures authenticate the author but do not make payloads safe or true. Every node MUST validate field bounds, units, authority, state preconditions, and cross-field invariants before applying an event. Economic transitions require independent derivation from verified settlement facts and atomic application; malformed inputs fail without partial state changes. RFC-0014 defines treasury-specific requirements.

Each space keeps a hash-linked, signed event log. The Alkaest protocol does not use a blockchain as its consensus or state-validation mechanism. For treasury and settlement, however, ADR-0007 requires Bitcoin transactions and periodic commitments to the signed treasury/workflow log. This gives public evidence of funds moved and log commitments without making every node agree on every fact in the world.

This avoids building a custom Alkaest blockchain, which would force every node, including phones, to agree on every fact in the world.

### 3. Privacy by architecture

Personal data stays on the node that owns it. The network carries signed, pseudonymous facts: provider listings are public business data; customers appear as per-space pseudonyms; queries can be routed through relays or Tor so that searching does not reveal who searches.

Future mobile evidence capture does not make device sensors protocol truth. Photos, precise coordinates, and location metadata remain off-chain and access-controlled; the protocol records what source produced an evidence claim and which policy accepted it. Commodity-device location signals may be spoofed, so location assurance requires task-specific, risk-based corroboration and a dispute path. See the [mobile evidence and location research](../research/mobile-work-evidence-and-location-assurance.md).

### 4. MVP scope

The first implementation still builds the **Standard** profile on a desktop (ADR-0001 stands for the implementation order). What changes is that the architecture must not assume every node is a full desktop node:

* node APIs and sync are designed for partial replication from day one;
* capability advertisement and role selection exist in the protocol, even if only one role is implemented first;
* the light profile is the second implementation target, not a someday item.

### 5. Reference technology (proposed)

* Node core in **Rust**: runs on phones (via UniFFI), ARM boards and servers with one codebase and a small footprint.
* **libp2p**: QUIC and TCP transports, Kademlia DHT for discovery, gossipsub for propagation, AutoNAT, hole punching and circuit relay v2 for nodes behind NAT. An optional Tor transport, as in Bisq. Adopted in the reference node for Phase 1: TCP/QUIC, Noise, Yamux, a request-response sync protocol and gossipsub announcements (RFC-0002 §6.6.1); discovery, NAT traversal and relays are not implemented yet.
* Storage: SQLite for light and standard nodes, an embedded key-value store (RocksDB) for service nodes.
* Integrations such as Alkaest Chatbot stay outside the node and talk to its local API (RFC-0002 §5.2).

---

## Consequences

Positive:

* The same network works for a barber's phone, a home mini PC and a data-center server.
* Trust does not depend on big nodes; they only make the network faster.
* No custom blockchain is needed for protocol validation. Bitcoin adds cost and operational dependencies only to treasury functions that actually move value.

Negative:

* Partial replication and multi-source queries are harder to build than "everyone stores everything".
* Sybil resistance (fake identities inflating reputation) is not solved by signatures alone. RFC-0006 must address evidence independence, self-dealing, collusion, and privacy tradeoffs before reputation affects consequential outcomes; identity age or counterparty history alone is not proof of independence.
* A Rust node core means the Java chatbot integrates through an API, not by sharing code.

---

## Follow-up

* Update RFC-0002 with node profiles and capability advertisement (done alongside this ADR).
* RFC-0006 (reputation proofs) must define verifiable recomputation and anti-manipulation controls before consequential reputation use.
* RFC-0009 (node API) must expose partial replication and capability queries.
