# Next Tasks

This list is ordered by dependency. Do not start token issuance, reputation-weighted production decisions, or autonomous real-money operation while their prerequisites are open.

## Before inviting outside contributors

- [x] Publish the root contribution guide, Code of Conduct, security policy, issue forms, and pull request template on the public default branch (done in PRs #5 and #6).
- [ ] Enable GitHub private vulnerability reporting or provide a verified private security contact; confirm the Code of Conduct reporting channel works.
- [ ] Resolve licensing for the public `alkaest-ai` repository and any companion repository without a license file. The node, app, Brain, and chatbot repositories are private and open to contributors only by maintainer invitation. The Flutter app currently depends on the node repository's private `alkaest-core` package.
- [ ] Review and open the [draft contributor starter issues](contributor-starter-issues.md) now that the contribution guide is public; assign a maintainer to triage issues and review pull requests.

## Immediate priority — Define Brain-led task selection and treasury policy

1. Cross-review RFC-0014's Brain decision policy: choose the enabled signal classes, freshness/corroboration rules, candidate ranking and tie-break method, and cold-start/quote pricing configuration for the first deployment. The RFC now defines the required policy fields and fails-closed behavior but intentionally supplies no universal ranking weights, rate table, or production limits. Candidate tasks are not open bounties until the Brain's decision passes policy and balance gates and a funded WorkItem is published.
2. Define the treasury's deterministic spendable-BTC calculation, including verified deposits, reserve, pending payouts, fees, and escrow commitments. Then prepare a candidate backlog containing the brand-identity and bounded Flutter tasks; these are candidates for Brain prioritization, not tasks already funded or promised. A first fictional arithmetic and adversarial scenario is in the [Brain and treasury decision rehearsal](brain-treasury-simulation-scenarios.md).
   An offline reference implementation now covers the arithmetic and deterministic candidate gates; run it with `python3 -m unittest discover -s tests -v`. Draft interfaces now exist in RFC-0003/RFC-0008/RFC-0013. Next, resolve the open escrow/key/mediator/refund decisions, then connect an isolated harness to Bitcoin `regtest` and independently replay synthetic metrics/reports/complaints with signed WorkItem creation. The current machine has no `bitcoind`/`bitcoin-cli`, so the chain-backed phase remains open. Only after wallet/key custody, treasury authority, escrow/refund and settlement rules, dispute/appeal process, adversarial and multi-node verification, and independent security review pass their gates can real BTC be accepted or paid. Do not send funds to an unspecified or prototype wallet. Bisq remains an optional, separate P2P route for a contributor seeking fiat; see [Bitcoin payouts and optional Bisq conversion](../research/bitcoin-payouts-and-bisq-conversion.md).

## P0 — Make the protocol drafts coherent

3. Implement the cross-RFC draft rules recorded in the [RFC-0001–0005 consistency review](core-rfc-cross-review.md), keeping all five RFCs in Draft until independently reviewed.
4. Run the expanded Draft [RFC-0004](../rfc/vectors/rfc-0004.json) and [RFC-0005](../rfc/vectors/rfc-0005.json) conformance vectors in at least two independent protocol implementations and record results. Primitive smoke checks in Node and Python confirmed current canonicalization, identifier/hash, and Ed25519 known answers, but they are not independent Alkaest implementations; full conformance remains open. New cases cover negative zero, non-finite and unsafe integer numbers, signature-length rejection, and out-of-order/competing conflict resolutions.
5. Cross-review the Draft B+C resource model and Space-local 2-of-3 conflict resolver baseline now recorded in RFC-0002/RFC-0005. Inventory payload classes and run the reproducible [ADR-0009 benchmark plan](../decisions/ADR-0009-resource-aware-capacity-and-deployment.md) before selecting numeric caps. Verify atomic admission, projection commit/rebuild, crash recovery, and malformed-input behavior against the [Bisq incident threat cases](../research/bisq-may-2026-incident-and-alkaest-mitigations.md); exact resolver schemas, key recovery, and appeal interaction remain open.
6. Cross-review RFC-0014 §10.1's role-separated pause/recovery model. Select the pause/recovery quorums and independent custody rules, deterministic expiry source and duration/extension limits, challenge window, and guardian succession schema; simulate the 3-of-5 baseline without treating it as adopted. Keep reserve spending, policy changes, and frozen obligations outside emergency pause/recovery authority.

## P1 — Specify the first workflow and security boundaries

7. Cross-review the new RFC-0003 WorkItem state machine, assignment proposal/acceptance, role separation, funding/settlement projections, and evidence provenance. Resolve project integration and external adapter trust; finalize payload schemas and actor authority for the now-aligned validation/funding event names across RFC-0003/0008/0013, align sequencing with RFC-0004/0005/0014, then add conformance scenarios. Keep `payout_authorized` distinct from settlement-confirmed `paid`.
8. Write RFC-0006 from the [reputation integrity threat model](../research/reputation-integrity-threat-model.md); make it a prerequisite to consequential production reputation.
9. Cross-review Draft RFC-0013 against RFC-0003/RFC-0005/RFC-0006/RFC-0008/RFC-0014; decide validator classes, conflict appeals, provisional/final states, and case deadlines without treating pseudonymous identities as proof of unique people.
10. Cross-review Draft RFC-0008 and RFC-0013 together; resolve the script/key, mediator, refund, recipient-control, chain-verification, and confirmation policy gates before regtest integration.
11. Complete RFC-0014 policy/event schemas, integer units, provider attestations, key separation, independent verification, pause/recovery, and adversarial regtest scenarios.
12. Define Alkaest donation allocation, reserve/operating limits, guardian quorum, reviewer classes, and `.alkaest/project.yaml`.

## P2 — Token decision package (design only)

13. Resolve guardian independence and role-separated recovery using the [continuity authority options](../research/long-term-continuity-requirements.md#recovery-authority-options); simulate the 3-of-5 baseline and incorporate the chosen thresholds, pause limits, and succession path into the owning ADRs/RFCs before enabling production authority.
14. Define the token's concrete utility and rights; compare fixed per-WorkItem rewards, capped epoch pools, and finite allocations; model transferability, mediator locks versus burns, and founder-independent succession using the [Bisq/token research](../research/bisq-dao-and-alkaest-token.md).
15. Compare a BSQ-like Bitcoin asset, an asset on an existing smart-contract platform, and no transferable token. Include attack, migration, operating, and jurisdiction analyses.
16. Do not create a token design RFC until those comparisons and multi-project simulations produce a coherent proposal. No issuance, public offer, listing, custody, or real-money vote is authorized.

## P3 — Defer until prerequisites or product evidence exist

17. Stabilize RFC-0009 after the node and module contracts settle.
18. Write RFC-0010–0012 (data availability/privacy, capabilities/permissions, governance/versioning) when their interfaces become implementation requirements; RFC-0010 must cover evidence access grants, media/location retention, redaction, replication, and privacy-preserving verification using the [mobile evidence research](../research/mobile-work-evidence-and-location-assurance.md).
19. Specify the WhatsApp Cloud API onboarding/credential model, provider-specific usage ledger, Meta/provider charge reconciliation, variable Alkaest service meter, estimates, caps, and billing statement before the paid chatbot pilot.
20. Revisit RFC-0007 and the chatbot-to-network mapping after Alkaest Chatbot demonstrates real provider workflows and privacy constraints.
21. Keep diagrams synchronized with the RFCs when protocol state or architecture changes; current diagram set is listed in the [documentation index](../README.md).

## Product research — optional professional tools

22. Interview independent professionals about the business reports and current tools they actually use; validate the proposed [multitenant, read-only Dolibarr pilot](../research/professional-tools-integration-pilot.md) with a small provider cohort.
23. Before implementation, run a two-tenant disposable-instance spike to verify isolation across authorization, storage, credentials, sync jobs, caches, reports, exports, support access, and deletion; also verify Dolibarr API permissions, data semantics, and deployment burden. Proceed only if cross-tenant access is prevented, data reconciles, and providers find the report useful; otherwise defer or use manual import.

## Paid open-source contribution model

24. Resolve RFC-0008's escrow/settlement and RFC-0013 dispute/appeal launch gates, resolving the dependencies listed in the [paid-work pilot cross-review](paid-work-cross-review.md). Keep the paid-work pilot valueless and internal.
25. Cross-review the Draft RFC-0008/0013 texts with RFC-0003/0004/0005/0006/0014, then write conformance scenarios and tests before implementation. Do not activate real funds until the launch gates listed in the pilot design and roadmap are complete.

## Chatbot-backed service network validation

26. Specify and test the [service-domain backend gate](../overview/network-rollout-plan.md#service-domain-backend-gate) before building a protocol/reputation frontend: isolated provider Spaces, synthetic data first, consent and privacy controls before real records, deterministic multi-node replay, and explicit provenance for provider completion versus customer-signed or relayed feedback. Keep RFC-0006's reputation launch gate in force.
