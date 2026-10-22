---
title: Agent Systems and Edge Orchestration
domain: ai-infra
tags:
  - agent
  - orchestration
  - slm
  - grpc
  - edge
  - scheduling-analogy
  - safety
aliases:
  - GRAFT
  - multi-device agent mesh
  - task routing
  - agentic ai
last-updated: 2026-10-22
---

# Agent Systems and Edge Orchestration

## 1. The shape of the problem

A single small language model (SLM) on one device handles short prompts. Many real tasks exceed the **context budget** or the **inference capacity** of a constrained endpoint. Example used in the literature: summarising a 941-page novel is feasible on a laptop only with aggressive truncation, while phone-class SLMs must trade coverage against degraded over-budget behaviour.

Two ways out: send it to the cloud (privacy, availability, cost), or **orchestrate a small heterogeneous mesh of nearby devices**. This note covers the second.

## 2. GRAFT — a concrete reference system

**GRAFT = gRPC-Routed Agent Framework for Tasking** (in Edge and Personal Devices).
- Published in **CAIS '26: Proceedings of the ACM Conference on AI and Agentic Systems**, pages 1204–1212, **26 May 2026**, DOI **10.1145/3786335.3813216**.
- Authors: Chinmay Shringi, Alon Hillel-Tuch, Sariya Rizwan.

> **Naming caution:** the acronym GRAFT is also used by an unrelated reinforcement-learning paper ("Gated Replacement of Answer-Failed groups with peer Trajectories"). Always write the full name when you cite it.

### 2.1 What it provides
- A **sessioned gRPC control plane** with device registration and a capability model.
- **Capability-aware policy routing.**
- A **compute-target inference router** dispatching by **CPU / GPU / NPU** target, with explicit fallback when an accelerator path is unavailable.
- **Safety-bounded remote execution**: command allowlists, bounded file access, one-time transfer tickets.
- **Per-request telemetry.**

### 2.2 Evaluation setup and findings
- Four-device mesh spanning **Apple (laptop), Snapdragon X Elite (laptop), Samsung (mobile), Arduino Q (embedded)**.
- Workflow: multi-device PDF summarisation — a coordinator partitions the document, each device runs a local SLM, partial results are merged through a **staged execution plan with explicit synchronisation barriers**.
- Test workloads: 13-page and ~1000-page instrumented PDFs, plus public-domain books (*The Adventures of Sherlock Holmes*, 183 pages; *The Count of Monte Cristo*, 941 pages).

**Key findings:**
1. All planned tasks execute on their intended devices; stage ordering is preserved.
2. **End-to-end completion time is governed by the slowest parallel worker, not by total document size.**
3. **For small personal meshes, the bottleneck is lightweight local orchestration, not raw compute.**
4. A capable laptop-class model can beat the mesh on raw wall clock — **but only the mesh achieves higher aggregate coverage while keeping every worker inside its native budget.** A phone-class 1B model either covers substantially less input or degrades badly when pushed beyond budget.

Finding 2 is the one to remember: it is the same result as "a parallel stage completes when its slowest worker finishes", which is exactly how a HARQ round-trip or a synchronisation barrier behaves.

## 3. The isomorphism with a RAN scheduler

This is the highest-value cross-domain argument available to a communications engineer. It is defensible because the structural elements genuinely correspond:

| RAN L2 scheduler | Agent task router (GRAFT) |
| --- | --- |
| UE capability report | Device registration + capability model |
| CQI / BSR measurement | Per-request telemetry, budget reports |
| Grant / PRB allocation | Task partition + dispatch |
| HARQ RTT deadline / sync point | Explicit synchronisation barrier |
| PF / EXP policy | Capability-aware policy routing |
| 5QI / QoS budget | Explicit input budget per worker |

**Where the analogy holds:** both allocate a scarce shared resource under a deadline, both rely on periodic measurement of consumer state, both need a fallback when the measured state is stale, and in both the completion time of a parallel stage is set by the slowest participant.

**Where it breaks — and saying this is what makes the answer senior:**
- **Timescale differs by orders of magnitude.** A MAC scheduler decides in 0.125–1 ms; an agent router decides in seconds to minutes. Techniques that require tight feedback (per-slot closed-loop control) have no analogue in agent orchestration.
- **Unit of work differs.** PRBs are fungible and pre-emptible; a model inference is a long, non-pre-emptible transaction with a large startup cost. Migration and pre-emption are cheap in RAN, expensive in agent land.
- **Channel variability versus device heterogeneity.** Radio conditions fluctuate rapidly and stochastically; device capability is largely static and known a priori. That is why agent routing can be mostly *planning*, while RAN scheduling must be mostly *reaction*.
- **Failure semantics.** A dropped HARQ is expected and recovered transparently; a failed agent task produces a partial semantic result that may need application-level compensation.

**The questions a communications engineer uniquely asks of an agent system:**
- What is the **latency determinism** of the orchestration path? Can a stage's worst case be bounded, or only its mean?
- What is the **signalling overhead** of the control plane relative to the work being done? (In small meshes, orchestration can dominate.)
- What is the **failure and rollback** story when a worker dies mid-stage?
- Is the **barrier** a hard sync, or can late workers be dropped with graceful degradation?

## 4. Agentic AI as a compute-architecture driver

From the Huawei Connect 2026 framing (see [[08-2 Cloud-Edge-End Collaboration and Heterogeneous Computing]]):
- Agents interact with models hundreds of times per hour, requiring **flexible CPU:NPU ratio configuration**.
- The resulting **KV Cache far exceeds memory capacity**, forcing cross-system and cross-tier storage — hence the push to PB-scale KV cache clusters with one-hop direct connection.
- This is why "network-defined compute" and memory pooling moved from research topics to shipping architecture.

## 5. On-device and edge agent deployment constraints

- **Memory**: weights + KV + OS + runtime must coexist in a unified-memory budget. See [[10-1 LLM Inference Engines and xLLM]] for block-size and prefix-caching trade-offs.
- **Thermal and power**: sustained decode on an NPU throttles; orchestration must account for a device whose capability changes over minutes.
- **Privacy boundary**: which sub-tasks may leave the device. This is a routing policy input, not an afterthought.
- **Offline operation**: no cloud fallback means the failure path must be local degradation, not an error.
- **Intermittency**: devices join and leave; the orchestrator needs lease/heartbeat semantics.

## 6. Semantic communication — the communications-side contribution

For constrained links (single antenna, half-duplex, uplink-limited — see [[01-4 Cellular IoT RedCap eRedCap and NTN]]), the interesting design question is:

> Instead of transmitting raw audio/features, transmit **compressed semantic features** and let the edge reconstruct intent.

Design considerations:
- **Where to cut**: the cut point determines payload size versus robustness. Earlier cuts preserve more information; later cuts are smaller but task-specific and brittle.
- **Joint source-channel coding**: at low SNR, separating compression and channel coding is suboptimal, but joint designs are hard to standardise and to interoperate.
- **Task-oriented metrics**: optimise for intent-recognition accuracy at a given bit budget, not for PSNR or bit error rate.
- **Fallback**: when the semantic channel degrades, the system must be able to fall back to raw transmission or to local-only handling.

## Anchors — verified facts

- **GRAFT (gRPC-Routed Agent Framework for Tasking)** — CAIS '26, ACM DL **10.1145/3786335.3813216**, pp. 1204–1212, published **26 May 2026**; authors Shringi, Hillel-Tuch, Rizwan.
- Four-device mesh: **Apple laptop, Snapdragon X Elite laptop, Samsung mobile, Arduino Q embedded**.
- Core results: **bottleneck is lightweight local orchestration, not raw compute**; **E2E time set by the slowest parallel worker, not document size**; only the mesh achieves higher aggregate coverage while keeping every worker inside its native budget.
- Safety mechanisms: **command allowlists, bounded file access, one-time transfer tickets, per-request telemetry**.
- A different paper also uses the acronym **GRAFT** for an RL method (Gated Replacement of Answer-Failed groups with peer Trajectories) — disambiguate explicitly.
- Agentic AI drivers stated at Huawei Connect 2026: hundreds of model interactions per hour, flexible CPU:NPU ratio, KV Cache exceeding memory capacity.

## Related

- [[08-2 Cloud-Edge-End Collaboration and Heterogeneous Computing]]
- [[10-1 LLM Inference Engines and xLLM]]
- [[01-2 5G NR RAN Layer 2 Protocol Stack]]
- [[01-4 Cellular IoT RedCap eRedCap and NTN]]
