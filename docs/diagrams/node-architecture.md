# Node Architecture

```mermaid
flowchart TD
    UI["Developer UI / Automation"] --> API["API Server"]
    GH["GitHub Integration"] --> ADAPTER["Integration Adapters"]

    subgraph NODE["Local Alkaest Node (MVP Full Node)"]
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

- The MVP assumes a local full node per developer.
- GitHub is an integration input, not protocol authority.
- Light-client behavior is intentionally out of scope for this diagram.
