# Open Questions

These are unresolved decisions, not implied defaults. Priority order follows the [roadmap](../overview/roadmap.md).

## Protocol correctness (resolve before implementation)

- Which scoped authority resolves non-financial event conflicts, and what roster/appeal rules prevent unilateral control? See the [Bisq 2 comparison and options](../research/bisq2-resource-bounds-and-dispute-authority.md).
- What hard per-class limits apply to canonical payloads, JSON complexity, batches, attachments, CPU, and concurrency? Which limits may be lower per node?
- Which representative hardware/workloads should establish resource budgets before numeric limits are fixed under [ADR-0009](../decisions/ADR-0009-resource-aware-capacity-and-deployment.md)?
- Which optional Service workloads can safely scale horizontally, and what measured operational thresholds would justify Kubernetes for one operator's managed services?
- Which event transitions require atomic validation/application and what is the deterministic invalid-event behavior?
- What is the signed emergency pause/recovery model and which operations can it pause?
- What exact artifact is the MVP: a local node, a node plus developer workflow UI, or a complete Alkaest self-hosted project workflow?
- Is initial validation project-curated, open to qualified participants, or hybrid, and what is trusted at each stage?

## First workflow, payments, and reputation (resolve before real value or consequential scores)

- RFC-0003/RFC-0014 Drafts now propose exclusive MVP assignment, pre-work funding, separate signed scope-amendment proposal/acceptance events, explicit release before reassignment, and reviewer conflict checks. See the [paid-work pilot cross-review](paid-work-cross-review.md); deadline semantics, related-identity limits, and event schemas still need review.
- How should contributor identity control and prove a settlement destination without publishing sensitive payment details? RFC-0003 proposes contributor-signed instructions; Draft RFC-0008 must specify verification, output validation, and privacy.
- Which mediator eligibility/selection, appeal, and finality policies should be adopted from Draft RFC-0013 for disputed paid WorkItems and event conflicts? This remains a real-money launch gate; the Draft deliberately does not choose a selection algorithm or Bitcoin spend authority.
- Which independent approvals and CI/security checks are required by change risk class?
- How are GitHub/CI adapter attestations signed, bound to immutable revisions, and independently verified?
- What mediator-selection randomness protocol resists block withholding, reorgs, selective participation, and candidate grinding while remaining independently verifiable?
- What policy limits govern task budget, per-contributor exposure, reserve floor, and agent allowance?
- RFC-0014 §10.1 proposes role-separated pause and recovery authorities. Should the 3-of-5 independent guardian set remain the simulation baseline, and what custody/organization independence, deterministic expiry source, maximum pause and extension duration, challenge window, and roster-succession rules should apply before real treasury use? See [recovery authority options](../research/long-term-continuity-requirements.md#recovery-authority-options).
- Should RFC-0005's Draft baseline of party agreement followed by a predeclared Space-local 2-of-3 panel be accepted? The approval schema, roster rotation/key-loss behavior, conflict-of-interest handling, and appeal relationship remain open.
- How do reputation proofs resist self-dealing, related identities, collusion, wash funding, duplicates, and task splitting while preserving pseudonymity?
- What independent-demand evidence matures a proof, and what are the challenge, appeal, correction, and revocation rules?
- Which audited escrow script/key and timeout/refund path should RFC-0008 use? What destination-control proof, Bitcoin chain verifier, confirmation/finality, audit commitment, and fee policy should its production profile require?
- What does the first paid-work pilot expose to contributors, and which operational decisions remain human-supervised?
- Which future service workflow justifies onsite evidence, and should its initial assurance baseline be fresh in-app capture plus task-bound challenge, recipient co-signature, or a stronger independent checkpoint? See [mobile work evidence and location assurance](../research/mobile-work-evidence-and-location-assurance.md).

## Token and multi-project governance (resolve before any issuance)

- What concrete utility and rights require an Alkaest-native transferable token?
- Should contributor rewards be fixed and preannounced per funded WorkItem, drawn from a capped epoch pool, or allocated from a finite supply? What economic budget actually backs them?
- Should mediator eligibility use a recoverable lock/bond or an irreversible burn? Does holding more than the minimum grant any additional influence (recommended: no)?
- Which protocol fees, if any, should be burned versus paid into a treasury or contributor fund, and what supply equation prevents uncontrolled issuance/dilution?
- What maintainership, threshold-key, repository/domain, upgrade-delay, and recovery policy keeps Alkaest operational if its founder disappears or loses control?
- Which decisions are local to a project and which belong to the shared protocol treasury/governance?
- Should governance, service access/fees, project budgets, settlement, and contributor incentives be separate assets or units?
- Which supply, distribution, and voting model resists concentration, Sybil attacks, vote buying, and low participation?
- Which asset representations and jurisdictions need technical/legal comparison?
- What recovery thresholds, release-signing rules, emergency-pause expiry, and redundancy targets satisfy the [long-term continuity scenarios](../research/long-term-continuity-requirements.md) without giving a single successor group unilateral control?
