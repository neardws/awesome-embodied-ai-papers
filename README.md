# 具身智能前沿方向调研结果

更新日期：2026-06-28

本 README 是调研结果索引：按方向总结具身智能前沿，并把已读 GitHub 仓库中明确归属 CCF-A 会议的论文整理为细粒度表格。

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
| VLN / 大范围导航 | 连续环境 VLN、地图记忆、物理可执行导航、城市/开放环境导航、低成本/端侧导航 | 34 | VLN 关注语言目标、空间地图、记忆、探索和导航决策，核心问题是把自然语言任务变成可执行的大范围移动计划。当前 CCF-A 条目显示，研究正在从离散导航图转向连续环境、物理可执行导航、开放城市环境和低成本端侧导航。 |
| VLA / 操作策略 | generalist VLA、action representation、diffusion/flow policy、3D grounding、online/RL fine-tuning、安全鲁棒性 | 106 | VLA 是机械臂和移动操作的主战场，但它不只是“大模型接动作头”。CCF-A 论文集中在动作表示、diffusion/flow policy、3D grounding、在线/RL 微调和安全鲁棒性上。 |
| WAM / 世界模型 | cascaded WAM、joint WAM、video/latent world model、world model for VLA、world model evaluation | 23 | WAM 将未来世界状态预测和动作生成合在一起，适合放在 agent 规划和低层控制之间。它的价值不是替代所有控制器，而是提供可想象、可验证、可恢复的中间层。 |
| Agentic Planning / 推理规划 | 任务分解、memory、failure monitor、constraint / affordance planning、self-improving planning | 48 | 这一方向强调任务分解、记忆、失败监控、约束/affordance planning 和自改进规划。它最贴近“agent 规划，小模型或传统方法执行”的系统路线。 |
| 本体扩展 / 灵巧操作 | humanoid、bimanual、dexterous hand、tactile/contact-rich、grasp | 30 | 本体扩展决定具身智能是否能从单机械臂走向人形、双臂、灵巧手和触觉接触任务。表中论文体现了动作空间、传感方式和控制目标随本体变化而复杂化。 |
| 轻量化 / 评测 / 数据 | quantization/cache/tokenization、real-time execution、benchmark/dataset、sim2real、safety evaluation | 46 | 这一方向决定能不能真实部署：端侧推理、缓存/量化/action tokenization、实时执行、sim2real、benchmark 和 safety evaluation 都是必需条件。 |

## 各方向详细表格

### VLN / 大范围导航

VLN 关注语言目标、空间地图、记忆、探索和导航决策，核心问题是把自然语言任务变成可执行的大范围移动计划。当前 CCF-A 条目显示，研究正在从离散导航图转向连续环境、物理可执行导航、开放城市环境和低成本端侧导航。

子方向：连续环境 VLN、地图记忆、物理可执行导航、城市/开放环境导航、低成本/端侧导航。

共 34 篇。

| 子方向 | 条目数 | 观察重点 |
| --- | ---: | --- |
| 连续环境 VLN | 17 | 看是否从离散导航图走向连续观察和实时决策。 |
| 地图记忆 | 5 | 看地图表示、语义记忆、缓存和检索机制。 |
| 物理可执行导航 | 5 | 看真实本体约束、动态环境和安全解码。 |
| 城市/开放环境导航 | 4 | 看开放世界、城市、拥挤环境和长期导航。 |
| 低成本/端侧导航 | 3 | 看端侧推理、低成本记忆和数据效率。 |

#### 连续环境 VLN

共 17 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- |
| ICML 2026 | [AdaNav: Adaptive Reasoning with Uncertainty for Vision-Language Navigation](https://icml.cc/virtual/2026/poster/61535) | reasoning | 移动机器人/移动操作 | 提升语言导航的规划和泛化 | [paper](https://icml.cc/virtual/2026/poster/61535) | 用于判断导航是否走向连续、物理和跨场景。 |
| ICML 2026 | [Instruction Decomposition and Action Alignment for Vision-Language Navigation](https://icml.cc/virtual/2026/poster/64780) | VLN policy | 移动机器人/移动操作 | 提升语言导航的规划和泛化 | [paper](https://icml.cc/virtual/2026/poster/64780) | 用于判断导航是否走向连续、物理和跨场景。 |
| ICML 2026 | [TIC-VLA: A Think-in-Control Vision-Language-Action Model for Robot Navigation in Dynamic Environments](https://icml.cc/virtual/2026/poster/65809) | VLA | 移动机器人/移动操作 | 改进视觉语言到动作策略 | [paper](https://icml.cc/virtual/2026/poster/65809) | 用于判断导航是否走向连续、物理和跨场景。 |
| ICML 2026 | [Hydra-Nav: Object Navigation via Adaptive Dual-Process Reasoning](https://icml.cc/virtual/2026/poster/61357) | reasoning | 移动机器人/移动操作 | 解决开放环境导航和决策 | [paper](https://icml.cc/virtual/2026/poster/61357) | 用于判断导航是否走向连续、物理和跨场景。 |
| ICML 2026 | [SafeDec: Constrained Decoding for Safe Autoregressive Generalist Robot Navigation Policies](https://icml.cc/virtual/2026/poster/60775) | autoregressive policy | 移动机器人/移动操作 | 解决开放环境导航和决策 | [paper](https://icml.cc/virtual/2026/poster/60775) | 用于判断导航是否走向连续、物理和跨场景。 |
| CVPR 2026 | [Wanderland: Geometrically Grounded Simulation for Open-World Embodied AI](https://arxiv.org/abs/2511.20620) | planning / RL | 仿真/评测环境 | 从离散导航走向连续环境 | [paper](https://arxiv.org/abs/2511.20620) / [project](https://ai4ce.github.io/wanderland/) | 用于判断导航是否走向连续、物理和跨场景。 |
| CVPR 2026 | [SpaceTools: Tool-Augmented Spatial Reasoning via Double Interactive RL](https://arxiv.org/abs/2512.04069) | planning / reasoning / RL | 移动机器人/导航环境 | 从离散导航走向连续环境 | [paper](https://arxiv.org/abs/2512.04069) / [project](https://spacetools.github.io/) | 用于判断导航是否走向连续、物理和跨场景。 |
| CVPR 2026 | [Dexterous World Models](https://arxiv.org/abs/2512.17907) | world model / planning / RL | 灵巧手/抓取 | 用世界预测支持机器人决策 | [paper](https://arxiv.org/abs/2512.17907) / [project](https://snuvclab.github.io/dwm/) / [code](https://github.com/snuvclab/dwm) | 用于判断导航是否走向连续、物理和跨场景。 |
| NeurIPS 2025 | [Distilling LLM Prior to Flow Model for Generalizable Agent’s Imagination in Object Goal Navigation](https://arxiv.org/abs/2508.09423) | flow matching | 移动机器人/移动操作 | 解决开放环境导航和决策 | [paper](https://arxiv.org/abs/2508.09423) | 用于判断导航是否走向连续、物理和跨场景。 |
| NeurIPS 2025 | TP-MDDN: Task-Preferenced Multi-Demand-Driven Navigation with Autonomous Decision-Making | VLN policy | 移动机器人/移动操作 | 解决开放环境导航和决策 |  | 用于判断导航是否走向连续、物理和跨场景。 |
| NeurIPS 2025 | [Active Test-time Vision-Language Navigation](https://arxiv.org/abs/2506.06630) | VLN policy | 移动机器人/移动操作 | 提升语言导航的规划和泛化 | [paper](https://arxiv.org/abs/2506.06630) | 用于判断导航是否走向连续、物理和跨场景。 |
| NeurIPS 2025 | [Seeing through Uncertainty: Robust Task-Oriented Optimization in Visual Navigation](https://arxiv.org/abs/2510.00441) | VLN policy | 移动机器人/移动操作 | 解决开放环境导航和决策 | [paper](https://arxiv.org/abs/2510.00441) / [project](https://github.com/PyyWill/NeuRO) | 用于判断导航是否走向连续、物理和跨场景。 |
| ICCV 2025 | [P3Nav: A Unified Framework for Embodied Navigation Integrating Perception, Planning, and Prediction](https://arxiv.org/abs/2503.18525) | planning | 移动机器人/移动操作 | 解决开放环境导航和决策 | [paper](https://arxiv.org/abs/2503.18525) | 用于判断导航是否走向连续、物理和跨场景。 |
| ICCV 2025 | [SAME: Learning Generic Language-Guided Visual Navigation with State-Adaptive Mixture of Experts](https://arxiv.org/abs/2412.05552) | VLN policy | 移动机器人/移动操作 | 解决开放环境导航和决策 | [paper](https://arxiv.org/abs/2412.05552) / [project](https://github.com/GengzeZhou/SAME) | 用于判断导航是否走向连续、物理和跨场景。 |
| ICCV 2025 | [Embodied Navigation with Auxiliary Task of Action Description Prediction](https://iccv.thecvf.com/virtual/2025/poster/1984) | VLN policy | 移动机器人/移动操作 | 解决开放环境导航和决策 | [paper](https://iccv.thecvf.com/virtual/2025/poster/1984) | 用于判断导航是否走向连续、物理和跨场景。 |
| ICCV 2025 | [CogNav: Cognitive Process Modeling for Object Goal Navigation with LLMs](https://arxiv.org/abs/2412.10439) | planning | 移动机器人/移动操作 | 解决开放环境导航和决策 | [paper](https://arxiv.org/abs/2412.10439) / [project](https://yhancao.github.io/CogNav/) | 用于判断导航是否走向连续、物理和跨场景。 |
| ICCV 2025 | [MoMa-Kitchen: A 100K+ Benchmark for Affordance-Grounded Last-Mile Navigation in Mobile Manipulation](https://arxiv.org/abs/2503.11081) | affordance | 移动机器人/移动操作 | 提供评测任务和数据基准 | [paper](https://arxiv.org/abs/2503.11081) / [project](https://momakitchen.github.io/) | 用于判断导航是否走向连续、物理和跨场景。 |

#### 地图记忆

共 5 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- |
| ICML 2026 | [MapDream: Task-Driven Map Learning for Vision-Language Navigation](https://icml.cc/virtual/2026/poster/64902) | map/memory | 移动机器人/移动操作 | 提升语言导航的规划和泛化 | [paper](https://icml.cc/virtual/2026/poster/64902) | 用于判断导航是否走向连续、物理和跨场景。 |
| CVPR 2026 | [GLMap: Multi-Scale Gaussian-Language Map for Zero-shot Embodied Navigation and Reasoning](https://arxiv.org/abs/2605.01736) | planning / reasoning / 3D Gaussian | 移动机器人/移动操作 | 解决开放环境导航和决策 | [paper](https://arxiv.org/abs/2605.01736) / [code](https://github.com/sx-zhang/GLMap) | 用于判断导航是否走向连续、物理和跨场景。 |
| NeurIPS 2025 | [EfficientNav: Towards On-Device Object-Goal Navigation with Navigation Map Caching and Retrieval](https://arxiv.org/abs/2510.18546) | map/memory | 移动机器人/移动操作 | 解决开放环境导航和决策 | [paper](https://arxiv.org/abs/2510.18546) | 用于判断导航是否走向连续、物理和跨场景。 |
| ICCV 2025 | [Move to Understand a 3D Scene: Bridging Visual Grounding and Exploration for Efficient and Versatile Embodied Navigation](https://arxiv.org/abs/2507.04047) | 3D representation | 移动机器人/移动操作 | 解决开放环境导航和决策 | [paper](https://arxiv.org/abs/2507.04047) / [project](https://mtu3d.github.io/) | 用于判断导航是否走向连续、物理和跨场景。 |
| ICCV 2025 | [NavQ: Learning a Q-Model for Foresighted Vision-and-Language Navigation](https://iccv.thecvf.com/virtual/2025/poster/944) | map/memory | 移动机器人/移动操作 | 提升语言导航的规划和泛化 | [paper](https://iccv.thecvf.com/virtual/2025/poster/944) | 用于判断导航是否走向连续、物理和跨场景。 |

#### 物理可执行导航

共 5 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- |
| ICML 2026 | [SC$^{2}$-WM: A Self-Correcting World Model with Closed-Loop Feedback for Vision-and-Language Navigation in Continuous Environments](https://icml.cc/virtual/2026/poster/64257) | world model / RL | 移动机器人/移动操作 | 提升语言导航的规划和泛化 | [paper](https://icml.cc/virtual/2026/poster/64257) | 用于判断导航是否走向连续、物理和跨场景。 |
| ICCV 2025 | [Rethinking the Embodied Gap in Vision-and-Language Navigation: A Holistic Study of Physical and Visual Disparities](https://arxiv.org/abs/2507.13019) | embodied navigation | 移动机器人/移动操作 | 提升语言导航的规划和泛化 | [paper](https://arxiv.org/abs/2507.13019) / [project](https://crystalsixone.github.io/vln_pe.github.io/) | 用于判断导航是否走向连续、物理和跨场景。 |
| ICCV 2025 | [NavMorph: A Self-Evolving World Model for Vision-and-Language Navigation in Continuous Environments](https://arxiv.org/abs/2506.23468) | world model / RL | 移动机器人/移动操作 | 提升语言导航的规划和泛化 | [paper](https://arxiv.org/abs/2506.23468) / [project](https://github.com/Feliciaxyao/NavMorph) | 用于判断导航是否走向连续、物理和跨场景。 |
| ICCV 2025 | [3D Gaussian Map with Open-Set Semantic Grouping for Vision-Language Navigation](https://iccv.thecvf.com/virtual/2025/poster/299) | 3D representation / 3D Gaussian | 移动机器人/移动操作 | 提升语言导航的规划和泛化 | [paper](https://iccv.thecvf.com/virtual/2025/poster/299) | 用于判断导航是否走向连续、物理和跨场景。 |
| ICCV 2025 | [monoVLN: Bridging the Observation Gap between Monocular and Panoramic Vision and Language Navigation](https://iccv.thecvf.com/virtual/2025/poster/1792) | embodied navigation | 移动机器人/移动操作 | 解决开放环境导航和决策 | [paper](https://iccv.thecvf.com/virtual/2025/poster/1792) | 用于判断导航是否走向连续、物理和跨场景。 |

#### 城市/开放环境导航

共 4 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- |
| ICML 2026 | [Plan in Sandbox, Navigate in Open Worlds: Learning Physics-Grounded Abstracted Experience for Embodied Navigation](https://icml.cc/virtual/2026/poster/63554) | RL | 移动机器人/移动操作 | 解决开放环境导航和决策 | [paper](https://icml.cc/virtual/2026/poster/63554) | 用于判断导航是否走向连续、物理和跨场景。 |
| NeurIPS 2025 | [C-NAV: Towards Self-Evolving Continual Object Navigation in Open World](https://arxiv.org/abs/2510.20685) | RL | 移动机器人/移动操作 | 解决开放环境导航和决策 | [paper](https://arxiv.org/abs/2510.20685) / [project](https://bigtree765.github.io/C-Nav-project/) | 用于判断导航是否走向连续、物理和跨场景。 |
| NeurIPS 2025 | Synthesizing Photorealistic and Dynamic Urban Environments for Multimodal Robot Navigation and Collaboration | open-world navigation | 无人车/城市环境 | 解决开放环境导航和决策 |  | 用于判断导航是否走向连续、物理和跨场景。 |
| CVPR 2025 | [RoboSense: Large-scale Dataset and Benchmark for Egocentric Robot Perception and Navigation in Crowded and Unstructured Environments](https://arxiv.org/abs/2408.15503) | open-world navigation | 移动机器人/移动操作 | 提供评测任务和数据基准 | [paper](https://arxiv.org/abs/2408.15503) / [project](https://github.com/suhaisheng/RoboSense) | 用于判断导航是否走向连续、物理和跨场景。 |

#### 低成本/端侧导航

共 3 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- |
| NeurIPS 2025 | Aux-Think: Exploring Reasoning Strategies for Data-Efficient Vision-Language Navigation | reasoning | 移动机器人/移动操作 | 提升语言导航的规划和泛化 |  | 用于判断导航是否走向连续、物理和跨场景。 |
| ICCV 2025 | [Harnessing Input-adaptive Inference for Efficient VLN](https://openreview.net/pdf?id=5gptKWnVPF) | efficient navigation | 移动机器人/导航环境 | 提升推理或执行效率 | [paper](https://openreview.net/pdf?id=5gptKWnVPF) | 用于判断导航是否走向连续、物理和跨场景。 |
| ICCV 2025 | [COSMO: Combination of Selective Memorization for Low-cost Vision-and-Language Navigation](https://arxiv.org/abs/2503.24065) | efficient navigation | 移动机器人/移动操作 | 提升语言导航的规划和泛化 | [paper](https://arxiv.org/abs/2503.24065) | 用于判断导航是否走向连续、物理和跨场景。 |

### VLA / 操作策略

VLA 是机械臂和移动操作的主战场，但它不只是“大模型接动作头”。CCF-A 论文集中在动作表示、diffusion/flow policy、3D grounding、在线/RL 微调和安全鲁棒性上。

子方向：generalist VLA、action representation、diffusion/flow policy、3D grounding、online/RL fine-tuning、安全鲁棒性。

共 106 篇。

| 子方向 | 条目数 | 观察重点 |
| --- | ---: | --- |
| generalist VLA | 44 | 看跨任务泛化、真实机器人验证和通用操作能力。 |
| action representation | 15 | 看动作 token、latent action、chunking 和动作空间设计。 |
| diffusion/flow policy | 28 | 看连续动作生成、稳定控制和执行平滑性。 |
| 3D grounding | 14 | 看点云、几何、affordance 与操作定位。 |
| online/RL fine-tuning | 3 | 看在线强化、人在回路和测试时适配。 |
| 安全鲁棒性 | 2 | 看攻击鲁棒、安全对齐和风险暴露。 |

#### generalist VLA

共 44 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- |
| ICML 2026 | [Vision-Language-Action Pretraining from Large-Scale Human Videos](https://icml.cc/virtual/2026/poster/62813) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://icml.cc/virtual/2026/poster/62813) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2026 | [RA-VLA: Retrieval-Augmented VLA for Test-Time Adaptation](https://icml.cc/virtual/2026/poster/60980) | VLA | 机械臂/机器人操作 | 扩展跨任务操作能力 | [paper](https://icml.cc/virtual/2026/poster/60980) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2026 | [A Generalist Pair-wise Progress Critic Model for Vision-Language-Action Robots](https://icml.cc/virtual/2026/poster/62270) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://icml.cc/virtual/2026/poster/62270) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2026 | [Bring My Cup! Personalizing Vision-Language-Action Models with Visual Attentive Prompting](https://icml.cc/virtual/2026/poster/62528) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://icml.cc/virtual/2026/poster/62528) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2026 | [From Abstraction to Instantiation: Learning Behavioral Representation for Vision-Language-Action Model](https://icml.cc/virtual/2026/poster/66596) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://icml.cc/virtual/2026/poster/66596) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2026 | [VLA-ATTC: Adaptive Test-Time Compute for VLA Models with Relative Action Critic Model](https://icml.cc/virtual/2026/poster/61157) | VLA | 机械臂/机器人操作 | 扩展跨任务操作能力 | [paper](https://icml.cc/virtual/2026/poster/61157) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2026 | [SCALE: Self-uncertainty Conditioned Adaptive Looking and Execution for Vision-Language-Action Models](https://icml.cc/virtual/2026/poster/66066) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://icml.cc/virtual/2026/poster/66066) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2026 | [XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations](https://icml.cc/virtual/2026/poster/64826) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://icml.cc/virtual/2026/poster/64826) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2026 | [Escaping the Diversity Trap in Robotic Manipulation via Anchor-Centric Adaptation](https://icml.cc/virtual/2026/poster/66510) | generalist VLA | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://icml.cc/virtual/2026/poster/66510) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2026 | [Embodied Interpretability: Linking Causal Understanding to Generalization in Vision-Language-Action Models](https://icml.cc/virtual/2026/poster/63997) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://icml.cc/virtual/2026/poster/63997) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2026 | [Evo-1: Lightweight Vision-Language-Action Model with Preserved Semantic Alignment](https://arxiv.org/abs/2511.04555) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2511.04555) / [code](https://github.com/MINT-SJTU/Evo-1) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2026 | [HiF-VLA: Hindsight, Insight and Foresight through Motion Representation for Vision-Language-Action Models](https://arxiv.org/abs/2512.09928) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2512.09928) / [project](https://hifvla.github.io/) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2026 | [SaPaVe: Towards Active Perception and Manipulation in Vision-Language-Action Models for Robotics](https://arxiv.org/abs/2603.12193) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2603.12193) / [project](https://lmzpai.github.io/SaPaVe) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2026 | [Contact-Aware Neural Dynamics](https://arxiv.org/abs/2601.12796) | generalist VLA | 触觉/接触操作 | 扩展跨任务操作能力 | [paper](https://arxiv.org/abs/2601.12796) / [project](https://changwei-jing.github.io/neural-physics/) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | [CogVLA: Cognition-Aligned Vision-Language-Action Models via Instruction-Driven Routing & Sparsification](https://arxiv.org/abs/2508.21046) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2508.21046) / [project](https://jiutian-vl.github.io/CogVLA-page/) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | [Exploring the Limits of Vision-Language-Action Manipulation in Cross-task Generalization](https://arxiv.org/abs/2505.15660) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2505.15660) / [project](https://jiaming-zhou.github.io/AGNOSTOS/) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | [Robo2VLM: Improving Visual Question Answering using Large-Scale Robot Manipulation Data](https://arxiv.org/abs/2505.15517) | VLA | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2505.15517) / [project](https://berkeleyautomation.github.io/robo2vlm/) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | 4D-VLA: Spatiotemporal Vision-Language-Action Pretraining with Cross-Scene Calibration | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 |  | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | [Blindfolded Experts Generalize Better: Insights from Robotic Manipulation and Videogames](https://arxiv.org/abs/2510.24194) | VLA | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2510.24194) / [project](https://sites.google.com/view/blindfoldedexperts/home) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | [HiMaCon: Discovering Hierarchical Manipulation Concepts from Unlabeled Multi-Modal Data](https://arxiv.org/abs/2510.11321) | VLA | 仿真/评测环境 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2510.11321) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | [Knowledge Insulating Vision-Language-Action Models: Train Fast, Run Fast, Generalize Better](https://arxiv.org/abs/2505.23705) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2505.23705) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | Diversifying Parallel Ergodic Search: A Signature Kernel Evolution Strategy | generalist VLA | 机械臂/机器人操作 | 扩展跨任务操作能力 |  | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICCV 2025 | [FedVLA: Federated Vision-Language-Action Learning with Dual Gating Mixture-of-Experts for Robotic Manipulation](https://iccv.thecvf.com/virtual/2025/poster/1325) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://iccv.thecvf.com/virtual/2025/poster/1325) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICCV 2025 | [PASG: A Closed-Loop Framework for Automated Geometric Primitive Extraction and Semantic Anchoring in Robotic Manipulation](https://iccv.thecvf.com/virtual/2025/poster/225) | VLA | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://iccv.thecvf.com/virtual/2025/poster/225) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICCV 2025 | [iManip: Skill-Incremental Learning for Robotic Manipulation](https://arxiv.org/abs/2503.07087) | generalist VLA | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2503.07087) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICCV 2025 | [4D Visual Pre-training for Robot Learning](https://iccv.thecvf.com/virtual/2025/poster/972) | generalist VLA | 机械臂/机器人操作 | 扩展跨任务操作能力 | [paper](https://iccv.thecvf.com/virtual/2025/poster/972) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2025 | [Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models](https://arxiv.org/abs/2502.19417) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2502.19417) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2025 | OTTER: A Vision-Language-Action Model with Text-Aware Visual Feature Extraction | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/pdf/2503.03734) / [project](https://ottervla.github.io/) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2025 | UP-VLA: A Unified Understanding and Prediction Model for Embodied Agent | VLA | 机械臂/机器人操作 | 扩展跨任务操作能力 | [paper](https://arxiv.org/abs/2501.18867) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2025 | ELEMENTAL: Interactive Learning from Demonstrations and Vision-Language Models for Reward Design in Robotics | VLA | 机械臂/机器人操作 | 扩展跨任务操作能力 | [paper](https://arxiv.org/abs/2411.18825) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2025 | A Large Recurrent Action Model: xLSTM enables Fast Inference for Robotics Tasks | VLA | 机械臂/机器人操作 | 扩展跨任务操作能力 | [paper](https://arxiv.org/abs/2410.22391) / [project](https://github.com/ml-jku/LRAM) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2025 | Pre-training Auto-regressive Robotic Models with 4D Representations | generalist VLA | 机械臂/机器人操作 | 扩展跨任务操作能力 | [paper](https://arxiv.org/pdf/2502.13142) / [project](https://arm4r.github.io/) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2025 | STAR: Learning Diverse Robot Skill Abstractions through Rotation-Augmented | generalist VLA | 机械臂/机器人操作 | 扩展跨任务操作能力 | [paper](https://www.arxiv.org/pdf/2506.03863) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | [UniAct: Universal Actions For Enhanced Embodied Foundation Models](https://arxiv.org/abs/2501.10105) | VLA | 机械臂/机器人操作 | 扩展跨任务操作能力 | [paper](https://arxiv.org/abs/2501.10105) / [project](https://2toinf.github.io/UniAct/) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | [MoManipVLA: Transferring Vision-language-action Models for General Mobile Manipulation](https://arxiv.org/abs/2503.13446) | VLA | 移动机器人/移动操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2503.13446) / [project](https://gary3410.github.io/momanipVLA/) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | [A Data-Centric Revisit of Pre-Trained Vision Models for Robot Learning](https://arxiv.org/abs/2503.06960) | VLA | 机械臂/机器人操作 | 扩展跨任务操作能力 | [paper](https://arxiv.org/abs/2503.06960) / [project](https://github.com/CVMI-Lab/SlotMIM) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | Think Small, Act Big: Primitive Prompt Learning for Lifelong Robot Manipulation | VLA | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 |  | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | [Phoenix: A Motion-based Self-Reflection Framework for Fine-grained Robotic Action Correction](https://cvpr.thecvf.com/virtual/2025/poster/32789) | VLA | 机械臂/机器人操作 | 扩展跨任务操作能力 | [paper](https://cvpr.thecvf.com/virtual/2025/poster/32789) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | [Mitigating the Human-Robot Domain Discrepancy in Visual Pre-training for Robotic Manipulation](https://arxiv.org/abs/2406.14235) | VLA | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2406.14235) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | Object-Centric Prompt-Driven Vision-Language-Action Model for Robotic Manipulation | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 |  | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | Robotic Visual Instruction | VLA | 机械臂/机器人操作 | 扩展跨任务操作能力 |  | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | [RoboPEPP: Vision-Based Robot Pose and Joint Angle Estimation through Embedding Predictive Pre-Training](https://arxiv.org/abs/2411.17662) | generalist VLA | 机械臂/机器人操作 | 扩展跨任务操作能力 | [paper](https://arxiv.org/abs/2411.17662) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | Two by Two: Learning Cross-Task Pairwise Objects Assembly for Generalizable Robot Manipulation | generalist VLA | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 |  | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | [Prof. Robot: Differentiable Robot Rendering Without Static and Self-Collisions](https://arxiv.org/abs/2503.11269) | generalist VLA | 机械臂/机器人操作 | 扩展跨任务操作能力 | [paper](https://arxiv.org/abs/2503.11269) / [project](https://www.qrcat.cn/prof-robot/) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |

#### action representation

共 15 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- |
| ICML 2026 | [DyGRO-VLA: Cross-Task Scaling of Vision-Language-Action Models via Dynamic Grouped Residual Optimization](https://icml.cc/virtual/2026/poster/60681) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://icml.cc/virtual/2026/poster/60681) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2026 | [LARA: Latent Action Representation Alignment for Vision-Language-Action Models](https://icml.cc/virtual/2026/poster/61232) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://icml.cc/virtual/2026/poster/61232) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2026 | [From Noise to Intent: Anchoring Generative VLA Policies with Residual Bridges](https://icml.cc/virtual/2026/poster/62908) | VLA | 机械臂/机器人操作 | 改进动作表示和解码 | [paper](https://icml.cc/virtual/2026/poster/62908) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2026 | [Demystifying Action Space Design for Robotic Manipulation Policies](https://icml.cc/virtual/2026/poster/65967) | action representation | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://icml.cc/virtual/2026/poster/65967) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2026 | [FocalPolicy: Frequency-Optimized Chunking and Locally Anchored Flow Matching for Coherent Visuomotor Policy](https://icml.cc/virtual/2026/poster/66520) | flow matching | 机械臂/机器人操作 | 改进动作表示和解码 | [paper](https://icml.cc/virtual/2026/poster/66520) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2026 | [GeoMoLa: Geometry-Aware Motion Latents for Learning Robust Manipulation Policies](https://icml.cc/virtual/2026/poster/62176) | action representation | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://icml.cc/virtual/2026/poster/62176) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2026 | [Adaptive Action Chunking at Inference-time for Vision-Language-Action Models](https://arxiv.org/abs/2604.04161) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2604.04161) / [project](https://lance-lot.github.io/adaptive-chunking.github.io/) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2026 | [XL-VLA: Cross-Hand Latent Representation for Vision-Language-Action Models](https://arxiv.org/abs/2603.10158) | VLA | 灵巧手/抓取 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2603.10158) / [project](https://xl-vla.github.io/) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | [Compliant Residual DAgger: Improving Real-World Contact-Rich Manipulation with Human Corrections](https://arxiv.org/abs/2506.16685) | VLA / RL | 触觉/接触操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2506.16685) / [project](https://compliant-residual-dagger.github.io/) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | [Learning Spatial-Aware Manipulation Ordering](https://arxiv.org/abs/2510.25138) | VLA | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2510.25138) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | [PRIMT: Preference-based Reinforcement Learning with Multimodal Feedback and Trajectory Synthesis from Foundation Models](https://arxiv.org/abs/2509.15607) | VLA / RL | 触觉/接触操作 | 改进动作表示和解码 | [paper](https://arxiv.org/abs/2509.15607) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | [Provable Ordering and Continuity in Vision-Language Pretraining for Generalizable Embodied Agents](https://arxiv.org/abs/2502.01218) | VLA | 机械臂/机器人操作 | 改进动作表示和解码 | [paper](https://arxiv.org/abs/2502.01218) / [project](https://actol-pretrain.github.io/) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | [Latent Policy Barrier: Learning Robust Visuomotor Policies by Staying In-Distribution](https://arxiv.org/abs/2508.05941) | action representation | 机械臂/机器人操作 | 改进动作表示和解码 | [paper](https://arxiv.org/abs/2508.05941) / [project](https://project-latentpolicybarrier.github.io/) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICCV 2025 | [Moto: Latent Motion Token as the Bridging Language for Learning Robot Manipulation from Videos](https://arxiv.org/abs/2412.04445) | VLA / action tokenization | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2412.04445) / [project](https://chenyi99.github.io/moto/) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | [Tra-MoE: Learning Trajectory Prediction Model from Multiple Domains for Adaptive Policy Conditioning](https://arxiv.org/abs/2411.14519) | action representation | 机械臂/机器人操作 | 改进动作表示和解码 | [paper](https://arxiv.org/abs/2411.14519) / [project](https://github.com/MCG-NJU/Tra-MoE) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |

#### diffusion/flow policy

共 28 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- |
| ICML 2026 | [Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies](https://icml.cc/virtual/2026/poster/62902) | VLA / diffusion policy | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://icml.cc/virtual/2026/poster/62902) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2026 | [STEP: Warm-Started Visuomotor Policies with Spatiotemporal Consistency Prediction](https://icml.cc/virtual/2026/poster/61717) | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://icml.cc/virtual/2026/poster/61717) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2026 | [Learning Human-Robot Collaboration via Heterogeneous-Agent Lyapunov Policy Optimization](https://icml.cc/virtual/2026/poster/61049) | diffusion/flow policy | 仿真/评测环境 | 提升连续动作生成质量 | [paper](https://icml.cc/virtual/2026/poster/61049) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2026 | [SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models](https://arxiv.org/abs/2511.15605) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2511.15605) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | [AC-DiT: Adaptive Coordination Diffusion Transformer for Mobile Manipulation](https://arxiv.org/abs/2507.01961) | VLA / diffusion policy / diffusion transformer | 移动机器人/移动操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2507.01961) / [project](https://ac-dit.github.io/) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | [PointMapPolicy: Structured Point Cloud Processing for Multi-Modal Imitation Learning](https://arxiv.org/abs/2510.20406) | VLA | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://arxiv.org/abs/2510.20406) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | Emerging Risks from Embodied AI Require Urgent Policy Action | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 |  | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | [Human-assisted Robotic Policy Refinement via Action Preference Optimization](https://arxiv.org/abs/2506.07127) | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://arxiv.org/abs/2506.07127) / [project](https://gewu-lab.github.io/action_preference_optimization/) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | *Hyper-GoalNet*: Goal-Conditioned Manipulation Policy Learning with HyperNetworks | diffusion/flow policy | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 |  | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | [ReinFlow: Fine-tuning Flow Matching Policy with Online Reinforcement Learning](https://arxiv.org/abs/2505.22094) | flow matching / RL | 触觉/接触操作 | 提升连续动作生成质量 | [paper](https://arxiv.org/abs/2505.22094) / [project](https://reinflow.github.io/) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | [A Practical Guide for Incorporating Symmetry in Diffusion Policy](https://arxiv.org/abs/2505.13431) | diffusion policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://arxiv.org/abs/2505.13431) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | [Act to See, See to Act: Diffusion-Driven Perception-Action Interplay for Adaptive Policies](https://arxiv.org/abs/2509.25822) | diffusion policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://arxiv.org/abs/2509.25822) / [project](https://jingwang18.github.io/dp-ag.github.io/) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | [Dynamic Test-Time Compute Scaling in Control Policy: Difficulty-Aware Stochastic Interpolant Policy](https://arxiv.org/abs/2511.20906) | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://arxiv.org/abs/2511.20906) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | [DynaGuide: Steering Diffusion Polices with Active Dynamic Guidance](https://arxiv.org/abs/2506.13922) | diffusion policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://arxiv.org/abs/2506.13922) / [project](https://dynaguide.github.io/) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICCV 2025 | [Dita: Scaling Diffusion Transformer for Generalist Vision-Language-Action Policy](https://arxiv.org/abs/2503.19757) | VLA / diffusion policy / diffusion transformer | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2503.19757) / [project](https://robodita.github.io/) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICCV 2025 | [SD2Actor: Continuous State Decomposition via Diffusion Embeddings for Robotic Manipulation](https://iccv.thecvf.com/virtual/2025/poster/1571) | VLA / diffusion policy | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://iccv.thecvf.com/virtual/2025/poster/1571) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICCV 2025 | [EC-Flow: Enabling Versatile Robotic Manipulation from Action-Unlabeled Videos via Embodiment-Centric Flow](https://arxiv.org/abs/2507.06224) | flow matching | 仿真/评测环境 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2507.06224) / [project](https://ec-flow1.github.io/) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICCV 2025 | [Dense Policy: Bidirectional Autoregressive Learning of Actions](https://arxiv.org/abs/2503.13217) | autoregressive policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://arxiv.org/abs/2503.13217) / [project](https://selen-suyue.github.io/DspNet/) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICCV 2025 | [Spatial-Temporal Aware Visuomotor Diffusion Policy Learning](https://arxiv.org/abs/2507.06710) | diffusion policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://arxiv.org/abs/2507.06710) / [project](https://zhenyangliu.github.io/DP4/) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICCV 2025 | [Wavelet Policy: Lifting Scheme for Policy Learning in Long-Horizon Tasks](https://arxiv.org/abs/2507.04331) | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://arxiv.org/abs/2507.04331) / [project](https://hhuang-code.github.io/wavelet_policy/) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2025 | Flow-based Domain Randomization for Learning and Sequencing Robotic Skills | flow matching | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://arxiv.org/pdf/2502.01800) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2025 | Learning Policy Committees for Effective Personalization in MDPs with Diverse Tasks | diffusion/flow policy | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://arxiv.org/abs/2503.01885) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | [Lift3D Policy: Lifting 2D Foundation Models for Robust 3D Robotic Manipulation](https://arxiv.org/abs/2411.18623) | 3D representation | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2411.18623) / [project](https://lift3d-web.github.io/) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | PDFactor: Learning Tri-Perspective View Policy Diffusion Field for Multi-Task Robotic Manipulation | diffusion policy | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 |  | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | FlowRAM: Grounding Flow Matching Policy with Region-Aware Mamba Framework for Robotic Manipulation | flow matching | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 |  | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | [G3Flow: Generative 3D Semantic Flow for Pose-aware and Generalizable Object Manipulation](https://arxiv.org/abs/2411.18369) | flow matching / 3D representation | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2411.18369) / [project](https://tianxingchen.github.io/G3Flow/) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | [AffordDP: Generalizable Diffusion Policy with Transferable Affordance](https://arxiv.org/abs/2412.03142) | diffusion policy / affordance | 机械臂/机器人操作 | 提升连续动作生成质量 | [paper](https://arxiv.org/abs/2412.03142) / [project](https://afforddp.github.io/) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | Touch2Shape: Touch-Conditioned 3D Diffusion for Shape Exploration and Reconstruction | diffusion policy / 3D representation | 触觉/接触操作 | 提升连续动作生成质量 |  | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |

#### 3D grounding

共 14 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- |
| NeurIPS 2025 | [DynaRend: Learning 3D Dynamics via Masked Future Rendering for Robotic Manipulation](https://arxiv.org/abs/2510.24261) | 3D representation | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2510.24261) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | [Building 3D Representations and Generating Motions From a Single Image via Video-Generation](https://neurips.cc/virtual/2025/loc/san-diego/poster/118141) | 3D representation | 机械臂/机器人操作 | 增强空间理解和操作定位 | [paper](https://neurips.cc/virtual/2025/loc/san-diego/poster/118141) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICCV 2025 | [A0: An Affordance-Aware Hierarchical Model for General Robotic Manipulation](https://arxiv.org/abs/2504.12636) | VLA / affordance | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2504.12636) / [project](https://a-embodied.github.io/A0/) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICCV 2025 | [Learning Precise Affordances from Egocentric Videos for Robotic Manipulation](https://arxiv.org/abs/2408.10123v1) | affordance | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2408.10123v1) / [project](https://reagan1311.github.io/affgrasp) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICCV 2025 | [EmbodiedOcc: Embodied 3D Occupancy Prediction for Vision-based Online Scene Understanding](https://arxiv.org/abs/2412.04380) | 3D representation | 机械臂/机器人操作 | 增强空间理解和操作定位 | [paper](https://arxiv.org/abs/2412.04380) / [project](https://ykiwu.github.io/EmbodiedOcc/) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICCV 2025 | [Embodied Image Captioning: Self-supervised Learning Agents for Spatially Coherent Image Descriptions](https://arxiv.org/abs/2504.08531) | 3D grounding | 机械臂/机器人操作 | 增强空间理解和操作定位 | [paper](https://arxiv.org/abs/2504.08531) / [project](https://hsp-iit.github.io/embodied-captioning/) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2025 | Unifying 2D and 3D Vision-Language Understanding | 3D representation | 机械臂/机器人操作 | 增强空间理解和操作定位 | [paper](https://arxiv.org/abs/2503.10745) / [project](https://univlg.github.io/) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2025 | GAPrompt: Geometry-Aware Point Cloud Prompt for 3D Vision Model | 3D representation | 机械臂/机器人操作 | 增强空间理解和操作定位 | [paper](https://arxiv.org/abs/2505.04119) / [project](https://github.com/zhoujiahuan1991/ICML2025-GAPrompt) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | [SOLAMI: Social Vision-Language-Action Modeling for Immersive Interaction with 3D Autonomous Characters](https://arxiv.org/abs/2412.00174) | VLA / 3D representation | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2412.00174) / [project](https://solami-ai.github.io/) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | [OmniManip: Towards General Robotic Manipulation via Object-Centric Interaction Primitives as Spatial Constraints](https://arxiv.org/abs/2501.03841) | VLA | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2501.03841) / [project](https://omnimanip.github.io/) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | RoboGround: Robot Manipulation with Grounded Vision-Language Priors | VLA | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 |  | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | [3D-MVP: 3D Multiview Pretraining for Robotic Manipulation](https://arxiv.org/abs/2406.18158) | 3D representation | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2406.18158) / [project](https://jasonqsy.github.io/3DMVP/) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | [VidBot: Learning Generalizable 3D Actions from In-the-Wild 2D Human Videos for Zero-Shot Robotic Manipulation](https://arxiv.org/abs/2503.07135) | 3D representation | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2503.07135) / [project](https://hanzhic.github.io/vidbot-project/) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| CVPR 2025 | [AutoURDF: Unsupervised Robot Modeling from Point Cloud Frames Using Cluster Registration](https://arxiv.org/abs/2412.05507) | 3D grounding | 机械臂/机器人操作 | 增强空间理解和操作定位 | [paper](https://arxiv.org/abs/2412.05507) / [project](https://github.com/jl6017/AutoURDF) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |

#### online/RL fine-tuning

共 3 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- |
| ICML 2026 | HIER: Human-in-the-Loop Imagination-Execution Refinement for General Real-World Vision-Language-Action Models | VLA / RL | 机械臂/机器人操作 | 改进视觉语言到动作策略 |  | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| NeurIPS 2025 | Real-World Reinforcement Learning of Active Perception Behaviors | RL | 触觉/接触操作 | 通过在线优化提升策略 |  | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICML 2025 | ReinboT: Amplifying Robot Visual-Language Manipulation with Reinforcement Learning | VLA / RL | 触觉/接触操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2505.07395) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |

#### 安全鲁棒性

共 2 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- |
| NeurIPS 2025 | [BadVLA: Towards Backdoor Attacks on Vision-Language-Action Models via Objective-Decoupled Optimization](https://arxiv.org/abs/2505.16640) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2505.16640) / [project](https://github.com/Zxy-MLlab/BadVLA) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |
| ICCV 2025 | [Exploring the Adversarial Vulnerabilities of Vision-Language-Action Models in Robotics](https://arxiv.org/abs/2411.13587) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2411.13587) / [project](https://vlaattacker.github.io/) | 用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。 |

### WAM / 世界模型

WAM 将未来世界状态预测和动作生成合在一起，适合放在 agent 规划和低层控制之间。它的价值不是替代所有控制器，而是提供可想象、可验证、可恢复的中间层。

子方向：cascaded WAM、joint WAM、video/latent world model、world model for VLA、world model evaluation。

共 23 篇。

| 子方向 | 条目数 | 观察重点 |
| --- | ---: | --- |
| cascaded WAM | 11 | 看先想象后执行的分层链路。 |
| joint WAM | 2 | 看视觉、状态和动作的联合建模。 |
| video/latent world model | 8 | 看未来视频或隐状态预测质量。 |
| world model for VLA | 2 | 看世界模型如何服务 VLA 决策。 |

#### cascaded WAM

共 11 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- |
| ICML 2026 | [Cross-Embodiment Robot Foundation World Models with Latent Actions](https://icml.cc/virtual/2026/poster/63978) | world model / RL | 机械臂/机器人操作 | 用世界预测支持机器人决策 | [paper](https://icml.cc/virtual/2026/poster/63978) | 用于判断世界预测是否能服务规划和动作验证。 |
| ICML 2026 | [DDP-WM: Disentangled Dynamics Prediction for Efficient World Models](https://icml.cc/virtual/2026/poster/62480) | world model / RL | 机械臂/机器人操作 | 用世界预测支持机器人决策 | [paper](https://icml.cc/virtual/2026/poster/62480) | 用于判断世界预测是否能服务规划和动作验证。 |
| ICML 2026 | [RoboFlow4D: A Lightweight Flow World Model Toward Real-Time Flow-Guided Robotic Manipulation](https://icml.cc/virtual/2026/poster/62543) | flow matching / world model / RL | 机械臂/机器人操作 | 用世界预测支持机器人决策 | [paper](https://icml.cc/virtual/2026/poster/62543) | 用于判断世界预测是否能服务规划和动作验证。 |
| ICML 2026 | [Learning Task-Sufficient World Models by Synergizing Agentic Exploration and Structured Modeling](https://icml.cc/virtual/2026/poster/64209) | world model / RL | 机械臂/机器人操作 | 用世界预测支持机器人决策 | [paper](https://icml.cc/virtual/2026/poster/64209) | 用于判断世界预测是否能服务规划和动作验证。 |
| NeurIPS 2025 | [SAMPO: Scale-wise Autoregression with Motion Prompt for Generative World Models](https://arxiv.org/abs/2509.15536) | world model / RL | 机械臂/机器人操作 | 用世界预测支持机器人决策 | [paper](https://arxiv.org/abs/2509.15536) | 用于判断世界预测是否能服务规划和动作验证。 |
| NeurIPS 2025 | [Learning 3D Persistent Embodied World Models](https://arxiv.org/abs/2505.05495) | world model / 3D representation / RL | 机械臂/机器人操作 | 用世界预测支持机器人决策 | [paper](https://arxiv.org/abs/2505.05495) | 用于判断世界预测是否能服务规划和动作验证。 |
| NeurIPS 2025 | [OSVI-WM: One-Shot Visual Imitation for Unseen Tasks using World-Model-Guided Trajectory Generation](https://arxiv.org/abs/2505.20425) | world model / RL | 机械臂/机器人操作 | 先预测未来再推导动作 | [paper](https://arxiv.org/abs/2505.20425) | 用于判断世界预测是否能服务规划和动作验证。 |
| ICCV 2025 | [IRASim: A Fine-Grained World Model for Robot Manipulation](https://arxiv.org/abs/2406.14540) | world model / RL | 机械臂/机器人操作 | 用世界预测支持机器人决策 | [paper](https://arxiv.org/abs/2406.14540) / [project](https://gen-irasim.github.io/) | 用于判断世界预测是否能服务规划和动作验证。 |
| ICCV 2025 | [GWM: Towards Scalable Gaussian World Models for Robotic Manipulation](https://ziweiwangthu.github.io/data/GWM.pdf) | world model / 3D Gaussian / RL | 仿真/评测环境 | 用世界预测支持机器人决策 | [paper](https://ziweiwangthu.github.io/data/GWM.pdf) / [project](https://gaussian-world-model.github.io/) | 用于判断世界预测是否能服务规划和动作验证。 |
| ICCV 2025 | [DyWA: Dynamics-adaptive World Action Model for Generalizable Non-prehensile Manipulation](https://arxiv.org/abs/2503.16806) | world model / RL | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2503.16806) / [project](https://pku-epic.github.io/DyWA/) | 用于判断世界预测是否能服务规划和动作验证。 |
| ICCV 2025 | [Learning 4D Embodied World Models](https://openreview.net/pdf?id=mnwlhvmKMN) | world model / RL | 机械臂/机器人操作 | 用世界预测支持机器人决策 | [paper](https://openreview.net/pdf?id=mnwlhvmKMN) | 用于判断世界预测是否能服务规划和动作验证。 |

#### joint WAM

共 2 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- |
| ICML 2026 | [Dual-Stream Diffusion for World-Model Augmented Vision-Language-Action Model](https://icml.cc/virtual/2026/poster/64447) | VLA / diffusion policy / world model | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://icml.cc/virtual/2026/poster/64447) | 用于判断世界预测是否能服务规划和动作验证。 |
| ICCV 2025 | [Diffusion-Based Imaginative Coordination for Bimanual Manipulation](https://arxiv.org/abs/2507.11296) | diffusion policy / world model / RL | 双臂机器人 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2507.11296) | 用于判断世界预测是否能服务规划和动作验证。 |

#### video/latent world model

共 8 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- |
| ICML 2026 | [DreamDojo: A Real-Time Robot World Model from Large-Scale Human Videos](https://icml.cc/virtual/2026/poster/65193) | world model / RL | 机械臂/机器人操作 | 用世界预测支持机器人决策 | [paper](https://icml.cc/virtual/2026/poster/65193) | 用于判断世界预测是否能服务规划和动作验证。 |
| ICML 2026 | [From Imagined Futures to Executable Actions: Mixture of Latent Actions for Robot Manipulation](https://icml.cc/virtual/2026/poster/66091) | world model / RL | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://icml.cc/virtual/2026/poster/66091) | 用于判断世界预测是否能服务规划和动作验证。 |
| NeurIPS 2025 | VideoVLA: Video Generators Can Be Generalizable Robot Manipulators | VLA | 机械臂/机器人操作 | 从视频或隐空间预测未来 |  | 用于判断世界预测是否能服务规划和动作验证。 |
| NeurIPS 2025 | [EnerVerse: Envisioning Embodied Future Space for Robotics Manipulation](https://arxiv.org/abs/2501.01895) | VLA | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2501.01895) | 用于判断世界预测是否能服务规划和动作验证。 |
| NeurIPS 2025 | [DreamVLA: A Vision-Language-Action Model Dreamed with Comprehensive World Knowledge](https://arxiv.org/abs/2507.04447) | VLA / RL | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2507.04447) / [project](https://zhangwenyao1.github.io/DreamVLA/index.html) | 用于判断世界预测是否能服务规划和动作验证。 |
| ICML 2025 | Video Prediction Policy: A Generalist Robot Policy with Predictive Visual Representations | video/latent world model | 机械臂/机器人操作 | 从视频或隐空间预测未来 | [paper](https://arxiv.org/abs/2412.14803) / [project](https://video-prediction-policy.github.io/) | 用于判断世界预测是否能服务规划和动作验证。 |
| CVPR 2025 | [TASTE-Rob: Advancing Video Generation of Task-Oriented Hand-Object Interaction for Generalizable Robotic Manipulation](https://arxiv.org/abs/2503.11423) | video/latent world model | 灵巧手/抓取 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2503.11423) | 用于判断世界预测是否能服务规划和动作验证。 |
| CVPR 2025 | [GraphMimic: Graph-to-Graphs Generative Modeling from Videos for Policy Learning](https://cvpr.thecvf.com/virtual/2025/poster/34942) | video/latent world model | 机械臂/机器人操作 | 从视频或隐空间预测未来 | [paper](https://cvpr.thecvf.com/virtual/2025/poster/34942) | 用于判断世界预测是否能服务规划和动作验证。 |

#### world model for VLA

共 2 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- |
| ICML 2026 | [VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model](https://icml.cc/virtual/2026/poster/66169) | VLA / world model / RL | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://icml.cc/virtual/2026/poster/66169) | 用于判断世界预测是否能服务规划和动作验证。 |
| CVPR 2026 | [CoWVLA: Chain of World: World Model Thinking in Latent Motion](https://arxiv.org/abs/2603.03195) | VLA / world model / RL | 机械臂/机器人操作 | 用世界预测支持机器人决策 | [paper](https://arxiv.org/abs/2603.03195) / [project](https://fx-hit.github.io/cowvla-io/) | 用于判断世界预测是否能服务规划和动作验证。 |

### Agentic Planning / 推理规划

这一方向强调任务分解、记忆、失败监控、约束/affordance planning 和自改进规划。它最贴近“agent 规划，小模型或传统方法执行”的系统路线。

子方向：任务分解、memory、failure monitor、constraint / affordance planning、self-improving planning。

共 48 篇。

| 子方向 | 条目数 | 观察重点 |
| --- | ---: | --- |
| 任务分解 | 8 | 看高层指令如何拆成可执行步骤。 |
| memory | 6 | 看长期记忆、经验复用和环境状态保持。 |
| failure monitor | 5 | 看失败检测、恢复和闭环修正。 |
| constraint / affordance planning | 2 | 看约束、可供性和物理可执行性。 |
| self-improving planning | 27 | 看自我改进、测试时优化和经验沉淀。 |

#### 任务分解

共 8 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- |
| ICML 2026 | [TapSampling: Inference-Time Sampling with a Task-Progress-Understanding Verifier for Robotic Manipulation](https://icml.cc/virtual/2026/poster/60500) | planning / reasoning | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://icml.cc/virtual/2026/poster/60500) | 用于评估高层规划是否能落到可执行动作。 |
| ICML 2026 | [Decompose and Recompose: Reasoning New Skills from Existing Abilities for Cross-Task Robotic Manipulation](https://icml.cc/virtual/2026/poster/63250) | planning / reasoning | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://icml.cc/virtual/2026/poster/63250) | 用于评估高层规划是否能落到可执行动作。 |
| NeurIPS 2025 | [SAFE: Multitask Failure Detection for Vision-Language-Action Models](https://arxiv.org/abs/2506.09937) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2506.09937) / [project](https://vla-safe.github.io/) | 用于评估高层规划是否能落到可执行动作。 |
| NeurIPS 2025 | [Towards Reliable Code-as-Policies: A Neuro-Symbolic Framework for Embodied Task Planning](https://arxiv.org/abs/2510.21302) | planning / reasoning | 机械臂/机器人操作 | 把高层目标转为可执行步骤 | [paper](https://arxiv.org/abs/2510.21302) | 用于评估高层规划是否能落到可执行动作。 |
| NeurIPS 2025 | [RDD: Retrieval-Based Demonstration Decomposer for Planner Alignment in Long-Horizon Tasks](https://arxiv.org/abs/2510.14968) | agent planner / planning / reasoning | 机械臂/机器人操作 | 把高层目标转为可执行步骤 | [paper](https://arxiv.org/abs/2510.14968) / [project](https://rdd-neurips.github.io/) | 用于评估高层规划是否能落到可执行动作。 |
| NeurIPS 2025 | [UniDomain: Pretraining a Unified PDDL Domain from Real-World Demonstrations for Generalizable Robot Task Planning](https://arxiv.org/abs/2507.21545) | planning / reasoning / RL | 机械臂/机器人操作 | 把高层目标转为可执行步骤 | [paper](https://arxiv.org/abs/2507.21545) | 用于评估高层规划是否能落到可执行动作。 |
| NeurIPS 2025 | [World-aware Planning Narratives Enhance Large Vision-Language Model Planner](https://arxiv.org/abs/2506.21230) | agent planner / planning / RL | 机械臂/机器人操作 | 把高层目标转为可执行步骤 | [paper](https://arxiv.org/abs/2506.21230) | 用于评估高层规划是否能落到可执行动作。 |
| ICCV 2025 | [VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics Manipulation with Long-Horizon Reasoning Tasks](https://arxiv.org/abs/2412.18194) | VLA / reasoning | 仿真/评测环境 | 提供评测任务和数据基准 | [paper](https://arxiv.org/abs/2412.18194) / [project](https://iranqin.github.io/robofactory/) | 用于评估高层规划是否能落到可执行动作。 |

#### memory

共 6 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- |
| ICML 2026 | [HiMe: Hierarchical Embodied Memory for Long-Horizon Vision-Language-Action Control](https://icml.cc/virtual/2026/poster/60897) | VLA / memory | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://icml.cc/virtual/2026/poster/60897) | 用于评估高层规划是否能落到可执行动作。 |
| ICML 2026 | [Spatial Memory for Out-of-Vision Manipulation in Vision-Language-Action](https://icml.cc/virtual/2026/poster/66214) | VLA / memory | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://icml.cc/virtual/2026/poster/66214) | 用于评估高层规划是否能落到可执行动作。 |
| CVPR 2026 | [OptimusVLA: Global Prior Meets Local Consistency: Dual-Memory Augmented Vision-Language-Action Model for Efficient Robotic Manipulation](https://arxiv.org/abs/2602.20200) | VLA / memory | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2602.20200) / [code](https://github.com/JiuTian-VL/OptimusVLA) | 用于评估高层规划是否能落到可执行动作。 |
| ICCV 2025 | [Embodied VideoAgent: Persistent Memory from Egocentric Videos and Embodied Sensors Enables Dynamic Scene Understanding](https://arxiv.org/abs/2501.00358) | VLA / memory | 机械臂/机器人操作 | 增强长期任务记忆 | [paper](https://arxiv.org/abs/2501.00358) / [project](https://embodied-videoagent.github.io/) | 用于评估高层规划是否能落到可执行动作。 |
| ICCV 2025 | [Towards Long-Horizon Vision-Language-Action System: Reasoning, Acting and Memory](https://iccv.thecvf.com/virtual/2025/poster/1915) | VLA / memory / reasoning | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://iccv.thecvf.com/virtual/2025/poster/1915) | 用于评估高层规划是否能落到可执行动作。 |
| ICML 2025 | SAM2Act:Integrating Visual Foundation Model with A Memory Architecture for Robotic Manipulation | memory | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2501.18564) | 用于评估高层规划是否能落到可执行动作。 |

#### failure monitor

共 5 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- |
| ICML 2026 | [Sentinel-VLA: A Metacognitive VLA Model with Active Status Monitoring for Dynamic Reasoning and Error Recovery](https://icml.cc/virtual/2026/poster/61750) | VLA / reasoning | 机械臂/机器人操作 | 发现并修复执行失败 | [paper](https://icml.cc/virtual/2026/poster/61750) | 用于评估高层规划是否能落到可执行动作。 |
| ICML 2026 | [NeurVLA: Unleashing Failure-Handling Capability of Vision-Language-Action Models via Neural-Symbolic Reasoning](https://icml.cc/virtual/2026/poster/63650) | VLA / reasoning | 灵巧手/抓取 | 改进视觉语言到动作策略 | [paper](https://icml.cc/virtual/2026/poster/63650) | 用于评估高层规划是否能落到可执行动作。 |
| ICML 2026 | [Can VLMs Diagnose and Recover from VLA Manipulation Faults?](https://icml.cc/virtual/2026/poster/64203) | VLA / planning / reasoning | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://icml.cc/virtual/2026/poster/64203) | 用于评估高层规划是否能落到可执行动作。 |
| NeurIPS 2025 | [Failure Prediction at Runtime for Generative Robot Policies](https://arxiv.org/abs/2510.09459) | failure monitor | 机械臂/机器人操作 | 检测或恢复执行失败 | [paper](https://arxiv.org/abs/2510.09459) | 用于评估高层规划是否能落到可执行动作。 |
| CVPR 2025 | [Code-as-Monitor: Constraint-aware Visual Programming for Reactive and Proactive Robotic Failure Detection](https://arxiv.org/abs/2412.04455) | planning / reasoning | 机械臂/机器人操作 | 检测或恢复执行失败 | [paper](https://arxiv.org/abs/2412.04455) / [project](https://zhoues.github.io/Code-as-Monitor/) | 用于评估高层规划是否能落到可执行动作。 |

#### constraint / affordance planning

共 2 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- |
| NeurIPS 2025 | InstructFlow: Adaptive Symbolic Constraint-Guided Code Generation for Long-Horizon Planning | flow matching / planning / reasoning | 机械臂/机器人操作 | 约束动作可执行性 |  | 用于评估高层规划是否能落到可执行动作。 |
| ICCV 2025 | [CoA-VLA: Improving Vision-Language-Action Models via Visual-Text Chain-of-Affordance](https://iccv.thecvf.com/virtual/2025/poster/542) | VLA / affordance | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://iccv.thecvf.com/virtual/2025/poster/542) | 用于评估高层规划是否能落到可执行动作。 |

#### self-improving planning

共 27 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- |
| ICML 2026 | [HALO: A Unified Vision-Language-Action Model for Embodied Multimodal Chain-of-Thought Reasoning](https://icml.cc/virtual/2026/poster/61922) | VLA / reasoning | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://icml.cc/virtual/2026/poster/61922) | 用于评估高层规划是否能落到可执行动作。 |
| ICML 2026 | [Latent Reasoning VLA: Latent Thinking and Prediction for Vision-Language-Action Models](https://icml.cc/virtual/2026/poster/64290) | VLA / reasoning | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://icml.cc/virtual/2026/poster/64290) | 用于评估高层规划是否能落到可执行动作。 |
| ICML 2026 | [LaST0: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model](https://icml.cc/virtual/2026/poster/61887) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://icml.cc/virtual/2026/poster/61887) | 用于评估高层规划是否能落到可执行动作。 |
| ICML 2026 | [LAGEA: Language Guided Embodied Agents for Robotic Manipulation](https://icml.cc/virtual/2026/poster/60801) | planning / reasoning | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://icml.cc/virtual/2026/poster/60801) | 用于评估高层规划是否能落到可执行动作。 |
| ICML 2026 | [Drift is a Sampling Error: SNR-Aware Power Distributions for Long-Horizon Robotic Planning](https://icml.cc/virtual/2026/poster/64055) | planning / reasoning | 机械臂/机器人操作 | 通过反馈自我改进规划 | [paper](https://icml.cc/virtual/2026/poster/64055) | 用于评估高层规划是否能落到可执行动作。 |
| CVPR 2026 | [ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models](https://arxiv.org/abs/2601.11404) | VLA | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2601.11404) / [code](https://github.com/AgibotTech/ACoT-VLA) | 用于评估高层规划是否能落到可执行动作。 |
| CVPR 2026 | [Fast-ThinkAct: Efficient Vision-Language-Action Reasoning via Verbalizable Latent Planning](https://arxiv.org/abs/2601.09708) | VLA / planning / reasoning | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2601.09708) / [project](https://research.nvidia.com/labs/twn/publication/cvpr_2026_fastthinkact/) | 用于评估高层规划是否能落到可执行动作。 |
| NeurIPS 2025 | [Fast-in-Slow: A Dual-System VLA Model Unifying Fast Manipulation within Slow Reasoning](https://arxiv.org/abs/2506.01953) | VLA / reasoning | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2506.01953) / [project](https://fast-in-slow.github.io/) | 用于评估高层规划是否能落到可执行动作。 |
| NeurIPS 2025 | [ChatVLA-2: Vision-Language-Action Model with Open-World Reasoning](https://arxiv.org/abs/2505.21906) | VLA / reasoning / RL | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2505.21906) / [project](https://chatvla-2.github.io/) | 用于评估高层规划是否能落到可执行动作。 |
| NeurIPS 2025 | [VLA-OS: Structuring and Dissecting Planning Representations and Paradigms in Vision-Language-Action Models](https://arxiv.org/abs/2506.17561) | VLA / planning | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2506.17561) / [project](https://nus-lins-lab.github.io/vlaos/) | 用于评估高层规划是否能落到可执行动作。 |
| NeurIPS 2025 | [ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning](https://arxiv.org/abs/2507.16815) | VLA / planning / reasoning | 触觉/接触操作 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2507.16815) / [project](https://jasper0314-huang.github.io/thinkact-vla/) | 用于评估高层规划是否能落到可执行动作。 |
| NeurIPS 2025 | [Self-Improving Embodied Foundation Models](https://arxiv.org/abs/2509.15155) | VLA | 机械臂/机器人操作 | 通过反馈自我改进规划 | [paper](https://arxiv.org/abs/2509.15155) / [project](https://self-improving-efms.github.io/) | 用于评估高层规划是否能落到可执行动作。 |
| NeurIPS 2025 | [Chain-of-Action: Trajectory Autoregressive Modeling for Robotic Manipulation](https://arxiv.org/abs/2506.09990) | VLA / autoregressive policy | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2506.09990) / [project](https://chain-of-action.github.io/) | 用于评估高层规划是否能落到可执行动作。 |
| NeurIPS 2025 | [Towards Reliable LLM-based Robots Planning via Combined Uncertainty Estimation](https://arxiv.org/abs/2510.08044) | planning / reasoning | 机械臂/机器人操作 | 通过反馈自我改进规划 | [paper](https://arxiv.org/abs/2510.08044) | 用于评估高层规划是否能落到可执行动作。 |
| NeurIPS 2025 | [HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning](https://arxiv.org/abs/2507.00833) | reasoning | 人形机器人 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2507.00833) | 用于评估高层规划是否能落到可执行动作。 |
| NeurIPS 2025 | [DexFlyWheel: A Scalable and Self-improving Data Generation Framework for Dexterous Manipulation](https://arxiv.org/abs/2509.23829) | self-improving planner | 灵巧手/抓取 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2509.23829) / [project](https://dexflywheel.github.io/) | 用于评估高层规划是否能落到可执行动作。 |
| ICCV 2025 | [Adaptive Articulated Object Manipulation On The Fly with Foundation Model Reasoning and Part Grounding](https://arxiv.org/abs/2507.18276) | planning / reasoning | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2507.18276) | 用于评估高层规划是否能落到可执行动作。 |
| ICCV 2025 | [RoBridge: A Hierarchical Architecture Bridging Cognition and Execution for General Robotic Manipulation](https://arxiv.org/abs/2505.01709) | planning | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2505.01709) / [project](https://abliao.github.io/RoBridge/) | 用于评估高层规划是否能落到可执行动作。 |
| ICML 2025 | Efficient Robotic Policy Learning via Latent Space Backward Planning | planning / reasoning | 机械臂/机器人操作 | 提升推理或执行效率 | [paper](https://arxiv.org/abs/2505.06861) / [project](https://lbp-authors.github.io/) | 用于评估高层规划是否能落到可执行动作。 |
| ICML 2025 | Closed-Loop Long-Horizon Robotic Planning via Equilibrium Sequence Modeling | planning / reasoning | 机械臂/机器人操作 | 通过反馈自我改进规划 | [paper](https://arxiv.org/pdf/2410.01440) / [project](https://github.com/Singularity0104/equilibrium-planner) | 用于评估高层规划是否能落到可执行动作。 |
| ICML 2025 | WOMD-Reasoning: A Large-Scale Dataset for Interaction Reasoning in Driving | reasoning | 仿真/评测环境 | 提供训练/评测数据资源 | [paper](https://arxiv.org/abs/2407.04281) / [project](https://github.com/yhli123/WOMD-Reasoning) | 用于评估高层规划是否能落到可执行动作。 |
| CVPR 2025 | [CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models](https://cvpr.thecvf.com/virtual/2025/poster/33233) | VLA / reasoning | 机械臂/机器人操作 | 改进视觉语言到动作策略 | [paper](https://cvpr.thecvf.com/virtual/2025/poster/33233) | 用于评估高层规划是否能落到可执行动作。 |
| CVPR 2025 | [DexHandDiff: Interaction-aware Diffusion Planning for Adaptive Dexterous Manipulation](https://arxiv.org/abs/2411.18562) | diffusion policy / planning | 灵巧手/抓取 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2411.18562) / [project](https://dexdiffuser.github.io/) | 用于评估高层规划是否能落到可执行动作。 |
| CVPR 2025 | [RoboBrain: A Unified Brain Model for Robotic Manipulation from Abstract to Concrete](https://arxiv.org/abs/2502.21257) | planning / reasoning | 机械臂/机器人操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2502.21257) | 用于评估高层规划是否能落到可执行动作。 |
| CVPR 2025 | [PhysVLM: Enabling Visual Language Models to Understand Robotic Physical Reachability](https://arxiv.org/abs/2503.08481) | planning / reasoning | 机械臂/机器人操作 | 通过反馈自我改进规划 | [paper](https://arxiv.org/abs/2503.08481) | 用于评估高层规划是否能落到可执行动作。 |
| CVPR 2025 | [RoboSpatial: Teaching Spatial Understanding to 2D and 3D Vision-Language Models for Robotics](https://arxiv.org/abs/2411.16537) | planning / reasoning / 3D representation | 机械臂/机器人操作 | 通过反馈自我改进规划 | [paper](https://arxiv.org/abs/2411.16537) | 用于评估高层规划是否能落到可执行动作。 |
| CVPR 2025 | Tartan IMU: A Light Foundation Model for Inertial Positioning in Robotics | planning / reasoning | 机械臂/机器人操作 | 通过反馈自我改进规划 |  | 用于评估高层规划是否能落到可执行动作。 |

### 本体扩展 / 灵巧操作

本体扩展决定具身智能是否能从单机械臂走向人形、双臂、灵巧手和触觉接触任务。表中论文体现了动作空间、传感方式和控制目标随本体变化而复杂化。

子方向：humanoid、bimanual、dexterous hand、tactile/contact-rich、grasp。

共 30 篇。

| 子方向 | 条目数 | 观察重点 |
| --- | ---: | --- |
| humanoid | 7 | 看全身控制、移动操作和人形本体泛化。 |
| bimanual | 8 | 看双臂协同、长程操作和协调控制。 |
| dexterous hand | 8 | 看灵巧手动作空间和抓取迁移。 |
| tactile/contact-rich | 7 | 看触觉、接触动力学和精细反馈。 |

#### humanoid

共 7 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- |
| ICML 2026 | [Scalable and General Whole-Body Control for Cross-Humanoid Locomotion](https://icml.cc/virtual/2026/poster/62003) | humanoid control | 人形机器人 | 提升人形机器人控制 | [paper](https://icml.cc/virtual/2026/poster/62003) | 用于观察本体差异如何改变控制和数据需求。 |
| ICML 2026 | [Learning Transferable Interaction Primitives from Game Videos for Humanoids](https://icml.cc/virtual/2026/poster/65120) | humanoid control | 人形机器人 | 提升人形机器人控制 | [paper](https://icml.cc/virtual/2026/poster/65120) | 用于观察本体差异如何改变控制和数据需求。 |
| CVPR 2026 | [VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation](https://arxiv.org/abs/2511.15200) | humanoid control | 人形机器人 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2511.15200) / [project](https://viral-humanoid.github.io/) | 用于观察本体差异如何改变控制和数据需求。 |
| NeurIPS 2025 | [Adversarial Locomotion and Motion Imitation for Humanoid Policy Learning](https://arxiv.org/abs/2504.14305) | humanoid control | 人形机器人 | 提升人形机器人控制 | [paper](https://arxiv.org/abs/2504.14305) / [project](https://almi-humanoid.github.io/) | 用于观察本体差异如何改变控制和数据需求。 |
| NeurIPS 2025 | [From Experts to a Generalist: Toward General Whole-Body Control for Humanoid Robots](https://arxiv.org/abs/2506.12779) | humanoid control | 人形机器人 | 提升人形机器人控制 | [paper](https://arxiv.org/abs/2506.12779) / [project](https://beingbeyond.github.io/BumbleBee/) | 用于观察本体差异如何改变控制和数据需求。 |
| NeurIPS 2025 | [KungfuBot: Physics-Based Humanoid Whole-Body Control for Learning Highly-Dynamic Skills](https://kungfubot.github.io/) | humanoid control | 人形机器人 | 提升人形机器人控制 | [paper](https://kungfubot.github.io/) / [project](https://arxiv.org/abs/2506.12851) | 用于观察本体差异如何改变控制和数据需求。 |
| CVPR 2025 | [Let Humanoid Robots Go Hiking! Integrative Skill Development over Complex Trails](https://cvpr.thecvf.com/virtual/2025/poster/34565) | humanoid control | 人形机器人 | 提升人形机器人控制 | [paper](https://cvpr.thecvf.com/virtual/2025/poster/34565) / [project](https://lego-h-humanoidrobothiking.github.io/) | 用于观察本体差异如何改变控制和数据需求。 |

#### bimanual

共 8 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- |
| ICML 2026 | [DexMachina: Functional Retargeting for Bimanual Dexterous Manipulation](https://icml.cc/virtual/2026/poster/63277) | bimanual policy | 双臂机器人 | 提升机器人操作泛化和稳定性 | [paper](https://icml.cc/virtual/2026/poster/63277) | 用于观察本体差异如何改变控制和数据需求。 |
| ICML 2026 | [DECO: Decoupled Multimodal Diffusion Transformer for Bimanual Dexterous Manipulation with a Plugin Tactile Adapter](https://icml.cc/virtual/2026/poster/66358) | diffusion policy / tactile policy / diffusion transformer | 双臂机器人 | 提升机器人操作泛化和稳定性 | [paper](https://icml.cc/virtual/2026/poster/66358) | 用于观察本体差异如何改变控制和数据需求。 |
| ICML 2026 | [RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation](https://icml.cc/virtual/2026/poster/62192) | bimanual policy | 双臂机器人 | 提供评测任务和数据基准 | [paper](https://icml.cc/virtual/2026/poster/62192) | 用于观察本体差异如何改变控制和数据需求。 |
| ICCV 2025 | [Rethinking Bimanual Robotic Manipulation: Learning with Decoupled Interaction Framework](https://arxiv.org/abs/2503.09186) | bimanual policy | 双臂机器人 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2503.09186) | 用于观察本体差异如何改变控制和数据需求。 |
| ICCV 2025 | [AnyBimanual: Transferring Unimanual Policy for General Bimanual Manipulation](https://arxiv.org/abs/2412.06779) | bimanual policy | 双臂机器人 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2412.06779) / [project](https://anybimanual.github.io/) | 用于观察本体差异如何改变控制和数据需求。 |
| ICCV 2025 | [DexH2R: A Benchmark for Dynamic Dexterous Grasping in Human-to-Robot Handover](https://arxiv.org/abs/2506.23152) | bimanual policy | 灵巧手/抓取 | 提供评测任务和数据基准 | [paper](https://arxiv.org/abs/2506.23152) / [project](https://dexh2r.github.io/) | 用于观察本体差异如何改变控制和数据需求。 |
| CVPR 2025 | [KStar Diffuser: Spatial-Temporal Graph Diffusion Policy with Kinematics Modeling for Bimanual Robotic Manipulation](https://arxiv.org/abs/2503.10743) | diffusion policy | 双臂机器人 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2503.10743) | 用于观察本体差异如何改变控制和数据需求。 |
| CVPR 2025 | [MobileH2R: Learning Generalizable Human to Mobile Robot Handover Exclusively from Scalable and Diverse Synthetic Data](https://arxiv.org/abs/2501.04595) | bimanual policy | 灵巧手/抓取 | 协调双臂协作操作 | [paper](https://arxiv.org/abs/2501.04595) | 用于观察本体差异如何改变控制和数据需求。 |

#### dexterous hand

共 8 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- |
| CVPR 2026 | [UniDex: A Robot Foundation Suite for Universal Dexterous Hand Control from Egocentric Human Videos](https://arxiv.org/abs/2603.22264) | VLA | 灵巧手/抓取 | 提升灵巧操作能力 | [paper](https://arxiv.org/abs/2603.22264) / [project](https://unidex-ai.github.io/) / [code](https://github.com/unidex-ai/UniDex) | 用于观察本体差异如何改变控制和数据需求。 |
| NeurIPS 2025 | [Contact Map Transfer with Conditional Diffusion Model for Generalizable Dexterous Grasp Generation](https://arxiv.org/pdf/2511.01276) | diffusion policy | 灵巧手/抓取 | 提升灵巧操作能力 | [paper](https://arxiv.org/pdf/2511.01276) / [project](https://cmtdiffusion.github.io/) | 用于观察本体差异如何改变控制和数据需求。 |
| NeurIPS 2025 | [Grasp2Grasp: Vision-Based Dexterous Grasp Translation via Schrödinger Bridges](https://arxiv.org/abs/2506.02489) | dexterous manipulation | 灵巧手/抓取 | 提升灵巧操作能力 | [paper](https://arxiv.org/abs/2506.02489) / [project](https://grasp2grasp.github.io/) | 用于观察本体差异如何改变控制和数据需求。 |
| NeurIPS 2025 | [Scaffolding Dexterous Manipulation with Vision-Language Models](https://arxiv.org/abs/2506.19212) | dexterous manipulation | 灵巧手/抓取 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2506.19212) / [project](https://sites.google.com/view/dexterous-vlm-scaffolding) | 用于观察本体差异如何改变控制和数据需求。 |
| NeurIPS 2025 | [DexGarmentLab: Dexterous Garment Manipulation Environment with Generalizable Policy](https://arxiv.org/abs/2505.11032) | dexterous manipulation | 灵巧手/抓取 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2505.11032) / [project](https://wayrise.github.io/DexGarmentLab/) | 用于观察本体差异如何改变控制和数据需求。 |
| CVPR 2025 | [UniGraspTransformer: Simplified Policy Distillation for Scalable Dexterous Robotic Grasping](https://arxiv.org/abs/2412.02699) | dexterous manipulation | 灵巧手/抓取 | 提升灵巧操作能力 | [paper](https://arxiv.org/abs/2412.02699) / [project](https://dexhand.github.io/UniGraspTransformer/) | 用于观察本体差异如何改变控制和数据需求。 |
| CVPR 2025 | [DexGrasp Anything: Towards Universal Robotic Dexterous Grasping with Physics Awareness](https://arxiv.org/abs/2503.08257) | dexterous manipulation | 灵巧手/抓取 | 提升灵巧操作能力 | [paper](https://arxiv.org/abs/2503.08257) / [project](https://github.com/4DVLab/DexGrasp-Anything) | 用于观察本体差异如何改变控制和数据需求。 |
| CVPR 2025 | [ZeroGrasp: Zero-Shot Shape Reconstruction Enabled Robotic Grasping](https://cvpr.thecvf.com/virtual/2025/poster/32440) | dexterous manipulation | 灵巧手/抓取 | 处理高自由度灵巧操作 | [paper](https://cvpr.thecvf.com/virtual/2025/poster/32440) | 用于观察本体差异如何改变控制和数据需求。 |

#### tactile/contact-rich

共 7 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- |
| ICML 2026 | [Cross-Tactile Sensor Representation Learning](https://icml.cc/virtual/2026/poster/66793) | tactile policy | 触觉/接触操作 | 引入触觉提升接触操作 | [paper](https://icml.cc/virtual/2026/poster/66793) | 用于观察本体差异如何改变控制和数据需求。 |
| ICML 2026 | [Tabero: Learning Gentle Manipulation with Closed-Loop Force Feedback from Vision, Touch, and Language](https://icml.cc/virtual/2026/poster/65669) | tactile policy | 触觉/接触操作 | 提升机器人操作泛化和稳定性 | [paper](https://icml.cc/virtual/2026/poster/65669) | 用于观察本体差异如何改变控制和数据需求。 |
| NeurIPS 2025 | [Universal Visuo-Tactile Video Understanding for Embodied Interaction](https://arxiv.org/abs/2505.22566) | tactile policy | 触觉/接触操作 | 引入触觉提升接触操作 | [paper](https://arxiv.org/abs/2505.22566) | 用于观察本体差异如何改变控制和数据需求。 |
| NeurIPS 2025 | [Enhancing Tactile-based Reinforcement Learning for Robotic Control](https://arxiv.org/abs/2510.21609) | tactile policy / RL | 触觉/接触操作 | 引入触觉提升接触操作 | [paper](https://arxiv.org/abs/2510.21609) / [project](https://elle-miller.github.io/tactile_rl/) | 用于观察本体差异如何改变控制和数据需求。 |
| NeurIPS 2025 | [Taccel: Scaling Up Vision-based Tactile Robotics via High-performance GPU Simulation](https://taccel-simulator.github.io/assets/taccel-paper.pdf) | tactile policy | 触觉/接触操作 | 引入触觉提升接触操作 | [paper](https://taccel-simulator.github.io/assets/taccel-paper.pdf) / [project](http://taccel-simulator.github.io/) | 用于观察本体差异如何改变控制和数据需求。 |
| NeurIPS 2025 | [Toward Artificial Palpation: Representation Learning of Touch on Soft Bodies](https://arxiv.org/abs/2511.16596) | tactile policy | 触觉/接触操作 | 处理触觉和接触丰富任务 | [paper](https://arxiv.org/abs/2511.16596) / [project](https://zoharri.github.io/artificial-palpation/) | 用于观察本体差异如何改变控制和数据需求。 |
| NeurIPS 2025 | [Touch in the Wild: Learning Fine-Grained Manipulation with a Portable Visuo-Tactile Gripper](https://arxiv.org/abs/2507.15062v1) | tactile policy | 触觉/接触操作 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2507.15062v1) / [project](https://binghao-huang.github.io/touch_in_the_wild/) | 用于观察本体差异如何改变控制和数据需求。 |

### 轻量化 / 评测 / 数据

这一方向决定能不能真实部署：端侧推理、缓存/量化/action tokenization、实时执行、sim2real、benchmark 和 safety evaluation 都是必需条件。

子方向：quantization/cache/tokenization、real-time execution、benchmark/dataset、sim2real、safety evaluation。

共 46 篇。

| 子方向 | 条目数 | 观察重点 |
| --- | ---: | --- |
| quantization/cache/tokenization | 7 | 看端侧部署、缓存复用和 action token 效率。 |
| real-time execution | 3 | 看低延迟执行和实时策略推理。 |
| benchmark/dataset | 20 | 看数据覆盖、任务设计和评测可信度。 |
| sim2real | 9 | 看仿真到真实迁移和真实部署差距。 |
| safety evaluation | 7 | 看鲁棒性、安全性和部署风险评估。 |

#### quantization/cache/tokenization

共 7 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- |
| CVPR 2026 | [QuantVLA: Scale-Calibrated Post-Training Quantization for Vision-Language-Action Models](https://arxiv.org/abs/2602.20309) | VLA / quantization | 机器人部署/评测环境 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2602.20309) / [project](https://quantvla.github.io/) | 用于评估部署效率、数据覆盖和评测可信度。 |
| NeurIPS 2025 | [BEAST: Efficient Tokenization of B-Splines Encoded Action Sequences for Imitation Learning](https://arxiv.org/abs/2506.06072) | VLA / action tokenization | 机器人部署/评测环境 | 提升推理或执行效率 | [paper](https://arxiv.org/abs/2506.06072) | 用于评估部署效率、数据覆盖和评测可信度。 |
| NeurIPS 2025 | [Quantization-Free Autoregressive Action Transformer](https://arxiv.org/abs/2503.14259) | quantization / autoregressive policy | 机器人部署/评测环境 | 降低模型部署成本 | [paper](https://arxiv.org/abs/2503.14259) | 用于评估部署效率、数据覆盖和评测可信度。 |
| NeurIPS 2025 | [EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models](https://arxiv.org/abs/2506.10100) | VLA | 机器人部署/评测环境 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2506.10100) | 用于评估部署效率、数据覆盖和评测可信度。 |
| NeurIPS 2025 | [VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching](https://arxiv.org/abs/2502.02175) | VLA / cache / action tokenization | 机器人部署/评测环境 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2502.02175) / [project](https://vla-cache.github.io/) | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICCV 2025 | [VQ-VLA: Improving Vision-Language-Action Models via Scaling Vector-Quantized Action Tokenizers](https://arxiv.org/abs/2507.01016) | VLA / quantization / action tokenization | 机器人部署/评测环境 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2507.01016) / [project](https://xiaoxiao0406.github.io/vqvla.github.io) | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICCV 2025 | [Saliency-Aware Quantized Imitation Learning for Efficient Robotic Control](https://arxiv.org/abs/2505.15304) | quantization | 机器人部署/评测环境 | 提升推理或执行效率 | [paper](https://arxiv.org/abs/2505.15304) | 用于评估部署效率、数据覆盖和评测可信度。 |

#### real-time execution

共 3 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- |
| NeurIPS 2025 | [Real-Time Execution of Action Chunking Flow Policies](https://www.physicalintelligence.company/download/real_time_chunking.pdf) | VLA / flow matching | 机器人部署/评测环境 | 提升实时执行能力 | [paper](https://www.physicalintelligence.company/download/real_time_chunking.pdf) / [project](https://www.physicalintelligence.company/research/real_time_chunking) | 用于评估部署效率、数据覆盖和评测可信度。 |
| NeurIPS 2025 | [Accelerating Visual-Policy Learning through Parallel Differentiable Simulation](https://www.arxiv.org/abs/2505.10646) | real-time execution | 仿真/评测环境 | 提升实时执行能力 | [paper](https://www.arxiv.org/abs/2505.10646) / [project](https://haoxiangyou.github.io/Dva_website/) | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICCV 2025 | [On-Device Diffusion Transformer Policy for Efficient Robot Manipulation](https://arxiv.org/abs/2508.00697) | diffusion policy / diffusion transformer | 机器人部署/评测环境 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2508.00697) | 用于评估部署效率、数据覆盖和评测可信度。 |

#### benchmark/dataset

共 20 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- |
| ICML 2026 | [AIR-VLA: Vision-Language-Action Systems for Aerial Manipulation](https://icml.cc/virtual/2026/poster/64411) | VLA | 无人机/空中机器人 | 改进视觉语言到动作策略 | [paper](https://icml.cc/virtual/2026/poster/64411) | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICML 2026 | [DLO-Lab: Benchmarking Deformable Linear Object Manipulations with Differentiable Physics](https://icml.cc/virtual/2026/poster/63391) | benchmark/dataset | 仿真/评测环境 | 提供评测任务和数据基准 | [paper](https://icml.cc/virtual/2026/poster/63391) | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICML 2026 | [ManiSoft: Towards Vision-Language Manipulation for Soft Robotics](https://icml.cc/virtual/2026/poster/63416) | benchmark/dataset | 机器人部署/评测环境 | 提升机器人操作泛化和稳定性 | [paper](https://icml.cc/virtual/2026/poster/63416) | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICML 2026 | [OXE-AugE: A Large-Scale Robot Augmentation of OXE for Scaling Cross-Embodiment Policy Learning](https://icml.cc/virtual/2026/poster/64619) | benchmark/dataset | 机器人部署/评测环境 | 提供可复用评测资源 | [paper](https://icml.cc/virtual/2026/poster/64619) | 用于评估部署效率、数据覆盖和评测可信度。 |
| NeurIPS 2025 | [BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models](https://arxiv.org/abs/2506.07961) | VLA / 3D representation | 机器人部署/评测环境 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2506.07961) / [project](https://bridgevla.github.io/) | 用于评估部署效率、数据覆盖和评测可信度。 |
| NeurIPS 2025 | [RobotSmith: Generative Robotic Tool Design for Acquisition of Complex Manipulation Skill](https://arxiv.org/abs/2506.14763) | benchmark/dataset | 机器人部署/评测环境 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2506.14763) / [project](https://umass-embodied-agi.github.io/RobotSmith/) | 用于评估部署效率、数据覆盖和评测可信度。 |
| NeurIPS 2025 | [URDF-Anything: Constructing Articulated Objects with 3D Multimodal Language Model](https://arxiv.org/abs/2511.00940) | 3D representation | 机器人部署/评测环境 | 提供可复用评测资源 | [paper](https://arxiv.org/abs/2511.00940) | 用于评估部署效率、数据覆盖和评测可信度。 |
| NeurIPS 2025 | [FreqPolicy: Efficient Flow-based Visuomotor Policy via Frequency Consistency](https://arxiv.org/abs/2506.08822) | flow matching | 机器人部署/评测环境 | 提升推理或执行效率 | [paper](https://arxiv.org/abs/2506.08822) | 用于评估部署效率、数据覆盖和评测可信度。 |
| NeurIPS 2025 | [RoboCerebra: A Large-scale Benchmark for Long-horizon Robotic Manipulation Evaluation](https://www.arxiv.org/pdf/2506.06677) | benchmark/dataset | 仿真/评测环境 | 提供评测任务和数据基准 | [paper](https://www.arxiv.org/pdf/2506.06677) / [project](https://github.com/qiuboxiang/RoboCerebra) | 用于评估部署效率、数据覆盖和评测可信度。 |
| NeurIPS 2025 | [SutureBot: A Precision Framework & Benchmark For Autonomous End-to-End Suturing](https://suturebot.github.io/static/SutureBot_NeurIPS_2025.pdf) | benchmark/dataset | 仿真/评测环境 | 提供评测任务和数据基准 | [paper](https://suturebot.github.io/static/SutureBot_NeurIPS_2025.pdf) / [project](https://suturebot.github.io/) | 用于评估部署效率、数据覆盖和评测可信度。 |
| NeurIPS 2025 | Embodied Crowd Counting | benchmark/dataset | 机器人部署/评测环境 | 提供可复用评测资源 |  | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICCV 2025 | [CARP: Coarse-to-Fine Autoregressive Prediction for Visuomotor Policy Learning](https://arxiv.org/abs/2412.06782) | autoregressive policy | 机器人部署/评测环境 | 提供可复用评测资源 | [paper](https://arxiv.org/abs/2412.06782) / [project](https://carp-robot.github.io/) | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICCV 2025 | [RoboFactory: Exploring Embodied Agent Collaboration with Compositional Constraints](https://arxiv.org/abs/2503.16408) | benchmark/dataset | 仿真/评测环境 | 提供可复用评测资源 | [paper](https://arxiv.org/abs/2503.16408) / [project](https://vlabench.github.io/) | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICCV 2025 | [HUMOTO: A 4D Dataset of Mocap Human Object Interactions](https://arxiv.org/abs/2504.10414) | benchmark/dataset | 仿真/评测环境 | 提供训练/评测数据资源 | [paper](https://arxiv.org/abs/2504.10414) / [project](https://jiaxin-lu.github.io/humoto/) | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICCV 2025 | [RoboMM: All-in-One Multimodal Large Model for Robotic Manipulation](https://arxiv.org/abs/2412.07215) | benchmark/dataset | 机器人部署/评测环境 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2412.07215) | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICCV 2025 | [Beyond the Destination: A Novel Benchmark for Exploration-Aware Embodied Question Answering](https://arxiv.org/abs/2503.11117) | benchmark/dataset | 仿真/评测环境 | 提供评测任务和数据基准 | [paper](https://arxiv.org/abs/2503.11117) / [project](https://github.com/HCPLab-SYSU/EXPRESS-Bench) | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICCV 2025 | [RobAVA: A Large-scale Dataset and Baseline Towards Video based Robotic Arm Action Understanding](https://iccv.thecvf.com/virtual/2025/poster/1787) | benchmark/dataset | 仿真/评测环境 | 提供训练/评测数据资源 | [paper](https://iccv.thecvf.com/virtual/2025/poster/1787) | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICCV 2025 | [RoboAnnotatorX: A Comprehensive and Universal Annotation Framework for Accurate Understanding of Long-horizon Robot Demonstration](https://iccv.thecvf.com/virtual/2025/poster/2215) | benchmark/dataset | 机器人部署/评测环境 | 提供可复用评测资源 | [paper](https://iccv.thecvf.com/virtual/2025/poster/2215) | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICML 2025 | EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents | benchmark/dataset | 仿真/评测环境 | 提供评测任务和数据基准 | [paper](https://arxiv.org/abs/2502.09560) / [project](https://embodiedbench.github.io/) | 用于评估部署效率、数据覆盖和评测可信度。 |
| CVPR 2025 | [Pixel-aligned RGB-NIR Stereo Imaging and Dataset for Robot Vision](https://arxiv.org/abs/2411.18025) | benchmark/dataset | 仿真/评测环境 | 提供训练/评测数据资源 | [paper](https://arxiv.org/abs/2411.18025) | 用于评估部署效率、数据覆盖和评测可信度。 |

#### sim2real

共 9 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- |
| ICML 2026 | [FlatLab: A Unified Methodology Framework and Simulation-Based Benchmark for Robotic Manipulation of Flat Objects](https://icml.cc/virtual/2026/poster/66662) | sim2real | 仿真/评测环境 | 提供评测任务和数据基准 | [paper](https://icml.cc/virtual/2026/poster/66662) | 用于评估部署效率、数据覆盖和评测可信度。 |
| CVPR 2026 | [GeCo-SRT: Geometry-aware Continual Adaptation for Robotic Cross-Task Sim-to-Real Transfer](https://arxiv.org/abs/2602.20871) | sim2real | 仿真/评测环境 | 缩小仿真到真实差距 | [paper](https://arxiv.org/abs/2602.20871) / [project](https://namelesscrew.github.io/) | 用于评估部署效率、数据覆盖和评测可信度。 |
| NeurIPS 2025 | [EgoBridge: Domain Adaptation for Generalizable Imitation from Egocentric Human Data](https://arxiv.org/abs/2509.19626) | sim2real | 机器人部署/评测环境 | 缩小仿真到真实差距 | [paper](https://arxiv.org/abs/2509.19626) / [project](https://ego-bridge.github.io/) | 用于评估部署效率、数据覆盖和评测可信度。 |
| NeurIPS 2025 | DEAL: Diffusion Evolution Adversarial Learning for Sim-to-Real Transfer | diffusion policy | 仿真/评测环境 | 缩小仿真到真实差距 |  | 用于评估部署效率、数据覆盖和评测可信度。 |
| NeurIPS 2025 | [Generalizable Domain Adaptation for Sim-and-Real Policy Co-Training](https://arxiv.org/abs/2509.18631) | sim2real | 机器人部署/评测环境 | 缩小仿真到真实差距 | [paper](https://arxiv.org/abs/2509.18631) / [project](https://ot-sim2real.github.io/) | 用于评估部署效率、数据覆盖和评测可信度。 |
| NeurIPS 2025 | [LabUtopia: High-Fidelity Simulation and Hierarchical Benchmark for Scientific Embodied Agents](https://arxiv.org/abs/2505.22634) | sim2real | 仿真/评测环境 | 提供评测任务和数据基准 | [paper](https://arxiv.org/abs/2505.22634) / [project](https://rui-li023.github.io/labutopia-site/) | 用于评估部署效率、数据覆盖和评测可信度。 |
| NeurIPS 2025 | [SonoGym: High Performance Simulation for Challenging Surgical Tasks with Robotic Ultrasound](https://arxiv.org/abs/2507.01152) | sim2real | 仿真/评测环境 | 缩小仿真到真实差距 | [paper](https://arxiv.org/abs/2507.01152) / [project](https://github.com/SonoGym/SonoGym) | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICCV 2025 | [RoboPearls: Editable Video Simulation for Robot Manipulation](https://arxiv.org/abs/2506.22756) | RL | 仿真/评测环境 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2506.22756) / [project](https://tangtaogo.github.io/RoboPearls/) | 用于评估部署效率、数据覆盖和评测可信度。 |
| CVPR 2025 | [RoboTwin: Dual-Arm Robot Benchmark with Generative Digital Twins (early version)](https://arxiv.org/abs/2409.02920) | RL | 双臂机器人 | 提供评测任务和数据基准 | [paper](https://arxiv.org/abs/2409.02920) / [project](https://robotwin-benchmark.github.io/early-version/) | 用于评估部署效率、数据覆盖和评测可信度。 |

#### safety evaluation

共 7 篇。

| 会议/年份 | 论文 | 技术路线 | 本体/场景 | 解决的问题 | 资源 | 调研判断 |
| --- | --- | --- | --- | --- | --- | --- |
| ICML 2026 | [Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds](https://icml.cc/virtual/2026/poster/60472) | VLA / 3D representation | 机器人部署/评测环境 | 评估鲁棒性和安全性 | [paper](https://icml.cc/virtual/2026/poster/60472) | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICML 2026 | [PACT: Self-Evolving Physical Safety Alignment for Diffusion Policies in Embodied Manipulation](https://icml.cc/virtual/2026/poster/62679) | diffusion policy | 机器人部署/评测环境 | 提升机器人操作泛化和稳定性 | [paper](https://icml.cc/virtual/2026/poster/62679) | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICML 2026 | [SafeLab: An Interactive High-Fidelity Benchmark for Embodied Safety in Scientific Robotics](https://icml.cc/virtual/2026/poster/61584) | safety evaluation | 仿真/评测环境 | 提供评测任务和数据基准 | [paper](https://icml.cc/virtual/2026/poster/61584) | 用于评估部署效率、数据覆盖和评测可信度。 |
| ICML 2026 | [Dismantling the Illusion of Vision-Language-Action Models Competence via Explicit Distributional Shifts](https://icml.cc/virtual/2026/poster/64080) | VLA | 机器人部署/评测环境 | 改进视觉语言到动作策略 | [paper](https://icml.cc/virtual/2026/poster/64080) | 用于评估部署效率、数据覆盖和评测可信度。 |
| CVPR 2026 | [LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models](https://arxiv.org/abs/2510.13626) | VLA | 机器人部署/评测环境 | 改进视觉语言到动作策略 | [paper](https://arxiv.org/abs/2510.13626) / [project](https://huggingface.co/papers/2510.13626) | 用于评估部署效率、数据覆盖和评测可信度。 |
| NeurIPS 2025 | [A Smooth Sea Never Made a Skilled SAILOR: Robust Imitation via Learning to Search](https://arxiv.org/abs/2506.05294) | safety evaluation | 机器人部署/评测环境 | 评估鲁棒性和安全性 | [paper](https://arxiv.org/abs/2506.05294) / [project](https://gokul.dev/sailor/) | 用于评估部署效率、数据覆盖和评测可信度。 |
| NeurIPS 2025 | [PAC Bench: Do Foundation Models Understand Prerequisites for Executing Manipulation Policies?](https://arxiv.org/abs/2506.23725) | safety evaluation | 机器人部署/评测环境 | 提升机器人操作泛化和稳定性 | [paper](https://arxiv.org/abs/2506.23725) | 用于评估部署效率、数据覆盖和评测可信度。 |

## 重点阅读顺序

1. 先看 VLN 和 Agentic Planning：确认“大范围规划”和“细粒度规划”分别解决什么。
2. 再看 VLA 和 WAM：区分“直接动作生成”和“先想象/预测再执行”。
3. 最后看本体扩展、轻量化、评测：这些决定路线能不能真实部署。

## 数据来源说明

| 仓库 | 用途 |
| --- | --- |
| [Songwxuan/Embodied-AI-Paper-TopConf](https://github.com/Songwxuan/Embodied-AI-Paper-TopConf) | CCF-A 论文主来源，按会议和方向分类；论文、代码和项目页链接优先采用该仓库中已给出的资源。 |
| [jonyzhang2023/awesome-embodied-vla-va-vln](https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln) | 参考 VLA、WAM、VLN、VA 和 survey 的组织方式。 |
| [OpenMOSS/Awesome-WAM](https://github.com/OpenMOSS/Awesome-WAM) | 参考 WAM 的 cascaded/joint、autoregressive/diffusion、evaluation/training data 分类。 |
| [UCSB-AI/awesome-vision-language-navigation](https://github.com/UCSB-AI/awesome-vision-language-navigation) | 参考 VLN 的 dataset、evaluation、representation、action strategy、planning、asking for help 分类。 |
| [DelinQu/awesome-vision-language-action-model](https://github.com/DelinQu/awesome-vision-language-action-model) | 参考 VLA 里程碑时间线。 |
| [yueen-ma/Awesome-VLA](https://github.com/yueen-ma/Awesome-VLA) | 参考 VLA components、world models、reasoning、policy steering、low-level/high-level planners 分类。 |
