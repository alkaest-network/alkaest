# Network Rollout Plan

## Purpose

Go from one node on a laptop to a network running across continents, on phones, weak machines and strong servers (ADR-0003), without betting on untested assumptions. Each phase has exit criteria; the next phase starts only when they are met.

---

## Phase 0 — Single local node

* One Standard node on a desktop, with CLI and local API.
* Identities and keys, signed envelopes, a space with a hash-linked event log, deterministic replay (RFC-0004, RFC-0005).

Exit: a space's state can be rebuilt from its log on a fresh machine, byte for byte.

## Phase 1 — Local multi-node network (one machine)

* 5 to 10 nodes in containers on one machine, including resource-capped nodes that imitate phones and weak machines (CPU, memory and bandwidth limits) and one Service node.
* Peer discovery, gossip, partial replication, mailbox, capability advertisement and role selection.
* Fault injection: kill nodes, partition the network, corrupt envelopes, replay old envelopes.
* Token and payment prototypes, if any, only against Bitcoin `regtest` and a local Lightning network (ADR-0004).

Exit: every node converges to the same state for the spaces it replicates; tampered or replayed envelopes are rejected everywhere; a capped "phone" node works through a relay.

## Phase 2 — Real devices on real networks

* A home mini PC (Standard), a laptop on another network, an Android phone (Light), all behind ordinary NATs.
* NAT traversal (hole punching, relays) and intermittent connectivity (phone offline for hours, then catches up).

Exit: the phone can publish, receive and verify updates after going offline; no manual port forwarding.

## Phase 3 — Global testnet

* Service and Standard nodes in several regions (for example Brazil, Europe, North America, Asia) on low-cost servers, plus volunteers' machines.
* Latency, churn and bandwidth measurements; search (alkaest-search.md, stage 3) across regions.
* Anchoring of space logs to Bitcoin `signet` or mainnet timestamps.

Exit: sync and search latency within targets across continents; the network survives losing any single region and any single Service node.

## Phase 4 — First real users

* Alkaest Chatbot providers become network providers: their chatbot talks to their own node; the chatbot operator runs Service nodes at first, later others join.
* Alkaest Search stays stealth until the launch gate (alkaest-search.md).

Exit: real appointments produce signed evidence and reputation that any node can verify.

---

## Cross-Cutting Rules

* **Every phase runs the same validation**; only scale and environment change.
* **No central component is required** in any phase; operator-run Service nodes are convenience, never authority.
* **Observability from Phase 1**: per-node metrics (peers, sync lag, rejected envelopes, storage, bandwidth) exported in a standard format, without personal data.
* **Phones are first-class from Phase 1** (as capped containers), not an afterthought in Phase 4.
