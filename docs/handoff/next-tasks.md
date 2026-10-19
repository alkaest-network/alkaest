# Next Tasks

1. Review and refine [0005-object-event-semantics-and-state-resolution.md](../rfc/0005-object-event-semantics-and-state-resolution.md) against RFC-0001 through RFC-0004
2. Define how donations to Alkaest are allocated into `alkaest-network` issues in a more formal funding policy
3. Define `.alkaest/project.yaml` draft for project integration
4. Write RFC-0006 Reputation Proofs and Scoring
5. Map Alkaest Chatbot concepts into future protocol objects, events, evidence, and privacy constraints
6. Decide when a Service Scheduling Workflow Module should enter the RFC sequence
7. Add Mermaid diagrams for:
   - node internals
   - command flow through the node
   - open-source issue lifecycle
   - donation-to-issue funding flow
   - envelope construction and validation flow
   - object/event state resolution flow
   - chatbot-to-network progression
8. Decide whether to narrow RFC-0001 further so marketplace details stay outside core protocol
9. Add an ADR index if more cross-cutting product decisions start accumulating

## Before inviting outside contributors

- Review and merge or retarget the open documentation pull requests in dependency order, then make sure this onboarding change matches the resulting default branch.
- Publish this contribution guide, the Code of Conduct, security policy, and issue templates on the public default branch.
- Verify a private vulnerability-reporting route and a working Code of Conduct contact; the repository files alone do not confirm those GitHub settings or contacts.
- Clarify access and licensing for companion repositories. The root MIT license applies only to this repository; as of 2026-10-19, the linked GitHub account could access `alkaest-ai` but not the node, app, Brain, or chatbot repositories. The public `alkaest-ai` repository had no top-level `LICENSE` file.
- Review and publish the [draft starter issue descriptions](contributor-starter-issues.md), then assign maintainers to triage issues and review pull requests.
