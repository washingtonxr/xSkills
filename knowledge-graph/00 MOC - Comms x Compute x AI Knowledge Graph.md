---
title: MOC - Communications x Heterogeneous Compute x AI
type: moc
domain: root
tags:
  - moc
  - index
  - telecom
  - ai
  - computing
last-updated: 2026-10-22
owner-background: Xidian MS in Communication Engineering; National Intermediate Engineer; Senior AI Trainer; IEEE member; ex cellular software / embedded software / wireless protocol stack engineer and system architect
---

# Communications x Heterogeneous Compute x AI — Knowledge Graph

This vault is the English-language knowledge base behind one career thesis:

> Cellular/WLAN protocol stacks, heterogeneous compute, and on-device AI are converging into a single scheduling problem — deciding *what* runs *where*, *when*, under a hard latency and power budget.

## The unifying mental model

A RAN MAC scheduler, an edge task router, and an LLM inference scheduler are all solving the same shape of problem:

| RAN L2 scheduler | Edge/agent orchestrator | LLM inference engine |
| --- | --- | --- |
| UE capability | Device capability (CPU/GPU/NPU) | Hardware backend / block pool |
| CQI / BSR report | Telemetry / budget report | KV cache occupancy |
| Grant / PRB allocation | Task partition + dispatch | Batch + block allocation |
| HARQ RTT deadline | Sync barrier | Prefill / decode SLO |
| PF / EXP policy | Capability-aware policy routing | Continuous batching |

Carrying this analogy into interviews is the differentiator versus a pure AI-infra or pure modem background. See [[08-2 Cloud-Edge-End Collaboration and Heterogeneous Computing]].

## Numbering scheme

Notes are numbered `GG-x`: `GG` is a **domain group**, `x` indexes within it. Group numbers are inherited from each group's original top-level note, so they are intentionally not contiguous.

| Group | Domain | Notes |
| --- | --- | --- |
| `01-x` | Cellular and mobile communications | 01-1 … 01-4 |
| `04-x` | WLAN | 04-1 … 04-3 |
| `06-x` | Low-power and sensor networking | 06-1 |
| `07-x` | Embedded and systems software | 07-1 … 07-3 |
| `08-x` | Data plane and heterogeneous compute | 08-1, 08-2 |
| `10-x` | AI inference and agent systems | 10-1, 10-2 |
| `12-x` | Silicon and instruction-set architecture | 12-1 |
| `13-x` | Programming languages and engineering practice | 13-1, 13-2 |

## Domains

### 01 · Cellular and mobile communications
- [[01-1 5G-Advanced and 6G Radio Access]] — Rel-19/20/21 timeline, AI-native air interface, ISAC, U6G, NTN
- [[01-2 5G NR RAN Layer 2 Protocol Stack]] — MAC / RLC / PDCP / SDAP, HARQ, BSR, grant lifecycle, QoS mapping
- [[01-3 AI-ML for RAN and O-RAN RIC]] — near-RT/non-RT RIC, xApps/rApps, DRL scheduling, sim-to-real
- [[01-4 Cellular IoT RedCap eRedCap and NTN]] — RedCap tiers, eRedCap, NTN, Ambient IoT, LP-WUS

### 04 · WLAN
- [[04-1 WLAN - Wi-Fi Generations Evolution]] — 802.11n/ac/ax/be/bn, Wi-Fi 4→9, MLO, OFDMA, UHR, multi-AP coordination
- [[04-2 WLAN - Power Saving Mechanisms and Evolution]] — legacy PS / PS-Poll, U-APSD, SMPS, TXOP PS, TWT and r-TWT, wake-up radio, AP power save, ambient power
- [[04-3 WLAN Ecosystem - WFA, EasyMesh and prpl]] — certification, Multi-AP control plane, prplMesh/prplOS

### 06 · Low-power and sensor networking
- [[06-1 Wireless Sensor Networks and Low-Power MAC]] — clustering, UAV-assisted collection, TSCH, AoI

### 07 · Embedded and systems software
- [[07-1 Embedded Systems RTOS and Hardware Interfaces]] — FreeRTOS, PendSV, I2C/SPI/UART/CAN, DMA, cache coherency
- [[07-2 Linux Embedded Development - Drivers, Applications and Core Subsystems]] — boot chain, device tree, kernel drivers, IPC, network stack, KVM/containers, PREEMPT_RT
- [[07-3 Embedded Software Architecture - Patterns, Layering and Wireless System Structure]] — layering and HAL/BSP, execution models, HSM, design patterns, AUTOSAR, safety, OTA, wireless stack decomposition

### 08 · Data plane and heterogeneous compute
- [[08-1 DPDK User Plane and 5G UPF]] — mbuf/mempool, PFCP, PDR/FAR/QER, QoS enforcement, small-packet pps
- [[08-2 Cloud-Edge-End Collaboration and Heterogeneous Computing]] — UnifiedBus, memory pooling, MFU, RDMA

### 10 · AI inference and agent systems
- [[10-1 LLM Inference Engines and xLLM]] — KV cache, PagedAttention, quantization, operator fusion, prefill/decode
- [[10-2 Agent Systems and Edge Orchestration]] — GRAFT, multi-device SLM mesh, safety-bounded execution

### 12 · Silicon and instruction-set architecture
- [[12-1 RISC-V for Communication Infrastructure]] — baseband clusters, EdgeQ, software-defined PHY, L1/L2 interface

### 13 · Programming languages and engineering practice
- [[13-1 Programming Languages Toolchain and Performance Engineering]] — build systems, Python, Linux, Verilog HDL, profiling
- [[13-2 C and C++ Programming - Language Features, STL and Systems Practice]] — C23/C++26 language features, templates, memory model, STL containers and algorithms, systems idioms

## Cross-cutting threads

1. **Determinism.** Tail latency / P99 is the shared KPI across Wi-Fi 8 UHR, URLLC, and agent orchestration barriers.
2. **Memory semantics.** KV cache, memory pooling, and UnifiedBus global addressing are the same battle fought at three layers.
3. **Interface semantics.** L1 accelerator ↔ L2 general-purpose core, NPU ↔ CPU, coordinator ↔ worker — the boundary always costs more than the compute.
4. **Verification methodology.** Simulation → data replay → hardware-in-the-loop is the only credible path for both AI schedulers and AI-native PHY.

## Companion documents (outside this vault)

This vault is opened at `knowledge-graph/`, so the source documents in the parent directory are **not** visible to Obsidian and cannot be wikilinked. They are plain-text references:

| Document | Purpose |
| --- | --- |
| `README.md` / `README.cn.md` | Project overview, reading path, directory structure, conventions, fact-checking strategy |
| `background.md` / `background.cn.md` | Profile, role trajectory, domains, tech stack, and the original task statement |
| `skills-draft.md` / `skills-draft.cn.md` | The 2026 knowledge framework plus interview question groups A/B/C/D |
| `readlist.md` | Books, papers, standards and reports, sectioned to mirror this vault's note numbering |

Naming convention: English is the default filename (no suffix); Chinese versions carry `.cn`.

## Conventions used in this vault

- Notes are numbered `GG-x` by domain group (see **Numbering scheme** above); `00 MOC` is the index.
- Every note carries a `last-updated` field and an **Anchors** section with dated, checkable facts (standard numbers, freeze dates, publication venues).
- Items that are plausible but not independently confirmed are marked `VERIFY` rather than stated as fact.
- Wikilinks are used deliberately: a link means the two concepts are argued about together in interviews.
- Diagrams are Mermaid, so they render in Obsidian's reading view without an external tool.
