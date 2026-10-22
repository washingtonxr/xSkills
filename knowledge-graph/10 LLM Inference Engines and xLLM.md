---
title: LLM Inference Engines and xLLM
domain: ai-infra
tags:
  - llm
  - inference
  - kv-cache
  - pagedattention
  - quantization
  - operator-fusion
  - xllm
  - moe
aliases:
  - xLLM
  - KV cache
  - prefill and decode
  - continuous batching
last-updated: 2026-10-22
---

# LLM Inference Engines and xLLM

## 1. Prefill versus decode — the axis every optimisation decision hangs on

| | Prefill | Decode |
| --- | --- | --- |
| Work shape | Large matrix-matrix (all prompt tokens at once) | Matrix-vector (one token at a time) |
| Regime | **Compute-bound** | **Memory-bound** (weights + KV cache must be re-read every step) |
| Bottleneck | Arithmetic throughput | Memory bandwidth |
| Optimisation that pays | Good GEMM tiling, chunking | Batching, KV cache layout, quantisation, operator fusion |

- **Chunked prefill** splits a long prompt so decode requests sharing the batch are not starved — this is why it matters for tail latency.
- **Disaggregated prefill/decode** (prefill instances and decode instances separated) lets each phase be scheduled and scaled independently.

## 2. KV Cache

### 2.1 Why K and V only, not Q
In decoder-only self-attention, token *t* computes:
`Q_t = x_t W_Q`, `K_t = x_t W_K`, `V_t = x_t W_V`, attention over `softmax(Q_t K^T_{1..t} / sqrt(d)) V_{1..t}`.

- The **query is only ever the current token** — it is recomputed each step and used immediately; caching it buys nothing.
- **K and V of all past tokens are read every step** — recomputing them would mean re-running the whole prefix through the projection layers, which is exactly the quadratic waste the cache exists to avoid.
- Hence memory scales as `O(sequence_length × layers × heads × head_dim × 2 × dtype_bytes)`.

### 2.2 Memory arithmetic you should be able to do live
Per token per layer: `2 (K,V) × n_kv_heads × head_dim × bytes_per_element`.
Multiply by layers and by context length to get per-sequence KV size; multiply by concurrent sequences for the pool.

### 2.3 Layout strategies
- **Contiguous KV cache** — one buffer per sequence, sized to max context. Simple and fast, but wastes memory when sequences are short and cannot grow.
- **PagedAttention** — KV stored in fixed-size blocks allocated on demand from a block pool; near-zero fragmentation and enables sharing.
- **Prefix caching / radix caching** — blocks for a shared prefix (system prompt, few-shot examples, document) are reused across requests by reference.
- **Multi-tier KV cache** — device → host → storage, with offload and prefetch. Necessary when KV exceeds accelerator memory, which is the norm for long-context agent workloads.

### 2.4 End-side versus data-centre trade-offs
On an end device there is no large HBM pool, no overcommit, and often unified memory shared with the OS:
- **Block size** becomes a real decision. Small blocks reduce internal fragmentation but increase block-table metadata and lookup overhead; large blocks waste memory in a small pool.
- **Prefix caching** is more valuable (system prompts and personas repeat heavily) but the cache competes with OS memory.
- Worked example shape: with 8 GB total and 4 GB of weights, roughly 3 GB remains for KV plus runtime plus OS. Compute per-token KV cost at your quantisation, divide, and you get the maximum concurrent context — then decide the block size that keeps internal waste under ~10% while keeping the block table small enough to fit in cache.
- **Offloading to storage** is usually a non-option on device: flash latency and write endurance make it a last resort rather than a tier.

## 3. Quantisation

- **FP16 / BF16** — baseline; BF16 has a larger exponent range and is more robust for training-ish numerics.
- **INT8** — weight and/or activation quantisation; per-channel or per-token scales; needs calibration.
- **FP8 / FP4** — increasingly common on newer accelerators; e4m3 and e5m2 variants.
- **KV cache quantisation** — often the single biggest memory win, because KV dominates memory in long-context serving.
- **Accuracy guardrails**: perplexity and task-level evaluation, not just average-bit-width claims; watch for outlier channels and attention softmax sensitivity.

## 4. Operator fusion and graph execution

- Fusion merges multiple elementwise / memory-bound operations into one kernel, eliminating intermediate global-memory reads and writes and the launch overhead.
- **Effective in memory-bound stages** (decode, elementwise chains, RMSNorm + residual + activation).
- **Diminishing returns in compute-bound stages** (large prefill GEMMs) where arithmetic dominates and fusion may restrict tiling.
- **Graph mode execution** (CUDA Graphs, ACL graphs) removes per-kernel launch overhead — critical at small batch sizes where launch overhead is a large fraction of step time.

## 5. Batching and scheduling

- **Continuous batching** — requests join and leave the batch at token boundaries rather than waiting for a whole request to finish; the core throughput technique in modern servers.
- **Chunked prefill** — prevents a long prompt from monopolising a step.
- **Speculative decoding** — a small draft model proposes tokens that the target model verifies in parallel; methods named in practice include **MTP (multi-token prediction), Eagle3, and suffix-based** approaches.
- **Priority / online versus offline** — online serving optimises latency under SLO; offline inference optimises throughput. Mixing them requires admission control.
- **MoE specifics** — expert parallelism and **EPLB (expert parallel load balancing)**; hot experts create stragglers, so load balancing is a scheduling problem, not a modelling one.

## 6. xLLM — a concrete open-source engine

### 6.1 Identity and status
- **xLLM** is an efficient open-source LLM inference framework, **released October 2025** by JD.com, **donated to the OpenAtom Foundation on 25 June 2026** (announced 6 July 2026), licensed **Apache 2.0**.
- Implemented in **C/C++ (with Python bindings)**; GitHub Stars exceeded 1.4k.
- Scope: **inference for LLM, VLM, DiT and REC models** — not training.
- Technical report: **arXiv:2510.14686** ("xLLM Technical Report", published 16 October 2025).
- Version **v0.11.0** released 7 August 2026.

### 6.2 Architecture — service/engine decoupling
- **Service layer** — request handling, scheduling, availability: `APIService` (HTTP/BRPC), schedulers, `AsyncResponseProcessor`, `XServiceClient` (distributed service discovery via Etcd).
- **Engine layer** — orchestration and resources: `Master`, `Engine`, `KVCacheManager`, `Executor` (graph-mode execution).
- **Runtime layer** — per-device workers (`LLMWorkerImpl`, `VLMWorkerImpl`, `DiTWorker`), registered models, layers (attention, MLP, MoE), and a unified **kernel API (`ops_api.h`)**.
- Why decoupling matters: request handling and compute scale independently, and disaggregated prefill/decode topologies become a deployment choice rather than a rewrite.

### 6.3 Multi-backend abstraction
- Single codebase, **compile-time dispatch** via backend macros (e.g. `USE_NPU`), with backend-specific kernels.
- Supported accelerators: **Ascend NPU (A2/A3; HDK Driver 25.2.0+, CANN 8.0.rc1+)**, **Cambricon MLU**, **Moore Threads GPU (MUSA S5000)**, **Hygon DCU (BW1000)**, **MetaX MACA (MXC500)**, **Iluvatar CoreX GPU (BI150)**, plus **NVIDIA CUDA**.
- Backend-specific optimisations cited: ATB for NPU, FlashAttention for CUDA, INT8 quantisation for MLU.

### 6.4 Feature set
- Graph-mode execution (CUDA / ACL graphs)
- Speculative decoding: **MTP, Eagle3, Suffix**
- **Chunked prefill**
- **Multi-tier KV cache** (device / host / storage)
- **EPLB** for MoE expert-parallel load balancing
- **Hybrid KV cache management based on Mooncake** — global KV cache management with intelligent offloading and prefetching (announced 5 December 2025); hierarchical KV cache events published asynchronously (October 2026)
- Configuration-driven behaviour with 100+ flags (device/backend selection, block size, max memory utilisation, tokens per batch, chunked prefill, node count, disaggregated prefill-decode)

### 6.5 Model support
DeepSeek-V3/R1, DeepSeek-R1-Distill-Qwen, Kimi-k2, Llama2/3, MiniCPM-V, MiMo-VL, Qwen2/2.5/QwQ, Qwen2.5-VL, **Qwen3/Qwen3-MoE**, GLM-4.5/4.6/4.6V/4.7/5, GLM-5.3-Flash, MiniMax-M3, DeepSeek-V4, VLM-R1.

### 6.6 Lineage
Built with/upon: **ScaleLLM** (graph construction and runtime execution), **Mooncake** (hybrid KV cache management), **brpc** (high-performance HTTP service), **tokenizers-cpp**, **safetensors**, **concurrentqueue** (lock-free multi-producer/multi-consumer queue).
Collaborating labs: THU-MIG (BNRist, Tsinghua), USTC Cloudlab, Beihang HiPO, PKU-DS-LAB, PKU-NetSys-LAB, TJU-TANKLab.

### 6.7 Roadmap
- 2026: full-modality model support, adaptation to mainstream domestic chips, enterprise edition, community contributors scaling towards ~200.
- From 2027: industry penetration and standards leadership phase.

## 7. Why write an inference engine in pure C++?

**Motivation (end-side and real-time scenarios):**
- Eliminate Python runtime overhead and interpreter dispatch in the hot loop
- Eliminate **GC-induced tail-latency jitter** — a stop-the-world pause is invisible in a benchmark and fatal in a real-time pipeline
- Manual memory control — deterministic allocation via pools rather than allocator/GC behaviour
- Direct access to low-level hardware intrinsics and vendor kernel libraries

**The costs, which you must be able to state:**
- **Model onboarding cost.** Every new architecture needs operator implementations per backend. Python ecosystems get day-0 support via reference implementations; a C++ engine pays an implementation lag.
- **Ecosystem gap.** Tokenizers, sampling utilities, evaluation harnesses, and research tooling are Python-first.
- **Debuggability.** No REPL, longer build cycles, harder experimentation.
- **Portability maintenance.** Each backend is a separate kernel maintenance surface.

**Balanced answer:** use C++ where the SLO is strict and the model set is stable (production serving, on-device, real-time); keep a Python path for model exploration and rapid onboarding. The trend in practice is a hybrid — C++ runtime with Python bindings and configuration, which is exactly the shape xLLM takes.

## Anchors — verified facts

- **xLLM**: JD.com open source, Oct 2025; **donated to OpenAtom Foundation 25 June 2026**; **Apache 2.0**; C/C++ + Python; **arXiv:2510.14686**; **v0.11.0 (7 Aug 2026)**; scope **LLM/VLM/DiT/REC inference**.
- Backends: **Ascend NPU (A2/A3, HDK 25.2.0+, CANN 8.0.rc1+), Cambricon MLU, Moore Threads MUSA S5000, Hygon DCU BW1000, MetaX MACA MXC500, Iluvatar CoreX BI150, NVIDIA CUDA**.
- Features: **chunked prefill, multi-tier KV cache (device/host/storage), speculative decoding (MTP / Eagle3 / Suffix), EPLB, Mooncake-based hybrid KV cache management (5 Dec 2025)**.
- KV cache stores **K and V only**; Q is recomputed per step because only the current token's query is needed.
- Operator fusion is a **memory-traffic optimisation**: it pays in decode (memory-bound) and gives diminishing returns in large prefill GEMMs (compute-bound).

## Related

- [[16 C and C++ Programming - Language Features, STL and Systems Practice]] — C++17/20 engine code, dtype dispatch via templates, `std::simd` kernels, `mdspan` tensors
- [[09 Cloud-Edge-End Collaboration and Heterogeneous Computing]]
- [[11 Agent Systems and Edge Orchestration]]
- [[12 RISC-V for Communication Infrastructure]]
