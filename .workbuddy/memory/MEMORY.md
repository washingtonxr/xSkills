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
- Notes are numbered `01`–`16`; the file name *is* the topic.
- Fixed note body shape: knowledge points → **Anchors** → **Related**.

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
