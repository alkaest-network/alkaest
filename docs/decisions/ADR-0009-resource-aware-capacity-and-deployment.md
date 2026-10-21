# ADR-0009 — Resource-Aware Node Capacity and Deployment

**Status:** Accepted direction; resource profiles and deployment thresholds remain open
**Date:** 2026-10-19
**Decision Type:** Node Architecture and Operations
**Related:** ADR-0001, ADR-0003, ADR-0005, RFC-0002, RFC-0009, [Bisq 2 resource-bound options](../research/bisq2-resource-bounds-and-dispute-authority.md), [network rollout plan](../overview/network-rollout-plan.md)

## Context

Alkaest must run on phones, small home machines, desktops, and servers. More capable machines should improve availability, indexing, replication, and delivery capacity while every node retains the same protocol validation rules. The network rollout already proposes resource-capped containers for local multi-node testing and independent Service nodes across regions.

Kubernetes is a container orchestration and scheduling platform. Its HorizontalPodAutoscaler changes workload replica counts from observed metrics, while node autoscalers provision or consolidate cloud-backed cluster machines. These are different operations from Alkaest's peer roles and network-wide capacity. A Kubernetes cluster also represents one operator's administrative domain, even when it contains many Kubernetes Nodes.

The project has not yet selected deployment technology for Alkaest nodes, gathered representative resource benchmarks, or implemented P2P Service nodes. The protocol should therefore define resource behavior and trust independently from a deployment platform.

## Proposed decision

1. **Keep protocol participation independent of Kubernetes.** A node operator may run a node directly, in a container, or under an orchestrator. No Kubernetes API, cluster controller, or central scheduler is required by the Alkaest protocol.
2. **Defer Kubernetes for the MVP and local multi-node phase.** Phase 0 runs one Standard node. Phase 1 uses containers on one host to simulate 5–10 heterogeneous nodes, with explicit CPU, memory, disk, and bandwidth constraints. Docker Compose or another simple local harness may run that test environment; the harness is not a protocol dependency or a production platform commitment.
3. **Use operator-controlled resource budgets.** Each node profile has hard protocol limits plus lower local caps set by its operator. Advertised capabilities are signed, time-bounded offers, not proof of permanently available or honest capacity. Nodes must tolerate peers overstating or withdrawing capacity.
4. **Use capable Service nodes for opt-in network services.** Subject to RFC-0002 and later implementation, these may provide additional replicas, indexes, archives, relays, bootstrap reachability, and mailbox capacity. Recipients verify signed data and query independent providers where needed. A Service node's hardware, uptime, payment, or capacity claim grants no extra protocol authority or validation weight.
5. **Optimize from measurements.** Before publishing numeric resource profiles or autoscaling rules, benchmark canonical validation, replay, storage growth, sync, indexing, relay traffic, and query workloads on representative Light/low-resource, Standard, and Service hardware. Record throughput, tail latency, peak memory, disk/IO, bandwidth, and power where relevant. Set protocol maxima independently from lower operator-local caps; use backpressure and chunking within those limits.
6. **Scale stateful protocol work through independent nodes and bounded data placement.** Do not make multiple replicas share mutable protocol state as a shortcut to network scaling. Keep signed logs portable and replayable; scale optional stateless or rebuildable services horizontally only where their data and consistency model permit it. Local vertical upgrades are an operator choice, not a protocol requirement.
7. **Keep heavy optional computation replaceable.** Search indexing and AI/model inference may use accelerators or separate workers when a measured workload benefits. They remain optional services. Protocol correctness, identity control, and treasury authority must not depend on a GPU, a particular model, or a high-capacity host.
8. **Evaluate Kubernetes only for an operator's managed service deployment.** Revisit it when measured demand requires multiple production hosts, independently deployable replicas, automated rollouts or recovery, and current operational procedures cannot meet defined availability/latency targets. The evaluation must include cluster security, secrets, persistent data, backups/restore, observability, on-call effort, cloud-provider dependence, and cost. HPA alone changes workload replicas; adding/removing machines requires a separate node-provisioning integration. The choice may be managed Kubernetes, a lightweight distribution, or another tool after that evaluation.
9. **Keep administrative independence visible.** Ten Alkaest nodes operated inside one Kubernetes cluster can test replication, resource constraints, and failure recovery, but do not demonstrate ten independent operators or regional diversity. Network resilience claims must use separately administered hosts/networks and include loss of a provider or region.
10. **Do not reward raw hardware claims.** Any future contribution incentives for storage, relay, bandwidth, or uptime need their own abuse-resistant measurement and governance design. Self-reported capability fields alone must not create reputation, payment, voting power, or admission preference.

## Reproducible benchmark plan

The following are reference workload classes for capacity measurement, not minimum device requirements or protocol limits. Record the exact hardware, operating system, runtime, storage medium, power mode, and software revision for every run; if the reference class is unavailable, document the substitute and its resource envelope.

| Profile under measurement | Reference hardware class | Workload emphasis |
|---|---|---|
| Light / low-resource | Mid-range supported phone, including a constrained-memory run at 4 GiB RAM | bounded envelope parsing and verification, on-demand retrieval, intermittent links, battery/thermal behavior, small local cache, relay-mediated sync |
| Standard | Lower-tier supported desktop or mini PC, 4 CPU cores, 8 GiB RAM, SSD | full replay of participating Space history, concurrent sync, local API queries, indexes needed by the MVP workflow |
| Service | Independently operated server, 8 CPU cores, 32 GiB RAM, NVMe storage and measured public network link | archive/replica ingest, relay and mailbox load, indexing, multi-peer sync, query concurrency, recovery after restart |

Use a versioned synthetic corpus with valid and adversarial records across each data class: small and large envelopes, deeply nested and high-member JSON, batch boundaries, attachment chunks, duplicate/replayed events, out-of-order histories, conflicting branches, resolution events, malformed-but-signed values, and oversized/decompression-bomb inputs. Sweep candidate sizes and concurrency levels to observe failure behavior; corpus sizes are experimental inputs, not selected ceilings. Include both hot-cache and cold-replay runs, and run profiles separately as well as under 5–10-node shared-host contention.

Capture operations/second and bytes/second, p50/p95/p99 latency, peak resident memory, allocation spikes, CPU time, database writes/IOPS, disk growth and replay duration, network bytes, queue depth, thermal throttling and energy where measurable. Every run must report accepted/rejected/deferred counts and confirm identical canonical projections across nodes for the same admitted event set. Fault injection must cover process termination between validation, record persistence, projection update, and checkpoint; after restart, the store must contain either the complete committed transition or no state mutation, and projections must rebuild from admitted records.

Numeric protocol ceilings are selected only after the corpus, benchmark runs, threat review, and low-resource failure behavior are reproducible. Publish each ceiling by data class and unit, separately define local operator caps, and version changes with an explicit compatibility and migration rule. Benchmarks inform the limits; they do not replace the requirement to enforce framing and parser bounds during decoding, validate semantics before durable mutation, and fail closed on exhaustion.

## Consequences

### Positive

- Strong hardware can serve more data and optional network services without becoming more trusted.
- Low-resource nodes retain predictable caps and can apply stricter local limits.
- Kubernetes can be introduced later for a concrete operator problem without coupling protocol clients to it.
- Benchmark evidence, rather than assumed server size, informs resource ceilings and performance targets.

### Costs and limitations

- Operators may initially manage several hosts individually; this is acceptable until operational evidence demonstrates a need for orchestration.
- Capability advertising and resource measurements are claims with freshness and availability limits; they do not prove future service quality.
- Replayable event logs, large archives, or indexes may require separate retention, verification, and placement designs before they scale horizontally.
- A single high-capacity host improves one operator's availability and throughput, but does not provide independent regional failure tolerance.

## Deployment guidance by phase

| Phase | Suggested operating shape | Capacity question |
|---|---|---|
| 0: one local node | Run the Standard node directly or in a simple container as convenient | Measure baseline replay, storage, and validation cost |
| 1: local multi-node | 5–10 isolated containers on one host, with deliberately constrained profiles and fault injection | Verify per-node caps, backpressure, and behavior under shared-host contention |
| 2: real devices | Standard/Light nodes on independently operated home devices and phones | Measure intermittent connectivity, local resource use, and relay need |
| 3: global testnet | Independently operated Service/Standard nodes in separate networks and regions | Measure sync/index/relay demand and single-host/provider/region failures |
| Later managed services | Consider orchestrating one operator's stateless/rebuildable services; evaluate stateful node placement separately | Adopt Kubernetes only when its measured availability and operations benefits justify its security and maintenance cost |

## Follow-up required before acceptance

- Resolve RFC-0002 resource and capability fields, including CPU/memory budgets, freshness/expiry, units, lower local caps, withdrawal, and their non-authority semantics.
- Reconcile RFC-0002 §1's legacy desktop-only wording with ADR-0003 and the profiles in §16 when RFC-0002 is next edited.
- Run and publish the benchmark plan above, then define numeric per-class limits and acceptance targets from measured low-resource behavior.
- Specify which Service workloads are stateless, rebuildable, or stateful and what consistency, retention, and verification each requires.
- Update Phase 1's deployment harness and node-failure scenarios only after the node implementation and benchmark plan are ready.

## References

- [ADR-0003 — Heterogeneous Nodes and Network Validation](ADR-0003-heterogeneous-nodes-and-network-validation.md)
- [RFC-0002 — Node Architecture, §16](../rfc/0002-node-architecture.md#16-node-profiles)
- [Network Rollout Plan](../overview/network-rollout-plan.md)
- [Docker Compose in production](https://docs.docker.com/compose/how-tos/production/)
- [Kubernetes concepts](https://kubernetes.io/docs/concepts/)
- [Kubernetes resource requests and limits](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)
- [Kubernetes workload autoscaling](https://kubernetes.io/docs/concepts/workloads/autoscaling/)
- [Kubernetes node autoscaling](https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/)
