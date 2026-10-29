---
title: Reading list — DATAPLANE · Data plane and heterogeneous compute
lang: en
category: reading-list
license: GPL-3.0-or-later OR AGPL-3.0-or-later
last-updated: 2026-10-29
---

# Reading list — DATAPLANE · Data plane and heterogeneous compute

> Packet processing and the compute fabric: DPDK and the 5G UPF, cloud-edge-end collaboration, memory pooling and the interconnect that makes pooling possible.
>
> One section per note, numbered `GG-x`. Where a note needed no source beyond its own
> **References**, there is no section here — the note is self-sufficient.

## How to use this list

- **Marks.** Type and priority marks (`★★★`, `[Book]`, `[EN]`) are defined once, in the MOC under *Reading marks*. The rule that matters: `★★★` means read or skim before you quote the note in an interview.
- **Titles** are kept in their published form and never translated; descriptions are English.
- **Nothing is asserted.** Where a citation could not be confirmed against a publisher, DOI, arXiv record or the issuing body, it is marked `VERIFY`.

---

## 05-1 · DPDK User Plane and 5G UPF
### Books

- **[Book · EN · ★★★]** *Data Plane Development Kit (DPDK): A Software Optimization Guide to the User Space-Based Network Applications* — Heqing Zhu, Cunming Liang (Intel) · CRC Press · ISBN 9781000194425
  - The only dedicated DPDK book, structured in two halves: foundations (CPU scheduling, multicore, cache and memory, hugepages and NUMA, data synchronisation, lock-free mechanisms, packet-forwarding models) and I/O optimisation (PCIe transaction detail, NIC tuning, multi-queue, flow classification, core assignment, load balancing, L2/L3/L4 offloads, crypto). Directly supports the run-to-completion versus pipeline decision and the small-packet pps argument.
- **[Book · EN · ★★]** *Understanding Linux Network Internals* — Christian Benvenuti · O'Reilly, 2005
  - Old but still the clearest walkthrough of the kernel network stack: `sk_buff`, NAPI, bridging, and the routing/neighbour subsystems. Read it to understand precisely what kernel bypass is bypassing.

### Documentation

- **[Doc · ★★★]** **DPDK Programmer's Guide** (dpdk.org, versioned per release)
  - The normative architecture reference: EAL, mbuf and mempool design, ring library, PMD model, and the optimisation guidelines. Pair with the API reference; read the "Writing Efficient Code" chapter before writing your first pipeline.
- **[Doc · ★★]** **FD.io VPP (Vector Packet Processing) documentation**
  - The alternative/complementary userspace dataplane: vectorised node graph processing. Useful for the "DPDK library versus VPP framework" design comparison.
- **[Doc · ★★]** **ETSI GS NFV specifications** (NFV 002 architectural framework, NFV-INF, NFV-MAN)
  - The virtualisation framing that UPF deployment sits inside.

### Standards

- **[Spec · ★★★]** **3GPP TS 29.244** — Interface between the Control Plane and the User Plane nodes (PFCP)
  - The UPF control interface: session establishment/modification, PDR, FAR, QER, URR, BAR, and usage reporting. This is the spec that defines what a UPF actually is.
- **[Spec · ★★★]** **3GPP TS 29.281** — General Packet Radio System (GPRS) Tunnelling Protocol User Plane (GTPv1-U)
  - Encapsulation for N3/N9, including the PDU Session Container extension header that carries the QoS flow identifier.
- **[Spec · ★★]** **3GPP TS 23.501 / TS 23.502** — 5G System architecture and procedures (Stage-2)
  - Where the UPF's role, the N3/N6/N9 reference points and the QoS enforcement model are defined.

---

## 05-2 · Cloud-Edge-End Collaboration and Heterogeneous Computing
### Books

- **[Book · EN · ★★★]** *Computer Architecture: A Quantitative Approach*, 6th ed. — John L. Hennessy, David A. Patterson · Morgan Kaufmann, 2017
  - The reference for reasoning quantitatively about heterogeneous systems: Amdahl's law, roofline-style analysis, memory hierarchy and parallelism scaling. Everything you need to turn "MFU is low" into a specific bottleneck.
- **[Book · EN · ★★]** *Programming Massively Parallel Processors: A Hands-on Approach*, 4th ed. — David B. Kirk, Wen-mei W. Hwu · Morgan Kaufmann, 2022
  - The accelerator-side counterpart: thread organisation, memory coalescing, tiling, occupancy, and reduction/scan patterns. Read it to understand why compute-bound kernels still miss the roofline.
- **[Book · EN · ★★]** *Heterogeneous Computing with OpenCL 2.0* — A. Munshi, B. R. Gaster, T. G. Mattson, J. Fung, D. Ginsburg · Morgan Kaufmann, 2015
  - Shared-virtual-memory and device-side enqueue models, and the platform-portability problem. Useful historical and conceptual grounding for today's heterogeneous runtimes.
- **[Book · EN · ★]** *Computer Systems: A Programmer's Perspective*, 3rd ed. — Randal E. Bryant, David R. O'Halloran · Prentice Hall, 2015
  - Cache behaviour, memory hierarchy and the cost model that dataplane and inference-engine work both depend on.

### Papers

- **[Paper · EN · ★★★]** "The Emergence of Edge Computing" — M. Satyanarayanan · *IEEE Computer*, vol. 50, no. 1, pp. 30–39, 2017
  - The conceptual foundation of edge computing: why cloud-only fails for latency-bound and bandwidth-heavy workloads, and what "edge" has to provide. Short and highly quotable.
- **[Paper · EN · ★★★]** "Edge Computing: Vision and Challenges" — W. Shi, J. Cao, Q. Zhang, Y. Li, L. Xu · *IEEE Internet of Things Journal*, vol. 3, no. 5, pp. 637–646, 2016
  - Formalises the cloud–edge–end taxonomy and the offloading decision problem. A good framing reference for task-placement discussions.
- **[Paper · EN · ★★]** "A Survey on Mobile Edge Computing: The Communication Perspective" — Y. Mao, C. You, J. Zhang, K. Huang, K. B. Letaief · *IEEE Communications Surveys & Tutorials*, vol. 19, no. 4, pp. 2322–2358, 2017
  - Joint communication-and-computation resource allocation: the model where radio resource and compute resource are optimised together. Directly relevant to the end–edge–cloud convergence thesis.
- **[Paper · EN · ★★]** "RDMA over Commodity Ethernet at Scale" — C. Guo et al. · *ACM SIGCOMM 2016*
  - Production-scale RDMA deployment: congestion control, PFC problems and the operational lessons. Read before claiming RDMA is free.
- **[Paper · EN · ★]** "Design Guidelines for High Performance RDMA Systems" — A. Kalia, M. Kaminsky, D. G. Andersen · *USENIX ATC 2016*
  - Concrete engineering guidance on queue-pair configuration, batching and doorbell cost.

### Documentation and vendor literature

- **[Doc · ★★★]** **UnifiedBus (灵衢) documentation — unifiedbus.com**
  - Primary source for the Huawei interconnect discussed in note 05-2: **《灵衢基础规范 2.0》** (UB Base Specification — architecture, protocol and programming models), **《灵衢固件规范 2.0》** (firmware architecture and interfaces), **《灵衢使能操作系统参考设计 2.0》** (UB OS Component), and **《基于灵衢的超节点参考架构白皮书》** (SuperPoD reference architecture: bus-level interconnect, unified protocol, peer-to-peer coordination, full-resource pooling, large-scale networking, high availability). UB Base Specification 2.1 adds 224/256 Gbit/s rates, reliable rerouting and lower multi-path latency. The 2.0 specifications were opened at HUAWEI CONNECT 2025 on 18 September 2025.
- **[Doc · ★★]** **昇腾 950 NPU 架构白皮书** (Ascend 950 NPU Architecture White Paper)
  - Chip-level detail: on-chip memory bandwidth and capacity, 72× HiLink ports at up to 112 Gbps, the UB2.0 protocol with URMA asynchronous copy and UB Memory global load/store semantics, PCIe GEN5 x16 reuse, and 2×400 Gbps UBoE for carrying UB over Ethernet.
- **[Doc · ★★]** **Ascend CANN documentation** (Huawei heterogeneous compute architecture)
  - Runtime, graph and operator-level interfaces for the NPU software stack.
- **[Doc · ★]** **ODCC (Open Data Center Committee) technical reports**
  - Chinese-industry server and datacentre architecture specifications, useful for the standards-body perspective in note 05-2.

---

## Standards and repositories

- **UnifiedBus (灵衢)** — `www.unifiedbus.com`. UB base, firmware, OS and SuperPoD reference architecture documents.
- **DPDK** — `dpdk.org` (Programmer's Guide, API reference, sample applications).


---

_Copyright (c) 2026 Washington Ruan and contributors · licensed under **GPL-3.0-or-later** or **AGPL-3.0-or-later**, at your option · see `LICENSE` and `LICENSE-AGPL`._
