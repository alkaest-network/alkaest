# RFC-0001 — Alkaest Protocol v0.1

**Status:** Draft
**Author:** modern_alchemist
**Date:** 2026
**Category:** Protocol Specification

---

# 1. Abstract

The **Alkaest Protocol** defines a decentralized runtime for coordination between identities over a peer-to-peer network. It enables distributed systems for collaboration, task execution, dispute resolution, messaging, and governance without relying on centralized servers.

The protocol is composed of:

* a **P2P node runtime**
* a **cryptographically verifiable data model**
* an **event-driven object system**
* a **distributed synchronization mechanism**
* a **standard API for external applications**

The goal is to allow developers to build coordination systems such as organizations, DAOs, work marketplaces, communities, and collaborative environments on top of a shared decentralized infrastructure.

---

# 2. Design Principles

The protocol is designed according to the following principles.

## 2.1 Node-first architecture

All protocol logic resides in the **node runtime**.
User interfaces are external clients interacting with the node via APIs.

## 2.2 Event-driven state

State transitions are represented as **signed events**, enabling verifiable history and replayable state reconstruction.

## 2.3 Cryptographic trust

Every meaningful action is signed by a cryptographic identity.

## 2.4 Decentralized synchronization

Nodes exchange state through a **peer-to-peer gossip and inventory mechanism**.

## 2.5 Interface agnosticism

Any application can interact with the node via API or SDK.

## 2.6 Extensibility

Payload schemas can evolve independently of the core protocol.

## 2.7 Offline resilience

Nodes may operate partially offline and synchronize later.

---

# 3. System Architecture

The system consists of four logical layers.

```
Applications (UI / automation)
        │
        ▼
Alkaest Node API
        │
        ▼
Alkaest Node Runtime
        │
        ▼
Alkaest P2P Network
```

## 3.1 Applications

Applications include:

* web interfaces
* mobile apps
* enterprise dashboards
* automation agents
* bots

Applications never communicate directly with the network. They interact with a **local or remote node**.

## 3.2 Node API

The node exposes a structured API providing:

* commands
* queries
* streaming subscriptions

## 3.3 Node Runtime

The node runtime implements:

* identity management
* object validation
* event processing
* storage
* P2P networking
* message routing

## 3.4 P2P Network

Nodes communicate via a decentralized peer network responsible for:

* object propagation
* state synchronization
* mailbox message relay
* peer discovery

---

# 4. Identity

Every participant in the network is represented by a cryptographic **Identity**.

Identities are based on public/private key pairs.

## Identity structure

```
Identity
- id
- publicKey
- createdAt
- metadata
```

### Identity ID

The identity identifier MUST be derived from the hash of the public key.

### Properties

Identities are:

* self-sovereign
* globally unique
* cryptographically verifiable

Identities sign:

* envelopes
* events
* objects
* messages
* decisions

---

# 5. Spaces

A **Space** represents a coordination context.

Examples include:

* organizations
* teams
* projects
* communities
* DAOs

Spaces provide a boundary for:

* membership
* permissions
* objects
* events
* messages

## Space structure

```
Space
- id
- ownerIdentityId
- name
- type
- metadata
- createdAt
```

---

# 6. Membership

Membership connects identities to spaces.

```
Membership
- id
- spaceId
- identityId
- role
- permissions
- createdBy
- createdAt
```

### Roles

Roles are not strictly defined by the core protocol.

Examples may include:

* owner
* admin
* member
* contributor
* validator

### Permissions

Permissions are interpreted by modules built on top of the protocol.

---

# 7. Objects

Objects represent generic entities within the protocol.

The object system allows applications to define domain-specific structures while maintaining a universal storage model.

```
Object
- id
- spaceId
- objectType
- schemaId
- ownerIdentityId
- payload
- visibility
- attachmentRefs
- createdAt
- updatedAt
```

### objectType

Defines the semantic category of the object.

Examples:

```
work_item
document
contract
proposal
evidence
```

### schemaId

Defines the schema used to interpret the payload.

Examples:

```
alkaest.workflow.work_item.v1
alkaest.documents.file.v1
com.acme.inspection.v2
```

---

# 8. Events

Events represent state transitions affecting objects.

```
Event
- id
- spaceId
- targetObjectId
- eventType
- actorIdentityId
- payload
- createdAt
```

Examples of event types:

```
object.created
object.updated
work_item.assigned
work_item.submitted
work_item.started
```

Events provide a verifiable history of actions.

---

# 9. Relations

Relations model connections between entities.

```
Relation
- id
- spaceId
- fromId
- toId
- relationType
- metadata
```

Examples:

```
assigned_to
depends_on
references
belongs_to
```

Relations allow graph-like structures to be constructed over protocol entities.

---

# 10. Messages

Messages enable communication within spaces.

```
Message
- id
- spaceId
- contextId
- senderIdentityId
- recipientIds
- body
- attachmentRefs
- createdAt
```

### contextId

The context may reference:

* a space
* an object
* a thread
* a workflow item

---

# 11. Attachments

Large binary data is not stored directly in the P2P network.

Instead, attachments are referenced by hash.

```
AttachmentRef
- id
- hash
- size
- mimeType
- storageRef
- encryptionInfo
```

### storageRef

Possible storage locations include:

* object storage
* decentralized storage
* node-local storage
* external blob services

Nodes verify file integrity via the hash.

---

# 12. Decisions

Decisions represent authoritative outcomes or formal actions.

```
Decision
- id
- spaceId
- targetId
- decisionType
- actorIdentityId
- reason
- payload
- createdAt
```

Examples:

```
approve
reject
mediate
vote
close_dispute
```

---

# 13. Universal Envelope

All data propagated through the network must be wrapped in a **protocol envelope**.

```
Envelope
- envelopeId
- protocolVersion
- objectKind
- objectId
- spaceId
- authorId
- createdAt
- payloadHash
- payloadBytes
- signature
```

### Properties

The envelope ensures:

* authenticity
* integrity
* version compatibility
* immutable transport

Nodes MUST verify:

* signature
* payload hash
* schema validity

before accepting an envelope.

---

# 14. P2P Synchronization

Nodes synchronize using an **inventory-based replication mechanism**.

Typical flow:

```
Node A → Node B : InventoryRequest
Node B → Node A : InventoryResponse
Node A → Node B : ObjectRequest
Node B → Node A : ObjectResponse
```

This allows nodes to:

* discover missing objects
* bootstrap new nodes
* recover partial state

---

# 15. Mailbox

Mailbox functionality enables private message relay when recipients are offline.

Workflow:

```
Sender → Peer : MailboxStore
Recipient → Peer : MailboxFetch
```

Messages are encrypted for recipients before being stored.

Peers act only as relays and cannot read mailbox contents.

---

# 16. Node API

External interfaces interact with the node through a structured API.

The API is divided into:

* commands
* queries
* streams

---

# 17. Commands

Commands create new envelopes and publish them to the network.

```
CreateSpace
GrantMembership
CreateObject
PublishEvent
CreateDecision
SendMessage
UploadAttachmentRef
```

Commands require appropriate permissions and identity signatures.

---

# 18. Queries

Queries retrieve data from node projections.

```
GetSpace
GetObject
GetObjectHistory
ListObjects
ListMemberships
ListMessages
```

Query responses are generated from node-maintained projections.

---

# 19. Streams

Streams provide real-time updates to clients.

```
SubscribeSpaceEvents
SubscribeObjectEvents
SubscribeInbox
SubscribeNetworkStatus
```

Streaming allows applications to react to changes immediately.

---

# 20. Node Responsibilities

Each node performs the following functions:

* cryptographic validation
* schema validation
* network synchronization
* local data persistence
* mailbox relay
* API exposure
* projection maintenance

Nodes operate independently but converge through synchronization.

---

# 21. Modules

The protocol supports modular extensions.

Examples include:

```
workflow
dispute_resolution
reputation
governance
identity_extensions
```

Modules define:

* additional object types
* event types
* validation rules
* domain behaviors

---

# 22. Workflow Module (Preview)

The first official module is **Workflow**.

This module enables task coordination.

Example mapping:

```
Object type : work_item
Event       : work_item.assigned
Event       : work_item.submitted
Decision    : work_item.accepted
Decision    : work_item.rejected
```

---

# 23. Security Model

Security is based on:

* cryptographic signatures
* hash verification
* recipient-based encryption
* schema validation
* authorization rules

Nodes must reject envelopes that fail validation.

---

# 24. Extensibility

The protocol allows new types to be introduced through identifiers:

```
schemaId
objectType
eventType
decisionType
```

Nodes that do not recognize a schema may still store and propagate the envelope.

---

# 25. Protocol Versioning

The envelope field:

```
protocolVersion
```

allows forward compatibility and controlled protocol upgrades.

---

# 26. Conclusion

The Alkaest Protocol defines a decentralized coordination runtime built around cryptographically verifiable objects, events, and identities.

By separating the node runtime from user interfaces, the protocol enables a wide range of applications to operate over a shared decentralized infrastructure.