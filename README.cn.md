---
title: PersonalSkills — 通信 × 异构算力 × AI 知识库
lang: zh-CN
category: project-readme
version: 1.24
sibling: README.md
last-updated: 2026-10-25
copyright: "Copyright (c) 2026 Washington Ruan. All rights reserved."
---

# PersonalSkills

**通信 × 异构算力 × AI —— 面试准备、知识框架与知识图谱**

> 语言版本：简体中文（当前） · [English](README.md)

本仓库沉淀"通信技术 + 异构算力 + AI"交叉领域的面试准备材料与分领域知识点，包含 **5 份源文档 + 1 个 Obsidian 知识图谱（41 篇笔记）**。

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
| RAN 系统架构师 | 01-1 → 01-2 → 01-6 → 01-7 → 01-8 → 01-5 → 01-3 → 05-1 → 07-1 |
| 边缘 AI / 端边云架构师 | 06-3 → 05-2 → 06-1 → 06-2 → 08-1 → 04-2 → 04-5 |
| 嵌入式 / Linux 平台 | 04-3 → 04-1 → 04-2 → 04-6 → 04-4 → 04-5 → 01-6 → 07-1 → 05-1 → 08-1 |
| WLAN / 网关方向 | 02-1 → 02-2 → 02-3 → 02-5 → 02-6 → 02-7 → 02-4 → 02-8 → 02-9 → 02-10 → 02-11 → 02-12 → 02-13 → 03-1 → 04-3 |
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
├── knowledge-graph/               Obsidian 知识图谱（Vault，41 篇笔记）
│   ├── 00 MOC - Comms x Compute x AI Knowledge Graph.md      ← 入口索引
│   ├── 01-1 5G-Advanced and 6G Radio Access.md
│   ├── 01-2 5G NR RAN Layer 2 Protocol Stack.md
│   ├── 01-3 AI-ML for RAN and O-RAN RIC.md
│   ├── 01-4 Cellular IoT RedCap eRedCap and NTN.md
│   ├── 01-5 NR Random Access - UE RACH Procedure, Signalling and Tuning.md
│   ├── 01-6 NR DU MAC Scheduler - Resource Allocation, HARQ and Real-Time Implementation.md
│   ├── 01-7 NR HARQ - Retransmission Flow, Timelines and LTE Comparison.md
│   ├── 01-8 5G NR - OpenAirInterface - Architecture of an Open-Source NR Stack.md
│   ├── 02-1 WLAN - Wi-Fi Generations Evolution.md
│   ├── 02-2 WLAN - Power Saving Mechanisms and Evolution.md
│   ├── 02-3 WLAN Ecosystem - WFA, EasyMesh and prpl.md
│   ├── 02-4 WLAN - Packet TX-RX Datapath and Offload Evolution.md
│   ├── 02-5 WLAN - STA-AP Discovery, Authentication and Association.md
│   ├── 02-6 WLAN - Multi-AP Roaming, Healing and Steering.md
│   ├── 02-7 WLAN - Wi-Fi EasyMesh, Operation, Tuning and Troubleshooting.md
│   ├── 02-8 WLAN - Scheduling - Channel Access, EDCA, OFDMA Resource Allocation, Airtime and Implementation.md
│   ├── 02-9 WLAN - Time-Sensitive Networking Across Wi-Fi Generations.md
│   ├── 02-10 WLAN - Baseband and Driver Architecture for Wi-Fi 6, 7 and 8 - Qualcomm as the Reference Design.md
│   ├── 02-11 WLAN - OpenWrt and the Software Architecture of a Wireless System.md
│   ├── 02-12 WLAN - openwifi - An Open-Source FPGA 802.11 Platform.md
│   ├── 02-13 WLAN - Reliability, Low Latency and Determinism - What the Wi-Fi Stack Can Actually Do.md
│   ├── 03-1 Wireless Sensor Networks and Low-Power MAC.md
│   ├── 04-1 Embedded Systems RTOS and Hardware Interfaces.md
│   ├── 04-2 Linux Embedded Development - Drivers, Applications and Core Subsystems.md
│   ├── 04-3 Embedded Software Architecture - Patterns, Layering and Wireless System Structure.md
│   ├── 04-4 Linux Interrupts - Types, Handlers, Threaded IRQs and Deferred Work.md
│   ├── 04-5 Linux Concurrency - Kernel and User Mode, Processes, Threads and IPC.md
│   ├── 04-6 Linux Device Drivers - Model, Probe, Data Path, Power and Bring-Up.md
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
│   ├── 08-5 Verilog HDL - RTL Design, Verification and Synthesis Practice.md
│   └── 09-1 Engineering Project Management - Methodology, Lifecycle, Tools and Best Practice.md
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
| `readlist.md` | 英文说明（标题保留原语种） | 参考文献 | 43 个主题域的书籍 / 论文 / 标准 / 文档清单，编号 `GG-x` 与图谱一致：01-1 5G-A 与 6G、01-2 NR L2、01-3 AI-RAN 与 O-RAN、01-4 RedCap/eRedCap/NTN、01-5 NR 随机接入（RACH）、01-6 NR DU MAC 调度器、01-7 NR HARQ 及与 LTE 的对比、01-8 OpenAirInterface、02-1 WLAN 代际、02-2 WLAN 节能、02-3 WLAN 生态、02-4 WLAN 收发包流程与 offload、02-5 WLAN 发现、鉴权与关联、02-6 WLAN 漫游、自愈与引导、02-7 EasyMesh 原理与运维排障、02-8 Wi-Fi 调度、02-9 Wi-Fi TSN、02-10 Wi-Fi 基带与驱动架构、02-11 OpenWrt 与无线系统软件、02-12 openwifi、02-13 可靠性/低时延/确定性、03-1 WSN、04-1 嵌入式 RTOS、04-2 Linux 嵌入式、04-3 嵌入式软件架构、04-4 Linux 中断、04-5 并发与进程/线程/IPC、04-6 设备驱动、05-1 DPDK/UPF、05-2 端边云、06-1 LLM 推理与 xLLM、06-2 Agent、06-3 机器学习基础、07-1 RISC-V、08-1 语言与性能、08-2 C/C++、08-3 Python、08-4 MATLAB 与 Simulink、08-5 Verilog HDL、09-1 工程项目管理，另附 40 一手标准库、41 阅读顺序、42 校核与维护 |

### 4.2 知识图谱笔记

| 编号 | 领域 | 核心覆盖 |
| --- | --- | --- |
| **00 MOC** | 总索引 | 统一心智模型、领域导航、编号方案、跨领域线索、仓库约定 |
| **01-1** | 5G-A / 6G 无线接入 | Rel-19/20/21 时间线、AI 原生空口、ISAC、U6G ELAA、NTN |
| **01-2** | 5G NR RAN L2 | MAC/RLC/PDCP/SDAP、HARQ、BSR、grant 生命周期、QoS 映射 |
| **01-3** | AI/ML for RAN 与 O-RAN | near-RT/non-RT RIC、xApp/rApp、DRL 调度、sim-to-real |
| **01-4** | 蜂窝 IoT | RedCap 分级、eRedCap、NTN、Ambient IoT、LP-WUS |
| **01-5** | **NR 随机接入（RACH）** | UE 随机接入全流程：MAC 层触发事件及其在 RRC 层的含义、RA 类型与按特性划分的接入资源选择（RedCap / SDT / NSAG / Msg3 重复）、PRACH 格式 0–3 与 A1–C2 及其 CP 隐含的小区半径、开环功率与功率爬坡规则、RA-RNTI 与 MSGB-RNTI 计算、RAR MAC PDU 与 Backoff Indicator 表、Msg3 调度（`k2 + Δ`）与载荷、竞争解决、两步接入 MsgA/MsgB 与 successRAR / fallbackRAR、CFRA 与波束失败恢复、SDT / NTN / RedCap 变体、时延预算、全部可调参数，以及分层排障决策树与症状对照表——**并分别从两侧重述同一流程：§9 是 UE 侧状态机与计数器，§10 是 gNB 侧的前导检测、RAR 组装与 CU-DU 分工，§10.4 列出双方各自知道而对方不知道的信息** |
| **01-6** | **NR DU 侧 MAC 调度器** | 调度器在 DU 内的完整实现：CU/DU 切分与 7-2x 前传的四个平面及八种 C-plane section type、FAPI 的 L2/L1 接口与每时隙消息时序、调度器同时分配的四种资源、含 O-RAN T1a/T2a/Ta3/Ta4 时间窗与 k0/k1/k2 下限的每时隙时间预算、十二个内部模块、十一步决策流水线、两阶段 TD/FD 下行分配与排序策略及 TBS 计算、SR/BSR/授权的上行链路与配置授权、HARQ 进程状态机与 PUCCH 应答难题、PDCCH 与 CCE 预算及候选位置哈希、TDD 与 DRX、实时执行模型、KPI 体系与排障决策树 |
| **01-7** | **NR HARQ · 与 LTE 对比** | 两代系统的重传机制全解：软缓冲区存什么、LLR 如何合并；每种 HARQ 方案都要回答的四个设计问题；NR 的实体与进程架构（缺省 8 进程、上限 16）；从 TB CRC、LDPC、速率匹配到 HARQ-ACK 判决的下行流水线；没有 PHICH、「下一个授权就是反馈」的上行流水线；k0/k1/k2 与 N1/N2 处理时延，以及算出来的 2.5 ms 往返对比 LTE 的 8 ms；三种 HARQ-ACK 码本与一个 type-2 DAI 算例；PUCCH 资源选择；CBGTI/CBGFI 的 CBG 重传；配置授权的推导进程号与 `configuredGrantTimer`；四个状态机；逐条对照的 NR 与 LTE 差异表（含 TDD 各配置的进程数表）；两代系统的软缓冲与 LBRM 计算；URLLC 与 NTN 的绕行方案；以及症状排查表 |
| **01-8** | **OpenAirInterface · 开源 NR 全栈** | 把整个 5G NR 协议栈当成一份能读的程序来讲：OAI 是什么、谁来治理；GPL → OAI PL v1.1 → CSSL v1.0 的许可演进与并入 Linux Foundation Networking 的 Duranta 项目；四大软件资产（RAN、CN、OAM、CI/CD）；从 `openair1` 到 `fronthaul` 的仓库地图；四个可执行文件各自变成什么网元；libconfig 与命令行参数面（真正有用的那十几个选项）；ITTI 任务与实时 L1 线程的两种执行模型（notifiedFIFO、线程池、启动屏障）；作为函数指针结构体的 FAPI L1/L2 接口与 P5/P7 节律；nFAPI 的 VNF/PNF 与三种传输；NR MAC 调度器逐文件拆解、preprocessor 与 postprocessor 的分工与 `gNB_dlsch_ulsch_scheduler()` 完整调用链；PHY 真正实现了什么，以及 USRP X310 的 80 MHz、N310 的 100 MHz 上限；RLC/PDCP/SDAP/RRC/NGAP/GTP-U 分别落在 F1 与 E1 的哪一侧；split 8 与 O-RAN 7.2x（libxran over DPDK、NETCONF/YANG、PTP）；nrUE 的 actor 框架与 k1/k2 处理预算；11 个 NF 的核心网；FlexRIC 与 E2/O1；从 `nr-ulsim`、`rfsim`、`vrtsim` 到 Colosseum 的仿真阶梯；带实际核分配表的实时性调优阶梯；实测吞吐表；与 srsRAN 的独立对比；排障决策树；以及十个面试简答 |
| **02-1** | WLAN 代际演进 | Wi-Fi 4→9、MLO、OFDMA、UHR、多 AP 协同、逐特性设计细节 |
| **02-2** | **WLAN 节能技术** | 能耗方程与四类机制族；Legacy PS/PS-Poll、U-APSD、SMPS、VHT TXOP PS 与 OM Control、802.11ah 的 TWT/RAW/TIM 分段、802.11ax TWT 与 trigger-enabled SP、802.11ba 唤醒无线电、802.11be r-TWT、802.11bn AP Power Save / DPS / 跨链路节能、802.11bp 环境供能——含逐代机制对比表、Mermaid 图、实现分层与失效模式 |
| **02-3** | WLAN 生态 | WFA 认证、EasyMesh、prplMesh/prplOS/prpl LCM |
| **02-4** | **WLAN 收发包流程与 offload** | 端到端发送路径（socket → qdisc/AQL → mac80211 填头/TID/SN/加密 → 描述符 → EDCA/A-MPDU → PHY）与接收路径（同步 → MPDU 定界符扫描 → FCS/地址过滤/解密 → 重排缓冲 → DMA/NAPI/GRO → TCP），含逐字节开销核算；五类 offload 平面（单包加速、FullMAC/SoftMAC/混合、AP 转发 offload 与 PPE/NSS/Runner/WED、内核旁路、控制面）；MLO 重排；节能与数据面交互；"症状 → 定位层"排查表 |
| **02-5** | **WLAN 发现、鉴权与关联** | 逐阶段拆解入网流程：被动/主动扫描与 6 GHz 发现（RNR、PSC、FILS Discovery、禁止通配 Probe）、MLME 三状态与原因码、Open System/Shared Key/SAE（Dragonfly、H2E、Dragonblood）/OWE/802.1X-EAP 对比、关联与 AID、PMK→PMK-R0/R1→PTK 密钥体系与四次握手逐报文、PMF 与 SA Query、FT 与 802.11k/v、FILS、MLO 多链路建立与 per-STA profile、hostapd/wpa_supplicant/mac80211 分工，以及"症状 → 阶段"排查表 |
| **02-6** | **WLAN 多 AP 漫游、自愈与引导** | 为什么 802.11 把漫游决策留给终端，以及网络侧能做什么：四种切换方式的代价对比（完整入网 / PMKSA 缓存 / FT / FILS）、802.11k 的 Neighbor Report 与 Beacon Report、一次端到端切换的逐帧时序、ESS 尺度的 FT（R0KH 部署位置、`0x890D` over-the-DS 转发帧、五类现网失效、切换后数据面要重建什么）、BTM / MBO / assoc control / EasyMesh 客户端引导的决策函数与乒乓问题、以回程状态机为核心的 mesh 自愈（拓扑修复与信道切换）、MLD 粒度的 MLO 引导，以及 Wi-Fi 8 的 SMD 与 MAPC |
| **02-7** | **Wi-Fi EasyMesh 原理、调优与排障** | EasyMesh 标准化了什么、刻意不标准化什么；规范版本 v1.0→v6.0 与 Profile-1/2/3；IEEE 1905.1 CMDU 与 TLV 机制（真实报文号 `0x893A`、`0x8003`、`0x8014`、`0x8019`、`0x9B`）；WPS/PBC 与 DPP 两条入网路径（`mapBackhaulSta`、`mapAgent`、CCE、代理封装）；AP-Autoconfiguration 的 M1/M2 与 Multi-AP IE（`0xDD`、OUI `50-6F-9A`、类型 `0x1B` 与扩展子元素的位定义）；四地址回程与 `multi_ap=1/2/3`；四类测量机制；信道选择、三种引导机制与回程优化；部署取舍；全部可调策略字段；以及分层排障方法论与症状对照表 |
| **02-8** | **Wi-Fi 调度** | 调度器在 AP 内的完整实现：帧间间隔族与 DCF 退避状态机、CCA 与 BSS Color 双 NAV、EDCA 四个接入类别及 802.11-2016 与 2012 两版 TXOP 限制的变迁与 DSSS 列、OFDMA 资源单元栅格与合法 MRU 组合、八种 Trigger 帧类型与一次完整的上行 OFDMA 回合、MU-MIMO 探测及其代价、Wi-Fi 7 跨链路调度（UMAC/LMAC 切分与 EMLSR 三个定时器）、空口时间公平与赤字轮询、每 TXOP 决策流水线、作为调度器一部分的速率控制、TWT 与 r-TWT 作为可调度状态、`mac80211` 中的 FQ-CoDel 与 AQL 及队列藏身的三处、KPI 体系与排障决策树 |
| **02-9** | **Wi-Fi TSN · 研究与实践** | 贯穿各代际的确定性主线：工业与沉浸式应用真正提出的四个数字（周期、时延界、可靠性、抖动），Wi-Fi 无法给出确定性上界的六个结构性原因，以及 802.1 工具箱逐项映射到 802.11 的结果。随后是阶梯：802.11e 的优先级、802.11v 的 Timing Measurement、802.11aa 的 SCS 与 AC 内队列、802.11mc 的 0.1 ns FTM、802.11ak 的中继链路、802.11ax 的触发式接入、802.11be 的 r-TWT（TID 位图与静默间隔），直到 802.11bn 被量化的 25% 目标。此外还有 TM/FTM 之上的 802.1AS 与软硬件时间戳的误差预算、五级接入阶梯、SCS 与四参数 QoS Characteristics 元素、MLO 之上的 802.1CB 以及冗余为何要付出空口代价、P-EDCA、NPCA、抢占与多 AP 协同、AP 作为网桥并与 Qbv 门控对齐的融合模型、证据强度的五层梳理、带时延预算算例的九步落地方法、症状排查表，；以及后续新增的第 11 节「融合」：为什么有线-无线 TSN 融合是趋势并给出每一步的带日期证据；一个 gPTP 时基如何跨四段跳变传递（AP 为 PTP Relay Instance、客户端为 End Instance）；以太网 peer-delay 机制与 802.11 TM/FTM 原生授时机制之间的媒体相关层切分；空口实测数字（从有线 52 ns 到商用 Wi-Fi 的 13 µs）；优先级如何穿越 802.11 Portal 并经历八→四的坍缩，以及「802.1Q 优先级 3 落到 Wi-Fi Best Effort」这个坑；为什么发送时刻归 AP 而不归客户端（mac80211 完全绕过 qdisc 层）；两端能力清单；以及六条仍未闭合的缺口 |
| **02-10** | **基带与驱动架构 · Wi-Fi 6/7/8** | 以高通为参考设计拆开无线电：基带里到底有什么、每一代究竟要哪一块电路长大；定义一切的两条边界；Wi-Fi 7 AP 与 Wi-Fi 8 终端的解剖；WCSS 与运行固件的 Q6 处理器；WMI/HTT/HTC/CE/QMI/MHI 协议栈与完整的 ring 清单；一张说明主机、固件、硬件各做什么的职责表；收发两条数据通路与描述符中真正关键的字段；中断组、NAPI 与 threaded NAPI 的实测收益；帧究竟在哪里排队，以及排错之后吞吐量与时延的实测权衡；MLO 在芯片里和驱动里分别是什么；功耗、散热与一次固件断言的真实代价；SoC 侧的 NSS 转发加速平面；从 ath9k、ath10k、ath11k 到 ath12k 及其双模块拆分的驱动演进；Wi-Fi 8 对每一层的诉求；架构正在走向的八个方向；十个面试答案；以及一张故障定位表 |
| **02-11** | **OpenWrt 与无线系统软件架构** | 把路由器当作软件系统来拆：OpenWrt 到底是什么（一个 Linux 发行版 + 交叉构建系统，对外是四件产物——源码树、ImageBuilder、SDK、软件仓库）；从意图到空口的五条边界；永远在跑的五个守护进程（procd、ubusd、rpcd、netifd、fw4）；把 `/etc/config/wireless` 变成 hostapd BSS 而不重启任何东西的 ucode 流水线；`wifi-device` / `wifi-iface` / `wifi-vlan` / `wifi-station` 的UCI 无线设备模型；hostapd 的 ubus 方法表以及为什么引导决策在用户态；netifd 的设备与接口状态机（含真实的事件名与状态名）；一个报文在盒子里怎么走、flow offload 与 WED 各自付出什么代价；固件、板级校准数据、MAC 地址与监管域这四样“不在源码里”的东西；含 apk 与 attended sysupgrade 的构建与升级体系；以及相邻模型的横向对比——TIP OpenWiFi（APNOS + uCentral + Cloud SDK 与设备 PKI）、OpenSync、prplOS 与 RDK-B、玩家分支、以及厂商 SDK——外加 OpenWrt One 参考硬件、六条诚实的局限、故障定位表和十个面试答案 |
| **02-12** | **openwifi · 开源 FPGA 802.11 平台** | 把驱动与空口之间那堵墙推倒：为什么需要一个 SDR 802.11 全栈（商用芯片不让你做的四件事）；Zynq + AD9361 平台与是否需要 Vivado 授权的开发板清单；三个仓库以及 Vivado、内核与镜像的构建流程；六个 FPGA IP 核及其逐文件构成；`xpu` 里的低 MAC——CSMA/CA 状态机，以及让 SIFS、时隙、ACK 超时、CCA、竞争窗口与重传次数都变成可写寄存器的那些寄存器；四个发送队列与按 MAC 地址的时隙切片；一个“硬件掌握时序”的 mac80211 驱动及其完整的 `ieee80211_ops` 清单；收发两条通路的逐步拆解；切分为何落在这一层；`sdrctl`（nl80211 testmode）与 sysfs 两条控制通道；各种工作模式与 802.11b 的坑；CSI / IQ / 感知类能力；公开性能数字及其受限原因；与商用芯片、GNU Radio 收发机、`mac80211_hwsim`、仿真器的对比；许可与资助；真实用例；故障定位表与十个面试答案 |
| **02-13** | **可靠性、低时延与确定性** | 一个时延或可靠性指标到底要付什么代价、由谁来付：三份契约以及它们为什么互相冲突；逐项拆解时延预算并指明每一项归哪一层；从应用一路到低 MAC 的调节杆分布图；MAC 重传的真实上限（短帧 7、长帧 4、MSDU 生存期 512 TU）以及为什么重传正是毁掉时延的东西；Minstrel 与它 26 ms 的重传链上限；用重复发送换取不以时延为代价的可靠性；含 802.11k/v/r 与 OKC 的漫游预算；从 EDCA 经 r-TWT 到抢占的四级阶梯；MLO 的 95 分位实测表与链路对称性警告；AQL 的 5000/12000/24000 常量与滞回状态机；带实测数字的公平排队与空口公平；TSQ 以及内核已经替你做出的3 ms 换 3 倍吞吐的取舍；L4S；一个「界」到底需要什么；诚实的能力边界表；跨技术对比；如何测量而不自欺；五套部署配方；故障定位表与十个面试答案 |
| **03-1** | WSN 与低功耗 MAC | 分簇路由、UAV 采集、TSCH、AoI |
| **04-1** | 嵌入式 RTOS | FreeRTOS、PendSV、I2C/SPI/UART/CAN、DMA、缓存一致性 |
| **04-2** | Linux 嵌入式开发 | 启动链、设备树、驱动、IPC、网络栈、虚拟化、PREEMPT_RT |
| **04-3** | 嵌入式软件架构 | 分层与 HAL/BSP 划分、执行模型（超级循环 / 时间触发 / RTOS / 主动对象）、调度理论、HSM 与事件驱动、设计模式、数据所有权与邮箱接口、无线协议栈切分（L1/L2 边界、CU/DU、O-RAN 7-2x）、内存与功耗架构、OTA 与回滚、ISO 26262 / IEC 61508 安全架构 |
| **04-4** | **Linux 中断** | 中断主题的完整展开（英文）：五个正交类型轴（同步/异步、可屏蔽/NMI 与 pseudo-NMI、电平/边沿、硬线 vs MSI-X、私有/共享/IPI）、三种中断控制器（ARM GICv2/v3/v4 含完整 INTID 映射与 ITS/LPI 模型、x86 IDT + LAPIC/IOAPIC/MSI、RISC-V PLIC 与 CLINT 对 AIA 的 APLIC/IMSIC）、通用中断层（`irq_desc`、`irq_chip`、`irq_domain`、五种流处理器、chained 与 nested 之别）、入口路径图、上半部清单（允许/禁止表）、四种下半部与十个固定 softirq 向量及 2 ms / 10 次重启的双重刹车、tasklet 的兴衰与 `WQ_BH`、SCHED_FIFO 优先级 50 的线程化中断、六个应用实例（NAPI、DMA 环形队列、GPIO 按键、IIO 触发、UIO/VFIO、rpmsg 门铃）、亲和性与隔离与合并的调优手段，以及症状到修法的排障表 |
| **04-5** | **并发：内核态与用户态、进程、线程与 IPC** | 并发主题的完整展开：x86 特权环、ARM 异常级与 RISC-V 模式下的特权边界及各自能触碰什么；五种内核执行上下文与"能否睡眠/被抢占/访问用户内存"矩阵；四种抢占模型与 `preempt_count`；进程模型（`task_struct`、TGID 与 TID、`clone` 标志表、写时复制及其在无 MMU 系统上的缺失、生命周期与 PID 1）；线程（NPTL 1:1 对 LinuxThreads 对 NGPT、共享与私有清单、栈大小、每线程信号掩码）；内核线程及其命名；基于原子与 futex 的 ITC，含私有/共享键、robust 与 PI 变体以及一个无锁环形队列算例；七轴 IPC 对比与决策树、共享内存 + 门铃模式与 `SCM_RIGHTS`、"万物皆 fd"的事件循环、一个多进程守护进程实例；以及并发缺陷分类与 TSan / `lockdep` / `perf sched` 工具链 |
| **04-6** | **设备驱动 · 模型、probe、数据通路、电源** | 面向嵌入式场景的驱动全景：驱动的五项职责与其所处的内核分层；字符/块/网络/IIO/hwmon 的选型；bus-device-driver-class 模型与 kobject、sysfs、uevent、devtmpfs；绑定流程与 `-EPROBE_DEFER`、`fw_devlink`；probe 的顺序约定与 `devm_*` 为何让 `remove()` 变空；一个生命周期状态机；字符设备完整 read 路径（`-ERESTARTSYS`、`O_NONBLOCK`）、ioctl 编码与 ABI、poll/fasync/mmap；中断驱动的数据通路与单次传输状态机；MMIO 与屏障；一致性/流式 DMA 与缓冲区归属状态机；使用真实 `rpm_status` 状态名的运行时 PM 与系统挂起回调顺序；platform 与 I2C/SPI/PCI 的驱动解剖及 regmap；框架选型树；加锁规则；内核到用户态接口决策；九步 bring-up 流程与十六行症状表；一份完整带注释的驱动；以及十个面试答案 |
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
| **09-1** | **工程项目管理** | 决定「哪些技术工作该做、按什么顺序做、用谁的时间做、什么时候停」的学科：项目、项目群、项目组合的区别，以及为什么把三者混为一谈是最常见的结构性错误；实证基础——Flyvbjerg 16,000 个项目中 47.9% 不超预算、8.5% 同时不超预算不超期、0.5% 连收益都达标，McKinsey 与牛津的研究为 45% 超预算、56% 价值打折，CHAOS 的规模效应，以及引用这些数字时必须同时说出的四条口径提醒；方法论族谱与「瀑布其实误读了 Royce」；由需求可变性、失效后果、认证要求和真正瓶颈推导方法选择的决策树；带门禁与显式「终止」分支的生命周期，覆盖 PMBOK 7、PRINCE2 Version 7、NASA 阶段与 KDP、Stage-Gate；WBS 与 100% 规则；从甘特图、CPM、PERT、关键链到蒙特卡洛，并给出一条算过的关键路径与 fever chart；把估算写成 P50/P80 的预测、参照类预测、以及从 1967 年 C/SCSC 到 2026 年 EIA-748-E 的挣值演进；ISO 31000 风险与 NASA 70% 联合置信度；V 模型的验证与确认；变更、基线与配置管理；决策权、单线程负责人与主查（chief engineer）模式；按例外管理、容差与无利益相关方评审的治理；工具栈与每一类工具的失效方式；项目管理计划包含什么，以及一份 Wi-Fi 7 多链路项目的完整样例（里程碑、缓冲、风险登记册）；丰田、亚马逊、Google、NASA、USDS 与 FBI Sentinel 反转的实践集，以及 Spotify 模型和 SAFe 里不该照搬的部分；Brooks 定律、100% 利用率、丹佛机场与 737 MAX 报告；利特尔法则与经得起推敲的度量；以及运行节奏与前 30 天清单 |

---

## 五、知识图谱使用说明

1. **打开方式**：在 Obsidian 中选择"打开本地仓库"，指向 `knowledge-graph/` 文件夹（而非项目根目录）。
2. **入口**：`00 MOC` 是唯一导航页，其余 40 篇均通过 `[[wikilink]]` 双向连通，可用 Graph View 查看关联密度。
3. **命名规则**：笔记按领域分组编号 `GG-x`——`00 MOC` 为索引，八个领域组从 `01` 起**连续编号**：`01-x` 移动通信、`02-x` WLAN、`03-x` 低功耗与传感组网、`04-x` 嵌入式与系统软件、`05-x` 数据面与异构算力、`06-x` AI 推理与智能体系统、`07-x` 芯片与指令集、`08-x` 编程语言与工程实践。组号顺序沿信号路径由内向外展开：从空口一直到芯片与语言底座。文件名即主题，便于按编号排序与按名检索。
4. **笔记结构**：知识点正文 → **Anchors（事实锚点）** → **Related（关联笔记）**，三段式固定。
5. **图示**：笔记使用 Mermaid 代码块，在 Obsidian 阅读视图中原生渲染。凡涉及结构的章节都配图——版本时间线、协议栈与数据通路、控制回路、决策树与状态机——全库共 378 个图块。
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
| Linux 下半部机制 | "tasklet 就是快速下半部" | tasklet 已**弃用**。API 在 5.9 前后完成现代化改造，替代者是 **WQ_BH**，于 **6.9** 合入（含 `system_bh_wq` 与 `system_bh_highpri_wq`），运行在 softirq 上下文、不可睡眠且要求 `max_active = 0`；tasklet API 仍在，转换工作尚未完成——见笔记 04-4 |
| 竞争解决失败后的功率爬坡 | "竞争失败的 UE 从 Msg1 重来且不爬坡" | 实际**会**爬坡。TS 38.321 第 5.1.3 节对 `PREAMBLE_POWER_RAMPING_COUNTER` 的递增只设四个条件——传输计数大于 1、SSB/CSI-RS 未变更、物理层未发出功率爬坡暂停通知、上一次传输无 LBT 失败——**没有为竞争解决失败开任何例外**。真正成立的是更窄的那条：换波束才不爬坡，与失败原因无关。这也否掉了一个常用捷径：碰撞与覆盖不足**无法靠功率列区分**——见笔记 01-5 §9.3 |

| OpenWrt 的定位 | “一个路由器固件” | 它是**一个 Linux 发行版 + 交叉构建系统**，对外是四件可下载的产物（源码树、ImageBuilder、SDK、软件仓库）。无线协议栈是一组各自独立版本化的 package（内核、`mac80211` 回移包、驱动、`wpad`、固件与板级数据），所以无线问题常常是它们之间的版本错配，而不是某一处的缺陷。另外 OpenWrt **不提供网络级无线策略**：引导、mesh 自愈与信道规划都要自己部署软件包——见笔记 02-11 |
| openwifi 的范围 | “开源 Wi-Fi 芯片” 或 “完整的现代 Wi-Fi 协议栈” | 它是 Zynq SoC 上**与 Linux mac80211 兼容的 802.11a/g/n SDR 实现**：PHY 与低 MAC 在 FPGA，高 MAC 在 mac80211。它只做 OFDM（不支持 802.11b）、20 MHz、MCS 0–7，实测 iperf TCP 40–50 Mbps；Wi-Fi 6、OFDMA、RFSoC 与 JCAS/ISAC 属于**订阅特性**而非开源部分。还要注意重名：TIP 的 OpenWiFi 是另一个项目——基于 OpenWrt 的云端管理 AP 架构——见笔记 02-12 |
| Wi-Fi 时延 | "几毫秒" | 空载是的。但在满载下载下，驱动或固件的深队列会把时延推到**数百毫秒**：FQ-CoDel 下慢站中位数仍在 200 ms 以上、快站约 35 ms，按站公平排队再给快站降约 45%。**负载下**的主导项是排队，**最坏情况**的主导项是信道接入——提高 PHY 速率对这两项都无效。见笔记 02-13 |
| MLO 时延 | "链路越多时延越低" | 只有在**各链路占用率相近**时成立。厂商实测显示 10/40/70% 负载下 STR 为 2/8/18 ms，而单链路为 30/70/150 ms（95 分位）；但若副链路明显更忙，STR 的最坏时延反而会高于单链路，而单射频的 EMLSR 在中高负载下对 p95 几乎没有改善。见笔记 02-13 |
| 「敏捷就是不做计划」·「加人来赶进度」 | 「敏捷用速度替代计划；人越多完成得越快」 | 两个说法都错，而且都可检验。敏捷提高的是计划的**频率**、缩短的是计划的**周期**——检视与调整是一个控制回路，不是没有控制回路。而 Brooks 定律说的是：给一个延期的项目加人只会更延期，因为新人需要培训、工作要重新切分、沟通路径按 n(n−1)/2 增长。实证比直觉更冷酷：Flyvbjerg 的 16,000 个项目里只有 8.5% 同时不超预算、不超期，Standish 的规模效应是小型项目 61% 成功、最大规模项目只有 6%——所以杠杆最大的动作是拆分工作、限制在制品，而不是加人。见笔记 09-1 |
| OpenAirInterface 许可 | "开源，Apache 或 GPL" | 三者都不是。OAI 的许可演进是 **GPL v2 → OAI Public License v1.1（2017）→ CSSL v1.0**，RAN 仓库于 **2026-03-27** 改许可，同期随 Duranta 项目并入 Linux Foundation Networking。CSSL 是 Apache 2.0 加一条 FRAND 专利条款，目的是让持有 3GPP 标准必要专利的公司也能贡献代码；它**不是 OSI 认证的许可**，商业使用按 FRAND 条款走。另需区分的是定位：OAI 是研究级软调制解调器——4 层下行 / 2 层上行、尚无量产 MU-MIMO、仅静态 TDD——不是运营商级 DU，见笔记 01-8 |
| NR HARQ 进程数 | "默认是 16" | 缺省是 **8**：`nrofHARQ-ProcessesForPDSCH` 缺省时 UE 按 8 个进程假设，16 是上限而非默认值。而且并非越多越好——每个进程都要占用软缓冲区，而 UE 的软缓冲总量是能力项不是配置项，只需要六个进程的小区配成 n16 反而会摊薄每次重传能拿到的合并增益——见笔记 01-6 §8.3 |
**更新触发点**

- 3GPP TSG 全会（每年 4 次）→ 更新 01-1/01-2/01-4
- 3GPP TS 38.321 / 38.331 新版发布与 RAN1/RAN2 关于随机接入的会议结论 → 更新 01-5（字段长度、计数器、窗口与参数取值都是随版本变化的；本文引用基线为 TS 38.321 v17.3.0，2023-01）
- IEEE 802.11 WG 与 WFA 认证公告 → 更新 02-1/02-2/02-3
- TGbn / TGbp 投票里程碑、WFA 功耗相关认证 → 更新 02-2（AP Power Save 仍为草案特性，P802.11bp 处于 D1.0 WG 投票）
- Linux kernel 主线与 LTS 发布 → 更新 08-1/04-2/04-4/04-5（本轮引用基线：PREEMPT_RT 于 6.12 合入、WQ_BH 于 6.9、EEVDF 于 6.6、clone3/pidfd_open 于 5.3、RISC-V AIA 驱动于 6.10）
- xLLM / Agent 框架的版本与论文 → 更新 06-1/06-2
- 主流框架大版本（scikit-learn、PyTorch、JAX）与教材新版 → 更新 06-3（本文引用基线为 scikit-learn 1.9.1 与 PyTorch 2.14.1，均为 2026 年 9 月）
- WG21 / WG14 会议与 GCC、Clang 大版本发布 → 更新 08-2
- CPython 特性版本发布（每年 10 月）与 PEP 采纳、NumPy 大版本 → 更新 08-3
- MATLAB / Simulink 发布（每年 3 月与 9 月）与 HDL / Embedded Coder 能力变化 → 更新 08-4
- IEEE 1800 修订与 IEEE 1800.2（UVM）修订 → 更新 08-5
- WFA Multi-AP / EasyMesh 规范修订与 prplMesh 版本发布 → 更新 02-7（当前为 v6.0，自 2024-12-31 起对新测 mesh 设备强制；报文号与 TLV 编号随版本增长）
- AUTOSAR 年度发布（每年 11 月）、MISRA 文档修订、Zephyr 半年发布与 LTS 分支 → 更新 04-3
- RISC-V International 批准与 AIA 文档修订、Arm GIC 规范更新 → 更新 04-4/07-1（引用基线：AIA v1.0 于 2023 年 6 月批准，文档修订 2025-03-12；APLIC/IMSIC 驱动于 Linux 6.10 合入）
- 主线工作队列与下半部转换（tasklet → WQ_BH 迁移）、调度器变更（EEVDF、sched_ext）与 rt-tests 发布 → 更新 04-4/04-5

---

## 八、维护者

Washington Ruan —— 通信软件 / 嵌入式软件 / 无线协议栈工程师与系统架构师；方向为 5G RAN L2、WLAN/WFA、IoT/WSN、嵌入式与 Linux、AI/ML、云边端协同与异构算力。

---

## 版权

Copyright (c) 2026 **Washington Ruan**. All rights reserved.

本仓库所有文档与笔记的著作权归 Washington Ruan 所有。未经书面许可，不得用于商业发布或二次分发。

---

© 2026 Washington Ruan. All rights reserved.
