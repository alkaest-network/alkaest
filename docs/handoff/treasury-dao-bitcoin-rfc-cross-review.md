# Treasury, DAO, Bitcoin and RFC Cross-Review

**Date:** 2026-10-19  
**Status:** Design review record; no protocol decision or implementation approval  
**Scope:** ADR-0007, ADR-0008 and Draft RFC-0014, cross-checked against ADR-0004, ADR-0006, RFC-0003, RFC-0004/0005 and the existing paid-work cross-review.

This review applies four specialist lenses: protocol security, DAO governance, Bitcoin settlement, and specification quality. It is a documentation review, not a code audit, legal opinion, Bitcoin script audit, or authorization to move funds. Follow-up: Draft RFC-0008 and Draft RFC-0013 now exist. They address settlement-state separation and a `regtest`-only on-chain interface, plus a conservative dispute lifecycle; script/key choice, mediator selection, refund, and production chain-proof rules remain unresolved.

## Summary

The high-level boundaries are coherent: no token issuance is authorized; reputation is separate and gated; Bitcoin is for future settlement and treasury audit commitments; Alkaest nodes validate signed protocol events rather than replaying Bitcoin as global protocol state; and the treasury agent is not a policy root or its own mediator.

RFC-0014 and RFC-0008 are not ready to define a real-money pilot. The blocking gap is the bridge from an agent's policy-level approval to independently enforceable spending and settlement: a signature and a policy document do not by themselves constrain a key that can sign arbitrary transactions. RFC-0008 now names that limitation and leaves production controls, Bitcoin chain verification/finality, and safe escrow paths unresolved. RFC-0013 must define selection, disputes and appeals. No implementation should treat these drafts as sufficient for real funds.

## Findings

### P1 — Per-task policy caps may not constrain a compromised allowance key

**Sources:** [ADR-0006, §5–6](../decisions/ADR-0006-self-funding-treasury-and-maintainer-agent.md); [RFC-0014, §5, §8, §10](../rfc/0014-treasury-agent-and-release-authorization.md).

ADR-0006 says the agent alone controls the operating allowance, while RFC-0014 says a compromised agent's loss is bounded by the allowance and per-task limits. The documents do not specify whether the agent key can sign arbitrary spends from that allowance or whether a separate signer/policy engine enforces per-task, period, recipient, and replay limits before signing. If the key can spend the entire allowance directly, a policy cap recorded in the event log is auditable after the fact but does not prevent a malicious key from draining the allowance in one transaction.

**Required resolution:** Explicitly choose the accepted blast radius. Define the spend-control mechanism, key permissions, concurrent reservation accounting, and what happens when the policy engine or signer is unavailable. If the allowance itself is the only hard loss limit, state that clearly and size it to the maximum tolerated compromise loss; do not claim per-task limits cryptographically bound key compromise unless enforced by the signing path or spending conditions.

### P1 — Bitcoin escrow, confirmation, and reorganization rules are missing

**Sources:** [ADR-0006, §2–4](../decisions/ADR-0006-self-funding-treasury-and-maintainer-agent.md); [ADR-0007, decisions 5–8](../decisions/ADR-0007-autonomous-treasury-and-bitcoin-audit.md); [RFC-0014, §7, §9–11](../rfc/0014-treasury-agent-and-release-authorization.md).

ADR-0006 names a 2-of-3 Bitcoin multisig and Lightning hold invoices as early payment paths. RFC-0014 leaves script construction, cooperative and unilateral spend paths, timelocks, refund rules, transaction replacement, fee handling, and settlement finality to RFC-0008. It requires nodes to verify transaction inputs, outputs, fees, destinations, and escrow state, but does not define how a node obtains and validates Bitcoin chain state, which proof is sufficient, how many confirmations are required, or how a reorganization affects `paid`, refunds, and audit anchors. Alkaest has heterogeneous node profiles, so an unspecified trusted indexer or RPC endpoint would create a material authority boundary.

**Required resolution:** RFC-0008 must state the supported Bitcoin payment mode for the first simulation, script/spend paths, exact transaction invariants, proof/chain source and trust model, confirmation/finality policy, reorg handling, refund and timeout safety, and how nodes update a previously observed settlement. It must distinguish transaction broadcast, inclusion, confirmation threshold, and final protocol settlement. Lightning should have its own timeout and claim/settlement semantics; do not infer them from on-chain escrow rules.

**Follow-up:** Draft RFC-0008 now chooses on-chain BTC `regtest` as the first conformance target, names a P2WSH 2-of-3 candidate, specifies the settlement event stages and ledger-category transitions, and explicitly defers Lightning. The final script/key model, mediator, timeout/refund behavior, destination-control proof, and production chain trust/finality remain unresolved.

### P1 — Mediator selection is not yet resistant to timing, roster manipulation, or reorg ambiguity

**Sources:** [ADR-0006, §2](../decisions/ADR-0006-self-funding-treasury-and-maintainer-agent.md); [open questions on payment and mediator randomness](open-questions.md).

ADR-0006 derives a mediator draw from the first Bitcoin block after a claim, but does not freeze the eligible candidate set, claim event/height, or roster version before the random value becomes knowable. It also does not fully define reorg treatment, late or unavailable candidates, or how repeated claim attempts are limited. The stated cost of a miner withholding blocks does not address a requester or worker choosing when to claim, changing the candidate set, or retrying to obtain a preferred result. Since the mediator key is part of the escrow, this is also a fund-control decision.

**Required resolution:** Any future RFC-0013 selection profile must define a committed candidate snapshot and eligibility rule, a deterministic claim/draw reference, reorg and timeout behavior, retry limits, and an independently recomputable selection proof. Until that is specified and tested, describe selection as a proposed mechanism, not as unbiased or manipulation-resistant.

**Follow-up:** Draft RFC-0013 explicitly does not accept the first-post-claim Bitcoin block proposal and lists roster commitment, eligibility, reorgs, retries, candidate unavailability, and grinding resistance as open decisions. It does not claim an unbiased or manipulation-resistant selection method.

### P1 — The release diagram skips the independently confirmed settlement state

**Sources:** [RFC-0003, §9–11](../rfc/0003-development-workflow-module.md); [RFC-0014, §7–9](../rfc/0014-treasury-agent-and-release-authorization.md); [core RFC cross-review](core-rfc-cross-review.md).

At the time of this original finding, RFC-0003 distinguished `payout_authorized` from `paid`, with `paid` requiring settlement confirmation, but RFC-0014 listed `work_item.release_decided` and `treasury.payout_settled` without intermediate states. Its original diagram went from the agent's release decision directly to “Bitcoin escrow settles” and then an audit anchor; it did not show a pending/broadcast/observed/confirmed transition, settlement failure or reorg rollback/challenge, or which event changes the WorkItem to `paid`.

**Required resolution:** Keep release authorization, transaction creation/broadcast, observed inclusion, confirmation/finality, and protocol `paid` as distinct states/events. Define idempotent retries and failure/reorg transitions. An anchor commitment must not be treated as proof of payment, and a payout authorization must not advance the state to `paid`.

**Follow-up:** Draft RFC-0003 and RFC-0008 now define separate authorization, broadcast, observation, confirmation, refund, and reorganization states; RFC-0014's diagram reflects the same sequence. Cross-RFC event names and state vectors remain to be verified.

### P2 — External review and CI evidence has no complete verifier trust model

**Sources:** [RFC-0014, §6, §8, §10, §12](../rfc/0014-treasury-agent-and-release-authorization.md); [ADR-0007, decisions 3 and 8](../decisions/ADR-0007-autonomous-treasury-and-bitcoin-audit.md).

RFC-0014 correctly labels an unsigned-provider observation as an adapter attestation and asks for independent re-fetch where possible. It does not define how adapter identities are authorized, how their keys/providers are rotated or revoked, what a node verifies from a provider-signed result, or what happens if independent re-fetch is unavailable. “Required CI/security checks passed” is not deterministic evidence until the workflow definition, repository identity, run, commit, artifact/result digest, and verifier policy are bound together. An adapter signature proves the adapter made the attestation, not that the provider result is true.

**Required resolution:** Specify evidence classes and their assurance levels; adapter identity enrollment/revocation; exact binding to repository, immutable commit, workflow definition and run; independent verification requirements; and a fail-closed/escalation path for unverifiable evidence. Keep human quality judgment separate from machine-verifiable gates.

### P2 — ADR-0008 needs to distinguish “design the token” from “evaluate whether a token is needed”

**Source:** [ADR-0008, decisions 1–3 and consequences](../decisions/ADR-0008-token-design-before-issuance.md).

Decision 1 says to “design the native-token system before launch decisions,” while the consequences require comparing a BSQ-like design with a no-transferable-token baseline and say no token is committed. This can be read as committing to a token design before evaluating whether Alkaest should have one.

**Required resolution:** Clarify that the required deliverable is a comparative token-design RFC that evaluates the no-token baseline against candidate assets and roles; it does not presuppose that a native transferable token will be selected. Keep issuance and real-money governance gated by a separate ADR, security review, and legal/accounting review.

## Decisions and boundaries that passed this review

- ADR-0007 and RFC-0014 clearly separate Bitcoin settlement/audit anchoring from deterministic Alkaest event validation; no custom chain is required for event replay.
- ADR-0008 preserves BTC settlement and prohibits using transferable reputation. It explicitly withholds token issuance, sale, listing, distribution, and real-money token governance.
- RFC-0014 binds work to immutable revisions/digests, excludes PR/issue text and model output as payout-destination authority, requires independent review, and separates the treasury agent from its own mediation.
- RFC-0014 treats GitHub/CI and model output as evidence rather than protocol truth, and requires fail-closed handling for invalid or ambiguous economic inputs.
- The existing [paid-work cross-review](paid-work-cross-review.md) records remaining RFC-0008/RFC-0013 gaps and blocks real-money use pending their resolution.

## RFC-0008 scope recommendation and follow-up review

The Draft RFC-0008 now follows the recommendation to keep settlement and escrow mechanics separate from mediation rules. It chooses on-chain BTC in `regtest` as the first conformance target and explicitly marks the 2-of-3 P2WSH profile as a candidate whose spend-policy limits are not enforced by the script itself. Before implementation beyond isolated prototypes, review the remaining points below against the RFC text and resolve them with RFC-0013 where indicated:

1. Initial scope and exclusions: choose whether the first conformance target is BTC on-chain escrow only; keep Lightning, fiat collateral, and tokenized assets out unless separately specified.
2. Asset units and canonical amount representation, overflow bounds, fee ownership, transaction size/dust constraints, and exact funding/reservation accounting.
3. Escrow construction and every spend path: cooperative release, refund, timeout, cancellation, mediator-assisted outcome, lost/unavailable key, and milestone escrow. Bind outputs to the frozen WorkItem terms and contributor-signed destination instruction.
4. Bitcoin node/proof assumptions, chain selection, transaction validation, confirmations, reorgs, replacement/fee bumping, and safe state transitions from authorized to broadcast to confirmed settlement.
5. Event contract and idempotency: separate allocation, escrow funded, payout authorized, transaction observed, payout confirmed, refunded, and failed/contested outcomes. Define what is immutable and how conflicts block irreversible action.
6. Privacy: keep personal data and full workflow payloads off-chain; document that on-chain values and addresses are public and define address-control proof without placing secrets in protocol events.
7. Audit-anchor construction and recovery: canonical ordered input set, commitment format, cadence, fee policy, inclusion/confirmation/reorg behavior, omitted-event detection, and independent verification.
8. Valueless regtest scenarios and interoperable vectors for malicious signed amounts, altered outputs, replay, concurrent spend attempts, key loss, timeout races, reorgs, and no-partial-state-mutation.

## Review sequence

1. Resolve the P1 boundaries above in ADR/RFC text; do not treat this report itself as normative.
2. Cross-review Draft RFC-0008, RFC-0013, and RFC-0014 together; keep the mediator-spend path disabled until their authority and script rules agree.
3. Resolve the remaining script/key, refund, proof/finality, and destination-control questions, then produce transaction/state vectors before implementation.
4. Keep all work valueless on `regtest` until RFC-0008 and RFC-0013 are accepted and the launch gates are independently verified.

## Source documents

- [ADR-0004 — Token and Settlement Direction](../decisions/ADR-0004-token-and-settlement-direction.md)
- [ADR-0006 — Self-Funding Treasury and Task Bounties](../decisions/ADR-0006-self-funding-treasury-and-maintainer-agent.md)
- [ADR-0007 — Autonomous Treasury and Bitcoin Audit Trail](../decisions/ADR-0007-autonomous-treasury-and-bitcoin-audit.md)
- [ADR-0008 — Design a Native Token Before Considering Issuance](../decisions/ADR-0008-token-design-before-issuance.md)
- [RFC-0003 — Development Workflow Module](../rfc/0003-development-workflow-module.md)
- [RFC-0008 — Bitcoin Escrow and Settlement](../rfc/0008-bitcoin-escrow-and-settlement.md)
- [RFC-0014 — Treasury Agent and Release Authorization](../rfc/0014-treasury-agent-and-release-authorization.md)
- [Paid-work pilot cross-review](paid-work-cross-review.md)
- RFC-0008 and RFC-0013 are Draft; neither has been independently audited or authorizes real funds.
