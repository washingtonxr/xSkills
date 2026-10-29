---
title: Reading list — SILICON · Silicon and instruction-set architecture
lang: en
category: reading-list
license: GPL-3.0-or-later OR AGPL-3.0-or-later
last-updated: 2026-10-29
---

# Reading list — SILICON · Silicon and instruction-set architecture

> The instruction set as a system decision: RISC-V in communication infrastructure, baseband clusters, software-defined PHY and the L1/L2 boundary.
>
> One section per note, numbered `GG-x`. Where a note needed no source beyond its own
> **References**, there is no section here — the note is self-sufficient.

## How to use this list

- **Marks.** Type and priority marks (`★★★`, `[Book]`, `[EN]`) are defined once, in the MOC under *Reading marks*. The rule that matters: `★★★` means read or skim before you quote the note in an interview.
- **Titles** are kept in their published form and never translated; descriptions are English.
- **Nothing is asserted.** Where a citation could not be confirmed against a publisher, DOI, arXiv record or the issuing body, it is marked `VERIFY`.

---

## 07-1 · RISC-V for Communication Infrastructure
### Books and specifications

- **[Spec · ★★★]** **The RISC-V Instruction Set Manual** — RISC-V International; Volume I: Unprivileged ISA, Volume II: Privileged Architecture
  - The normative specification. Volume II is where you find the privilege levels, PMP/PMA, interrupt and exception model, and the hypervisor extension.
- **[Spec · ★★★]** **RISC-V Hypervisor Extension ("H") v1.0** — ratified December 2019; mandatory in the RVA23 profile
  - The virtualisation baseline. Combined with the memory-management and interrupt-architecture extensions, this is what makes RISC-V viable for mixed-criticality infrastructure.
- **[Book · EN · ★★]** *The RISC-V Reader: An Open Architecture Atlas* — David A. Patterson, Andrew Waterman · Strawberry Canyon, 2017
  - Short, accessible introduction to the ISA and its design decisions, written by the architects. Best first read on RISC-V.
- **[Book · EN/CN · ★★★]** *Computer Organization and Design RISC-V Edition: The Hardware/Software Interface* — David A. Patterson, John L. Hennessy
  - English 2nd edition (Morgan Kaufmann); Chinese 《计算机组成与设计:硬件/软件接口 RISC-V版(原书第2版)》, translated by 易江芳, 刘先华 · 机械工业出版社, 2023 · ISBN 9787111727972 (earlier 5th-edition-based translation: ISBN 9787111652144, 2020)
  - The 2nd edition switches from RV64 to RV32 to reduce learning difficulty and adds a discussion of domain-specific architectures (DSA) — directly relevant to why baseband accelerators look the way they do.
- **[Doc · ★★]** **RISC-V International profiles (RVA20 / RVA22 / RVA23)** and the **RISC-V Vector ("V")** and **Bit-Manipulation ("B")** extension specifications
  - Profiles determine what software can assume; the vector extension is what makes software-defined baseband feasible.

### Papers

- **[Paper · EN · ★★★]** "A 410 GFLOP/s, 64 RISC-V Cores, 204.8 GBps Shared-Memory Cluster in 12 nm FinFET with Systolic Execution Support for Efficient B5G/6G AI-Enhanced O-RAN" — Y. Zhang, M. Bertuletti, S. Mazzola, S. Riedel, L. Benini · *IEEE ESSERC 2025*, pp. 401–404 · DOI 10.1109/ESSERC66193.2025.11214075
  - "HeartStream": a 64-RV-core shared-L1-memory cluster for baseband, with complex (16-bit real/imaginary) MAC, division and square-root instructions, SIMD, and hardware-managed systolic queues — improving the energy efficiency of key baseband kernels by up to 1.89×. 243 GFLOP/s on complex-valued wireless workloads at 800 MHz, 72 GOP/s for on-received-data AI, 49.6 GFLOP/s/W software-defined PUSCH efficiency, and 0.68 W at 645 MHz within the 4 ms end-to-end uplink constraint. The strongest available evidence that RISC-V is a credible baseband platform, not just a microcontroller ISA.
- **[Paper · EN · ★]** "End-to-End Learning for OFDM: From Neural Receivers to Pilotless Communication" (see §01-1)
  - Cited by the HeartStream work; explains why an AI-capable baseband cluster is worth building.

---

## Standards and repositories

- **RISC-V International** — `riscv.org/technical/specifications`. ISA manuals, extension specs and profiles.


---

_Copyright (c) 2026 Washington Ruan and contributors · licensed under **GPL-3.0-or-later** or **AGPL-3.0-or-later**, at your option · see `LICENSE` and `LICENSE-AGPL`._
