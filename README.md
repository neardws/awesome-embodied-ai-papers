# 具身智能前沿方向调研结果

更新日期：2026-06-28

本 README 是调研结果索引：按方向总结具身智能前沿，并把已读公开来源中明确归属 CCF-A 会议的论文整理为细粒度表格。

## 总体判断

当前具身智能的热点可以分成六条线：VLN 大范围导航、VLA 操作策略、WAM 世界动作模型、Agentic Planning 推理规划、本体扩展/灵巧操作、轻量化/评测/数据。

最值得持续跟踪的系统路线是：

```text
任务理解与细粒度规划 agent
        -> WAM / world model 做想象、验证和失败预测
        -> 小 VLA、diffusion policy、技能库或传统控制执行
        -> 机器人本地安全闭环
```

原因很直接：单体 VLA 仍然重要，但真实机器人需要可解释规划、可执行约束、低延迟控制、失败恢复和端侧自治。

## 方向总览表

| 方向 | 子方向 | CCF-A 条目数 | 结果判断 |
| --- | --- | --- | --- |
| VLN / 大范围导航 | 连续环境 VLN、地图记忆、物理可执行导航、城市/开放环境导航、低成本/端侧导航 | 75 | VLN 关注语言目标、空间地图、记忆、探索和导航决策，核心问题是把自然语言任务变成可执行的大范围移动计划。当前 CCF-A 条目显示，研究正在从离散导航图转向连续环境、物理可执行导航、开放城市环境和低成本端侧导航。 |
| VLA / 操作策略 | generalist VLA、action representation、diffusion/flow policy、3D grounding、online/RL fine-tuning、安全鲁棒性 | 182 | VLA 是机械臂和移动操作的主战场，但它不只是“大模型接动作头”。CCF-A 论文集中在动作表示、diffusion/flow policy、3D grounding、在线/RL 微调和安全鲁棒性上。 |
| WAM / 世界模型 | cascaded WAM、joint WAM、video/latent world model、world model for VLA、world model evaluation | 46 | WAM 将未来世界状态预测和动作生成合在一起，适合放在 agent 规划和低层控制之间。它的价值不是替代所有控制器，而是提供可想象、可验证、可恢复的中间层。 |
| Agentic Planning / 推理规划 | 任务分解、memory、failure monitor、constraint / affordance planning、self-improving planning | 89 | 这一方向强调任务分解、记忆、失败监控、约束/affordance planning 和自改进规划。它最贴近“agent 规划，小模型或传统方法执行”的系统路线。 |
| 本体扩展 / 灵巧操作 | humanoid、bimanual、dexterous hand、tactile/contact-rich、grasp | 72 | 本体扩展决定具身智能是否能从单机械臂走向人形、双臂、灵巧手和触觉接触任务。表中论文体现了动作空间、传感方式和控制目标随本体变化而复杂化。 |
| 轻量化 / 评测 / 数据 | quantization/cache/tokenization、real-time execution、benchmark/dataset、sim2real、safety evaluation | 79 | 这一方向决定能不能真实部署：端侧推理、缓存/量化/action tokenization、实时执行、sim2real、benchmark 和 safety evaluation 都是必需条件。 |

## 各方向详细表格

### VLN / 大范围导航

VLN 关注语言目标、空间地图、记忆、探索和导航决策，核心问题是把自然语言任务变成可执行的大范围移动计划。当前 CCF-A 条目显示，研究正在从离散导航图转向连续环境、物理可执行导航、开放城市环境和低成本端侧导航。

子方向：连续环境 VLN、地图记忆、物理可执行导航、城市/开放环境导航、低成本/端侧导航。

共 75 篇。

| 子方向 | 条目数 | 观察重点 |
| --- | ---: | --- |
| 连续环境 VLN | 31 | 看是否从离散导航图走向连续观察和实时决策。 |
| 地图记忆 | 17 | 看地图表示、语义记忆、缓存和检索机制。 |
| 物理可执行导航 | 6 | 看真实本体约束、动态环境和安全解码。 |
| 城市/开放环境导航 | 18 | 看开放世界、城市、拥挤环境和长期导航。 |
| 低成本/端侧导航 | 3 | 看端侧推理、低成本记忆和数据效率。 |

#### 连续环境 VLN

共 31 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 来源 | 导航/评测属性 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ICLR 2026 | [Embodied Navigation Foundation Model](https://openreview.net/forum?id=kkBOIsrCXh) | VLN policy | 移动机器人/移动操作 | 提升语言导航的规划和泛化 | [paper](https://openreview.net/forum?id=kkBOIsrCXh) | EAI-VLA-VLN | 连续 VLN | 用于判断导航是否走向连续、物理和跨场景。 |
| ICLR 2026 | [Ground Slow, Move Fast: A Dual-System Foundation Model for Generalizable Vision-Language Navigation](https://openreview.net/forum?id=GK4rznYwhn) | VLN policy | 移动机器人/移动操作 | 提升语言导航的规划和泛化 | [paper](https://openreview.net/forum?id=GK4rznYwhn) | EAI-VLA-VLN | 连续 VLN | 用于判断导航是否走向连续、物理和跨场景。 |
| ICLR 2026 | [CompassNav: Steering From Path Imitation to Decision Understanding In Navigation](https://openreview.net/forum?id=eqcDckWHik) | VLN policy | 移动机器人/移动操作 | 提升语言导航的规划和泛化 | [paper](https://openreview.net/forum?id=eqcDckWHik) | - | 连续 VLN | 用于判断导航是否走向连续、物理和跨场景。 |
| ICLR 2026 | [M$^3$E: Continual Vision-and-Language Navigation via Mixture of Macro and Micro Experts](https://openreview.net/forum?id=pFh5ygjN3V) | VLN policy | 移动机器人/移动操作 | 提升语言导航的规划和泛化 | [paper](https://openreview.net/forum?id=pFh5ygjN3V) | - | 连续 VLN | 用于判断导航是否走向连续、物理和跨场景。 |
| ICLR 2026 | [OmniNav: A Unified Framework for Prospective Exploration and Visual-Language Navigation](https://openreview.net/forum?id=zGtTQTD1zu) | VLN policy | 移动机器人/移动操作 | 提升语言导航的规划和泛化 | [paper](https://openreview.net/forum?id=zGtTQTD1zu) | - | 连续 VLN | 用于判断导航是否走向连续、物理和跨场景。 |
| ICLR 2026 | [From Seeing to Experiencing: Scaling Navigation Foundation Models with Reinforcement Learning](https://openreview.net/forum?id=0c7nAZjyr5) | VLN policy | 移动机器人/移动操作 | 提升语言导航的规划和泛化 | [paper](https://openreview.net/forum?id=0c7nAZjyr5) | - | 连续 VLN | 用于判断导航是否走向连续、物理和跨场景。 |
| ICLR 2026 | [CE-Nav: Flow-Guided Reinforcement Refinement for Cross-Embodiment Local Navigation](https://openreview.net/forum?id=apaLoTumdO) | VLN policy | 移动机器人/移动操作 | 提升语言导航的规划和泛化 | [paper](https://openreview.net/forum?id=apaLoTumdO) | - | 连续 VLN | 用于判断导航是否走向连续、物理和跨场景。 |
| ICLR 2026 | [CoNavBench: Collaborative Long-Horizon Vision-Language Navigation Benchmark](https://openreview.net/forum?id=bMrH2PFMsi) | VLN policy | 移动机器人/移动操作 | 提升语言导航的规划和泛化 | [paper](https://openreview.net/forum?id=bMrH2PFMsi) | - | 评测/数据 | 用于判断导航是否走向连续、物理和跨场景。 |
| AAAI 2026 | [NaVLA$^2$: A Vision-Language-Audio-Action Model for Multimodal Instruction Navigation](https://ojs.aaai.org/index.php/AAAI/article/view/38886) | VLN policy | 移动机器人/移动操作 | 提升语言导航的规划和泛化 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38886) | - | 多模态导航 | 用于判断导航是否走向连续、物理和跨场景。 |
| AAAI 2026 | [VPN: Visual Prompt Navigation](https://ojs.aaai.org/index.php/AAAI/article/view/38888) | VLN policy | 移动机器人/移动操作 | 提升语言导航的规划和泛化 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38888) | - | 连续 VLN | 用于判断导航是否走向连续、物理和跨场景。 |
| AAAI 2026 | [SeqWalker: Sequential-Horizon Vision-and-Language Navigation with Hierarchical Planning](https://ojs.aaai.org/index.php/AAAI/article/view/38891) | VLN policy | 移动机器人/移动操作 | 提升语言导航的规划和泛化 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38891) | - | 连续 VLN | 用于判断导航是否走向连续、物理和跨场景。 |
| AAAI 2026 | [UNeMo: Collaborative Visual-Language Reasoning and Navigation via a Multimodal World Model](https://ojs.aaai.org/index.php/AAAI/article/view/38895) | VLN policy | 移动机器人/移动操作 | 提升语言导航的规划和泛化 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38895) | - | 世界模型导航 | 用于判断导航是否走向连续、物理和跨场景。 |
| AAAI 2026 | [DNOI-4DRO: Deep 4D Radar Odometry with Differentiable Neural-Optimization Iterations](https://ojs.aaai.org/index.php/AAAI/article/view/38914) | VLN policy | 移动机器人/移动操作 | 提升语言导航的规划和泛化 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38914) | - | 连续 VLN | 用于判断导航是否走向连续、物理和跨场景。 |
| AAAI 2026 | [Run, Ruminate, and Regulate: A Dual-process Thinking System for Vision-and-Language Navigation](https://ojs.aaai.org/index.php/AAAI/article/view/38954) | VLN policy | 移动机器人/移动操作 | 提升语言导航的规划和泛化 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38954) | - | 连续 VLN | 用于判断导航是否走向连续、物理和跨场景。 |
| ICML 2026 | [AdaNav: Adaptive Reasoning with Uncertainty for Vision-Language Navigation](https://icml.cc/virtual/2026/poster/61535) | reasoning | 移动机器人/移动操作 | 提升语言导航的规划和泛化 | [paper](https://icml.cc/virtual/2026/poster/61535) | - | 连续 VLN | 用于判断导航是否走向连续、物理和跨场景。 |
| ICML 2026 | [Instruction Decomposition and Action Alignment for Vision-Language Navigation](https://icml.cc/virtual/2026/poster/64780) | VLN policy | 移动机器人/移动操作 | 提升语言导航的规划和泛化 | [paper](https://icml.cc/virtual/2026/poster/64780) | - | 连续 VLN | 用于判断导航是否走向连续、物理和跨场景。 |
| ICML 2026 | [TIC-VLA: A Think-in-Control Vision-Language-Action Model for Robot Navigation in Dynamic Environments](https://icml.cc/virtual/2026/poster/65809) | VLA | 移动机器人/移动操作 | 改进视觉语言到动作策略 | [paper](https://icml.cc/virtual/2026/poster/65809) | - | 连续 VLN | 用于判断导航是否走向连续、物理和跨场景。 |
| ICML 2026 | [Hydra-Nav: Object Navigation via Adaptive Dual-Process Reasoning](https://icml.cc/virtual/2026/poster/61357) | reasoning | 移动机器人/移动操作 | 解决开放环境导航和决策 | [paper](https://icml.cc/virtual/2026/poster/61357) | - | 开放环境 | 用于判断导航是否走向连续、物理和跨场景。 |
| ICML 2026 | [SafeDec: Constrained Decoding for Safe Autoregressive Generalist Robot Navigation Policies](https://icml.cc/virtual/2026/poster/60775) | autoregressive policy | 移动机器人/移动操作 | 解决开放环境导航和决策 | [paper](https://icml.cc/virtual/2026/poster/60775) | - | 开放环境 | 用于判断导航是否走向连续、物理和跨场景。 |
| CVPR 2026 | [Wanderland: Geometrically Grounded Simulation for Open-World Embodied AI](https://arxiv.org/abs/2511.20620) | planning / RL | 仿真/评测环境 | 从离散导航走向连续环境 | [paper](https://arxiv.org/abs/2511.20620) / [project](https://ai4ce.github.io/wanderland/) | - | 评测/数据 | 用于判断导航是否走向连续、物理和跨场景。 |
| CVPR 2026 | [SpaceTools: Tool-Augmented Spatial Reasoning via Double Interactive RL](https://arxiv.org/abs/2512.04069) | planning / reasoning / RL | 移动机器人/导航环境 | 从离散导航走向连续环境 | [paper](https://arxiv.org/abs/2512.04069) / [project](https://spacetools.github.io/) | - | 连续 VLN | 用于判断导航是否走向连续、物理和跨场景。 |
| CVPR 2026 | [Dexterous World Models](https://arxiv.org/abs/2512.17907) | world model / planning / RL | 灵巧手/抓取 | 用世界预测支持机器人决策 | [paper](https://arxiv.org/abs/2512.17907) / [project](https://snuvclab.github.io/dwm/) / [code](https://github.com/snuvclab/dwm) | HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Humanoid-RL, WAM | 世界模型导航 | 用于判断导航是否走向连续、物理和跨场景。 |
| NeurIPS 2025 | [Distilling LLM Prior to Flow Model for Generalizable Agent’s Imagination in Object Goal Navigation](https://arxiv.org/abs/2508.09423) | flow matching | 移动机器人/移动操作 | 解决开放环境导航和决策 | [paper](https://arxiv.org/abs/2508.09423) | - | 开放环境 | 用于判断导航是否走向连续、物理和跨场景。 |
| NeurIPS 2025 | TP-MDDN: Task-Preferenced Multi-Demand-Driven Navigation with Autonomous Decision-Making | VLN policy | 移动机器人/移动操作 | 解决开放环境导航和决策 |  | - | 开放环境 | 用于判断导航是否走向连续、物理和跨场景。 |
| NeurIPS 2025 | [Active Test-time Vision-Language Navigation](https://arxiv.org/abs/2506.06630) | VLN policy | 移动机器人/移动操作 | 提升语言导航的规划和泛化 | [paper](https://arxiv.org/abs/2506.06630) | EAI-VLA-VLN | 连续 VLN | 用于判断导航是否走向连续、物理和跨场景。 |
| NeurIPS 2025 | [Seeing through Uncertainty: Robust Task-Oriented Optimization in Visual Navigation](https://arxiv.org/abs/2510.00441) | VLN policy | 移动机器人/移动操作 | 解决开放环境导航和决策 | [paper](https://arxiv.org/abs/2510.00441) / [project](https://github.com/PyyWill/NeuRO) | - | 开放环境 | 用于判断导航是否走向连续、物理和跨场景。 |
| ICCV 2025 | [P3Nav: A Unified Framework for Embodied Navigation Integrating Perception, Planning, and Prediction](https://arxiv.org/abs/2503.18525) | planning | 移动机器人/移动操作 | 解决开放环境导航和决策 | [paper](https://arxiv.org/abs/2503.18525) | EAI-VLA-VLN | 开放环境 | 用于判断导航是否走向连续、物理和跨场景。 |
| ICCV 2025 | [SAME: Learning Generic Language-Guided Visual Navigation with State-Adaptive Mixture of Experts](https://arxiv.org/abs/2412.05552) | VLN policy | 移动机器人/移动操作 | 解决开放环境导航和决策 | [paper](https://arxiv.org/abs/2412.05552) / [project](https://github.com/GengzeZhou/SAME) | Awesome-VLA, EAI-Safety | 开放环境 | 用于判断导航是否走向连续、物理和跨场景。 |
| ICCV 2025 | [Embodied Navigation with Auxiliary Task of Action Description Prediction](https://iccv.thecvf.com/virtual/2025/poster/1984) | VLN policy | 移动机器人/移动操作 | 解决开放环境导航和决策 | [paper](https://iccv.thecvf.com/virtual/2025/poster/1984) | - | 开放环境 | 用于判断导航是否走向连续、物理和跨场景。 |
| ICCV 2025 | [CogNav: Cognitive Process Modeling for Object Goal Navigation with LLMs](https://arxiv.org/abs/2412.10439) | planning | 移动机器人/移动操作 | 解决开放环境导航和决策 | [paper](https://arxiv.org/abs/2412.10439) / [project](https://yhancao.github.io/CogNav/) | - | 开放环境 | 用于判断导航是否走向连续、物理和跨场景。 |
| ICCV 2025 | [MoMa-Kitchen: A 100K+ Benchmark for Affordance-Grounded Last-Mile Navigation in Mobile Manipulation](https://arxiv.org/abs/2503.11081) | affordance | 移动机器人/移动操作 | 提供评测任务和数据基准 | [paper](https://arxiv.org/abs/2503.11081) / [project](https://momakitchen.github.io/) | - | 评测/数据 | 用于判断导航是否走向连续、物理和跨场景。 |

#### 地图记忆

共 17 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 来源 | 导航/评测属性 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ICLR 2026 | [Towards Physically Executable 3D Gaussian for Embodied Navigation](https://openreview.net/forum?id=HB6KvsqcAn) | map/memory | 移动机器人/移动操作 | 解决开放环境导航和决策 | [paper](https://openreview.net/forum?id=HB6KvsqcAn) | - | 地图/记忆 | 用于判断导航是否走向连续、物理和跨场景。 |
| ICLR 2026 | [Uncertainty-Aware Gaussian Map for Vision-Language Navigation](https://openreview.net/forum?id=LPv59noPAy) | map/memory | 移动机器人/移动操作 | 解决开放环境导航和决策 | [paper](https://openreview.net/forum?id=LPv59noPAy) | HCP-Survey, WAM | 地图/记忆 | 用于判断导航是否走向连续、物理和跨场景。 |
| ICLR 2026 | [JanusVLN: Decoupling Semantics and Spatiality with Dual Implicit Memory for Vision-Language Navigation](https://openreview.net/forum?id=RnuB0Nlbd5) | map/memory | 移动机器人/移动操作 | 解决开放环境导航和决策 | [paper](https://openreview.net/forum?id=RnuB0Nlbd5) | EAI-VLA-VLN | 地图/记忆 | 用于判断导航是否走向连续、物理和跨场景。 |
| ICLR 2026 | [Emergence of Spatial Representation in an Actor-Critic Agent with Hippocampus-Inspired Sequence Generator](https://openreview.net/forum?id=li1vfqDzRD) | map/memory | 移动机器人/移动操作 | 解决开放环境导航和决策 | [paper](https://openreview.net/forum?id=li1vfqDzRD) | - | 地图/记忆 | 用于判断导航是否走向连续、物理和跨场景。 |
| ICLR 2026 | [GRL-SNAM: Geometric Reinforcement Learning with Differential Hamiltonians for Navigation and Mapping in Unknown Environments](https://openreview.net/forum?id=KcC5mwfGf0) | map/memory | 移动机器人/移动操作 | 解决开放环境导航和决策 | [paper](https://openreview.net/forum?id=KcC5mwfGf0) | - | 地图/记忆 | 用于判断导航是否走向连续、物理和跨场景。 |
| AAAI 2026 | [RflyPano: A Panoramic Benchmark for Ultra-low Altitude UAV Localization Powered by RflySim](https://ojs.aaai.org/index.php/AAAI/article/view/38884) | map/memory | 移动机器人/移动操作 | 解决开放环境导航和决策 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38884) | - | 评测/数据 | 用于判断导航是否走向连续、物理和跨场景。 |
| AAAI 2026 | [MHED-SLAM: Multi-Scale Hybrid Encoding-Based Decoupled SLAM](https://ojs.aaai.org/index.php/AAAI/article/view/38887) | map/memory | 移动机器人/移动操作 | 解决开放环境导航和决策 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38887) | - | 地图/记忆 | 用于判断导航是否走向连续、物理和跨场景。 |
| AAAI 2026 | [LOG-Nav: Efficient Layout-Aware Object-Goal Navigation with Hierarchical Planning](https://ojs.aaai.org/index.php/AAAI/article/view/38893) | map/memory | 移动机器人/移动操作 | 解决开放环境导航和决策 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38893) | - | 地图/记忆 | 用于判断导航是否走向连续、物理和跨场景。 |
| AAAI 2026 | [PanoNav: Mapless Zero-Shot Object Navigation with Panoramic Scene Parsing and Dynamic Memory](https://ojs.aaai.org/index.php/AAAI/article/view/38899) | map/memory | 移动机器人/移动操作 | 解决开放环境导航和决策 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38899) | - | 地图/记忆 | 用于判断导航是否走向连续、物理和跨场景。 |
| AAAI 2026 | [Lightweight Adaptive Topological Layout and Semantic Mapping in Vision-and-Language Navigation on Websites](https://ojs.aaai.org/index.php/AAAI/article/view/38901) | map/memory | 移动机器人/移动操作 | 解决开放环境导航和决策 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38901) | - | 地图/记忆 | 用于判断导航是否走向连续、物理和跨场景。 |
| AAAI 2026 | [Expand Your SCOPE: Semantic Cognition over Potential-Based Exploration for Embodied Visual Navigation](https://ojs.aaai.org/index.php/AAAI/article/view/38929) | map/memory | 移动机器人/移动操作 | 解决开放环境导航和决策 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38929) | - | 地图/记忆 | 用于判断导航是否走向连续、物理和跨场景。 |
| AAAI 2026 | [Agent Journey Beyond RGB: Hierarchical Semantic-Spatial Representation Enrichment for Vision-and-Language Navigation](https://ojs.aaai.org/index.php/AAAI/article/view/38948) | map/memory | 移动机器人/移动操作 | 解决开放环境导航和决策 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38948) | - | 地图/记忆 | 用于判断导航是否走向连续、物理和跨场景。 |
| ICML 2026 | [MapDream: Task-Driven Map Learning for Vision-Language Navigation](https://icml.cc/virtual/2026/poster/64902) | map/memory | 移动机器人/移动操作 | 提升语言导航的规划和泛化 | [paper](https://icml.cc/virtual/2026/poster/64902) | - | 地图/记忆 | 用于判断导航是否走向连续、物理和跨场景。 |
| CVPR 2026 | [GLMap: Multi-Scale Gaussian-Language Map for Zero-shot Embodied Navigation and Reasoning](https://arxiv.org/abs/2605.01736) | planning / reasoning / 3D Gaussian | 移动机器人/移动操作 | 解决开放环境导航和决策 | [paper](https://arxiv.org/abs/2605.01736) / [code](https://github.com/sx-zhang/GLMap) | - | 地图/记忆 | 用于判断导航是否走向连续、物理和跨场景。 |
| NeurIPS 2025 | [EfficientNav: Towards On-Device Object-Goal Navigation with Navigation Map Caching and Retrieval](https://arxiv.org/abs/2510.18546) | map/memory | 移动机器人/移动操作 | 解决开放环境导航和决策 | [paper](https://arxiv.org/abs/2510.18546) | - | 地图/记忆 | 用于判断导航是否走向连续、物理和跨场景。 |
| ICCV 2025 | [Move to Understand a 3D Scene: Bridging Visual Grounding and Exploration for Efficient and Versatile Embodied Navigation](https://arxiv.org/abs/2507.04047) | 3D representation | 移动机器人/移动操作 | 解决开放环境导航和决策 | [paper](https://arxiv.org/abs/2507.04047) / [project](https://mtu3d.github.io/) | - | 地图/记忆 | 用于判断导航是否走向连续、物理和跨场景。 |
| ICCV 2025 | [NavQ: Learning a Q-Model for Foresighted Vision-and-Language Navigation](https://iccv.thecvf.com/virtual/2025/poster/944) | map/memory | 移动机器人/移动操作 | 提升语言导航的规划和泛化 | [paper](https://iccv.thecvf.com/virtual/2025/poster/944) | - | 地图/记忆 | 用于判断导航是否走向连续、物理和跨场景。 |

#### 物理可执行导航

共 6 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 来源 | 导航/评测属性 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AAAI 2026 | [CorrectNav: Self-Correction Flywheel Empowers Vision-Language-Action Navigation Model](https://ojs.aaai.org/index.php/AAAI/article/view/38942) | embodied navigation | 移动机器人/移动操作 | 提升语言导航的规划和泛化 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38942) | EAI-VLA-VLN | 连续 VLN | 用于判断导航是否走向连续、物理和跨场景。 |
| ICML 2026 | [SC$^{2}$-WM: A Self-Correcting World Model with Closed-Loop Feedback for Vision-and-Language Navigation in Continuous Environments](https://icml.cc/virtual/2026/poster/64257) | world model / RL | 移动机器人/移动操作 | 提升语言导航的规划和泛化 | [paper](https://icml.cc/virtual/2026/poster/64257) | - | 世界模型导航 | 用于判断导航是否走向连续、物理和跨场景。 |
| ICCV 2025 | [Rethinking the Embodied Gap in Vision-and-Language Navigation: A Holistic Study of Physical and Visual Disparities](https://arxiv.org/abs/2507.13019) | embodied navigation | 移动机器人/移动操作 | 提升语言导航的规划和泛化 | [paper](https://arxiv.org/abs/2507.13019) / [project](https://crystalsixone.github.io/vln_pe.github.io/) | - | 连续 VLN | 用于判断导航是否走向连续、物理和跨场景。 |
| ICCV 2025 | [NavMorph: A Self-Evolving World Model for Vision-and-Language Navigation in Continuous Environments](https://arxiv.org/abs/2506.23468) | world model / RL | 移动机器人/移动操作 | 提升语言导航的规划和泛化 | [paper](https://arxiv.org/abs/2506.23468) / [project](https://github.com/Feliciaxyao/NavMorph) | - | 世界模型导航 | 用于判断导航是否走向连续、物理和跨场景。 |
| ICCV 2025 | [3D Gaussian Map with Open-Set Semantic Grouping for Vision-Language Navigation](https://iccv.thecvf.com/virtual/2025/poster/299) | 3D representation / 3D Gaussian | 移动机器人/移动操作 | 提升语言导航的规划和泛化 | [paper](https://iccv.thecvf.com/virtual/2025/poster/299) | - | 地图/记忆 | 用于判断导航是否走向连续、物理和跨场景。 |
| ICCV 2025 | [monoVLN: Bridging the Observation Gap between Monocular and Panoramic Vision and Language Navigation](https://iccv.thecvf.com/virtual/2025/poster/1792) | embodied navigation | 移动机器人/移动操作 | 解决开放环境导航和决策 | [paper](https://iccv.thecvf.com/virtual/2025/poster/1792) | - | 开放环境 | 用于判断导航是否走向连续、物理和跨场景。 |

#### 城市/开放环境导航

共 18 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 来源 | 导航/评测属性 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ICLR 2026 | [AutoFly: Vision-Language-Action Model for UAV Autonomous Navigation in the Wild](https://openreview.net/forum?id=88RKxlFUNY) | open-world navigation | 无人机/城市环境 | 解决开放环境导航和决策 | [paper](https://openreview.net/forum?id=88RKxlFUNY) | - | 开放环境 | 用于判断导航是否走向连续、物理和跨场景。 |
| ICLR 2026 | [OpenFly: A COMPREHENSIVE PLATFORM FOR AERIAL VISION-LANGUAGE NAVIGATION](https://openreview.net/forum?id=OKm3w71ymP) | open-world navigation | 无人机/城市环境 | 解决开放环境导航和决策 | [paper](https://openreview.net/forum?id=OKm3w71ymP) | EAI-VLA-VLN | 开放环境 | 用于判断导航是否走向连续、物理和跨场景。 |
| ICLR 2026 | [All-day Multi-scenes Lifelong Vision-and-Language Navigation with Tucker Adaptation](https://openreview.net/forum?id=qSak1Hjfdq) | open-world navigation | 无人机/城市环境 | 解决开放环境导航和决策 | [paper](https://openreview.net/forum?id=qSak1Hjfdq) | - | 开放环境 | 用于判断导航是否走向连续、物理和跨场景。 |
| ICLR 2026 | [Lifelong Embodied Navigation Learning](https://openreview.net/forum?id=PaYo96rjij) | open-world navigation | 无人机/城市环境 | 解决开放环境导航和决策 | [paper](https://openreview.net/forum?id=PaYo96rjij) | - | 开放环境 | 用于判断导航是否走向连续、物理和跨场景。 |
| ICLR 2026 | [CitySeeker: How Do VLMs Explore Embodied Urban Navigation with Implicit Human Needs?](https://openreview.net/forum?id=hzf23XSDcs) | open-world navigation | 无人机/城市环境 | 解决开放环境导航和决策 | [paper](https://openreview.net/forum?id=hzf23XSDcs) | - | 开放环境 | 用于判断导航是否走向连续、物理和跨场景。 |
| AAAI 2026 | [AerialVLA: A Vision-Language-Action Model for Aerial Navigation with Online Dialogue](https://ojs.aaai.org/index.php/AAAI/article/view/38878) | open-world navigation | 无人机/城市环境 | 解决开放环境导航和决策 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38878) | - | 开放环境 | 用于判断导航是否走向连续、物理和跨场景。 |
| AAAI 2026 | [History-Enhanced Two-Stage Transformer for Aerial Vision-and-Language Navigation](https://ojs.aaai.org/index.php/AAAI/article/view/38885) | open-world navigation | 无人机/城市环境 | 解决开放环境导航和决策 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38885) | - | 开放环境 | 用于判断导航是否走向连续、物理和跨场景。 |
| AAAI 2026 | [RENEW: Risk- and Energy-Aware Navigation in Dynamic Waterways](https://ojs.aaai.org/index.php/AAAI/article/view/38897) | open-world navigation | 无人机/城市环境 | 解决开放环境导航和决策 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38897) | - | 开放环境 | 用于判断导航是否走向连续、物理和跨场景。 |
| AAAI 2026 | [Towards Autonomous UAV Visual Object Search in City Space: Benchmark and Agentic Methodology](https://ojs.aaai.org/index.php/AAAI/article/view/38898) | open-world navigation | 无人机/城市环境 | 解决开放环境导航和决策 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38898) | - | 评测/数据 | 用于判断导航是否走向连续、物理和跨场景。 |
| AAAI 2026 | [UrbanNav: Learning Language-Guided Embodied Urban Navigation from Web-Scale Human Trajectories](https://ojs.aaai.org/index.php/AAAI/article/view/38916) | open-world navigation | 无人机/城市环境 | 解决开放环境导航和决策 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38916) | - | 开放环境 | 用于判断导航是否走向连续、物理和跨场景。 |
| AAAI 2026 | [Autonomous Vehicle Path Planning by Searching with Differentiable Simulation](https://ojs.aaai.org/index.php/AAAI/article/view/38917) | open-world navigation | 无人机/城市环境 | 解决开放环境导航和决策 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38917) | - | 开放环境 | 用于判断导航是否走向连续、物理和跨场景。 |
| AAAI 2026 | [Real-Time Path Planning for UAVs in Windy Environments Without Computational Fluid Dynamics](https://ojs.aaai.org/index.php/AAAI/article/view/38920) | open-world navigation | 无人机/城市环境 | 解决开放环境导航和决策 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38920) | HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Efficient-VLA, Humanoid-RL, EAI-Safety, WAM | 开放环境 | 用于判断导航是否走向连续、物理和跨场景。 |
| AAAI 2026 | [ReflexDiffusion: Reflection-Enhanced Trajectory Planning for High-lateral-acceleration Scenarios in Autonomous Driving](https://ojs.aaai.org/index.php/AAAI/article/view/38938) | open-world navigation | 无人机/城市环境 | 解决开放环境导航和决策 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38938) | - | 开放环境 | 用于判断导航是否走向连续、物理和跨场景。 |
| AAAI 2026 | [Learning from Human Gaze: Human-like Robot Social Navigation in Dense Crowds](https://ojs.aaai.org/index.php/AAAI/article/view/38941) | open-world navigation | 无人机/城市环境 | 解决开放环境导航和决策 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38941) | - | 开放环境 | 用于判断导航是否走向连续、物理和跨场景。 |
| ICML 2026 | [Plan in Sandbox, Navigate in Open Worlds: Learning Physics-Grounded Abstracted Experience for Embodied Navigation](https://icml.cc/virtual/2026/poster/63554) | RL | 移动机器人/移动操作 | 解决开放环境导航和决策 | [paper](https://icml.cc/virtual/2026/poster/63554) | - | 开放环境 | 用于判断导航是否走向连续、物理和跨场景。 |
| NeurIPS 2025 | [C-NAV: Towards Self-Evolving Continual Object Navigation in Open World](https://arxiv.org/abs/2510.20685) | RL | 移动机器人/移动操作 | 解决开放环境导航和决策 | [paper](https://arxiv.org/abs/2510.20685) / [project](https://bigtree765.github.io/C-Nav-project/) | - | 开放环境 | 用于判断导航是否走向连续、物理和跨场景。 |
| NeurIPS 2025 | Synthesizing Photorealistic and Dynamic Urban Environments for Multimodal Robot Navigation and Collaboration | open-world navigation | 无人车/城市环境 | 解决开放环境导航和决策 |  | - | 开放环境 | 用于判断导航是否走向连续、物理和跨场景。 |
| CVPR 2025 | [RoboSense: Large-scale Dataset and Benchmark for Egocentric Robot Perception and Navigation in Crowded and Unstructured Environments](https://arxiv.org/abs/2408.15503) | open-world navigation | 移动机器人/移动操作 | 提供评测任务和数据基准 | [paper](https://arxiv.org/abs/2408.15503) / [project](https://github.com/suhaisheng/RoboSense) | - | 评测/数据 | 用于判断导航是否走向连续、物理和跨场景。 |

#### 低成本/端侧导航

共 3 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 来源 | 导航/评测属性 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NeurIPS 2025 | Aux-Think: Exploring Reasoning Strategies for Data-Efficient Vision-Language Navigation | reasoning | 移动机器人/移动操作 | 提升语言导航的规划和泛化 |  | EAI-VLA-VLN | 端侧/低成本 | 用于判断导航是否走向连续、物理和跨场景。 |
| ICCV 2025 | [Harnessing Input-adaptive Inference for Efficient VLN](https://openreview.net/pdf?id=5gptKWnVPF) | efficient navigation | 移动机器人/导航环境 | 提升推理或执行效率 | [paper](https://openreview.net/pdf?id=5gptKWnVPF) | - | 端侧/低成本 | 用于判断导航是否走向连续、物理和跨场景。 |
| ICCV 2025 | [COSMO: Combination of Selective Memorization for Low-cost Vision-and-Language Navigation](https://arxiv.org/abs/2503.24065) | efficient navigation | 移动机器人/移动操作 | 提升语言导航的规划和泛化 | [paper](https://arxiv.org/abs/2503.24065) | EAI-VLA-VLN | 端侧/低成本 | 用于判断导航是否走向连续、物理和跨场景。 |

### VLA / 操作策略

VLA 是机械臂和移动操作的主战场，但它不只是“大模型接动作头”。CCF-A 论文集中在动作表示、diffusion/flow policy、3D grounding、在线/RL 微调和安全鲁棒性上。

子方向：generalist VLA、action representation、diffusion/flow policy、3D grounding、online/RL fine-tuning、安全鲁棒性。

共 182 篇。

| 子方向 | 条目数 | 观察重点 |
| --- | ---: | --- |
| generalist VLA | 58 | 看跨任务泛化、真实机器人验证和通用操作能力。 |
| action representation | 18 | 看动作 token、latent action、chunking 和动作空间设计。 |
| diffusion/flow policy | 63 | 看连续动作生成、稳定控制和执行平滑性。 |
| 3D grounding | 28 | 看点云、几何、affordance 与操作定位。 |
| online/RL fine-tuning | 12 | 看在线强化、人在回路和测试时适配。 |
| 安全鲁棒性 | 3 | 看攻击鲁棒、安全对齐和风险暴露。 |

#### generalist VLA

共 58 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 来源 | 训练/动作属性 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ICLR 2026 | [MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation](https://openreview.net/forum?id=54U3XHf7qq) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://openreview.net/forum?id=54U3XHf7qq) | - | 通用 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [Disentangled Robot Learning via Separate Forward and Inverse Dynamics Pretraining](https://openreview.net/forum?id=DdrsHWobR1) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://openreview.net/forum?id=DdrsHWobR1) | - | 通用 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [Hybrid Training for Vision-Language-Action Models](https://openreview.net/forum?id=IBJtOltTbx) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://openreview.net/forum?id=IBJtOltTbx) | - | 通用 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [End-to-end Listen, Look, Speak and Act](https://openreview.net/forum?id=LYyoRqf0Ij) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://openreview.net/forum?id=LYyoRqf0Ij) | HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Humanoid-RL, EAI-Safety | 通用 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [RoboOmni: Proactive Robot Manipulation in Omni-modal Context](https://openreview.net/forum?id=OJh7oBCYhL) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://openreview.net/forum?id=OJh7oBCYhL) | WAM | 通用 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [Unified Vision-Language-Action Model](https://openreview.net/forum?id=PklMD8PwUy) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://openreview.net/forum?id=PklMD8PwUy) | HCP-Survey, EAI-VLA-VLN, Awesome-VLA, Efficient-VLA | 高效/轻量 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [Align-Then-stEer: Adapting the Vision-Language Action Models through Unified Latent Guidance](https://openreview.net/forum?id=T3i7Ifeatk) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://openreview.net/forum?id=T3i7Ifeatk) | Efficient-VLA | 高效/轻量 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [Verifier-free Test-Time Sampling for Vision Language Action Models](https://openreview.net/forum?id=UD4Rw8MOEK) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://openreview.net/forum?id=UD4Rw8MOEK) | EAI-VLA-VLN | 通用 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model](https://openreview.net/forum?id=kt51kZH4aG) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://openreview.net/forum?id=kt51kZH4aG) | EAI-VLA-VLN | 通用 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [VLM4VLA: Revisiting Vision-Language-Models in Vision-Language-Action Models](https://openreview.net/forum?id=tc2UsBeODW) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://openreview.net/forum?id=tc2UsBeODW) | EAI-VLA-VLN | 通用 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [Vision-Language-Action Instruction Tuning: From Understanding to Manipulation](https://openreview.net/forum?id=tsxwloasw5) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://openreview.net/forum?id=tsxwloasw5) | EAI-Guide, HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Efficient-VLA, Robot-Learning, Humanoid-RL, EAI-Safety, EAI-ROS, WAM, RL-VLA | RL/在线微调 | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [HAMLET: Switch Your Vision-Language-Action Model into a History-Aware Policy](https://openreview.net/forum?id=KcJ9U0x6kO) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://openreview.net/forum?id=KcJ9U0x6kO) | - | 通用 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| AAAI 2026 | [DiTEA: Mixture-of-Experts for Vision-Language-Action Model in Robotic Manipulation](https://ojs.aaai.org/index.php/AAAI/article/view/38902) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38902) | - | 通用 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| AAAI 2026 | [TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for Vision-Language-Action Models](https://ojs.aaai.org/index.php/AAAI/article/view/38910) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38910) | EAI-VLA-VLN | 通用 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2026 | [Vision-Language-Action Pretraining from Large-Scale Human Videos](https://icml.cc/virtual/2026/poster/62813) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://icml.cc/virtual/2026/poster/62813) | EAI-Guide, HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Efficient-VLA, Robot-Learning, Humanoid-RL, EAI-Safety, EAI-ROS, WAM, RL-VLA | RL/在线微调 | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2026 | [RA-VLA: Retrieval-Augmented VLA for Test-Time Adaptation](https://icml.cc/virtual/2026/poster/60980) | VLA | 机械臂/机器人操作 | 扩展跨任务操作能力 | [paper](https://icml.cc/virtual/2026/poster/60980) | - | 通用 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2026 | [A Generalist Pair-wise Progress Critic Model for Vision-Language-Action Robots](https://icml.cc/virtual/2026/poster/62270) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://icml.cc/virtual/2026/poster/62270) | - | 通用 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2026 | [Bring My Cup! Personalizing Vision-Language-Action Models with Visual Attentive Prompting](https://icml.cc/virtual/2026/poster/62528) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://icml.cc/virtual/2026/poster/62528) | - | 通用 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2026 | [From Abstraction to Instantiation: Learning Behavioral Representation for Vision-Language-Action Model](https://icml.cc/virtual/2026/poster/66596) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://icml.cc/virtual/2026/poster/66596) | - | 通用 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2026 | [VLA-ATTC: Adaptive Test-Time Compute for VLA Models with Relative Action Critic Model](https://icml.cc/virtual/2026/poster/61157) | VLA | 机械臂/机器人操作 | 扩展跨任务操作能力 | [paper](https://icml.cc/virtual/2026/poster/61157) | - | 通用 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2026 | [SCALE: Self-uncertainty Conditioned Adaptive Looking and Execution for Vision-Language-Action Models](https://icml.cc/virtual/2026/poster/66066) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://icml.cc/virtual/2026/poster/66066) | HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Efficient-VLA, Robot-Learning, Humanoid-RL, EAI-Safety, WAM, RL-VLA | RL/在线微调 | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2026 | [XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations](https://icml.cc/virtual/2026/poster/64826) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://icml.cc/virtual/2026/poster/64826) | - | 通用 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2026 | [Escaping the Diversity Trap in Robotic Manipulation via Anchor-Centric Adaptation](https://icml.cc/virtual/2026/poster/66510) | generalist VLA | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://icml.cc/virtual/2026/poster/66510) | - | 通用 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2026 | [Embodied Interpretability: Linking Causal Understanding to Generalization in Vision-Language-Action Models](https://icml.cc/virtual/2026/poster/63997) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://icml.cc/virtual/2026/poster/63997) | - | 通用 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2026 | [Evo-1: Lightweight Vision-Language-Action Model with Preserved Semantic Alignment](https://arxiv.org/abs/2511.04555) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2511.04555) / [code](https://github.com/MINT-SJTU/Evo-1) | - | 通用 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2026 | [HiF-VLA: Hindsight, Insight and Foresight through Motion Representation for Vision-Language-Action Models](https://arxiv.org/abs/2512.09928) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2512.09928) / [project](https://hifvla.github.io/) | - | 通用 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2026 | [SaPaVe: Towards Active Perception and Manipulation in Vision-Language-Action Models for Robotics](https://arxiv.org/abs/2603.12193) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2603.12193) / [project](https://lmzpai.github.io/SaPaVe) | - | 通用 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2026 | [Contact-Aware Neural Dynamics](https://arxiv.org/abs/2601.12796) | generalist VLA | 触觉/接触操作 | 扩展跨任务操作能力 | [paper](https://arxiv.org/abs/2601.12796) / [project](https://changwei-jing.github.io/neural-physics/) | Awesome-EAI, EAI-VLA-VLN | 通用 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | [CogVLA: Cognition-Aligned Vision-Language-Action Models via Instruction-Driven Routing & Sparsification](https://arxiv.org/abs/2508.21046) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2508.21046) / [project](https://jiutian-vl.github.io/CogVLA-page/) | EAI-VLA-VLN, Efficient-VLA | 高效/轻量 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | [Exploring the Limits of Vision-Language-Action Manipulation in Cross-task Generalization](https://arxiv.org/abs/2505.15660) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2505.15660) / [project](https://jiaming-zhou.github.io/AGNOSTOS/) | WAM | 通用 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | [Robo2VLM: Improving Visual Question Answering using Large-Scale Robot Manipulation Data](https://arxiv.org/abs/2505.15517) | VLA | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2505.15517) / [project](https://berkeleyautomation.github.io/robo2vlm/) | - | 通用 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | 4D-VLA: Spatiotemporal Vision-Language-Action Pretraining with Cross-Scene Calibration | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 |  | - | 通用 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | [Blindfolded Experts Generalize Better: Insights from Robotic Manipulation and Videogames](https://arxiv.org/abs/2510.24194) | VLA | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2510.24194) / [project](https://sites.google.com/view/blindfoldedexperts/home) | - | 通用 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | [HiMaCon: Discovering Hierarchical Manipulation Concepts from Unlabeled Multi-Modal Data](https://arxiv.org/abs/2510.11321) | VLA | 仿真/评测环境 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2510.11321) | - | 通用 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | [Knowledge Insulating Vision-Language-Action Models: Train Fast, Run Fast, Generalize Better](https://arxiv.org/abs/2505.23705) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2505.23705) | EAI-VLA-VLN | 通用 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | Diversifying Parallel Ergodic Search: A Signature Kernel Evolution Strategy | generalist VLA | 机械臂/机器人操作 | 扩展跨任务操作能力 |  | - | 通用 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICCV 2025 | [FedVLA: Federated Vision-Language-Action Learning with Dual Gating Mixture-of-Experts for Robotic Manipulation](https://iccv.thecvf.com/virtual/2025/poster/1325) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://iccv.thecvf.com/virtual/2025/poster/1325) | Efficient-VLA | 高效/轻量 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICCV 2025 | [PASG: A Closed-Loop Framework for Automated Geometric Primitive Extraction and Semantic Anchoring in Robotic Manipulation](https://iccv.thecvf.com/virtual/2025/poster/225) | VLA | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://iccv.thecvf.com/virtual/2025/poster/225) | - | 通用 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICCV 2025 | [iManip: Skill-Incremental Learning for Robotic Manipulation](https://arxiv.org/abs/2503.07087) | generalist VLA | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2503.07087) | EAI-VLA-VLN | 通用 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICCV 2025 | [4D Visual Pre-training for Robot Learning](https://iccv.thecvf.com/virtual/2025/poster/972) | generalist VLA | 机械臂/机器人操作 | 扩展跨任务操作能力 | [paper](https://iccv.thecvf.com/virtual/2025/poster/972) | - | 通用 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2025 | [Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models](https://arxiv.org/abs/2502.19417) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2502.19417) | EAI-VLA-VLN | 通用 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2025 | OTTER: A Vision-Language-Action Model with Text-Aware Visual Feature Extraction | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/pdf/2503.03734) / [project](https://ottervla.github.io/) | EAI-VLA-VLN | 通用 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2025 | UP-VLA: A Unified Understanding and Prediction Model for Embodied Agent | VLA | 机械臂/机器人操作 | 扩展跨任务操作能力 | [paper](https://arxiv.org/abs/2501.18867) | Awesome-EAI, Awesome-VLA | 通用 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2025 | ELEMENTAL: Interactive Learning from Demonstrations and Vision-Language Models for Reward Design in Robotics | VLA | 机械臂/机器人操作 | 扩展跨任务操作能力 | [paper](https://arxiv.org/abs/2411.18825) | - | 通用 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2025 | A Large Recurrent Action Model: xLSTM enables Fast Inference for Robotics Tasks | VLA | 机械臂/机器人操作 | 扩展跨任务操作能力 | [paper](https://arxiv.org/abs/2410.22391) / [project](https://github.com/ml-jku/LRAM) | - | 通用 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2025 | Pre-training Auto-regressive Robotic Models with 4D Representations | generalist VLA | 机械臂/机器人操作 | 扩展跨任务操作能力 | [paper](https://arxiv.org/pdf/2502.13142) / [project](https://arm4r.github.io/) | HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Efficient-VLA, Humanoid-RL, WAM | 高效/轻量 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2025 | STAR: Learning Diverse Robot Skill Abstractions through Rotation-Augmented | generalist VLA | 机械臂/机器人操作 | 扩展跨任务操作能力 | [paper](https://www.arxiv.org/pdf/2506.03863) | EAI-Guide, Octoday, HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Efficient-VLA, Robot-Learning, Humanoid-RL, EAI-Safety, RL-VLA | RL/在线微调 | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | [UniAct: Universal Actions For Enhanced Embodied Foundation Models](https://arxiv.org/abs/2501.10105) | VLA | 机械臂/机器人操作 | 扩展跨任务操作能力 | [paper](https://arxiv.org/abs/2501.10105) / [project](https://2toinf.github.io/UniAct/) | Awesome-EAI, Humanoid-RL | 通用 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | [MoManipVLA: Transferring Vision-language-action Models for General Mobile Manipulation](https://arxiv.org/abs/2503.13446) | VLA | 移动机器人/移动操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2503.13446) / [project](https://gary3410.github.io/momanipVLA/) | EAI-VLA-VLN, Efficient-VLA | 高效/轻量 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | [A Data-Centric Revisit of Pre-Trained Vision Models for Robot Learning](https://arxiv.org/abs/2503.06960) | VLA | 机械臂/机器人操作 | 扩展跨任务操作能力 | [paper](https://arxiv.org/abs/2503.06960) / [project](https://github.com/CVMI-Lab/SlotMIM) | - | 通用 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | Think Small, Act Big: Primitive Prompt Learning for Lifelong Robot Manipulation | VLA | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 |  | EAI-VLA-VLN | 通用 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | [Phoenix: A Motion-based Self-Reflection Framework for Fine-grained Robotic Action Correction](https://cvpr.thecvf.com/virtual/2025/poster/32789) | VLA | 机械臂/机器人操作 | 扩展跨任务操作能力 | [paper](https://cvpr.thecvf.com/virtual/2025/poster/32789) | - | 通用 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | [Mitigating the Human-Robot Domain Discrepancy in Visual Pre-training for Robotic Manipulation](https://arxiv.org/abs/2406.14235) | VLA | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2406.14235) | - | 通用 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | Object-Centric Prompt-Driven Vision-Language-Action Model for Robotic Manipulation | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 |  | HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Efficient-VLA, Robot-Learning, Humanoid-RL, EAI-Safety | 高效/轻量 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | Robotic Visual Instruction | VLA | 机械臂/机器人操作 | 扩展跨任务操作能力 |  | EAI-Guide, HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Efficient-VLA, Robot-Learning, Humanoid-RL, EAI-Safety, WAM, RL-VLA | RL/在线微调 | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | [RoboPEPP: Vision-Based Robot Pose and Joint Angle Estimation through Embedding Predictive Pre-Training](https://arxiv.org/abs/2411.17662) | generalist VLA | 机械臂/机器人操作 | 扩展跨任务操作能力 | [paper](https://arxiv.org/abs/2411.17662) | - | 通用 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | Two by Two: Learning Cross-Task Pairwise Objects Assembly for Generalizable Robot Manipulation | generalist VLA | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 |  | EAI-VLA-VLN | 通用 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | [Prof. Robot: Differentiable Robot Rendering Without Static and Self-Collisions](https://arxiv.org/abs/2503.11269) | generalist VLA | 机械臂/机器人操作 | 扩展跨任务操作能力 | [paper](https://arxiv.org/abs/2503.11269) / [project](https://www.qrcat.cn/prof-robot/) | - | 通用 VLA | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |

#### action representation

共 18 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 来源 | 训练/动作属性 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ICLR 2026 | [villa-X: Enhancing Latent Action Modeling in Vision-Language-Action Models](https://openreview.net/forum?id=y5CaJb17Fn) | action representation | 机械臂/机器人操作 | 改进动作表示和解码 | [paper](https://openreview.net/forum?id=y5CaJb17Fn) | EAI-VLA-VLN, WAM | 动作表示/tokenization | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [Rodrigues Network for Learning Robot Actions](https://openreview.net/forum?id=IZHk6BXBST) | action representation | 机械臂/机器人操作 | 改进动作表示和解码 | [paper](https://openreview.net/forum?id=IZHk6BXBST) | - | 动作表示/tokenization | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| AAAI 2026 | [Actor-Critic for Continuous Action Chunks: A Reinforcement Learning Framework for Long-Horizon Robotic Manipulation with Sparse Reward](https://ojs.aaai.org/index.php/AAAI/article/view/38937) | action representation | 机械臂/机器人操作 | 改进动作表示和解码 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38937) | EAI-VLA-VLN, EAI-Safety, RL-VLA | RL/在线微调 | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2026 | [DyGRO-VLA: Cross-Task Scaling of Vision-Language-Action Models via Dynamic Grouped Residual Optimization](https://icml.cc/virtual/2026/poster/60681) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://icml.cc/virtual/2026/poster/60681) | - | 动作表示/tokenization | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2026 | [LARA: Latent Action Representation Alignment for Vision-Language-Action Models](https://icml.cc/virtual/2026/poster/61232) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://icml.cc/virtual/2026/poster/61232) | - | 动作表示/tokenization | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2026 | [From Noise to Intent: Anchoring Generative VLA Policies with Residual Bridges](https://icml.cc/virtual/2026/poster/62908) | VLA | 机械臂/机器人操作 | 改进动作表示和解码 | [paper](https://icml.cc/virtual/2026/poster/62908) | - | 动作表示/tokenization | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2026 | [Demystifying Action Space Design for Robotic Manipulation Policies](https://icml.cc/virtual/2026/poster/65967) | action representation | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://icml.cc/virtual/2026/poster/65967) | - | 动作表示/tokenization | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2026 | [FocalPolicy: Frequency-Optimized Chunking and Locally Anchored Flow Matching for Coherent Visuomotor Policy](https://icml.cc/virtual/2026/poster/66520) | flow matching | 机械臂/机器人操作 | 改进动作表示和解码 | [paper](https://icml.cc/virtual/2026/poster/66520) | - | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2026 | [GeoMoLa: Geometry-Aware Motion Latents for Learning Robust Manipulation Policies](https://icml.cc/virtual/2026/poster/62176) | action representation | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://icml.cc/virtual/2026/poster/62176) | - | 动作表示/tokenization | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2026 | [Adaptive Action Chunking at Inference-time for Vision-Language-Action Models](https://arxiv.org/abs/2604.04161) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2604.04161) / [project](https://lance-lot.github.io/adaptive-chunking.github.io/) | - | 动作表示/tokenization | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2026 | [XL-VLA: Cross-Hand Latent Representation for Vision-Language-Action Models](https://arxiv.org/abs/2603.10158) | VLA | 灵巧手/抓取 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2603.10158) / [project](https://xl-vla.github.io/) | Efficient-VLA | 动作表示/tokenization | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | [Compliant Residual DAgger: Improving Real-World Contact-Rich Manipulation with Human Corrections](https://arxiv.org/abs/2506.16685) | VLA / RL | 触觉/接触操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2506.16685) / [project](https://compliant-residual-dagger.github.io/) | - | RL/在线微调 | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | [Learning Spatial-Aware Manipulation Ordering](https://arxiv.org/abs/2510.25138) | VLA | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2510.25138) | - | 动作表示/tokenization | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | [PRIMT: Preference-based Reinforcement Learning with Multimodal Feedback and Trajectory Synthesis from Foundation Models](https://arxiv.org/abs/2509.15607) | VLA / RL | 触觉/接触操作 | 改进动作表示和解码 | [paper](https://arxiv.org/abs/2509.15607) | - | RL/在线微调 | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | [Provable Ordering and Continuity in Vision-Language Pretraining for Generalizable Embodied Agents](https://arxiv.org/abs/2502.01218) | VLA | 机械臂/机器人操作 | 改进动作表示和解码 | [paper](https://arxiv.org/abs/2502.01218) / [project](https://actol-pretrain.github.io/) | - | 动作表示/tokenization | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | [Latent Policy Barrier: Learning Robust Visuomotor Policies by Staying In-Distribution](https://arxiv.org/abs/2508.05941) | action representation | 机械臂/机器人操作 | 改进动作表示和解码 | [paper](https://arxiv.org/abs/2508.05941) / [project](https://project-latentpolicybarrier.github.io/) | - | 动作表示/tokenization | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICCV 2025 | [Moto: Latent Motion Token as the Bridging Language for Learning Robot Manipulation from Videos](https://arxiv.org/abs/2412.04445) | VLA / action tokenization | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2412.04445) / [project](https://chenyi99.github.io/moto/) | - | 动作表示/tokenization | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | [Tra-MoE: Learning Trajectory Prediction Model from Multiple Domains for Adaptive Policy Conditioning](https://arxiv.org/abs/2411.14519) | action representation | 机械臂/机器人操作 | 改进动作表示和解码 | [paper](https://arxiv.org/abs/2411.14519) / [project](https://github.com/MCG-NJU/Tra-MoE) | - | 动作表示/tokenization | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |

#### diffusion/flow policy

共 63 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 来源 | 训练/动作属性 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ICLR 2026 | [Unifying Diffusion and Autoregression for Generalizable Vision-Language-Action Model](https://openreview.net/forum?id=H1KDMNOKQn) | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://openreview.net/forum?id=H1KDMNOKQn) | - | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [Unified Diffusion VLA: Vision-Language-Action Model via Joint Discrete Diffusion Diffusion Process](https://openreview.net/forum?id=UvQOcw2oCD) | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://openreview.net/forum?id=UvQOcw2oCD) | WAM | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [Master Skill Learning with Policy-Grounded Synergy of LLM-based Reward Shaping and Exploring](https://openreview.net/forum?id=1vXMfIYFZp) | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://openreview.net/forum?id=1vXMfIYFZp) | - | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [When would Vision-Proprioception Policies Fail in Robotic Manipulation?](https://openreview.net/forum?id=2RIqqNqALN) | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://openreview.net/forum?id=2RIqqNqALN) | - | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [Capturing Visual Environment Structure Correlates with Control Performance](https://openreview.net/forum?id=AmczI1k3Yk) | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://openreview.net/forum?id=AmczI1k3Yk) | - | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [VITA: Vision-to-Action Flow Matching Policy](https://openreview.net/forum?id=BTe5VLBjPg) | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://openreview.net/forum?id=BTe5VLBjPg) | EAI-VLA-VLN | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [When a Robot is More Capable than a Human: Learning from Constrained Demonstrators](https://openreview.net/forum?id=BvirMuKWV1) | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://openreview.net/forum?id=BvirMuKWV1) | - | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [Autonomous Play with Correspondence-Driven Trajectory Warping](https://openreview.net/forum?id=FqDmvMZish) | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://openreview.net/forum?id=FqDmvMZish) | - | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [Reference Guided Skill Discovery](https://openreview.net/forum?id=IaGf8Eh5Uo) | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://openreview.net/forum?id=IaGf8Eh5Uo) | - | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [Masked Generative Policy for Robotic Control](https://openreview.net/forum?id=KFu4p3pd11) | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://openreview.net/forum?id=KFu4p3pd11) | - | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [Learning Video Generation for Robotic Manipulation with Collaborative Trajectory Control](https://openreview.net/forum?id=OeDwYtp8n1) | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://openreview.net/forum?id=OeDwYtp8n1) | - | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [Policy Contrastive Decoding for Robotic Foundation Models](https://openreview.net/forum?id=P9PVdWyM3U) | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://openreview.net/forum?id=P9PVdWyM3U) | - | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [Demystifying Robot Diffusion Policies: Action Memorization and a Simple Lookup Table Alternative](https://openreview.net/forum?id=PL0tJOfm7I) | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://openreview.net/forum?id=PL0tJOfm7I) | - | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [H$^3$DP: Triply‑Hierarchical Diffusion Policy for Visuomotor Learning](https://openreview.net/forum?id=Q1CP0iAmOb) | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://openreview.net/forum?id=Q1CP0iAmOb) | - | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [Compose Your Policies! Improving Diffusion-based or Flow-based Robot Policies via Test-time Distribution-level Composition](https://openreview.net/forum?id=TnLFRhLuZ6) | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://openreview.net/forum?id=TnLFRhLuZ6) | EAI-VLA-VLN | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [Abstracting Robot Manipulation Skills via Mixture-of-Experts Diffusion Policies](https://openreview.net/forum?id=VSWjHIveqZ) | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://openreview.net/forum?id=VSWjHIveqZ) | - | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [Accelerated co-design of robots through morphological pretraining](https://openreview.net/forum?id=WVliGyFwZv) | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://openreview.net/forum?id=WVliGyFwZv) | - | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [VER: Vision Expert Transformer for Robot Learning via Foundation Distillation and Dynamic Routing](https://openreview.net/forum?id=aoorNQFpM6) | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://openreview.net/forum?id=aoorNQFpM6) | Awesome-VLA | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [SpikePingpong: Spike Vision-based Fast-Slow Pingpong Robot System](https://openreview.net/forum?id=d08yOXs1Dl) | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://openreview.net/forum?id=d08yOXs1Dl) | EAI-VLA-VLN | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [Translating Flow to Policy via Hindsight Online Imitation](https://openreview.net/forum?id=dQ6d5bgXtM) | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://openreview.net/forum?id=dQ6d5bgXtM) | - | RL/在线微调 | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [Cortical Policy: A Dual-Stream View Transformer for Robotic Manipulation](https://openreview.net/forum?id=eWe8zqGvs5) | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://openreview.net/forum?id=eWe8zqGvs5) | - | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [Contractive Diffusion Policies: Robust Action Diffusion via Contractive Score-Based Sampling with Differential Equations](https://openreview.net/forum?id=iKJbmx1iuQ) | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://openreview.net/forum?id=iKJbmx1iuQ) | - | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [Scalable Exploration for High-Dimensional Continuous Control via Value-Guided Flow](https://openreview.net/forum?id=kIYNtxE13h) | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://openreview.net/forum?id=kIYNtxE13h) | - | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [ViPRA: Video Prediction for Robot Actions](https://openreview.net/forum?id=w3Ik8HUyTT) | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://openreview.net/forum?id=w3Ik8HUyTT) | - | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [DataMIL: Selecting Data for Robot Imitation Learning with Datamodels](https://openreview.net/forum?id=AcTsKglDdh) | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://openreview.net/forum?id=AcTsKglDdh) | EAI-VLA-VLN | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [MIMIC: Mask-Injected Manipulation Video Generation with Interaction Control](https://openreview.net/forum?id=COrUdVuInH) | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://openreview.net/forum?id=COrUdVuInH) | WAM | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [LeRobot: An Open-Source Library for End-to-End Robot Learning](https://openreview.net/forum?id=CiZMMAFQR3) | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://openreview.net/forum?id=CiZMMAFQR3) | EAI-VLA-VLN, Awesome-VLA, Efficient-VLA, Robot-Learning, WAM | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| AAAI 2026 | [ManiLong-Shot: Interaction-Aware One-Shot Imitation Learning for Long-Horizon Manipulation](https://ojs.aaai.org/index.php/AAAI/article/view/38881) | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38881) | - | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| AAAI 2026 | [Learning Diffusion Policy from Primitive Skills for Robot Manipulation](https://ojs.aaai.org/index.php/AAAI/article/view/38889) | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38889) | - | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| AAAI 2026 | [Intention-Aware Diffusion Model for Pedestrian Trajectory Prediction](https://ojs.aaai.org/index.php/AAAI/article/view/38912) | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38912) | Humanoid-RL | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| AAAI 2026 | [MP1: MeanFlow Tames Policy Learning in 1-step for Robotic Manipulation](https://ojs.aaai.org/index.php/AAAI/article/view/38919) | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38919) | EAI-VLA-VLN | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| AAAI 2026 | [ForeDiffusion: Foresight-Conditioned Diffusion Policy via Future View Construction for Robot Manipulation](https://ojs.aaai.org/index.php/AAAI/article/view/38934) | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38934) | - | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| AAAI 2026 | [Balancing Signal and Variance: Adaptive Offline RL Post-Training for VLA Flow Models](https://ojs.aaai.org/index.php/AAAI/article/view/38944) | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38944) | Efficient-VLA, RL-VLA | RL/在线微调 | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| AAAI 2026 | [Bridging Scale Discrepancies in Robotic Control via Language-Based Action Representations](https://ojs.aaai.org/index.php/AAAI/article/view/38950) | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38950) | - | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| AAAI 2026 | [D²PPO: Diffusion Policy Policy Optimization with Dispersive Loss](https://ojs.aaai.org/index.php/AAAI/article/view/38959) | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38959) | - | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2026 | [Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies](https://icml.cc/virtual/2026/poster/62902) | VLA / diffusion policy | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://icml.cc/virtual/2026/poster/62902) | EAI-VLA-VLN, Efficient-VLA | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2026 | [STEP: Warm-Started Visuomotor Policies with Spatiotemporal Consistency Prediction](https://icml.cc/virtual/2026/poster/61717) | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://icml.cc/virtual/2026/poster/61717) | HCP-Survey, EAI-VLA-VLN, Humanoid-RL | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2026 | [Learning Human-Robot Collaboration via Heterogeneous-Agent Lyapunov Policy Optimization](https://icml.cc/virtual/2026/poster/61049) | diffusion/flow policy | 仿真/评测环境 | 提升连续动作生成质量 | [paper](https://icml.cc/virtual/2026/poster/61049) | - | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2026 | [SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models](https://arxiv.org/abs/2511.15605) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2511.15605) | WAM, RL-VLA | RL/在线微调 | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | [AC-DiT: Adaptive Coordination Diffusion Transformer for Mobile Manipulation](https://arxiv.org/abs/2507.01961) | VLA / diffusion policy / diffusion transformer | 移动机器人/移动操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2507.01961) / [project](https://ac-dit.github.io/) | EAI-VLA-VLN | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | [PointMapPolicy: Structured Point Cloud Processing for Multi-Modal Imitation Learning](https://arxiv.org/abs/2510.20406) | VLA | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://arxiv.org/abs/2510.20406) | - | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | Emerging Risks from Embodied AI Require Urgent Policy Action | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 |  | EAI-Safety | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | [Human-assisted Robotic Policy Refinement via Action Preference Optimization](https://arxiv.org/abs/2506.07127) | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://arxiv.org/abs/2506.07127) / [project](https://gewu-lab.github.io/action_preference_optimization/) | - | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | *Hyper-GoalNet*: Goal-Conditioned Manipulation Policy Learning with HyperNetworks | diffusion/flow policy | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 |  | - | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | [ReinFlow: Fine-tuning Flow Matching Policy with Online Reinforcement Learning](https://arxiv.org/abs/2505.22094) | flow matching / RL | 触觉/接触操作 | 提升连续动作生成质量 | [paper](https://arxiv.org/abs/2505.22094) / [project](https://reinflow.github.io/) | RL-VLA | RL/在线微调 | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | [A Practical Guide for Incorporating Symmetry in Diffusion Policy](https://arxiv.org/abs/2505.13431) | diffusion policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://arxiv.org/abs/2505.13431) | EAI-VLA-VLN | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | [Act to See, See to Act: Diffusion-Driven Perception-Action Interplay for Adaptive Policies](https://arxiv.org/abs/2509.25822) | diffusion policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://arxiv.org/abs/2509.25822) / [project](https://jingwang18.github.io/dp-ag.github.io/) | - | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | [Dynamic Test-Time Compute Scaling in Control Policy: Difficulty-Aware Stochastic Interpolant Policy](https://arxiv.org/abs/2511.20906) | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://arxiv.org/abs/2511.20906) | - | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | [DynaGuide: Steering Diffusion Polices with Active Dynamic Guidance](https://arxiv.org/abs/2506.13922) | diffusion policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://arxiv.org/abs/2506.13922) / [project](https://dynaguide.github.io/) | - | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICCV 2025 | [Dita: Scaling Diffusion Transformer for Generalist Vision-Language-Action Policy](https://arxiv.org/abs/2503.19757) | VLA / diffusion policy / diffusion transformer | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2503.19757) / [project](https://robodita.github.io/) | EAI-VLA-VLN | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICCV 2025 | [SD2Actor: Continuous State Decomposition via Diffusion Embeddings for Robotic Manipulation](https://iccv.thecvf.com/virtual/2025/poster/1571) | VLA / diffusion policy | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://iccv.thecvf.com/virtual/2025/poster/1571) | - | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICCV 2025 | [EC-Flow: Enabling Versatile Robotic Manipulation from Action-Unlabeled Videos via Embodiment-Centric Flow](https://arxiv.org/abs/2507.06224) | flow matching | 仿真/评测环境 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2507.06224) / [project](https://ec-flow1.github.io/) | - | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICCV 2025 | [Dense Policy: Bidirectional Autoregressive Learning of Actions](https://arxiv.org/abs/2503.13217) | autoregressive policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://arxiv.org/abs/2503.13217) / [project](https://selen-suyue.github.io/DspNet/) | EAI-VLA-VLN | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICCV 2025 | [Spatial-Temporal Aware Visuomotor Diffusion Policy Learning](https://arxiv.org/abs/2507.06710) | diffusion policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://arxiv.org/abs/2507.06710) / [project](https://zhenyangliu.github.io/DP4/) | HCP-Survey, EAI-VLA-VLN, Awesome-VLA, EAI-Safety | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICCV 2025 | [Wavelet Policy: Lifting Scheme for Policy Learning in Long-Horizon Tasks](https://arxiv.org/abs/2507.04331) | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://arxiv.org/abs/2507.04331) / [project](https://hhuang-code.github.io/wavelet_policy/) | - | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2025 | Flow-based Domain Randomization for Learning and Sequencing Robotic Skills | flow matching | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://arxiv.org/pdf/2502.01800) | EAI-VLA-VLN, Efficient-VLA, EAI-ROS | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2025 | Learning Policy Committees for Effective Personalization in MDPs with Diverse Tasks | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://arxiv.org/abs/2503.01885) | - | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | [Lift3D Policy: Lifting 2D Foundation Models for Robust 3D Robotic Manipulation](https://arxiv.org/abs/2411.18623) | 3D representation | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2411.18623) / [project](https://lift3d-web.github.io/) | EAI-VLA-VLN | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | PDFactor: Learning Tri-Perspective View Policy Diffusion Field for Multi-Task Robotic Manipulation | diffusion policy | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 |  | - | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | FlowRAM: Grounding Flow Matching Policy with Region-Aware Mamba Framework for Robotic Manipulation | flow matching | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 |  | Efficient-VLA | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | [G3Flow: Generative 3D Semantic Flow for Pose-aware and Generalizable Object Manipulation](https://arxiv.org/abs/2411.18369) | flow matching / 3D representation | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2411.18369) / [project](https://tianxingchen.github.io/G3Flow/) | EAI-VLA-VLN | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | [AffordDP: Generalizable Diffusion Policy with Transferable Affordance](https://arxiv.org/abs/2412.03142) | diffusion policy / affordance | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://arxiv.org/abs/2412.03142) / [project](https://afforddp.github.io/) | - | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | Touch2Shape: Touch-Conditioned 3D Diffusion for Shape Exploration and Reconstruction | diffusion policy / 3D representation | 触觉/接触操作 | 提升连续动作生成质量 |  | - | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |

#### 3D grounding

共 28 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 来源 | 训练/动作属性 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ICLR 2026 | [PixelVLA: Advancing Pixel-level Understanding in Vision-Language-Action Model](https://openreview.net/forum?id=7M6ryCABIc) | 3D representation | 机械臂/机器人操作 | 增强空间理解和操作定位 | [paper](https://openreview.net/forum?id=7M6ryCABIc) | - | 3D grounding | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [Spatially Guided Training for Vision-Language-Action Model](https://openreview.net/forum?id=eKhOrQWAVJ) | 3D representation | 机械臂/机器人操作 | 增强空间理解和操作定位 | [paper](https://openreview.net/forum?id=eKhOrQWAVJ) | - | 3D grounding | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model](https://openreview.net/forum?id=euMVC1DO4k) | 3D representation | 机械臂/机器人操作 | 增强空间理解和操作定位 | [paper](https://openreview.net/forum?id=euMVC1DO4k) | EAI-VLA-VLN | 3D grounding | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [From Spatial to Actions: Grounding Vision-Language-Action Model in Spatial Foundation Priors](https://openreview.net/forum?id=fzmittHfq3) | 3D representation | 机械臂/机器人操作 | 增强空间理解和操作定位 | [paper](https://openreview.net/forum?id=fzmittHfq3) | - | 3D grounding | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [Geometry-aware 4D Video Generation for Robot Manipulation](https://openreview.net/forum?id=18gC6pZVVc) | 3D representation | 机械臂/机器人操作 | 增强空间理解和操作定位 | [paper](https://openreview.net/forum?id=18gC6pZVVc) | HCP-Survey, Awesome-EAI, Humanoid-RL, WAM | 3D grounding | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [Generalizable Coarse-to-Fine Robot Manipulation via Language-Aligned 3D Keypoints](https://openreview.net/forum?id=WXFfMLyB6y) | 3D representation | 机械臂/机器人操作 | 增强空间理解和操作定位 | [paper](https://openreview.net/forum?id=WXFfMLyB6y) | - | 3D grounding | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [Geometry-aware Policy Imitation](https://openreview.net/forum?id=ggofj6tyr3) | 3D representation | 机械臂/机器人操作 | 增强空间理解和操作定位 | [paper](https://openreview.net/forum?id=ggofj6tyr3) | HCP-Survey, Awesome-EAI, Humanoid-RL, WAM | 3D grounding | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [Learning Part-Aware Dense 3D Feature Field For Generalizable Articulated Object Manipulation](https://openreview.net/forum?id=qXfRXfAHOK) | 3D representation | 机械臂/机器人操作 | 增强空间理解和操作定位 | [paper](https://openreview.net/forum?id=qXfRXfAHOK) | - | 3D grounding | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [RAVEN: End-to-end Equivariant Robot Learning with RGB Cameras](https://openreview.net/forum?id=z8BN7KyaPl) | 3D representation | 机械臂/机器人操作 | 增强空间理解和操作定位 | [paper](https://openreview.net/forum?id=z8BN7KyaPl) | - | 3D grounding | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [On the Generalization Capacities of MLLMs for Spatial Intelligence](https://openreview.net/forum?id=DE5ZJtR4bg) | 3D representation | 机械臂/机器人操作 | 增强空间理解和操作定位 | [paper](https://openreview.net/forum?id=DE5ZJtR4bg) | - | 3D grounding | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| AAAI 2026 | [ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver](https://ojs.aaai.org/index.php/AAAI/article/view/38921) | 3D representation | 机械臂/机器人操作 | 增强空间理解和操作定位 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38921) | EAI-VLA-VLN | 3D grounding | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| AAAI 2026 | [Indoor Multi-View Radar Object Detection via 3D Bounding Box Diffusion](https://ojs.aaai.org/index.php/AAAI/article/view/38939) | 3D representation | 机械臂/机器人操作 | 增强空间理解和操作定位 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38939) | - | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| AAAI 2026 | [RaLD: Generating High-Resolution 3D Radar Point Clouds with Latent Diffusion](https://ojs.aaai.org/index.php/AAAI/article/view/38946) | 3D representation | 机械臂/机器人操作 | 增强空间理解和操作定位 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38946) | - | diffusion/flow policy | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| AAAI 2026 | [Grounding Actions in Camera Space: Observation-Centric Vision-Language-Action Policy](https://ojs.aaai.org/index.php/AAAI/article/view/38947) | 3D representation | 机械臂/机器人操作 | 增强空间理解和操作定位 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38947) | EAI-VLA-VLN | 3D grounding | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | [DynaRend: Learning 3D Dynamics via Masked Future Rendering for Robotic Manipulation](https://arxiv.org/abs/2510.24261) | 3D representation | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2510.24261) | - | 3D grounding | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | [Building 3D Representations and Generating Motions From a Single Image via Video-Generation](https://neurips.cc/virtual/2025/loc/san-diego/poster/118141) | 3D representation | 机械臂/机器人操作 | 增强空间理解和操作定位 | [paper](https://neurips.cc/virtual/2025/loc/san-diego/poster/118141) | - | 3D grounding | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICCV 2025 | [A0: An Affordance-Aware Hierarchical Model for General Robotic Manipulation](https://arxiv.org/abs/2504.12636) | VLA / affordance | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2504.12636) / [project](https://a-embodied.github.io/A0/) | EAI-VLA-VLN | 3D grounding | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICCV 2025 | [Learning Precise Affordances from Egocentric Videos for Robotic Manipulation](https://arxiv.org/abs/2408.10123v1) | affordance | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2408.10123v1) / [project](https://reagan1311.github.io/affgrasp) | - | 3D grounding | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICCV 2025 | [EmbodiedOcc: Embodied 3D Occupancy Prediction for Vision-based Online Scene Understanding](https://arxiv.org/abs/2412.04380) | 3D representation | 机械臂/机器人操作 | 增强空间理解和操作定位 | [paper](https://arxiv.org/abs/2412.04380) / [project](https://ykiwu.github.io/EmbodiedOcc/) | - | RL/在线微调 | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICCV 2025 | [Embodied Image Captioning: Self-supervised Learning Agents for Spatially Coherent Image Descriptions](https://arxiv.org/abs/2504.08531) | 3D grounding | 机械臂/机器人操作 | 增强空间理解和操作定位 | [paper](https://arxiv.org/abs/2504.08531) / [project](https://hsp-iit.github.io/embodied-captioning/) | - | 3D grounding | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2025 | Unifying 2D and 3D Vision-Language Understanding | 3D representation | 机械臂/机器人操作 | 增强空间理解和操作定位 | [paper](https://arxiv.org/abs/2503.10745) / [project](https://univlg.github.io/) | - | 3D grounding | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2025 | GAPrompt: Geometry-Aware Point Cloud Prompt for 3D Vision Model | 3D representation | 机械臂/机器人操作 | 增强空间理解和操作定位 | [paper](https://arxiv.org/abs/2505.04119) / [project](https://github.com/zhoujiahuan1991/ICML2025-GAPrompt) | - | 3D grounding | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | [SOLAMI: Social Vision-Language-Action Modeling for Immersive Interaction with 3D Autonomous Characters](https://arxiv.org/abs/2412.00174) | VLA / 3D representation | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2412.00174) / [project](https://solami-ai.github.io/) | - | 3D grounding | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | [OmniManip: Towards General Robotic Manipulation via Object-Centric Interaction Primitives as Spatial Constraints](https://arxiv.org/abs/2501.03841) | VLA | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2501.03841) / [project](https://omnimanip.github.io/) | EAI-VLA-VLN | 3D grounding | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | RoboGround: Robot Manipulation with Grounded Vision-Language Priors | VLA | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 |  | EAI-VLA-VLN | 3D grounding | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | [3D-MVP: 3D Multiview Pretraining for Robotic Manipulation](https://arxiv.org/abs/2406.18158) | 3D representation | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2406.18158) / [project](https://jasonqsy.github.io/3DMVP/) | - | 3D grounding | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | [VidBot: Learning Generalizable 3D Actions from In-the-Wild 2D Human Videos for Zero-Shot Robotic Manipulation](https://arxiv.org/abs/2503.07135) | 3D representation | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2503.07135) / [project](https://hanzhic.github.io/vidbot-project/) | EAI-VLA-VLN | 3D grounding | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | [AutoURDF: Unsupervised Robot Modeling from Point Cloud Frames Using Cluster Registration](https://arxiv.org/abs/2412.05507) | 3D grounding | 机械臂/机器人操作 | 增强空间理解和操作定位 | [paper](https://arxiv.org/abs/2412.05507) / [project](https://github.com/jl6017/AutoURDF) | - | 3D grounding | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |

#### online/RL fine-tuning

共 12 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 来源 | 训练/动作属性 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ICLR 2026 | [Interleave-VLA: Enhancing Robot Manipulation with Image-Text Interleaved Instructions](https://openreview.net/forum?id=ULTWUuGhC3) | VLA / RL | 机械臂/机器人操作 | 通过在线优化提升策略 | [paper](https://openreview.net/forum?id=ULTWUuGhC3) | EAI-VLA-VLN | RL/在线微调 | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [Self-Improving Vision-Language-Action Models with Data Generation via Residual RL](https://openreview.net/forum?id=eUGoqrZ6Ea) | VLA / RL | 机械臂/机器人操作 | 通过在线优化提升策略 | [paper](https://openreview.net/forum?id=eUGoqrZ6Ea) | Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, EAI-Safety, WAM, RL-VLA | RL/在线微调 | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting](https://openreview.net/forum?id=sFO9d6XSlf) | VLA / RL | 机械臂/机器人操作 | 通过在线优化提升策略 | [paper](https://openreview.net/forum?id=sFO9d6XSlf) | - | RL/在线微调 | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [Cross-Embodiment Offline Reinforcement Learning for Heterogeneous Robot Datasets](https://openreview.net/forum?id=GrsoLVNy3Y) | VLA / RL | 机械臂/机器人操作 | 通过在线优化提升策略 | [paper](https://openreview.net/forum?id=GrsoLVNy3Y) | HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Humanoid-RL, WAM | RL/在线微调 | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [Policy Likelihood-based Query Sampling and Critic-Exploited Reset for Efficient Preference-based Reinforcement Learning](https://openreview.net/forum?id=ITeuGb2bYg) | VLA / RL | 机械臂/机器人操作 | 通过在线优化提升策略 | [paper](https://openreview.net/forum?id=ITeuGb2bYg) | - | RL/在线微调 | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning](https://openreview.net/forum?id=TQhSodCM4r) | VLA / RL | 机械臂/机器人操作 | 通过在线优化提升策略 | [paper](https://openreview.net/forum?id=TQhSodCM4r) | EAI-VLA-VLN, Efficient-VLA, RL-VLA | RL/在线微调 | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [Robust Fine-tuning of Vision-Language-Action Robot Policies via Parameter Merging](https://openreview.net/forum?id=uWJwQ5SZoM) | VLA / RL | 机械臂/机器人操作 | 通过在线优化提升策略 | [paper](https://openreview.net/forum?id=uWJwQ5SZoM) | - | RL/在线微调 | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICLR 2026 | [World2Minecraft: Occupancy-Driven simulated scenes Construction](https://openreview.net/forum?id=dc90uPqxWF) | VLA / RL | 机械臂/机器人操作 | 通过在线优化提升策略 | [paper](https://openreview.net/forum?id=dc90uPqxWF) | - | RL/在线微调 | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| AAAI 2026 | [Steering Visuomotor Policy in Open Worlds via Cross-View Goal Alignment](https://ojs.aaai.org/index.php/AAAI/article/view/38876) | VLA / RL | 机械臂/机器人操作 | 通过在线优化提升策略 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38876) | - | RL/在线微调 | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2026 | HIER: Human-in-the-Loop Imagination-Execution Refinement for General Real-World Vision-Language-Action Models | VLA / RL | 机械臂/机器人操作 | 改进视觉语言到动作策略 |  | - | RL/在线微调 | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | Real-World Reinforcement Learning of Active Perception Behaviors | RL | 触觉/接触操作 | 通过在线优化提升策略 |  | HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Efficient-VLA, Robot-Learning, Humanoid-RL, EAI-Safety, WAM, RL-VLA | RL/在线微调 | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2025 | ReinboT: Amplifying Robot Visual-Language Manipulation with Reinforcement Learning | VLA / RL | 触觉/接触操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2505.07395) | RL-VLA | RL/在线微调 | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |

#### 安全鲁棒性

共 3 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 来源 | 训练/动作属性 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ICLR 2026 | [On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations](https://openreview.net/forum?id=cS6xizdYD5) | VLA / safety | 机械臂/机器人操作 | 评估鲁棒性和安全性 | [paper](https://openreview.net/forum?id=cS6xizdYD5) | - | 安全鲁棒 | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | [BadVLA: Towards Backdoor Attacks on Vision-Language-Action Models via Objective-Decoupled Optimization](https://arxiv.org/abs/2505.16640) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2505.16640) / [project](https://github.com/Zxy-MLlab/BadVLA) | EAI-Safety | 安全鲁棒 | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICCV 2025 | [Exploring the Adversarial Vulnerabilities of Vision-Language-Action Models in Robotics](https://arxiv.org/abs/2411.13587) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2411.13587) / [project](https://vlaattacker.github.io/) | EAI-Safety | 安全鲁棒 | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |

### WAM / 世界模型

WAM 将未来世界状态预测和动作生成合在一起，适合放在 agent 规划和低层控制之间。它的价值不是替代所有控制器，而是提供可想象、可验证、可恢复的中间层。

子方向：cascaded WAM、joint WAM、video/latent world model、world model for VLA、world model evaluation。

共 46 篇。

| 子方向 | 条目数 | 观察重点 |
| --- | ---: | --- |
| cascaded WAM | 23 | 看先想象后执行的分层链路。 |
| joint WAM | 3 | 看视觉、状态和动作的联合建模。 |
| video/latent world model | 13 | 看未来视频或隐状态预测质量。 |
| world model for VLA | 7 | 看世界模型如何服务 VLA 决策。 |

#### cascaded WAM

共 23 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 来源 | WAM 属性 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ICLR 2026 | [Ctrl-World: A Controllable Generative World Model for Robot Manipulation](https://openreview.net/forum?id=748bHL2BAv) | world model / RL | 机械臂/机器人操作 | 用世界预测支持机器人决策 | [paper](https://openreview.net/forum?id=748bHL2BAv) | WAM | cascaded WAM | 用于判断世界预测是否能服务规划和动作验证。 |
| ICLR 2026 | [Context and Diversity Matter: The Emergence of In-Context Learning in World Models](https://openreview.net/forum?id=0GNBqoYcAP) | world model / RL | 机械臂/机器人操作 | 用世界预测支持机器人决策 | [paper](https://openreview.net/forum?id=0GNBqoYcAP) | - | cascaded WAM | 用于判断世界预测是否能服务规划和动作验证。 |
| ICLR 2026 | [NeMo-map: Neural Implicit Flow Fields for Spatio-Temporal Motion Mapping](https://openreview.net/forum?id=4HZgkwVVFO) | world model / RL | 机械臂/机器人操作 | 用世界预测支持机器人决策 | [paper](https://openreview.net/forum?id=4HZgkwVVFO) | - | cascaded WAM | 用于判断世界预测是否能服务规划和动作验证。 |
| ICLR 2026 | [Astra: General Interactive World Model with Autoregressive Denoising](https://openreview.net/forum?id=8UZpmrxoLG) | world model / RL | 机械臂/机器人操作 | 用世界预测支持机器人决策 | [paper](https://openreview.net/forum?id=8UZpmrxoLG) | - | cascaded WAM | 用于判断世界预测是否能服务规划和动作验证。 |
| ICLR 2026 | [Test-Time Mixture of World Models for Embodied Agents in Dynamic Environments](https://openreview.net/forum?id=LQD1MrnbxH) | world model / RL | 机械臂/机器人操作 | 用世界预测支持机器人决策 | [paper](https://openreview.net/forum?id=LQD1MrnbxH) | HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Humanoid-RL, EAI-Safety, WAM, RL-VLA | cascaded WAM | 用于判断世界预测是否能服务规划和动作验证。 |
| ICLR 2026 | [Learning Massively Multitask World Models for Continuous Control](https://openreview.net/forum?id=MPabX9LEds) | world model / RL | 机械臂/机器人操作 | 用世界预测支持机器人决策 | [paper](https://openreview.net/forum?id=MPabX9LEds) | - | cascaded WAM | 用于判断世界预测是否能服务规划和动作验证。 |
| ICLR 2026 | [ExoPredicator: Learning Abstract Models of Dynamic Worlds for Robot Planning](https://openreview.net/forum?id=a1zfcaNTkM) | world model / RL | 机械臂/机器人操作 | 用世界预测支持机器人决策 | [paper](https://openreview.net/forum?id=a1zfcaNTkM) | - | cascaded WAM | 用于判断世界预测是否能服务规划和动作验证。 |
| ICLR 2026 | [Efficient Reinforcement Learning by Guiding World Models with Non-Curated Data](https://openreview.net/forum?id=oBXfPyi47m) | world model / RL | 机械臂/机器人操作 | 用世界预测支持机器人决策 | [paper](https://openreview.net/forum?id=oBXfPyi47m) | - | cascaded WAM | 用于判断世界预测是否能服务规划和动作验证。 |
| ICLR 2026 | [Object-Centric World Models from Few-Shot Annotations for Sample-Efficient Reinforcement Learning](https://openreview.net/forum?id=qmEyJadwHA) | world model / RL | 机械臂/机器人操作 | 用世界预测支持机器人决策 | [paper](https://openreview.net/forum?id=qmEyJadwHA) | HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Efficient-VLA, Robot-Learning, Humanoid-RL, EAI-Safety | cascaded WAM | 用于判断世界预测是否能服务规划和动作验证。 |
| ICLR 2026 | [Building spatial world models from sparse transitional episodic memories](https://openreview.net/forum?id=w3w7WVG4ks) | world model / RL | 机械臂/机器人操作 | 用世界预测支持机器人决策 | [paper](https://openreview.net/forum?id=w3w7WVG4ks) | - | cascaded WAM | 用于判断世界预测是否能服务规划和动作验证。 |
| ICLR 2026 | [WoW!: World Models in a Closed-Loop World](https://openreview.net/forum?id=yDmb7xAfeb) | world model / RL | 机械臂/机器人操作 | 用世界预测支持机器人决策 | [paper](https://openreview.net/forum?id=yDmb7xAfeb) | WAM | cascaded WAM | 用于判断世界预测是否能服务规划和动作验证。 |
| ICLR 2026 | [ENACT: Evaluating Embodied Cognition with World Modeling of Egocentric Interaction](https://openreview.net/forum?id=Patx6MRipw) | world model / RL | 机械臂/机器人操作 | 用世界预测支持机器人决策 | [paper](https://openreview.net/forum?id=Patx6MRipw) | - | cascaded WAM | 用于判断世界预测是否能服务规划和动作验证。 |
| ICML 2026 | [Cross-Embodiment Robot Foundation World Models with Latent Actions](https://icml.cc/virtual/2026/poster/63978) | world model / RL | 机械臂/机器人操作 | 用世界预测支持机器人决策 | [paper](https://icml.cc/virtual/2026/poster/63978) | HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Humanoid-RL, WAM | cascaded WAM | 用于判断世界预测是否能服务规划和动作验证。 |
| ICML 2026 | [DDP-WM: Disentangled Dynamics Prediction for Efficient World Models](https://icml.cc/virtual/2026/poster/62480) | world model / RL | 机械臂/机器人操作 | 用世界预测支持机器人决策 | [paper](https://icml.cc/virtual/2026/poster/62480) | - | cascaded WAM | 用于判断世界预测是否能服务规划和动作验证。 |
| ICML 2026 | [RoboFlow4D: A Lightweight Flow World Model Toward Real-Time Flow-Guided Robotic Manipulation](https://icml.cc/virtual/2026/poster/62543) | flow matching / world model / RL | 机械臂/机器人操作 | 用世界预测支持机器人决策 | [paper](https://icml.cc/virtual/2026/poster/62543) | - | cascaded WAM | 用于判断世界预测是否能服务规划和动作验证。 |
| ICML 2026 | [Learning Task-Sufficient World Models by Synergizing Agentic Exploration and Structured Modeling](https://icml.cc/virtual/2026/poster/64209) | world model / RL | 机械臂/机器人操作 | 用世界预测支持机器人决策 | [paper](https://icml.cc/virtual/2026/poster/64209) | - | cascaded WAM | 用于判断世界预测是否能服务规划和动作验证。 |
| NeurIPS 2025 | [SAMPO: Scale-wise Autoregression with Motion Prompt for Generative World Models](https://arxiv.org/abs/2509.15536) | world model / RL | 机械臂/机器人操作 | 用世界预测支持机器人决策 | [paper](https://arxiv.org/abs/2509.15536) | - | cascaded WAM | 用于判断世界预测是否能服务规划和动作验证。 |
| NeurIPS 2025 | [Learning 3D Persistent Embodied World Models](https://arxiv.org/abs/2505.05495) | world model / 3D representation / RL | 机械臂/机器人操作 | 用世界预测支持机器人决策 | [paper](https://arxiv.org/abs/2505.05495) | - | cascaded WAM | 用于判断世界预测是否能服务规划和动作验证。 |
| NeurIPS 2025 | [OSVI-WM: One-Shot Visual Imitation for Unseen Tasks using World-Model-Guided Trajectory Generation](https://arxiv.org/abs/2505.20425) | world model / RL | 机械臂/机器人操作 | 先预测未来再推导动作 | [paper](https://arxiv.org/abs/2505.20425) | - | cascaded WAM | 用于判断世界预测是否能服务规划和动作验证。 |
| ICCV 2025 | [IRASim: A Fine-Grained World Model for Robot Manipulation](https://arxiv.org/abs/2406.14540) | world model / RL | 机械臂/机器人操作 | 用世界预测支持机器人决策 | [paper](https://arxiv.org/abs/2406.14540) / [project](https://gen-irasim.github.io/) | - | cascaded WAM | 用于判断世界预测是否能服务规划和动作验证。 |
| ICCV 2025 | [GWM: Towards Scalable Gaussian World Models for Robotic Manipulation](https://ziweiwangthu.github.io/data/GWM.pdf) | world model / 3D Gaussian / RL | 仿真/评测环境 | 用世界预测支持机器人决策 | [paper](https://ziweiwangthu.github.io/data/GWM.pdf) / [project](https://gaussian-world-model.github.io/) | - | cascaded WAM | 用于判断世界预测是否能服务规划和动作验证。 |
| ICCV 2025 | [DyWA: Dynamics-adaptive World Action Model for Generalizable Non-prehensile Manipulation](https://arxiv.org/abs/2503.16806) | world model / RL | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2503.16806) / [project](https://pku-epic.github.io/DyWA/) | EAI-VLA-VLN | cascaded WAM | 用于判断世界预测是否能服务规划和动作验证。 |
| ICCV 2025 | [Learning 4D Embodied World Models](https://openreview.net/pdf?id=mnwlhvmKMN) | world model / RL | 机械臂/机器人操作 | 用世界预测支持机器人决策 | [paper](https://openreview.net/pdf?id=mnwlhvmKMN) | WAM | cascaded WAM | 用于判断世界预测是否能服务规划和动作验证。 |

#### joint WAM

共 3 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 来源 | WAM 属性 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ICLR 2026 | [Empowering Multi-Robot Cooperation via Sequential World Models](https://openreview.net/forum?id=IvUM6UwYCJ) | world model / RL | 机械臂/机器人操作 | 用世界预测支持机器人决策 | [paper](https://openreview.net/forum?id=IvUM6UwYCJ) | - | joint WAM | 用于判断世界预测是否能服务规划和动作验证。 |
| ICML 2026 | [Dual-Stream Diffusion for World-Model Augmented Vision-Language-Action Model](https://icml.cc/virtual/2026/poster/64447) | VLA / diffusion policy / world model | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://icml.cc/virtual/2026/poster/64447) | EAI-VLA-VLN, WAM | joint WAM | 用于判断世界预测是否能服务规划和动作验证。 |
| ICCV 2025 | [Diffusion-Based Imaginative Coordination for Bimanual Manipulation](https://arxiv.org/abs/2507.11296) | diffusion policy / world model / RL | 双臂机器人 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2507.11296) | Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Efficient-VLA, EAI-Safety, WAM | joint WAM | 用于判断世界预测是否能服务规划和动作验证。 |

#### video/latent world model

共 13 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 来源 | WAM 属性 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ICLR 2026 | [FantasyWorld: Geometry-Consistent World Modeling via Unified Video and 3D Prediction](https://openreview.net/forum?id=3q9vHEqsNx) | video/latent world model | 机械臂/机器人操作 | 从视频或隐空间预测未来 | [paper](https://openreview.net/forum?id=3q9vHEqsNx) | - | video/latent world model | 用于判断世界预测是否能服务规划和动作验证。 |
| ICLR 2026 | [Unified 3D Scene Understanding Through Physical World Modeling](https://openreview.net/forum?id=NQq9JLMfNN) | video/latent world model | 机械臂/机器人操作 | 从视频或隐空间预测未来 | [paper](https://openreview.net/forum?id=NQq9JLMfNN) | - | video/latent world model | 用于判断世界预测是否能服务规划和动作验证。 |
| ICLR 2026 | [Vid2World: Crafting Video Diffusion Models to Interactive World Models](https://openreview.net/forum?id=pFyzqbUiF9) | video/latent world model | 机械臂/机器人操作 | 从视频或隐空间预测未来 | [paper](https://openreview.net/forum?id=pFyzqbUiF9) | - | video/latent world model | 用于判断世界预测是否能服务规划和动作验证。 |
| ICLR 2026 | [EgoWorld: Translating Exocentric View to Egocentric View using Rich Exocentric Observations](https://openreview.net/forum?id=wcTuZG9P2o) | video/latent world model | 机械臂/机器人操作 | 从视频或隐空间预测未来 | [paper](https://openreview.net/forum?id=wcTuZG9P2o) | - | video/latent world model | 用于判断世界预测是否能服务规划和动作验证。 |
| AAAI 2026 | [LiDARCrafter: Dynamic 4D World Modeling from LiDAR Sequences](https://ojs.aaai.org/index.php/AAAI/article/view/38905) | video/latent world model | 机械臂/机器人操作 | 从视频或隐空间预测未来 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38905) | - | video/latent world model | 用于判断世界预测是否能服务规划和动作验证。 |
| ICML 2026 | [DreamDojo: A Real-Time Robot World Model from Large-Scale Human Videos](https://icml.cc/virtual/2026/poster/65193) | world model / RL | 机械臂/机器人操作 | 用世界预测支持机器人决策 | [paper](https://icml.cc/virtual/2026/poster/65193) | Humanoid-RL, WAM | video/latent world model | 用于判断世界预测是否能服务规划和动作验证。 |
| ICML 2026 | [From Imagined Futures to Executable Actions: Mixture of Latent Actions for Robot Manipulation](https://icml.cc/virtual/2026/poster/66091) | world model / RL | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://icml.cc/virtual/2026/poster/66091) | - | video/latent world model | 用于判断世界预测是否能服务规划和动作验证。 |
| NeurIPS 2025 | VideoVLA: Video Generators Can Be Generalizable Robot Manipulators | VLA | 机械臂/机器人操作 | 从视频或隐空间预测未来 |  | EAI-VLA-VLN, WAM | video/latent world model | 用于判断世界预测是否能服务规划和动作验证。 |
| NeurIPS 2025 | [EnerVerse: Envisioning Embodied Future Space for Robotics Manipulation](https://arxiv.org/abs/2501.01895) | VLA | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2501.01895) | EAI-VLA-VLN | video/latent world model | 用于判断世界预测是否能服务规划和动作验证。 |
| NeurIPS 2025 | [DreamVLA: A Vision-Language-Action Model Dreamed with Comprehensive World Knowledge](https://arxiv.org/abs/2507.04447) | VLA / RL | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2507.04447) / [project](https://zhangwenyao1.github.io/DreamVLA/index.html) | Awesome-VLA | video/latent world model | 用于判断世界预测是否能服务规划和动作验证。 |
| ICML 2025 | Video Prediction Policy: A Generalist Robot Policy with Predictive Visual Representations | video/latent world model | 机械臂/机器人操作 | 从视频或隐空间预测未来 | [paper](https://arxiv.org/abs/2412.14803) / [project](https://video-prediction-policy.github.io/) | EAI-VLA-VLN, WAM | video/latent world model | 用于判断世界预测是否能服务规划和动作验证。 |
| CVPR 2025 | [TASTE-Rob: Advancing Video Generation of Task-Oriented Hand-Object Interaction for Generalizable Robotic Manipulation](https://arxiv.org/abs/2503.11423) | video/latent world model | 灵巧手/抓取 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2503.11423) | - | video/latent world model | 用于判断世界预测是否能服务规划和动作验证。 |
| CVPR 2025 | [GraphMimic: Graph-to-Graphs Generative Modeling from Videos for Policy Learning](https://cvpr.thecvf.com/virtual/2025/poster/34942) | video/latent world model | 机械臂/机器人操作 | 从视频或隐空间预测未来 | [paper](https://cvpr.thecvf.com/virtual/2025/poster/34942) | - | video/latent world model | 用于判断世界预测是否能服务规划和动作验证。 |

#### world model for VLA

共 7 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 来源 | WAM 属性 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ICLR 2026 | [Genie Envisioner: A Unified World Foundation Platform for Robotic Manipulation](https://openreview.net/forum?id=fHLtSxDFKC) | VLA / world model / RL | 机械臂/机器人操作 | 用世界预测支持机器人决策 | [paper](https://openreview.net/forum?id=fHLtSxDFKC) | EAI-VLA-VLN | world model for VLA | 用于判断世界预测是否能服务规划和动作验证。 |
| ICLR 2026 | [RIG: Synergizing Reasoning and Imagination in End-to-End Generalist Policy](https://openreview.net/forum?id=LQv9LU2Ufg) | VLA / world model / RL | 机械臂/机器人操作 | 用世界预测支持机器人决策 | [paper](https://openreview.net/forum?id=LQv9LU2Ufg) | - | world model for VLA | 用于判断世界预测是否能服务规划和动作验证。 |
| ICLR 2026 | [WMPO: World Model-based Policy Optimization for Vision-Language-Action Models](https://openreview.net/forum?id=qE2FyvRvuF) | VLA / world model / RL | 机械臂/机器人操作 | 用世界预测支持机器人决策 | [paper](https://openreview.net/forum?id=qE2FyvRvuF) | WAM, RL-VLA | world model for VLA | 用于判断世界预测是否能服务规划和动作验证。 |
| ICLR 2026 | [Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning](https://openreview.net/forum?id=wPEIStHxYH) | VLA / world model / RL | 机械臂/机器人操作 | 用世界预测支持机器人决策 | [paper](https://openreview.net/forum?id=wPEIStHxYH) | EAI-VLA-VLN, WAM | video/latent world model | 用于判断世界预测是否能服务规划和动作验证。 |
| AAAI 2026 | [WorldAgen: Unified State-Action Prediction with Test-Time World Model Training](https://ojs.aaai.org/index.php/AAAI/article/view/38925) | VLA / world model / RL | 机械臂/机器人操作 | 用世界预测支持机器人决策 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38925) | - | world model for VLA | 用于判断世界预测是否能服务规划和动作验证。 |
| ICML 2026 | [VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model](https://icml.cc/virtual/2026/poster/66169) | VLA / world model / RL | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://icml.cc/virtual/2026/poster/66169) | - | world model for VLA | 用于判断世界预测是否能服务规划和动作验证。 |
| CVPR 2026 | [CoWVLA: Chain of World: World Model Thinking in Latent Motion](https://arxiv.org/abs/2603.03195) | VLA / world model / RL | 机械臂/机器人操作 | 用世界预测支持机器人决策 | [paper](https://arxiv.org/abs/2603.03195) / [project](https://fx-hit.github.io/cowvla-io/) | - | video/latent world model | 用于判断世界预测是否能服务规划和动作验证。 |

### Agentic Planning / 推理规划

这一方向强调任务分解、记忆、失败监控、约束/affordance planning 和自改进规划。它最贴近“agent 规划，小模型或传统方法执行”的系统路线。

子方向：任务分解、memory、failure monitor、constraint / affordance planning、self-improving planning。

共 89 篇。

| 子方向 | 条目数 | 观察重点 |
| --- | ---: | --- |
| 任务分解 | 30 | 看高层指令如何拆成可执行步骤。 |
| memory | 10 | 看长期记忆、经验复用和环境状态保持。 |
| failure monitor | 8 | 看失败检测、恢复和闭环修正。 |
| constraint / affordance planning | 9 | 看约束、可供性和物理可执行性。 |
| self-improving planning | 32 | 看自我改进、测试时优化和经验沉淀。 |

#### 任务分解

共 30 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 来源 | 规划属性 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ICLR 2026 | [Vlaser: Vision-Language-Action Model with Synergistic Embodied Reasoning](https://openreview.net/forum?id=8xTDnj39Ti) | planning / reasoning | 机械臂/机器人操作 | 把高层目标转为可执行步骤 | [paper](https://openreview.net/forum?id=8xTDnj39Ti) | - | 任务分解 | 用于评估高层规划是否能落到可执行动作。 |
| ICLR 2026 | [OneTwoVLA: A Unified Vision-Language-Action Model with Adaptive Reasoning](https://openreview.net/forum?id=tWMfhoP3as) | planning / reasoning | 机械臂/机器人操作 | 把高层目标转为可执行步骤 | [paper](https://openreview.net/forum?id=tWMfhoP3as) | EAI-VLA-VLN | 任务分解 | 用于评估高层规划是否能落到可执行动作。 |
| ICLR 2026 | [From Seeing to Doing: Bridging Reasoning and Decision for Robotic Manipulation](https://openreview.net/forum?id=yngvAamNQi) | planning / reasoning | 机械臂/机器人操作 | 把高层目标转为可执行步骤 | [paper](https://openreview.net/forum?id=yngvAamNQi) | EAI-VLA-VLN | 任务分解 | 用于评估高层规划是否能落到可执行动作。 |
| ICLR 2026 | [VLMgineer: Vision-Language Models as Robotic Toolsmiths](https://openreview.net/forum?id=nESyz4PvJL) | planning / reasoning | 机械臂/机器人操作 | 把高层目标转为可执行步骤 | [paper](https://openreview.net/forum?id=nESyz4PvJL) | - | 任务分解 | 用于评估高层规划是否能落到可执行动作。 |
| ICLR 2026 | [MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Models for Embodied Task Planning](https://openreview.net/forum?id=3eTr9dGwJv) | planning / reasoning | 机械臂/机器人操作 | 把高层目标转为可执行步骤 | [paper](https://openreview.net/forum?id=3eTr9dGwJv) | - | 任务分解 | 用于评估高层规划是否能落到可执行动作。 |
| ICLR 2026 | [Theory of Space: Can Foundation Models Construct Spatial Beliefs through Active Exploration?](https://openreview.net/forum?id=8iPwqr6Adk) | planning / reasoning | 机械臂/机器人操作 | 把高层目标转为可执行步骤 | [paper](https://openreview.net/forum?id=8iPwqr6Adk) | - | 任务分解 | 用于评估高层规划是否能落到可执行动作。 |
| ICLR 2026 | [Compositional Visual Planning via Inference-Time Diffusion Scaling](https://openreview.net/forum?id=EEONns7ae4) | planning / reasoning | 机械臂/机器人操作 | 把高层目标转为可执行步骤 | [paper](https://openreview.net/forum?id=EEONns7ae4) | - | 任务分解 | 用于评估高层规划是否能落到可执行动作。 |
| ICLR 2026 | [One Demo Is All It Takes: Planning Domain Derivation with LLMs from A Single Demonstration](https://openreview.net/forum?id=Y1VgLHbzCC) | planning / reasoning | 机械臂/机器人操作 | 把高层目标转为可执行步骤 | [paper](https://openreview.net/forum?id=Y1VgLHbzCC) | - | 任务分解 | 用于评估高层规划是否能落到可执行动作。 |
| ICLR 2026 | [OmniEVA: Embodied Versatile Planner via Task-Adaptive 3D-Grounded and Embodiment-aware Reasoning](https://openreview.net/forum?id=tkEmIJv1tB) | planning / reasoning | 机械臂/机器人操作 | 把高层目标转为可执行步骤 | [paper](https://openreview.net/forum?id=tkEmIJv1tB) | - | 任务分解 | 用于评估高层规划是否能落到可执行动作。 |
| ICLR 2026 | [ManipEvalAgent: Promptable and Efficient Evaluation Framework for Robotic Manipulation Policies](https://openreview.net/forum?id=3u6AkbWEls) | planning / reasoning | 机械臂/机器人操作 | 把高层目标转为可执行步骤 | [paper](https://openreview.net/forum?id=3u6AkbWEls) | - | 任务分解 | 用于评估高层规划是否能落到可执行动作。 |
| ICLR 2026 | [Difference-Aware Retrieval Polices for Imitation Learning](https://openreview.net/forum?id=9AA27en4go) | planning / reasoning | 机械臂/机器人操作 | 把高层目标转为可执行步骤 | [paper](https://openreview.net/forum?id=9AA27en4go) | - | 任务分解 | 用于评估高层规划是否能落到可执行动作。 |
| ICLR 2026 | [EquAct: An SE(3)-Equivariant Multi-Task Transformer for 3D Robotic Manipulation](https://openreview.net/forum?id=d1wuA8oIH0) | planning / reasoning | 机械臂/机器人操作 | 把高层目标转为可执行步骤 | [paper](https://openreview.net/forum?id=d1wuA8oIH0) | EAI-VLA-VLN | 任务分解 | 用于评估高层规划是否能落到可执行动作。 |
| ICLR 2026 | [Seeing Across Views: Benchmarking Spatial Reasoning of Vision-Language Models in Robotic Scenes](https://openreview.net/forum?id=jXDZJAfRZB) | planning / reasoning | 机械臂/机器人操作 | 把高层目标转为可执行步骤 | [paper](https://openreview.net/forum?id=jXDZJAfRZB) | - | 任务分解 | 用于评估高层规划是否能落到可执行动作。 |
| ICLR 2026 | [REI-Bench: Can Embodied Agents Understand Vague Human Instructions in Task Planning?](https://openreview.net/forum?id=vmBIF25KLf) | planning / reasoning | 机械臂/机器人操作 | 把高层目标转为可执行步骤 | [paper](https://openreview.net/forum?id=vmBIF25KLf) | - | 任务分解 | 用于评估高层规划是否能落到可执行动作。 |
| ICLR 2026 | [PhyScensis: Physics-Augmented LLM Agents for Complex Physical Scene Arrangement](https://openreview.net/forum?id=aCVfhY4Qen) | planning / reasoning | 机械臂/机器人操作 | 把高层目标转为可执行步骤 | [paper](https://openreview.net/forum?id=aCVfhY4Qen) | - | 任务分解 | 用于评估高层规划是否能落到可执行动作。 |
| ICLR 2026 | [OmniActor: A Generalist GUI and Embodied Agent for 2D&3D Worlds](https://openreview.net/forum?id=oJAIjUDxkZ) | planning / reasoning | 机械臂/机器人操作 | 把高层目标转为可执行步骤 | [paper](https://openreview.net/forum?id=oJAIjUDxkZ) | - | 任务分解 | 用于评估高层规划是否能落到可执行动作。 |
| AAAI 2026 | [GraphCoT-VLA: A 3D Spatial-Aware Reasoning Vision-Language-Action Model for Robotic Manipulation with Ambiguous Instructions](https://ojs.aaai.org/index.php/AAAI/article/view/38896) | planning / reasoning | 机械臂/机器人操作 | 把高层目标转为可执行步骤 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38896) | - | 任务分解 | 用于评估高层规划是否能落到可执行动作。 |
| AAAI 2026 | [PhyPlan: Learning to Plan Tasks with Generalizable and Rapid Physical Reasoning for Embodied Manipulation](https://ojs.aaai.org/index.php/AAAI/article/view/38900) | planning / reasoning | 机械臂/机器人操作 | 把高层目标转为可执行步骤 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38900) | - | 任务分解 | 用于评估高层规划是否能落到可执行动作。 |
| AAAI 2026 | [Cook and Clean Together: Teaching Embodied Agents for Parallel Task Execution](https://ojs.aaai.org/index.php/AAAI/article/view/38906) | planning / reasoning | 机械臂/机器人操作 | 把高层目标转为可执行步骤 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38906) | - | 任务分解 | 用于评估高层规划是否能落到可执行动作。 |
| AAAI 2026 | [FoAM: Foresight-Augmented Multi-Task Imitation Policy for Robotic Manipulation](https://ojs.aaai.org/index.php/AAAI/article/view/38911) | planning / reasoning | 机械臂/机器人操作 | 把高层目标转为可执行步骤 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38911) | - | 任务分解 | 用于评估高层规划是否能落到可执行动作。 |
| AAAI 2026 | [Zero-Shot Robotic Manipulation via 3D Gaussian Splatting-Enhanced Multimodal Retrieval-Augmented Generation](https://ojs.aaai.org/index.php/AAAI/article/view/38936) | planning / reasoning | 机械臂/机器人操作 | 把高层目标转为可执行步骤 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38936) | HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Humanoid-RL, EAI-Safety, WAM | 任务分解 | 用于评估高层规划是否能落到可执行动作。 |
| AAAI 2026 | [H-GAR: A Hierarchical Interaction Framework via Goal-Driven Observation-Action Refinement for Robotic Manipulation](https://ojs.aaai.org/index.php/AAAI/article/view/38958) | planning / reasoning | 机械臂/机器人操作 | 把高层目标转为可执行步骤 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38958) | - | 任务分解 | 用于评估高层规划是否能落到可执行动作。 |
| ICML 2026 | [TapSampling: Inference-Time Sampling with a Task-Progress-Understanding Verifier for Robotic Manipulation](https://icml.cc/virtual/2026/poster/60500) | planning / reasoning | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://icml.cc/virtual/2026/poster/60500) | - | 任务分解 | 用于评估高层规划是否能落到可执行动作。 |
| ICML 2026 | [Decompose and Recompose: Reasoning New Skills from Existing Abilities for Cross-Task Robotic Manipulation](https://icml.cc/virtual/2026/poster/63250) | planning / reasoning | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://icml.cc/virtual/2026/poster/63250) | - | 任务分解 | 用于评估高层规划是否能落到可执行动作。 |
| NeurIPS 2025 | [SAFE: Multitask Failure Detection for Vision-Language-Action Models](https://arxiv.org/abs/2506.09937) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2506.09937) / [project](https://vla-safe.github.io/) | Awesome-EAI, EAI-VLA-VLN, Humanoid-RL, EAI-Safety | 失败监控 | 用于评估高层规划是否能落到可执行动作。 |
| NeurIPS 2025 | [Towards Reliable Code-as-Policies: A Neuro-Symbolic Framework for Embodied Task Planning](https://arxiv.org/abs/2510.21302) | planning / reasoning | 机械臂/机器人操作 | 把高层目标转为可执行步骤 | [paper](https://arxiv.org/abs/2510.21302) | - | 任务分解 | 用于评估高层规划是否能落到可执行动作。 |
| NeurIPS 2025 | [RDD: Retrieval-Based Demonstration Decomposer for Planner Alignment in Long-Horizon Tasks](https://arxiv.org/abs/2510.14968) | agent planner / planning / reasoning | 机械臂/机器人操作 | 把高层目标转为可执行步骤 | [paper](https://arxiv.org/abs/2510.14968) / [project](https://rdd-neurips.github.io/) | - | 任务分解 | 用于评估高层规划是否能落到可执行动作。 |
| NeurIPS 2025 | [UniDomain: Pretraining a Unified PDDL Domain from Real-World Demonstrations for Generalizable Robot Task Planning](https://arxiv.org/abs/2507.21545) | planning / reasoning / RL | 机械臂/机器人操作 | 把高层目标转为可执行步骤 | [paper](https://arxiv.org/abs/2507.21545) | - | 任务分解 | 用于评估高层规划是否能落到可执行动作。 |
| NeurIPS 2025 | [World-aware Planning Narratives Enhance Large Vision-Language Model Planner](https://arxiv.org/abs/2506.21230) | agent planner / planning / RL | 机械臂/机器人操作 | 把高层目标转为可执行步骤 | [paper](https://arxiv.org/abs/2506.21230) | - | 任务分解 | 用于评估高层规划是否能落到可执行动作。 |
| ICCV 2025 | [VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics Manipulation with Long-Horizon Reasoning Tasks](https://arxiv.org/abs/2412.18194) | VLA / reasoning | 仿真/评测环境 | 提供评测任务和数据基准 | [paper](https://arxiv.org/abs/2412.18194) / [project](https://iranqin.github.io/robofactory/) | HCP-Survey, Awesome-EAI, EAI-VLA-VLN, WAM | 任务分解 | 用于评估高层规划是否能落到可执行动作。 |

#### memory

共 10 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 来源 | 规划属性 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ICLR 2026 | [Scaling up Memory for Robotic Control via Experience Retrieval](https://openreview.net/forum?id=1dH4ARGdwD) | memory | 机械臂/机器人操作 | 增强长期任务记忆 | [paper](https://openreview.net/forum?id=1dH4ARGdwD) | - | 记忆规划 | 用于评估高层规划是否能落到可执行动作。 |
| ICLR 2026 | [Planning with an Embodied Learnable Memory](https://openreview.net/forum?id=79BOATBal9) | memory | 机械臂/机器人操作 | 增强长期任务记忆 | [paper](https://openreview.net/forum?id=79BOATBal9) | - | 记忆规划 | 用于评估高层规划是否能落到可执行动作。 |
| ICLR 2026 | [Memory, Benchmark & Robots: A Benchmark for Solving Complex Tasks with Reinforcement Learning](https://openreview.net/forum?id=9cLPurIZMj) | memory | 机械臂/机器人操作 | 增强长期任务记忆 | [paper](https://openreview.net/forum?id=9cLPurIZMj) | - | 记忆规划 | 用于评估高层规划是否能落到可执行动作。 |
| ICLR 2026 | [Embodied Agents Meet Personalization: Investigating Challenges and Solutions Through the Lens of Memory Utilization](https://openreview.net/forum?id=E5L43l5EIu) | memory | 机械臂/机器人操作 | 增强长期任务记忆 | [paper](https://openreview.net/forum?id=E5L43l5EIu) | EAI-Safety | 记忆规划 | 用于评估高层规划是否能落到可执行动作。 |
| ICML 2026 | [HiMe: Hierarchical Embodied Memory for Long-Horizon Vision-Language-Action Control](https://icml.cc/virtual/2026/poster/60897) | VLA / memory | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://icml.cc/virtual/2026/poster/60897) | - | 记忆规划 | 用于评估高层规划是否能落到可执行动作。 |
| ICML 2026 | [Spatial Memory for Out-of-Vision Manipulation in Vision-Language-Action](https://icml.cc/virtual/2026/poster/66214) | VLA / memory | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://icml.cc/virtual/2026/poster/66214) | - | 记忆规划 | 用于评估高层规划是否能落到可执行动作。 |
| CVPR 2026 | [OptimusVLA: Global Prior Meets Local Consistency: Dual-Memory Augmented Vision-Language-Action Model for Efficient Robotic Manipulation](https://arxiv.org/abs/2602.20200) | VLA / memory | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2602.20200) / [code](https://github.com/JiuTian-VL/OptimusVLA) | Efficient-VLA | 记忆规划 | 用于评估高层规划是否能落到可执行动作。 |
| ICCV 2025 | [Embodied VideoAgent: Persistent Memory from Egocentric Videos and Embodied Sensors Enables Dynamic Scene Understanding](https://arxiv.org/abs/2501.00358) | VLA / memory | 机械臂/机器人操作 | 增强长期任务记忆 | [paper](https://arxiv.org/abs/2501.00358) / [project](https://embodied-videoagent.github.io/) | - | 记忆规划 | 用于评估高层规划是否能落到可执行动作。 |
| ICCV 2025 | [Towards Long-Horizon Vision-Language-Action System: Reasoning, Acting and Memory](https://iccv.thecvf.com/virtual/2025/poster/1915) | VLA / memory / reasoning | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://iccv.thecvf.com/virtual/2025/poster/1915) | - | 记忆规划 | 用于评估高层规划是否能落到可执行动作。 |
| ICML 2025 | SAM2Act:Integrating Visual Foundation Model with A Memory Architecture for Robotic Manipulation | memory | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2501.18564) | EAI-VLA-VLN | 记忆规划 | 用于评估高层规划是否能落到可执行动作。 |

#### failure monitor

共 8 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 来源 | 规划属性 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ICLR 2026 | [Experience-based Knowledge Correction for Robust Planning in Minecraft](https://openreview.net/forum?id=N22lDHYrXe) | failure monitor | 机械臂/机器人操作 | 检测或恢复执行失败 | [paper](https://openreview.net/forum?id=N22lDHYrXe) | - | 失败监控 | 用于评估高层规划是否能落到可执行动作。 |
| ICLR 2026 | [ReCAPA: Hierarchical Predictive Correction to Mitigate Cascading Failures](https://openreview.net/forum?id=WC6MJ5r5Bj) | failure monitor | 机械臂/机器人操作 | 检测或恢复执行失败 | [paper](https://openreview.net/forum?id=WC6MJ5r5Bj) | - | 失败监控 | 用于评估高层规划是否能落到可执行动作。 |
| ICLR 2026 | [Self-Refining Vision Language Model for Robotic Failure Detection and Reasoning](https://openreview.net/forum?id=jr9hGWQioP) | failure monitor | 机械臂/机器人操作 | 检测或恢复执行失败 | [paper](https://openreview.net/forum?id=jr9hGWQioP) | EAI-VLA-VLN | 失败监控 | 用于评估高层规划是否能落到可执行动作。 |
| ICML 2026 | [Sentinel-VLA: A Metacognitive VLA Model with Active Status Monitoring for Dynamic Reasoning and Error Recovery](https://icml.cc/virtual/2026/poster/61750) | VLA / reasoning | 机械臂/机器人操作 | 发现并修复执行失败 | [paper](https://icml.cc/virtual/2026/poster/61750) | - | 失败监控 | 用于评估高层规划是否能落到可执行动作。 |
| ICML 2026 | [NeurVLA: Unleashing Failure-Handling Capability of Vision-Language-Action Models via Neural-Symbolic Reasoning](https://icml.cc/virtual/2026/poster/63650) | VLA / reasoning | 灵巧手/抓取 | 改进视觉语言到动作策略 | [paper](https://icml.cc/virtual/2026/poster/63650) | - | 失败监控 | 用于评估高层规划是否能落到可执行动作。 |
| ICML 2026 | [Can VLMs Diagnose and Recover from VLA Manipulation Faults?](https://icml.cc/virtual/2026/poster/64203) | VLA / planning / reasoning | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://icml.cc/virtual/2026/poster/64203) | - | 失败监控 | 用于评估高层规划是否能落到可执行动作。 |
| NeurIPS 2025 | [Failure Prediction at Runtime for Generative Robot Policies](https://arxiv.org/abs/2510.09459) | failure monitor | 机械臂/机器人操作 | 检测或恢复执行失败 | [paper](https://arxiv.org/abs/2510.09459) | - | 失败监控 | 用于评估高层规划是否能落到可执行动作。 |
| CVPR 2025 | [Code-as-Monitor: Constraint-aware Visual Programming for Reactive and Proactive Robotic Failure Detection](https://arxiv.org/abs/2412.04455) | planning / reasoning | 机械臂/机器人操作 | 检测或恢复执行失败 | [paper](https://arxiv.org/abs/2412.04455) / [project](https://zhoues.github.io/Code-as-Monitor/) | HCP-Survey, Awesome-EAI | 失败监控 | 用于评估高层规划是否能落到可执行动作。 |

#### constraint / affordance planning

共 9 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 来源 | 规划属性 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ICLR 2026 | [Towards Improvisational TAMP: Learning Low-Level Shortcuts in Abstract Planning Graphs](https://openreview.net/forum?id=enprG5H9aD) | planning / affordance | 机械臂/机器人操作 | 约束动作可执行性 | [paper](https://openreview.net/forum?id=enprG5H9aD) | - | 约束/affordance | 用于评估高层规划是否能落到可执行动作。 |
| ICLR 2026 | [Natural Language PDDL (NL-PDDL) for Open-world Goal-oriented Commonsense Regression Planning in Embodied AI](https://openreview.net/forum?id=kWCNhRdcDI) | planning / affordance | 机械臂/机器人操作 | 约束动作可执行性 | [paper](https://openreview.net/forum?id=kWCNhRdcDI) | - | 约束/affordance | 用于评估高层规划是否能落到可执行动作。 |
| ICLR 2026 | [SafeFlowMatcher: Safe and Fast Planning using Flow Matching with Control Barrier Functions](https://openreview.net/forum?id=refcXHU1Nh) | planning / affordance | 机械臂/机器人操作 | 约束动作可执行性 | [paper](https://openreview.net/forum?id=refcXHU1Nh) | - | 约束/affordance | 用于评估高层规划是否能落到可执行动作。 |
| ICLR 2026 | [MoMaGen: Generating Demonstrations under Soft and Hard Constraints for Multi-Step Bimanual Mobile Manipulation](https://openreview.net/forum?id=bGPDviEtZ1) | planning / affordance | 机械臂/机器人操作 | 约束动作可执行性 | [paper](https://openreview.net/forum?id=bGPDviEtZ1) | - | 约束/affordance | 用于评估高层规划是否能落到可执行动作。 |
| AAAI 2026 | [A3D: Adaptive Affordance Assembly with Dual-Arm Manipulation](https://ojs.aaai.org/index.php/AAAI/article/view/38907) | planning / affordance | 机械臂/机器人操作 | 约束动作可执行性 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38907) | - | 约束/affordance | 用于评估高层规划是否能落到可执行动作。 |
| AAAI 2026 | [Affordance-Guided Coarse-to-Fine Exploration for Base Placement in Open-Vocabulary Mobile Manipulation](https://ojs.aaai.org/index.php/AAAI/article/view/38909) | planning / affordance | 机械臂/机器人操作 | 约束动作可执行性 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38909) | EAI-VLA-VLN | 约束/affordance | 用于评估高层规划是否能落到可执行动作。 |
| AAAI 2026 | [Gentle Manipulation Policy Learning via Demonstrations from VLM Planned Atomic Skills](https://ojs.aaai.org/index.php/AAAI/article/view/38955) | planning / affordance | 机械臂/机器人操作 | 约束动作可执行性 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38955) | - | 约束/affordance | 用于评估高层规划是否能落到可执行动作。 |
| NeurIPS 2025 | InstructFlow: Adaptive Symbolic Constraint-Guided Code Generation for Long-Horizon Planning | flow matching / planning / reasoning | 机械臂/机器人操作 | 约束动作可执行性 |  | - | 约束/affordance | 用于评估高层规划是否能落到可执行动作。 |
| ICCV 2025 | [CoA-VLA: Improving Vision-Language-Action Models via Visual-Text Chain-of-Affordance](https://iccv.thecvf.com/virtual/2025/poster/542) | VLA / affordance | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://iccv.thecvf.com/virtual/2025/poster/542) | - | 约束/affordance | 用于评估高层规划是否能落到可执行动作。 |

#### self-improving planning

共 32 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 来源 | 规划属性 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ICLR 2026 | [Self-Improving Loops for Visual Robotic Planning](https://openreview.net/forum?id=SzUgx5r3wy) | planning / reasoning / RL | 机械臂/机器人操作 | 通过反馈自我改进规划 | [paper](https://openreview.net/forum?id=SzUgx5r3wy) | Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, EAI-Safety, WAM, RL-VLA | 自改进规划 | 用于评估高层规划是否能落到可执行动作。 |
| ICLR 2026 | [BOLT: Decision‑Aligned Distillation and Budget-Aware Routing for Constrained Multimodal QA on Robots](https://openreview.net/forum?id=Vsy3nAnaX6) | planning / reasoning / RL | 机械臂/机器人操作 | 通过反馈自我改进规划 | [paper](https://openreview.net/forum?id=Vsy3nAnaX6) | - | 自改进规划 | 用于评估高层规划是否能落到可执行动作。 |
| ICLR 2026 | [EVLP: Learning Unified Embodied Vision-Language Planner with Reinforced Supervised Fine-Tuning](https://openreview.net/forum?id=eJcCW9oNfH) | planning / reasoning / RL | 机械臂/机器人操作 | 通过反馈自我改进规划 | [paper](https://openreview.net/forum?id=eJcCW9oNfH) | - | 自改进规划 | 用于评估高层规划是否能落到可执行动作。 |
| ICLR 2026 | [Embodied-R1: Reinforced Embodied Reasoning for General Robotic Manipulation](https://openreview.net/forum?id=i5wlozMFsQ) | planning / reasoning / RL | 机械臂/机器人操作 | 通过反馈自我改进规划 | [paper](https://openreview.net/forum?id=i5wlozMFsQ) | EAI-VLA-VLN | 自改进规划 | 用于评估高层规划是否能落到可执行动作。 |
| AAAI 2026 | [ManipLVM-R1: Reinforcement Learning for Reasoning in Embodied Manipulation with Large Vision-Language Models](https://ojs.aaai.org/index.php/AAAI/article/view/38922) | planning / reasoning / RL | 机械臂/机器人操作 | 通过反馈自我改进规划 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38922) | - | 自改进规划 | 用于评估高层规划是否能落到可执行动作。 |
| ICML 2026 | [HALO: A Unified Vision-Language-Action Model for Embodied Multimodal Chain-of-Thought Reasoning](https://icml.cc/virtual/2026/poster/61922) | VLA / reasoning | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://icml.cc/virtual/2026/poster/61922) | - | 自改进规划 | 用于评估高层规划是否能落到可执行动作。 |
| ICML 2026 | [Latent Reasoning VLA: Latent Thinking and Prediction for Vision-Language-Action Models](https://icml.cc/virtual/2026/poster/64290) | VLA / reasoning | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://icml.cc/virtual/2026/poster/64290) | - | 自改进规划 | 用于评估高层规划是否能落到可执行动作。 |
| ICML 2026 | [LaST0: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model](https://icml.cc/virtual/2026/poster/61887) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://icml.cc/virtual/2026/poster/61887) | - | 自改进规划 | 用于评估高层规划是否能落到可执行动作。 |
| ICML 2026 | [LAGEA: Language Guided Embodied Agents for Robotic Manipulation](https://icml.cc/virtual/2026/poster/60801) | planning / reasoning | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://icml.cc/virtual/2026/poster/60801) | - | 自改进规划 | 用于评估高层规划是否能落到可执行动作。 |
| ICML 2026 | [Drift is a Sampling Error: SNR-Aware Power Distributions for Long-Horizon Robotic Planning](https://icml.cc/virtual/2026/poster/64055) | planning / reasoning | 机械臂/机器人操作 | 通过反馈自我改进规划 | [paper](https://icml.cc/virtual/2026/poster/64055) | - | 自改进规划 | 用于评估高层规划是否能落到可执行动作。 |
| CVPR 2026 | [ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models](https://arxiv.org/abs/2601.11404) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2601.11404) / [code](https://github.com/AgibotTech/ACoT-VLA) | Awesome-EAI | 自改进规划 | 用于评估高层规划是否能落到可执行动作。 |
| CVPR 2026 | [Fast-ThinkAct: Efficient Vision-Language-Action Reasoning via Verbalizable Latent Planning](https://arxiv.org/abs/2601.09708) | VLA / planning / reasoning | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2601.09708) / [project](https://research.nvidia.com/labs/twn/publication/cvpr_2026_fastthinkact/) | - | 自改进规划 | 用于评估高层规划是否能落到可执行动作。 |
| NeurIPS 2025 | [Fast-in-Slow: A Dual-System VLA Model Unifying Fast Manipulation within Slow Reasoning](https://arxiv.org/abs/2506.01953) | VLA / reasoning | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2506.01953) / [project](https://fast-in-slow.github.io/) | EAI-VLA-VLN, Efficient-VLA | 自改进规划 | 用于评估高层规划是否能落到可执行动作。 |
| NeurIPS 2025 | [ChatVLA-2: Vision-Language-Action Model with Open-World Reasoning](https://arxiv.org/abs/2505.21906) | VLA / reasoning / RL | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2505.21906) / [project](https://chatvla-2.github.io/) | - | 自改进规划 | 用于评估高层规划是否能落到可执行动作。 |
| NeurIPS 2025 | [VLA-OS: Structuring and Dissecting Planning Representations and Paradigms in Vision-Language-Action Models](https://arxiv.org/abs/2506.17561) | VLA / planning | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2506.17561) / [project](https://nus-lins-lab.github.io/vlaos/) | - | 自改进规划 | 用于评估高层规划是否能落到可执行动作。 |
| NeurIPS 2025 | [ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning](https://arxiv.org/abs/2507.16815) | VLA / planning / reasoning | 触觉/接触操作 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2507.16815) / [project](https://jasper0314-huang.github.io/thinkact-vla/) | EAI-VLA-VLN, RL-VLA | 自改进规划 | 用于评估高层规划是否能落到可执行动作。 |
| NeurIPS 2025 | [Self-Improving Embodied Foundation Models](https://arxiv.org/abs/2509.15155) | VLA | 机械臂/机器人操作 | 通过反馈自我改进规划 | [paper](https://arxiv.org/abs/2509.15155) / [project](https://self-improving-efms.github.io/) | Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, EAI-Safety, WAM, RL-VLA | 自改进规划 | 用于评估高层规划是否能落到可执行动作。 |
| NeurIPS 2025 | [Chain-of-Action: Trajectory Autoregressive Modeling for Robotic Manipulation](https://arxiv.org/abs/2506.09990) | VLA / autoregressive policy | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2506.09990) / [project](https://chain-of-action.github.io/) | EAI-VLA-VLN | 自改进规划 | 用于评估高层规划是否能落到可执行动作。 |
| NeurIPS 2025 | [Towards Reliable LLM-based Robots Planning via Combined Uncertainty Estimation](https://arxiv.org/abs/2510.08044) | planning / reasoning | 机械臂/机器人操作 | 通过反馈自我改进规划 | [paper](https://arxiv.org/abs/2510.08044) | - | 自改进规划 | 用于评估高层规划是否能落到可执行动作。 |
| NeurIPS 2025 | [HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning](https://arxiv.org/abs/2507.00833) | reasoning | 人形机器人 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2507.00833) | Humanoid-RL, WAM | 自改进规划 | 用于评估高层规划是否能落到可执行动作。 |
| NeurIPS 2025 | [DexFlyWheel: A Scalable and Self-improving Data Generation Framework for Dexterous Manipulation](https://arxiv.org/abs/2509.23829) | self-improving planner | 灵巧手/抓取 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2509.23829) / [project](https://dexflywheel.github.io/) | - | 自改进规划 | 用于评估高层规划是否能落到可执行动作。 |
| ICCV 2025 | [Adaptive Articulated Object Manipulation On The Fly with Foundation Model Reasoning and Part Grounding](https://arxiv.org/abs/2507.18276) | planning / reasoning | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2507.18276) | - | 自改进规划 | 用于评估高层规划是否能落到可执行动作。 |
| ICCV 2025 | [RoBridge: A Hierarchical Architecture Bridging Cognition and Execution for General Robotic Manipulation](https://arxiv.org/abs/2505.01709) | planning | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2505.01709) / [project](https://abliao.github.io/RoBridge/) | EAI-VLA-VLN | 自改进规划 | 用于评估高层规划是否能落到可执行动作。 |
| ICML 2025 | Efficient Robotic Policy Learning via Latent Space Backward Planning | planning / reasoning | 机械臂/机器人操作 | 提升推理或执行效率 | [paper](https://arxiv.org/abs/2505.06861) / [project](https://lbp-authors.github.io/) | - | 自改进规划 | 用于评估高层规划是否能落到可执行动作。 |
| ICML 2025 | Closed-Loop Long-Horizon Robotic Planning via Equilibrium Sequence Modeling | planning / reasoning | 机械臂/机器人操作 | 通过反馈自我改进规划 | [paper](https://arxiv.org/pdf/2410.01440) / [project](https://github.com/Singularity0104/equilibrium-planner) | Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Humanoid-RL, EAI-Safety, WAM, RL-VLA | 自改进规划 | 用于评估高层规划是否能落到可执行动作。 |
| ICML 2025 | WOMD-Reasoning: A Large-Scale Dataset for Interaction Reasoning in Driving | reasoning | 仿真/评测环境 | 提供训练/评测数据资源 | [paper](https://arxiv.org/abs/2407.04281) / [project](https://github.com/yhli123/WOMD-Reasoning) | - | 自改进规划 | 用于评估高层规划是否能落到可执行动作。 |
| CVPR 2025 | [CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models](https://cvpr.thecvf.com/virtual/2025/poster/33233) | VLA / reasoning | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://cvpr.thecvf.com/virtual/2025/poster/33233) | EAI-VLA-VLN, Awesome-VLA, WAM | 自改进规划 | 用于评估高层规划是否能落到可执行动作。 |
| CVPR 2025 | [DexHandDiff: Interaction-aware Diffusion Planning for Adaptive Dexterous Manipulation](https://arxiv.org/abs/2411.18562) | diffusion policy / planning | 灵巧手/抓取 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2411.18562) / [project](https://dexdiffuser.github.io/) | - | 自改进规划 | 用于评估高层规划是否能落到可执行动作。 |
| CVPR 2025 | [RoboBrain: A Unified Brain Model for Robotic Manipulation from Abstract to Concrete](https://arxiv.org/abs/2502.21257) | planning / reasoning | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2502.21257) | EAI-VLA-VLN | 自改进规划 | 用于评估高层规划是否能落到可执行动作。 |
| CVPR 2025 | [PhysVLM: Enabling Visual Language Models to Understand Robotic Physical Reachability](https://arxiv.org/abs/2503.08481) | planning / reasoning | 机械臂/机器人操作 | 通过反馈自我改进规划 | [paper](https://arxiv.org/abs/2503.08481) | EAI-VLA-VLN | 自改进规划 | 用于评估高层规划是否能落到可执行动作。 |
| CVPR 2025 | [RoboSpatial: Teaching Spatial Understanding to 2D and 3D Vision-Language Models for Robotics](https://arxiv.org/abs/2411.16537) | planning / reasoning / 3D representation | 机械臂/机器人操作 | 通过反馈自我改进规划 | [paper](https://arxiv.org/abs/2411.16537) | - | 自改进规划 | 用于评估高层规划是否能落到可执行动作。 |
| CVPR 2025 | Tartan IMU: A Light Foundation Model for Inertial Positioning in Robotics | planning / reasoning | 机械臂/机器人操作 | 通过反馈自我改进规划 |  | - | 自改进规划 | 用于评估高层规划是否能落到可执行动作。 |

### 本体扩展 / 灵巧操作

本体扩展决定具身智能是否能从单机械臂走向人形、双臂、灵巧手和触觉接触任务。表中论文体现了动作空间、传感方式和控制目标随本体变化而复杂化。

子方向：humanoid、bimanual、dexterous hand、tactile/contact-rich、grasp。

共 72 篇。

| 子方向 | 条目数 | 观察重点 |
| --- | ---: | --- |
| humanoid | 21 | 看全身控制、移动操作和人形本体泛化。 |
| bimanual | 11 | 看双臂协同、长程操作和协调控制。 |
| dexterous hand | 27 | 看灵巧手动作空间和抓取迁移。 |
| tactile/contact-rich | 13 | 看触觉、接触动力学和精细反馈。 |

#### humanoid

共 21 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 来源 | 本体/控制属性 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ICLR 2026 | [WholeBodyVLA: Towards Unified Latent VLA for Whole-body Loco-manipulation Control](https://openreview.net/forum?id=OCJmVjyzN7) | humanoid control | 人形/足式机器人 | 提升复杂本体控制 | [paper](https://openreview.net/forum?id=OCJmVjyzN7) | Awesome-EAI, Humanoid-RL | 人形/全身控制 | 用于观察本体差异如何改变控制和数据需求。 |
| ICLR 2026 | [Endowing GPT-4 with a Humanoid Body: Building the Bridge Between Off-the-Shelf VLMs and the Physical World](https://openreview.net/forum?id=aQWSEjcN9V) | humanoid control | 人形/足式机器人 | 提升复杂本体控制 | [paper](https://openreview.net/forum?id=aQWSEjcN9V) | Humanoid-RL | 人形/全身控制 | 用于观察本体差异如何改变控制和数据需求。 |
| ICLR 2026 | [HWC-Loco: A Hierarchical Whole-Body Control Approach to Robust Humanoid Locomotion](https://openreview.net/forum?id=3UE3Aatcjy) | humanoid control | 人形/足式机器人 | 提升复杂本体控制 | [paper](https://openreview.net/forum?id=3UE3Aatcjy) | Humanoid-RL | 人形/全身控制 | 用于观察本体差异如何改变控制和数据需求。 |
| ICLR 2026 | [Task Tokens: A Flexible Approach to Adapting Behavior Foundation Models](https://openreview.net/forum?id=6T3wJQhvc3) | humanoid control | 人形/足式机器人 | 提升复杂本体控制 | [paper](https://openreview.net/forum?id=6T3wJQhvc3) | - | 人形/全身控制 | 用于观察本体差异如何改变控制和数据需求。 |
| ICLR 2026 | [BFM-Zero: A Promptable Behavioral Foundation Model for Humanoid Control Using Unsupervised Reinforcement Learning](https://openreview.net/forum?id=jkhl2oI0g5) | humanoid control | 人形/足式机器人 | 提升复杂本体控制 | [paper](https://openreview.net/forum?id=jkhl2oI0g5) | Humanoid-RL | 人形/全身控制 | 用于观察本体差异如何改变控制和数据需求。 |
| ICLR 2026 | [From Language to Locomotion: Retargeting-free Humanoid Control via Motion Latent Guidance](https://openreview.net/forum?id=k3Cyx3Uets) | humanoid control | 人形/足式机器人 | 提升复杂本体控制 | [paper](https://openreview.net/forum?id=k3Cyx3Uets) | Humanoid-RL | 人形/全身控制 | 用于观察本体差异如何改变控制和数据需求。 |
| ICLR 2026 | [Towards Bridging the Gap between Large-Scale Pretraining and Efficient Finetuning for Humanoid Control](https://openreview.net/forum?id=NEOTsyyYH7) | humanoid control | 人形/足式机器人 | 提升复杂本体控制 | [paper](https://openreview.net/forum?id=NEOTsyyYH7) | Humanoid-RL | 人形/全身控制 | 用于观察本体差异如何改变控制和数据需求。 |
| ICLR 2026 | [Hierarchical Value-Decomposed Offline Reinforcement Learning for Whole-Body Control](https://openreview.net/forum?id=eSkDNIGbcd) | humanoid control | 人形/足式机器人 | 提升复杂本体控制 | [paper](https://openreview.net/forum?id=eSkDNIGbcd) | - | 人形/全身控制 | 用于观察本体差异如何改变控制和数据需求。 |
| AAAI 2026 | [Whole-Body Coordination for Dynamic Object Grasping with Legged Manipulators](https://ojs.aaai.org/index.php/AAAI/article/view/38908) | humanoid control | 人形/足式机器人 | 提升复杂本体控制 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38908) | HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Robot-Learning, Humanoid-RL, EAI-Safety, WAM | 人形/全身控制 | 用于观察本体差异如何改变控制和数据需求。 |
| AAAI 2026 | [Coordinated Humanoid Robot Locomotion with Symmetry Equivariant Reinforcement Learning Policy](https://ojs.aaai.org/index.php/AAAI/article/view/38918) | humanoid control | 人形/足式机器人 | 提升复杂本体控制 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38918) | Humanoid-RL | 人形/全身控制 | 用于观察本体差异如何改变控制和数据需求。 |
| AAAI 2026 | [FARM: Frame-Accelerated Augmentation and Residual Mixture-of-Experts for Physics-Based High-Dynamic Humanoid Control](https://ojs.aaai.org/index.php/AAAI/article/view/38924) | humanoid control | 人形/足式机器人 | 提升复杂本体控制 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38924) | Humanoid-RL | 人形/全身控制 | 用于观察本体差异如何改变控制和数据需求。 |
| AAAI 2026 | [ODYSSEY: Open-World Quadrupeds Exploration and Manipulation for Long-Horizon Tasks](https://ojs.aaai.org/index.php/AAAI/article/view/38927) | humanoid control | 人形/足式机器人 | 提升复杂本体控制 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38927) | - | 人形/全身控制 | 用于观察本体差异如何改变控制和数据需求。 |
| AAAI 2026 | [Keep On Going: Learning Robust Humanoid Motion Skills via Selective Adversarial Training](https://ojs.aaai.org/index.php/AAAI/article/view/38949) | humanoid control | 人形/足式机器人 | 提升复杂本体控制 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38949) | Humanoid-RL | 人形/全身控制 | 用于观察本体差异如何改变控制和数据需求。 |
| AAAI 2026 | [Towards Adaptive Humanoid Control via Multi-Behavior Distillation and Reinforced Fine-Tuning](https://ojs.aaai.org/index.php/AAAI/article/view/38951) | humanoid control | 人形/足式机器人 | 提升复杂本体控制 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38951) | Humanoid-RL | 人形/全身控制 | 用于观察本体差异如何改变控制和数据需求。 |
| ICML 2026 | [Scalable and General Whole-Body Control for Cross-Humanoid Locomotion](https://icml.cc/virtual/2026/poster/62003) | humanoid control | 人形机器人 | 提升人形机器人控制 | [paper](https://icml.cc/virtual/2026/poster/62003) | Awesome-EAI, Humanoid-RL | 人形/全身控制 | 用于观察本体差异如何改变控制和数据需求。 |
| ICML 2026 | [Learning Transferable Interaction Primitives from Game Videos for Humanoids](https://icml.cc/virtual/2026/poster/65120) | humanoid control | 人形机器人 | 提升人形机器人控制 | [paper](https://icml.cc/virtual/2026/poster/65120) | - | 人形/全身控制 | 用于观察本体差异如何改变控制和数据需求。 |
| CVPR 2026 | [VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation](https://arxiv.org/abs/2511.15200) | humanoid control | 人形机器人 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2511.15200) / [project](https://viral-humanoid.github.io/) | Humanoid-RL | 人形/全身控制 | 用于观察本体差异如何改变控制和数据需求。 |
| NeurIPS 2025 | [Adversarial Locomotion and Motion Imitation for Humanoid Policy Learning](https://arxiv.org/abs/2504.14305) | humanoid control | 人形机器人 | 提升人形机器人控制 | [paper](https://arxiv.org/abs/2504.14305) / [project](https://almi-humanoid.github.io/) | Humanoid-RL | 人形/全身控制 | 用于观察本体差异如何改变控制和数据需求。 |
| NeurIPS 2025 | [From Experts to a Generalist: Toward General Whole-Body Control for Humanoid Robots](https://arxiv.org/abs/2506.12779) | humanoid control | 人形机器人 | 提升人形机器人控制 | [paper](https://arxiv.org/abs/2506.12779) / [project](https://beingbeyond.github.io/BumbleBee/) | Humanoid-RL | 人形/全身控制 | 用于观察本体差异如何改变控制和数据需求。 |
| NeurIPS 2025 | [KungfuBot: Physics-Based Humanoid Whole-Body Control for Learning Highly-Dynamic Skills](https://kungfubot.github.io/) | humanoid control | 人形机器人 | 提升人形机器人控制 | [paper](https://kungfubot.github.io/) / [project](https://arxiv.org/abs/2506.12851) | Humanoid-RL | 人形/全身控制 | 用于观察本体差异如何改变控制和数据需求。 |
| CVPR 2025 | [Let Humanoid Robots Go Hiking! Integrative Skill Development over Complex Trails](https://cvpr.thecvf.com/virtual/2025/poster/34565) | humanoid control | 人形机器人 | 提升人形机器人控制 | [paper](https://cvpr.thecvf.com/virtual/2025/poster/34565) / [project](https://lego-h-humanoidrobothiking.github.io/) | - | 人形/全身控制 | 用于观察本体差异如何改变控制和数据需求。 |

#### bimanual

共 11 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 来源 | 本体/控制属性 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ICLR 2026 | [TwinVLA: Data-Efficient Bimanual Manipulation with Twin Single-Arm Vision-Language-Action Models](https://openreview.net/forum?id=jG9W6nAwVz) | bimanual policy | 双臂机器人 | 提升机器人操作泛化和稳定性 | [paper](https://openreview.net/forum?id=jG9W6nAwVz) | - | 双臂操作 | 用于观察本体差异如何改变控制和数据需求。 |
| ICLR 2026 | [VLBiMan: Vision-Language Anchored One-Shot Demonstration Enables Generalizable Bimanual Robotic Manipulation](https://openreview.net/forum?id=he86smZzRk) | bimanual policy | 双臂机器人 | 提升机器人操作泛化和稳定性 | [paper](https://openreview.net/forum?id=he86smZzRk) | - | 双臂操作 | 用于观察本体差异如何改变控制和数据需求。 |
| AAAI 2026 | [LatentVLA: Taming Latent Space for Generalizable and Long-Horizon Bimanual Manipulation](https://ojs.aaai.org/index.php/AAAI/article/view/38926) | bimanual policy | 双臂机器人 | 提升机器人操作泛化和稳定性 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38926) | - | 双臂操作 | 用于观察本体差异如何改变控制和数据需求。 |
| ICML 2026 | [DexMachina: Functional Retargeting for Bimanual Dexterous Manipulation](https://icml.cc/virtual/2026/poster/63277) | bimanual policy | 双臂机器人 | 提升机器人操作泛化和稳定性 | [paper](https://icml.cc/virtual/2026/poster/63277) | - | 双臂操作 | 用于观察本体差异如何改变控制和数据需求。 |
| ICML 2026 | [DECO: Decoupled Multimodal Diffusion Transformer for Bimanual Dexterous Manipulation with a Plugin Tactile Adapter](https://icml.cc/virtual/2026/poster/66358) | diffusion policy / tactile policy / diffusion transformer | 双臂机器人 | 提升机器人操作泛化和稳定性 | [paper](https://icml.cc/virtual/2026/poster/66358) | EAI-VLA-VLN | 双臂操作 | 用于观察本体差异如何改变控制和数据需求。 |
| ICML 2026 | [RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation](https://icml.cc/virtual/2026/poster/62192) | bimanual policy | 双臂机器人 | 提供评测任务和数据基准 | [paper](https://icml.cc/virtual/2026/poster/62192) | EAI-Guide, EAI-VLA-VLN, Efficient-VLA, WAM, RL-VLA | 双臂操作 | 用于观察本体差异如何改变控制和数据需求。 |
| ICCV 2025 | [Rethinking Bimanual Robotic Manipulation: Learning with Decoupled Interaction Framework](https://arxiv.org/abs/2503.09186) | bimanual policy | 双臂机器人 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2503.09186) | EAI-VLA-VLN | 双臂操作 | 用于观察本体差异如何改变控制和数据需求。 |
| ICCV 2025 | [AnyBimanual: Transferring Unimanual Policy for General Bimanual Manipulation](https://arxiv.org/abs/2412.06779) | bimanual policy | 双臂机器人 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2412.06779) / [project](https://anybimanual.github.io/) | - | 双臂操作 | 用于观察本体差异如何改变控制和数据需求。 |
| ICCV 2025 | [DexH2R: A Benchmark for Dynamic Dexterous Grasping in Human-to-Robot Handover](https://arxiv.org/abs/2506.23152) | bimanual policy | 灵巧手/抓取 | 提供评测任务和数据基准 | [paper](https://arxiv.org/abs/2506.23152) / [project](https://dexh2r.github.io/) | - | 双臂操作 | 用于观察本体差异如何改变控制和数据需求。 |
| CVPR 2025 | [KStar Diffuser: Spatial-Temporal Graph Diffusion Policy with Kinematics Modeling for Bimanual Robotic Manipulation](https://arxiv.org/abs/2503.10743) | diffusion policy | 双臂机器人 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2503.10743) | HCP-Survey | 双臂操作 | 用于观察本体差异如何改变控制和数据需求。 |
| CVPR 2025 | [MobileH2R: Learning Generalizable Human to Mobile Robot Handover Exclusively from Scalable and Diverse Synthetic Data](https://arxiv.org/abs/2501.04595) | bimanual policy | 灵巧手/抓取 | 协调双臂协作操作 | [paper](https://arxiv.org/abs/2501.04595) | Humanoid-RL | 双臂操作 | 用于观察本体差异如何改变控制和数据需求。 |

#### dexterous hand

共 27 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 来源 | 本体/控制属性 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ICLR 2026 | [DemoGrasp: Universal Dexterous Grasping from a Single Demonstration](https://openreview.net/forum?id=Bf4FeuW0Mr) | dexterous manipulation | 灵巧手/抓取 | 提升灵巧操作能力 | [paper](https://openreview.net/forum?id=Bf4FeuW0Mr) | - | 灵巧手/抓取 | 用于观察本体差异如何改变控制和数据需求。 |
| ICLR 2026 | [DexNDM: Closing the Reality Gap for Dexterous In-Hand Rotation via Joint-Wise Neural Dynamics Model](https://openreview.net/forum?id=80vjyj5o7l) | dexterous manipulation | 灵巧手/抓取 | 提升灵巧操作能力 | [paper](https://openreview.net/forum?id=80vjyj5o7l) | - | 灵巧手/抓取 | 用于观察本体差异如何改变控制和数据需求。 |
| ICLR 2026 | [EgoDex: Learning Dexterous Manipulation from Large-Scale Egocentric Video](https://openreview.net/forum?id=FFxkFMU89E) | dexterous manipulation | 灵巧手/抓取 | 提升灵巧操作能力 | [paper](https://openreview.net/forum?id=FFxkFMU89E) | Humanoid-RL, WAM | 灵巧手/抓取 | 用于观察本体差异如何改变控制和数据需求。 |
| ICLR 2026 | [RFS: Reinforcement learning with Residual flow steering for dexterous manipulation](https://openreview.net/forum?id=Kt9tJeOwjy) | dexterous manipulation | 灵巧手/抓取 | 提升灵巧操作能力 | [paper](https://openreview.net/forum?id=Kt9tJeOwjy) | - | 灵巧手/抓取 | 用于观察本体差异如何改变控制和数据需求。 |
| ICLR 2026 | [Learning to Grasp Anything By Playing with Random Toys](https://openreview.net/forum?id=NZDaMcpXZm) | dexterous manipulation | 灵巧手/抓取 | 提升灵巧操作能力 | [paper](https://openreview.net/forum?id=NZDaMcpXZm) | Humanoid-RL | 灵巧手/抓取 | 用于观察本体差异如何改变控制和数据需求。 |
| ICLR 2026 | [SARM: Stage-Aware Reward Modeling for Long Horizon Robot Manipulation](https://openreview.net/forum?id=aemqAxScl9) | dexterous manipulation | 灵巧手/抓取 | 提升灵巧操作能力 | [paper](https://openreview.net/forum?id=aemqAxScl9) | - | 灵巧手/抓取 | 用于观察本体差异如何改变控制和数据需求。 |
| ICLR 2026 | [UniHM: Unified Dexterous Hand Manipulation with Vision Language Model](https://openreview.net/forum?id=cVX3VqO8BO) | dexterous manipulation | 灵巧手/抓取 | 提升灵巧操作能力 | [paper](https://openreview.net/forum?id=cVX3VqO8BO) | - | 灵巧手/抓取 | 用于观察本体差异如何改变控制和数据需求。 |
| ICLR 2026 | [Cross-Embodied Co-Design for Dexterous Hands](https://openreview.net/forum?id=k8ovuXEQQu) | dexterous manipulation | 灵巧手/抓取 | 提升灵巧操作能力 | [paper](https://openreview.net/forum?id=k8ovuXEQQu) | - | 灵巧手/抓取 | 用于观察本体差异如何改变控制和数据需求。 |
| ICLR 2026 | [Robotic Manipulation by Imitating Generated Videos Without Physical Demonstrations](https://openreview.net/forum?id=tv0Sz8A9Tc) | dexterous manipulation | 灵巧手/抓取 | 提升灵巧操作能力 | [paper](https://openreview.net/forum?id=tv0Sz8A9Tc) | EAI-Guide, HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Efficient-VLA, Robot-Learning, Humanoid-RL, EAI-Safety, WAM, RL-VLA | 灵巧手/抓取 | 用于观察本体差异如何改变控制和数据需求。 |
| ICLR 2026 | [Primary-Fine Decoupling for Action Generation in Robotic Imitation](https://openreview.net/forum?id=wySMuWHmt4) | dexterous manipulation | 灵巧手/抓取 | 提升灵巧操作能力 | [paper](https://openreview.net/forum?id=wySMuWHmt4) | - | 灵巧手/抓取 | 用于观察本体差异如何改变控制和数据需求。 |
| ICLR 2026 | [D-REX: Differentiable Real-to-Sim-to-Real Engine for Learning Dexterous Grasping](https://openreview.net/forum?id=13jshGCK9i) | dexterous manipulation | 灵巧手/抓取 | 提升灵巧操作能力 | [paper](https://openreview.net/forum?id=13jshGCK9i) | - | 灵巧手/抓取 | 用于观察本体差异如何改变控制和数据需求。 |
| ICLR 2026 | [Interaction-aware Representation Modeling With Co-Occurrence Consistency for Egocentric Hand-Object Parsing](https://openreview.net/forum?id=RYwQ0xQcAh) | dexterous manipulation | 灵巧手/抓取 | 提升灵巧操作能力 | [paper](https://openreview.net/forum?id=RYwQ0xQcAh) | - | 灵巧手/抓取 | 用于观察本体差异如何改变控制和数据需求。 |
| AAAI 2026 | [GRIM: Task-Oriented Grasping with Conditioning on Generative Examples](https://ojs.aaai.org/index.php/AAAI/article/view/38873) | dexterous manipulation | 灵巧手/抓取 | 提升灵巧操作能力 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38873) | - | 灵巧手/抓取 | 用于观察本体差异如何改变控制和数据需求。 |
| AAAI 2026 | [Dexterous Manipulation Transfer via Progressive Kinematic-Dynamic Alignment](https://ojs.aaai.org/index.php/AAAI/article/view/38874) | dexterous manipulation | 灵巧手/抓取 | 提升灵巧操作能力 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38874) | HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Humanoid-RL, WAM | 灵巧手/抓取 | 用于观察本体差异如何改变控制和数据需求。 |
| AAAI 2026 | [Learning Object-Centric Motion Priors from Human for Robotic Dexterous Manipulation](https://ojs.aaai.org/index.php/AAAI/article/view/38892) | dexterous manipulation | 灵巧手/抓取 | 提升灵巧操作能力 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38892) | - | 灵巧手/抓取 | 用于观察本体差异如何改变控制和数据需求。 |
| AAAI 2026 | [Real Garment Benchmark (RGBench): A Comprehensive Benchmark for Robotic Garment Manipulation Featuring a High-Fidelity Scalable Simulator](https://ojs.aaai.org/index.php/AAAI/article/view/38894) | dexterous manipulation | 灵巧手/抓取 | 提升灵巧操作能力 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38894) | - | 灵巧手/抓取 | 用于观察本体差异如何改变控制和数据需求。 |
| AAAI 2026 | [GraphGrasp: Lightweight and Efficient Graph-Guided 6-DoF Robotic Grasp Pose Estimation Network](https://ojs.aaai.org/index.php/AAAI/article/view/38940) | dexterous manipulation | 灵巧手/抓取 | 提升灵巧操作能力 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38940) | - | 灵巧手/抓取 | 用于观察本体差异如何改变控制和数据需求。 |
| AAAI 2026 | [DexGraspVLA: A Vision-Language-Action Framework Towards General Dexterous Grasping](https://ojs.aaai.org/index.php/AAAI/article/view/38953) | dexterous manipulation | 灵巧手/抓取 | 提升灵巧操作能力 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38953) | EAI-VLA-VLN, Awesome-VLA | 灵巧手/抓取 | 用于观察本体差异如何改变控制和数据需求。 |
| AAAI 2026 | [Effective Robotic Cloth Grasping Through Suppressing False Discoveries](https://ojs.aaai.org/index.php/AAAI/article/view/38957) | dexterous manipulation | 灵巧手/抓取 | 提升灵巧操作能力 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38957) | - | 灵巧手/抓取 | 用于观察本体差异如何改变控制和数据需求。 |
| CVPR 2026 | [UniDex: A Robot Foundation Suite for Universal Dexterous Hand Control from Egocentric Human Videos](https://arxiv.org/abs/2603.22264) | VLA | 灵巧手/抓取 | 提升灵巧操作能力 | [paper](https://arxiv.org/abs/2603.22264) / [project](https://unidex-ai.github.io/) / [code](https://github.com/unidex-ai/UniDex) | - | 灵巧手/抓取 | 用于观察本体差异如何改变控制和数据需求。 |
| NeurIPS 2025 | [Contact Map Transfer with Conditional Diffusion Model for Generalizable Dexterous Grasp Generation](https://arxiv.org/pdf/2511.01276) | diffusion policy | 灵巧手/抓取 | 提升灵巧操作能力 | [paper](https://arxiv.org/pdf/2511.01276) / [project](https://cmtdiffusion.github.io/) | - | 灵巧手/抓取 | 用于观察本体差异如何改变控制和数据需求。 |
| NeurIPS 2025 | [Grasp2Grasp: Vision-Based Dexterous Grasp Translation via Schrödinger Bridges](https://arxiv.org/abs/2506.02489) | dexterous manipulation | 灵巧手/抓取 | 提升灵巧操作能力 | [paper](https://arxiv.org/abs/2506.02489) / [project](https://grasp2grasp.github.io/) | - | 灵巧手/抓取 | 用于观察本体差异如何改变控制和数据需求。 |
| NeurIPS 2025 | [Scaffolding Dexterous Manipulation with Vision-Language Models](https://arxiv.org/abs/2506.19212) | dexterous manipulation | 灵巧手/抓取 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2506.19212) / [project](https://sites.google.com/view/dexterous-vlm-scaffolding) | - | 灵巧手/抓取 | 用于观察本体差异如何改变控制和数据需求。 |
| NeurIPS 2025 | [DexGarmentLab: Dexterous Garment Manipulation Environment with Generalizable Policy](https://arxiv.org/abs/2505.11032) | dexterous manipulation | 灵巧手/抓取 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2505.11032) / [project](https://wayrise.github.io/DexGarmentLab/) | EAI-VLA-VLN | 灵巧手/抓取 | 用于观察本体差异如何改变控制和数据需求。 |
| CVPR 2025 | [UniGraspTransformer: Simplified Policy Distillation for Scalable Dexterous Robotic Grasping](https://arxiv.org/abs/2412.02699) | dexterous manipulation | 灵巧手/抓取 | 提升灵巧操作能力 | [paper](https://arxiv.org/abs/2412.02699) / [project](https://dexhand.github.io/UniGraspTransformer/) | - | 灵巧手/抓取 | 用于观察本体差异如何改变控制和数据需求。 |
| CVPR 2025 | [DexGrasp Anything: Towards Universal Robotic Dexterous Grasping with Physics Awareness](https://arxiv.org/abs/2503.08257) | dexterous manipulation | 灵巧手/抓取 | 提升灵巧操作能力 | [paper](https://arxiv.org/abs/2503.08257) / [project](https://github.com/4DVLab/DexGrasp-Anything) | HCP-Survey, EAI-VLA-VLN | 灵巧手/抓取 | 用于观察本体差异如何改变控制和数据需求。 |
| CVPR 2025 | [ZeroGrasp: Zero-Shot Shape Reconstruction Enabled Robotic Grasping](https://cvpr.thecvf.com/virtual/2025/poster/32440) | dexterous manipulation | 灵巧手/抓取 | 处理高自由度灵巧操作 | [paper](https://cvpr.thecvf.com/virtual/2025/poster/32440) | EAI-VLA-VLN | 灵巧手/抓取 | 用于观察本体差异如何改变控制和数据需求。 |

#### tactile/contact-rich

共 13 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 来源 | 本体/控制属性 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ICLR 2026 | [DexMove: Learning Tactile-Guided Non-Prehensile Manipulation with Dexterous Hands](https://openreview.net/forum?id=dT3ZciXvNX) | tactile policy | 触觉/接触操作 | 引入触觉提升接触操作 | [paper](https://openreview.net/forum?id=dT3ZciXvNX) | - | 灵巧手/抓取 | 用于观察本体差异如何改变控制和数据需求。 |
| ICLR 2026 | [AnyTouch 2: General Optical Tactile Representation Learning For Dynamic Tactile Perception](https://openreview.net/forum?id=ndilONnABZ) | tactile policy | 触觉/接触操作 | 引入触觉提升接触操作 | [paper](https://openreview.net/forum?id=ndilONnABZ) | - | 触觉/接触 | 用于观察本体差异如何改变控制和数据需求。 |
| ICLR 2026 | [APPLE: Toward General Active Perception via Reinforcement Learning](https://openreview.net/forum?id=hU2gT2Ucua) | tactile policy | 触觉/接触操作 | 引入触觉提升接触操作 | [paper](https://openreview.net/forum?id=hU2gT2Ucua) | Awesome-EAI, WAM | 触觉/接触 | 用于观察本体差异如何改变控制和数据需求。 |
| AAAI 2026 | [STOLA: Self-Adaptive Touch-Language Framework for Tactile Commonsense Reasoning in Open-Ended Scenarios](https://ojs.aaai.org/index.php/AAAI/article/view/38882) | tactile policy | 触觉/接触操作 | 引入触觉提升接触操作 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38882) | - | 触觉/接触 | 用于观察本体差异如何改变控制和数据需求。 |
| AAAI 2026 | [TouchFormer: A Robust Transformer-based Framework for Multimodal Material Perception](https://ojs.aaai.org/index.php/AAAI/article/view/38915) | tactile policy | 触觉/接触操作 | 引入触觉提升接触操作 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38915) | - | 触觉/接触 | 用于观察本体差异如何改变控制和数据需求。 |
| AAAI 2026 | [Collaborative Representation Learning for Alignment of Tactile, Language, and Vision Modalities](https://ojs.aaai.org/index.php/AAAI/article/view/38956) | tactile policy | 触觉/接触操作 | 引入触觉提升接触操作 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38956) | - | 触觉/接触 | 用于观察本体差异如何改变控制和数据需求。 |
| ICML 2026 | [Cross-Tactile Sensor Representation Learning](https://icml.cc/virtual/2026/poster/66793) | tactile policy | 触觉/接触操作 | 引入触觉提升接触操作 | [paper](https://icml.cc/virtual/2026/poster/66793) | - | 触觉/接触 | 用于观察本体差异如何改变控制和数据需求。 |
| ICML 2026 | [Tabero: Learning Gentle Manipulation with Closed-Loop Force Feedback from Vision, Touch, and Language](https://icml.cc/virtual/2026/poster/65669) | tactile policy | 触觉/接触操作 | 提升机器人操作泛化和稳定性 | [paper](https://icml.cc/virtual/2026/poster/65669) | - | 触觉/接触 | 用于观察本体差异如何改变控制和数据需求。 |
| NeurIPS 2025 | [Universal Visuo-Tactile Video Understanding for Embodied Interaction](https://arxiv.org/abs/2505.22566) | tactile policy | 触觉/接触操作 | 引入触觉提升接触操作 | [paper](https://arxiv.org/abs/2505.22566) | - | 触觉/接触 | 用于观察本体差异如何改变控制和数据需求。 |
| NeurIPS 2025 | [Enhancing Tactile-based Reinforcement Learning for Robotic Control](https://arxiv.org/abs/2510.21609) | tactile policy / RL | 触觉/接触操作 | 引入触觉提升接触操作 | [paper](https://arxiv.org/abs/2510.21609) / [project](https://elle-miller.github.io/tactile_rl/) | - | 触觉/接触 | 用于观察本体差异如何改变控制和数据需求。 |
| NeurIPS 2025 | [Taccel: Scaling Up Vision-based Tactile Robotics via High-performance GPU Simulation](https://taccel-simulator.github.io/assets/taccel-paper.pdf) | tactile policy | 触觉/接触操作 | 引入触觉提升接触操作 | [paper](https://taccel-simulator.github.io/assets/taccel-paper.pdf) / [project](http://taccel-simulator.github.io/) | - | 触觉/接触 | 用于观察本体差异如何改变控制和数据需求。 |
| NeurIPS 2025 | [Toward Artificial Palpation: Representation Learning of Touch on Soft Bodies](https://arxiv.org/abs/2511.16596) | tactile policy | 触觉/接触操作 | 处理触觉和接触丰富任务 | [paper](https://arxiv.org/abs/2511.16596) / [project](https://zoharri.github.io/artificial-palpation/) | - | 触觉/接触 | 用于观察本体差异如何改变控制和数据需求。 |
| NeurIPS 2025 | [Touch in the Wild: Learning Fine-Grained Manipulation with a Portable Visuo-Tactile Gripper](https://arxiv.org/abs/2507.15062v1) | tactile policy | 触觉/接触操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2507.15062v1) / [project](https://binghao-huang.github.io/touch_in_the_wild/) | - | 触觉/接触 | 用于观察本体差异如何改变控制和数据需求。 |

### 轻量化 / 评测 / 数据

这一方向决定能不能真实部署：端侧推理、缓存/量化/action tokenization、实时执行、sim2real、benchmark 和 safety evaluation 都是必需条件。

子方向：quantization/cache/tokenization、real-time execution、benchmark/dataset、sim2real、safety evaluation。

共 79 篇。

| 子方向 | 条目数 | 观察重点 |
| --- | ---: | --- |
| quantization/cache/tokenization | 17 | 看端侧部署、缓存复用和 action token 效率。 |
| real-time execution | 6 | 看低延迟执行和实时策略推理。 |
| benchmark/dataset | 30 | 看数据覆盖、任务设计和评测可信度。 |
| sim2real | 17 | 看仿真到真实迁移和真实部署差距。 |
| safety evaluation | 9 | 看鲁棒性、安全性和部署风险评估。 |

#### quantization/cache/tokenization

共 17 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 来源 | 部署/评测属性 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ICLR 2026 | [MetaVLA: Unified Meta Co-Training for Efficient Embodied Adaptation](https://openreview.net/forum?id=E1K2Ph3LtS) | VLA / efficiency | 机器人部署/评测环境 | 提升推理或执行效率 | [paper](https://openreview.net/forum?id=E1K2Ph3LtS) | EAI-VLA-VLN | 压缩/缓存/tokenization | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICLR 2026 | [SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration](https://openreview.net/forum?id=RwdGIIjPlC) | VLA / efficiency | 机器人部署/评测环境 | 提升推理或执行效率 | [paper](https://openreview.net/forum?id=RwdGIIjPlC) | Efficient-VLA | 压缩/缓存/tokenization | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICLR 2026 | [AutoQVLA: Not All Channels Are Equal in Vision-Language-Action Model's Quantization](https://openreview.net/forum?id=TpL2nXanru) | VLA / efficiency | 机器人部署/评测环境 | 提升推理或执行效率 | [paper](https://openreview.net/forum?id=TpL2nXanru) | - | 压缩/缓存/tokenization | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICLR 2026 | [Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation](https://openreview.net/forum?id=ea6j8k8Rnw) | VLA / efficiency | 机器人部署/评测环境 | 提升推理或执行效率 | [paper](https://openreview.net/forum?id=ea6j8k8Rnw) | EAI-VLA-VLN, Efficient-VLA | 压缩/缓存/tokenization | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICLR 2026 | [FASTer: Toward Powerful and Efficient Autoregressive Vision–Language–Action Models with Learnable Action Tokenizer and Block-wise Decoding](https://openreview.net/forum?id=k6nTUFoqeT) | VLA / efficiency | 机器人部署/评测环境 | 提升推理或执行效率 | [paper](https://openreview.net/forum?id=k6nTUFoqeT) | HCP-Survey, Awesome-EAI, EAI-VLA-VLN, EAI-Safety, RL-VLA | 压缩/缓存/tokenization | 用于评估部署效率、数据覆盖和评测可信度。 |
| AAAI 2026 | [FT-NCFM: An Influence-Aware Data Distillation Framework for Efficient VLA Models](https://ojs.aaai.org/index.php/AAAI/article/view/38880) | VLA / efficiency | 机器人部署/评测环境 | 提升推理或执行效率 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38880) | - | 压缩/缓存/tokenization | 用于评估部署效率、数据覆盖和评测可信度。 |
| AAAI 2026 | [Towards Efficient and Robust Manipulation via Multi-Frame Vision-Language-Action Modeling](https://ojs.aaai.org/index.php/AAAI/article/view/38903) | VLA / efficiency | 机器人部署/评测环境 | 提升推理或执行效率 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38903) | - | 压缩/缓存/tokenization | 用于评估部署效率、数据覆盖和评测可信度。 |
| AAAI 2026 | [SemanticVLA: Semantic-Aligned Sparsification and Enhancement for Efficient Robotic Manipulation](https://ojs.aaai.org/index.php/AAAI/article/view/38904) | VLA / efficiency | 机器人部署/评测环境 | 提升推理或执行效率 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38904) | - | 压缩/缓存/tokenization | 用于评估部署效率、数据覆盖和评测可信度。 |
| AAAI 2026 | [VLA-Adapter: An Effective Paradigm for Tiny-Scale Vision-Language-Action Model](https://ojs.aaai.org/index.php/AAAI/article/view/38931) | VLA / efficiency | 机器人部署/评测环境 | 提升推理或执行效率 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38931) | EAI-VLA-VLN, Awesome-VLA, Efficient-VLA, RL-VLA | 压缩/缓存/tokenization | 用于评估部署效率、数据覆盖和评测可信度。 |
| AAAI 2026 | [MoLe-VLA: Dynamic Layer-skipping Vision Language Action Model via Mixture-of-Layers for Efficient Robot Manipulation](https://ojs.aaai.org/index.php/AAAI/article/view/38945) | VLA / efficiency | 机器人部署/评测环境 | 提升推理或执行效率 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38945) | EAI-VLA-VLN, Efficient-VLA | 压缩/缓存/tokenization | 用于评估部署效率、数据覆盖和评测可信度。 |
| CVPR 2026 | [QuantVLA: Scale-Calibrated Post-Training Quantization for Vision-Language-Action Models](https://arxiv.org/abs/2602.20309) | VLA / quantization | 机器人部署/评测环境 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2602.20309) / [project](https://quantvla.github.io/) | - | 压缩/缓存/tokenization | 用于评估部署效率、数据覆盖和评测可信度。 |
| NeurIPS 2025 | [BEAST: Efficient Tokenization of B-Splines Encoded Action Sequences for Imitation Learning](https://arxiv.org/abs/2506.06072) | VLA / action tokenization | 机器人部署/评测环境 | 提升推理或执行效率 | [paper](https://arxiv.org/abs/2506.06072) | - | 压缩/缓存/tokenization | 用于评估部署效率、数据覆盖和评测可信度。 |
| NeurIPS 2025 | [Quantization-Free Autoregressive Action Transformer](https://arxiv.org/abs/2503.14259) | quantization / autoregressive policy | 机器人部署/评测环境 | 降低模型部署成本 | [paper](https://arxiv.org/abs/2503.14259) | - | 压缩/缓存/tokenization | 用于评估部署效率、数据覆盖和评测可信度。 |
| NeurIPS 2025 | [EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models](https://arxiv.org/abs/2506.10100) | VLA | 机器人部署/评测环境 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2506.10100) | Efficient-VLA | 压缩/缓存/tokenization | 用于评估部署效率、数据覆盖和评测可信度。 |
| NeurIPS 2025 | [VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching](https://arxiv.org/abs/2502.02175) | VLA / cache / action tokenization | 机器人部署/评测环境 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2502.02175) / [project](https://vla-cache.github.io/) | EAI-VLA-VLN, Efficient-VLA | 压缩/缓存/tokenization | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICCV 2025 | [VQ-VLA: Improving Vision-Language-Action Models via Scaling Vector-Quantized Action Tokenizers](https://arxiv.org/abs/2507.01016) | VLA / quantization / action tokenization | 机器人部署/评测环境 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2507.01016) / [project](https://xiaoxiao0406.github.io/vqvla.github.io) | EAI-VLA-VLN, Efficient-VLA | 压缩/缓存/tokenization | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICCV 2025 | [Saliency-Aware Quantized Imitation Learning for Efficient Robotic Control](https://arxiv.org/abs/2505.15304) | quantization | 机器人部署/评测环境 | 提升推理或执行效率 | [paper](https://arxiv.org/abs/2505.15304) | Efficient-VLA | 压缩/缓存/tokenization | 用于评估部署效率、数据覆盖和评测可信度。 |

#### real-time execution

共 6 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 来源 | 部署/评测属性 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ICLR 2026 | [Time Optimal Execution of Action Chunk Policies Beyond Demonstration Speed](https://openreview.net/forum?id=INsLvSCJ4z) | real-time execution | 机器人部署/评测环境 | 提升实时执行能力 | [paper](https://openreview.net/forum?id=INsLvSCJ4z) | - | 实时执行 | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICLR 2026 | [Mean Flow Policy with Instantaneous Velocity Constraint for One-step Action Generation](https://openreview.net/forum?id=mIeKe74W43) | real-time execution | 机器人部署/评测环境 | 提升实时执行能力 | [paper](https://openreview.net/forum?id=mIeKe74W43) | - | 实时执行 | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICLR 2026 | [Real-Time Robot Execution with Masked Action Chunking](https://openreview.net/forum?id=r0RGJ1j9on) | real-time execution | 机器人部署/评测环境 | 提升实时执行能力 | [paper](https://openreview.net/forum?id=r0RGJ1j9on) | HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Efficient-VLA, Humanoid-RL, EAI-Safety, WAM | 实时执行 | 用于评估部署效率、数据覆盖和评测可信度。 |
| NeurIPS 2025 | [Real-Time Execution of Action Chunking Flow Policies](https://www.physicalintelligence.company/download/real_time_chunking.pdf) | VLA / flow matching | 机器人部署/评测环境 | 提升实时执行能力 | [paper](https://www.physicalintelligence.company/download/real_time_chunking.pdf) / [project](https://www.physicalintelligence.company/research/real_time_chunking) | HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Efficient-VLA, Humanoid-RL, EAI-Safety, WAM | 实时执行 | 用于评估部署效率、数据覆盖和评测可信度。 |
| NeurIPS 2025 | [Accelerating Visual-Policy Learning through Parallel Differentiable Simulation](https://www.arxiv.org/abs/2505.10646) | real-time execution | 仿真/评测环境 | 提升实时执行能力 | [paper](https://www.arxiv.org/abs/2505.10646) / [project](https://haoxiangyou.github.io/Dva_website/) | - | 实时执行 | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICCV 2025 | [On-Device Diffusion Transformer Policy for Efficient Robot Manipulation](https://arxiv.org/abs/2508.00697) | diffusion policy / diffusion transformer | 机器人部署/评测环境 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2508.00697) | EAI-VLA-VLN, Efficient-VLA | 实时执行 | 用于评估部署效率、数据覆盖和评测可信度。 |

#### benchmark/dataset

共 30 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 来源 | 部署/评测属性 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ICLR 2026 | [D2E: Scaling Vision-Action Pretraining on Desktop Data for Transfer to Embodied AI](https://openreview.net/forum?id=TRwQND3xpt) | benchmark/dataset | 仿真/评测环境 | 提供评测任务和数据基准 | [paper](https://openreview.net/forum?id=TRwQND3xpt) | EAI-VLA-VLN | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICLR 2026 | [RoboInter: A Holistic Intermediate Representation Suite Towards Robotic Manipulation](https://openreview.net/forum?id=PGUC3mmMoi) | benchmark/dataset | 仿真/评测环境 | 提供评测任务和数据基准 | [paper](https://openreview.net/forum?id=PGUC3mmMoi) | - | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICLR 2026 | [AutoBio: A Simulation and Benchmark for Robotic Automation in Digital Biology Laboratory](https://openreview.net/forum?id=UUE6HEtjhu) | benchmark/dataset | 仿真/评测环境 | 提供评测任务和数据基准 | [paper](https://openreview.net/forum?id=UUE6HEtjhu) | - | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICLR 2026 | [Image Quality Assessment for Embodied AI](https://openreview.net/forum?id=azj53PLJRL) | benchmark/dataset | 仿真/评测环境 | 提供评测任务和数据基准 | [paper](https://openreview.net/forum?id=azj53PLJRL) | - | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICLR 2026 | [RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots](https://openreview.net/forum?id=tQJYKwc3n4) | benchmark/dataset | 仿真/评测环境 | 提供评测任务和数据基准 | [paper](https://openreview.net/forum?id=tQJYKwc3n4) | Humanoid-RL | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| AAAI 2026 | [H-RDT: Human Manipulation Enhanced Bimanual Robotic Manipulation](https://ojs.aaai.org/index.php/AAAI/article/view/38875) | benchmark/dataset | 仿真/评测环境 | 提供评测任务和数据基准 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38875) | EAI-VLA-VLN, Humanoid-RL | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| AAAI 2026 | [PEOD: A Pixel-Aligned Event-RGB Benchmark for Object Detection Under Challenging Conditions](https://ojs.aaai.org/index.php/AAAI/article/view/38883) | benchmark/dataset | 仿真/评测环境 | 提供评测任务和数据基准 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38883) | - | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| AAAI 2026 | [SIAM: Towards Generalizable Articulated Object Modeling via Single Robot-Object Interaction](https://ojs.aaai.org/index.php/AAAI/article/view/38913) | benchmark/dataset | 仿真/评测环境 | 提供评测任务和数据基准 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38913) | - | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| AAAI 2026 | [VirtualEnv: A Platform for Embodied AI Research](https://ojs.aaai.org/index.php/AAAI/article/view/38923) | benchmark/dataset | 仿真/评测环境 | 提供评测任务和数据基准 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38923) | - | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| AAAI 2026 | [Lifelong Language-Conditioned Robotic Manipulation Learning](https://ojs.aaai.org/index.php/AAAI/article/view/38930) | benchmark/dataset | 仿真/评测环境 | 提供评测任务和数据基准 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38930) | - | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICML 2026 | [AIR-VLA: Vision-Language-Action Systems for Aerial Manipulation](https://icml.cc/virtual/2026/poster/64411) | VLA | 无人机/空中机器人 | 改进视觉语言到动作策略 | [paper](https://icml.cc/virtual/2026/poster/64411) | Awesome-EAI | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICML 2026 | [DLO-Lab: Benchmarking Deformable Linear Object Manipulations with Differentiable Physics](https://icml.cc/virtual/2026/poster/63391) | benchmark/dataset | 仿真/评测环境 | 提供评测任务和数据基准 | [paper](https://icml.cc/virtual/2026/poster/63391) | - | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICML 2026 | [ManiSoft: Towards Vision-Language Manipulation for Soft Robotics](https://icml.cc/virtual/2026/poster/63416) | benchmark/dataset | 机器人部署/评测环境 | 提升机器人操作泛化和稳定性 | [paper](https://icml.cc/virtual/2026/poster/63416) | - | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICML 2026 | [OXE-AugE: A Large-Scale Robot Augmentation of OXE for Scaling Cross-Embodiment Policy Learning](https://icml.cc/virtual/2026/poster/64619) | benchmark/dataset | 机器人部署/评测环境 | 提供可复用评测资源 | [paper](https://icml.cc/virtual/2026/poster/64619) | - | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| NeurIPS 2025 | [BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models](https://arxiv.org/abs/2506.07961) | VLA / 3D representation | 机器人部署/评测环境 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2506.07961) / [project](https://bridgevla.github.io/) | EAI-VLA-VLN | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| NeurIPS 2025 | [RobotSmith: Generative Robotic Tool Design for Acquisition of Complex Manipulation Skill](https://arxiv.org/abs/2506.14763) | benchmark/dataset | 机器人部署/评测环境 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2506.14763) / [project](https://umass-embodied-agi.github.io/RobotSmith/) | EAI-VLA-VLN | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| NeurIPS 2025 | [URDF-Anything: Constructing Articulated Objects with 3D Multimodal Language Model](https://arxiv.org/abs/2511.00940) | 3D representation | 机器人部署/评测环境 | 提供可复用评测资源 | [paper](https://arxiv.org/abs/2511.00940) | - | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| NeurIPS 2025 | [FreqPolicy: Efficient Flow-based Visuomotor Policy via Frequency Consistency](https://arxiv.org/abs/2506.08822) | flow matching | 机器人部署/评测环境 | 提升推理或执行效率 | [paper](https://arxiv.org/abs/2506.08822) | EAI-VLA-VLN, Efficient-VLA | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| NeurIPS 2025 | [RoboCerebra: A Large-scale Benchmark for Long-horizon Robotic Manipulation Evaluation](https://www.arxiv.org/pdf/2506.06677) | benchmark/dataset | 仿真/评测环境 | 提供评测任务和数据基准 | [paper](https://www.arxiv.org/pdf/2506.06677) / [project](https://github.com/qiuboxiang/RoboCerebra) | EAI-VLA-VLN, WAM | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| NeurIPS 2025 | [SutureBot: A Precision Framework & Benchmark For Autonomous End-to-End Suturing](https://suturebot.github.io/static/SutureBot_NeurIPS_2025.pdf) | benchmark/dataset | 仿真/评测环境 | 提供评测任务和数据基准 | [paper](https://suturebot.github.io/static/SutureBot_NeurIPS_2025.pdf) / [project](https://suturebot.github.io/) | - | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| NeurIPS 2025 | Embodied Crowd Counting | benchmark/dataset | 机器人部署/评测环境 | 提供可复用评测资源 |  | - | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICCV 2025 | [CARP: Coarse-to-Fine Autoregressive Prediction for Visuomotor Policy Learning](https://arxiv.org/abs/2412.06782) | autoregressive policy | 机器人部署/评测环境 | 提供可复用评测资源 | [paper](https://arxiv.org/abs/2412.06782) / [project](https://carp-robot.github.io/) | EAI-VLA-VLN | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICCV 2025 | [RoboFactory: Exploring Embodied Agent Collaboration with Compositional Constraints](https://arxiv.org/abs/2503.16408) | benchmark/dataset | 仿真/评测环境 | 提供可复用评测资源 | [paper](https://arxiv.org/abs/2503.16408) / [project](https://vlabench.github.io/) | EAI-VLA-VLN | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICCV 2025 | [HUMOTO: A 4D Dataset of Mocap Human Object Interactions](https://arxiv.org/abs/2504.10414) | benchmark/dataset | 仿真/评测环境 | 提供训练/评测数据资源 | [paper](https://arxiv.org/abs/2504.10414) / [project](https://jiaxin-lu.github.io/humoto/) | Humanoid-RL | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICCV 2025 | [RoboMM: All-in-One Multimodal Large Model for Robotic Manipulation](https://arxiv.org/abs/2412.07215) | benchmark/dataset | 机器人部署/评测环境 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2412.07215) | EAI-VLA-VLN, WAM | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICCV 2025 | [Beyond the Destination: A Novel Benchmark for Exploration-Aware Embodied Question Answering](https://arxiv.org/abs/2503.11117) | benchmark/dataset | 仿真/评测环境 | 提供评测任务和数据基准 | [paper](https://arxiv.org/abs/2503.11117) / [project](https://github.com/HCPLab-SYSU/EXPRESS-Bench) | HCP-Survey | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICCV 2025 | [RobAVA: A Large-scale Dataset and Baseline Towards Video based Robotic Arm Action Understanding](https://iccv.thecvf.com/virtual/2025/poster/1787) | benchmark/dataset | 仿真/评测环境 | 提供训练/评测数据资源 | [paper](https://iccv.thecvf.com/virtual/2025/poster/1787) | - | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICCV 2025 | [RoboAnnotatorX: A Comprehensive and Universal Annotation Framework for Accurate Understanding of Long-horizon Robot Demonstration](https://iccv.thecvf.com/virtual/2025/poster/2215) | benchmark/dataset | 机器人部署/评测环境 | 提供可复用评测资源 | [paper](https://iccv.thecvf.com/virtual/2025/poster/2215) | - | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICML 2025 | EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents | benchmark/dataset | 仿真/评测环境 | 提供评测任务和数据基准 | [paper](https://arxiv.org/abs/2502.09560) / [project](https://embodiedbench.github.io/) | HCP-Survey, EAI-Safety | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| CVPR 2025 | [Pixel-aligned RGB-NIR Stereo Imaging and Dataset for Robot Vision](https://arxiv.org/abs/2411.18025) | benchmark/dataset | 仿真/评测环境 | 提供训练/评测数据资源 | [paper](https://arxiv.org/abs/2411.18025) | - | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |

#### sim2real

共 17 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 来源 | 部署/评测属性 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ICLR 2026 | [PD$^{2}$GS: Part-Level Decoupling and Continuous Deformation of Articulated Objects via Gaussian Splatting](https://openreview.net/forum?id=W3Q2xvrZtx) | sim2real | 仿真/评测环境 | 缩小仿真到真实差距 | [paper](https://openreview.net/forum?id=W3Q2xvrZtx) | - | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICLR 2026 | [Manipulation as in Simulation: Enabling Accurate Geometry Perception in Robots](https://openreview.net/forum?id=sWyX1BpeN4) | sim2real | 仿真/评测环境 | 缩小仿真到真实差距 | [paper](https://openreview.net/forum?id=sWyX1BpeN4) | - | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICLR 2026 | [Emergent Dexterity Via Diverse Resets and Large-Scale Reinforcement Learning](https://openreview.net/forum?id=nAO9LcV7nE) | sim2real | 仿真/评测环境 | 缩小仿真到真实差距 | [paper](https://openreview.net/forum?id=nAO9LcV7nE) | - | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICLR 2026 | [Sim2Real VLA: Zero-Shot Generalization of Synthesized Skills to Realistic Manipulation](https://openreview.net/forum?id=H4SyKHjd4c) | sim2real | 仿真/评测环境 | 缩小仿真到真实差距 | [paper](https://openreview.net/forum?id=H4SyKHjd4c) | EAI-Guide, Octoday, HCP-Survey, EAI-VLA-VLN, Humanoid-RL | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICLR 2026 | [Exo-Plore: Exploring Exoskeleton Control Space through Human-aligned Simulation](https://openreview.net/forum?id=TmYcqOnxhN) | sim2real | 仿真/评测环境 | 缩小仿真到真实差距 | [paper](https://openreview.net/forum?id=TmYcqOnxhN) | - | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICLR 2026 | [Latent Adaptation of Foundation Policies for Sim-to-Real Transfer](https://openreview.net/forum?id=yn9dzttHvT) | sim2real | 仿真/评测环境 | 缩小仿真到真实差距 | [paper](https://openreview.net/forum?id=yn9dzttHvT) | - | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICLR 2026 | [RobotArena $\infty$: Unlimited Robot Benchmarking via Real-to-Sim Translation](https://openreview.net/forum?id=OutljIofvS) | sim2real | 仿真/评测环境 | 缩小仿真到真实差距 | [paper](https://openreview.net/forum?id=OutljIofvS) | - | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICLR 2026 | [Contact-guided Real2Sim from Monocular Video with Planar Scene Primitives](https://openreview.net/forum?id=xlr3NqxUqY) | sim2real | 仿真/评测环境 | 缩小仿真到真实差距 | [paper](https://openreview.net/forum?id=xlr3NqxUqY) | Humanoid-RL | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICML 2026 | [FlatLab: A Unified Methodology Framework and Simulation-Based Benchmark for Robotic Manipulation of Flat Objects](https://icml.cc/virtual/2026/poster/66662) | sim2real | 仿真/评测环境 | 提供评测任务和数据基准 | [paper](https://icml.cc/virtual/2026/poster/66662) | - | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| CVPR 2026 | [GeCo-SRT: Geometry-aware Continual Adaptation for Robotic Cross-Task Sim-to-Real Transfer](https://arxiv.org/abs/2602.20871) | sim2real | 仿真/评测环境 | 缩小仿真到真实差距 | [paper](https://arxiv.org/abs/2602.20871) / [project](https://namelesscrew.github.io/) | - | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| NeurIPS 2025 | [EgoBridge: Domain Adaptation for Generalizable Imitation from Egocentric Human Data](https://arxiv.org/abs/2509.19626) | sim2real | 机器人部署/评测环境 | 缩小仿真到真实差距 | [paper](https://arxiv.org/abs/2509.19626) / [project](https://ego-bridge.github.io/) | - | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| NeurIPS 2025 | DEAL: Diffusion Evolution Adversarial Learning for Sim-to-Real Transfer | diffusion policy | 仿真/评测环境 | 缩小仿真到真实差距 |  | - | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| NeurIPS 2025 | [Generalizable Domain Adaptation for Sim-and-Real Policy Co-Training](https://arxiv.org/abs/2509.18631) | sim2real | 机器人部署/评测环境 | 缩小仿真到真实差距 | [paper](https://arxiv.org/abs/2509.18631) / [project](https://ot-sim2real.github.io/) | - | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| NeurIPS 2025 | [LabUtopia: High-Fidelity Simulation and Hierarchical Benchmark for Scientific Embodied Agents](https://arxiv.org/abs/2505.22634) | sim2real | 仿真/评测环境 | 提供评测任务和数据基准 | [paper](https://arxiv.org/abs/2505.22634) / [project](https://rui-li023.github.io/labutopia-site/) | - | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| NeurIPS 2025 | [SonoGym: High Performance Simulation for Challenging Surgical Tasks with Robotic Ultrasound](https://arxiv.org/abs/2507.01152) | sim2real | 仿真/评测环境 | 缩小仿真到真实差距 | [paper](https://arxiv.org/abs/2507.01152) / [project](https://github.com/SonoGym/SonoGym) | - | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICCV 2025 | [RoboPearls: Editable Video Simulation for Robot Manipulation](https://arxiv.org/abs/2506.22756) | RL | 仿真/评测环境 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2506.22756) / [project](https://tangtaogo.github.io/RoboPearls/) | EAI-VLA-VLN | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| CVPR 2025 | [RoboTwin: Dual-Arm Robot Benchmark with Generative Digital Twins (early version)](https://arxiv.org/abs/2409.02920) | RL | 双臂机器人 | 提供评测任务和数据基准 | [paper](https://arxiv.org/abs/2409.02920) / [project](https://robotwin-benchmark.github.io/early-version/) | EAI-Guide, EAI-VLA-VLN, Efficient-VLA, WAM, RL-VLA | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |

#### safety evaluation

共 9 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 来源 | 部署/评测属性 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ICLR 2026 | [Remotely Detectable Robot Policy Watermarking](https://openreview.net/forum?id=8s5jBVybhQ) | safety evaluation | 机器人部署/评测环境 | 评估鲁棒性和安全性 | [paper](https://openreview.net/forum?id=8s5jBVybhQ) | - | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICLR 2026 | [Uncovering Robot Vulnerabilities through Semantic Potential Fields](https://openreview.net/forum?id=Gsrw1vxq1G) | safety evaluation | 机器人部署/评测环境 | 评估鲁棒性和安全性 | [paper](https://openreview.net/forum?id=Gsrw1vxq1G) | - | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICML 2026 | [Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds](https://icml.cc/virtual/2026/poster/60472) | VLA / 3D representation | 机器人部署/评测环境 | 评估鲁棒性和安全性 | [paper](https://icml.cc/virtual/2026/poster/60472) | - | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICML 2026 | [PACT: Self-Evolving Physical Safety Alignment for Diffusion Policies in Embodied Manipulation](https://icml.cc/virtual/2026/poster/62679) | diffusion policy | 机器人部署/评测环境 | 提升机器人操作泛化和稳定性 | [paper](https://icml.cc/virtual/2026/poster/62679) | Awesome-VLA | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICML 2026 | [SafeLab: An Interactive High-Fidelity Benchmark for Embodied Safety in Scientific Robotics](https://icml.cc/virtual/2026/poster/61584) | safety evaluation | 仿真/评测环境 | 提供评测任务和数据基准 | [paper](https://icml.cc/virtual/2026/poster/61584) | - | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICML 2026 | [Dismantling the Illusion of Vision-Language-Action Models Competence via Explicit Distributional Shifts](https://icml.cc/virtual/2026/poster/64080) | VLA | 机器人部署/评测环境 | 改进视觉语言到动作策略 | [paper](https://icml.cc/virtual/2026/poster/64080) | - | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| CVPR 2026 | [LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models](https://arxiv.org/abs/2510.13626) | VLA | 机器人部署/评测环境 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2510.13626) / [project](https://huggingface.co/papers/2510.13626) | EAI-Safety, WAM | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| NeurIPS 2025 | [A Smooth Sea Never Made a Skilled SAILOR: Robust Imitation via Learning to Search](https://arxiv.org/abs/2506.05294) | safety evaluation | 机器人部署/评测环境 | 评估鲁棒性和安全性 | [paper](https://arxiv.org/abs/2506.05294) / [project](https://gokul.dev/sailor/) | - | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |
| NeurIPS 2025 | [PAC Bench: Do Foundation Models Understand Prerequisites for Executing Manipulation Policies?](https://arxiv.org/abs/2506.23725) | safety evaluation | 机器人部署/评测环境 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2506.23725) | RL-VLA | benchmark/dataset | 用于评估部署效率、数据覆盖和评测可信度。 |


## 重点阅读顺序

1. 先看 VLN 和 Agentic Planning：确认“大范围规划”和“细粒度规划”分别解决什么。
2. 再看 VLA 和 WAM：区分“直接动作生成”和“先想象/预测再执行”。
3. 最后看本体扩展、轻量化、评测：这些决定路线能不能真实部署。

## 源仓库补充条目

以下条目来自本次保存的 README 快照，不并入 CCF-A 主表；它们用于跟踪 WAM 数据源和 RL-VLA 方法线索。

| 条目 | 来源 | 方向 | 时间 | 资源 | 为什么跟踪 |
| --- | --- | --- | --- | --- | --- |
| UnifoLM-WBT Dataset | WAM | WAM training data / robot-centric | 2026-03 | [dataset](https://huggingface.co/collections/unitreerobotics/unifolm-wbt-dataset) | 机器人中心数据源，适合后续看 WAM 训练数据覆盖。 |
| DexUMI | WAM | UMI / dexterous manipulation data | 2025-05 | [paper](https://arxiv.org/pdf/2505.21864) / [web](https://dex-umi.github.io/) / [dataset](https://umi-data.github.io/) / [code](https://github.com/real-stanford/DexUMI) | 手部交互数据源，连接 WAM 与灵巧操作。 |
| InternData-A1 / InternVLA-A1 | WAM | simulation + VLA data | 2026-01 | [paper](https://arxiv.org/pdf/2601.02456) / [web](https://internrobotics.github.io/interndata-a1.github.io/) / [dataset](https://huggingface.co/datasets/InternRobotics/InternData-A1) / [code](https://github.com/InternRobotics/InternVLA-A1) | 同时有数据、模型和代码，适合作为 VLA/WAM 联合入口。 |
| EgoDex | WAM | egocentric dexterous data | 2025-05 | [paper](https://arxiv.org/pdf/2505.11709) / [dataset+code](https://github.com/apple/ml-egodex) | 第一视角灵巧操作数据，适合补足人类视频到机器人策略的链路。 |
| ARM | RL-VLA | Offline RL-VLA / real robot | 2026.4 | [paper](https://arxiv.org/pdf/2604.03037) / [project](https://aiming1998.github.io/ARM/) | 基于 GR00T N1.5 的真实机器人 RL-VLA 方法。 |
| LaST-R1 | RL-VLA | Online RL-VLA / simulation | 2026.04 | [paper](https://arxiv.org/abs/2604.28192) | RL-VLA 在线训练线索，适合后续补到 VLA 微调方向。 |
| POCO | RL-VLA | Offline + Online RL-VLA | 2026.04 | [paper](https://arxiv.org/abs/2604.01860) / [project](https://cccedric.github.io/poco/) | 覆盖 sim 和 real，且连接 π0/Octo 与 RL 优化。 |
| FASTER | RL-VLA | Test-time RL-VLA | 2026.04 | [paper](https://arxiv.org/abs/2604.19730) | 测试时 action optimization 线索，适合跟踪 VLA 执行期优化。 |

## 数据来源说明

GitHub 源仓库的元数据和 README 快照见 [`sources/github/repos.json`](sources/github/repos.json)；表格中的 `来源` 使用该文件里的 `id`。

| 来源 | 用途 |
| --- | --- |
| [CCF 2026 推荐目录](https://ccf.atom.im/) | 核对 2026 版 CCF-A 人工智能会议口径。 |
| [Songwxuan/Embodied-AI-Paper-TopConf](https://github.com/Songwxuan/Embodied-AI-Paper-TopConf) | CCF-A 论文主来源，按会议和方向分类；论文、代码和项目页链接优先采用该仓库中已给出的资源。 |
| [ICLR 2026 OpenReview](https://openreview.net/group?id=ICLR.cc/2026/Conference) | 核对 ICLR 2026 公开论文页和 PDF 资源。 |
| [AAAI-26 Intelligent Robotics proceedings](https://ojs.aaai.org/index.php/AAAI/issue/view/703) | 核对并补入 AAAI 2026 机器人方向论文。 |
| [jonyzhang2023/awesome-embodied-vla-va-vln](https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln) | 参考 VLA、WAM、VLN、VA 和 survey 的组织方式。 |
| [OpenMOSS/Awesome-WAM](https://github.com/OpenMOSS/Awesome-WAM) | 参考 WAM 的 cascaded/joint、autoregressive/diffusion、evaluation/training data 分类。 |
| [UCSB-AI/awesome-vision-language-navigation](https://github.com/UCSB-AI/awesome-vision-language-navigation) | 参考 VLN 的 dataset、evaluation、representation、action strategy、planning、asking for help 分类。 |
| [DelinQu/awesome-vision-language-action-model](https://github.com/DelinQu/awesome-vision-language-action-model) | 参考 VLA 里程碑时间线。 |
| [yueen-ma/Awesome-VLA](https://github.com/yueen-ma/Awesome-VLA) | 参考 VLA components、world models、reasoning、policy steering、low-level/high-level planners 分类。 |
