---
title: Reading list — LANGUAGES · Programming languages and practice
lang: en
category: reading-list
license: GPL-3.0-or-later OR AGPL-3.0-or-later
last-updated: 2026-10-29
---

# Reading list — LANGUAGES · Programming languages and practice

> The languages and the measurement discipline: toolchain and performance engineering, C and C++, Python, MATLAB/Simulink, and Verilog HDL.
>
> One section per note, numbered `GG-x`. Where a note needed no source beyond its own
> **References**, there is no section here — the note is self-sufficient.

## How to use this list

- **Marks.** Type and priority marks (`★★★`, `[Book]`, `[EN]`) are defined once, in the MOC under *Reading marks*. The rule that matters: `★★★` means read or skim before you quote the note in an interview.
- **Titles** are kept in their published form and never translated; descriptions are English.
- **Nothing is asserted.** Where a citation could not be confirmed against a publisher, DOI, arXiv record or the issuing body, it is marked `VERIFY`.

---

## 08-1 · Languages, Toolchain and Performance Engineering
### Books

- **[Book · EN · ★★★]** *Computer Systems: A Programmer's Perspective*, 3rd ed. — Bryant, O'Halloran (see §05-2)
  - Memory hierarchy, cache behaviour, linking, and the cost model behind every performance claim. If you only read one performance book, read this.
- **[Book · EN · ★★★]** *Systems Performance: Enterprise and the Cloud*, 2nd ed. — Brendan Gregg · Addison-Wesley, 2020
  - The methodology: the USE method, workload characterisation, drill-down analysis, and the counterintuitive results that come from measuring before theorising. Covers CPU, memory, file systems, disk and network.
- **[Book · EN · ★★]** *BPF Performance Tools: Linux System and Application Observability* — Brendan Gregg · Addison-Wesley, 2019
  - The BCC and bpftrace toolchain in practice. eBPF is now the standard way to get production-visible tracing without redeploying, which matters for on-device and edge systems where you cannot restart to instrument.
- **[Book · EN · ★★]** *Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14* — Scott Meyers · O'Reilly, 2014
  - Move semantics, smart pointers, lambda correctness and type deduction. The difference between "C++ that works" and "C++ that is safe and fast".
- **[Book · EN · ★★]** *C++ Concurrency in Action*, 2nd ed. — Anthony Williams · Manning, 2019
  - Memory model, atomics, memory ordering and lock-free design. Essential for dataplane and inference-engine work where the concurrency is real, not theoretical.
- **[Book · EN · ★★]** *Is Parallel Programming Hard, And, If So, What Can You Do About It?* — Paul E. McKenney · freely available
  - The definitive treatment of RCU, memory ordering and scalable synchronisation, written by a kernel maintainer. Read before designing any lock-free structure.
- **[Book · EN · ★]** *Operating Systems: Three Easy Pieces* — R. H. Arpaci-Dusseau, A. C. Arpaci-Dusseau · freely available
  - Virtualisation, concurrency and persistence explained cleanly. Good for filling conceptual gaps without a textbook budget.

---

## 08-2 · C and C++ Programming — Language Features, STL and Systems Practice
Supports vault note `16`. Note that §13 covers toolchain, profiling and performance engineering; this section is the language itself.

### Books — C

- **[Book · EN/CN · ★★★]** *The C Programming Language*, 2nd ed. — Brian W. Kernighan, Dennis M. Ritchie · Prentice Hall, 1988 · ISBN 9780131103627 · Chinese 《C程序设计语言(第2版·新版)》, translated by 徐宝文, 李志 · 机械工业出版社, 2004 · ISBN 9787111128069 (典藏版 reissue ISBN 9787111617945)
  - Written by the language's designer. Still the clearest account of pointers, arrays and the preprocessor — and still thin on the parts the standard later changed. Read it for the model, then read a modern text for C11/C23.
- **[Book · EN · ★★★]** *Modern C* — Jens Gustedt · Manning, 2019 (2nd ed. 2022, freely available online)
  - The modern replacement for K\&R: written by a WG14 member and organised around C17/C23 rather than C89. Covers `stdint.h`, atomics, alignment, `_Generic`, and the undefined-behaviour traps that K\&R never had to warn about. **This is the C book to read if you already know C.**
- **[Book · EN · ★★]** *C Programming: A Modern Approach*, 2nd ed. — K. N. King · W. W. Norton, 2008 · ISBN 9780393979503
  - The best teaching text on the language: exhaustive, precise about the standard, and unusually good on the "why is this undefined" questions.
- **[Book · EN · ★★]** *Expert C Programming: Deep C Secrets* — Peter van der Linden · Prentice Hall, 1994 · ISBN 9780131774292
  - Old, but the chapters on array/pointer equivalence, declaration parsing, and linker/memory layout still explain things no current book does as well.
- **[Book · EN · ★]** *21st Century C*, 2nd ed. — Ben Klemens · O'Reilly, 2014
  - How to write C as it is actually written now: build tooling, unit testing with a real framework, and using the standard library instead of reinventing it.

### Books — C++ language

- **[Book · EN/CN · ★★★]** *C++ Primer*, 5th ed. — Stanley B. Lippman, Josée Lajoie, Barbara E. Moo · Addison-Wesley, 2012 · ISBN 9780321714114 · Chinese 《C++ Primer 中文版(第5版)》, translated by 王刚, 杨巨峰 · 电子工业出版社, 2013 · ISBN 9787121155352
  - The most complete single-volume tutorial, rewritten for C++11. Use it as the reference for the core language — types, classes, templates, the standard library — and supplement it for C++17/20/23.
- **[Book · EN/CN · ★★★]** *The C++ Programming Language*, 4th ed. — Bjarne Stroustrup · Addison-Wesley, 2013 · ISBN 9780321563842 · Chinese 《C++程序设计语言(特别版)》 translated by 裘宗燕 · 机械工业出版社 · ISBN 9787111102029
  - The language from its author. Less tutorial, more "what the abstraction means and what it costs" — which is the framing interviewers reward.
- **[Book · EN · ★★★]** *Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14* — Scott Meyers · O'Reilly, 2014 (see §08-1)
  - Type deduction, `auto`, move semantics, smart pointers and lambda correctness. Pair it with *Effective C++*, 3rd ed. (ISBN 9780321334879, Chinese 《Effective C++ 改善程序与设计的55个具体做法》, 机械工业出版社) for the pre-C++11 core.
- **[Book · EN · ★★]** *A Tour of C++*, 3rd ed. — Bjarne Stroustrup · Addison-Wesley, 2022
  - The shortest accurate overview of modern C++ as a whole language, covering C++20 and C++23 in ~250 pages. Read this first if your C++ knowledge stopped at C++11.
- **[Book · EN · ★★]** *C++ Templates: The Complete Guide*, 2nd ed. — David Vandevoorde, Nicolai M. Josuttis, Douglas Gregor · Addison-Wesley, 2017 · ISBN 9780321714121
  - Everything about templates: deduction, specialisation, variadics, SFINAE, trait and policy-based design, and compile-time cost. The book to own if templates appear in your job description.
- **[Book · EN/CN · ★★]** *Inside the C++ Object Model* — Stanley B. Lippman · Addison-Wesley, 1996 · Chinese 《深度探索C++对象模型》, translated by 侯捷 · 华中科技大学出版社, 2001 · ISBN 9787560924182
  - How virtual functions, inheritance, and object layout are actually implemented — vptr/vtable placement, the cost of multiple and virtual inheritance. Answers "what does a virtual call really cost" at the representation level.
- **[Book · EN · ★★]** *C++ Software Design* — Klaus Iglberger · Addison-Wesley, 2022
  - Design-level C++: value semantics, type erasure, CRTP, policy-based design, and *when not to use inheritance*. Strong on the patterns that replace OOP in performance-sensitive code.
- **[Book · EN · ★]** *C++23 — The Complete Guide* and *C++ Move Semantics — The Complete Guide* — Nicolai M. Josuttis · C++20 and C++17 volumes also exist; all freely available online
  - Feature-by-feature guides to a single standard, with compiler-support tables. The fastest way to check "which standard did X arrive in".

### Books — STL and standard library

- **[Book · EN/CN · ★★★]** *The C++ Standard Library: A Tutorial and Reference*, 2nd ed. — Nicolai M. Josuttis · Addison-Wesley, 2012 · ISBN 9780321623218 · Chinese 《C++标准库(第2版)》, translated by 侯捷, 孟岩 · 华中科技大学出版社
  - The STL reference with explanations: every container, iterator, algorithm and functor, plus the trade-offs. If you need one STL book, this is it.
- **[Book · EN/CN · ★★★]** 《STL源码剖析》 (The Annotated STL Sources) — 侯捷 · 华中科技大学出版社, 2002 · ISBN 9787560926995
  - A source-level walkthrough of the SGI/STLPort implementation: allocators and memory pools, iterator traits, the sequence containers, red-black tree and hash table, algorithms, functors and adapters. Reading the implementation is how you learn *why* `vector` beats `list` and what a traits mechanism is for. Based on a pre-C++11 implementation, so read it for mechanism, not for API.
- **[Book · EN · ★★]** *Effective STL: 50 Specific Ways to Improve Your Use of the Standard Template Library* — Scott Meyers · Addison-Wesley, 2001 · ISBN 9780201749625
  - Dated in places (no move semantics), still the sharpest writing on container selection, iterator invalidation, and the algorithm-vs-hand-written-loop decision.
- **[Book · EN · ★]** *Hands-On Design Patterns with C++*, 2nd ed. — Fedor Pikus · Packt, 2022
  - C++-specific patterns including CRTP, type erasure, the policy pattern and lock-free structures, with performance measurements.

### Standards and committee documents

- **[Standard · ★★★]** **ISO/IEC 9899:2024** (C23) — WG14. Closest free draft: **N3220**. `__STDC_VERSION__` = `202311L`
- **[Standard · ★★★]** **ISO/IEC 14882:2026** (C++26) — WG21. Working draft **N5046**, shipped by WG21 on **28 March 2026**
- **[Spec · ★★★]** **WG21 papers** (`open-std.org/jtc1/sc22/wg21/docs/papers`), and **WG14 papers** (`open-std.org/jtc1/sc22/wg14`). Key C++26 papers: **P2996** reflection · **P2900** contracts · **P2300** `std::execution` · **P1928** `std::simd` · **P1673** `std::linalg` · **P0843** `std::inplace_vector` · **P0447** `std::hive` · **P3471** library hardening · **P2795** erroneous behaviour · **P1306** expansion statements · **P2530** hazard pointers · **P2545** RCU · **P0429** `flat_map` · **P1222** `flat_set` · **P1967** `#embed`
  - Read the paper, not the blog post. Each one states the problem, the design alternatives considered, and the cost — which is exactly what an interviewer asks about.
- **[Doc · ★★★]** **cppreference.com** — the de facto standard library reference, with per-standard version markers and per-compiler support tables
- **[Doc · ★★]** **C++ Core Guidelines** — Bjarne Stroustrup, Herb Sutter · `isocpp.github.io/CppCoreGuidelines`, with the associated GSL
  - The closest thing to a house style for modern C++: ownership, lifetime, interfaces, error handling and performance, each with a stated rationale.
- **[Doc · ★★]** **GCC C++ status page** (`gcc.gnu.org/projects/cxx-status.html`) and **libc++/libstdc++ implementation status pages**
  - Where to check whether a feature you want to quote is actually available in your compiler version.
- **[Doc · ★]** **Compiler Explorer** (`godbolt.org`) — for checking codegen, especially whether a construct vectorises or allocates

### Papers and talks

- **[Paper · ★★]** *"A Tour of C++"* / Stroustrup's **"The Design and Evolution of C++"** and **"Thriving in a Crowded and Changing World: C++ 2006–2020"** (ACM HOPL IV, 2020)
  - The history is useful: knowing *why* a feature exists (compatibility, zero-overhead, evolving hardware) is what lets you defend a language choice under questioning.
- **[Paper · ★★]** *"Memory Ordering in C++"* and Paul E. McKenney's **perfbook** (see §08-1)
  - The memory model is the part of C++ most people get wrong. Read the model, not the rules of thumb.
- **[Doc · ★]** **CppCon talks** on `std::execution` (senders/receivers), reflection (P2996), and `std::simd` — the fastest route to C++26 material, since no book covers it yet.

---

## 08-3 · Python Programming — Language, Object Model and Engineering Practice
### Books

- **[Book · ★★★]** *Fluent Python: Clear, Concise, and Effective Programming*, 2nd ed. — Luciano Ramalho, O'Reilly, 2022. ISBN 978-1-492-05635-5. [EN]
  - The reference for the data model: dunder protocols, descriptors, MRO, generators. Read Part I and Part IV before any interview that claims Python fluency.
- **[Book · ★★★]** *Effective Python: 90 Specific Ways to Write Better Python*, 2nd ed. — Brett Slatkin, Addison-Wesley, 2019. ISBN 978-0-13-485398-7. [EN]
  - Item-level advice with the "why"; the chapters on closures, generators and concurrency map directly onto interview questions.
- **[Book · ★★]** *Python Cookbook*, 3rd ed. — David Beazley and Brian K. Jones, O'Reilly, 2013. ISBN 978-1-449-34037-7. [EN]
  - Recipe-level: iterators, `__slots__`, wrapping C libraries with `ctypes`, mixing threads and processes.
- **[Book · ★★]** *Python for Data Analysis*, 3rd ed. — Wes McKinney, O'Reilly, 2022. ISBN 978-1-098-10403-0. [EN]
  - Written by NumPy/pandas' author; the clearest account of the array-and-label model behind KPI analysis.
- **[Book · ★★]** *High Performance Python*, 2nd ed. — Micha Gorelick and Ian Ozsvald, O'Reilly, 2020. ISBN 978-1-492-05502-0. [EN]
  - The measurement-first approach: profiling, memory, C extensions, multiprocessing, and when each one actually helps.
- **[Book · ★]** *CPython Internals* — Anthony Shaw, Real Python, 2021. [EN]
  - Compiler pipeline, frames, the evaluation loop and object representation, written for people who want to reason about CPython rather than about Python.


### Documentation and specifications

- **[Doc · ★★★]** *The Python Language Reference* and *The Python Data Model*. <https://docs.python.org/3/reference/> [EN]
  - The data model chapter is the normative description of every dunder method; read it once end to end.
- **[Doc · ★★★]** *What's New In Python 3.15* (released 2026-10-09). <https://docs.python.org/3/whatsnew/3.15.html> [EN]
  - Lazy imports (PEP 810), `frozendict` (PEP 814), UTF-8 default (PEP 686), Tachyon profiler (PEP 799).
- **[Standard · ★★]** PEP 8 (style), PEP 484 (type hints), PEP 544 (Protocols), PEP 557 (dataclasses), PEP 659 (adaptive interpreter), PEP 703 (free-threading), PEP 779 (free-threading support status). <https://peps.python.org/> [EN]
- **[Doc · ★★]** *asyncio* documentation — task groups, timeouts, cancellation, the event loop. <https://docs.python.org/3/library/asyncio.html> [EN]
- **[Standard · ★★]** NumPy *NEP 50* — promotion rules for Python scalars, the change that broke dtype assumptions in NumPy 2.0. <https://numpy.org/neps/nep-0050-scalar-promotion.html> [EN]

### Papers and practice

- **[Paper · ★★★]** Harris, C. R., Millman, K. J., van der Walt, S. J., et al. "Array programming with NumPy." *Nature* 585, 357–362 (2020). DOI 10.1038/s41586-020-2649-2. [EN]
  - The canonical citation for why strided arrays with a dtype beat lists by two orders of magnitude.
- **[Code · ★★]** pybind11 and nanobind — C++ ↔ Python binding layers; the casters and GIL handling are the practical content. <https://pybind11.readthedocs.io/> · <https://nanobind.readthedocs.io/> [EN]
- **[Code · ★★]** Numba and Cython — JIT and ahead-of-time compilation of numeric Python. <https://numba.readthedocs.io/> · <https://cython.readthedocs.io/> [EN]
- **[Doc · ★★]** pytest, ruff, mypy, uv — the 2026 default toolchain for tests, lint, types and environments. [EN]

---

## 08-4 · MATLAB and Simulink — Programming, Modelling and Code Generation
### Books

- **[Book · ★★★]** *MATLAB Guide*, 3rd ed. — Desmond J. Higham and Nicholas J. Higham, SIAM, 2017. ISBN 978-1-611974-18-6. [EN]
  - The best-written account of the language itself: arrays, functions, object-oriented programming, and numerical quality. Written by numerical analysts, so the advice on conditioning is worth taking.
- **[Book · ★★★]** *Numerical Computing with MATLAB* — Cleve B. Moler, SIAM, 2004. ISBN 978-0-89871-660-3. [EN]
  - MATLAB's creator on the numerical methods behind the built-ins; explains why `\` is not `inv(A)*b`.
- **[Book · ★★]** *MATLAB: A Practical Introduction to Programming and Problem Solving*, 5th ed. — Stormy Attaway, Butterworth-Heinemann, 2019. ISBN 978-0-12-815479-3. [EN]
  - Fastest route for someone coming from C or Python; the chapter on vectorisation is the useful part.
- **[Book · ★★]** *Basic MATLAB, Simulink, and Stateflow* — Richard D. Colgren, AIAA Education Series, 2007. ISBN 978-1-56347-838-1. [EN]
  - Written for aerospace control work, which is exactly the audience that needs sample time and state machines explained together.
- **[Book · ★★]** *Simulation of Dynamic Systems with MATLAB and Simulink*, 3rd ed. — Harold Klee and Randal Allen, CRC Press, 2018. [EN]
  - Integrator theory, stiffness and solver selection treated as numerical analysis rather than as tool settings.

### Documentation

- **[Doc · ★★★]** *Object-Oriented Programming in MATLAB* — handle vs value classes, property validation, events, `matlab.System`. <https://www.mathworks.com/help/matlab/matlab_oop/object-oriented-programming.html> [EN]
- **[Doc · ★★★]** *Function Argument Validation* — the `arguments` block, validators, name-value arguments. <https://www.mathworks.com/help/matlab/matlab_prog/function-argument-validation-1.html> [EN]
- **[Doc · ★★★]** *Choose a Solver* — stiffness, variable vs fixed step, and the code-generation constraint. <https://www.mathworks.com/help/simulink/ug/choose-a-solver.html> [EN]
- **[Doc · ★★]** *Stateflow User's Guide* — hierarchy, temporal logic, truth tables, generated-code structure. <https://www.mathworks.com/help/stateflow/> [EN]
- **[Doc · ★★]** *Fixed-Point Designer* — `fi`, `fimath`, rounding and overflow modes, word-length analysis. <https://www.mathworks.com/help/fixedpoint/> [EN]
- **[Doc · ★★]** *HDL Coder* and *Embedded Coder* — synthesizable subset, latency balancing, MISRA checking, SIL/PIL. <https://www.mathworks.com/help/hdlcoder/> · <https://www.mathworks.com/help/ecoder/> [EN]
- **[Doc · ★★]** *MATLAB and Simulink Release Notes* — R2026a (April 2026) and R2026b (24 September 2026) are the current pair. <https://www.mathworks.com/help/relnotes/> [EN]
- **[Doc · ★]** *5G Toolbox* — NR waveform generation, TDL/CDL channel models, reference measurement channels. <https://www.mathworks.com/help/5g/> [EN]

### Papers and practitioner material

- **[Doc · ★★]** "MATLAB R2026a has been released — What's new?" *MATLAB Blog*, 21 April 2026. <https://blogs.mathworks.com/matlab/2026/04/21/matlab-r2026a-has-been-released-whats-new/> [EN]
  - Release-level summary with worked examples: ODE automatic differentiation, `metafunction` introspection, Python 3.9–3.13 support.
- **[Doc · ★★]** "MathWorks Introduces Release 2026b of MATLAB and Simulink." Press release, 24 September 2026. [EN]
  - The variant-management, JSON data dictionary, custom-solver and TOML project changes that affect how a model is version-controlled.

---

## 08-5 · Verilog HDL — RTL Design, Verification and Synthesis Practice
### Books

- **[Book · ★★★]** *Verilog HDL: A Guide to Digital Design and Synthesis*, 2nd ed. — Samir Palnitkar, Prentice Hall, 2003. ISBN 0-13-044911-3. [EN]
  - The standard teaching text: language, modelling styles, synthesisable subset. Old, and still the clearest explanation of blocking vs non-blocking.
- **[Book · ★★★]** *SystemVerilog for Verification: A Guide to Learning the Testbench Language Features*, 3rd ed. — Chris Spear, Springer, 2012. ISBN 978-1-4614-0714-0. [EN]
  - Classes, virtual interfaces, mailboxes, constrained random and coverage — the class layer of the language, which plain Verilog does not have.
- **[Book · ★★]** *The Verilog Hardware Description Language*, 5th ed. — Donald E. Thomas and Philip R. Moorby, Springer, 2002. ISBN 978-0-7923-7621-7. [EN]
  - Written by Verilog's co-designer; the simulation semantics are explained from the scheduler's point of view.
- **[Book · ★★]** *FPGA Prototyping by Verilog Examples* — Pong P. Chu, Wiley-IEEE Press, 2008. ISBN 978-0-470-18532-2. [EN]
  - Working RTL for FSMs, UARTs, video and DSP blocks; useful because every example is complete and synthesizable.
- **[Book · ★★]** *Advanced FPGA Design: Architecture, Implementation, and Optimization* — Steve Kilts, Wiley-IEEE Press, 2007. ISBN 978-0-470-05437-6. [EN]
  - Pipelining, retiming, resource sharing and timing closure as architecture decisions rather than tool settings.

### Standards

- **[Standard · ★★★]** IEEE Std 1364-2005 — *IEEE Standard for Verilog Hardware Description Language*. [EN]
  - The last standalone Verilog standard; superseded by inclusion in IEEE 1800-2009.
- **[Standard · ★★★]** IEEE Std 1800-2023 — *IEEE Standard for SystemVerilog*, approved 6 December 2023. <https://ieeexplore.ieee.org/document/10458102> [EN]
  - The current normative text. Verilog is the synthesizable core of this document, not a separate standard.
- **[Standard · ★★]** IEEE Std 1800.2-2020 — *Universal Verification Methodology (UVM) Language Reference Manual*. <https://ieeexplore.ieee.org/document/9195920> [EN]
- **[Standard · ★]** IEEE Std 1076-2019 — *VHDL Language Reference Manual*, for the nine-state `std_logic` comparison. [EN]

### Papers and application notes

- **[Paper · ★★★]** Cummings, C. E. "Nonblocking Assignments in Verilog Synthesis, Coding Styles That Kill!" SNUG-2000. <https://www.sunburst-design.com/papers/> [EN]
  - The paper that settled the blocking/non-blocking convention the industry now follows.
- **[Paper · ★★★]** Cummings, C. E., and Mills, D. "Synchronous Resets? Asynchronous Resets? I am so confused! How will I ever know which to use?" SNUG-2002. [EN]
  - Reset strategy, and the async-assert/sync-release synchroniser that most designs need.
- **[Paper · ★★★]** Cummings, C. E. "Simulation and Synthesis Techniques for Asynchronous FIFO Design." SNUG-2002. [EN]
  - Gray-coded pointers, synchronised flags, and why the depth must exceed the synchroniser latency.
- **[Paper · ★★]** Cummings, C. E. "Clock Domain Crossing (CDC) Design & Verification Techniques Using SystemVerilog." SNUG-2008. [EN]
  - The taxonomy of crossings and the structure that makes each one checkable.

### Tools and open flows

- **[Code · ★★]** Verilator — compiles synthesizable Verilog to C++ for fast simulation. <https://verilator.org/guide/latest/> [EN]
- **[Code · ★★]** Yosys and OpenLane/OpenROAD with the SkyWater SKY130 PDK — a fully open synthesis-to-GDSII flow. <https://yosyshq.readthedocs.io/> · <https://openlane.readthedocs.io/> [EN]
- **[Code · ★]** Icarus Verilog and GTKWave — the long-standing open simulator and waveform viewer. <https://steveicarus.github.io/iverilog/> [EN]

---

## Standards and repositories

- **MISRA** — `misra.org.uk` (MISRA C:2025, MISRA C++:2023, and the MISRA Compliance documents).


---

_Copyright (c) 2026 Washington Ruan and contributors · licensed under **GPL-3.0-or-later** or **AGPL-3.0-or-later**, at your option · see `LICENSE` and `LICENSE-AGPL`._
