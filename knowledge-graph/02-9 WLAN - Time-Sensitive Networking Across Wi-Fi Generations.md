---
title: "WLAN — Time-Sensitive Networking over Wi-Fi: Research and Practice Across Generations"
type: domain-note
domain: wlan
group: "02"
series: "02-9"
tags:
  - wlan
  - wifi
  - tsn
  - time-sensitive-networking
  - 802-1as
  - gptp
  - 802-1qbv
  - 802-1cb
  - frer
  - scs
  - mscs
  - qos-characteristics
  - twt
  - rtWT
  - trigger-frame
  - mlo
  - tid-to-link
  - p-edca
  - npca
  - preemption
  - mapc
  - 60802
  - determinism
  - bounded-latency
  - industrial-wireless
copyright: "Copyright (c) 2026 Washington Ruan. All rights reserved."
last-updated: 2026-10-25
aliases:
  - Wi-Fi TSN
  - Wireless TSN
  - Wi-Fi Determinism
---

# WLAN — Time-Sensitive Networking over Wi-Fi: Research and Practice Across Generations

> Part of the [[00 MOC - Comms x Compute x AI Knowledge Graph|Comms × Compute × AI knowledge graph]] · group **02 · WLAN**

Every note in this group has quietly assumed that a frame eventually gets through.
[[02-8 WLAN - Scheduling - Channel Access, EDCA, OFDMA Resource Allocation, Airtime and Implementation]] ends with
the admission that EDCA gives you *priorities*, not *guarantees*: the medium is contended, the contention is
statistical, and the tail of the delay distribution belongs to whoever else is on the channel.
[[02-2 WLAN - Power Saving Mechanisms and Evolution]] introduced TWT as a way to make a station sleep, and left
the AP's side of the service period unexplored. [[02-6 WLAN - Multi-AP Roaming, Healing and Steering]] shows a
transition that can cost hundreds of milliseconds — an eternity next to a 1 ms control cycle.

This note is about the other half of the requirement: not "how fast" but "by when, every time". It walks the
problem from the numbers industrial and immersive applications actually demand, through the six structural reasons
Wi-Fi cannot offer them, to every mechanism the IEEE has built to close the gap, generation by generation:
802.11e → 802.11v → 802.11aa → 802.11mc → 802.11ak → 802.11ax → 802.11be → 802.11bn. It ends with what has
actually been measured, how to deploy it, and how to know when it is not working.

The single sentence to carry into an interview: **wired TSN bought determinism by owning the wire; Wi-Fi has to buy
it by owning the schedule, and every generation has bought a slightly larger piece of it.**

---

## 0. Vocabulary — say these precisely or the whole answer collapses

| Term | What it means here | What it is commonly confused with |
| --- | --- | --- |
| **TSN** | The IEEE 802.1 toolbox: time synchronisation, bounded latency, reliability, resource management. Not one standard. | "Low latency" — TSN is about the *bound*, not the mean |
| **Deterministic** | A bound that can be computed in advance and holds under a stated load and failure model | "Fast" / "prioritised" |
| **Bounded latency** | `P(latency > L) < ε` for a stated `L` and `ε`, under a stated traffic and interference model | Mean or median latency |
| **Jitter / PDV** | Variation of the one-way delay across packets of a stream | Latency itself |
| **Talker / Listener** | 802.1 terms for the producer and consumer of a stream | Client / server |
| **Stream** | An identified, unidirectional flow with a declared traffic specification | A TCP connection |
| **CNC / CUC** | Centralised Network Configuration (the network's scheduler of schedules) and Centralised User Configuration (the collector of talker/listener demands) | A Wi-Fi controller, an SDN controller |
| **Bridge delay** | The per-port-pair, per-traffic-class residence time a bridge reports so the CNC can compute the end-to-end bound | Queueing delay |
| **Gate / GCL** | 802.1Qbv's per-queue transmission gate and the Gate Control List that opens and closes it on a cycle | A Wi-Fi TXOP |
| **802.1AS** | gPTP — the Layer 2 profile of IEEE 1588 that distributes the shared clock every other mechanism depends on | NTP, the 802.11 TSF |
| **Syntonisation** | Frequency alignment, as opposed to *synchronisation*, which is time-of-day alignment | The same thing |
| **UP / TID / AC / TSID** | 802.1Q User Priority (0–7) → 802.11 Traffic Identifier (0–7) → Access Category (BK/BE/VI/VO) → Traffic Stream Identifier (8–15 in later work) | Each other |
| **Service period** | A scheduled interval in which a station (TWT) or a queue (Qbv) is allowed to use the medium | A TXOP (which is won, not granted) |
| **MSDU Delivery Ratio** | The fraction of MSDUs a stream needs delivered within its delay bound | Packet error rate |

Two clarifications that prevent most arguments:

1. **TSN is a Layer 2 toolbox, not a wireless one.** Most of it is media-agnostic in principle and wired in
   practice. Bringing it to Wi-Fi is not a port; it is a negotiation between a schedule that assumes a wire and a
   medium that assumes contention.
2. **A bound is a statement about a system, not a device.** "This AP supports r-TWT" says nothing about the bound
   unless the BSS is managed, every participant honours the schedule, and the neighbouring BSSs are accounted for.

---

## 1. What "time-sensitive" actually demands

The requirement does not arrive as "low latency". It arrives as four numbers, and they pull in different
directions.

```mermaid
graph TD
    A["Application requirement"] --> B["Cycle time<br/>how often the loop closes"]
    A --> C["Latency bound<br/>how late is too late"]
    A --> D["Reliability<br/>how many misses are allowed"]
    A --> E["Jitter / synchronisation<br/>how much the timing may wander"]

    B --> B1["Motion control 250 us to 4 ms<br/>PROFINET IRT cycle under 1 ms"]
    C --> C1["Closed loop 1 ms end to end<br/>XR motion to photon under 20 ms"]
    D --> D1["99.999 pct per transaction<br/>some profiles ask 99.9999"]
    E --> E1["1 us jitter implies better than<br/>plus or minus 500 ns sync"]

    B1 --> F["These four together are the contract"]
    C1 --> F
    D1 --> F
    E1 --> F
    F --> G["Everything below is how 802.11<br/>has learned to honour parts of it"]
```

The canonical industrial numbers, quoted consistently across the TSN literature: a closed-loop control transaction
must complete **within a 1 ms cycle time** with **99.999 %** reliability, and the delivery jitter of responses is
constrained to **1 µs**, which in turn requires synchronisation accuracy better than **±500 ns** among devices.
PROFINET isochronous real-time (IRT) states the same thing from the application side: **clock rate under 1 ms and
jitter under 1 µs**, achieved with hardware support in the device. IEC/IEEE 60802, the TSN profile for industrial
automation, allows a **synchronisation error of 0.1–1 µs from the grandmaster**.

Those are wired numbers. The whole question of this note is how much of them survives a shared, contended,
unlicensed medium.

### 1.1 The budget you have to fit inside

A time-sensitive packet's one-way delay decomposes the same way on every hop, and the decomposition is what turns
"we need 1 ms" into an engineering task.

```mermaid
flowchart LR
    T["Talker<br/>application + stack"] --> E["Egress queue<br/>shaper or gate"]
    E --> M["Medium access<br/>contention or grant"]
    M --> P["Transmission<br/>frame at PHY rate"]
    P --> R["Retransmission<br/>MAC retry budget"]
    R --> B["Bridge or AP<br/>residence time"]
    B --> L["Listener<br/>stack + application"]

    E --> X1["Wired: bounded by the GCL"]
    M --> X2["Wireless: unbounded a priori<br/>this is the whole problem"]
    P --> X3["Long frames block everyone<br/>preemption is the wired answer"]
    R --> X4["Wireless: retry is per link<br/>and interacts with rate control"]
```

In a wired TSN network the middle terms are bounded by construction: the gate opens at a known instant, the frame
is the only thing on the wire, preemption caps the wait behind a long best-effort frame at roughly a microsecond
instead of roughly 12 µs at 1 Gbit/s. In Wi-Fi, every one of those four terms is a random variable at the start of
this story, and each generation of the standard has been an attempt to convert one of them into a constant.

---

## 2. Why Wi-Fi resists determinism — six structural reasons

Before listing mechanisms, it is worth writing down what they are fighting. Almost every Wi-Fi TSN feature maps
onto one of these six.

```mermaid
graph TD
    R1["1. Contention<br/>CSMA/CA is statistical"] --> L["Latency tail without a bound"]
    R2["2. Channel occupancy by others<br/>a TXOP won by anyone blocks everyone"] --> L
    R3["3. OBSS and hidden nodes<br/>interference is not observable at the transmitter"] --> L
    R4["4. Retransmission<br/>MAC retry until a limit not a deadline"] --> L
    R5["5. Rate adaptation<br/>MCS collapses under movement or interference"] --> L
    R6["6. No global schedule and no global clock<br/>every BSS is its own island"] --> L

    L --> C1["Consequence: the mean can be excellent<br/>while the 99th percentile is unusable"]
    L --> C2["Consequence: reliability and latency trade<br/>against each other through the retry budget"]
    L --> C3["Consequence: a guarantee inside one BSS<br/>does not survive the neighbour"]
```

| # | Structural property | What it costs | Which generation first attacked it |
| --- | --- | --- | --- |
| 1 | Contention is probabilistic | No bound at all, only a distribution | 802.11e (priorities), 802.11ax (granted access) |
| 2 | Anyone's TXOP blocks the channel | One long frame adds its full duration to your wait | 802.11e (TXOP limits), 802.11be (r-TWT), 802.11bn (preemption) |
| 3 | Interference arrives from unobservable places | Retries, rate collapse, unpredictable loss | 802.11ax (BSS colour, spatial reuse), 802.11bn (MAPC) |
| 4 | Retransmission is counted, not timed | A burst of retries can consume the whole cycle | 802.11aa (drop eligibility), 802.11be (delay-bound-aware scheduling) |
| 5 | Rate adaptation is reactive | The same frame takes 10× the airtime after a fade | 802.11be (link selection via TID-to-link), 802.11bn (MAPC, ELR) |
| 6 | No shared clock, no shared schedule | Nothing can be aligned across BSSs | 802.11v (TM), 802.11mc (FTM), 802.11be (r-TWT + 802.1AS) |

Reason 6 is the one that makes this a *systems* problem rather than a MAC problem: without a common clock there is
no "at time T", and without "at time T" there is no schedule, and without a schedule there is no bound. It is also
the reason the story starts, counter-intuitively, with synchronisation rather than with channel access.

---

## 3. The 802.1 toolbox, and what each tool becomes over Wi-Fi

TSN is not one standard. It is a toolbox maintained by the IEEE 802.1 Time-Sensitive Networking Task Group, which
grew out of the Audio Video Bridging Task Group and was renamed in **November 2012** when industrial and automotive
users arrived. Most amendments have since been rolled into the base bridging standard, so a datasheet may cite
either the amendment or plain 802.1Q.

| Tool | Year | What it does | The Wi-Fi counterpart, and its status |
| --- | --- | --- | --- |
| **802.1AS** (gPTP) | 2011, rev 2020, rev 2025 | Distributes one clock to sub-microsecond accuracy | Runs over 802.11 using **TM** (802.11v) and, in 802.1AS-2020, **FTM** (802.11mc). Works, but accuracy depends on timestamping in hardware |
| **802.1Qav** (CBS) | 2009 | Credit-based shaper; smooths a traffic class | No direct counterpart. EDCA is a strict-priority contention system, not a shaper |
| **802.1Qat** (SRP) | 2010 | Stream reservation | 802.11aa declared support for it; never widely used in Wi-Fi |
| **802.1Qbv** (TAS) | 2015 | Time-aware shaper: gates per queue on a repeating schedule | Approximated by **trigger-based access** and, in 802.11be, by **r-TWT service periods aligned to gate-open times** |
| **802.1Qbu** + **802.3br** | 2016 | Frame preemption: an express frame interrupts a long one | No Wi-Fi equivalent until **802.11bn preemption**. This is the single biggest structural gap |
| **802.1Qci** (PSFP) | 2017 | Per-stream filtering and policing at ingress | Partially covered by admission control (802.11e, extended by 802.11aa); no per-stream policing in the 802.11 MAC |
| **802.1CB** (FRER) | 2017 | Frame replication and elimination over disjoint paths | Emulated over **MLO**: duplicate across links, eliminate at the upper MAC. Weaker than disjoint paths |
| **802.1Qch** (CQF) | 2017 | Cyclic queueing and forwarding | Not mapped; the cyclic nature is closest to a periodic r-TWT SP |
| **802.1Qcc** | 2018 | Centralised configuration models, CNC/CUC interfaces | The model for Wi-Fi TSN: the AP as a bridge managed by a CNC |
| **802.1Qcr** (ATS) | 2020 | Asynchronous traffic shaping, no network-wide sync needed | Interesting for Wi-Fi precisely because it relaxes the clock requirement; not standardised over 802.11 |
| **802.1CS** (LRP) | 2020 | Link-local registration protocol | Not used in 802.11 |
| **802.1CM** | 2018, amended 2020 | TSN for fronthaul | The cellular analogue: a profile, not a mechanism |

Profiles exist because the toolbox is too big to specify directly — two vendors can both claim "TSN" and share
almost no features. The ones that matter here: **IEC/IEEE 60802** (industrial automation, published **29 June
2026**), **IEEE 802.1DG-2025** (automotive in-vehicle, published **6 June 2025**), **IEEE 802.1DP-2025 / SAE
AS6675** (aerospace), and **IEEE 802.1BA-2021** (the AVB systems profile, revised).

### 3.1 The integration architecture everyone draws

```mermaid
graph TD
    subgraph Wired["Wired TSN domain"]
        GM["Grandmaster clock"]
        BR["TSN bridges"]
        PLC["PLC controller<br/>talker"]
        Robot["Robot controller<br/>listener"]
    end

    subgraph Wireless["Wireless TSN domain"]
        AP["Wireless TSN AP<br/>802.11ak capable"]
        STA1["TSN STA<br/>with 802.1AS"]
        STA2["TSN STA<br/>with r-TWT"]
    end

    subgraph Control["Configuration plane"]
        CNC["CNC<br/>computes the schedule"]
        CUC["CUC<br/>collects the demands"]
    end

    PLC --> BR
    BR --> AP
    AP --> STA1
    AP --> STA2
    GM -.->|"802.1AS across wired and wireless"| AP
    AP -.->|"FTM or TM"| STA1
    AP -.->|"FTM or TM"| STA2
    CUC --> CNC
    CNC -.->|"GCL and stream config"| BR
    CNC -.->|"AP seen as a TSN bridge"| AP
    STA1 -.->|"talker or listener demands"| CUC
```

The architectural claim behind that picture is the important one: **the AP is presented to the wired network as a
TSN bridge**, with ports, a bridge delay, and a schedule. What happens between the AP and its stations is an
implementation detail the wired side never sees — provided the AP can state a bound for it and hold it.

---

## 4. Generation by generation — the Wi-Fi TSN ladder

```mermaid
graph LR
    E["802.11e<br/>2005<br/>EDCA HCCA TSPEC"] --> V["802.11v<br/>2011<br/>Timing Measurement"]
    V --> AA["802.11aa<br/>2012<br/>SCS intra-AC OBSS"]
    AA --> MC["802.11mc<br/>2016<br/>FTM 0.1 ns"]
    MC --> AK["802.11ak<br/>2018<br/>transit links"]
    AK --> AX["802.11ax<br/>2021<br/>OFDMA trigger TWT"]
    AX --> BE["802.11be<br/>2024<br/>r-TWT QoS Char MLO"]
    BE --> BN["802.11bn<br/>2028<br/>P-EDCA NPCA preemption MAPC"]

    E --> N1["priorities"]
    V --> N2["a clock"]
    AA --> N3["per-stream requests"]
    MC --> N4["a precise clock"]
    AK --> N5["a bridge port"]
    AX --> N6["granted access"]
    BE --> N7["protected periodic access"]
    BN --> N8["preemption and multi-AP schedules"]
```

### 4.1 802.11e-2005 — priorities, and the first honest attempt at reservation

802.11e gave Wi-Fi its four access categories and EDCA, which the Wi-Fi Alliance certified as **WMM** from 2004.
It also gave it two things that failed in the market and one that failed in the specification:

- **TSPEC** — a station describes its traffic to the AP and the AP admits or rejects. It failed because it asked
  applications for a large set of parameters they could not supply; 802.11be would later succeed by asking for
  four.
- **HCCA** — a centralised, polling-based scheduler in the AP. It failed partly on complexity and partly because
  nothing in the ecosystem needed it badly enough. 802.11aa tried again with coordinated CAPs between APs; it
  still did not ship.
- **Admission control** — survived, and is still the only mechanism in Wi-Fi that bounds *load*.

What 802.11e could not do, and it is worth being blunt about it: EDCA orders the queue, it does not bound the wait.
Under load, four access categories contend for a medium that any bystander can take.

### 4.2 802.11v-2011 — the first clock

Timing Measurement (TM) let a station and an AP exchange time-stamped action frames and compute an offset, with
**10 ns** timestamp resolution. This is what made 802.1AS operation over 802.11 possible at all: IEEE Std
802.11-2012 introduced support for TSN time synchronisation based on 802.1AS over the 802.11 TM protocol.

### 4.3 802.11aa-2012 — per-stream thinking arrives

"MAC Enhancements for Robust Audio Video Streaming" is the amendment where Wi-Fi first treated a *stream* as a
first-class object rather than a priority level:

- **SCS (Stream Classification Service)** — a station sends an SCS Request to the AP with a classifier and a
  requested treatment; the AP accepts or rejects. Unlike TSPEC, SCS attaches rules to a TID or 802.1Q User
  Priority, which made it far more usable.
- **Intra-AC prioritisation** — each of the voice and video queues splits into a *primary* and an *alternate*
  queue, so two video streams can be served differently.
- **Drop Eligibility Indicator (DEI)** — frames marked DEI get a shorter retry budget, so a stream degrades
  gracefully instead of consuming the channel.
- **OBSS management** — APs exchange load metrics, including medium occupancy and admitted stream counts, so
  admission control can consider neighbours.
- **GCR (GroupCast with Retries)** — reliable group-addressed delivery, which matters for industrial multicast.
- Support for **IEEE 802.1Qat** (SRP) was declared.

802.11aa is the amendment most often skipped in Wi-Fi histories and the one most worth knowing for this topic: it
is where the *vocabulary* of wireless TSN was established, eight years before r-TWT.

### 4.4 802.11mc / 802.11-2016 — a clock precise enough to schedule with

Fine Timing Measurement (FTM) refined the timestamp resolution from 10 ns to **0.1 ns** and was folded into IEEE
Std 802.11-2016. **IEEE 802.1AS-2020 specifies the use of FTM for TSN integration over 802.11.** This amendment
also carried the **Mirrored SCS (MSCS)** work: instead of the station declaring its downlink requirements
explicitly as in SCS, the AP observes the station's uplink flows and mirrors their QoS onto the downlink. That is
the answer to the real-world problem that downlink flows arriving from the public internet often have no usable
DSCP marking. The Wi-Fi Alliance states MSCS is defined in IEEE 802.11 REVmd, and it became mandatory for
**Wi-Fi CERTIFIED QoS Management**, launched **23 February 2021**.

### 4.5 802.11ak-2018 — Wi-Fi as a bridge port

IEEE Std 802.11ak-2018, "Enhancements for Transit Links Within Bridged Networks", amended 802.11 so that a wireless
link can be an *internal* connection inside an IEEE 802.1Q bridged network rather than an edge access link. It was
developed alongside **IEEE Std 802.1Qbz-2016** and **802.1AC-REV**, and was rolled into IEEE Std 802.11-2020.

This is the least glamorous and most load-bearing amendment in the whole story. Without it, a Wi-Fi link is a
network *edge*; with it, a Wi-Fi link is a *transit* link that a TSN bridge can schedule across. If someone asks
"how does 802.1Qbv reach a wireless segment", the first word of the answer is 802.11ak.

### 4.6 802.11ax-2021 — granted access

IEEE Std 802.11ax-2021 (published **19 May 2021**) changed what the AP can do with the medium:

- **OFDMA and MU-MIMO** — many stations in one transmission, so the AP's scheduling decision covers several
  streams at once.
- **Trigger-based uplink access** — the AP polls; the stations do not contend. This is the first time a Wi-Fi
  transmission is *granted* rather than *won* at scale, and it is the direct ancestor of everything deterministic
  that follows.
- **TWT** (individual and broadcast) — scheduled wake windows. Designed for power saving, but it is the first
  periodic, negotiated service period in the standard.
- **BSS colour and spatial reuse** — less time spent deferring to neighbours.

What 802.11ax did not do: protect the service period. A station that won a TXOP immediately before a TWT SP simply
overlaps it — the AP's schedule is a request, not a reservation.

### 4.7 802.11be-2024 — the TSN generation

IEEE Std 802.11be-2024 is the amendment where wireless TSN stops being research. Its PAR approved **21 March
2019**, the board approved it **26 September 2024**, and it was published **22 July 2025** (DOI
10.1109/IEEESTD.2024.11090080). Note what the PAR says: at least one mode capable of **30 Gbit/s** at the MAC SAP,
*and* "at least one mode of operation capable of improved worst case latency and jitter" — the first time latency
appeared in a Wi-Fi PAR, though unquantified.

The three mechanisms that matter, in the order the liaison to 802.1 listed them:

1. **QoS signalling — SCS with the QoS Characteristics element.** A station declares four mandatory parameters
   (Minimum Service Interval, Maximum Service Interval, Minimum Data Rate, Delay Bound), plus up to eight optional
   ones (Maximum MSDU Size, Service Start Time, MSDU Delivery Ratio and others), with a Control Info field carrying
   the **direction** (uplink, downlink, or direct link), TID and User Priority. Four parameters where TSPEC
   demanded a set applications could not populate — that change is why this one might ship.
2. **Restricted TWT (r-TWT)** for bounded latency.
3. **TID-to-link mapping** and **MLO** for reliability and for steering critical traffic to the best link.

The 802.11 working group's own summary, sent as a liaison to 802.1 in December 2022, reduces the mapping to a
three-row table: time synchronisation → 802.1AS over TM/FTM; bounded latency → 802.11ax scheduling plus SCS, r-TWT
and TID-to-link mapping; reliability → 802.1CB over multi-radio devices using MLO.

### 4.8 802.11bn (Wi-Fi 8) — quantified, at last

The 802.11bn PAR, approved **21 September 2023**, is the first Wi-Fi PAR to state latency as a number:

- at least **25 % higher throughput** at the MAC SAP at at least one SINR level (rate-vs-range),
- at least **25 % lower latency at the 95th percentile** of the latency distribution,
- at least **25 % lower MPDU loss**, especially for transitions between BSSs,
- reduced AP power consumption and improved peer-to-peer operation.

Schedule: first TG meeting November 2023, D1.0 July 2025, D2.0 WG letter ballot July 2026, final 802.11 WG
approval projected **March 2028**, RevCom **May 2028**. The Wi-Fi Alliance has planned certification for late 2027.

The significance is not the percentages. It is that Wi-Fi finally has a target that is *defined on the tail* — the
95th percentile, not the mean — which is exactly where Wi-Fi has always failed.

---

## 5. Time synchronisation over Wi-Fi — the foundation everything else stands on

Every scheduled mechanism needs a shared clock. Wi-Fi has always had one (the TSF), but the TSF is a beacon-timed
counter with microsecond-scale agreement across a BSS and no relationship to a grandmaster anywhere else. TSN
needs a clock that is traceable across wired and wireless domains.

```mermaid
sequenceDiagram
    participant GM as Grandmaster
    participant AP as Wireless TSN AP
    participant STA as TSN STA

    Note over GM,AP: 802.1AS gPTP over the wired domain
    GM->>AP: Sync + Follow_Up
    AP->>GM: Delay_Req
    GM->>AP: Delay_Resp
    Note over AP: AP holds the 802.1AS time base

    Note over AP,STA: 802.11 FTM exchange carries the wireless offset
    STA->>AP: FTM Request
    AP->>STA: ACK with t1
    AP->>STA: FTM frame with t1 and t4
    STA->>AP: ACK with t2 and t3
    Note over STA: STA computes offset and rate ratio then aligns its clock
    STA->>STA: syntonise frequency then synchronise time of day
```

Two procedures, with very different resolutions:

| Procedure | Introduced by | Timestamp resolution | Status |
| --- | --- | --- | --- |
| **TM** (Timing Measurement) | 802.11v, in 802.11-2012 | **10 ns** | The original 802.1AS-over-802.11 method |
| **FTM** (Fine Timing Measurement) | 802.11mc, in 802.11-2016 | **0.1 ns** | What **802.1AS-2020** specifies for 802.11 |

Resolution is not accuracy, and this is where most deployments fail. Published comparisons put **hardware
timestamping at 10–40 ns** against **software timestamping at around 1 µs** — and software timestamping is what
commodity Wi-Fi NICs and modems do. IEC/IEEE 60802 tolerates 0.1–1 µs of error from the grandmaster, so a
software-timestamped Wi-Fi segment can consume the entire synchronisation budget before a single frame is
scheduled.

```mermaid
graph TD
    A["Clock error budget<br/>0.1 to 1 us allowed by 60802"] --> B["Grandmaster error"]
    A --> C["Wired path asymmetry<br/>and residence time error"]
    A --> D["Wireless offset error"]
    D --> E["Timestamping method<br/>HW 10 to 40 ns vs SW about 1 us"]
    D --> F["FTM exchange rate<br/>drift between exchanges"]
    D --> G["Wireless asymmetry<br/>the air is symmetric by reciprocity not by construction"]
    E --> H["If SW timestamping then the wireless hop<br/>alone can exceed the whole budget"]
    F --> I["Long FTM intervals let the local oscillator<br/>drift between corrections"]
    G --> J["Contention delays one FTM frame and the<br/>offset estimate is biased"]
```

The practical rule: **you cannot schedule what you cannot timestamp in hardware.** An industrial wireless TSN
deployment that buys r-TWT-capable APs and software-timestamped clients has bought the mechanism and not the
guarantee.

---

## 6. Deterministic channel access — the ladder from "win the medium" to "be given the medium"

This is the heart of the subject. Five rungs, each closing one of the gaps in §2.

```mermaid
flowchart TD
    Start["A frame with a deadline arrives"] --> Q{"Is the medium granted or contended"}

    Q -->|"contended"| EDCA["EDCA<br/>four ACs different AIFS and CW<br/>result: prioritised not bounded"]
    EDCA --> Q2{"Can the AP grant the access"}
    Q2 -->|"no legacy or unmanaged"| Done1["Bound is not available<br/>engineer the load instead"]
    Q2 -->|"yes"| TRIG["Trigger based access 802.11ax<br/>AP polls stations do not contend"]

    TRIG --> Q3{"Does the grant recur periodically"}
    Q3 -->|"no"| Done2["Bounded within a TXOP<br/>not across a cycle"]
    Q3 -->|"yes"| TWT["TWT 802.11ax<br/>negotiated service periods"]

    TWT --> Q4{"Is the service period protected"}
    Q4 -->|"no legacy may overlap"| Done3["Periodic but not deterministic<br/>a bystander can take the slot"]
    Q4 -->|"yes"| RTWT["r-TWT 802.11be<br/>members only others must end TXOPs<br/>optional quiet interval"]

    RTWT --> Q5{"Can an urgent frame interrupt"}
    Q5 -->|"no"| Done4["Bounded latency inside the SP<br/>a long frame can still block its start"]
    Q5 -->|"yes 802.11bn"| PRE["Preemption and P-EDCA 802.11bn<br/>urgent traffic takes the medium"]

    PRE --> Q6{"Are neighbouring BSSs coordinated"}
    Q6 -->|"no"| Done5["Bound holds inside the BSS<br/>OBSS can still break it"]
    Q6 -->|"yes"| MAPC["MAPC 802.11bn<br/>coordinated schedules across APs"]
```

### 6.1 Rung 4 in detail — how r-TWT actually works

r-TWT is a **broadcast** TWT agreement with a marker: inside the TWT element, a Broadcast TWT Parameter Set whose
**Broadcast TWT Recommendation subfield is set to 4** identifies an r-TWT schedule. It is not a separate element,
which is why legacy stations cannot parse it and why sniffer decoders must look inside the TWT element rather than
filter for an r-TWT element ID.

The schedule is announced in **beacon and probe response frames**, so every station in the BSS knows when the
restricted windows occur. Two fields do the work:

- **Restricted TWT Traffic Info** — a TID bitmap per direction. Bit `p` set to 1 means TID `p` is treated as
  latency-sensitive in the uplink or downlink for this schedule. Frames of other TIDs from member stations still
  use ordinary EDCA.
- **Restricted TWT Schedule Info** — the current state of the schedule.

Three rules create the protected window:

1. **r-TWT-enabled stations must end their TXOPs before the SP start time.** This is the rule that produces an
   idle channel at the instant the window opens.
2. **The AP may announce a quiet interval aligned with the SP start** to quieten stations that are not members.
   Published evaluations model this at **1024 µs**.
3. **Inside the SP the AP triggers the members**, so the exchange is contention-free by construction.

```mermaid
sequenceDiagram
    participant AP as AP
    participant M as Member STA
    participant N as Non-member STA

    AP->>N: Beacon with TWT element and quiet element
    Note over N: non-member learns the SP start and the quiet interval
    N->>AP: ordinary EDCA traffic before the SP
    Note over N: must end its TXOP before the SP start
    Note over AP,M: quiet interval begins the channel is protected
    AP->>M: Trigger frame for the bound TIDs
    M->>AP: TB PPDU with latency sensitive frames
    AP->>M: BlockAck
    Note over AP,M: inside the SP no non-member may contend
    Note over N: SP ends and EDCA resumes
```

The state machine a station runs is small, and every bug in an r-TWT implementation lives on one of its edges:

```mermaid
stateDiagram-v2
    [*] --> Idle: associated and no schedule
    Idle --> Scheduled: beacon carries an r-TWT SP and the STA is capable
    Scheduled --> PreSP: SP start minus guard time reached
    PreSP --> InSP: SP start time
    InSP --> Doze: SP end and no more buffered units
    InSP --> PreSP: next SP in the schedule
    PreSP --> Scheduled: SP abandoned because the medium was not free
    Scheduled --> Idle: schedule withdrawn or disassociation
    Doze --> PreSP: next SP start approaches
    Doze --> Idle: agreement torn down
```

Two properties of this machine are worth stating explicitly, because they are what separates r-TWT from TWT:

| Property | TWT (802.11ax) | r-TWT (802.11be) |
| --- | --- | --- |
| Purpose | Energy saving | Bounded latency for declared traffic |
| Who may transmit in the SP | Anyone who contends successfully | Members, on the bound TIDs, when triggered |
| Protection of the SP start | None | TXOPs must end before it; optional quiet interval |
| Legacy stations | N/A | Not obliged to honour anything — they may interfere |
| Traffic binding | Per agreement | Per agreement **and** per TID bitmap |
| Status | Individual TWT is mandatory for certification | Optional, and intended for managed networks |

The last row is the practical caveat that dominates everything: **r-TWT is optional in 802.11be, and a single
legacy or non-participating station in the BSS can break the window.** The IEEE's own liaison said it plainly —
r-TWT "is expected to be used in managed networks where policies and tools are in place to ensure minimal
capabilities are required in alignment with the performance expectations". A café with one Wi-Fi 5 laptop does not
have a bound.

### 6.2 What the AP actually decides, per service period

```mermaid
flowchart TD
    A["SP start approaches"] --> B{"Which streams are bound to this SP"}
    B --> C["Read the SCS QoS Characteristics<br/>service interval min and max<br/>delay bound minimum data rate"]
    C --> D["Compute the deadline of each buffered MSDU"]
    D --> E{"Any MSDU whose deadline falls inside this SP"}
    E -->|"no"| F["Release the remaining airtime to EDCA"]
    E -->|"yes"| G["Allocate RUs or MU-MIMO to the members"]
    G --> H["Emit the trigger frame or transmit DL directly"]
    H --> I["Collect BlockAck and update the retry budget"]
    I --> J{"Deadline still reachable after retries"}
    J -->|"no"| K["Drop the MSDU and do not retry<br/>a late frame is a wrong frame"]
    J -->|"yes"| L["Carry the remainder into the next SP"]
```

That last decision is the conceptual break from ordinary Wi-Fi. Conventional MAC retry logic retries until a
*count* limit. Deadline-aware scheduling retries until a *time* limit, and then discards — because for a control
loop, a frame that arrives after the cycle has closed is worse than a frame that never arrives.

### 6.3 The evaluation literature on r-TWT, and what it can and cannot show

The most careful published evaluation to date (Mozaffariahrar, Wilhelmi, Galati-Giordano, Imputato, Menth and
Avallone, **ETFA 2025**, DOI 10.1109/ETFA65518.2025.11205686) used **ns-3** to compare r-TWT against power-save
mode and DCF across worst-case latency, energy efficiency, collision rate and throughput, for uplink UDP and TCP.
The findings: r-TWT achieves bounded latency for IoT and real-time traffic classes, improves energy efficiency and
collision rate over the legacy mechanisms, and stays stable as the network grows.

One methodological detail deserves attention because it constrains how far the result can be generalised: the
study **mimics restricted access using individual TWT with non-overlapping wake times**, rather than a full r-TWT
implementation. That is a faithful model of the *protection* and a partial model of the *signalling*. When citing
this work, say what it measured.

A second strand (Haxhibeqiri, Jiao, Shen, Pan, Jiang, Hoebeke and Moerman, **IEEE Communications Magazine**
62(8):118–124, August 2024, DOI 10.1109/MCOM.001.2300431) went in the opposite direction — a **real
implementation** of coordinated spatial reuse and r-TWT on the **openwifi** open-source SDR platform. That paper
matters for a different reason: it demonstrates that these mechanisms are implementable in firmware on real
hardware, not only in a simulator, and that the coordination between APs is the hard part rather than the SP
itself.

---

## 7. QoS signalling — from "describe everything" to "describe four numbers"

A bound can only be computed if the network knows what the traffic is. Three generations of mechanism, in
historical order, and the reason each one exists:

| Mechanism | Generation | What the station says | Why it succeeded or failed |
| --- | --- | --- | --- |
| **TSPEC** | 802.11e | A large traffic specification: nominal and peak MSDU size, mean and peak data rate, delay bound, surplus bandwidth allowance, and more | Failed in the market — applications cannot populate it |
| **SCS** | 802.11aa, extended in 802.11be | A classifier plus requested treatment, attached to a TID or User Priority | Survived, and is the basis of everything after |
| **MSCS** | REVmd (802.11-2020), certified from 2021 | Nothing explicit — the AP *mirrors* the uplink QoS onto the downlink | Solves the unmarked-downlink problem |
| **QoS Characteristics** | 802.11be | Four mandatory parameters and up to eight optional ones | The version that may ship |

The 802.11be QoS Characteristics element, carried in the SCS Descriptor of an SCS Request:

- **Control Info** — direction (uplink, downlink, or direct link for peer-to-peer), TID, User Priority, a presence
  bitmap for the optional parameters, and a link ID when the direction is a direct link.
- **Four mandatory traffic parameters** — Minimum Service Interval, Maximum Service Interval, Minimum Data Rate,
  and Delay Bound. The first two express periodicity; the third is in kbit/s at the MAC SAP; the fourth is the
  targeted maximum time to transport an MSDU or A-MSDU.
- **Up to eight optional parameters** — Maximum MSDU Size, Service Start Time, MSDU Delivery Ratio and others.

Two details that come up in design reviews: the TID field is set to the same value as the User Priority field in
802.11be (the separation exists to allow future expansion beyond eight TIDs); and the AP's obligation is stated in
terms of *enabling* rather than *guaranteeing* — an EHT AP "should" schedule downlink so that the requested delay
bound and minimum data rate are met. **How** the AP uses the information is not specified, which is precisely why
two conforming APs can behave very differently.

```mermaid
sequenceDiagram
    participant App as Application or TSN stack
    participant STA as Non-AP STA
    participant AP as AP
    participant Sched as AP scheduler

    App->>STA: traffic requirement from 802.1Qcc or local knowledge
    STA->>AP: SCS Request with SCS Descriptor and QoS Characteristics
    AP->>Sched: classify the flow then check admission
    alt resources available
        AP->>STA: SCS Response accepted with an SCS ID
        Note over AP,Sched: create or extend an r-TWT schedule for the stream
        AP->>STA: Beacon with the r-TWT schedule and TID bitmap
        STA->>AP: frames inside the SP on the bound TID
    else resources unavailable
        AP->>STA: SCS Response rejected with a status code
        Note over App: the application falls back to best effort
    end
    STA->>AP: SCS Request with Request Type Remove when the flow ends
```

```mermaid
stateDiagram-v2
    [*] --> Unclassified
    Unclassified --> Requested: SCS Request sent
    Requested --> Rejected: SCS Response with refusal
    Requested --> Admitted: SCS Response accepted
    Admitted --> Active: schedules in place and traffic flowing
    Active --> Degraded: delay bound missed repeatedly
    Degraded --> Active: conditions recovered
    Degraded --> Removed: stream abandoned or application gave up
    Active --> Removed: Request Type Remove or timeout
    Rejected --> Unclassified: backoff then optionally retry
    Removed --> [*]
```

The *Degraded* state is the one no standard specifies and every implementation needs. Something must decide when a
stream that is missing its bound should be renegotiated, downgraded, or torn down — and that something is policy,
living in the AP or in the CNC.

---

## 8. Reliability — 802.1CB over multiple links, and what redundancy cannot fix

802.1CB provides Frame Replication and Elimination for Reliability: send each frame over two disjoint paths, drop
the duplicate at the far end. It removes the loss due to a single link or node failure.

Wi-Fi has no disjoint paths in the wired sense, but MLO gives two or more links inside one device, and the IEEE's
own liaison describes the mapping: multiple links within an MLD can implement redundancy with a single 802.11
network interface, with the upper MLD MAC discarding the duplicated packets received by its affiliated lower MACs.

```mermaid
graph TD
    U["Upper MAC of the MLD"] --> R["Replication function"]
    R --> L1["Link 1 lower MAC<br/>for example 5 GHz"]
    R --> L2["Link 2 lower MAC<br/>for example 6 GHz"]
    L1 --> A1["Affiliated AP link 1"]
    L2 --> A2["Affiliated AP link 2"]
    A1 --> E["Elimination function at the peer"]
    A2 --> E
    E --> DU["Upper MAC of the peer MLD"]

    R --> W1["Caveat one: both links may share a radio front end"]
    R --> W2["Caveat two: adjacent bands can fade together"]
    R --> W3["Caveat three: duplication consumes airtime and can<br/>destroy the very bound it protects"]
```

That last caveat is the important one, and it is the reason redundancy in Wi-Fi is a decision rather than a
default. Duplicating every frame doubles the airtime the stream consumes. Under a tight delay bound, the extra
airtime raises everyone's latency, including the duplicated stream's.

```mermaid
flowchart TD
    A["Reliability requirement stated as a loss ratio"] --> B{"Is the loss dominated by<br/>collisions or by fades"}
    B -->|"collisions"| C["Fix the schedule first<br/>r-TWT and admission control"]
    B -->|"fades and shadowing"| D{"Are there two links with<br/>independent fading"}
    D -->|"no"| E["Redundancy will not help<br/>improve the link budget instead"]
    D -->|"yes"| F{"Is there airtime to spend"}
    F -->|"no"| G["Use selective duplication<br/>only the most critical frames"]
    F -->|"yes"| H["Duplicate over MLO links<br/>eliminate at the upper MAC"]
    C --> I["Re-measure then decide again"]
    H --> I
    G --> I
```

A useful way to say this in an interview: **in wired TSN, redundancy is nearly free because the paths are disjoint
and the capacity is not scarce; in Wi-Fi, redundancy is bought with the same currency as latency, so it has to be
budgeted like any other expense.**

---

## 9. Wi-Fi 8 (802.11bn) — where determinism becomes the objective

802.11bn is the first generation whose PAR is written in the language of this note. The mechanisms under
development divide cleanly into four groups.

### 9.1 Channel access — cutting the tail

- **P-EDCA (prioritised EDCA).** A station with an urgent frame sends a **defer signal** (a CTS variant referred to
  as DS-CTS) that temporarily excludes stations with non-urgent traffic from contending, while legacy stations
  continue with ordinary EDCA. The result is explicitly *not* higher average throughput: it is a tighter delay
  distribution, fewer spikes where a voice or game-input frame waits far longer than usual.
- **NPCA (non-primary channel access).** Every previous generation depends on the primary 20 MHz channel for beacons,
  trigger frames and channel announcements, so an OBSS busy on that channel blocks the entire 80/160/320 MHz
  bandwidth. NPCA lets a device use a different 20 MHz channel as a temporary primary. This is capacity work that
  shows up directly as a latency improvement.
- **Preemption.** Stop an ongoing transmission and start an urgent one. This is the Wi-Fi answer to 802.1Qbu and
  802.3br, and the last structural gap from §3 closes here.
- **LLI (low-latency indication).** A station that is a TXOP *responder* can report that it has buffered urgent
  traffic by setting an indication bit in a response frame, so the holder can grant it a slot in the current or
  next TXOP. This closes the signalling gap where the AP simply did not know a deadline was pending.
- **Group-based TXOP allocation** for low-latency peer-to-peer, and off-channel P2P coordination.

```mermaid
sequenceDiagram
    participant Legacy as Legacy STA
    participant Urgent as P-EDCA STA
    participant AP as AP

    Note over Legacy,Urgent: a TXOP has just ended
    Legacy->>Legacy: wait AIFS then backoff
    Urgent->>AP: DS-CTS defer signal
    Note over Legacy: non-urgent stations defer for the defer interval
    Urgent->>AP: P-EDCA PPDU with the urgent frame
    AP->>Urgent: ACK or BlockAck
    Note over Legacy: defer interval ends and ordinary EDCA resumes
```

```mermaid
stateDiagram-v2
    [*] --> Contending
    Contending --> Granted: TXOP acquired
    Granted --> Transmitting: urgent frame on air
    Granted --> Preempted: AP or peer preempts for higher urgency
    Transmitting --> Completed: frame acknowledged
    Preempted --> Suspended: transmission interrupted and state saved
    Suspended --> Resuming: medium returns
    Resuming --> Transmitting: remainder sent
    Completed --> [*]
    Transmitting --> Aborted: deadline passed
    Aborted --> [*]
```

The *Aborted* transition is worth noticing. Once deadlines are first-class, the MAC needs a rule for a frame whose
deadline expires mid-transmission, and that rule is "stop", not "finish".

### 9.2 Multi-AP coordination — the OBSS problem, finally addressed

Multi-AP coordination was discussed in 802.11be and postponed for specification complexity; 802.11bn took it up.
In essence it strengthens classical mechanisms — r-TWT, spatial reuse, beamforming — by making them work
cooperatively across BSSs: **Co-BF** (coordinated beamforming), **Co-SR** (coordinated spatial reuse), Co-OFDMA,
Co-CR, and coordinated r-TWT. This is the level at which reason 3 in §2 is attacked, and it is the only mechanism
in the whole note that can produce a bound that survives a neighbour.

```mermaid
graph TD
    subgraph BSS1["BSS 1"]
        AP1["AP 1"]
        S11["STA 1.1 time critical"]
        S12["STA 1.2 best effort"]
    end
    subgraph BSS2["BSS 2"]
        AP2["AP 2"]
        S21["STA 2.1"]
    end
    subgraph Coord["Coordination domain"]
        MA["Coordination group<br/>shares schedules and resource maps"]
    end
    AP1 --- MA
    AP2 --- MA
    MA --> R1["Coordinated r-TWT windows do not overlap"]
    MA --> R2["Co-SR sets transmit power so parallel TXOPs coexist"]
    MA --> R3["Co-BF nulls interference toward neighbour STAs"]
    R1 --> OUT["Bounded latency that survives an OBSS"]
    R2 --> OUT
    R3 --> OUT
```

### 9.3 Seamless mobility and the rest

**SMD (Seamless Mobility Domain)** defines a single entity spanning several AP MLDs — not necessarily in one
physical device — within which handshake states, sequence numbers, security keys and capabilities can be
transferred. It enables per-link transition of a client MLD between AP MLDs. For a mobile robot crossing cells,
this is the difference between a bound that holds and a bound with a 200 ms hole in it — the phenomenon
[[02-6 WLAN - Multi-AP Roaming, Healing and Steering]] describes from the client's side.

Also in scope, with latency relevance: **DSO** (dynamic subband operation) and **DBE** (dynamic bandwidth
expansion) for spectrum use; **ELR** (enhanced long range, 20 MHz, one spatial stream, BPSK/QPSK with
quadruplication for a 6 dB gain) and **DRU** (distributed-tone resource units, to raise uplink transmit power under
PSD limits) for the link budget; **PUO/DUO** (periodic and dynamic unavailability operation) for in-device
coexistence with Bluetooth and others, which is a real source of otherwise inexplicable latency spikes.

---

## 10. Wired–wireless integration — making the bound end to end

None of the above produces a *network* guarantee by itself. That requires the AP to behave as a bridge that can
state its own delay, and a controller that can add it up.

```mermaid
flowchart LR
    A["Talker residence time"] --> B["Talker egress gate wait<br/>802.1Qbv GCL"]
    B --> C["Wired bridge delays<br/>per port pair per traffic class"]
    C --> D["AP ingress to air<br/>queue plus access plus transmission"]
    D --> E["Air time including retries"]
    E --> F["STA to listener stack"]
    D --> G["This is the term only Wi-Fi owns<br/>and the one that must be bounded locally"]
    C --> H["5GS reports dependentDelayMin and Max<br/>per port pair and traffic class"]
```

In the 5G system, the analogue is explicit: the TSN Application Function computes the 5GS bridge delay from the
**UE–DS-TT residence time** plus the per-traffic-class minimum and maximum delay between the UE and the
UPF/NW-TT, and reports `dependentDelayMin` and `dependentDelayMax` as defined in IEEE 802.1Qcc. **Wi-Fi has no
equivalent normative quantity.** That absence is the deepest remaining difference between the cellular and Wi-Fi
answers to the same question, and it is why Wi-Fi TSN is usually deployed as an engineered system with measured
bounds rather than as a computed one.

### 10.1 Aligning the Qbv schedule with r-TWT

```mermaid
sequenceDiagram
    participant CNC as CNC
    participant Bridge as Wired TSN bridge
    participant AP as Wireless TSN AP
    participant STA as TSN STA

    CNC->>Bridge: GCL with gate open times for the stream
    CNC->>AP: AP presented as a TSN bridge port
    Note over AP: translate gate open times into r-TWT SP start times
    AP->>STA: Beacon with r-TWT schedule aligned to the GCL
    Note over Bridge,AP: frames arrive at the AP while its gate is open
    AP->>STA: trigger or DL transmission inside the r-TWT SP
    STA->>AP: uplink response inside the SP
    AP->>Bridge: response forwarded while the wired gate is open
```

The alignment is the whole trick: the r-TWT service period is placed so that the wireless hop happens *while the
wired gate is open*, which means the wireless segment has to be inside the wired cycle, and the wired cycle has to
be long enough to contain the worst-case wireless access delay. If the wireless worst case exceeds the gate-open
window, the schedule cannot be met by alignment alone and the cycle time has to grow.

### 10.2 The lifecycle of a stream in a managed network

```mermaid
stateDiagram-v2
    [*] --> Discovered
    Discovered --> Demanded: CUC collects talker and listener requirements
    Demanded --> Computed: CNC computes paths gates and service periods
    Computed --> Admitted: resources reserved on bridges and AP
    Admitted --> Running: traffic flows under the schedule
    Running --> Monitored: KPIs collected latency CDF loss and sync error
    Monitored --> Running: within bounds
    Monitored --> Violated: bound exceeded more than the allowed ratio
    Violated --> Computed: recompute with the observed behaviour
    Violated --> Rejected: no feasible schedule
    Rejected --> [*]
    Running --> Withdrawn: stream ends
    Withdrawn --> [*]
```

Note the *Monitored → Violated → Computed* loop. A deterministic network is not configured once; it is a control
loop, and the feedback signal — measured latency distributions, not averages — is what distinguishes a deployment
that holds its bound from one that held it on commissioning day.

---

## 11. The research landscape — what has actually been established, and how

It is worth separating three kinds of evidence, because they support very different claims.

| Layer | Method | Representative work | What it can support | What it cannot |
| --- | --- | --- | --- | --- |
| **Analytical** | Queueing and probability models of EDCA, TWT and r-TWT | Delay-distribution models for real-time traffic over r-TWT parametrised by SP and wake interval | Comparative insight and parameter choice | Absolute numbers for a real deployment |
| **Simulation** | ns-3, and purpose-built Wi-Fi 8 simulators such as Kom8ndor | The ETFA 2025 r-TWT evaluation; the 802.11bn MAPC tutorial with system-level results | Mechanism comparison at scale, sensitivity analyses | Claim that a specific product meets a specific bound |
| **Implementation** | Open-source SDR, notably openwifi | Coordinated SR and r-TWT implemented and measured on openwifi | Proof that the mechanism is implementable, and realistic overheads | Certification-grade conformance |
| **Standardisation** | Contributions, liaisons, TIG reports | The 802.11 RTA TIG report; the 802.11→802.1 TSN liaisons | The agreed direction and the agreed vocabulary | Nothing about shipped behaviour |
| **Profiles and certification** | IEC/IEEE 60802, 802.1DG, WFA programs | 60802 published 29 June 2026; Wi-Fi QoS Management from 2021 | Interoperability claims | That Wi-Fi segments are inside the profile's scope in every case |

Five findings are solid enough to state without hedging:

1. **Prioritisation is not determinism.** EDCA and WMM-era QoS improve the mean and do not bound the tail. Every
   serious study of latency-sensitive traffic over Wi-Fi reaches this conclusion in its first section.
2. **Granted access is the necessary step.** Trigger-based access is what converts a contended medium into a
   scheduled one; everything after 802.11ax is built on it.
3. **Protection of the service period is the sufficient step**, and it is only as strong as the least capable
   device in the BSS. r-TWT's guarantee is a property of a managed deployment, not of an AP.
4. **Time synchronisation is the binding constraint in practice.** Software timestamping on commodity hardware
   consumes the profile's entire synchronisation budget before scheduling begins.
5. **Multi-AP coordination is where the remaining uncertainty lives.** No single-BSS mechanism can bound the
   effect of a neighbouring BSS, which is why 802.11bn's MAPC is the most consequential item in the pipeline.

Three open problems are worth naming, because they are where a candidate can show they have thought rather than
read:

- **How does a Wi-Fi segment report a bridge delay?** 5G answers this with `dependentDelayMin/Max`; Wi-Fi has no
  normative equivalent, so the CNC has no standard number to add up.
- **What is the right failure model?** TSN bounds are computed under a stated failure model. For Wi-Fi, the honest
  model includes a bystander turning on a microwave, and no standard writes that down.
- **How should redundancy and latency share one budget?** Duplication for reliability consumes the airtime that
  bounded latency depends on, and the trade-off has no standard rule.

---

## 12. Application method — how to actually deploy this

Research findings do not deploy themselves. The practical procedure has nine steps, and the ordering matters
because each step can invalidate the one before it.

```mermaid
flowchart TD
    S1["1. Write the requirement as four numbers<br/>cycle bound reliability jitter"] --> S2{"Is the bound tighter than about 1 ms<br/>with jitter near 1 us"}
    S2 -->|"yes"| W1["Wireless is probably not the answer<br/>use a wire or accept a relaxed bound"]
    S2 -->|"no"| S3["2. Secure spectrum and a managed BSS<br/>prefer 6 GHz where every client understands the schedule"]
    S3 --> S4["3. Fix the clock first<br/>hardware timestamping FTM and 802.1AS"]
    S4 --> S5{"Measured sync error inside the budget"}
    S5 -->|"no"| W2["No schedule can hold<br/>fix timestamping before anything else"]
    S5 -->|"yes"| S6["4. Admission control<br/>bound the load before bounding the latency"]
    S6 --> S7["5. Choose the access mechanism<br/>trigger then TWT then r-TWT then preemption"]
    S7 --> S8["6. Bind the streams<br/>SCS with QoS Characteristics per direction"]
    S8 --> S9["7. Align the schedule<br/>r-TWT SPs inside the Qbv gate open times"]
    S9 --> S10["8. Decide the retry policy<br/>retry until a deadline not until a count"]
    S10 --> S11["9. Measure the tail<br/>latency CDF P99 P99.9 and loss under load"]
    S11 --> S12{"Bound held under the worst planned load"}
    S12 -->|"no"| S7
    S12 -->|"yes"| OK["Commission then keep monitoring"]
```

Five rules that come out of practice and are worth memorising:

1. **Fix the clock before the schedule.** Every scheduled mechanism is meaningless without hardware timestamping,
   and this is the step most often skipped because it is invisible in a datasheet.
2. **Bound the load before the latency.** Admission control is the only mechanism that limits how much contention
   exists to be scheduled around.
3. **Prefer a band where everyone understands the rules.** The r-TWT guarantee is only as strong as the least
   capable station present; 6 GHz with no pre-802.11ax devices is the cleanest place to get it.
4. **Retry until a deadline, not until a count.** A frame delivered after the cycle closed is a wrong answer.
5. **Measure the tail.** The mean will look excellent while the 99th percentile is unusable — this is the defining
   failure mode of Wi-Fi latency work.

### 12.1 A worked latency budget

The following is an **illustrative** design calculation, not a specification-derived number. Its purpose is to show
which term dominates.

Scenario: a control stream of 128 bytes, cycle 2 ms, deadline 1 ms, one wireless hop, two wired bridges.

| Component | Typical | Worst case in this design |
| --- | --- | --- |
| Wait for the next r-TWT SP (SP every 500 µs) | 250 µs | 500 µs |
| Guard and quiet interval at the SP start | 50 µs | 150 µs |
| Trigger + TB PPDU + SIFS + BlockAck | 220 µs | 300 µs |
| One scheduled retry | 0 µs | 300 µs |
| Wired segment, two bridges | 20 µs | 60 µs |
| Synchronisation error contribution | ±0.1 µs | ±1 µs |
| **Total** | **~540 µs** | **~1.31 ms** |

The worst case exceeds the 1 ms deadline. The fix is not a faster MCS: it is a **shorter SP period** (250 µs) and a
policy that **drops rather than retries** a frame that has already missed its bound, which brings the worst case to
roughly 0.6 ms. The general lesson, and it is the one to carry into an interview: **in a scheduled wireless system
the service-period interval is the dominant term in the latency bound, and the retry policy is the second.**

---

## 13. Measurement and troubleshooting

### 13.1 The KPIs that matter

| KPI | Why it is the right one | What a wrong value looks like |
| --- | --- | --- |
| **Latency CDF, especially P99 and P99.9** | The requirement is a bound, so the tail is the product | P50 of 3 ms with P99 of 90 ms |
| **Per-stream loss ratio** | Reliability is stated per stream, not per link | Aggregate loss of 0.1 % hiding 2 % on one stream |
| **Packet delay variation** | Jitter is what breaks isochronous execution | P99 stable but PDV growing with load |
| **Synchronisation error from the grandmaster** | Everything scheduled depends on it | Software timestamping showing ~1 µs |
| **Deadline-miss ratio** | The only KPI the application actually cares about | Excellent latency, missed cycles |
| **Service-period utilisation** | Shows whether the schedule is correctly sized | SP always full, meaning SP too short or load unbounded |

### 13.2 Symptom table

| Symptom | Most likely cause | How to confirm | Fix |
| --- | --- | --- | --- |
| P50 excellent, P99 terrible | Contention, not scheduling | Compare P99 with and without best-effort load | Admission control, then r-TWT |
| Latency spikes at a regular period | Another station's TXOP or a beacon interval interaction | Capture the airtime and correlate | Align SPs, shorten TXOP limits |
| r-TWT configured and no improvement | A non-participating or legacy station in the BSS | Check capability of every associated STA | Enforce a managed band, or admit only capable STAs |
| Bound holds when idle, breaks under load | Load is unbounded, so the schedule is over-committed | Measure deadline-miss ratio versus offered load | Admission control, or a longer cycle |
| Jitter fine, occasional huge outliers | Roaming or scanning | Correlate with roam events and scan results | See [[02-6 WLAN - Multi-AP Roaming, Healing and Steering]]; SMD in Wi-Fi 8 |
| Duplicate frames arriving | An elimination function is missing or misconfigured | Count sequence numbers per stream | Fix the FRER elimination point |
| Sync error exceeds budget | Software timestamping or long FTM intervals | Compare HW and SW timestamp paths, check FTM rate | Move timestamping to hardware, shorten intervals |
| SCS requests rejected | Resources unavailable or capability missing | Read the status code in the SCS Response | Reduce the request, or add airtime |
| Latency good in the lab, bad on site | OBSS interference | Channel utilisation and OBSS scan | Channel plan, then multi-AP coordination |
| Frame delivered but cycle missed | Retry policy is count-based | Correlate retries with deadline misses | Deadline-aware retry and drop |

```mermaid
flowchart TD
    A["Bound is being missed"] --> B{"Is the clock inside budget"}
    B -->|"no"| F1["Fix timestamping then re-measure"]
    B -->|"yes"| C{"Is the tail or the whole distribution affected"}
    C -->|"whole distribution"| D{"Is offered load within the admitted load"}
    D -->|"no"| F2["Admission control or more airtime"]
    D -->|"yes"| F3["Check the SP period it is probably too long"]
    C -->|"tail only"| E{"Do spikes correlate with a period or an event"}
    E -->|"periodic"| F4["Align schedules and check TXOP limits"]
    E -->|"event driven"| F5["Check roaming scanning and OBSS activity"]
    E -->|"neither"| F6["Suspect retries switch to deadline aware policy"]
```

---

## 14. Wi-Fi TSN versus 5G TSN — the same question, two answers

Both communities were asked to carry deterministic traffic over a shared medium, and their answers differ in a way
that is more instructive than either answer alone.

| Aspect | Wi-Fi (IEEE 802.11 + 802.1) | 5G (3GPP since Release 16) |
| --- | --- | --- |
| Architectural model | The AP is presented as a TSN bridge; the wireless hop is inside the 802.1Q domain | The 5G system **is** a TSN bridge: DS-TT and NW-TT terminate the TSN domain at its edges |
| Integration point | 802.11ak makes the link a transit link inside a bridged network | TS 23.501 §5.28 defines 5GS-TSN integration; §5.29 covers 5G LAN |
| Control function | CNC plus CUC, with the AP configured as a bridge | TSN Application Function (TSN-AF), and from Rel-17 the TSCTSF |
| Time synchronisation | 802.1AS over TM (10 ns) and FTM (0.1 ns) | 5G access-stratum timing distribution plus a gPTP domain, with PTP timestamping at DS-TT and NW-TT |
| Bridge delay reporting | No normative equivalent | `dependentDelayMin` and `dependentDelayMax` per port pair and traffic class, per 802.1Qcc |
| Medium access | Contended by construction; determinism has to be granted by the AP (trigger, r-TWT) | Scheduled by construction; the gNB owns the resources every slot |
| Reliability | 802.1CB emulated over MLO links | Packet duplication over two PDU sessions or two 5QI flows; Rel-17 adds survival time to QoS |
| Where it is strong | Cost, spectrum availability, enterprise ownership, evolution to 802.11bn | Licensed spectrum, mobility, a normative delay model |
| Where it is weak | The neighbour BSS, and the absence of a reported bridge delay | Cost, spectrum, deployment ownership |

The one-sentence version: **5G was designed as a scheduled system and had to learn to speak TSN; Wi-Fi was designed
as a contended system and has to keep buying pieces of a schedule.** The cellular comparison is also the sharpest
way to see what
[[02-8 WLAN - Scheduling - Channel Access, EDCA, OFDMA Resource Allocation, Airtime and Implementation]] means
by "a scheduler that must first win a contended medium".

---

## 15. Ten answers worth having on the tip of your tongue

1. **"What is TSN?"** Not a standard — the IEEE 802.1 toolbox: time synchronisation (802.1AS), bounded latency
   (802.1Qbv, Qch, Qcr), reliability (802.1CB), and resource management (802.1Qcc). Grew out of AVB, renamed in
   November 2012.
2. **"Why can't Wi-Fi just use 802.1Qbv?"** Because Qbv assumes you own the medium at the scheduled instant. Wi-Fi
   has to win the medium first, so the schedule must be carried by a granted-access mechanism — trigger frames and
   r-TWT — and even then a bystander can break it.
3. **"What did 802.11be actually add for TSN?"** Three things: SCS with the QoS Characteristics element (four
   mandatory parameters), restricted TWT for protected periodic access, and TID-to-link mapping over MLO so
   critical traffic can be steered to the best link and 802.1CB-style redundancy becomes possible.
4. **"How is r-TWT different from TWT?"** TWT saves energy and anyone may contend inside a service period; r-TWT
   exists to bound latency — only members on the bound TIDs transmit, they are triggered, other stations must end
   their TXOPs before the SP starts, and the AP may announce a quiet interval.
5. **"What breaks r-TWT?"** Legacy or non-participating stations. The feature is optional in 802.11be and its
   guarantee is a property of a managed deployment, not of an AP.
6. **"Why does time synchronisation matter so much?"** Because without a shared clock there is no "at time T", so
   there is no schedule, so there is no bound. And in practice hardware timestamping gives 10–40 ns while
   software timestamping gives about 1 µs — which can consume the whole 0.1–1 µs budget allowed by IEC/IEEE 60802.
7. **"What is the biggest structural gap versus wired TSN?"** Preemption. 802.1Qbu and 802.3br let an express frame
   interrupt a long one, cutting worst-case blocking from about 12 µs to about 1 µs at 1 Gbit/s. Wi-Fi has no
   equivalent until 802.11bn.
8. **"What does Wi-Fi 8 change?"** The target becomes quantified: 25 % lower latency at the **95th percentile**,
   25 % lower MPDU loss, 25 % higher throughput at a given SINR. The mechanisms are P-EDCA, NPCA, preemption, LLI,
   multi-AP coordination and SMD.
9. **"How does this compare with 5G?"** 5G is scheduled by construction and reports a bridge delay
   (`dependentDelayMin/Max`); Wi-Fi is contended by construction and has no normative bridge delay. Wi-Fi is
   cheaper and enterprise-owned; 5G has licensed spectrum and a normative delay model.
10. **"If I had to deploy wireless TSN next quarter, what would I do?"** Choose a managed band with capable clients,
    fix hardware timestamping first, bound the load with admission control, schedule with r-TWT aligned to the Qbv
    cycle, retry until a deadline rather than a count, and then measure the P99.9 — not the mean.

---

## Anchors — verified facts

- **IEEE Std 802.11ax-2021** published **19 May 2021**. **IEEE Std 802.11be-2024**: PAR approved **21 March 2019**,
  IEEE-SA board approval **26 September 2024**, published **22 July 2025**, DOI 10.1109/IEEESTD.2024.11090080; its
  scope requires at least one mode with **30 Gbit/s** at the MAC SAP and "at least one mode of operation capable of
  improved worst case latency and jitter".
- **IEEE P802.11bn** PAR approved **21 September 2023**; first TG meeting November 2023; D1.0 July 2025; D2.0 WG
  letter ballot July 2026; final 802.11 WG approval projected March 2028, RevCom May 2028. UHR targets: **≥25 %
  throughput** at the MAC SAP at ≥1 SINR level, **≥25 % latency reduction at the 95th percentile**, **≥25 % MPDU
  loss reduction**, AP power reduction, improved P2P, 1–7.250 GHz, backward compatible in 2.4/5/6 GHz.
- **IEEE Std 802.11ak-2018**, "Enhancements for Transit Links Within Bridged Networks", published 2018; developed
  alongside IEEE Std 802.1Qbz-2016 and 802.1AC-REV; rolled into IEEE Std 802.11-2020.
- **802.11aa-2012** "MAC Enhancements for Robust Audio Video Streaming": SCS, intra-access-category prioritisation
  (primary and alternate queues), Drop Eligibility Indicator, OBSS management, GCR, declared support for IEEE
  802.1Qat SRP.
- **Timing Measurement (TM)**: 802.11v, **10 ns** timestamp resolution, the basis of 802.1AS over 802.11 in IEEE Std
  802.11-2012. **Fine Timing Measurement (FTM)**: 802.11mc, **0.1 ns** resolution; **IEEE 802.1AS-2020 specifies
  the use of FTM** for TSN integration over 802.11.
- **Hardware timestamping 10–40 ns** versus **software timestamping ~1 µs**; **IEC/IEEE 60802** allows
  **0.1–1 µs** synchronisation error from the grandmaster.
- **Industrial targets** quoted consistently: closed-loop transaction within a **1 ms cycle** at **99.999 %**
  reliability, **1 µs** jitter implying better than **±500 ns** synchronisation; PROFINET IRT **clock rate < 1 ms,
  jitter < 1 µs**.
- **802.11be QoS Characteristics element**: Control Info carries direction (uplink, downlink, direct link), TID and
  User Priority; four mandatory traffic parameters — Minimum Service Interval, Maximum Service Interval, Minimum
  Data Rate, Delay Bound — plus up to eight optional ones including Maximum MSDU Size, Service Start Time and MSDU
  Delivery Ratio. TID is set to the same value as UP in 802.11be.
- **r-TWT**: a broadcast TWT parameter set whose **Broadcast TWT Recommendation subfield is 4**; announced in beacon
  and probe response frames; Restricted TWT Traffic Info carries **TID bitmaps per direction**; r-TWT-capable STAs
  **must end their TXOPs before the SP start**; the AP **may set a quiet interval** (published evaluations model
  **1024 µs**); legacy STAs are not obliged to honour any of it; r-TWT is **optional** in 802.11be and is expected
  to be used in **managed networks**.
- **IEEE 802.11 WG liaison to 802.1, December 2022**, maps the 802.1 toolbox onto 802.11be in three rows: time
  synchronisation → 802.1AS over TM/FTM; bounded latency → 802.11ax scheduling plus SCS, r-TWT and TID-to-link
  mapping; reliability → 802.1CB over multi-radio devices using MLO.
- **TSN toolbox dates**: 802.1Qav-2009, 802.1AS-2011, 802.1Qat-2010, 802.1Qbv-2015, 802.1Qca-2015, 802.1Qbu-2016
  with 802.3br-2016, 802.1CB-2017, 802.1Qch-2017, 802.1Qci-2017, 802.1Qcc-2018, 802.1CM-2018, 802.1CS-2020,
  802.1Qcr-2020, 802.1AS-2025. AVB TG renamed TSN TG in **November 2012**.
- **Profiles**: **IEC/IEEE 60802** published **29 June 2026**; **IEEE 802.1DG-2025** approved 28 May 2025,
  published 6 June 2025; **IEEE 802.1DP-2025 / SAE AS6675** aerospace, 2025; **IEEE 802.1BA-2021** AVB profile.
- **Wi-Fi CERTIFIED QoS Management** launched **23 February 2021** with MSCS and DSCP mapping based on **RFC 8325**;
  extended **21 October 2021** to four features: SCS, MSCS, DSCP mapping and DSCP Policy. MSCS is the mirroring
  mechanism defined in IEEE 802.11 REVmd.
- **3GPP**: Rel-16 makes the 5G system a TSN bridge with **DS-TT** and **NW-TT** and the **TSN-AF** (TS 23.501
  §5.28; §5.29 covers 5G LAN); bridge delay reported as `dependentDelayMin`/`dependentDelayMax` per 802.1Qcc,
  computed from UE–DS-TT residence time plus per-traffic-class UE↔UPF/NW-TT delay. Rel-17 adds **TSCTSF**,
  **TSCAI**, uplink time synchronisation and RTT-based propagation delay compensation.
- **Key literature**: Adame, Carrascosa-Zamacois and Bellalta, *Sensors* **21**(15):4954, 2021, DOI
  10.3390/s21154954; Haxhibeqiri et al., *IEEE Communications Magazine* **62**(8):118–124, 2024, DOI
  10.1109/MCOM.001.2300431 (openwifi SDR implementation of C-SR and r-TWT); Mozaffariahrar et al., **ETFA 2025**,
  DOI 10.1109/ETFA65518.2025.11205686 (ns-3 evaluation; mimics restricted access with individual TWT);
  Karamyshev, Levitsky, Bankov and Khorov, *Problems of Information Transmission* **61**(2):164–210, 2025, DOI
  10.1134/S003294602502005X.
- **VERIFY**: the exact clause number in which MSCS is specified (sources place it in the 2016 revision and in
  REVmd/IEEE Std 802.11-2020; the Wi-Fi Alliance states REVmd). The quiet-interval duration used with r-TWT is
  variously given as 1024 µs in published evaluations and 1 ms in some vendor documentation.

---

## Related

- [[02-8 WLAN - Scheduling - Channel Access, EDCA, OFDMA Resource Allocation, Airtime and Implementation]] — the mechanism layer this note's determinism story sits on: EDCA, the RU grid, trigger frames, airtime fairness, and why a Wi-Fi scheduler must win the medium before it can schedule it
- [[02-2 WLAN - Power Saving Mechanisms and Evolution]] — TWT as a power-saving mechanism, and therefore the origin of the service period that r-TWT turns into a latency tool
- [[02-1 WLAN - Wi-Fi Generations Evolution]] — which generation each feature belongs to, and where Wi-Fi 8's quantified latency target came from
- [[02-6 WLAN - Multi-AP Roaming, Healing and Steering]] — the client-controlled transition that puts a hole in any latency bound, and what SMD does about it
- [[02-4 WLAN - Packet TX-RX Datapath and Offload Evolution]] — where the deadline is actually spent: host, firmware, and the offload boundaries a scheduled design has to respect
- [[02-7 WLAN - Wi-Fi EasyMesh, Operation, Tuning and Troubleshooting]] — the multi-AP management plane that a coordinated-schedule deployment has to configure, and what a controller can actually observe
- [[02-3 WLAN Ecosystem - WFA, EasyMesh and prpl]] — where certification constrains practice: WMM, Wi-Fi QoS Management, and what vendors actually implement
- [[02-5 WLAN - STA-AP Discovery, Authentication and Association]] — what has to have happened before a station can be scheduled at all
- [[01-6 NR DU MAC Scheduler - Resource Allocation, HARQ and Real-Time Implementation]] — the cellular scheduler: a slot that is already owned, against a medium that must first be won
- [[01-7 NR HARQ - Retransmission Flow, Timelines and LTE Comparison]] — the other side of reliability: retransmission counted against a deadline rather than a retry limit
- [[04-4 Linux Interrupts - Types, Handlers, Threaded IRQs and Deferred Work]] — the execution context a host-side TSN stack and its timestamping path run in
- [[04-6 Linux Device Drivers - Model, Probe, Data Path, Power and Bring-Up]] — where hardware timestamping lives: the NIC driver, its DMA path, and the interrupt latency that decides whether a timestamp is trustworthy
- [[08-1 Programming Languages Toolchain and Performance Engineering]] — profiling worst-case rather than mean behaviour in a path whose deadline is measured in microseconds

---

## References

1. IEEE. *IEEE Std 802.11be-2024 — Amendment 2: Enhancements for Extremely High Throughput (EHT)*. Published 22 July 2025. DOI 10.1109/IEEESTD.2024.11090080. — The TSN-relevant MAC: SCS with the QoS Characteristics element, restricted TWT, MLO and TID-to-link mapping. Free via the IEEE GET program.
2. IEEE. *IEEE Std 802.11ax-2021 — Amendment 1: Enhancements for High Efficiency WLAN*. Published 19 May 2021. — OFDMA, trigger-based uplink access and TWT: the granted-access foundation.
3. IEEE. *IEEE Std 802.11ak-2018 — Amendment 4: Enhancements for Transit Links Within Bridged Networks*. — The amendment that lets a Wi-Fi link be an internal transit link inside an 802.1Q bridged network.
4. IEEE. *IEEE Std 802.11aa-2012 — Amendment 2: MAC Enhancements for Robust Audio Video Streaming*. — SCS, intra-AC prioritisation, DEI, OBSS management and GCR: where the vocabulary of wireless TSN was established.
5. IEEE. *IEEE Std 802.11-2024* (maintenance revision), published 28 April 2025. — The consolidated base document.
6. IEEE 802.11 Working Group. *P802.11bn PAR and Criteria for Standards Development*. PAR approved 21 September 2023. <https://grouper.ieee.org/groups/802/11/PARs/P802.11bn_PAR.pdf> — The UHR targets quoted in §4.8 and the Anchors, in the task group's own words.
7. IEEE 802.11 Working Group. *Task Group BN (UHR) status*. <https://www.ieee802.org/11/Reports/tgbn_update.htm> — Milestones, officers, and the comment-resolution topics that reveal what is actually in the draft.
8. IEEE 802.11 Working Group. *Liaison communication to IEEE 802.1 regarding TSN support*, 20 December 2022. <https://grouper.ieee.org/groups/802/11/Liaisons/2022-12-20-802-11%20liaison%20to%20802-1%20re%20TSN%20support.pdf> — The working group's own three-row mapping of the 802.1 toolbox onto 802.11be; the single best primary source for §3 and §4.7.
9. Cavalcanti, D., and Venkatesan, G. *802.1 TSN over 802.11, with updates from developments in 802.11be*. IEEE 802.1 Plenary, November 2020. <https://www.ieee802.org/1/files/public/docs2020/new-Cavalcanti-802-1TSN-over-802-11-1120-v00.pdf> — The architecture of a wireless TSN domain, the 802.1AC GLK convergence function, and which TSN features already operate over 802.11.
10. IEEE 802.1 Time-Sensitive Networking Task Group. *TSN standards and projects*. <https://1.ieee802.org/tsn/> — Base standards, profiles and publication dates: 802.1AS-2025, 802.1Qbv-2015, 802.1Qbu-2016, 802.1CB-2017, 802.1Qci-2017, 802.1Qch-2017, 802.1Qcc-2018, 802.1CS-2020, 802.1CM-2018, 802.1DG-2025, 802.1DP-2025, 802.1BA-2021.
11. IEC/IEEE. *IEC/IEEE 60802 — Time-Sensitive Networking Profile for Industrial Automation*. Published 29 June 2026. <https://1.ieee802.org/tsn/iec-ieee-60802/> — The industrial profile: which features, defaults and configuration a converged network must implement.
12. IEEE. *IEEE Std 802.1DG-2025 — TSN Profile for Automotive In-Vehicle Ethernet Communications*. Published 6 June 2025. — The automotive counterpart; useful for understanding how a profile narrows a toolbox.
13. Adame, T., Carrascosa-Zamacois, M., and Bellalta, B. "Time-Sensitive Networking in IEEE 802.11be: On the Way to Low-Latency WiFi 7." *Sensors* 21(15):4954, 2021. DOI 10.3390/s21154954. — The reference survey: how each 802.1 TSN tool maps onto 802.11be, with the multimedia, healthcare, industrial and transport use cases. Open access.
14. Haxhibeqiri, J., Jiao, X., Shen, X., Pan, C., Jiang, X., Hoebeke, J., and Moerman, I. "Coordinated SR and Restricted TWT for Time Sensitive Applications in WiFi 7 Networks." *IEEE Communications Magazine* 62(8):118–124, August 2024. DOI 10.1109/MCOM.001.2300431. — A real implementation of C-SR and r-TWT on the openwifi SDR platform; the evidence that these mechanisms are implementable in firmware.
15. Mozaffariahrar, E., Wilhelmi, F., Galati-Giordano, L., Imputato, P., Menth, M., and Avallone, S. "R-TWT in Wi-Fi 7 and Beyond: Enabling Bounded Latency, Energy Efficiency, and Reliability." *IEEE 30th International Conference on Emerging Technologies and Factory Automation (ETFA)*, 2025. DOI 10.1109/ETFA65518.2025.11205686. — The ns-3 evaluation behind §6.3, including the honest caveat that restricted access is mimicked with individual TWT.
16. Karamyshev, A., Levitsky, I., Bankov, D., and Khorov, E. "A Tutorial on Wi-Fi 8: The Journey to Ultra High Reliability." *Problems of Information Transmission* 61(2):164–210, 2025. DOI 10.1134/S003294602502005X. — Feature by feature on 802.11bn: DRU, UEQM, P-EDCA, NPCA, preemption, roaming and multi-AP coordination.
17. Wilhelmi, F., Bellalta, B., Geraci, G., Galati-Giordano, L., Meneghello, F., Kijanka, A., Val, I., and López-Pérez, D. "A Tutorial on IEEE 802.11bn Multi-AP Coordination for Wi-Fi 8: From Standardization to Performance Evaluation." arXiv:2606.13759. — Co-TDMA, Co-SR, Co-BF and Co-RTWT, with the Kom8ndor open-source Wi-Fi 8 simulator.
18. Khorov, E., Kiryanov, A., Lyakhov, A., and Bianchi, G. "A Tutorial on IEEE 802.11ax High Efficiency WLANs." *IEEE Communications Surveys & Tutorials* 21(1):197–216, 2019. — The Wi-Fi 6 PHY and MAC reset: OFDMA, the new numerology, trigger-based uplink.
19. Nurchis, M., and Bellalta, B. "Target Wake Time: Scheduled Access in IEEE 802.11ax WLANs." *IEEE Wireless Communications* 26(2), 2019. — The origin of the service period as a scheduling primitive rather than a sleep mechanism.
20. Bellalta, B. "IEEE 802.11ax: High-Efficiency WLANs." *IEEE Wireless Communications* 23(1):38–46, 2016. — Why dense deployments forced a different approach, written while 802.11ax was still being designed.
21. Reshef, E., and Cordeiro, C. "Future Directions for Wi-Fi 8 and Beyond." *IEEE Communications Magazine* 60(10):50–55, 2022. — The market drivers and candidate directions that became the UHR brief.
22. Geraci, G., Meneghello, F., Wilhelmi, F., López-Pérez, D., Val, I., Galati Giordano, L., Cordeiro, C., Ghosh, M., Knightly, E., and Bellalta, B. "Wi-Fi: Twenty-Five Years and Counting." arXiv:2507.09613. — From 802.11b to 802.11bn, organised by mechanism rather than generation.
23. Liu, X., Gan, M., Dai, W., Dong, Y., Chan, C. C.-K., and Song, J. "Towards Ultra-High Reliability in Wi-Fi 8: IEEE 802.11bn Core Mechanisms, mmWave Integration, and Performance Verification." arXiv:2607.19931. — System-level simulations of whether the 802.11bn mechanisms actually meet their targets.
24. IEEE 802.11 Real Time Applications Topic Interest Group. *RTA TIG Report*, doc. 11-18/2009-06, 2019. <https://www.ieee802.org/11/Reports/rtatigupdate.htm> — Where the requirement set for real-time applications over 802.11 was first written down by the working group itself.
25. Hu, C. et al. "Protected TWT Enhancement for Latency Sensitive Traffic." IEEE 802.11 contribution 11-20/1046r14, 2020. — The TGbe contribution lineage from which restricted TWT emerged.
26. 3GPP. *TS 23.501 — System Architecture for the 5G System*, §5.28 (TSN integration) and §5.29 (5G LAN). — The cellular answer: DS-TT, NW-TT, TSN-AF and bridge delay; the sharpest contrast with the Wi-Fi approach in §14.
27. Wi-Fi Alliance. *Wi-Fi CERTIFIED QoS Management*. Announced 23 February 2021; extended 21 October 2021 to SCS, MSCS, DSCP mapping and DSCP Policy. <https://www.wi-fi.org/news-events/newsroom/wi-fi-alliance-enhances-consistent-quality-of-service-for-latency-sensitive-wi> — What is actually certified, and therefore what actually ships.
28. Wi-Fi Alliance. *Wi-Fi CERTIFIED QoS Management prioritizes traffic to improve user experience*. <https://www.wi-fi.org> — MSCS defined in IEEE 802.11 REVmd, DSCP mapping defaulting to RFC 8325, and the QoS Map feature from 802.11u.
29. IETF. *Reliable and Available Wireless Technologies* (RAW), draft-ietf-raw-technologies. <https://ftp.ripe.net/mirrors/internet-drafts/draft-ietf-raw-technologies-05.html> — An unusually accurate cross-technology summary: what 802.11-2012, 802.11-2016, 802.11ak, 802.11ax and 802.11be each contribute to TSN, and the trade-offs of extending TSN to any wireless medium.
30. Jiao, X. et al. "openwifi: A Free and Open-Source IEEE 802.11 SDR Implementation on SoC." *IEEE VTC*, 2020. — The platform on which r-TWT and coordinated SR have been implemented and measured.
31. Aslam, M. et al. "Hardware Efficient Clock Synchronization Across Wi-Fi and Ethernet Based Network Using PTP." *IEEE Transactions on Industrial Informatics*, 2021. — The hardware-timestamping argument in §5 with measurements.
32. Samsung Research. *IEEE 802.11bn (Ultra-High Reliability, Wi-Fi 8)* — Ha, T., Shafin, R., and Manasi. <https://research.samsung.com/blog/IEEE-802-11bn-Ultra-High-Reliability-UHR-Wi-Fi-8> — An engineering walkthrough from a TGbn contributor: P-EDCA and DS-CTS, LLI, NPCA, ELR and DRU, with the certification timeline.
33. MaxLinear. *Quality of Service (QoS) Mechanisms in Wi-Fi*, white paper, 2024. <https://www.maxlinear.com/news/white-papers/2024/quality-of-service-(qos)-mechanisms-in-wi-fi> — A readable secondary account of the amendment-by-amendment QoS story from 802.11e through 802.11be.
34. Things Embedded. *Time Sensitive Networking (TSN): Standards, Scheduling and Hardware*. <https://things-embedded.com/uk/white-paper/time-sensitive-networking-tsn-guide/> — The clearest short explanation of why priority alone is not enough, and what preemption buys at 1 Gbit/s.

---

Copyright (c) 2026 Washington Ruan. All rights reserved.


