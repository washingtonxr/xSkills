---
title: 2026 Knowledge Framework and Interview Outline for the Communications x Compute x AI Intersection
lang: en
category: interview-prep
version: 1.0
sibling: skills-draft.cn.md
last-updated: 2026-10-22
license: GPL-3.0-or-later OR AGPL-3.0-or-later
---

# 2026 Knowledge Framework and Interview Outline
## Communications x Compute x AI

> This document is organised in three layers: **knowledge framework -> interview outline -> document production**. All specification numbers, timeline milestones and platform names are verifiable fact anchors; verify them before the interview.

---

## Part I. Knowledge Framework

### 1. 5G-Advanced / 6G Radio Access and Protocol Stack

#### 1.1 5G-Advanced (Rel-19/20): "AI-native air interface" and RedCap evolution

- **Positioning of Rel-19**: frozen at the end of **2025**, it establishes the **commercial monetisation baseline for 5G-Advanced**. Focus areas include the **AI-native air interface, RedCap satellite direct connectivity, and elastic network topology**. AI is no longer a bolt-on network-management add-on; it enters link adaptation, beam management, and positioning.

- **RedCap -> eRedCap: "extreme lightweighting + NTN convergence"**: eRedCap is seen as the natural successor of **LTE Cat 1/1bis** within the 5G ecosystem, and by **2026** chipset platforms supporting **NTN (GEO/LEO)** eRedCap have appeared.
  - In an interview you must be able to explain what the reduction in **bandwidth, antenna count and UE complexity** does to L2 scheduling constraints — for example **HARQ process count, number of blind decodes, and the trade-off between uplink coverage and grant granularity**.

- **Coupling of network energy saving and AI**: 5G-A energy saving is evolving from "symbol/channel/cell shutdown" toward AI-generated **"one policy per site"**. The core is using traffic prediction and multi-objective optimisation to switch energy-efficiency modes between low-load and high-load periods.

#### 1.2 6G: what "Rel-21 as the first 6G release" actually means

- **Timeline**: 3GPP started 6G standardisation in **2025**; **Rel-21 is the first 6G specification release**, targeting **standard completion in 2029 and commercial readiness by 2030**. **Rel-20** is the cross-generation bridge that closes out 5G-A and launches 6G study work; Rel-21 enters substantive standardisation.

- **6G scenarios and requirements are settled**: the TSG SA 6G use-case and service-requirement study (**TR 22.870**) and the RAN 6G scenario and requirement study (**TR 38.914**) have been completed or are at a high degree of completion, and 6G radio technology study has entered the **"key technology convergence phase"**. Convergence centres on **waveform, modulation, channel coding, bandwidth, and network architecture interfaces**, with industry leaning toward "inherit mature frameworks + keep necessary room for innovation".

- **6G features most likely to be commercialised first** (industry's first tier):
  1. **ISAC (Integrated Sensing and Communication)** — basic sensing/communication study completed in Rel-19/20; Rel-21 brings native 6G ISAC into the baseline;
  2. **Built-in AI-native capability** — treated as a core capability in the SA2 6G architecture study; Rel-21 fixes AI capability into the architecture (radio link AI optimisation, fault self-healing, AI resource scheduling, **AI-DPD**, and so on);
  3. **U6G mid-band ELAA**;
  4. **NTN enhancement**.

- **Interview relevance**: coming from an L2/system-architecture background, you must be able to discuss how "AI-native" affects protocol stack layering —
  - Do AI decisions live **inside the MAC scheduler** or in a **cross-layer controller**?
  - How does model lifecycle management align with the **O-RAN near-RT/non-RT RIC**?
  - Does training/inference compute sit in the **DU, the CU, or the edge cloud**?

#### 1.3 What changes and what does not in 5G RAN L2

- **The unchanging skeleton**:
  - MAC scheduling is still the core function that **decides PDSCH/PUSCH resource allocation every slot**;
  - The uplink grant lifecycle (**SR -> BSR -> PUSCH**, plus configured grant pre-allocation and activation) is still a high-frequency interview follow-up;
  - RLC/PDCP mechanisms — **ARQ, reordering, security, header compression** — remain the L2 fundamentals.

- **What is changing**:
  1. **Fast mobility driven by L1/L2 signalling** — Rel-18 already focused on cross-cell fast handover based purely on L1/L2 signalling, reducing the interruption caused by RRC-layer involvement; this directly touches the coupling between MAC/PHY measurement and handover decision.
  2. **AI/ML entering L2 scheduling** — RL methods such as DQN are used for massive MIMO beam selection and resource allocation, multi-agent DRL for power allocation, and L3 multi-layer management agents for load balancing and interference coordination.
     - You must be able to answer: **"what are the respective applicability boundaries of an RL scheduler versus a conventional PF/EXP rule-based scheduler"**, and **"how do the training environment (sim-to-real gap) and online inference latency constrain the scheduling period"**.
  3. **L2 complexity under carrier aggregation and multi-connectivity** — 5G-A CA enhancement, uplink enhancement, and multi-carrier scheduling impose finer constraints on **HARQ entity management, buffer status reporting, and cross-carrier scheduling timing**.

---

### 2. WLAN / WFA and Short-Range Wireless

#### 2.1 Engineering maturity of Wi-Fi 7 (802.11be) and the repositioning of Wi-Fi 8 (802.11bn)

- **Wi-Fi 7 is still the commercial mainstay in 2026**: the core is **320 MHz, 4096-QAM and MLO**, pursuing EHT and low latency. On the embedded/gateway side, **MLO link selection, TID-to-link mapping, multi-link security and power-saving modes** are the real deployment difficulties.

- **Official standard status of Wi-Fi 8**:
  - IEEE **802.11bn (Wi-Fi 8) Draft 1.0** was released in **August 2025**;
  - The target is not peak rate but **Ultra-High Reliability (UHR)** — tail latency, seamless roaming, multi-AP coordination, deterministic experience under high density;
  - **Wi-Fi Alliance certification is expected around 2028**, but chip vendors had already announced "Wi-Fi 8-ready" products at **CES 2026**, with mass production pointed at **summer 2026**;
  - In interviews you must separate **"standard completeness" from "marketing cadence"**, and explain why building pre-standard products before the standard is frozen carries **interoperability and feature-truncation risk**.

- **Key technology directions for Wi-Fi 8**: **multi-AP coordination (Co-SR/Co-BF)**, dynamic resource scheduling, and **enhanced long range (ELR/DRU)**, targeting roughly **1/6 of Wi-Fi 7's P99 latency** and roughly **2x wider IoT coverage**. From an L2/MAC viewpoint this involves **scheduling coordination signalling between APs, inter-BSS interference management, and cross-AP extension of TWT**.

- **Early discussion of Wi-Fi 9**: the WNG discussed the scope of **802.11bnext** in **2026**, driven by **AI-native applications, immersive entertainment, industrial automation and robotics**; technical themes include **AI-native PHY, deterministic MAC, enhanced uplink, Age-of-Information scheduling, and automotive-specific requirements**. This shows the next-generation WLAN battleground shifting from "throughput" to **"determinism + adaptation to AI traffic characteristics"**.

#### 2.2 Where WFA certification and the prpl framework intersect in engineering

- **Positioning of prpl**:
  - **prplWrt** is an enterprise/carrier-grade open-source framework built on OpenWrt;
  - **prplMesh** is an open-source implementation targeting **EasyMesh**, supporting OpenWrt, RDK-B and multiple SoC platforms, with hardware abstraction through a **HAL**;
  - prplMesh drives **hostapd / wpa_supplicant** directly and is deployed on vanilla OpenWrt through the **NL80211 backend**.

- **Interview follow-ups**:
  1. In carrier gateway scenarios, how does the prplMesh **controller/agent architecture** align with EasyMesh multi-AP coordination?
  2. What is the practical value of **prpl LCM containerised microservices** for Wi-Fi gateway software upgrades and functional decoupling?
  3. If Wi-Fi 8 multi-AP coordination features land, what extensions does the prpl framework need in its **management and control planes**?

---

### 3. IoT / WSN / Embedded

#### 3.1 The twin track of "eRedCap + NTN" in cellular IoT

- The convergence of eRedCap and NTN is **one of the clearest productisation signals on the IoT chipset side in 2026**.
  - Platforms such as **ALT1350 / ALT1550** simultaneously support **NB-IoT, NTN (Iridium's 3GPP-standard NTN service) and eRedCap**, targeting D2D and low-power wide-area scenarios;
  - **Nordic's nRF91 series** is on the same roadmap, layering **LTE-M/NB-IoT, NTN and 5G eRedCap**.

- **Interview requirements**:
  1. How does NTN **timing/coverage extension (HARQ, timing advance, feeder link delay)** change eRedCap **MAC/RLC parameter configuration**?
  2. What does the **long RTT** of a satellite link mean for the **TCP/application-layer retransmission strategy** of IoT small-packet traffic?

#### 3.2 The low-power paradigm shift in WSN

- Classic clustering routing (**LEACH / DEEC**) remains the baseline for understanding WSN energy balance, but by 2026 the engineering focus has shifted to **UAV-enabled WSN**:
  - Using drones for **on-demand proximity collection** to avoid the exponential energy decay of multi-hop relaying (**each forwarding hop accounts for roughly 30%-50% of total energy consumption**);
  - Combined with **cooperative sensor sleeping**, standby current can be cut by **more than 90%**.

- **Connection to the background**: low-power scheduling under an embedded RTOS, and the coordination between **Wake-up Radio** and **MAC-layer duty cycling**, are still the hard questions that test whether someone has genuinely built resource-constrained systems.

#### 3.3 RTOS / embedded communication device interview hardcore

- **High-frequency topics**: **I2C bus arbitration and pull-up resistors, SPI/UART/DMA, CAN bus**, plus **FreeRTOS task scheduling, priority inversion, the PendSV trigger mechanism, task state transitions, and the differences between queues, semaphores and mutexes**.

- **Bonus points**: being able to bind these low-level mechanisms to communications equipment scenarios —
  - **Buffer management of DPAA/DPDK on embedded multicore** versus the trade-offs of RTOS message queues under a **"zero-copy"** goal;
  - The correspondence between **interrupt top half / bottom half** and the **real-time requirements** of a wireless protocol stack.

---

### 4. Cloud / Edge / Cloud-Edge-End Collaboration and Heterogeneous Computing

#### 4.1 The latest engineering abstraction of cloud-edge-end collaboration

- The 2026 trend is moving from **"static layering"** to **task-level dynamic orchestration**.

- **GRAFT** is a representative system:
  - It uses a **sessioned gRPC control plane** to do **capability-aware policy routing** across heterogeneous personal devices (**Apple laptop, Snapdragon X Elite, Samsung phone, Arduino Q**);
  - It distributes inference tasks by **CPU/GPU/NPU**, completes **cross-device SLM collaboration with no cloud involved**, and keeps every worker within an **explicit input budget**;
  - Key observation: **the bottleneck of a small mesh is not single-device compute but lightweight local orchestration**; end-to-end time is determined by the **slowest parallel worker**, not by total document size.

- **Model partitioning and dependability**: research on **DNN partitioning** for dependable inference on end devices continues, with the goal of real-time AI through partitioning without cloud dependence — but the **engineering complexity of partition-point selection and fallback strategy is high**.

- **Where the L2/protocol-stack view enters**: the "control-plane signalling" in cloud-edge-end collaboration is structurally isomorphic to RAN scheduling signalling —
  - **Task routing ~ scheduling decision**
  - **Budget ~ resource quota**
  - **Synchronisation barrier ~ timing constraint of HARQ/ARQ**

  Being able to make that analogy in an interview clearly differentiates you from a pure AI-infrastructure candidate.

#### 4.2 Heterogeneous computing and "network-defined compute"

- **Huawei's UnifiedBus (Lingqu) public information for 2026** is a good case of system-level heterogeneous coordination:
  - It unifies **more than ten interconnect protocols**, raises interconnect bandwidth from the **hundred-GB class to the TB class**, and compresses **RTT from 7 us to 2 us**;
  - It supports **globally unified memory addressing within a super-node**; CPU, NPU, memory and SSD interconnect directly through UnifiedBus, with CPU/NPU resources flexibly ratioed;
  - It performs **hierarchical tiered Transformer hardware acceleration** (decoupling Attention and FFN, with **AF disaggregated deployment**);
  - **Hundred-billion-scale / thousand-dimension vector retrieval performance doubles**, and the **per-card HBM capacity requirement for 10T-scale model training drops**.

- **The ODCC view**: the pain points of 10k-card intelligent computing clusters are summarised as **"aggregating heterogeneous compute, breaking the bandwidth bottleneck, latency jitter, and operational complexity"**, with **new end-network-coordinated RDMA protocols** and **memory pooling** seen as the next-stage direction.

- **The causal chain to establish in interviews**: the performance bottleneck of heterogeneous compute convergence is not FLOPS alone, but the product of **interconnect bandwidth x memory semantics x scheduling granularity**. Being able to explain quantitatively —
  - **"why memory pooling raises MFU"**
  - **"why operator fusion pays off in the memory-bound regime but shows diminishing returns in the compute-bound regime"**

  is a key differentiator for senior roles.

#### 4.3 DPDK / user plane / edge forwarding

- **The core value of DPDK in 5G UPF and edge forwarding** remains: **bypassing the kernel protocol stack**, **pre-allocating mbufs with rte_mempool**, reducing memory copies, and doing **CPU core-pinning affinity scheduling**. Open-source UPFs (for example **free5GC**) implement **PDR/FAR/QER** flow-table matching and QoS enforcement on top of DPDK.

- **New problems in edge scenarios**: **64-byte small-packet forwarding, latency jitter, and AQM policy under mixed traffic** test a design more than pure throughput; comparison data for approaches such as **DPDK + HDB Interface** on the edge forwarding plane also shows that **the benefit and the cost in small-packet scenarios must be evaluated separately**.

- **Connection to L2 experience**: UPF **QoS flow mapping** and RAN-side **DRB/QoS flow mapping** are aligned end to end within the 3GPP framework; in interviews you can discuss **"when the RAN scheduler and UPF QoS enforcement operate on mismatched timescales, how do you determine whether the bottleneck is the air interface or the user plane"**.

---

### 5. xLLM / Agent / On-Device Inference

#### 5.1 Technical positioning of xLLM and interview follow-up depth

**xLLM** is a high-performance **pure C++ LLM inference framework** open-sourced by JD.com, targeting the removal of **Python runtime overhead and GC stalls** in on-device and real-time scenarios, optimising operators directly against the underlying hardware.

| Technical feature | Description |
| --- | --- |
| **KV Cache management** | Reduces redundant computation and speeds up long-text generation |
| **Quantisation support** | FP16 / INT8 and others, compressing memory footprint with controllable accuracy loss |
| **Operator fusion** | Merges multiple element-wise/matrix operations into a single kernel to reduce read/write traffic in the memory-bound phase |
| **Manual memory control** | Avoids the tail-latency jitter caused by Python GC |

- **2026 roadmap**: full-modality support, adaptation to domestic chips, an enterprise edition, and support for models such as **DeepSeek-V3/R1** and **Qwen3/Qwen3-MoE**.

- **Interview follow-up directions**:
  1. **"Why does KV Cache cache only K and V, not Q?"** — tests understanding of the decoder self-attention computation graph.
  2. **"The trade-off of PagedAttention / prefix caching versus contiguous KV Cache in memory-constrained on-device scenarios"** — on-device has no datacentre-class large memory, so the fragmentation versus pre-allocation trade-off is different.
  3. **"The difference in operator-fusion benefit between prefill and decode"** — decode is memory-bound, so fusion pays off more; prefill is more compute-bound.

#### 5.2 Agent orchestration form at the edge / on device

- **GRAFT** represents the direction of a **"multi-device SLM Agent mesh"**: instead of running one large model on a single device, structured tasks are routed to small models across multiple heterogeneous devices, with a **coordinator doing partitioning and merging**; **safety-bounded remote execution** and **per-request telemetry** are the core engineering components.

- **The connection to communications**: Agent task routing can be mapped onto RAN scheduling and slicing frameworks —
  - **Device capability ~ UE capability**
  - **Policy routing ~ RRM policy**
  - **Budget ~ resource quota**

  If you can point out, from a communications-system-engineer perspective, the **latency determinism, signalling overhead, and failure-fallback** problems of Agent orchestration, you will stand out more than a candidate with a pure AI-application background.

---

### 6. RISC-V and Communications Infrastructure

- RISC-V is penetrating from **"MCU/embedded"** into **"communication baseband + edge AI"**. Representative work in 2026 includes:
  - A **64-core RISC-V shared-memory cluster** (**12 nm FinFET, 410 GFLOP/s, 204.8 GBps**) aimed at **B5G/6G AI-enhanced O-RAN**, supporting systolic execution;
  - **EdgeQ's** unified 4G/5G platform, which integrates **baseband, AI acceleration, CPU and networking functions** in a single chip based on the RISC-V architecture, supporting **software-defined PHY and O-RAN**.

- **A deeper signal**: baseband chip companies such as **Picocom** have launched RISC-V based **5G-NR/NTN dual-mode satellite backhaul solutions**; the research goal of RISC-V baseband SoCs is to compress the gap between **GPP programmability and ASIC energy efficiency** (some work reports compressing it from roughly **10^3x** to the order of **10x**).

- **Architectural judgement for interviews**: the core selling point of RISC-V in baseband is **programmability plus an open ecosystem**, but the high energy-efficiency demand of L1 still requires **domain-specific accelerators (FEC, DFE, systolic arrays)**. Coming from an L2/system-architecture background, you need to be able to discuss —
  - **"When the L2 protocol stack runs on general-purpose RISC-V cores, how are the interface semantics, cache coherency, and scheduling real-time behaviour with the L1 accelerator guaranteed"**

  This is a cross-domain question that both 6G O-RAN and cloudified RAN interviews are likely to ask.

---

## Part II. Interview Question Outline

> Organised in four layers: **"resume deep-dive — technical depth — frontier judgement — system design"**. Each question is annotated with its assessment intent and an acceptable answer anchor.

### A. Resume deep-dive and basic verification (approx. 15-20 minutes)

| No. | Question | Assessment intent | Answer anchor |
| --- | --- | --- | --- |
| **A1** | For the scheduler you owned in 5G RAN L2, what specific traffic-mix scenario did it handle? How were PF weights, HARQ timing, and the BSR reporting period configured? | Verify the real granularity of L2 experience | Concrete parameter ranges, slot-level timing constraints, and one scheduling anomaly encountered plus the localisation process |
| **A2** | In a carrier aggregation scenario, how did your scheduler handle cross-carrier scheduling timing and HARQ entity management? | CA is a high-frequency L2 interview area | The CIF field in cross-carrier PDCCH, the constraint between HARQ process count and RTT, and the carrier selection logic for uplink grants |
| **A3** | What exactly did you do with DPDK on the user plane / forwarding plane? How did you decide the rte_mempool size and NUMA binding strategy? | Verify whether DPDK experience is real | mbuf size, mempool cache size, cooperation between core pinning and RSS/RPS, and the pps baseline in small-packet scenarios |
| **A4** | Which layer did you modify in prplMesh or prplWrt? Can you describe the mapping between hostapd's NL80211 interface and EasyMesh control messages? | Verify WLAN gateway/embedded experience | Division of labour between prplMesh controller and agent, the NL80211 command path, and the relationship to 802.11k/v/r |
| **A5** | What actual training/tuning experience corresponds to your "AI Trainer" certificate? Which RL or DRL methods have you used for resource allocation? | Separate "certificate" from "hands-on" | Environment modelling, reward design, the sim-to-real gap, and the impact of inference latency on the scheduling period |

### B. Technical depth (approx. 20-25 minutes)

#### B1. 5G-A / 6G and the AI air interface

1. What is the essential difference between Rel-19's **"AI-native air interface"** and Rel-18's **AI/ML for NR**? If you had to introduce an online-learning weight adjuster into the MAC scheduler, how would you design the placement of training/inference compute and the update frequency?
2. Rel-21 makes **AI-native** a core architectural capability of 6G. What structural difference do you see between "AI-native" and the **"bolt-on" intelligence of today's O-RAN RIC**? What new measurement/control interfaces does the L2 protocol stack need to expose?
3. **ISAC** is widely considered one of the first commercially viable 6G features. From an L2 scheduling perspective, at which layer should the resource competition introduced by integrated sensing and communication (**sensing waveform vs communication waveform**) be arbitrated? What new grant types or priority semantics does MAC need?

#### B2. WLAN

1. Wi-Fi 8's core KPI shifts from throughput to **UHR (tail latency, multi-AP coordination)**. If your gateway must support multi-AP coordinated scheduling, at which layer of **prplMesh** should the control signalling live? How does it coexist with Wi-Fi 7 MLO **TID-to-link mapping**?
2. Wi-Fi 9 (**802.11bnext**) discussions already treat **AI-native PHY** and **deterministic MAC** as themes. Which part of "AI-native PHY" do you think lands in engineering first — channel estimation, beam management, or CSI compression feedback? Why?

#### B3. IoT / embedded / RISC-V

1. After eRedCap and NTN converge, what is the impact of the satellite link's **long RTT** on **HARQ process count and the RLC ARQ retransmission timer**? If you had to make the minimal change to an existing L2 stack to support eRedCap NTN, which parameters/state machines would you change?
2. The selling point of a RISC-V baseband SoC is programmability. From an L2 engineer's perspective, would you rather run the scheduler on **general-purpose RISC-V cores** or on a **dedicated accelerator**? What guarantees are needed on the interface and on real-time behaviour respectively?
3. What problem does the existence of **PendSV** in FreeRTOS solve? If you made MAC scheduling decisions directly in the "interrupt context" of a wireless protocol stack, what risks would that introduce?

#### B4. Cloud-edge-end / xLLM / Agent / heterogeneous compute

1. xLLM uses **pure C++** to remove Python runtime overhead — what is the cost? In a scenario where on-device models iterate frequently, how do you weigh the model onboarding cost of a C++ framework against the flexibility of the Python ecosystem?
2. What is the core difference between **PagedAttention** for KV Cache on end devices versus in datacentre scenarios? If the device has only **8 GB of memory and model weights occupy 4 GB**, how would you set the KV block size and the prefix caching strategy?
3. GRAFT's observation is that **"the bottleneck of a small mesh is not single-device compute but local orchestration"**. If you treat GRAFT's task routing as a kind of "scheduler", what are its structural similarities to and essential differences from a 5G MAC scheduler?
4. The UnifiedBus architecture compresses **RTT from 7 us to 2 us** and provides **globally unified memory addressing**. From a protocol-stack engineer's perspective, which abstractions in an upper-layer distributed inference framework can disappear under such memory semantics, and which abstractions become more important instead?

### C. Frontier judgement and system design (approx. 20-25 minutes)

#### C1. Scenario design questions (choose one, depending on the target role)

**Design 1: Design an end-to-end system of "eRedCap NTN terminal + edge AI Agent"**

- The terminal has a **single antenna, is half-duplex, and is uplink-limited**;
- The Agent must complete **speech intent recognition** locally and, when necessary, upload **compressed semantic features** to the edge;
- Provide the **L2 scheduling strategy, the on-device inference resource budget, and the semantic transmission format** between device and edge.
- *Assessment: the intersection of IoT protocol constraints + on-device inference + semantic communication thinking.*

**Design 2: In an enterprise gateway supporting Wi-Fi 8 multi-AP coordination**

- Three traffic classes coexist: **XR, industrial robots, and massive sensors**;
- How should the **prplMesh control plane and the Wi-Fi MAC scheduling plane** divide responsibility so as to simultaneously satisfy XR tail latency, robot deterministic periodicity, and sensor low power?
- *Assessment: WLAN architecture + scheduling + low-power design.*

**Design 3: Implement a 5G L2 user-plane forwarding slice (including PDCP/RLC/GTP-U) on general-purpose RISC-V cores plus domain accelerators**

- Draw the **data path** and explain the placement choices for **DPDK or equivalent userspace I/O, memory pools, lock-free inter-core queues, and the QoS enforcement point**.
- *Assessment: DPDK + L2 protocol stack + hardware/software co-design on a RISC-V platform.*

#### C2. Open judgement questions

1. For **2026-2028**, which bottleneck in the "communications + heterogeneous compute + AI" intersection do you think is **most underestimated**: interconnect bandwidth, memory semantics, scheduling real-time behaviour, or model/protocol verification methodology? Give your ranking and reasoning.
2. If your team must track **3GPP Rel-21, IEEE 802.11bn, and xLLM/Agent** simultaneously, how would you design a minimal viable **"technology radar + prototype validation"** mechanism to prevent pre-research from decoupling from productisation?

### D. Suggested questions to ask the interviewer

1. Ask how the team validates AI decisions in its current **5G-A/6G pre-research**: simulation, live-network data replay, or a hardware-in-the-loop testbed?
2. Ask what the actual authority boundary of the **"system architect" role** is in cross-protocol-stack decisions (**RAN + device side + edge**): does it define interfaces, or is it directly accountable for performance KPIs?

---

## Part III. Word Document Generation

> Because the environment cannot emit a binary .docx directly, generate it in Word following the structure below, which takes about 10 minutes.

### Document structure

**Title**: Interview Preparation for the Communications x Heterogeneous Compute x AI Intersection — Knowledge Framework and Question Outline (2026)

#### Section 1: Personal background and role-fit summary (half a page)

1. Use **5-6 lines** to summarise the core tags: 5G RAN L2 + WLAN/WFA + embedded/RTOS + AI/ML + cloud-edge-end + xLLM/Agent + heterogeneous compute.
2. List **3 "cross-domain narrative" selling points**:
   - You can start from the **timing constraints of a MAC scheduler** to understand the real-time boundary of cloud-edge-end task orchestration;
   - You have both **DPDK user-plane performance tuning** and **prpl/OpenWrt gateway software stack** experience, fitting a "communications infrastructure + edge intelligence" system architect role;
   - You have architecture-level judgement on the trade-offs between **RISC-V baseband programmability** and the **L2 protocol stack interface**.

#### Section 2: Knowledge framework

- Reuse **Part I** above directly, keeping the heading hierarchy and the 2026 fact anchors;
- Use **"Heading 1/2/3" styles** in Word, with **2-3 bullet points** under each entry;
- **Bold** the key standard numbers, timeline milestones, and chip/platform names so they can be scanned quickly before the interview.

#### Section 3: Interview question outline

- Reuse the tables and question lists from **Part II** above;
- Set tables to the **"light grid" style**; use numbered paragraphs for question lists;
- In the **"Answer anchor" column**, note only **1-2 keywords** as a reminder to yourself; do not write out full answers.

#### Section 4: 48-hour pre-interview quick-reference checklist (one page)

- **5 numbers to quote from memory**: Rel-21 is the first 6G release / standard complete 2029 / commercial 2030; Wi-Fi 8 Draft 1.0 in 2025-08; the chipset timeline for eRedCap and NTN convergence; UnifiedBus RTT of 2 us; xLLM pure C++ / KV Cache / operator fusion.
- **3 diagrams to draw from memory**: the 5G L2 uplink grant lifecycle; the isomorphic diagram of cloud-edge-end Agent task routing versus RAN scheduling; the interface block diagram between L2 general-purpose cores and the L1 accelerator in a RISC-V baseband.
- **2 questions to ask back**: how the team validates AI decisions; the KPI boundary of the architect role.

#### Section 5: Reference fact anchors (for verification)

6G Rel-21 timeline and the positioning of AI-native/ISAC; Wi-Fi 8 UHR and 802.11bn Draft 1.0; eRedCap + NTN chipset progress; xLLM technical features; RISC-V baseband and EdgeQ; UnifiedBus heterogeneous coordination; DPDK UPF; prplMesh architecture.

---

## Appendix: Narrowing suggestion

If the target role leans more toward **"RAN system architect"** or **"edge AI / cloud-edge-end architect"**, the design questions and follow-up chains can be narrowed further, removing off-target items and making the outline more focused.

---

_Copyright (c) 2026 Washington Ruan and contributors · licensed under **GPL-3.0-or-later** or **AGPL-3.0-or-later**, at your option · see `LICENSE` and `LICENSE-AGPL`._
