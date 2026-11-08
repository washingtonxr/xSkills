# Project: 261022,PersonalSkills — long-term conventions

Personal knowledge base for interview preparation at the intersection of
**communications technology x heterogeneous compute x AI**. Owner: Washington Ruan.

## Language and file naming

- Every note under `knowledge-graph/` is **English only**; Chinese appears only in `README.md`,
  `other/*.cn.md`, and quoted source titles inside readlists.
- English is the default filename; Chinese variants carry `.cn`. `.en` is **not** used.
- `README.md` is **one file, Chinese then English** (no `README.cn.md`).
- `other/background[.cn].md`, `other/skills-draft[.cn].md`.
- `knowledge-graph/<DIR>/readlist.md` — **one per directory** (root readlist split 2026-10-29).
- Note filename: `GG-x DOMAIN - Topic - Scope.md` — ASCII hyphens, no slashes, no em dashes.
  Frontmatter `title:` mirrors it as `"DOMAIN — Topic: Scope"` (em dash, then colon).
  Required frontmatter keys: `title`, `type`, `domain`, `group`, `series`, `tags`, `aliases`,
  `license`, `last-updated`. Renaming a note = rewriting every wikilink + MOC + README + readlist
  + memory in one scripted pass.

## Vault structure

- `knowledge-graph/` is the Obsidian vault root — open *that* folder, not the project root.
- `00 MOC - Comms x Compute x AI Knowledge Graph.md` is the single entry point (directory map,
  reading/memory method, contribution method, maintenance triggers, staleness table).
- One folder per domain: `MN/ WLAN/ WSN/ EMBEDDED/ DATAPLANE/ AI/ SILICON/ LANGUAGES/
  MANAGEMENT/ BUSINESS/ HAM/ SECURITY/`. Obsidian resolves wikilinks by note name, so moving a
  note between folders does not break links. `SECURITY` is the one cross-cutting directory — it
  links out to WLAN 02-19, MN, EMBEDDED and DATAPLANE rather than duplicating them.
- `99 Corrections - Verified Facts That Popular Sources Get Wrong.md` — source-vs-verified
  discrepancies; a new note that corrects a popular claim adds rows there.

## Note numbering `GG-x` (sequential from 01, contiguous; `GG` is also the folder)

| Group | Folder | Notes |
| --- | --- | --- |
| `01-x` | `MN` | 01-1 5G-A/6G · 01-2 NR RAN L2 · 01-3 AI/ML for RAN and O-RAN · 01-4 cellular IoT · 01-5 NR RACH · 01-6 NR DU MAC scheduler · 01-7 NR HARQ vs LTE · 01-8 OpenAirInterface |
| `02-x` | `WLAN` | 02-1 generations Wi-Fi 4→8 · 02-2 power saving · 02-3 ecosystem and WFA certification · 02-4 TX/RX datapath · 02-5 discovery/auth/association · 02-6 roaming and steering · 02-7 EasyMesh operation · 02-8 scheduling/EDCA/OFDMA · 02-9 TSN · 02-10 baseband and driver · 02-11 OpenWrt · 02-12 openwifi · 02-13 reliability and determinism · 02-14 fundamentals · 02-15 transceiver and AI-native radio · 02-16 RRM · 02-17 DFS · 02-18 AI in Wi-Fi and 802.11bx WIN · 02-19 security (RSNA, WPA3, mesh, threat horizon) |
| `03-x` | `WSN` | 03-1 WSN and low-power MAC |
| `04-x` | `EMBEDDED` | 04-1 RTOS/interfaces · 04-2 Linux embedded · 04-3 software architecture · 04-4 interrupts · 04-5 concurrency and IPC · 04-6 device drivers |
| `05-x` | `DATAPLANE` | 05-1 DPDK/UPF · 05-2 cloud-edge-end |
| `06-x` | `AI` | 06-1 LLM inference/xLLM · 06-2 agent systems · 06-3 ML foundations |
| `07-x` | `SILICON` | 07-1 RISC-V |
| `08-x` | `LANGUAGES` | 08-1 toolchain/performance · 08-2 C/C++ · 08-3 Python · 08-4 MATLAB/Simulink · 08-5 Verilog |
| `09-x` | `MANAGEMENT` | 09-1 engineering project management |
| `10-x` | `BUSINESS` | 10-1 value-driven business model |
| `11-x` | `HAM` | 11-1 amateur radio history/regulation · 11-2 operating practice |
| `12-x` | `SECURITY` | 12-1 cryptographic foundations (primitives, protocols, trust anchors) · 12-2 threats and defences (attack surface, detection, IR) · 12-3 standards and architecture (risk, controls, compliance, zero trust) · 12-4 the frontier (AI-native threats, PQC migration) |

Per-note detail is *not* duplicated here — it lives in each note's title, its directory
`readlist.md`, and the MOC table row. Renumbering a note means renumbering its readlist
section and its MOC row.

## Content conventions

- Body shape: knowledge points → **Anchors** → **Related** → **References**; every substantial
  note closes with real citations (book ISBN, DOI, RFC/PEP/standard number, URL).
- **Anchors** hold only checkable facts with a date or number (spec numbers, freeze dates, DOIs,
  release versions). Anything unconfirmed is marked **`VERIFY`**, never asserted.
- **Verify procedural claims against the clause, not secondary sources.** Blog sources repeat
  errors verbatim (e.g. "RACH contention-resolution losers do not ramp power" — TS 38.321
  §5.1.3 says they do). Re-check the clause before restating a claim.
- `[[wikilinks]]` are deliberate — a link means the two concepts get argued about together.
- Structural diagrams are **Mermaid** blocks, present in architecture / data path / timing /
  decision-logic sections. An "architecture, who does what" view is a `sequenceDiagram` with the
  layers as participants, not a flowchart of boxes.
- Licensing (2026-10-29): **GPL-3.0-or-later OR AGPL-3.0-or-later**, dual. Frontmatter carries
  `license: GPL-3.0-or-later OR AGPL-3.0-or-later`; footer is one italic line:
  `_Copyright (c) 2026 Washington Ruan and contributors · licensed under **GPL-3.0-or-later** or
  **AGPL-3.0-or-later**, at your option · see \`LICENSE\` and \`LICENSE-AGPL\`._`
  Texts: `LICENSE` (GPLv3), `LICENSE-AGPL` (AGPLv3). No "All rights reserved" anywhere.
- Bulk renumbering recipe: two-phase `git mv` (old → `__tmp__` → final), then one regex pass with
  `(?<![\d\-])(\d{2})-(\d)(?!\d)` plus a lookup dict (single pass avoids chained rewrites; the
  lookbehind protects dates and version strings).

## Verification commands

```bash
node "C:/Users/Avenger/.workbuddy/binaries/node/workspace/mval.mjs"   # all Mermaid blocks
```

- Mermaid render test: `mermaid` + `jsdom` from the node workspace; jsdom needs `getBBox`,
  `getComputedTextLength`, `getScreenCTM` and `CSSStyleSheet` stubs or every diagram falsely fails.
- Python passes: strip ``` fences and `code spans` before matching wikilinks (C++ `[[nodiscard]]`
  and lambda `[](int a, int b)` are false positives); check table column counts, CJK chars, single
  trailing newline.
- Verify facts with WebSearch/WebFetch against primary sources (IEEE 802.11 draft text, eCFR, ETSI,
  WFA, vendor docs) — never from memory.

## Workflow rules

- **Ask before `git commit`.** Stage nothing that was not asked for; suggest a commit message.
- On finishing a note: ripple to `00 MOC` (count, map node, table row, read order), `README.md`
  (both languages: counts, tree, directory table, role table), the directory `readlist.md` (new
  `## GG-x` section with annotated sources), `99 Corrections`, `MEMORY.md`, and today's
  `.workbuddy/memory/YYYY-MM-DD.md` log (append-only).
- Daily logs older than 30 days get distilled into this file by topic, then deleted.
