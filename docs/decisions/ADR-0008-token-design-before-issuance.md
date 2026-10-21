# ADR-0008 — Design a Native Token Before Considering Issuance

**Status:** Accepted direction; token mechanics unresolved  
**Date:** 2026-10-18  
**Decision Type:** Economic and Governance Architecture  
**Related:** ADR-0003, ADR-0004, ADR-0006, ADR-0007, RFC-0003, RFC-0008, RFC-0014, [Bisq DAO and Alkaest Token Research](../research/bisq-dao-and-alkaest-token.md)

## Context

Alkaest's intended scope is broader than one product DAO: the protocol may coordinate its own development, independent projects, service providers, node operators, mediators, and future AI agents. The project needs to understand how shared protocol funding and governance could work at that scale before implementation hardens assumptions.

Bisq's BSQ demonstrates an integrated DAO asset for contributor compensation, voting, and product fees, verified through the Bisq protocol and Bitcoin. Alkaest's multi-project scope introduces additional boundaries: protocol treasury versus project treasury, governance versus service access, project-local decisions versus shared constitutional decisions, and transferable economic assets versus non-transferable reputation.

ADR-0004 selected Bitcoin for future settlement and explicitly deferred token issuance. This ADR supersedes only the implication that token architecture can wait until after real usage. It does not supersede Bitcoin as the settlement/audit direction, the no-custom-chain constraint, or the prohibition on tokenizing reputation.

## Decision

1. **Design the native-token system before launch decisions.** Token purpose, rights, governance scope, treasury boundaries, issuance rules, and risk controls must be documented and simulated before Alkaest enables token functionality in production.
2. **Do not issue, sell, list, distribute, or enable real-money token governance yet.** This ADR authorizes research and valueless local/testnet simulations only. Mainnet issuance requires a separate ADR, legal/accounting review, security review, and explicit launch gates.
3. **Do not assume one asset should serve every role.** Token governance, project budgets, settlement, service access, and credentials are separate design concerns until evidence justifies combining them.
4. **Reputation remains non-transferable.** It must be derived from verifiable evidence and cannot be bought, sold, staked, or transferred (ADR-0004).
5. **Reputation integrity is a launch gate.** No reputation score or contribution proof may affect production authority, material ranking, funding eligibility, governance, or treasury limits until RFC-0006 addresses self-dealing, Sybil identities, collusion, related-party payouts, task splitting, independent validation, appeals, and privacy tradeoffs. See [Reputation Integrity Threat Model](../research/reputation-integrity-threat-model.md).
6. **Preserve the Bitcoin settlement and audit direction.** A future governance or incentive token does not automatically replace BTC settlement, escrow, or Bitcoin audit commitments (ADR-0004, ADR-0007).
7. **Keep protocol treasury authority separate from project budgets.** Projects may adopt local economic rules, but cannot spend shared protocol funds without an explicit authorization path. Cross-project allocations must be visible as signed protocol decisions.
8. **Bound automated treasury actors.** An AI agent may execute only pre-authorized budget and policy decisions. It cannot change issuance policy, increase its authority, mint for itself, or adjudicate its own work or disputes (ADR-0007, RFC-0014).
9. **Do not build a custom chain for this purpose.** Evaluate existing settlement/asset layers against deterministic validation, independent node verification, privacy, fees, UX, migration, security, and legal requirements.
10. **Require an attack and legal review before design approval.** At minimum, evaluate concentration, Sybil attacks, vote buying, apathy/quorum failure, conflicts of interest, treasury capture, emergency issuance, key loss, and jurisdiction-specific obligations.

## Consequences

- Token economics become an explicit architecture workstream before production token assumptions appear in code or marketing.
- No token launch date, supply, ticker, price, allocations, revenue rights, or chain is committed by this decision.
- Project payments can continue to be modeled as pre-funded WorkItems and settled under ADR-0004/RFC-0008 without waiting for a token.
- The design must compare a BSQ-like model with alternatives and a no-transferable-token baseline; inspiration from Bisq is not a requirement to copy its compensation cadence, voting, or asset representation.
- Legal obligations may vary according to the token's actual rights, offer, trading, custody, and services. A “utility token” or “DAO” label is not a legal conclusion.
- Token design cannot rely on reputation as a Sybil-resistant shortcut; the reputation integrity launch gate is independent and mandatory.

## Required next work

The research document `docs/research/bisq-dao-and-alkaest-token.md` captures the current baseline and open questions, including contributor rewards, mediator bonds, burns, and the distinction between Bitcoin's issuance horizon and adoption. The [long-term continuity requirements](../research/long-term-continuity-requirements.md) record founder-loss, key-compromise, treasury-capture, governance-deadlock, maintainer, and fork scenarios; these are candidate requirements until adopted by their owning ADRs/RFCs. Before token implementation, create a token design RFC covering roles and rights, scopes, supply and issuance, burns and locks, governance, treasury flows, distribution, succession/recovery, deterministic validation, security, migrations, and legal gates. Simulate multi-project operations and continuity failures with valueless test data first.
