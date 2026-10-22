# AGENTS.md

## Project
Alkaest is a decentralized coordination protocol.
This repository contains protocol specifications, RFCs, diagrams, and future implementation plans.

## Current phase
Desktop-first MVP for open-source development coordination.
The first implementation is a desktop Standard node, but the architecture must support heterogeneous nodes (phones, weak machines, servers) from the start (ADR-0003, RFC-0002 §16).

Alkaest Chatbot is the commercial bootstrap path for near-term revenue and service-domain learning.
Keep chatbot-specific operational details out of the protocol core. Service scheduling is a module (RFC-0007), not core: channel details (WhatsApp, aliases, message wording) and calendar sync stay in integrations.

## Primary goals
1. Finish protocol specifications before implementation.
2. Keep the protocol generic enough to support future marketplace domains.
3. Use open-source development workflow as the first real domain.
4. Use Alkaest Chatbot as a practical commercial wedge without making the core protocol scheduling-specific.
5. Prefer RFCs and ADRs over undocumented decisions.

## Documentation rules
- Any major architectural change must update the relevant RFC.
- If a new recurring rule appears, update AGENTS.md.
- Keep RFCs precise and implementation-aware.
- Prefer additive edits over rewriting history unless requested.
- Keep `docs/README.md`, `docs/decisions/README.md`, `docs/handoff/current-state.md`, `docs/handoff/next-tasks.md`, and `docs/overview/roadmap.md` synchronized when decisions, RFC maturity, launch gates, or priorities change.
- Research documents are informative, not normative; promote adopted requirements into the owning ADR/RFC and link back to the evidence.
- Use relative repository links in documentation; do not commit machine-specific absolute filesystem paths.

## Development rules
- The project follows TDD.
- Everything implemented in this repository should start with tests.
- When beginning development work, write or update the tests first before writing implementation code.
- Treat test coverage as part of the feature, not as follow-up work.

## Writing rules
- Write specs in English.
- Use stable terminology consistently:
  - Identity
  - Space
  - Membership
  - Object
  - Event
  - Relation
  - Message
  - Decision
  - Envelope
  - WorkItem
  - Evidence
- Distinguish clearly between:
  - current MVP
  - future architecture
  - long-term vision

## RFC process
- RFC-0001 is the protocol core.
- RFC-0002 is node architecture.
- RFC-0003 is development workflow module.
- Future RFCs must reference prior RFC assumptions.

## Priorities
When in doubt, prioritize:
1. clarity
2. protocol correctness
3. test-first development
4. future extensibility
5. implementation feasibility

## Anti-patterns
- Do not make the protocol GitHub-specific.
- Do not make the protocol WhatsApp-specific, Google Calendar-specific, or scheduling-only.
- Do not assume centralized operators.
- Do not introduce marketplace/mobile complexity into the MVP unless explicitly asked.
- Do not assume every node is a desktop full node or that big nodes are trusted more (ADR-0003).
- Do not build a blockchain for validation; signed, replayable space logs are validated by every node (ADR-0003).
- Do not turn reputation into a transferable token (ADR-0004).
- Do not let payment, task creation, merge, or AI acceptance alone create mature reputation; follow the launch gate in RFC-0006 and the reputation integrity threat model.
- Do not reimplement the protocol in the app: the Flutter app uses `alkaest-core` through `flutter_rust_bridge`, and talks to every node (embedded, self-hosted, hosted) through the same Local API (ADR-0005).
- Do not rely on a phone as a business's always-on node; phones run Light nodes (ADR-0005).
- Do not give the maintainer agent sole control of funds beyond its operating allowance, never let it mediate its own tasks, and never take payout amounts or destinations from PR or issue content (ADR-0006).
