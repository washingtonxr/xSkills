---
title: Reading List — Comms × Heterogeneous Compute × AI
lang: en
category: reading-list
version: 1.0
last-updated: 2026-10-22
copyright: "Copyright (c) 2026 Washington Ruan. All rights reserved."
---

# Reading List

**Books, papers, standards and technical reports for the PersonalSkills knowledge base**

> This file supports the 16 notes in `knowledge-graph/`. Sections are numbered to match:
> `01` = 5G-Advanced and 6G Radio Access, `02` = NR RAN L2, `03` = AI/ML for RAN and O-RAN RIC,
> `04` = WLAN Generations, `05` = RedCap/eRedCap/NTN, `06` = WSN, `07` = Embedded RTOS,
> `08` = DPDK/UPF, `09` = Cloud-Edge-End, `10` = LLM Inference, `11` = Agent Systems,
> `12` = RISC-V, `13` = Languages and Performance, `14` = WLAN Ecosystem, `15` = Linux Embedded.
> Sections `16`–`18` collect primary standards repositories, a reading order, and maintenance notes.
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

## 01 · 5G-Advanced and 6G Radio Access

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
  - Becomes the authoritative "what is in Rel-21" summary once the release closes. Until then, use the four freeze milestones recorded in note 01.
- **[Standard · ★★]** **3GPP TS 38.300** — "NR; Overall description" (Stage-2)
  - The entry point to the whole NR specification set. Read §9 (protocol architecture) and the L2 sections before any deeper TS.
- **[Standard · ★★]** **3GPP TS 38.211 / 38.212 / 38.213 / 38.214** — Physical channels and modulation; multiplexing and channel coding; physical layer procedures for control; physical layer procedures for data
  - The L1 core. Use as lookup, not as reading.

---

## 02 · 5G NR RAN Layer 2 Protocol Stack

### Books

- **[Book · EN/CN · ★★★]** *5G NR: The Next Generation Wireless Access Technology* (see §01) — chapters 6 (radio-interface architecture), 13 (retransmission protocols), 14 (scheduling)
  - The most efficient path to L2 competence. Chapter 14 in particular covers the interaction between BSR, grant, HARQ and QoS enforcement that most candidates hand-wave.
- **[Book · EN · ★★]** *5G NR: Architecture, Technology, Implementation, and Operation of 3GPP New Radio Standards* (see §01)
  - Chapter-level detail on MAC/RLC/PDCP/SDAP procedures and RRC states. Complements Dahlman with a more specification-structured layout.
- **[Book · EN · ★]** *LTE — The UMTS Long Term Evolution* (see §01)
  - For the inherited parts of L2 — RLC modes, PDCP, status reporting — LTE still has the clearest explanations, and NR's deviations are easier to see against that baseline.

### Papers

- **[Paper · EN · ★★]** "A Survey on Low Latency Towards 5G: RAN, Core Network and Caching Solutions" — I. Parvez, A. Rahmati, I. Guvenc, A. I. Sarwat, H. Dai · *IEEE Communications Surveys & Tutorials*, vol. 20, no. 4, pp. 3098–3129, 2018
  - Maps every latency contributor across the RAN and core. The reference for decomposing a 1 ms or 5 ms budget into per-stage terms, which is exactly what a URLLC question asks you to do.
- **[Paper · EN · ★]** "Toward Massive, Ultra-Reliable, and Low-Latency Wireless Communication with Short Packets" (see §01)
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

## 03 · AI/ML for RAN and O-RAN RIC

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
- **[Paper · EN · ★★]** "End-to-End Learning for OFDM: From Neural Receivers to Pilotless Communication" (see §01)
  - The PHY-side evidence base that motivates putting AI inside the RAN at all.
- **[Paper · EN · ★★]** "Age of Information: An Introduction and Survey" (see §06)
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

## 04 · WLAN — Wi-Fi Generations Evolution

### Books

- **[Book · EN · ★★★]** *802.11 Wireless Networks: The Definitive Guide*, 2nd ed. — Matthew Gast · O'Reilly, 2005
  - Still the clearest explanation of the 802.11 MAC: DCF/PCF, CSMA/CA, the interframe spaces, NAV, RTS/CTS, fragmentation, power save and the management/frame taxonomy. Wi-Fi 4 through 8 all build on this substrate, and candidates who cannot explain the IFS/NAV mechanics cannot explain what OFDMA changed.
- **[Book · EN · ★★]** *Next Generation Wireless LANs: 802.11n and 802.11ac*, 2nd ed. — Eldad Perahia, Robert Stacey · Cambridge University Press, 2013
  - The authoritative treatment of MIMO, channel bonding, beamforming sounding and the 802.11n/ac PHY. Read for the design rationale behind features now treated as table stakes.

### Papers

- **[Paper · EN · ★★★]** "Wi-Fi: Twenty-Five Years and Counting" — G. Geraci, F. Meneghello, F. Wilhelmi, D. López-Pérez, I. Val, L. Galati Giordano, C. Cordeiro, M. Ghosh, E. Knightly, B. Bellalta · *Proceedings of the IEEE*, vol. 113, no. 11, pp. 1290–1336, 2025 · arXiv:2507.09613
  - The first single tutorial to span 802.11b through 802.11bn, organised by *mechanism* rather than by generation: spectrum, PHY, MAC, multi-user, power save, multi-band aggregation, multi-AP coordination. The best long read for understanding why each generation looks the way it does, and the appendix covers what comes beyond 802.11bn (mmWave, sensing, AI/ML, security).
- **[Paper · EN · ★★★]** "A Tutorial on Wi-Fi 8: The Journey to Ultra High Reliability" — A. Karamyshev, I. Levitsky, D. Bankov, E. Khorov · *Problems of Information Transmission*, vol. 61, no. 2, pp. 164–210, 2025 · DOI 10.1134/S003294602502005X
  - Feature-by-feature treatment of 802.11bn: distributed-tone resource units, unequal modulation, prioritised and non-primary channel access, advanced roaming, and multi-AP coordination, with explicit targets (throughput across SINR levels, 95th-percentile latency, packet loss, power). The primary reference behind note 04's Wi-Fi 8 section.
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
  - The WNG Standing Committee contributions on post-802.11bn direction: determinism over nominal rate, uplink asymmetry driven by AI workloads, AI-native PHY, deterministic MAC, Age-of-Information scheduling, and the LAN-controller-plus-APs AI architecture. Cited in note 04; verify the current citation before quoting.

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
  - Relevant to the ISAC/sensing convergence discussed in note 04's future-generation section.
- **[Doc · ★★]** **IEEE 802.11 Working Group timelines and TGbn status pages**
  - The source for ballot and approval dates. Use these rather than secondary reporting when a date matters.

---

## 05 · Cellular IoT — RedCap, eRedCap and NTN

### Papers

- **[Paper · EN · ★★★]** "Resource Management for Reduced Capability New Radio Devices in Beyond 5G Networks: Opportunities and Research Road Map" — N. S. Ferdous, M. Z. Hassan, I. Ahmed, L. Akter · *IEEE Xplore* document 10757145
  - The best single overview of RedCap: what was reduced (bandwidth, MIMO layers, baseband complexity, DL modulation order, RF cost), the three use-case families (industrial sensors, wearables, video surveillance), and the coexistence problem with legacy NR. Covers coverage, capacity and energy-efficiency solutions plus a research roadmap.
- **[Paper · EN · ★★]** "Positioning of RedCap Devices in 5G Networks" — F. Munier, Z. Xiong, R. Shreevastav, X. Jiang, Y. Lyazidi, D. Shrestha, C. Zhang, G. Lindmark, J. Nygren, S. Moloudi, S. Dwivedi, F. Gunnarsson · *IEEE Communications Magazine*, vol. 62, no. 8, pp. 110–116, 2024 · DOI 10.1109/MCOM.001.2300802
  - Ericsson-authored account of the Rel-18 positioning enhancement for RedCap — extending effective bandwidth by frequency hopping — with 3GPP channel-model simulation results. Concrete and recent.
- **[Paper · EN · ★]** "Age of Information: An Introduction and Survey" (see §06)
  - Useful here because RedCap/eRedCap deployment targets are mostly status-update systems, where AoI is the more honest metric than throughput.

### Books

- **[Book · EN/CN · ★★★]** *5G-ADVANCED NR增强标准:下一代无线通信技术(原书第3版)* (see §01)
  - Contains the RedCap and NTN chapters in Chinese, including the NTN air-interface changes: uplink/downlink timing relations and HARQ enhancements.

### Standards

- **[Spec · ★★★]** **3GPP TR 38.865** — Study on further reduced capability NR devices (Rel-18)
  - The study that produced eRedCap. Standardised in **Release 18, frozen June 2024** (RAN#104) — not Rel-19, a correction recorded in note 05.
- **[Spec · ★★★]** **3GPP TR 38.821** — "Solutions for NR to support non-terrestrial networks (NTN)" (Rel-16) · **3GPP TR 38.811** — "Study on New Radio to support non-terrestrial networks" (Rel-15)
  - The NTN foundation: propagation delay, Doppler, moving cells, and the timing/HARQ adaptations required. Read 38.821 first.
- **[Spec · ★★]** **3GPP TS 38.306** — UE radio access capabilities
  - Where RedCap/eRedCap capability signalling and bandwidth reduction are actually defined.
- **[Spec · ★★]** **3GPP TS 38.331** (see §02)
  - Carries the NTN system information and the RedCap access control mechanisms.

---

## 06 · Wireless Sensor Networks and Low-Power MAC

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

## 07 · Embedded Systems, RTOS and Hardware Interfaces

### Books

- **[Book · EN · ★★★]** *Mastering the FreeRTOS Real Time Kernel — A Hands On Tutorial Guide* — Richard Barry · FreeRTOS; release v1.1.0, 19 August 2024 (references FreeRTOS V10.6.2)
  - The official kernel book, freely available with companion source. Covers tasks, scheduling, queues, semaphores and mutexes, direct-to-task notifications, stream and message buffers, memory management, and priority inheritance. Read this alongside the source; the context-switch and tick-handling detail is what separates real RTOS understanding from API familiarity.
- **[Book · EN · ★★]** *Making Embedded Systems: Design Patterns for Great Software*, 2nd ed. — Elecia White · O'Reilly, 2021
  - Practical patterns for resource-constrained firmware: state machines, hardware abstraction, debugging without a debugger, and how to structure code you can actually test on target.
- **[Book · EN · ★★]** *Embedded Systems Architecture: Explore System-Level Design and Advanced Features* — Daniele Lacamera · Packt, 2nd ed. 2021
  - System-level view: boot sequence, linker scripts and memory layout, interrupt and exception handling, RTOS integration, and the build/flash/debug flow. Good for connecting bare-metal mechanics to the Linux view in note 15.
- **[Book · EN · ★★★]** *Hard Real-Time Computing Systems: Predictable Scheduling Algorithms and Applications*, 3rd ed. — Giorgio C. Buttazzo · Springer, 2011
  - The rigorous treatment of schedulability analysis, rate-monotonic and EDF scheduling, priority inversion and aperiodic servers. This is what makes a "hard real-time" claim defensible rather than rhetorical.
- **[Book · EN/CN · ★★]** *Computer Organization and Design RISC-V Edition* (see §12)
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

## 08 · DPDK User Plane and 5G UPF

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

## 09 · Cloud-Edge-End Collaboration and Heterogeneous Computing

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
  - Primary source for the Huawei interconnect discussed in note 09: **《灵衢基础规范 2.0》** (UB Base Specification — architecture, protocol and programming models), **《灵衢固件规范 2.0》** (firmware architecture and interfaces), **《灵衢使能操作系统参考设计 2.0》** (UB OS Component), and **《基于灵衢的超节点参考架构白皮书》** (SuperPoD reference architecture: bus-level interconnect, unified protocol, peer-to-peer coordination, full-resource pooling, large-scale networking, high availability). UB Base Specification 2.1 adds 224/256 Gbit/s rates, reliable rerouting and lower multi-path latency. The 2.0 specifications were opened at HUAWEI CONNECT 2025 on 18 September 2025.
- **[Doc · ★★]** **昇腾 950 NPU 架构白皮书** (Ascend 950 NPU Architecture White Paper)
  - Chip-level detail: on-chip memory bandwidth and capacity, 72× HiLink ports at up to 112 Gbps, the UB2.0 protocol with URMA asynchronous copy and UB Memory global load/store semantics, PCIe GEN5 x16 reuse, and 2×400 Gbps UBoE for carrying UB over Ethernet.
- **[Doc · ★★]** **Ascend CANN documentation** (Huawei heterogeneous compute architecture)
  - Runtime, graph and operator-level interfaces for the NPU software stack.
- **[Doc · ★]** **ODCC (Open Data Center Committee) technical reports**
  - Chinese-industry server and datacentre architecture specifications, useful for the standards-body perspective in note 09.

---

## 10 · LLM Inference Engines and xLLM

### Papers

- **[Paper · EN · ★★★]** "xLLM Technical Report" — xLLM team (JD.com) · arXiv:2510.14686, 2025
  - The primary reference for the framework in note 10: the service–engine decoupled architecture, optimisation for Chinese AI accelerators (Ascend NPU, Cambricon MLU, Moore Threads GPU, Hygon DCU, MetaX MACA, Iluvatar CoreX), and hybrid KV cache management built on Mooncake with intelligent offloading and prefetching. Battle-tested at scale in JD.com's retail business, which is the strongest available evidence for the engineering claims.
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

## 11 · Agent Systems and Edge Orchestration

### Papers

- **[Paper · EN · ★★★]** "gRPC-Routed Agent Framework for Tasking (GRAFT)" · CAIS '26 · DOI 10.1145/3786335.3813216
  - The specific paper behind note 11: sessioned gRPC routing across heterogeneous personal devices, capability-aware task routing in a small-language-model agent mesh. Note that GRAFT is an overloaded acronym — cite the DOI, not the name.
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

## 12 · RISC-V for Communication Infrastructure

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
- **[Paper · EN · ★]** "End-to-End Learning for OFDM: From Neural Receivers to Pilotless Communication" (see §01)
  - Cited by the HeartStream work; explains why an AI-capable baseband cluster is worth building.

---

## 13 · Languages, Toolchain and Performance Engineering

### Books

- **[Book · EN · ★★★]** *Computer Systems: A Programmer's Perspective*, 3rd ed. — Bryant, O'Halloran (see §09)
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

## 14 · WLAN Ecosystem — WFA, EasyMesh and prpl

### Books

- **[Book · EN · ★★★]** *802.11 Wireless Networks: The Definitive Guide*, 2nd ed. — Matthew Gast (see §04)
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

## 15 · Linux Embedded Development — Drivers, Applications and Core Subsystems

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
- **[Book · EN · ★]** *Understanding Linux Network Internals* — Christian Benvenuti · O'Reilly, 2005 (see §08)

### Books — system and application programming

- **[Book · EN · ★★★]** *The Linux Programming Interface* — Michael Kerrisk · No Starch Press, 2010
  - The definitive system-programming reference: processes, threads, IPC, signals, timers, file I/O, memory mapping, and sockets. Over 1500 pages, with every syscall documented against its behaviour. This is the book to own for the IPC and networking sections of note 15.
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
  - The two build-system references that matter. Use the Yocto LTS release names recorded in note 15 when citing versions.
- **[Doc · ★★]** **U-Boot documentation** and **Device Tree Specification** (devicetree.org)
  - Boot chain and hardware description. The DT spec is short; read it once properly.
- **[Doc · ★★]** **cyclictest / rt-tests documentation** and the **PREEMPT_RT wiki**
  - Real-time verification tooling. PREEMPT_RT was merged into mainline in Linux 6.12 for x86, arm64 and RISC-V; 32-bit ARM followed later.

---

## 16 · Primary Standards and Specification Repositories

Cross-cutting sources that back every section above. Bookmark these; they are always more authoritative than secondary writing.

- **3GPP specifications** — `portal.3gpp.org`. Search by TS/TR number or by release. All 3GPP specs are freely downloadable.
  - RAN L1: TS 38.201–38.215 · RAN L2/L3: TS 38.300, 38.321, 38.322, 38.323, 37.324, 38.331 · Core: TS 23.501, 23.502, 23.503 · Interfaces: TS 29.244 (PFCP), TS 29.281 (GTP-U) · Studies: TR 22.870, TR 38.914, TR 38.843, TR 38.865, TR 38.821
- **IEEE 802.11 Working Group** — `www.ieee802.org/11/`. Task group pages (TGbn for Wi-Fi 8), ballot status and amendment timelines.
- **IEEE Xplore / IEEE Standards Association** — normative texts of 802.11-2024, 802.11ax-2021, 802.11be-2024, 802.11bf-2025, 802.15.4-2020, 1905.1a-2014.
- **ITU-R** — Recommendation M.2160 (IMT-2030 framework).
- **O-RAN Alliance** — `o-ran.org/specifications`. WG1 (architecture), WG2 (A1), WG3 (E2/E2SM), WG4 (Open Fronthaul), WG6 (cloudification).
- **O-RAN Software Community (OSC)** — reference implementations and the xApp framework.
- **Wi-Fi Alliance** — `wi-fi.org`. Certification program specifications and EasyMesh.
- **RISC-V International** — `riscv.org/technical/specifications`. ISA manuals, extension specs and profiles.
- **UnifiedBus (灵衢)** — `www.unifiedbus.com`. UB base, firmware, OS and SuperPoD reference architecture documents.
- **DPDK** — `dpdk.org` (Programmer's Guide, API reference, sample applications).
- **FreeRTOS** — `freertos.org` (kernel book, API reference, LTS release notes).
- **The Linux kernel** — `kernel.org` and the in-tree `Documentation/`.
- **Yocto Project** — `docs.yoctoproject.org` · **Buildroot** — `buildroot.org/downloads/manual`.
- **prpl Foundation** — prplOS, prplMesh and prpl LCM open-source projects.
- **Broadband Forum** — TR-069, TR-181, TR-369 (USP).

---

## 17 · Suggested Reading Order

**If you have 4 weeks before an interview:**

| Week | Focus | Reading |
| --- | --- | --- |
| 1 | Anchor the map | Note `00 MOC`; Dahlman *5G NR* chapters 6/13/14; Gast *802.11* chapters on DCF and IFS/NAV |
| 2 | Your primary track | RAN architect: TS 38.321/38.322/38.323 + TR 38.843 · Edge AI: xLLM technical report + Mooncake + PagedAttention · Embedded/Linux: LDD3 (model chapters) + Kerrisk (IPC chapters) · WLAN: 802.11ax tutorial + Wi-Fi 8 tutorial |
| 3 | Future direction | TR 22.870 + "What Should 6G Be?" + "Wi-Fi: Twenty-Five Years and Counting" + HeartStream (ESSERC 2025) |
| 4 | Consolidate | Each note's **Anchors** section; the correction table in `README.md` §7; re-read only what you cannot state from memory |

**Two rules that make this list productive rather than decorative:**

1. **Read the standard, not the summary, for anything you will be asked to quote.** Spec numbers, freeze dates and parameter values are cheap to check and expensive to get wrong.
2. **Pair every systems paper with its implementation.** xLLM/Mooncake, FlashInfer, prplMesh, DPDK and FreeRTOS all ship source. Reading the code is how you discover what the paper left out — usually the part an interviewer asks about.

---

## 18 · Verification and Maintenance

- Every entry above was checked against a publisher page, library catalogue, DOI, arXiv record or the issuing standards body before inclusion.
- Entries are recorded with the identifier that makes them checkable: **ISBN** for books, **DOI** or **arXiv ID** for papers, **specification number** for standards. Where a citation could not be independently confirmed at the time of writing, it is marked **VERIFY** rather than asserted.
- **Chinese-language entries keep their original titles.** The English text following them is a description, not a translation of the title.
- Update triggers: 3GPP TSG plenaries (four per year) for §01/§02/§05; IEEE 802.11 working group and Wi-Fi Alliance announcements for §04/§14; Linux mainline and LTS releases for §13/§15; xLLM, Mooncake and agent-framework releases for §10/§11; RISC-V International ratifications for §12.

---

## Copyright

Copyright (c) 2026 **Washington Ruan**. All rights reserved.

All titles, ISBNs, DOIs and specification numbers are the property of their respective publishers, authors and standards bodies and are reproduced here for reference purposes.

---

© 2026 Washington Ruan. All rights reserved.
