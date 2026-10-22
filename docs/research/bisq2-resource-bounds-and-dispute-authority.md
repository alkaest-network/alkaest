# Research: Bisq 2 Patterns for Resource Bounds and Conflict Authority

**Status:** Decision support; no Alkaest option has been adopted.
**Date:** 2026-10-19
**Related:** RFC-0002, RFC-0004, RFC-0005, RFC-0008 (Draft), RFC-0013 (Draft), RFC-0014

This note compares patterns documented or proposed in Bisq 2 with the needs of Alkaest. It separates published Bisq 2 role behavior from an open rate-limit proposal and from Bisq v1's different escrow/dispute design. These are inputs to decisions, not protocol requirements.

## What Bisq 2 offers as inspiration

### Role separation in Bisq Easy

Bisq 2 dispute resolution is protocol-dependent. Bisq Easy offers encrypted trader chat and mediation; the Bisq 2 roles documentation says a mediator has no direct enforcement power and can report bad behavior to a moderator. Moderators handle reports, investigate violations, and can ban profile IDs. This separation is useful for Alkaest: helping parties reach agreement, deciding a protocol-state conflict, restricting network participation, and controlling funds are different powers and should not silently belong to one role. Bisq's own roles page notes that profile bans can have limited effect because users can create multiple identities. See [Bisq 2 dispute resolution](https://bisq.wiki/Dispute_Resolution_in_Bisq_2) and [Bisq 2 roles](https://bisq.wiki/Bisq_2_Roles).

The Bisq 2 pages are not perfectly consistent about whether a mediator can ban a trader. This review follows the dedicated roles page's explicit separation: mediator has no direct enforcement power; moderator handles bans. Alkaest should state the distinction normatively rather than inherit that ambiguity.

### Rate limits, attestations, and retention

The Bisq 2 discussion [Trade-Rate Limiting for New Buyers](https://github.com/bisq-network/bisq2/discussions/4164) describes a proposal, not a general-purpose set of protocol size limits. It uses signed claims, oracle validation, a fingerprint-based key to reduce multi-profile bypass, short retention for rate-limit evidence, and a fail-open path if all oracles are unavailable. The discussion also identifies unresolved concerns: multiple accounts can reset account age, fingerprint-based keys create privacy/linkability concerns, a claimant can grief a victim's rate-limit slot, and oracle outage weakens enforcement.

Transferable lessons: bound the lifetime and count of ephemeral data; bind abuse controls to more than a freshly created profile; authenticate and independently verify attestations; and make the security/availability trade-off explicit. Do not copy the proposal's identity fingerprint, oracle trust, sample quotas, or fail-open policy into Alkaest without a privacy and adversarial review.

The reviewed Bisq 2 materials do not establish one universal Alkaest-like envelope, event, batch, JSON-depth, or attachment ceiling. We therefore should not present any numeric cap below as a Bisq limit.

### Financial settlement is a separate design

Bisq v1's documented trade workflow includes a 2-of-2 escrow and a time-locked transaction that changes the consequences of arbitration. That is specific to its trading protocol and differs from Bisq Easy's mediation model. It is useful as a reminder to make dispute outcomes enforceable through precommitted settlement conditions where possible, but its donation-address penalty or time-lock mechanism should not be transplanted into Alkaest task payments. See [Bisq trading rules and dispute resolution](https://docs.bisq.network/trading-rules.html). Alkaest's generic event resolver must not gain a key or permission to redirect treasury funds; RFC-0008 and RFC-0013 must define settlement and appeals separately.

## Decision A — Protocol resource bounds

Three viable starting policies:

| Option | Protocol-wide maximums | Advantages | Costs and risks |
|---|---|---|---|
| A. Tight fixed ceilings | Low hard ceilings for canonical envelope/event size, JSON complexity, and sync batches; attachments are referenced out of band. | Easiest to review and safest for heterogeneous nodes; predictable memory and CPU. | May reject legitimate large project metadata; ceiling changes need a protocol upgrade. |
| B. Tiered message classes | Small limits for state events, separate larger caps for documents/attachments, with class-specific count and byte budgets. | Matches object purpose; prevents a large artifact from consuming the event budget. | More schemas and validation paths; a type must not be relabeled to get a larger allowance. |
| C. Capability-negotiated limits | Peers advertise what they can handle and sync is chunked to the receiver's advertised cap, under a smaller absolute protocol maximum. | Better for future Light/mobile nodes and gradual transfer. | Negotiation alone cannot protect parsers; malicious peers can lie, so a hard absolute maximum remains mandatory. |

**Candidate combined model:** choose B for protocol data classes and use C only to negotiate smaller transport chunks. Every class gets a hard network maximum; each node may set a lower local maximum. No peer may raise another node's limit. Attachments stay outside signed event payload bytes and are transferred in bounded chunks.

Provisional cap bands for discussion only—not adopted and not sourced from Bisq:

| Profile | Signed event payload | Sync batch | JSON nesting | Intended trade-off |
|---|---:|---:|---:|---|
| Conservative | 64 KiB | 512 KiB | 32 | Small attack surface, more references/chunks |
| Balanced | 256 KiB | 2 MiB | 48 | Room for metadata and moderate batches |
| Generous | 1 MiB | 8 MiB | 64 | Fewer round trips, greater parser and memory pressure |

These numbers are only discussion anchors. Before selecting any cap, inventory actual RFC payloads, define byte accounting (decoded canonical bytes vs. transport bytes), and benchmark peak memory/CPU on the Light/low-resource profile as well as the desktop node. JSON property count, array length, string length, event count, signature count, compressed/uncompressed size, decompression ratio, attachments, processing deadline, and concurrent requests also need bounds; a single payload-byte ceiling is insufficient.

### Resource controls that apply under every option

1. Reject an over-limit frame before allocating the full decoded payload where the transport permits streaming length checks.
2. Bound bytes, nesting, object members, array members, strings, signatures, batch count, decompression ratio, CPU time, and concurrent work independently.
3. Use transport-level per-peer backpressure and local ingress quotas. Do not make a node's local rate limiter alter the canonical meaning of an otherwise valid event.
4. Apply any protocol-wide quota only to a clearly defined unit and epoch. Identity-only quotas are Sybil-bypassable; IP-based quotas can exclude shared networks and leak metadata.
5. Use TTL only for explicitly ephemeral data (presence, transient chat delivery, caches, rate attestations). Do not expire signed state history or evidence needed for replay, appeals, or payout audit. If history compaction is needed, specify verifiable checkpoints and retention proofs separately.
6. For sync, fetch bounded pages/chunks and make resume, deduplication, and cancellation explicit. Never trust a peer's advertised total size or item count.

## Decision B — Authority for conflicting events

First separate four actions that are often conflated:

1. **Mediation:** help parties communicate; a recommendation has no protocol effect unless the parties accept it or a separately authorized process adopts it.
2. **Conflict resolution:** select which branch becomes the object's canonical successor under RFC-0005. This does not grant permission to move funds.
3. **Moderation:** restrict an Identity/Space or suppress abusive network traffic. This must not rewrite prior event history or decide ownership of escrow.
4. **Settlement authorization:** release/refund funds under RFC-0008 and the dispute/finality rules in RFC-0013. This must use separate evidence and keys from routine protocol moderation.

| Option | Who resolves a state conflict? | Advantages | Costs and risks |
|---|---|---|---|
| A. Space owner | One predeclared Space authority signs a resolution. | Simple, fast, clear accountability for a small project. | Single-key compromise, capture, unavailability, and maintainer self-dealing; weak for disputes involving the owner. |
| B. Space-local 2-of-3 panel | A predeclared roster of three distinct eligible reviewers; two sign the same resolution. | No single resolver can decide; low latency; role can be scoped to one Space and event type. | Three colluding/related identities can still control outcome; selection, rotation, key loss, conflict checks, and appeals need specification. |
| C. Network-wide governance | A protocol/DAO process approves the resolution or the resolver roster. | Broad legitimacy and public accountability; can handle cross-Space incidents. | Slow and costly for ordinary task conflicts; token governance is not designed or authorized; voter capture and low participation risk. |
| D. Party agreement after mediation | An advisory mediator proposes an outcome; affected parties sign acceptance. | Strong consent and minimal central authority; practical for cooperative disputes. | Either party can stall; unsuitable for unilateral abuse reports, lost keys, or an escrow deadline without a separate fallback. |

**Candidate hybrid:** ordinary factual transitions remain deterministic and need no human arbitration. A valid fork stops at the common ancestor. A Space-local 2-of-3 panel can sign a scoped, auditable resolution for non-financial protocol state; mediation is available before or alongside that process but is advisory. Financial disputes freeze the relevant escrow and use RFC-0013's appeal path plus RFC-0008's settlement enforcement. A resolver event can never itself sign, redirect, or release funds.

The panel roster should be fixed before the conflict, versioned, and signed by the Space's governance policy. A resolution should identify the object, common ancestor, all known competing event IDs, selected successor or explicit cancellation, evidence references, policy version, resolver signatures, and an appeal deadline. Identity/event ID order is not a substitute for authority. For a conflict involving a panel member, require a replacement from a roster snapshot that predates the conflict; do not let the accused party pick the replacement.

### Bonded roles: optional, not a default

Bisq 2 uses DAO-approved bonded roles, with a BSQ bond that can be confiscated through governance in documented circumstances. This can raise the cost of role abuse and make role owners accountable. Alkaest has no selected token or operational DAO, and a financial bond can exclude contributors or be funded by an attacker. If Alkaest later considers bonds, make them an optional role-security mechanism with a defined adjudication and appeal path, not an assumption for the first protocol release.

## Current recommendation for discussion

- Resource bounds: **B + C** — message-class hard ceilings, lower local caps, chunked transfer, and no unbounded history; choose numeric caps only after payload inventory and low-resource benchmarks.
- Conflict authority: **D as the cooperative first step, then B for unresolved non-financial state conflicts**. Keep moderation and treasury settlement separate. Do not require a token bond or network-wide DAO vote for routine project state.
- Before any real payout, wait for RFC-0008 settlement rules and RFC-0013 dispute/finality rules. A WorkItem conflict resolver cannot authorize payment by itself.

## Decisions for Alkaest

1. Should we use the combined B+C resource model as the design direction, leaving numeric caps to measured conformance work?
2. For unresolved non-financial state conflicts, do you prefer a Space-local 2-of-3 panel, a single Space authority, or participant agreement only?
3. Should the resolver role be limited to selecting a state branch, with all moderation and financial settlement handled by separate authorities? This is the recommended separation.

