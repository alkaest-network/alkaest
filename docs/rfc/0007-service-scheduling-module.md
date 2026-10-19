# RFC-0007 — Service Scheduling Module

**Status:** Draft
**Author:** modern_alchemist
**Date:** 2026
**Category:** Module Specification
**Related:** RFC-0001, RFC-0004, RFC-0005 §10, RFC-0006 (reputation), RFC-0009, ADR-0002, ADR-0005, `docs/overview/chatbot-to-network-strategy.md`

Note on numbering: this number was reserved for "Validation and Dispute Resolution" in the roadmap. That RFC is now RFC-0013.

---

# 1. Abstract

This RFC defines the second domain module of Alkaest: **service scheduling**, for local service providers such as barbers, dentists, clinics and studios.

It turns what Alkaest Chatbot does today (service catalog, bookings, added services, cancellations, outcomes and ratings) into protocol objects and events. With them, the same booking rules run on every node: embedded in the app, self-hosted with the local AI, or hosted (ADR-0005).

The module stays generic. It is not specific to WhatsApp, Google Calendar or barbershops. Channels and calendars are integrations.

---

# 2. Goals

* Deterministic, double-booking-free scheduling built only on RFC-0005 (no new consensus).
* A catalog with service durations and buffers, which decide how long a booking blocks.
* A booking lifecycle with completion, no-show and cancellation outcomes, the evidence that reputation needs.
* Ratings that exist only for appointments that happened.
* No personal data in envelopes: no phone numbers, customer names or message text.

## Non-goals

* Reputation formulas (RFC-0006). This RFC only defines which facts reputation may consume (§10).
* Payments, deposits and no-show fees (RFC-0008).
* Fine-grained roles (RFC-0011). Until then, a schedule carries an explicit staff list (§5.2).
* Shared resources (rooms, chairs, equipment) and appointments with several professionals (§12).

---

# 3. Design Overview

| Protocol concept | Scheduling meaning |
|---|---|
| Space | A provider: one establishment |
| Object `service_catalog` | The services the provider offers, with durations |
| Object `schedule` | One professional's agenda for one calendar month |
| State event on a `schedule` | A booking, a change, a cancellation or an outcome |
| Evidence event on a `schedule` | A customer's rating of a completed appointment |
| Customer reference | A per-space pseudonym, never a phone number |

**Why the agenda is the object, not the appointment.** RFC-0005 resolves conflicts per object: competing events for the same version slot get a deterministic winner. If each appointment were its own object, two nodes could book the same professional at the same time in two different objects, and nothing would detect it.

Putting every booking for one professional and month into one `schedule` object makes overlapping bookings compete for the same version slot. Exactly one wins on every node, and the other is `conflicting` (§7).

Monthly partitioning keeps each object's log small enough to replay on a phone.

---

# 4. Identities and Customer References

* **Provider owner:** the identity that owns the space (RFC-0001).
* **Staff:** identities allowed to manage a schedule: the professional, a receptionist, or the chatbot's **agent identity**. Each schedule lists its staff (§5.2).
* **Customer:** either
  * a protocol identity booking for itself (for example from the app), or
  * a **customer reference**, used when the provider's agent books on the customer's behalf through a channel such as WhatsApp.

A customer reference is:

```text
cus_ + lowercase hex( HMAC-SHA-256( spaceSecret, normalizedChannelAddress ) )
```

* `spaceSecret` is a random 32-byte secret held only by the provider's nodes.
* `normalizedChannelAddress` is, for example, `whatsapp:+5534999999999`.

The same person has unrelated references at different providers. The mapping from reference to phone number is integration state on the provider's node (RFC-0002 §11) and MUST NOT appear in any envelope.

When the customer is an identity, `customerRef` is its identity id (`idn_…`).

---

# 5. Objects

## 5.1 `service_catalog`

Schema: `alkaest.scheduling.service_catalog.v1`. One per space, owned by the space owner.

Initial `state`:

```json
{
  "services": {
    "haircut": {
      "name": "Corte de cabelo",
      "durationMin": 30,
      "bufferBeforeMin": 0,
      "bufferAfterMin": 10,
      "active": true
    }
  }
}
```

Rules for service entries:
* **Keys:** service codes are stable keys: lowercase ASCII letters, digits and `_`.
* **Duration:** a positive integer number of minutes.
* **Buffers:** non-negative integers. They default to 0.

Customer-facing aliases and slang ("tapa na fuça" for a full service) are channel configuration on the node, not protocol data.

Events (state class, owner only):

| Event | `data` | Effect |
|---|---|---|
| `catalog.service_upserted` | `{code, name, durationMin, bufferBeforeMin?, bufferAfterMin?}` | Adds or replaces a service and sets it active |
| `catalog.service_retired` | `{code}` | Sets `active: false`; history stays valid |

## 5.2 `schedule`

Schema: `alkaest.scheduling.schedule.v1`. One per professional per calendar month, owned by the space owner.

Initial `state`:

```json
{
  "professional": { "name": "João", "identityId": null },
  "period": "2026-10",
  "timezone": "America/Sao_Paulo",
  "hours": {
    "mon": [["09:00", "18:00"]], "tue": [["09:00", "18:00"]], "wed": [["09:00", "18:00"]],
    "thu": [["09:00", "18:00"]], "fri": [["09:00", "18:00"]], "sat": [["09:00", "13:00"]], "sun": []
  },
  "staff": ["idn_agent", "idn_joao"],
  "appointments": {}
}
```

Rules for the schedule fields:
* **`period`:** written `YYYY-MM`.
* **`timezone`:** an IANA zone name.
* **`hours`:** local working intervals per weekday, written as half-open `HH:MM` pairs.
* **`appointments`:** a map from appointment id to an appointment entry (§6.1). It is maintained by the events in §6.2 and starts empty.

The owner creates next month's schedule before it is needed. A node SHOULD create it when the first booking for that month is requested.

---

# 6. Appointments

## 6.1 Appointment entry

```json
{
  "status": "booked",
  "customerRef": "cus_…",
  "services": [{ "code": "haircut", "durationMin": 30 }],
  "start": "2026-10-19T17:00:00Z",
  "end": "2026-10-19T17:30:00Z",
  "blockStart": "2026-10-19T17:00:00Z",
  "blockEnd": "2026-10-19T17:40:00Z",
  "bookedAt": "2026-10-18T21:15:00Z",
  "canceledBy": null,
  "noticeMin": null
}
```

The fields mean:
* **appointment id:** the `evt_` id of the `appointment.booked` event that created the entry. It is content-derived and unique.
* **`start` and `end`:** when the customer is served.
* **`blockStart` and `blockEnd`:** what the booking occupies, including buffers.
* **Precision:** all four are RFC 3339 UTC instants, precise to the minute.

The booking node computes these values from the catalog. The module checks only the invariants in §6.3. The catalog lives in another object, and a module sees only its own object's state (RFC-0005 §10).

## 6.2 Events

All of these are state events on the professional's `schedule` object.

| Event | `data` | Who may perform it |
|---|---|---|
| `schedule.hours_set` | `{hours}` | Owner |
| `schedule.staff_set` | `{staff}` | Owner |
| `appointment.booked` | `{customerRef, services, start, end, blockStart, blockEnd}` | Staff, or the customer identity booking for itself |
| `appointment.services_added` | `{appointmentId, services, end, blockEnd}` | Staff, or the appointment's customer identity |
| `appointment.rescheduled` | `{appointmentId, start, end, blockStart, blockEnd}` | Staff, or the appointment's customer identity |
| `appointment.canceled` | `{appointmentId, by: "customer" \| "provider"}` | Staff, or the appointment's customer identity (`by` must be `customer`) |
| `appointment.completed` | `{appointmentId}` | Staff |
| `appointment.no_show` | `{appointmentId}` | Staff |

Notes on `services_added` and `canceled`:
* **Added services keep the start time.** `appointment.services_added` replaces `services` with the full new list and extends `end` and `blockEnd`.
* **Not enough room.** If the longer block no longer fits, the event is rejected. The provider's policy decides what to tell the customer: offer alternatives, alert the owner, or notify the next customer. That policy is node configuration (Alkaest Chatbot's `add_service_policy`), not protocol.
* **Notice.** `appointment.canceled` records `noticeMin`: the whole minutes between the event's `createdAt` and the appointment's `start`. The value is negative for a late cancellation.

Rating is an evidence event (RFC-0005 §6.3):

| Event | `data` | Who may perform it |
|---|---|---|
| `appointment.rated` | `{appointmentId, stars}` (`stars` from 1 to 5) | The appointment's customer, or staff relaying the customer's answer on a channel |

## 6.3 Legality rules

A `schedule` module MUST reject an event (RFC-0005 §8) unless all of the rules below hold.

**Time rules:**
1. `start < end`, `blockStart <= start` and `end <= blockEnd`. All values are minute-precise UTC instants.
2. `[blockStart, blockEnd)` lies inside one local day of the schedule's `timezone`, inside the schedule's `period`, and inside one working interval in `hours` for that weekday.
3. `[blockStart, blockEnd)` does not overlap the block of any other appointment whose status is `booked`.

**Lifecycle rules:**
4. Only an appointment whose status is `booked` can be modified. The statuses `completed`, `no_show` and `canceled` are terminal.
5. `appointment.completed` and `appointment.no_show` need an event `createdAt` at or after the appointment's `end`. The signed timestamp keeps this rule deterministic.
6. The actor is allowed by §6.2. "The appointment's customer identity" means `customerRef` equals the actor's identity id.

**Rating rules:**
7. `appointment.rated` refers to a `completed` appointment and is made within 7 days of the `appointment.completed` event.
8. If several valid ratings exist for one appointment, the one with the latest `createdAt` counts, with ties broken by the smallest event id. Ratings never change appointment status.

Times are compared as instants. Local-day and weekday checks convert with the schedule's `timezone`, using the IANA tz database bundled with the implementation.

**Known risk:** nodes with different tz database versions could disagree when an offset changes. Providers SHOULD keep working hours away from transition times, and implementations SHOULD pin the tz database version per protocol release.

---

# 7. Concurrency: Booking Without Double-Booking

Every booking for one professional and month extends the same `schedule` head (RFC-0005 §6.2).

* **Two bookings for overlapping times at the same head:** both target the same version slot. The winner is deterministic (RFC-0005 §9.5) and the loser is `conflicting`. No node will ever show both bookings.
* **Two bookings for different times at the same head:** they also compete, because they target the same slot. The losing node **rebases**: it reads the new head, checks again that the slot is free, and seals a new event with the new `prevEventId` and `targetVersion`. If the slot is still free, the rebased booking applies.
* **Rebasing is automatic.** The Local API (RFC-0009) rebases automatically for commands it authors. Embedded clients rebase before telling the customer anything.

A client confirms a booking to a customer only after its event is `applied`. Alkaest Chatbot's "Agendado ✅" message is sent after that point.

Bookings are human-scale, at most a few events per professional per minute, so serializing them through one object costs nothing noticeable.

---

# 8. Privacy

Service records can be sensitive. A dental or medical service name linked to a person reveals health data, which LGPD art. 11 and GDPR art. 9 treat as a special category.

1. **No personal data in payloads.** Envelopes of this module MUST NOT carry any of the following:
   * phone numbers or customer names;
   * message text, or free-text notes about a customer;
   * health details beyond the provider's own service codes.
2. **Provider spaces are private by default.** `schedule` and `service_catalog` objects are replicated only to the provider's own nodes and paired devices. They are not replicated to the wider network.
3. **What may leave the space.** Only what reputation needs leaves the space, and only in the form RFC-0006 defines. That means aggregates or selectively disclosed evidence, never the raw schedule.
4. **Customer references are per space** (§4). Linking a customer across providers requires the customer's explicit consent and a later RFC.
5. **Deletion.** Erasing the reference mapping on the provider's node unlinks a customer from their history, even though envelopes are immutable.

---

# 9. Mapping from Alkaest Chatbot

| Chatbot today | This module |
|---|---|
| `establishments` | Space; `timezone` and hours go to each `schedule` |
| `professionals` | One `schedule` per professional per month |
| `services` and `service_aliases` | `service_catalog` entries; aliases stay as channel configuration |
| Google Calendar event | Mirror of an applied appointment (integration), no longer the source of truth |
| Booking confirmed on WhatsApp | `appointment.booked` applied, then the confirmation message |
| Services added to an existing appointment | `appointment.services_added` |
| `domain_events` (NETWORK_READINESS.md) | Replaced by signed envelopes in the node |
| Rating request after `rating_request_delay_minutes` | Node job; the answer becomes `appointment.rated` |
| Customer phone (JID) | Customer reference `cus_…`; the mapping stays on the node |

Migration happens in two steps:
1. **First:** the chatbot writes through the node's Local API while still mirroring to Google Calendar.
2. **Then:** the calendar becomes a read-only mirror of the node's applied state.

---

# 10. Reputation Evidence Boundaries

RFC-0006 may consume only these facts from this module:

* **Provider reputation:** `appointment.rated` on `completed` appointments, aggregated per professional and per provider.
* **Customer reliability:** `completed`, `no_show`, and `canceled` with `by` and `noticeMin`, per customer reference.

Customer reliability stays inside the provider's space until the open legal question in NETWORK_READINESS.md (cross-establishment sharing under LGPD) is resolved.

No-shows are recorded only by staff, never inferred.

---

# 11. Security Considerations

* **Agent identity.** The agent identity books on behalf of customers, so a compromised agent key can create or cancel bookings. Owners SHOULD give the agent its own key and remove it from `staff` to revoke it.
* **Validation.** Customers booking with their own identity are checked like any actor (§6.3). A node never trusts client-side availability checks.
* **Rejected bookings.** Booking events that are rejected or conflicting stay in the log as evidence. They do not block the slot.

---

# 12. Open Questions

* Shared resources and multi-professional appointments: a `resource` schedule, plus an atomic booking across two objects.
* Recurring appointments.
* Deposits and no-show fees (RFC-0008).
* Replacing `staff` lists with RFC-0011 capabilities.
* Allowing a single appointment that crosses local midnight (night shifts).
