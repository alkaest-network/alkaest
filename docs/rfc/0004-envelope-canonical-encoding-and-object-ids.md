# RFC-0004 — Envelope, Canonical Encoding, and Object IDs

**Status:** Draft
**Author:** modern_alchemist
**Date:** 2026
**Category:** Protocol Specification

---

# 1. Abstract

This RFC defines how Alkaest protocol data becomes deterministic bytes that can be hashed, signed, stored, and replicated across nodes.

It specifies:

* the canonical encoding format
* the hash function used for protocol integrity
* the signature algorithm used for protocol signing
* how object identifiers are derived
* how envelopes are constructed and validated

The goal is simple: two honest nodes given the same protocol payload must derive the same bytes, the same hash, and the same identifier.

---

# 2. Goals

This RFC defines:

* a deterministic serialization strategy
* stable payload hashing rules
* a default signature scheme
* ID derivation rules for identities, objects, events, relations, messages, decisions, and envelopes
* the envelope validation procedure used by nodes

This RFC does not define:

* event ordering or conflict resolution
* workflow-specific schemas
* settlement logic
* remote key custody
* alternative transport encodings

Those concerns belong in other RFCs.

---

# 3. Context

RFC-0001 defines the envelope concept and requires nodes to verify:

* signature
* payload hash
* schema validity

RFC-0002 defines the node architecture and requires the Envelope Engine to:

* prepare canonical payloads
* hash payloads
* assemble envelopes
* verify signatures

RFC-0003 defines workflow module objects that will need deterministic encoding in order to be safely stored and propagated.

This RFC provides the shared serialization and identity rules that make those RFCs implementable.

---

# 4. Design Principles

## 4.1 Determinism over convenience

Protocol payloads must always encode to the same bytes when their semantic content is the same.

## 4.2 Transport independence

The canonical byte representation is the signed and hashed representation.
Network transports may wrap it, but they must not change its meaning.

## 4.3 Hash-addressed integrity

Identifiers and payload verification should be derived from stable cryptographic hashes.

## 4.4 Minimal cryptographic surface

The MVP should adopt one primary signature algorithm and one primary hash function instead of supporting many options too early.

---

# 5. Canonical Encoding Format

## 5.1 Canonical payload representation

All signed protocol payloads MUST be canonically encoded as **UTF-8 JSON** using a deterministic canonicalization procedure.

This RFC refers to that procedure as **Alkaest Canonical JSON v1**.

## 5.2 Canonicalization rules

The canonicalization procedure MUST obey the following rules:

* objects are encoded with keys sorted lexicographically by Unicode code point
* arrays preserve their original order
* strings are encoded as JSON strings in UTF-8
* numbers MUST be integers or JSON numbers that round-trip exactly
* insignificant whitespace is not permitted
* object members with `null` values MUST be preserved if present
* object members that are absent MUST remain absent

## 5.3 Disallowed values

The following values MUST NOT appear in canonical payloads:

* `NaN`
* `Infinity`
* `-Infinity`
* duplicate object keys

## 5.4 Timestamp format

All protocol timestamps MUST use RFC 3339 UTC format.

Example:

```text
2026-03-16T21:15:00Z
```

## 5.5 Binary data

Binary payload bytes MUST NOT be embedded directly in signed protocol payload objects unless a later RFC explicitly allows it.
Binary data should be referenced through attachment structures and hashes.

---

# 6. Canonical Hashing

## 6.1 Hash function

The default protocol hash function for the MVP is:

```text
SHA-256
```

## 6.2 Hash input

Hashes MUST be computed over the exact canonical UTF-8 bytes of the payload being hashed.

## 6.3 Hash encoding

Hashes SHOULD be represented in lowercase hexadecimal when rendered as strings.

Example:

```text
3f5e...abcd
```

Base64 encodings MAY be used internally by implementations, but protocol-visible string fields SHOULD prefer lowercase hexadecimal for consistency.

---

# 7. Signature Scheme

## 7.1 Default signature algorithm

The default signature algorithm for the MVP is:

```text
Ed25519
```

## 7.2 Signature input

The signature MUST be created over the canonical UTF-8 bytes of the envelope signing payload as defined in this RFC.

## 7.3 Public key encoding

Public keys SHOULD be represented as lowercase hexadecimal or base64url strings in implementation interfaces, but each implementation MUST choose one stable external form.

For protocol-level validation, the critical requirement is that the same public key bytes are recovered unambiguously before verification.

---

# 8. Identifier Derivation

## 8.1 General rule

Unless otherwise noted, protocol identifiers SHOULD be content-derived.
That means an identifier is generated from a stable hash of canonical payload content or canonical signing material.

This allows nodes to:

* detect duplicates
* verify integrity
* avoid accidental ID collisions

## 8.2 Identifier prefixing

For readability and type separation, identifiers SHOULD include a short type prefix.

Recommended prefixes:

```text
idn_  Identity
spc_  Space
mem_  Membership
obj_  Object
evt_  Event
rel_  Relation
msg_  Message
dec_  Decision
env_  Envelope
att_  AttachmentRef
```

## 8.3 Identity ID

As established in RFC-0001, the Identity ID MUST be derived from the hash of the public key.

Recommended derivation:

```text
idn_ + hex(SHA-256(publicKeyBytes))
```

## 8.4 Object IDs

Object identifiers MUST be deterministic and derived from canonical object creation content.

Recommended rule:

```text
obj_ + hex(SHA-256(canonical Object payload bytes))
```

The same rule applies to:

* Space
* Membership
* Relation
* Message
* Decision

with their corresponding type prefix.

## 8.5 Event IDs

Event identifiers MUST be derived from canonical event payload bytes.

Recommended rule:

```text
evt_ + hex(SHA-256(canonical Event payload bytes))
```

## 8.6 Envelope IDs

Envelope identifiers MUST be derived from canonical envelope signing payload bytes.

Recommended rule:

```text
env_ + hex(SHA-256(canonical envelope signing payload bytes))
```

## 8.7 AttachmentRef IDs

Attachment reference IDs SHOULD be derived from the attachment content hash and attachment metadata.

---

# 9. Envelope Structure

RFC-0001 defines the envelope fields:

```text
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

This RFC refines how that structure is produced.

## 9.1 objectKind

`objectKind` identifies the top-level payload category.

Allowed MVP values:

```text
space
membership
object
event
relation
message
decision
attachment_ref
```

## 9.2 payloadBytes

`payloadBytes` represents the canonical UTF-8 JSON bytes of the enclosed protocol payload.

## 9.3 payloadHash

`payloadHash` is:

```text
hex(SHA-256(payloadBytes))
```

## 9.4 Signing payload

The signature is NOT created over the raw envelope object including the signature field.
Instead, it is created over a canonical **Envelope Signing Payload**.

Recommended structure:

```text
EnvelopeSigningPayload
- protocolVersion
- objectKind
- objectId
- spaceId
- authorId
- createdAt
- payloadHash
```

This payload MUST be canonically encoded before signing.

## 9.5 envelopeId

`envelopeId` is derived from the canonical bytes of `EnvelopeSigningPayload`.

## 9.6 Signature field

The `signature` field contains the Ed25519 signature bytes encoded as a stable string representation chosen by the implementation.

For interoperability, base64url without padding is RECOMMENDED.

---

# 10. Payload Hashing and Signing Procedure

To construct an envelope, a node MUST perform the following steps:

1. Construct the protocol payload object.
2. Canonically encode the payload into UTF-8 bytes.
3. Compute `payloadHash = SHA-256(payloadBytes)`.
4. Derive `objectId` from the canonical payload if it is not already fixed by a prior rule.
5. Construct `EnvelopeSigningPayload`.
6. Canonically encode `EnvelopeSigningPayload`.
7. Compute `envelopeId = SHA-256(signingPayloadBytes)`.
8. Sign `signingPayloadBytes` with the author's private key using Ed25519.
9. Assemble the final envelope.

---

# 11. Envelope Validation Procedure

Before accepting an envelope, a node MUST perform the following validations in order.

## 11.1 Structural validation

The node MUST verify that:

* all required envelope fields are present
* `objectKind` is recognized
* `protocolVersion` is supported
* `createdAt` is a valid RFC 3339 UTC timestamp

## 11.2 Payload decoding validation

The node MUST verify that:

* `payloadBytes` can be decoded as UTF-8
* `payloadBytes` parse as valid JSON
* the JSON payload satisfies canonicalization requirements

## 11.3 Hash validation

The node MUST recompute the payload hash and verify that it matches `payloadHash`.

## 11.4 Identifier validation

The node MUST recompute the expected `objectId` and `envelopeId` where derivation rules apply and verify that they match the envelope values.

## 11.5 Author validation

The node MUST verify that:

* `authorId` resolves to a known or locally acceptable identity format
* the signing public key used for verification corresponds to `authorId`

## 11.6 Signature validation

The node MUST reconstruct the canonical `EnvelopeSigningPayload` bytes and verify the Ed25519 signature.

## 11.7 Schema validation

The node MUST verify that the decoded payload is valid for:

* its top-level protocol kind
* its declared schema, where applicable

Only after these checks pass may the envelope be admitted into local protocol state.

---

# 12. Canonical Examples

## 12.1 Canonical payload example

Example payload object:

```json
{
  "createdAt": "2026-03-16T21:15:00Z",
  "objectType": "work_item",
  "ownerIdentityId": "idn_abc123",
  "schemaId": "alkaest.workflow.work_item.v1",
  "spaceId": "spc_example"
}
```

Canonical encoded form:

```json
{"createdAt":"2026-03-16T21:15:00Z","objectType":"work_item","ownerIdentityId":"idn_abc123","schemaId":"alkaest.workflow.work_item.v1","spaceId":"spc_example"}
```

## 12.2 Why this matters

If one node inserts spaces, reorders keys, or changes timestamp shape, the hash changes and signatures no longer match.

---

# 13. Versioning Rules

## 13.1 protocolVersion

Every envelope MUST include a `protocolVersion`.

For the MVP, this RFC assumes:

```text
0.1
```

## 13.2 Forward compatibility

Nodes MAY reject envelopes using unsupported protocol versions.
They MUST NOT silently reinterpret unknown versions as current ones.

## 13.3 Schema evolution

Schema versioning belongs in `schemaId`.
The canonical encoding rules in this RFC remain independent from application schema evolution.

---

# 14. Implementation Notes

Implementations SHOULD:

* centralize canonicalization in one library or runtime module
* expose a test corpus of payload-to-hash examples
* reject non-canonical payloads before persistence
* store canonical bytes alongside parsed representations when useful

Because the project follows TDD, implementations of this RFC should begin with:

* canonicalization tests
* hash derivation tests
* signature verification tests
* envelope round-trip tests
* malformed envelope rejection tests

---

# 15. Future Work

Later RFCs may extend or refine:

* multi-algorithm cryptographic agility
* binary canonical formats
* compressed envelope transport
* delegated signature models
* attachment chunk hashing
* zero-knowledge or privacy-preserving payload strategies

These are intentionally out of MVP scope.

---

# 16. Summary

This RFC gives Alkaest a deterministic serialization and signing model.

The MVP rules are intentionally simple:

* canonical UTF-8 JSON
* SHA-256 hashing
* Ed25519 signatures
* content-derived identifiers
* one explicit validation procedure

With these rules in place, later RFCs can safely define state resolution, workflow semantics, and implementation behavior on top of a shared cryptographic foundation.
