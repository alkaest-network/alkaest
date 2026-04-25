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

    subgraph P3["Phase 3: WhatsApp Discovery Number"]
        USER["Person Searching"]
        DISC["Discovery Assistant"]
        MATCH["Service and Availability Match"]

        USER --> DISC
        EST --> MATCH
        PRO --> MATCH
        SVC --> MATCH
        AUD --> MATCH
        DISC --> MATCH
    end

    subgraph P4["Phase 4: Alkaest Protocol Mapping"]
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

    subgraph P5["Phase 5: Progressive Decentralization"]
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
```

## Notes

This diagram shows product progression, not a commitment that all chatbot data becomes public protocol data.

Appointment-derived records must be filtered through privacy, consent, and minimization rules before becoming network Evidence.

