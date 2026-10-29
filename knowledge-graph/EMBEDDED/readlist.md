---
title: Reading list — EMBEDDED · Embedded and systems software
lang: en
category: reading-list
license: GPL-3.0-or-later OR AGPL-3.0-or-later
last-updated: 2026-10-29
---

# Reading list — EMBEDDED · Embedded and systems software

> The software the stack runs on: RTOS and hardware interfaces, embedded Linux, software architecture, interrupts, concurrency and IPC, and the device-driver model.
>
> One section per note, numbered `GG-x`. Where a note needed no source beyond its own
> **References**, there is no section here — the note is self-sufficient.

## How to use this list

- **Marks.** Type and priority marks (`★★★`, `[Book]`, `[EN]`) are defined once, in the MOC under *Reading marks*. The rule that matters: `★★★` means read or skim before you quote the note in an interview.
- **Titles** are kept in their published form and never translated; descriptions are English.
- **Nothing is asserted.** Where a citation could not be confirmed against a publisher, DOI, arXiv record or the issuing body, it is marked `VERIFY`.

---

## 04-1 · Embedded Systems, RTOS and Hardware Interfaces
### Books

- **[Book · EN · ★★★]** *Mastering the FreeRTOS Real Time Kernel — A Hands On Tutorial Guide* — Richard Barry · FreeRTOS; release v1.1.0, 19 August 2024 (references FreeRTOS V10.6.2)
  - The official kernel book, freely available with companion source. Covers tasks, scheduling, queues, semaphores and mutexes, direct-to-task notifications, stream and message buffers, memory management, and priority inheritance. Read this alongside the source; the context-switch and tick-handling detail is what separates real RTOS understanding from API familiarity.
- **[Book · EN · ★★]** *Making Embedded Systems: Design Patterns for Great Software*, 2nd ed. — Elecia White · O'Reilly, 2021
  - Practical patterns for resource-constrained firmware: state machines, hardware abstraction, debugging without a debugger, and how to structure code you can actually test on target.
- **[Book · EN · ★★]** *Embedded Systems Architecture: Explore System-Level Design and Advanced Features* — Daniele Lacamera · Packt, 2nd ed. 2021
  - System-level view: boot sequence, linker scripts and memory layout, interrupt and exception handling, RTOS integration, and the build/flash/debug flow. Good for connecting bare-metal mechanics to the Linux view in note 04-2.
- **[Book · EN · ★★★]** *Hard Real-Time Computing Systems: Predictable Scheduling Algorithms and Applications*, 3rd ed. — Giorgio C. Buttazzo · Springer, 2011
  - The rigorous treatment of schedulability analysis, rate-monotonic and EDF scheduling, priority inversion and aperiodic servers. This is what makes a "hard real-time" claim defensible rather than rhetorical.
- **[Book · EN/CN · ★★]** *Computer Organization and Design RISC-V Edition* (see §07-1)
  - For the cache-coherency, memory-barrier and DMA-consistency reasoning that embedded work depends on.

### Papers and documentation

- **[Doc · ★★★]** **FreeRTOS kernel documentation and reference manual** (freertos.org)
  - The authoritative API reference and porting guide. Note the LTS releases (for example the 202604.00-LTS libraries) and the SMP support, both relevant to multi-core embedded design.
- **[Standard · ★]** **IEEE Std 802.15.4-2020** — Low-Rate Wireless Personal Area Networks (LR-WPANs)
  - The PHY/MAC baseline for most low-power sensor radios.
- **[Standard · ★]** **CAN / ISO 11898-1:2015** — Road vehicles; Controller area network; Part 1: Data link layer and physical signalling
  - The canonical CAN reference if your hardware-interface discussion covers automotive or industrial buses.
- **[Doc · ★★]** **ARM Cortex-M documentation: NVIC, MPU, SysTick, and the ARMv8-M TrustZone / PACBTI extensions**
  - Exception model and memory-protection mechanics that RTOS ports actually depend on.

---

## 04-2 · Linux Embedded Development — Drivers, Applications and Core Subsystems
### Books — driver development

- **[Book · EN/CN · ★★★]** *Linux Device Drivers*, 3rd ed. — Jonathan Corbet, Alessandro Rubini, Greg Kroah-Hartman · O'Reilly, 2005 · ISBN 9780596005900 · Chinese 《Linux设备驱动程序(第3版)》, translated by 魏永明, 耿岳, 钟书毅 · 中国电力出版社, 2006 · ISBN 9787508338637
  - The classic. Written against kernel 2.6.10, so the subsystem-specific chapters (PCI, USB) are dated, but the chapters on the character-device model, concurrency and locking, blocking I/O, memory allocation, interrupts, time and the memory-mapping/DMA chapter remain the clearest exposition available. Read it for the model; cross-check current APIs against the kernel tree.
- **[Book · CN · ★★★]** 《Linux设备驱动开发详解》 — 宋宝华 · 人民邮电出版社; 1st ed. 2008 (ISBN 9787115172396), 2nd ed. 2010 (ISBN 9787115236579)
  - The standard Chinese driver book, grounded in real ARM board work (LDD6410, Linux 2.6). Covers spinlocks, semaphores, completions, top-half/bottom-half interrupt handling, timers, and I/O mapping, then walks char, block, TTY, I2C, LCD, audio, USB, network and PCI device drivers. Strong on the *framework-per-subsystem* idea.
- **[Book · EN · ★★]** *Linux Device Drivers Development*, 2nd ed. — John Madieu · Packt, 2022
  - A modern, device-tree-first update in the spirit of LDD3: regmap, IIO, and the current kernel APIs. Use it to correct what LDD3 leaves stale.
- **[Book · EN · ★★]** *Linux Driver Development for Embedded Processors*, 2nd ed. — Alberto Liberal de los Ríos · self-published
  - ARM-focused, with complete runnable examples on Raspberry Pi and i.MX covering device tree, GPIO, I2C, SPI, UART and USB. The fastest path from "I understand the model" to "my driver enumerates and probes".

### Books — kernel internals

- **[Book · EN/CN · ★★★]** *Understanding the Linux Kernel*, 3rd ed. — Daniel P. Bovet, Marco Cesati · O'Reilly · Chinese 《深入理解Linux内核(第三版)》, translated by 陈莉君, 张琼声, 张宏伟 · 中国电力出版社, 2007 · ISBN 9787508353944
  - The structure of the kernel: process and memory management, the VFS, block I/O, and the interrupt/exception paths. Read for the conceptual architecture; verify current behaviour against the source, since the kernel has moved on.
- **[Book · EN · ★★]** *Linux Kernel Development*, 3rd ed. — Robert Love · Addison-Wesley, 2010
  - Concise, current-for-its-era account of process scheduling, the interrupt handler path, kernel synchronisation and the VFS. Written by a kernel contributor with an emphasis on *why* the code is shaped that way.
- **[Book · EN · ★★]** *Linux Kernel Networking: Implementation and Theory* — Rami Rosen · Apress, 2013
  - The kernel network stack in detail: `sk_buff`, netfilter, the routing and neighbour subsystems, and the driver interface. Use alongside the DPDK material in §08.
- **[Book · EN · ★]** *Understanding Linux Network Internals* — Christian Benvenuti · O'Reilly, 2005 (see §05-1)

### Books — system and application programming

- **[Book · EN · ★★★]** *The Linux Programming Interface* — Michael Kerrisk · No Starch Press, 2010
  - The definitive system-programming reference: processes, threads, IPC, signals, timers, file I/O, memory mapping, and sockets. Over 1500 pages, with every syscall documented against its behaviour. This is the book to own for the IPC and networking sections of note 04-2.
- **[Book · EN · ★★]** *Linux System Programming*, 2nd ed. — Robert Love · O'Reilly, 2013
  - Shorter and more opinionated, covering the same ground with more emphasis on writing correct and efficient code. Good complement to Kerrisk.
- **[Book · EN/CN · ★★★]** *UNIX Network Programming, Vol. 1: The Sockets Networking API*, 3rd ed. — W. Richard Stevens, Bill Fenner, Andrew M. Rudoff · Chinese 《UNIX网络编程 卷1:套接字联网API(第3版)》, translated by 杨继张 · 人民邮电出版社, 2010 · ISBN 9787115228406 (2019 printing ISBN 9787115517791)
  - The socket reference: TCP/UDP/SCTP, the elementary and advanced socket APIs, I/O models (`select`/`poll`/`epoll`), non-blocking I/O, broadcast and multicast, and client/server design alternatives. All examples are real, runnable code. Read chapters 6, 15–16 and 30 before any serious network-service work.
- **[Book · EN/CN · ★★]** *TCP/IP Illustrated, Vol. 1: The Protocols* — W. Richard Stevens · Chinese 《TCP/IP详解 卷1:协议》
  - Packet-level protocol walkthroughs that no other book matches. Read it with a packet capture open.
- **[Book · CN · ★★]** 《UNIX环境高级编程》 (Advanced Programming in the UNIX Environment) — W. Richard Stevens, Stephen A. Rago
  - The Chinese standard for UNIX/Linux system programming fundamentals, and the usual reference for signal handling, daemonisation and file I/O semantics in Chinese-language teams.

### Books — embedded Linux and build systems

- **[Book · EN/CN · ★★★]** *Embedded Linux Primer: A Practical, Real-World Approach*, 2nd ed. — Christopher Hallinan · Prentice Hall · Chinese 《嵌入式Linux基础教程》, 人民邮电出版社; 1st ed. 2009 (ISBN 9787115215222), 2nd ed. 2012, translated by 周鹏 (ISBN 9787115278272)
  - The engineering picture in one volume: bootloaders, kernel initialisation, cross-compilation, file systems, flash/MTD, and debugging (including KGDB/gdb). The 2nd edition adds udev, USB and open build systems.
- **[Book · EN · ★★★]** *Mastering Embedded Linux Programming*, 3rd ed. — Chris Simmonds (with Frank Vasquez) · Packt, 2021
  - The most current end-to-end text: toolchains, U-Boot, kernel configuration, Buildroot versus Yocto, root filesystem construction, and driver interaction. Chapter 6 (choosing a build system) and chapter 11 (interacting with device drivers) are the two most useful.
- **[Book · EN · ★★]** *Building Embedded Linux Systems*, 2nd ed. — Karim Yaghmour, Jon Masters, Gilad Ben-Yossef, Philippe Gerum · O'Reilly, 2008
  - Deeper on BSP construction: toolchain internals, kernel configuration, root filesystem assembly, booting and power management. The BSP engineer's reference.

### Documentation

- **[Doc · ★★★]** **Linux kernel Documentation/** (in-tree) — and in particular `core-api/`, `driver-api/`, `devicetree/bindings/`, `scheduler/`, `networking/` and `virt/`
  - The authoritative and current reference. Device tree bindings are the stable ABI; read them before writing or reviewing a binding.
- **[Doc · ★★★]** **Yocto Project documentation** (mega-manual, BSP Developer's Guide, Kernel Development Manual) and **Buildroot user manual**
  - The two build-system references that matter. Use the Yocto LTS release names recorded in note 04-2 when citing versions.
- **[Doc · ★★]** **U-Boot documentation** and **Device Tree Specification** (devicetree.org)
  - Boot chain and hardware description. The DT spec is short; read it once properly.
- **[Doc · ★★]** **cyclictest / rt-tests documentation** and the **PREEMPT_RT wiki**
  - Real-time verification tooling. PREEMPT_RT was merged into mainline in Linux 6.12 for x86, arm64 and RISC-V; 32-bit ARM followed later.

---

## 04-3 · Embedded Software Architecture — Patterns, Layering and Wireless System Structure
### Books — architecture and design method

- **[Book · ★★★ · EN]** **Making Embedded Systems: Design Patterns for Great Software**, 2nd ed. — Elecia White, O'Reilly, 2024. ISBN 9781098151546. The most readable entry point into embedded architecture as a *design* discipline rather than a driver catalogue. Chapter 2 ("Creating a System Architecture") is the one to read before an interview; the second edition adds IoT/networked sensors, motors and data-handling strategy. Chapters on reducing RAM, code space and power are directly quotable.
- **[Book · ★★★ · EN]** **Embedded Systems Architecture**, 2nd ed. — Daniele Lacamera, Packt, Jan 2023. ISBN 9781803239545 (342 pp.). Chapter 3 is literally "Architectural Patterns"; also covers boot-up procedure, memory management, distributed/IoT architecture, parallel tasks and scheduling, and Trusted Execution Environment. Good coverage of the memory-isolation-oriented view of RTOS design.
- **[Book · ★★ · EN]** **Software Engineering for Embedded Systems: Methods, Practical Techniques, and Applications**, 2nd ed. — Robert Oshana and Mark Kraeling (eds.), Newnes/Elsevier, 2019. ISBN 978-0-12-809448-8 (1st ed. 2013, ISBN 978-0-12-415917-4). Multi-author reference; the relevant chapters are on architecture and design patterns, real-time building blocks, safety-critical development, and multicore software development. Contributors include Jean Labrosse and Bruce Douglass.
- **[Book · ★★ · EN]** **Better Embedded System Software** — Philip Koopman, Drumnadrochit Education, 2010. ISBN 978-0-9844490-0-2. Short, opinionated and practice-driven: requirements, design, implementation and test discipline specifically for embedded. Strong on the failure modes that architecture should prevent.
- **[Book · ★ · EN]** **The Art of Designing Embedded Systems**, 2nd ed. — Jack Ganssle, Newnes, 2008. Essays rather than a textbook; useful for the project-reality side (estimation, firmware process, why projects fail). `VERIFY` the exact edition/ISBN before citing.

### Books — execution models, scheduling and time-triggered design

- **[Book · ★★★ · EN]** **Hard Real-Time Computing Systems: Predictable Scheduling Algorithms and Applications**, 3rd ed. — Giorgio C. Buttazzo, Springer, 2011. ISBN 978-1-4614-0676-1, DOI 10.1007/978-1-4614-0676-1 (Real-Time Systems Series, vol. 24). The standard text for the scheduling theory in note 04-3 §2.3: periodic and aperiodic task scheduling, fixed- and dynamic-priority servers, resource access protocols, limited-preemptive scheduling, overload handling, kernel and application design issues.
- **[Book · ★★ · EN]** **Real-Time Systems and Programming Languages**, 4th ed. — Alan Burns and Andy Wellings, Addison-Wesley, 2009. Broader than Buttazzo: covers the language and OS support for real-time (Ada, Real-Time Java, real-time POSIX, Ada/RT scheduling). Good for the "what does the platform actually give you" question.
- **[Book · ★★ · EN]** **Patterns for Time-Triggered Embedded Systems: Building Reliable Applications with the 8051 Family of Microcontrollers** — Michael J. Pont, Addison-Wesley, 2001. ISBN 0-201-33138-1 / 9780201331387. The canonical catalogue of time-triggered architecture patterns (70+). Free PDF from the author's site. 8051-flavoured, which is dated — read it for the *patterns*, not the silicon.
- **[Book · ★★★ · EN]** **The Engineering of Reliable Embedded Systems**, 2nd ed. — Michael J. Pont, SafeTTy Systems, 2016/2017. ISBN 978-0-9930355-3-1. The successor to PTTES and the one to cite for safety work: second-generation time-triggered architectures, with worked case studies targeting IEC 61508 SIL 2, IEC 60730 Class B, IEC 62304 Class C, ISO 26262 ASIL D and DO-178C Level A.

### Books — state machines and event-driven architecture

- **[Book · ★★★ · EN]** **Practical UML Statecharts in C/C++: Event-Driven Programming for Embedded Systems**, 2nd ed. — Miro Samek, Newnes/Elsevier, 2008/2009. ISBN 978-0-7506-8706-5. The definitive text: UML statecharts, hierarchical state machines, run-to-completion, inversion of control, event queues, and the design study of the QP event-driven framework (including the QEP hierarchical event processor). Read Part II even if you never use QP — the argument for RTC over blocking is the architectural core.
- **[Book · ★ · EN]** **Design Patterns: Elements of Reusable Object-Oriented Software** — Gamma, Helm, Johnson, Vlissides (GoF), Addison-Wesley, 1994. ISBN 978-0-201-63361-0. The source catalogue for §4. Read it knowing that the embedded cost accounting differs: virtual dispatch, object size and allocation are all first-class costs on a microcontroller.

### Papers — scheduling theory

- **[Paper · ★★★ · EN]** Liu, C. L. and Layland, J. W., **"Scheduling Algorithms for Multiprogramming in a Hard-Real-Time Environment"**, *Journal of the ACM* 20(1): 46–61, 1973. The founding paper: rate-monotonic priority assignment is optimal among fixed-priority schemes for implicit deadlines; utilization bound `n(2^(1/n) − 1)` tending to `ln 2 ≈ 0.693`; EDF is feasible up to `U ≤ 1`.
- **[Paper · ★★ · EN]** Sha, L., Rajkumar, R. and Lehoczky, J. P., **"Priority Inheritance Protocols: An Approach to Real-Time Synchronization"**, *IEEE Transactions on Computers* 39(9): 1175–1185, 1990. The reference for priority inheritance and ceiling protocols — the standard answer to priority inversion.
- **[Paper · ★★ · EN]** Baker, T. P., **"A Stack-Based Resource Allocation Policy for Realtime Processes"**, IEEE Real-Time Systems Symposium, 1990. Stack Resource Policy: the bound-optimal approach that also yields the best known worst-case stack requirement.
- **[Paper · ★★ · EN]** Leung, J. Y.-T. and Whitehead, J., **"On the Complexity of Fixed-Priority Scheduling of Periodic, Real-Time Tasks"**, *Performance Evaluation* 2(4): 237–250, 1982. Deadline-monotonic priority ordering.
- **[Paper · ★ · EN]** Audsley, N. C., Burns, A., Richardson, M. F. and Wellings, A. J., **"Hard Real-Time Scheduling: The Deadline-Monotonic Approach"** (1991) and **"Applying New Scheduling Theory to Static Priority Pre-emptive Scheduling"** (1993). Audsley's Optimal Priority Assignment: an optimal ordering in at most `n(n+1)/2` tests, plus the release-jitter extensions.
- **[Paper · ★ · EN]** Buttazzo, G. C., **"Rate Monotonic vs. EDF: Judgment Day"**. A systematic demolition of the common misconceptions that favour RM over EDF. Excellent interview ammunition — it lets you answer "RM or EDF?" with the trade-offs rather than the folklore.

### Papers — safety, protection and dependability

- **[Paper · ★★ · EN]** Holzmann, G. J., **"The Power of 10: Rules for Developing Safety-Critical Code"**, *IEEE Computer* 39(6): 95–99, 2006. DOI 10.1109/MC.2006.212. NASA/JPL. Ten rules, including bounded loops, no dynamic allocation after initialisation, and restricted use of interrupts and recursion. Short enough to memorise and quote.
- **[Paper · ★★ · EN]** Zhou, W. et al., **"Good Motive But Bad Design: Why ARM MPU Has Become an Outcast in Embedded Systems"**, arXiv:1908.03638, 2019. Documents why the ARM MPU is rarely configured as intended. The credible, non-obvious point to raise when discussing memory protection and freedom from interference.
- **[Paper · ★ · EN]** Stankovic, J. A., **"Misconceptions About Real-Time Computing: A Serious Problem for Next-Generation Systems"**, *IEEE Computer* 21(10): 10–19, 1988. Still worth reading: the gap between "fast" and "predictable" is the same confusion that appears in modern latency-vs-throughput arguments.

### Standards and specifications

- **[Standard · ★★★ · EN]** **AUTOSAR Classic Platform** — current release **R25-11** (Release Event 4 December 2025). `autosar.org/standards/classic-platform`. Application / RTE / BSW layering, MCAL, Complex Drivers, and the Virtual Functional Bus. Start with *Layered Software Architecture* and *Methodology*.
- **[Standard · ★★ · EN]** **AUTOSAR Adaptive Platform** — same release train; ARA (AUTOSAR Runtime for Adaptive Applications), functional clusters, POSIX-based, service-oriented. Read alongside the **Foundation** standard for cross-platform interoperability.
- **[Standard · ★★★ · EN]** **MISRA C:2025** — current edition (updated March 2025), MISRA. Supersedes MISRA C:2023. The coding standard referenced for safety-critical C.
- **[Standard · ★★ · EN]** **MISRA C++:2023** (with TC1:2026) — current MISRA C++, written against **C++17**. Note the implication: a MISRA-conformant C++ project is not on C++20/23/26.
- **[Standard · ★★ · EN]** **ISO 26262:2018** (2nd ed., December 2018) — *Road vehicles — Functional safety*. 12 parts; Part 4 system level, Part 5 hardware, Part 6 software, Part 9 ASIL-oriented analysis, Part 11 semiconductors, Part 12 motorcycles. ASIL A–D and QM from Severity/Exposure/Controllability; SPFM/LFM/PMHF targets.
- **[Standard · ★★ · EN]** **IEC 61508** (2nd ed., 2010) — the parent functional-safety standard; SIL 1–4. Sector derivatives: IEC 61511 (process), IEC 62061/ISO 13849 (machinery), EN 5012x (rail), IEC 62304 (medical software), IEC 60730 (household), DO-178C (avionics).
- **[Spec · ★★ · EN]** **OSEK/VDX Operating System Specification 2.2.1** (2003) — the static, configurable RTOS specification that AUTOSAR OS descends from. Worth knowing conceptually: it is where the "configuration rather than code" philosophy comes from.
- **[Spec · ★★ · EN]** **ETSI TS 103859** (O-RAN.WG4.CUS.0) — O-RAN Fronthaul Control, User and Synchronization Plane. Defines the **7-2x** split, Category A/B O-RUs, eCPRI transport and IQ compression. The normative source for note 04-3 §6.3.
- **[Spec · ★ · EN]** **O-RAN.WG1 Architecture Description** and **O-RAN.WG3 (E2/E2SM)** — the architecture and near-RT RIC interface specs. See §18.
- **[Spec · ★★ · EN]** **3GPP TS 38.401** — NG-RAN architecture description, including the CU/DU split. `VERIFY` the F1/E1 part numbers before quoting them.

### Documentation and code

- **[Doc · ★★★ · EN]** **Zephyr Project documentation** — `docs.zephyrproject.org`. Releases, devicetree, Kconfig, power management, and MCUboot. Current stable **4.4.0** (2026-04-14); **3.7.0** is LTS3 (2024-07-26, EOL 2029-07-27); LTS4 planned as 5.0 (Oct 2027). Read the *release and migration guides* — they are the best available example of how a serious embedded project manages long-term compatibility.
- **[Code · ★★ · EN]** **MCUboot** — open-source secure bootloader for 32-bit MCUs, integrated with Zephyr. Study it for the A/B update, image format, signature verification and swap/overwrite strategies described in note 04-3 §9.
- **[Code · ★★ · EN]** **QP / QP/C / QP/C++** (Quantum Leaps) — the open-source active-object and hierarchical state machine framework behind Samek's book. Read `qpc` source for a production-quality HSM dispatcher and event queue implementation in C.
- **[Code · ★ · EN]** **FreeRTOS kernel** — `freertos.org`; see §07. Read its `port.c` for the PendSV context-switch mechanics that the execution model in note 04-3 §2 depends on.
- **[Doc · ★ · EN]** **MCUboot / RAUC / SWUpdate / Mender documentation** — three different answers to the same update problem; comparing them is the fastest way to internalise what is *essential* in an OTA architecture versus what is implementation detail.

---

## 04-4 · Linux Interrupts — Types, Handlers, Threaded IRQs and Deferred Work
> The general driver and kernel texts are in §04-2. This section lists the interrupt-specific sources: the three interrupt-controller specifications, the generic-IRQ and workqueue kernel documentation, the mailing-list record of the deferred-work conversion, and the real-time measurement tooling.

### Standards — interrupt controllers

- **[Spec · ★★★ · EN]** **Arm Generic Interrupt Controller Architecture Specification, GICv3 and GICv4** — Arm, **ARM IHI 0069** (`developer.arm.com`, free download)
  - The normative source for the INTID map (SGI 0–15, PPI 16–31, SPI 32–1019, special 1020–1023, LPI 8192+), the Distributor / Redistributor / CPU-interface split, the ITS, the LPI configuration in memory tables, and GICv4 direct vLPI injection. Cite the document number, not a blog post.
- **[Spec · ★★ · EN]** **Arm Generic Interrupt Controller Architecture Specification, GICv2** — Arm, **ARM IHI 0048**
  - Still what a large number of shipping embedded SoCs implement; read it to see what v3 added and why.
- **[Doc · ★★★ · EN]** **Learn the Architecture: Generic Interrupt Controller v3 and v4** — Arm developer documentation; the *Overview*, *Locality-specific Peripheral Interrupts* and *Virtualization* guides
  - The readable entry point. The INTID table and the "dedicated signal versus message" figures quoted in note 04-4 follow it.
- **[Spec · ★★ · EN]** **Intel 64 and IA-32 Architectures Software Developer's Manual, Volumes 3A and 3B** — Intel
  - The chapters on the IDT, the Local APIC, the I/O APIC, MSI, and NMI/SMI/machine-check. The x86 ground truth for §3.2 of note 04-4.
- **[Spec · ★★ · EN]** **PCI Express Base Specification** — PCI-SIG
  - The MSI and MSI-X capability structures, the 32-vector / 2048-vector limits, and the MSI-X table and PBA layout.
- **[Spec · ★★★ · EN]** **The RISC-V Advanced Interrupt Architecture, Version 1.0** — John Hauser (ed.); ratified by RISC-V International **June 2023**; document revision **2025-03-12**. `docs.riscv.org/reference/aia`
  - Chapters 3 (IMSIC), 4 (APLIC), 5 (interrupts at M and S levels), 6 (virtual machines), 7 (IPIs), 8 (IOMMU support). Released under CC BY 4.0.
- **[Spec · ★★ · EN]** **The RISC-V Instruction Set Manual, Volume II: Privileged Architecture**
  - The base external-interrupt conventions (`mip`/`mie`, major interrupt numbers) that AIA extends.

### Kernel documentation

- **[Doc · ★★★ · EN]** **Linux `Documentation/core-api/irq/`** — `docs.kernel.org/core-api/irq/`
  - The upstream description of the generic IRQ layer: `irq-domain.rst`, `irq-generic.rst`, and `concepts.rst` (which is where `irq_desc`, `irq_chip`, the flow handlers and chained versus nested chips are defined).
- **[Doc · ★★★ · EN]** **Linux `Documentation/core-api/workqueue.rst`** — `docs.kernel.org/core-api/workqueue.html`
  - The normative text for `WQ_BH`, `WQ_UNBOUND`, `WQ_HIGHPRI`, `WQ_CPU_INTENSIVE`, `WQ_MEM_RECLAIM`, and `@max_active` (maximum 512, default 256 when 0 is passed).
- **[Doc · ★★ · EN]** **Linux `Documentation/admin-guide/IRQ-affinity.rst`** — `docs.kernel.org/admin-guide/IRQ-affinity.html`
  - Affinity, `irqbalance`, and the interaction with CPU isolation.
- **[Doc · ★★★ · EN]** **Linux `Documentation/admin-guide/kernel-parameters.txt`** — `docs.kernel.org/admin-guide/kernel-parameters.html`
  - The authoritative list for `threadirqs`, `irqaffinity=`, `irqchip.gicv3_pseudo_nmi=`, `irqchip.gicv3_nolpi=`, `irqpoll`, `irqfixup`, `nmi_watchdog`.
- **[Doc · ★★★ · EN]** **Linux `Documentation/core-api/real-time/differences.rst`** — added 2025
  - The official statement of how PREEMPT_RT differs: sleeping locks, forced-threaded interrupts, and the "SCHED_FIFO priority 50" default.
- **[Doc · ★★ · EN]** **Linux `Documentation/networking/napi.rst`** and **`Documentation/networking/scaling.rst`**
  - The NAPI driver contract, and RSS / RPS / RFS / XPS.
- **[Doc · ★★ · EN]** **Linux `Documentation/core-api/genericirq.rst`** (formerly `IRQ.txt`) and the in-tree **`Documentation/driver-api/irq`** material — the historical names are worth knowing because many secondary sources still cite them.

### Papers and mailing-list records

- **[Paper · ★★★ · EN]** Eric Dumazet, **"softirq: reduce latencies"** — LKML, 2013-01-03. `<lkml.iu.edu/hypermail/linux/kernel/1301.0/00627.html>`
  - The patch that added the 2 ms time budget on top of the 10-restart limit. The commit message is the best short explanation of why the softirq loop needs a brake.
- **[Paper · ★★★ · EN]** Tejun Heo, **"[PATCHSET wq/for-6.9] workqueue: Implement BH workqueue and convert several tasklet users"** — LKML, 2024-01-30; and **"[GIT PULL] workqueue changes for v6.9"**, 2024-03-11
  - The primary record of why `WQ_BH` exists, what its constraints are, and what the conversion is expected to achieve.
- **[Paper · ★★ · EN]** Julien Thierry, **"arm64: Enable the support of pseudo-NMIs"** — LKML, v6 2018-11 and v7 2018-12
  - The series that introduced `CONFIG_ARM64_PSEUDO_NMI` and the boot parameter.
- **[Paper · ★★ · EN]** Anup Patel, **"Linux RISC-V AIA Support"** (v12 v16) — LKML and Patchwork, 2024-01 to 2024-03
  - The authoritative description of what APLIC and IMSIC each do in the kernel, and of their dependencies on the per-device MSI domain work.
- **[Paper · ★ · EN]** The **tasklet-removal** discussions on LKML: Steven Rostedt's 2007 proposal, the 2019 2020 API-modernisation thread, and the 2024 `WQ_BH` decision
  - Cited for the history of a decision, not for any number. Reading them is how you learn to say "deprecated, conversion ongoing" with a straight face.

### Books

- **[Book · ★★ · EN]** **Mastering Linux Device Driver Development** — John Madieu · Packt, January 2021 · ISBN 978-1-78934-204-8
  - Chapter 1 (*Linux Kernel Concepts for Embedded Developers*) is the one that matters here: kernel locking helpers, work-deferral mechanisms and interrupt management, written against a recent kernel. Use it to check that a habit you learned from LDD3 still applies.
- **[Book · ★★ · EN]** **Operating System Concepts**, 10th ed. — Abraham Silberschatz, Peter B. Galvin, Greg Gagne · Wiley, 2018 · ISBN 978-1-119-32091-3
  - Chapter 12 (I/O systems) and the chapters on interrupts and scheduling. Use for the vocabulary that predates and outlives Linux: synchronous versus asynchronous, vectored versus polled, and the interrupt-handling model in general.

### Tools

- **[Tool · ★★★ · EN]** **rt-tests** — `cyclictest`, `hwlatdetect`, `osnoise`, `signaltest`. `wiki.linuxfoundation.org/realtime/documentation/`
  - `cyclictest` for worst-case wakeup latency; `hwlatdetect` for SMI/SMM and other latencies the kernel cannot see.
- **[Tool · ★★ · EN]** **trace-cmd and KernelShark** — recording and visualising IRQ entry/exit, softirq and scheduling events.
- **[Tool · ★★ · EN]** **util-linux** — `irqtop` for a live sorted view of `/proc/interrupts`; `taskset` and `chrt` for affinity and priority.
- **[Tool · ★★ · EN]** **perf** — `perf top/record/report`, `perf probe`, and the `irq:irq_handler_entry` / `irq:softirq_entry` tracepoints.

---

## 04-5 · Linux Concurrency — Kernel and User Mode, Processes, Threads and IPC
> Kerrisk's *The Linux Programming Interface* is listed in §04-2 and remains the owner of the user-space API; this section collects the concurrency-specific material around it: the POSIX text, the futex primary sources, the memory-model theory, and the race and contention tooling.

### Standards

- **[Standard · ★★★ · EN]** **The Open Group Base Specifications, Issue 7 (POSIX.1-2017)** — `pubs.opengroup.org/onlinepubs/9699919799/`
  - The normative text for processes, threads, mutexes, condition variables, and every IPC mechanism in §7 of note 04-5. Merrily paraphrased everywhere, so quote from here.
- **[Standard · ★★★ · EN]** **IEEE Std 1003.1c-1995** — the POSIX threads amendment
  - Where `pthread_create`, `pthread_mutex_t`, condition variables and thread-specific data come from.
- **[Standard · ★★ · EN]** **ISO/IEC 9899:2018 (C17)** and the current **C23** — §7.17 `<stdatomic.h>` and the memory-model clauses
  - The C-side view of `memory_order_*`; the enumeration is the same one C++ uses. **ISO/IEC 14882 (C++20 / C++23)** — `[[atomics.order]]` — is the C++ text.

### Books — the API

- **[Book · ★★★ · EN]** **Advanced Programming in the UNIX Environment**, 3rd ed. — W. Richard Stevens, Stephen A. Rago · Addison-Wesley, 2013 · ISBN 978-0-321-63773-4
  - Chapters 8 (process control), 11 (threads), 12 (thread control) and 15 17 (IPC). The classic treatment of the process lifecycle, `fork`/`exec`/`wait`, and the original presentation of the pipe, FIFO, message-queue, semaphore and shared-memory mechanisms.
- **[Book · ★★★ · EN]** **UNIX Network Programming, Volume 2: Interprocess Communications**, 2nd ed. — W. Richard Stevens · Prentice Hall, 1999 · ISBN 0-13-081081-9
  - The most detailed treatment of POSIX IPC, Unix domain sockets, `SCM_RIGHTS` and shared memory available. Chapters 5, 12 and 15 are the sources for §7 of note 04-5; appendix A is the most useful IPC-mechanism comparison table ever printed.

### Books — the theory and the primitives

- **[Book · ★★★ · EN]** **Is Parallel Programming Hard, And, If So, What Can You Do About It?** — Paul E. McKenney (`perfbook`, continuously updated, free)
  - The single most practical text on memory ordering, locking, lock-free techniques and deferred processing. Read the memory-ordering and counting chapters before designing anything lock-free, and the deferred-processing chapter before arguing about workqueues.
- **[Book · ★★★ · EN]** **The Art of Multiprocessor Programming**, 2nd ed. — Maurice Herlihy, Nir Shavit · Morgan Kaufmann, 2020 · ISBN 978-0-12-397337-5 (1st ed. 2008, ISBN 978-0-12-370591-4)
  - Linearisability, spin locks, concurrent queues and stacks. The correctness standards that make "my lock-free ring is fine" a checkable claim.
- **[Book · ★★ · EN]** **Modern Operating Systems**, 4th ed. — Andrew S. Tanenbaum, Herbert Bos · Pearson, 2015 · ISBN 978-0-13-359162-0
  - Chapters 2 (processes and threads), 6 (deadlock) and 7 for the OS-theory grounding: the dining philosophers, the readers-writers problem, and why IPC is presented as a scheduling problem.
- **[Book · ★★ · EN]** **Operating System Concepts**, 10th ed. — Abraham Silberschatz, Peter B. Galvin, Greg Gagne · Wiley, 2018 · ISBN 978-1-119-32091-3
  - Chapters 3 7: processes, threads, CPU scheduling and synchronisation.

### Papers

- **[Paper · ★★★ · EN]** Hubertus Franke, Rusty Russell, Matthew Kirkwood, **"Fuss, Futexes and Furwocks: Fast Userlevel Locking in Linux"** — *Ottawa Linux Symposium 2002*, pp. 479 495. `kernel.org/doc/ols/2002/ols2002-pages-479-495.pdf`
  - The primary source for §6.3: the design, the earlier approaches it replaced, and the benchmarks that justified it.
- **[Paper · ★★★ · EN]** Ulrich Drepper, **"Futexes Are Tricky"** — Red Hat
  - The document to read before using a bare futex instead of a mutex. Its existence is the argument.
- **[Paper · ★★ · EN]** Maged M. Michael and Michael L. Scott, **"Simple, Fast, and Practical Non-Blocking and Blocking Concurrent Queue Algorithms"** — *PODC 1996*
  - The reference lock-free queue; the standard against which a hand-rolled ring should be measured.
- **[Paper · ★★ · EN]** Lamport, L., **"Time, Clocks, and the Ordering of Events in a Distributed System"** — *Communications of the ACM* 21(7): 558 565, 1978
  - The origin of the happens-before relation.
- **[Paper · ★★ · EN]** Herlihy, M. and Wing, J. M., **"Linearizability: A Correctness Condition for Concurrent Objects"** — *ACM TOPLAS* 12(3): 463 492, 1990
  - The correctness condition for concurrent objects.
- **[Paper · ★★ · EN]** Adve, S. V. and Gharachorloo, K., **"Shared Memory Consistency Models: A Tutorial"** — *IEEE Computer* 29(12): 66 76, 1996
  - Why relaxed ordering exists and what it permits.
- **[Paper · ★★ · EN]** Silas Boyd-Wickizer et al., **"An Analysis of Linux Scalability to Many Cores"** — *OSDI 2010*
  - The measurement that motivated a decade of per-CPU and lock-free kernel work.
- **[Paper · ★★ · EN]** Tudor David, Rachid Guerraoui, Vasileios Trigonakis, **"Everything You Always Wanted to Know About Synchronization but Were Afraid to Ask"** — *SOSP 2013*
  - A systematic empirical comparison; the antidote to "lock-free is faster".
- **[Paper · ★★ · EN]** Hans-J. Boehm, **"Threads Cannot Be Implemented as a Library"** — *PLDI 2004*
  - The argument that forced a memory model into C11 and C++11; the reason §6.2 of note 04-5 exists at all.

### Documentation and code

- **[Doc · ★★★ · EN]** **Linux man-pages** — `man7.org/linux/man-pages/`. The directly relevant pages: `futex(2)`, `futex(7)`, `clone(2)`, `clone3(2)`, `set_tid_address(2)`, `pthreads(7)`, `sched(7)`, `cgroups(7)`, `namespaces(7)`, `mq_overview(7)`, `sem_overview(7)`, `svipc(7)`, `shm_overview(7)`, `memfd_create(2)`, `eventfd(2)`, `signalfd(2)`, `timerfd_create(2)`, `pidfd_open(2)`, `io_uring(7)`, `unix(7)`, `epoll(7)`
  - Maintained with authoritative VERSIONS sections, which is how you check when a syscall appeared without reading the git history.
- **[Doc · ★★ · EN]** **Linux `Documentation/scheduler/`** and **`Documentation/locking/`** — `docs.kernel.org`
  - Scheduler policies, EEVDF and `SCHED_DEADLINE`; and the kernel's own statement of its locking rules.
- **[Code · ★★★ · EN]** **glibc NPTL sources** (`nptl/`) — in particular `pthread_mutex_lock.c` and `pthread_cond_wait.c`
  - The actual implementation. Reading it alongside §6 is the fastest way to internalise why the uncontended path has no syscall.
- **[Code · ★★ · EN]** **the kernel's `kernel/futex/`** — the `futex_q`, `futex_hash_bucket` and PI state machinery
  - The kernel side of the primitive, including why private and shared futexes are keyed differently.

### Tools

- **[Tool · ★★★ · EN]** **ThreadSanitizer (TSan)** — GCC and Clang, `-fsanitize=thread`
  - The default tool for data races. If you only add one thing to a concurrency test plan, add this.
- **[Tool · ★★ · EN]** **rr** (`rr-project.org`) — record and replay
  - Makes a racy failure deterministic, which is otherwise the hardest part of debugging concurrency.
- **[Tool · ★★ · EN]** **valgrind / helgrind** — race and lock-order detection without a rebuild; slower, but it needs no instrumentation.
- **[Tool · ★★ · EN]** **perf** (`perf sched record`, `perf sched latency`) and **trace-cmd / KernelShark** with the `sched_switch` and `sched_wakeup` tracepoints
  - The visual timeline of who ran when, and who waited for whom.

---

## 04-6 · Linux Device Drivers — Model, Probe, Data Path, Power and Bring-Up
### Books

- **[Book · ★★★ · EN]** **Linux Device Drivers**, 3rd ed. — Jonathan Corbet, Alessandro Rubini, Greg Kroah-Hartman · O'Reilly, 2005 · ISBN 978-0-596-00590-7 · free at `lwn.net/Kernel/LDD3/`
  - The narrative account of the character driver, the device model and the interrupt path. Specific APIs have moved on — `cdev` replaced the old registration, devres removed the teardown ladder, threaded IRQs changed the interrupt story — so read it for the model and check every call against `Documentation/`.
- **[Book · ★★★ · EN]** **Linux Kernel Development**, 3rd ed. — Robert Love · Addison-Wesley, 2010 · ISBN 978-0-672-32946-3
  - The device model, interrupts and bottom halves, and kernel synchronisation at exactly the depth §3, §7 and §12 of the note need. The shortest correct route into the driver core.
- **[Book · ★★ · EN]** **Essential Linux Device Drivers** — Sreekrishnan Venkateswaran · Prentice Hall, 2008 · ISBN 978-0-13-239655-4
  - The bus-by-bus tour: I2C, SPI, PCI, USB, video, audio and the kernel classes. The practical counterpart to §10 and §11.
- **[Book · ★★ · EN]** **Professional Linux Kernel Architecture** — Wolfgang Mauerer · Wrox, 2008 · ISBN 978-0-470-34343-2
  - `struct device`, kobjects, sysfs internals and the power-management framework at reference depth.
- **[Book · ★★ · EN]** **Linux Device Drivers Development** — John Madieu · Packt, 2017 · ISBN 978-1-78439-512-8
  - Modern-API coverage: device tree, regmap, IIO and the `devm_*` idioms of §4, written against a recent kernel.
- **[Book · ★★ · EN]** **Embedded Linux Primer: A Practical Real-World Approach**, 2nd ed. — Christopher Hallinan · Prentice Hall, 2010 · ISBN 978-0-13-701782-9
  - Board bring-up, bootloaders and the device-tree-to-probe path from the embedded side rather than the maintainer side.
- **[Book · ★ · EN]** **Mastering Embedded Linux Programming**, 3rd ed. — Frank Vasquez, Chris Simmonds · Packt, 2021 · ISBN 978-1-78995-253-9
  - Build systems, root filesystems and the cold-board-to-shell workflow that §14 assumes.

### Kernel documentation — the primary source, always

- **[Doc · ★★★ · EN]** **The Linux Kernel documentation** — `docs.kernel.org`
  - `driver-api/driver-model/` (overview, `device`, `driver`, `bus`, `class`, `devres`, `platform`), `driver-api/pm/` (`runtime_pm`, `devices`, `drivers`), `core-api/` (locking, `genericirq`, `dma-api`, `dma-api-howto`), `devicetree/` (`usage-model`, `bindings`, `overlay-notes`), `process/` (`submitting-patches`, `coding-style`, `stable-api-nonsense`).
- **[Doc · ★★★ · EN]** **Documentation/admin-guide/devices.txt**
  - The registry of statically assigned major and minor numbers, and the note that 384-511 is reserved for dynamic assignment. The source of §6.1 and of the Anchors.
- **[Doc · ★★★ · EN]** **Linux man-pages** — `man7.org/linux/man-pages/`
  - `open(2)`, `read(2)`, `ioctl(2)`, `poll(2)`, `mmap(2)`, `close(2)`, `udev(7)`, `sysfs(5)`, `signal(7)` — the userspace half of every contract in §6.
- **[Code · ★★★ · EN]** **Bootlin Elixir cross-referencer** — `elixir.bootlin.com/linux/latest/source`
  - The fastest way to check whether the API you are about to cite still exists and what its current signature is.
- **[Doc · ★★ · EN]** **Documentation/trace/ftrace.rst** and **Documentation/admin-guide/dynamic-debug-howto.rst**
  - The normative versions of the two tools in §14.2 that you will actually use during bring-up.

### Standards and specifications

- **[Standard · ★★★ · EN]** **Devicetree Specification** — `devicetree.org/specifications/`
  - The normative text behind `compatible`, `reg`, `interrupts`, `#address-cells`, and the binding rules quoted in §4.1 — including why `compatible` is a list ordered most-specific-first.
- **[Standard · ★★ · EN]** **PCI Express Base Specification** — `pcisig.com`
  - Configuration space, BARs and MSI/MSI-X: everything that makes §10.3 different from the rest of the note.
- **[Standard · ★★ · EN]** **IEEE Std 1275-1994 / Open Firmware** — the ancestor of the device tree and of the `compatible` property's semantics.
- **[Standard · ★ · EN]** **ACPI Specification** — `uefi.org`
  - The non-DT discovery path and `_DSD` device properties: the server counterpart to §4.1.

### Papers, talks and articles

- **[Paper · ★★★ · EN]** Corbet, J. **"The managed resource API"** — LWN, 2007 · `lwn.net/Articles/222860/`
  - Why devres exists and what it covers; §4.3 in three pages.
- **[Paper · ★★★ · EN]** **"Driver Core: devtmpfs — kernel-maintained tmpfs-based /dev"** — LWN, 2009 · `lwn.net/Articles/345480/`
  - Kay Sievers' own description of the mechanism and of the intended division of labour with udev, quoted in §3.2.
- **[Paper · ★★★ · EN]** Corbet, J. **"Deferred driver probing"** — LWN, 2011 · `lwn.net/Articles/450460/`
  - The OLPC camera problem that produced `-EPROBE_DEFER`: the anecdote that makes §3.4 memorable.
- **[Paper · ★★★ · EN]** Kannan, S. **"fw_devlink: Device dependency tracking"** — Linux Plumbers Conference 2024 · `lpc.events/event/18/contributions/1734/`
  - What the four `fw_devlink` modes do, how many DT properties are parsed, and how the deferred-probe timeout now extends itself when a new driver registers.
- **[Paper · ★★ · EN]** Kleine-König, U. **"[PATCH] platform: Make platform_driver::remove() return void"** — LKML, May 2024 · `lore.kernel.org/all/20240527083416.1177106-2-u.kleine-koenig@pengutronix.de/`
  - The commit message states the reason better than any secondary source: the old return value was ignored by the driver core, and drivers wrote error handling that could not work.
- **[Paper · ★★ · EN]** **"Rust in the Linux kernel"** — `rust-for-linux.com`, and LWN's **"The (successful) end of the kernel Rust experiment"**
  - The milestones in the Anchors: 6.1 infrastructure, the v6.8 ASIX PHY reference driver, and the December 2025 change of status. Worth knowing even if you write C, because it is where new driver abstractions are being built first.

---

## Standards and repositories

- **FreeRTOS** — `freertos.org` (kernel book, API reference, LTS release notes).
- **Zephyr Project** — `zephyrproject.org` and `docs.zephyrproject.org` (releases, migration guides, devicetree, power management, MCUboot).
- **AUTOSAR** — `autosar.org/standards` (Classic Platform, Adaptive Platform, Foundation, Application Interfaces; current release R25-11).
- **ISO / IEC** — `iso.org`, `iec.ch` (ISO 26262:2018, IEC 61508, IEC 62304; purchased, not free).
- **The Linux kernel** — `kernel.org` and the in-tree `Documentation/`.
- **Yocto Project** — `docs.yoctoproject.org` · **Buildroot** — `buildroot.org/downloads/manual`.


---

_Copyright (c) 2026 Washington Ruan and contributors · licensed under **GPL-3.0-or-later** or **AGPL-3.0-or-later**, at your option · see `LICENSE` and `LICENSE-AGPL`._
