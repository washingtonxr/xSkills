---
title: PersonalSkills — 通信 × 异构算力 × AI 知识库
lang: zh-CN
category: project-readme
version: 1.2
sibling: README.md
last-updated: 2026-10-22
copyright: "Copyright (c) 2026 Washington Ruan. All rights reserved."
---

# PersonalSkills

**通信 × 异构算力 × AI —— 面试准备、知识框架与知识图谱**

> 语言版本：简体中文（当前） · [English](README.md)

本仓库沉淀"通信技术 + 异构算力 + AI"交叉领域的面试准备材料与分领域知识点，包含 **5 份源文档 + 1 个 Obsidian 知识图谱（18 篇笔记）**。

---

## 一、项目定位

所有内容围绕一条主线组织：

> 蜂窝 / WLAN 协议栈、异构算力与端侧 AI 正在收敛为同一个调度问题——在确定的时延与功耗预算下，决定"什么任务在什么时间、运行在什么资源上"。

因此本项目不只是罗列知识点，而是把 **RAN MAC 调度器、端边云任务编排器、LLM 推理引擎** 视为同一问题形态的三种实例，并显式标注类比的成立条件与失效边界。

四条贯穿全库的交叉线索：

1. **确定性** —— 尾时延 / P99 是 Wi-Fi 8 UHR、URLLC 与 Agent 编排共享的 KPI。
2. **内存语义** —— KV Cache、内存池化、UnifiedBus 全局统一编址，是同一场战斗在三个层次上的不同形态。
3. **接口语义** —— L1 加速器 ↔ L2 通用核、NPU ↔ CPU、coordinator ↔ worker：边界成本永远高于计算成本。
4. **验证方法学** —— 仿真 → 数据回放 → 硬件在环，是 AI 调度器与 AI 原生 PHY 唯一可信的落地路径。

---

## 二、快速开始：推荐阅读路径

| 阶段 | 做什么 | 目标产出 |
| --- | --- | --- |
| 1. 建立地图 | 通读 `knowledge-graph/00 MOC ...` | 掌握统一心智模型与领域导航 |
| 2. 按岗位选读 | 见下方选读建议 | 形成 3–5 个可深挖的领域主线 |
| 3. 追一手资料 | 按 `readlist.md` 对应章节查阅书籍 / 论文 / 标准 | 每个关键论断都有一手出处可引 |
| 4. 模拟面试 | 用 `skills-draft.cn.md`（或 `skills-draft.md`）的 A/B/C/D 四组题目自测 | 每个问题能给出参数级答案 |
| 5. 48 小时冲刺 | 只看各笔记的 **Anchors** 小节 + `skills-draft.cn.md` 第四部分速查清单 | 数字、时间线、架构图脱口而出 |

**按目标岗位选读**

| 目标岗位 | 优先笔记 |
| --- | --- |
| RAN 系统架构师 | 01 → 02 → 03 → 08 → 12 |
| 边缘 AI / 端边云架构师 | 09 → 10 → 11 → 13 → 15 |
| 嵌入式 / Linux 平台 | 17 → 07 → 15 → 12 → 08 → 13 |
| WLAN / 网关方向 | 04 → 14 → 06 → 17 |
| 软件 / 语言基础（任何岗位都要过一遍） | 16 → 13 |

---

## 三、目录结构

```
261022,PersonalSkills/
├── README.md                      Project README（English，默认）
├── README.cn.md                   项目说明（中文，本文件）
├── background.md                  Personal Background and Task Statement（English，默认）
├── background.cn.md               个人背景与任务说明（中文）
├── skills-draft.md                Knowledge Framework and Interview Outline（English，默认）
├── skills-draft.cn.md             知识框架与面试题纲（中文）
├── readlist.md                    参考文献清单（中英文书籍 / 论文 / 标准，说明为英文）
├── knowledge-graph/               Obsidian 知识图谱（Vault，18 篇笔记）
│   ├── 00 MOC - Comms x Compute x AI Knowledge Graph.md      ← 入口索引
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
│   ├── 16 C and C++ Programming - Language Features, STL and Systems Practice.md
│   └── 17 Embedded Software Architecture - Patterns, Layering and Wireless System Structure.md
└── .workbuddy/                    项目工作数据（勿删）
```

---

## 四、文档清单

### 4.1 源文档

| 文件 | 语言 | 定位 | 主要内容 |
| --- | --- | --- | --- |
| `README.md` | English | 项目说明 | 项目定位、阅读路径、目录结构、文档清单、仓库约定、事实校核策略 |
| `README.cn.md` | 中文 | 项目说明 | 同上，中文表述 |
| `background.md` | English | 输入源 | 背景原文 + 结构化拆解（学历 / 证书 / 任职轨迹 / 领域 / 技术栈）+ 任务要求 |
| `background.cn.md` | 中文 | 输入源 | 同上，中文表述 |
| `skills-draft.md` | English | 主文档 | 2026 知识框架（6 大领域）+ 面试题纲（A/B/C/D 四层）+ Word 产出结构 |
| `skills-draft.cn.md` | 中文 | 主文档 | 同上，中文表述 |
| `readlist.md` | 英文说明（标题保留原语种） | 参考文献 | 20 个主题域的书籍 / 论文 / 标准 / 文档清单：01 5G-A 与 6G、02 NR L2、03 AI-RAN 与 O-RAN、04 WLAN 代际、05 RedCap/eRedCap/NTN、06 WSN、07 嵌入式 RTOS、08 DPDK/UPF、09 端边云与异构算力、10 LLM 推理与 xLLM、11 Agent 与边缘编排、12 RISC-V、13 语言与性能、14 WLAN 生态、15 Linux 嵌入式、16 C/C++ 语言与 STL、17 嵌入式软件架构，另附 18 一手标准库、19 阅读顺序、20 校核与维护 |

### 4.2 知识图谱笔记

| 编号 | 领域 | 核心覆盖 |
| --- | --- | --- |
| **00 MOC** | 总索引 | 统一心智模型、领域导航、跨领域线索、仓库约定 |
| 01 | 5G-A / 6G 无线接入 | Rel-19/20/21 时间线、AI 原生空口、ISAC、U6G ELAA、NTN |
| 02 | 5G NR RAN L2 | MAC/RLC/PDCP/SDAP、HARQ、BSR、grant 生命周期、QoS 映射 |
| 03 | AI/ML for RAN 与 O-RAN | near-RT/non-RT RIC、xApp/rApp、DRL 调度、sim-to-real |
| 04 | WLAN 代际演进 | Wi-Fi 4→9、MLO、OFDMA、UHR、多 AP 协同、逐特性设计细节 |
| 05 | 蜂窝 IoT | RedCap 分级、eRedCap、NTN、Ambient IoT、LP-WUS |
| 06 | WSN 与低功耗 MAC | 分簇路由、UAV 采集、TSCH、AoI |
| 07 | 嵌入式 RTOS | FreeRTOS、PendSV、I2C/SPI/UART/CAN、DMA、缓存一致性 |
| 08 | DPDK 与 5G UPF | mbuf/mempool、PFCP、PDR/FAR/QER、QoS 执行、小包 pps |
| 09 | 端边云协同与异构算力 | UnifiedBus、内存池化、MFU、RDMA |
| 10 | LLM 推理引擎与 xLLM | KV Cache、PagedAttention、量化、算子融合、prefill/decode |
| 11 | Agent 系统与边缘编排 | GRAFT、多设备 SLM mesh、安全边界执行 |
| 12 | RISC-V 通信基础设施 | 基带集群、软件定义 PHY、H 扩展、L1/L2 接口 |
| 13 | 语言、工具链与性能工程 | 构建系统、Python、内核旁路选型、性能方法论 |
| 14 | WLAN 生态 | WFA 认证、EasyMesh、prplMesh/prplOS/prpl LCM |
| 15 | Linux 嵌入式开发 | 启动链、设备树、驱动、IPC、网络栈、虚拟化、PREEMPT_RT |
| 16 | C/C++ 编程与 STL | C23/C++26 语言特性、模板与编译期计算、内存模型与并发、STL 容器/迭代器/算法、系统级惯用法与 UB 清单 |
| **17** | **嵌入式软件架构** | 分层与 HAL/BSP 划分、执行模型（超级循环 / 时间触发 / RTOS / 主动对象）、调度理论、HSM 与事件驱动、设计模式、数据所有权与邮箱接口、无线协议栈切分（L1/L2 边界、CU/DU、O-RAN 7-2x）、内存与功耗架构、OTA 与回滚、ISO 26262 / IEC 61508 安全架构 |

---

## 五、知识图谱使用说明

1. **打开方式**：在 Obsidian 中选择"打开本地仓库"，指向 `knowledge-graph/` 文件夹（而非项目根目录）。
2. **入口**：`00 MOC` 是唯一导航页，其余 17 篇均通过 `[[wikilink]]` 双向连通，可用 Graph View 查看关联密度。
3. **命名规则**：`00 MOC` 为索引；`01`–`17` 为领域笔记，文件名即主题，便于按编号排序与按名检索。
4. **笔记结构**：知识点正文 → **Anchors（事实锚点）** → **Related（关联笔记）**，三段式固定。
5. **检索建议**：优先用 `tags` 与 `aliases`（frontmatter 中已定义），其次用全文搜索标准号（如 `38.914`、`802.11bn`）。

---

## 六、仓库约定

1. **语言与文件命名**：`knowledge-graph/` 下全部笔记使用**英文**书写，便于国际团队与英文面试场景直接复用；源文档中英双语并存、一一对应，且**以英文为默认（无后缀）、中文加 `.cn` 后缀**：`README.md` / `README.cn.md`、`background.md` / `background.cn.md`、`skills-draft.md` / `skills-draft.cn.md`；`readlist.md` 是唯一例外——文献标题已保留原语种、说明文字统一用英文，因此不另设中文版。
2. **Frontmatter**：所有 `.md` 文件均含 YAML frontmatter，字段包括 `title`、`lang`、`category`、`last-updated`、`copyright`；中英对照文档另加 `sibling` 指向另一语种版本，有修订历史的文档另加 `version`。
3. **事实锚点**：每个笔记末尾设 **Anchors** 小节，只写可核实且带日期或编号的事实（标准号、冻结时间、论文 DOI、发布版本）。
4. **存疑标注**：无法独立核实的信息一律标注 **`VERIFY`**，不作断言。
5. **双向链接**：`[[wikilink]]` 是有意为之的——一条链接意味着两个概念会在面试中被放在一起讨论；链接完整性可核验。
6. **编码与格式**：全部文件使用 UTF-8；正文以 Markdown 标准语法书写，表格用于对比，引用块用于"主线/原则"类陈述。
7. **版权头**：每个文件在 frontmatter 与文末同时标注版权信息。
8. **参考文献规则**：`readlist.md` 中的文献名称一律保留出版时的原始形式（中文书保留中文书名与 `《》`），不做翻译；条目的说明文字一律用英文书写。

---

## 七、事实校核与更新策略

**源文档与知识图谱的分工**

- `skills-draft.cn.md` / `skills-draft.md` 忠实保留原始草稿的表述与判断，便于对照原始思路；
- 校核后的事实以 `knowledge-graph/` 各笔记的 **Anchors** 小节为准。

**已校正的事实（引用时请以 Anchors 为准）**

| 条目 | 原始草稿 | 校核结论 |
| --- | --- | --- |
| eRedCap 归属 | 归为 Rel-19 | 属 **Rel-18**（2024-06 冻结，5 MHz、1 Rx、HD-FDD、~10 Mbps）；Rel-19 的贡献是 NTN 扩展、LP-WUS 与 Ambient IoT |
| Wi-Fi 8 进展 | Draft 1.0（2025-08） | **Draft 1.0 为 2025-07**；Draft 2.0 于 2026-09-02 以 76.5% 通过 WG ballot；WFA 认证约 **2028-01** |
| Rel-21 节点 | "2029 完成、2030 商用" | 官方四个里程碑：Stage-1 **2027-03** / Stage-2 **2028-06** / Stage-3 **2028-12** / ASN.1+OpenAPI **2029-03** |
| PREEMPT_RT | 未涉及 | 已于 **Linux 6.12（2024-11）** 合入主线（x86/arm64/RISC-V），32 位 ARM 于 7.1 补齐 |
| C/C++ 标准现状 | 仅提及 "C/C++" | **C23 = ISO/IEC 9899:2024**（2024-10-31 发布，`__STDC_VERSION__` = 202311L）；**C++26 由 WG21 于 2026-03-28 定稿**（工作草案 N5046），待发布为 ISO/IEC 14882:2026 |
| AUTOSAR / MISRA 版本 | 未涉及 | **AUTOSAR R25-11** 为当前版本（2025-12-04 发布会）；**MISRA C:2025** 为 C 语言现行版并取代 MISRA C:2023；**MISRA C++:2023**（TC1:2026）面向 C++17 —— 因此符合 MISRA 的 C++ 项目并不在 C++20/23/26 上 |

**更新触发点**

- 3GPP TSG 全会（每年 4 次）→ 更新 01/02/05
- IEEE 802.11 WG 与 WFA 认证公告 → 更新 04/14
- Linux kernel 主线与 LTS 发布 → 更新 13/15
- xLLM / Agent 框架的版本与论文 → 更新 10/11
- WG21 / WG14 会议与 GCC、Clang 大版本发布 → 更新 16
- AUTOSAR 年度发布（每年 11 月）、MISRA 文档修订、Zephyr 半年发布与 LTS 分支 → 更新 17

---

## 八、维护者

Washington Ruan —— 通信软件 / 嵌入式软件 / 无线协议栈工程师与系统架构师；方向为 5G RAN L2、WLAN/WFA、IoT/WSN、嵌入式与 Linux、AI/ML、云边端协同与异构算力。

---

## 版权

Copyright (c) 2026 **Washington Ruan**. All rights reserved.

本仓库所有文档与笔记的著作权归 Washington Ruan 所有。未经书面许可，不得用于商业发布或二次分发。

---

© 2026 Washington Ruan. All rights reserved.
