# Research: Reputation Integrity and Self-Dealing Resistance

**Status:** Required design work before reputation can influence launch decisions  
**Date:** 2026-10-18  
**Related:** ADR-0003, ADR-0004, ADR-0006, ADR-0007, ADR-0008, RFC-0003, future RFC-0006

## Problem

Reputation derived from completed work can be manipulated if one participant can create a task, assign it to an identity they control, approve the work, and claim a contribution proof. Repeating this loop can manufacture apparent track record without independent demand or value delivered. The same attack can use multiple identities, friendly reviewers, shell projects, split tasks, circular payments, or a colluding group.

This is a launch-blocking integrity problem if reputation affects access, trust, ranking, governance, funding, or other consequential decisions. A token, payment, GitHub merge, or signed event does not independently prove that useful work happened.

## Threat model

Assume an attacker can:

- create and control multiple cryptographic Identities;
- create Spaces and WorkItems, or recruit a colluding project maintainer;
- submit trivial, duplicated, self-serving, or deliberately reversible work;
- control or collude with a reviewer, mediator, sponsor, or treasury agent integration;
- recycle funds or pay themselves through related identities;
- split one task into many small tasks to exploit per-task thresholds;
- accumulate legitimate history and later use it to gain influence;
- exploit incomplete, delayed, or private evidence.

Assume protocol participants cannot generally prove that two pseudonymous Identities belong to different human beings without introducing an identity, privacy, or centralization tradeoff. The protocol therefore must not claim universal Sybil resistance from signatures alone.

## Required design controls to evaluate

These are protocol requirements for the future reputation RFC, not yet a final scoring formula:

1. **Role separation:** the task creator/funder, assignee, validator, mediator, and payout destination must be recorded as distinct protocol roles. An identity must not validate its own submission or mediate its own task.
2. **Conflict declarations and graph checks:** capture declared control/affiliation links and check protocol-visible relations among project, funder, assignee, validators, and payout identities. A detected conflict excludes or downgrades the contribution proof and can trigger review. Absence of a declared link is not proof of independence.
3. **Independent demand:** contribution weight should depend on evidence that an independent beneficiary wanted and used the result, not merely on the existence of a task, payment, merge, or approval. Define domain-specific evidence and avoid leaking unnecessary personal data.
4. **Validator diversity:** higher-impact proofs require reviewers from distinct, eligible identities and histories, with risk-based thresholds. Multiple identities controlled by one person remain a residual risk unless additional assurance mechanisms are adopted.
5. **Funding provenance and payout loop detection:** preserve the source and movement of task funding. Detect circular flows, self-funding, same-controller payout paths where observable, and repeated related-party transactions. BTC transaction tracing alone cannot establish real-world beneficial ownership.
6. **Novelty and aggregation:** detect near-duplicate work, repeated low-value tasks, task splitting, reciprocal contribution rings, and correlated approval patterns. Score or cap correlated evidence as a group, with transparent, appealable rules.
7. **Delayed and revocable evidence:** reputation proofs start provisional, mature after a challenge window or evidence of real use, and may be corrected or revoked through an explicit dispute process. Downstream systems must consume proof status and provenance, not just a number.
8. **Bounded consequences:** during early network operation, reputation should inform discovery and eligibility gradually. It must not alone authorize treasury access, irreversible governance control, or a high-value payout.
9. **Auditable decisions:** preserve signed evidence references, policy version, reviewers, conflict checks, and appeal outcome. Keep private evidence off public ledgers; publish commitments only where appropriate.
10. **Economic friction and limits:** evaluate funding deposits, rate limits, epoch caps, minimum independent review, and costs for repeated claims. These raise attack cost but do not prove unique personhood.
11. **Cross-Space safeguards:** reputation gained in one Space should not automatically confer authority in another. Domain, recency, evidence provenance, and transfer rules must be explicit.
12. **Governance separation:** do not let a reputation score silently convert to token voting weight. Any relationship between contribution history and governance requires a separate, explicit, attack-tested rule.

## Proposed MVP policy

The MVP should issue contribution proofs, not a fungible or globally comparable reputation score. Each proof records a domain, task, worker Identity, evidence, funding source (if any), beneficiary/project, validators, conflict checks, and status. A consumer derives only the view it needs from those proofs.

### Hard exclusions

- The same Identity cannot create/authorize and claim a task, validate its own submission, act as mediator, or select its own payout destination.
- A known related Identity cannot bypass those role constraints. A detected conflict blocks reputation credit pending review; it does not automatically erase payment rights for legitimate work.
- The same event (e.g. one PR, release, or service outcome) cannot generate multiple independent contribution proofs through task splitting or mirrored Spaces.
- Payment, task creation, self-reported completion, code merge, and an AI agent's acceptance are each insufficient alone to mature reputation.
- Reputation evidence cannot be transferred between Identities or converted directly into token voting weight.

### Proof lifecycle

1. **Submitted:** worker attaches evidence to a predeclared WorkItem and exact artifact/revision.
2. **Accepted for payment:** task-specific acceptance criteria pass and, where funded, the payout decision is independently auditable. Payment eligibility is separate from reputation eligibility.
3. **Provisional proof:** distinct eligible validators attest to the evidence; conflicts and duplicate-work checks pass. The proof is visible with provenance but carries no consequential authority.
4. **Mature proof:** after a challenge window and, for relevant domains, evidence of beneficiary use or an independent outcome, the proof can contribute to a domain-specific history. A challenge suspends maturity pending resolution.
5. **Corrected/revoked:** an appeal outcome can append a correction or revocation event. History is not silently rewritten; consumers must read the current proof status.

For the first Alkaest project, the bootstrap maintainers can authorize WorkItems, but a contributor cannot be the sole authorizer and validator of their own paid work. High-impact core, treasury, identity, or reputation changes require at least two independent reviewers under a predeclared rule. The final minimum and eligibility rules belong in RFC-0006 and RFC-0014.

### What "independent" means in the protocol

Independence is assessed from protocol-visible facts: distinct Identities and keys, distinct task roles, no declared affiliation/conflict, no shared funding or payout path where observable, reviewer eligibility, and absence of suspicious reciprocal or correlated patterns. It is a confidence assessment, not proof of separate human beings. If all parties collude and disclose nothing, a pseudonymous protocol cannot reliably discover common ownership by itself.

Where a use case needs stronger assurance, a Space can require an optional identity-assurance credential issued by a named attestor, with explicit scope, expiration, revocation, and privacy costs. This must not become a global mandatory real-name registry by default.

### Conservative influence

- Keep proof dimensions separate (e.g. domain, recency, validation strength, dispute status, and independence confidence); do not collapse them into one universal score in the MVP.
- Consumers define thresholds for their own context. No cross-Space authority is inherited automatically.
- Start with low caps and human review for consequential uses. Proof volume alone cannot raise treasury limits or grant governance authority.
- Detect and rate-limit clusters of correlated work/reviews/funding. Apply caps to related evidence clusters, not just individual tasks, and provide a documented appeal path.
- Preserve legitimate contributor payment even when reputation is withheld or challenged, unless the payment itself is disputed under its own rules.

### Test cases required for RFC-0006

The design must show expected outcomes for: one Identity opening and claiming its own task; two Identities controlled by one operator; circular funder/worker/reviewer groups; repeated reciprocal approvals; one contribution split into many WorkItems; copied or trivially changed artifacts; a real contributor with a disclosed affiliation; reviewer misconduct discovered after maturity; and a false-positive conflict appeal. Tests must distinguish payment decision, reputation proof status, and authority granted downstream.

No fixed financial bond is proposed for the MVP. A deposit can exclude low-resource contributors and still be funded by an attacker; evaluate rate limits, independent demand, validator diversity, and delayed influence first.

## Important design tension

Alkaest aims to support pseudonymous and multiple Identities per node. A strict one-person-one-Identity gate would conflict with that goal and would require identity verification or trusted attestations, which can exclude users and expose personal data. The protocol should first make self-dealing unproductive through role separation, independent demand, provenance, correlated-evidence analysis, and bounded influence. If a use case needs stronger personhood assurance, make it an explicit optional assurance tier with a documented privacy model; do not pretend signatures solve personhood.

## Launch gate

Before a reputation score or contribution proof affects production access, trust labels, rankings with material consequences, funding eligibility, protocol governance, or treasury limits, RFC-0006 MUST define:

- contribution-proof schema and evidence provenance;
- task/funder/worker/validator/mediator conflict rules;
- Sybil, collusion, wash-funding, duplicate-task, and task-splitting threat cases;
- independent-demand and validator-diversity requirements by risk tier;
- provisional status, challenge windows, appeals, correction, and revocation;
- privacy limits and optional identity-assurance tradeoffs;
- cross-Space portability and domain separation;
- influence caps and explicit prohibition on direct reputation-to-token conversion unless separately approved;
- test scenarios and measurable failure criteria.

Until then, reputation may be displayed only as clearly labeled raw, contextualized evidence and must not independently grant authority or funds.

## Open decisions

- What counts as independent demand in software, services, research, and other domains?
- Should reputation be a vector of evidence dimensions rather than one score?
- How are affiliation claims, conflicts, or collusion findings challenged without creating a public doxxing mechanism?
- Which optional uniqueness attestations, if any, provide sufficient benefit to justify their privacy and access costs?
- How does a protocol handle reviewers who later become affiliated with a contributor?
- Which evidence is public, encrypted to a Space, or represented only by a commitment?
