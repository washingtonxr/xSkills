---
title: Reading list — WSN · Low-power and sensor networking
lang: en
category: reading-list
license: GPL-3.0-or-later OR AGPL-3.0-or-later
last-updated: 2026-10-29
---

# Reading list — WSN · Low-power and sensor networking

> Low-power wireless: WPAN medium access, clustering and routing, time-slotted channel hopping, and age of information as the metric that matters when energy is the constraint.
>
> One section per note, numbered `GG-x`. Where a note needed no source beyond its own
> **References**, there is no section here — the note is self-sufficient.

## How to use this list

- **Marks.** Type and priority marks (`★★★`, `[Book]`, `[EN]`) are defined once, in the MOC under *Reading marks*. The rule that matters: `★★★` means read or skim before you quote the note in an interview.
- **Titles** are kept in their published form and never translated; descriptions are English.
- **Nothing is asserted.** Where a citation could not be confirmed against a publisher, DOI, arXiv record or the issuing body, it is marked `VERIFY`.

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

## Standards and repositories

- **IEEE 802.15.4-2020** — the normative low-rate WPAN MAC and PHY text (802.15.4-2020 consolidated the 2015 base with its amendments). Use it for frame formats, the superframe and GTS structure, and the CSMA-CA parameters; vendor and silicon documentation is where the actual radio behaviour lives.


---

_Copyright (c) 2026 Washington Ruan and contributors · licensed under **GPL-3.0-or-later** or **AGPL-3.0-or-later**, at your option · see `LICENSE` and `LICENSE-AGPL`._
