# Architecture Decision Records

ADRs record the current Alkaest product and architecture decisions. Status is authoritative: `Accepted` is a settled direction, `Accepted direction` leaves implementation details open, and `Proposed` needs explicit resolution.

| ADR | Decision | Status | Open boundary |
|---|---|---|---|
| [0001](ADR-0001-desktop-first-mvp.md) | Desktop-first MVP | Accepted | Desktop is first implementation target; not a permanent node limit |
| [0002](ADR-0002-chatbot-commercial-wedge.md) | Chatbot commercial wedge, official WhatsApp API, metered billing | Accepted | Exact usage margin, bill period, payment method, and WABA ownership remain open |
| [0003](ADR-0003-heterogeneous-nodes-and-network-validation.md) | Heterogeneous nodes and validation | Accepted direction | Reference technology choices remain proposals |
| [0004](ADR-0004-token-and-settlement-direction.md) | Reputation, token design timing, Bitcoin settlement | Accepted | Token mechanics/issuance remain unresolved under ADR-0008 |
| [0005](ADR-0005-cross-platform-app-and-deployment-modes.md) | Cross-platform app and deployment modes | Accepted | Applies to product/client deployment, not protocol authority |
| [0006](ADR-0006-self-funding-treasury-and-maintainer-agent.md) | Self-funding treasury, bounties, mediation, agent | Accepted direction | RFC-0008, RFC-0013, RFC-0014 must specify mechanisms and gates |
| [0007](ADR-0007-autonomous-treasury-and-bitcoin-audit.md) | Policy-bounded autonomous treasury and Bitcoin audit | Accepted direction | RFC-0014 and RFC-0008 remain Draft; no mainnet authority |
| [0008](ADR-0008-token-design-before-issuance.md) | Design token before considering issuance | Accepted direction | Purpose, rights, supply, chain, legal status, and launch remain open |
| [0009](ADR-0009-resource-aware-capacity-and-deployment.md) | Resource-aware node capacity and deployment | Proposed | Proposes deferring Kubernetes until measured multi-host operations justify it; protocol resource profiles and benchmarks remain open |
| [0010](ADR-0010-decentralized-source-and-site-hosting.md) | Decentralized source and site hosting | Proposed | Radicle or NIP-34 as canonical forge, seed/pin operators, and migration timing remain open |

## Decision dependencies

```text
ADR-0001 ──> ADR-0003 ──> RFC-0002
ADR-0002 ──> RFC-0007 (Draft service scheduling module)
ADR-0004 ──> RFC-0008 (settlement) ──> RFC-0014 (treasury operation)
ADR-0006 ──> RFC-0013 (validation/disputes) ──> RFC-0003/RFC-0014
ADR-0007 ──> RFC-0008 + RFC-0014
ADR-0008 ──> future token RFC (not yet numbered)
ADR-0003 ──> ADR-0009 ──> RFC-0002 resource/capability follow-up
ADR-0006 ──> ADR-0010 (maintainer agent may operate a seed node)
Reputation integrity research ──> RFC-0006 (not written; production gate)
Bisq incident research ──> RFC-0004/0005 security review + RFC-0008/0014 launch gates
```

## Change rule

When an accepted direction changes, update the ADR that owns it and all dependent specifications/indexes in the same change. Research findings do not silently change protocol policy. Keep historical rationale and supersession links rather than rewriting the record without explanation.
