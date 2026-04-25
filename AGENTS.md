# AGENTS.md

## Project
Alkaest is a decentralized coordination protocol.
This repository contains protocol specifications, RFCs, diagrams, and future implementation plans.

## Current phase
Desktop-first MVP for open-source development coordination.
Do not optimize for mobile-first or light-client-first unless an RFC explicitly requires it.

Alkaest Chatbot is the commercial bootstrap path for near-term revenue and service-domain learning.
Keep chatbot-specific operational details out of the protocol core unless a future RFC explicitly defines a service scheduling module.

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
