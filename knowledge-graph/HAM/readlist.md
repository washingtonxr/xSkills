---
title: Reading list — HAM · Amateur Radio
lang: en
category: reading-list
license: GPL-3.0-or-later OR AGPL-3.0-or-later
last-updated: 2026-11-08
---

# Reading list — HAM · Amateur Radio

> Amateur radio as a service and as a practice: the treaty definition and the century of negotiation
> behind it, the three bodies that govern it, the spectrum it occupies, and then the method — the link
> budget, the propagation mechanisms, the antenna and feedline arithmetic, the mode catalogue, and the
> conventions of a contact.
>
> One section per note, numbered `GG-x`. Where a note needed no source beyond its own
> **References**, there is no section here — the note is self-sufficient.

## How to use this list

- **Marks.** Type and priority marks (`★★★`, `[Book]`, `[EN]`) are defined once, in the MOC under *Reading marks*. The rule that matters: `★★★` means read or skim before you quote the note.
- **Titles** are kept in their published form and never translated; descriptions are English.
- **Nothing is asserted.** Where a citation could not be confirmed against a publisher, DOI or the issuing body, it is marked `VERIFY`.
- **Start here:** `11-1` first if the institution is unfamiliar — the history explains why the bands are where they are. Then `11-2`, which is the one you will actually use at the bench.
- **The regulator is a primary source.** ITU Radio Regulations Article 25, 47 CFR Part 97 and MIIT Order No. 67 are short, free, and settle most arguments that secondary sources prolong.
- **Not covered here:** the antenna modelling and RF design texts overlap heavily with `WLAN/02-15`; that note's section covers the transceiver side and is not duplicated here.

---

## 11-1 · HAM — Amateur Radio: History, Regulation and the State of the Hobby

### Books

- **[Book · EN · ★★★]** *Ham Radio's Technical Culture* — Kristen Haring · MIT Press, 2007
  - The only serious academic history of the hobby as a *culture*: how American amateurs built an identity around technical competence, why "the experimenter" was a moral category, and how that identity shaped who joined and who left. Read it to understand why the hobby argues about FT8 the way it does — the same argument happened about SSB in 1950.
- **[Book · EN · ★★]** *The Continuous Wave: Technology and American Radio, 1900–1932* — Hugh G. J. Aitken · Princeton University Press, 1985
  - The technical and economic history of the transition from spark to continuous wave, including the amateurs' role in proving shortwave. Dense, and the best account of why the 1912 settlement collapsed.
- **[Book · EN · ★★]** *The Invisible Weapon: Telecommunications and International Politics, 1851–1945* — Daniel R. Headrick · Oxford University Press, 1991
  - Puts spectrum allocation in its geopolitical frame: every amateur band is the residue of a treaty negotiation between states and commercial interests. Explains the WARC process better than any amateur publication.
- **[Book · EN · ★]** *Empire of the Air: The Men Who Made Radio* — Tom Lewis · HarperCollins, 1991
  - De Forest, Armstrong and Sarnoff, and the amateur milieu they came out of. Useful background for the 1920s, and for understanding how an amateur technique becomes an industry.
- **[Book · EN · ★]** *Signor Marconi's Magic Box* — Gavin Weightman · HarperCollins, 2003
  - The 1901 transatlantic story told as narrative history. Read for the engineering constraints — coherers, kites, aerials — not for analysis.

### Standards and regulation

- **[Standard · EN · ★★★]** *Radio Regulations*, Articles 1 and 25, and Appendix 4 — International Telecommunication Union, 2020 edition with the WRC-19 Final Acts
  - Nos. 1.56 and 1.57 define the amateur and amateur-satellite services; Article 25 sets the operating obligations every national code copies. Six pages that overrule every secondary source.
- **[Standard · EN · ★★★]** *47 CFR Part 97* — Federal Communications Commission, current eCFR
  - The US amateur service rules in full: §97.301 band edges, §97.303 sharing, §97.305 emission types, §97.307 technical standards, §97.501–97.507 examinations.
- **[Standard · CN · ★★★]** 《业余无线电台管理办法》(工业和信息化部令第67号) — 中华人民共和国工业和信息化部, 2024年1月18日公布, 2024年3月1日施行
  - The current Chinese framework: A/B/C classes, power limits per class and band, licence term, log retention, identification interval. Free to download from gov.cn and the primary source for §8.2.

### Papers and institutional documents

- **[Paper · EN · ★★★]** "The FT4 and FT8 Communication Protocols" — S. Franke (K9AN), B. Somerville (G4WJS), J. Taylor (K1JT) · *QEX*, July/August 2020
  - The protocol paper: message compression, LDPC(174,91), Costas arrays, the −21 dB threshold and the reason a 50 Hz signal can be copied 20 dB below the noise. The single best example in the hobby of a design constrained by an information budget.
- **[Doc · EN · ★★★]** *FCC License Counts* and the ARRL licence-class reports — ARRL, updated monthly
  - The primary series behind every "is ham radio dying" claim: total licences, class split, and the month-to-month deltas. Cite this rather than a blog's interpretation of it.
- **[Doc · EN · ★★]** "FCC Allocates 60-Meter World-Wide Amateur Band Approved at WRC-15" — ARRL News, 11 December 2025
  - The 5351.5–5366.5 kHz allocation, 9.15 W ERP, 2.8 kHz bandwidth and the four retained channels. The clearest example of a fifteen-year gap between a WRC decision and a national rule.
- **[Doc · EN · ★★]** *Report and Order and Further Notice of Proposed Rulemaking*, FCC 23-93, WT Docket 16-239 — FCC, adopted 13 November 2023
  - The end of the HF symbol-rate limit and its replacement by a 2.8 kHz bandwidth limit. Read it for the reasoning about why a baud limit became meaningless once modems became DSP.
- **[Doc · EN · ★★]** "OSCAR I and Amateur Radio Satellites: Celebrating 50 Years" — ARRL, 2011
  - The primary account of the 1961 spacecraft: 140 mW, 144.983 MHz, 22 days, $68. Also the best short case study in how a launch opportunity, not a budget, is the scarce resource.
- **[Doc · EN · ★]** "Amateur Radio by the Numbers: Demographics, Trends, and the Future of the Hobby" — OERadio, 2026
  - A compiled series of US licence counts from 2005 to April 2026, the class split, ARRL market share and the available age data. Secondary, but the only place the long series is tabulated in one view.

---

## 11-2 · HAM — Operating Practice: Station, Propagation, Modes and the QSO

### Books

- **[Book · EN · ★★★]** *The ARRL Handbook for Radio Communications*, 2025 edition — ARRL
  - The reference. Everything from Ohm's law to a complete station design, with the measured tables that this note's budgets draw on. The 2025 edition is the one to buy; older editions are fine for everything except the digital chapters.
- **[Book · EN · ★★★]** *The ARRL Antenna Book*, 25th edition — ARRL, 2022
  - Dipoles, verticals, Yagis, feedlines, matching, radial systems and the measured efficiency data in §5. The chapters on ground systems and common-mode chokes are the ones worth reading twice.
- **[Book · EN · ★★★]** *Low-Band DXing*, 5th edition — John Devoldere (ON4UN) · ARRL, 2010
  - The definitive treatment of 160/80/40 m: vertical efficiency versus radial count, ground loss, receiving antennas, and why a low-band station is an antenna-farm problem rather than a power problem.
- **[Book · EN · ★★]** *The ARRL Operating Manual*, 12th edition — ARRL
  - QSO structure, RST, Q-signals, pile-up and split technique, band plans, awards and the contest calendar. The social protocol of the hobby, written down.
- **[Book · EN · ★★]** *Antenna Theory: Analysis and Design*, 4th edition — Constantine A. Balanis · Wiley, 2016
  - The theory behind the rules of thumb: reciprocity, pattern multiplication, the array factor, and why boom length determines Yagi gain. Read the chapters on dipoles and arrays, not the whole book.
- **[Book · EN · ★★]** *Experimental Methods in RF Design* — Wes Hayward (W7ZOI), Rick Campbell (KK7B), Bob Larkin (W7PUA) · ARRL, 2003
  - How to measure and build RF circuits rather than simulate them: front-end dynamic range, mixers, filters, and the measurement technique that makes a homebrew receiver work. The antidote to software-only intuition.
- **[Book · EN · ★★]** *The Electronics of Radio* — David B. Rutledge · Cambridge University Press, 1999
  - A one-semester course built around a complete 40 m transceiver, with the mathematics at each stage. The best single book for someone who wants to understand a radio rather than operate one.
- **[Book · EN · ★]** *RF Circuit Design*, 2nd edition — Christopher Bowick · Newnes, 2008
  - Impedance matching, Smith charts, resonators, and the practical component selection that a tuner and a filter design require.

### Standards and technical recommendations

- **[Standard · EN · ★★★]** *Recommendation ITU-R P.525*, Calculation of free-space attenuation — ITU
  - The path-loss formula in §2, in its normative form, including the unit conventions that most amateur texts get slightly wrong.
- **[Standard · EN · ★★★]** *Recommendation ITU-R P.372*, Radio noise — ITU
  - The man-made and atmospheric noise model behind §3.1: why the HF noise floor in a city is tens of dB above thermal, and how the curve varies with frequency and business type.
- **[Standard · EN · ★★]** *47 CFR §1.1310* and *OET Bulletin 65* — FCC
  - The maximum permissible exposure table and the power-density calculation method used in §12.1. Short, and the only authority that matters for a US station.

### Documentation and code

- **[Doc · EN · ★★★]** *WSJT-X User Guide* — J. Taylor (K1JT) and the WSJT Development Group
  - The operating manual for FT8, FT4, WSPR and MSK144, including the clock-accuracy requirement, the audio-level procedure and the "Fox/Hound" DXpedition mode. Free, and more precise than any tutorial.
- **[Doc · EN · ★★]** *ADIF Specification*, version 3.1.4 — ADIF development group
  - The interchange format in §9. Worth reading once because it explains why every logger can talk to every other logger, and why Cabrillo exists separately for contests.
- **[Doc · EN · ★★]** *Winlink Global Radio Email* system documentation — Winlink Development Team
  - VARA and PACTOR bandwidths, the ICS-213 workflow, and the gateway model that makes HF email work without an internet connection.
- **[Doc · EN · ★]** *NanoVNA User Guide* and the NanoVNA firmware documentation
  - The instrument that turned antenna work into measurement. Read the calibration section before the first sweep, or every reading will be wrong in the same way.
- **[Doc · EN · ★]** *AMSAT Satellite Handbook* — AMSAT
  - Transponder types, Doppler correction, pass prediction and the operating conventions for linear satellites and QO-100.

---

## A short reading order

| If you have | Read |
| --- | --- |
| **An evening** | `11-1` §1 (the definition), §8 (licence classes), §10 (the numbers) — then `11-2` §1 (the budget) and §2 (decibels) |
| **A weekend** | `11-1` end to end, then `11-2` §4 (propagation) and §5 (antennas) |
| **A month** | Both notes, plus the ARRL *Handbook* chapters on receivers and transmission lines, and *Low-Band DXing* §1–§3 if the low bands are the goal |
| **Before building anything** | `11-2` §5 and §6, the *Antenna Book* on radial systems, and ITU-R P.372 — in that order |

The one habit that separates operators who improve from operators who accumulate equipment: **measure
before and after every change**. A NanoVNA sweep and a logged noise floor turn a hobby into a series
of experiments, which is what the service was created to support in the first place.
