# Project: 261022,PersonalSkills — long-term conventions

Personal knowledge base for interview preparation at the intersection of
**communications technology x heterogeneous compute x AI**. Owner: Washington Ruan.

## File naming convention (decided 2026-10-22)

**English is the default filename (no suffix); Chinese versions carry `.cn`.**

| File | Role |
| --- | --- |
| `README.md` / `README.cn.md` | Project README (English default) |
| `background.md` / `background.cn.md` | Profile + task statement |
| `skills-draft.md` / `skills-draft.cn.md` | Knowledge framework + interview outline |
| `readlist.md` | **No Chinese edition** — titles are already kept in their original published form with English descriptions |

The `.en` suffix is **not** used. Do not reintroduce it.

## Language convention

- Every note under `knowledge-graph/` is **English only**. Never write Chinese inside the vault.
- Source documents are bilingual, one-to-one.

## Vault structure

- `knowledge-graph/` is the Obsidian vault root — open *that* folder, not the project root.
- `00 MOC - Comms x Compute x AI Knowledge Graph.md` is the single entry point.
- Notes are numbered **`GG-x`** by domain group; the file name *is* the topic.
- Fixed note body shape: knowledge points → **Anchors** → **Related** → **References**; the big domain notes (01-5/02-7/06-3/04-4/04-5) all close with **References** (real books/PEPs/standards with ISBN/DOI/URL), because the user requires citations at the end of the article.
- Diagrams are **Mermaid** code blocks (render natively in Obsidian reading view); every note is expected to carry them in its structural sections (architecture, data path, timing, decision logic), not just in passing.
- Bulk renumbering recipe: two-phase `git mv` (old → `__tmp__` → final) to avoid filename collisions, then one regex pass with `(?<![\d\-])(\d{2})-(\d)(?!\d)` and a lookup dict — single pass avoids chained rewrites, and the lookbehind protects dates and version strings.

## Note numbering scheme `GG-x` (renumbered 2026-10-22)

Group number `GG` is **sequential from `01` and contiguous** — an earlier scheme
inherited numbers from each group's original top-level note and left gaps; that was
replaced on request. Group order follows the signal path outward:

| Group | Domain | Notes |
| --- | --- | --- |
| `01-x` | Cellular and mobile communications | 01-1 5G-A/6G radio access · 01-2 NR RAN L2 · 01-3 AI/ML for RAN and O-RAN · 01-4 cellular IoT (RedCap/eRedCap/NTN) · 01-5 NR random access (RACH) |
| `02-x` | WLAN | 02-1 generations · 02-2 power saving · 02-3 ecosystem (WFA/EasyMesh/prpl) · 02-4 TX/RX datapath and offload · 02-5 discovery, authentication and association · 02-6 roaming, healing and steering · 02-7 EasyMesh operation, tuning and troubleshooting |
| `03-x` | Low-power and sensor networking | 03-1 WSN and low-power MAC |
| `04-x` | Embedded and systems software | 04-1 RTOS and hardware interfaces · 04-2 Linux embedded · 04-3 software architecture · 04-4 Linux interrupts · 04-5 concurrency, processes, threads and IPC |
| `05-x` | Data plane and heterogeneous compute | 05-1 DPDK/UPF · 05-2 cloud-edge-end |
| `06-x` | Machine learning, AI inference and agent systems | 06-1 LLM inference/xLLM · 06-2 agent systems · 06-3 machine learning foundations (read first) |
| `07-x` | Silicon and ISA | 07-1 RISC-V |
| `08-x` | Programming languages and practice | 08-1 toolchain and performance · 08-2 C and C++ · 08-3 Python · 08-4 MATLAB/Simulink · 08-5 Verilog HDL |

`readlist.md` sections use the **same** `GG-x` numbers (sections 30–32 are the
standards repositories, reading order, and maintenance). Renumbering a note means
renumbering its readlist section too.

## Content conventions

- **Anchors** sections hold only checkable facts with a date or number (spec numbers, freeze dates, DOIs, release versions).
- Anything not independently confirmed is marked **`VERIFY`**, never asserted.
- `[[wikilinks]]` are deliberate — a link means the two concepts get argued about together in interviews.
- Source documents stay faithful to the original draft; **corrected facts live in the Anchors sections**, and the README §7 table records source-vs-verified discrepancies.
- Copyright line `Copyright (c) 2026 Washington Ruan. All rights reserved.` appears in frontmatter and footer of every file.
- Frontmatter: `title`, `lang`, `category`, `last-updated`, `copyright`, plus `sibling` for bilingual pairs and `version` for documents with revision history.

## Verification commands

Link and structure integrity is checkable with a Python pass that strips code
fences and code spans before matching (C++ attribute syntax such as
`[[nodiscard]]` and lambda parameter lists like `[](int a, int b)` are false
positives otherwise):

```python
import re, glob, os
# strip ``` fences and `code spans`, then match [[wikilinks]] and [](links)
```
