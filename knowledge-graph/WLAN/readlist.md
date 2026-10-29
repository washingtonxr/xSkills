---
title: Reading list — WLAN · IEEE 802.11
lang: en
category: reading-list
license: GPL-3.0-or-later OR AGPL-3.0-or-later
last-updated: 2026-10-29
---

# Reading list — WLAN · IEEE 802.11

> IEEE 802.11 from the fundamentals to the silicon: the substrate note that explains what the technology is and where it came from, the generation map, power saving, the certification and Multi-AP ecosystem, the packet datapath, discovery and association, roaming, EasyMesh, scheduling, TSN, baseband and driver architecture, OpenWrt, openwifi, and the reliability/latency/determinism question.
>
> One section per note, numbered `GG-x`. Where a note needed no source beyond its own
> **References**, there is no section here — the note is self-sufficient.

## How to use this list

- **Marks.** Type and priority marks (`★★★`, `[Book]`, `[EN]`) are defined once, in the MOC under *Reading marks*. The rule that matters: `★★★` means read or skim before you quote the note in an interview.
- **Titles** are kept in their published form and never translated; descriptions are English.
- **Nothing is asserted.** Where a citation could not be confirmed against a publisher, DOI, arXiv record or the issuing body, it is marked `VERIFY`.
- **Start here:** if you are new to 802.11, read `02-14` first and use its two source books as the spine; the remaining sections assume the vocabulary it defines.
- **Not covered here:** `02-4` has no separate section — its sources (the mac80211 code paths and the vendor offload documentation) are cited in the note's own **References**.

---

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

---

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

---

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

## 02-9 · WLAN — Time-Sensitive Networking over Wi-Fi: Research and Practice Across Generations
### Standards and specifications

- **[Standard · ★★★ · EN]** IEEE. *IEEE Std 802.11be-2024 — Amendment 2: Enhancements for Extremely High Throughput (EHT)*, published 22 July 2025 · DOI 10.1109/IEEESTD.2024.11090080 · free via the IEEE GET program
  - The TSN generation itself: SCS with the QoS Characteristics element, restricted TWT, MLO and TID-to-link mapping. Read alongside the 802.11→802.1 liaison below, which explains the intent.
- **[Standard · ★★★ · EN]** IEEE. *IEEE Std 802.11ax-2021 — Amendment 1: Enhancements for High Efficiency WLAN*, published 19 May 2021
  - OFDMA, trigger-based uplink access and TWT. Every granted-access mechanism in the note is built on these three.
- **[Standard · ★★★ · EN]** IEEE. *IEEE Std 802.11ak-2018 — Amendment 4: Enhancements for Transit Links Within Bridged Networks*
  - The amendment that lets a Wi-Fi link be a transit link inside an IEEE 802.1Q bridged network. Without it there is no "802.1Qbv reaches a wireless segment" answer.
- **[Standard · ★★★ · EN]** IEEE. *IEEE Std 802.11aa-2012 — Amendment 2: MAC Enhancements for Robust Audio Video Streaming*
  - SCS, intra-access-category queues, the Drop Eligibility Indicator, OBSS management and GCR. Where the vocabulary of wireless TSN was established eight years before r-TWT.
- **[Standard · ★★★ · EN]** IEEE. *IEEE Std 802.11-2024* (maintenance revision), published 28 April 2025
  - The consolidated base document, including the FTM procedure from 802.11mc that 802.1AS-2020 relies on.
- **[Standard · ★★★ · EN]** IEEE. *IEEE Std 802.1AS-2020 / 802.1AS-2025 — Timing and Synchronization for Time-Sensitive Applications*
  - gPTP, and the specification of FTM as the 802.11 time-transfer method. The clause that decides whether your synchronisation budget is spent before scheduling begins.
- **[Standard · ★★ · EN]** IEEE. *IEEE Std 802.1Qbv-2015 — Amendment 25: Enhancements for Scheduled Traffic*
  - The time-aware shaper and the gate control list: the wired mechanism that r-TWT service periods have to be aligned with.
- **[Standard · ★★ · EN]** IEEE. *IEEE Std 802.1CB-2017 — Frame Replication and Elimination for Reliability*
  - The redundancy mechanism that MLO is asked to emulate, and the reason emulation is weaker than disjoint paths.
- **[Standard · ★★ · EN]** IEEE. *IEEE Std 802.1Qci-2017* (per-stream filtering and policing), *802.1Qcc-2018* (SRP enhancements and centralised configuration), *802.1Qbu-2016* with *802.3br-2016* (frame preemption), *802.1Qch-2017* (cyclic queueing), *802.1Qcr-2020* (asynchronous traffic shaping)
  - The rest of the toolbox, each with a different answer to "what happens to this over the air". Preemption is the one whose absence from Wi-Fi is most keenly felt.
- **[Standard · ★★ · EN]** IEC/IEEE. *IEC/IEEE 60802 — Time-Sensitive Networking Profile for Industrial Automation*, published 29 June 2026 · <https://1.ieee802.org/tsn/iec-ieee-60802/>
  - The profile: which features, defaults and configuration a converged industrial network must implement, including the 0.1–1 µs synchronisation allowance.
- **[Standard · ★ · EN]** IEEE. *IEEE Std 802.1DG-2025 — TSN Profile for Automotive In-Vehicle Ethernet*, published 6 June 2025
  - The automotive counterpart; the best worked example of how a profile narrows a toolbox into something purchasable.
- **[Standard · ★★ · EN]** 3GPP. *TS 23.501 — System Architecture for the 5G System*, §5.28 (TSN integration) and §5.29 (5G LAN)
  - The cellular answer to the same question: DS-TT, NW-TT, TSN-AF, and `dependentDelayMin`/`dependentDelayMax`. The sharpest contrast with the Wi-Fi approach, which has no equivalent normative quantity.

### Papers and technical documentation

- **[Doc · ★★★ · EN]** IEEE 802.11 Working Group. *Liaison communication to IEEE 802.1 regarding TSN support*, 20 December 2022
  - The working group's own three-row mapping of the 802.1 toolbox onto 802.11be, plus the SCS/QoS Characteristics and r-TWT descriptions. The single best primary source for this topic.
- **[Doc · ★★★ · EN]** Cavalcanti, D., and Venkatesan, G. *802.1 TSN over 802.11, with updates from developments in 802.11be*, IEEE 802.1 Plenary, November 2020
  - The architecture of a wireless TSN domain, the 802.1AC GLK convergence function, and the honest list of which TSN features already operate over 802.11.
- **[Paper · ★★★ · EN]** Adame, T., Carrascosa-Zamacois, M., and Bellalta, B. *Time-Sensitive Networking in IEEE 802.11be: On the Way to Low-Latency WiFi 7*, Sensors 21(15):4954, 2021 · DOI 10.3390/s21154954 · open access
  - The reference survey: every 802.1 tool mapped onto 802.11be, and the multimedia, healthcare, industrial and transport use cases with their numbers.
- **[Paper · ★★★ · EN]** Haxhibeqiri, J., Jiao, X., Shen, X., Pan, C., Jiang, X., Hoebeke, J., and Moerman, I. *Coordinated SR and Restricted TWT for Time Sensitive Applications in WiFi 7 Networks*, IEEE Communications Magazine 62(8):118–124, 2024 · DOI 10.1109/MCOM.001.2300431
  - A real implementation of coordinated SR and r-TWT on the openwifi SDR platform. Read it for the overheads, which simulations never show.
- **[Paper · ★★★ · EN]** Mozaffariahrar, E., Wilhelmi, F., Galati-Giordano, L., Imputato, P., Menth, M., and Avallone, S. *R-TWT in Wi-Fi 7 and Beyond: Enabling Bounded Latency, Energy Efficiency, and Reliability*, IEEE ETFA 2025 · DOI 10.1109/ETFA65518.2025.11205686
  - The ns-3 evaluation of r-TWT against PSM and DCF, and the methodological caveat that matters: restricted access is mimicked with individual TWT.
- **[Paper · ★★★ · EN]** Karamyshev, A., Levitsky, I., Bankov, D., and Khorov, E. *A Tutorial on Wi-Fi 8: The Journey to Ultra High Reliability*, Problems of Information Transmission 61(2):164–210, 2025 · DOI 10.1134/S003294602502005X
  - Feature by feature on 802.11bn: DRU, UEQM, P-EDCA, NPCA, preemption, roaming and multi-AP coordination.
- **[Paper · ★★ · EN]** Wilhelmi, F., Bellalta, B., Geraci, G., et al. *A Tutorial on IEEE 802.11bn Multi-AP Coordination for Wi-Fi 8*, arXiv:2606.13759
  - Co-TDMA, Co-SR, Co-BF and Co-RTWT, with the Kom8ndor open-source simulator. The evidence for the "multi-AP coordination is where the remaining uncertainty lives" claim.
- **[Paper · ★★ · EN]** Nurchis, M., and Bellalta, B. *Target Wake Time: Scheduled Access in IEEE 802.11ax WLANs*, IEEE Wireless Communications 26(2), 2019
  - The service period as a scheduling primitive rather than a sleep mechanism — the origin of everything r-TWT does.
- **[Paper · ★★ · EN]** Khorov, E., Kiryanov, A., Lyakhov, A., and Bianchi, G. *A Tutorial on IEEE 802.11ax High Efficiency WLANs*, IEEE Communications Surveys & Tutorials 21(1):197–216, 2019
  - The Wi-Fi 6 PHY and MAC reset in detail. Where to go when the trigger frame in §6 needs its full derivation.
- **[Paper · ★★ · EN]** Aslam, M. et al. *Hardware Efficient Clock Synchronization Across Wi-Fi and Ethernet Based Network Using PTP*, IEEE Transactions on Industrial Informatics, 2021
  - The hardware-timestamping argument with measurements. Read it before promising a synchronisation budget to anyone.
- **[Doc · ★★ · EN]** IEEE 802.11 Real Time Applications Topic Interest Group. *RTA TIG Report*, doc. 11-18/2009-06, 2019
  - Where the requirement set for real-time applications over 802.11 was first written down inside the working group.
- **[Doc · ★★ · EN]** IETF RAW. *Reliable and Available Wireless Technologies*, draft-ietf-raw-technologies
  - An unusually accurate cross-technology summary of what each 802.11 revision contributes to TSN, and of the trade-offs any wireless extension of TSN has to accept.
- **[Doc · ★★ · EN]** Wi-Fi Alliance. *Wi-Fi CERTIFIED QoS Management*, announced 23 February 2021, extended 21 October 2021
  - SCS, MSCS, DSCP mapping and DSCP Policy: what is actually certified, which is the only reliable guide to what actually ships.
- **[Doc · ★ · EN]** Jiao, X. et al. *openwifi: A Free and Open-Source IEEE 802.11 SDR Implementation on SoC*, IEEE VTC, 2020
  - The platform on which r-TWT and coordinated SR have been implemented and measured.
- **[Doc · ★ · EN]** Samsung Research — Ha, T., Shafin, R., and Manasi. *IEEE 802.11bn (Ultra-High Reliability, Wi-Fi 8)*
  - An engineering walkthrough from a TGbn contributor: DS-CTS and P-EDCA, LLI, NPCA, ELR and DRU, plus the certification timeline.
- **[Doc · ★ · EN]** MaxLinear. *Quality of Service (QoS) Mechanisms in Wi-Fi*, white paper, 2024
  - A readable secondary account of the amendment-by-amendment QoS story from 802.11e to 802.11be. Use it for orientation, verify every claim against the amendment.


### The converged network — when both the client and the AP are TSN-aware

- **[Doc · ★★★ · EN]** Garner, G. *The Transport and Impact of Synchronization in Time-Sensitive Networking: An Introduction to IEEE 802.1AS*. IEEE 802 Foundational Technologies webinar, February 2022. <https://www.ieee802.org/1/files/public/docs2022/webinar-garner-synchronization-0222.pdf>
  - The starting point for the clock half of section 11: the media-independent and media-dependent layer split, which media have native timing mechanisms, the meanLinkDelay and neighborRateRatio formulas, and how the correction field and the accumulated rate ratio are built hop by hop.
- **[Doc · ★★★ · EN]** IEEE 802.1. *Draft blog post for IEEE Std 802.1AS-2020*, July 2020. <https://www.ieee802.org/1/files/public/docs2020/as-draft-blog-post-0720-v01.pdf>
  - What 802.1AS-2020 adds over 2011 in the working group's own words: FTM transport over 802.11, multiple domains, detection of non-compliant devices, and the Common Mean Link Delay Service. Read it before you argue about clocks over Wi-Fi.
- **[Doc · ★★ · EN]** IEEE 802.1 Time-Sensitive Networking Task Group. *TSN summary*, July 2025. <https://ieee802.org/1/files/public/docs2025/admin-tsn-summary-0725-v01.pdf>
  - The one-page map of the toolbox, the profiles and the recent amendments: 802.1ASdn-2024, 802.1ASdm-2024, 802.1ASed-2026, 802.1Qdj-2024, 802.1Qdx-2024, 802.1DG-2025, 802.1DP-2025. Use it to keep your dates honest.
- **[Standard · ★★★ · EN]** IEC/IEEE. *IEC/IEEE 60802:2026 — Time-Sensitive Networking Profile for Industrial Automation*. Edition 1.0, published 29 June 2026, ISBN 9782832712870. <https://webstore.iec.ch/en/publication/60188>
  - The profile a wireless segment has to plug into: conformance classes ccA and ccB, the seven traffic types, multiple gPTP domains with a working clock and a global time, the Annex C clock control model and the Annex D synchronisation error budget. Check its annexes before claiming it covers wireless.
- **[Doc · ★★★ · EN]** Broadcom. *802.11 QoS Queue Architecture and Possible 802.1bz Bridge Model*. IEEE 802.11 contribution 11-13-0221-01-00ak, March 2013. <https://mentor.ieee.org/802.11/dcn/13/11-13-0221-01-00ak-802-11-qos-queue-architecture-and-possible-802-1bz-bridge-model.pptx>
  - Where the 802.11 Portal argument comes from, and the side-by-side table showing that 802.1Q traffic classes and 802.11 access categories are different mappings of the same eight priorities. Also the origin of the alternate voice and video queues.
- **[Doc · ★★★ · EN]** IETF. Szigeti, T., Baker, F., Mohapatra, P., and McCann, J. *Mapping Diffserv to IEEE 802.11*, RFC 8325, February 2018. <https://www.rfc-editor.org/rfc/rfc8325>
  - The UP-to-AC table reproduced from IEEE 802.11-2016 Table 10-1, the AIFS table, the statement that the mapping is non-configurable, and the Diffserv-to-UP mapping a converged network should actually use.
- **[Code · ★★★ · EN]** Linux. *net/mac80211/wme.c*. <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/net/mac80211/wme.c>
  - `ieee802_1d_to_ac`, `ieee80211_select_queue()`, `wme_downgrade_ac()` and the admission-control downgrade walk. The only place the client-side behaviour is unambiguous.
- **[Paper · ★★★ · EN]** Høiland-Jørgensen, T., Kazior, M., Täht, D., Hurtig, P., and Brunstrom, A. *Bufferbloat mitigation in the WiFi stack — status and next steps*, Netdev 2.2. <https://www.netdevconf.info/2.2/papers/jorgensen-wifistack-talk.pdf>
  - The source of the asymmetry: mac80211 disables the qdisc layer entirely on WiFi interfaces, because a generic qdisc cannot split a flow into the per-TID aggregates 802.11 aggregation requires. This is why `taprio` and `etf` are Ethernet tools.
- **[Doc · ★★ · EN]** iproute2 and Linux man-pages. *tc-etf(8)*, *tc-taprio(8)*, and `SO_TXTIME` / `SCM_TXTIME` in *socket(7)*. <https://man7.org/linux/man-pages/man8/ETF.8.html>
  - The wired end-station launch-time machinery, documented precisely, so that the contrast with a Wi-Fi client is exact rather than rhetorical.
- **[Thesis · ★★★ · EN]** Wu, P. *Time Synchronization Protocols for Industrial Use Cases: A Performance Review of NTP and PTP and a Wireless-aware Enhancement*. KTH Royal Institute of Technology, 29 October 2024, DiVA diva2:1942067. <https://www.diva-portal.org/smash/get/diva2:1942067/FULLTEXT01.pdf>
  - The survey behind the measured table: LinuxPTP over Wi-Fi, ath9k software versus TSF hardware timestamping, outlier filtering, Kalman-filtered control loops, openwifi, and the finding that in infrastructure mode most error comes from delay variation inside the AP.
- **[Paper · ★★ · EN]** *Extending Reference Broadcast Infrastructure Synchronization Protocol in IEEE 802.11 as Enabler for the Industrial Internet of Things*. arXiv:2106.03732. <https://arxiv.org/html/2106.03732v1>
  - The three-way measurement: wireline gPTP median 52 ns and max 254 ns, plain IEEE 1588 over the air median about 0.95 ms with outliers to several ms, and RBIS at median 13 us and max below 40 us on commodity hardware.
- **[Paper · ★★ · EN]** *Integration of IEEE 802.1AS-based Time Synchronization in IEEE 802.11 as an Enabler for Novel Industrial Use Cases*. arXiv:2101.02434. <https://arxiv.org/pdf/2101.02434>
  - A worked 802.11-plus-802.1AS integration with a TSN evaluation kit as grandmaster and linuxptp: about plus or minus 350 ns at a 31.25 ms sync interval, against the contrast of carrying PTP directly over the air.
- **[Paper · ★★ · EN]** *Practical IEEE 802.1AS-Based TSN Time Synchronization over Wi-Fi for Bare-Metal Devices*. Project WiWiOPT, BMWK grant KK5189604MS1. <https://dtic.dimensions.ai/details/publication/pub.1186205720>
  - Bare-metal gPTP supporting both Ethernet and 802.11 links on low-cost embedded hardware, below 10 us without additional components. Proof that the client side does not have to be exotic.
- **[Doc · ★ · EN]** Espressif Systems. *Wi-Fi FTM: carry and retrieve Vendor Specific IE in FTM frames*, issue IDFGH-17768. <https://github.com/espressif/esp-idf/issues/18689>
  - An implementer's working reading of 802.1AS-2020 over 802.11: the media-dependent sync is the FTM exchange, the FollowUpInformation rides inside it as a Vendor Specific element, and putting it in a beacon instead makes the origin timestamp stale by the beacon marshal-to-transmit latency. Read as implementation evidence, not as the standard.
- **[Doc · ★★ · EN]** Wi-Fi Alliance. *Wi-Fi Alliance extends Wi-Fi CERTIFIED 7 to 20 MHz-only devices*, 6 January 2026. <https://www.wi-fi.org/news-events/newsroom/wi-fi-alliance-extends-wi-fi-certified-7-20-mhz-only-devices>
  - The ecosystem evidence for the trend, and the caveat: the certified feature list is MLO, DL/UL MU-MIMO and Multi-RUs, not r-TWT, SCS or MSCS.

---

## 02-10 · WLAN — Baseband and Driver Architecture for Wi-Fi 6, 7 and 8
### Vendor documentation — primary, and unusually good

- **[Doc · ★★★ · EN]** Qualcomm Technologies. *Wi-Fi software architecture: ath11k driver software architecture*, document 80-80021-14. <https://docs.qualcomm.com/doc/80-80021-14/topic/wlan_sw_overview.html>
  - The vendor's own decomposition of the driver and the firmware: the MAC interface, control path, data path, the WMI/HTT/HAL host-firmware interface, bus abstraction, PCIe, and the copy engine as "a hardware pipe, standard ring interface based communication channel". Then the Q6 firmware's contents, including the named performance-algorithm block with the transmit scheduler, MU scheduler, MU grouping, RU allocator and airtime fairness. Start here.
- **[Doc · ★★★ · EN]** Qualcomm Technologies. *Networking Pro 1620 Platform product brief*, 87-PW325-1. <https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/documents/Networking-Pro-1620-product-brief_87-PW325-1.pdf>
  - 33 Gbps, quad-band 16-stream, 320 MHz, 240 MHz for 6-GHz-less regions, 4K QAM, 2000 clients, 37-user OFDMA per channel, 4-user MU-MIMO per channel, AFC, and the IPQ9574 ordering part. The numbers to quote when someone asks what a Wi-Fi 7 platform claims.
- **[Doc · ★★★ · EN]** Qualcomm Technologies. *Qualcomm FastConnect 7900 Mobile Connectivity System product brief*, 87-73970-1. <https://docs.qualcomm.com/bundle/publicresource/87-73970-1_REV_B_Qualcomm_FastConnect_7900_Mobile_Connectivity_System_Product_Brief.pdf>
  - 6 nm single-chip 2x2, 5.8 Gbps with 4K QAM on 320 MHz, 4.3 Gbps on 240 MHz of 5 GHz, High Band Simultaneous, and the "AI-optimized" framing that became explicit in the next generation.
- **[Doc · ★★★ · EN]** Qualcomm Technologies. *"Qualcomm Debuts AI-Native Wi-Fi 8 Portfolio"*, press release, MWC Barcelona, 2 March 2026. <https://www.qualcomm.com/news/releases/2026/03/qualcomm-debuts-ai-native-wifi-8-portfolio-unifying-client-and-n>
  - FastConnect 8800 (first 4x4 mobile Wi-Fi radio, beyond 10 Gbps, 2x performance, 3x gigabit range, Bluetooth HDT at 7.5 Mbps, Wi-Fi 8 plus Bluetooth 7.0 plus UWB 802.15.4ab plus Thread 1.5) and the five Dragonwing platforms, including NPro A8 Elite with a 5x5 radio, 2.5x latency reduction and an integrated Hexagon NPU.
- **[Doc · ★★ · EN]** Qualcomm Technologies. *"Wi-Fi 8 under the hood: The technologies powering ultra-high reliability"*, OnQ, November 2025. <https://www.qualcomm.com/news/onq/2025/11/wi-fi-8-technologies-powering-ultra-high-reliability>
  - A vendor engineering account of the PHY changes: longer LDPC block lengths, UEQM, new MCS levels, ELR, DRU. Read it next to the MaxLinear white paper for the numbers.
- **[Doc · ★★ · EN]** MaxLinear. *Wi-Fi 8 for Broadband Service Providers*. <https://www.maxlinear.com/document?id=23470>
  - The most concrete secondary source on the Wi-Fi 8 PHY: 2x LDPC at 3888 bits with 0.5-1 dB measured gain, the new MCS entries, UEQM for two to four streams with LDPC only, and the full DRU definition including sizes, distribution bandwidth, uplink-only operation and the two-stream limit.

### Kernel mailing lists and driver documentation — where the truth lives

- **[Code · ★★★ · EN]** Valo, K. *"ath11k: driver for Qualcomm IEEE 802.11ax devices"*, LWN, 2019. <https://lwn.net/Articles/796850>
  - Why ath11k was a clean start, that its datapath is completely different from ath10k's, that it supports multiple MACs called "soc", and that there is only one WMI interface.
- **[Code · ★★★ · EN]** WikiDevi. *ath11k — supported devices*. <https://wikidevi.wive-ng.ru/Ath11k>
  - Which kernel version each chipset first appeared in: IPQ8074 in v5.6, IPQ6018 and QCA6390 in v5.10, QCN9074 in v5.14, WCN6855, QCA6698AQ and QCA2066 in v5.17.
- **[Code · ★★★ · EN]** LibrePhone. *The ath11k Driver*. <https://librephone.fsf.org/site/ath11k/>
  - The layer stack from HDD and WMA down through WMI, HTT, HTC, HIF and CE to SNOC/AHB or PCIe, and the three mandatory HTT initialisation messages.
- **[Code · ★★★ · EN]** *Qualcomm-Atheros-Ath12k-documentation*, Chapter 4: TX Path in ath12k. <https://github.com/shibinkr/Qualcomm-Atheros-Ath12k-documentation>
  - Descriptor allocation, DMA mapping, pushing to the TCL SRNG, head and tail pointers and the doorbell. The clearest walkthrough of the transmit hot path.
- **[Code · ★★★ · EN]** Bairaktaris, J. *"wifi: ath11k: airtime queue limits, fairness and a driver TXQ scheduler"*, LWN, 2026. <https://lwn.net/Articles/1090342> and <https://lwn.net/Articles/1093204>
  - The single best measurement in this whole subject: AQL and airtime fairness inert on ath11k, throughput against latency at several limit settings, two-station fairness, and the 1.85 ratio between the host's charge and the radio's own measurement.
- **[Code · ★★★ · EN]** Bairaktaris, J. *"fix SoC reboot on firmware crash on AHB"*, LKML, July 2026. <https://lkml.iu.edu/hypermail/linux/kernel/2608.0/08477.html>
  - The IPQ8074 assert-reboots-the-SoC bug, why only the debugfs `assert` trigger reproduces it, and the before-and-after recovery counts. Read it for the method as much as the fix.
- **[Code · ★★ · EN]** Gong, W. *"ath11k: add feature for device recovery"*, LKML, October 2021. <https://lore.kernel.org/linux-wireless/20211015035459.14190-1-wgong@codeaurora.org/t/>
  - Why PCIe parts need their own recovery logic absent remoteproc, the `MHI_CB_EE_RDDM` event, and the reset path through host-interface power down and up.
- **[Code · ★★ · EN]** Zhu, H. *"wifi: ath12k: enable threaded NAPI when DP IRQ affinity is unavailable"*, LKML, 2026. <https://lkml.iu.edu/2605.2/04437.html>
  - The 802 Mbit/s to 2.58 Gbps measurement, and the runtime test that decides the policy.
- **[Code · ★★ · EN]** Kolli, A., and Valo, K. *"ath11k: add firmware-2.bin support"*, LKML, January 2023. <https://patchwork.kernel.org/project/linux-wireless/patch/20230111092547.21425-4-kvalo@kernel.org/>
  - Firmware API 2, the IE container format, and how the MHI layer is handed the amss image by pointer.
- **[Code · ★★ · EN]** Pubbisetty, M. *"ath11k: Add QMI changes for WCN6750"*, ath11k list, January 2022. <https://lists.infradead.org/pipermail/ath11k/2022-January/002590.html>
  - The QMI message sequence, the fixed 12 MB MSA region, and the M3 image bundled into the Q6 image.
- **[Code · ★★ · EN]** Pan, M. *"wifi: ath11k: support usecase-specific firmware overrides"*, LKML, May 2025. <https://patchwork.ozlabs.org/project/devicetree-bindings/cover/20250522013444.1301330-1-miaoqing.pan@oss.qualcomm.com>
  - The `firmware-name` device-tree property and the WCN6855 default-versus-`nfa765` firmware split.
- **[Code · ★★ · EN]** Bhagat, R. K. *"wifi: ath12k: add Ath12k AHB driver support for IPQ5332"*, LWN, 2025. <https://lwn.net/Articles/1015075>
  - IPQ5332 as an 802.11be 2.4 GHz 2x2 device, the separate CE register space, fixed QMI firmware memory, and WCSS secure PIL userPD handling.
- **[Code · ★★ · EN]** Sriram, R., Sundaram, R., and Valo, K. *"wifi: ath12k: ath12k_mac_op_tx(): MLO support"*, LKML, November 2024. <https://lore.kernel.org/all/20241126171139.2350704-3-kvalo@kernel.org/>
  - The transmit link id, per-link address translation, and the rule that 802.3 frames are enqueued on the primary association link with firmware doing link selection.
- **[Code · ★★ · EN]** Mahalingam, B. *"wifi: ath12k: Add support for MLO Multicast handling in driver"*, LKML, January 2025. <https://lore.kernel.org/all/20250109184932.1593157-3-quic_bmahalin@quicinc.com/>
  - IEEE 802.11be-2024 section 10.3.2.14.2, the same sequence number on every link, the vdev id plus 128 trick, and the multicast global sequence number in HTT metadata.
- **[Code · ★★ · EN]** Sahu, A. *"wifi: ath12k: report proper tx completion status to mac80211"*, LKML, 2025. <https://lore.kernel.org/ath12k/20250505221419.2672473-315-sashal@kernel.org/T/>
  - WMI MLO setup, ready and teardown for a single split-phy device, and the firmware assert that follows when they are not sent.
- **[Code · ★ · EN]** Huang, C. *"ath11k: supports one MSI vector"*, LKML, December 2020. <https://patchwork.kernel.org/project/linux-wireless/patch/20201223030225.2345-6-cjhuang@codeaurora.org/>
  - The single-MSI fallback and the copy-engine interrupt handling.
- **[Code · ★ · EN]** LKDDb. *CONFIG_ATH12K_AHB*. <https://cateee.net/lkddb/web-lkddb/ATH12K_AHB.html>
  - Device-tree compatibles and kernel versions for ath12k AHB, including IPQ5332 and IPQ5424.

### Papers and secondary analysis

- **[Paper · ★★★ · EN]** Karamyshev, A., Levitsky, I., Bankov, D., and Khorov, E. "A Tutorial on Wi-Fi 8: The Journey to Ultra High Reliability." *Problems of Information Transmission* 61(2):164-210, 2025. DOI 10.1134/S003294602502005X.
  - DRUs, interference-mitigation pilots, UEQM, the doubled LDPC codeword, ELR with data quadruplication, and the full MAC candidate list: P-EDCA, NPCA, preemption, DSO, DBE, unavailability reporting and QoS signalling.
- **[Doc · ★★ · EN]** *OpenWrt NSS acceleration and optimisations* — generated documentation. <https://deepwiki.com/LiBwrt/openwrt-6.x/5.3-nss-acceleration-and-optimizations>
  - The NSS driver, ECM, the WiFi offload module, and the accelerated-path-versus-standard-path packet flow.
- **[Code · ★★ · EN]** *nss-packages: Qualcomm NSS offload packages for the OpenWrt qualcommax EDMA stack*. <https://github.com/juliusbairaktaris/nss-packages>
  - The component list: `qca-nss-drv`, `qca-nss-ecm`, `qca-mcs`, PPPoE, bridge and VLAN managers, NSS SQM, and the NSS firmware package.
- **[Doc · ★★ · EN]** *OpenWrt firmware_qca-wireless: ATH11K platform support* — generated documentation. <https://deepwiki.com/openwrt/firmware_qca-wireless/3-ath11k-platform-support-(wi-fi-66e)>
  - Board-data file naming, the QMI hardware-detection and BDF-matching sequence, and the exact-match rule for the `variant` string.
- **[Doc · ★★ · EN]** OpenWrt Forum. *"MX4200v2 / IPQ8074: continuous reboot loop caused by ath11k firmware crash"*. <https://forum.openwrt.org/t/mx4200v2-ipq8074-continuous-reboot-loop-caused-by-ath11k-firmware-crash-with-two-ssids-on-one-2-4ghz-radio/252958>
  - A firmware assert taking a whole board down, with the assertion line, the two conditions that trigger it, and a method for isolating which. The best available case study of a firmware failure diagnosed from Linux.
- **[Doc · ★ · EN]** Aerlync. *The ath12k Unified Driver Model*. <https://www.aerlync.com/Company/Blogs/ath12k>
  - A secondary write-up of the two-module split, the `wifi7/` directory and the per-commit change statistics. Useful for the direction; **verify the numbers against the mailing list**.
- **[Doc · ★ · EN]** Gunbark security research. *ath11k driver audit notes*. <https://gunbark.dev/content/51b398b0-9cf2-4075-b5ed-54d48a2a5ce7>
  - The trust-boundary argument: coherent DMA rings the device writes, an IOMMU that bounds where but not when, and descriptor fields derived from over-the-air frames.

---

## 02-11 · WLAN — OpenWrt and the Software Architecture of a Wireless System
### The project itself — release, support and the reference hardware

- **[Doc · ★★★ · EN]** OpenWrt Project. *Welcome to the OpenWrt Project*. <https://openwrt.org/>
  - The current stable series and its latest service release with the kernel they ship, the old stable series and its end-of-life date, and the OpenWrt One announcement with its specification. The page to check before quoting any version.
- **[Doc · ★★★ · EN]** OpenWrt Project. *OpenWrt version history*. <https://openwrt.org/about/history>
  - Per-series kernel versions and dates, and the three 25.12 highlights that actually change the architecture: apk replacing opkg, attended sysupgrade enabled by default, and the Wi-Fi handling scripts rewritten in ucode.
- **[Doc · ★★ · EN]** OpenWrt Project. *OpenWrt 25.12*. <https://openwrt.org/releases/25.12/start>
  - The release and service-release list for the current stable series.
- **[Doc · ★★ · EN]** OpenWrt Project. *Security — support status*. <https://openwrt.org/docs/guide-developer/security>
  - Supported, security-maintenance and end-of-life dates per series, and the rule that only the latest minor release of a series is supported.
- **[Doc · ★★★ · EN]** OpenWrt Project. *OpenWrt One*. <https://openwrt.org/toh/openwrt/one>
  - MT7981BA, MT7976CN, 1 GB DDR4, 256 MiB NAND plus 16 MiB NOR for recovery, the 2.5 GbE and 1 GbE ports, M.2 NVMe, and the project's own guidance on packet steering, hardware flow offload and WED — including the warning that WED bypasses AQL.

### netifd, ubus and the wireless pipeline

- **[Code · ★★★ · EN]** OpenWrt Project. *netifd DESIGN*. <https://git.openwrt.org/?p=project/netifd.git;a=blob;f=DESIGN;hb=HEAD>
  - The source of section 7: devices and their refcounting, the seven device events, interfaces with `active`, `autostart` and the four `IFS_*` states, and the protocol-handler contract that must never block.
- **[Code · ★★★ · EN]** Golle, D., Crispin, J., and Wich, J.-P. *"How to trigger wifi reload from wifi.lua"*, openwrt-devel, October 2019. <https://lists.openwrt.org/pipermail/openwrt-devel/2019-October/025251.html>
  - The change that made hostapd and wpa_supplicant permanent ubus servers so that netifd can add, remove and modify interfaces at runtime. Read this before you answer "how does a wireless config change get applied".
- **[Doc · ★★★ · EN]** OpenWrt Project. *hostapd package README: UBUS methods*. <https://github.com/openwrt/openwrt/tree/master/package/network/services/hostapd>
  - `bss_mgmt_enable`, `bss_transition_request`, `config_add`, `config_remove`, `del_client`, `get_clients`, `get_features` and `get_status`, with argument tables and worked `ubus call` examples.
- **[Doc · ★★ · EN]** OpenWrt Project. *uci_wireless.txt*. <https://git.openwrt.org/?p=web.git;a=blob;f=docs/uci_wireless.txt;hb=HEAD>
  - The `wifi-device` and `wifi-iface` option reference.
- **[Doc · ★★ · EN]** OpenWrt Project. *Start/Stop wireless — basic Wi-Fi configuration*. <https://openwrt.org/docs/guide-user/network/wifi/basic>
  - `wifi` command semantics, the `wifi-station` section with PSK or MAC matching and WPA3 SAE support since 24.10, and the `wifi-vlan` section.
- **[Doc · ★★ · EN]** *OpenWrt wireless subsystem* — generated documentation of the source tree. <https://deepwiki.com/openwrt/openwrt/5.2-wireless-subsystem>
  - The file inventory behind the pipeline: `wifi-scripts`, `wireless.uc`, `mac80211.sh`, `hostapd.uc`, `wpa_supplicant.uc`, `wpad_acl.json`, the `601-ucode_support.patch`, and the wireless schema.
- **[Doc · ★★ · EN]** *Wireless management: mac80211, hostapd and wifi-scripts* — generated documentation. <https://deepwiki.com/ansuel/openwrt/5.2-wireless-management:-mac80211-hostapd-and-wifi-scripts>
  - How UCI becomes a hostapd configuration through ucode, and how the mt76 package is structured.
- **[Doc · ★★ · EN]** *Network configuration in OpenWrt* — community architecture write-up. <https://ducndc.github.io/blog/network-openwrt-configuration>
  - The config-to-kernel mental model, the who-does-what table, and the debugging order: config, then ubus, then kernel, then packets.
- **[Doc · ★★ · EN]** OpenWrt Project. *DSA — Distributed Switch Architecture*. <https://openwrt.org/docs/guide-user/network/dsa/start>
  - The switch model that replaced `swconfig`, and how VLAN filtering is configured on `br-lan`.
- **[Doc · ★★ · EN]** OpenWrt Project. *Firewall configuration*. <https://openwrt.org/docs/guide-user/firewall/firewall_configuration>
  - The UCI firewall options behind the data-plane section, including `flow_offloading` and `flow_offloading_hw`.
- **[Doc · ★★ · EN]** OpenWrt Project. *Attended Sysupgrade (ASU)*. <https://openwrt.org/docs/guide-user/installation/attended.sysupgrade>
  - The on-demand image build that preserves a device's package set across an upgrade.

### The neighbours — operator and cloud-managed stacks

- **[Doc · ★★★ · EN]** PLVision. *"How OpenWiFi Works: Architecture, Trust Infrastructure, and the Wired Layer."* <https://plvision.eu/blog/networking/how-openwifi-works>
  - The three-layer disaggregation, APNOS and the uCentral agent with schema-and-ucode rendering, the modular package split, the Cloud SDK with OWGW and Kafka, and the PKI 2.0 birth and operational certificate model using EST.
- **[Doc · ★★ · EN]** Light Reading. *"TIP, CableLabs advance on 'OpenWiFi'"*. <https://www.lightreading.com/broadband/tip-cablelabs-advance-on-openwifi>
  - OpenWiFi's OpenWrt origin, the move from OpenSync to uCentral, deployment scale, and CableLabs validation of the 2.9 release.
- **[Doc · ★★ · EN]** Wi-Fi NOW. *"Telecom Infra Project launches grand new vision for open-source Wi-Fi architecture"*. <https://staging.wifinowglobal.com/news-and-blog/tip-launches-grand-new-vision-for-open-source-wi-fi-architecture-everywhere>
  - The original full-stack disaggregation announcement, with OpenSync as the AP-to-cloud middleware.
- **[Doc · ★★ · EN]** Tanaza. *Open WiFi System for Communication Service Providers*. <https://www.tanaza.com/blog/open-wi-fi-system/>
  - The OpenSync model: a cloud-agnostic data model on the AP so that any controller can manage any whitebox AP.

### Wi-Fi 7 on OpenWrt — check before you quote

- **[Doc · ★★ · EN]** *MT76 device architecture* — generated documentation. <https://deepwiki.com/openwrt/mt76/9.1-device-architecture>
  - MT7996, MT7992 and MT7990 variants, band counts, the MLD index mask, WTBL size, and the per-band OMAC and VIF limits.
- **[Doc · ★★ · EN]** OpenWrt Forum. *"BPI-R4 WiFi 7 Manager — LuCI app for MT7996 / MT7988A"*. <https://forum.openwrt.org/t/bpi-r4-wifi-7-manager-luci-app-for-mt7996-mt7988a/250060/3>
  - Runtime evidence for MLO on mt76: `hostapd_cli` reporting `ieee80211be=1`, `num_links=3` and `ap_mld_type=STR`, and the beacon Multi-Link element showing EMLSR supported while EMLMR is not.

---

## 02-12 · WLAN — openwifi: An Open-Source FPGA 802.11 Platform
### The project — start here and check the licence

- **[Code · ★★★ · EN]** Jiao, X., Mehari, M., and Liu, W. *openwifi* — repository README. <https://github.com/open-sdr/openwifi>
  - The project description, the feature list, the supported boards, the published performance figures, the 802.11b note, the porting guide, and the licensing and funding statements.
- **[Code · ★★★ · EN]** Jiao, X. *openwifi-hw* — FPGA design repository README. <https://github.com/open-sdr/openwifi-hw>
  - The board table with its Vivado-licence column, the build flow and every script, the baseband clock options, the IP-core modification and simulation workflow, conditional compilation, and migration guidance for new Vivado and ADI releases.
- **[Doc · ★★★ · EN]** Jiao, X. *openwifi document* — `doc/README.md`. <https://github.com/open-sdr/openwifi/blob/master/doc/README.md>
  - The `ieee80211_ops` the driver implements, the receive and transmit interrupt paths, `sdrctl` as an nl80211 testmode command, the `tx` and `rx` register tables, the nine decisions inside `openwifi_tx()`, and the TSF timestamp explanation.
- **[Code · ★★★ · EN]** *openwifi driver source* — `driver/sdr.c`, `sdr.h`, `hw_def.h`, `sdrctl_intf.c`, `sysfs_intf.c`. <https://github.com/open-sdr/openwifi/tree/master/driver>
  - `MODULE_LICENSE("GPL v2")`, the mac80211 ops, `openwifi_rx_interrupt()` with `ieee80211_rx_irqsafe()`, `openwifi_tx_interrupt()` with `ieee80211_tx_status_irqsafe()`, and the per-IP driver modules.
- **[Code · ★★ · EN]** *openwifi-hw IP cores* — `ip/xpu/src`, `ip/tx_intf/src`, `ip/rx_intf/src`, `ip/side_ch/src`. <https://github.com/open-sdr/openwifi-hw/tree/master/ip>
  - The module inventory: `csma_ca.v`, `cw_exp.v`, `cca.v`, `tsf_timer.v`, `tx_control.v`, `pkt_filter_ctl.v`, `time_slice_gen.v`, `phy_rx_parse.v`, `tx_bit_intf.v`, `tx_iq_intf.v`, `dac_intf.v`, `csi_fuzzer.v`, `adc_intf.v`, `byte_to_word_fcs_sn_insert.v`, `side_ch_control.v` and their companions.
- **[Paper · ★★★ · EN]** Jiao, X., Liu, W., Mehari, M., Aslam, M., and Moerman, I. "openwifi: a free and open-source IEEE802.11 SDR implementation on SoC." *2020 IEEE 91st Vehicular Technology Conference (VTC2020-Spring)*, pp. 1-2, 2020.
  - The project's conference paper. Citation metadata is in `doc/cite-openwifi-vtc-paper.md`.

### The substrate it is built on

- **[Code · ★★ · EN]** *openofdm* — the 802.11 OFDM receiver openwifi's receiver derives from, and the `dot11zynq` fork carrying openwifi's improvements. <https://github.com/jhshi/openofdm>
  - Read it to understand what `openofdm_rx` does before you modify it.
- **[Code · ★★ · EN]** Analog Devices. *HDL Reference Designs*. <https://github.com/analogdevicesinc/hdl>
  - The reference designs openwifi builds on, including the `fmcomms2` project used as the porting baseline.
- **[Doc · ★ · EN]** openwifi. *Subscription and advanced features*. <https://openwifi.tech>
  - The dual-licence model and the feature set that is not in the open-source edition: Wi-Fi 6, OFDMA, RFSoC, JCAS/ISAC and other bandwidths.

### The comparison class — host-based SDR 802.11

- **[Paper · ★★★ · EN]** Bloessl, B., Segata, M., Sommer, C., and Dressler, F. "An IEEE 802.11a/g/p OFDM Receiver for GNU Radio." *Proceedings of the 2nd ACM SIGCOMM Workshop on Software Radio Implementation Forum (SRIF 2013)*, 2013.
  - The first open GNU Radio OFDM receiver for 802.11a/g/p. Defines the transceiver end of the comparison: full visibility, no MAC deadlines.
- **[Paper · ★★★ · EN]** Bloessl, B., Segata, M., Sommer, C., and Dressler, F. "Performance Assessment of IEEE 802.11p with an Open Source SDR-Based Prototype." *IEEE Transactions on Mobile Computing*, 2018. <https://www.computer.org/csdl/journal/tm/2018/05/08031977/13rRUxlgy4n>
  - A validated SDR-based 802.11p transceiver with the simulation-to-experiment methodology that a platform like this exists to support.
- **[Code · ★★ · EN]** *Wime project*. <https://wime-project.net>
  - The open-source SDR-based experimentation framework behind the GNU Radio transceiver lineage, including the 802.11p work and its measurement studies.

### Funding and provenance

- **[Doc · ★ · EN]** ORCA project. *EU Horizon 2020 research and innovation programme, grant agreement no. 732174* — the funding source acknowledged by openwifi.
- **[Doc · ★ · EN]** NLnet / NGI Zero Core. *openwifi funding pages* — the 802.11n feature, the 802.11a/g/n maturity work, and the extended OpenWrt support.

---

## 02-13 · WLAN — Reliability, Low Latency and Determinism
### The standards and the numbers they commit to

- **[Std · ★★★ · EN]** IEEE Std 802.11-2020 — retransmission limits, RTS threshold, MSDU lifetime, EDCA, TWT, BlockAck.
  - The primary source for section 4.1. Read the retry-limit and lifetime clauses rather than any secondary summary.
- **[Doc · ★★★ · EN]** Calhoun, P., Montemurro, M., and Stanley, D. (eds.). *CAPWAP Protocol Binding for IEEE 802.11*, RFC 5416. <https://www.rfc-editor.org/rfc/rfc5416.html>
  - §6.7 restates the dot11 MIB defaults that this note quotes: short retry 7, long retry 4, RTS threshold 2347, Tx MSDU lifetime 512 TU, Rx MSDU lifetime 512.
- **[Std · ★★ · EN]** IEEE Std 802.11e-2005, 802.11r-2008, 802.11k-2008, 802.11v-2011, 802.11ax-2021 and 802.11be-2024 — EDCA, Fast BSS Transition, radio resource measurement, WNM, TWT/OFDMA, and MLO with r-TWT and SCS.
- **[Doc · ★ · EN]** ITU-T Recommendation G.114 — the 150 ms one-way recommendation that every voice roaming budget is measured against.

### Rate control — read the algorithm before you claim a reliability problem

- **[Doc · ★★★ · EN]** Linux wireless. *Minstrel rate control — theory of operation*. <https://www.linuxwireless.sipsolutions.net/en/developers/Documentation/mac80211/RateControl/minstrel>
  - The 100 ms interval, the EWMA smoothing factor, the 10% lookaround rate, the four-entry MRR chain and the 26 ms chain cap. Also where `rc_stats` in debugfs is explained.
- **[Paper · ★★★ · EN]** *MAC-Layer Rate Control for 802.11 Networks: Lesson Learned and Looking Forward*. arXiv:1807.02827. <https://arxiv.org/abs/1807.02827>
  - The survey with the Minstrel equations, the 75% EWMA weight, the retry-preference tables, and why throughput-based control behaves differently from loss-based control under collisions.

### Queueing in the Wi-Fi stack — the part you can actually change

- **[Code · ★★★ · EN]** Yan, K., and Høiland-Jørgensen, T. *mac80211: Implement Airtime-based Queue Limit (AQL)*, Linux commit `3ace10f`. <https://lore.kernel.org/r/20191119060610.76681-4-kyan@google.com>
  - The rationale (CoDel's sojourn time excludes the firmware queue; bytes are the wrong unit for a wireless queue) and the constants 5000 / 12000 / 24000 plus the debugfs interface.
- **[Paper · ★★★ · EN]** Høiland-Jørgensen, T., Kazior, M., Täht, D., Hurtig, P., and Brunstrom, A. *Bufferbloat mitigation in the WiFi stack — status and next steps*, Netdev 2.2. <https://www.netdevconf.info/2.2/papers/jorgensen-wifistack-talk.pdf>
  - The numbers this note quotes: FIFO versus FQ-CoDel versus FQ-MAC latency under a saturating download, the airtime shares, and the net throughput increase from fairness.
- **[Code · ★★★ · EN]** Høiland-Jørgensen, T. *mac80211: Adjust TSQ pacing shift*, Linux commit `36148c2bbfbe`. <https://lore.kernel.org/linux-wireless/20180202151105.30043-1-toke@toke.dk/t/>
  - The throughput table for `sk_pacing_shift` 10/9/8/7 and the explicit latency cost of the change.
- **[Paper · ★★ · EN]** Grazia, C. A., Patriciello, N., Høiland-Jørgensen, T., Klapez, M., Casoni, M., and Mangues-Bafalluy, J. *Adapting TCP Small Queues for IEEE 802.11 Networks*. IEEE PIMRC 2018, pp. 1-6. <https://doi.org/10.1109/PIMRC.2018.8581048>
  - Controlled TSQ: the throughput/latency trade made rate-aware rather than fixed.
- **[Doc · ★★ · EN]** Corbet, J. *TCP small queues and WiFi aggregation — a war story*. LWN.net. <https://lwn.net/Articles/757643>
  - The engineering narrative behind the pacing-shift change, told by the people who debugged it.
- **[Paper · ★★★ · EN]** Nichols, K., and Jacobson, V. *Controlling Queue Delay*. Communications of the ACM 55(7), 2012 — CoDel: 5 ms target, 100 ms interval, minimum sojourn time as the control signal.
- **[Doc · ★★ · EN]** IETF. *Controlled Delay Active Queue Management*, RFC 8289; *The Flow Queue CoDel Packet Scheduler*, RFC 8290.
- **[Doc · ★★★ · EN]** Briscoe, B., Schepper, K. D., Bagnulo, M., and White, G. *L4S architecture*, RFC 9330; Schepper and Briscoe, *ECN protocol for L4S*, RFC 9331; *DualQ Coupled AQM*, RFC 9332. <https://www.rfc-editor.org/rfc/rfc9332.html>
  - RFC 9332 carries the measured L4S queuing delays and the note that Wi-Fi L4S trials were in progress at the time of writing.

### Latency across links and generations

- **[Paper · ★★★ · EN]** *Next Generation Wi-Fi and 5G NR-U in the 6 GHz Bands: Opportunities & Challenges*. IEEE document 9165719. <https://ieeexplore.ieee.org/ielaam/6287639/8948470/9165719-aam.pdf>
  - The four-component latency decomposition, and the multi-link results: hundreds of milliseconds at the 95th percentile for a single-link device, an order-of-magnitude reduction with multi-link, latency as low as 25% of single-link.
- **[Paper · ★★★ · EN]** MediaTek. *Wi-Fi 7 Multi-Link Operation (MLO) White Paper*, WF7MLOWP0622. <https://www.mediatek.com/hubfs/Wi-Fi-7-MLO-White-Paper-WF7MLOWP0622.pdf>
  - The 95th-percentile latency table for single-link, NSTR, STR and EMLSR at 10/40/70% network loading, and the UMAC/LMAC architecture partitions.
- **[Paper · ★★ · EN]** Kedar, E. *Single-Chip MLO Coordination Enables Path to Lowest Latency*. MaxLinear white paper, 2025. <https://www.maxlinear.com/news/white-papers/2025/single-chip-mlo-coordination-enables-path-to-lowest-latency>
  - The ~70% STR latency reduction claim in dense simulated and real environments, and the single-MAC versus multi-MAC argument.
- **[Paper · ★★★ · EN]** Multi-link analyses: arXiv:2111.09281 (latency with real over-the-air occupancy traces), arXiv:2210.07695 (the starvation anomaly), arXiv:2212.12420 (finite-load delay model), arXiv:2205.15065 (coexistence with legacy single-link), arXiv:2305.02052 (latency and throughput together).
  - Read these for the caveats: symmetry decides the sign, single-radio MLO underdelivers on worst case, and more than two links adds little.

### Bounded latency and the next generation

- **[Paper · ★★★ · EN]** Ofinno. *Wi-Fi 8: Ultra High Reliability in the Unlicensed Bands*. <https://ofinno.com/wp-content/uploads/2023/01/Wi-Fi-8-Ultra-High-Reliability-in-the-Unlicensed-Bands_Digital-Copy.pdf>
  - The statement that 802.11be with r-TWT and SCS achieves bounded latency below 25 ms, why that is not enough for sub-millisecond industrial use, and why r-TWT cannot protect aperiodic traffic.
- **[Paper · ★★★ · EN]** Mozaffariahrar, E., Wilhelmi, F., Galati-Giordano, L., Imputato, P., Menth, M., and Avallone, S. *R-TWT in Wi-Fi 7 and Beyond: Enabling Bounded Latency, Energy Efficiency, and Reliability*. <https://www.upf.edu/documents/d/fwilhelmi/r-twt_in_wi-fi_7_and_beyond_enabling_bounded_latency_energy_efficiency_and_reliability-pdf>
  - ns-3 evaluation of r-TWT across traffic types and network sizes: worst-case latency, energy, collision rate and throughput, against PSM and DCF.
- **[Paper · ★★★ · EN]** Ha, T., Shafin, R., and Manasi. *IEEE 802.11bn (Ultra-High Reliability, Wi-Fi 8)*. Samsung Research. <https://research.samsung.com/blog/IEEE-802-11bn-Ultra-High-Reliability-UHR-Wi-Fi-8>
  - The PAR targets as stated by a participant: +25% throughput at a given SINR, -25% latency at the 95th percentile, -25% dropped packets.
- **[Paper · ★★★ · EN]** *What Will Wi-Fi 8 Be? A Primer on IEEE 802.11bn Ultra High Reliability*. arXiv:2303.10442. <https://arxiv.org/html/2303.10442v2>
  - The use-case requirements table (99.9% to 99.9999999% reliability, 0.1-100 ms latency) that motivates the whole UHR programme.

### Measurement

- **[Tool · ★★★ · EN]** Høiland-Jørgensen, T., and Täht, D. *FLENT: The FLExible Network Tester*. <https://flent.org>
  - Controlled load plus latency distribution in one run — the tool that produced the curves behind the bufferbloat work.
- **[Paper · ★★ · EN]** Gettys, J., and Nichols, K. *Bufferbloat: Dark Buffers in the Internet*. ACM Queue 9(11), 2011 — the problem statement.
- **[Code · ★★ · EN]** Linux `iw` source, `phy.c` — `set retry`, `set rts`, `set frag`, `set coverage`, `set distance`, `set txq`, all over `NL80211_CMD_SET_WIPHY`.

### The comparison case

- **[Std · ★★ · EN]** 3GPP TS 22.261 and TR 22.804 — the URLLC service requirements used in the cross-technology comparison, and TS 23.501 for ATSSS as the multi-access reliability counterpart.

---

## 02-14 · WLAN — Wi-Fi Fundamentals: History, Architecture, PHY, MAC and the Road to Wi-Fi 7

The two books this note is built from are the only books in the vault that are read end to end rather than
consulted. Everything else in this section exists to check them.

### The two books — read these first, in this order

- **[Book · EN · ★★★]** *Wi-Fi 7 In Depth: Your Guide to Mastering Wi-Fi 7, the 802.11be Protocol, and Their Deployment* — Jerome Henry, Binita Gupta, Brian Hart, Malcolm Smith · Addison-Wesley / Cisco Press, 2024 · 385 pp. · ISBN 978-0-13-532351-9
  - The protocol reference. Chapter 1 is the best short account of the 802.11 architecture, the connection process and channel access in print; ch 2 explains what legacy QoS could not do and therefore why 802.11be exists; ch 3 treats Wi-Fi 6 as the foundation rather than a footnote; ch 5 walks the EHT PPDU field by field; ch 6 is the MLO chapter, including the five client modes that decide what a deployment may promise; ch 7 covers r-TWT, SCS, triggered uplink and TXOP sharing; ch 8 is deployment and site survey; ch 9 is the future-direction chapter.
  - Read ch 1 twice. Sections 3, 4 and 5 of note 02-14 are essentially a compression of it, and every later chapter assumes it.
- **[Book · EN · ★★★]** *Wi-Fi 7: Principles, Technology, and Applications* — Gang Cheng, Zhihong Qian, Yiming Jiang, Zhijie Yang, Thirumurthy Rajamanickam · Springer, 2025 · XXVI + 464 pp. · DOI 10.1007/978-981-97-9026-5
  - The device-vendor reference, written by a Nokia broadband device BU. Chapter 1 is a 77-page Wi-Fi overview with the historical and standards scaffolding; ch 2 is Wi-Fi 6; ch 3 is the Wi-Fi 7 feature set at 136 pages; **ch 4 is the one nobody else writes**: product development and test methods, from EVT to mass production; ch 5 is the Wi-Fi Alliance programme; ch 6 is applications; **ch 7 is the convergence chapter** — 5G-RG, non-3GPP access, ATSSS, FWA; ch 8 is the outlook.
  - Read ch 4 and ch 7 even if you never touch a product line. They are the two chapters that connect the standard to money.

### Standards — the things the books paraphrase

- **[Std · ★★★ · EN]** IEEE Std 802.11be-2024 — EHT: 320 MHz, 4096-QAM, MRU, preamble puncturing, MLO, r-TWT, SCS, triggered TXOP sharing.
  - The books describe these accurately; the clause is what settles an argument about a permitted puncturing pattern or an MLO capability bit.
- **[Std · ★★★ · EN]** IEEE Std 802.11-2020 (and the 2024 revision) — the base document: MAC architecture, frame formats, DCF and EDCA parameters, block acknowledgement.
  - Table 10-x of the EDCA defaults, clause 10.3 for DCF, clause 9 for frames. Quote the clause, not a blog.
- **[Std · ★★ · EN]** IEEE Std 802.11-1997, 802.11b-1999, 802.11a-1999, 802.11g-2003, 802.11e-2005, 802.11i-2004, 802.11n-2009, 802.11ac-2013, 802.11ax-2021.
  - For the history section: read the scope clause of each amendment and note what it says the problem was. The preambles are a primary source for the intent behind each generation.

### History and context

- **[Paper · EN · ★★]** Abramson, N. *The ALOHA System — Another Alternative for Computer Communications*. AFIPS Fall Joint Computer Conference, 1970.
  - Where random access over a shared medium begins. Every backoff in every Wi-Fi chip is a descendant of this paper.
- **[Doc · EN · ★★]** FCC. *Report and Order, Unlicensed Use of the 6 GHz Band*, ET Docket No. 18-295, adopted 23 April 2020.
  - The 1200 MHz allocation, the three device classes, and the AFC framework that decides whether 320 MHz is usable at a given address.
- **[Doc · EN · ★★]** Wi-Fi Alliance. *Wi-Fi CERTIFIED 7* programme (January 2024) and *Wi-Fi CERTIFIED 6E* (January 2021).
  - What the logo tests, and — more usefully — what it does not. See also `02-3` for the programme history.
- **[Paper · EN · ★★]** *Wi-Fi: Twenty-Five Years and Counting* — Geraci et al., *Proceedings of the IEEE* 113(11), 2025, arXiv:2507.09613.
  - The independent cross-check on the history in §2 of note 02-14. Where the two books and this paper disagree on a date, trust the paper and mark the book `VERIFY`.
- **[Paper · EN · ★★]** Khorov, E., Kiryanov, A., Lyakhov, A., and Bianchi, G. *A Tutorial on IEEE 802.11ax High Efficiency WLANs*. IEEE Communications Surveys & Tutorials 21(1), 2019.
  - The Wi-Fi 6 mechanisms in §10 of note 02-14, with the analysis behind the uplink-OFDMA round cost.

### Convergence with 5G

- **[Std · ★★ · EN]** 3GPP TS 23.316 — wireless and wireline convergence: 5G-RG, FN-RG and the wireline access gateway function.
- **[Std · ★★ · EN]** 3GPP TS 23.501 — non-3GPP access: N3IWF for untrusted, TNGF for trusted Wi-Fi.
- **[Std · ★★ · EN]** 3GPP TS 23.793 — ATSSS: steering, switching and splitting, with MP-TCP, MP-QUIC and ATSSS-LL.
  - Read the three together, not separately: TS 23.316 gives the residential gateway its 5G identity, TS 23.501 gives Wi-Fi a path into the core, TS 23.793 decides which link carries which flow. The convergence diagram in §17 of note 02-14 is these three clauses drawn once.

### Cross-checks for the arithmetic

- **[Doc · EN · ★]** TP-Link. *What is Wi-Fi 7* — PHY rate derivation table. <https://www.tp-link.com/wifi7/>
  - A vendor page, not an authority, but it publishes the tone-plan arithmetic (`3920 × 5/6 × log2(4096) / 13.6 µs`) that reproduces 2882.4 Mbps per stream and 46.08 Gbps at 16 streams. Useful precisely because it also publishes the 16-stream number that the standard does not contain.
- **[Book · EN · ★★]** Gast, M. S. *802.11 Wireless Networks: The Definitive Guide*, 2nd ed., O'Reilly, 2005 — see §02-1.
  - The IFS, NAV and frame taxonomy in §3 and §5 of note 02-14 are his; the tables are worth checking against the clause.

---

## Standards and repositories

- **IEEE 802.11 Working Group** — `www.ieee802.org/11/`. Task group pages (TGbn for Wi-Fi 8), ballot status and amendment timelines.
- **IEEE Xplore / IEEE Standards Association** — normative texts of 802.11-2024, 802.11ax-2021, 802.11be-2024, 802.11bf-2025, 802.11ba-2021 (wake-up radio), 802.11ah-2016 (HaLow), 802.15.4-2020, 1905.1a-2014.
- **Wi-Fi Alliance** — `wi-fi.org`. Certification program specifications and EasyMesh.
- **prpl Foundation** — prplOS, prplMesh and prpl LCM open-source projects.
- **Broadband Forum** — TR-069, TR-181, TR-369 (USP).


---

_Copyright (c) 2026 Washington Ruan and contributors · licensed under **GPL-3.0-or-later** or **AGPL-3.0-or-later**, at your option · see `LICENSE` and `LICENSE-AGPL`._
