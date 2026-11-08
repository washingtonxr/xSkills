---
title: Reading list — SECURITY · Network and Systems Security
lang: en
category: reading-list
license: GPL-3.0-or-later OR AGPL-3.0-or-later
last-updated: 2026-11-08
---

# Reading list — SECURITY · Network and Systems Security

> Security as a chain rather than a checklist: the primitives and the constructions around them, the
> attacks that actually happen and the defences that actually work, the frameworks and regulations
> that decide what gets funded, and the three forces — AI, quantum computing and product regulation —
> that will reorder all of it before 2035.
>
> One section per note, numbered `GG-x`. Where a note needed no source beyond its own
> **References**, there is no section here — the note is self-sufficient.

## How to use this list

- **Marks.** Type and priority marks (`★★★`, `[Book]`, `[EN]`) are defined once, in the MOC under *Reading marks*. The rule that matters: `★★★` means read or skim before you quote the note.
- **Titles** are kept in their published form and never translated; descriptions are English.
- **Nothing is asserted.** Where a citation could not be confirmed against a publisher, RFC number, DOI or the issuing body, it is marked `VERIFY`.
- **Start here:** `12-1` if you need the substrate, `12-2` if you are defending a network next week, `12-3` if you have to justify a budget, `12-4` if you are planning beyond the current fiscal year. Reading order for an interview loop: 12-1 → 12-2 → 12-3 → 12-4.
- **RFCs are the cheapest primary source in the field.** They are free, authoritative, and they settle most arguments that blog posts prolong. Where an RFC has been obsoleted, read the current one — TLS 1.3 is the standing example (§12-1).
- **Not covered here:** 802.11-specific security is in [[readlist|WLAN/02-19]], and the applied-cryptography books below cover the mathematics in more depth than any note should.

---

## 12-1 · SECURITY — Cryptographic Foundations: Primitives, Protocols and Trust Anchors

The substrate. Everything else in this directory assumes it: what the primitives are, how the
constructions around them fail, and why the failures are almost never in the primitive.

### Read these first

- **[Book · ★★★ · EN]** Boneh, D., Shoup, V. *A Graduate Course in Applied Cryptography*, v0.6,
  2023 — <https://toc.cryptobook.us/>. Free, rigorous, and the single best return on time in the
  field. Chapters 5–7 (block ciphers, modes, AEAD), 10–12 (public key, RSA, discrete log) and 13
  (key exchange) cover §2–§6 of the note.
  - Read the security-definition sections even if you skip the proofs; the definitions are what let
    you say "this construction is broken" without hand-waving.
- **[Book · ★★★ · EN]** Ferguson, N., Schneier, B., Kohno, T. *Cryptography Engineering: Design
  Principles and Practical Applications*. Wiley, 2010. ISBN 978-0-470-47424-2.
  - The engineering counterpart: what breaks in implementations, how to manage keys, why protocol
    design is harder than primitive selection. §9 (key lifecycle) is built on it.
- **[Standard · ★★★ · EN]** National Institute of Standards and Technology. *FIPS 197 (AES)*,
  *FIPS 180-4 (SHA-2)*, *FIPS 202 (SHA-3)*, *SP 800-38D (GCM)*, *SP 800-56A/56B/56C (key
  establishment)*. <https://csrc.nist.gov/>.
  - Free, normative, and shorter than their reputation. Read SP 800-38D §8 if you want to know
    exactly what GCM's nonce requirements are rather than what a blog says they are.

### Protocols

- **[Standard · ★★★ · EN]** Rescorla, E. *The Transport Layer Security (TLS) Protocol Version 1.3*.
  **RFC 9846**, July 2026 (obsoletes RFC 8446, August 2018).
  - Read §4 (handshake), §7 (key schedule) and Appendix A. The key schedule diagram in §7.1 is the
    clearest explanation of HKDF-with-labels that exists.
- **[Standard · ★★★ · EN]** Kwiatkowski, K., Kampanakis, P., Westerbaan, B., Stebila, D.
  *Post-Quantum Traditional (PQ/T) Hybrid Key Agreement Mechanisms for TLS 1.3*. RFC 10024,
  August 2026.
  - Nine pages, and the source of every byte count in §6.2: 1216-byte client share, 1120-byte server
    share, 64-byte shared secret, code points 0x11EC / 0x11EB / 0x11ED.
- **[Standard · ★★ · EN]** Kaufman, C., et al. *Internet Key Exchange Protocol Version 2 (IKEv2)*.
  RFC 7296, October 2014. And *IPsec*: RFC 4301–4303.
- **[Standard · ★★ · EN]** Iyengar, J., Thomson, M. *QUIC: A UDP-Based Multiplexed and Secure
  Transport*. RFC 9000, and *Using TLS to Secure QUIC*. RFC 9001, May 2021.
- **[Paper · ★★ · EN]** Donenfeld, J. A. *WireGuard: Next Generation Kernel Network Tunnel*. NDSS
  2017.
  - The design argument for refusing cipher agility, which is exactly the decision that makes the PQC
    transition harder. Read it as a case study in trade-offs, not as a template.

### Post-quantum

- **[Standard · ★★★ · EN]** NIST. *FIPS 203 (ML-KEM)*, *FIPS 204 (ML-DSA)*, *FIPS 205 (SLH-DSA)*.
  13 August 2024.
- **[Standard · ★★★ · EN]** Moody, D., et al. *NIST IR 8547, Transition to Post-Quantum Cryptography
  Standards*. Initial public draft 12 November 2024; final October 2026.
  - The tables in §4.1 are the authoritative deprecation schedule: 112-bit deprecated after 2030,
    everything quantum-vulnerable disallowed after 2035.
- **[Doc · ★★★ · EN]** National Security Agency. *CNSA 2.0 FAQ* (PP-24-4014) and *Announcing the
  Commercial National Security Algorithm Suite 2.0*. 2022, updated May 2025.
  - The procurement ladder that arrives earlier than most vendors expect: new NSS acquisitions from
    1 January 2027.
- **[Doc · ★★ · EN]** European Commission / NIS Cooperation Group / ENISA. *Coordinated
  Implementation Roadmap for the Transition to Post-Quantum Cryptography*. 23 June 2025.
  - The EU dates (2026 roadmaps, 2030 high-risk, 2035 all) and the member-state coordination
    machinery behind them.
- **[Doc · ★★ · EN]** UK NCSC. *Timelines for migration to post-quantum cryptography*. 20 March 2025.

### Failures, as case studies

- **[Paper · ★★★ · EN]** Böck, H., Somorovsky, J., Young, C. *Return Of the Bleichenbacher's Oracle
  Threat (ROBOT)*. USENIX Security 2018. And Bleichenbacher, D. *Chosen Ciphertext Attacks Against
  Protocols Based on the RSA Encryption Standard PKCS #1*. CRYPTO 1998.
  - Nineteen years between the paper and the widespread rediscovery. Read them together; the lesson
    is about how long a known class survives in production code.
- **[Paper · ★★ · EN]** Bhargavan, K., Leurent, G., Mercier, C., et al. *ALPACA: Application Layer
  Protocol Confusion*. USENIX Security 2021.
- **[Doc · ★★ · EN]** Project Wycheproof, <https://github.com/C2SP/wycheproof>.
  - The edge-case corpus that finds what test vectors miss: invalid curve points, non-canonical
    encodings, ASN.1 quirks.

### Practice

- **[Code · ★★★ · EN]** OpenSSL 3.5+, BoringSSL, Go `crypto/tls`, `rustls` — release notes and the
  hybrid-group implementation.
  - The fastest way to confirm §6.2 is to run `openssl s_client -groups X25519MLKEM768` against a
    server that supports it and read the byte counts in a capture.
- **[Tool · ★★ · EN]** `openssl`, `tshark`, `testssl.sh`, `sslyze`.
  - §12 of the note is a checklist; these are the instruments that produce the evidence.

---

## 12-2 · SECURITY — Threats and Defences: Attack Surface, Detection and Incident Response

The adversary's side of the table: what they actually do, in what order, and which controls change the
outcome. Heavier on incident data than on theory, deliberately.

### Frameworks and threat intelligence

- **[Doc · ★★★ · EN]** MITRE. *ATT&CK Enterprise Matrix*, <https://attack.mitre.org/>.
  - Use the live matrix, not a saved copy: the 2025–2026 version has **15 tactics**, with Defense
    Evasion renamed **Stealth** and **Defense Impairment (TA0112)** added. Most study material still
    shows 14.
- **[Paper · ★★★ · EN]** Hutchins, E. M., Cloppert, M. J., Amin, R. M. *Intelligence-Driven Computer
  Network Defense Informed by Analysis of Adversary Campaigns and Intrusion Kill Chains*. 2011.
  - The original kill chain. Read it for the argument that intelligence should drive defence, then
    read ATT&CK for the operational version.
- **[Doc · ★★★ · EN]** Cloudflare. *2026 Cloudflare Threat Report* and *2025 Q4 DDoS Threat Report*.
  March 2026.
  - The numbers in §4: 31.4 Tbps, 14.1 Bpps, 47.1 M attacks in 2025, +121% year on year, and the
    statement that the record attack was mitigated without human intervention.
- **[Doc · ★★ · EN]** Verizon. *Data Breach Investigations Report*, 2025 and 2026 editions.
  - Treat the pattern percentages as directional and the incident narratives as the valuable part.
- **[Doc · ★★ · EN]** Microsoft. *Digital Defense Report 2025*; Google Threat Intelligence Group
  advisories on the 2025 SaaS/OAuth campaigns.

### The attack classes worth reading properly

- **[Paper · ★★★ · EN]** Kaminsky, D. *Black Ops 2008: It's the End of the Cache as We Know It*.
  Black Hat 2008.
  - The DNS cache-poisoning talk that forced source-port randomisation into every resolver. The
    mechanism is still the clearest example of a protocol designed without an adversary in the room.
- **[Doc · ★★★ · EN]** Cloudflare. *Inside the 31.4 Tbps attack* and the Aisuru/Kimwolf botnet
  analysis, Q4 2025 – Q1 2026.
  - Read for the architecture: consumer IoT devices, UDP carpet bombing, short duration, autonomous
    mitigation. The number is less instructive than the duration.
- **[Paper · ★★ · EN]** Antonakakis, M., et al. *Understanding the Mirai Botnet*. USENIX Security
  2017.
  - The canonical analysis of the botnet family that still underpins the 2025 records.
- **[Doc · ★★ · EN]** CISA. *Advisory AA23-144a: Vice Society* and the annual *Top Routinely
  Exploited Vulnerabilities* catalogue.
  - The list that justifies "patch internet-facing systems first" better than any maturity model.
- **[Doc · ★★ · EN]** Google Threat Intelligence Group. *UNC6040 / ShinyHunters Salesforce vishing
  campaign*, 2025.
  - The clearest public account of OAuth token theft as the primary access path in a SaaS estate.

### Detection engineering

- **[Doc · ★★★ · EN]** SigmaHQ. *Sigma* rule repository, <https://github.com/SigmaHQ/sigma>. And
  MITRE *ATT&CK Navigator* for coverage mapping.
  - The two artefacts that turn detection from an art into an engineering practice with version
    control and tests.
- **[Doc · ★★ · EN]** Zalewski, M. *The Tangled Web* (No Starch, 2011) — not about detection, and
  still the best explanation of why browser-side attacks work, which is where a large share of
  initial access now begins.
- **[Doc · ★★ · EN]** Bejtlich, R. *The Practice of Network Security Monitoring*. No Starch, 2013.
  ISBN 978-1-59327-509-9.
  - Dated in tooling, correct in method: full packet capture, session data, alert data, and the
    discipline of knowing what normal looks like.

### Response

- **[Standard · ★★★ · EN]** National Institute of Standards and Technology. *SP 800-61 Rev. 3,
  Incident Response Recommendations and Considerations for Cybersecurity Risk Management*. 2024.
  - Rev. 3 restructures IR as part of the CSF 2.0 lifecycle; the operational content is unchanged and
    still the best checklist.
- **[Standard · ★★ · EN]** RFC 3227. Brezinski, D., Killalea, T. *Guidelines for Evidence Collection
  and Archiving*. February 2002.
  - Two pages, and the only thing standing between an analyst and a destroyed memory image.
- **[Book · ★★ · EN]** Roberts, S., Brown, R. *Intelligence-Driven Incident Response*. O'Reilly,
  2017. ISBN 978-1-491-93694-4.

### Practice

- **[Doc · ★★★ · EN]** Atomic Red Team, <https://github.com/redcanaryco/atomic-red-team>, and
  MITRE CALDERA.
  - The only honest way to know whether a detection works is to run the technique and watch.
- **[Doc · ★★ · EN]** Zeek, Suricata, Velociraptor documentation.
  - Zeek for behaviour and protocol logs, Suricata for signature and anomaly detection, Velociraptor
    for endpoint triage at scale.

---

## 12-3 · SECURITY — Standards and Architecture: Risk, Controls, Compliance and Zero Trust

The management and architecture layer: how risk becomes a decision, how a decision becomes a control,
and how a control becomes evidence that survives an audit without becoming theatre.

### Risk

- **[Standard · ★★★ · EN]** Open Group. *Risk Analysis (O-RA), Version 2.0* (Open FAIR), 2018. And
  Freund, J., Jones, J. *Measuring and Managing Information Risk: A FAIR Approach*. Butterworth-
  Heinemann, 2014. ISBN 978-0-12-420231-3.
  - The worked example in §1.2 is this method. Read the book for the calibration technique, which is
    where most FAIR programmes fail.
- **[Standard · ★★★ · EN]** NIST. *SP 800-30 Rev. 1, Guide for Conducting Risk Assessments*.
  September 2012.
- **[Standard · ★★ · EN]** ISO 31000:2018, *Risk management — Guidelines*. And ISO/IEC 27005:2022
  for the information-security-specific application.

### Control catalogues

- **[Standard · ★★★ · EN]** NIST. *The NIST Cybersecurity Framework (CSF) 2.0*. CSWP 29,
  26 February 2024.
  - Six Functions, 22 Categories, 106 Subcategories. The Govern Function is the political change;
    read it first if you need to persuade a board.
- **[Standard · ★★★ · EN]** NIST. *SP 800-53 Rev. 5* (September 2020, Release 5.2.0 August 2025) and
  *SP 800-53B* baselines.
  - The catalogue everything else maps to. Do not read it end to end; read the families your risk
    register points at.
- **[Standard · ★★★ · EN]** ISO/IEC 27001:2022 and 27002:2022.
  - Clauses 4–10 are the certifiable part; Annex A is a menu of 93. The Statement of Applicability is
    the document auditors actually test.
- **[Standard · ★★★ · EN]** Center for Internet Security. *CIS Critical Security Controls v8.1*.
  June 2024. And the *CIS Benchmarks*.
  - The prioritisation layer, and the only major framework that tells you what to do first.
- **[Standard · ★★ · EN]** IEC 62443-3-3, -4-1, -4-2. — Zones and conduits, Security Levels SL1–SL4.
  Read this before proposing an IT security model to an OT team.

### Zero trust and architecture

- **[Standard · ★★★ · EN]** NIST. *SP 800-207, Zero Trust Architecture*. August 2020.
  - Seven tenets, PDP/PEP, three deployment approaches. Twenty-three pages and still the only
    vendor-neutral definition.
- **[Standard · ★★★ · EN]** CISA. *Zero Trust Maturity Model, Version 2.0*. April 2023.
  - Five pillars, three cross-cutting capabilities, four stages. Use it to sequence, not to score.
- **[Doc · ★★ · EN]** OMB. *M-22-09, Federal Zero Trust Strategy*. 26 January 2022.
  - The clearest example of a zero trust programme with dates and an owner.
- **[Doc · ★★ · EN]** NIST. *SP 1800-35, Implementing a Zero Trust Architecture*. Final June 2025.
  - Nineteen worked builds. The most useful part is what each one cost and what it did not solve.

### Regulation and audit

- **[Standard · ★★★ · EN]** Regulation (EU) 2024/2847 (Cyber Resilience Act); Regulation (EU)
  2022/2554 (DORA); Directive (EU) 2022/2555 (NIS2); Regulation (EU) 2024/1689 (AI Act).
  - Read the article that sets the date, not the recitals. Article 71 of the CRA and Article 113 of
    the AI Act are where the timelines live.
- **[Standard · ★★ · EN]** PCI Security Standards Council. *PCI DSS v4.0.1*. 11 June 2024.
- **[Standard · ★★ · EN]** AICPA. *Trust Services Criteria*. 2017, revised 2022.
  - Read the Type I versus Type II distinction before you accept a vendor's SOC 2 report as evidence.
- **[Standard · ★★ · EN]** GB/T 22239-2019, *Baseline for classified protection of cybersecurity*
  (MLPS 2.0), with the Cybersecurity Law, Data Security Law and Personal Information Protection Law.

### Governance and metrics

- **[Doc · ★★ · EN]** Institute of Internal Auditors. *The IIA's Three Lines Model*. July 2020.
  - Short, and the vocabulary every audit committee already uses.
- **[Book · ★★ · EN]** Hubbard, D. W., Seiersen, R. *How to Measure Anything in Cybersecurity Risk*.
  Wiley, 2nd ed. 2023. ISBN 978-1-119-79130-4.
  - The antidote to vanity metrics; read it alongside the FAIR material.

---

## 12-4 · SECURITY — The Frontier: AI-Native Threats, Post-Quantum Migration and the Next Decade

The forecast section, and therefore the one most likely to age. Read it for the structure of the
argument — three forces interacting — rather than for any individual prediction.

### AI security

- **[Doc · ★★★ · EN]** OWASP GenAI Security Project. *OWASP Top 10 for LLM Applications 2025*,
  <https://genai.owasp.org/llm-top-10/>.
  - The 2025 list, not the 2023 one. LLM01 prompt injection, LLM06 excessive agency and LLM03 supply
    chain are the three that change architecture.
- **[Doc · ★★★ · EN]** OWASP. *Top 10 for Agentic Applications*, December 2025 (labelled 2026),
  ASI01–ASI10.
  - The list that covers actions rather than outputs. Read it with the LLM list, not instead of it.
- **[Paper · ★★★ · EN]** Greshake, K., Abdelnabi, S., Mishra, S., Endres, C., Holz, T., Fritz, M.
  *Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect
  Prompt Injection*. AISec 2023.
  - The paper that established indirect injection as a structural problem rather than a bug.
- **[Doc · ★★ · EN]** Willison, S. *The lethal trifecta for AI agents*, 2025.
  - Private data + untrusted content + outbound communication. The most useful single heuristic in
    the field, and the basis of §2.3.
- **[Standard · ★★ · EN]** NIST. *AI Risk Management Framework (AI 100-1)*, January 2023, and
  *Generative AI Profile (AI 600-1)*, July 2024. ISO/IEC 42001:2023 for the management system.
- **[Doc · ★★ · EN]** Model Context Protocol specification, <https://modelcontextprotocol.io/>.
  - Read the security considerations section and then ask who approves a server in your organisation.

### Adversarial ML and model confidentiality

- **[Paper · ★★★ · EN]** Szegedy, C., et al. *Intriguing properties of neural networks*.
  arXiv:1312.6199, 2013.
  - The origin of adversarial examples, and still the clearest statement that a classifier's decision
    boundary is not a security boundary.
- **[Paper · ★★ · EN]** Carlini, N., et al. *Extracting Training Data from Large Language Models*.
  USENIX Security 2021. And Shokri, R., et al. *Membership Inference Attacks Against Machine Learning
  Models*. IEEE S&P 2017.
- **[Paper · ★★ · EN]** Tramèr, F., et al. *Stealing Machine Learning Models via Prediction APIs*.
  USENIX Security 2016.

### Post-quantum, programme view

- **[Standard · ★★★ · EN]** NIST IR 8547 (final, October 2026) and the FIPS 203/204/205 texts.
- **[Doc · ★★★ · EN]** NSA CNSA 2.0 FAQ; EU coordinated roadmap (June 2025); UK NCSC timelines
  (March 2025).
  - Three authorities, three schedules, one direction. The differences between them are the useful
    part — they tell you which deadline is real for your market.
- **[Standard · ★★ · EN]** RFC 10024. — The implementation-level detail: share sizes, code points,
  and the FIPS ordering rationale for which half of the hybrid must be certified.
- **[Doc · ★★ · EN]** NSA. *Quantum Key Distribution (QKD) and Quantum Cryptography (QC)* FAQ, 2020.
  - The argument in §6.5, from the agency that buys the most cryptography.

### Confidential computing and platform trust

- **[Paper · ★★★ · EN]** Costan, V., Devadas, S. *Intel SGX Explained*. IACR ePrint 2016/086.
  - Long, and the only complete description of what an enclave actually guarantees.
- **[Paper · ★★ · EN]** Van Bulck, J., et al. *Foreshadow*. USENIX Security 2018; Murdock, K., et al.
  *Plundervolt*. IEEE S&P 2020; Borrello, P., et al. *ÆPIC Leak*. USENIX Security 2022.
  - Read as a sequence: each generation's fix moved the attack, it did not end it.

### Resilience and the regulatory direction

- **[Standard · ★★ · EN]** ISO 22301:2019, *Business continuity management systems*. And NIST
  *SP 800-34 Rev. 1*, *Contingency Planning Guide*.
- **[Doc · ★★ · EN]** UK Department for Science, Innovation and Technology. *Code of Practice for
  the Security of Software Suppliers* and the *Cyber Security Breaches Survey* (annual).
  - The policy direction that the CRA formalised, stated before it was law.
- **[Doc · ★★ · EN]** FTC. *The Cyber Trust Mark* programme materials, 2025–2026.
  - The US consumer-labelling counterpart to the EU's CE marking for products with digital elements.

---

## Standards and repositories

- **IETF** — <https://datatracker.ietf.org/>. TLS, QUIC, IPsec, SSH, PKIX, and the RFC 10024 hybrid
  groups. The datatracker page for a working group is a better history than any summary.
- **NIST CSRC** — <https://csrc.nist.gov/>. FIPS, SP 800 series, CSF, PQC project, CMVP.
- **ENISA** — <https://www.enisa.europa.eu/>. Threat landscape, certification schemes, NIS2 guidance.
- **CISA** — <https://www.cisa.gov/>. Advisories, KEV catalogue, Zero Trust Maturity Model.
- **MITRE** — <https://attack.mitre.org/>, <https://cwe.mitre.org/>, <https://cve.mitre.org/>.
- **OWASP** — <https://owasp.org/>, and the GenAI project at <https://genai.owasp.org/>.
- **ISO/IEC JTC 1/SC 27** — <https://www.iso.org/committee/45306.html>. 27000 family, 62443 is IEC TC 65.
- **IACR ePrint** — <https://eprint.iacr.org/>. Where the attacks appear before the conferences.

---

_Copyright (c) 2026 Washington Ruan and contributors · licensed under **GPL-3.0-or-later** or **AGPL-3.0-or-later**, at your option · see `LICENSE` and `LICENSE-AGPL`._
