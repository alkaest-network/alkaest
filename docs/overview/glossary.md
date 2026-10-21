# Glossary

## Node

The runtime that executes the Alkaest protocol.
The first implementation target is a local Standard node. The architecture supports Light, Standard, and Service profiles; storage and service capacity differ by profile, but a profile does not grant extra protocol authority (RFC-0002, ADR-0003).

## Identity

A cryptographic participant in the protocol.
Identities sign protocol actions and may accumulate contribution evidence over time. Reputation remains a derived, gated interpretation of that evidence (RFC-0006).

## Multiple Identities Per Node

The ability for one node operator to manage more than one Identity while keeping each reputation history separate.

## Space

A coordination context within the protocol, such as a project, organization, or team.

## Membership

The relationship between an Identity and a Space, including role or permission context.

## Object

A generic protocol entity stored in a space.
Objects are typed and interpreted through schemas.

## Event

A signed state transition affecting an Object or other protocol state.
Events provide replayable history.

## Relation

A protocol link between entities, such as assignment, dependency, or reference.

## Message

A communication record within a space or context, potentially relayed through mailbox mechanisms.

## Decision

A formal outcome or authoritative action in the protocol, such as approval, rejection, or dispute closure.

## Envelope

The transport wrapper used to propagate protocol data across nodes.
It carries metadata, payload integrity information, and signatures.

## Task

A conceptual unit of work coordinated through Alkaest.
In the first domain, the Development Workflow Module represents a task as a `WorkItem` (RFC-0003).

## WorkItem

The protocol object for a development-workflow task. Its terms are frozen and its lifecycle is projected from signed events; funding, validation, acceptance, payout authorization, settlement, and reputation remain distinct (RFC-0003).

## Evidence

Proof or supporting material attached to work, validation, or dispute processes.
Examples may include commits, pull requests, CI results, artifacts, or external attestations.

## Reputation

A domain-aware trust signal derived from verifiable work history, outcomes, and other protocol evidence. Its production use is gated until RFC-0006 addresses self-dealing, Sybil/collusion risks, validation, appeals, and privacy.

## Reputation Profile

A domain-specific view of reputation for an identity.
This may eventually include success rate, weighted score, dispute rate, validator diversity, and recency effects.

## Reputation Wallet

A conceptual collection of contribution proofs and related reputation evidence associated with an Identity.

## Contribution Proof

A record that a task or unit of work was completed and validated.
This is part of the planned reputation model and is not yet fully specified.

## Identity Assurance Level

An optional trust tier attached to an identity through attestations or credentials.
This may be used for work that requires stronger personhood or verification guarantees.

## Validator

A participant or role responsible for reviewing submitted work and attesting to whether it satisfies task requirements.

## Validation Tier

A task-dependent level of validation strictness, such as single-validator review for simpler work and broader review for higher-risk work.

## Mediator

A participant or role responsible for resolving disputes when requester and worker outcomes conflict.

## Integration Adapter

Node-local logic that connects external systems such as GitHub or CI providers to the protocol without making those systems authoritative.

## Standard Node

The first implementation target: a desktop/workstation node that stores full history for its participating Spaces and a configurable share of other data. It exposes the Local API, validates accepted records, updates projections, and synchronizes with peers (RFC-0002).

## Light Node

A node profile for phones and browsers that keeps its identities and Spaces and fetches other data on demand. It validates every record it accepts and may use relays for reachability. It is the second implementation target, not a separate trust class (RFC-0002, ADR-0003).

## Query Projection

A derived read model built from accepted protocol objects and events.
Queries should read from projections rather than mutate state directly.

## P2P Sync

The peer-to-peer synchronization process used by nodes to exchange inventories, fetch missing data, and propagate accepted protocol state.

## Mailbox

A relay mechanism for encrypted message delivery when recipients are offline.

## Requester

The party that creates or funds a unit of work.
This term belongs primarily to the marketplace and workflow layer.

## Worker

The party that accepts and performs a unit of work.
This term belongs primarily to the marketplace and workflow layer.

## Reward Escrow

Funds locked for a task's agreed payout or refund path. RFC-0008 drafts an on-chain BTC `regtest` profile; its script, keys, recovery, and production settlement rules remain unresolved, and no real-fund operation is authorized.

## Bond

Collateral locked to discourage spam, fraud, abandonment, or malicious behavior.
This may apply to requesters, workers, validators, or mediators depending on future RFCs.

## Blockchain Anchoring

An external timestamp commitment that binds a digest of off-chain protocol records to a blockchain without storing those records on-chain. Alkaest requires Bitcoin settlement references and periodic treasury-log anchors for live treasury operation (ADR-0007); anchors are not used as general protocol consensus or state validation (ADR-0003).
