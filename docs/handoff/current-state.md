# Current State

## What has been decided
- Alkaest is protocol-first, not app-first.
- The MVP is desktop-first.
- Each developer runs a local node.
- The first domain is open-source development coordination.
- Alkaest Chatbot is the commercial wedge for near-term revenue and service-domain learning.
- The intended product bridge is Alkaest Chatbot -> WhatsApp discovery number -> Alkaest Network.
- GitHub is an integration layer, not the protocol itself.
- Future support for consumer apps and light clients is desired, but not MVP-critical.
- The MVP node model is a local full node running on the developer workstation.
- Light-client and mobile-specific behavior remain future work.
- The first project intended to run on the network is Alkaest itself.
- Donations to Alkaest are expected to be distributed across `alkaest-network` issues for Alkaest contributors.

## Current RFC status
- RFC-0001: drafted
- RFC-0002: drafted
- RFC-0003: drafted
- RFC-0004: drafted
- RFC-0005: drafted

## Main architectural direction
Demand -> Worker -> Evidence -> Validation -> Settlement

## First bootstrap project
Donation -> Alkaest issue -> Contributor work -> Evidence -> Validation -> Payout

## Current node direction
Developer UI -> Local Alkaest Node -> Alkaest P2P Network
GitHub -> Integration Adapter -> Local Alkaest Node

## Recently completed
- RFC-0002 defines the desktop-first node architecture.
- Node architecture visuals now align with the MVP full-node model.
- RFC-0003 defines the first development workflow module around funded issue-based coordination.
- RFC-0004 defines canonical encoding, hashing, signatures, identifiers, and envelope validation.
- RFC-0005 defines object/event semantics, projection rebuild rules, and deterministic state resolution.
- ADR-0001 records the desktop-first MVP decision as an explicit architecture and product constraint.
- ADR-0002 records Alkaest Chatbot as the commercial wedge and future service-domain bridge.
