# Alkaest Documentation

This directory contains the living architecture and research record for Alkaest. The repository's [README](../README.md) introduces the project; this page is the map for contributors and reviewers.

## Read in this order

1. [Vision](overview/vision.md) — what Alkaest aims to become and what remains conceptual.
2. [Current state](handoff/current-state.md) — what exists in this repository and the current maturity of each area.
3. [Roadmap](overview/roadmap.md) — prioritized work and launch gates.
4. [Glossary](overview/glossary.md) — stable protocol terms.
5. [Architecture decisions](decisions/README.md) — accepted directions and unresolved choices.
6. The relevant [RFC](#rfc-specifications) — proposed protocol behavior.
7. Research documents — threat models and external references that inform, but do not themselves finalize, protocol rules.

## Documentation authority

- **Vision and overview documents** state intent and product context. They do not override an ADR or an RFC.
- **ADRs** record decisions and constraints. An ADR marked “direction” may leave implementation details open.
- **RFCs** specify protocol behavior. `Draft` does not mean implemented or safe for production.
- **Research** records evidence, analysis, and candidate mitigations. A research recommendation becomes binding only when adopted in an ADR or RFC.
- **Handoff documents** are working navigation aids, kept aligned with the roadmap and decision index.
- **WHITEPAPER.md** is historical/conceptual origin material; consult current `docs/` specifications for live direction.

No document in this repository by itself authorizes real-money operation, token issuance, public sale, production reputation scoring, or autonomous mainnet treasury spending. Those capabilities require the explicit launch gates listed in the relevant ADRs and RFCs.

## RFC specifications

| RFC | Topic | Current maturity |
|---|---|---|
| [0001](rfc/0001-protocol-core.md) | Protocol core | Draft; cross-reviewed with RFC-0002–0005, implementation and independent review pending |
| [0002](rfc/0002-node-architecture.md) | Node architecture | Draft; cross-reviewed with RFC-0001 and RFC-0003–0005, boundary limits and implementation review pending |
| [0003](rfc/0003-development-workflow-module.md) | Open-source development workflow | Draft; lifecycle, role separation, funding/settlement projections and evidence provenance specified; schema conformance, cross-RFC review, security and reputation integration pending |
| [0004](rfc/0004-envelope-canonical-encoding-and-object-ids.md) | Encoding, signatures, IDs | Draft; JCS, encodings and domain-separated IDs specified; [known-answer vectors drafted](rfc/vectors/rfc-0004.json), independent implementation and security review pending |
| [0005](rfc/0005-object-event-semantics-and-state-resolution.md) | Event semantics and deterministic state | Draft; unresolved conflicts and authorized resolution specified; [state-machine vectors drafted](rfc/vectors/rfc-0005.json), authority schemas and independent implementation review pending |
| 0006 | Reputation proofs and integrity | Not written; see [next tasks](handoff/next-tasks.md); launch-blocking for consequential reputation use |
| [0007](rfc/0007-service-scheduling-module.md) | Service scheduling | Draft; backend chatbot integration and private multi-node validation precede protocol-facing discovery/reputation screens |
| [0008](rfc/0008-bitcoin-escrow-and-settlement.md) | Bitcoin escrow and settlement | Draft; `regtest`-only profile, script/key, mediator, refund, and production chain-verification gates unresolved |
| [0009](rfc/0009-node-api-and-sdk-contract.md) | Node API and SDK | Draft; stabilize after core semantics |
| [0010–0012](overview/roadmap.md) | Data availability, permissions, governance/versioning | Planned; not written |
| [0013](rfc/0013-validation-dispute-resolution-and-appeals.md) | Validation, dispute resolution and appeals | Draft; selection, bonds, deadlines, Bitcoin spend path and independent review remain unresolved |
| [0014](rfc/0014-treasury-agent-and-release-authorization.md) | Treasury agent and payout authorization | Draft; security, escrow, policy, and test gates required |

Missing RFC numbers are intentional gaps, not specifications. Do not create numbered specifications by assuming an existing description is an accepted rule.

## Architecture decisions

- [Decision index](decisions/README.md) — status and open boundary of ADR-0001 through ADR-0010.
- [ADR-0009 — Resource-Aware Node Capacity and Deployment](decisions/ADR-0009-resource-aware-capacity-and-deployment.md) — Proposed; no Kubernetes dependency in the protocol or MVP
- [ADR-0010 — Decentralized Source and Site Hosting](decisions/ADR-0010-decentralized-source-and-site-hosting.md) — Accepted; Radicle is the canonical forge for code, patches and paid work, GitHub a mirror; [seed node over Tor](operations/radicle-seed-node.md)

## Overview and handoff

- [Roadmap](overview/roadmap.md)
- [Network rollout plan](overview/network-rollout-plan.md)
- [Alkaest Search](overview/alkaest-search.md)
- [Chatbot-to-Network strategy](overview/chatbot-to-network-strategy.md)
- [Current state](handoff/current-state.md)
- [Next tasks](handoff/next-tasks.md)
- [Draft first network WorkItem — professional brand identity](handoff/first-brand-identity-workitem.md)
- [Draft remunerated Flutter WorkItems](handoff/flutter-paid-workitems.md)
- [Open questions](handoff/open-questions.md)
- [RFC-0001–0005 consistency review](handoff/core-rfc-cross-review.md)
- [Paid-work pilot cross-review](handoff/paid-work-cross-review.md)
- [Draft contributor starter issues](handoff/contributor-starter-issues.md) — proposed unassigned documentation tasks; not yet published as GitHub issues
- [Treasury, DAO, Bitcoin and RFC cross-review](handoff/treasury-dao-bitcoin-rfc-cross-review.md)
- [Brain and treasury decision rehearsal](handoff/brain-treasury-simulation-scenarios.md)
- [Offline treasury reference prototype](../tools/treasury_sim.py) and [unit tests](../tests/test_treasury_sim.py) — arithmetic and policy-gate rehearsal only; no Bitcoin Core or protocol integration

## Contributor onboarding and project origin

- [Contributor page](https://alkaest-network.org/contribute/) — source in [`site/contribute/`](../site/contribute/index.html)
- [Contribution guide](../CONTRIBUTING.md)
- [Code of Conduct](../CODE_OF_CONDUCT.md)
- [Security policy](../SECURITY.md)
- [Open issues](https://github.com/alkaest-network/alkaest/issues)
- [Original whitepaper](../WHITEPAPER.md) — historical concept; current constraints live in ADRs and RFCs.

## Brand

- [Visual identity](brand/visual-identity.md) — selected identity references and practical guidance for applying them.

## Research

- [Bisq DAO and Alkaest token](research/bisq-dao-and-alkaest-token.md)
- [Long-term continuity requirements](research/long-term-continuity-requirements.md)
- [Mobile work evidence and location assurance](research/mobile-work-evidence-and-location-assurance.md)
- [Reputation integrity threat model](research/reputation-integrity-threat-model.md)
- [Bisq May 2026 incident and Alkaest mitigations](research/bisq-may-2026-incident-and-alkaest-mitigations.md)
- [Bisq 2 resource bounds and conflict authority options](research/bisq2-resource-bounds-and-dispute-authority.md)
- [Professional tools integration pilot](research/professional-tools-integration-pilot.md)
- [JHipster GitHub bounty model](research/jhipster-bounty-model.md)
- [Alkaest paid work pilot design](research/alkaest-paid-work-pilot-design.md)
- [Bisq compensation and Bisq 2 protocol patterns](research/bisq-compensation-and-bisq2-protocol-patterns.md) — separates Bisq DAO's post-delivery contributor compensation from Bisq 2 trade protocols and compares relevant patterns with Alkaest's first pre-funded WorkItem.
- [Bitcoin payouts and optional Bisq conversion](research/bitcoin-payouts-and-bisq-conversion.md) — records the intended BTC contributor-payment direction and the boundary between Alkaest settlement and a contributor's optional peer-to-peer fiat trade.

## Diagrams

- [System overview](diagrams/system-overview.md)
- [Node architecture](diagrams/node-architecture.md)
- [Request lifecycle](diagrams/request-lifecycle.md)
- [Chatbot-to-Network progression](diagrams/chatbot-to-network.md)
