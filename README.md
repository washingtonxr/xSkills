---
title: PersonalSkills — Communications x Heterogeneous Compute x AI
lang: zh-en
category: project-readme
version: 2.0.0
license: GPL-3.0-or-later OR AGPL-3.0-or-later
last-updated: 2026-10-29
---

# PersonalSkills

**一个开源的通信 × 异构计算 × AI 知识库**
**An open knowledge base for communications, heterogeneous compute and AI**

**License** GPL-3.0-or-later or AGPL-3.0-or-later · **10 directories** · **43 notes** · Obsidian-compatible

[中文](#中文) · [English](#english)

---

# 中文

## 这是什么

一个围绕单一论点组织起来的工程知识库：

> 蜂窝与 WLAN 协议栈、异构计算、端侧 AI 正在收敛成同一个调度问题——决定**什么在哪儿跑、什么时候跑**，在硬性的时延与功耗预算之内。RAN 的 MAC 调度器、端边云的任务编排器、LLM 推理引擎，是同一个闭环在三个不同时间尺度上的实例。

所以这里不是事实清单。每篇笔记都说明这个类比在哪里成立，更重要的是在哪里失效。

- **43 篇笔记，10 个目录。** 目录即主题，笔记编号即阅读顺序。
- **每篇形态固定：** 结论 → 分层论述（配 Mermaid 图）→ **Anchors**（有日期、可核查的事实）→ **Related**（会被一起追问的邻居）→ **References**（一手来源）。
- **笔记正文只用英文**，以便原样用于国际团队与英文面试；说明文档中英双语。
- **不确定的就说不知道：** 无法独立确认的说法标注 `VERIFY`；流行说法与一手来源的差异集中记录在勘误表里。

## 仓库结构

```
PersonalSkills/
├── README.md                    本文件，中英双语
├── LICENSE                      GNU General Public License v3.0
├── LICENSE-AGPL                 GNU Affero General Public License v3.0
├── other/
│   ├── background.md  .cn.md    个人背景、方向轨迹与原始任务说明
│   └── skills-draft.md  .cn.md  2026 知识框架与 A/B/C/D 面试题纲
└── knowledge-graph/             Obsidian vault —— 用 Obsidian 打开这个目录
    ├── 00 MOC - ...md           唯一入口：目录地图、学习方法、贡献方法
    ├── 99 Corrections - ...md   勘误表：流行说法 vs 一手来源
    ├── MN/           01-x  移动通信（8 篇）+ readlist.md
    ├── WLAN/         02-x  IEEE 802.11（15 篇）+ readlist.md
    ├── WSN/          03-x  低功耗与传感网（1 篇）+ readlist.md
    ├── EMBEDDED/     04-x  嵌入式与系统软件（6 篇）+ readlist.md
    ├── DATAPLANE/    05-x  数据面与异构计算（2 篇）+ readlist.md
    ├── AI/           06-x  机器学习与推理（3 篇）+ readlist.md
    ├── SILICON/      07-x  芯片与指令集（1 篇）+ readlist.md
    ├── LANGUAGES/    08-x  编程语言与工程实践（5 篇）+ readlist.md
    ├── MANAGEMENT/   09-x  工程项目管理（1 篇）+ readlist.md
    └── BUSINESS/     10-x  价值主导的商业模式（1 篇）+ readlist.md
```

每个目录自带一份 `readlist.md`：该目录的书籍、论文、标准与技术报告，按笔记编号分节，`★★★` 表示「引用前至少翻过」。

## 快速开始

1. `git clone` 之后，用 Obsidian「打开文件夹作为仓库」，**指向 `knowledge-graph/`**——不是仓库根目录。
2. 从 `00 MOC` 开始。它给出十个目录的扼要介绍、每个目录的阅读顺序、学习方法与贡献方法。
3. 进入与你目标岗位对应的目录，按该目录给出的顺序读笔记；需要一手来源时，翻该目录的 `readlist.md`。
4. 每篇笔记先读开头的结论与末尾的 **Anchors**，再回读正文。这是判断「这篇值不值得细读」最快的办法。

## 十个目录

| 目录 | 主题 | 篇数 | 面向 |
| --- | --- | --- | --- |
| `MN` | 3GPP 空口与 RAN 协议栈：release 地图、L2、AI/ML for RAN、蜂窝 IoT、随机接入、DU 调度器、HARQ，以及一个可读的开源实现 | 8 | RAN、协议栈、基带软件 |
| `WLAN` | IEEE 802.11：基础与历史、收发机与射频、代际、省电、生态、数据通路、接入、漫游、EasyMesh、调度、TSN、基带与驱动、OpenWrt、openwifi、可靠性与确定性 | 15 | WLAN 协议栈、AP/网关、客户端 |
| `WSN` | 低功耗无线：WPAN 介质访问、分簇、TSCH、信息年龄 | 1 | IoT、低功耗设备 |
| `EMBEDDED` | 嵌入式与系统软件：RTOS、嵌入式 Linux、软件架构、中断、并发与 IPC、设备驱动 | 6 | 嵌入式、Linux 平台 |
| `DATAPLANE` | 数据面与异构计算：DPDK 与 5G UPF、端边云协同、内存池化与互联 | 2 | 数据面、边缘计算 |
| `AI` | 机器学习与推理：基础与失败模式、LLM 服务引擎、智能体系统 | 3 | 端侧 AI、推理系统 |
| `SILICON` | 芯片与指令集：RISC-V 在通信基础设施中的位置、L1/L2 边界 | 1 | 基带芯片、体系结构 |
| `LANGUAGES` | 编程语言与工程实践：工具链与性能、C/C++、Python、MATLAB/Simulink、Verilog | 5 | 所有岗位的底层能力 |
| `MANAGEMENT` | 工程项目管理：方法论、生命周期、计划与挣值、风险、治理、成熟企业实践 | 1 | 技术负责人、项目管理 |
| `BUSINESS` | 价值主导的商业模式：价值创造与捕获、计费度量、定价、条款 | 1 | 产品、商业化、技术决策 |

按目标岗位选起点：

| 目标岗位 | 从哪里开始 |
| --- | --- |
| RAN / 协议栈 | `MN` 01-2 → 01-6 → 01-7 → 01-8，再 `DATAPLANE` 05-1 |
| WLAN / AP 与客户端 | `WLAN` 02-14 → 02-15 → 02-1 → 02-5 → 02-4 → 02-8 → 02-10，再 02-13 与 02-9 |
| 嵌入式 / Linux 平台 | `EMBEDDED` 04-3 → 04-1 → 04-2 → 04-4 → 04-5 → 04-6，再 `MN` 01-6 |
| 端侧 AI / 推理系统 | `AI` 06-3 → 06-1 → 06-2，再 `DATAPLANE` 05-2 |
| 技术负责人 / 架构 | `SILICON` 07-1 与 `MANAGEMENT` 09-1 横向读，其余按需 |

## 学习方法

- **Anchors 就是考纲。** 每篇 8–20 条有日期、可核查的事实：条款号、冻结日期、实测数字。能脱离文件说出来，就能把它讲住。
- **先还原一张图。** 图里的结构比正文忘得快，而结构恰恰是最常被追问的部分。
- **讲回去 90 秒。** 不用行话，讲给领域外的人听；卡在哪个术语上，就回去读哪一段。
- **按 1 / 3 / 7 / 21 天复习。** 同一篇读第二遍，价值低于读一篇邻居。四周冲刺计划在 MOC 的 §4。

## 许可

本仓库以 **GPL-3.0-or-later 或 AGPL-3.0-or-later** 双许可发布，使用者可任选其一。SPDX 标识符：`GPL-3.0-or-later OR AGPL-3.0-or-later`。

- 许可全文：`LICENSE`（GNU GPL v3）、`LICENSE-AGPL`（GNU AGPL v3）。
- 你可以自由使用、修改、再分发。再分发或衍生作品须保留版权与许可声明，并以同一许可发布；AGPL 另有「通过网络提供服务亦视为分发」的条款。
- 被引用的标准编号、书名、ISBN/DOI 与第三方引文归各自权利人所有，本仓库仅作引用与评论之用。

## 贡献

欢迎三类贡献，按价值排序：**带引用的勘误**（说法错了，或对的但过期了）、**填补空白的笔记**（放进已有目录）、**值得收进 `readlist.md` 的参考文献**。

一个 PR 一件事，提交时带 `git commit -s`（DCO 签署，不要求 CLA）。完整检查清单——编号、英文行文、一手来源、`VERIFY` 标记、Anchors/Related/References 结构、Mermaid 图、`readlist.md` 与目录表同步——见 MOC 的 §16。

最有价值的一种提交长这样：给出**说法、一手来源、日期、条款号**，而不是一句「这里不对」。

## 维护与勘误

- 每篇笔记的 **Anchors** 只放可核查的事实，正文负责论证。
- 无法独立确认的说法标 `VERIFY`，宁可留白也不写成结论。
- 流行说法与一手来源的差异集中在 [`knowledge-graph/99 Corrections`](knowledge-graph/99%20Corrections%20-%20Verified%20Facts%20That%20Popular%20Sources%20Get%20Wrong.md)：先查这里，再引用。
- 「什么时候该重读」按目录列在 MOC 的 §17——每个领域的失效触发条件不同。

---

# English

## What this is

An engineering knowledge base organised around a single thesis:

> Cellular and WLAN protocol stacks, heterogeneous compute and on-device AI are converging into one scheduling problem — deciding **what runs where, when**, under a hard latency and power budget. A RAN MAC scheduler, an edge task router and an LLM inference engine are the same closed loop at three different time scales.

So this is not a list of facts. Every note states where that analogy holds and, more usefully, where it breaks.

- **43 notes across 10 directories.** The directory is the domain; the note number is the reading order.
- **Every note has the same shape:** claim → layered argument with Mermaid diagrams → **Anchors** (dated, checkable facts) → **Related** (neighbours that get argued about together) → **References** (primary sources).
- **Notes are written in English only**, so they can be reused with international teams and in English interviews. The documentation is bilingual.
- **Doubt is marked, not smoothed over.** Claims that could not be independently confirmed carry a `VERIFY` flag, and the gap between the popular claim and the primary source is recorded in one corrections page.

## Repository layout

```
PersonalSkills/
├── README.md                    this file, Chinese and English
├── LICENSE                      GNU General Public License v3.0
├── LICENSE-AGPL                 GNU Affero General Public License v3.0
├── other/
│   ├── background.md  .cn.md    profile, role trajectory, original task statement
│   └── skills-draft.md  .cn.md  2026 knowledge framework and the A/B/C/D question groups
└── knowledge-graph/             the Obsidian vault — open *this* folder as a vault
    ├── 00 MOC - ...md           the only entry point: map, reading method, contribution method
    ├── 99 Corrections - ...md   verified facts that popular sources get wrong
    ├── MN/           01-x  mobile network (8 notes) + readlist.md
    ├── WLAN/         02-x  IEEE 802.11 (15 notes) + readlist.md
    ├── WSN/          03-x  low-power and sensor networking (1 note) + readlist.md
    ├── EMBEDDED/     04-x  embedded and systems software (6 notes) + readlist.md
    ├── DATAPLANE/    05-x  packet plane and heterogeneous compute (2 notes) + readlist.md
    ├── AI/           06-x  machine learning and inference (3 notes) + readlist.md
    ├── SILICON/      07-x  silicon and instruction-set architecture (1 note) + readlist.md
    ├── LANGUAGES/    08-x  programming languages and practice (5 notes) + readlist.md
    ├── MANAGEMENT/   09-x  engineering project management (1 note) + readlist.md
    └── BUSINESS/     10-x  value-driven business model (1 note) + readlist.md
```

Each directory carries its own `readlist.md` — the books, papers, standards and reports behind its notes, sectioned by note number, with `★★★` marking the entries to read or skim before quoting.

## Quick start

1. `git clone`, then in Obsidian choose "Open folder as vault" and point it at **`knowledge-graph/`** — not the repository root.
2. Start at `00 MOC`. It introduces each of the ten directories, gives the reading order inside each, and documents the reading and contribution methods.
3. Open the directory that matches your target role, read its notes in the order given, and pull primary sources from that directory's `readlist.md`.
4. In any note, read the opening claim and the closing **Anchors** first, then the body. It is the fastest way to decide whether the note deserves a close read.

## The ten directories

| Directory | Domain | Notes | Built for |
| --- | --- | --- | --- |
| `MN` | 3GPP radio access and the RAN stack: release map, L2, AI/ML for RAN, cellular IoT, random access, the DU scheduler, HARQ, and one open-source implementation | 8 | RAN, protocol stack, baseband software |
| `WLAN` | IEEE 802.11: fundamentals and history, transceiver and RF, generations, power saving, ecosystem, datapath, join, roaming, EasyMesh, scheduling, TSN, baseband and drivers, OpenWrt, openwifi, reliability and determinism | 15 | WLAN stack, AP and gateway, client |
| `WSN` | Low-power wireless: WPAN medium access, clustering, TSCH, age of information | 1 | IoT, low-power devices |
| `EMBEDDED` | Embedded and systems software: RTOS, embedded Linux, software architecture, interrupts, concurrency and IPC, device drivers | 6 | Embedded, Linux platform |
| `DATAPLANE` | Packet plane and heterogeneous compute: DPDK and the 5G UPF, cloud-edge-end, memory pooling and interconnect | 2 | Data plane, edge computing |
| `AI` | Machine learning and inference: foundations and failure modes, LLM serving, agent systems | 3 | On-device AI, inference systems |
| `SILICON` | Silicon and instruction-set architecture: where RISC-V sits in communications infrastructure, the L1/L2 boundary | 1 | Baseband silicon, architecture |
| `LANGUAGES` | Languages and practice: toolchain and performance, C/C++, Python, MATLAB/Simulink, Verilog | 5 | Foundation for every role |
| `MANAGEMENT` | Engineering project management: methodology, lifecycle, planning and earned value, risk, governance, practice | 1 | Technical lead, project management |
| `BUSINESS` | Value-driven business model: value creation and capture, the value metric, pricing, clauses | 1 | Product, commercial, technical decisions |

Where to start, by target role:

| Target role | Start here |
| --- | --- |
| RAN / protocol stack | `MN` 01-2 → 01-6 → 01-7 → 01-8, then `DATAPLANE` 05-1 |
| WLAN / AP and client | `WLAN` 02-14 → 02-15 → 02-1 → 02-5 → 02-4 → 02-8 → 02-10, then 02-13 and 02-9 |
| Embedded / Linux platform | `EMBEDDED` 04-3 → 04-1 → 04-2 → 04-4 → 04-5 → 04-6, then `MN` 01-6 |
| On-device AI / inference | `AI` 06-3 → 06-1 → 06-2, then `DATAPLANE` 05-2 |
| Technical lead / architect | `SILICON` 07-1 and `MANAGEMENT` 09-1 sideways, the rest on demand |

## How to read it

- **Anchors are the syllabus.** Each note carries 8–20 dated, checkable facts — a clause number, a freeze date, a measured value. If you can state them without the file, you can defend the note.
- **Reproduce a diagram from memory**, then diff it. Structure decays faster than prose, and structure is what gets tested.
- **Explain it back in 90 seconds**, without jargon, to someone outside the field. The term you reach for and cannot define is the paragraph to re-read.
- **Space the passes** at one, three, seven and twenty-one days. A second reading of the same note is worth less than a first reading of a neighbour. The four-week plan is in MOC §4.

## Licence

This repository is dual-licensed under **GPL-3.0-or-later or AGPL-3.0-or-later**; you may use it under either. SPDX identifier: `GPL-3.0-or-later OR AGPL-3.0-or-later`.

- Full texts: `LICENSE` (GNU GPL v3) and `LICENSE-AGPL` (GNU AGPL v3).
- You may use, modify and redistribute it freely. Redistribution and derivative works must keep the copyright and licence notices and be released under the same licence; the AGPL adds the network-use clause, so offering a modified version as a service also counts as distribution.
- Specification numbers, book titles, ISBNs, DOIs and third-party quotations remain the property of their respective owners and appear here for reference and comment only.

## Contributing

Three kinds of contribution are welcome, in this order of value: **a correction with a citation** (a claim that is wrong, or right but dated), **a note that fills a gap** in an existing directory, and **a reference** worth adding to a `readlist.md`.

One pull request per idea, committed with `git commit -s` (DCO sign-off; no CLA). The full checklist — numbering, English prose, primary sources, `VERIFY` flags, the Anchors/Related/References shape, Mermaid diagrams, and keeping `readlist.md` and the directory table in sync — is in MOC §16.

The most valuable pull request states **the claim, the primary source, the date and the clause** — not "this is wrong".

## Maintenance and corrections

- **Anchors** hold only checkable facts; the body does the arguing.
- Claims that could not be independently confirmed are marked `VERIFY` rather than asserted.
- The gap between the popular claim and the primary source is collected in [`knowledge-graph/99 Corrections`](knowledge-graph/99%20Corrections%20-%20Verified%20Facts%20That%20Popular%20Sources%20Get%20Wrong.md). Check it before you quote a number.
- What makes each directory go stale — and therefore when to re-read it — is tabulated in MOC §17, because the trigger is different in every domain.

---

_Copyright (c) 2026 Washington Ruan and contributors · licensed under **GPL-3.0-or-later** or **AGPL-3.0-or-later**, at your option · see `LICENSE` and `LICENSE-AGPL`._
