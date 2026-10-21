# ADR-0002 - Chatbot Commercial Wedge

**Status:** Accepted
**Date:** 2026-04-25
**Decision Type:** Product Strategy and Protocol Direction
**Amended:** 2026-10-19 — production WhatsApp channel and usage-based customer billing

---

## Context

Alkaest began as a protocol-first project for decentralized work coordination.
The current protocol documents focus on a desktop-first MVP for open-source development coordination.

There is also a sibling project, Alkaest Chatbot, which defines a WhatsApp scheduling assistant for local service providers such as barbers, dentists, doctors, salons, and clinics.

The chatbot project has a clearer near-term commercial path:

* sell scheduling automation to known local businesses
* start with WhatsApp because customers and owners already use it
* generate revenue before the decentralized protocol is production-ready
* collect real operational data from appointments, cancellations, availability, and provider reliability

The strategic question is how to connect this commercial product with the long-term Alkaest network without making the protocol too narrow or delaying revenue behind decentralization work.

---

## Decision

Alkaest will treat **Alkaest Chatbot as the commercial wedge** for the broader Alkaest vision.

The planned sequence is:

```text
Alkaest Chatbot -> Private Service-Network Backend Pilot -> Discovery Frontend -> Alkaest Network
```

This means:

* Alkaest Chatbot may start as a centralized, locally operated product.
* The first customers are appointment-based local service providers.
* The product should prioritize revenue, reliability, and customer proof.
* After a useful provider base exists, integrate the chatbot with provider-private Alkaest Spaces and validate the backend on an isolated multi-node network before adding protocol-facing discovery or reputation screens.
* After the backend gate passes, Alkaest may add a public WhatsApp discovery number where consumers can search for professionals already served by the chatbot.
* The decentralized Alkaest protocol should carry only the durable coordination concepts proven by the chatbot business. Completion, customer feedback, and reputation are separate evidence concepts; consequential reputation remains gated on RFC-0006.

The protocol core remains generic.
It must not become specific to WhatsApp, Google Calendar, Baileys, Brazil, or scheduling.

### Production channel and commercial billing (amendment, 2026-10-19)

1. **Use the official WhatsApp Business Platform API for production messaging.** The Cloud API is the default integration when it meets the product's needs. Keep the messaging provider behind an adapter so channel policy and transport do not become protocol rules. Unofficial WhatsApp automation is not the production path.
2. **Charge each provider according to measured usage, not a flat recurring subscription as the sole price.** The billed customer is the business/provider using Alkaest Chatbot; people messaging that business do not pay Alkaest for sending or receiving a WhatsApp message.
3. **Give each customer a traceable usage ledger.** Attribute delivered WhatsApp messages to the correct customer account and number, record the applicable category/market and provider charge where available, and separately measure AI inference and other variable service usage. Retries and duplicate webhooks must not create duplicate billable records.
4. **Separate pass-through costs from Alkaest's service charge.** A statement should show Meta/provider charges under the rate rules active at the time, variable AI/hosting usage, and the disclosed Alkaest service margin. Do not hard-code WhatsApp rate cards into the product; Meta's prices depend on delivery, recipient market, category, volume rules, and may change. Recheck the official [Business Platform pricing](https://whatsappbusiness.com/products/platform-pricing/) before launch and when Meta announces changes.
5. **Make variable usage predictable.** Show an estimate before onboarding, a live or recent usage view, billing-period statements, and customer-selected warning and spending thresholds. At a configured cap, stop or degrade optional outbound/AI-heavy behavior safely and provide a clear handoff path; do not silently accrue unlimited cost.
6. **Follow WhatsApp consent and messaging rules.** Store consent and opt-out state by customer and message purpose, apply current template and service-window requirements, and do not optimize revenue by generating unnecessary messages.

The exact Alkaest per-usage margin, billing period, payment method, customer-owned versus Alkaest-managed WhatsApp Business Account (WABA), and minimum/activation fee remain open until cost simulations and a pilot validate them. This amendment chooses the metered model and official production channel, not a final price list.

---

## Why this decision was made

### 1. The chatbot can produce revenue earlier

A decentralized protocol may take substantial design and implementation time before it can support real economic coordination.
The chatbot can serve local businesses sooner and fund continued work.

### 2. WhatsApp matches the first market

Small local businesses in the target market already coordinate with customers through WhatsApp.
A chatbot can reduce friction without asking them to install new software or understand protocol concepts.

### 3. Scheduling creates useful marketplace data

Appointments produce concrete records:

* service offered
* provider availability
* customer demand
* bookings
* cancellations
* completions
* operational reliability

These records can later become reputation and evidence inputs if privacy and consent are handled correctly.

### 4. The discovery number creates a bridge

A public WhatsApp number for finding professionals can become the first marketplace-like surface.
It can validate demand discovery before the system becomes decentralized.

### 5. Progressive decentralization reduces risk

The project should decentralize proven workflows rather than speculating too early.
This keeps the first product useful while preserving the long-term protocol direction.

---

## Consequences

### Positive consequences

* Alkaest gets a clearer revenue path.
* The project can learn from real service providers before designing marketplace modules.
* The protocol gains a practical future domain beyond open-source development.
* Provider reputation can be grounded in real outcomes instead of abstract ratings.
* The discovery number creates a natural bridge from SaaS to network.
* Customers can scale their bill with actual chatbot usage; variable Meta, AI, and service costs are visible instead of hidden in one flat plan.

### Negative consequences

* The product direction becomes broader than the original open-source development MVP.
* There is a risk that the chatbot business remains centralized and never becomes protocol-native.
* Appointment data introduces stronger privacy concerns, especially for health-related services.
* The team must avoid mixing commercial product urgency with protocol correctness.

### Constraints introduced

* Chatbot-specific details must stay out of the protocol core.
* Service scheduling is specified in Draft RFC-0007 as a domain module, not RFC-0001 behavior; backend integration and privacy validation remain ahead of protocol-facing discovery/reputation screens.
* Chatbot data models should preserve enough audit history to map to future protocol Evidence.
* Any future network export of appointment history must respect privacy, consent, and minimization.
* Early providers should not be required to run protocol nodes.
* Production WhatsApp messaging uses the official platform API, with explicit consent and usage accounting. The channel and its changing prices remain product integration details, not protocol rules.

---

## Relationship to current RFCs

This decision does not replace the existing RFCs.

It adds a commercial bootstrap path alongside the protocol foundation:

* RFC-0001 remains the protocol core.
* RFC-0002 remains the node architecture.
* RFC-0003 remains the development workflow module.
* RFC-0004 remains the canonical encoding and identifier specification.
* RFC-0005 remains the object/event semantics and state resolution specification.

The Service Scheduling Workflow Module is now specified as Draft [RFC-0007](../rfc/0007-service-scheduling-module.md); it should be refined once the chatbot product has produced enough real operational learning.

---

## Relationship to ADR-0001

ADR-0001 says the protocol MVP is desktop-first for open-source development coordination.

This ADR does not require barbers, dentists, doctors, customers, or small business owners to run desktop nodes in the early chatbot product.

Instead, it separates:

* the protocol MVP, which remains desktop-first
* the commercial wedge, which starts through WhatsApp
* the long-term network, which may later decentralize proven service coordination flows

---

## Follow-up implications

Upcoming documentation should:

* add a service scheduling module to the RFC roadmap (done: Draft [RFC-0007](../rfc/0007-service-scheduling-module.md))
* map chatbot concepts to Alkaest primitives
* define privacy boundaries for appointment-derived evidence
* keep the chatbot implementation test-first
* keep operational chatbot choices behind adapters where possible
* avoid making centralized operator assumptions part of the protocol core

---

## Summary

Alkaest will use Alkaest Chatbot to get real customers, revenue, and service coordination data before the decentralized network is ready.

The chatbot business should remain practical and centralized at first.
The protocol should remain generic and absorb only the durable coordination concepts that are proven through real use.
