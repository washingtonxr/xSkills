---
title: Reading list — MN · Mobile network
lang: en
category: reading-list
license: GPL-3.0-or-later OR AGPL-3.0-or-later
last-updated: 2026-10-29
---

# Reading list — MN · Mobile network

> 3GPP radio access and the RAN stack: the release map, the NR layer-2 protocol stack, AI/ML for RAN, cellular IoT, random access, the DU scheduler, HARQ, and an open-source implementation.
>
> One section per note, numbered `GG-x`. Where a note needed no source beyond its own
> **References**, there is no section here — the note is self-sufficient.

## How to use this list

- **Marks.** Type and priority marks (`★★★`, `[Book]`, `[EN]`) are defined once, in the MOC under *Reading marks*. The rule that matters: `★★★` means read or skim before you quote the note in an interview.
- **Titles** are kept in their published form and never translated; descriptions are English.
- **Nothing is asserted.** Where a citation could not be confirmed against a publisher, DOI, arXiv record or the issuing body, it is marked `VERIFY`.
- **Not covered here:** `01-3` has no separate section — its sources are cited in the note's own **References**, which is where the RIC specifications and the DRL papers live.

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

---

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

## 01-7 · NR HARQ — Retransmission Flow, Timelines and LTE Comparison
### Standards

- **[Standard · ★★★]** 3GPP. *TS 38.321 — Medium Access Control (MAC) protocol specification*. <https://www.etsi.org/deliver/etsi_TS/138300_138399/138321/>
  - Clause 5.3.2 the DL HARQ entity and process behaviour, 5.4.1 the UL HARQ entity with the configured-grant process-ID formula and `configuredGrantTimer`, 5.7 the DRX retransmission timers. The normative source for every state machine in the note.
- **[Standard · ★★★]** 3GPP. *TS 38.214 — Physical layer procedures for data*, v18.9.0 (ETSI TS 138 214 V18.9.0). <https://www.etsi.org/deliver/etsi_ts/138200_138299/138214/18.09.00_60/ts_138214v180900p.pdf>
  - Clause 5.1 the 16-process maximum, the 32-process capability and the default of 8; 5.1.7.2 CBG reception with CBGTI and CBGFI; 6.1 the UL figure of 16; Tables 5.3-1 and 6.4-1 the N1 and N2 processing times.
- **[Standard · ★★★]** 3GPP. *TS 38.212 — Multiplexing and channel coding*. <https://www.etsi.org/deliver/etsi_TS/138200_138299/138212/>
  - Clause 5.4.2 rate matching: the circular buffer, the RV start index `k0`, and limited buffer rate matching with `Ncb = min(N, Nref)` and `R_LBRM = 2/3`. The arithmetic in §8 of the note comes from here.
- **[Standard · ★★★]** 3GPP. *TS 38.213 — Physical layer procedures for control*. <https://www.etsi.org/deliver/etsi_TS/138200_138299/138213/>
  - Clause 9.1 the HARQ-ACK codebook determination, 9.2.1 PUCCH resource sets, 9.2.3 the PDSCH-to-HARQ-ACK timing and the DCI 1_0 k1 table, 9.2.5 UCI multiplexing onto PUSCH.
- **[Standard · ★★]** 3GPP. *TS 38.331 — Radio Resource Control (RRC) protocol specification*. <https://www.etsi.org/deliver/etsi_TS/138300_138399/138331/>
  - `nrofHARQ-ProcessesForPDSCH` and its `v1700` extension, `dl-DataToUL-ACK`, `pdsch-TimeDomainAllocationList`, `pusch-TimeDomainAllocationList`, `ConfiguredGrantConfig` with `repK` and `repK-RV`, `downlinkHARQ-FeedbackDisabled-r17`, `cellSpecificKoffset-r17`.
- **[Standard · ★★]** 3GPP. *TS 36.321 — E-UTRA; MAC protocol specification*. <https://www.etsi.org/deliver/etsi_TS/136300_136399/136321/>
  - The LTE side: the synchronous uplink HARQ operation, the PHICH-driven non-adaptive retransmission, and `maxHARQ-Tx`. Read it next to TS 38.321 §5.4.1 and the whole comparison becomes obvious.
- **[Standard · ★★]** 3GPP. *TS 36.213 — E-UTRA; Physical layer procedures*. <https://www.etsi.org/deliver/etsi_TS/136300_136399/136213/>
  - The TDD HARQ-ACK timing tables, the PHICH resource mapping from the lowest PRB index and the DMRS cyclic shift, and the maximum number of HARQ processes per UL/DL configuration.
- **[Standard · ★★]** 3GPP. *TS 36.212 — E-UTRA; Multiplexing and channel coding*. <https://www.etsi.org/deliver/etsi_TS/136300_136399/136212/>
  - Clause 5.1.4.1.2: the turbo circular buffer `Kw = 3·K_Pi`, `N_IR` and `N_cb = min(floor(N_IR / C), Kw)`. The direct ancestor of NR's `Ncb`.
- **[Standard · ★]** 3GPP. *TS 36.306 — E-UTRA; UE radio access capabilities*, v14.2.0. <https://www.etsi.org/deliver/etsi_ts/136300_136399/136306/14.02.00_60/ts_136306v140200p.pdf>
  - Table 4.1-1: `N_soft` per UE category — 250,368 for category 1, 1,827,072 for category 4, 35,982,720 for category 8.
- **[Standard · ★]** 3GPP. *TS 38.306 — UE radio access capabilities*. <https://www.etsi.org/deliver/etsi_TS/138300_138399/138306/>
  - The rate expression the NR soft-buffer capability is derived from, and the 16- versus 32-process capability signalling.
- **[Standard · ★]** 3GPP. *TR 38.821 — Solutions for NR to support non-terrestrial networks (NTN)*. <https://www.etsi.org/deliver/etsi_tr/138800_138899/138821/>
  - The delay ladder that motivates 32 processes, `K_offset`, and per-process HARQ feedback disabling.

### Books

- **[Book · ★★★ · EN]** *5G NR: The Next Generation Wireless Access Technology*, 2nd ed. — Erik Dahlman, Stefan Parkvall, Johan Sköld · Academic Press, 2021 · ISBN 978-0-12-822320-8
  - Chapters 13 and 14: retransmission protocols and scheduling. The authors were in the room when the PHICH was deleted, and this is where the reasoning is written down rather than inferred.
- **[Book · ★★★ · EN]** *4G: LTE-Advanced Pro and The Road to 5G*, 3rd ed. — Erik Dahlman, Stefan Parkvall, Johan Sköld · Academic Press, 2016 · ISBN 978-0-12-804575-6
  - The LTE half of the comparison by the same three authors: the synchronous uplink design, the PHICH, the 8 ms round trip and the 1 ms subframe grid that produced it.
- **[Book · ★★ · EN]** *LTE — The UMTS Long Term Evolution: From Theory to Practice*, 2nd ed. — Stefania Sesia, Issam Toufik, Matthew Baker · Wiley, 2011 · ISBN 978-0-470-69716-0
  - Turbo rate matching, the HARQ process model and the TDD HARQ timing tables at a level of detail the specifications assume rather than explain.

### Papers and technical documentation

- **[Doc · ★★★ · EN]** lte5ghub. *HARQ — Downlink and Uplink in 5G NR*. <https://lte5ghub.com/harq>
  - The process-count discussion with the 8-process default, the NDI pipeline, the worked k1 example, the LBRM consequence and the Rel-17 long-round-trip mechanisms, all in one page.
- **[Doc · ★★★ · EN]** lte5ghub. *Scheduling and HARQ timing (n+4) in LTE*. <https://lte5ghub.com/lte-td-allocation>
  - The 8 ms uplink round trip walked around the clock, and an explicit statement of LTE's two HARQ styles versus NR's single one.
- **[Doc · ★★ · EN]** lte5ghub. *PUSCH — Uplink Shared Channel in LTE*. <https://lte5ghub.com/lte-pusch>
  - The PHICH, non-adaptive versus adaptive retransmission, and how UCI is punctured onto PUSCH next to the DMRS.
- **[Doc · ★★ · EN]** ShareTechnote. *5G/NR — Channel Coding: code block group*. <https://www.sharetechnote.com/html/5G/5G_CBG.html>
  - The `PDSCH-CodeBlockGroupTransmission` ASN.1, `maxCodeBlockGroupsPerTransportBlock`, and the roles of CBGTI and CBGFI.
- **[Doc · ★★ · EN]** ShareTechnote. *5G NR LDPC rate matching, TS 38.212 §5.4.2*. <https://www.sharetechnote.com/html/WebProgramming/Websim_LdpcRatematch.html>
  - An interactive simulation of the circular buffer, the `k0` formula and the BG1/BG2 RV offset tables — the fastest way to make §8 of the note concrete.
- **[Doc · ★★ · EN]** 5G/6G Academy. *5G from orbit: NTN engineering and the direct-to-device race*. <https://www.5g6gacademy.com/whitepapers/pdf/wp08-ntn-direct-to-device.pdf>
  - The TR 38.821 delay ladder from 12.89 ms for a regenerative LEO at 600 km to 541.46 ms for a transparent GEO, and what each rung breaks first.
- **[Doc · ★ · EN]** 3GPP. *EP4250626 — Communication in the presence of uplink-downlink configuration change*. <https://data.epo.org/publication-server/>
  - The LTE per-configuration HARQ process tables for both directions, and why an UL/DL reconfiguration is a HARQ event that resizes every soft buffer.
- **[Doc · ★ · EN]** USPTO. *US10911187 — User equipment provision of enhanced capability information for HARQ processing*. <https://uspto.report/patent/grant/10,911,187>
  - Why soft-buffer size is proportional to data rate times HARQ RTT, and why a higher peak rate forces a choice between fewer processes and a lower rate.

---

## 01-8 · 5G NR — OpenAirInterface: the open-source NR stack
### Project, governance and licence

- **[Doc · ★★★ · EN]** Kaltenberger, F., Gosain, A., Ghauri, I., Knopp, R., et al. *Driving Innovation in 6G Wireless Technologies: The OpenAirInterface Approach*. arXiv:2412.13295 (published in *Computer Networks*). <https://arxiv.org/abs/2412.13295>
  - The one document to read first. History and governance, the licence argument, the RAN/CN/OAM asset split, F1/E1/FAPI/7.2/E2/O1 support, the PHY parameter table, the O-RU vendor list, the performance tables, the 11-NF core and FlexRIC's service models and latency, all in one place.
- **[Doc · ★★★ · EN]** OpenAirInterface Software Alliance. *OAI License Model*. <https://openairinterface.org/?page_id=101>
  - The four repositories and their licences, and the FRAND patent clause that distinguishes CSSL from Apache 2.0. Read it before you answer any licensing question about OAI.
- **[Doc · ★★ · EN]** OpenAirInterface Software Alliance. *CSSL — The OAI move to a generic license*, OAI Webinar Series chapter 16. <https://openairinterface.org/?p=1495/>
  - Why OAI Public License v1.1 became CSSL v1.0 with the Duranta launch, in the project's own words.
- **[Doc · ★★ · EN]** Linux Foundation Networking and OpenAirInterface Software Alliance. *LF Networking and OSA collaborate to announce Duranta* (2025-08-27). <https://lfnetworking.org/>
  - The governance change: OAI assets seeded into an LFN incubation project with a governing board, security processes and Nephio integration.
- **[Doc · ★★ · EN]** OpenAirInterface Software Alliance. *OAI 5G RAN Project Group Charter*. <https://www.openairinterface.org/docs/OSA-5G-RAN-Project-Group-Charter.pdf>
  - How the 5G work is funded and steered: the two-year project group started 2020-11-15, its steering committee and its output list.
- **[Doc · ★ · EN]** OpenAirInterface Software Alliance. *Winter Newsletter, January 2022*. <https://openairinterface.org/wp-content/uploads/2025/10/Winter_Newsletter.pdf>
  - The July 2021 launch of the 5G Stand-Alone gNB stack: containerised AMF/UPF/SMF, a bare-metal gNB on two USRP N310s, and a Quectel module as the UE.

### Source code and architecture

- **[Code · ★★★ · EN]** Duranta project. *openairinterface5g*. <https://github.com/duranta-project/openairinterface5g>
  - The repository. Start at `README.md` for the directory map, then `executables/nr-softmodem.c` for startup, `openair2/NR_PHY_INTERFACE/NR_IF_Module.c` for the L1/L2 boundary and `openair2/LAYER2/NR_MAC_gNB/gNB_scheduler.c` for the scheduler. Check `CHANGELOG.md` and the weekly tag before quoting any feature.
- **[Code · ★★★ · EN]** OpenAirInterface. *openairinterface5g tags*. <https://gitlab.eurecom.fr/oai/openairinterface5g/-/tags>
  - Weekly integration tags (`2026.w43` merged 2026-10-23). The per-week merge-request summaries are the best available record of what actually changed, and the only honest answer to "does OAI support X today".
- **[Doc · ★★★ · EN]** OpenAirInterface. *Feature set, build and run documentation* — `doc/FEATURE_SET.md`, `doc/BUILD.md`, `doc/RUNMODEM.md`, `doc/tuning_and_security.md`. <https://openairinterface.org/docs/>
  - The supported parameter table, the `build_oai` invocations, the softmodem command line, and the performance-tuning section: L1 thread cores, thread pool, `L1_num_tx_sym_per_thread`, `max_ldpc_iterations`, `ul_max_mcs`, and the AMD EPYC core-complex caveat.
- **[Doc · ★★★ · EN]** Kaltenberger, F. *OAI Layer 1/2 procedures*, OAI Fall 2019 Workshop, Beijing. <https://www.openairinterface.org/docs/workshop/8_Fall2019Workshop-Beijing/Training/2019-12-03-KALTENBERGER-2.pdf>
  - The thread inventory and timing diagrams: `ru_thread`, `ru_thread_tx`, `fep_thread`, `feptx_thread`, `ru_thread_prach`, `ru_thread_asynch`, `L1_thread_rx`, `L1_thread_tx`, `L1_thread_prach`.
- **[Doc · ★★ · EN]** Thomas, L. *Configuration files and Linux threading in the OAI RAN code*, OAI Webinar Series chapter one. <https://openairinterface.org/wp-content/uploads/2022/01/OAI-webinar-chapter-one.pdf>
  - The notifiedFIFO discipline, the permanent-thread inventory, and the argument against allocation in the hot path.
- **[Doc · ★★★ · EN]** Knopp, R., Kaltenberger, F., et al. *The OpenAirInterface 5G New Radio Implementation: Current Status and Roadmap*. EURECOM. <https://www.eurecom.fr/publication/5822/download/comsys-publi-5822.pdf>
  - The FAPI P5 and P7 figures, and the USRP X310 (184.32 Msps, 80 MHz, 217 PRB) versus N310 (122.88 Msps, 100 MHz, 273 PRB) bandwidth analysis that explains the config-file PRB counts.
- **[Doc · ★★★ · EN]** OpenAirInterface. *VNF/PNF split architecture* (`doc/NR_NFAPI_archi.md`). <https://openairinterface-docs-5b3d70.eurecom.io/projects/OpenAirInterface5G/architecture/NR_NFAPI_archi/>
  - The nFAPI split in detail: `configure_nr_nfapi_vnf()` and `configure_nr_nfapi_pnf()`, the P5 and P7 loops, socket versus WLS versus nvIPC encoding, and how `UL_INFO` is packed and shipped.
- **[Doc · ★★ · EN]** OpenAirInterface. *O-RAN FHI 7.2 tutorial* (`doc/ORAN_FHI7.2_Tutorial.md`). <https://openairinterface.org/docs/>
  - Which functions sit in the O-DU and which in the O-RU, the Intel libxran and DPDK dependency, the M-plane, the PTP LLS-C configuration, and worked kernel command lines.
- **[Doc · ★★ · EN]** OpenAirInterface. *5G NR SA tutorial with OAI nrUE and GPU offload* (`doc/NR_SA_Tutorial_OAI_nrUE_GPU_offload.md`).
  - The UE command line: `--num-dl-actors`, `--num-ul-actors`, `--thread-pool`, `--loader.ldpc.shlibversion`, `--ue-fo-compensation`, plus the DPDK and UHD build prerequisites.
- **[Doc · ★★ · EN]** COSMOS testbed. *Duranta/OAI 5G SA soft-only: gNB + nrUE + OAI CN5G over RFsim*. <https://www.cosmos-lab.org/wiki/public/tutorials/cellular-4g5g-oran/duranta-soft-5g-single-host>
  - A worked single-host rfsim deployment with the core, including the image-to-tag mapping (`duranta-20260907c` built from tag `2026.w36`), the PLMN and UE pool, and the path onward to over-the-air.
- **[Code · ★★ · EN]** OpenAirInterface. *oai-cn5g-fed*. <https://gitlab.eurecom.fr/oai/cn5g/oai-cn5g-fed>
  - The core federation: the NF list, the two UPF variants, UPF-VPP under Apache 2.0, and the deployment tutorials.

### Papers, benchmarks and deployment

- **[Paper · ★★★ · EN]** Kaltenberger, F., et al. *An Open, Programmable, Multi-vendor 5G O-RAN Testbed with NVIDIA ARC and OpenAirInterface*. arXiv:2310.17062. <https://arxiv.org/abs/2310.17062>
  - The FAPI split in a real deployment: L1 as master sending a slot indication every slot, L2 replying with a UL or DL request, O-RAN 7.2 with the S-plane on PTPv2 and sync architecture option 3.
- **[Paper · ★★★ · EN]** Guemdani, M., Gu, P., Phung, C.-D., Secci, S. *Comparative E2E Performance Analysis of O-RAN Designs in a 5G Standalone Testbed*. IEEE HPSR 2025.
  - The independent srsRAN versus OAI comparison: bitrate stability, jitter, packet loss, CPU and disk write, in monolithic and split configurations. Read it before you argue either stack's superiority.
- **[Doc · ★★ · EN]** NgKore Foundation. *ORAN end-to-end commands cheatsheet*.
  - The exact build and run commands for B210, N310, X410 and the `oran_fhlib_5g` target, the `ptp4l`/`phc2sys` invocations per O-RU and NIC pair, and the kernel command line used for a tuned 18-core box.
- **[Doc · ★★ · EN]** NgKore Foundation. *OAI NTN: inside the source code*. <https://docs.ngkorefoundation.org/ntn/oai/oai-ntn/>
  - A code-level walk of `apply_ntn_config()`, SIB19, `nr_mac_configure_sib19()` and `get_NTN_Koffset()`, with the GEO and LEO K2 values. The practical companion to §01-4.
- **[Doc · ★ · EN]** Northeastern University. *Colosseum — massive channel emulator*.
  - The 128 SRN, 128 USRP X310 and 64 FPGA testbed where the soft-UE throughput figures were measured, and the only place to do reproducible large-scale OAI experiments.
- **[Doc · ★ · EN]** Keysight. *RuSIM and CoreSIM*. <https://www.keysight.com/>
  - RU, channel and UE emulation plus core emulation: how the 1.61 Gbps figure and the stress tests were produced.

### Standards and specifications it implements

- **[Standard · ★★★]** 3GPP. *TS 38.211 — Physical channels and modulation*. <https://www.etsi.org/deliver/etsi_TS/138200_138299/138211/>
  - Numerology, frame and slot structure and the physical channels that `openair1/PHY/NR_TRANSPORT` implements. Read it beside the code, not before it.
- **[Standard · ★★★]** 3GPP. *TS 38.212 — Multiplexing and channel coding*. <https://www.etsi.org/deliver/etsi_TS/138200_138299/138212/>
  - LDPC and Polar coding and rate matching — the reference for the decoder whose iteration count is the single most useful OAI tuning knob.
- **[Standard · ★★★]** 3GPP. *TS 38.321 — Medium Access Control (MAC) protocol specification*. <https://www.etsi.org/deliver/etsi_TS/138300_138399/138321/>
  - The normative source for everything in `NR_MAC_gNB`: RACH, HARQ, BSR, LCP and DRX.
- **[Standard · ★★]** 3GPP. *TS 38.401 / TS 38.470 series — NG-RAN architecture and F1*. <https://www.etsi.org/deliver/etsi_TS/138400_138499/>
  - The CU/DU split, F1-C and F1-U, and the E1 interface that decides which OAI task runs in which box.
- **[Standard · ★★]** Small Cell Forum. *FAPI and nFAPI specifications*. <https://www.smallcellforum.org/>
  - The P5 and P7 procedures OAI adopts verbatim as its L1/L2 boundary, in and out of the process.
- **[Standard · ★★]** O-RAN ALLIANCE. *Open Fronthaul Control, User and Synchronization Plane Specification (7.2x)*. <https://www.o-ran.org/specifications>
  - The C-, U- and S-plane definition behind `radio/fhi_72`, including the section types and compression options.
- **[Standard · ★★]** IEEE. *1588-2019 — Precision Time Protocol*. <https://standards.ieee.org/ieee/1588/6211/>
  - The clock O-RAN 7.2 depends on, and the reason a bring-up is ordered PTP, then M-plane, then C/U-plane.
- **[Doc · ★★ · EN]** Intel. *DPDK and the bb-dev (ACC200) acceleration framework*. <https://www.dpdk.org/>
  - The two Intel dependencies in one: the fronthaul data path and the look-aside LDPC path.
- **[Book · ★★★ · EN]** *5G NR: The Next Generation Wireless Access Technology*, 2nd ed. — Erik Dahlman, Stefan Parkvall, Johan Sköld · Academic Press, 2021 · ISBN 978-0-12-822320-8
  - The specification-side reference to keep open next to the source, chapter by chapter.

---

## Standards and repositories

- **3GPP specifications** — `portal.3gpp.org`. Search by TS/TR number or by release. All 3GPP specs are freely downloadable.
  - RAN L1: TS 38.201–38.215 · RAN L2/L3: TS 38.300, 38.321, 38.322, 38.323, 37.324, 38.331 · Core: TS 23.501, 23.502, 23.503 · Interfaces: TS 29.244 (PFCP), TS 29.281 (GTP-U) · Studies: TR 22.870, TR 38.914, TR 38.843, TR 38.865, TR 38.821
- **ITU-R** — Recommendation M.2160 (IMT-2030 framework).
- **O-RAN Alliance** — `o-ran.org/specifications`. WG1 (architecture), WG2 (A1), WG3 (E2/E2SM), WG4 (Open Fronthaul), WG6 (cloudification).
- **O-RAN Software Community (OSC)** — reference implementations and the xApp framework.


---

_Copyright (c) 2026 Washington Ruan and contributors · licensed under **GPL-3.0-or-later** or **AGPL-3.0-or-later**, at your option · see `LICENSE` and `LICENSE-AGPL`._
