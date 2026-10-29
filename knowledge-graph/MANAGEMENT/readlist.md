---
title: Reading list — MANAGEMENT · Engineering project management
lang: en
category: reading-list
license: GPL-3.0-or-later OR AGPL-3.0-or-later
last-updated: 2026-10-29
---

# Reading list — MANAGEMENT · Engineering project management

> The discipline that decides which technical work gets attempted, in what order, with whose time, and when it is stopped: methodology, lifecycle, planning, risk, governance and the practice of organisations that ship.
>
> One section per note, numbered `GG-x`. Where a note needed no source beyond its own
> **References**, there is no section here — the note is self-sufficient.

## How to use this list

- **Marks.** Type and priority marks (`★★★`, `[Book]`, `[EN]`) are defined once, in the MOC under *Reading marks*. The rule that matters: `★★★` means read or skim before you quote the note in an interview.
- **Titles** are kept in their published form and never translated; descriptions are English.
- **Nothing is asserted.** Where a citation could not be confirmed against a publisher, DOI, arXiv record or the issuing body, it is marked `VERIFY`.

---

## 09-1 · Engineering Project Management — methodology, lifecycle, tools and best practice
### The evidence base

- **[Book · ★★★ · EN]** Flyvbjerg, B. and Gardner, D. *How Big Things Get Done: The Surprising Factors That Determine the Fate of Every Project, from Home Renovations to Space Exploration and Everything in Between*. Crown Currency, 2023 · ISBN 978-0-593-23450-4
  - The 16,000-project database behind 47.9% on budget, 8.5% on budget and on time, and 0.5% on all three. Reference class forecasting, modularity, "think slow, act fast", and Pixar as the worked example of slow planning and fast delivery. Read this before quoting any project statistic.
- **[Paper · ★★★ · EN]** Flyvbjerg, B., Holm, M. S. and Buhl, S. "Underestimating Costs in Public Works Projects: Error or Lie?" *Journal of the American Planning Association* 68(3), 2002.
  - The distinction that changes the fix: optimism bias and strategic misrepresentation are different failures, and no estimation technique repairs the second.
- **[Book · ★★ · EN]** Flyvbjerg, B., Bruzelius, N. and Rothengatter, W. *Megaprojects and Risk: An Anatomy of Ambition*. Cambridge University Press, 2003 · ISBN 978-0-521-00946-1
  - The original 258-project transport study: ~9 of 10 underestimated, ~28% average overrun, rail ~45%, fixed links ~34%, roads ~20%.
- **[Paper · ★★★ · EN]** Kahneman, D. and Tversky, A. "Intuitive Prediction: Biases and Corrective Procedures." *Management Science*, 1979.
  - The planning fallacy and the outside view. Two ideas, and every estimation technique in the note is an application of the second.
- **[Report · ★★★ · EN]** Bloch, M., Blumberg, S. and Laartz, J. *Delivering large-scale IT projects on time, on budget, and on value*. McKinsey and Company with the University of Oxford BT Centre, October 2012.
  - 5,400+ projects above $15M: 45% over budget, 7% over time, 56% less value, ~15% added to cost overrun per extra scheduled year, 17% black swans above 200%.
- **[Report · ★★ · EN]** The Standish Group. *CHAOS Report 2020: Beyond Infinity*, March 2020.
  - ~31/50/19, the size effect (61% for small against 6% for the largest), and sponsor maturity moving success from 18% to 67%. Paywalled; the widely reported secondary figures are what most people quote.
- **[Report · ★★ · EN]** Project Management Institute. *Pulse of the Profession 2020: Ahead of the Curve — Forging a Future-Focused Culture*.
  - 11.4% of investment wasted on poor project performance; ~67% more projects failing outright in organisations that undervalue project management.
- **[Paper · ★★ · EN]** Budzier, A. and Flyvbjerg, B. "Why Your IT Project May Be Riskier Than You Think." *Harvard Business Review*, September 2011.
  - 1,471 projects, a 27% average overrun, and a one-in-six black swan. The argument for distributions over averages.

### Methodology, standards and lifecycle

- **[Standard · ★★★ · EN]** Project Management Institute. *A Guide to the Project Management Body of Knowledge (PMBOK Guide)*, 7th edition, 2021; and *Process Groups: A Practice Guide*, 2022.
  - 12 principles and 8 performance domains, plus the companion volume that restores the process-group view. Read both, or you will argue about a standard you have only half read.
- **[Standard · ★★★ · EN]** AXELOS / PeopleCert. *Managing Successful Projects with PRINCE2 — Version 7*, September 2023.
  - Seven principles, seven practices replacing the 6th edition's themes, seven processes, people as an integrated element, sustainability as a seventh performance target.
- **[Standard · ★★★]** ISO/TC 258. *ISO 21500:2021* · *ISO 21502:2020* · *ISO 21503:2022* · *ISO 21504:2022* · *ISO 21505:2017* · *ISO 21506:2024* · *ISO 21508* · *ISO 21511:2018* · *ISO 21512:2024* · *ISO 21513:2026*. <https://www.iso.org/committee/624837.html>
  - The international family: context and concepts, project, programme, portfolio, governance, vocabulary, earned value, work breakdown structures, EVM implementation, post-project evaluation. The correct citation whenever someone asks what "the standard" says.
- **[Standard · ★★★]** ISO. *31000:2018 — Risk management — Guidelines*.
  - Risk as the effect of uncertainty on objectives, and the framework the risk section follows.
- **[Doc · ★★★ · EN]** NASA. *NPR 7120.5E — NASA Space Flight Program and Project Management Requirements*, especially §2.4.4.
  - The phase A-to-F structure, key decision points, and the 70% joint cost and schedule confidence level policy with its 50% funding floor and $250M threshold.
- **[Report · ★★ · EN]** NASA Office of Inspector General. *Audit of NASA's Joint Cost and Schedule Confidence Level Process*, IG-15-024, 2015.
  - How the JCL policy was built: GAO 2004, the 70% cost confidence level, joint cost and schedule from 2005 and 2009, into 7120.5E in 2012.
- **[Book · ★★ · EN]** Cooper, R. G. *Winning at New Products: Creating Value through Innovation*, 4th ed. Basic Books, 2017 · ISBN 978-0-465-05784-9
  - Stage-gate: the gate criteria, the kill decision as a legitimate outcome, and the data on what separates winners.
- **[Paper · ★★★ · EN]** Royce, W. W. "Managing the Development of Large Software Systems." *Proceedings of IEEE WESCON*, 1970.
  - Nine pages. Read it before you argue about waterfall: the author recommended an iteration before build.

### Planning, scheduling, cost and risk

- **[Paper · ★★★ · EN]** Kelley, J. E. and Walker, M. R. "Critical-Path Planning and Scheduling." *Proceedings of the Eastern Joint Computer Conference*, 1959.
  - CPM from DuPont and Remington Rand, with the Louisville shutdown result (125 to 93 hours).
- **[Book · ★★★ · EN]** Goldratt, E. M. *Critical Chain*. North River Press, 1997 · ISBN 978-0-88427-153-6
  - 50% estimates, buffers instead of per-task padding, student syndrome, Parkinson's law, multitasking, and buffer management as the control signal.
- **[Book · ★★★ · EN]** Goldratt, E. M. and Cox, J. *The Goal*. North River Press, 1984 · ISBN 978-0-88427-061-4
  - Theory of Constraints from the beginning: throughput, drum-buffer-rope, and why local efficiency is not global efficiency.
- **[Book · ★★★ · EN]** Brooks, F. P. *The Mythical Man-Month: Essays on Software Engineering*. Addison-Wesley, 1975; anniversary edition 1995 · ISBN 978-0-201-83595-3
  - Brooks's law, conceptual integrity, and "no silver bullet". Fifty years old and still the best thing written on staffing a software project.
- **[Book · ★★ · EN]** Boehm, B. W. *Software Engineering Economics*. Prentice Hall, 1981 · ISBN 978-0-13-822122-5
  - The defect-cost escalation curve and COCOMO. The source of the 1-10-100 rule of thumb, and of the argument for front-loading.
- **[Book · ★★ · EN]** Fleming, Q. W. and Koppelman, J. M. *Earned Value Project Management*, 4th ed. PMI, 2010 · ISBN 978-1-933890-27-5
  - The clearest practical treatment of EV, including the EAC variants and what each one assumes.
- **[Doc · ★★ · EN]** Roland Wanner. *The History of Earned Value Management* and *The Origin of the EVMS Guidelines and Their Future*. <https://www.rolandwanner.com/>
  - The dated lineage from PERT/Cost and C/SCSC's 35 criteria in 1967 through 32 in 1996, ANSI/EIA-748 in 1998, -C and -D, to EIA-748-E in February 2026. Marked VERIFY in the note because it is a specialist secondary source.

### Quality, leadership and teams

- **[Book · ★★★ · EN]** Deming, W. E. *Out of the Crisis*. MIT Press, 1982 · ISBN 978-0-911379-01-3
  - The 14 points, PDCA, and why quality cannot be inspected in. Short sections; read one a day.
- **[Book · ★★★ · EN]** DeMarco, T. and Lister, T. *Peopleware: Productive Projects and Teams*, 3rd ed. Addison-Wesley, 2013 · ISBN 978-0-321-93411-6
  - The evidence that environment, focus and uninterrupted time dominate individual capability. The book that makes "people are the constraint" measurable.
- **[Book · ★★★ · EN]** Edmondson, A. *The Fearless Organization*. Wiley, 2018 · ISBN 978-1-119-45723-7
  - Psychological safety and accountability as independent axes, and how to build the first without losing the second.
- **[Article · ★★★ · EN]** Duhigg, C. "What Google Learned From Its Quest to Build the Perfect Team." *The New York Times*, 2016-02-25; and Google re:Work, *Understand Team Effectiveness*.
  - Project Aristotle: 180+ teams, five dynamics, psychological safety first.
- **[Book · ★★ · EN]** Yourdon, E. *Death March*. Prentice Hall, 1997 · ISBN 978-0-13-748310-9
  - How to recognise a mission-impossible project before you join it, and what to do once you are in one.

### Practice in mature organisations

- **[Book · ★★★ · EN]** Morgan, J. M. and Liker, J. K. *The Toyota Product Development System: Integrating People, Process and Technology*. Productivity Press, 2006 · ISBN 978-1-56327-282-3
  - The 13 principles, the chief engineer system, set-based concurrent engineering, obeya, and the Prius programme as a worked example. The single most useful book on engineering development.
- **[Book · ★★★ · EN]** Ward, A. C. *Lean Product and Process Development*. Lean Enterprise Institute, 2007 · ISBN 978-1-934109-10-9
  - "Almost all defective projects result from not having the right knowledge in the right place at the right time." The case for set-based design, trade-off curves and knowledge reuse.
- **[Book · ★★ · EN]** Liker, J. K. *The Toyota Way*. McGraw-Hill, 2004 · ISBN 978-0-07-139231-0
  - The 14 management principles behind the development system, including respect for people.
- **[Book · ★★★ · EN]** Bryar, C. and Carr, B. *Working Backwards: Insights, Stories, and Secrets from Inside Amazon*. St. Martin's Press, 2021 · ISBN 978-1-250-26702-8
  - Single-threaded leaders, two-pizza teams, the six-page narrative, PR/FAQ, bar raisers, input metrics, and mechanisms instead of intentions.
- **[Doc · ★★ · EN]** Amazon Web Services. *AWS Executive Insights: Product Management at Amazon*. <https://aws.amazon.com/executive-insights/content/product-management-at-amazon/>
  - The organisation's own account of single-threaded ownership, working backwards and the mechanisms that hold teams aligned.
- **[Book · ★★★ · EN]** Beyer, B., Jones, C., Petoff, J. and Murphy, N. R. *Site Reliability Engineering*. O'Reilly, 2016 · <https://sre.google/sre-book/>
  - SLI, SLO, error budget, the 50% toil cap, on-call load, blameless postmortems. Reliability as a numeric bargain rather than an argument.
- **[Book · ★★★ · EN]** Forsgren, N., Humble, J. and Kim, G. *Accelerate: The Science of Lean Software and DevOps*. IT Revolution, 2018 · ISBN 978-1-945055-01-1
  - The four key metrics, the capabilities that predict them, and the research method behind the claims.
- **[Report · ★★ · EN]** DORA / Google Cloud. *Accelerate State of DevOps Report 2024*. <https://dora.dev/research/>
  - The last year with directly comparable Elite-through-Low clusters, and the caveat that they are clusters, not targets.
- **[Book · ★★ · EN]** Humble, J. and Farley, D. *Continuous Delivery*. Addison-Wesley, 2010 · ISBN 978-0-321-60191-9
  - The deployment pipeline as the mechanism that turns release into a policy.
- **[Book · ★★ · EN]** Doerr, J. *Measure What Matters*. Portfolio, 2018 · ISBN 978-0-525-53623-9
  - OKRs from Grove's iMBOs to Google, and why grading matters more than scoring.
- **[Essay · ★★ · EN]** Kniberg, H. and Ivarsson, A. "Scaling Agile at Spotify with Tribes, Squads, Chapters and Guilds", 2012; and Lee, J. "Failed #SquadGoals", 2020.
  - The model everyone copied, and the correction from inside. Read them as a pair.
- **[Site · ★★ · EN]** Scaled Agile. *SAFe 6.0*, March 2023. <https://scaledagileframework.com/>
  - The most widely adopted scaling framework, its Essential configuration, and the flow accelerators worth borrowing even if you adopt nothing else.

### Cases, and how failure is documented

- **[Report · ★★★ · EN]** United States Digital Service. *Report to Congress, December 2016 — Stabilizing and Improving HealthCare.gov*. <https://usds.gov/report-to-congress/2016/healthcare-dot-gov/>
  - The tech surge, 8 million enrolments by March 2014, USDS creation in August 2014, 99.99% SLS uptime, and the 55% to 85% conversion improvement.
- **[Report · ★★★ · EN]** House Committee on Transportation and Infrastructure. *The Design, Development and Certification of the Boeing 737 MAX*, final report, September 2020.
  - Production pressure, faulty assumptions, concealment, conflicted representation, and influence over oversight — with the countdown clock and the 2,000-hour testing reduction in evidence.
- **[Report · ★★ · EN]** Federal News Network, "FBI turns troubled into triumph with Sentinel system", August 2012; and Computerworld, "How the FBI proves agile works for government agencies", 2012.
  - VCF cancelled at ~$170M against Sentinel's in-house agile recovery and July 2012 deployment. The cleanest natural experiment in the literature.
- **[Case · ★★★ · EN]** SEBoK. *Denver Airport Baggage Handling System*. <https://www.sebokwiki.org/>
  - Sixteen months, ~$500M, a $238M system, and eight structural causes. The canonical systems-engineering failure case.
- **[Guidance · ★★ · EN]** UK HM Treasury. *The Green Book: Central Government Guidance on Appraisal and Evaluation*.
  - Optimism-bias uplifts since 2003: reference class forecasting as government policy, with the tables.

---

_Copyright (c) 2026 Washington Ruan and contributors · licensed under **GPL-3.0-or-later** or **AGPL-3.0-or-later**, at your option · see `LICENSE` and `LICENSE-AGPL`._
