# Roadmap

This roadmap separates what the repository already specifies from what remains a decision, draft, or launch prerequisite. It prioritizes protocol correctness and threat reduction before payment or reputation features can affect real users.

## Current maturity

Alkaest is currently a **documentation and architecture project** in this repository, which contains no protocol implementation. A prototype node (Phase 0 plus a signed Local API, device pairing and event streaming) exists in the separate private `alkaest-node` repository; it does not yet conform to the RFC-0004/0005 vectors, and conformance work is starting. The existing RFCs are drafts, not production guarantees. See the [documentation index](../README.md) and [current state](../handoff/current-state.md).

### Defined directions

- Desktop-first implementation, with future heterogeneous-node support (ADR-0001, ADR-0003, ADR-0005).
- Generic protocol core; open-source development is the first workflow domain (RFC-0001–0003).
- Canonical envelope/identity direction and deterministic event processing are described in RFC-0004/0005. Both have been cross-reviewed and have drafted known-answer vectors, but the vectors have not yet been exercised by any implementation.
- Bitcoin is the current settlement and treasury audit direction; no Alkaest chain (ADR-0004, ADR-0007).
- The founder intends initial paid contributor WorkItems to settle in BTC through Alkaest; contributors may independently trade BTC for fiat through Bisq if they choose. Bisq is not an Alkaest payout processor and conversion/liquidity is not guaranteed. Draft RFC-0008 selects on-chain BTC in `regtest` for initial conformance and defers Lightning; production profile, quote denomination, destination proof, and fees remain open. See [Bitcoin payout research](../research/bitcoin-payouts-and-bisq-conversion.md).
- Design token economics before launch, but do not issue, sell, list, or activate real-money token governance yet (ADR-0008).
- Reputation remains non-transferable. Reputation that affects production authority, funding, governance, or consequential ranking is blocked until RFC-0006 resolves self-dealing, Sybil/collusion risks, appeals, and privacy tradeoffs.
- A bounded treasury agent may perform routine work only under predeclared policy and evidence rules; autonomous mainnet treasury operation is not authorized (ADR-0007, RFC-0014).
- The May 2026 Bisq v1 incident is a concrete security case for validating adversarial inputs before any economic state mutation.
- Stronger hosts may contribute optional Service capacity without receiving extra protocol authority. [ADR-0009](../decisions/ADR-0009-resource-aware-capacity-and-deployment.md) defers Kubernetes until an operator has measured multi-host orchestration needs; representative resource benchmarks remain open.

### Draft specifications

RFC-0001 through RFC-0005, RFC-0007 through RFC-0009, RFC-0013, and RFC-0014 exist as drafts. RFC-0008 and RFC-0013 remain settlement and dispute launch gates; their high-impact selection, escrow and settlement decisions are open. They require consistency and security review before implementation. RFC-0007 is a future service-domain module, not a core MVP blocker.

### Planned specifications not yet written

- RFC-0006: reputation proofs, integrity, scoring and appeals.
- RFC-0010 through RFC-0012: data availability/privacy, permissions/capabilities, and governance/versioning.
- A future token design RFC, number to be assigned through the RFC process after ADR-0008 research/simulation.

## Prioritized work

### Initial candidate backlog — Professional identity and Flutter tasks

The first candidate needs include hiring a professional brand/visual identity designer and bounded Flutter app work. The founder can seed priorities and budget boundaries, then the Brain should select which issue to open first and determine its BTC bounty from evidence, quotes/rate rules, and the verified treasury balance. This makes Alkaest its own first customer while letting the network's decision loop choose the actual order and allocation. Begin with a local/no-value or Bitcoin `regtest` rehearsal. Real deposits and payouts remain blocked until wallet/key custody, treasury authority, escrow/refunds, settlement, disputes/appeals, and independent security review satisfy the launch gates for RFC-0003, RFC-0008, RFC-0013, and RFC-0014. Do not send funds to an unspecified or prototype wallet. The [current visual identity guide](../brand/visual-identity.md) is the creative brief; the reference boards are not final specifications or authority for product claims. Apply the [Bisq comparison](../research/bisq-compensation-and-bisq2-protocol-patterns.md) with care: Bisq DAO compensation is retrospective and should not be mistaken for this pre-funded bounty model. See the [next-tasks list](../handoff/next-tasks.md#immediate-priority--define-brain-led-task-selection-and-treasury-policy).

### P0 — Documentation and protocol consistency

1. Cross-review the Draft RFC-0005 Space-local 2-of-3 resolver baseline and RFC-0002 class-based resource model in the [RFC-0001–0005 cross-review](../handoff/core-rfc-cross-review.md); run the [ADR-0009 benchmark plan](../decisions/ADR-0009-resource-aware-capacity-and-deployment.md) before choosing numeric limits.
2. Review and exercise the Draft conformance vectors for canonical encoding, IDs, signatures, and event-state transitions in independent implementations before implementation claims conformance.
3. Ensure every economic/authority-critical input is treated as untrusted, even when signed. Verify bounded integer units, per-class field/resource limits, cross-field invariants, atomic admission, and projection rebuild behavior. Benchmark representative Light/low-resource, Standard, and Service workloads before selecting numeric resource profiles (ADR-0009).
4. Cross-review Draft RFC-0014 §10.1's role-separated pause/recovery model; choose its guardian quorums, deterministic expiry source and bounds, challenge window, and succession rules without creating unilateral fund-seizure or history-rewrite authority.
5. Confirm the MVP deliverable and initial validation model (project-curated, qualified-open, or hybrid) before freezing implementation scope.

### P1 — Define the first self-hosted workflow safely

1. Cross-review and complete RFC-0003 WorkItem lifecycle, role separation, project integration, task funding, evidence provenance, and conformance scenarios.
2. Write RFC-0006 before any reputation score/proof can influence production access, material ranking, funding, governance, or treasury limits. Use the [reputation integrity threat model](../research/reputation-integrity-threat-model.md).
3. Cross-review Draft RFC-0013 validator eligibility, disputes, mediation, appeals, and finality before implementing disputed-work automation.
4. Cross-review Draft RFC-0008 settlement/escrow rules with RFC-0003/RFC-0013/RFC-0014; resolve the exact transaction, key, recovery, mediator and Bitcoin anchoring gates before implementation.
5. Complete RFC-0014 event schemas, policy evaluation, independent provider attestations, integer bounds, key separation, emergency pause, and recovery. Include regression scenarios based on the [Bisq incident review](../research/bisq-may-2026-incident-and-alkaest-mitigations.md).
6. Decide donation allocation, treasury limits, guardian quorum, reviewer classes, `.alkaest/project.yaml`, and which work can be paid or accepted autonomously.
7. Define the contributor-facing paid-work pilot separately from long-term multi-project economics; disclose what is simulated, supervised, or operational.
8. Cross-review the valueless [Alkaest paid work pilot](../research/alkaest-paid-work-pilot-design.md) rules in RFC-0003/RFC-0014 against event ordering, escrow, and dispute RFCs, informed by the [JHipster bounty model analysis](../research/jhipster-bounty-model.md). Demonstrate a concrete improvement before any real-money launch or external-project invitation.

### P2 — Implement a no-value local prototype

A prototype local node already exists in the private `alkaest-node` repository, but it predates conformance with the Draft vectors. Only after P0 specifications stabilize, bring that node into conformance and implement the first workflow using simulated accounts and Bitcoin `regtest`. Test malicious modified clients, malformed-but-signed inputs, negative/overflow values, replay, inconsistent transaction outputs, conflicting event order, self-dealing, collusive review, duplicate work, and appeals. No production reputation weight, token, public sale, or mainnet treasury permissions in this phase.

### P3 — Multi-node and testnet validation

Run independent nodes and verify byte-for-byte deterministic outcomes, treasury event commitments, recovery, and operational caps. Use `signet` for settlement/anchor experiments. Any token experiment must be valueless, non-transferable outside the test environment, and have no redemption or market promise.

### P4 — Product and network expansion

Use Alkaest Chatbot to validate provider workflows and service-domain privacy needs. The production channel is the official WhatsApp Business Platform API; launch the provider-facing usage ledger, cost estimates, billing statements, thresholds, and safe-cap behavior before onboarding paid production customers. RFC-0007 now exists as a Draft; the next service step is a private backend integration through provider Spaces and an isolated multi-node network, using synthetic data first. Pass the [service-domain backend gate](network-rollout-plan.md#service-domain-backend-gate) before adding protocol-facing discovery or reputation screens. Do not let customer data or scheduling assumptions leak into protocol core. Production reputation remains behind RFC-0006 launch gates.

Before onsite service work is used for paid-work or reputation decisions, design and test the [mobile evidence and location assurance model](../research/mobile-work-evidence-and-location-assurance.md). Phones are evidence-capture clients; GPS, a photo, or a vendor integrity verdict alone is never treated as proof of physical presence. Define task-specific evidence profiles, privacy/retention rules, corroboration, and an appeal path first.

Grow work-market participation in steps:

1. **Coordinated demand:** let experienced operators and teams bring opportunities, turn them into scoped and funded WorkItems, and coordinate contributors. Record the scope, budget, roles, acceptance rules, and any subcontracted work before delivery begins.
2. **Open discovery:** make eligible WorkItems discoverable through independent indexes and clients, with enough context for a person to judge fit without relying on a single operator's private account or ranking.
3. **Direct participation:** make it practical for individual contributors to run or connect through an Alkaest client/node, find work, and claim or negotiate it directly under the project's policy.
4. **Coexistence and portability:** retain a useful role for coordinators who add scoping, trust, or delivery capacity, while allowing contributors and projects to move their identities, evidence, and eligible records between clients and operators.

These are adoption capabilities, not launch promises or fixed dates. Direct discovery must not imply that all demand is public, that work is automatically open to everyone, or that a protocol role determines employment status. Privacy, funding, selection rules, disputes, and jurisdiction-specific responsibilities remain explicit launch constraints.

Expand from service coordination into a professional operating layer only after provider workflows and consent are proven:

1. **Connect, do not absorb:** integrate selected open-source scheduling, customer-management, invoicing, and bookkeeping tools through replaceable adapters. Give the professional control over scopes, permissions, export, and disconnect.
2. **Explain the business:** provide reports from user-authorized operational data, with provenance, time ranges, and uncertainty visible. Start with descriptive history before forecasts or recommendations.
3. **Support planning:** evaluate opt-in decision support such as identifying a lower-demand window for time off. Show the evidence and assumptions; the professional decides whether to act. Do not present an estimate as guaranteed income, financial advice, or an automatic action.
4. **Onboard independent projects:** provide reusable setup and governance tooling for open-source projects to form their own Spaces, publish budgets and decision rules, coordinate funded WorkItems, and replace project roles. DAO-like governance is project-scoped and does not require an Alkaest token or a global treasury.
5. **Grow a module ecosystem:** let projects and providers add, maintain, and replace integrations without giving an adapter authority over identity, project funds, or protocol state.

Choose specific open-source tools only after validating target-provider workflows, maintenance health, integration interfaces, data export, security posture, and deployment options. Alkaest should orchestrate interoperable tools rather than become a monolithic accounting or ERP system.

The initial research candidate is an optional, read-only Dolibarr connector in a multitenant product, described in the [professional tools integration pilot](../research/professional-tools-integration-pilot.md). Tenant isolation is required from the pilot onward and must be demonstrated across data, credentials, background work, reports, exports, and deletion. This is a validation target, not an adopted dependency: confirm provider demand, API permission granularity, and deployment burden before implementation.

### Long-term concept — autonomous operations for physical assets

After the professional-tool layer, service marketplace, evidence, permissions, and dispute controls are mature, Alkaest could coordinate a managed rental property through replaceable home-automation and service-provider adapters. A bounded agent could handle routine bookings and approved cleaning or maintenance WorkItems under owner-defined, revocable policies. This remains a distant vision, not a committed roadmap phase. It requires explicit guest privacy/consent, tenant isolation, device security, auditable authority, spending and access limits, emergency handling, and human escalation for high-impact or out-of-policy actions. See [vision: autonomous operations for physical assets](vision.md#autonomous-operations-for-physical-assets).

## Decisions that must precede launch

### Before any paid work or real treasury

- Accepted RFC-0003, RFC-0008, RFC-0013, and RFC-0014 behavior.
- Exact budget/payout units, escrow terms, transaction verification, treasury reserve and operating caps.
- Guardian quorum, key separation, pause scope, recovery drill, dispute/appeal process, security incident response.
- Independent review of code, dependency, design, documentation, and operational changes by risk class.
- Legal, tax, and accounting review for the actual jurisdictions and services.

### Before reputation affects consequential decisions

- RFC-0006 specifies proof provenance, role separation, independent demand, validator diversity, anti-collusion and task-splitting rules, provisional maturity, revocation, appeals, privacy, domain boundaries, and influence caps.
- Tests demonstrate that self-created tasks and related-identity activity do not automatically create mature reputation or authority.
- Define how reputational evidence is shown without overstating identity uniqueness or certainty.

### Before token issuance or token governance

- Identify a concrete protocol utility and exact rights; compare a BSQ-like design, existing alternative asset layers, and a no-transferable-token baseline.
- Simulate multi-project treasury flows and governance capture, concentration, Sybil attacks, vote buying, quorum failure, key loss, and emergency issuance.
- Decide whether governance, fees, project budgets, settlement, and incentives are separate assets/units.
- Approve distribution, supply, issuance caps, upgrade rules, migration, and incident/sunset plan.
- Obtain jurisdiction-specific legal, tax, and accounting opinions before any distribution, offer, listing, custody, or related service.

## Scope discipline

- Do not build a custom chain for ordinary Alkaest event validation.
- Do not use a transferable token as reputation or treat paid tasks as proof of merit by themselves.
- Do not let GitHub, CI, an indexer, or an AI model become the protocol authority.
- Keep chatbot/WhatsApp details in integrations and service modules.
- Do not increase treasury, token, or reputation authority merely to meet a roadmap date; advance phases only when their exit criteria are evidenced.
