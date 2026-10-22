---
title: PersonalSkills - Communications x Heterogeneous Compute x AI Knowledge Base
lang: en
category: project-readme
version: 1.2
sibling: README.cn.md
last-updated: 2026-10-22
copyright: "Copyright (c) 2026 Washington Ruan. All rights reserved."
---

# PersonalSkills

**Communications x Heterogeneous Compute x AI — Interview Preparation, Knowledge Framework and Knowledge Graph**

> Language: English (current) · [简体中文](README.cn.md)

This repository holds interview-preparation material and per-domain knowledge notes for the intersection of **communications technology, heterogeneous compute, and AI**: **5 source documents plus 1 Obsidian knowledge graph (17 notes)**.

---

## 1. Project Purpose

Everything is organised around a single thesis:

> Cellular/WLAN protocol stacks, heterogeneous compute, and on-device AI are converging into one scheduling problem — deciding *what* runs *where*, *when*, under a fixed latency and power budget.

So this is not a list of facts. It treats the **RAN MAC scheduler, the cloud-edge-end task orchestrator, and the LLM inference engine** as three instances of the same problem shape, and states explicitly where the analogy holds and where it breaks.

Four cross-cutting threads run through the whole vault:

1. **Determinism** — tail latency / P99 is the shared KPI across Wi-Fi 8 UHR, URLLC, and agent orchestration.
2. **Memory semantics** — KV cache, memory pooling, and UnifiedBus global addressing are the same battle fought at three layers.
3. **Interface semantics** — L1 accelerator ↔ L2 general-purpose core, NPU ↔ CPU, coordinator ↔ worker: the boundary always costs more than the compute.
4. **Verification methodology** — simulation → data replay → hardware-in-the-loop is the only credible path for both AI schedulers and AI-native PHY.

---

## 2. Quick Start: Recommended Reading Path

| Stage | What to do | Output |
| --- | --- | --- |
| 1. Build the map | Read `knowledge-graph/00 MOC ...` end to end | A unified mental model and a domain map |
| 2. Read by target role | See the selection table below | 3-5 domain threads you can drill into |
| 3. Go to primary sources | Use the matching section of `readlist.md` to pull books, papers and standards | A first-hand citation behind every claim you make |
| 4. Mock interview | Self-test with groups A/B/C/D of `skills-draft.md` (or `skills-draft.cn.md`) | A parameter-level answer for every question |
| 5. 48-hour sprint | Read only the **Anchors** section of each note plus Part III, Section 4 of `skills-draft.md` | Numbers, timelines and architecture diagrams on demand |

**Selection by target role**

| Target role | Priority notes |
| --- | --- |
| RAN system architect | 01 → 02 → 03 → 08 → 12 |
| Edge AI / cloud-edge-end architect | 09 → 10 → 11 → 13 → 15 |
| Embedded / Linux platform | 07 → 15 → 12 → 08 → 13 |
| WLAN / gateway | 04 → 14 → 06 → 15 |
| Software / language foundation (any role) | 16 → 13 |

---

## 3. Directory Structure

```
261022,PersonalSkills/
├── README.md                       Project README (English, default, this file)
├── README.cn.md                    Project README (Chinese)
├── background.md                   Personal Background and Task Statement (English, default)
├── background.cn.md                个人背景与任务说明（中文）
├── skills-draft.md                 Knowledge Framework and Interview Outline (English, default)
├── skills-draft.cn.md              知识框架与面试题纲（中文）
├── readlist.md                     Reading list (Chinese/English books, papers, standards; descriptions in English)
├── knowledge-graph/                Obsidian knowledge graph (vault, 17 notes)
│   ├── 00 MOC - Comms x Compute x AI Knowledge Graph.md      <- entry index
│   ├── 01 5G-Advanced and 6G Radio Access.md
│   ├── 02 5G NR RAN Layer 2 Protocol Stack.md
│   ├── 03 AI-ML for RAN and O-RAN RIC.md
│   ├── 04 WLAN - Wi-Fi Generations Evolution.md
│   ├── 05 Cellular IoT RedCap eRedCap and NTN.md
│   ├── 06 Wireless Sensor Networks and Low-Power MAC.md
│   ├── 07 Embedded Systems RTOS and Hardware Interfaces.md
│   ├── 08 DPDK User Plane and 5G UPF.md
│   ├── 09 Cloud-Edge-End Collaboration and Heterogeneous Computing.md
│   ├── 10 LLM Inference Engines and xLLM.md
│   ├── 11 Agent Systems and Edge Orchestration.md
│   ├── 12 RISC-V for Communication Infrastructure.md
│   ├── 13 Programming Languages Toolchain and Performance Engineering.md
│   ├── 14 WLAN Ecosystem - WFA, EasyMesh and prpl.md
│   ├── 15 Linux Embedded Development - Drivers, Applications and Core Subsystems.md
│   └── 16 C and C++ Programming - Language Features, STL and Systems Practice.md
└── .workbuddy/                     Project working data (do not delete)
```

---

## 4. Document Inventory

### 4.1 Source documents

| File | Language | Role | Content |
| --- | --- | --- | --- |
| `README.md` | English | Project README | This file: purpose, reading path, directory structure, inventory, conventions, fact-checking strategy |
| `README.cn.md` | Chinese | Project README | Same, in Chinese |
| `background.md` | English | Input source | Original profile + structured breakdown (education / certifications / role trajectory / domains / tech stack) + task statement |
| `background.cn.md` | Chinese | Input source | Same, in Chinese |
| `skills-draft.md` | English | Main document | 2026 knowledge framework (6 domains) + interview outline (layers A/B/C/D) + Word production structure |
| `skills-draft.cn.md` | Chinese | Main document | Same, in Chinese |
| `readlist.md` | Descriptions in English, titles in their original language | References | Books, papers, standards and documentation across 19 themed sections: 01 5G-A and 6G, 02 NR L2, 03 AI-RAN and O-RAN, 04 WLAN generations, 05 RedCap/eRedCap/NTN, 06 WSN, 07 embedded RTOS, 08 DPDK/UPF, 09 cloud-edge-end, 10 LLM inference and xLLM, 11 agent systems, 12 RISC-V, 13 languages and performance, 14 WLAN ecosystem, 15 Linux embedded, 16 C and C++ — plus 17 primary standards repositories, 18 a reading order, and 19 verification and maintenance |

### 4.2 Knowledge graph notes

| No. | Domain | Core coverage |
| --- | --- | --- |
| **00 MOC** | Root index | Unified mental model, domain navigation, cross-cutting threads, vault conventions |
| 01 | 5G-A / 6G radio access | Rel-19/20/21 timeline, AI-native air interface, ISAC, U6G ELAA, NTN |
| 02 | 5G NR RAN L2 | MAC/RLC/PDCP/SDAP, HARQ, BSR, grant lifecycle, QoS mapping |
| 03 | AI/ML for RAN and O-RAN | near-RT/non-RT RIC, xApp/rApp, DRL scheduling, sim-to-real |
| 04 | WLAN generational evolution | Wi-Fi 4 to 9, MLO, OFDMA, UHR, multi-AP coordination, per-feature design detail |
| 05 | Cellular IoT | RedCap tiers, eRedCap, NTN, Ambient IoT, LP-WUS |
| 06 | WSN and low-power MAC | Clustering routing, UAV-assisted collection, TSCH, AoI |
| 07 | Embedded RTOS | FreeRTOS, PendSV, I2C/SPI/UART/CAN, DMA, cache coherency |
| 08 | DPDK and 5G UPF | mbuf/mempool, PFCP, PDR/FAR/QER, QoS enforcement, small-packet pps |
| 09 | Cloud-edge-end and heterogeneous compute | UnifiedBus, memory pooling, MFU, RDMA |
| 10 | LLM inference engines and xLLM | KV cache, PagedAttention, quantization, operator fusion, prefill/decode |
| 11 | Agent systems and edge orchestration | GRAFT, multi-device SLM mesh, safety-bounded execution |
| 12 | RISC-V for communications infrastructure | Baseband clusters, software-defined PHY, H extension, L1/L2 interface |
| 13 | Languages, toolchain and performance engineering | Build systems, Python, kernel-bypass selection, performance methodology |
| 14 | WLAN ecosystem | WFA certification, EasyMesh, prplMesh/prplOS/prpl LCM |
| 15 | Linux embedded development | Boot chain, device tree, drivers, IPC, network stack, virtualization, PREEMPT_RT |
| **16** | **C and C++ programming and STL** | C23/C++26 language features, templates and compile-time computation, memory model and concurrency, STL containers/iterators/algorithms, systems idioms and the UB catalogue |

---

## 5. Using the Knowledge Graph

1. **Opening it**: in Obsidian choose "Open folder as vault" and point it at `knowledge-graph/` — not at the project root.
2. **Entry point**: `00 MOC` is the only navigation page. The other 16 notes are connected bidirectionally through `[[wikilinks]]`; use Graph View to see connection density.
3. **Naming rule**: `00 MOC` is the index; `01`-`16` are domain notes, where the file name *is* the topic, so they sort by number and are searchable by name.
4. **Note structure**: body of knowledge points → **Anchors** → **Related**. This three-part shape is fixed.
5. **Search tips**: start with `tags` and `aliases` (defined in frontmatter), then full-text search on specification numbers (for example `38.914`, `802.11bn`).

---

## 6. Repository Conventions

1. **Language and file naming**: every note under `knowledge-graph/` is written in **English** so it can be reused directly with international teams and in English interviews. Source documents exist in both languages one-to-one, with **English as the default (no suffix)** and Chinese marked `.cn`: `README.md` / `README.cn.md`, `background.md` / `background.cn.md`, `skills-draft.md` / `skills-draft.cn.md`. `readlist.md` is the single exception — it has no separate Chinese edition because its titles are already kept in their original published form with English descriptions.
2. **Frontmatter**: every `.md` file carries YAML frontmatter with `title`, `lang`, `category`, `last-updated`, and `copyright`; bilingual pairs also carry `sibling` pointing at the other language, and documents that change carry `version`.
3. **Fact anchors**: every note ends with an **Anchors** section containing only checkable facts with a date or number (specification numbers, freeze dates, paper DOIs, release versions).
4. **Doubtful items**: anything not independently confirmed is marked **`VERIFY`** rather than asserted.
5. **Bidirectional links**: `[[wikilinks]]` are deliberate — a link means the two concepts are argued about together in interviews; link integrity is verifiable.
6. **Encoding and formatting**: all files are UTF-8; body text uses standard Markdown, tables for comparisons, and blockquotes for thesis/principle statements.
7. **Copyright header**: every file carries copyright information in both its frontmatter and its footer.
8. **Reference rule**: in `readlist.md`, titles are kept in their original published form (Chinese books keep the Chinese title and `《》` brackets) and are never translated; every entry's description is written in English.

---

## 7. Fact Checking and Update Strategy

**Division of labour between source documents and the knowledge graph**

- `skills-draft.md` / `skills-draft.cn.md` faithfully preserve the wording and judgement of the original draft, so the original line of thinking stays traceable;
- verified facts live in the **Anchors** section of each note under `knowledge-graph/`.

**Facts already corrected (cite the Anchors, not the draft)**

| Item | Original draft | Verified conclusion |
| --- | --- | --- |
| eRedCap release | attributed to Rel-19 | It is **Rel-18** (frozen 2024-06; 5 MHz, 1 Rx, HD-FDD, ~10 Mbps). Rel-19's contribution is the NTN extension, LP-WUS, and Ambient IoT |
| Wi-Fi 8 progress | Draft 1.0 (2025-08) | **Draft 1.0 was 2025-07**; Draft 2.0 passed WG ballot on 2026-09-02 at 76.5%; WFA certification around **2028-01** |
| Rel-21 milestones | "complete 2029, commercial 2030" | Four official milestones: Stage-1 **2027-03** / Stage-2 **2028-06** / Stage-3 **2028-12** / ASN.1+OpenAPI **2029-03** |
| PREEMPT_RT | not covered | Merged into mainline in **Linux 6.12 (2024-11)** for x86/arm64/RISC-V; 32-bit ARM added in 7.1 |
| C/C++ standard status | mentions only "C/C++" | **C23 = ISO/IEC 9899:2024** (published 2024-10-31, `__STDC_VERSION__` = 202311L); **C++26 shipped by WG21 on 2026-03-28** (working draft N5046), to be published as ISO/IEC 14882:2026 |

**Update triggers**

- 3GPP TSG plenary meetings (4 per year) → update 01/02/05
- IEEE 802.11 WG sessions and WFA certification announcements → update 04/14
- Linux mainline and LTS releases → update 13/15
- xLLM / agent framework releases and papers → update 10/11
- WG21 / WG14 meetings and GCC / Clang major releases → update 16

---

## 8. Maintainer

Washington Ruan — communications software / embedded software / wireless protocol stack engineer and system architect; focus on 5G RAN L2, WLAN/WFA, IoT/WSN, embedded systems and Linux, AI/ML, cloud-edge-end collaboration and heterogeneous compute.

---

## Copyright

Copyright (c) 2026 **Washington Ruan**. All rights reserved.

All documents and notes in this repository are the copyrighted work of Washington Ruan. Commercial publication or redistribution requires written permission.

---

© 2026 Washington Ruan. All rights reserved.
