# Node Architecture

```mermaid
flowchart TD
    UI["Developer UI / Automation"] --> API["API Server"]
    GH["GitHub Integration"] --> ADAPTER["Integration Adapters"]

    subgraph NODE["Local Standard Node (first implementation target)"]
        API --> CMD["Command Handler"]
        ADAPTER --> CMD
        CMD --> ID["Identity Engine"]
        ID --> ENV["Envelope Engine"]
        ENV --> OBJ["Object and Event Engine"]
        OBJ --> PROJ["Projection Engine"]
        OBJ --> STORE["Storage Engine"]
        PROJ --> STORE
        OBJ --> SYNC["P2P Sync Engine"]
        SYNC --> MAIL["Mailbox Service"]
    end

    SYNC --> NET["Alkaest P2P Network"]
```

## Notes

- This diagram shows the first implementation path. The architecture supports Light, Standard, and Service profiles; see [RFC-0002](../rfc/0002-node-architecture.md) §16 and [ADR-0003](../decisions/ADR-0003-heterogeneous-nodes-and-network-validation.md).
- GitHub is an integration input, not protocol authority.
