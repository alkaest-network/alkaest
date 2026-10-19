# Draft Starter Issues for New Contributors

These are proposed issue bodies for maintainers to review and publish on GitHub. They are not yet open issues, assignments, or funded WorkItems. Keep scope documentation-only; do not imply protocol acceptance or payment.

## 1. Add RFC-0003 assignment lifecycle examples

**Suggested title:** `docs: add RFC-0003 assignment lifecycle conformance examples`

**Description:** Add a compact set of event traces that make the WorkItem assignment transition table easier to review. Follow RFC-0003 §8–10 and RFC-0005 sequencing rules. Do not choose a trusted clock, deadline grace period, expiry authority roster, or new economic rule; those remain open.

**Acceptance criteria:**

- Include the successful path from an eligible claim through proposal, separate assignee acceptance, start, and submission.
- Include declined and expired unaccepted proposals returning to `open`, without making work eligible from a proposal alone.
- Include release/expiry of an accepted assignment before reassignment, including after work has started.
- Include at least one out-of-order or competing-event case and state when the projection remains unresolved.
- For each trace, show the relevant event order and resulting `workStatus`; do not rely on local-clock observation or provider callbacks as expiry proof.
- Link each rule to its RFC-0003/RFC-0005 source and flag any source ambiguity instead of silently resolving it.

**Suggested labels:** `documentation`, `good first issue` (create these labels if the repository does not already have them).

## 2. Clarify existing WorkItem terms in the glossary

**Suggested title:** `docs: clarify WorkItem lifecycle terms in the glossary`

**Description:** Review the glossary against RFC-0003 and clarify the WorkItem terms that are already defined there. Keep definitions aligned with the RFC and identify any terms that need an RFC decision instead of guessing at future funding or settlement behavior.

**Acceptance criteria:**

- Define only terms and transitions already present in RFC-0003, using plain language.
- Preserve the distinction between source events and derived WorkItem state.
- Link each definition to its RFC-0003 source section.
- Add a short note or issue comment for any glossary term that lacks a settled source definition; do not invent funding or settlement rules.

**Suggested labels:** `documentation`, `good first issue` (create these labels if the repository does not already have them).

## Maintainer publishing checklist

- Confirm the RFC source sections still match these issue scopes.
- Create the issue labels, or remove the suggested labels from the issue text.
- Publish the issues after the contribution guide and issue forms are on the public default branch.
- Leave the issues unassigned and explicitly state that they are unpaid documentation tasks.
