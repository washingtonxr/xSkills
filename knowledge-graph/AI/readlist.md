---
title: Reading list — AI · Machine learning and inference
lang: en
category: reading-list
license: GPL-3.0-or-later OR AGPL-3.0-or-later
last-updated: 2026-10-29
---

# Reading list — AI · Machine learning and inference

> Machine learning from foundations to serving: the learning loop and its failure modes, LLM inference engines, and agent systems at the edge. The primary literature is the standard here; standards bodies are not the right filter.
>
> One section per note, numbered `GG-x`. Where a note needed no source beyond its own
> **References**, there is no section here — the note is self-sufficient.

## How to use this list

- **Marks.** Type and priority marks (`★★★`, `[Book]`, `[EN]`) are defined once, in the MOC under *Reading marks*. The rule that matters: `★★★` means read or skim before you quote the note in an interview.
- **Titles** are kept in their published form and never translated; descriptions are English.
- **Nothing is asserted.** Where a citation could not be confirmed against a publisher, DOI, arXiv record or the issuing body, it is marked `VERIFY`.

---

## 06-1 · LLM Inference Engines and xLLM
### Papers

- **[Paper · EN · ★★★]** "xLLM Technical Report" — xLLM team (JD.com) · arXiv:2510.14686, 2025
  - The primary reference for the framework in note 06-1: the service–engine decoupled architecture, optimisation for Chinese AI accelerators (Ascend NPU, Cambricon MLU, Moore Threads GPU, Hygon DCU, MetaX MACA, Iluvatar CoreX), and hybrid KV cache management built on Mooncake with intelligent offloading and prefetching. Battle-tested at scale in JD.com's retail business, which is the strongest available evidence for the engineering claims.
- **[Paper · EN · ★★★]** "Mooncake: A KVCache-centric Disaggregated Architecture for LLM Serving" — R. Qin et al. · *USENIX FAST 2025* · arXiv:2407.00079
  - The KV-cache-centric disaggregated design: separating prefill and decode clusters, and treating KV cache as a first-class schedulable resource with a global pool. Directly the substrate xLLM's hybrid KV cache builds on.
- **[Paper · EN · ★★★]** "Efficient Memory Management for Large Language Model Serving with PagedAttention" — W. Kwon et al. · *ACM SOSP 2023* · arXiv:2309.06180
  - Paged virtual-memory-style KV cache management: eliminates fragmentation, enables sharing across requests, and is now the default mental model for KV cache. Know the block-allocation and copy-on-write mechanisms, not just the name.
- **[Paper · EN · ★★★]** "FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness" — T. Dao, D. Y. Fu, S. Ermon, A. Rudra, C. Ré · *NeurIPS 2022* · arXiv:2205.14135
  - IO-aware exact attention: tiling and recomputation to avoid materialising the attention matrix, turning attention from HBM-bound into compute-bound. The single most important inference optimisation of the last cycle.
- **[Paper · EN · ★★]** "FlashInfer: Efficient and Customizable Attention Engine for LLM Inference Serving" — Z. Ye et al. · *MLSys 2025* · arXiv:2501.01005
  - Production attention engine: a unified KV-cache format, JIT-generated kernels, and load-balanced scheduling for variable-length inputs. The right citation for "what does a real attention kernel library look like".
- **[Paper · EN · ★★★]** "Orca: A Distributed Serving System for Transformer-Based Generative Models" — G.-I. Yu et al. · *USENIX OSDI 2022*
  - Introduced iteration-level (continuous) batching and selective batching. This is the mechanism behind modern throughput, and the reason request-level batching is obsolete for decode.
- **[Paper · EN · ★★]** "Efficiently Scaling Transformer Inference" — N. Shazeer · *MLSys 2023* · arXiv:2211.05102
  - Multi-query attention and the systems-level scaling argument. Short and high density.
- **[Paper · EN · ★★]** "Fast Inference from Transformers via Speculative Decoding" — Y. Leviathan, M. Kalman, Y. Matias · *ICML 2023* · arXiv:2211.17192
  - Speculative decoding: draft-then-verify with exact distribution preservation. Essential for the latency side of the decode-phase discussion.
- **[Paper · EN · ★★]** "AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration" — J. Lin et al. · *MLSys 2024* · arXiv:2306.00978
  - Post-training quantization that protects salient weights identified by activation distribution. Know the difference between AWQ's activation-aware approach and GPTQ's second-order approach.
- **[Paper · EN · ★★]** "GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers" — E. Frantar et al. · *ICLR 2023* · arXiv:2210.17323
  - Layer-wise, Hessian-based one-shot quantization. The baseline all weight-only quantization is compared against.
- **[Paper · EN · ★★]** "Attention Is All You Need" — A. Vaswani et al. · *NeurIPS 2017* · arXiv:1706.03762
  - The architecture origin. Worth re-reading specifically for the inference-cost implications of multi-head attention and the KV cache it implies.
- **[Paper · EN · ★]** "Mamba: Linear-Time Sequence Modeling with Selective State Spaces" — A. Gu, T. Dao · arXiv:2312.00752
  - The most credible alternative to attention for sequence modelling, with linear-time inference and constant-memory state. Relevant to the "does the KV cache problem disappear" question.
- **[Paper · EN · ★]** "A Survey of Large Language Models" — W. X. Zhao et al. · arXiv:2303.18223
  - Comprehensive survey across pre-training, adaptation, utilization and evaluation. Use as a structured map of the field rather than as a systems reference.

### Code

- **[Code · ★★★]** **xLLM** (github.com — JD.com) — Apache License, C++ primary
  - The implementation behind the technical report. Read the service/engine split and the hybrid KV cache path. Acknowledges ScaleLLM (graph construction and runtime), Mooncake (KV cache), brpc (HTTP service), tokenizers-cpp, safetensors and concurrentqueue.
- **[Code · ★★]** **Mooncake** — KV-cache-centric disaggregated serving store
- **[Code · ★★]** **FlashInfer / FlashAttention** — attention kernel libraries

---

## 06-2 · Agent Systems and Edge Orchestration
### Papers

- **[Paper · EN · ★★★]** "gRPC-Routed Agent Framework for Tasking (GRAFT)" · CAIS '26 · DOI 10.1145/3786335.3813216
  - The specific paper behind note 06-2: sessioned gRPC routing across heterogeneous personal devices, capability-aware task routing in a small-language-model agent mesh. Note that GRAFT is an overloaded acronym — cite the DOI, not the name.
- **[Paper · EN · ★★★]** "A Survey on Large Language Model based Autonomous Agents" — L. Wang et al. · arXiv:2308.11432
  - The standard taxonomy for agent systems: construction (profile/memory/planning/action), evaluation and application, with an explicit agent-society discussion. Use it to place any specific agent framework on a map.
- **[Paper · EN · ★★]** "The Rise and Potential of Large Language Model Based Agents: A Survey" — Z. Xi et al. · arXiv:2309.07864
  - A complementary survey with a stronger emphasis on the brain–perception–action decomposition and the open problems.
- **[Paper · EN · ★★★]** "ReAct: Synergizing Reasoning and Acting in Language Models" — S. Yao et al. · *ICLR 2023* · arXiv:2210.03629
  - Interleaves reasoning traces with actions. The baseline agent loop; most frameworks are variations on it.
- **[Paper · EN · ★★]** "Reflexion: Language Agents with Verbal Reinforcement Learning" — N. Shinn et al. · *NeurIPS 2023* · arXiv:2303.11366
  - Self-reflection with episodic memory, improving without gradient updates. Relevant to the "how does an agent improve at runtime" question.
- **[Paper · EN · ★★]** "Toolformer: Language Models Can Teach Themselves to Use Tools" — T. Schick et al. · *NeurIPS 2023* · arXiv:2302.04761
  - Self-supervised tool-use learning with API calls inserted into text. The origin of the tool-calling pattern.
- **[Paper · EN · ★★]** "Voyager: An Open-Ended Embodied Agent with Large Language Models" — G. Wang et al. · *TMLR 2024* · arXiv:2305.16291
  - Skill library, automatic curriculum and iterative prompting in a long-horizon embodied setting. Good example of persistent agent memory as a library of executable skills.
- **[Paper · EN · ★]** "Generative Agents: Interactive Simulacra of Human Behavior" — J. S. Park et al. · *UIST 2023* · arXiv:2304.03442
  - Memory stream, reflection and planning in a multi-agent simulation. Read for the memory-architecture design, not the social-simulation framing.
- **[Paper · EN · ★★]** "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation" — Q. Wu et al. · arXiv:2308.08155
  - Conversable-agent abstraction and multi-agent conversation orchestration. The clearest example of conversation-as-control-flow.
- **[Paper · EN · ★]** "MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework" — S. Hong et al. · *ICLR 2024* · arXiv:2308.00352
  - Encodes standardised operating procedures into agent prompts, structured around assembly-line division of labour.

### Cross-references

- **[Paper · ★★★]** Edge offloading and resource allocation papers in §09 (Satyanarayanan 2017; Shi et al. 2016; Mao et al. 2017)
  - The placement half of edge orchestration. An agent mesh that ignores the communication cost of placing a task is the failure mode to describe explicitly.
- **[Paper · ★★]** "Age of Information: An Introduction and Survey" (§06)
  - The metric to prefer over latency when agents are dispatching status-driven tasks.

---

## 06-3 · Machine Learning — Foundations, Core Algorithms and Applications
### Books

- **[Book · ★★★]** Gareth James, Daniela Witten, Trevor Hastie and Robert Tibshirani. *An Introduction to Statistical Learning with Applications in R*, 2nd ed. Springer, 2021. ISBN 978-1-0716-1417-4. <https://www.statlearning.com>
  - The best first book. Chapters 2–8 cover what this note covers in §5 and §9, with labs. The Python edition (ISLP, 2023) exists if you would rather not read R. Free PDF from the authors.
- **[Book · ★★★]** Aurélien Géron. *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow*, 3rd ed. O'Reilly, 2022. ISBN 978-1-098-12597-4
  - The practical counterpart: a full project end to end, then trees, ensembles, dimensionality reduction, neural networks, CNNs, RNNs and attention, autoencoders/GANs/diffusion, and reinforcement learning. Its Appendix A "Machine Learning Project Checklist" is the checklist in §3.1 written out properly.
- **[Book · ★★]** Trevor Hastie, Robert Tibshirani and Jerome Friedman. *The Elements of Statistical Learning*, 2nd ed. Springer, 2009. ISBN 978-0-387-84857-0. <https://hastie.su.domains/ElemStatLearn/>
  - The graduate version of ISLR, and free. Read chapters 3 (linear methods), 7 (model assessment), 9 (additive models and trees), 10 (boosting) and 15 (random forests) when you need the derivation, not the recipe.
- **[Book · ★★]** Christopher M. Bishop. *Pattern Recognition and Machine Learning*. Springer, 2006. ISBN 978-0-387-31073-2
  - The probabilistic view: §5.3's bias–variance decomposition and §5.9's regularisation story are cleanest here. Dense, and worth owning once you have finished ISLR.
- **[Book · ★★]** Kevin P. Murphy. *Probabilistic Machine Learning: An Introduction*. MIT Press, 2022. ISBN 978-0-262-04682-4. <https://probml.github.io/pml-book/book1.html>
  - The modern replacement for Bishop at twice the length, with the deep-learning material Bishop predates. Free online.
- **[Book · ★]** Ian Goodfellow, Yoshua Bengio and Aaron Courville. *Deep Learning*. MIT Press, 2016. ISBN 978-0-262-03561-3. <https://www.deeplearningbook.org>
  - Chapters 6–8 (deep networks and optimisation) are still the reference for backpropagation and for why the tricks in §6.5 exist. The later chapters have aged.

### Courses, guides and documentation

- **[Doc · ★★★]** scikit-learn developers. *User Guide — Choosing the right estimator; Common pitfalls and recommended practices*. <https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html> · <https://scikit-learn.org/stable/common_pitfalls.html>
  - The official flowchart for picking a model family, and the official statement of the preprocessing-leakage rule in §3.1. Short, and directly quotable in an interview.
- **[Doc · ★★★]** Google. *Machine Learning Crash Course*. <https://developers.google.com/machine-learning/crash-course>
  - The fastest route from zero to "I have trained something and I know what a learning rate is": gradient descent, generalisation, training sets, neural networks, embedding, and a fairness unit.
- **[Doc · ★★★]** Google. *Rules of Machine Learning: Best Practices for ML Engineering*. <http://martin.zinkevich.org/rules_of_ml/rules_of_ml.pdf>
  - Forty-three rules from people who shipped. It is where the advice in §2.2 ("start with a heuristic") and §12 ("keep the first model simple, design for iteration") comes from. Re-read it after your second project.
- **[Doc · ★★]** PyTorch Foundation. *PyTorch Tutorials*. <https://pytorch.org/tutorials/>
  - Enough to do weeks 1 and 4 of the learning path in §14: tensors and autograd, then a classifier, then transfer learning.
- **[Doc · ★★]** Aston Zhang, Zack Lipton, Mu Li, Alex Smola et al. *Dive into Deep Learning*. <https://d2l.ai>
  - One book-sized site with runnable code for every architecture in §7, including the convolutional output-size arithmetic and the attention implementation. Use it as the worked-code companion.
- **[Doc · ★]** Google. *Machine Learning Glossary*. <https://developers.google.com/machine-learning/glossary>
  - For when you need the standard definition of a term rather than a paraphrase.

### Papers — foundations

- **[Paper · ★★★]** Leo Breiman. "Random Forests." *Machine Learning* 45, 5–32, 2001. <https://link.springer.com/article/10.1023/A:1010933404324>
  - Bagging plus random feature subsets, out-of-bag error, and variable importance, from the inventor. Read the sections on the strength–correlation trade-off; it is the clearest explanation of why decorrelating the trees matters.
- **[Paper · ★★★]** Yoav Freund and Robert E. Schapire. "A Decision-Theoretic Generalization of On-Line Learning and an Application to Boosting." *Journal of Computer and System Sciences* 55(1), 119–139, 1997
  - AdaBoost, with the training-error bound that explains why boosting looks like it should overfit and mostly does not.
- **[Paper · ★★★]** Tianqi Chen and Carlos Guestrin. "XGBoost: A Scalable Tree Boosting System." arXiv:1603.02754, 2016 (KDD 2016). <https://arxiv.org/abs/1603.02754>
  - The system that made gradient boosting the default for tabular data: the regularised objective, the weighted quantile sketch for split finding, sparsity-aware handling of missing values, and the cache- and out-of-core-aware implementation.
- **[Paper · ★★]** James Bergstra and Yoshua Bengio. "Random Search for Hyper-Parameter Optimization." *JMLR* 13, 281–305, 2012. <https://jmlr.org/papers/v13/bergstra12a.html>
  - The two-page argument, with figures, for why random search beats grid search at equal budget. The reason — only a few hyperparameters matter, and grid search wastes trials on the rest — is worth stating from memory.
- **[Paper · ★★]** Lisha Li, Kevin Jamieson, Giulia DeSalvo, Afshin Rostamizadeh and Ameet Talwalkar. "Hyperband: A Novel Bandit-Based Approach to Hyperparameter Optimization." *JMLR* 18(185), 2018. <https://jmlr.org/papers/v18/16-558.html>
  - Successive halving done right, with the budget-versus-configuration trade-off made explicit.
- **[Paper · ★★]** Scott M. Lundberg and Su-In Lee. "A Unified Approach to Interpreting Model Predictions." arXiv:1705.07874, 2017 (NeurIPS 2017). <https://arxiv.org/abs/1705.07874>
  - SHAP. Read it for the additivity property and for the reminder that an explanation describes the model, not the world.
- **[Paper · ★]** Fei Tony Liu, Kai Ming Ting and Zhi-Hua Zhou. "Isolation Forest." *ICDM*, 2008
  - Anomaly detection by random splitting, with the expected-path-length argument that makes it linear-time and sub-sampling-friendly.
- **[Paper · ★]** David H. Wolpert and William G. Macready. "No Free Lunch Theorems for Optimization." *IEEE Transactions on Evolutionary Computation* 1(1), 67–82, 1997
  - The reason no algorithm is universally best. Cite it before anyone claims one is.
- **[Paper · ★]** Frank Rosenblatt. "The perceptron: a probabilistic model for information storage and organization in the brain." *Psychological Review* 65(6), 1958; and David E. Rumelhart, Geoffrey E. Hinton and Ronald J. Williams, "Learning representations by back-propagating errors," *Nature* 323, 1986
  - The two ends of the first neural-network cycle: the model, and the learning rule that made hidden layers usable.

### Papers — deep learning

- **[Paper · ★★★]** Alex Krizhevsky, Ilya Sutskever and Geoffrey E. Hinton. "ImageNet Classification with Deep Convolutional Neural Networks." *NeurIPS*, 2012. <https://papers.nips.cc/paper_files/paper/2012>
  - The paper that started the current era: 5 convolutional and 3 fully connected layers, 60 million parameters, 650,000 neurons, two GPUs, ReLU, dropout, data augmentation — and 15.3% top-5 error against 26.2% for the runner-up.
- **[Paper · ★★★]** Ashish Vaswani, Noam Shazeer, Niki Parmar et al. "Attention Is All You Need." arXiv:1706.03762, 2017. <https://arxiv.org/abs/1706.03762>
  - Scaled dot-product attention, multi-head attention, positional encoding, and the complexity table comparing self-attention with recurrent and convolutional layers. Note the `sqrt(d_k)` scaling and the reason given for it.
- **[Paper · ★★★]** Diederik P. Kingma and Jimmy Ba. "Adam: A Method for Stochastic Optimization." arXiv:1412.6980, 2014 (ICLR 2015). <https://arxiv.org/abs/1412.6980>
  - The update rules and the bias-correction terms. Three pages of actual algorithm.
- **[Paper · ★★]** Kaiming He, Xiangyu Zhang, Shaoqing Ren and Jian Sun. "Deep Residual Learning for Image Recognition." arXiv:1512.03385, 2015. <https://arxiv.org/abs/1512.03385>
  - Residual connections, the degradation problem they solve, and the 152-layer result. The identity-mapping follow-up (arXiv:1603.05027) is worth reading immediately afterwards.
- **[Paper · ★★]** Nitish Srivastava, Geoffrey Hinton, Alex Krizhevsky, Ilya Sutskever and Ruslan Salakhutdinov. "Dropout: A Simple Way to Prevent Neural Networks from Overfitting." *JMLR* 15(56), 2014. <https://jmlr.org/papers/v15/srivastava14a.html>
  - The technique, the inverted scaling at test time, and the interpretation as model averaging.
- **[Paper · ★★]** Sergey Ioffe and Christian Szegedy. "Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift." arXiv:1502.03167, 2015 (ICML 2015). <https://arxiv.org/abs/1502.03167>
  - The algorithm in full, including the inference-time population statistics — the part people get wrong in production.
- **[Paper · ★★]** Sepp Hochreiter and Jürgen Schmidhuber. "Long Short-Term Memory." *Neural Computation* 9(8), 1735–1780, 1997. <https://direct.mit.edu/neco/article/9/8/1735/6109>
  - The constant-error-carousel argument for the gates. Still the source to cite when someone says LSTMs are ad hoc.
- **[Paper · ★★]** Dzmitry Bahdanau, Kyunghyun Cho and Yoshua Bengio. "Neural Machine Translation by Jointly Learning to Align and Translate." arXiv:1409.0473, 2014. <https://arxiv.org/abs/1409.0473>
  - Attention as a soft alignment over all encoder states: the direct ancestor of §7.3.
- **[Paper · ★★]** Jonathan Ho, Ajay Jain and Pieter Abbeel. "Denoising Diffusion Probabilistic Models." arXiv:2006.11239, 2020. <https://arxiv.org/abs/2006.11239>
  - The forward noising process, the reverse-parameterisation choice, and — importantly — the simplified training objective of predicting the noise.
- **[Paper · ★]** Ian J. Goodfellow, Jean Pouget-Abadie, Mehdi Mirza et al. "Generative Adversarial Nets." arXiv:1406.2661, 2014. <https://arxiv.org/abs/1406.2661>
  - The minimax game, the global-optimality proof, and the failure modes everyone then spent a decade fixing.

### Papers — scaling and systems

- **[Paper · ★★★]** Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch et al. "Training Compute-Optimal Large Language Models." arXiv:2203.15556, 2022. <https://arxiv.org/abs/2203.15556>
  - The source of the "~20 training tokens per parameter" figure, and of the method (fit the loss–compute frontier across model sizes) that produced it.
- **[Paper · ★★]** Priya Goyal, Piotr Dollár, Ross Girshick et al. "Accurate, Large Minibatch SGD: Training ImageNet in 1 Hour." arXiv:1706.02677, 2017. <https://arxiv.org/abs/1706.02677>
  - The linear scaling rule for learning rate versus batch size, the warmup needed to make it work, and the batch-size ceiling past which it stops holding.
- **[Paper · ★★]** Samyam Rajbhandari, Jeff Rasley, Olatunji Ruwase and Yuxiong He. "ZeRO: Memory Optimizations Toward Training Trillion Parameter Models." arXiv:1910.02054, 2019 (SC 2020). <https://arxiv.org/abs/1910.02054>
  - The three stages of sharding optimiser state, gradients and parameters — the mechanism behind §8.3's memory arithmetic.
- **[Paper · ★★]** Mohammad Shoeybi, Mostofa Patwary, Raul Puri et al. "Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism." arXiv:1909.08053, 2019. <https://arxiv.org/abs/1909.08053>
  - Tensor parallelism done at layer granularity: the column-then-row split of the attention and MLP blocks, with the synchronisation points made explicit.
- **[Paper · ★]** Yanping Huang, Youlong Cheng, Ankur Bapna et al. "GPipe: Efficient Training of Giant Neural Networks using Pipeline Parallelism." arXiv:1811.06965, 2018. <https://arxiv.org/abs/1811.06965>
  - Microbatches and the pipeline bubble, quantified.

### Cross-references

- For what happens after training — serving, batching, quantisation and KV-cache management — see **§06-1**.
- For models that act rather than predict — planning, tools, safety boundaries — see **§06-2**.
- For these algorithms placed under a RAN's millisecond timing constraints and inside an O-RAN RIC, see **§01-3**.
- For where the training and serving compute physically sits, see **§05-2**.
- For the array semantics the Python stack depends on, see **§08-3**.

---

_Copyright (c) 2026 Washington Ruan and contributors · licensed under **GPL-3.0-or-later** or **AGPL-3.0-or-later**, at your option · see `LICENSE` and `LICENSE-AGPL`._
