# Glossary

## Node

The runtime that executes the Alkaest protocol.
In the MVP, a node is a local full node run by a developer on their own machine.

## Identity

A cryptographic participant in the protocol.
Identities sign protocol actions and accumulate reputation over time.

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
In later module RFCs this will likely be represented by a specific object schema such as `WorkItem`.

## WorkItem

The expected protocol object type for development workflow tasks in the first domain.
This term belongs primarily to the workflow module layer rather than the minimal core.

## Evidence

Proof or supporting material attached to work, validation, or dispute processes.
Examples may include commits, pull requests, CI results, artifacts, or external attestations.

## Reputation

A domain-aware trust signal derived from verifiable work history, outcomes, and other protocol evidence.

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

## Local Full Node

The MVP node profile.
It stores protocol state locally, exposes the node API, validates envelopes, updates projections, and synchronizes with peers.

## Light Client

A future node profile with partial storage or selective synchronization.
This is intentionally out of MVP scope unless a later RFC brings it in.

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

Funds reserved for successful task completion.
This is part of the planned settlement model and is not yet fully specified.

## Bond

Collateral locked to discourage spam, fraud, abandonment, or malicious behavior.
This may apply to requesters, workers, validators, or mediators depending on future RFCs.

## Blockchain Anchoring

An optional mechanism for recording hashes or checkpoints of protocol state on a blockchain for stronger auditability without storing all details on-chain.
