# Alkaest Paid Work Pilot Design

**Status:** Proposed supervised simulation; no real-money pilot is authorized.  
**Scope:** Alkaest-owned GitHub issues and pull requests only.  
**Inputs:** RFC-0003, ADR-0006/0007, RFC-0014, and the [JHipster bounty model analysis](jhipster-bounty-model.md).

## Objective

Demonstrate that Alkaest can make the lifecycle of a paid open-source task clearer and more auditable while preserving the contributor's familiar GitHub workflow. The simulation should test whether predeclared scope, funding state, acceptance evidence, role separation, and payout state reduce ambiguity enough to justify added process.

The pilot is not a launch of the marketplace, token, reputation scoring, mediator pool, or autonomous treasury. It does not contact or enroll JHipster or another external project.

## Pilot boundaries

- Use Alkaest-owned issues and a disposable test repository or clearly labeled simulated records.
- Use valueless simulated balances and payout receipts only. Do not solicit, custody, escrow, promise, or transfer real funds.
- Continue to use GitHub for issues, source control, pull requests, code review, and CI. Alkaest records references and decisions; it does not replace GitHub.
- Keep project maintainers responsible for issue scope and acceptance; require a reviewer who is not the requester or contributor for the simulation's approval event.
- Keep reputation, tokens, transferable rewards, and automatic payment execution out of the pilot.
- Do not publish a bounty label that could be confused with a guaranteed real payment. Mark simulated work `SIMULATION — NO REAL FUNDS` in every relevant interface and record.

## Baseline workflow to simulate

1. **Need proposed:** a maintainer or the simulated treasury agent creates an Alkaest `WorkItem` linked to a GitHub issue. The agent may draft; the maintainer decides whether the work is valid and in scope.
2. **Terms fixed:** before anyone is assigned, the WorkItem records deliverable, acceptance criteria, repository/base revision, amount and unit (simulation units only), budget source, maximum amount, due date, eligibility, reviewer, concurrency rule, and dispute/escalation route. Later scope or amount changes require a new signed decision and event history.
3. **Funding declared:** the simulation records `funding_reserved` only after the fictitious budget policy approves an allocation. The record must say `simulated`; no real account balance or escrow is implied. Work cannot enter `assigned` until this event exists.
4. **Exclusive assignment:** retain RFC-0003's MVP baseline: one contributor identity is assigned at a time after maintainer review. A claim is a request, not an assignment. A second contributor may not be told the work is reserved or payable unless the active assignment is released or expires under a predeclared rule.
5. **Delivery submitted:** contributor links the PR and exact commit/base revisions. Attach CI and review evidence as references, with adapter provenance and timestamps. GitHub merge status alone is not acceptance.
6. **Independent review:** a non-conflicted reviewer checks each acceptance criterion and records accept, request changes, reject, or escalate, with reasons and evidence references. Do not let the treasury agent approve work that it funded or receive its own payout.
7. **Payout lifecycle modeled separately:** record `payout_authorized` only after acceptance and policy checks. Record `paid` only in the simulation after adding a matching, valueless settlement receipt. A PR merge, approval, bounty label, or payout authorization must never imply `paid`.
8. **Close and audit:** publish a redacted, reproducible lifecycle report showing what was proposed, funded in simulation, assigned, delivered, reviewed, authorized, and settled in the simulation. Do not expose personal or private customer data.

## Rules to exercise

### Multiple contributors and duplicate work

Only the assigned contributor is eligible under this first-workflow baseline. If two PRs arrive, the reviewer can select the assigned contributor's eligible delivery or release/expire that assignment and explicitly assign another contributor. The simulation must record why an unselected PR was not eligible for payment; it must not imply that useful but unselected work earns a bounty. Competitive first-valid-PR payout is out of scope.

### Conflicts and self-dealing

The creator/requester, contributor, reviewer, and payout authorizer are recorded as distinct roles. A participant cannot approve their own work or act as the independent reviewer for a task they funded. Related identities and collusion cannot be reliably ruled out by a pilot; record declared conflicts and test policy handling, but do not claim Sybil resistance. Mature reputation cannot be created from a simulated self-funded task.

### Scope changes, abandonment, and disputes

Any change to amount, deliverable, base revision, or acceptance criteria requires agreement and a new versioned event before the changed work is treated as eligible. If a contributor abandons or the deadline expires, close/release assignment under the recorded policy; the next contributor needs a new assignment event. A disputed case enters `disputed` and stops simulated payout authorization until an independent decision event. The simulation may model a mediator outcome, but does not activate the unresolved random mediator or appeal design in ADR-0006/RFC-0013.

### AI assistance

Contributors may use AI tools, but a human contributor must understand and stand behind the submitted work, consistent with the JHipster precedent. An autonomous bot/agent cannot claim a simulated bounty. The treasury agent may draft a task and provide preliminary checks, but it cannot change fixed terms, approve its own funded task, choose the payout destination, or decide a dispute.

## Scenarios and success criteria

Run tabletop scenarios before any implementation:

1. Normal accepted PR with CI evidence and simulated settlement receipt.
2. Two contributors attempt the same exclusive task; only the assigned identity is eligible.
3. Scope changes after work begins; old and new criteria remain distinguishable.
4. Requester is also proposed reviewer; conflict blocks approval.
5. Treasury agent attempts to alter amount or destination through issue/PR text; signed policy and task fields control.
6. PR is merged but a required acceptance criterion is missing; no payout authorization.
7. Payout is authorized but there is no settlement receipt; status remains unpaid.
8. Dispute, abandonment, expiration, and reassignment; state remains replayable and non-contradictory.

The design passes this stage only if every scenario yields one deterministic state, the reason and authority are inspectable, and no scenario converts a merge, AI output, label, or unverified receipt directly into `paid`. Also assess the contributor experience: terms must be understandable before work starts and the state of review/payment must be easy to inspect.

## Desk simulation result

**Review date:** 2026-10-19. This is a paper walkthrough of the proposed rules, not an implementation test or protocol conformance result.

| Scenario | Expected result under this proposal | Remaining rule to specify before implementation |
|---|---|---|
| Normal accepted PR | Assignment → delivery → independent acceptance → payout authorization → simulated receipt → paid. | Canonical event names, required signers, and receipt schema. |
| Competing contributors | Only the explicitly assigned contributor is bounty-eligible. Others remain unassigned; reassignment requires a release/expiry event and a new assignment. | Exact assignment expiry and what happens to work already submitted after expiry. |
| Scope changes | Original terms remain immutable; revised terms become eligible only after a signed change event and contributor acceptance. | Whether an in-progress contributor may decline revised terms and receive a partial award (not supported in this pilot baseline). |
| Requester is proposed reviewer | Conflict check blocks the review event; a separate eligible reviewer must be assigned. | How related identities are declared and what happens when no independent reviewer is available. |
| Agent prompt tries to change amount/destination | Issue/PR prose is evidence only; fixed WorkItem amount and signed worker payout identity remain authoritative. Reject mutation and log the rejected attempt where appropriate. | Exact policy authority and secure binding of payout identity are not yet specified. |
| Merged PR misses a criterion | Validation is not accepted; payout authorization is forbidden even if GitHub merged the change. | Who can request revisions or close as incomplete, and the deadline/appeal semantics. |
| Authorization without settlement receipt | State remains `payout_authorized`, never `paid`; missing or invalid receipt enters a recoverable exception path. | Settlement verification is reserved for RFC-0008/RFC-0014 and must validate actual outputs/amount/destination. |
| Dispute, abandonment, expiration | Dispute suspends authorization; abandonment/expiry releases assignment only through declared authority and event; later assignment is a separate event. | Dispute roles/appeals remain RFC-0013; assignment expiration and partial-work handling need a precise policy. |

The walkthrough found no contradiction in the intended happy path, but it is **not ready for implementation**: assignment expiry, scope renegotiation, reviewer availability/conflicts, state/event schemas, payout identity binding, and dispute/appeal behavior still need normative rules. This confirms the next work is specification, not a real bounty launch.

## Gates before any real-money experiment

This simulation does not waive the launch gates in ADR-0007, ADR-0006, RFC-0003, RFC-0008, RFC-0013, and RFC-0014. Before considering real funds, the project must complete protocol behavior and conformance work, escrow and settlement design, dispute/appeal rules, treasury/key/recovery controls, adversarial and multi-node verification, independent security review, and jurisdiction-specific legal/accounting review. Until then, no bounty page, task label, or contributor communication may imply a real payout guarantee.

## Recommended rules to close the identified gaps

The following rules are now added to the RFC-0003 and RFC-0014 Drafts for cross-review:

- Each exclusive assignment freezes a start-by deadline, delivery deadline, and optional inactivity timeout. Reassignment requires an explicit release/expiry event by the contributor or authorized maintainer; expiry alone carries no reputation penalty.
- Material changes to scope, amount, deadline, or review rules require a versioned proposal and a separate acceptance event signed by the assignee. The assignee can decline and release the assignment without that refusal alone counting as failure.
- Partial payment is available only for milestones separately defined and funded before work starts.
- Required reviewers must be distinct from requester, funding authority, assignee, and known related identities. If the required independent review is unavailable, payout remains blocked and the declared escalation path applies.
- Assignment binds the payout recipient identity. A contributor-signed settlement instruction supplies the destination; RFC-0008 must verify it. Issue/PR text, AI output, and integration callbacks cannot choose or alter the destination.

These are Draft RFC requirements for cross-review, not an accepted production payment policy. Reviewer identity linkage, exact timestamp/deadline semantics, recipient-key proof, and mediation/appeal finality still require security and protocol review.

## Decision after simulation

With these proposed rules in the Draft RFCs, the next step is cross-reviewing state transitions and then writing conformance tests before implementation. If terms are hard for contributors to understand, revise the WorkItem presentation and repeat the simulation. External-project outreach is considered only after an Alkaest-owned pilot provides evidence of concrete benefit.
