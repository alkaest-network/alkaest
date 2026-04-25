# Chatbot-to-Network Strategy

## Purpose

This document connects the Alkaest Chatbot business path with the long-term Alkaest protocol vision.

The short version:

```text
Alkaest Chatbot -> WhatsApp Discovery Number -> Alkaest Network
```

Alkaest Chatbot is the commercial wedge.
The Alkaest protocol remains the long-term decentralized coordination layer.

See also:

- [Chatbot-to-Network Progression](/Users/nivaldojunior/Documents/Alkaest/alkaest/docs/diagrams/chatbot-to-network.md)

The goal is not to make the protocol a scheduling chatbot.
The goal is to use a real scheduling business to create revenue, operational experience, verified service history, and a first marketplace dataset that can later become protocol-native.

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

Once Alkaest Chatbot has a base of paying clients, the next product layer can be a public WhatsApp discovery number where people search for professionals already using the chatbot.
That creates the first marketplace-like experience without requiring decentralization on day one.

After enough professionals, appointments, and reputation evidence exist, the system can progressively move parts of that coordination model into Alkaest protocol objects, events, identities, evidence, and reputation.

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

### Phase 3: WhatsApp Discovery Number

Create a public WhatsApp number for consumers to search for available professionals in the Alkaest Chatbot base.

The discovery number should support:

- natural language search
- location-aware provider discovery
- service matching
- availability checks
- routing to a provider
- optional booking through the same conversation

This phase introduces marketplace behavior, but it may still be centrally operated.

The key protocol lesson is discovery:

```text
Customer demand -> service search -> provider availability -> booking intent -> outcome evidence
```

### Phase 4: Protocol Mapping

Start representing proven chatbot concepts as Alkaest-compatible objects and events.

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
| Completed appointment | Evidence |
| Provider reliability | Reputation evidence |

This does not require changing RFC-0001.
It likely requires a future service workflow module RFC.

### Phase 5: Progressive Decentralization

Move selected responsibilities from the centralized chatbot system into protocol-native coordination.

Potential order:

1. Export signed provider profiles and service catalogs.
2. Issue portable evidence for completed appointments.
3. Represent provider reputation as protocol evidence.
4. Let providers control their own identity and service history.
5. Let discovery read from protocol state instead of only the central database.
6. Introduce provider-run or community-run nodes.
7. Move settlement, validation, and dispute mechanisms into later protocol modules when needed.

Progressive decentralization should be earned by real use.
Do not decentralize parts that have not been operationally proven.

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

Service scheduling should live in a future domain module, similar to how open-source development is currently represented by RFC-0003.

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

Not all of this data should be public.
Privacy and consent must be handled before exporting anything to a decentralized network.

### Preserve Provider Portability

The long-term promise should be that a professional can eventually carry their reputation and service history outside the original chatbot operator.

That means the system should avoid designing reputation as merely a private ranking inside a central database.

### Do Not Force Nodes Too Early

Barbers, dentists, and doctors should not need to run Alkaest nodes in the early commercial product.

Early adoption should be through WhatsApp.
Node operation can become relevant later for providers, operators, communities, or advanced users who want stronger control.

---

## New RFC Direction

The current RFC sequence can remain valid for the protocol foundation.

Add a future module RFC:

```text
RFC-0006 or later: Service Scheduling Workflow Module
```

That RFC should define:

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

If RFC-0006 remains reserved for reputation proofs and scoring, the service scheduling module can become RFC-0007 or later.

---

## Business Strategy

The chatbot strategy should prioritize revenue and proof.

Recommended sequence:

1. Make the first barber successful.
2. Add one dentist or similar professional service.
3. Standardize onboarding.
4. Keep pricing simple in BRL.
5. Build reliability before broad growth.
6. Use testimonials and referrals before paid traffic.
7. Create the discovery number only after there are enough providers to make search useful.

The discovery number should not launch too early.
If there are too few providers, it will feel empty and damage trust.

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
Baileys is unofficial and can create account/session instability.

Mitigation:
Keep WhatsApp behind a messaging port and preserve a migration path to the official WhatsApp Business Platform.

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
