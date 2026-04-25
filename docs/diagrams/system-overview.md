# System Overview

```mermaid
flowchart LR
    subgraph USER["Developer Environment"]
        UI["Developer UI"]
        AUTO["Local Automation"]
        NODE["Local Alkaest Node"]
        UI --> NODE
        AUTO --> NODE
    end

    subgraph NODE_RUNTIME["Node Runtime"]
        API["API Server"]
        ID["Identity Engine"]
        ENV["Envelope Engine"]
        OBJ["Object and Event Engine"]
        PROJ["Projection Engine"]
        STORE["Storage Engine"]
        SYNC["P2P Sync Engine"]
        MAIL["Mailbox Service"]
        ADAPTER["Integration Adapters"]

        NODE --> API
        API --> ID
        ID --> ENV
        ENV --> OBJ
        OBJ --> PROJ
        OBJ --> STORE
        OBJ --> SYNC
        SYNC --> MAIL
        ADAPTER --> API
    end

    GH["GitHub"]
    CI["CI / External Evidence"]
    P2P["Alkaest P2P Network"]
    PEERS["Other Alkaest Nodes"]

    GH --> ADAPTER
    CI --> ADAPTER
    SYNC --> P2P
    P2P --> PEERS
```

## Notes

- The MVP is desktop-first and assumes a local full node per developer.
- The local node is the protocol boundary for UI, automation, and integrations.
- GitHub and CI systems are inputs to the node, not protocol authorities.
- Detailed node internals are described in [node-architecture.md](/Users/nivaldojunior/Documents/Alkaest/alkaest/docs/diagrams/node-architecture.md).
