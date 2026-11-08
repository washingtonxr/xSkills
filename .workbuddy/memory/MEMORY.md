# Project: 261022,PersonalSkills — long-term conventions

Personal knowledge base for interview preparation at the intersection of **communications x heterogeneous
compute x AI**. Owner: Washington Ruan.

## Naming and language

- `knowledge-graph/` notes are **English only**; Chinese only in `README.md` (one file, zh then en),
  `other/*.cn.md`, and quoted source titles in readlists. `.cn` variants exist, `.en` never does.
- `knowledge-graph/<DIR>/readlist.md` — one per directory.
- Note file `GG-x DOMAIN - Topic - Scope.md` (ASCII hyphens); frontmatter `title:` mirrors it as
  `"DOMAIN — Topic: Scope"` (em dash, then colon), plus type/domain/group/series/tags/aliases/license.
- Renaming a note = one scripted pass over every wikilink + MOC + README + readlist + memory.

## Vault

- Root is `knowledge-graph/`; entry point `00 MOC - ...` (map, reading method, maintenance, staleness).
- Folders: `MN WLAN WSN EMBEDDED DATAPLANE AI SILICON LANGUAGES MANAGEMENT BUSINESS HAM SECURITY`. Links
  resolve by note name, so moving between folders is safe. `SECURITY` is the cross-cutting one.
- `99 Corrections - ...` records source-vs-verified discrepancies; new corrections add rows there.

## Numbering `GG-x` (contiguous from 01; `GG` is the folder)

| GG | Folder | Notes |
| --- | --- | --- |
| 01 | MN | 5G-A/6G · RAN L2 · AI/ML RAN · cellular IoT · RACH · MAC scheduler · HARQ · OAI |
| 02 | WLAN | generations · power · ecosystem · datapath · join · roaming · EasyMesh ops · scheduling · TSN · baseband · OpenWrt · openwifi · determinism · fundamentals · transceiver · RRM · DFS · AI/802.11bx · security ladder |
| 03 | WSN | WSN and low-power MAC |
| 04 | EMBEDDED | RTOS · Linux · architecture · interrupts · concurrency · drivers |
| 05 | DATAPLANE | DPDK/UPF · cloud-edge-end |
| 06 | AI | LLM inference · agents · ML foundations |
| 07 | SILICON | RISC-V |
| 08 | LANGUAGES | toolchain · C/C++ · Python · MATLAB · Verilog |
| 09 | MANAGEMENT | project management |
| 10 | BUSINESS | business model |
| 11 | HAM | history/regulation · operating |
| 12 | SECURITY | crypto · threats and IR · standards and zero trust · frontier |

Per-note detail lives in the note title, its readlist section and its MOC row — not duplicated here.

## Content

- Body: knowledge points → **Anchors** → **Related** → **References** (real ISBN/DOI/RFC/URL).
- Anchors = checkable facts with a date or number; anything unconfirmed is **`VERIFY`**, never asserted.
- Verify procedural claims against the clause, not secondary sources — blogs repeat each other verbatim.
- `[[wikilinks]]` are deliberate: a link means the two ideas get argued about together.
- Diagrams are **Mermaid**, in architecture / data path / timing / decision sections. A "who does what"
  view is a `sequenceDiagram` with layers as participants, not a flowchart of boxes.
- Long notes may be a **ladder**: a question→section table up front, each section answering what the
  previous one raised (02-19 is the reference).
- Licence **GPL-3.0-or-later OR AGPL-3.0-or-later**; one italic footer line, no "All rights reserved".
- Renumbering: two-phase `git mv` (old → `__tmp__` → final), then one regex pass
  `(?<![\d\-])(\d{2})-(\d)(?!\d)` with a lookup dict — single pass avoids chained rewrites.

## Verification

- `node "C:/Users/Avenger/.workbuddy/binaries/node/workspace/mval.mjs"` parses every mermaid block, and
  only parses. To render, use `mermaid.render` under jsdom (stub `getBBox`, `getComputedTextLength`,
  `getScreenCTM`, `CSSStyleSheet.insertRule`), run from that workspace directory.
- Python passes: strip fences and code spans (C++ `[[nodiscard]]` is a false positive), then wikilinks,
  per-table column counts, CJK, trailing newline.
- Facts come from primary sources (IEEE draft, eCFR, ETSI, WFA, vendor docs), never from memory.

## Workflow

- **Ask before `git commit`**; stage nothing that was not asked for, suggest a message.
- Finishing a note ripples to MOC (count, map, table row, read order), README (both languages),
  the readlist, `99 Corrections`, this file, and today's log.
- Daily logs are append-only; older than 30 days get distilled here by topic, then deleted.
