---
title: PersonalSkills — 通信 × 异构算力 × AI 知识库
lang: zh-CN
category: project-readme
version: 1.11
sibling: README.md
last-updated: 2026-10-23
copyright: "Copyright (c) 2026 Washington Ruan. All rights reserved."
---

# PersonalSkills

**通信 × 异构算力 × AI —— 面试准备、知识框架与知识图谱**

> 语言版本：简体中文（当前） · [English](README.md)

本仓库沉淀"通信技术 + 异构算力 + AI"交叉领域的面试准备材料与分领域知识点，包含 **5 份源文档 + 1 个 Obsidian 知识图谱（28 篇笔记）**。

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

```mermaid
flowchart LR
    MOC["00 MOC<br/>建立地图"] --> ROLE["按岗位选读 3–5 篇笔记"]
    ROLE --> SRC["readlist.md<br/>查阅一手资料"]
    SRC --> MOCK["skills-draft.cn.md<br/>A/B/C/D 四组自测"]
    MOCK --> SPRINT["48 小时冲刺<br/>只看 Anchors"]
```

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
| RAN 系统架构师 | 01-1 → 01-2 → 01-5 → 01-3 → 05-1 → 07-1 |
| 边缘 AI / 端边云架构师 | 06-3 → 05-2 → 06-1 → 06-2 → 08-1 → 04-2 |
| 嵌入式 / Linux 平台 | 04-3 → 04-1 → 04-2 → 07-1 → 05-1 → 08-1 |
| WLAN / 网关方向 | 02-1 → 02-2 → 02-3 → 02-5 → 02-6 → 02-7 → 02-4 → 03-1 → 04-3 |
| WLAN 安全 / 客户端协议栈方向 | 02-5 → 02-6 → 02-7 → 02-1 → 02-3 → 08-2 |
| 低功耗 / IoT 设备方向 | 02-2 → 03-1 → 01-4 → 01-5 → 04-1 |
| 软件 / 语言基础（任何岗位都要过一遍） | 08-2 → 08-3 → 08-1 |
| 算法建模 / DSP 原型验证 | 08-4 → 08-5 → 08-3 |

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
├── knowledge-graph/               Obsidian 知识图谱（Vault，28 篇笔记）
│   ├── 00 MOC - Comms x Compute x AI Knowledge Graph.md      ← 入口索引
│   ├── 01-1 5G-Advanced and 6G Radio Access.md
│   ├── 01-2 5G NR RAN Layer 2 Protocol Stack.md
│   ├── 01-3 AI-ML for RAN and O-RAN RIC.md
│   ├── 01-4 Cellular IoT RedCap eRedCap and NTN.md
│   ├── 01-5 NR Random Access - UE RACH Procedure, Signalling and Tuning.md
│   ├── 02-1 WLAN - Wi-Fi Generations Evolution.md
│   ├── 02-2 WLAN - Power Saving Mechanisms and Evolution.md
│   ├── 02-3 WLAN Ecosystem - WFA, EasyMesh and prpl.md
│   ├── 02-4 WLAN - Packet TX-RX Datapath and Offload Evolution.md
│   ├── 02-5 WLAN - STA-AP Discovery, Authentication and Association.md
│   ├── 02-6 WLAN - Multi-AP Roaming, Healing and Steering.md
│   ├── 02-7 WLAN - Wi-Fi EasyMesh, Operation, Tuning and Troubleshooting.md
│   ├── 03-1 Wireless Sensor Networks and Low-Power MAC.md
│   ├── 04-1 Embedded Systems RTOS and Hardware Interfaces.md
│   ├── 04-2 Linux Embedded Development - Drivers, Applications and Core Subsystems.md
│   ├── 04-3 Embedded Software Architecture - Patterns, Layering and Wireless System Structure.md
│   ├── 05-1 DPDK User Plane and 5G UPF.md
│   ├── 05-2 Cloud-Edge-End Collaboration and Heterogeneous Computing.md
│   ├── 06-1 LLM Inference Engines and xLLM.md
│   ├── 06-2 Agent Systems and Edge Orchestration.md
│   ├── 06-3 Machine Learning - Foundations, Core Algorithms and Applications.md
│   ├── 07-1 RISC-V for Communication Infrastructure.md
│   ├── 08-1 Programming Languages Toolchain and Performance Engineering.md
│   ├── 08-2 C and C++ Programming - Language Features, STL and Systems Practice.md
│   ├── 08-3 Python Programming - Language, Object Model and Engineering Practice.md
│   ├── 08-4 MATLAB and Simulink - Programming, Modelling and Code Generation.md
│   └── 08-5 Verilog HDL - RTL Design, Verification and Synthesis Practice.md
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
| `readlist.md` | 英文说明（标题保留原语种） | 参考文献 | 30 个主题域的书籍 / 论文 / 标准 / 文档清单，编号 `GG-x` 与图谱一致：01-1 5G-A 与 6G、01-2 NR L2、01-3 AI-RAN 与 O-RAN、01-4 RedCap/eRedCap/NTN、01-5 NR 随机接入（RACH）、02-1 WLAN 代际、02-2 WLAN 节能、02-3 WLAN 生态、02-4 WLAN 收发包流程与 offload、02-5 WLAN 发现、鉴权与关联、02-6 WLAN 漫游、自愈与引导、02-7 EasyMesh 原理与运维排障、03-1 WSN、04-1 嵌入式 RTOS、04-2 Linux 嵌入式、04-3 嵌入式软件架构、05-1 DPDK/UPF、05-2 端边云、06-1 LLM 推理与 xLLM、06-2 Agent、06-3 机器学习基础、07-1 RISC-V、08-1 语言与性能、08-2 C/C++、08-3 Python、08-4 MATLAB 与 Simulink、08-5 Verilog HDL，另附 28 一手标准库、29 阅读顺序、30 校核与维护 |

### 4.2 知识图谱笔记

| 编号 | 领域 | 核心覆盖 |
| --- | --- | --- |
| **00 MOC** | 总索引 | 统一心智模型、领域导航、编号方案、跨领域线索、仓库约定 |
| **01-1** | 5G-A / 6G 无线接入 | Rel-19/20/21 时间线、AI 原生空口、ISAC、U6G ELAA、NTN |
| **01-2** | 5G NR RAN L2 | MAC/RLC/PDCP/SDAP、HARQ、BSR、grant 生命周期、QoS 映射 |
| **01-3** | AI/ML for RAN 与 O-RAN | near-RT/non-RT RIC、xApp/rApp、DRL 调度、sim-to-real |
| **01-4** | 蜂窝 IoT | RedCap 分级、eRedCap、NTN、Ambient IoT、LP-WUS |
| **01-5** | **NR 随机接入（RACH）** | UE 随机接入全流程：MAC 层触发事件及其在 RRC 层的含义、RA 类型与按特性划分的接入资源选择（RedCap / SDT / NSAG / Msg3 重复）、PRACH 格式 0–3 与 A1–C2 及其 CP 隐含的小区半径、开环功率与功率爬坡规则、RA-RNTI 与 MSGB-RNTI 计算、RAR MAC PDU 与 Backoff Indicator 表、Msg3 调度（`k2 + Δ`）与载荷、竞争解决、两步接入 MsgA/MsgB 与 successRAR / fallbackRAR、CFRA 与波束失败恢复、SDT / NTN / RedCap 变体、时延预算、全部可调参数，以及分层排障决策树与症状对照表 |
| **02-1** | WLAN 代际演进 | Wi-Fi 4→9、MLO、OFDMA、UHR、多 AP 协同、逐特性设计细节 |
| **02-2** | **WLAN 节能技术** | 能耗方程与四类机制族；Legacy PS/PS-Poll、U-APSD、SMPS、VHT TXOP PS 与 OM Control、802.11ah 的 TWT/RAW/TIM 分段、802.11ax TWT 与 trigger-enabled SP、802.11ba 唤醒无线电、802.11be r-TWT、802.11bn AP Power Save / DPS / 跨链路节能、802.11bp 环境供能——含逐代机制对比表、Mermaid 图、实现分层与失效模式 |
| **02-3** | WLAN 生态 | WFA 认证、EasyMesh、prplMesh/prplOS/prpl LCM |
| **02-4** | **WLAN 收发包流程与 offload** | 端到端发送路径（socket → qdisc/AQL → mac80211 填头/TID/SN/加密 → 描述符 → EDCA/A-MPDU → PHY）与接收路径（同步 → MPDU 定界符扫描 → FCS/地址过滤/解密 → 重排缓冲 → DMA/NAPI/GRO → TCP），含逐字节开销核算；五类 offload 平面（单包加速、FullMAC/SoftMAC/混合、AP 转发 offload 与 PPE/NSS/Runner/WED、内核旁路、控制面）；MLO 重排；节能与数据面交互；"症状 → 定位层"排查表 |
| **02-5** | **WLAN 发现、鉴权与关联** | 逐阶段拆解入网流程：被动/主动扫描与 6 GHz 发现（RNR、PSC、FILS Discovery、禁止通配 Probe）、MLME 三状态与原因码、Open System/Shared Key/SAE（Dragonfly、H2E、Dragonblood）/OWE/802.1X-EAP 对比、关联与 AID、PMK→PMK-R0/R1→PTK 密钥体系与四次握手逐报文、PMF 与 SA Query、FT 与 802.11k/v、FILS、MLO 多链路建立与 per-STA profile、hostapd/wpa_supplicant/mac80211 分工，以及"症状 → 阶段"排查表 |
| **02-6** | **WLAN 多 AP 漫游、自愈与引导** | 为什么 802.11 把漫游决策留给终端，以及网络侧能做什么：四种切换方式的代价对比（完整入网 / PMKSA 缓存 / FT / FILS）、802.11k 的 Neighbor Report 与 Beacon Report、一次端到端切换的逐帧时序、ESS 尺度的 FT（R0KH 部署位置、`0x890D` over-the-DS 转发帧、五类现网失效、切换后数据面要重建什么）、BTM / MBO / assoc control / EasyMesh 客户端引导的决策函数与乒乓问题、以回程状态机为核心的 mesh 自愈（拓扑修复与信道切换）、MLD 粒度的 MLO 引导，以及 Wi-Fi 8 的 SMD 与 MAPC |
| **02-7** | **Wi-Fi EasyMesh 原理、调优与排障** | EasyMesh 标准化了什么、刻意不标准化什么；规范版本 v1.0→v6.0 与 Profile-1/2/3；IEEE 1905.1 CMDU 与 TLV 机制（真实报文号 `0x893A`、`0x8003`、`0x8014`、`0x8019`、`0x9B`）；WPS/PBC 与 DPP 两条入网路径（`mapBackhaulSta`、`mapAgent`、CCE、代理封装）；AP-Autoconfiguration 的 M1/M2 与 Multi-AP IE（`0xDD`、OUI `50-6F-9A`、类型 `0x1B` 与扩展子元素的位定义）；四地址回程与 `multi_ap=1/2/3`；四类测量机制；信道选择、三种引导机制与回程优化；部署取舍；全部可调策略字段；以及分层排障方法论与症状对照表 |
| **03-1** | WSN 与低功耗 MAC | 分簇路由、UAV 采集、TSCH、AoI |
| **04-1** | 嵌入式 RTOS | FreeRTOS、PendSV、I2C/SPI/UART/CAN、DMA、缓存一致性 |
| **04-2** | Linux 嵌入式开发 | 启动链、设备树、驱动、IPC、网络栈、虚拟化、PREEMPT_RT |
| **04-3** | 嵌入式软件架构 | 分层与 HAL/BSP 划分、执行模型（超级循环 / 时间触发 / RTOS / 主动对象）、调度理论、HSM 与事件驱动、设计模式、数据所有权与邮箱接口、无线协议栈切分（L1/L2 边界、CU/DU、O-RAN 7-2x）、内存与功耗架构、OTA 与回滚、ISO 26262 / IEC 61508 安全架构 |
| **05-1** | DPDK 与 5G UPF | mbuf/mempool、PFCP、PDR/FAR/QER、QoS 执行、小包 pps |
| **05-2** | 端边云协同与异构算力 | UnifiedBus、内存池化、MFU、RDMA |
| **06-1** | LLM 推理引擎与 xLLM | KV Cache、PagedAttention、量化、算子融合、prefill/decode |
| **06-2** | Agent 系统与边缘编排 | GRAFT、多设备 SLM mesh、安全边界执行 |
| **06-3** | **机器学习基础、核心算法与应用** | 从入门到实践的完整路径（英文）：AI / 机器学习 / 深度学习 / 生成式建模的边界；模型 / 损失 / 优化器三要素与学习闭环；监督、无监督、自监督、半监督与强化学习及范式选择决策树；端到端流程、切分与交叉验证、六类数据泄漏；各类数据的表示、编码、标准化与维度灾难；线性回归与逻辑回归手算梯度、偏差-方差与正则化、决策树的 Gini 划分算例、Bagging 与 Boosting、kNN、SVM、朴素贝叶斯、k-means、DBSCAN 与 PCA；神经网络与逐步反传数值算例、优化器与正则化；CNN、RNN/LSTM、Transformer、迁移学习与生成式架构及尺寸算力算例；大规模训练、精度与三种并行策略；由一张混淆矩阵推导全部评估指标、调参方法、应用方向、MLOps、失效模式与四周学习路径 |
| **07-1** | RISC-V 通信基础设施 | 基带集群、软件定义 PHY、H 扩展、L1/L2 接口 |
| **08-1** | 语言、工具链与性能工程 | 构建系统、内核旁路选型、性能方法论、各语言的定位与衔接 |
| **08-2** | C/C++ 编程与 STL | C23/C++26 语言特性、模板与编译期计算、内存模型与并发、STL 容器/迭代器/算法、系统级惯用法与 UB 清单 |
| **08-3** | **Python 编程** | CPython 执行模型（字节码、特化、JIT、GIL 与自由线程）、dunder 对象协议、属性查找与 C3 MRO、从 dataclass 到 Protocol 到元类的类体系、生成器与 asyncio、类型标注演进、NumPy 跨步数组模型、性能决策树、打包与测试实践 |
| **08-4** | **MATLAB 与 Simulink** | 列主序数组语义与写时复制、向量化、`classdef` 值类与句柄类、`arguments` 参数校验、事件、System 对象、Simulink 采样时间与求解器选择、Stateflow、定点字长设计、Embedded/HDL Coder、SIL/PIL/HIL |
| **08-5** | **Verilog HDL** | IEEE 1364→1800 沿革、线网与变量及四值逻辑、阻塞与非阻塞调度、状态机与复位纪律、时序方程、CDC 与异步 FIFO、测试平台与 SystemVerilog 类/UVM、FPGA 与 ASIC 综合流程、DSP RTL 结构 |

---

## 五、知识图谱使用说明

1. **打开方式**：在 Obsidian 中选择"打开本地仓库"，指向 `knowledge-graph/` 文件夹（而非项目根目录）。
2. **入口**：`00 MOC` 是唯一导航页，其余 27 篇均通过 `[[wikilink]]` 双向连通，可用 Graph View 查看关联密度。
3. **命名规则**：笔记按领域分组编号 `GG-x`——`00 MOC` 为索引，八个领域组从 `01` 起**连续编号**：`01-x` 移动通信、`02-x` WLAN、`03-x` 低功耗与传感组网、`04-x` 嵌入式与系统软件、`05-x` 数据面与异构算力、`06-x` AI 推理与智能体系统、`07-x` 芯片与指令集、`08-x` 编程语言与工程实践。组号顺序沿信号路径由内向外展开：从空口一直到芯片与语言底座。文件名即主题，便于按编号排序与按名检索。
4. **笔记结构**：知识点正文 → **Anchors（事实锚点）** → **Related（关联笔记）**，三段式固定。
5. **图示**：笔记使用 Mermaid 代码块，在 Obsidian 阅读视图中原生渲染。凡涉及结构的章节都配图——版本时间线、协议栈与数据通路、控制回路、决策树与状态机——全库共 153 个图块。
6. **检索建议**：优先用 `tags` 与 `aliases`（frontmatter 中已定义），其次用全文搜索标准号（如 `38.914`、`802.11bn`）。

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
| TWT 的出处 | 常被归为 802.11ax | 实为 **802.11ah-2016**（Wi-Fi HaLow）首创，后引入 802.11ax；802.11be 又增加 **r-TWT**，它首先是时延机制、其次才是节能机制 |
| 802.11bi | 有时被说成唤醒无线电 | 实为 **Enhanced Privacy Protection**，**2026-09-25** 批准发布（见笔记 02-2）；唤醒无线电修订版是 **802.11ba-2021** |
| r-TWT 落地情况 | 常被当作 Wi-Fi 7 已有能力 | r-TWT 在 802.11be 中为**可选**特性，且**不在 Wi-Fi CERTIFIED 7 强制要求内**；2026 年 CWNP 综述指出在售客户端与 AP 未声明支持。引用前按 `VERIFY` 处理 |

**更新触发点**

- 3GPP TSG 全会（每年 4 次）→ 更新 01-1/01-2/01-4
- 3GPP TS 38.321 / 38.331 新版发布与 RAN1/RAN2 关于随机接入的会议结论 → 更新 01-5（字段长度、计数器、窗口与参数取值都是随版本变化的；本文引用基线为 TS 38.321 v17.3.0，2023-01）
- 3GPP TS 38.321 / 38.331 新版发布与 RAN1/RAN2 关于随机接入的会议结论 → 更新 01-5（字段长度、计数器、窗口与参数取值都是随版本变化的；本文引用基线为 TS 38.321 v17.3.0，2023-01）
- IEEE 802.11 WG 与 WFA 认证公告 → 更新 02-1/02-2/02-3
- TGbn / TGbp 投票里程碑、WFA 功耗相关认证 → 更新 02-2（AP Power Save 仍为草案特性，P802.11bp 处于 D1.0 WG 投票）
- Linux kernel 主线与 LTS 发布 → 更新 08-1/04-2
- xLLM / Agent 框架的版本与论文 → 更新 06-1/06-2
- 主流框架大版本（scikit-learn、PyTorch、JAX）与教材新版 → 更新 06-3（本文引用基线为 scikit-learn 1.9.1 与 PyTorch 2.14.1，均为 2026 年 9 月）
- WG21 / WG14 会议与 GCC、Clang 大版本发布 → 更新 08-2
- CPython 特性版本发布（每年 10 月）与 PEP 采纳、NumPy 大版本 → 更新 08-3
- MATLAB / Simulink 发布（每年 3 月与 9 月）与 HDL / Embedded Coder 能力变化 → 更新 08-4
- IEEE 1800 修订与 IEEE 1800.2（UVM）修订 → 更新 08-5
- WFA Multi-AP / EasyMesh 规范修订与 prplMesh 版本发布 → 更新 02-7（当前为 v6.0，自 2024-12-31 起对新测 mesh 设备强制；报文号与 TLV 编号随版本增长）
- AUTOSAR 年度发布（每年 11 月）、MISRA 文档修订、Zephyr 半年发布与 LTS 分支 → 更新 04-3

---

## 八、维护者

Washington Ruan —— 通信软件 / 嵌入式软件 / 无线协议栈工程师与系统架构师；方向为 5G RAN L2、WLAN/WFA、IoT/WSN、嵌入式与 Linux、AI/ML、云边端协同与异构算力。

---

## 版权

Copyright (c) 2026 **Washington Ruan**. All rights reserved.

本仓库所有文档与笔记的著作权归 Washington Ruan 所有。未经书面许可，不得用于商业发布或二次分发。

---

© 2026 Washington Ruan. All rights reserved.
