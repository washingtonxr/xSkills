---
title: Corrections — Verified Facts That Popular Sources Get Wrong
type: appendix
domain: root
tags:
  - corrections
  - verification
license: GPL-3.0-or-later OR AGPL-3.0-or-later
last-updated: 2026-10-29
---

# Corrections — verified facts that popular sources get wrong

> **What this page is for.** Every row below is a claim you will meet in a blog post, a vendor deck or a textbook margin, next to what the primary source actually says. They are the residue of writing the notes: the places where the widely repeated version is wrong, out of date, or true only under a condition nobody states.
>
> Use it two ways. Before you repeat a number in an interview, check it here — the correction is cheaper than the wrong answer. And when a note and a blog disagree, this page is the record of which one was checked.

## How to read the table

- **The claim** column is the popular version, quoted or paraphrased as it usually appears.
- **What the source says** column is the verified position, with the clause, release or date that settles it, and the note that carries the full argument in its **Anchors**.
- Rows marked `VERIFY` in a note are a different thing: those are *open* questions, kept deliberately in the note rather than resolved here.

| Claim | What the source says |
| --- | --- |
| **eRedCap release** — attributed to Rel-19 | It is **Rel-18** (frozen 2024-06; 5 MHz, 1 Rx, HD-FDD, ~10 Mbps). Rel-19's contribution is the NTN extension, LP-WUS, and Ambient IoT |
| **Wi-Fi 8 progress** — Draft 1.0 (2025-08) | **Draft 1.0 was 2025-07**; Draft 2.0 passed WG ballot on 2026-09-02 at 76.5%; WFA certification around **2028-01** |
| **Rel-21 milestones** — "complete 2029, commercial 2030" | Four official milestones: Stage-1 **2027-03** / Stage-2 **2028-06** / Stage-3 **2028-12** / ASN.1+OpenAPI **2029-03** |
| **PREEMPT_RT** — not covered | Merged into mainline in **Linux 6.12 (2024-11)** for x86/arm64/RISC-V; 32-bit ARM added in 7.1 |
| **C/C++ standard status** — mentions only "C/C++" | **C23 = ISO/IEC 9899:2024** (published 2024-10-31, `__STDC_VERSION__` = 202311L); **C++26 shipped by WG21 on 2026-03-28** (working draft N5046), to be published as ISO/IEC 14882:2026 |
| **AUTOSAR / MISRA versions** — not covered | **AUTOSAR R25-11** is current (Release Event 2025-12-04); **MISRA C:2025** is the current C edition and supersedes MISRA C:2023; **MISRA C++:2023** (TC1:2026) targets C++17 — so a MISRA-conformant C++ project is not on C++20/23/26 |
| **TWT origin** — often attributed to 802.11ax | It originated in **802.11ah-2016** (Wi-Fi HaLow) and was carried into 802.11ax. 802.11be then added **r-TWT**, which is a latency mechanism first and a power mechanism second |
| **802.11bi** — sometimes described as a wake-up-radio amendment | It is **Enhanced Privacy Protection**, approved for publication **2026-09-25** — see note 02-2. The wake-up radio amendment is **802.11ba-2021** |
| **r-TWT deployment** — assumed present in Wi-Fi 7 devices | r-TWT is **optional** in 802.11be and **not required for Wi-Fi CERTIFIED 7**; a 2026 CWNP review reports shipping clients and APs did not advertise support. Treat as `VERIFY` before claiming deployment |
| **Linux bottom halves** — "tasklet is the fast deferred-work mechanism" | Tasklets are **deprecated**. The API was modernised around 5.9 and the replacement is **WQ_BH**, merged for **6.9** with `system_bh_wq` and `system_bh_highpri_wq`; it runs in softirq context, may not sleep and requires `max_active = 0`. The tasklet API still exists and conversion is ongoing — see note 04-4 |
| **Power ramping after a contention loss** — "a UE that loses contention restarts from Msg1 without ramping power" | It **does** ramp. TS 38.321 clause 5.1.3 increments `PREAMBLE_POWER_RAMPING_COUNTER` on four transmission conditions only — the attempt counter is above one, the SSB/CSI-RS is unchanged, the PHY has not sent the power-ramping-suspension notification, and no LBT failure was reported — with **no carve-out for contention-resolution losses**. The narrow statement that is true is the beam rule: no ramping when the beam changes, whatever the cause. Note that this also removes a common shortcut — collisions cannot be told apart from coverage misses by the power column — see note 01-5 §9.3 |
| **OpenWrt identity** — “a router firmware” | It is a **Linux distribution plus a cross-build system** with four downloadable artifacts (source tree, ImageBuilder, SDK, package repository). The wireless stack is a set of independently versioned packages — kernel, `mac80211` backport, driver, `wpad`, firmware and board data — so a wireless regression is often version skew between them, not a bug in one. And OpenWrt ships **no network-level wireless policy**: steering, mesh healing and channel planning are packages you deploy — see note 02-11 |
| **openwifi scope** — “an open-source Wi-Fi chip” or “a full modern Wi-Fi stack” | It is a **Linux-mac80211-compatible SDR implementation of 802.11a/g/n** on a Zynq SoC: PHY and low MAC in FPGA, high MAC in mac80211. It is OFDM only (no 802.11b), 20 MHz, MCS 0–7, and measured at iperf TCP 40–50 Mbps; Wi-Fi 6, OFDMA, RFSoC and JCAS/ISAC are **subscription features**, not open source. Note also the name collision: TIP’s OpenWiFi is a different project — a cloud-managed AP architecture on OpenWrt — see note 02-12 |
| **Wi-Fi latency** — "a few milliseconds" | Idle, yes. Under a saturating download a deep driver or firmware queue puts latency at **several hundred milliseconds**; FQ-CoDel leaves a slow station above 200 ms median and fast ones around 35 ms, and per-station fair queueing cuts the fast stations by another ~45%. The dominant *loaded* term is queueing, and the dominant *worst-case* term is channel access — raising the PHY rate does not shorten either. See note 02-13 |
| **MLO latency** — "more links always means lower latency" | Only when the links are **similarly occupied**. Vendor measurements show STR at 2/8/18 ms versus single-link 30/70/150 ms at the 95th percentile across 10/40/70% load, but with a much busier secondary link, STR can raise worst-case latency above single-link, and single-radio EMLSR gives negligible p95 improvement at medium-to-high load. See note 02-13 |
| **"Good technology wins the market" · "price from cost, then discount"** — "the best product sells itself; cost plus margin is the honest price" | Both fail on the same arithmetic. Creating value and capturing it are different activities, and your share is bounded by your **added value** — what the chain loses without you — not by how good the engineering is: Xerox PARC produced the graphical interface and laser printing and captured comparatively little, because appropriability was weak and the complementary assets sat elsewhere. And cost sets the *floor*, not the price: on the average S&P 1500 income statement a 1% price rise lifts operating profit about **8%** (8.7% on Global 1200 figures), roughly 50% more than a 1% variable-cost cut and three times a 1% volume gain, while a 5% price cut needs about **18.7%** more volume to break even. Price to a measured value range instead, and make the **metric** — what you charge for — track the value driver. See note 10-1 |
| **"Agile means no planning" · "add people to catch up"** — "agile replaces planning with speed; more people finish sooner" | Both are wrong, and both are testable. Agile increases planning *frequency* and shortens the planning *horizon* — inspect-and-adapt is a control loop, not the absence of one. And Brooks's law: adding people to a late project makes it later, because newcomers need training, the work must be repartitioned, and communication paths grow as n(n−1)/2. The empirical base is harsher than intuition: on Flyvbjerg's 16,000-project database only 8.5% of projects land on budget **and** on time, while the Standish size effect puts small projects at 61% success against 6% for the largest — so the highest-leverage move is splitting the work and limiting WIP, not staffing up. See note 09-1 |
| **OpenAirInterface licence** — "open source, Apache or GPL" | None of the three. OAI moved **GPL v2 → OAI Public License v1.1 (2017) → CSSL v1.0**, changed in the RAN repository on **2026-03-27** alongside the Duranta launch under Linux Foundation Networking. CSSL is Apache 2.0 plus a FRAND patent clause, so SEP holders can contribute; it is **not OSI-approved** and commercial use is on FRAND terms. Also worth separating: OAI is a research-grade softmodem — 4-layer DL / 2-layer UL, no production MU-MIMO, static TDD — not a carrier DU, see note 01-8 |
| **NR HARQ process count** — "16 by default" | It is **8** when `nrofHARQ-ProcessesForPDSCH` is absent; 16 is the maximum, not the default. And more is not automatically better: every process holds a soft buffer and total UE soft-buffer memory is a capability, so n16 on a cell that only needs six can reduce the combining gain available to each retransmission — see note 01-6 §8.3 |

---

## Why a corrections page instead of footnotes

Two reasons, both practical.

**Secondary sources copy each other.** The RACH write-ups all repeat each other's claim that contention-resolution losers do not ramp power; TS 38.321 clause 5.1.3 has no such carve-out. Once a wrong sentence has three citations behind it, the only defence is to go back to the clause — so the clause number belongs in one place, not scattered across ten notes.

**Dates decay silently.** "Current release", "latest kernel", "shipping devices" are all true for about a year. Where a note depends on one of those, the date is written down here and in the note's Anchors, so a reader in 2028 can see which sentence has expired instead of trusting the whole document.

Corrections to this page are the most valuable contribution the repository accepts: open a pull request with the claim, the primary source and the date, and cite the clause rather than a summary of it.

---

_Copyright (c) 2026 Washington Ruan and contributors · licensed under **GPL-3.0-or-later** or **AGPL-3.0-or-later**, at your option · see `LICENSE` and `LICENSE-AGPL`._
