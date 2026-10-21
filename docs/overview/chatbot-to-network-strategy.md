# Chatbot-to-Network Strategy

## Purpose

This document connects the Alkaest Chatbot business path with the long-term Alkaest protocol vision.

The short version:

```text
Alkaest Chatbot -> Private Service-Network Backend Pilot -> Discovery Frontend -> Alkaest Network
```

Alkaest Chatbot is the commercial wedge.
The Alkaest protocol remains the long-term decentralized coordination layer.

See also:

- [Chatbot-to-Network Progression](../diagrams/chatbot-to-network.md)

The goal is not to make the protocol a scheduling chatbot.
The goal is to use a real scheduling business to create revenue, operational experience, verified service history, and a first marketplace dataset that can later become protocol-native.
Over a longer horizon, the product can grow into an opt-in operating layer for independent professionals and a set of reusable tools for self-governed open-source projects. The [roadmap](roadmap.md) separates those capabilities from the first chatbot launch.

---

## Strategic Thesis

Alkaest needs a practical path from idea to revenue before the decentralized network is ready.

The chatbot project provides that path because it can start as a useful centralized product for local businesses:

- barbershops
- dentists
- doctors
- salons
- clinics
- other appointment-based service providers

These businesses already use WhatsApp as their daily operating interface.
The first product should meet them there instead of asking them to adopt a new app, dashboard, wallet, or protocol node.

Once Alkaest Chatbot has a base of paying clients, first integrate the protocol behind the existing interface and validate provider-private service records on isolated nodes. The service network must be well tested before a protocol-facing discovery or reputation frontend is exposed. After that backend gate, a public WhatsApp discovery number can create the first marketplace-like experience without requiring providers to run nodes.

Progressively move only proven coordination concepts into protocol objects, events, identities, and evidence. Do not treat service completion or a rating as mature reputation; RFC-0006's integrity, consent, and appeal requirements remain separate gates.

---

## Relationship Between The Projects

### Alkaest Chatbot

Alkaest Chatbot is the near-term product.
It is a WhatsApp scheduling assistant for small local service providers.

Its immediate goals are:

- help customers book and cancel appointments through natural language
- help business owners reduce manual WhatsApp scheduling work
- generate early revenue
- learn real operational constraints
- collect trustworthy service and appointment history
- build relationships with local providers

In V1, Alkaest Chatbot may remain centralized and locally operated.
That is acceptable because its job is validation and revenue, not protocol purity.

### WhatsApp Discovery Number

The admin discovery number is the bridge product.

It is a WhatsApp number where any person can ask for professionals from the Alkaest Chatbot client base.

Examples:

```text
Preciso de um barbeiro hoje a tarde em Uberlandia.
```

```text
Tem dentista com horario essa semana?
```

```text
Quero cortar cabelo amanha perto do centro.
```

The system can search the existing client base, check availability, and route the customer to a professional.

This creates a simple marketplace surface before the decentralized protocol is ready.
It also gives Alkaest a reason to standardize provider profiles, service catalogs, availability, location, evidence, and reputation-like signals.

### Alkaest Protocol

The Alkaest protocol is the long-term decentralized coordination network.

Its role is to turn the proven centralized business model into portable, verifiable coordination primitives:

- professional identities
- provider spaces
- service objects
- appointment or work objects
- signed events
- evidence of completed service
- customer or provider decisions
- reputation derived from real outcomes
- decentralized discovery and coordination

The protocol should remain generic.
It should support service scheduling as one future domain without hard-coding WhatsApp, Google Calendar, Baileys, barbershops, dentists, or any single local market into the core.

---

## Product Phases

### Phase 0: Protocol Research

This is the current Alkaest documentation base:

- RFC-0001 defines the protocol core.
- RFC-0002 defines the node architecture.
- RFC-0003 defines the first development workflow module.
- RFC-0004 defines envelope encoding and IDs.
- RFC-0005 defines object/event semantics and state resolution.

This phase is still useful, but it should no longer be the only path to progress.

### Phase 1: Chatbot Revenue Wedge

Build and sell Alkaest Chatbot to a small number of trusted local clients.

Initial client profile:

- local business in Uberlandia-MG
- appointment-based
- owner already uses WhatsApp
- simple working hours
- one establishment
- one or more professionals
- Google Calendar can be the appointment source of truth

Phase 1 should optimize for:

- first happy client
- reliability
- low cost
- simple onboarding
- test-first implementation
- operational runbooks
- clear audit data
- repeatable local sales
- official WhatsApp Business Platform API for production messaging
- usage metering and a clear monthly statement for each provider

Phase 1 should not optimize for:

- public SaaS onboarding
- multi-city discovery
- decentralized operation
- self-custody
- protocol wallets
- open marketplace governance

### Phase 2: Client Base And Operational Data

Grow from one client to a small base of paying providers.

Important outputs:

- standardized establishment profiles
- standardized professional profiles
- service catalogs
- appointment audit records
- cancellation records
- availability and demand patterns
- customer contact mappings
- provider reliability signals
- support and failure patterns

This data should stay practical first.
It should also be shaped so it can later map to Alkaest protocol concepts.

### Phase 3: Protocol Backend Pilot Behind The Chatbot

Start representing proven chatbot concepts as Alkaest-compatible objects and events before exposing them through a protocol-facing frontend. The chatbot remains the user interface while a provider-authorized node records scheduling events in private Spaces and an isolated test network validates them. This backend-first step tests the actual network lifecycle before adding a new discovery or reputation interface.

Possible mappings:

| Chatbot Concept | Alkaest Concept |
| --- | --- |
| Business owner | Identity |
| Establishment | Space |
| Professional | Identity or Space member |
| Service catalog entry | Object |
| Appointment | WorkItem-like Object or service booking Object |
| Booking created | Event |
| Booking cancelled | Event |
| Calendar change | Evidence or external integration event |
| Customer notification | Message |
| Admin command | Decision or privileged Event |
| Provider-recorded completed appointment | Provider-authored service outcome evidence |
| Optional customer rating | Separate customer-feedback evidence with explicit consent and source provenance |
| Provider reliability | A later reputation interpretation of multiple eligible evidence items, gated by RFC-0006 |

These are different claims. A provider's `appointment.completed` event is evidence that the provider recorded completion; it does not prove by itself that useful work occurred. A star rating or comment is feedback, not proof of completion or merit. A WhatsApp reply relayed by the provider's integration is attributable to that integration/channel and is not a cryptographic signature by the customer's Alkaest identity. Where a customer has an Alkaest identity, direct signed feedback can carry stronger provenance, but it remains a subjective claim and still needs abuse controls.

The customer-facing chatbot may offer a brief, optional feedback request after the service. Explain what will be stored and whether it may be used in provider reputation; declining or ignoring it must not affect service access. Free-text comments can contain personal or sensitive information, so they stay private to the provider's product records by default and are never copied to public/protocol records by default. Only a deliberately consented, minimized, policy-eligible feedback record can be considered for later portability. Do not ask for health details or publish customer comments as a reputation shortcut.

#### Backend-first network gate

Before a reputation or protocol frontend is introduced, the chatbot-to-node backend must pass the [network rollout plan's service-data gate](network-rollout-plan.md#service-domain-backend-gate). Use private provider Spaces and isolated test identities/nodes. Initially use synthetic records; real appointments or feedback may be used only with a clear provider/customer notice, an opt-in basis appropriate to the jurisdiction, data minimization, and a way to decline. Do not hide the collection or network use from participants even though the integration runs behind the existing chatbot interface.

The gate proves deterministic scheduling state, valid signatures/authority, privacy boundaries, idempotent chatbot retries, recovery and multi-node replication, and accurate provenance labels. Passing it enables only the next private/consented pilot step. It does not turn ratings into mature reputation or authorize public discovery/ranking; RFC-0006's integrity launch gate still applies.

### Phase 4: WhatsApp Discovery Number

After the service-domain backend gate, create a public WhatsApp number for consumers to search for professionals in the Alkaest Chatbot base. The discovery number should support natural-language search, service matching, availability checks, routing to providers, and optional booking.

This phase introduces marketplace behavior and may remain centrally operated. Initially, discovery results use service fit and availability; reputation-based ranking remains blocked until RFC-0006 passes its integrity launch gate.

The key protocol lesson is discovery:

```text
Customer demand -> service search -> provider availability -> booking intent -> outcome evidence
```

This does not require changing RFC-0001. The service workflow is described in Draft RFC-0007; backend validation and privacy review must precede protocol-facing discovery or reputation screens.

### Phase 5: Progressive Decentralization

Move selected responsibilities from the centralized chatbot system into protocol-native coordination.

Potential order:

1. Export provider-authorized profiles and service catalogs.
2. Issue portable, provenance-labeled evidence for provider-recorded completed appointments.
3. Accept optional customer feedback separately, with explicit consent and source strength recorded.
4. Let providers control their own identity and service history.
5. Let discovery read from protocol state instead of only the central database.
6. Represent provider reputation only after RFC-0006 defines integrity, privacy, challenge, and appeal rules.
7. Introduce provider-run or community-run nodes.
8. Move settlement, validation, and dispute mechanisms into later protocol modules when needed.

Progressive decentralization should be earned by real use.
Do not decentralize parts that have not been operationally proven.

### Phase 6: Professional Tools And Project Spaces

After the network has working provider and contributor flows, Alkaest may add an opt-in professional dashboard that connects open-source tools for scheduling, customer management, invoicing, bookkeeping, and reporting. Integrations remain replaceable, user-authorized, exportable, and outside protocol core. Reports begin with explainable historical facts; forecasts such as low-demand windows for a holiday are optional decision support with visible assumptions and uncertainty.

In parallel, provide project onboarding templates so open-source projects can create their own Spaces, publish governance and budget policies, fund WorkItems, and rotate roles. These spaces can adopt DAO-like decision processes without a mandatory token, shared global treasury, or claim that protocol membership alone defines a legal DAO.

Do not select a fixed set of tools or promise predictive business outcomes until provider interviews and a small pilot establish which data is available, useful, and safe to connect.

The first tool comparison and pilot proposal are recorded in the [professional tools integration pilot](../research/professional-tools-integration-pilot.md). Dolibarr is only the first candidate to validate; this does not commit the product to that tool.

---

## Protocol Design Implications

### Keep The Core Generic

The protocol core must not become:

- WhatsApp-specific
- Google Calendar-specific
- Brazil-specific
- scheduling-only
- controlled by a central operator

Instead, the core should continue to define generic primitives:

- Identity
- Space
- Membership
- Object
- Event
- Relation
- Message
- Decision
- Envelope

Service scheduling belongs in a domain module, not protocol core. It is currently described by Draft RFC-0007 and must be validated through the chatbot backend pilot before protocol-facing service screens are introduced.

### Treat Chatbot Records As Future Evidence

The chatbot should store enough operational history to become evidence later:

- who booked
- which provider accepted
- which service was scheduled
- when the appointment was created
- whether the appointment was completed, cancelled, or missed
- which calendar event represented the booking
- which admin command changed the schedule
- which notification was sent

Not all of this data should be public. Appointment completion, customer feedback, and review text are separate records with different authors and evidentiary strength. Privacy and explicit notice/consent must be handled before any real customer-derived record is exported or replicated to a network.

### Preserve Provider Portability

The long-term promise should be that a professional can eventually carry their reputation and service history outside the original chatbot operator.

That means the system should avoid designing reputation as merely a private ranking inside a central database.

### Do Not Force Nodes Too Early

Barbers, dentists, and doctors should not need to run Alkaest nodes in the early commercial product.

Early adoption should be through WhatsApp.
Node operation can become relevant later for providers, operators, communities, or advanced users who want stronger control.

---

## New RFC Direction

The current RFC sequence remains valid for the protocol foundation. Draft RFC-0007 already describes the service scheduling module; its next revision should incorporate evidence from the backend pilot and retain clear boundaries for:

- provider Spaces
- professional Membership
- service catalog Objects
- appointment or booking Objects
- booking lifecycle Events
- customer/provider Messages
- admin Decisions
- completion Evidence
- cancellation Evidence
- reputation evidence boundaries
- privacy rules for service records

The service module identifies source events only. RFC-0006 must separately specify how any evidence may contribute to reputation and what consent, independence, challenge, and appeal rules apply.

---

## Business Strategy

The chatbot strategy should prioritize revenue and proof.

Recommended sequence:

1. Make the first barber successful.
2. Add one dentist or similar professional service.
3. Standardize onboarding.
4. Keep usage pricing simple to understand in BRL: measured usage, separated cost components, estimates, alerts, and a customer-selected cap.
5. Build reliability before broad growth.
6. Use testimonials and referrals before paid traffic.
7. Create the discovery number only after there are enough providers to make search useful.

The discovery number should not launch too early.
If there are too few providers, it will feel empty and damage trust.

### Usage-Based Commercial Model

Alkaest Chatbot should charge the service provider according to measured usage rather than relying on a fixed recurring subscription as the only price. The WhatsApp API bill varies with the applicable provider pricing rules, while Alkaest's own variable cost also changes with AI inference and other usage. Keep those cost sources visible as separate line items.

The usage ledger should attribute provider-delivered messages, applicable Meta/provider charges, AI consumption, and relevant service actions to one business account and billing period. Count a WhatsApp message as a Meta pass-through cost only when the active Meta rules make that event billable; do not equate every inbound/outbound message with a Meta fee. Deduplicate webhook events and sending retries before calculating charges.

Before a provider connects its number, show a usage estimate and explain which costs can vary. Let each provider set warning thresholds and a spending cap, then degrade optional automation safely at the cap with a clear human handoff. The exact Alkaest margin and whether WABAs are customer-owned or Alkaest-managed remain open until a cost model and pilot are complete. Recheck Meta's [official pricing page](https://whatsappbusiness.com/products/platform-pricing/) before launch because categories and rates can change.

---

## Risks

### Centralization Drift

Risk:
The chatbot business becomes a normal centralized SaaS and never returns to the protocol vision.

Mitigation:
Record protocol mappings early, store exportable evidence, and keep future provider portability as a product constraint.

### Premature Decentralization

Risk:
The project forces protocol complexity into a product that needs simple WhatsApp reliability.

Mitigation:
Keep Phase 1 centralized and operationally boring.
Only decentralize proven flows.

### Privacy And Consent

Risk:
Appointment data can include sensitive personal information, especially for dentists and doctors.

Mitigation:
Treat health-related scheduling as higher risk.
Do not publish customer appointment details to a network.
Design reputation evidence around minimal proofs and consent.

### WhatsApp Provider Risk

Risk:
An unofficial integration or an undocumented provider surcharge can create account/session instability, customer billing disputes, and unexpected operating costs.

Mitigation:
Use the official WhatsApp Business Platform API in production, keep it behind a messaging adapter, reconcile usage from provider delivery events, and show any intermediary/BSP fees separately.

### Protocol Scope Creep

Risk:
The protocol absorbs every chatbot feature.

Mitigation:
Keep operational product features in the chatbot.
Move only durable coordination concepts into RFCs.

---

## Updated North Star

Alkaest should start by solving a real coordination problem for real local businesses.

The first revenue product is:

```text
WhatsApp scheduling for service providers.
```

The first marketplace bridge is:

```text
A WhatsApp discovery number for professionals already in the Alkaest Chatbot base.
```

The long-term network is:

```text
A decentralized coordination protocol where service providers, customers, developers, and other workers can discover each other, coordinate work, and build portable reputation from verifiable evidence.
```

---

## Network Readiness in the Chatbot (2026-10)

The chatbot implementation and its operational design are in a private repository. This public summary records the current protocol-facing direction; it is sufficient context for discussing or proposing changes here:

- domain facts recorded as append-only, signed events (Space = establishment, Object = appointment, Event, Evidence);
- an Ed25519 key pair per establishment node from install time;
- pseudonymous customer identifiers outside the establishment;
- two-sided reputation: customers rate providers after completed appointments (delay configurable per establishment), and customer reliability is derived from outcomes.

These choices are intended to keep the protocol generic: nothing in them is specific to WhatsApp, Google Calendar or barbershops. The detailed design may change; this summary does not make the private implementation available to public contributors.

