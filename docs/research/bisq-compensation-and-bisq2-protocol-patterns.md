# Bisq Compensation and Bisq 2 Protocol Patterns

**Status:** Informative research; not an Alkaest protocol decision.  
**Reviewed:** 2026-10-19

## Scope and important distinction

“Bisq 2” and “the Bisq DAO compensation process” are related parts of the Bisq ecosystem, but they are not the same protocol. Bisq 2 currently describes itself as a platform for multiple trade protocols; its initial released protocol is Bisq Easy. Contributor compensation requests and BSQ issuance are governed by the Bisq DAO process, historically implemented in Bisq 1 and Bitcoin-based DAO transactions. Do not describe the DAO compensation workflow as a Bisq 2 trade protocol.

The Alkaest use case is also different: the founder wants to seed project funds and open a **pre-funded WorkItem** to hire a brand identity professional, then exercise the work, evidence, review, and payout flow. Bisq's retrospective compensation request is a useful comparison, but it does not itself provide this escrowed task-bounty model.

## What the Bisq DAO compensation flow does

The documented workflow is roughly:

1. The contributor discusses planned work and an approximate compensation expectation with other contributors or team leads before starting, where practical.
2. The contributor completes and publishes the work. Planned or in-progress work is not eligible under the guide's normal rule; merged work is an example of delivered work.
3. The contributor opens a detailed compensation issue in the dedicated GitHub repository. A bot checks formatting, and contributors/team leads review the request.
4. The contributor submits a compensation proposal in the Bisq DAO with the issue reference and requested amount. The request enters a recurring proposal and voting cycle; stakeholders review and vote.
5. If accepted, BSQ issuance follows the DAO result. The contributor links the proposal transaction ID back to the issue so the request and on-chain record can be cross-referenced.

This is **post-delivery compensation**, not a promise that a task is funded before work starts. GitHub carries human-readable proposal metadata; the DAO transaction commits to proposal data and voting/result state. The process has a lead-review convention and broad stakeholder vote, not an automatic PR-approval trigger.

## Relevant Bisq 2 trade-protocol patterns

Bisq 2's protocol design discussions describe explicit trade state machines. The patterns relevant to Alkaest are:

- Define allowed state transitions from an event and current state, so invalid transitions are rejected by construction.
- For inbound events, validate first, compute changes without mutating the durable model where feasible, and commit only after processing succeeds.
- If an external side effect such as a wallet operation cannot be rolled back, split the transition so the recorded protocol state accurately reflects the side effect boundary.
- Treat ordering, duplicate/late messages, errors, and recovery as protocol cases. Bisq's discussion notes limitations in its then-current FSM (including queued events not being persisted and weak structural enforcement across branches); these are cautions to address, not features Alkaest should copy.
- Keep security, dispute mechanisms, and required deposits specific to each trade protocol rather than assuming one mechanism fits every workflow.

Bisq Easy's dispute guidance emphasizes direct encrypted trade chat first, then mediation. Because Bisq Easy has no security deposit, a mediator's powers are limited. This illustrates a general tradeoff: dispute resolution cannot guarantee a financial outcome when funds were never reserved or escrowed.

## What Alkaest can adapt for its first funded WorkItem

The following are candidate design lessons for the first Alkaest task flow; they do not supersede RFCs or authorize real funds:

1. **Publish the scope and compensation expectation before work begins.** The first brand-design WorkItem should state deliverables, milestones, acceptance criteria, asset/source-file requirements, licensing or ownership terms, budget cap, reviewer, deadline, and dispute path.
2. **Separate a pre-funded bounty from retrospective compensation.** Alkaest should model funding reservation and payout/refund explicitly. A request for compensation after delivered work is a separate workflow and should not be represented as an escrowed bounty.
3. **Keep human-readable evidence and protocol commitments linked.** Preserve a detailed task record and bind it to signed WorkItem events and settlement identifiers/digests, while keeping private commercial or personal details out of public replicated data.
4. **Make review visible, but separate roles.** A task funder, assignee, reviewer, mediator, and payout authority should be recorded as distinct protocol roles. A signature or role label alone does not prove independent people; apply the anti-Sybil and conflict limits in the reputation threat model.
5. **Use an explicit lifecycle and atomic transitions.** Candidate flow: `draft -> published -> funding_pending -> funded -> assigned -> in_progress -> submitted -> accepted | disputed -> payout_authorized -> settled`, with explicit `cancelled`, `rejected`, `expired`, and `refunded` outcomes. Define these states and allowed transitions in the owning RFC before implementation.
6. **Do not equate PR approval with payment authorization.** PR/CI results can be evidence from an adapter, but acceptance and payout must follow the WorkItem's predeclared policy, independent review requirements, exact amount/destination validation, and dispute window.
7. **Rehearse with valueless infrastructure first.** Exercise task publication, funding reservation, replays, failures, disputes, and refund paths in local/no-value or Bitcoin `regtest` environments. Do not transfer founder funds to an unspecified prototype wallet.

For the brand task specifically, split acceptance into objective deliverables (editable marks, token definitions, usage rules, application examples, and agreed source files/licenses) plus human quality review. If subjective design acceptance is disputed, do not have an AI model make the final quality judgment or control the payout.

## Applicability limits

- Bisq DAO compensation issues pay contributors after completed work through BSQ issuance and recurring stakeholder voting; Alkaest's desired first task is funded up front from a project treasury and should have an explicit reservation/settlement lifecycle.
- Bisq's trade FSM handles trade-specific interactions. It is not directly reusable as the Alkaest WorkItem state machine.
- Bisq's voting/BSQ token model should not be imported wholesale. Alkaest's token and governance decisions remain open under ADR-0008; the first task can be funded and tested without an Alkaest token.
- GitHub issue references and CI results can be replaceable integrations in Alkaest, not protocol authorities.

## Sources

- [Bisq 2 repository](https://github.com/bisq-network/bisq2) — describes Bisq 2's multiple trade-protocol direction and Bisq Easy's role.
- [Bisq 2 FSM and MuSig protocol discussion](https://github.com/bisq-network/bisq2/discussions/3108) — state-machine design, validate/process/commit approach, out-of-order events, side-effect considerations, and acknowledged limitations.
- [Making a compensation request](https://bisq.wiki/Making_a_compensation_request) — contributor expectations, delivered-work criterion, issue review, DAO proposal, and voting workflow.
- [Compensation](https://bisq.wiki/Compensation) — contributor, compensation-maintainer, and stakeholder roles.
- [DAO technical overview](https://bisq.wiki/Bisq_DAO_technical_overview) — DAO proposal/voting cycle and transaction/data model.
- [Dispute resolution in Bisq 2](https://bisq.wiki/Dispute_Resolution_in_Bisq_2) — trade-chat and Bisq Easy mediation model and its limits without deposits.
- [Bisq getting started](https://bisq.network/getting-started/) — Bitcoin wallet/trade flow and the fact that fiat payment is external to Bisq.
- [Bisq 2 overview](https://bisq.wiki/Bisq_2) — distinction between Bisq applications, planned protocol choices, and wallet direction.
