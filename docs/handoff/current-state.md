# Current State

**As of:** 2026-10-22
**Repository maturity:** documentation and architecture planning, plus an offline treasury decision prototype; no protocol or Bitcoin settlement implementation is present in this repository.

## Product and protocol direction

- Alkaest is a protocol-first project; the initial domain is open-source development coordination.
- Desktop Standard node is the first implementation target; architecture should support Light, Standard, and Service profiles (ADR-0001, ADR-0003, ADR-0005).
- Alkaest Chatbot is a commercial bootstrap product and future source of service-domain learning. It is not the protocol core (ADR-0002).
- ADR-0002 now selects the official WhatsApp Business Platform API for production and usage-based billing per provider; exact Alkaest margin, billing period, payment method, and WABA ownership remain undecided.
- The long-term adoption path now includes both coordinated demand brought by operators/teams and direct WorkItem discovery by individual contributors; this is a future expansion direction, not an MVP promise. See [vision](../overview/vision.md#market-participation-over-time) and [roadmap](../overview/roadmap.md).
- Long-term product vision includes an opt-in operating layer for independent professionals using replaceable open-source integrations and reports, plus project-scoped DAO-like governance for independent open-source projects. No specific tool, predictive feature, token, or global DAO model is selected.
- A distant vision extends this operating layer to physical assets such as rental homes: bounded agents coordinate bookings and approved cleaning/repair work through replaceable home-automation and service adapters. This is not a current capability or committed roadmap phase; owner authority, guest privacy, multitenant isolation, spending/access limits, safety escalation, and evidence requirements remain prerequisites. See [vision](../overview/vision.md#autonomous-operations-for-physical-assets).
- Future mobile work evidence is a design topic, not an MVP requirement. Location and media are evidence claims with explicit source/assurance, privacy controls, and corroboration; commodity GPS alone is not treated as proof. See [mobile evidence research](../research/mobile-work-evidence-and-location-assurance.md).
- Radicle is the canonical forge (ADR-0010, accepted 2026-10-22): patches are reviewed and merged there, and paid work references Radicle patches. GitHub is a read-mostly mirror. Forges and CI are integrations that provide evidence, not authorities over Alkaest state. The canonical Radicle repository and the project's onion seed node are not set up yet.
- Bitcoin is the current direction for treasury settlement and audit commitments. No custom Alkaest chain is planned (ADR-0004, ADR-0007).
- Token economics should be designed before launch, but no token is selected or authorized for issuance, sale, listing, or real-money governance (ADR-0008).
- Reputation is non-transferable. No reputation score/proof may affect consequential production outcomes until RFC-0006 resolves self-dealing, Sybil/collusion risks, evidence provenance, appeals, and privacy.
- Treasury automation is a direction only. RFC-0014 is draft; autonomous mainnet spending is not authorized.
- An offline Python treasury prototype now reproduces the fictional BTC balance and candidate-allocation arithmetic in the [decision rehearsal](brain-treasury-simulation-scenarios.md). Its six unit tests pass, but it does not run `bitcoind`, verify settlement, process complaint provenance, sign WorkItems, or authorize funds; Bitcoin `regtest` integration remains pending RFC-0003/RFC-0008 cross-review and an available Bitcoin Core toolchain.
- The paid open-source work pilot is design-only and valueless. RFC-0003/RFC-0014 drafts specify exclusive timed assignments with separate signed offer/acceptance, a WorkItem lifecycle, role separation, funding and settlement projections, evidence provenance, independent reviewer conflict checks, and contributor-bound payout instructions. RFC-0003 blocks payout and closure while an RFC-0013 dispute remains unresolved. RFC-0003/0008/0013 now align submission and funding event names; canonical payload schemas, actor authority, expiry semantics, event vectors, and integration trust still need review. Script/key, mediator selection, appeal parameters, timeout/refund, destination-control, production chain verification, and independent security review remain launch gates. Disputed Bitcoin spending is disabled. No conformance vectors or real-payment pilot are ready yet. See the [pilot design](../research/alkaest-paid-work-pilot-design.md), [cross-review](paid-work-cross-review.md), [RFC-0008](../rfc/0008-bitcoin-escrow-and-settlement.md), and [RFC-0013](../rfc/0013-validation-dispute-resolution-and-appeals.md).
- The chatbot is now planned as the first backend integration pilot for the service network, before a protocol/reputation frontend: private provider Spaces, test nodes, synthetic data first, and no hidden collection of customer-derived evidence. Provider-recorded completion, customer-signed feedback, and chatbot-relayed feedback remain distinct claims; free-text comments stay private by default. Mature or consequential reputation remains blocked by RFC-0006. See the [chatbot-to-network strategy](../overview/chatbot-to-network-strategy.md) and [rollout gate](../overview/network-rollout-plan.md#service-domain-backend-gate).
- Long-term continuity scenarios now inform ADR-0007 and draft RFC-0014: founder/key loss, bounded pause expiry, recovery deadlock, independent artifacts, safe fork/exit, and no-token operation. RFC-0014 §10.1 now separates pause, recovery, policy-change, and spending authority and defines scoped pause and delayed key-rotation requirements. Guardian thresholds (3-of-5 is only a simulation baseline), deterministic expiry source, maximum pause duration, challenge window, and succession schemas remain open; see [continuity requirements](../research/long-term-continuity-requirements.md).
- Draft RFC-0004 and RFC-0005 known-answer fixtures cover canonical encoding, crypto/ID derivation, replay, arrival order, and authorized conflict resolution, with added numeric-boundary and delayed-resolution cases. Primitive smoke checks in Node and Python passed the current encoding, hash/ID, and Ed25519 vectors; neither is an independent Alkaest implementation, so independent multi-implementation conformance remains open.
- ADR-0009 (Proposed) recommends deferring Kubernetes through the MVP/local multi-node phase, benchmark resource use before fixing numeric profiles, and treat high-capacity Service contributions as optional with no extra protocol authority. A reproducible Light/Standard/Service benchmark plan is now specified; measurements, numeric caps, and multi-host adoption thresholds remain open. RFC-0002 records a Draft class-based limit model, and RFC-0005 records a Draft Space-local 2-of-3 conflict-resolution baseline; their schemas and independent review remain open.

## Specification inventory

- Draft RFCs present: RFC-0001–0005, RFC-0007–0009, RFC-0013, RFC-0014.
- Not written but required before relevant production use: RFC-0006 (reputation). RFC-0008 and RFC-0013 are Drafts and remain production launch gates.
- Planned for later ecosystem maturity: RFC-0010–0012; future token design RFC not yet numbered.
- ADRs 0001–0009 are indexed in [decisions](../decisions/README.md). ADR-0003 is accepted as an architectural direction; its reference technologies remain proposals. ADR-0009 is Proposed, with numeric resource profiles and platform thresholds still open.

## Implementation status (separate repositories)

These components live outside this repository; see the [repository map](../../CONTRIBUTING.md#choose-a-repository).

- `alkaest-node` (private): `main` has the Phase 0 node plus a signed Local API, device pairing, and server-sent event streaming. It now passes the Draft RFC-0004/0005 vectors (RFC 8785 canonical JSON, domain-separated ids, fail-closed conflicts), implements the RFC-0003 assignment proposal/acceptance flow with `paid` reachable only through settlement, and enforces Space policy roles and the review gate of RFC-0003 §14 (node PRs #2–#5). The RFC-0007 `service_catalog` and `schedule` modules are implemented in core, including staff-signed resolution of competing bookings (node PR #6); The Local API settles booking races automatically, and the chatbot can mirror its bookings to a node in shadow mode. Phase 1 has started: nodes replicate Spaces by pull-based inventory sync (RFC-0002 §6.6.1), validated in a 5–6-node in-process simulation, and carry it over libp2p with gossipsub announcements, mDNS discovery and circuit relays (`alkaest p2p`, `alkaest serve --replicate`). A six-container network with a capped weak node and a capped phone that opens no port and is reached through a relay runs the Phase 1 exit checks (`deploy/phase1/` in alkaest-node). Bandwidth caps, wide-area discovery, capability records and private-Space access control are next. Settlement (RFC-0008), dispute cases (RFC-0013) and resolver panels (RFC-0005 §9.7) are not implemented.
- `alkaest-app` (private): Flutter connect mode with device pairing, exercised end to end against a real node.
- `alkaest-brain` (private): the phase A planner.
- `alkaest-chatbot` (private): the WhatsApp scheduling product.

None of these components authorizes real funds, production reputation, or token operation.

## Security research now incorporated

- [Reputation integrity threat model](../research/reputation-integrity-threat-model.md): identifies self-awarding and collusion risks, proposes controls, and defines a launch gate.
- [Bisq May 2026 incident review](../research/bisq-may-2026-incident-and-alkaest-mitigations.md): requires validation of adversarial inputs before economic state changes, bounded integer amounts, atomic transitions, and incident controls.
- [Bisq DAO and Alkaest token research](../research/bisq-dao-and-alkaest-token.md): token roles, multi-project governance, regulatory considerations, and pre-issuance gates.
- [Bisq 2 resource-bound and dispute-authority comparison](../research/bisq2-resource-bounds-and-dispute-authority.md): informs the Draft class-based resource limits and scoped conflict-authority baseline; numeric caps and implementation details remain open.

## Contributor-facing material

- Root [README](../../README.md), [contribution guide](../../CONTRIBUTING.md), and [contributor page](https://alkaest-network.org/contribute/) describe the current project and how to join. Issue forms, a pull request template, a [Code of Conduct](../../CODE_OF_CONDUCT.md), and a [security policy](../../SECURITY.md) are published on the default branch; two [draft starter issues](contributor-starter-issues.md) are prepared but not yet opened. The node, app, Brain, and chatbot repositories are private and accessible by maintainer invitation. External contributor readiness still depends on enabling/verifying private reporting, clarifying licensing for component repositories, and opening the starter issues.
- The contribution page uses the Alkaest visual identity and presents the chatbot as an optional hosted/self-run path; it should not imply that protocol economics or reputation are already live.
- The selected visual reference boards are recorded in the [visual identity guide](../brand/visual-identity.md). The intended first WorkItem on the Alkaest network is to hire a professional designer for a coherent, accessible, production-ready brand system. The founder intends to seed its funding from personal funds. Rehearse with no-value or `regtest` funds first; the repository contains no implemented wallet or protocol, and real deposits/payouts must wait for the RFC-0003/0008/0013/0014 launch gates and independent security review. Current boards are creative direction, not finished specifications.
- The founder intends for paid WorkItems to settle in BTC through Alkaest, with optional independent Bisq trades for contributors seeking fiat. Draft RFC-0008 selects on-chain BTC in `regtest` for its first conformance target and defers Lightning; production fee, finality, destination-control, and escrow rules remain open. Alkaest must not imply that Bisq is a payout processor or guarantees fiat liquidity/conversion; no real treasury operation is enabled. See [Bitcoin payout and Bisq conversion research](../research/bitcoin-payouts-and-bisq-conversion.md).
- Treasury direction gives the Brain discretion to choose which candidate issue to open and its BTC bounty using provenance-labeled metrics, reports, complaints, and verified available funds, within a signed budget/pricing policy. Deterministic balance and policy gates must authorize every allocation; a single complaint cannot trigger a penalty or payment, and the Brain cannot invent funds or revise its own limits. Details are in Draft [RFC-0014 §5](../rfc/0014-treasury-agent-and-release-authorization.md#5-treasury-policy-and-agent-authority).
- Draft remunerated Flutter task briefs are prepared for node-pairing/recovery UX, WorkItem detail/action feedback, and later application of the professional identity system. The Flutter app already supports connect-mode pairing and basic WorkItem actions; the briefs target improvements and defer real payment until the treasury launch gates pass. See [Flutter paid WorkItems](flutter-paid-workitems.md).

## Core workflow being specified

```text
Need -> predeclared WorkItem -> funding/escrow -> contributor delivery
 -> independently verifiable evidence -> decision -> settlement/audit record
```

Payment eligibility and reputation eligibility are separate. Payment, merge, or an AI decision alone does not prove contribution merit.

## Source-of-truth documents

- [Documentation index](../README.md)
- [Decision index](../decisions/README.md)
- [Roadmap and launch gates](../overview/roadmap.md)
- [Next tasks](next-tasks.md)
- [Open questions](open-questions.md)
