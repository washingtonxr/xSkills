---
title: Reading List — Comms × Heterogeneous Compute × AI
lang: en
category: reading-list
version: 1.3
last-updated: 2026-10-22
copyright: "Copyright (c) 2026 Washington Ruan. All rights reserved."
---

# Reading List

**Books, papers, standards and technical reports for the PersonalSkills knowledge base**

> This file supports the 19 notes in `knowledge-graph/`. Sections are numbered `GG-x` to match the
> vault's domain groups:
> `01-x` cellular and mobile communications — `01-1` 5G-Advanced and 6G Radio Access, `01-2` NR RAN L2,
> `01-3` AI/ML for RAN and O-RAN RIC, `01-4` RedCap/eRedCap/NTN;
> `04-x` WLAN — `04-1` Wi-Fi generations, `04-2` power saving, `04-3` WFA/EasyMesh/prpl ecosystem;
> `06-1` WSN; `07-x` embedded and systems software — `07-1` RTOS, `07-2` Linux embedded, `07-3` software architecture;
> `08-x` data plane and heterogeneous compute — `08-1` DPDK/UPF, `08-2` cloud-edge-end;
> `10-x` AI — `10-1` LLM inference, `10-2` agent systems; `12-1` RISC-V;
> `13-x` programming — `13-1` toolchain and performance, `13-2` C and C++.
> Sections `19`–`21` collect primary standards repositories, a reading order, and maintenance notes.
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
  - Chinese translation of the first English edition. Widely used as the onboarding text in Chinese 5G R&D teams; useful when you need to quote standard terminology in Chinese and match it to the English term.
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

---

## 01-3 · AI/ML for RAN and O-RAN RIC


### Books

- **[Book · EN · ★★★]** *Open RAN: Technology and Ecosystem* — Vladimir Yanover · Wiley, January 2025 · ISBN 9781394241149 · DOI 10.1002/9781394241170
  - The most architecture-complete O-RAN reference. Explicit chapters on the Non-RT RIC and rApps, the A1 policy interface, Near-RT RIC functional procedures, the E2 service models (REPORT, INSERT, CONTROL, POLICY), xApp hosting, RAN decomposition, and **AI/ML support in the O-RAN architecture**. Written by an O-RAN contributor, so it reflects what the specs actually say.
- **[Book · EN · ★★]** *Open RAN Explained: The New Era of Radio Networks* — Jyrki T. J. Penttinen, Michele Zarri, Dongwook Kim · Wiley, 2024 · ISBN 9781119847045
  - Shorter and more accessible: network modularisation, RAN split options, deployment scenarios, and the GSMA/TIP/3GPP context around O-RAN. Read first if you are new to the topic; use Yanover for depth.

### Papers

- **[Paper · EN · ★★★]** "Managing O-RAN Networks: xApp Development From Zero to Hero" — J. F. Santos, A. Huff, D. Campos, K. V. Cardoso, C. B. Both, L. A. DaSilva · *IEEE Communications Surveys & Tutorials*, 2024
  - A hands-on tutorial on building, onboarding, debugging and testing an xApp against the O-RAN Software Community stack: descriptor and schema files, RMR messaging, SDL storage, E2 service models, and E2Sim-based testing. This is what turns "I know what an xApp is" into "I have built one".
- **[Paper · EN · ★★]** "Explainable AI in 6G O-RAN: A Tutorial and Survey on Architecture, Use Cases, Challenges, and Future Research" — B. Brik, H. Chergui, L. Zanzi, F. Devoti, A. Ksentini, M. S. Siddiqui, X. Costa-Pérez, C. Verikoukis · *IEEE Communications Surveys & Tutorials*, vol. 27, no. 5, pp. 2826–2859, 2024
  - Survey of XAI methods mapped onto the O-RAN architecture, plus use cases, security aspects and open challenges. The right citation when a discussion turns to "how do you make an AI scheduler trustworthy enough to deploy".
- **[Paper · EN · ★★]** "End-to-End Learning for OFDM: From Neural Receivers to Pilotless Communication" (see §01-1)
  - The PHY-side evidence base that motivates putting AI inside the RAN at all.
- **[Paper · EN · ★★]** "Age of Information: An Introduction and Survey" (see §06-1)
  - Relevant here because AoI is one of the few metrics a learned scheduler can optimise directly, which classical proportional-fair scheduling never did.

### Standards and reports

- **[Spec · ★★★]** **3GPP TR 38.843** — "Study on AI/ML for NR air interface" (Rel-18)
  - The 3GPP entry point for AI in the air interface: beam management, CSI compression feedback and positioning. Where the "AI-native air interface" conversation starts, and the baseline that Rel-19/Rel-21 work builds on.
- **[Standard · ★★★]** **O-RAN Alliance specifications** — O-RAN.WG1 (Architecture Description), O-RAN.WG2 (A1AP, A1 policy), O-RAN.WG3 (E2AP, E2SM-KPM, E2SM-RC, E2SM-CCC), O-RAN.WG4 (Open Fronthaul), O-RAN.WG6 (Cloudification and Orchestration)
  - The normative source. At minimum, know the architecture description and one E2 service model well enough to describe a subscription→indication→control loop concretely.
- **[Doc · ★★]** **O-RAN Software Community (OSC)** — reference implementations of the Near-RT RIC, E2 interface and xApp framework
  - The practical substrate for the "from zero to hero" tutorial above. Useful for getting real logs rather than simulated ones.
- **[Doc · ★]** **O-RAN Alliance white paper "O-RAN: Towards an Open and Smart RAN"** (2018)
  - Short founding-document framing: why openness, why intelligence, what the architecture was meant to enable.

---

## 01-4 · Cellular IoT — RedCap, eRedCap and NTN


### Papers

- **[Paper · EN · ★★★]** "Resource Management for Reduced Capability New Radio Devices in Beyond 5G Networks: Opportunities and Research Road Map" — N. S. Ferdous, M. Z. Hassan, I. Ahmed, L. Akter · *IEEE Xplore* document 10757145
  - The best single overview of RedCap: what was reduced (bandwidth, MIMO layers, baseband complexity, DL modulation order, RF cost), the three use-case families (industrial sensors, wearables, video surveillance), and the coexistence problem with legacy NR. Covers coverage, capacity and energy-efficiency solutions plus a research roadmap.
- **[Paper · EN · ★★]** "Positioning of RedCap Devices in 5G Networks" — F. Munier, Z. Xiong, R. Shreevastav, X. Jiang, Y. Lyazidi, D. Shrestha, C. Zhang, G. Lindmark, J. Nygren, S. Moloudi, S. Dwivedi, F. Gunnarsson · *IEEE Communications Magazine*, vol. 62, no. 8, pp. 110–116, 2024 · DOI 10.1109/MCOM.001.2300802
  - Ericsson-authored account of the Rel-18 positioning enhancement for RedCap — extending effective bandwidth by frequency hopping — with 3GPP channel-model simulation results. Concrete and recent.
- **[Paper · EN · ★]** "Age of Information: An Introduction and Survey" (see §06-1)
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

## 04-1 · WLAN — Wi-Fi Generations Evolution


### Books

- **[Book · EN · ★★★]** *802.11 Wireless Networks: The Definitive Guide*, 2nd ed. — Matthew Gast · O'Reilly, 2005
  - Still the clearest explanation of the 802.11 MAC: DCF/PCF, CSMA/CA, the interframe spaces, NAV, RTS/CTS, fragmentation, power save and the management/frame taxonomy. Wi-Fi 4 through 8 all build on this substrate, and candidates who cannot explain the IFS/NAV mechanics cannot explain what OFDMA changed.
- **[Book · EN · ★★]** *Next Generation Wireless LANs: 802.11n and 802.11ac*, 2nd ed. — Eldad Perahia, Robert Stacey · Cambridge University Press, 2013
  - The authoritative treatment of MIMO, channel bonding, beamforming sounding and the 802.11n/ac PHY. Read for the design rationale behind features now treated as table stakes.

### Papers

- **[Paper · EN · ★★★]** "Wi-Fi: Twenty-Five Years and Counting" — G. Geraci, F. Meneghello, F. Wilhelmi, D. López-Pérez, I. Val, L. Galati Giordano, C. Cordeiro, M. Ghosh, E. Knightly, B. Bellalta · *Proceedings of the IEEE*, vol. 113, no. 11, pp. 1290–1336, 2025 · arXiv:2507.09613
  - The first single tutorial to span 802.11b through 802.11bn, organised by *mechanism* rather than by generation: spectrum, PHY, MAC, multi-user, power save, multi-band aggregation, multi-AP coordination. The best long read for understanding why each generation looks the way it does, and the appendix covers what comes beyond 802.11bn (mmWave, sensing, AI/ML, security).
- **[Paper · EN · ★★★]** "A Tutorial on Wi-Fi 8: The Journey to Ultra High Reliability" — A. Karamyshev, I. Levitsky, D. Bankov, E. Khorov · *Problems of Information Transmission*, vol. 61, no. 2, pp. 164–210, 2025 · DOI 10.1134/S003294602502005X
  - Feature-by-feature treatment of 802.11bn: distributed-tone resource units, unequal modulation, prioritised and non-primary channel access, advanced roaming, and multi-AP coordination, with explicit targets (throughput across SINR levels, 95th-percentile latency, packet loss, power). The primary reference behind note 04-1's Wi-Fi 8 section.
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
  - The WNG Standing Committee contributions on post-802.11bn direction: determinism over nominal rate, uplink asymmetry driven by AI workloads, AI-native PHY, deterministic MAC, Age-of-Information scheduling, and the LAN-controller-plus-APs AI architecture. Cited in note 04-1; verify the current citation before quoting.

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
  - Relevant to the ISAC/sensing convergence discussed in note 04-1's future-generation section.
- **[Doc · ★★]** **IEEE 802.11 Working Group timelines and TGbn status pages**
  - The source for ballot and approval dates. Use these rather than secondary reporting when a date matters.

---

## 04-2 · WLAN — Power Saving Mechanisms and Evolution

Supports note `04-2 WLAN - Power Saving Mechanisms and Evolution`. Where an item duplicates a reference already listed under **§04-1**, it is cross-referenced rather than repeated, with the specific part to read.

### Books

- **[Book · EN · ★★★]** *802.11 Wireless Networks: The Definitive Guide*, 2nd ed. — Matthew Gast · O'Reilly, 2005
  - The power-management chapters are still the clearest plain-English account of the PM bit, TIM/DTIM, PS-Poll and the beacon-synchronised model that every later mechanism is a reaction against. Read this before any paper on TWT, or the motivation will not land.
- **[Book · EN · ★★]** *Next Generation Wireless LANs: 802.11n and 802.11ac*, 2nd ed. — Eldad Perahia, Robert Stacey · Cambridge University Press, 2013
  - Listed in §04-1; for this note use its treatment of SMPS, operating-mode feedback and the power cost of MIMO chains.
- **[Book · CN · ★]** 《802.11无线网络权威指南（第2版）》 — Matthew Gast · O'Reilly 中文版
  - Chinese edition of the Gast volume above, for the power-management and MAC chapters. `VERIFY` ISBN and edition year before citing.

### Papers

- **[Paper · EN · ★★★]** "A Primer on AP Power Save in Wi-Fi 8: Overview, Analysis, and Open Challenges" — R. Sanchez-Vital, A. Belogaev, C. Gomez, J. Famaey, E. Garcia-Villegas · *IEEE Wireless Communications*, 2025 · DOI 10.1109/MCOM.004.2400486 · preprint arXiv:2411.17424
  - The definitive reference for what Wi-Fi 8 changes: Scheduled Power Save, (Semi-)Dynamic Power Save, Cross-Link Power Save, plus wake-up-radio integration and STA offloading. Quantifies up to ~28% average AP power reduction on a dataset from 470 real campus APs, and names the open challenges (legacy compatibility, policy selection).
- **[Paper · EN · ★★★]** "What is Wrong/Right with IEEE 802.11n Spatial Multiplexing Power Save Feature?" — I. Pefkianakis, C.-Y. Li, S. Lu · *IEEE ICNP*, 2011
  - The paper that proves power and energy are different metrics. Measurements on real 802.11n hardware show ~2.5 W for a high-rate MIMO receiver, up to 1.15 W saved by SMPS, but also that a single chain can be worse per bit; their MRES algorithm beats SMPS by up to 37%, and optimal chain selection differs from the SMPS choice by up to 78.6% in per-bit energy.
- **[Paper · EN · ★★★]** "A Tutorial on IEEE 802.11ax High Efficiency WLANs" — E. Khorov, A. Kiryanov, A. Lyakhov, G. Bianchi · *IEEE Communications Surveys & Tutorials*, vol. 21, no. 1, pp. 197–216, 2019
  - Listed in §04-1. For this note it is the primary source on TWT: individual versus broadcast, implicit versus explicit, trigger-enabled service periods, and Opportunistic Power Save.
- **[Paper · EN · ★★★]** "A Tutorial on Wi-Fi 8: The Journey to Ultra High Reliability" — A. Karamyshev, I. Levitsky, D. Bankov, E. Khorov · *Problems of Information Transmission*, vol. 61, no. 2, pp. 164–210, 2025 · DOI 10.1134/S003294602502005X
  - Listed in §04-1. For this note, read its power-saving part: unavailability reporting, periodic and dynamic unavailability operation, dynamic power save, cross-link power save, and scheduled AP power save.
- **[Paper · EN · ★★★]** "Wi-Fi: Twenty-Five Years and Counting" — G. Geraci, F. Meneghello, F. Wilhelmi, D. López-Pérez, I. Val, L. Galati Giordano, C. Cordeiro, M. Ghosh, E. Knightly, B. Bellalta · *Proceedings of the IEEE*, vol. 113, no. 11, pp. 1290–1336, 2025 · arXiv:2507.09613
  - Listed in §04-1. Its power-saving section is the best single-source cross-generation comparison, because it is organised by mechanism rather than by amendment.
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

## 04-3 · WLAN Ecosystem — WFA, EasyMesh and prpl


### Books

- **[Book · EN · ★★★]** *802.11 Wireless Networks: The Definitive Guide*, 2nd ed. — Matthew Gast (see §04-1)
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

---

## 06-1 · Wireless Sensor Networks and Low-Power MAC


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

## 07-1 · Embedded Systems, RTOS and Hardware Interfaces


### Books

- **[Book · EN · ★★★]** *Mastering the FreeRTOS Real Time Kernel — A Hands On Tutorial Guide* — Richard Barry · FreeRTOS; release v1.1.0, 19 August 2024 (references FreeRTOS V10.6.2)
  - The official kernel book, freely available with companion source. Covers tasks, scheduling, queues, semaphores and mutexes, direct-to-task notifications, stream and message buffers, memory management, and priority inheritance. Read this alongside the source; the context-switch and tick-handling detail is what separates real RTOS understanding from API familiarity.
- **[Book · EN · ★★]** *Making Embedded Systems: Design Patterns for Great Software*, 2nd ed. — Elecia White · O'Reilly, 2021
  - Practical patterns for resource-constrained firmware: state machines, hardware abstraction, debugging without a debugger, and how to structure code you can actually test on target.
- **[Book · EN · ★★]** *Embedded Systems Architecture: Explore System-Level Design and Advanced Features* — Daniele Lacamera · Packt, 2nd ed. 2021
  - System-level view: boot sequence, linker scripts and memory layout, interrupt and exception handling, RTOS integration, and the build/flash/debug flow. Good for connecting bare-metal mechanics to the Linux view in note 07-2.
- **[Book · EN · ★★★]** *Hard Real-Time Computing Systems: Predictable Scheduling Algorithms and Applications*, 3rd ed. — Giorgio C. Buttazzo · Springer, 2011
  - The rigorous treatment of schedulability analysis, rate-monotonic and EDF scheduling, priority inversion and aperiodic servers. This is what makes a "hard real-time" claim defensible rather than rhetorical.
- **[Book · EN/CN · ★★]** *Computer Organization and Design RISC-V Edition* (see §12-1)
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

## 07-2 · Linux Embedded Development — Drivers, Applications and Core Subsystems


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
- **[Book · EN · ★]** *Understanding Linux Network Internals* — Christian Benvenuti · O'Reilly, 2005 (see §08-1)

### Books — system and application programming

- **[Book · EN · ★★★]** *The Linux Programming Interface* — Michael Kerrisk · No Starch Press, 2010
  - The definitive system-programming reference: processes, threads, IPC, signals, timers, file I/O, memory mapping, and sockets. Over 1500 pages, with every syscall documented against its behaviour. This is the book to own for the IPC and networking sections of note 07-2.
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
  - The two build-system references that matter. Use the Yocto LTS release names recorded in note 07-2 when citing versions.
- **[Doc · ★★]** **U-Boot documentation** and **Device Tree Specification** (devicetree.org)
  - Boot chain and hardware description. The DT spec is short; read it once properly.
- **[Doc · ★★]** **cyclictest / rt-tests documentation** and the **PREEMPT_RT wiki**
  - Real-time verification tooling. PREEMPT_RT was merged into mainline in Linux 6.12 for x86, arm64 and RISC-V; 32-bit ARM followed later.

---

## 07-3 · Embedded Software Architecture — Patterns, Layering and Wireless System Structure


### Books — architecture and design method

- **[Book · ★★★ · EN]** **Making Embedded Systems: Design Patterns for Great Software**, 2nd ed. — Elecia White, O'Reilly, 2024. ISBN 9781098151546. The most readable entry point into embedded architecture as a *design* discipline rather than a driver catalogue. Chapter 2 ("Creating a System Architecture") is the one to read before an interview; the second edition adds IoT/networked sensors, motors and data-handling strategy. Chapters on reducing RAM, code space and power are directly quotable.
- **[Book · ★★★ · EN]** **Embedded Systems Architecture**, 2nd ed. — Daniele Lacamera, Packt, Jan 2023. ISBN 9781803239545 (342 pp.). Chapter 3 is literally "Architectural Patterns"; also covers boot-up procedure, memory management, distributed/IoT architecture, parallel tasks and scheduling, and Trusted Execution Environment. Good coverage of the memory-isolation-oriented view of RTOS design.
- **[Book · ★★ · EN]** **Software Engineering for Embedded Systems: Methods, Practical Techniques, and Applications**, 2nd ed. — Robert Oshana and Mark Kraeling (eds.), Newnes/Elsevier, 2019. ISBN 978-0-12-809448-8 (1st ed. 2013, ISBN 978-0-12-415917-4). Multi-author reference; the relevant chapters are on architecture and design patterns, real-time building blocks, safety-critical development, and multicore software development. Contributors include Jean Labrosse and Bruce Douglass.
- **[Book · ★★ · EN]** **Better Embedded System Software** — Philip Koopman, Drumnadrochit Education, 2010. ISBN 978-0-9844490-0-2. Short, opinionated and practice-driven: requirements, design, implementation and test discipline specifically for embedded. Strong on the failure modes that architecture should prevent.
- **[Book · ★ · EN]** **The Art of Designing Embedded Systems**, 2nd ed. — Jack Ganssle, Newnes, 2008. Essays rather than a textbook; useful for the project-reality side (estimation, firmware process, why projects fail). `VERIFY` the exact edition/ISBN before citing.

### Books — execution models, scheduling and time-triggered design

- **[Book · ★★★ · EN]** **Hard Real-Time Computing Systems: Predictable Scheduling Algorithms and Applications**, 3rd ed. — Giorgio C. Buttazzo, Springer, 2011. ISBN 978-1-4614-0676-1, DOI 10.1007/978-1-4614-0676-1 (Real-Time Systems Series, vol. 24). The standard text for the scheduling theory in note 07-3 §2.3: periodic and aperiodic task scheduling, fixed- and dynamic-priority servers, resource access protocols, limited-preemptive scheduling, overload handling, kernel and application design issues.
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
- **[Spec · ★★ · EN]** **ETSI TS 103859** (O-RAN.WG4.CUS.0) — O-RAN Fronthaul Control, User and Synchronization Plane. Defines the **7-2x** split, Category A/B O-RUs, eCPRI transport and IQ compression. The normative source for note 07-3 §6.3.
- **[Spec · ★ · EN]** **O-RAN.WG1 Architecture Description** and **O-RAN.WG3 (E2/E2SM)** — the architecture and near-RT RIC interface specs. See §18.
- **[Spec · ★★ · EN]** **3GPP TS 38.401** — NG-RAN architecture description, including the CU/DU split. `VERIFY` the F1/E1 part numbers before quoting them.

### Documentation and code

- **[Doc · ★★★ · EN]** **Zephyr Project documentation** — `docs.zephyrproject.org`. Releases, devicetree, Kconfig, power management, and MCUboot. Current stable **4.4.0** (2026-04-14); **3.7.0** is LTS3 (2024-07-26, EOL 2029-07-27); LTS4 planned as 5.0 (Oct 2027). Read the *release and migration guides* — they are the best available example of how a serious embedded project manages long-term compatibility.
- **[Code · ★★ · EN]** **MCUboot** — open-source secure bootloader for 32-bit MCUs, integrated with Zephyr. Study it for the A/B update, image format, signature verification and swap/overwrite strategies described in note 07-3 §9.
- **[Code · ★★ · EN]** **QP / QP/C / QP/C++** (Quantum Leaps) — the open-source active-object and hierarchical state machine framework behind Samek's book. Read `qpc` source for a production-quality HSM dispatcher and event queue implementation in C.
- **[Code · ★ · EN]** **FreeRTOS kernel** — `freertos.org`; see §07. Read its `port.c` for the PendSV context-switch mechanics that the execution model in note 07-3 §2 depends on.
- **[Doc · ★ · EN]** **MCUboot / RAUC / SWUpdate / Mender documentation** — three different answers to the same update problem; comparing them is the fastest way to internalise what is *essential* in an OTA architecture versus what is implementation detail.

---

## 08-1 · DPDK User Plane and 5G UPF


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

## 08-2 · Cloud-Edge-End Collaboration and Heterogeneous Computing


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
  - Primary source for the Huawei interconnect discussed in note 08-2: **《灵衢基础规范 2.0》** (UB Base Specification — architecture, protocol and programming models), **《灵衢固件规范 2.0》** (firmware architecture and interfaces), **《灵衢使能操作系统参考设计 2.0》** (UB OS Component), and **《基于灵衢的超节点参考架构白皮书》** (SuperPoD reference architecture: bus-level interconnect, unified protocol, peer-to-peer coordination, full-resource pooling, large-scale networking, high availability). UB Base Specification 2.1 adds 224/256 Gbit/s rates, reliable rerouting and lower multi-path latency. The 2.0 specifications were opened at HUAWEI CONNECT 2025 on 18 September 2025.
- **[Doc · ★★]** **昇腾 950 NPU 架构白皮书** (Ascend 950 NPU Architecture White Paper)
  - Chip-level detail: on-chip memory bandwidth and capacity, 72× HiLink ports at up to 112 Gbps, the UB2.0 protocol with URMA asynchronous copy and UB Memory global load/store semantics, PCIe GEN5 x16 reuse, and 2×400 Gbps UBoE for carrying UB over Ethernet.
- **[Doc · ★★]** **Ascend CANN documentation** (Huawei heterogeneous compute architecture)
  - Runtime, graph and operator-level interfaces for the NPU software stack.
- **[Doc · ★]** **ODCC (Open Data Center Committee) technical reports**
  - Chinese-industry server and datacentre architecture specifications, useful for the standards-body perspective in note 08-2.

---

## 10-1 · LLM Inference Engines and xLLM


### Papers

- **[Paper · EN · ★★★]** "xLLM Technical Report" — xLLM team (JD.com) · arXiv:2510.14686, 2025
  - The primary reference for the framework in note 10-1: the service–engine decoupled architecture, optimisation for Chinese AI accelerators (Ascend NPU, Cambricon MLU, Moore Threads GPU, Hygon DCU, MetaX MACA, Iluvatar CoreX), and hybrid KV cache management built on Mooncake with intelligent offloading and prefetching. Battle-tested at scale in JD.com's retail business, which is the strongest available evidence for the engineering claims.
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

## 10-2 · Agent Systems and Edge Orchestration


### Papers

- **[Paper · EN · ★★★]** "gRPC-Routed Agent Framework for Tasking (GRAFT)" · CAIS '26 · DOI 10.1145/3786335.3813216
  - The specific paper behind note 10-2: sessioned gRPC routing across heterogeneous personal devices, capability-aware task routing in a small-language-model agent mesh. Note that GRAFT is an overloaded acronym — cite the DOI, not the name.
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

## 12-1 · RISC-V for Communication Infrastructure


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

## 13-1 · Languages, Toolchain and Performance Engineering


### Books

- **[Book · EN · ★★★]** *Computer Systems: A Programmer's Perspective*, 3rd ed. — Bryant, O'Halloran (see §08-2)
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

## 13-2 · C and C++ Programming — Language Features, STL and Systems Practice


Supports vault note `16`. Note that §13 covers toolchain, profiling and performance engineering; this section is the language itself.

### Books — C

- **[Book · EN/CN · ★★★]** *The C Programming Language*, 2nd ed. — Brian W. Kernighan, Dennis M. Ritchie · Prentice Hall, 1988 · ISBN 9780131103627 · Chinese 《C程序设计语言(第2版·新版)》, translated by 徐宝文, 李志 · 机械工业出版社, 2004 · ISBN 9787111128069 (典藏版 reissue ISBN 9787111617945)
  - Written by the language's designer. Still the clearest account of pointers, arrays and the preprocessor — and still thin on the parts the standard later changed. Read it for the model, then read a modern text for C11/C23.
- **[Book · EN · ★★★]** *Modern C* — Jens Gustedt · Manning, 2019 (2nd ed. 2022, freely available online)
  - The modern replacement for K&R: written by a WG14 member and organised around C17/C23 rather than C89. Covers `stdint.h`, atomics, alignment, `_Generic`, and the undefined-behaviour traps that K&R never had to warn about. **This is the C book to read if you already know C.**
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
- **[Book · EN · ★★★]** *Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14* — Scott Meyers · O'Reilly, 2014 (see §13-1)
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
- **[Paper · ★★]** *"Memory Ordering in C++"* and Paul E. McKenney's **perfbook** (see §13-1)
  - The memory model is the part of C++ most people get wrong. Read the model, not the rules of thumb.
- **[Doc · ★]** **CppCon talks** on `std::execution` (senders/receivers), reflection (P2996), and `std::simd` — the fastest route to C++26 material, since no book covers it yet.

---

## 19 · Primary Standards and Specification Repositories


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

## 20 · Suggested Reading Order


**If you have 4 weeks before an interview:**

| Week | Focus | Reading |
| --- | --- | --- |
| 1 | Anchor the map | Note `00 MOC`; Dahlman *5G NR* chapters 6/13/14; Gast *802.11* chapters on DCF and IFS/NAV |
| 2 | Your primary track | RAN architect: TS 38.321/38.322/38.323 + TR 38.843 · Edge AI: xLLM technical report + Mooncake + PagedAttention · Embedded/Linux: LDD3 (model chapters) + Kerrisk (IPC chapters) · WLAN: 802.11ax tutorial + Wi-Fi 8 tutorial · WLAN low power: §04-2 — Gast power-management chapters, then the AP Power Save primer and the SMPS critique |
| 2b | Language layer (do this once, whatever your track) | *Modern C* (Gustedt) for C23 + Josuttis *C++23 — The Complete Guide* for the modern C++ surface; then Stroustrup *A Tour of C++*, 3rd ed. if the gap is large |
| 2c | Architecture layer (do this once, whatever your track) | White *Making Embedded Systems* ch. 2 + Lacamera *Embedded Systems Architecture* ch. 3 + Samek *Practical UML Statecharts* Part II, then Buttazzo ch. on resource access protocols if you will be asked about priority inversion |
| 3 | Future direction | TR 22.870 + "What Should 6G Be?" + "Wi-Fi: Twenty-Five Years and Counting" + HeartStream (ESSERC 2025) |
| 4 | Consolidate | Each note's **Anchors** section; the correction table in `README.md` §7; re-read only what you cannot state from memory |

**Two rules that make this list productive rather than decorative:**

1. **Read the standard, not the summary, for anything you will be asked to quote.** Spec numbers, freeze dates and parameter values are cheap to check and expensive to get wrong.
2. **Pair every systems paper with its implementation.** xLLM/Mooncake, FlashInfer, prplMesh, DPDK and FreeRTOS all ship source. Reading the code is how you discover what the paper left out — usually the part an interviewer asks about.

---

## 21 · Verification and Maintenance


- Every entry above was checked against a publisher page, library catalogue, DOI, arXiv record or the issuing standards body before inclusion.
- Entries are recorded with the identifier that makes them checkable: **ISBN** for books, **DOI** or **arXiv ID** for papers, **specification number** for standards. Where a citation could not be independently confirmed at the time of writing, it is marked **VERIFY** rather than asserted.
- **Chinese-language entries keep their original titles.** The English text following them is a description, not a translation of the title.
- Update triggers: 3GPP TSG plenaries (four per year) for §01-1/§01-2/§01-4; IEEE 802.11 working group and Wi-Fi Alliance announcements for §04-1/§04-2/§04-3; Linux mainline and LTS releases for §13-1/§07-2; xLLM, Mooncake and agent-framework releases for §10-1/§10-2; RISC-V International ratifications for §12-1; **WG21/WG14 meetings and GCC/Clang major releases for §13-2** — C++26 reached WG21 shipping on 2026-03-28, and compiler support tables change with every GCC and Clang major release; **AUTOSAR releases (annual, R25-11 current), MISRA document revisions, Zephyr six-month releases and LTS branches, and ISO/IEC 26262 / IEC 61508 maintenance for §07-3** — AUTOSAR releases once a year in November, so any "current AUTOSAR release" claim has a one-year shelf life; **for §04-2 specifically, track TGbn and TGbp ballot milestones plus Wi-Fi Alliance power-management certifications** — 802.11bn AP Power Save is still a draft feature and P802.11bp is at D1.0 working-group ballot, so both will move before ratification.

---

## Copyright

Copyright (c) 2026 **Washington Ruan**. All rights reserved.

All titles, ISBNs, DOIs and specification numbers are the property of their respective publishers, authors and standards bodies and are reproduced here for reference purposes.

---

© 2026 Washington Ruan. All rights reserved.
