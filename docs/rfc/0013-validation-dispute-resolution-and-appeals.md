# RFC-0013 — Validation, Dispute Resolution, and Appeals

**Status:** Draft; no production or real-funds authorization  
**Date:** 2026-10-19  
**Category:** Work Validation and Conflict Resolution  
**Related:** ADR-0006, ADR-0007, RFC-0003, RFC-0005, RFC-0006 (planned, not yet written), RFC-0008, RFC-0014

## 1. Abstract

This RFC defines the boundary between deliverable review, party-to-party mediation, protocol dispute decisions, appeals, and Bitcoin settlement. It establishes a conservative workflow and signed evidence record. It does not finalize mediator selection, bonds, fees, deadlines, token privileges, reputation thresholds, a Bitcoin escrow script, or production launch policy.

The key constraint is that a dispute verdict is a protocol decision; it is not itself a Bitcoin spend. RFC-0008's candidate 2-of-3 escrow gives the mediator key spending power with either party. That key arrangement is not safe for real funds merely because RFC-0013 records a signed verdict. A disputed-spend path remains disabled until the script, authority, timeout/recovery behavior, and independent review are resolved together.

## 2. Goals and non-goals

Goals:

- Separate technical/work validation, mediation, adjudication, appeals, and settlement authorization.
- Record role separation, conflicts, evidence references, policy versions, decisions, and corrections as replayable events.
- Prevent self-review and self-mediation at the protocol-identity level, while stating the residual limits of pseudonymous Sybil detection.
- Keep payment rights distinct from reputation credit or governance influence.
- Provide a future conformance target that works with RFC-0003 WorkItems, RFC-0005 event resolution, RFC-0006 reputation proofs (planned, not yet written), RFC-0008 settlement, and RFC-0014 treasury authorization.

Non-goals:

- Guarantee that distinct protocol identities represent distinct people.
- Prove that a human read, understood, or independently judged evidence.
- Make an AI model, GitHub status, merge, customer rating, or token balance the final arbiter.
- Define legal arbitration, fiat escrow, a global reputation score, token issuance, or mainnet settlement.

## 3. Bisq design lessons and limits

Bisq is a source of patterns, not a drop-in protocol. Bisq 1 trade mediation is designed to seek a cooperative settlement; its mediator cannot unilaterally enforce an outcome or spend escrow. Its older on-chain trade design used delayed payout arrangements and arbitration as a separate last resort. Bisq 2 has protocol-specific dispute flows; one must not assume every Bisq 2 trade protocol has identical roles or remedies. Alkaest should therefore keep facilitation, decision authority, and fund-control authority explicit and separate.

This draft adopts the lesson that mediation should first help parties reach a mutually signed outcome, and that any non-consensual decision path must be separately bounded and reviewable. It does not adopt Bisq's historic bond amounts, fee values, timeouts, or governance roles.

## 4. Roles and separation

For a WorkItem, the event history MUST identify the task creator/funder, assignee, submitter, validator(s), mediator, appeal reviewer(s), treasury authorizer, and payout destination authority. One protocol Identity MUST NOT act in conflicting roles on the same case: a creator/funder, assignee, or payout recipient cannot validate or mediate their own case, and the treasury agent cannot mediate its own WorkItem.

Known affiliations and protocol-visible funding, approval, and review relationships MUST be recorded as conflict evidence. A declared or detected conflict blocks that reviewer from the case pending policy resolution. Lack of a detected relationship is not proof of independence. Multiple keys, bonds, reputation, or token ownership alone do not prove multiple independent humans. No token-weighted mediator eligibility is enabled by this RFC; token design remains deferred.

The MVP may use a named, human-appointed reviewer roster for supervised internal exercises, but that is a trust assumption, not decentralized or Sybil-resistant selection. Open-network eligibility and selection require a later explicit policy and adversarial review.

## 5. Review and resolution lifecycle

The conceptual case lifecycle is:

```text
submitted -> validation_pending -> accepted | challenged
challenged -> mediation_open -> mutually_resolved | mediation_failed
mediation_failed -> adjudication_pending -> decision_provisional
decision_provisional -> appeal_open -> final_decision | decision_reversed
final_decision -> settlement_authorization_pending -> RFC-0008 settlement lifecycle
```

An accepted deliverable with no challenge may follow the predeclared cooperative close path. A challenge MUST identify the relevant WorkItem term version, acceptance criterion, disputed evidence, requested remedy, and deadline-policy reference. A case is not opened merely because a customer submitted a low rating; feedback can be evidence, but must be scoped to the agreed terms and handled with privacy safeguards.

Mediation seeks a voluntary settlement. The parties may jointly sign full payment, partial payment, revision, or refund terms when allowed by the frozen WorkItem. The protocol records the exact proposal and each party's acceptance. A mediator may facilitate and explain options; a mediator proposal has no spending effect unless both parties accept it or a separately specified adjudication rule authorizes a later decision.

If mediation fails, a qualified independent adjudicator may issue a reasoned, signed provisional decision under the frozen task criteria and case policy. The decision MUST state the evidence references, criteria applied, conflicts disclosed, remedy, and policy version. It MUST NOT claim certainty beyond the available evidence. A party may appeal within the policy's appeal window; the appeal MUST identify a procedural error, undisclosed conflict, material new evidence, or misapplication of frozen criteria. An appeal stays disputed settlement authorization until resolved.

Appeal reviewers must not include the original mediator/adjudicator or a conflicted party. A panel is not automatically independent merely because it has three identities. Panel size, selection, quorum, deadlines, and whether appeal is limited to one level remain unresolved parameters; no default numbers are implied here.

## 6. AI assistance and human attestations

AI may summarize evidence, map it to declared acceptance criteria, detect missing artifacts, or propose questions. Any AI output is an untrusted, reproducible-or-not advisory attachment: it is not a verdict, proof of work, or proof that a human reviewed the case. Record model and prompt metadata only when the policy requires it and doing so does not disclose private data; never make such metadata a substitute for a responsible decision-maker.

A human may sign an attestation that they reviewed specified evidence and accept responsibility for a decision. A comprehension quiz, signed statement, interaction log, or response time is not cryptographic proof of reading or understanding. These may be review signals, but must not be represented as proof. The protocol cannot establish human cognition from a signature.

## 7. Selection, randomness, and bonds — unresolved

ADR-0006 proposed selecting a mediator using the first Bitcoin block after a claim. This draft does not accept that mechanism. The candidate roster, eligibility snapshot, case context, policy version, and claim event would need to be committed before the seed is knowable. A protocol would also need defined behavior for retries, non-acceptance, unavailable candidates, reorganization, seed withholding/grinding, and candidate-set manipulation. A future Bitcoin block hash alone does not solve those issues.

No random-selection algorithm, bond amount, bond slash, or reputation threshold is chosen here. Bonding can impose a financial barrier without proving independence; random selection can be manipulated or colluded with if the candidate set or retries are controllable. These mechanisms require explicit economic analysis and adversarial conformance cases before adoption. Until then, any roster is a supervised trust model and must be labeled as such.

## 8. Events and evidence record

The following are semantic event names; canonical schemas and identifiers remain subject to RFC-0004 and RFC-0005:

- `work_item.submitted` (defined by RFC-0003) — exact term version, artifact/revision digests, evidence access references, and submitter signature. RFC-0013 does not define a second submission event for the same delivery.
- `work_item.validation_attested` (shared with RFC-0003) — validator identity, decision, criterion-level rationale, conflict declaration/check result, policy version, and evidence references.
- `dispute.opened` — parties, case scope, contested criteria, requested remedy, deadlines policy, and evidence commitment/access policy.
- `dispute.mediator_assigned` — selection method, frozen roster digest, eligibility/policy version, acceptance, conflict declaration, and assignment proof. It MUST NOT imply funds can be spent.
- `dispute.proposal_made` / `dispute.proposal_accepted` — proposal digest and explicit signatures from each accepting party.
- `dispute.mediation_failed` — no agreed outcome by the applicable process condition; timeout alone assigns no fault.
- `dispute.decision_provisional` — adjudicator, rationale, remedy, evidence references, conflicts, and appeal deadline policy.
- `dispute.appeal_filed` / `dispute.appeal_decided` — grounds, panel/decision references, and outcome.
- `dispute.decision_finalized` — derives from an unappealed provisional decision or completed appeal under the configured policy; it preserves the complete history.
- `dispute.decision_corrected` — append-only correction/reversal with the superseded event and reason.
- `work_item.settlement_authorization_requested` — final decision reference and exact RFC-0008 settlement plan. It does not authorize a spend unless RFC-0008 policy and script conditions also pass.

Sensitive evidence SHOULD remain off public append-only logs. Events may carry content-addressed encrypted references or commitments, with scoped access and retention rules. A public digest can prove that a later-presented artifact matches a commitment; it does not prove that the artifact is true, complete, or admissible.

## 9. Settlement and finality boundary

`dispute.decision_finalized` is not equivalent to `treasury.payout_settled`, `treasury.refund_settled`, or `work_item.paid`. RFC-0008 chain verification and spend-path conditions remain mandatory. No implementation may treat a mediator signature plus one party's signature as a safe real-money settlement path until an audited script/profile enforces the intended authority or the remaining trust assumptions are explicitly approved.

For the initial RFC-0008 `regtest` profile, disputed payouts and mediator-assisted spending remain disabled until the script and signer policy have been reviewed jointly. The protocol may record simulated decisions and proposed settlement plans without signing or broadcasting funds. No timeout, silence, AI score, appeal expiration observed on one local clock, or invalid/unavailable mediator may silently trigger a unilateral spend. Refund and recovery require the explicit RFC-0008 policy and script path.

## 10. Reputation and payment separation

Payment resolution and contribution-proof eligibility are separate decisions. A conflict, review failure, appeal, or reputation hold MUST NOT silently erase a legitimate payment claim. Conversely, payment or a favorable verdict alone does not prove independent demand or create a mature reputation proof. RFC-0006 controls provisional, challenge, correction, and revocation status. Consequential use of reputation remains blocked until RFC-0006's integrity gate is met.

## 11. Required conformance and adversarial cases

Before implementation is considered conformant, deterministic fixtures MUST cover at least:

1. creator/worker attempting to validate or mediate their own case;
2. two related or colluding identities attempting to bypass role separation;
3. undisclosed conflict found after a provisional decision;
4. mediation accepted by only one party, then mutually accepted, versus timeout/no response;
5. appeal filed during the window and a late appeal under the same frozen policy;
6. AI recommendation differing from the signed human decision, and missing/unavailable AI;
7. a reviewer attestation that cannot establish proof of reading;
8. duplicate or inaccessible evidence, changed WorkItem terms, and conflicting event histories;
9. appeal reversal after provisional reputation or payout authorization was requested;
10. mediator unavailable, roster changed after commitment, retry/grinding attempt, or Bitcoin reorganization affecting a proposed seed;
11. final decision with an incompatible or unreviewed Bitcoin spend path;
12. payment decided while reputation remains withheld, and reputation correction without silent event-history rewrite.

All financial scenarios remain synthetic or on isolated `regtest`; this RFC does not authorize real BTC. Independent review must include protocol security, Sybil/collusion analysis, privacy, Bitcoin script/key analysis, and economic accessibility.

## 12. Open decisions and launch gates

The following remain open and MUST be resolved before dispute-driven real-money settlement:

1. Initial validation domains, reviewer criteria, evidence standards, and acceptable levels of automation.
2. Supervised bootstrap roster and transition criteria to open participation.
3. Conflict declarations, related-identity evidence, challenge process, and false-positive remedy.
4. Mediator selection: committed roster, unbiased-enough seed, non-acceptance, retry limits, reorgs, and unavailable candidates.
5. Whether bonds exist, their sizing/accessibility, custody, return/slashing authority, and appeal safeguards.
6. Case deadlines and trusted time/block-height source; no timeout implies fault or unilateral recovery by default.
7. Appeal scope, panel composition, quorum, cost, and bounded finality.
8. Evidence confidentiality, access, retention, and deletion/cryptographic-erasure rules.
9. A Bitcoin script/key design that matches the decision policy, protects against one mediator plus one party spending contrary to the final decision, and handles recovery safely.
10. Whether any optional role attestation or reputation dimension is appropriate; no transferable-token weight is assumed.

Until these gates are resolved and independently reviewed, RFC-0013 is a design draft, mediator selection is not protocol-secure, disputed Bitcoin spends remain disabled, and real-money task settlement must not use this workflow.

## 13. References

- [Bisq Trading Rules and Dispute Resolution](https://docs.bisq.network/trading-rules.html) — Bisq 1 documentation; use as a design reference, not as an Alkaest specification.
- [Bisq trade protocols](https://bisq.network/blog/bisq-trade-protocols/) — official overview of mediation/arbitration boundaries in Bisq 1.
- [Bisq 2 dispute resolution](https://github.com/bisq-network/bisq2/wiki/Dispute-resolution) — protocol-specific Bisq 2 design notes.
- [Alkaest reputation integrity threat model](../research/reputation-integrity-threat-model.md).
- [Alkaest RFC-0008 — Bitcoin Escrow and Settlement](0008-bitcoin-escrow-and-settlement.md).
- [Alkaest treasury, DAO, Bitcoin and RFC cross-review](../handoff/treasury-dao-bitcoin-rfc-cross-review.md).
