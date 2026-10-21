# RFC-0009 — Node API and SDK Contract

**Status:** Draft
**Author:** modern_alchemist
**Date:** 2026
**Category:** Protocol Specification
**Related:** RFC-0002 §7.1, RFC-0004, RFC-0005, ADR-0003, ADR-0005
**Reference implementation:** `alkaest-node` (`alkaest serve`), `alkaest-core::request_auth`

---

# 1. Abstract

This RFC defines the Local API: the boundary between a node and the applications and integrations that use it. RFC-0002 §7.1 left the API surface to a later RFC.

The same API serves every deployment mode of ADR-0005 (embedded, self-hosted and hosted), so an app behaves the same whoever runs the node.

This draft covers version 1: authentication, device pairing, commands, queries, the event stream, errors and idempotency.

---

# 2. Goals

* One API for every deployment mode.
* No passwords or bearer tokens: requests are signed by device keys, using the identity model of RFC-0004.
* A captured request cannot be altered or replayed.
* Commands report the protocol outcome of what they did (RFC-0005 §8), so apps can explain it to users.

## Non-goals

* Peer-to-peer synchronization between nodes (RFC-0002 §6.6). This RFC covers clients only.
* Permission scopes per device or per identity (RFC-0011, planned, not yet written).
* Transport encryption. It is provided by TLS (§9).

---

# 3. Transport

* HTTP/1.1 or later, with JSON bodies (`application/json`, UTF-8). Paths are prefixed with the API version: `/v1/...`.
* A node binds to the loopback interface by default. The reference port is `7420`.
* Streams use server-sent events (§7). The stream flows only from node to client, and SSE passes through common proxies.

---

# 4. Signed Requests

Every request MUST carry these headers:

| Header | Value |
|---|---|
| `alkaest-key` | Device Ed25519 public key, lowercase hex (RFC-0004 §7.3) |
| `alkaest-timestamp` | RFC 3339 UTC timestamp |
| `alkaest-nonce` | 1 to 128 characters, unique per key within the freshness window |
| `alkaest-signature` | base64url Ed25519 signature (no padding) over the Request Signing Payload |

## 4.1 Request Signing Payload

The signature covers the Alkaest Canonical JSON (RFC-0004 §5) of:

```json
{
  "bodyHash": "<lowercase hex SHA-256 of the raw body bytes; of the empty string when there is no body>",
  "method": "<HTTP method, uppercase>",
  "nonce": "<alkaest-nonce>",
  "path": "<path and query exactly as sent>",
  "purpose": "alkaest-local-api-v1",
  "timestamp": "<alkaest-timestamp>"
}
```

`purpose` separates API signatures from envelope signatures made with the same key.

## 4.2 Node checks

A node MUST check, in order:

1. All four headers are present and the nonce length is valid → otherwise `unauthenticated`.
2. The signature verifies against `alkaest-key` → otherwise `invalid_signature`.
3. The timestamp is within **2 minutes** of the node's clock → otherwise `stale_request`.
4. The pair (key, nonce) was not seen while the timestamp is fresh → otherwise `replayed_request`.
5. The key belongs to a paired device → otherwise `device_not_paired`. The only exception is `POST /v1/pair`.

A node MAY keep nonces only in memory. After a restart, a captured request can then be replayed only within its freshness window.

---

# 5. Device Pairing

1. The node operator creates a pairing code on the node, for example with `alkaest device pair`. The code is at least 128 bits of randomness, single use, and expires (10 minutes by default). The node SHOULD store only a hash of the code.
2. The node shows a pairing URI, usually as a QR code: `alkaest-pair:?node=<url>&code=<code>`.
3. The app sends `POST /v1/pair` with `{"code", "label"}` (label: 1 to 64 characters), signed by its device key. The signature proves the app holds the key.
4. The node consumes the code, even when it is expired, and records the device:
   * `deviceId` = `idn_` + SHA-256 of the key (RFC-0004 §8);
   * the label;
   * the public key;
   * `pairedAt`.

Revoking a device removes its record. Its next request fails with `device_not_paired`.

---

# 6. Resources

A paired device may act as any identity held by the node (`as` field). Narrower grants belong to RFC-0011 (planned, not yet written).

| Method and path | Request | Response |
|---|---|---|
| `POST /v1/pair` | `{code, label}` | `200 {deviceId, label}` |
| `GET /v1/node` | | `200 {software, version, protocolVersion, profile}` |
| `GET /v1/identities` | | `200 {identities: [{identityId, label}]}` |
| `POST /v1/identities` | `{label}` | `201 {identityId}` |
| `POST /v1/spaces` | `{name, as}` | `201 {objectId, envelopeId}` |
| `POST /v1/objects` | `{spaceId, objectType, state, as}` | `201 {objectId, envelopeId}` |
| `POST /v1/events` | `{objectId, eventType, eventClass?, data?, as}` | `201 {eventId, envelopeId, status}` |
| `GET /v1/objects/{objectId}` | | `200` resolved object state (RFC-0005 §7.2, §8) |
| `GET /v1/state` | | `200` resolved state plus `stateHash` |
| `GET /v1/envelopes` | | `200 {envelopes: [...]}` |
| `POST /v1/envelopes` | an envelope (RFC-0004 §9) | `201 {envelopeId, admitted: true}` or `200 {envelopeId, admitted: false}` |
| `GET /v1/stream` | | `text/event-stream` (§7) |

Notes on the event and envelope routes:
* **Event defaults.** `eventClass` defaults to `state` and `data` defaults to `{}`.
* **Event head.** The node fills `targetVersion` and `prevEventId` from the object's current applied head.
* **Event outcome.** `status` is the outcome after resolution: `applied`, `recorded` (evidence), `pending`, `conflicting` or `rejected`.
* **Envelopes signed elsewhere.** `POST /v1/envelopes` admits envelopes signed outside the node, for example by an embedded Light node in the app, after full validation (RFC-0004 §11).

Request bodies reject unknown fields.

---

# 7. Stream

`GET /v1/stream` emits server-sent events:

* `event: envelope`, with `data: {envelopeId, objectKind, objectId, spaceId, stateHash}` for each envelope the node admits through this API.
* `event: resync`, with `data: {}`, when the client fell behind and must reload the state.

The stream is a change notification, not a source of truth. Clients reload what they need through the query routes.

---

# 8. Errors and Idempotency

Errors use the body `{"error": {"code", "message"}}`.

| Status | Codes |
|---|---|
| 400 | `invalid_request` |
| 401 | `unauthenticated`, `invalid_signature`, `stale_request`, `replayed_request` |
| 403 | `device_not_paired`, `invalid_pairing_code` |
| 404 | `unknown_identity`, `unknown_object` |
| 413 | `payload_too_large` (bodies above 1 MiB) |
| 422 | `envelope_rejected` |
| 500 | `internal` (no local details are exposed) |

**Idempotency:**
* `POST /v1/envelopes` is idempotent, because envelopes are deduplicated by `envelopeId` (RFC-0005 §13.3).
* The authoring commands (`spaces`, `objects`, `events`) are not idempotent: each call seals a new envelope with a new timestamp. A client that must retry safely can seal the envelope itself and submit it through `POST /v1/envelopes`.

---

# 9. Security Considerations

* Signatures provide authenticity and replay protection, not confidentiality. A node reachable beyond loopback MUST be served over TLS.
* Identifiers received from clients MUST be validated before use as storage keys. For example, identity ids must match `idn_` followed by 64 lowercase hex digits.
* Pairing codes are secrets with a short life. Nodes store their hash and consume them on first use.
* Hosted nodes (ADR-0005) hold identity keys on behalf of their owners. Signing on the device instead, through `POST /v1/envelopes`, keeps keys off the hosted node.

---

# 10. Open Questions

* Per-device scopes and per-identity grants (RFC-0011, planned, not yet written).
* Pagination and filtering for `GET /v1/envelopes` and `GET /v1/state` once spaces grow.
* Capability and replication-status queries for node profiles (RFC-0002 §16.4).
* Reaching self-hosted nodes behind NAT (ADR-0005 open question; Phase 1).
