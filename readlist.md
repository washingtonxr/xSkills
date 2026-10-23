---
title: Reading List — Comms × Heterogeneous Compute × AI
lang: en
category: reading-list
version: 1.15
last-updated: 2026-10-23
copyright: "Copyright (c) 2026 Washington Ruan. All rights reserved."
---

# Reading List

**Books, papers, standards and technical reports for the PersonalSkills knowledge base**

> This file supports the 32 notes in `knowledge-graph/`. Sections are numbered `GG-x` to match the  
> vault's domain groups:  
> `01-x` cellular and mobile communications — `01-1` 5G-Advanced and 6G Radio Access, `01-2` NR RAN L2,  
> `01-3` AI/ML for RAN and O-RAN RIC, `01-4` RedCap/eRedCap/NTN, `01-5` NR random access (RACH),  
> `01-6` NR DU MAC scheduler;  
> `02-x` WLAN — `02-1` Wi-Fi generations, `02-2` power saving, `02-3` WFA/EasyMesh/prpl ecosystem,  
> `02-4` packet TX/RX datapath and offload, `02-5` discovery, authentication and association,  
> `02-6` multi-AP roaming, healing and steering, `02-7` EasyMesh operation, tuning and troubleshooting,  
> `02-8` Wi-Fi scheduling — channel access, EDCA, OFDMA allocation and airtime;  
> `03-x` low-power and sensor networking — `03-1` WSN and low-power MAC;  
> `04-x` embedded and systems software — `04-1` RTOS and hardware interfaces, `04-2` Linux embedded, `04-3` software architecture,
> `04-4` Linux interrupts, `04-5` concurrency, processes, threads and IPC;  
> `05-x` data plane and heterogeneous compute — `05-1` DPDK/UPF, `05-2` cloud-edge-end;  
> `06-x` machine learning, AI inference and agent systems — `06-1` LLM inference, `06-2` agent systems,  
> `06-3` machine learning foundations;  
> `07-x` silicon and ISA — `07-1` RISC-V;  
> `08-x` programming languages — `08-1` toolchain and performance, `08-2` C and C++, `08-3` Python,  
> `08-4` MATLAB and Simulink, `08-5` Verilog HDL.  
> Sections `30`–`32` collect primary standards repositories, a reading order, and maintenance notes.
>
> This file lives at the project root, not inside the Obsidian vault, so it refers to notes by number  
> rather than by `[[wikilink]]`.

## How to read this file

- **Titles are kept in their original published form.** Chinese editions keep the Chinese title and `《》` brackets; English editions keep the English title. Titles are never translated.
- **All descriptions are written in English**, including descriptions of Chinese-language works.
- Entries are tagged by type: **[Book]** · **[Paper]** · **[Standard]** · **[Spec]** · **[Doc]** · **[Code]**.
- Priority marks: **★★★** read or at least skim before an interview · **★★** read for depth in your chosen track · **★** lookup reference, read on demand.
- Language marks: **[EN]** English · **[CN]** Chinese · **[EN/CN]** both editions available.

---

## 01-1 · 5G-Advanced and 6G Radio Access

### Books

- **[Book · EN/CN · ★★★]** *5G NR: The Next Generation Wireless Access Technology* — Erik Dahlman, Stefan Parkvall, Johan Sköld · Academic Press; 1st ed. 2018 (ISBN 9780128143230), 2nd ed. 2021 (ISBN 9780128223208)
  - Written by the Ericsson delegates who actually designed NR, so every mechanism is explained with the *reason* it was standardised, not just the result. The single best book for moving from "I know the parameter" to "I know why the parameter has this value". Chapters 13 (retransmission) and 14 (scheduling) are the L2 core.
- **[Book · CN · ★★★]** 《5G NR标准:下一代无线通信技术》 — [Sweden] Erik Dahlman, Stefan Parkvall, Johan Sköld; translated by 朱怀松, 王剑, 刘阳 · 机械工业出版社, 2019 · ISBN 9787111624745
  - Chinese translation of the first English edition. Widely used as the onboarding text in Chinese 5G R\&D teams; useful when you need to quote standard terminology in Chinese and match it to the English term.
- **[Book · CN · ★★★]** 《5G-ADVANCED NR增强标准:下一代无线通信技术(原书第3版)》 — Erik Dahlman, Stefan Parkvall, Johan Sköld · 机械工业出版社
  - Chinese translation of the third edition. Adds the Rel-17/Rel-18 material that matters for a 5G-Advanced interview: spectrum above 52.6 GHz, network-controlled repeaters, RedCap, sidelink enhancements, positioning, MIMO evolution, **non-terrestrial networks (NTN)**, broadcast/multicast, duplex evolution, and 3GPP's AI/ML study. New chapters cover NR reduced-capability IoT, NR multicast/broadcast, and the NTN air-interface changes.
- **[Book · EN · ★★]** *NR: The New 5G Radio Access Technology* — Ali Zaidi, Fredrik Athley, Jonas Medbo, Ulf Gustavsson, Giuseppe Durisi, Xiaoming Chen · Academic Press, 2018
  - A more academic, signal-processing-flavoured treatment than Dahlman. Strongest on the numerology, channel modelling, beam management and the mmWave/above-6 GHz RF reality. Good complement when Dahlman's system view leaves you short on physical-layer depth.
- **[Book · EN · ★]** *5G NR: Architecture, Technology, Implementation, and Operation of 3GPP New Radio Standards* — edited by Sassan Ahmadi · Academic Press, 2019
  - Broad implementation-oriented reference spanning L1 through RRC and the procedures. Best used as a lookup when you need the exact parameterisation of a procedure rather than a narrative.
- **[Book · EN · ★]** *6G Wireless: The Communication Paradigm Beyond 2030* — edited by Faisal Tariq, Muhammad Khandaker, Imran Shafique Ansari · CRC Press, 2025 · ISBN 9781032252353
  - Tutorial-style edited volume covering IRS/RIS, UAV and aerial computing, THz, NOMA and RSMA, plus 6G security and blockchain-oriented IoT. Use it for breadth on the candidate-technology landscape; it is not a substitute for the 3GPP study items.

- **[Book · EN · ★]** *LTE — The UMTS Long Term Evolution: From Theory to Practice*, 2nd ed. — Stefania Sesia, Issam Toufik, Matthew Baker · Wiley, 2011
  - Still the clearest exposition of the L2 architecture (MAC/RLC/PDCP), HARQ and scheduling that NR inherited. Read selectively for those chapters; NR changed the details, not the shape of the problems.

### Papers

- **[Paper · EN · ★★★]** "What Should 6G Be?" — H. Ning et al. · *Nature Electronics*, vol. 6, pp. 566–574, 2023
  - Short, high-signal framing of the 6G debate: what actually differentiates 6G from 5G-A versus what is marketing. Ideal for the "why is 6G needed" opening question.
- **[Paper · EN · ★★]** "A Vision of 6G Wireless Systems: Applications, Trends, Technologies, and Open Research Problems" — M. Z. Chowdhury, M. Shahjalal, S. Ahmed, Y. M. Jang · *IEEE Network*, vol. 34, no. 3, pp. 134–142, 2020
  - Systematic mapping of 6G use cases to enabling technologies, with the KPI table most 6G surveys reuse. Good for producing a requirements-to-technology chain on demand.



- **[Paper · EN · ★★]** "End-to-End Learning for OFDM: From Neural Receivers to Pilotless Communication" — F. Aoudia, J. Hoydis · *IEEE Transactions on Wireless Communications*, vol. 21, no. 4, pp. 2759–2773, 2022
  - The canonical reference for the AI-native air interface argument. Shows a learned receiver beating a hand-designed one, and pushes to the endpoint where pilots are removed entirely. This is the paper to cite when the conversation reaches "is AI in the PHY real or hype".
- **[Paper · EN · ★]** "Toward Massive, Ultra-Reliable, and Low-Latency Wireless Communication with Short Packets" — G. Durisi, T. Koch, P. Popovski · *Proceedings of the IEEE*, vol. 104, no. 9, pp. 1746–1766, 2016
  - Establishes why the classical Shannon capacity framing breaks down for URLLC short packets. The information-theoretic grounding behind finite-blocklength arguments.

### Standards and reports

- **[Standard · ★★★]** **ITU-R Recommendation M.2160-0** (11/2023) — "Framework and overall objectives of the future development of IMT for 2030 and beyond"
  - The IMT-2030 framework: the usage scenarios, the 15 capability dimensions and the target values. This is the document 3GPP Rel-21 is written to satisfy, and the reason TR 22.870 exists.
- **[Spec · ★★★]** **3GPP TR 22.870** — "Study on 6G Use Cases and Service Requirements" (approved in Rel-20)
  - The Stage-1 anchor for Rel-21. Quote from here when asked what 6G is *for*.
- **[Spec · ★★★]** **3GPP TR 38.914** — "Study on 6G Scenarios and Requirements" (TSG RAN approval scheduled June 2026)
  - The RAN-side counterpart to TR 22.870. Track its approval; it is what converts 6G from aspiration to a parameterised design target.
- **[Spec · ★★]** **3GPP TR 21.921** — Release 21 description document (published at the end of the release)
  - Becomes the authoritative "what is in Rel-21" summary once the release closes. Until then, use the four freeze milestones recorded in note 01-1.
- **[Standard · ★★]** **3GPP TS 38.300** — "NR; Overall description" (Stage-2)
  - The entry point to the whole NR specification set. Read §9 (protocol architecture) and the L2 sections before any deeper TS.
- **[Standard · ★★]** **3GPP TS 38.211 / 38.212 / 38.213 / 38.214** — Physical channels and modulation; multiplexing and channel coding; physical layer procedures for control; physical layer procedures for data
  - The L1 core. Use as lookup, not as reading.

---

## 01-2 · 5G NR RAN Layer 2 Protocol Stack

### Books

- **[Book · EN/CN · ★★★]** *5G NR: The Next Generation Wireless Access Technology* (see §01-1) — chapters 6 (radio-interface architecture), 13 (retransmission protocols), 14 (scheduling)
  - The most efficient path to L2 competence. Chapter 14 in particular covers the interaction between BSR, grant, HARQ and QoS enforcement that most candidates hand-wave.
- **[Book · EN · ★★]** *5G NR: Architecture, Technology, Implementation, and Operation of 3GPP New Radio Standards* (see §01-1)
  - Chapter-level detail on MAC/RLC/PDCP/SDAP procedures and RRC states. Complements Dahlman with a more specification-structured layout.
- **[Book · EN · ★]** *LTE — The UMTS Long Term Evolution* (see §01-1)
  - For the inherited parts of L2 — RLC modes, PDCP, status reporting — LTE still has the clearest explanations, and NR's deviations are easier to see against that baseline.

### Papers

- **[Paper · EN · ★★]** "A Survey on Low Latency Towards 5G: RAN, Core Network and Caching Solutions" — I. Parvez, A. Rahmati, I. Guvenc, A. I. Sarwat, H. Dai · *IEEE Communications Surveys & Tutorials*, vol. 20, no. 4, pp. 3098–3129, 2018
  - Maps every latency contributor across the RAN and core. The reference for decomposing a 1 ms or 5 ms budget into per-stage terms, which is exactly what a URLLC question asks you to do.
- **[Paper · EN · ★]** "Toward Massive, Ultra-Reliable, and Low-Latency Wireless Communication with Short Packets" (see §01-1)
  - Use it to justify why HARQ retransmission is not always the right answer for latency-bounded traffic.

### Standards

- **[Spec · ★★★]** **3GPP TS 38.321** — MAC protocol specification
  - The normative source for LCID mapping, MAC CE formats (BSR, PHR, configured grant confirmation), DRX, random access and HARQ operation. Cite clause numbers here, not blog posts.
- **[Spec · ★★★]** **3GPP TS 38.322** — RLC protocol specification
  - TM/UM/AM modes, sequence numbering, polling and status reporting, re-segmentation. Read alongside 38.321 to understand which retransmission layer is doing the work.
- **[Spec · ★★★]** **3GPP TS 38.323** — PDCP specification; **3GPP TS 37.324** — SDAP specification
  - PDCP handles ciphering, integrity, reordering, duplication and header compression; SDAP is the thin QoS-flow-to-DRB mapping layer. Note that SDAP lives in the 37 series, not 38 — a small detail many candidates get wrong.
- **[Spec · ★★★]** **3GPP TS 38.331** — RRC protocol specification
  - RRC states, configuration, measurement reporting, mobility and the IEs that carry L2 configuration. Where "the network tells the UE how to behave" is actually written down.
- **[Spec · ★★]** **3GPP TS 23.501** — System architecture for the 5G System (Stage-2); **TS 23.503** — Policy and charging control framework
  - Needed for the QoS flow / QFI / 5QI model that L2 must enforce. Read §5.7 of 23.501 for the QoS architecture.




## 01-4 · Cellular IoT — RedCap, eRedCap and NTN

### Papers

- **[Paper · EN · ★★★]** "Resource Management for Reduced Capability New Radio Devices in Beyond 5G Networks: Opportunities and Research Road Map" — N. S. Ferdous, M. Z. Hassan, I. Ahmed, L. Akter · *IEEE Xplore* document 10757145
  - The best single overview of RedCap: what was reduced (bandwidth, MIMO layers, baseband complexity, DL modulation order, RF cost), the three use-case families (industrial sensors, wearables, video surveillance), and the coexistence problem with legacy NR. Covers coverage, capacity and energy-efficiency solutions plus a research roadmap.
- **[Paper · EN · ★★]** "Positioning of RedCap Devices in 5G Networks" — F. Munier, Z. Xiong, R. Shreevastav, X. Jiang, Y. Lyazidi, D. Shrestha, C. Zhang, G. Lindmark, J. Nygren, S. Moloudi, S. Dwivedi, F. Gunnarsson · *IEEE Communications Magazine*, vol. 62, no. 8, pp. 110–116, 2024 · DOI 10.1109/MCOM.001.2300802
  - Ericsson-authored account of the Rel-18 positioning enhancement for RedCap — extending effective bandwidth by frequency hopping — with 3GPP channel-model simulation results. Concrete and recent.
- **[Paper · EN · ★]** "Age of Information: An Introduction and Survey" (see §03-1)
  - Useful here because RedCap/eRedCap deployment targets are mostly status-update systems, where AoI is the more honest metric than throughput.

### Books

- **[Book · EN/CN · ★★★]** *5G-ADVANCED NR增强标准:下一代无线通信技术(原书第3版)* (see §01-1)
  - Contains the RedCap and NTN chapters in Chinese, including the NTN air-interface changes: uplink/downlink timing relations and HARQ enhancements.

### Standards

- **[Spec · ★★★]** **3GPP TR 38.865** — Study on further reduced capability NR devices (Rel-18)
  - The study that produced eRedCap. Standardised in **Release 18, frozen June 2024** (RAN#104) — not Rel-19, a correction recorded in note 01-4.
- **[Spec · ★★★]** **3GPP TR 38.821** — "Solutions for NR to support non-terrestrial networks (NTN)" (Rel-16) · **3GPP TR 38.811** — "Study on New Radio to support non-terrestrial networks" (Rel-15)
  - The NTN foundation: propagation delay, Doppler, moving cells, and the timing/HARQ adaptations required. Read 38.821 first.
- **[Spec · ★★]** **3GPP TS 38.306** — UE radio access capabilities
  - Where RedCap/eRedCap capability signalling and bandwidth reduction are actually defined.
- **[Spec · ★★]** **3GPP TS 38.331** (see §01-2)
  - Carries the NTN system information and the RedCap access control mechanisms.

---

## 01-5 · NR Random Access — UE RACH Procedure, Signalling and Tuning

### Standards

- **[Standard · ★★★]** 3GPP. *TS 38.321 — Medium Access Control (MAC) protocol specification*, v17.3.0 (ETSI TS 138 321 V17.3.0, 2023-01). <https://www.etsi.org/deliver/etsi_TS/138300_138399/138321/17.03.00_60/ts_138321v170300p.pdf>
  - The normative text for this note: clause 5.1 (random access), 5.1.1b–5.1.1d (feature-based resource partitioning), 6.2.3 and 6.2.3a (MAC RAR, fallbackRAR, successRAR), 7.2 (Backoff Parameter values), 7.3 (DELTA_PREAMBLE), 7.4 (PRACH Mask Index). Read the clause 5.1 state machine once end to end before reading anything else about RACH.
- **[Standard · ★★★]** 3GPP. *TS 38.321 — Medium Access Control (MAC) protocol specification*, v17.14.0 (ETSI TS 138 321 V17.14.0, 2025-10). <https://www.etsi.org/deliver/etsi_ts/138300_138399/138321/17.14.00_60/ts_138321v171400p.pdf>
  - The same clause 5.1 in a later release, and the version to check against before quoting a counter rule. It settles the two facts this note had to correct: the four conditions under which `PREAMBLE_POWER_RAMPING_COUNTER` is incremented (5.1.3 — attempt counter above one, SSB/CSI-RS unchanged, no power-ramping-suspension notification from lower layers, no LBT failure), and the restart of `ra-ContentionResolutionTimer` at each Msg3 HARQ retransmission (5.1.5). Clause 6.1.5 carries the RAR MAC PDU ordering rule (BI first, padding last), and the NOTE in 5.1.4 is the one that leaves UE behaviour undefined when the Msg3 grant size changes within a procedure.
- **[Standard · ★★★]** 3GPP. *TS 38.211 — Physical channels and modulation*. <https://www.etsi.org/deliver/etsi_TS/138200_138299/138211/>
  - PRACH in clause 6.3.3: the preamble format tables (6.3.3.1-1 and 6.3.3.1-2), sequence generation, and the three time-domain configuration tables 6.3.3.2-2 (FR1 FDD/SUL), 6.3.3.2-3 (FR1 TDD) and 6.3.3.2-4 (FR2).
- **[Standard · ★★★]** 3GPP. *TS 38.213 — Physical layer procedures for control*. <https://www.etsi.org/deliver/etsi_TS/138200_138299/138213/>
  - Clause 4.2 (timing advance), clause 8 (the physical-layer random access procedure, Msg3 PUSCH scheduling), clause 8.1 (SSB-to-PRACH-occasion association).
- **[Standard · ★★]** 3GPP. *TS 38.331 — Radio Resource Control (RRC) protocol specification*. <https://www.etsi.org/deliver/etsi_TS/138300_138399/138331/>
  - `RACH-ConfigCommon`, `RACH-ConfigGeneric`, `RACH-ConfigDedicated`, `BeamFailureRecoveryConfig`, `RA-Prioritization`, `RRCSetupRequest`, `RRCResumeRequest(1)`, `UE-TimersAndConstants`. Every parameter range quoted in the note comes from here.
- **[Standard · ★★]** 3GPP. *TS 38.300 — NR; Overall description; Stage 2*. <https://www.etsi.org/deliver/etsi_TS/138300_138399/138300/>
  - Clause 9.2.6 is the list of events that initiate random access, and clause 16 is the NTN material. Read 9.2.6 to get the trigger-to-RRC-consequence mapping right.
- **[Standard · ★★]** 3GPP. *TS 38.214 — Physical layer procedures for data*. <https://www.etsi.org/deliver/etsi_TS/138200_138299/138214/>
  - Table 6.1.2.1.1-5 for the numerology-dependent Msg3 delay Δ, plus the default `k2` allocation tables.
- **[Standard · ★]** 3GPP. *TS 38.101-1 / -2 / -3 — User Equipment radio transmission and reception*. <https://www.etsi.org/deliver/etsi_TS/138100_138199/13810101/>
  - `P_CMAX,f,c`, the ceiling in the open-loop PRACH power formula. Only needed to check the arithmetic in a power-ramping calculation.

### Books

- **[Book · ★★★]** *5G NR: The Next Generation Wireless Access Technology* — Erik Dahlman, Stefan Parkvall and Johan Sköld, Academic Press, 2018. ISBN 978-0-12-814323-0 (print), 978-0-12-814324-7 (e-book)
  - Chapter 16 "Initial access" is the best narrative account of why NR random access looks the way it does, and chapter 15 "Uplink power and timing control" is the background for the open-loop formula and the TA loop. Read these two chapters before arguing about any RACH parameter.
- **[Book · ★]** *5G NR and Beyond* or any later Dahlman/Parkvall/Sköld volume covering Rel-16 and Rel-17
  - Only if you need the 2-step RACH and SDT material in book form; the specifications and the 3GPP work-item documents are more reliable for those.

### Specifications-in-progress and work items

- **[Doc · ★★★]** 3GPP. *RP-200085 — Revised WID on 2-step RACH for NR*. <https://portal.3gpp.org/>
  - The Rel-16 work item that introduced MsgA/MsgB. Two pages, and it states exactly what problem 2-step was meant to solve (latency and, in unlicensed spectrum, the number of channel-access attempts).
- **[Doc · ★★]** i TecSpec. *TR 21.916 §19.1.2 — 2-step RACH for NR*. <https://itecspec.com/3gpp/21.916/s/19.1.2>
  - The Rel-16 feature summary: MsgA composition, shared versus separate PRACH occasions, preamble-to-PUSCH-occasion mapping, and the fallback indication.
- **[Doc · ★★]** Nokia, Nokia Shanghai Bell. *Introduction of SDT — Stage-2 running CR* (RAN2 #116-e, Rel-17). <https://www.3gpp.org/ftp/Email_Discussions/RAN2/%5BRAN2%23116-e%5D/>
  - The RAN2 agreements in their own words: 2-step and 4-step RA-SDT, CFRA not supported for RA-SDT, switching from SDT to non-SDT, and the events that terminate an SDT session.
- **[Doc · ★★]** Thales. *NTN Stage 2 CR* (RAN2 #117-e). <https://www.3gpp.org/FTP/Email_Discussions/RAN2/%5BRAN2%23117-e%5D/>
  - The Rel-17 NTN timing-advance formula with common TA and UE self-estimated TA, plus the K_offset and K_mac timing relationships that make Msg3 and BFR scheduling causal.
- **[Doc · ★]** i TecSpec. *TR 38.822 §6.1.4 — NR_NTN_solutions*. <https://itecspec.com/3gpp/38.822/s/6.1.4>
  - The L1 feature list for NTN, including `uplinkPreCompensation-r17` and the mandatory GNSS-based TA and frequency pre-compensation.


### Implementation references and worked examples

- **[Doc · ★★★]** lte5ghub. *Random Access (4-step & 2-step) in 5G NR*. <https://lte5ghub.com/random-access>
  - The trigger-to-RRC-consequence table, the RA-RNTI worked example, the shared MsgA/preamble budget pitfall, the spatial-filter ramping rule, and a log-reading checklist that is directly usable in the field.
- **[Doc · ★★★]** NR Explained. *Random access: PUSCH scheduled by RAR UL grant (Msg3)*. <https://www.nrexplained.com/ra_msg3>
  - The 27-bit RAR UL grant field by field, the default `k2` table, the Δ table, and the minimum RAR-to-Msg3 processing time. The clearest single page on Msg3 scheduling.
- **[Doc · ★★]** ShareTechnote. *5G/NR — Random Access Procedure (Msg1–Msg4)*. <https://sharetechnote.com/html/5G/5G_RACH_old1.html>
  - A real Amarisoft log with the `k2 + Δ` arithmetic visible in the SFN timestamps, plus the Msg4 HARQ-ACK behaviour.
- **[Doc · ★★]** CafeTele. *The 5G NR Random Access Procedure — PRACH, Msg1–Msg4, 2-Step RACH, Counters & Optimization*. <https://www.cafetele.com/articles/article-5g-nr-random-access-rach.html>
  - The two contention-resolution mechanisms stated plainly, the backoff valve, and the MsgA/MsgB fallback story.
- **[Doc · ★★]** MathWorks. *5G NR PRACH Configuration* (`nrPRACHConfig`). <https://uk.mathworks.com/help/releases/R2022a/5g/ug/5g-nr-prach-configuration.html>
  - Which configuration table applies to which frequency range and duplex mode. Useful for reproducing the format tables and for checking a `prach-ConfigurationIndex` without opening the PDF.
- **[Doc · ★]** Howl Testuff Works. *5G NR: 2-Step Random Access Procedure (Release-16)*. <http://howltestuffworks.blogspot.com/2020/04/5g-nr-2-step-random-access-procedure.html>
  - The successRAR and fallbackRAR field lists and the MsgA PUSCH-to-PRACH symbol gap by numerology. Secondary — cross-check field sizes against TS 38.321.
- **[Doc · ★]** i TecSpec. *TS 38.331 §RRCSetupRequest*. <https://itecspec.com/3gpp/38.331/s/rrcsetuprequest>
  - The exact `InitialUE-Identity` and `EstablishmentCause` enumerations, when you need to quote them rather than paraphrase.

### Practitioner and operator material

- **[Doc · ★★]** 3GPP. *Small Data Transmission (SDT)*. <https://www.3gpp.org/technologies/sdt>
  - The official one-page description of RA-SDT and CG-SDT, including the separation of SDT and non-SDT random-access resources.
- **[Doc · ★★]** ShareTechnote. *NTN — Random Access*. <https://www.sharetechnote.com/html/NTN/NTN_RACH.html>
  - Which TR 38.821 candidate solutions survived into Rel-17 and which disappeared once GNSS-based pre-compensation was made mandatory, plus an NTN RACH symptom table.
- **[Doc · ★★]** NTT DOCOMO Technical Journal, Vol. 24 No. 3. *Special Articles on 3GPP Release 17 Standardization Activities*. <https://dcm-dpweb51.tz.nttdocomo.co.jp/english/corporate/technology/rd/technical_journal/bn/vol24_3/005.html>
  - K_offset, the HARQ enhancement, and the NTN mobility triggers, explained from an operator's point of view.
- **[Doc · ★]** lte5ghub. *TS 38.331: RRC States (Idle / Inactive / Connected)*. <https://lte5ghub.com/rrc-states>
  - Why a completed random access no longer implies a state transition once SDT is enabled — the KPI trap worth knowing before you read a drive-test report.

## 02-1 · WLAN — Wi-Fi Generations Evolution

### Books

- **[Book · EN · ★★★]** *802.11 Wireless Networks: The Definitive Guide*, 2nd ed. — Matthew Gast · O'Reilly, 2005
  - Still the clearest explanation of the 802.11 MAC: DCF/PCF, CSMA/CA, the interframe spaces, NAV, RTS/CTS, fragmentation, power save and the management/frame taxonomy. Wi-Fi 4 through 8 all build on this substrate, and candidates who cannot explain the IFS/NAV mechanics cannot explain what OFDMA changed.
- **[Book · EN · ★★]** *Next Generation Wireless LANs: 802.11n and 802.11ac*, 2nd ed. — Eldad Perahia, Robert Stacey · Cambridge University Press, 2013
  - The authoritative treatment of MIMO, channel bonding, beamforming sounding and the 802.11n/ac PHY. Read for the design rationale behind features now treated as table stakes.

### Papers

- **[Paper · EN · ★★★]** "Wi-Fi: Twenty-Five Years and Counting" — G. Geraci, F. Meneghello, F. Wilhelmi, D. López-Pérez, I. Val, L. Galati Giordano, C. Cordeiro, M. Ghosh, E. Knightly, B. Bellalta · *Proceedings of the IEEE*, vol. 113, no. 11, pp. 1290–1336, 2025 · arXiv:2507.09613
  - The first single tutorial to span 802.11b through 802.11bn, organised by *mechanism* rather than by generation: spectrum, PHY, MAC, multi-user, power save, multi-band aggregation, multi-AP coordination. The best long read for understanding why each generation looks the way it does, and the appendix covers what comes beyond 802.11bn (mmWave, sensing, AI/ML, security).
- **[Paper · EN · ★★★]** "A Tutorial on Wi-Fi 8: The Journey to Ultra High Reliability" — A. Karamyshev, I. Levitsky, D. Bankov, E. Khorov · *Problems of Information Transmission*, vol. 61, no. 2, pp. 164–210, 2025 · DOI 10.1134/S003294602502005X
  - Feature-by-feature treatment of 802.11bn: distributed-tone resource units, unequal modulation, prioritised and non-primary channel access, advanced roaming, and multi-AP coordination, with explicit targets (throughput across SINR levels, 95th-percentile latency, packet loss, power). The primary reference behind note 02-1's Wi-Fi 8 section.
- **[Paper · EN · ★★★]** "A Tutorial on IEEE 802.11ax High Efficiency WLANs" — E. Khorov, A. Kiryanov, A. Lyakhov, G. Bianchi · *IEEE Communications Surveys & Tutorials*, vol. 21, no. 1, pp. 197–216, 2019
  - The Wi-Fi 6 PHY and MAC reset in full detail: OFDMA resource units, the new numerology, trigger-based uplink, BSS colour, spatial reuse and TWT. Everything in Wi-Fi 7 and 8 sits on top of this.
- **[Paper · EN · ★★]** "IEEE 802.11be: Wi-Fi 7 Strikes Back" — A. Garcia-Rodriguez, D. López-Pérez, L. Galati-Giordano, G. Geraci · *IEEE Communications Magazine*, vol. 59, no. 4, pp. 102–108, 2021
  - Short, current-status digest of 802.11be EHT features, arguing multi-AP coordination is mandatory for latency-critical traffic. Includes coordinated beamforming results showing near-tenfold worst-case delay reduction.
- **[Paper · EN · ★★]** "IEEE 802.11be Extremely High Throughput: The Next Generation of Wi-Fi Technology Beyond 802.11ax" — D. López-Pérez, A. Garcia-Rodriguez, L. Galati-Giordano, M. Kasslin, K. Doppler · *IEEE Communications Magazine*, vol. 57, no. 9, pp. 113–119, 2019
  - The early feature-level overview of 802.11be, written while the amendment was still being shaped. Useful for seeing which features survived to the standard.
- **[Paper · EN · ★★]** "IEEE 802.11ax: High-Efficiency WLANs" — B. Bellalta · *IEEE Wireless Communications*, vol. 23, no. 1, pp. 38–46, 2016
  - Written during 802.11ax development; explains why dense deployments forced a fundamentally different approach from rate maximisation.
- **[Paper · EN · ★★]** "What Will Wi-Fi 8 Be? A Primer on IEEE 802.11bn Ultra High Reliability" — L. Galati-Giordano, G. Geraci, M. Carrascosa, B. Bellalta · *IEEE Communications Magazine*, vol. 62, no. 8, pp. 126–132, 2024
  - The clearest short introduction to the reliability pivot: why UHR replaced throughput as the headline goal, and how multi-AP coordination extends Wi-Fi 7's multi-link operation.
- **[Paper · EN · ★]** "Future Directions for Wi-Fi 8 and Beyond" — E. Reshef, C. Cordeiro · *IEEE Communications Magazine*, vol. 60, no. 10, pp. 50–55, 2022
  - Pre-802.11bn view of the market drivers and candidate directions that became the UHR brief.
- **[Paper · EN · ★]** "Towards Wi-Fi 9: Vision, Requirements and Candidate Technologies"
  - The WNG Standing Committee contributions on post-802.11bn direction: determinism over nominal rate, uplink asymmetry driven by AI workloads, AI-native PHY, deterministic MAC, Age-of-Information scheduling, and the LAN-controller-plus-APs AI architecture. Cited in note 02-1; verify the current citation before quoting.

### Standards

- **[Standard · ★★★]** **IEEE Std 802.11-2020/-2024** — Wireless LAN MAC and PHY base standard (with consolidated amendments)
  - The base document. Every amendment is a delta against this.
- **[Standard · ★★★]** **IEEE Std 802.11be-2024** — Enhancements for Extremely High Throughput (EHT), i.e. Wi-Fi 7
  - 320 MHz, 4096-QAM, MRU, puncturing and multi-link operation, in normative form.
- **[Standard · ★★★]** **IEEE P802.11bn** (TGbn) — Ultra High Reliability (UHR), i.e. Wi-Fi 8, draft
  - Track the task group's scope, objectives and ballot milestones directly; the draft is the only authoritative source for what is in and what has been cut.
- **[Standard · ★]** **IEEE Std 802.11ax-2021** (Wi-Fi 6) · **IEEE Std 802.11ac-2013** (Wi-Fi 5) · **IEEE Std 802.11n-2009** (Wi-Fi 4)
  - Amendment texts for generational comparison at parameter level.
- **[Standard · ★]** **IEEE Std 802.11bf-2025** — WLAN Sensing
  - Relevant to the ISAC/sensing convergence discussed in note 02-1's future-generation section.
- **[Doc · ★★]** **IEEE 802.11 Working Group timelines and TGbn status pages**
  - The source for ballot and approval dates. Use these rather than secondary reporting when a date matters.

---

## 02-2 · WLAN — Power Saving Mechanisms and Evolution

Supports note `02-2 WLAN - Power Saving Mechanisms and Evolution`. Where an item duplicates a reference already listed under **§02-1**, it is cross-referenced rather than repeated, with the specific part to read.

### Books

- **[Book · EN · ★★★]** *802.11 Wireless Networks: The Definitive Guide*, 2nd ed. — Matthew Gast · O'Reilly, 2005
  - The power-management chapters are still the clearest plain-English account of the PM bit, TIM/DTIM, PS-Poll and the beacon-synchronised model that every later mechanism is a reaction against. Read this before any paper on TWT, or the motivation will not land.
- **[Book · EN · ★★]** *Next Generation Wireless LANs: 802.11n and 802.11ac*, 2nd ed. — Eldad Perahia, Robert Stacey · Cambridge University Press, 2013
  - Listed in §02-1; for this note use its treatment of SMPS, operating-mode feedback and the power cost of MIMO chains.
- **[Book · CN · ★]** 《802.11无线网络权威指南（第2版）》 — Matthew Gast · O'Reilly 中文版
  - Chinese edition of the Gast volume above, for the power-management and MAC chapters. `VERIFY` ISBN and edition year before citing.


### Papers

- **[Paper · EN · ★★★]** "A Primer on AP Power Save in Wi-Fi 8: Overview, Analysis, and Open Challenges" — R. Sanchez-Vital, A. Belogaev, C. Gomez, J. Famaey, E. Garcia-Villegas · *IEEE Wireless Communications*, 2025 · DOI 10.1109/MCOM.004.2400486 · preprint arXiv:2411.17424
  - The definitive reference for what Wi-Fi 8 changes: Scheduled Power Save, (Semi-)Dynamic Power Save, Cross-Link Power Save, plus wake-up-radio integration and STA offloading. Quantifies up to ~28% average AP power reduction on a dataset from 470 real campus APs, and names the open challenges (legacy compatibility, policy selection).
- **[Paper · EN · ★★★]** "What is Wrong/Right with IEEE 802.11n Spatial Multiplexing Power Save Feature?" — I. Pefkianakis, C.-Y. Li, S. Lu · *IEEE ICNP*, 2011
  - The paper that proves power and energy are different metrics. Measurements on real 802.11n hardware show ~2.5 W for a high-rate MIMO receiver, up to 1.15 W saved by SMPS, but also that a single chain can be worse per bit; their MRES algorithm beats SMPS by up to 37%, and optimal chain selection differs from the SMPS choice by up to 78.6% in per-bit energy.
- **[Paper · EN · ★★★]** "A Tutorial on IEEE 802.11ax High Efficiency WLANs" — E. Khorov, A. Kiryanov, A. Lyakhov, G. Bianchi · *IEEE Communications Surveys & Tutorials*, vol. 21, no. 1, pp. 197–216, 2019
  - Listed in §02-1. For this note it is the primary source on TWT: individual versus broadcast, implicit versus explicit, trigger-enabled service periods, and Opportunistic Power Save.
- **[Paper · EN · ★★★]** "A Tutorial on Wi-Fi 8: The Journey to Ultra High Reliability" — A. Karamyshev, I. Levitsky, D. Bankov, E. Khorov · *Problems of Information Transmission*, vol. 61, no. 2, pp. 164–210, 2025 · DOI 10.1134/S003294602502005X
  - Listed in §02-1. For this note, read its power-saving part: unavailability reporting, periodic and dynamic unavailability operation, dynamic power save, cross-link power save, and scheduled AP power save.
- **[Paper · EN · ★★★]** "Wi-Fi: Twenty-Five Years and Counting" — G. Geraci, F. Meneghello, F. Wilhelmi, D. López-Pérez, I. Val, L. Galati Giordano, C. Cordeiro, M. Ghosh, E. Knightly, B. Bellalta · *Proceedings of the IEEE*, vol. 113, no. 11, pp. 1290–1336, 2025 · arXiv:2507.09613
  - Listed in §02-1. Its power-saving section is the best single-source cross-generation comparison, because it is organised by mechanism rather than by amendment.
- **[Paper · EN · ★★★]** "R-TWT in Wi-Fi 7 and Beyond: Enabling Bounded Latency, Energy Efficiency, and Reliability" — E. Mozaffari Ahrar, F. Wilhelmi, L. Galati-Giordano, P. Imputato, M. Menth, S. Avallone · 2025
  - ns-3 evaluation of Restricted TWT across service types and network sizes: worst-case latency, energy, collision rate and throughput, versus legacy Power Saving Mode and DCF. Finds bounded latency for IoT and real-time traffic plus better energy efficiency, scaling with network size. `VERIFY` final publication venue.
- **[Paper · EN · ★★]** "Multi-Link Scheduling with Restricted Target Wake Time in Wi-Fi 7" — D. Ergenç, M. Zakrzewski, F. Dressler · Telecommunication Networks Group, TU Berlin, 2026
  - The joint-MLO-and-r-TWT case that neither feature's own literature covers: heuristics for coordinating r-TWT service periods across links, with an open-source OMNeT++ multi-link framework. Reports predictable latency and clear energy reduction versus unscheduled operation.
- **[Paper · EN · ★★]** "Wi-Fi in Constrained Devices: A Literature Review" — Tom Carpenter · CWNP, 2026
  - A practitioner-facing synthesis covering TWT parameter tuning, R-TWT, idle listening and BSS Max Idle. Notably states that R-TWT is **not** required for Wi-Fi CERTIFIED 7 and that shipping client devices and APs did not advertise support at time of writing — the most useful caution against assuming Wi-Fi 7 power features are deployed.
- **[Paper · EN · ★★]** "Performance and Power Consumption Analysis of IEEE 802.11ah for Smart Grid" — Hindawi, 2018 · DOI 10.1155/2018/5286560
  - Worked power modelling for HaLow, including TIM segmentation and page slicing, maximum sleep-time expansion, and TWT grouping. Useful for the arithmetic of duty-cycled Wi-Fi rather than for the smart-grid application.
- **[Paper · EN · ★]** "Idle listening energy" measurements for low-traffic IoT — Park and Adnan, 2016
  - Establishes the result that idle listening exceeds transmission energy for low-to-moderate traffic IoT, and proposes downclocking plus aggregation. `VERIFY` full venue and author names before citing; cited second-hand in the CWNP review above.
- **[Paper · EN · ★]** Survey of IEEE 802.11ah MAC-layer features for massive IoT — Farhad and Pyun, 2022
  - Positions TWT alongside RAW and TIM segmentation as complementary, and identifies adaptive TWT parameter tuning under heterogeneous traffic as an open problem. `VERIFY` venue.

### Standards and specifications

- **[Standard · ★★★]** **IEEE Std 802.11ba-2021** — Wireless LAN MAC and PHY, Amendment 3: Wake-Up Radio Operation · published 8 October 2021 · ISBN 978-1-5044-7508-2
  - The normative source for the wake-up radio: MC-OOK PHY, WUR MAC procedures including duty-cycle operation, and the sub-milliwatt target. This is the document to quote when comparing against 3GPP LP-WUS.
- **[Standard · ★★★]** **IEEE Std 802.11ah-2016** — Sub-1 GHz license-exempt operation (Wi-Fi HaLow)
  - Where TWT originated, together with TIM segmentation, non-TIM STA operation, RAW and bidirectional TXOP.
- **[Standard · ★★★]** **IEEE Std 802.11-2020 / -2024** — base standard, power-management and TWT clauses
  - Clause 11.2 for legacy power management and U-APSD; the TWT procedures and element in the high-efficiency clauses. Navigate here rather than to summaries when a field's exact encoding matters.
- **[Standard · ★★★]** **IEEE Std 802.11be-2024** — EHT (Wi-Fi 7), Restricted TWT
  - Normative r-TWT: schedule broadcast, membership negotiation, restricted access and legacy quieting.
- **[Spec · ★★★]** **IEEE P802.11bn** (TGbn) draft — UHR (Wi-Fi 8), AP Power Save
  - The only authoritative source for Dynamic Power Save, Cross-Link Power Save, scheduled AP power save on PUO, and unavailability reporting. Draft; verify against the current draft version before quoting.
- **[Spec · ★★]** **IEEE P802.11bp** (TGbp) draft — Ambient Power Communication (AMP)
  - Battery-free STAs powered by energy harvesting: sub-1 GHz plus 2.4 GHz, wireless power transfer modes, and AMP STA status reporting. D1.0 working-group ballot ran October–November 2026.
- **[Doc · ★★]** **IEEE 802.11 Task Group status pages** — TGba, TGbp, TGbn
  - Publication dates, ballot results and milestone timelines, directly from the working group. Prefer these over secondary reporting for any date.
- **[Doc · ★★]** **IEEE 802.11 Working Group liaison to IEEE 802.1 on TSN support** (2022)
  - Sets out r-TWT in the TSN framework: alignment of restricted service periods with 802.1Qbv gate-open times, alongside QoS signalling (SCS) and TID-to-link mapping.

### Wi-Fi Alliance

- **[Doc · ★★★]** **Wi-Fi CERTIFIED 6 Release 2 announcement** — Wi-Fi Alliance, 5 January 2022
  - The point at which Wi-Fi 6 power saving became a buying criterion: broadcast TWT, extended sleep time, and dynamic multi-user SMPS, plus uplink MU-MIMO.
- **[Doc · ★★]** **WMM Power Save specification** — Wi-Fi Alliance
  - The interoperability layer over U-APSD, and the source of the certified behaviour at the AC-level trigger/delivery boundary.
- **[Doc · ★★]** "Wi-Fi CERTIFIED 6 Release 2: Better wireless for IoT" — Wi-Fi Alliance Beacon blog
  - Practitioner-level explanation of dynamic SMPS, 20 MHz STA, broadcast TWT and BSS Max Idle, with the IoT framing.

### Tools and measurement

- **[Doc · ★]** **Linux `iw` and `hostapd` TWT configuration** — `iw dev <dev> set twt …`; `he_twt_required=1` in `hostapd.conf`
  - How to exercise TWT on real hardware with mac80211 and HE support.
- **[Doc · ★]** **Wireshark display filters for power save** — `wlan.fc.pwrmgt == 1`, `wlan.fc.type_subtype == 0x1a` (PS-Poll), `wlan.qos.eosp == 1`, `wlan_mgt.tim.dtim_period`
  - The fastest way to confirm whether a device is actually using U-APSD or has silently fallen back to PS-Poll.

---

## 02-3 · WLAN Ecosystem — WFA, EasyMesh and prpl

### Books

- **[Book · EN · ★★★]** *802.11 Wireless Networks: The Definitive Guide*, 2nd ed. — Matthew Gast (see §02-1)
  - The MAC and management-frame foundation that certification programs build on.

### Standards and program documents

- **[Standard · ★★★]** **Wi-Fi Alliance certification program specifications** — Wi-Fi CERTIFIED n / ac / ax / be, Wi-Fi CERTIFIED 6 / 7, WPA3 (Security), Wi-Fi EasyMesh, Wi-Fi Agile Multiband, Wi-Fi Data Elements, Wi-Fi Location, Wi-Fi Aware
  - Certification is what makes Wi-Fi a product category rather than a standard. Know which program constrains which behaviour, and that Wi-Fi 8 certification is expected around January 2028 while IEEE approval is expected March–May 2028.
- **[Standard · ★★★]** **Wi-Fi EasyMesh Specification** (Wi-Fi Alliance, Multi-AP)
  - The interoperable multi-AP architecture: controller/agent roles, the 1905.1 abstraction layer, topology discovery, channel planning, client steering, and AP auto-configuration. This is the standards counterpart to the multi-AP coordination mechanisms in 802.11bn.
- **[Standard · ★★]** **IEEE 1905.1a-2014** — Convergent Digital Home Network for Heterogeneous Technologies
  - The abstraction layer EasyMesh uses to unify Wi-Fi, Ethernet, MoCA and powerline backhaul. Read it to understand where EasyMesh's "multi-AP" is really heterogeneous-backhaul management.
- **[Standard · ★★]** **Broadband Forum TR-069 / TR-181** (CPE WAN Management Protocol, device data model) and **TR-369** (User Services Platform, USP)
  - The remote management stack for carrier-grade gateways. TR-181's data model is where EasyMesh and Wi-Fi parameters are exposed to the operator.
- **[Doc · ★★]** **prpl Foundation: prplOS, prplMesh, prpl LCM** (open source)
  - The open-source EasyMesh implementation and its lifecycle-management layer. Read prplMesh to see how the abstract EasyMesh architecture maps onto hostapd, nl80211 and the Linux network stack.
- **[Doc · ★★]** **OpenWrt documentation** and **hostapd / wpa_supplicant documentation**
  - The de facto reference implementation for Wi-Fi stack behaviour on Linux. When in doubt about how a feature behaves on a real device, read hostapd.
- **[Doc · ★]** **RDK-B (Reference Design Kit for Broadband)** documentation
  - The cable/telco gateway software stack; useful context for the operator-managed device world EasyMesh and prpl target.


## 02-5 · WLAN — STA/AP Discovery, Authentication and Association

### Books

- **[Book · ★★★]** *802.11 Wireless Networks: The Definitive Guide*, 2nd ed. — Matthew Gast, O'Reilly, 2005. ISBN 978-0-596-10052-0
  - Chapters on scanning, the MAC state machine and management frames are the clearest prose account of what this note covers. Read the association and authentication sections alongside a capture, not on their own.
- **[Book · ★★★]** *Real 802.11 Security: Wi-Fi Protected Access and 802.11i* — Jon Edney and William A. Arbaugh, Addison-Wesley, 2003. ISBN 978-0-321-13620-6
  - The 802.1X port model, the RSN key hierarchy and the reasoning behind the 4-way handshake, written by people who were in the room. Dated on WPA3, still correct on everything below it.

### Standards

- **[Standard · ★★★]** IEEE Std 802.11-2024 — *Wireless LAN MAC and PHY Specifications*, published 28 April 2025
  - Clauses 11 (MLME), 12 (security) and the RSN IE definition are normative for this note. The MLME state machine diagram and the reason-code table live here.
- **[Standard · ★★★]** IEEE Std 802.11be-2024 — *Enhancements for Extremely High Throughput*, published 22 July 2025
  - Multi-link discovery, the Basic Multi-Link Element, multi-link setup with per-STA profiles, and per-link group keys.
- **[Standard · ★★★]** IEEE Std 802.11-2020 — the revision that consolidated SAE, OWE, FILS and PMF into the base standard
  - Use it to trace which amendment introduced which element; the SAE and FILS clauses are the substantive ones.
- **[Standard · ★★★]** IEEE Std 802.11i-2004 — *Medium Access Control Security Enhancements*
  - The original RSNA specification: the 4-way handshake, the key hierarchy and the group key handshake, still described more plainly here than in the consolidated revisions.
- **[Standard · ★★]** IEEE Std 802.11w-2009 — *Protected Management Frames*
  - BIP, the IGTK, and the SA Query procedure that makes a forged deauthentication survivable.
- **[Standard · ★★]** IEEE Std 802.11r-2008 (fast BSS transition), 802.11k-2008 (radio resource measurement), 802.11v-2011 (network management), 802.11ai-2016 (FILS)
  - The four roaming amendments. Read 11r for the key hierarchy (PMK-R0/R1), 11k for the neighbour report, 11v for the transition management frame, 11ai for the four-frame join.
- **[Standard · ★★]** IEEE Std 802.11ax-2021 — *Enhancements for High Efficiency WLAN*
  - 6 GHz operation and the discovery rules that go with it: RNR carriage, FILS Discovery and the PSC convention.

### Papers and practitioner material

- **[Paper · ★★★]** Vanhoef, M., and Ronen, E. "Dragonblood: Analyzing the Dragonfly Handshake of WPA3 and EAP-pwd." *IEEE Symposium on Security and Privacy*, 2020. DOI 10.1109/SP40000.2020.00031
  - Timing and cache side channels in hunting-and-pecking, the group-downgrade attack, and why H2E exists. The paper to cite before claiming SAE is attack-free.
- **[Paper · ★★★]** Vanhoef, M., and Piessens, F. "Key Reinstallation Attacks: Forcing Nonce Reuse in WPA2." *ACM CCS*, 2017. DOI 10.1145/3133956.3134027
  - Why a retransmitted M3 is dangerous, and the install-once rule every implementation now follows.
- **[Paper · ★★]** Harkins, D. "Simultaneous Authentication of Equals: A Secure, Password-Based Key Exchange for Mesh Networks." *SENSET*, 2008
  - The Dragonfly protocol that SAE is built on, described before it was a Wi-Fi amendment.
- **[Paper · ★★]** "Multi-Link Operation in IEEE 802.11be Extremely High Throughput: A Survey." IEEE Xplore document 10474403
  - Multi-link setup, per-STA profiles, TID-to-link mapping and the discovery cost of an MLD, with the state of the art around it.
- **[Doc · ★★]** IEEE 802.11 TGax. "Considerations on 6 GHz Discovery," 11-18-1922-00-00ax, November 2018. <https://mentor.ieee.org/802.11/dcn/18/11-18-1922-00-00ax-considerations-on-6-ghz-discovery.pptx>
  - The airtime arithmetic behind FILS Discovery at a 20 TU cadence, and why Multiple BSSID is mandatory in 6 GHz.
- **[Doc · ★★]** Cisco. "Something New: AP Discovery Methods for 6 GHz Wi-Fi." *Cisco Blogs*. <https://blogs.cisco.com/networking/something-new-ap-discovery-methods-for-6ghz-wi-fi-part-2>
  - RNR versus PSC versus FILS Discovery versus unsolicited probe response, with the 59-channel and 102.4 ms numbers worked out.
- **[Standard · ★★]** RFC 8110 (OWE), RFC 3748 (EAP), RFC 5247 (EAP key management), RFC 5216 (EAP-TLS), RFC 7170 (TEAP), RFC 6696 (ERP), RFC 2865 (RADIUS)
  - The IETF half of the Enterprise path: what the MSK is, how it becomes the PMK, and how FILS re-authenticates in one round trip.
- **[Doc · ★★]** Wi-Fi Alliance. *WPA3 Specification* and *Wi-Fi CERTIFIED 7* requirements. <https://www.wi-fi.org/discover-wi-fi/security>
  - Which features are mandatory rather than optional: WPA3 and PMF for Wi-Fi 7, SAE with H2E for WPA3-Personal, PMF for 6 GHz.
- **[Doc · ★★]** `hostapd` and `wpa_supplicant` source and documentation; `iw` and the Wireshark 802.11 dissector
  - `wpa_supplicant -dd` and `hostapd -dd` are where a failed join becomes readable; the Wireshark RSN IE and EAPOL-Key dissections name every field this note describes.

---

## 02-6 · WLAN — Multi-AP Roaming, Healing and Steering

### Books

- **[Book · ★★★]** *802.11 Wireless Networks: The Definitive Guide*, 2nd ed. — Matthew Gast, O'Reilly, 2005. ISBN 978-0-596-10052-0
  - Reassociation as a *service* rather than an event, and the plain statement that the standard has no opinion on when to roam. Read it before reading anything about steering; it explains why the industry had to invent steering at all.
- **[Book · ★★]** *Real 802.11 Security: Wi-Fi Protected Access and 802.11i* — Jon Edney and William A. Arbaugh, Addison-Wesley, 2003. ISBN 978-0-321-13620-6
  - The key hierarchy that PMKSA caching, OKC and FT each cut into at a different depth — the reason "we do fast roaming" can mean three different things.
- **[Book · ★★]** *802.11ac: A Survival Guide* and *802.11n: A Survival Guide* — Matthew Gast, O'Reilly, 2013 / 2012
  - Short, and useful for how APs actually behave in dense deployments: channel width decisions, co-channel interference, and why raw RSSI comparisons mislead.


### Standards

- **[Standard · ★★★]** IEEE Std 802.11k-2008 — *Radio Resource Measurement*
  - Neighbor Report and Beacon Report. Everything in this note that is a measurement rather than a command comes from here.
- **[Standard · ★★★]** IEEE Std 802.11v-2011 — *Wireless Network Management*
  - BSS Transition Management: the Query, Request and Response action frames, the candidate list with its preference field, and the disassociation-imminent timer. The single most useful amendment for anybody building a steering feature.
- **[Standard · ★★★]** IEEE Std 802.11r-2008 — *Fast BSS Transition*
  - The PMK-R0/R1 hierarchy, the mobility domain element, over-the-air versus over-the-DS, PMK-R1 pull and push, and the remote frame that carries the DS path.
- **[Standard · ★★]** IEEE Std 802.11-2024 — *Wireless LAN MAC and PHY Specifications*
  - The consolidated text: clause 35.3.23 (BSS transition management for MLDs), the WNM and RRM clauses, and the status-code table that names `REJECTED_WITH_SUGGESTED_BSS_TRANSITION`.
- **[Standard · ★★]** IEEE Std 802.11be-2024 — *Enhancements for Extremely High Throughput*
  - The Basic Multi-Link element inside the Neighbor Report, link reconfiguration, and BPCC — the mechanisms that make steering an MLD-level question.
- **[Standard · ★★]** IEEE Std 802.11s-2011 — *Mesh Networking*
  - HWMP, RANN and the airtime link metric. Read it to understand what EasyMesh deliberately did *not* adopt, and why.
- **[Standard · ★★]** IEEE Std 1905.1-2013 and 1905.1a-2014 — *Convergent Digital Home Network*
  - CMDU and TLV framing. Every Multi-AP message in this note is a payload inside this envelope.
- **[Standard · ★]** IEEE Std 802.11ai-2016 (FILS) and 802.11u-2011 (Interworking)
  - FILS is what makes a roam cheap for a client that already has a PMKSA; 802.11u's ANQP/GAS is where MBO and Passpoint ride.

### Papers and practitioner material

- **[Paper · ★★★]** Karamyshev, A., Levitsky, I., Bankov, D., and Khorov, E. "A Tutorial on Wi-Fi 8: The Journey to Ultra High Reliability." *Problems of Information Transmission*, 61(2), 2025. DOI 10.1134/S003294602502005X
  - The most honest public account of 802.11bn: SMD as the roaming answer, the MAPC scheme family, and the 25% targets. Use it instead of vendor blogs when you need a citable statement.
- **[Spec · ★★★]** Wi-Fi Alliance. *Wi-Fi EasyMesh Specification v6.0* and *Test Plan v6.0*, August 2024
  - The message catalogue: Client Steering Request, Client Association Control Request, Backhaul Steering Request, Steering Completed, Client Disassociation Stats. The normative source for §4.4 and §5.
- **[Doc · ★★★]** Wi-Fi Alliance. *Wi-Fi CERTIFIED Agile Multiband Technology Overview*, April 2021. <https://www.wi-fi.org/system/files/Wi-Fi_CERTIFIED_Agile_Multiband_Technology_Overview_202104.pdf>
  - The MBO-OCE information element, the non-preferred channel report, WNM reason codes and throttling. The missing half of BTM, written by the body that certifies it.
- **[Doc · ★★★]** Cisco. *Catalyst 9800 Configuration Guide*, Fast Transition chapter. <https://www.cisco.com/c/en/us/td/docs/wireless/controller/9800/17-17/config-guide/b_wl_17_17_cg/m_fast_transition_ewlc.pdf>
  - The failure statuses (`STATUS_INVALID_MDE`, the AKM rejection), the documented three-concurrent-FT limit, and the practical advice on over-the-air versus over-the-DS. Vendor documentation as a source of failure taxonomy.
- **[Doc · ★★★]** Cisco. "What is 802.11r? Why is this Important?" *Cisco Blogs*. <https://blogs.cisco.com/networking/what-is-802-11r-why-is-this-important>
  - The clearest short explanation of FT as make-before-break, and of what over-the-DS actually tunnels.
- **[Doc · ★★]** Wi-Fi Alliance. "Wi-Fi CERTIFIED Agile Multiband balances network resources with intelligent guidance." *Wi-Fi Alliance Beacon*
  - Why Agile Multiband is a requirement for Wi-Fi CERTIFIED 6, plus the CableLabs 2019 field trial with the 84% reconnection-time improvement.
- **[Doc · ★★]** IEEE 802.11 TGbe. "SB1 CR for CIDs 22000 and 22001," 11-24-0699r1, 2024. <https://mentor.ieee.org/802.11/dcn/24/11-24-0699-01-00be-sb1-cr-for-cids-22000-and-22001.docx>
  - A worked example of extending an existing mechanism (the Neighbor Report in a rejected association) to MLDs rather than inventing a new one — good material for a design-discussion interview.
- **[Doc · ★★]** prpl Foundation. "Appendix: EasyMesh Standards Compliance," prplMesh wiki. <https://gitlab.com/prpl-foundation/prplmesh/prplMesh/-/wikis/Appendix-EasyMesh-Standards-Compliance>
  - Which prplMesh release implements which EasyMesh release, and which R6 features landed early. The practical map from spec version to code.
- **[Doc · ★★]** HPE Aruba Networking. *Wi-Fi generations — design and deployment*. <https://www.arubanetworks.com/techdocs/aos/wifi-design-deploy/generations/\_print>
  - The U-MAC / L-MAC split, MLD versus link addresses, BPCC, and link recommendation through BTM — a vendor doc that is unusually precise about MLO internals.
- **[Code · ★★★]** `hostapd/src/ap/wnm_ap.c`, `rrm.c`, `neighbor_db.c`; `wpa_supplicant/wnm_sta.c`; `hostapd_cli bss_tm_req`, `set_neighbor`
  - The AP side and client side of BTM as implemented, including what happens when a client never answers. Faster than any book for the timeout behaviour.
- **[Code · ★★]** prplMesh controller tasks (`optimal_path_task`, `network_health_check_task`, `client_locating_task`) and the agent `backhaul_manager`
  - A readable reference implementation of mesh healing: the parent-selection state machine, and the wired-over-wireless preference that prevents most loop bugs.
- **[Code · ★★]** Linux `mac80211` (`mlme.c`, beacon-loss handling) and the `nl80211` roaming interface
  - Where the client's own roam trigger actually lives, and why the network cannot see it.

---

## 02-7 · WLAN — Wi-Fi EasyMesh: Operation, Tuning and Troubleshooting

### Standards

- **[Standard · ★★★]** Wi-Fi Alliance. *Wi-Fi EasyMesh Specification*, v1.0 (2018-06-18), v2.0 (2019-12-18, Profile-2), v3.0 (2020-12-07, Profile-3), v4.0 (2021-11-16), v5.0 (2022-12-08), v6.0 (2024). <https://www.wi-fi.org/discover-wi-fi/wi-fi-easymesh>
  - The normative text for this note: onboarding, AP-autoconfiguration, channel selection, client steering, backhaul optimisation, link metrics, traffic separation, 1905-layer security, and the four-address rules. Use the revision table in the front matter to anchor any release claim you make in an interview.
- **[Standard · ★★★]** IEEE Std 1905.1-2013 — *IEEE Standard for a Convergent Digital Home Network for Heterogeneous Technologies* (with 1905.1a-2014)
  - The transport EasyMesh rides on: EtherType `0x893A`, the 8-octet CMDU header, TLV framing, neighbor versus relayed versus unicast transmission, and topology discovery. Notably it defines **no** forwarding or loop-prevention protocol — bridging is somebody else's problem.
- **[Standard · ★★]** IEEE Std 802.11-2020 — *Wireless LAN Medium Access Control and Physical Layer Specifications*
  - The four-address MAC header (clause 9), the vendor-specific element used by the Multi-AP IE, and the status and reason code tables that EasyMesh reuses for steering and backhaul rejections.
- **[Standard · ★★]** Wi-Fi Alliance. *Wi-Fi Easy Connect Specification* — Device Provisioning Protocol (DPP)
  - The Profile-3 onboarding path: bootstrapping, the authentication protocol, `netRole` values including the Multi-AP-specific `mapBackhaulSta` and `mapAgent`, CCE, and reconfiguration. Read the base DPP spec before the EasyMesh clauses that wrap it.
- **[Standard · ★★]** Wi-Fi Alliance. *Wi-Fi Agile Multiband Specification* and *Wi-Fi Optimized Connectivity Specification*
  - The MBO-OCE IE with the transition reason code and candidate preference, the Association Disallowed attribute, and RSSI-based association rejection. EasyMesh references both as the client-facing half of steering.
- **[Standard · ★]** Wi-Fi Alliance. *Wi-Fi Simple Configuration (WSC) v2.0.5*
  - The M1/M8 exchange EasyMesh extends with the Multi-AP Extension subelement, and the Authentication Types table to which Multi-AP adds `0x0040` (SAE).

### Books

- **[Book · ★★]** *802.11 Wireless Networks: The Definitive Guide*, 2nd ed. — Matthew Gast, O'Reilly, 2005. ISBN 978-0-596-10052-0
  - Still the clearest explanation of the four-address (WDS) frame format and why a station cannot bridge multiple MACs in three-address mode. Read it before debugging a wireless backhaul.
- **[Doc · ★★]** Broadband Forum. *TR-069 Amendment 6 — CPE WAN Management Protocol* and *TR-181 Issue 2 — Device:2 Data Model*. <https://www.broadband-forum.org/technical/download>
  - The remote management path: 1905.1 topology information is exposed through the device data model, which is how an operator's ACS actually sees an EasyMesh network. Reach for this when the question is "how is this managed at scale?" rather than "how does it work?".
- **[Book · ★]** *Next Generation Wireless LANs: 802.11n and 802.11ac*, 2nd ed. — Eldad Perahia and Robert Stacey, Cambridge University Press, 2013. ISBN 978-1-107-01176-1
  - Channelisation, operating classes and DFS/CAC mechanics — the physical reality behind the Channel Preference and Channel Selection exchanges.

### Implementation references

- **[Doc · ★★★]** J. Malinen et al. *hostapd / wpa_supplicant — README-MULTI-AP*. <https://android.googlesource.com/platform/external/wpa_supplicant_8/+/refs/heads/main/hostapd/README-MULTI-AP>
  - The shortest accurate statement of scope: hostapd implements only WPS onboarding and backhaul link configuration; everything else belongs to a separate daemon. Also the `multi_ap=1/2/3` semantics, `multi_ap_backhaul_sta=1`, the per-bSTA VLAN, and the M1-to-M8 backhaul credential rule.
- **[Doc · ★★★]** prpl Foundation. *prplMesh — Interface Tools*. <https://gitlab.com/prpl-foundation/prplmesh/prplMesh/-/wikis/Management-Interfaces-and-Tools/Interface-Tools>
  - `prplmesh_cli`, `beerocks_cli`, `prplmesh_utils.sh` management modes, log locations and the topology visualiser. The practical answer to "how do I look inside a running EasyMesh network?"
- **[Doc · ★★]** prpl Foundation. *prplMesh — Appendix: EasyMesh Standards Compliance*. <https://gitlab.com/prpl-foundation/prplmesh/prplMesh/-/wikis/Appendix-EasyMesh-Standards-Compliance>
  - Maps prplMesh major versions to EasyMesh releases (1.x R1 … 6.x R6) and lists which features landed where. The best public evidence for what a release actually contains.
- **[Code · ★★]** iopsys / Genexis. *map2.h — Multi-AP message and TLV definitions*. <https://dev.iopsys.eu/multi-ap/ieee1905/-/commit/c3bc7a76836f13f0c257907a036adad7c6497961>
  - Concrete `#define` values for the CMDU types (`0x8000`–`0x8033`) and TLV types. Use it when you need a number on a slide; cross-check against the specification's own tables before quoting it.
- **[Doc · ★★]** Wireshark. *IEEE 1905.1 dissector reference*. <https://www.wireshark.org/docs/dfref/i/ieee1905.html>
  - The `ieee1905.cmdu.type` and `ieee1905.tlv.type` display filters. Without these, EasyMesh debugging is guesswork.

### Papers and practitioner material

- **[Doc · ★★★]** NXP Semiconductors. *AN14996 — PBC method for Agent 2 and beyond onboarding over Wi-Fi*. <https://docs.nxp.com/bundle/AN14996/page/topics/pbc_method_for_agent_2_and_beyond_onboarding_over\_.html>
  - A runnable onboarding recipe: `systemctl start easymesh-agent`, `wpa_cli wps_pbc multi_ap=1` on the enrollee, `hostapd_cli wps_pbc` on the existing agent, then verify with `iw dev ... link`. Vendor documentation as a bring-up template.
- **[Paper · ★★]** Rajamanickam, A. et al. "5G and Wi-Fi 7 Network Convergence with End-to-End Network Slicing." *NCTA Technical Papers*, 2024. <https://www.nctatechnicalpapers.com/Paper/2024/WLESS03_Rajamanickam_6573_paper/download>
  - How EasyMesh R6 (Multi-AP R6) is described in operator terms: Wi-Fi 7 integrated into the controller, 20–320 MHz configuration with static puncturing, MLO backhaul and MLO fronthaul, and MLD-level steering.
- **[Doc · ★★]** Allion Labs. *2024 New Spec Update — August*. <https://www.allion.com/news-center/new_spec_202408>
  - The dated third-party record of the WFA announcement: Wi-Fi EasyMesh Specification v6.0 and Test Plan v6.0, effective 2024-12-31 for newly tested mesh devices.
- **[Doc · ★★]** Wi-Fi Alliance. *Wi-Fi CERTIFIED EasyMesh Technical Overview* (2022). <https://wi-fi.org/zh-hant/file/wi-fi-certified-easymesh-jishugaishu-2022>
  - The marketing-level statement of what the programme covers — onboarding, channel and network management, AP reporting, path optimisation — useful for framing, not for protocol detail.
- **[Doc · ★]** Comnect. *EasyMesh Is Not Just Mesh: Understanding the Evolution of Multi-AP Wi-Fi*. <https://comnect.com/service/pro_news_info.html?id=195>
  - Release-by-release feature evolution R1→R6 and the recurring warning that "R6" is not a synonym for "Wi-Fi 7". Secondary source — verify individual claims against the specification.
- **[Doc · ★]** Huawei. *How Do I Complete EasyMesh Networking on Routers?* <https://consumer.huawei.com/en/support/content/en-us16057841/>
  - The three consumer onboarding methods (WPS button, wireless relay, Ethernet) and the placement guidance vendors give. Useful for understanding what users actually do before they call support.
- **[Doc · ★]** TP-Link Community. *Knowledge Base: EasyMesh*. <https://community.tp-link.com/en/home/forum/topic/660384>
  - Real field cases, including EasyMesh Ethernet backhaul failing behind a particular managed switch — exactly the multicast/VLAN class of fault described in §9 of the note.


## 02-8 · WLAN — Scheduling: Channel Access, EDCA, OFDMA Allocation, Airtime and Implementation

### Standards

- **[Standard · ★★★ · EN]** IEEE. *IEEE Std 802.11-2024 — Wireless LAN Medium Access Control (MAC) and Physical Layer (PHY) Specifications*. <https://standards.ieee.org/ieee/802.11/>>
  - Clause 10 (DCF, EDCA, HCF), 9.3.1.22 (trigger frame formats), 9.4.2.x (TWT, EDCA Parameter Set, UORA Parameter Set), 26 (HE), 35 (EHT multi-link operation). Every fact in the note cites one of these clauses; read clause 10 once end to end before anything else.
- **[Standard · ★★★ · EN]** IEEE. *IEEE Std 802.11-2016*, clause 9.4.2.29, Table 9-137 "Default EDCA Parameter Set element".
  - The source of the EDCA table. Compare it against 802.11-2012 Table 8-105 — the TXOP limits changed for every access category, and that difference explains a real category of field failures.
- **[Standard · ★★★ · EN]** IEEE. *IEEE Std 802.11ax-2021 — Enhancements for High Efficiency WLAN*, clause 27 (HE PHY), 26.5 (trigger-based UL), 27.5.5 (UORA).
  - OFDMA resource units, the HE 80 MHz tone plan that 802.11be later revised, the trigger frame, and the normative UORA text with its OCW rules.
- **[Standard · ★★★ · EN]** IEEE. *IEEE Std 802.11be-2024 — Enhancements for Extremely High Throughput (EHT)*, clause 35 (MLO), 36 (EHT PHY).
  - Multiple resource units, the corrected 80 MHz tone plan, enhanced puncturing, EMLSR/EMLMR, TID-to-link mapping, SCS and restricted TWT. This is where the scheduling surface of Wi-Fi 7 is defined.
- **[Doc · ★★ · EN]** i TecSpec. *IEEE 802.11 — resource unit and MRU allocations*. <https://itecspec.com/>
  - The RU and MRU tables in quotable form, including which combinations are illegal. Useful because the legal set is small enough to enumerate and the exclusions are easy to get wrong.

### Books

- **[Book · ★★★ · EN]** Gast, Matthew S. *802.11 Wireless Networks: The Definitive Guide*, 2nd ed. — O'Reilly, 2005 · ISBN 978-0-596-10052-0
  - The clearest prose account of DCF, interframe spaces, the NAV and the backoff machine that exists. It predates OFDMA entirely, which is exactly why it is still the right place to learn the part that has not changed.
- **[Book · ★★ · EN]** Perahia, Eldad, and Stacey, Robert. *Next Generation Wireless LANs: 802.11n and 802.11ac* — Cambridge University Press, 2nd ed., 2013 · ISBN 978-1-107-01677-6
  - For the aggregation and Block Ack machinery that turns "one frame per access" into the burst economy the scheduler actually operates in.

### Papers

- **[Paper · ★★★ · EN]** Bianchi, G. "Performance Analysis of the IEEE 802.11 Distributed Coordination Function." *IEEE Journal on Selected Areas in Communications*, vol. 18, no. 3, March 2000, pp. 535–547 · DOI 10.1109/49.840210
  - The analytical model behind every backoff and contention-window argument. Its saturation-throughput result is still the reference point for "how much does contention cost", and it is the paper to cite when someone asks why CWmin and CWmax have the values they do.
- **[Paper · ★★★ · EN]** Høiland-Jørgensen, T., Kazior, M., Täht, D., Hurtig, P., and Brunström, A. "Ending the Anomaly: Achieving Low Latency and Airtime Fairness in WiFi." *USENIX Annual Technical Conference (ATC)*, 2017. <https://www.usenix.org/conference/atc17/technical-sessions/presentation/hoiland-jorgensen>
  - The argument for airtime fairness and the origin of the `mac80211` work in this note. Read it together with the AQL commit below: the paper is the why, the commit is the what shipped.
- **[Paper · ★★ · EN]** Kelly, F. P., Maulloo, A. K., Tan, D. K. H. "Rate control for communication networks: shadow prices, proportional fairness and stability." *Journal of the Operational Research Society*, vol. 49, no. 3, pp. 237–252, March 1998 · DOI 10.1057/palgrave.jors.2600523
  - The origin of the proportional-fairness criterion discussed and then set aside in §8.1. Worth reading so that "fair" is never used loosely again.

### Implementation references

- **[Code · ★★★ · EN]** Linux kernel, commit `3ace10f5b5ad` — Kan Yan, Toke Høiland-Jørgensen. *mac80211: Implement Airtime-based Queue Limit (AQL)*, authored 2019-11-18. <https://git.kernel.org/torvalds/c/3ace10f5b5ad>
  - The commit message is the best single explanation of why bytes are the wrong queue depth. The diff introduces `IEEE80211_DEFAULT_AQL_TXQ_LIMIT_L 5000`, `_H 12000`, `IEEE80211_AQL_THRESHOLD 24000`.
- **[Code · ★★★ · EN]** Linux kernel, commit `911bde0fe5cc` — Toke Høiland-Jørgensen. *mac80211: Turn AQL into an NL80211_EXT_FEATURE*, December 2019. <https://git.kernel.org/torvalds/c/911bde0fe5cc>
  - Why AQL is opt-in, and the specific reason `iwlwifi` was excluded: TSO underflows, and HE rates not reported so AQL would assume 6 Mbps instead of up to 2400 Mbps. The most instructive queueing bug in Wi-Fi.
- **[Code · ★★★ · EN]** Linux kernel source — `net/mac80211/tx.c`, `net/mac80211/airtime.c`, `net/mac80211/sta_info.c`, `net/mac80211/rc80211_minstrel_ht.c`, `include/net/cfg80211.h`.
  - `airtime.c` for the accounting, `rc80211_minstrel_ht.c` for the rate controller that feeds it, `cfg80211.h` for the AQL constants. Read these three against §8 and §10.
- **[Code · ★ · EN]** Linux kernel, Felix Fietkau. *mac80211: add AQL support for broadcast/multicast packets*, February 2024.
  - Adds `IEEE80211_DEFAULT_AQL_TXQ_LIMIT_BC 50000`. The reason it was needed — broadcast floods hardware queues and breaks fair queueing — is the multicast story of §2.3 and §12.3 in one patch.

### Practitioner and operator material

- **[Doc · ★★ · EN]** Ryan, Dan. *Cisco WLC: EDCA timers* — 802.11-2016 Table 9-137 versus 802.11-2012 Table 8-105. <https://netgab.net/web/2017/12/05/cisco-wlc-edca-timers/>
  - The side-by-side that makes the TXOP-limit change legible, and the argument that the 2016 change *caps* slow stations rather than rewarding background traffic.
- **[Doc · ★★ · EN]** York University EECS course notes. *IEEE 802.11 Medium Access Control*. <https://www.eecs.yorku.ca/course_archive/2017-18/W/3214/Notes/c7b_CSMA.pdf>
  - The per-PHY SIFS / slot / PIFS / DIFS / EIFS table across HR-DSSS, ERP long and short slot, and OFDM, in one place.
- **[Doc · ★★ · EN]** Shankarwifi. *Multi-Link Operation (MLO) Modes — 802.11 Protocol Library*. <https://shankarwifi.com/mlo-visualizer>
  - Practitioner-level detail on EML Padding Delay, EML Transition Delay and Medium Sync Delay, plus the useful datum that in-device coexistence typically yields 40–60 dB of isolation where STR wants closer to 80 dB.
- **[Doc · ★ · EN]** Ruijie. *WiFi 6 (802.11ax) Technology White Paper*.
  - The trigger-frame Common Info / Per User Info breakdown and the trigger-type table in their most quotable form.
- **[Doc · ★ · EN]** Wait, but Wi-Fi? *Interframe Space Basics*. <https://waitbutwifi.com/interframe-space-basics/>
  - A short, correct refresher on why the interframe-space ordering is the priority ordering.

### Measurement and trial reports

- **[Report · ★★ · EN]** Wireless Broadband Alliance, NextGen Work Group. *Wi-Fi 7 MLO Enterprise Field Trials Report (Phase 2)*, with AT&T, Ruckus Networks and Intel, v1.0.0, March 2026. <https://wballiance.com/wi-fi-7-mlo-trial-att-ruckus-intel-enterprise/>
  - The measured EMLSR numbers: under co-channel interference at 40/40 MHz, DL 317.2 → 558.0 Mbps and UL 244.8 → 528.8 Mbps, latency −44% DL and −66% UL; clean spectrum at 40/40 MHz, +42.2% DL and +139.9% UL; at 40/160 MHz only +2.9% DL. Read the width column, not the headline.
- **[Paper · ★★ · EN]** "IEEE 802.11be Wi-Fi 7: Feature Summary and Performance Evaluation." arXiv:2309.15951.
  - A consolidated feature-and-numbers reference for the EHT scheduling surface.
- **[Paper · ★ · EN]** "Understanding Multi-link Operation in Wi-Fi 7: Performance, Anomalies, and Solutions." arXiv:2210.07695.
  - The anomalies side of MLO, which is where a scheduler engineer actually spends their time.

### Uplink random access

- **[Doc · ★★ · EN]** IEEE P802.11. *Default UORA parameters*, document 11-19/0006r3. <https://mentor.ieee.org/802.11/dcn/19/11-19-0006-03-00ax-cr-default-uora-parameters.docx>
  - Where `OCWmin = 7` / `OCWmax = 31` comes from, and the reasoning behind the default.
- **[Paper · ★ · EN]** "OFDMA Backoff Control Scheme for Improving Channel Efficiency in the Dynamic Network Environment of IEEE 802.11ax WLANs." *Sensors*, vol. 21, no. 15, 2021, article 5111 · DOI 10.3390/s21155111
  - The EOCW tuning problem stated properly: more RUs speeds the countdown without reducing collision probability.
- **[Paper · ★ · EN]** "An Efficient Backoff Procedure for IEEE 802.11ax Uplink OFDMA-Based Random Access." *IEEE Xplore* document 9669929.
  - The complementary view — reducing collisions rather than reducing countdown time.
- **[Doc · ★ · EN]** EURECOM. *Analysis of uplink OFDMA in 802.11ax networks*. <http://www.eurecom.fr/fr/publication/6316/download/comsys-publi-6316.pdf>
  - Simulation-based quantification of when triggered access pays for itself, which is the question §5.2's ~500–800 µs figure is trying to answer.

---

## 03-1 · Wireless Sensor Networks and Low-Power MAC

### Books

- **[Book · CN · ★★★]** 《无线传感器网络》 — 孙利民, 李建中, 陈渝, 朱红松 · 清华大学出版社, 2005 · ISBN 9787302106937
  - The standard Chinese WSN reference, in three parts: communication protocols (topology control, routing, MAC, and the short-range low-power wireless standard IEEE 802.15.4); supporting technologies (localisation, time synchronisation, security, data management and data fusion); and application technologies (node hardware platforms, the nesC programming language, and TinyOS). Covers LEACH-class clustering routing and the energy-model reasoning that still underpins UAV-assisted collection and AoI scheduling.
- **[Book · EN · ★]** *Wireless Sensor Networks: An Information Processing Approach* — Feng Zhao, Leonidas Guibas · Morgan Kaufmann, 2004
  - Frames a sensor network as a distributed information-processing system rather than a networking problem. Good for the algorithmic/in-network-processing angle.

### Papers

- **[Paper · EN · ★★★]** "Age of Information: An Introduction and Survey" — R. D. Yates, Y. Sun, D. R. Brown, S. K. Kaul, E. Modiano, S. Ulukus · *IEEE Journal on Selected Areas in Communications*, vol. 39, no. 5, pp. 1183–1210, 2021
  - The definitive AoI survey: definitions, queueing models, scheduling policies and the metric's relationship to latency. This is the bridge between WSN status-update design and the Wi-Fi 8 / 6G determinism agenda.
- **[Paper · EN · ★★★]** "Real-time status: How often should one update?" — S. Kaul, R. Yates, M. Gruteser · *IEEE INFOCOM 2012*, pp. 2731–2735
  - The paper that established AoI. Short, foundational, and worth citing by name.
- **[Paper · EN · ★★]** "The Age of Information: Real-Time Status Updating by Multiple Sources" — R. D. Yates, S. K. Kaul · *IEEE Transactions on Information Theory*, vol. 65, no. 3, pp. 1807–1827, 2019
  - The queueing-theoretic treatment for multi-source systems, including FCFS and LCFS variants and the feasible average-age region.
- **[Paper · ★★]** **IEEE 802.15.4 / 802.15.4e (TSCH)** standards and the **6TiSCH** architecture (IETF RFC 8180, "Minimal IPv6 over the TSCH Mode of IEEE 802.15.4e (6TiSCH) Configuration")
  - The deterministic low-power MAC that industrial WSN converged on. RFC 8180 is the concrete, implementable reference.

---

## 04-1 · Embedded Systems, RTOS and Hardware Interfaces

### Books

- **[Book · EN · ★★★]** *Mastering the FreeRTOS Real Time Kernel — A Hands On Tutorial Guide* — Richard Barry · FreeRTOS; release v1.1.0, 19 August 2024 (references FreeRTOS V10.6.2)
  - The official kernel book, freely available with companion source. Covers tasks, scheduling, queues, semaphores and mutexes, direct-to-task notifications, stream and message buffers, memory management, and priority inheritance. Read this alongside the source; the context-switch and tick-handling detail is what separates real RTOS understanding from API familiarity.
- **[Book · EN · ★★]** *Making Embedded Systems: Design Patterns for Great Software*, 2nd ed. — Elecia White · O'Reilly, 2021
  - Practical patterns for resource-constrained firmware: state machines, hardware abstraction, debugging without a debugger, and how to structure code you can actually test on target.
- **[Book · EN · ★★]** *Embedded Systems Architecture: Explore System-Level Design and Advanced Features* — Daniele Lacamera · Packt, 2nd ed. 2021
  - System-level view: boot sequence, linker scripts and memory layout, interrupt and exception handling, RTOS integration, and the build/flash/debug flow. Good for connecting bare-metal mechanics to the Linux view in note 04-2.
- **[Book · EN · ★★★]** *Hard Real-Time Computing Systems: Predictable Scheduling Algorithms and Applications*, 3rd ed. — Giorgio C. Buttazzo · Springer, 2011
  - The rigorous treatment of schedulability analysis, rate-monotonic and EDF scheduling, priority inversion and aperiodic servers. This is what makes a "hard real-time" claim defensible rather than rhetorical.
- **[Book · EN/CN · ★★]** *Computer Organization and Design RISC-V Edition* (see §07-1)
  - For the cache-coherency, memory-barrier and DMA-consistency reasoning that embedded work depends on.

### Papers and documentation

- **[Doc · ★★★]** **FreeRTOS kernel documentation and reference manual** (freertos.org)
  - The authoritative API reference and porting guide. Note the LTS releases (for example the 202604.00-LTS libraries) and the SMP support, both relevant to multi-core embedded design.
- **[Standard · ★]** **IEEE Std 802.15.4-2020** — Low-Rate Wireless Personal Area Networks (LR-WPANs)
  - The PHY/MAC baseline for most low-power sensor radios.
- **[Standard · ★]** **CAN / ISO 11898-1:2015** — Road vehicles; Controller area network; Part 1: Data link layer and physical signalling
  - The canonical CAN reference if your hardware-interface discussion covers automotive or industrial buses.
- **[Doc · ★★]** **ARM Cortex-M documentation: NVIC, MPU, SysTick, and the ARMv8-M TrustZone / PACBTI extensions**
  - Exception model and memory-protection mechanics that RTOS ports actually depend on.

---

## 04-2 · Linux Embedded Development — Drivers, Applications and Core Subsystems

### Books — driver development

- **[Book · EN/CN · ★★★]** *Linux Device Drivers*, 3rd ed. — Jonathan Corbet, Alessandro Rubini, Greg Kroah-Hartman · O'Reilly, 2005 · ISBN 9780596005900 · Chinese 《Linux设备驱动程序(第3版)》, translated by 魏永明, 耿岳, 钟书毅 · 中国电力出版社, 2006 · ISBN 9787508338637
  - The classic. Written against kernel 2.6.10, so the subsystem-specific chapters (PCI, USB) are dated, but the chapters on the character-device model, concurrency and locking, blocking I/O, memory allocation, interrupts, time and the memory-mapping/DMA chapter remain the clearest exposition available. Read it for the model; cross-check current APIs against the kernel tree.
- **[Book · CN · ★★★]** 《Linux设备驱动开发详解》 — 宋宝华 · 人民邮电出版社; 1st ed. 2008 (ISBN 9787115172396), 2nd ed. 2010 (ISBN 9787115236579)
  - The standard Chinese driver book, grounded in real ARM board work (LDD6410, Linux 2.6). Covers spinlocks, semaphores, completions, top-half/bottom-half interrupt handling, timers, and I/O mapping, then walks char, block, TTY, I2C, LCD, audio, USB, network and PCI device drivers. Strong on the *framework-per-subsystem* idea.
- **[Book · EN · ★★]** *Linux Device Drivers Development*, 2nd ed. — John Madieu · Packt, 2022
  - A modern, device-tree-first update in the spirit of LDD3: regmap, IIO, and the current kernel APIs. Use it to correct what LDD3 leaves stale.
- **[Book · EN · ★★]** *Linux Driver Development for Embedded Processors*, 2nd ed. — Alberto Liberal de los Ríos · self-published
  - ARM-focused, with complete runnable examples on Raspberry Pi and i.MX covering device tree, GPIO, I2C, SPI, UART and USB. The fastest path from "I understand the model" to "my driver enumerates and probes".

### Books — kernel internals

- **[Book · EN/CN · ★★★]** *Understanding the Linux Kernel*, 3rd ed. — Daniel P. Bovet, Marco Cesati · O'Reilly · Chinese 《深入理解Linux内核(第三版)》, translated by 陈莉君, 张琼声, 张宏伟 · 中国电力出版社, 2007 · ISBN 9787508353944
  - The structure of the kernel: process and memory management, the VFS, block I/O, and the interrupt/exception paths. Read for the conceptual architecture; verify current behaviour against the source, since the kernel has moved on.
- **[Book · EN · ★★]** *Linux Kernel Development*, 3rd ed. — Robert Love · Addison-Wesley, 2010
  - Concise, current-for-its-era account of process scheduling, the interrupt handler path, kernel synchronisation and the VFS. Written by a kernel contributor with an emphasis on *why* the code is shaped that way.
- **[Book · EN · ★★]** *Linux Kernel Networking: Implementation and Theory* — Rami Rosen · Apress, 2013
  - The kernel network stack in detail: `sk_buff`, netfilter, the routing and neighbour subsystems, and the driver interface. Use alongside the DPDK material in §08.
- **[Book · EN · ★]** *Understanding Linux Network Internals* — Christian Benvenuti · O'Reilly, 2005 (see §05-1)

### Books — system and application programming

- **[Book · EN · ★★★]** *The Linux Programming Interface* — Michael Kerrisk · No Starch Press, 2010
  - The definitive system-programming reference: processes, threads, IPC, signals, timers, file I/O, memory mapping, and sockets. Over 1500 pages, with every syscall documented against its behaviour. This is the book to own for the IPC and networking sections of note 04-2.
- **[Book · EN · ★★]** *Linux System Programming*, 2nd ed. — Robert Love · O'Reilly, 2013
  - Shorter and more opinionated, covering the same ground with more emphasis on writing correct and efficient code. Good complement to Kerrisk.
- **[Book · EN/CN · ★★★]** *UNIX Network Programming, Vol. 1: The Sockets Networking API*, 3rd ed. — W. Richard Stevens, Bill Fenner, Andrew M. Rudoff · Chinese 《UNIX网络编程 卷1:套接字联网API(第3版)》, translated by 杨继张 · 人民邮电出版社, 2010 · ISBN 9787115228406 (2019 printing ISBN 9787115517791)
  - The socket reference: TCP/UDP/SCTP, the elementary and advanced socket APIs, I/O models (`select`/`poll`/`epoll`), non-blocking I/O, broadcast and multicast, and client/server design alternatives. All examples are real, runnable code. Read chapters 6, 15–16 and 30 before any serious network-service work.
- **[Book · EN/CN · ★★]** *TCP/IP Illustrated, Vol. 1: The Protocols* — W. Richard Stevens · Chinese 《TCP/IP详解 卷1:协议》
  - Packet-level protocol walkthroughs that no other book matches. Read it with a packet capture open.
- **[Book · CN · ★★]** 《UNIX环境高级编程》 (Advanced Programming in the UNIX Environment) — W. Richard Stevens, Stephen A. Rago
  - The Chinese standard for UNIX/Linux system programming fundamentals, and the usual reference for signal handling, daemonisation and file I/O semantics in Chinese-language teams.

### Books — embedded Linux and build systems

- **[Book · EN/CN · ★★★]** *Embedded Linux Primer: A Practical, Real-World Approach*, 2nd ed. — Christopher Hallinan · Prentice Hall · Chinese 《嵌入式Linux基础教程》, 人民邮电出版社; 1st ed. 2009 (ISBN 9787115215222), 2nd ed. 2012, translated by 周鹏 (ISBN 9787115278272)
  - The engineering picture in one volume: bootloaders, kernel initialisation, cross-compilation, file systems, flash/MTD, and debugging (including KGDB/gdb). The 2nd edition adds udev, USB and open build systems.
- **[Book · EN · ★★★]** *Mastering Embedded Linux Programming*, 3rd ed. — Chris Simmonds (with Frank Vasquez) · Packt, 2021
  - The most current end-to-end text: toolchains, U-Boot, kernel configuration, Buildroot versus Yocto, root filesystem construction, and driver interaction. Chapter 6 (choosing a build system) and chapter 11 (interacting with device drivers) are the two most useful.
- **[Book · EN · ★★]** *Building Embedded Linux Systems*, 2nd ed. — Karim Yaghmour, Jon Masters, Gilad Ben-Yossef, Philippe Gerum · O'Reilly, 2008
  - Deeper on BSP construction: toolchain internals, kernel configuration, root filesystem assembly, booting and power management. The BSP engineer's reference.

### Documentation

- **[Doc · ★★★]** **Linux kernel Documentation/** (in-tree) — and in particular `core-api/`, `driver-api/`, `devicetree/bindings/`, `scheduler/`, `networking/` and `virt/`
  - The authoritative and current reference. Device tree bindings are the stable ABI; read them before writing or reviewing a binding.
- **[Doc · ★★★]** **Yocto Project documentation** (mega-manual, BSP Developer's Guide, Kernel Development Manual) and **Buildroot user manual**
  - The two build-system references that matter. Use the Yocto LTS release names recorded in note 04-2 when citing versions.
- **[Doc · ★★]** **U-Boot documentation** and **Device Tree Specification** (devicetree.org)
  - Boot chain and hardware description. The DT spec is short; read it once properly.
- **[Doc · ★★]** **cyclictest / rt-tests documentation** and the **PREEMPT_RT wiki**
  - Real-time verification tooling. PREEMPT_RT was merged into mainline in Linux 6.12 for x86, arm64 and RISC-V; 32-bit ARM followed later.

---

## 04-3 · Embedded Software Architecture — Patterns, Layering and Wireless System Structure

### Books — architecture and design method

- **[Book · ★★★ · EN]** **Making Embedded Systems: Design Patterns for Great Software**, 2nd ed. — Elecia White, O'Reilly, 2024. ISBN 9781098151546. The most readable entry point into embedded architecture as a *design* discipline rather than a driver catalogue. Chapter 2 ("Creating a System Architecture") is the one to read before an interview; the second edition adds IoT/networked sensors, motors and data-handling strategy. Chapters on reducing RAM, code space and power are directly quotable.
- **[Book · ★★★ · EN]** **Embedded Systems Architecture**, 2nd ed. — Daniele Lacamera, Packt, Jan 2023. ISBN 9781803239545 (342 pp.). Chapter 3 is literally "Architectural Patterns"; also covers boot-up procedure, memory management, distributed/IoT architecture, parallel tasks and scheduling, and Trusted Execution Environment. Good coverage of the memory-isolation-oriented view of RTOS design.
- **[Book · ★★ · EN]** **Software Engineering for Embedded Systems: Methods, Practical Techniques, and Applications**, 2nd ed. — Robert Oshana and Mark Kraeling (eds.), Newnes/Elsevier, 2019. ISBN 978-0-12-809448-8 (1st ed. 2013, ISBN 978-0-12-415917-4). Multi-author reference; the relevant chapters are on architecture and design patterns, real-time building blocks, safety-critical development, and multicore software development. Contributors include Jean Labrosse and Bruce Douglass.
- **[Book · ★★ · EN]** **Better Embedded System Software** — Philip Koopman, Drumnadrochit Education, 2010. ISBN 978-0-9844490-0-2. Short, opinionated and practice-driven: requirements, design, implementation and test discipline specifically for embedded. Strong on the failure modes that architecture should prevent.
- **[Book · ★ · EN]** **The Art of Designing Embedded Systems**, 2nd ed. — Jack Ganssle, Newnes, 2008. Essays rather than a textbook; useful for the project-reality side (estimation, firmware process, why projects fail). `VERIFY` the exact edition/ISBN before citing.

### Books — execution models, scheduling and time-triggered design

- **[Book · ★★★ · EN]** **Hard Real-Time Computing Systems: Predictable Scheduling Algorithms and Applications**, 3rd ed. — Giorgio C. Buttazzo, Springer, 2011. ISBN 978-1-4614-0676-1, DOI 10.1007/978-1-4614-0676-1 (Real-Time Systems Series, vol. 24). The standard text for the scheduling theory in note 04-3 §2.3: periodic and aperiodic task scheduling, fixed- and dynamic-priority servers, resource access protocols, limited-preemptive scheduling, overload handling, kernel and application design issues.
- **[Book · ★★ · EN]** **Real-Time Systems and Programming Languages**, 4th ed. — Alan Burns and Andy Wellings, Addison-Wesley, 2009. Broader than Buttazzo: covers the language and OS support for real-time (Ada, Real-Time Java, real-time POSIX, Ada/RT scheduling). Good for the "what does the platform actually give you" question.
- **[Book · ★★ · EN]** **Patterns for Time-Triggered Embedded Systems: Building Reliable Applications with the 8051 Family of Microcontrollers** — Michael J. Pont, Addison-Wesley, 2001. ISBN 0-201-33138-1 / 9780201331387. The canonical catalogue of time-triggered architecture patterns (70+). Free PDF from the author's site. 8051-flavoured, which is dated — read it for the *patterns*, not the silicon.
- **[Book · ★★★ · EN]** **The Engineering of Reliable Embedded Systems**, 2nd ed. — Michael J. Pont, SafeTTy Systems, 2016/2017. ISBN 978-0-9930355-3-1. The successor to PTTES and the one to cite for safety work: second-generation time-triggered architectures, with worked case studies targeting IEC 61508 SIL 2, IEC 60730 Class B, IEC 62304 Class C, ISO 26262 ASIL D and DO-178C Level A.

### Books — state machines and event-driven architecture

- **[Book · ★★★ · EN]** **Practical UML Statecharts in C/C++: Event-Driven Programming for Embedded Systems**, 2nd ed. — Miro Samek, Newnes/Elsevier, 2008/2009. ISBN 978-0-7506-8706-5. The definitive text: UML statecharts, hierarchical state machines, run-to-completion, inversion of control, event queues, and the design study of the QP event-driven framework (including the QEP hierarchical event processor). Read Part II even if you never use QP — the argument for RTC over blocking is the architectural core.
- **[Book · ★ · EN]** **Design Patterns: Elements of Reusable Object-Oriented Software** — Gamma, Helm, Johnson, Vlissides (GoF), Addison-Wesley, 1994. ISBN 978-0-201-63361-0. The source catalogue for §4. Read it knowing that the embedded cost accounting differs: virtual dispatch, object size and allocation are all first-class costs on a microcontroller.

### Papers — scheduling theory

- **[Paper · ★★★ · EN]** Liu, C. L. and Layland, J. W., **"Scheduling Algorithms for Multiprogramming in a Hard-Real-Time Environment"**, *Journal of the ACM* 20(1): 46–61, 1973. The founding paper: rate-monotonic priority assignment is optimal among fixed-priority schemes for implicit deadlines; utilization bound `n(2^(1/n) − 1)` tending to `ln 2 ≈ 0.693`; EDF is feasible up to `U ≤ 1`.
- **[Paper · ★★ · EN]** Sha, L., Rajkumar, R. and Lehoczky, J. P., **"Priority Inheritance Protocols: An Approach to Real-Time Synchronization"**, *IEEE Transactions on Computers* 39(9): 1175–1185, 1990. The reference for priority inheritance and ceiling protocols — the standard answer to priority inversion.
- **[Paper · ★★ · EN]** Baker, T. P., **"A Stack-Based Resource Allocation Policy for Realtime Processes"**, IEEE Real-Time Systems Symposium, 1990. Stack Resource Policy: the bound-optimal approach that also yields the best known worst-case stack requirement.
- **[Paper · ★★ · EN]** Leung, J. Y.-T. and Whitehead, J., **"On the Complexity of Fixed-Priority Scheduling of Periodic, Real-Time Tasks"**, *Performance Evaluation* 2(4): 237–250, 1982. Deadline-monotonic priority ordering.
- **[Paper · ★ · EN]** Audsley, N. C., Burns, A., Richardson, M. F. and Wellings, A. J., **"Hard Real-Time Scheduling: The Deadline-Monotonic Approach"** (1991) and **"Applying New Scheduling Theory to Static Priority Pre-emptive Scheduling"** (1993). Audsley's Optimal Priority Assignment: an optimal ordering in at most `n(n+1)/2` tests, plus the release-jitter extensions.
- **[Paper · ★ · EN]** Buttazzo, G. C., **"Rate Monotonic vs. EDF: Judgment Day"**. A systematic demolition of the common misconceptions that favour RM over EDF. Excellent interview ammunition — it lets you answer "RM or EDF?" with the trade-offs rather than the folklore.

### Papers — safety, protection and dependability

- **[Paper · ★★ · EN]** Holzmann, G. J., **"The Power of 10: Rules for Developing Safety-Critical Code"**, *IEEE Computer* 39(6): 95–99, 2006. DOI 10.1109/MC.2006.212. NASA/JPL. Ten rules, including bounded loops, no dynamic allocation after initialisation, and restricted use of interrupts and recursion. Short enough to memorise and quote.
- **[Paper · ★★ · EN]** Zhou, W. et al., **"Good Motive But Bad Design: Why ARM MPU Has Become an Outcast in Embedded Systems"**, arXiv:1908.03638, 2019. Documents why the ARM MPU is rarely configured as intended. The credible, non-obvious point to raise when discussing memory protection and freedom from interference.
- **[Paper · ★ · EN]** Stankovic, J. A., **"Misconceptions About Real-Time Computing: A Serious Problem for Next-Generation Systems"**, *IEEE Computer* 21(10): 10–19, 1988. Still worth reading: the gap between "fast" and "predictable" is the same confusion that appears in modern latency-vs-throughput arguments.

### Standards and specifications

- **[Standard · ★★★ · EN]** **AUTOSAR Classic Platform** — current release **R25-11** (Release Event 4 December 2025). `autosar.org/standards/classic-platform`. Application / RTE / BSW layering, MCAL, Complex Drivers, and the Virtual Functional Bus. Start with *Layered Software Architecture* and *Methodology*.
- **[Standard · ★★ · EN]** **AUTOSAR Adaptive Platform** — same release train; ARA (AUTOSAR Runtime for Adaptive Applications), functional clusters, POSIX-based, service-oriented. Read alongside the **Foundation** standard for cross-platform interoperability.
- **[Standard · ★★★ · EN]** **MISRA C:2025** — current edition (updated March 2025), MISRA. Supersedes MISRA C:2023. The coding standard referenced for safety-critical C.
- **[Standard · ★★ · EN]** **MISRA C++:2023** (with TC1:2026) — current MISRA C++, written against **C++17**. Note the implication: a MISRA-conformant C++ project is not on C++20/23/26.
- **[Standard · ★★ · EN]** **ISO 26262:2018** (2nd ed., December 2018) — *Road vehicles — Functional safety*. 12 parts; Part 4 system level, Part 5 hardware, Part 6 software, Part 9 ASIL-oriented analysis, Part 11 semiconductors, Part 12 motorcycles. ASIL A–D and QM from Severity/Exposure/Controllability; SPFM/LFM/PMHF targets.
- **[Standard · ★★ · EN]** **IEC 61508** (2nd ed., 2010) — the parent functional-safety standard; SIL 1–4. Sector derivatives: IEC 61511 (process), IEC 62061/ISO 13849 (machinery), EN 5012x (rail), IEC 62304 (medical software), IEC 60730 (household), DO-178C (avionics).
- **[Spec · ★★ · EN]** **OSEK/VDX Operating System Specification 2.2.1** (2003) — the static, configurable RTOS specification that AUTOSAR OS descends from. Worth knowing conceptually: it is where the "configuration rather than code" philosophy comes from.
- **[Spec · ★★ · EN]** **ETSI TS 103859** (O-RAN.WG4.CUS.0) — O-RAN Fronthaul Control, User and Synchronization Plane. Defines the **7-2x** split, Category A/B O-RUs, eCPRI transport and IQ compression. The normative source for note 04-3 §6.3.
- **[Spec · ★ · EN]** **O-RAN.WG1 Architecture Description** and **O-RAN.WG3 (E2/E2SM)** — the architecture and near-RT RIC interface specs. See §18.
- **[Spec · ★★ · EN]** **3GPP TS 38.401** — NG-RAN architecture description, including the CU/DU split. `VERIFY` the F1/E1 part numbers before quoting them.

### Documentation and code

- **[Doc · ★★★ · EN]** **Zephyr Project documentation** — `docs.zephyrproject.org`. Releases, devicetree, Kconfig, power management, and MCUboot. Current stable **4.4.0** (2026-04-14); **3.7.0** is LTS3 (2024-07-26, EOL 2029-07-27); LTS4 planned as 5.0 (Oct 2027). Read the *release and migration guides* — they are the best available example of how a serious embedded project manages long-term compatibility.
- **[Code · ★★ · EN]** **MCUboot** — open-source secure bootloader for 32-bit MCUs, integrated with Zephyr. Study it for the A/B update, image format, signature verification and swap/overwrite strategies described in note 04-3 §9.
- **[Code · ★★ · EN]** **QP / QP/C / QP/C++** (Quantum Leaps) — the open-source active-object and hierarchical state machine framework behind Samek's book. Read `qpc` source for a production-quality HSM dispatcher and event queue implementation in C.
- **[Code · ★ · EN]** **FreeRTOS kernel** — `freertos.org`; see §07. Read its `port.c` for the PendSV context-switch mechanics that the execution model in note 04-3 §2 depends on.
- **[Doc · ★ · EN]** **MCUboot / RAUC / SWUpdate / Mender documentation** — three different answers to the same update problem; comparing them is the fastest way to internalise what is *essential* in an OTA architecture versus what is implementation detail.

---

## 04-4 · Linux Interrupts — Types, Handlers, Threaded IRQs and Deferred Work

> The general driver and kernel texts are in §04-2. This section lists the interrupt-specific sources: the three interrupt-controller specifications, the generic-IRQ and workqueue kernel documentation, the mailing-list record of the deferred-work conversion, and the real-time measurement tooling.

### Standards — interrupt controllers

- **[Spec · ★★★ · EN]** **Arm Generic Interrupt Controller Architecture Specification, GICv3 and GICv4** — Arm, **ARM IHI 0069** (`developer.arm.com`, free download)
  - The normative source for the INTID map (SGI 0–15, PPI 16–31, SPI 32–1019, special 1020–1023, LPI 8192+), the Distributor / Redistributor / CPU-interface split, the ITS, the LPI configuration in memory tables, and GICv4 direct vLPI injection. Cite the document number, not a blog post.
- **[Spec · ★★ · EN]** **Arm Generic Interrupt Controller Architecture Specification, GICv2** — Arm, **ARM IHI 0048**
  - Still what a large number of shipping embedded SoCs implement; read it to see what v3 added and why.
- **[Doc · ★★★ · EN]** **Learn the Architecture: Generic Interrupt Controller v3 and v4** — Arm developer documentation; the *Overview*, *Locality-specific Peripheral Interrupts* and *Virtualization* guides
  - The readable entry point. The INTID table and the "dedicated signal versus message" figures quoted in note 04-4 follow it.
- **[Spec · ★★ · EN]** **Intel 64 and IA-32 Architectures Software Developer's Manual, Volumes 3A and 3B** — Intel
  - The chapters on the IDT, the Local APIC, the I/O APIC, MSI, and NMI/SMI/machine-check. The x86 ground truth for §3.2 of note 04-4.
- **[Spec · ★★ · EN]** **PCI Express Base Specification** — PCI-SIG
  - The MSI and MSI-X capability structures, the 32-vector / 2048-vector limits, and the MSI-X table and PBA layout.
- **[Spec · ★★★ · EN]** **The RISC-V Advanced Interrupt Architecture, Version 1.0** — John Hauser (ed.); ratified by RISC-V International **June 2023**; document revision **2025-03-12**. `docs.riscv.org/reference/aia`
  - Chapters 3 (IMSIC), 4 (APLIC), 5 (interrupts at M and S levels), 6 (virtual machines), 7 (IPIs), 8 (IOMMU support). Released under CC BY 4.0.
- **[Spec · ★★ · EN]** **The RISC-V Instruction Set Manual, Volume II: Privileged Architecture**
  - The base external-interrupt conventions (`mip`/`mie`, major interrupt numbers) that AIA extends.

### Kernel documentation

- **[Doc · ★★★ · EN]** **Linux `Documentation/core-api/irq/`** — `docs.kernel.org/core-api/irq/`
  - The upstream description of the generic IRQ layer: `irq-domain.rst`, `irq-generic.rst`, and `concepts.rst` (which is where `irq_desc`, `irq_chip`, the flow handlers and chained versus nested chips are defined).
- **[Doc · ★★★ · EN]** **Linux `Documentation/core-api/workqueue.rst`** — `docs.kernel.org/core-api/workqueue.html`
  - The normative text for `WQ_BH`, `WQ_UNBOUND`, `WQ_HIGHPRI`, `WQ_CPU_INTENSIVE`, `WQ_MEM_RECLAIM`, and `@max_active` (maximum 512, default 256 when 0 is passed).
- **[Doc · ★★ · EN]** **Linux `Documentation/admin-guide/IRQ-affinity.rst`** — `docs.kernel.org/admin-guide/IRQ-affinity.html`
  - Affinity, `irqbalance`, and the interaction with CPU isolation.
- **[Doc · ★★★ · EN]** **Linux `Documentation/admin-guide/kernel-parameters.txt`** — `docs.kernel.org/admin-guide/kernel-parameters.html`
  - The authoritative list for `threadirqs`, `irqaffinity=`, `irqchip.gicv3_pseudo_nmi=`, `irqchip.gicv3_nolpi=`, `irqpoll`, `irqfixup`, `nmi_watchdog`.
- **[Doc · ★★★ · EN]** **Linux `Documentation/core-api/real-time/differences.rst`** — added 2025
  - The official statement of how PREEMPT_RT differs: sleeping locks, forced-threaded interrupts, and the "SCHED_FIFO priority 50" default.
- **[Doc · ★★ · EN]** **Linux `Documentation/networking/napi.rst`** and **`Documentation/networking/scaling.rst`**
  - The NAPI driver contract, and RSS / RPS / RFS / XPS.
- **[Doc · ★★ · EN]** **Linux `Documentation/core-api/genericirq.rst`** (formerly `IRQ.txt`) and the in-tree **`Documentation/driver-api/irq`** material — the historical names are worth knowing because many secondary sources still cite them.

### Papers and mailing-list records

- **[Paper · ★★★ · EN]** Eric Dumazet, **"softirq: reduce latencies"** — LKML, 2013-01-03. `<lkml.iu.edu/hypermail/linux/kernel/1301.0/00627.html>`
  - The patch that added the 2 ms time budget on top of the 10-restart limit. The commit message is the best short explanation of why the softirq loop needs a brake.
- **[Paper · ★★★ · EN]** Tejun Heo, **"[PATCHSET wq/for-6.9] workqueue: Implement BH workqueue and convert several tasklet users"** — LKML, 2024-01-30; and **"[GIT PULL] workqueue changes for v6.9"**, 2024-03-11
  - The primary record of why `WQ_BH` exists, what its constraints are, and what the conversion is expected to achieve.
- **[Paper · ★★ · EN]** Julien Thierry, **"arm64: Enable the support of pseudo-NMIs"** — LKML, v6 2018-11 and v7 2018-12
  - The series that introduced `CONFIG_ARM64_PSEUDO_NMI` and the boot parameter.
- **[Paper · ★★ · EN]** Anup Patel, **"Linux RISC-V AIA Support"** (v12 v16) — LKML and Patchwork, 2024-01 to 2024-03
  - The authoritative description of what APLIC and IMSIC each do in the kernel, and of their dependencies on the per-device MSI domain work.
- **[Paper · ★ · EN]** The **tasklet-removal** discussions on LKML: Steven Rostedt's 2007 proposal, the 2019 2020 API-modernisation thread, and the 2024 `WQ_BH` decision
  - Cited for the history of a decision, not for any number. Reading them is how you learn to say "deprecated, conversion ongoing" with a straight face.

### Books

- **[Book · ★★ · EN]** **Mastering Linux Device Driver Development** — John Madieu · Packt, January 2021 · ISBN 978-1-78934-204-8
  - Chapter 1 (*Linux Kernel Concepts for Embedded Developers*) is the one that matters here: kernel locking helpers, work-deferral mechanisms and interrupt management, written against a recent kernel. Use it to check that a habit you learned from LDD3 still applies.
- **[Book · ★★ · EN]** **Operating System Concepts**, 10th ed. — Abraham Silberschatz, Peter B. Galvin, Greg Gagne · Wiley, 2018 · ISBN 978-1-119-32091-3
  - Chapter 12 (I/O systems) and the chapters on interrupts and scheduling. Use for the vocabulary that predates and outlives Linux: synchronous versus asynchronous, vectored versus polled, and the interrupt-handling model in general.

### Tools

- **[Tool · ★★★ · EN]** **rt-tests** — `cyclictest`, `hwlatdetect`, `osnoise`, `signaltest`. `wiki.linuxfoundation.org/realtime/documentation/`
  - `cyclictest` for worst-case wakeup latency; `hwlatdetect` for SMI/SMM and other latencies the kernel cannot see.
- **[Tool · ★★ · EN]** **trace-cmd and KernelShark** — recording and visualising IRQ entry/exit, softirq and scheduling events.
- **[Tool · ★★ · EN]** **util-linux** — `irqtop` for a live sorted view of `/proc/interrupts`; `taskset` and `chrt` for affinity and priority.
- **[Tool · ★★ · EN]** **perf** — `perf top/record/report`, `perf probe`, and the `irq:irq_handler_entry` / `irq:softirq_entry` tracepoints.

---

## 04-5 · Linux Concurrency — Kernel and User Mode, Processes, Threads and IPC

> Kerrisk's *The Linux Programming Interface* is listed in §04-2 and remains the owner of the user-space API; this section collects the concurrency-specific material around it: the POSIX text, the futex primary sources, the memory-model theory, and the race and contention tooling.

### Standards

- **[Standard · ★★★ · EN]** **The Open Group Base Specifications, Issue 7 (POSIX.1-2017)** — `pubs.opengroup.org/onlinepubs/9699919799/`
  - The normative text for processes, threads, mutexes, condition variables, and every IPC mechanism in §7 of note 04-5. Merrily paraphrased everywhere, so quote from here.
- **[Standard · ★★★ · EN]** **IEEE Std 1003.1c-1995** — the POSIX threads amendment
  - Where `pthread_create`, `pthread_mutex_t`, condition variables and thread-specific data come from.
- **[Standard · ★★ · EN]** **ISO/IEC 9899:2018 (C17)** and the current **C23** — §7.17 `<stdatomic.h>` and the memory-model clauses
  - The C-side view of `memory_order_*`; the enumeration is the same one C++ uses. **ISO/IEC 14882 (C++20 / C++23)** — `[[atomics.order]]` — is the C++ text.

### Books — the API

- **[Book · ★★★ · EN]** **Advanced Programming in the UNIX Environment**, 3rd ed. — W. Richard Stevens, Stephen A. Rago · Addison-Wesley, 2013 · ISBN 978-0-321-63773-4
  - Chapters 8 (process control), 11 (threads), 12 (thread control) and 15 17 (IPC). The classic treatment of the process lifecycle, `fork`/`exec`/`wait`, and the original presentation of the pipe, FIFO, message-queue, semaphore and shared-memory mechanisms.
- **[Book · ★★★ · EN]** **UNIX Network Programming, Volume 2: Interprocess Communications**, 2nd ed. — W. Richard Stevens · Prentice Hall, 1999 · ISBN 0-13-081081-9
  - The most detailed treatment of POSIX IPC, Unix domain sockets, `SCM_RIGHTS` and shared memory available. Chapters 5, 12 and 15 are the sources for §7 of note 04-5; appendix A is the most useful IPC-mechanism comparison table ever printed.

### Books — the theory and the primitives

- **[Book · ★★★ · EN]** **Is Parallel Programming Hard, And, If So, What Can You Do About It?** — Paul E. McKenney (`perfbook`, continuously updated, free)
  - The single most practical text on memory ordering, locking, lock-free techniques and deferred processing. Read the memory-ordering and counting chapters before designing anything lock-free, and the deferred-processing chapter before arguing about workqueues.
- **[Book · ★★★ · EN]** **The Art of Multiprocessor Programming**, 2nd ed. — Maurice Herlihy, Nir Shavit · Morgan Kaufmann, 2020 · ISBN 978-0-12-397337-5 (1st ed. 2008, ISBN 978-0-12-370591-4)
  - Linearisability, spin locks, concurrent queues and stacks. The correctness standards that make "my lock-free ring is fine" a checkable claim.
- **[Book · ★★ · EN]** **Modern Operating Systems**, 4th ed. — Andrew S. Tanenbaum, Herbert Bos · Pearson, 2015 · ISBN 978-0-13-359162-0
  - Chapters 2 (processes and threads), 6 (deadlock) and 7 for the OS-theory grounding: the dining philosophers, the readers-writers problem, and why IPC is presented as a scheduling problem.
- **[Book · ★★ · EN]** **Operating System Concepts**, 10th ed. — Abraham Silberschatz, Peter B. Galvin, Greg Gagne · Wiley, 2018 · ISBN 978-1-119-32091-3
  - Chapters 3 7: processes, threads, CPU scheduling and synchronisation.

### Papers

- **[Paper · ★★★ · EN]** Hubertus Franke, Rusty Russell, Matthew Kirkwood, **"Fuss, Futexes and Furwocks: Fast Userlevel Locking in Linux"** — *Ottawa Linux Symposium 2002*, pp. 479 495. `kernel.org/doc/ols/2002/ols2002-pages-479-495.pdf`
  - The primary source for §6.3: the design, the earlier approaches it replaced, and the benchmarks that justified it.
- **[Paper · ★★★ · EN]** Ulrich Drepper, **"Futexes Are Tricky"** — Red Hat
  - The document to read before using a bare futex instead of a mutex. Its existence is the argument.
- **[Paper · ★★ · EN]** Maged M. Michael and Michael L. Scott, **"Simple, Fast, and Practical Non-Blocking and Blocking Concurrent Queue Algorithms"** — *PODC 1996*
  - The reference lock-free queue; the standard against which a hand-rolled ring should be measured.
- **[Paper · ★★ · EN]** Lamport, L., **"Time, Clocks, and the Ordering of Events in a Distributed System"** — *Communications of the ACM* 21(7): 558 565, 1978
  - The origin of the happens-before relation.
- **[Paper · ★★ · EN]** Herlihy, M. and Wing, J. M., **"Linearizability: A Correctness Condition for Concurrent Objects"** — *ACM TOPLAS* 12(3): 463 492, 1990
  - The correctness condition for concurrent objects.
- **[Paper · ★★ · EN]** Adve, S. V. and Gharachorloo, K., **"Shared Memory Consistency Models: A Tutorial"** — *IEEE Computer* 29(12): 66 76, 1996
  - Why relaxed ordering exists and what it permits.
- **[Paper · ★★ · EN]** Silas Boyd-Wickizer et al., **"An Analysis of Linux Scalability to Many Cores"** — *OSDI 2010*
  - The measurement that motivated a decade of per-CPU and lock-free kernel work.
- **[Paper · ★★ · EN]** Tudor David, Rachid Guerraoui, Vasileios Trigonakis, **"Everything You Always Wanted to Know About Synchronization but Were Afraid to Ask"** — *SOSP 2013*
  - A systematic empirical comparison; the antidote to "lock-free is faster".
- **[Paper · ★★ · EN]** Hans-J. Boehm, **"Threads Cannot Be Implemented as a Library"** — *PLDI 2004*
  - The argument that forced a memory model into C11 and C++11; the reason §6.2 of note 04-5 exists at all.

### Documentation and code

- **[Doc · ★★★ · EN]** **Linux man-pages** — `man7.org/linux/man-pages/`. The directly relevant pages: `futex(2)`, `futex(7)`, `clone(2)`, `clone3(2)`, `set_tid_address(2)`, `pthreads(7)`, `sched(7)`, `cgroups(7)`, `namespaces(7)`, `mq_overview(7)`, `sem_overview(7)`, `svipc(7)`, `shm_overview(7)`, `memfd_create(2)`, `eventfd(2)`, `signalfd(2)`, `timerfd_create(2)`, `pidfd_open(2)`, `io_uring(7)`, `unix(7)`, `epoll(7)`
  - Maintained with authoritative VERSIONS sections, which is how you check when a syscall appeared without reading the git history.
- **[Doc · ★★ · EN]** **Linux `Documentation/scheduler/`** and **`Documentation/locking/`** — `docs.kernel.org`
  - Scheduler policies, EEVDF and `SCHED_DEADLINE`; and the kernel's own statement of its locking rules.
- **[Code · ★★★ · EN]** **glibc NPTL sources** (`nptl/`) — in particular `pthread_mutex_lock.c` and `pthread_cond_wait.c`
  - The actual implementation. Reading it alongside §6 is the fastest way to internalise why the uncontended path has no syscall.
- **[Code · ★★ · EN]** **the kernel's `kernel/futex/`** — the `futex_q`, `futex_hash_bucket` and PI state machinery
  - The kernel side of the primitive, including why private and shared futexes are keyed differently.

### Tools

- **[Tool · ★★★ · EN]** **ThreadSanitizer (TSan)** — GCC and Clang, `-fsanitize=thread`
  - The default tool for data races. If you only add one thing to a concurrency test plan, add this.
- **[Tool · ★★ · EN]** **rr** (`rr-project.org`) — record and replay
  - Makes a racy failure deterministic, which is otherwise the hardest part of debugging concurrency.
- **[Tool · ★★ · EN]** **valgrind / helgrind** — race and lock-order detection without a rebuild; slower, but it needs no instrumentation.
- **[Tool · ★★ · EN]** **perf** (`perf sched record`, `perf sched latency`) and **trace-cmd / KernelShark** with the `sched_switch` and `sched_wakeup` tracepoints
  - The visual timeline of who ran when, and who waited for whom.

---

## 01-6 · NR DU MAC Scheduler — Resource Allocation, HARQ and Real-Time Implementation

### Standards

- **[Standard · ★★★]** 3GPP. *TS 38.321 — Medium Access Control (MAC) protocol specification*. <https://www.etsi.org/deliver/etsi_TS/138300_138399/138321/>
  - Clause 5.4.3.1 logical channel prioritisation, 5.4.4 scheduling request, 5.4.5 buffer status reporting, 5.7 power headroom, 5.13 DRX. The normative source for what the scheduler is obliged to do.
- **[Standard · ★★★]** 3GPP. *TS 38.213 — Physical layer procedures for control*. <https://www.etsi.org/deliver/etsi_TS/138200_138299/138213/>
  - Clause 10.1: the CCE aggregation levels (Table 10.1-1), the per-slot candidate budget (10.1-2) and the non-overlapped-CCE budget (10.1-3). Clause 9.2.1 PUCCH resource sets, 9.2.3 HARQ-ACK timing, 11.2 uplink power control. These three clauses are the whole of §9 and §8.4.
- **[Standard · ★★★]** 3GPP. *TS 38.214 — Physical layer procedures for data*, v18.9.0 (ETSI TS 138 214 V18.9.0). <https://www.etsi.org/deliver/etsi_ts/138200_138299/138214/18.09.00_60/ts_138214v180900p.pdf>
  - Clause 5.1 the 16-process maximum and the default of 8, 5.1.3.1 the MCS tables, 5.1.3.2 TBS determination, 5.3 the PDSCH processing time N1, 6.4 the PUSCH preparation time N2. The two timing tables in 5.3 and 6.4 set every k1 and k2 in the note.
- **[Standard · ★★★]** 3GPP. *TS 38.211 — Physical channels and modulation*. <https://www.etsi.org/deliver/etsi_TS/138200_138299/138211/>
  - Clause 7.3.2 the CORESET and REG/CCE structure, 7.3.2.1 the supported aggregation levels, 7.4 the PDSCH DMRS patterns that the TBS computation subtracts.
- **[Standard · ★★]** 3GPP. *TS 38.331 — Radio Resource Control (RRC) protocol specification*. <https://www.etsi.org/deliver/etsi_TS/138300_138399/138331/>
  - `PDSCH-ServingCellConfig`, `PDSCH-Config`, `PUSCH-Config`, `PDCCH-Config`, `PUCCH-Config`, `ConfiguredGrantConfig`, `DRX-Config`. Every bound a scheduler must respect is an ASN.1 constraint in here.
- **[Standard · ★★]** 3GPP. *TS 38.212 — Multiplexing and channel coding*. <https://www.etsi.org/deliver/etsi_TS/138200_138299/138212/>
  - Clause 5.4.2 rate matching and the limited buffer rate matching circular buffer `Ncb = min(N, Nref)`; clause 5.2.2 the base-graph selection behind the 3824-bit TBS threshold.
- **[Standard · ★★]** 3GPP. *TS 38.300 — NR; Overall description; Stage 2*. <https://www.etsi.org/deliver/etsi_TS/138300_138399/138300/>
  - Clause 16 the CU/DU split and which node owns what — the reason the scheduler is in the DU at all.
- **[Standard · ★]** 3GPP. *TS 38.306 — UE radio access capabilities*. <https://www.etsi.org/deliver/etsi_TS/138300_138399/138306/>
  - Where the 16- versus 32-process HARQ capability and the PDCCH monitoring capability are signalled. A scheduler is bounded by what the UE reports, not by what the network would like.
- **[Standard · ★]** 3GPP. *TS 38.473 — F1 application protocol (F1AP)*. <https://www.etsi.org/deliver/etsi_TS/138400_138499/138473/>
  - UE Context Setup and Modification: the procedures that create and mutate the contexts the scheduler reads in every slot.
- **[Doc · ★★]** i TecSpec. *TS 38.213 §9.2.1 — PUCCH Resource Sets*. <https://itecspec.com/3gpp/38.213/s/9.2.1>
  - The exact text for the four sets, the 32-resource first set, the 8-resource others and the `maxPayloadSize` selection rule.
- **[Doc · ★★]** i TecSpec. *TS 38.331 — Multiplicity and type constraint definitions*. <http://itecspec.com/3gpp/38.331/s/multiplicity-and-type-constraint-definitions>
  - `maxNrofPUCCH-Resources = 128`, `maxNrofPUCCH-ResourceSets = 4`, `maxNrofPUCCH-ResourcesPerSet = 32`, `maxNrofDL-Allocations = 16`.

### Books

- **[Book · ★★★ · EN]** *5G NR: The Next Generation Wireless Access Technology*, 2nd ed. — Erik Dahlman, Stefan Parkvall, Johan Sköld · Academic Press, 2021 · ISBN 978-0-12-822320-8
  - Chapter 14 is the scheduling chapter, 13 the retransmission protocols, 15 uplink power and timing control, 21 interference handling in TDD networks. Three Ericsson people who were in the room: the "why it is like this" parts are the parts a specification cannot give you, and they are what an interview asks for.

### Papers

- **[Paper · ★★★ · EN]** "Rate control for communication networks: shadow prices, proportional fairness and stability" — F. P. Kelly, A. K. Maulloo, D. K. H. Tan · *Journal of the Operational Research Society*, vol. 49, no. 3, pp. 237–252, March 1998 · DOI 10.1057/palgrave.jors.2600523
  - The origin of the proportional-fairness criterion. Read it once and you will never again say "PF is fair" without qualifying it — it maximises the sum of log rates, which is a fairness criterion, not fairness, and the two are not the same thing.

### Open interfaces

- **[Standard · ★★★ · EN]** O-RAN ALLIANCE. *O-RAN.WG4.CUS — Control, User and Synchronization Plane Specification*. <https://www.o-ran.org/specifications>
  - The eCPRI message types, the C-plane section types 0 to 8, the eAxC identifier, and the T1a/T2a/Ta3/Ta4/Tcp_adv_dl timing windows. If you work on a 7-2x box, this document decides your slot pipeline.
- **[Standard · ★★ · EN]** O-RAN ALLIANCE. *O-RAN.WG1.OAD — O-RAN Architecture Description*. <https://www.o-ran.org/specifications>
  - The O-CU / O-DU / O-RU functional split and the 7-2x categories A and B, which decide where beamforming weights are computed.
- **[Standard · ★★★ · EN]** Small Cell Forum. *SCF222.10.02 / 222.10.04 — 5G NR FAPI specification*. <https://www.smallcellforum.org/>
  - The P5 control and P7 data-path messages with their IDs. This is the interface the scheduler actually speaks.
- **[Doc · ★★ · EN]** NVIDIA. *SCF FAPI support — Aerial cuBB release notes*. <https://docs.nvidia.com/aerial/>
  - The supported-message matrix, and the practical note that the PDU travels in a separate buffer rather than inside the message.

### Implementation references

- **[Code · ★★★ · EN]** **srsRAN Project** — `github.com/srsran/srsRAN_Project`
  - A complete open scheduler you can read end to end: the per-slot UE context, the two-stage DL allocation, the CCE allocator and the PUCCH reservation. Pair it with §5 and §9.
- **[Code · ★★ · EN]** **OpenAirInterface** — `github.com/OPENAIRINTERFACE/openairinterface5g`, the `open-nFAPI` P7 implementation
  - The pack and unpack functions for DL_TTI.request, UL_TTI.request, UL_DCI.request and TX_Data.request, and the uplink indications. The clearest place to see the L2/L1 contract as code.
- **[Doc · ★★ · EN]** COSMOS. *O-RAN architecture and the 7.2x fronthaul*. <https://www.cosmos-lab.org/wiki/public/tutorials/cellular-4g5g-oran/oran-intro>
  - The window definitions, the early/on-time/late counters, and two worked failures worth memorising: a `ta4_max` too narrow loses every PRACH, and a `T1a` outside the O-RU's window means the cell never radiates.
- **[Doc · ★★ · EN]** ShareTechnote. *Open RAN — eCPRI and the O-RAN C/U-plane*. <https://www.sharetechnote.com/html/OpenRAN/OR_eCPRI.html>
  - The section-type table and the eAxC sequence-id rules.
- **[Doc · ★ · EN]** Intel. *O-RAN Intel FPGA IP User Guide*. <https://cdrdv2-public.intel.com/812720/ug_oran-683238-812720.pdf>
  - How `t2a_min_up` / `t2a_max_up` / `ta3_min_up` are programmed from real O-RU processing delay, which is what makes the abstract windows concrete.
- **[Doc · ★ · EN]** Eurecom. *Experimental analysis of massive MIMO antennas in O-RAN systems*. <https://www.eurecom.fr/publication/8398>
  - The 7-2x functional allocation and the argument for centralising high-PHY in the O-DU.

### Practitioner and operator material

- **[Doc · ★★ · EN]** lte5ghub. *HARQ in 5G NR — downlink and uplink*. <https://lte5ghub.com/harq>
  - The process-count table, the NDI-toggle pipeline and the asynchronous-in-both-directions comparison with LTE.
- **[Doc · ★★ · EN]** lte5ghub. *TS 38.214: time-domain resource allocation and SLIV in 5G NR*. <https://lte5ghub.com/time-domain-allocation>
  - The N1/N2 table and the practical k2 floors per numerology, plus the SLIV decoding that turns a TDRA field into symbols.
- **[Doc · ★★ · EN]** lte5ghub. *TS 38.321: scheduling — dynamic, SPS and configured grant in 5G NR*. <https://lte5ghub.com/scheduling>
  - The candidate-to-CCE mapping formula and the per-slot PDCCH monitoring limits, both worked.
- **[Doc · ★ · EN]** 5G/6G Academy. *CORESET and search spaces in 5G NR*. <https://www.5g6gacademy.com/learn/coreset-and-search-spaces>
  - The per-slot blind-decode and CCE budgets, and why the caps tighten as SCS rises.
- **[Doc · ★ · EN]** HiCellTek. *MCS, TBS and code rate reference*. <https://hicelltek.com/en/mcs-tbs-code-rate/>
  - Per-index Qm and code rate for MCS tables 1 to 4, and the resulting spectral-efficiency ceilings.

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

## 06-1 · LLM Inference Engines and xLLM

### Papers

- **[Paper · EN · ★★★]** "xLLM Technical Report" — xLLM team (JD.com) · arXiv:2510.14686, 2025
  - The primary reference for the framework in note 06-1: the service–engine decoupled architecture, optimisation for Chinese AI accelerators (Ascend NPU, Cambricon MLU, Moore Threads GPU, Hygon DCU, MetaX MACA, Iluvatar CoreX), and hybrid KV cache management built on Mooncake with intelligent offloading and prefetching. Battle-tested at scale in JD.com's retail business, which is the strongest available evidence for the engineering claims.
- **[Paper · EN · ★★★]** "Mooncake: A KVCache-centric Disaggregated Architecture for LLM Serving" — R. Qin et al. · *USENIX FAST 2025* · arXiv:2407.00079
  - The KV-cache-centric disaggregated design: separating prefill and decode clusters, and treating KV cache as a first-class schedulable resource with a global pool. Directly the substrate xLLM's hybrid KV cache builds on.
- **[Paper · EN · ★★★]** "Efficient Memory Management for Large Language Model Serving with PagedAttention" — W. Kwon et al. · *ACM SOSP 2023* · arXiv:2309.06180
  - Paged virtual-memory-style KV cache management: eliminates fragmentation, enables sharing across requests, and is now the default mental model for KV cache. Know the block-allocation and copy-on-write mechanisms, not just the name.
- **[Paper · EN · ★★★]** "FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness" — T. Dao, D. Y. Fu, S. Ermon, A. Rudra, C. Ré · *NeurIPS 2022* · arXiv:2205.14135
  - IO-aware exact attention: tiling and recomputation to avoid materialising the attention matrix, turning attention from HBM-bound into compute-bound. The single most important inference optimisation of the last cycle.
- **[Paper · EN · ★★]** "FlashInfer: Efficient and Customizable Attention Engine for LLM Inference Serving" — Z. Ye et al. · *MLSys 2025* · arXiv:2501.01005
  - Production attention engine: a unified KV-cache format, JIT-generated kernels, and load-balanced scheduling for variable-length inputs. The right citation for "what does a real attention kernel library look like".
- **[Paper · EN · ★★★]** "Orca: A Distributed Serving System for Transformer-Based Generative Models" — G.-I. Yu et al. · *USENIX OSDI 2022*
  - Introduced iteration-level (continuous) batching and selective batching. This is the mechanism behind modern throughput, and the reason request-level batching is obsolete for decode.
- **[Paper · EN · ★★]** "Efficiently Scaling Transformer Inference" — N. Shazeer · *MLSys 2023* · arXiv:2211.05102
  - Multi-query attention and the systems-level scaling argument. Short and high density.
- **[Paper · EN · ★★]** "Fast Inference from Transformers via Speculative Decoding" — Y. Leviathan, M. Kalman, Y. Matias · *ICML 2023* · arXiv:2211.17192
  - Speculative decoding: draft-then-verify with exact distribution preservation. Essential for the latency side of the decode-phase discussion.
- **[Paper · EN · ★★]** "AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration" — J. Lin et al. · *MLSys 2024* · arXiv:2306.00978
  - Post-training quantization that protects salient weights identified by activation distribution. Know the difference between AWQ's activation-aware approach and GPTQ's second-order approach.
- **[Paper · EN · ★★]** "GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers" — E. Frantar et al. · *ICLR 2023* · arXiv:2210.17323
  - Layer-wise, Hessian-based one-shot quantization. The baseline all weight-only quantization is compared against.
- **[Paper · EN · ★★]** "Attention Is All You Need" — A. Vaswani et al. · *NeurIPS 2017* · arXiv:1706.03762
  - The architecture origin. Worth re-reading specifically for the inference-cost implications of multi-head attention and the KV cache it implies.
- **[Paper · EN · ★]** "Mamba: Linear-Time Sequence Modeling with Selective State Spaces" — A. Gu, T. Dao · arXiv:2312.00752
  - The most credible alternative to attention for sequence modelling, with linear-time inference and constant-memory state. Relevant to the "does the KV cache problem disappear" question.
- **[Paper · EN · ★]** "A Survey of Large Language Models" — W. X. Zhao et al. · arXiv:2303.18223
  - Comprehensive survey across pre-training, adaptation, utilization and evaluation. Use as a structured map of the field rather than as a systems reference.

### Code

- **[Code · ★★★]** **xLLM** (github.com — JD.com) — Apache License, C++ primary
  - The implementation behind the technical report. Read the service/engine split and the hybrid KV cache path. Acknowledges ScaleLLM (graph construction and runtime), Mooncake (KV cache), brpc (HTTP service), tokenizers-cpp, safetensors and concurrentqueue.
- **[Code · ★★]** **Mooncake** — KV-cache-centric disaggregated serving store
- **[Code · ★★]** **FlashInfer / FlashAttention** — attention kernel libraries

---

## 06-2 · Agent Systems and Edge Orchestration

### Papers

- **[Paper · EN · ★★★]** "gRPC-Routed Agent Framework for Tasking (GRAFT)" · CAIS '26 · DOI 10.1145/3786335.3813216
  - The specific paper behind note 06-2: sessioned gRPC routing across heterogeneous personal devices, capability-aware task routing in a small-language-model agent mesh. Note that GRAFT is an overloaded acronym — cite the DOI, not the name.
- **[Paper · EN · ★★★]** "A Survey on Large Language Model based Autonomous Agents" — L. Wang et al. · arXiv:2308.11432
  - The standard taxonomy for agent systems: construction (profile/memory/planning/action), evaluation and application, with an explicit agent-society discussion. Use it to place any specific agent framework on a map.
- **[Paper · EN · ★★]** "The Rise and Potential of Large Language Model Based Agents: A Survey" — Z. Xi et al. · arXiv:2309.07864
  - A complementary survey with a stronger emphasis on the brain–perception–action decomposition and the open problems.
- **[Paper · EN · ★★★]** "ReAct: Synergizing Reasoning and Acting in Language Models" — S. Yao et al. · *ICLR 2023* · arXiv:2210.03629
  - Interleaves reasoning traces with actions. The baseline agent loop; most frameworks are variations on it.
- **[Paper · EN · ★★]** "Reflexion: Language Agents with Verbal Reinforcement Learning" — N. Shinn et al. · *NeurIPS 2023* · arXiv:2303.11366
  - Self-reflection with episodic memory, improving without gradient updates. Relevant to the "how does an agent improve at runtime" question.
- **[Paper · EN · ★★]** "Toolformer: Language Models Can Teach Themselves to Use Tools" — T. Schick et al. · *NeurIPS 2023* · arXiv:2302.04761
  - Self-supervised tool-use learning with API calls inserted into text. The origin of the tool-calling pattern.
- **[Paper · EN · ★★]** "Voyager: An Open-Ended Embodied Agent with Large Language Models" — G. Wang et al. · *TMLR 2024* · arXiv:2305.16291
  - Skill library, automatic curriculum and iterative prompting in a long-horizon embodied setting. Good example of persistent agent memory as a library of executable skills.
- **[Paper · EN · ★]** "Generative Agents: Interactive Simulacra of Human Behavior" — J. S. Park et al. · *UIST 2023* · arXiv:2304.03442
  - Memory stream, reflection and planning in a multi-agent simulation. Read for the memory-architecture design, not the social-simulation framing.
- **[Paper · EN · ★★]** "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation" — Q. Wu et al. · arXiv:2308.08155
  - Conversable-agent abstraction and multi-agent conversation orchestration. The clearest example of conversation-as-control-flow.
- **[Paper · EN · ★]** "MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework" — S. Hong et al. · *ICLR 2024* · arXiv:2308.00352
  - Encodes standardised operating procedures into agent prompts, structured around assembly-line division of labour.

### Cross-references

- **[Paper · ★★★]** Edge offloading and resource allocation papers in §09 (Satyanarayanan 2017; Shi et al. 2016; Mao et al. 2017)
  - The placement half of edge orchestration. An agent mesh that ignores the communication cost of placing a task is the failure mode to describe explicitly.
- **[Paper · ★★]** "Age of Information: An Introduction and Survey" (§06)
  - The metric to prefer over latency when agents are dispatching status-driven tasks.

---

## 06-3 · Machine Learning — Foundations, Core Algorithms and Applications

### Books

- **[Book · ★★★]** Gareth James, Daniela Witten, Trevor Hastie and Robert Tibshirani. *An Introduction to Statistical Learning with Applications in R*, 2nd ed. Springer, 2021. ISBN 978-1-0716-1417-4. <https://www.statlearning.com>
  - The best first book. Chapters 2–8 cover what this note covers in §5 and §9, with labs. The Python edition (ISLP, 2023) exists if you would rather not read R. Free PDF from the authors.
- **[Book · ★★★]** Aurélien Géron. *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow*, 3rd ed. O'Reilly, 2022. ISBN 978-1-098-12597-4
  - The practical counterpart: a full project end to end, then trees, ensembles, dimensionality reduction, neural networks, CNNs, RNNs and attention, autoencoders/GANs/diffusion, and reinforcement learning. Its Appendix A "Machine Learning Project Checklist" is the checklist in §3.1 written out properly.
- **[Book · ★★]** Trevor Hastie, Robert Tibshirani and Jerome Friedman. *The Elements of Statistical Learning*, 2nd ed. Springer, 2009. ISBN 978-0-387-84857-0. <https://hastie.su.domains/ElemStatLearn/>
  - The graduate version of ISLR, and free. Read chapters 3 (linear methods), 7 (model assessment), 9 (additive models and trees), 10 (boosting) and 15 (random forests) when you need the derivation, not the recipe.
- **[Book · ★★]** Christopher M. Bishop. *Pattern Recognition and Machine Learning*. Springer, 2006. ISBN 978-0-387-31073-2
  - The probabilistic view: §5.3's bias–variance decomposition and §5.9's regularisation story are cleanest here. Dense, and worth owning once you have finished ISLR.
- **[Book · ★★]** Kevin P. Murphy. *Probabilistic Machine Learning: An Introduction*. MIT Press, 2022. ISBN 978-0-262-04682-4. <https://probml.github.io/pml-book/book1.html>
  - The modern replacement for Bishop at twice the length, with the deep-learning material Bishop predates. Free online.
- **[Book · ★]** Ian Goodfellow, Yoshua Bengio and Aaron Courville. *Deep Learning*. MIT Press, 2016. ISBN 978-0-262-03561-3. <https://www.deeplearningbook.org>
  - Chapters 6–8 (deep networks and optimisation) are still the reference for backpropagation and for why the tricks in §6.5 exist. The later chapters have aged.

### Courses, guides and documentation

- **[Doc · ★★★]** scikit-learn developers. *User Guide — Choosing the right estimator; Common pitfalls and recommended practices*. <https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html> · <https://scikit-learn.org/stable/common_pitfalls.html>
  - The official flowchart for picking a model family, and the official statement of the preprocessing-leakage rule in §3.1. Short, and directly quotable in an interview.
- **[Doc · ★★★]** Google. *Machine Learning Crash Course*. <https://developers.google.com/machine-learning/crash-course>
  - The fastest route from zero to "I have trained something and I know what a learning rate is": gradient descent, generalisation, training sets, neural networks, embedding, and a fairness unit.
- **[Doc · ★★★]** Google. *Rules of Machine Learning: Best Practices for ML Engineering*. <http://martin.zinkevich.org/rules_of_ml/rules_of_ml.pdf>
  - Forty-three rules from people who shipped. It is where the advice in §2.2 ("start with a heuristic") and §12 ("keep the first model simple, design for iteration") comes from. Re-read it after your second project.
- **[Doc · ★★]** PyTorch Foundation. *PyTorch Tutorials*. <https://pytorch.org/tutorials/>
  - Enough to do weeks 1 and 4 of the learning path in §14: tensors and autograd, then a classifier, then transfer learning.
- **[Doc · ★★]** Aston Zhang, Zack Lipton, Mu Li, Alex Smola et al. *Dive into Deep Learning*. <https://d2l.ai>
  - One book-sized site with runnable code for every architecture in §7, including the convolutional output-size arithmetic and the attention implementation. Use it as the worked-code companion.
- **[Doc · ★]** Google. *Machine Learning Glossary*. <https://developers.google.com/machine-learning/glossary>
  - For when you need the standard definition of a term rather than a paraphrase.

### Papers — foundations

- **[Paper · ★★★]** Leo Breiman. "Random Forests." *Machine Learning* 45, 5–32, 2001. <https://link.springer.com/article/10.1023/A:1010933404324>
  - Bagging plus random feature subsets, out-of-bag error, and variable importance, from the inventor. Read the sections on the strength–correlation trade-off; it is the clearest explanation of why decorrelating the trees matters.
- **[Paper · ★★★]** Yoav Freund and Robert E. Schapire. "A Decision-Theoretic Generalization of On-Line Learning and an Application to Boosting." *Journal of Computer and System Sciences* 55(1), 119–139, 1997
  - AdaBoost, with the training-error bound that explains why boosting looks like it should overfit and mostly does not.
- **[Paper · ★★★]** Tianqi Chen and Carlos Guestrin. "XGBoost: A Scalable Tree Boosting System." arXiv:1603.02754, 2016 (KDD 2016). <https://arxiv.org/abs/1603.02754>
  - The system that made gradient boosting the default for tabular data: the regularised objective, the weighted quantile sketch for split finding, sparsity-aware handling of missing values, and the cache- and out-of-core-aware implementation.
- **[Paper · ★★]** James Bergstra and Yoshua Bengio. "Random Search for Hyper-Parameter Optimization." *JMLR* 13, 281–305, 2012. <https://jmlr.org/papers/v13/bergstra12a.html>
  - The two-page argument, with figures, for why random search beats grid search at equal budget. The reason — only a few hyperparameters matter, and grid search wastes trials on the rest — is worth stating from memory.
- **[Paper · ★★]** Lisha Li, Kevin Jamieson, Giulia DeSalvo, Afshin Rostamizadeh and Ameet Talwalkar. "Hyperband: A Novel Bandit-Based Approach to Hyperparameter Optimization." *JMLR* 18(185), 2018. <https://jmlr.org/papers/v18/16-558.html>
  - Successive halving done right, with the budget-versus-configuration trade-off made explicit.
- **[Paper · ★★]** Scott M. Lundberg and Su-In Lee. "A Unified Approach to Interpreting Model Predictions." arXiv:1705.07874, 2017 (NeurIPS 2017). <https://arxiv.org/abs/1705.07874>
  - SHAP. Read it for the additivity property and for the reminder that an explanation describes the model, not the world.
- **[Paper · ★]** Fei Tony Liu, Kai Ming Ting and Zhi-Hua Zhou. "Isolation Forest." *ICDM*, 2008
  - Anomaly detection by random splitting, with the expected-path-length argument that makes it linear-time and sub-sampling-friendly.
- **[Paper · ★]** David H. Wolpert and William G. Macready. "No Free Lunch Theorems for Optimization." *IEEE Transactions on Evolutionary Computation* 1(1), 67–82, 1997
  - The reason no algorithm is universally best. Cite it before anyone claims one is.
- **[Paper · ★]** Frank Rosenblatt. "The perceptron: a probabilistic model for information storage and organization in the brain." *Psychological Review* 65(6), 1958; and David E. Rumelhart, Geoffrey E. Hinton and Ronald J. Williams, "Learning representations by back-propagating errors," *Nature* 323, 1986
  - The two ends of the first neural-network cycle: the model, and the learning rule that made hidden layers usable.

### Papers — deep learning

- **[Paper · ★★★]** Alex Krizhevsky, Ilya Sutskever and Geoffrey E. Hinton. "ImageNet Classification with Deep Convolutional Neural Networks." *NeurIPS*, 2012. <https://papers.nips.cc/paper_files/paper/2012>
  - The paper that started the current era: 5 convolutional and 3 fully connected layers, 60 million parameters, 650,000 neurons, two GPUs, ReLU, dropout, data augmentation — and 15.3% top-5 error against 26.2% for the runner-up.
- **[Paper · ★★★]** Ashish Vaswani, Noam Shazeer, Niki Parmar et al. "Attention Is All You Need." arXiv:1706.03762, 2017. <https://arxiv.org/abs/1706.03762>
  - Scaled dot-product attention, multi-head attention, positional encoding, and the complexity table comparing self-attention with recurrent and convolutional layers. Note the `sqrt(d_k)` scaling and the reason given for it.
- **[Paper · ★★★]** Diederik P. Kingma and Jimmy Ba. "Adam: A Method for Stochastic Optimization." arXiv:1412.6980, 2014 (ICLR 2015). <https://arxiv.org/abs/1412.6980>
  - The update rules and the bias-correction terms. Three pages of actual algorithm.
- **[Paper · ★★]** Kaiming He, Xiangyu Zhang, Shaoqing Ren and Jian Sun. "Deep Residual Learning for Image Recognition." arXiv:1512.03385, 2015. <https://arxiv.org/abs/1512.03385>
  - Residual connections, the degradation problem they solve, and the 152-layer result. The identity-mapping follow-up (arXiv:1603.05027) is worth reading immediately afterwards.
- **[Paper · ★★]** Nitish Srivastava, Geoffrey Hinton, Alex Krizhevsky, Ilya Sutskever and Ruslan Salakhutdinov. "Dropout: A Simple Way to Prevent Neural Networks from Overfitting." *JMLR* 15(56), 2014. <https://jmlr.org/papers/v15/srivastava14a.html>
  - The technique, the inverted scaling at test time, and the interpretation as model averaging.
- **[Paper · ★★]** Sergey Ioffe and Christian Szegedy. "Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift." arXiv:1502.03167, 2015 (ICML 2015). <https://arxiv.org/abs/1502.03167>
  - The algorithm in full, including the inference-time population statistics — the part people get wrong in production.
- **[Paper · ★★]** Sepp Hochreiter and Jürgen Schmidhuber. "Long Short-Term Memory." *Neural Computation* 9(8), 1735–1780, 1997. <https://direct.mit.edu/neco/article/9/8/1735/6109>
  - The constant-error-carousel argument for the gates. Still the source to cite when someone says LSTMs are ad hoc.
- **[Paper · ★★]** Dzmitry Bahdanau, Kyunghyun Cho and Yoshua Bengio. "Neural Machine Translation by Jointly Learning to Align and Translate." arXiv:1409.0473, 2014. <https://arxiv.org/abs/1409.0473>
  - Attention as a soft alignment over all encoder states: the direct ancestor of §7.3.
- **[Paper · ★★]** Jonathan Ho, Ajay Jain and Pieter Abbeel. "Denoising Diffusion Probabilistic Models." arXiv:2006.11239, 2020. <https://arxiv.org/abs/2006.11239>
  - The forward noising process, the reverse-parameterisation choice, and — importantly — the simplified training objective of predicting the noise.
- **[Paper · ★]** Ian J. Goodfellow, Jean Pouget-Abadie, Mehdi Mirza et al. "Generative Adversarial Nets." arXiv:1406.2661, 2014. <https://arxiv.org/abs/1406.2661>
  - The minimax game, the global-optimality proof, and the failure modes everyone then spent a decade fixing.

### Papers — scaling and systems

- **[Paper · ★★★]** Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch et al. "Training Compute-Optimal Large Language Models." arXiv:2203.15556, 2022. <https://arxiv.org/abs/2203.15556>
  - The source of the "~20 training tokens per parameter" figure, and of the method (fit the loss–compute frontier across model sizes) that produced it.
- **[Paper · ★★]** Priya Goyal, Piotr Dollár, Ross Girshick et al. "Accurate, Large Minibatch SGD: Training ImageNet in 1 Hour." arXiv:1706.02677, 2017. <https://arxiv.org/abs/1706.02677>
  - The linear scaling rule for learning rate versus batch size, the warmup needed to make it work, and the batch-size ceiling past which it stops holding.
- **[Paper · ★★]** Samyam Rajbhandari, Jeff Rasley, Olatunji Ruwase and Yuxiong He. "ZeRO: Memory Optimizations Toward Training Trillion Parameter Models." arXiv:1910.02054, 2019 (SC 2020). <https://arxiv.org/abs/1910.02054>
  - The three stages of sharding optimiser state, gradients and parameters — the mechanism behind §8.3's memory arithmetic.
- **[Paper · ★★]** Mohammad Shoeybi, Mostofa Patwary, Raul Puri et al. "Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism." arXiv:1909.08053, 2019. <https://arxiv.org/abs/1909.08053>
  - Tensor parallelism done at layer granularity: the column-then-row split of the attention and MLP blocks, with the synchronisation points made explicit.
- **[Paper · ★]** Yanping Huang, Youlong Cheng, Ankur Bapna et al. "GPipe: Efficient Training of Giant Neural Networks using Pipeline Parallelism." arXiv:1811.06965, 2018. <https://arxiv.org/abs/1811.06965>
  - Microbatches and the pipeline bubble, quantified.

### Cross-references

- For what happens after training — serving, batching, quantisation and KV-cache management — see **§06-1**.
- For models that act rather than predict — planning, tools, safety boundaries — see **§06-2**.
- For these algorithms placed under a RAN's millisecond timing constraints and inside an O-RAN RIC, see **§01-3**.
- For where the training and serving compute physically sits, see **§05-2**.
- For the array semantics the Python stack depends on, see **§08-3**.

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

## 08-1 · Languages, Toolchain and Performance Engineering

### Books

- **[Book · EN · ★★★]** *Computer Systems: A Programmer's Perspective*, 3rd ed. — Bryant, O'Halloran (see §05-2)
  - Memory hierarchy, cache behaviour, linking, and the cost model behind every performance claim. If you only read one performance book, read this.
- **[Book · EN · ★★★]** *Systems Performance: Enterprise and the Cloud*, 2nd ed. — Brendan Gregg · Addison-Wesley, 2020
  - The methodology: the USE method, workload characterisation, drill-down analysis, and the counterintuitive results that come from measuring before theorising. Covers CPU, memory, file systems, disk and network.
- **[Book · EN · ★★]** *BPF Performance Tools: Linux System and Application Observability* — Brendan Gregg · Addison-Wesley, 2019
  - The BCC and bpftrace toolchain in practice. eBPF is now the standard way to get production-visible tracing without redeploying, which matters for on-device and edge systems where you cannot restart to instrument.
- **[Book · EN · ★★]** *Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14* — Scott Meyers · O'Reilly, 2014
  - Move semantics, smart pointers, lambda correctness and type deduction. The difference between "C++ that works" and "C++ that is safe and fast".
- **[Book · EN · ★★]** *C++ Concurrency in Action*, 2nd ed. — Anthony Williams · Manning, 2019
  - Memory model, atomics, memory ordering and lock-free design. Essential for dataplane and inference-engine work where the concurrency is real, not theoretical.
- **[Book · EN · ★★]** *Is Parallel Programming Hard, And, If So, What Can You Do About It?* — Paul E. McKenney · freely available
  - The definitive treatment of RCU, memory ordering and scalable synchronisation, written by a kernel maintainer. Read before designing any lock-free structure.
- **[Book · EN · ★]** *Operating Systems: Three Easy Pieces* — R. H. Arpaci-Dusseau, A. C. Arpaci-Dusseau · freely available
  - Virtualisation, concurrency and persistence explained cleanly. Good for filling conceptual gaps without a textbook budget.

---

## 08-2 · C and C++ Programming — Language Features, STL and Systems Practice

Supports vault note `16`. Note that §13 covers toolchain, profiling and performance engineering; this section is the language itself.

### Books — C

- **[Book · EN/CN · ★★★]** *The C Programming Language*, 2nd ed. — Brian W. Kernighan, Dennis M. Ritchie · Prentice Hall, 1988 · ISBN 9780131103627 · Chinese 《C程序设计语言(第2版·新版)》, translated by 徐宝文, 李志 · 机械工业出版社, 2004 · ISBN 9787111128069 (典藏版 reissue ISBN 9787111617945)
  - Written by the language's designer. Still the clearest account of pointers, arrays and the preprocessor — and still thin on the parts the standard later changed. Read it for the model, then read a modern text for C11/C23.
- **[Book · EN · ★★★]** *Modern C* — Jens Gustedt · Manning, 2019 (2nd ed. 2022, freely available online)
  - The modern replacement for K\&R: written by a WG14 member and organised around C17/C23 rather than C89. Covers `stdint.h`, atomics, alignment, `_Generic`, and the undefined-behaviour traps that K\&R never had to warn about. **This is the C book to read if you already know C.**
- **[Book · EN · ★★]** *C Programming: A Modern Approach*, 2nd ed. — K. N. King · W. W. Norton, 2008 · ISBN 9780393979503
  - The best teaching text on the language: exhaustive, precise about the standard, and unusually good on the "why is this undefined" questions.
- **[Book · EN · ★★]** *Expert C Programming: Deep C Secrets* — Peter van der Linden · Prentice Hall, 1994 · ISBN 9780131774292
  - Old, but the chapters on array/pointer equivalence, declaration parsing, and linker/memory layout still explain things no current book does as well.
- **[Book · EN · ★]** *21st Century C*, 2nd ed. — Ben Klemens · O'Reilly, 2014
  - How to write C as it is actually written now: build tooling, unit testing with a real framework, and using the standard library instead of reinventing it.

### Books — C++ language

- **[Book · EN/CN · ★★★]** *C++ Primer*, 5th ed. — Stanley B. Lippman, Josée Lajoie, Barbara E. Moo · Addison-Wesley, 2012 · ISBN 9780321714114 · Chinese 《C++ Primer 中文版(第5版)》, translated by 王刚, 杨巨峰 · 电子工业出版社, 2013 · ISBN 9787121155352
  - The most complete single-volume tutorial, rewritten for C++11. Use it as the reference for the core language — types, classes, templates, the standard library — and supplement it for C++17/20/23.
- **[Book · EN/CN · ★★★]** *The C++ Programming Language*, 4th ed. — Bjarne Stroustrup · Addison-Wesley, 2013 · ISBN 9780321563842 · Chinese 《C++程序设计语言(特别版)》 translated by 裘宗燕 · 机械工业出版社 · ISBN 9787111102029
  - The language from its author. Less tutorial, more "what the abstraction means and what it costs" — which is the framing interviewers reward.
- **[Book · EN · ★★★]** *Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14* — Scott Meyers · O'Reilly, 2014 (see §08-1)
  - Type deduction, `auto`, move semantics, smart pointers and lambda correctness. Pair it with *Effective C++*, 3rd ed. (ISBN 9780321334879, Chinese 《Effective C++ 改善程序与设计的55个具体做法》, 机械工业出版社) for the pre-C++11 core.
- **[Book · EN · ★★]** *A Tour of C++*, 3rd ed. — Bjarne Stroustrup · Addison-Wesley, 2022
  - The shortest accurate overview of modern C++ as a whole language, covering C++20 and C++23 in ~250 pages. Read this first if your C++ knowledge stopped at C++11.
- **[Book · EN · ★★]** *C++ Templates: The Complete Guide*, 2nd ed. — David Vandevoorde, Nicolai M. Josuttis, Douglas Gregor · Addison-Wesley, 2017 · ISBN 9780321714121
  - Everything about templates: deduction, specialisation, variadics, SFINAE, trait and policy-based design, and compile-time cost. The book to own if templates appear in your job description.
- **[Book · EN/CN · ★★]** *Inside the C++ Object Model* — Stanley B. Lippman · Addison-Wesley, 1996 · Chinese 《深度探索C++对象模型》, translated by 侯捷 · 华中科技大学出版社, 2001 · ISBN 9787560924182
  - How virtual functions, inheritance, and object layout are actually implemented — vptr/vtable placement, the cost of multiple and virtual inheritance. Answers "what does a virtual call really cost" at the representation level.
- **[Book · EN · ★★]** *C++ Software Design* — Klaus Iglberger · Addison-Wesley, 2022
  - Design-level C++: value semantics, type erasure, CRTP, policy-based design, and *when not to use inheritance*. Strong on the patterns that replace OOP in performance-sensitive code.
- **[Book · EN · ★]** *C++23 — The Complete Guide* and *C++ Move Semantics — The Complete Guide* — Nicolai M. Josuttis · C++20 and C++17 volumes also exist; all freely available online
  - Feature-by-feature guides to a single standard, with compiler-support tables. The fastest way to check "which standard did X arrive in".

### Books — STL and standard library

- **[Book · EN/CN · ★★★]** *The C++ Standard Library: A Tutorial and Reference*, 2nd ed. — Nicolai M. Josuttis · Addison-Wesley, 2012 · ISBN 9780321623218 · Chinese 《C++标准库(第2版)》, translated by 侯捷, 孟岩 · 华中科技大学出版社
  - The STL reference with explanations: every container, iterator, algorithm and functor, plus the trade-offs. If you need one STL book, this is it.
- **[Book · EN/CN · ★★★]** 《STL源码剖析》 (The Annotated STL Sources) — 侯捷 · 华中科技大学出版社, 2002 · ISBN 9787560926995
  - A source-level walkthrough of the SGI/STLPort implementation: allocators and memory pools, iterator traits, the sequence containers, red-black tree and hash table, algorithms, functors and adapters. Reading the implementation is how you learn *why* `vector` beats `list` and what a traits mechanism is for. Based on a pre-C++11 implementation, so read it for mechanism, not for API.
- **[Book · EN · ★★]** *Effective STL: 50 Specific Ways to Improve Your Use of the Standard Template Library* — Scott Meyers · Addison-Wesley, 2001 · ISBN 9780201749625
  - Dated in places (no move semantics), still the sharpest writing on container selection, iterator invalidation, and the algorithm-vs-hand-written-loop decision.
- **[Book · EN · ★]** *Hands-On Design Patterns with C++*, 2nd ed. — Fedor Pikus · Packt, 2022
  - C++-specific patterns including CRTP, type erasure, the policy pattern and lock-free structures, with performance measurements.

### Standards and committee documents

- **[Standard · ★★★]** **ISO/IEC 9899:2024** (C23) — WG14. Closest free draft: **N3220**. `__STDC_VERSION__` = `202311L`
- **[Standard · ★★★]** **ISO/IEC 14882:2026** (C++26) — WG21. Working draft **N5046**, shipped by WG21 on **28 March 2026**
- **[Spec · ★★★]** **WG21 papers** (`open-std.org/jtc1/sc22/wg21/docs/papers`), and **WG14 papers** (`open-std.org/jtc1/sc22/wg14`). Key C++26 papers: **P2996** reflection · **P2900** contracts · **P2300** `std::execution` · **P1928** `std::simd` · **P1673** `std::linalg` · **P0843** `std::inplace_vector` · **P0447** `std::hive` · **P3471** library hardening · **P2795** erroneous behaviour · **P1306** expansion statements · **P2530** hazard pointers · **P2545** RCU · **P0429** `flat_map` · **P1222** `flat_set` · **P1967** `#embed`
  - Read the paper, not the blog post. Each one states the problem, the design alternatives considered, and the cost — which is exactly what an interviewer asks about.
- **[Doc · ★★★]** **cppreference.com** — the de facto standard library reference, with per-standard version markers and per-compiler support tables
- **[Doc · ★★]** **C++ Core Guidelines** — Bjarne Stroustrup, Herb Sutter · `isocpp.github.io/CppCoreGuidelines`, with the associated GSL
  - The closest thing to a house style for modern C++: ownership, lifetime, interfaces, error handling and performance, each with a stated rationale.
- **[Doc · ★★]** **GCC C++ status page** (`gcc.gnu.org/projects/cxx-status.html`) and **libc++/libstdc++ implementation status pages**
  - Where to check whether a feature you want to quote is actually available in your compiler version.
- **[Doc · ★]** **Compiler Explorer** (`godbolt.org`) — for checking codegen, especially whether a construct vectorises or allocates

### Papers and talks

- **[Paper · ★★]** *"A Tour of C++"* / Stroustrup's **"The Design and Evolution of C++"** and **"Thriving in a Crowded and Changing World: C++ 2006–2020"** (ACM HOPL IV, 2020)
  - The history is useful: knowing *why* a feature exists (compatibility, zero-overhead, evolving hardware) is what lets you defend a language choice under questioning.
- **[Paper · ★★]** *"Memory Ordering in C++"* and Paul E. McKenney's **perfbook** (see §08-1)
  - The memory model is the part of C++ most people get wrong. Read the model, not the rules of thumb.
- **[Doc · ★]** **CppCon talks** on `std::execution` (senders/receivers), reflection (P2996), and `std::simd` — the fastest route to C++26 material, since no book covers it yet.

---

## 08-3 · Python Programming — Language, Object Model and Engineering Practice

### Books

- **[Book · ★★★]** *Fluent Python: Clear, Concise, and Effective Programming*, 2nd ed. — Luciano Ramalho, O'Reilly, 2022. ISBN 978-1-492-05635-5. [EN]
  - The reference for the data model: dunder protocols, descriptors, MRO, generators. Read Part I and Part IV before any interview that claims Python fluency.
- **[Book · ★★★]** *Effective Python: 90 Specific Ways to Write Better Python*, 2nd ed. — Brett Slatkin, Addison-Wesley, 2019. ISBN 978-0-13-485398-7. [EN]
  - Item-level advice with the "why"; the chapters on closures, generators and concurrency map directly onto interview questions.
- **[Book · ★★]** *Python Cookbook*, 3rd ed. — David Beazley and Brian K. Jones, O'Reilly, 2013. ISBN 978-1-449-34037-7. [EN]
  - Recipe-level: iterators, `__slots__`, wrapping C libraries with `ctypes`, mixing threads and processes.
- **[Book · ★★]** *Python for Data Analysis*, 3rd ed. — Wes McKinney, O'Reilly, 2022. ISBN 978-1-098-10403-0. [EN]
  - Written by NumPy/pandas' author; the clearest account of the array-and-label model behind KPI analysis.
- **[Book · ★★]** *High Performance Python*, 2nd ed. — Micha Gorelick and Ian Ozsvald, O'Reilly, 2020. ISBN 978-1-492-05502-0. [EN]
  - The measurement-first approach: profiling, memory, C extensions, multiprocessing, and when each one actually helps.
- **[Book · ★]** *CPython Internals* — Anthony Shaw, Real Python, 2021. [EN]
  - Compiler pipeline, frames, the evaluation loop and object representation, written for people who want to reason about CPython rather than about Python.


### Documentation and specifications

- **[Doc · ★★★]** *The Python Language Reference* and *The Python Data Model*. <https://docs.python.org/3/reference/> [EN]
  - The data model chapter is the normative description of every dunder method; read it once end to end.
- **[Doc · ★★★]** *What's New In Python 3.15* (released 2026-10-09). <https://docs.python.org/3/whatsnew/3.15.html> [EN]
  - Lazy imports (PEP 810), `frozendict` (PEP 814), UTF-8 default (PEP 686), Tachyon profiler (PEP 799).
- **[Standard · ★★]** PEP 8 (style), PEP 484 (type hints), PEP 544 (Protocols), PEP 557 (dataclasses), PEP 659 (adaptive interpreter), PEP 703 (free-threading), PEP 779 (free-threading support status). <https://peps.python.org/> [EN]
- **[Doc · ★★]** *asyncio* documentation — task groups, timeouts, cancellation, the event loop. <https://docs.python.org/3/library/asyncio.html> [EN]
- **[Standard · ★★]** NumPy *NEP 50* — promotion rules for Python scalars, the change that broke dtype assumptions in NumPy 2.0. <https://numpy.org/neps/nep-0050-scalar-promotion.html> [EN]

### Papers and practice

- **[Paper · ★★★]** Harris, C. R., Millman, K. J., van der Walt, S. J., et al. "Array programming with NumPy." *Nature* 585, 357–362 (2020). DOI 10.1038/s41586-020-2649-2. [EN]
  - The canonical citation for why strided arrays with a dtype beat lists by two orders of magnitude.
- **[Code · ★★]** pybind11 and nanobind — C++ ↔ Python binding layers; the casters and GIL handling are the practical content. <https://pybind11.readthedocs.io/> · <https://nanobind.readthedocs.io/> [EN]
- **[Code · ★★]** Numba and Cython — JIT and ahead-of-time compilation of numeric Python. <https://numba.readthedocs.io/> · <https://cython.readthedocs.io/> [EN]
- **[Doc · ★★]** pytest, ruff, mypy, uv — the 2026 default toolchain for tests, lint, types and environments. [EN]

---

## 08-4 · MATLAB and Simulink — Programming, Modelling and Code Generation

### Books

- **[Book · ★★★]** *MATLAB Guide*, 3rd ed. — Desmond J. Higham and Nicholas J. Higham, SIAM, 2017. ISBN 978-1-611974-18-6. [EN]
  - The best-written account of the language itself: arrays, functions, object-oriented programming, and numerical quality. Written by numerical analysts, so the advice on conditioning is worth taking.
- **[Book · ★★★]** *Numerical Computing with MATLAB* — Cleve B. Moler, SIAM, 2004. ISBN 978-0-89871-660-3. [EN]
  - MATLAB's creator on the numerical methods behind the built-ins; explains why `\` is not `inv(A)*b`.
- **[Book · ★★]** *MATLAB: A Practical Introduction to Programming and Problem Solving*, 5th ed. — Stormy Attaway, Butterworth-Heinemann, 2019. ISBN 978-0-12-815479-3. [EN]
  - Fastest route for someone coming from C or Python; the chapter on vectorisation is the useful part.
- **[Book · ★★]** *Basic MATLAB, Simulink, and Stateflow* — Richard D. Colgren, AIAA Education Series, 2007. ISBN 978-1-56347-838-1. [EN]
  - Written for aerospace control work, which is exactly the audience that needs sample time and state machines explained together.
- **[Book · ★★]** *Simulation of Dynamic Systems with MATLAB and Simulink*, 3rd ed. — Harold Klee and Randal Allen, CRC Press, 2018. [EN]
  - Integrator theory, stiffness and solver selection treated as numerical analysis rather than as tool settings.

### Documentation

- **[Doc · ★★★]** *Object-Oriented Programming in MATLAB* — handle vs value classes, property validation, events, `matlab.System`. <https://www.mathworks.com/help/matlab/matlab_oop/object-oriented-programming.html> [EN]
- **[Doc · ★★★]** *Function Argument Validation* — the `arguments` block, validators, name-value arguments. <https://www.mathworks.com/help/matlab/matlab_prog/function-argument-validation-1.html> [EN]
- **[Doc · ★★★]** *Choose a Solver* — stiffness, variable vs fixed step, and the code-generation constraint. <https://www.mathworks.com/help/simulink/ug/choose-a-solver.html> [EN]
- **[Doc · ★★]** *Stateflow User's Guide* — hierarchy, temporal logic, truth tables, generated-code structure. <https://www.mathworks.com/help/stateflow/> [EN]
- **[Doc · ★★]** *Fixed-Point Designer* — `fi`, `fimath`, rounding and overflow modes, word-length analysis. <https://www.mathworks.com/help/fixedpoint/> [EN]
- **[Doc · ★★]** *HDL Coder* and *Embedded Coder* — synthesizable subset, latency balancing, MISRA checking, SIL/PIL. <https://www.mathworks.com/help/hdlcoder/> · <https://www.mathworks.com/help/ecoder/> [EN]
- **[Doc · ★★]** *MATLAB and Simulink Release Notes* — R2026a (April 2026) and R2026b (24 September 2026) are the current pair. <https://www.mathworks.com/help/relnotes/> [EN]
- **[Doc · ★]** *5G Toolbox* — NR waveform generation, TDL/CDL channel models, reference measurement channels. <https://www.mathworks.com/help/5g/> [EN]

### Papers and practitioner material

- **[Doc · ★★]** "MATLAB R2026a has been released — What's new?" *MATLAB Blog*, 21 April 2026. <https://blogs.mathworks.com/matlab/2026/04/21/matlab-r2026a-has-been-released-whats-new/> [EN]
  - Release-level summary with worked examples: ODE automatic differentiation, `metafunction` introspection, Python 3.9–3.13 support.
- **[Doc · ★★]** "MathWorks Introduces Release 2026b of MATLAB and Simulink." Press release, 24 September 2026. [EN]
  - The variant-management, JSON data dictionary, custom-solver and TOML project changes that affect how a model is version-controlled.

---

## 08-5 · Verilog HDL — RTL Design, Verification and Synthesis Practice

### Books

- **[Book · ★★★]** *Verilog HDL: A Guide to Digital Design and Synthesis*, 2nd ed. — Samir Palnitkar, Prentice Hall, 2003. ISBN 0-13-044911-3. [EN]
  - The standard teaching text: language, modelling styles, synthesisable subset. Old, and still the clearest explanation of blocking vs non-blocking.
- **[Book · ★★★]** *SystemVerilog for Verification: A Guide to Learning the Testbench Language Features*, 3rd ed. — Chris Spear, Springer, 2012. ISBN 978-1-4614-0714-0. [EN]
  - Classes, virtual interfaces, mailboxes, constrained random and coverage — the class layer of the language, which plain Verilog does not have.
- **[Book · ★★]** *The Verilog Hardware Description Language*, 5th ed. — Donald E. Thomas and Philip R. Moorby, Springer, 2002. ISBN 978-0-7923-7621-7. [EN]
  - Written by Verilog's co-designer; the simulation semantics are explained from the scheduler's point of view.
- **[Book · ★★]** *FPGA Prototyping by Verilog Examples* — Pong P. Chu, Wiley-IEEE Press, 2008. ISBN 978-0-470-18532-2. [EN]
  - Working RTL for FSMs, UARTs, video and DSP blocks; useful because every example is complete and synthesizable.
- **[Book · ★★]** *Advanced FPGA Design: Architecture, Implementation, and Optimization* — Steve Kilts, Wiley-IEEE Press, 2007. ISBN 978-0-470-05437-6. [EN]
  - Pipelining, retiming, resource sharing and timing closure as architecture decisions rather than tool settings.

### Standards

- **[Standard · ★★★]** IEEE Std 1364-2005 — *IEEE Standard for Verilog Hardware Description Language*. [EN]
  - The last standalone Verilog standard; superseded by inclusion in IEEE 1800-2009.
- **[Standard · ★★★]** IEEE Std 1800-2023 — *IEEE Standard for SystemVerilog*, approved 6 December 2023. <https://ieeexplore.ieee.org/document/10458102> [EN]
  - The current normative text. Verilog is the synthesizable core of this document, not a separate standard.
- **[Standard · ★★]** IEEE Std 1800.2-2020 — *Universal Verification Methodology (UVM) Language Reference Manual*. <https://ieeexplore.ieee.org/document/9195920> [EN]
- **[Standard · ★]** IEEE Std 1076-2019 — *VHDL Language Reference Manual*, for the nine-state `std_logic` comparison. [EN]

### Papers and application notes

- **[Paper · ★★★]** Cummings, C. E. "Nonblocking Assignments in Verilog Synthesis, Coding Styles That Kill!" SNUG-2000. <https://www.sunburst-design.com/papers/> [EN]
  - The paper that settled the blocking/non-blocking convention the industry now follows.
- **[Paper · ★★★]** Cummings, C. E., and Mills, D. "Synchronous Resets? Asynchronous Resets? I am so confused! How will I ever know which to use?" SNUG-2002. [EN]
  - Reset strategy, and the async-assert/sync-release synchroniser that most designs need.
- **[Paper · ★★★]** Cummings, C. E. "Simulation and Synthesis Techniques for Asynchronous FIFO Design." SNUG-2002. [EN]
  - Gray-coded pointers, synchronised flags, and why the depth must exceed the synchroniser latency.
- **[Paper · ★★]** Cummings, C. E. "Clock Domain Crossing (CDC) Design & Verification Techniques Using SystemVerilog." SNUG-2008. [EN]
  - The taxonomy of crossings and the structure that makes each one checkable.

### Tools and open flows

- **[Code · ★★]** Verilator — compiles synthesizable Verilog to C++ for fast simulation. <https://verilator.org/guide/latest/> [EN]
- **[Code · ★★]** Yosys and OpenLane/OpenROAD with the SkyWater SKY130 PDK — a fully open synthesis-to-GDSII flow. <https://yosyshq.readthedocs.io/> · <https://openlane.readthedocs.io/> [EN]
- **[Code · ★]** Icarus Verilog and GTKWave — the long-standing open simulator and waveform viewer. <https://steveicarus.github.io/iverilog/> [EN]

---

## 32 · Primary Standards and Specification Repositories

Cross-cutting sources that back every section above. Bookmark these; they are always more authoritative than secondary writing.

- **3GPP specifications** — `portal.3gpp.org`. Search by TS/TR number or by release. All 3GPP specs are freely downloadable.
  - RAN L1: TS 38.201–38.215 · RAN L2/L3: TS 38.300, 38.321, 38.322, 38.323, 37.324, 38.331 · Core: TS 23.501, 23.502, 23.503 · Interfaces: TS 29.244 (PFCP), TS 29.281 (GTP-U) · Studies: TR 22.870, TR 38.914, TR 38.843, TR 38.865, TR 38.821
- **IEEE 802.11 Working Group** — `www.ieee802.org/11/`. Task group pages (TGbn for Wi-Fi 8), ballot status and amendment timelines.
- **IEEE Xplore / IEEE Standards Association** — normative texts of 802.11-2024, 802.11ax-2021, 802.11be-2024, 802.11bf-2025, 802.11ba-2021 (wake-up radio), 802.11ah-2016 (HaLow), 802.15.4-2020, 1905.1a-2014.
- **ITU-R** — Recommendation M.2160 (IMT-2030 framework).
- **O-RAN Alliance** — `o-ran.org/specifications`. WG1 (architecture), WG2 (A1), WG3 (E2/E2SM), WG4 (Open Fronthaul), WG6 (cloudification).
- **O-RAN Software Community (OSC)** — reference implementations and the xApp framework.
- **Wi-Fi Alliance** — `wi-fi.org`. Certification program specifications and EasyMesh.
- **RISC-V International** — `riscv.org/technical/specifications`. ISA manuals, extension specs and profiles.
- **UnifiedBus (灵衢)** — `www.unifiedbus.com`. UB base, firmware, OS and SuperPoD reference architecture documents.
- **DPDK** — `dpdk.org` (Programmer's Guide, API reference, sample applications).
- **FreeRTOS** — `freertos.org` (kernel book, API reference, LTS release notes).
- **Zephyr Project** — `zephyrproject.org` and `docs.zephyrproject.org` (releases, migration guides, devicetree, power management, MCUboot).
- **AUTOSAR** — `autosar.org/standards` (Classic Platform, Adaptive Platform, Foundation, Application Interfaces; current release R25-11).
- **MISRA** — `misra.org.uk` (MISRA C:2025, MISRA C++:2023, and the MISRA Compliance documents).
- **ISO / IEC** — `iso.org`, `iec.ch` (ISO 26262:2018, IEC 61508, IEC 62304; purchased, not free).
- **The Linux kernel** — `kernel.org` and the in-tree `Documentation/`.
- **Yocto Project** — `docs.yoctoproject.org` · **Buildroot** — `buildroot.org/downloads/manual`.
- **prpl Foundation** — prplOS, prplMesh and prpl LCM open-source projects.
- **Broadband Forum** — TR-069, TR-181, TR-369 (USP).

---

## 33 · Suggested Reading Order

**If you have 4 weeks before an interview:**

| Week | Focus                                                  | Reading                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---- | ------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | Anchor the map                                         | Note `00 MOC`; Dahlman *5G NR* chapters 6/13/14; Gast *802.11* chapters on DCF and IFS/NAV                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 2    | Your primary track                                     | RAN architect: TS 38.321/38.322/38.323 + TR 38.843 · Edge AI: xLLM technical report + Mooncake + PagedAttention · scheduling: §01-6 — TS 38.213 clause 10.1 and 9.2.1 first, then the srsRAN scheduler source, then the O-RAN WG4 CUS timing windows · Embedded/Linux: LDD3 (model chapters) + Kerrisk (IPC chapters) · interrupts: §04-4 — the Arm GICv3/v4 INTID table, then the IRQ-domain and workqueue docs · concurrency: §04-5 — McKenney perfbook memory-ordering chapters + the Franke/Russell OLS 2002 futex paper, then the "Fuss, Futexes and Furwocks" claims checked against glibc nptl/pthread_mutex_lock.c · WLAN: 802.11ax tutorial + Wi-Fi 8 tutorial · WLAN scheduling: §02-8 — Gast's DCF/backoff chapters first, then 802.11-2016 Table 9-137 side by side with 802.11-2012 Table 8-105, then `net/mac80211/airtime.c` and `rc80211_minstrel_ht.c` with the AQL commit message open · WLAN low power: §02-2 — Gast power-management chapters, then the AP Power Save primer and the SMPS critique · WLAN datapath: §02-4 against `net/mac80211/tx.c` and `rx.c` — read the code once, it is the only way the host/device split becomes obvious · WLAN join sequence: §02-5 with a capture open, then Dragonblood before repeating any claim that SAE cannot be attacked |
| 2b   | Language layer (do this once, whatever your track)     | *Modern C* (Gustedt) for C23 + Josuttis *C++23 — The Complete Guide* for the modern C++ surface; then Stroustrup *A Tour of C++*, 3rd ed. if the gap is large                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 2c   | Architecture layer (do this once, whatever your track) | White *Making Embedded Systems* ch. 2 + Lacamera *Embedded Systems Architecture* ch. 3 + Samek *Practical UML Statecharts* Part II, then Buttazzo ch. on resource access protocols if you will be asked about priority inversion                                                                                                                                                                                                                                                                                                                                                                                  |
| 3    | Future direction                                       | TR 22.870 + "What Should 6G Be?" + "Wi-Fi: Twenty-Five Years and Counting" + HeartStream (ESSERC 2025)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 4    | Consolidate                                            | Each note's **Anchors** section; the correction table in `README.md` §7; re-read only what you cannot state from memory                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

**Two rules that make this list productive rather than decorative:**

1. **Read the standard, not the summary, for anything you will be asked to quote.** Spec numbers, freeze dates and parameter values are cheap to check and expensive to get wrong.
2. **Pair every systems paper with its implementation.** xLLM/Mooncake, FlashInfer, prplMesh, DPDK and FreeRTOS all ship source. Reading the code is how you discover what the paper left out — usually the part an interviewer asks about.

---

## 34 · Verification and Maintenance

- Every entry above was checked against a publisher page, library catalogue, DOI, arXiv record or the issuing standards body before inclusion.
- Entries are recorded with the identifier that makes them checkable: **ISBN** for books, **DOI** or **arXiv ID** for papers, **specification number** for standards. Where a citation could not be independently confirmed at the time of writing, it is marked **VERIFY** rather than asserted.
- **Chinese-language entries keep their original titles.** The English text following them is a description, not a translation of the title.
- Update triggers: 3GPP TSG plenaries (four per year) for §01-1/§01-2/§01-4; IEEE 802.11 working group and Wi-Fi Alliance announcements for §02-1/§02-2/§02-3; Linux mainline and LTS releases for §08-1/§04-2; xLLM, Mooncake and agent-framework releases for §06-1/§06-2; RISC-V International ratifications for §07-1; **CPython feature releases each October, PEP acceptances and NumPy major versions for §08-3** (3.15.0 shipped 2026-10-09, so any "current Python version" claim has a one-year shelf life); **MATLAB/Simulink's March and September releases for §08-4** (R2026a in April 2026, R2026b on 2026-09-24, and Python-interoperability support moves with them); **IEEE 1800 revisions and IEEE 1800.2 (UVM) revisions for §08-5** (1800-2023 approved 2023-12-06 is current, and there is no standalone Verilog standard after 1364-2005); **WG21/WG14 meetings and GCC/Clang major releases for §08-2** — C++26 reached WG21 shipping on 2026-03-28, and compiler support tables change with every GCC and Clang major release; **AUTOSAR releases (annual, R25-11 current), MISRA document revisions, Zephyr six-month releases and LTS branches, and ISO/IEC 26262 / IEC 61508 maintenance for §04-3** — AUTOSAR releases once a year in November, so any "current AUTOSAR release" claim has a one-year shelf life; **for §02-2 specifically, track TGbn and TGbp ballot milestones plus Wi-Fi Alliance power-management certifications** — 802.11bn AP Power Save is still a draft feature and P802.11bp is at D1.0 working-group ballot, so both will move before ratification; **for §02-5, track IEEE 802.11 security amendments, Wi-Fi Alliance WPA3 specification revisions and hostapd/wpa_supplicant releases** — the frame sequence is stable but the mandatory bits move with certification (WPA3 and PMF for Wi-Fi 7, H2E-only SAE in 6 GHz), and every join failure mode in this note is observable in `wpa_supplicant -dd`, so a version bump is worth re-reading; **for §02-4, follow the mac80211/driver merge window and AP silicon offload announcements** — the packet path changes with kernel releases (`net/mac80211/`), not with standards, and vendor packet engines (PPE/NSS/Runner, WED) are documented only in release notes and SDKs, so every "which offload is available" claim needs a current device check; **for §01-5, track new 3GPP TS 38.321 / 38.331 versions and RAN2 agreements on random access, SDT and NTN timing** — field sizes, counters, windows and parameter ranges are all release-specific (the quoted baseline is TS 38.321 v17.3.0 of 2023-01), and the feature-partitioning clauses 5.1.1b–5.1.1d only exist from Rel-17, so a version bump changes which mechanisms you may claim at all. **for §01-6, track new 3GPP TS 38.213 / 38.214 / 38.331 versions, O-RAN WG4 CUS and WG1 OAD releases, and SCF FAPI revisions** — the per-slot PDCCH candidate and non-overlapped-CCE budgets, the HARQ process ceiling and the PUCCH resource-set bounds are all release-specific (the quoted baselines are TS 38.214 v18.9.0 and TS 38.321 v17.3.0), the 16-to-32 process extension only exists from Rel-17, and a 7-2x integration lives or dies on the T1a/T2a/Ta3/Ta4 windows the two boxes negotiate, so this is one section where a version bump changes answers rather than details. **for §02-6, track EasyMesh release updates, Wi-Fi Alliance Agile Multiband revisions and TGbn ballot milestones** — the steering message catalogue moves with the EasyMesh major release (v6.0 effective 2024-12-31), the decision logic is vendor code and never stable, and the roaming model itself moves with 802.11bn, where SMD is still draft (D1.x in 2026, publication projected 2028), so every "seamless roaming" claim needs a date attached. **for §02-8, track IEEE 802.11 working-group ballots (TGbe/TGbn) and the mac80211 merge window** — the EDCA default table is release-specific (802.11-2016 and 802.11-2012 disagree on every TXOP limit), the MRU set and the EHT 80 MHz tone plan only exist from 802.11be, the EMLSR timers are negotiated per device, and the AQL constants live in `include/net/cfg80211.h`, so both the protocol numbers and the implementation constants move. **for §02-7, track Wi-Fi Alliance Multi-AP specification revisions, EasyMesh test-plan updates and prplMesh major releases** — the message and TLV numberings grow with each release (v6.0 effective 2024-12-31) and profile negotiation is what actually decides the feature set of a mixed-vendor network, so a version bump changes both the protocol detail and the interop story. **for §06-3, track major scikit-learn, PyTorch and JAX releases, and new textbook editions** **for §04-4, track Arm GIC specification revisions, RISC-V International AIA document revisions, and the mainline workqueue and deferred-work conversions** — the tasklet-to-WQ_BH migration changes which mechanism is correct for new code, the AIA document carries clarifications with each revision (v1.0 ratified June 2023, revision 2025-03-12), and the APLIC/IMSIC drivers only exist from Linux 6.10, so the controller you can rely on depends on the kernel you ship. **for §04-5, track the kernel fence (the per-CPU and scheduling primitives that land with each release), the glibc NPTL sources, and the sanitizer support in your toolchain** — the futex operations, the `clone3` flags and the fd-ified kernel objects (pidfd in 5.3, `waitid(P_PIDFD)` in 5.4, io_uring in 5.1) all have a minimum kernel version, and POSIX.1-2017 is stable while everything on top of it is not, so every "which primitive" answer needs a kernel and a toolchain version attached. — the quoted baseline is scikit-learn 1.9.1 and PyTorch 2.14.1, both September 2026, and the practical rules of thumb (which model family wins on tabular data, what precision a given accelerator supports) are properties of the ecosystem rather than of the theory, so they move faster than the mathematics does.

---

## Copyright

Copyright (c) 2026 **Washington Ruan**. All rights reserved.

All titles, ISBNs, DOIs and specification numbers are the property of their respective publishers, authors and standards bodies and are reproduced here for reference purposes.

---

© 2026 Washington Ruan. All rights reserved.
