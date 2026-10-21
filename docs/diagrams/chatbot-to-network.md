# Chatbot-to-Network Progression

```mermaid
flowchart LR
    subgraph P1["Phase 1: Alkaest Chatbot"]
        OWNER["Business Owner"]
        WA["Customer WhatsApp"]
        BOT["Scheduling Chatbot"]
        CAL["Google Calendar"]
        DB["Operational Database"]

        WA --> BOT
        OWNER --> BOT
        BOT --> CAL
        BOT --> DB
    end

    subgraph P2["Phase 2: Provider Base"]
        EST["Establishment Profiles"]
        PRO["Professional Profiles"]
        SVC["Service Catalogs"]
        AUD["Appointment Audit"]

        DB --> EST
        DB --> PRO
        DB --> SVC
        DB --> AUD
    end

    subgraph P3["Phase 3: Private Protocol Backend Pilot"]
        BOTNODE["Chatbot -> Provider Node"]
        TESTNET["Isolated Multi-Node Test Network"]
        BOTNODE --> TESTNET
    end

    subgraph P4["Phase 4: WhatsApp Discovery Number"]
        USER["Person Searching"]
        DISC["Discovery Assistant"]
        MATCH["Service and Availability Match"]

        USER --> DISC
        EST --> MATCH
        PRO --> MATCH
        SVC --> MATCH
        DISC --> MATCH
    end

    subgraph P5["Protocol Objects And Evidence (Mapped In Phase 3)"]
        ID["Identity"]
        SPACE["Space"]
        OBJ["Object"]
        EVT["Event"]
        MSG["Message"]
        DEC["Decision"]
        EVD["Evidence"]

        EST --> SPACE
        PRO --> ID
        SVC --> OBJ
        AUD --> EVT
        AUD --> EVD
        DISC --> MSG
        OWNER --> DEC
    end

    subgraph P6["Progressive Decentralization"]
        NODE["Provider or Community Node"]
        NET["Alkaest Network"]
        REP["Portable Reputation"]

        ID --> NODE
        SPACE --> NODE
        OBJ --> NODE
        EVT --> NODE
        EVD --> NODE
        NODE --> NET
        NET --> REP
    end

    AUD --> BOTNODE
    TESTNET --> DISC
    TESTNET --> MATCH
    TESTNET --> EVD
```

## Notes

This diagram shows product progression, not a commitment that all chatbot data becomes public protocol data.

The protocol backend is validated behind the existing chatbot before the discovery or reputation frontend is exposed. Appointment-derived records must be filtered through privacy, consent, provenance, and minimization rules before becoming network Evidence. Completion, customer feedback, and reputation are separate concepts.

