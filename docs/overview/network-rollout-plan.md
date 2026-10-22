# Network Rollout Plan

## Purpose

Go from one node on a laptop to a network running across continents, on phones, weak machines and strong servers (ADR-0003), without betting on untested assumptions. Each phase has exit criteria; the next phase starts only when they are met.

---

## Phase 0 — Single local node

* One Standard node on a desktop, with CLI and local API.
* Identities and keys, signed envelopes, a space with a hash-linked event log, deterministic replay (RFC-0004, RFC-0005).
* Simulated treasury policy, funded WorkItems, PR/CI evidence, release decisions, and Bitcoin treasury/audit flows on `regtest` (RFC-0014).
* Adversarial inputs: malformed-but-signed messages, negative/overflow values, replay, inconsistent transaction outputs, invalid authority, and atomic no-mutation-on-failure checks (Bisq incident research).

Exit: a space's state can be rebuilt from its log on a fresh machine, byte for byte; independent local nodes agree on valid state, reject adversarial inputs without partial mutation, and verify the same simulated treasury decisions and settlement references.

## Phase 1 — Local multi-node network (one machine)

* 5 to 10 nodes in isolated containers on one machine, including resource-capped profiles that imitate phones and weak machines (CPU, memory, storage and bandwidth constraints) and one Service node. This is a test harness for protocol and resource behavior; it does not require Kubernetes or demonstrate independent operators.
* Peer discovery, gossip, partial replication, mailbox, capability advertisement and role selection.
* Fault injection: kill nodes, partition the network, corrupt envelopes, replay old envelopes.
* Valueless token/accounting and payment simulations, if any, only in isolated local environments and Bitcoin `regtest`; no issuance, market, redemption promise, or real-money voting (ADR-0004, ADR-0008).

Exit: every node converges to the same state for the spaces it replicates; tampered or replayed envelopes are rejected everywhere; a capped "phone" node works through a relay.

Status (2026-10-22): the reference node meets these exit checks in a six-container network (`deploy/phase1/` in alkaest-node): a relay Service node, three desktops, a node capped at 0.5 CPU / 256 MiB, and a phone capped at 0.25 CPU / 128 MiB that opens no port. Still open in Phase 1: bandwidth caps and packet loss, wide-area discovery, mailbox, capability advertisement and role selection.

## Phase 2 — Real devices on real networks

* A home mini PC (Standard), a laptop on another network, an Android phone (Light), all behind ordinary NATs.
* NAT traversal (hole punching, relays) and intermittent connectivity (phone offline for hours, then catches up).

Exit: the phone can publish, receive and verify updates after going offline; no manual port forwarding.

## Phase 3 — Global testnet

* Service and Standard nodes in several regions (for example Brazil, Europe, North America, Asia) on low-cost servers, plus volunteers' machines.
* Latency, churn and bandwidth measurements; search (alkaest-search.md, stage 3) across regions.
* Anchoring of space logs to Bitcoin `signet`; mainnet anchors require a separate operational and privacy review.
* Multi-node verification of treasury event commitments against Bitcoin `signet`.

Exit: sync and search latency within targets across continents; the network survives losing any single region and any single Service node.

## Service-domain backend gate

Before adding a protocol/reputation frontend, run Alkaest Chatbot against provider-private Spaces on an isolated network of independent test nodes. Keep the existing chatbot as the customer interface. Begin with synthetic bookings and outcomes; move to real appointment-derived events only after provider/customer notice, opt-in where required, privacy review, and data minimization are in place.

The backend pilot must validate:

* the chatbot writes through the same Local API and protocol rules as other clients;
* schedule/booking event signatures, authorization, replay, retries, and deterministic conflict handling;
* identical reconstructed state on independent nodes, including offline recovery and duplicate webhook/message delivery;
* tenant/Space isolation and that no phone number, name, free-text comment, or sensitive service detail leaks into public replication;
* clear provenance separation among provider-recorded completion, customer-signed feedback, and feedback relayed by the provider's WhatsApp integration;
* consent, withdrawal/retention behavior, and minimized export of any customer-derived evidence;
* no reputation output affecting ranking, funding, access, or authority before RFC-0006 passes its launch gate.

Exit: independent nodes deterministically agree on valid scheduling state, reject malformed or unauthorized events, and preserve the stated privacy boundaries. Only then may the product design a protocol-facing reputation frontend. Passing this gate does not itself make a service claim or rating mature reputation.

## Phase 4 — First real users

* After the service-domain backend gate, Alkaest Chatbot providers may opt in to having the chatbot write to provider-private Spaces. The chatbot operator may run Service nodes at first; providers can later operate their own.
* Alkaest Search stays stealth until the launch gate (alkaest-search.md).

Exit: service-domain records can produce signed, provenance-labeled evidence that nodes verify. Feedback remains optional and separate from completion. Reputation affects ranking, funding, access, or authority only after RFC-0006's anti-manipulation launch gate is met.

---

## Cross-Cutting Rules

* **Every phase runs the same protocol validation**; only scale and environment change. Bitcoin is used for treasury settlement and audit anchoring, not as Alkaest's general consensus mechanism.
* **No central component is required** in any phase; operator-run Service nodes are convenience, never authority.
* **Observability from Phase 1**: per-node metrics (peers, sync lag, rejected envelopes, storage, bandwidth) exported in a standard format, without personal data.
* **Phones are first-class from Phase 1** (as capped containers), not an afterthought in Phase 4.
* **Deployment orchestration is operator-owned.** Kubernetes may manage one operator's services when justified by measured multi-host needs; it is neither a protocol dependency nor evidence that clustered Alkaest nodes are independently administered. See [ADR-0009](../decisions/ADR-0009-resource-aware-capacity-and-deployment.md).
