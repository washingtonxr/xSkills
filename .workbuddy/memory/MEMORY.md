# Project: 261022,PersonalSkills — long-term conventions

Personal knowledge base for interview preparation at the intersection of
**communications technology x heterogeneous compute x AI**. Owner: Washington Ruan.

## File naming convention (decided 2026-10-22)

**English is the default filename (no suffix); Chinese versions carry `.cn`.**

| File | Role |
| --- | --- |
| `README.md` | **One file, Chinese then English.** There is no `README.cn.md` any more (removed 2026-10-29) |
| `other/background.md` / `other/background.cn.md` | Profile + task statement (moved to `other/` 2026-10-29) |
| `other/skills-draft.md` / `other/skills-draft.cn.md` | Knowledge framework + interview outline (moved to `other/`) |
| `knowledge-graph/<DIR>/readlist.md` | **One per directory** — the root `readlist.md` was split 2026-10-29 |

The `.en` suffix is **not** used. Do not reintroduce it.

**Note filenames (normalised 2026-11-01)** follow one scheme across every directory:/n`GG-x DOMAIN - Topic - Scope.md` — ASCII hyphens, no slashes, no em dashes. The frontmatter `title:`
mirrors it as `"DOMAIN — Topic: Scope"` (em dash then colon). Frontmatter always carries `type`, `domain`,
`group`, `series`, `tags`, `aliases`, `license`, `last-updated`. Renaming a note means rewriting every
`[[wikilink]]` vault-wide plus MOC, README, readlist and memory in one scripted pass.

## Language convention

- Every note under `knowledge-graph/` is **English only**. Never write Chinese inside the vault.
- Source documents are bilingual, one-to-one.

## Vault structure

- `knowledge-graph/` is the Obsidian vault root — open *that* folder, not the project root.
- `00 MOC - Comms x Compute x AI Knowledge Graph.md` is the single entry point: directory map, reading and memory method, contribution method, maintenance triggers.
- Notes live in **one folder per domain**: `MN/ WLAN/ WSN/ EMBEDDED/ DATAPLANE/ AI/ SILICON/ LANGUAGES/ MANAGEMENT/ BUSINESS/ HAM/`. Wikilinks still resolve because Obsidian matches by note name, so moving a note between folders does not break links.
- `99 Corrections - Verified Facts That Popular Sources Get Wrong.md` is the appendix that used to be README §7.
- Notes are numbered **`GG-x`** by domain group; the file name *is* the topic.
- Fixed note body shape: knowledge points → **Anchors** → **Related** → **References**; the big domain notes (01-5/01-6/01-7/01-8/09-1/10-1/02-7/02-8/02-9/02-10/02-11/02-12/02-13/06-3/04-4/04-5/04-6) all close with **References** (real books/PEPs/standards with ISBN/DOI/URL), because the user requires citations at the end of the article.
- Diagrams are **Mermaid** code blocks (render natively in Obsidian reading view); every note is expected to carry them in its structural sections (architecture, data path, timing, decision logic), not just in passing.
- Bulk renumbering recipe: two-phase `git mv` (old → `__tmp__` → final) to avoid filename collisions, then one regex pass with `(?<![\d\-])(\d{2})-(\d)(?!\d)` and a lookup dict — single pass avoids chained rewrites, and the lookbehind protects dates and version strings.

## Note numbering scheme `GG-x` (renumbered 2026-10-22)

Group number `GG` is **sequential from `01` and contiguous** — an earlier scheme
inherited numbers from each group's original top-level note and left gaps; that was
replaced on request. Group order follows the signal path outward:

| Group | Domain | Notes |
| --- | --- | --- |
| `01-x` | Cellular and mobile communications | 01-1 5G-A/6G radio access · 01-2 NR RAN L2 · 01-3 AI/ML for RAN and O-RAN · 01-4 cellular IoT (RedCap/eRedCap/NTN) · 01-5 NR random access (RACH) · 01-6 NR DU MAC scheduler · 01-7 NR HARQ with the LTE comparison · 01-8 OpenAirInterface and the architecture of an open-source NR stack |
| `02-x` | WLAN | 02-1 generations from Wi-Fi 4 to Wi-Fi 8 and beyond, with which WFA programme certified each and which application paid for it · 02-2 power saving · 02-3 ecosystem: the four bodies (IEEE / WFA / WBA / prpl-BBF), the eight-category WFA certification catalogue, generation programmes 6E/7/8, WPA3 / Enhanced Open / PMF, Passpoint and OpenRoaming, EasyMesh R1-R6, prplMesh / prplOS / RDK-B, and the application map · 02-4 TX/RX datapath and offload · 02-5 discovery, authentication and association · 02-6 roaming, healing and steering · 02-7 EasyMesh operation, tuning and troubleshooting · 02-8 scheduling, EDCA, OFDMA, airtime · 02-9 TSN over Wi-Fi across generations · 02-10 baseband and driver architecture for Wi-Fi 6/7/8 with Qualcomm as the reference design · 02-11 OpenWrt and the software architecture of a wireless system · 02-12 openwifi an open-source FPGA 802.11 platform · 02-13 reliability low latency and determinism in the Wi-Fi stack · 02-14 Wi-Fi fundamentals (history, architecture, join, CSMA/CA, numerology, rate arithmetic, Wi-Fi 6 hinge, Wi-Fi 7 PHY/MAC, deployment, product test, 5G convergence) built from *Wi-Fi 7 In Depth* and *Wi-Fi 7: Principles, Technology, and Applications* · 02-15 the transceiver (five jobs, noise/EVM budget, superheterodyne to zero-IF to digital-assisted, TX/RX chains with time budgets, MIMO and MLO costs, power and coexistence, 802.11bf sensing, AI in the radio and the 16 microsecond SIFS wall) · 02-16 radio resource management (four resources and four clocks, measure-decide-actuate-verify and the authority gradient, the 802.11k measurement catalogue, five channel assignment families, Cisco TPCv1 with Tx_Ideal, DFS, spatial reuse and equation 26-5, admission control, the worked steering score function, the six-phase roam algorithm with its time budget, EasyMesh vs 802.11bn MAPC, and what AI can and cannot change) · 02-17 dynamic frequency selection (three laws, U-NII and ETSI channel maps, FCC vs ETSI parameter table, master/client obligations, radar waveforms and detection probabilities, CSA machinery, outage budget, why 6 GHz has no DFS) · 02-18 AI in Wi-Fi and the 802.11bx WIN vision (three roles: AI as protocol, platform and traffic; the AI/ML TIG to AI-Offload-SG to WIN-SG paper trail; PHY candidates ranked by what they break, from CSI compression and neural receivers to pilotless waveforms; the four MAC time loops; why a learned MAC cannot promise five nines; the AC_AI case study with its parameters and arithmetic; determinism enforced outside the learner; the four gates incl. testability without the model) |
| `03-x` | Low-power and sensor networking | 03-1 WSN and low-power MAC |
| `04-x` | Embedded and systems software | 04-1 RTOS and hardware interfaces · 04-2 Linux embedded · 04-3 software architecture · 04-4 Linux interrupts · 04-5 concurrency, processes, threads and IPC · 04-6 device drivers (model, probe, data path, power, bring-up) |
| `05-x` | Data plane and heterogeneous compute | 05-1 DPDK/UPF · 05-2 cloud-edge-end |
| `06-x` | Machine learning, AI inference and agent systems | 06-1 LLM inference/xLLM · 06-2 agent systems · 06-3 machine learning foundations (read first) |
| `07-x` | Silicon and ISA | 07-1 RISC-V |
| `08-x` | Programming languages and practice | 08-1 toolchain and performance · 08-2 C and C++ · 08-3 Python · 08-4 MATLAB/Simulink · 08-5 Verilog HDL |
| `09-x` | Engineering project management and delivery | 09-1 engineering project management — methodology, lifecycle, tools and best practice |
| `10-x` | Value-driven business model and monetisation | 10-1 value-driven business model — methodology, process, tools and best practice |
| `11-x` | Amateur radio (ham radio) | 11-1 amateur radio — history, regulation, licence classes, bands, the 2026 state of the hobby · 11-2 operating practice — link budget, propagation, antennas, feedlines, modes, the QSO |

Group number `GG` is also the **folder name**, in order: `01 → MN`, `02 → WLAN`,
`03 → WSN`, `04 → EMBEDDED`, `05 → DATAPLANE`, `06 → AI`, `07 → SILICON`,
`08 → LANGUAGES`, `09 → MANAGEMENT`, `10 → BUSINESS`, `11 → HAM`.

Each directory's `readlist.md` uses the **same** `GG-x` numbers for its sections.
Renumbering a note means renumbering its readlist section and its directory table
row in the MOC.

## Content conventions

- **Anchors** sections hold only checkable facts with a date or number (spec numbers, freeze dates, DOIs, release versions).
- Anything not independently confirmed is marked **`VERIFY`**, never asserted.
- `[[wikilinks]]` are deliberate — a link means the two concepts get argued about together in interviews.
- Source documents stay faithful to the original draft; **corrected facts live in the Anchors sections**, and `knowledge-graph/99 Corrections ...` records source-vs-verified discrepancies (it replaced the README fact-check table on 2026-10-29).
- **Verify procedural claims against the clause, not the secondary sources.** Collected blog sources repeat errors verbatim — every popular RACH write-up claims contention-resolution losers do not ramp power, and TS 38.321 clause 5.1.3 shows they do. When a new section will restate an existing claim, re-check the clause first.
- Structural diagrams follow the question: an "architecture / who does what" view is a **sequenceDiagram with the layers as participants** (the vertical order is the layering, the horizontal arrows are the messages), not a flowchart of boxes.
- **Licensing (changed 2026-10-29, on request):** the project is open source under **GPL-3.0-or-later OR AGPL-3.0-or-later** (dual, user's choice). The old `All rights reserved` line is gone everywhere — do not reintroduce it. Frontmatter carries `license: GPL-3.0-or-later OR AGPL-3.0-or-later`; the footer is one italic line: `_Copyright (c) 2026 Washington Ruan and contributors · licensed under **GPL-3.0-or-later** or **AGPL-3.0-or-later**, at your option · see \`LICENSE\` and \`LICENSE-AGPL\`._` Full texts: `LICENSE` (GPL v3), `LICENSE-AGPL` (AGPL v3).
- Frontmatter: `title`, `last-updated`, `license`; `lang`/`category` where the document has one; `sibling` for bilingual pairs in `other/`; `version` for the README.

## Verification commands

Link and structure integrity is checkable with a Python pass that strips code
fences and code spans before matching (C++ attribute syntax such as
`[[nodiscard]]` and lambda parameter lists like `[](int a, int b)` are false
positives otherwise):

```python
import re, glob, os
# strip ``` fences and `code spans`, then match [[wikilinks]] and [](links)
```
