# ADR-0005 - Cross-Platform App and Deployment Modes

**Status:** Accepted
**Date:** 2026-10-18
**Decision Type:** Product and Architecture
**Related:** ADR-0001, ADR-0002, ADR-0003, RFC-0002 §7.1 and §16

---

## Context

Alkaest needs one user-facing application for business owners (and later their customers) that works on any platform: Android, iOS, macOS, Windows, Linux and the web.

The operator wants the same app to serve every way of running Alkaest:

* use the app itself as a node;
* connect the app to a node running on a machine the owner controls, optionally with a local AI that acts as a chatbot and as a way to run the business;
* pay the operator to run the node and the AI, with the app behaving exactly the same.

ADR-0003 already defines the node profiles (Light, Standard, Service) and a Rust node core. The first node, `alkaest-node`, reached Phase 0 with a Rust protocol library (`alkaest-core`) and a CLI.

Constraints that shape the decision:

* Phones suspend background work (iOS and Android both restrict it), so a phone cannot be relied on to answer customers 24 hours a day.
* The current local model (qwen3:4b-instruct through Ollama) needs about 4 GB of free memory to stay loaded. Running it on a phone is slow and drains the battery.
* Determinism depends on byte-identical canonical JSON, hashing and signing. Reimplementing the protocol in a second language risks two implementations that disagree.

---

## Decision

### 1. One Flutter app, with the protocol core in Rust

The app is written in **Flutter** for every platform. The protocol is **not** reimplemented in Dart: `alkaest-core` is compiled into the app through `flutter_rust_bridge`, so validation, signing and state resolution run the same code on the phone, the desktop and the server.

Dart owns only the interface and the platform integration.

### 2. Three deployment modes, one API

In every mode, the app talks to a node through the same **Local API** (RFC-0002 §7.1).

| Mode | Where the node runs | Node profile | Typical user |
|---|---|---|---|
| **Embedded** | Inside the app | Light on phones; Standard on desktops | Trying Alkaest, very small businesses, customers |
| **Self-hosted** | On a machine the owner controls, with the local AI and the WhatsApp adapter | Standard | Owners who want full control |
| **Hosted** | On the operator's infrastructure, as a paid service | Standard or Service | Owners who want nothing to manage |

Hosted and self-hosted are the same software. The only difference is who operates the machine, so a business can move between them by exporting and importing its spaces. The Phase 0 exit criterion (rebuild state from the log, byte for byte) is what makes this move safe.

### 3. Phones are Light nodes, not the business's always-on node

A phone running the embedded node stores and signs its owner's data and validates what it receives. It is **not** the node that answers customers around the clock.

A business that needs 24-hour availability (the chatbot, bookings arriving at night) runs a self-hosted or hosted node. The app on the phone then connects to it.

### 4. The AI and the channel adapters run next to the node

The local model, the WhatsApp adapter and other channel adapters run on the node's machine, never inside the app. The app is the interface for the conversation and for running the business: agenda, services, messages and settings.

**Recommended minimum machine for self-hosting with local AI:** a mini PC with 16 GB of RAM, for example an Intel N100-class machine. The model stays loaded in memory (Ollama `keep_alive=-1`), so replies take a few seconds.

Nodes without the AI can run on weaker hardware, as ADR-0003 allows.

### 5. Pairing by key, not by password

The app owns an Ed25519 identity, the same identity model as the protocol (RFC-0004).

To connect the app to a node, the node shows a pairing code (a QR code) and authorizes the app's public key. From then on, every Local API request is signed by the app's key and checked by the node. A request without a valid signature from an authorized key is rejected.

The same flow works for self-hosted and hosted nodes, and there is no password to leak. Revoking a device revokes its key.

---

## Consequences

### Positive

* One codebase for every platform, and a single protocol implementation.
* Moving between hosted and self-hosted needs no changes to the app.
* The hosted offer is a revenue path that does not lock customers in.
* Phones take part in the network without being trusted for availability.

### Negative

* Rust and Flutter both enter the toolchain, and the bridge adds build complexity, especially for iOS and web.
* The web build cannot embed a full node (no persistent background process or raw sockets). On the web, the app runs only in connect mode.
* The scheduling logic of Alkaest Chatbot lives today in Spring Boot and Postgres. For "the same behavior in every mode" it must become a protocol module (like `work_item`), with appointments as objects and changes as events. This is the largest piece of work in this ADR.

### Amendment to ADR-0001

ADR-0001 keeps the MVP desktop-first and free of light-client requirements. This ADR does not change the MVP scope of the development workflow: the Standard node still comes first. It adds the Flutter app and the Light embedded mode as the next product surface, consistent with ADR-0003.

---

## Implementation Order

1. **Local API** in `alkaest-node`: HTTP with a server-sent event stream, requests authenticated by signature, and device pairing (RFC-0009).
2. **Flutter app, connect mode**: pairing and protocol-backed coordination views against a self-hosted node.
3. **Scheduling module and backend pilot**: RFC-0007 is now Draft. Move Alkaest Chatbot's booking rules through the node Local API into provider-private Spaces, then validate privacy, deterministic replay, idempotent retries, and independent multi-node state before presenting network-derived reputation in a frontend.
4. **Service screens in the Flutter app**: expose provider agenda/services only after the service-domain backend gate passes; make post-service feedback optional and clearly disclosed. Reputation remains behind RFC-0006's integrity and privacy launch gate.
5. **Embedded mode**: `alkaest-core` inside the app through `flutter_rust_bridge`; a Light node on phones and a Standard node on desktops.
6. **Hosted offer**: operator-run nodes with the same software, plus export and import between modes.

---

## Open Questions

* Local API transport over the internet for self-hosted nodes behind NAT: relay through hosted nodes, libp2p relay, or Tor (ADR-0003). This is decided in Phase 1.
* Pricing and terms of the hosted offer.
* Whether customers (not only business owners) get the app in the first release, or only the WhatsApp channel.
