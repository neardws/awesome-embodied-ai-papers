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

<table>
<thead>
<tr>
<th nowrap>方向</th>
<th nowrap>子方向</th>
<th nowrap>CCF-A 条目数</th>
<th nowrap>结果判断</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>VLN / 大范围导航</td>
<td nowrap>连续环境 VLN、地图记忆、物理可执行导航、城市/开放环境导航、低成本/端侧导航</td>
<td nowrap>75</td>
<td nowrap>VLN 关注语言目标、空间地图、记忆、探索和导航决策，核心问题是把自然语言任务变成可执行的大范围移动计划。当前 CCF-A 条目显示，研究正在从离散导航图转向连续环境、物理可执行导航、开放城市环境和低成本端侧导航。</td>
</tr>
<tr>
<td nowrap>VLA / 操作策略</td>
<td nowrap>generalist VLA、action representation、diffusion/flow policy、3D grounding、online/RL fine-tuning、安全鲁棒性</td>
<td nowrap>182</td>
<td nowrap>VLA 是机械臂和移动操作的主战场，但它不只是“大模型接动作头”。CCF-A 论文集中在动作表示、diffusion/flow policy、3D grounding、在线/RL 微调和安全鲁棒性上。</td>
</tr>
<tr>
<td nowrap>WAM / 世界模型</td>
<td nowrap>cascaded WAM、joint WAM、video/latent world model、world model for VLA、world model evaluation</td>
<td nowrap>46</td>
<td nowrap>WAM 将未来世界状态预测和动作生成合在一起，适合放在 agent 规划和低层控制之间。它的价值不是替代所有控制器，而是提供可想象、可验证、可恢复的中间层。</td>
</tr>
<tr>
<td nowrap>Agentic Planning / 推理规划</td>
<td nowrap>任务分解、memory、failure monitor、constraint / affordance planning、self-improving planning</td>
<td nowrap>89</td>
<td nowrap>这一方向强调任务分解、记忆、失败监控、约束/affordance planning 和自改进规划。它最贴近“agent 规划，小模型或传统方法执行”的系统路线。</td>
</tr>
<tr>
<td nowrap>本体扩展 / 灵巧操作</td>
<td nowrap>humanoid、bimanual、dexterous hand、tactile/contact-rich、grasp</td>
<td nowrap>72</td>
<td nowrap>本体扩展决定具身智能是否能从单机械臂走向人形、双臂、灵巧手和触觉接触任务。表中论文体现了动作空间、传感方式和控制目标随本体变化而复杂化。</td>
</tr>
<tr>
<td nowrap>轻量化 / 评测 / 数据</td>
<td nowrap>quantization/cache/tokenization、real-time execution、benchmark/dataset、sim2real、safety evaluation</td>
<td nowrap>79</td>
<td nowrap>这一方向决定能不能真实部署：端侧推理、缓存/量化/action tokenization、实时执行、sim2real、benchmark 和 safety evaluation 都是必需条件。</td>
</tr>
</tbody>
</table>

## 各方向详细表格

### VLN / 大范围导航

VLN 关注语言目标、空间地图、记忆、探索和导航决策，核心问题是把自然语言任务变成可执行的大范围移动计划。当前 CCF-A 条目显示，研究正在从离散导航图转向连续环境、物理可执行导航、开放城市环境和低成本端侧导航。

子方向：连续环境 VLN、地图记忆、物理可执行导航、城市/开放环境导航、低成本/端侧导航。

共 75 篇。

<table>
<thead>
<tr>
<th nowrap>子方向</th>
<th nowrap>条目数</th>
<th nowrap>观察重点</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>连续环境 VLN</td>
<td nowrap>31</td>
<td nowrap>看是否从离散导航图走向连续观察和实时决策。</td>
</tr>
<tr>
<td nowrap>地图记忆</td>
<td nowrap>17</td>
<td nowrap>看地图表示、语义记忆、缓存和检索机制。</td>
</tr>
<tr>
<td nowrap>物理可执行导航</td>
<td nowrap>6</td>
<td nowrap>看真实本体约束、动态环境和安全解码。</td>
</tr>
<tr>
<td nowrap>城市/开放环境导航</td>
<td nowrap>18</td>
<td nowrap>看开放世界、城市、拥挤环境和长期导航。</td>
</tr>
<tr>
<td nowrap>低成本/端侧导航</td>
<td nowrap>3</td>
<td nowrap>看端侧推理、低成本记忆和数据效率。</td>
</tr>
</tbody>
</table>

#### 连续环境 VLN

共 31 篇。

<table>
<thead>
<tr>
<th nowrap>会议/年份</th>
<th nowrap>论文/方法</th>
<th nowrap>任务类型</th>
<th nowrap>环境</th>
<th nowrap>地图/记忆</th>
<th nowrap>训练/反馈</th>
<th nowrap>Sim/Real/Benchmark</th>
<th nowrap>问题/目标</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>来源</th>
<th nowrap>调研判断</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=kkBOIsrCXh">Embodied Navigation Foundation Model</a></td>
<td nowrap>连续 VLN</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>-</td>
<td nowrap>VLN policy</td>
<td nowrap>-</td>
<td nowrap>提升语言导航的规划和泛化</td>
<td nowrap><a href="https://openreview.net/forum?id=kkBOIsrCXh">paper</a></td>
<td nowrap><a href="https://pku-epic.github.io/NavFoM-Web/">project</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://pku-epic.github.io/NavFoM-Web/">benchmarks</a></td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=GK4rznYwhn">Ground Slow, Move Fast: A Dual-System Foundation Model for Generalizable Vision-Language Navigation</a></td>
<td nowrap>连续 VLN</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>-</td>
<td nowrap>VLN policy</td>
<td nowrap>-</td>
<td nowrap>提升语言导航的规划和泛化</td>
<td nowrap><a href="https://openreview.net/forum?id=GK4rznYwhn">paper</a></td>
<td nowrap><a href="https://internrobotics.github.io/internvla-n1-dualvln.github.io/">project</a></td>
<td nowrap><a href="https://github.com/InternRobotics/InternNav">code</a></td>
<td nowrap><a href="https://huggingface.co/datasets/InternRobotics/InternData-N1">InternData-N1</a></td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=eqcDckWHik">CompassNav: Steering From Path Imitation to Decision Understanding In Navigation</a></td>
<td nowrap>连续 VLN</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>-</td>
<td nowrap>VLN policy</td>
<td nowrap>-</td>
<td nowrap>提升语言导航的规划和泛化</td>
<td nowrap><a href="https://openreview.net/forum?id=eqcDckWHik">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=pFh5ygjN3V">M$^3$E: Continual Vision-and-Language Navigation via Mixture of Macro and Micro Experts</a></td>
<td nowrap>连续 VLN</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>-</td>
<td nowrap>VLN policy</td>
<td nowrap>-</td>
<td nowrap>提升语言导航的规划和泛化</td>
<td nowrap><a href="https://openreview.net/forum?id=pFh5ygjN3V">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=zGtTQTD1zu">OmniNav: A Unified Framework for Prospective Exploration and Visual-Language Navigation</a></td>
<td nowrap>连续 VLN</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>-</td>
<td nowrap>VLN policy</td>
<td nowrap>-</td>
<td nowrap>提升语言导航的规划和泛化</td>
<td nowrap><a href="https://openreview.net/forum?id=zGtTQTD1zu">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=0c7nAZjyr5">From Seeing to Experiencing: Scaling Navigation Foundation Models with Reinforcement Learning</a></td>
<td nowrap>连续 VLN</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>-</td>
<td nowrap>VLN policy</td>
<td nowrap>-</td>
<td nowrap>提升语言导航的规划和泛化</td>
<td nowrap><a href="https://openreview.net/forum?id=0c7nAZjyr5">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=apaLoTumdO">CE-Nav: Flow-Guided Reinforcement Refinement for Cross-Embodiment Local Navigation</a></td>
<td nowrap>连续 VLN</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>-</td>
<td nowrap>VLN policy</td>
<td nowrap>-</td>
<td nowrap>提升语言导航的规划和泛化</td>
<td nowrap><a href="https://openreview.net/forum?id=apaLoTumdO">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=bMrH2PFMsi">CoNavBench: Collaborative Long-Horizon Vision-Language Navigation Benchmark</a></td>
<td nowrap>评测/数据</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>-</td>
<td nowrap>VLN policy</td>
<td nowrap>Benchmark</td>
<td nowrap>提升语言导航的规划和泛化</td>
<td nowrap><a href="https://openreview.net/forum?id=bMrH2PFMsi">paper</a></td>
<td nowrap><a href="https://navcraft.github.io">NavCraft</a></td>
<td nowrap>-</td>
<td nowrap>CoNavBench; 4,048 single/collaborative episodes; NavCraft platform</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38886">NaVLA$^2$: A Vision-Language-Audio-Action Model for Multimodal Instruction Navigation</a></td>
<td nowrap>多模态导航</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>-</td>
<td nowrap>VLN policy</td>
<td nowrap>-</td>
<td nowrap>提升语言导航的规划和泛化</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38886">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38888">VPN: Visual Prompt Navigation</a></td>
<td nowrap>连续 VLN</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>-</td>
<td nowrap>VLN policy</td>
<td nowrap>-</td>
<td nowrap>提升语言导航的规划和泛化</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38888">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38891">SeqWalker: Sequential-Horizon Vision-and-Language Navigation with Hierarchical Planning</a></td>
<td nowrap>连续 VLN</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>-</td>
<td nowrap>VLN policy</td>
<td nowrap>-</td>
<td nowrap>提升语言导航的规划和泛化</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38891">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38895">UNeMo: Collaborative Visual-Language Reasoning and Navigation via a Multimodal World Model</a></td>
<td nowrap>世界模型导航</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>-</td>
<td nowrap>VLN policy</td>
<td nowrap>-</td>
<td nowrap>提升语言导航的规划和泛化</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38895">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38914">DNOI-4DRO: Deep 4D Radar Odometry with Differentiable Neural-Optimization Iterations</a></td>
<td nowrap>4D radar odometry / localization</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>-</td>
<td nowrap>VLN policy</td>
<td nowrap>-</td>
<td nowrap>提升语言导航的规划和泛化</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38914">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38954">Run, Ruminate, and Regulate: A Dual-process Thinking System for Vision-and-Language Navigation</a></td>
<td nowrap>连续 VLN</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>-</td>
<td nowrap>VLN policy</td>
<td nowrap>-</td>
<td nowrap>提升语言导航的规划和泛化</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38954">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61535">AdaNav: Adaptive Reasoning with Uncertainty for Vision-Language Navigation</a></td>
<td nowrap>连续 VLN</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>-</td>
<td nowrap>reasoning</td>
<td nowrap>-</td>
<td nowrap>提升语言导航的规划和泛化</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61535">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64780">Instruction Decomposition and Action Alignment for Vision-Language Navigation</a></td>
<td nowrap>连续 VLN</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>-</td>
<td nowrap>VLN policy</td>
<td nowrap>-</td>
<td nowrap>提升语言导航的规划和泛化</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64780">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/65809">TIC-VLA: A Think-in-Control Vision-Language-Action Model for Robot Navigation in Dynamic Environments</a></td>
<td nowrap>连续 VLN</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>-</td>
<td nowrap>VLA</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/65809">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61357">Hydra-Nav: Object Navigation via Adaptive Dual-Process Reasoning</a></td>
<td nowrap>开放环境</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>-</td>
<td nowrap>reasoning</td>
<td nowrap>-</td>
<td nowrap>解决开放环境导航和决策</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61357">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/60775">SafeDec: Constrained Decoding for Safe Autoregressive Generalist Robot Navigation Policies</a></td>
<td nowrap>开放环境</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>-</td>
<td nowrap>autoregressive policy</td>
<td nowrap>-</td>
<td nowrap>解决开放环境导航和决策</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/60775">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2511.20620">Wanderland: Geometrically Grounded Simulation for Open-World Embodied AI</a></td>
<td nowrap>评测/数据</td>
<td nowrap>仿真/评测环境</td>
<td nowrap>-</td>
<td nowrap>planning / RL</td>
<td nowrap>Sim/Benchmark</td>
<td nowrap>从离散导航走向连续环境</td>
<td nowrap><a href="https://arxiv.org/abs/2511.20620">paper</a></td>
<td nowrap><a href="https://ai4ce.github.io/wanderland/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2512.04069">SpaceTools: Tool-Augmented Spatial Reasoning via Double Interactive RL</a></td>
<td nowrap>连续 VLN</td>
<td nowrap>移动机器人/导航环境</td>
<td nowrap>-</td>
<td nowrap>planning / reasoning / RL</td>
<td nowrap>-</td>
<td nowrap>从离散导航走向连续环境</td>
<td nowrap><a href="https://arxiv.org/abs/2512.04069">paper</a></td>
<td nowrap><a href="https://spacetools.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2512.17907">Dexterous World Models</a></td>
<td nowrap>世界模型导航</td>
<td nowrap>灵巧手/抓取</td>
<td nowrap>-</td>
<td nowrap>world model / planning / RL</td>
<td nowrap>-</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap><a href="https://arxiv.org/abs/2512.17907">paper</a></td>
<td nowrap><a href="https://snuvclab.github.io/dwm/">project</a></td>
<td nowrap><a href="https://github.com/snuvclab/dwm">code</a></td>
<td nowrap>-</td>
<td nowrap>HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Humanoid-RL, WAM</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2508.09423">Distilling LLM Prior to Flow Model for Generalizable Agent’s Imagination in Object Goal Navigation</a></td>
<td nowrap>开放环境</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>-</td>
<td nowrap>flow matching</td>
<td nowrap>-</td>
<td nowrap>解决开放环境导航和决策</td>
<td nowrap><a href="https://arxiv.org/abs/2508.09423">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap>TP-MDDN: Task-Preferenced Multi-Demand-Driven Navigation with Autonomous Decision-Making</td>
<td nowrap>开放环境</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>-</td>
<td nowrap>VLN policy</td>
<td nowrap>-</td>
<td nowrap>解决开放环境导航和决策</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.06630">Active Test-time Vision-Language Navigation</a></td>
<td nowrap>连续 VLN</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>-</td>
<td nowrap>test-time adaptation</td>
<td nowrap>-</td>
<td nowrap>提升语言导航的规划和泛化</td>
<td nowrap><a href="https://arxiv.org/abs/2506.06630">paper</a></td>
<td nowrap><a href="https://kuai-lab.github.io/neurips2025atena/">project</a></td>
<td nowrap><a href="https://github.com/kuai-lab/NeurIPS25_att_vln">code</a></td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2510.00441">Seeing through Uncertainty: Robust Task-Oriented Optimization in Visual Navigation</a></td>
<td nowrap>开放环境</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>-</td>
<td nowrap>VLN policy</td>
<td nowrap>-</td>
<td nowrap>解决开放环境导航和决策</td>
<td nowrap><a href="https://arxiv.org/abs/2510.00441">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/PyyWill/NeuRO">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.18525">P3Nav: A Unified Framework for Embodied Navigation Integrating Perception, Planning, and Prediction</a></td>
<td nowrap>开放环境</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>-</td>
<td nowrap>planning</td>
<td nowrap>-</td>
<td nowrap>解决开放环境导航和决策</td>
<td nowrap><a href="https://arxiv.org/abs/2503.18525">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2412.05552">SAME: Learning Generic Language-Guided Visual Navigation with State-Adaptive Mixture of Experts</a></td>
<td nowrap>开放环境</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>-</td>
<td nowrap>VLN policy</td>
<td nowrap>-</td>
<td nowrap>解决开放环境导航和决策</td>
<td nowrap><a href="https://arxiv.org/abs/2412.05552">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/GengzeZhou/SAME">project</a></td>
<td nowrap>-</td>
<td nowrap>Awesome-VLA, EAI-Safety</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/1984">Embodied Navigation with Auxiliary Task of Action Description Prediction</a></td>
<td nowrap>开放环境</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>-</td>
<td nowrap>VLN policy</td>
<td nowrap>-</td>
<td nowrap>解决开放环境导航和决策</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/1984">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2412.10439">CogNav: Cognitive Process Modeling for Object Goal Navigation with LLMs</a></td>
<td nowrap>开放环境</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>-</td>
<td nowrap>planning</td>
<td nowrap>-</td>
<td nowrap>解决开放环境导航和决策</td>
<td nowrap><a href="https://arxiv.org/abs/2412.10439">paper</a></td>
<td nowrap><a href="https://yhancao.github.io/CogNav/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.11081">MoMa-Kitchen: A 100K+ Benchmark for Affordance-Grounded Last-Mile Navigation in Mobile Manipulation</a></td>
<td nowrap>评测/数据</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>-</td>
<td nowrap>affordance</td>
<td nowrap>Benchmark</td>
<td nowrap>提供评测任务和数据基准</td>
<td nowrap><a href="https://arxiv.org/abs/2503.11081">paper</a></td>
<td nowrap><a href="https://momakitchen.github.io/">project</a></td>
<td nowrap><a href="https://github.com/MoMaKitchen/MoMaKitchen">code</a></td>
<td nowrap><a href="https://huggingface.co/datasets/IPEC-COMMUNITY/MoMa-Kitchen-Data">MoMa-Kitchen-Data</a></td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
</tbody>
</table>

#### 地图记忆

共 17 篇。

<table>
<thead>
<tr>
<th nowrap>会议/年份</th>
<th nowrap>论文/方法</th>
<th nowrap>任务类型</th>
<th nowrap>环境</th>
<th nowrap>地图/记忆</th>
<th nowrap>训练/反馈</th>
<th nowrap>Sim/Real/Benchmark</th>
<th nowrap>问题/目标</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>来源</th>
<th nowrap>调研判断</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=HB6KvsqcAn">Towards Physically Executable 3D Gaussian for Embodied Navigation</a></td>
<td nowrap>地图/记忆</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>地图/记忆</td>
<td nowrap>map/memory</td>
<td nowrap>-</td>
<td nowrap>解决开放环境导航和决策</td>
<td nowrap><a href="https://openreview.net/forum?id=HB6KvsqcAn">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=LPv59noPAy">Uncertainty-Aware Gaussian Map for Vision-Language Navigation</a></td>
<td nowrap>地图/记忆</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>地图/记忆</td>
<td nowrap>map/memory</td>
<td nowrap>-</td>
<td nowrap>解决开放环境导航和决策</td>
<td nowrap><a href="https://openreview.net/forum?id=LPv59noPAy">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>HCP-Survey, WAM</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=RnuB0Nlbd5">JanusVLN: Decoupling Semantics and Spatiality with Dual Implicit Memory for Vision-Language Navigation</a></td>
<td nowrap>地图/记忆</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>地图/记忆</td>
<td nowrap>dual implicit neural memory; KV-cache incremental update</td>
<td nowrap>-</td>
<td nowrap>解决开放环境导航和决策</td>
<td nowrap><a href="https://openreview.net/forum?id=RnuB0Nlbd5">paper</a></td>
<td nowrap><a href="https://miv-xjtu.github.io/JanusVLN.github.io/">project</a></td>
<td nowrap><a href="https://github.com/MIV-XJTU/JanusVLN">code</a></td>
<td nowrap><a href="https://miv-xjtu.github.io/JanusVLN.github.io/">dataset/weights</a></td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=li1vfqDzRD">Emergence of Spatial Representation in an Actor-Critic Agent with Hippocampus-Inspired Sequence Generator</a></td>
<td nowrap>地图/记忆</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>地图/记忆</td>
<td nowrap>map/memory</td>
<td nowrap>-</td>
<td nowrap>解决开放环境导航和决策</td>
<td nowrap><a href="https://openreview.net/forum?id=li1vfqDzRD">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=KcC5mwfGf0">GRL-SNAM: Geometric Reinforcement Learning with Differential Hamiltonians for Navigation and Mapping in Unknown Environments</a></td>
<td nowrap>地图/记忆</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>地图/记忆</td>
<td nowrap>map/memory</td>
<td nowrap>-</td>
<td nowrap>解决开放环境导航和决策</td>
<td nowrap><a href="https://openreview.net/forum?id=KcC5mwfGf0">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38884">RflyPano: A Panoramic Benchmark for Ultra-low Altitude UAV Localization Powered by RflySim</a></td>
<td nowrap>评测/数据</td>
<td nowrap>超低空 UAV / RflySim 仿真</td>
<td nowrap>评测/数据</td>
<td nowrap>map/memory</td>
<td nowrap>Benchmark</td>
<td nowrap>解决开放环境导航和决策</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38884">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/DUNDAI1998/RflyPano">code</a></td>
<td nowrap><a href="https://github.com/DUNDAI1998/RflyPano">dataset</a></td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38887">MHED-SLAM: Multi-Scale Hybrid Encoding-Based Decoupled SLAM</a></td>
<td nowrap>地图/记忆</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>地图/记忆</td>
<td nowrap>map/memory</td>
<td nowrap>-</td>
<td nowrap>解决开放环境导航和决策</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38887">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38893">LOG-Nav: Efficient Layout-Aware Object-Goal Navigation with Hierarchical Planning</a></td>
<td nowrap>地图/记忆</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>地图/记忆</td>
<td nowrap>map/memory</td>
<td nowrap>-</td>
<td nowrap>解决开放环境导航和决策</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38893">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38899">PanoNav: Mapless Zero-Shot Object Navigation with Panoramic Scene Parsing and Dynamic Memory</a></td>
<td nowrap>地图/记忆</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>地图/记忆</td>
<td nowrap>map/memory</td>
<td nowrap>-</td>
<td nowrap>解决开放环境导航和决策</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38899">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38901">Lightweight Adaptive Topological Layout and Semantic Mapping in Vision-and-Language Navigation on Websites</a></td>
<td nowrap>地图/记忆</td>
<td nowrap>Web / 网站导航环境</td>
<td nowrap>地图/记忆</td>
<td nowrap>map/memory</td>
<td nowrap>-</td>
<td nowrap>解决开放环境导航和决策</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38901">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38929">Expand Your SCOPE: Semantic Cognition over Potential-Based Exploration for Embodied Visual Navigation</a></td>
<td nowrap>地图/记忆</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>地图/记忆</td>
<td nowrap>map/memory</td>
<td nowrap>-</td>
<td nowrap>解决开放环境导航和决策</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38929">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38948">Agent Journey Beyond RGB: Hierarchical Semantic-Spatial Representation Enrichment for Vision-and-Language Navigation</a></td>
<td nowrap>地图/记忆</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>地图/记忆</td>
<td nowrap>map/memory</td>
<td nowrap>-</td>
<td nowrap>解决开放环境导航和决策</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38948">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64902">MapDream: Task-Driven Map Learning for Vision-Language Navigation</a></td>
<td nowrap>地图/记忆</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>地图/记忆</td>
<td nowrap>map/memory</td>
<td nowrap>-</td>
<td nowrap>提升语言导航的规划和泛化</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64902">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2605.01736">GLMap: Multi-Scale Gaussian-Language Map for Zero-shot Embodied Navigation and Reasoning</a></td>
<td nowrap>地图/记忆</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>地图/记忆</td>
<td nowrap>planning / reasoning / 3D Gaussian</td>
<td nowrap>-</td>
<td nowrap>解决开放环境导航和决策</td>
<td nowrap><a href="https://arxiv.org/abs/2605.01736">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/sx-zhang/GLMap">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2510.18546">EfficientNav: Towards On-Device Object-Goal Navigation with Navigation Map Caching and Retrieval</a></td>
<td nowrap>地图/记忆</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>地图/记忆</td>
<td nowrap>map/memory</td>
<td nowrap>-</td>
<td nowrap>解决开放环境导航和决策</td>
<td nowrap><a href="https://arxiv.org/abs/2510.18546">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2507.04047">Move to Understand a 3D Scene: Bridging Visual Grounding and Exploration for Efficient and Versatile Embodied Navigation</a></td>
<td nowrap>地图/记忆</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>地图/记忆</td>
<td nowrap>3D representation</td>
<td nowrap>-</td>
<td nowrap>解决开放环境导航和决策</td>
<td nowrap><a href="https://arxiv.org/abs/2507.04047">paper</a></td>
<td nowrap><a href="https://mtu3d.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/944">NavQ: Learning a Q-Model for Foresighted Vision-and-Language Navigation</a></td>
<td nowrap>地图/记忆</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>地图/记忆</td>
<td nowrap>map/memory</td>
<td nowrap>-</td>
<td nowrap>提升语言导航的规划和泛化</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/944">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
</tbody>
</table>

#### 物理可执行导航

共 6 篇。

<table>
<thead>
<tr>
<th nowrap>会议/年份</th>
<th nowrap>论文/方法</th>
<th nowrap>任务类型</th>
<th nowrap>环境</th>
<th nowrap>地图/记忆</th>
<th nowrap>训练/反馈</th>
<th nowrap>Sim/Real/Benchmark</th>
<th nowrap>问题/目标</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>来源</th>
<th nowrap>调研判断</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38942">CorrectNav: Self-Correction Flywheel Empowers Vision-Language-Action Navigation Model</a></td>
<td nowrap>连续 VLN</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>-</td>
<td nowrap>self-correction flywheel / post-training</td>
<td nowrap>-</td>
<td nowrap>提升语言导航的规划和泛化</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38942">paper</a></td>
<td nowrap><a href="https://correctnav.github.io/">project</a></td>
<td nowrap><a href="https://github.com/owlet914/CorrectNav">code</a></td>
<td nowrap><a href="https://github.com/owlet914/CorrectNav">model/benchmarks</a></td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64257">SC$^{2}$-WM: A Self-Correcting World Model with Closed-Loop Feedback for Vision-and-Language Navigation in Continuous Environments</a></td>
<td nowrap>世界模型导航</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>-</td>
<td nowrap>world model / RL</td>
<td nowrap>-</td>
<td nowrap>提升语言导航的规划和泛化</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64257">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2507.13019">Rethinking the Embodied Gap in Vision-and-Language Navigation: A Holistic Study of Physical and Visual Disparities</a></td>
<td nowrap>连续 VLN</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>-</td>
<td nowrap>embodied navigation</td>
<td nowrap>-</td>
<td nowrap>提升语言导航的规划和泛化</td>
<td nowrap><a href="https://arxiv.org/abs/2507.13019">paper</a></td>
<td nowrap><a href="https://crystalsixone.github.io/vln_pe.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.23468">NavMorph: A Self-Evolving World Model for Vision-and-Language Navigation in Continuous Environments</a></td>
<td nowrap>世界模型导航</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>-</td>
<td nowrap>world model / RL</td>
<td nowrap>-</td>
<td nowrap>提升语言导航的规划和泛化</td>
<td nowrap><a href="https://arxiv.org/abs/2506.23468">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/Feliciaxyao/NavMorph">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/299">3D Gaussian Map with Open-Set Semantic Grouping for Vision-Language Navigation</a></td>
<td nowrap>地图/记忆</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>地图/记忆</td>
<td nowrap>3D representation / 3D Gaussian</td>
<td nowrap>-</td>
<td nowrap>提升语言导航的规划和泛化</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/299">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/1792">monoVLN: Bridging the Observation Gap between Monocular and Panoramic Vision and Language Navigation</a></td>
<td nowrap>开放环境</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>-</td>
<td nowrap>embodied navigation</td>
<td nowrap>-</td>
<td nowrap>解决开放环境导航和决策</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/1792">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
</tbody>
</table>

#### 城市/开放环境导航

共 18 篇。

<table>
<thead>
<tr>
<th nowrap>会议/年份</th>
<th nowrap>论文/方法</th>
<th nowrap>任务类型</th>
<th nowrap>环境</th>
<th nowrap>地图/记忆</th>
<th nowrap>训练/反馈</th>
<th nowrap>Sim/Real/Benchmark</th>
<th nowrap>问题/目标</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>来源</th>
<th nowrap>调研判断</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=88RKxlFUNY">AutoFly: Vision-Language-Action Model for UAV Autonomous Navigation in the Wild</a></td>
<td nowrap>开放环境</td>
<td nowrap>无人机/城市环境</td>
<td nowrap>-</td>
<td nowrap>open-world navigation</td>
<td nowrap>-</td>
<td nowrap>解决开放环境导航和决策</td>
<td nowrap><a href="https://openreview.net/forum?id=88RKxlFUNY">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=OKm3w71ymP">OpenFly: A COMPREHENSIVE PLATFORM FOR AERIAL VISION-LANGUAGE NAVIGATION</a></td>
<td nowrap>评测/数据</td>
<td nowrap>无人机/城市环境</td>
<td nowrap>-</td>
<td nowrap>open-world navigation</td>
<td nowrap>Benchmark</td>
<td nowrap>解决开放环境导航和决策</td>
<td nowrap><a href="https://openreview.net/forum?id=OKm3w71ymP">paper</a></td>
<td nowrap><a href="https://shailab-ipec.github.io/openfly/">project</a></td>
<td nowrap><a href="https://github.com/Eziotic/OpenFly">code</a></td>
<td nowrap><a href="https://shailab-ipec.github.io/openfly/">OpenFly dataset</a></td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=qSak1Hjfdq">All-day Multi-scenes Lifelong Vision-and-Language Navigation with Tucker Adaptation</a></td>
<td nowrap>开放环境</td>
<td nowrap>无人机/城市环境</td>
<td nowrap>-</td>
<td nowrap>open-world navigation</td>
<td nowrap>-</td>
<td nowrap>解决开放环境导航和决策</td>
<td nowrap><a href="https://openreview.net/forum?id=qSak1Hjfdq">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=PaYo96rjij">Lifelong Embodied Navigation Learning</a></td>
<td nowrap>开放环境</td>
<td nowrap>无人机/城市环境</td>
<td nowrap>-</td>
<td nowrap>open-world navigation</td>
<td nowrap>-</td>
<td nowrap>解决开放环境导航和决策</td>
<td nowrap><a href="https://openreview.net/forum?id=PaYo96rjij">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=hzf23XSDcs">CitySeeker: How Do VLMs Explore Embodied Urban Navigation with Implicit Human Needs?</a></td>
<td nowrap>评测/数据</td>
<td nowrap>无人机/城市环境</td>
<td nowrap>-</td>
<td nowrap>open-world navigation</td>
<td nowrap>Benchmark</td>
<td nowrap>解决开放环境导航和决策</td>
<td nowrap><a href="https://openreview.net/forum?id=hzf23XSDcs">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>CitySeeker; 6,440 trajectories across 8 cities</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38878">AerialVLA: A Vision-Language-Action Model for Aerial Navigation with Online Dialogue</a></td>
<td nowrap>开放环境</td>
<td nowrap>无人机/城市环境</td>
<td nowrap>-</td>
<td nowrap>open-world navigation</td>
<td nowrap>-</td>
<td nowrap>解决开放环境导航和决策</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38878">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38885">History-Enhanced Two-Stage Transformer for Aerial Vision-and-Language Navigation</a></td>
<td nowrap>开放环境</td>
<td nowrap>无人机/城市环境</td>
<td nowrap>-</td>
<td nowrap>open-world navigation</td>
<td nowrap>-</td>
<td nowrap>解决开放环境导航和决策</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38885">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38897">RENEW: Risk- and Energy-Aware Navigation in Dynamic Waterways</a></td>
<td nowrap>开放环境</td>
<td nowrap>动态水道 / 水域导航</td>
<td nowrap>-</td>
<td nowrap>open-world navigation</td>
<td nowrap>-</td>
<td nowrap>解决开放环境导航和决策</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38897">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38898">Towards Autonomous UAV Visual Object Search in City Space: Benchmark and Agentic Methodology</a></td>
<td nowrap>评测/数据</td>
<td nowrap>无人机/城市环境</td>
<td nowrap>object-centric dynamic semantic map; 3D cognitive map; 3D uncertainty map</td>
<td nowrap>open-world navigation</td>
<td nowrap>Benchmark</td>
<td nowrap>解决开放环境导航和决策</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38898">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>CityAVOS benchmark; 2,420 tasks</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38916">UrbanNav: Learning Language-Guided Embodied Urban Navigation from Web-Scale Human Trajectories</a></td>
<td nowrap>开放环境</td>
<td nowrap>地面城市 / 四轮移动机器人</td>
<td nowrap>-</td>
<td nowrap>open-world navigation</td>
<td nowrap>-</td>
<td nowrap>解决开放环境导航和决策</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38916">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/CASIA-IVA-Lab/UrbanNav">code</a></td>
<td nowrap><a href="https://huggingface.co/datasets/Vigar001/UrbanNav">UrbanNav dataset</a></td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38917">Autonomous Vehicle Path Planning by Searching with Differentiable Simulation</a></td>
<td nowrap>开放环境</td>
<td nowrap>无人车 / 自动驾驶</td>
<td nowrap>-</td>
<td nowrap>open-world navigation</td>
<td nowrap>-</td>
<td nowrap>解决开放环境导航和决策</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38917">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38920">Real-Time Path Planning for UAVs in Windy Environments Without Computational Fluid Dynamics</a></td>
<td nowrap>开放环境</td>
<td nowrap>无人机/城市环境</td>
<td nowrap>-</td>
<td nowrap>open-world navigation</td>
<td nowrap>-</td>
<td nowrap>解决开放环境导航和决策</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38920">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Efficient-VLA, Humanoid-RL, EAI-Safety, WAM</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38938">ReflexDiffusion: Reflection-Enhanced Trajectory Planning for High-lateral-acceleration Scenarios in Autonomous Driving</a></td>
<td nowrap>开放环境</td>
<td nowrap>无人车 / 自动驾驶</td>
<td nowrap>-</td>
<td nowrap>open-world navigation</td>
<td nowrap>-</td>
<td nowrap>解决开放环境导航和决策</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38938">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38941">Learning from Human Gaze: Human-like Robot Social Navigation in Dense Crowds</a></td>
<td nowrap>开放环境</td>
<td nowrap>移动机器人 / 拥挤人群社交导航</td>
<td nowrap>-</td>
<td nowrap>open-world navigation</td>
<td nowrap>-</td>
<td nowrap>解决开放环境导航和决策</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38941">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/63554">Plan in Sandbox, Navigate in Open Worlds: Learning Physics-Grounded Abstracted Experience for Embodied Navigation</a></td>
<td nowrap>开放环境</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>-</td>
<td nowrap>RL</td>
<td nowrap>-</td>
<td nowrap>解决开放环境导航和决策</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/63554">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2510.20685">C-NAV: Towards Self-Evolving Continual Object Navigation in Open World</a></td>
<td nowrap>开放环境</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>-</td>
<td nowrap>RL</td>
<td nowrap>-</td>
<td nowrap>解决开放环境导航和决策</td>
<td nowrap><a href="https://arxiv.org/abs/2510.20685">paper</a></td>
<td nowrap><a href="https://bigtree765.github.io/C-Nav-project/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap>Synthesizing Photorealistic and Dynamic Urban Environments for Multimodal Robot Navigation and Collaboration</td>
<td nowrap>开放环境</td>
<td nowrap>无人车/城市环境</td>
<td nowrap>-</td>
<td nowrap>open-world navigation</td>
<td nowrap>-</td>
<td nowrap>解决开放环境导航和决策</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2408.15503">RoboSense: Large-scale Dataset and Benchmark for Egocentric Robot Perception and Navigation in Crowded and Unstructured Environments</a></td>
<td nowrap>评测/数据</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>-</td>
<td nowrap>open-world navigation</td>
<td nowrap>Benchmark</td>
<td nowrap>提供评测任务和数据基准</td>
<td nowrap><a href="https://arxiv.org/abs/2408.15503">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/suhaisheng/RoboSense">code</a></td>
<td nowrap><a href="https://huggingface.co/datasets/suhaisheng0527/RoboSense">RoboSense dataset</a></td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
</tbody>
</table>

#### 低成本/端侧导航

共 3 篇。

<table>
<thead>
<tr>
<th nowrap>会议/年份</th>
<th nowrap>论文/方法</th>
<th nowrap>任务类型</th>
<th nowrap>环境</th>
<th nowrap>地图/记忆</th>
<th nowrap>训练/反馈</th>
<th nowrap>Sim/Real/Benchmark</th>
<th nowrap>问题/目标</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>来源</th>
<th nowrap>调研判断</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap>Aux-Think: Exploring Reasoning Strategies for Data-Efficient Vision-Language Navigation</td>
<td nowrap>端侧/低成本</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>-</td>
<td nowrap>reasoning</td>
<td nowrap>-</td>
<td nowrap>提升语言导航的规划和泛化</td>
<td nowrap><a href="https://arxiv.org/abs/2505.11886">paper</a></td>
<td nowrap><a href="https://horizonrobotics.github.io/robot_lab/aux-think/">project</a></td>
<td nowrap>-</td>
<td nowrap>R2R-CoT-320k</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://openreview.net/pdf?id=5gptKWnVPF">Harnessing Input-adaptive Inference for Efficient VLN</a></td>
<td nowrap>端侧/低成本</td>
<td nowrap>移动机器人/导航环境</td>
<td nowrap>-</td>
<td nowrap>efficient navigation</td>
<td nowrap>-</td>
<td nowrap>提升推理或执行效率</td>
<td nowrap><a href="https://openreview.net/pdf?id=5gptKWnVPF">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/secure-ai-systems-group/adaptive-vision-and-language-navigation">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.24065">COSMO: Combination of Selective Memorization for Low-cost Vision-and-Language Navigation</a></td>
<td nowrap>端侧/低成本</td>
<td nowrap>移动机器人/移动操作</td>
<td nowrap>-</td>
<td nowrap>efficient navigation</td>
<td nowrap>-</td>
<td nowrap>提升语言导航的规划和泛化</td>
<td nowrap><a href="https://arxiv.org/abs/2503.24065">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于判断导航是否走向连续、物理和跨场景。</td>
</tr>
</tbody>
</table>

### VLA / 操作策略

VLA 是机械臂和移动操作的主战场，但它不只是“大模型接动作头”。CCF-A 论文集中在动作表示、diffusion/flow policy、3D grounding、在线/RL 微调和安全鲁棒性上。

子方向：generalist VLA、action representation、diffusion/flow policy、3D grounding、online/RL fine-tuning、安全鲁棒性。

共 182 篇。

<table>
<thead>
<tr>
<th nowrap>子方向</th>
<th nowrap>条目数</th>
<th nowrap>观察重点</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>generalist VLA</td>
<td nowrap>58</td>
<td nowrap>看跨任务泛化、真实机器人验证和通用操作能力。</td>
</tr>
<tr>
<td nowrap>action representation</td>
<td nowrap>18</td>
<td nowrap>看动作 token、latent action、chunking 和动作空间设计。</td>
</tr>
<tr>
<td nowrap>diffusion/flow policy</td>
<td nowrap>63</td>
<td nowrap>看连续动作生成、稳定控制和执行平滑性。</td>
</tr>
<tr>
<td nowrap>3D grounding</td>
<td nowrap>28</td>
<td nowrap>看点云、几何、affordance 与操作定位。</td>
</tr>
<tr>
<td nowrap>online/RL fine-tuning</td>
<td nowrap>12</td>
<td nowrap>看在线强化、人在回路和测试时适配。</td>
</tr>
<tr>
<td nowrap>安全鲁棒性</td>
<td nowrap>3</td>
<td nowrap>看攻击鲁棒、安全对齐和风险暴露。</td>
</tr>
</tbody>
</table>

#### generalist VLA

共 58 篇。

<table>
<thead>
<tr>
<th nowrap>会议/年份</th>
<th nowrap>论文/方法</th>
<th nowrap>Base VLA</th>
<th nowrap>Action</th>
<th nowrap>训练/反馈</th>
<th nowrap>Algorithm</th>
<th nowrap>Policy/Type</th>
<th nowrap>Sim/Real</th>
<th nowrap>问题/目标</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>来源</th>
<th nowrap>调研判断</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=54U3XHf7qq">MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA / 通用 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://openreview.net/forum?id=54U3XHf7qq">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=DdrsHWobR1">Disentangled Robot Learning via Separate Forward and Inverse Dynamics Pretraining</a></td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>VLA / 通用 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://openreview.net/forum?id=DdrsHWobR1">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=IBJtOltTbx">Hybrid Training for Vision-Language-Action Models</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA / 通用 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://openreview.net/forum?id=IBJtOltTbx">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=LYyoRqf0Ij">End-to-end Listen, Look, Speak and Act</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA / 通用 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://openreview.net/forum?id=LYyoRqf0Ij">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Humanoid-RL, EAI-Safety</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=OJh7oBCYhL">RoboOmni: Proactive Robot Manipulation in Omni-modal Context</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA / 通用 VLA</td>
<td nowrap>Perceiver-Thinker-Talker-Executor</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://openreview.net/forum?id=OJh7oBCYhL">paper</a> / <a href="https://arxiv.org/pdf/2510.23763">📄 Paper</a></td>
<td nowrap><a href="https://openmoss.github.io/RoboOmni/">🌍 Web</a></td>
<td nowrap><a href="https://github.com/OpenMOSS/RoboOmni">💻 Code</a></td>
<td nowrap><a href="https://huggingface.co/OpenMOSS-Team/RoboOmni">RoboOmni model</a> / <a href="https://huggingface.co/datasets/fnlp/OmniAction">OmniAction dataset</a></td>
<td nowrap>WAM</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=PklMD8PwUy">Unified Vision-Language-Action Model</a></td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion</td>
<td nowrap>VLA / 高效/轻量 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://openreview.net/forum?id=PklMD8PwUy">paper</a> / <a href="https://arxiv.org/abs/2503.10631">HybridVLA: Collaborative Diffusion and Autoregression in a Unified Vision-Language-Action Model</a> / <a href="https://arxiv.org/abs/2506.19850">Unified Vision-Language-Action Model</a></td>
<td nowrap><a href="https://hybrid-vla.github.io/">🌐</a> / <a href="https://robertwyq.github.io/univla.github.io/">🌐</a></td>
<td nowrap><a href="https://github.com/PKU-HMI-Lab/Hybrid-VLA">💻</a> / <a href="https://github.com/baaivision/UniVLA">💻</a></td>
<td nowrap>-</td>
<td nowrap>HCP-Survey, EAI-VLA-VLN, Awesome-VLA, Efficient-VLA</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=T3i7Ifeatk">Align-Then-stEer: Adapting the Vision-Language Action Models through Unified Latent Guidance</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA / 高效/轻量 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://openreview.net/forum?id=T3i7Ifeatk">paper</a> / <a href="https://arxiv.org/abs/2509.02055">Align-Then-stEer: Adapting the Vision-Language Action Models through Unified Latent Guidance</a></td>
<td nowrap><a href="https://align-then-steer.github.io/">🌐</a></td>
<td nowrap><a href="https://github.com/TeleHuman/Align-Then-Steer">💻</a></td>
<td nowrap>-</td>
<td nowrap>Efficient-VLA</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=UD4Rw8MOEK">Verifier-free Test-Time Sampling for Vision Language Action Models</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA / 通用 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://openreview.net/forum?id=UD4Rw8MOEK">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=kt51kZH4aG">X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA / 通用 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://openreview.net/forum?id=kt51kZH4aG">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=tc2UsBeODW">VLM4VLA: Revisiting Vision-Language-Models in Vision-Language-Action Models</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA / 通用 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://openreview.net/forum?id=tc2UsBeODW">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=tsxwloasw5">Vision-Language-Action Instruction Tuning: From Understanding to Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA / RL/在线微调</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://openreview.net/forum?id=tsxwloasw5">paper</a> / <a href="https://arxiv.org/abs/2507.17520">InstructVLA: Vision-Language-Action Instruction Tuning from Understanding to Manipulation</a></td>
<td nowrap><a href="https://yangs03.github.io/InstructVLA_Home/">🌐</a></td>
<td nowrap><a href="https://github.com/InternRobotics/InstructVLA">💻</a></td>
<td nowrap>-</td>
<td nowrap>EAI-Guide, HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Efficient-VLA, Robot-Learning, Humanoid-RL, EAI-Safety, EAI-ROS, WAM, RL-VLA</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=KcJ9U0x6kO">HAMLET: Switch Your Vision-Language-Action Model into a History-Aware Policy</a></td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>VLA / 通用 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://openreview.net/forum?id=KcJ9U0x6kO">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38902">DiTEA: Mixture-of-Experts for Vision-Language-Action Model in Robotic Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA / 通用 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38902">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38910">TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for Vision-Language-Action Models</a></td>
<td nowrap>-</td>
<td nowrap>Tokenization</td>
<td nowrap>VLA / 通用 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38910">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62813">Vision-Language-Action Pretraining from Large-Scale Human Videos</a></td>
<td nowrap>Being-H0</td>
<td nowrap>AR</td>
<td nowrap>VLA / RL/在线微调</td>
<td nowrap>physical instruction tuning + explicit hand motion modeling</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62813">paper</a> / <a href="https://arxiv.org/pdf/2507.15597">📄 Paper</a> / <a href="https://arxiv.org/abs/2507.15597">Being-H0: Vision-Language-Action Pretraining from Large-Scale Human Videos</a></td>
<td nowrap><a href="https://beingbeyond.github.io/Being-H0">🌍 Web</a> / <a href="https://beingbeyond.github.io/Being-H0/">🌐</a></td>
<td nowrap><a href="https://github.com/BeingBeyond/Being-H0">💻 Code</a></td>
<td nowrap><a href="https://huggingface.co/datasets/BeingBeyond/h0_post_train_db_2508">📦 Dataset</a></td>
<td nowrap>EAI-Guide, HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Efficient-VLA, Robot-Learning, Humanoid-RL, EAI-Safety, EAI-ROS, WAM, RL-VLA</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/60980">RA-VLA: Retrieval-Augmented VLA for Test-Time Adaptation</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA / 通用 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>扩展跨任务操作能力</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/60980">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62270">A Generalist Pair-wise Progress Critic Model for Vision-Language-Action Robots</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA / 通用 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62270">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62528">Bring My Cup! Personalizing Vision-Language-Action Models with Visual Attentive Prompting</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA / 通用 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62528">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66596">From Abstraction to Instantiation: Learning Behavioral Representation for Vision-Language-Action Model</a></td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>VLA / 通用 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66596">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61157">VLA-ATTC: Adaptive Test-Time Compute for VLA Models with Relative Action Critic Model</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA / 通用 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>扩展跨任务操作能力</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61157">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66066">SCALE: Self-uncertainty Conditioned Adaptive Looking and Execution for Vision-Language-Action Models</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA / RL/在线微调</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66066">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Efficient-VLA, Robot-Learning, Humanoid-RL, EAI-Safety, WAM, RL-VLA</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64826">XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations</a></td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>VLA / 通用 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64826">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66510">Escaping the Diversity Trap in Robotic Manipulation via Anchor-Centric Adaptation</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>generalist VLA / 通用 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66510">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/63997">Embodied Interpretability: Linking Causal Understanding to Generalization in Vision-Language-Action Models</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA / 通用 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/63997">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2511.04555">Evo-1: Lightweight Vision-Language-Action Model with Preserved Semantic Alignment</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA / 通用 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://arxiv.org/abs/2511.04555">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/MINT-SJTU/Evo-1">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2512.09928">HiF-VLA: Hindsight, Insight and Foresight through Motion Representation for Vision-Language-Action Models</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA / 通用 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://arxiv.org/abs/2512.09928">paper</a></td>
<td nowrap><a href="https://hifvla.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2603.12193">SaPaVe: Towards Active Perception and Manipulation in Vision-Language-Action Models for Robotics</a></td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>VLA / 通用 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://arxiv.org/abs/2603.12193">paper</a></td>
<td nowrap><a href="https://lmzpai.github.io/SaPaVe">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2601.12796">Contact-Aware Neural Dynamics</a></td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>generalist VLA / 通用 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>扩展跨任务操作能力</td>
<td nowrap><a href="https://arxiv.org/abs/2601.12796">paper</a></td>
<td nowrap><a href="https://changwei-jing.github.io/neural-physics/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Awesome-EAI, EAI-VLA-VLN</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2508.21046">CogVLA: Cognition-Aligned Vision-Language-Action Models via Instruction-Driven Routing &amp; Sparsification</a></td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>VLA / 高效/轻量 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://arxiv.org/abs/2508.21046">paper</a></td>
<td nowrap><a href="https://jiutian-vl.github.io/CogVLA-page/">project</a></td>
<td nowrap><a href="https://github.com/JiuTian-VL/CogVLA">💻</a></td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN, Efficient-VLA</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2505.15660">Exploring the Limits of Vision-Language-Action Manipulation in Cross-task Generalization</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA / 通用 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://arxiv.org/abs/2505.15660">paper</a> / <a href="https://arxiv.org/pdf/2505.15660">📄 Paper</a></td>
<td nowrap><a href="https://jiaming-zhou.github.io/AGNOSTOS/">project</a> / <a href="https://jiaming-zhou.github.io/AGNOSTOS">🌍 Web</a></td>
<td nowrap><a href="https://github.com/jiaming-zhou/X-ICM">💻 Code</a></td>
<td nowrap>-</td>
<td nowrap>WAM</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2505.15517">Robo2VLM: Improving Visual Question Answering using Large-Scale Robot Manipulation Data</a></td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>VLA / 通用 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2505.15517">paper</a></td>
<td nowrap><a href="https://berkeleyautomation.github.io/robo2vlm/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap>4D-VLA: Spatiotemporal Vision-Language-Action Pretraining with Cross-Scene Calibration</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA / 通用 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2510.24194">Blindfolded Experts Generalize Better: Insights from Robotic Manipulation and Videogames</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA / 通用 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2510.24194">paper</a></td>
<td nowrap><a href="https://sites.google.com/view/blindfoldedexperts/home">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2510.11321">HiMaCon: Discovering Hierarchical Manipulation Concepts from Unlabeled Multi-Modal Data</a></td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>VLA / 通用 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Sim/Benchmark</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2510.11321">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2505.23705">Knowledge Insulating Vision-Language-Action Models: Train Fast, Run Fast, Generalize Better</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA / 通用 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://arxiv.org/abs/2505.23705">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap>Diversifying Parallel Ergodic Search: A Signature Kernel Evolution Strategy</td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>generalist VLA / 通用 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>扩展跨任务操作能力</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/1325">FedVLA: Federated Vision-Language-Action Learning with Dual Gating Mixture-of-Experts for Robotic Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>VLA / 高效/轻量 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/1325">paper</a> / <a href="https://arxiv.org/abs/2508.02190">FedVLA: Federated Vision-Language-Action Learning with Dual Gating Mixture-of-Experts for Robotic Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Efficient-VLA</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/225">PASG: A Closed-Loop Framework for Automated Geometric Primitive Extraction and Semantic Anchoring in Robotic Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA / 通用 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/225">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.07087">iManip: Skill-Incremental Learning for Robotic Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>generalist VLA / 通用 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2503.07087">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/972">4D Visual Pre-training for Robot Learning</a></td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>generalist VLA / 通用 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>扩展跨任务操作能力</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/972">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICML 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2502.19417">Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models</a></td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>VLA / 通用 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://arxiv.org/abs/2502.19417">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICML 2025</td>
<td nowrap>OTTER: A Vision-Language-Action Model with Text-Aware Visual Feature Extraction</td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>VLA / 通用 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://arxiv.org/pdf/2503.03734">paper</a></td>
<td nowrap><a href="https://ottervla.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICML 2025</td>
<td nowrap>UP-VLA: A Unified Understanding and Prediction Model for Embodied Agent</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA / 通用 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>扩展跨任务操作能力</td>
<td nowrap><a href="https://arxiv.org/abs/2501.18867">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/CladernyJorn/UP-VLA">code</a></td>
<td nowrap>-</td>
<td nowrap>Awesome-EAI, Awesome-VLA</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICML 2025</td>
<td nowrap>ELEMENTAL: Interactive Learning from Demonstrations and Vision-Language Models for Reward Design in Robotics</td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>VLA / 通用 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>扩展跨任务操作能力</td>
<td nowrap><a href="https://arxiv.org/abs/2411.18825">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICML 2025</td>
<td nowrap>A Large Recurrent Action Model: xLSTM enables Fast Inference for Robotics Tasks</td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>VLA / 通用 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>扩展跨任务操作能力</td>
<td nowrap><a href="https://arxiv.org/abs/2410.22391">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/ml-jku/LRAM">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICML 2025</td>
<td nowrap>Pre-training Auto-regressive Robotic Models with 4D Representations</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>generalist VLA / 高效/轻量 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>扩展跨任务操作能力</td>
<td nowrap><a href="https://arxiv.org/pdf/2502.13142">paper</a></td>
<td nowrap><a href="https://arm4r.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Efficient-VLA, Humanoid-RL, WAM</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICML 2025</td>
<td nowrap>STAR: Learning Diverse Robot Skill Abstractions through Rotation-Augmented</td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>generalist VLA / RL/在线微调</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>扩展跨任务操作能力</td>
<td nowrap><a href="https://www.arxiv.org/pdf/2506.03863">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-Guide, Octoday, HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Efficient-VLA, Robot-Learning, Humanoid-RL, EAI-Safety, RL-VLA</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2501.10105">UniAct: Universal Actions For Enhanced Embodied Foundation Models</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA / 通用 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>扩展跨任务操作能力</td>
<td nowrap><a href="https://arxiv.org/abs/2501.10105">paper</a></td>
<td nowrap><a href="https://2toinf.github.io/UniAct/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Awesome-EAI, Humanoid-RL</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.13446">MoManipVLA: Transferring Vision-language-action Models for General Mobile Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA / 高效/轻量 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2503.13446">paper</a></td>
<td nowrap><a href="https://gary3410.github.io/momanipVLA/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN, Efficient-VLA</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.06960">A Data-Centric Revisit of Pre-Trained Vision Models for Robot Learning</a></td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>VLA / 通用 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>扩展跨任务操作能力</td>
<td nowrap><a href="https://arxiv.org/abs/2503.06960">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/CVMI-Lab/SlotMIM">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap>Think Small, Act Big: Primitive Prompt Learning for Lifelong Robot Manipulation</td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>VLA / 通用 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://cvpr.thecvf.com/virtual/2025/poster/32789">Phoenix: A Motion-based Self-Reflection Framework for Fine-grained Robotic Action Correction</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA / 通用 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>扩展跨任务操作能力</td>
<td nowrap><a href="https://cvpr.thecvf.com/virtual/2025/poster/32789">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2406.14235">Mitigating the Human-Robot Domain Discrepancy in Visual Pre-training for Robotic Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA / 通用 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2406.14235">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap>Object-Centric Prompt-Driven Vision-Language-Action Model for Robotic Manipulation</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA / 高效/轻量 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Efficient-VLA, Robot-Learning, Humanoid-RL, EAI-Safety</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap>Robotic Visual Instruction</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA / RL/在线微调</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>扩展跨任务操作能力</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-Guide, HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Efficient-VLA, Robot-Learning, Humanoid-RL, EAI-Safety, WAM, RL-VLA</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2411.17662">RoboPEPP: Vision-Based Robot Pose and Joint Angle Estimation through Embedding Predictive Pre-Training</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>generalist VLA / 通用 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>扩展跨任务操作能力</td>
<td nowrap><a href="https://arxiv.org/abs/2411.17662">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap>Two by Two: Learning Cross-Task Pairwise Objects Assembly for Generalizable Robot Manipulation</td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>generalist VLA / 通用 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.11269">Prof. Robot: Differentiable Robot Rendering Without Static and Self-Collisions</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>generalist VLA / 通用 VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>扩展跨任务操作能力</td>
<td nowrap><a href="https://arxiv.org/abs/2503.11269">paper</a></td>
<td nowrap><a href="https://www.qrcat.cn/prof-robot/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
</tbody>
</table>

#### action representation

共 18 篇。

<table>
<thead>
<tr>
<th nowrap>会议/年份</th>
<th nowrap>论文/方法</th>
<th nowrap>Base VLA</th>
<th nowrap>Action</th>
<th nowrap>训练/反馈</th>
<th nowrap>Algorithm</th>
<th nowrap>Policy/Type</th>
<th nowrap>Sim/Real</th>
<th nowrap>问题/目标</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>来源</th>
<th nowrap>调研判断</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=y5CaJb17Fn">villa-X: Enhancing Latent Action Modeling in Vision-Language-Action Models</a></td>
<td nowrap>-</td>
<td nowrap>Tokenization</td>
<td nowrap>action representation / 动作表示/tokenization</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进动作表示和解码</td>
<td nowrap><a href="https://openreview.net/forum?id=y5CaJb17Fn">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN, WAM</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=IZHk6BXBST">Rodrigues Network for Learning Robot Actions</a></td>
<td nowrap>-</td>
<td nowrap>AR / Tokenization</td>
<td nowrap>action representation / 动作表示/tokenization</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进动作表示和解码</td>
<td nowrap><a href="https://openreview.net/forum?id=IZHk6BXBST">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38937">Actor-Critic for Continuous Action Chunks: A Reinforcement Learning Framework for Long-Horizon Robotic Manipulation with Sparse Reward</a></td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>action representation / RL/在线微调</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进动作表示和解码</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38937">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN, EAI-Safety, RL-VLA</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/60681">DyGRO-VLA: Cross-Task Scaling of Vision-Language-Action Models via Dynamic Grouped Residual Optimization</a></td>
<td nowrap>-</td>
<td nowrap>Tokenization</td>
<td nowrap>VLA / 动作表示/tokenization</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/60681">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61232">LARA: Latent Action Representation Alignment for Vision-Language-Action Models</a></td>
<td nowrap>-</td>
<td nowrap>AR / Tokenization</td>
<td nowrap>VLA / 动作表示/tokenization</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61232">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62908">From Noise to Intent: Anchoring Generative VLA Policies with Residual Bridges</a></td>
<td nowrap>-</td>
<td nowrap>Tokenization</td>
<td nowrap>VLA / 动作表示/tokenization</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进动作表示和解码</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62908">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/65967">Demystifying Action Space Design for Robotic Manipulation Policies</a></td>
<td nowrap>-</td>
<td nowrap>Tokenization</td>
<td nowrap>action representation / 动作表示/tokenization</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/65967">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66520">FocalPolicy: Frequency-Optimized Chunking and Locally Anchored Flow Matching for Coherent Visuomotor Policy</a></td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>flow matching / diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进动作表示和解码</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66520">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62176">GeoMoLa: Geometry-Aware Motion Latents for Learning Robust Manipulation Policies</a></td>
<td nowrap>-</td>
<td nowrap>AR / Tokenization</td>
<td nowrap>action representation / 动作表示/tokenization</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62176">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2604.04161">Adaptive Action Chunking at Inference-time for Vision-Language-Action Models</a></td>
<td nowrap>-</td>
<td nowrap>Tokenization</td>
<td nowrap>VLA / 动作表示/tokenization</td>
<td nowrap>adaptive action chunking via action entropy</td>
<td nowrap>-</td>
<td nowrap>Sim + Real</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://arxiv.org/abs/2604.04161">paper</a></td>
<td nowrap><a href="https://lance-lot.github.io/adaptive-chunking.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2603.10158">XL-VLA: Cross-Hand Latent Representation for Vision-Language-Action Models</a></td>
<td nowrap>-</td>
<td nowrap>Tokenization</td>
<td nowrap>VLA / 动作表示/tokenization</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://arxiv.org/abs/2603.10158">paper</a></td>
<td nowrap><a href="https://xl-vla.github.io/">project</a></td>
<td nowrap><a href="https://github.com/EmptyBlueBox/DexLatent">💻</a></td>
<td nowrap>-</td>
<td nowrap>Efficient-VLA</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.16685">Compliant Residual DAgger: Improving Real-World Contact-Rich Manipulation with Human Corrections</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA / RL / RL/在线微调</td>
<td nowrap>DAgger</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2506.16685">paper</a></td>
<td nowrap><a href="https://compliant-residual-dagger.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2510.25138">Learning Spatial-Aware Manipulation Ordering</a></td>
<td nowrap>-</td>
<td nowrap>AR / Tokenization</td>
<td nowrap>VLA / 动作表示/tokenization</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2510.25138">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2509.15607">PRIMT: Preference-based Reinforcement Learning with Multimodal Feedback and Trajectory Synthesis from Foundation Models</a></td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>VLA / RL / RL/在线微调</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进动作表示和解码</td>
<td nowrap><a href="https://arxiv.org/abs/2509.15607">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2502.01218">Provable Ordering and Continuity in Vision-Language Pretraining for Generalizable Embodied Agents</a></td>
<td nowrap>-</td>
<td nowrap>Tokenization</td>
<td nowrap>VLA / 动作表示/tokenization</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进动作表示和解码</td>
<td nowrap><a href="https://arxiv.org/abs/2502.01218">paper</a></td>
<td nowrap><a href="https://actol-pretrain.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2508.05941">Latent Policy Barrier: Learning Robust Visuomotor Policies by Staying In-Distribution</a></td>
<td nowrap>-</td>
<td nowrap>AR / Tokenization</td>
<td nowrap>action representation / 动作表示/tokenization</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进动作表示和解码</td>
<td nowrap><a href="https://arxiv.org/abs/2508.05941">paper</a></td>
<td nowrap><a href="https://project-latentpolicybarrier.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2412.04445">Moto: Latent Motion Token as the Bridging Language for Learning Robot Manipulation from Videos</a></td>
<td nowrap>-</td>
<td nowrap>AR / Tokenization</td>
<td nowrap>VLA / action tokenization / 动作表示/tokenization</td>
<td nowrap>latent motion tokenizer + Moto-GPT autoregression</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2412.04445">paper</a></td>
<td nowrap><a href="https://chenyi99.github.io/moto/">project</a></td>
<td nowrap><a href="https://github.com/TencentARC/Moto">code</a></td>
<td nowrap><a href="https://huggingface.co/TencentARC/Moto">Moto weights</a></td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2411.14519">Tra-MoE: Learning Trajectory Prediction Model from Multiple Domains for Adaptive Policy Conditioning</a></td>
<td nowrap>-</td>
<td nowrap>AR / Tokenization</td>
<td nowrap>action representation / 动作表示/tokenization</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进动作表示和解码</td>
<td nowrap><a href="https://arxiv.org/abs/2411.14519">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/MCG-NJU/Tra-MoE">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
</tbody>
</table>

#### diffusion/flow policy

共 63 篇。

<table>
<thead>
<tr>
<th nowrap>会议/年份</th>
<th nowrap>论文/方法</th>
<th nowrap>Base VLA</th>
<th nowrap>Action</th>
<th nowrap>训练/反馈</th>
<th nowrap>Algorithm</th>
<th nowrap>Policy/Type</th>
<th nowrap>Sim/Real</th>
<th nowrap>问题/目标</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>来源</th>
<th nowrap>调研判断</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=H1KDMNOKQn">Unifying Diffusion and Autoregression for Generalizable Vision-Language-Action Model</a></td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://openreview.net/forum?id=H1KDMNOKQn">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=UvQOcw2oCD">Unified Diffusion VLA: Vision-Language-Action Model via Joint Discrete Diffusion Diffusion Process</a></td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://openreview.net/forum?id=UvQOcw2oCD">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>WAM</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=1vXMfIYFZp">Master Skill Learning with Policy-Grounded Synergy of LLM-based Reward Shaping and Exploring</a></td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://openreview.net/forum?id=1vXMfIYFZp">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=2RIqqNqALN">When would Vision-Proprioception Policies Fail in Robotic Manipulation?</a></td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://openreview.net/forum?id=2RIqqNqALN">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=AmczI1k3Yk">Capturing Visual Environment Structure Correlates with Control Performance</a></td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://openreview.net/forum?id=AmczI1k3Yk">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=BTe5VLBjPg">VITA: Vision-to-Action Flow Matching Policy</a></td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://openreview.net/forum?id=BTe5VLBjPg">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=BvirMuKWV1">When a Robot is More Capable than a Human: Learning from Constrained Demonstrators</a></td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://openreview.net/forum?id=BvirMuKWV1">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=FqDmvMZish">Autonomous Play with Correspondence-Driven Trajectory Warping</a></td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://openreview.net/forum?id=FqDmvMZish">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=IaGf8Eh5Uo">Reference Guided Skill Discovery</a></td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://openreview.net/forum?id=IaGf8Eh5Uo">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=KFu4p3pd11">Masked Generative Policy for Robotic Control</a></td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://openreview.net/forum?id=KFu4p3pd11">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=OeDwYtp8n1">Learning Video Generation for Robotic Manipulation with Collaborative Trajectory Control</a></td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://openreview.net/forum?id=OeDwYtp8n1">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=P9PVdWyM3U">Policy Contrastive Decoding for Robotic Foundation Models</a></td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://openreview.net/forum?id=P9PVdWyM3U">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=PL0tJOfm7I">Demystifying Robot Diffusion Policies: Action Memorization and a Simple Lookup Table Alternative</a></td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://openreview.net/forum?id=PL0tJOfm7I">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=Q1CP0iAmOb">H$^3$DP: Triply‑Hierarchical Diffusion Policy for Visuomotor Learning</a></td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>5 simulation benchmarks + real Galaxea R1</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://openreview.net/forum?id=Q1CP0iAmOb">paper</a></td>
<td nowrap><a href="https://lyy-iiis.github.io/h3dp/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=TnLFRhLuZ6">Compose Your Policies! Improving Diffusion-based or Flow-based Robot Policies via Test-time Distribution-level Composition</a></td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>GPC; test-time distribution-level policy composition</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://openreview.net/forum?id=TnLFRhLuZ6">paper</a></td>
<td nowrap><a href="https://sagecao1125.github.io/GPC-Site/">project</a></td>
<td nowrap><a href="https://github.com/SageCao1125/GPC">code</a></td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=VSWjHIveqZ">Abstracting Robot Manipulation Skills via Mixture-of-Experts Diffusion Policies</a></td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://openreview.net/forum?id=VSWjHIveqZ">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=WVliGyFwZv">Accelerated co-design of robots through morphological pretraining</a></td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://openreview.net/forum?id=WVliGyFwZv">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=aoorNQFpM6">VER: Vision Expert Transformer for Robot Learning via Foundation Distillation and Dynamic Routing</a></td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://openreview.net/forum?id=aoorNQFpM6">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Awesome-VLA</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=d08yOXs1Dl">SpikePingpong: Spike Vision-based Fast-Slow Pingpong Robot System</a></td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://openreview.net/forum?id=d08yOXs1Dl">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=dQ6d5bgXtM">Translating Flow to Policy via Hindsight Online Imitation</a></td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy / RL/在线微调</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://openreview.net/forum?id=dQ6d5bgXtM">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=eWe8zqGvs5">Cortical Policy: A Dual-Stream View Transformer for Robotic Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://openreview.net/forum?id=eWe8zqGvs5">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=iKJbmx1iuQ">Contractive Diffusion Policies: Robust Action Diffusion via Contractive Score-Based Sampling with Differential Equations</a></td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://openreview.net/forum?id=iKJbmx1iuQ">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=kIYNtxE13h">Scalable Exploration for High-Dimensional Continuous Control via Value-Guided Flow</a></td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://openreview.net/forum?id=kIYNtxE13h">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=w3Ik8HUyTT">ViPRA: Video Prediction for Robot Actions</a></td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://openreview.net/forum?id=w3Ik8HUyTT">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=AcTsKglDdh">DataMIL: Selecting Data for Robot Imitation Learning with Datamodels</a></td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://openreview.net/forum?id=AcTsKglDdh">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=COrUdVuInH">MIMIC: Mask-Injected Manipulation Video Generation with Interaction Control</a></td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://openreview.net/forum?id=COrUdVuInH">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>WAM</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=CiZMMAFQR3">LeRobot: An Open-Source Library for End-to-End Robot Learning</a></td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>simulation + real hardware</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://openreview.net/forum?id=CiZMMAFQR3">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/huggingface/lerobot">code</a></td>
<td nowrap><a href="https://huggingface.co/lerobot">LeRobotDataset / HF Hub</a></td>
<td nowrap>EAI-VLA-VLN, Awesome-VLA, Efficient-VLA, Robot-Learning, WAM</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38881">ManiLong-Shot: Interaction-Aware One-Shot Imitation Learning for Long-Horizon Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38881">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38889">Learning Diffusion Policy from Primitive Skills for Robot Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38889">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38912">Intention-Aware Diffusion Model for Pedestrian Trajectory Prediction</a></td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38912">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Humanoid-RL</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38919">MP1: MeanFlow Tames Policy Learning in 1-step for Robotic Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38919">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38934">ForeDiffusion: Foresight-Conditioned Diffusion Policy via Future View Construction for Robot Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38934">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38944">Balancing Signal and Variance: Adaptive Offline RL Post-Training for VLA Flow Models</a></td>
<td nowrap>π₀</td>
<td nowrap>Flow</td>
<td nowrap>diffusion/flow policy / RL/在线微调 / Reward D</td>
<td nowrap>ARFM</td>
<td nowrap>Off-Policy / MF</td>
<td nowrap>Sim ✓ / Real ✓</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38944">paper</a> / <a href="https://arxiv.org/pdf/2509.04063">ARFM</a> / <a href="https://arxiv.org/abs/2509.04063">Balancing Signal and Variance: Adaptive Offline RL Post-Training for VLA Flow Models</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Efficient-VLA, RL-VLA</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38950">Bridging Scale Discrepancies in Robotic Control via Language-Based Action Representations</a></td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38950">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38959">D²PPO: Diffusion Policy Policy Optimization with Dispersive Loss</a></td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>PPO</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38959">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62902">Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies</a></td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>VLA / diffusion policy / diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62902">paper</a> / <a href="https://arxiv.org/abs/2508.20072">Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN, Efficient-VLA</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61717">STEP: Warm-Started Visuomotor Policies with Spatiotemporal Consistency Prediction</a></td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61717">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>HCP-Survey, EAI-VLA-VLN, Humanoid-RL</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61049">Learning Human-Robot Collaboration via Heterogeneous-Agent Lyapunov Policy Optimization</a></td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Sim/Benchmark</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61049">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2511.15605">SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models</a></td>
<td nowrap>OpenVLA* / π₀ / π₀-Fast</td>
<td nowrap>AR / Flow</td>
<td nowrap>VLA / RL/在线微调 / Reward D</td>
<td nowrap>SRPO</td>
<td nowrap>Hybrid / MF (MB-Reward but MF-RL)</td>
<td nowrap>Sim ✓(MT) / Real ✓(MT)</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://arxiv.org/abs/2511.15605">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/sii-research/siiRL">🔗</a></td>
<td nowrap>-</td>
<td nowrap>WAM, RL-VLA</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2507.01961">AC-DiT: Adaptive Coordination Diffusion Transformer for Mobile Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>VLA / diffusion policy / diffusion transformer / diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2507.01961">paper</a></td>
<td nowrap><a href="https://ac-dit.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2510.20406">PointMapPolicy: Structured Point Cloud Processing for Multi-Modal Imitation Learning</a></td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>VLA / diffusion/flow policy</td>
<td nowrap>PPO</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://arxiv.org/abs/2510.20406">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap>Emerging Risks from Embodied AI Require Urgent Policy Action</td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-Safety</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.07127">Human-assisted Robotic Policy Refinement via Action Preference Optimization</a></td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://arxiv.org/abs/2506.07127">paper</a></td>
<td nowrap><a href="https://gewu-lab.github.io/action_preference_optimization/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap>*Hyper-GoalNet*: Goal-Conditioned Manipulation Policy Learning with HyperNetworks</td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2505.22094">ReinFlow: Fine-tuning Flow Matching Policy with Online Reinforcement Learning</a></td>
<td nowrap>-</td>
<td nowrap>AR / Flow</td>
<td nowrap>flow matching / RL / RL/在线微调</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://arxiv.org/abs/2505.22094">paper</a></td>
<td nowrap><a href="https://reinflow.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>RL-VLA</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2505.13431">A Practical Guide for Incorporating Symmetry in Diffusion Policy</a></td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion policy / diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://arxiv.org/abs/2505.13431">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2509.25822">Act to See, See to Act: Diffusion-Driven Perception-Action Interplay for Adaptive Policies</a></td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion policy / diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://arxiv.org/abs/2509.25822">paper</a></td>
<td nowrap><a href="https://jingwang18.github.io/dp-ag.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2511.20906">Dynamic Test-Time Compute Scaling in Control Policy: Difficulty-Aware Stochastic Interpolant Policy</a></td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://arxiv.org/abs/2511.20906">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.13922">DynaGuide: Steering Diffusion Polices with Active Dynamic Guidance</a></td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion policy / diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://arxiv.org/abs/2506.13922">paper</a></td>
<td nowrap><a href="https://dynaguide.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.19757">Dita: Scaling Diffusion Transformer for Generalist Vision-Language-Action Policy</a></td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>VLA / diffusion policy / diffusion transformer / diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>LIBERO + SimplerEnv + real Franka</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://arxiv.org/abs/2503.19757">paper</a></td>
<td nowrap><a href="https://robodita.github.io/">project</a></td>
<td nowrap><a href="https://github.com/RoboDita/Dita">code</a></td>
<td nowrap><a href="https://robodita.github.io/">model checkpoints</a></td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/1571">SD2Actor: Continuous State Decomposition via Diffusion Embeddings for Robotic Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>VLA / diffusion policy / diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/1571">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2507.06224">EC-Flow: Enabling Versatile Robotic Manipulation from Action-Unlabeled Videos via Embodiment-Centric Flow</a></td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>flow matching / diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Sim/Benchmark</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2507.06224">paper</a></td>
<td nowrap><a href="https://ec-flow1.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.13217">Dense Policy: Bidirectional Autoregressive Learning of Actions</a></td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>autoregressive policy / diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://arxiv.org/abs/2503.13217">paper</a></td>
<td nowrap><a href="https://selen-suyue.github.io/DspNet/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2507.06710">Spatial-Temporal Aware Visuomotor Diffusion Policy Learning</a></td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>diffusion policy / diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://arxiv.org/abs/2507.06710">paper</a></td>
<td nowrap><a href="https://zhenyangliu.github.io/DP4/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>HCP-Survey, EAI-VLA-VLN, Awesome-VLA, EAI-Safety</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2507.04331">Wavelet Policy: Lifting Scheme for Policy Learning in Long-Horizon Tasks</a></td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://arxiv.org/abs/2507.04331">paper</a></td>
<td nowrap><a href="https://hhuang-code.github.io/wavelet_policy/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICML 2025</td>
<td nowrap>Flow-based Domain Randomization for Learning and Sequencing Robotic Skills</td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>flow matching / diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://arxiv.org/pdf/2502.01800">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN, Efficient-VLA, EAI-ROS</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICML 2025</td>
<td nowrap>Learning Policy Committees for Effective Personalization in MDPs with Diverse Tasks</td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://arxiv.org/abs/2503.01885">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2411.18623">Lift3D Policy: Lifting 2D Foundation Models for Robust 3D Robotic Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>3D representation / diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>simulation benchmarks + real FR3</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2411.18623">paper</a></td>
<td nowrap><a href="https://lift3d-web.github.io/">project</a></td>
<td nowrap><a href="https://github.com/PKU-HMI-Lab/LIFT3D">code</a></td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap>PDFactor: Learning Tri-Perspective View Policy Diffusion Field for Multi-Task Robotic Manipulation</td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>diffusion policy / diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap>FlowRAM: Grounding Flow Matching Policy with Region-Aware Mamba Framework for Robotic Manipulation</td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>flow matching / diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2506.16201">FlowRAM: Grounding Flow Matching Policy with Region-Aware Mamba Framework for Robotic Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Efficient-VLA</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2411.18369">G3Flow: Generative 3D Semantic Flow for Pose-aware and Generalizable Object Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>flow matching / 3D representation / diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2411.18369">paper</a></td>
<td nowrap><a href="https://tianxingchen.github.io/G3Flow/">project</a></td>
<td nowrap><a href="https://github.com/TianxingChen/G3Flow">code</a></td>
<td nowrap>RoboTwin_Benchmark tasks</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2412.03142">AffordDP: Generalizable Diffusion Policy with Transferable Affordance</a></td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion policy / affordance / diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Sim + Real</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap><a href="https://arxiv.org/abs/2412.03142">paper</a></td>
<td nowrap><a href="https://afforddp.github.io/">project</a></td>
<td nowrap><a href="https://github.com/SshiJwu/AffordDP">code</a></td>
<td nowrap><a href="https://afforddp.github.io/">simulation data</a></td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap>Touch2Shape: Touch-Conditioned 3D Diffusion for Shape Exploration and Reconstruction</td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion policy / 3D representation / diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升连续动作生成质量</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
</tbody>
</table>

#### 3D grounding

共 28 篇。

<table>
<thead>
<tr>
<th nowrap>会议/年份</th>
<th nowrap>论文/方法</th>
<th nowrap>Base VLA</th>
<th nowrap>Action</th>
<th nowrap>训练/反馈</th>
<th nowrap>Algorithm</th>
<th nowrap>Policy/Type</th>
<th nowrap>Sim/Real</th>
<th nowrap>问题/目标</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>来源</th>
<th nowrap>调研判断</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=7M6ryCABIc">PixelVLA: Advancing Pixel-level Understanding in Vision-Language-Action Model</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>3D representation / 3D grounding</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>增强空间理解和操作定位</td>
<td nowrap><a href="https://openreview.net/forum?id=7M6ryCABIc">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=eKhOrQWAVJ">Spatially Guided Training for Vision-Language-Action Model</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>3D representation / 3D grounding</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>增强空间理解和操作定位</td>
<td nowrap><a href="https://openreview.net/forum?id=eKhOrQWAVJ">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=euMVC1DO4k">Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>3D representation / 3D grounding</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>增强空间理解和操作定位</td>
<td nowrap><a href="https://openreview.net/forum?id=euMVC1DO4k">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=fzmittHfq3">From Spatial to Actions: Grounding Vision-Language-Action Model in Spatial Foundation Priors</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>3D representation / 3D grounding</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>增强空间理解和操作定位</td>
<td nowrap><a href="https://openreview.net/forum?id=fzmittHfq3">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=18gC6pZVVc">Geometry-aware 4D Video Generation for Robot Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>3D representation / 3D grounding</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>增强空间理解和操作定位</td>
<td nowrap><a href="https://openreview.net/forum?id=18gC6pZVVc">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>HCP-Survey, Awesome-EAI, Humanoid-RL, WAM</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=WXFfMLyB6y">Generalizable Coarse-to-Fine Robot Manipulation via Language-Aligned 3D Keypoints</a></td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>3D representation / 3D grounding</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>增强空间理解和操作定位</td>
<td nowrap><a href="https://openreview.net/forum?id=WXFfMLyB6y">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=ggofj6tyr3">Geometry-aware Policy Imitation</a></td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>3D representation / 3D grounding</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>增强空间理解和操作定位</td>
<td nowrap><a href="https://openreview.net/forum?id=ggofj6tyr3">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>HCP-Survey, Awesome-EAI, Humanoid-RL, WAM</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=qXfRXfAHOK">Learning Part-Aware Dense 3D Feature Field For Generalizable Articulated Object Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>3D representation / 3D grounding</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>增强空间理解和操作定位</td>
<td nowrap><a href="https://openreview.net/forum?id=qXfRXfAHOK">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=z8BN7KyaPl">RAVEN: End-to-end Equivariant Robot Learning with RGB Cameras</a></td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>3D representation / 3D grounding</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>增强空间理解和操作定位</td>
<td nowrap><a href="https://openreview.net/forum?id=z8BN7KyaPl">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=DE5ZJtR4bg">On the Generalization Capacities of MLLMs for Spatial Intelligence</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>3D representation / 3D grounding</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>增强空间理解和操作定位</td>
<td nowrap><a href="https://openreview.net/forum?id=DE5ZJtR4bg">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38921">ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>3D representation / 3D grounding</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>增强空间理解和操作定位</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38921">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38939">Indoor Multi-View Radar Object Detection via 3D Bounding Box Diffusion</a></td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>3D representation / diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>增强空间理解和操作定位</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38939">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38946">RaLD: Generating High-Resolution 3D Radar Point Clouds with Latent Diffusion</a></td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>3D representation / diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>增强空间理解和操作定位</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38946">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38947">Grounding Actions in Camera Space: Observation-Centric Vision-Language-Action Policy</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>3D representation / 3D grounding</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>增强空间理解和操作定位</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38947">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2510.24261">DynaRend: Learning 3D Dynamics via Masked Future Rendering for Robotic Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>3D representation / 3D grounding</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2510.24261">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://neurips.cc/virtual/2025/loc/san-diego/poster/118141">Building 3D Representations and Generating Motions From a Single Image via Video-Generation</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>3D representation / 3D grounding</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>增强空间理解和操作定位</td>
<td nowrap><a href="https://neurips.cc/virtual/2025/loc/san-diego/poster/118141">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2504.12636">A0: An Affordance-Aware Hierarchical Model for General Robotic Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>VLA / affordance / 3D grounding</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2504.12636">paper</a></td>
<td nowrap><a href="https://a-embodied.github.io/A0/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2408.10123v1">Learning Precise Affordances from Egocentric Videos for Robotic Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>affordance / 3D grounding</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2408.10123v1">paper</a></td>
<td nowrap><a href="https://reagan1311.github.io/affgrasp">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2412.04380">EmbodiedOcc: Embodied 3D Occupancy Prediction for Vision-based Online Scene Understanding</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>3D representation / RL/在线微调</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>增强空间理解和操作定位</td>
<td nowrap><a href="https://arxiv.org/abs/2412.04380">paper</a></td>
<td nowrap><a href="https://ykiwu.github.io/EmbodiedOcc/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2504.08531">Embodied Image Captioning: Self-supervised Learning Agents for Spatially Coherent Image Descriptions</a></td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>3D grounding</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>增强空间理解和操作定位</td>
<td nowrap><a href="https://arxiv.org/abs/2504.08531">paper</a></td>
<td nowrap><a href="https://hsp-iit.github.io/embodied-captioning/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICML 2025</td>
<td nowrap>Unifying 2D and 3D Vision-Language Understanding</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>3D representation / 3D grounding</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>增强空间理解和操作定位</td>
<td nowrap><a href="https://arxiv.org/abs/2503.10745">paper</a></td>
<td nowrap><a href="https://univlg.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICML 2025</td>
<td nowrap>GAPrompt: Geometry-Aware Point Cloud Prompt for 3D Vision Model</td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>3D representation / 3D grounding</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>增强空间理解和操作定位</td>
<td nowrap><a href="https://arxiv.org/abs/2505.04119">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/zhoujiahuan1991/ICML2025-GAPrompt">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2412.00174">SOLAMI: Social Vision-Language-Action Modeling for Immersive Interaction with 3D Autonomous Characters</a></td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>VLA / 3D representation / 3D grounding</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://arxiv.org/abs/2412.00174">paper</a></td>
<td nowrap><a href="https://solami-ai.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2501.03841">OmniManip: Towards General Robotic Manipulation via Object-Centric Interaction Primitives as Spatial Constraints</a></td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>VLA / 3D grounding</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2501.03841">paper</a></td>
<td nowrap><a href="https://omnimanip.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap>RoboGround: Robot Manipulation with Grounded Vision-Language Priors</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA / 3D grounding</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2406.18158">3D-MVP: 3D Multiview Pretraining for Robotic Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>3D representation / 3D grounding</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2406.18158">paper</a></td>
<td nowrap><a href="https://jasonqsy.github.io/3DMVP/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.07135">VidBot: Learning Generalizable 3D Actions from In-the-Wild 2D Human Videos for Zero-Shot Robotic Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>3D representation / 3D grounding</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2503.07135">paper</a></td>
<td nowrap><a href="https://hanzhic.github.io/vidbot-project/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2412.05507">AutoURDF: Unsupervised Robot Modeling from Point Cloud Frames Using Cluster Registration</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>3D grounding</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>增强空间理解和操作定位</td>
<td nowrap><a href="https://arxiv.org/abs/2412.05507">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/jl6017/AutoURDF">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
</tbody>
</table>

#### online/RL fine-tuning

共 12 篇。

<table>
<thead>
<tr>
<th nowrap>会议/年份</th>
<th nowrap>论文/方法</th>
<th nowrap>Base VLA</th>
<th nowrap>Action</th>
<th nowrap>训练/反馈</th>
<th nowrap>Algorithm</th>
<th nowrap>Policy/Type</th>
<th nowrap>Sim/Real</th>
<th nowrap>问题/目标</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>来源</th>
<th nowrap>调研判断</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=ULTWUuGhC3">Interleave-VLA: Enhancing Robot Manipulation with Image-Text Interleaved Instructions</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA / RL / RL/在线微调</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>SIMPLER + VIMA-Bench + real FANUC</td>
<td nowrap>通过在线优化提升策略</td>
<td nowrap><a href="https://openreview.net/forum?id=ULTWUuGhC3">paper</a></td>
<td nowrap><a href="https://interleave-vla.github.io/Interleave-VLA-Anonymous/">project</a></td>
<td nowrap>-</td>
<td nowrap>Interleaved X-Embodiment; 210k trajectories</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=eUGoqrZ6Ea">Self-Improving Vision-Language-Action Models with Data Generation via Residual RL</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA / RL / RL/在线微调</td>
<td nowrap>PLD residual RL + SFT distillation</td>
<td nowrap>Off-policy residual RL</td>
<td nowrap>LIBERO + SimplerEnv + real Franka/YAM</td>
<td nowrap>通过在线优化提升策略</td>
<td nowrap><a href="https://openreview.net/forum?id=eUGoqrZ6Ea">paper</a></td>
<td nowrap><a href="https://wenlixiao.com/self-improve-VLA-PLD">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, EAI-Safety, WAM, RL-VLA</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=sFO9d6XSlf">Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA / RL / RL/在线微调</td>
<td nowrap>VLM2VLA; language action representation + LoRA</td>
<td nowrap>-</td>
<td nowrap>800+ real robot experiments</td>
<td nowrap>通过在线优化提升策略</td>
<td nowrap><a href="https://openreview.net/forum?id=sFO9d6XSlf">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/irom-princeton/vlm2vla">code</a></td>
<td nowrap><a href="https://huggingface.co/AasherH/vlm2vla">adapter</a></td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=GrsoLVNy3Y">Cross-Embodiment Offline Reinforcement Learning for Heterogeneous Robot Datasets</a></td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>VLA / RL / RL/在线微调</td>
<td nowrap>offline RL + morphology grouping</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>通过在线优化提升策略</td>
<td nowrap><a href="https://openreview.net/forum?id=GrsoLVNy3Y">paper</a></td>
<td nowrap><a href="https://haruki-abe.github.io/cross_embodiment_offline_rl_website">project</a></td>
<td nowrap>-</td>
<td nowrap>16 robot-platform locomotion dataset suite</td>
<td nowrap>HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Humanoid-RL, WAM</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=ITeuGb2bYg">Policy Likelihood-based Query Sampling and Critic-Exploited Reset for Efficient Preference-based Reinforcement Learning</a></td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>VLA / RL / RL/在线微调</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>通过在线优化提升策略</td>
<td nowrap><a href="https://openreview.net/forum?id=ITeuGb2bYg">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=TQhSodCM4r">SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning</a></td>
<td nowrap>OpenVLA-OFT</td>
<td nowrap>AR</td>
<td nowrap>VLA / RL / RL/在线微调 / Reward S</td>
<td nowrap>GRPO</td>
<td nowrap>On-Policy / MF</td>
<td nowrap>Sim ✓ (MT) / Real ✓ (ST)</td>
<td nowrap>通过在线优化提升策略</td>
<td nowrap><a href="https://openreview.net/forum?id=TQhSodCM4r">paper</a> / <a href="https://arxiv.org/pdf/2509.09674">SimpleVLA-RL</a> / <a href="https://arxiv.org/abs/2509.09674">SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/PRIME-RL/SimpleVLA-RL">🔗</a></td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN, Efficient-VLA, RL-VLA</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=uWJwQ5SZoM">Robust Fine-tuning of Vision-Language-Action Robot Policies via Parameter Merging</a></td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>VLA / RL / RL/在线微调</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>通过在线优化提升策略</td>
<td nowrap><a href="https://openreview.net/forum?id=uWJwQ5SZoM">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=dc90uPqxWF">World2Minecraft: Occupancy-Driven simulated scenes Construction</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA / RL / RL/在线微调</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>通过在线优化提升策略</td>
<td nowrap><a href="https://openreview.net/forum?id=dc90uPqxWF">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38876">Steering Visuomotor Policy in Open Worlds via Cross-View Goal Alignment</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA / RL / RL/在线微调</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>通过在线优化提升策略</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38876">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap>HIER: Human-in-the-Loop Imagination-Execution Refinement for General Real-World Vision-Language-Action Models</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA / RL / RL/在线微调</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap>Real-World Reinforcement Learning of Active Perception Behaviors</td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>RL / RL/在线微调</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>通过在线优化提升策略</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Efficient-VLA, Robot-Learning, Humanoid-RL, EAI-Safety, WAM, RL-VLA</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICML 2025</td>
<td nowrap>ReinboT: Amplifying Robot Visual-Language Manipulation with Reinforcement Learning</td>
<td nowrap>ReinboT</td>
<td nowrap>AR</td>
<td nowrap>VLA / RL / RL/在线微调</td>
<td nowrap>DT + RTG</td>
<td nowrap>Off-Policy / MF</td>
<td nowrap>Sim + Real</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2505.07395">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/COST-97/reinboT">code</a></td>
<td nowrap>-</td>
<td nowrap>RL-VLA</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
</tbody>
</table>

#### 安全鲁棒性

共 3 篇。

<table>
<thead>
<tr>
<th nowrap>会议/年份</th>
<th nowrap>论文/方法</th>
<th nowrap>Base VLA</th>
<th nowrap>Action</th>
<th nowrap>训练/反馈</th>
<th nowrap>Algorithm</th>
<th nowrap>Policy/Type</th>
<th nowrap>Sim/Real</th>
<th nowrap>问题/目标</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>来源</th>
<th nowrap>调研判断</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=cS6xizdYD5">On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations</a></td>
<td nowrap>π0 / OpenVLA</td>
<td nowrap>-</td>
<td nowrap>VLA / safety / 安全鲁棒</td>
<td nowrap>RobustVLA; 17 perturbations across 4 modalities</td>
<td nowrap>-</td>
<td nowrap>LIBERO + real FR5</td>
<td nowrap>评估鲁棒性和安全性</td>
<td nowrap><a href="https://openreview.net/forum?id=cS6xizdYD5">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/gakakulicc/RobustVLA">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2505.16640">BadVLA: Towards Backdoor Attacks on Vision-Language-Action Models via Objective-Decoupled Optimization</a></td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>VLA / 安全鲁棒</td>
<td nowrap>objective-decoupled backdoor attack</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://arxiv.org/abs/2505.16640">paper</a></td>
<td nowrap><a href="https://badvla-project.github.io/">project</a></td>
<td nowrap><a href="https://github.com/Zxy-MLlab/BadVLA">project</a></td>
<td nowrap><a href="https://huggingface.co/datasets/Lostgreen/BadVLA">BadVLA dataset</a></td>
<td nowrap>EAI-Safety</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2411.13587">Exploring the Adversarial Vulnerabilities of Vision-Language-Action Models in Robotics</a></td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>VLA / 安全鲁棒</td>
<td nowrap>UADA / UPA / TMA adversarial attacks</td>
<td nowrap>-</td>
<td nowrap>simulation + physical setup</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://arxiv.org/abs/2411.13587">paper</a></td>
<td nowrap><a href="https://vlaattacker.github.io/">project</a></td>
<td nowrap><a href="https://github.com/William-wAng618/roboticAttack">code</a></td>
<td nowrap>LIBERO + BridgeData V2 attack assets</td>
<td nowrap>EAI-Safety</td>
<td nowrap>用于比较 VLA 在泛化、动作表示和执行稳定性上的进展。</td>
</tr>
</tbody>
</table>

### WAM / 世界模型

WAM 将未来世界状态预测和动作生成合在一起，适合放在 agent 规划和低层控制之间。它的价值不是替代所有控制器，而是提供可想象、可验证、可恢复的中间层。

子方向：cascaded WAM、joint WAM、video/latent world model、world model for VLA、world model evaluation。

共 46 篇。

<table>
<thead>
<tr>
<th nowrap>子方向</th>
<th nowrap>条目数</th>
<th nowrap>观察重点</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>cascaded WAM</td>
<td nowrap>23</td>
<td nowrap>看先想象后执行的分层链路。</td>
</tr>
<tr>
<td nowrap>joint WAM</td>
<td nowrap>3</td>
<td nowrap>看视觉、状态和动作的联合建模。</td>
</tr>
<tr>
<td nowrap>video/latent world model</td>
<td nowrap>13</td>
<td nowrap>看未来视频或隐状态预测质量。</td>
</tr>
<tr>
<td nowrap>world model for VLA</td>
<td nowrap>7</td>
<td nowrap>看世界模型如何服务 VLA 决策。</td>
</tr>
</tbody>
</table>

#### cascaded WAM

共 23 篇。

<table>
<thead>
<tr>
<th nowrap>会议/年份</th>
<th nowrap>论文/方法</th>
<th nowrap>WAM 类型</th>
<th nowrap>状态表示</th>
<th nowrap>动作接口</th>
<th nowrap>用途</th>
<th nowrap>Sim/Real</th>
<th nowrap>问题/目标</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>来源</th>
<th nowrap>调研判断</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=748bHL2BAv">Ctrl-World: A Controllable Generative World Model for Robot Manipulation</a></td>
<td nowrap>cascaded WAM</td>
<td nowrap>world model</td>
<td nowrap>world model / RL / cascaded WAM</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap>-</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap><a href="https://openreview.net/forum?id=748bHL2BAv">paper</a></td>
<td nowrap><a href="https://ctrl-world.github.io/">project</a></td>
<td nowrap><a href="https://github.com/Robert-gyj/Ctrl-World">code</a></td>
<td nowrap><a href="https://huggingface.co/yjguo/Ctrl-World">model/data</a></td>
<td nowrap>WAM</td>
<td nowrap>用于判断世界预测是否能服务规划和动作验证。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=0GNBqoYcAP">Context and Diversity Matter: The Emergence of In-Context Learning in World Models</a></td>
<td nowrap>cascaded WAM</td>
<td nowrap>world model</td>
<td nowrap>-</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap>-</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap><a href="https://openreview.net/forum?id=0GNBqoYcAP">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断世界预测是否能服务规划和动作验证。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=4HZgkwVVFO">NeMo-map: Neural Implicit Flow Fields for Spatio-Temporal Motion Mapping</a></td>
<td nowrap>cascaded WAM</td>
<td nowrap>world model</td>
<td nowrap>-</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap>-</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap><a href="https://openreview.net/forum?id=4HZgkwVVFO">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断世界预测是否能服务规划和动作验证。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=8UZpmrxoLG">Astra: General Interactive World Model with Autoregressive Denoising</a></td>
<td nowrap>cascaded WAM</td>
<td nowrap>world model</td>
<td nowrap>-</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap>-</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap><a href="https://openreview.net/forum?id=8UZpmrxoLG">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断世界预测是否能服务规划和动作验证。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=LQD1MrnbxH">Test-Time Mixture of World Models for Embodied Agents in Dynamic Environments</a></td>
<td nowrap>cascaded WAM</td>
<td nowrap>world model</td>
<td nowrap>-</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap>-</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap><a href="https://openreview.net/forum?id=LQD1MrnbxH">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Humanoid-RL, EAI-Safety, WAM, RL-VLA</td>
<td nowrap>用于判断世界预测是否能服务规划和动作验证。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=MPabX9LEds">Learning Massively Multitask World Models for Continuous Control</a></td>
<td nowrap>cascaded WAM</td>
<td nowrap>world model</td>
<td nowrap>world model / RL / cascaded WAM</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap>-</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap><a href="https://openreview.net/forum?id=MPabX9LEds">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断世界预测是否能服务规划和动作验证。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=a1zfcaNTkM">ExoPredicator: Learning Abstract Models of Dynamic Worlds for Robot Planning</a></td>
<td nowrap>cascaded WAM</td>
<td nowrap>world model</td>
<td nowrap>-</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap>-</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap><a href="https://openreview.net/forum?id=a1zfcaNTkM">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断世界预测是否能服务规划和动作验证。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=oBXfPyi47m">Efficient Reinforcement Learning by Guiding World Models with Non-Curated Data</a></td>
<td nowrap>cascaded WAM</td>
<td nowrap>world model</td>
<td nowrap>-</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap>-</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap><a href="https://openreview.net/forum?id=oBXfPyi47m">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断世界预测是否能服务规划和动作验证。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=qmEyJadwHA">Object-Centric World Models from Few-Shot Annotations for Sample-Efficient Reinforcement Learning</a></td>
<td nowrap>cascaded WAM</td>
<td nowrap>world model</td>
<td nowrap>-</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap>-</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap><a href="https://openreview.net/forum?id=qmEyJadwHA">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Efficient-VLA, Robot-Learning, Humanoid-RL, EAI-Safety</td>
<td nowrap>用于判断世界预测是否能服务规划和动作验证。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=w3w7WVG4ks">Building spatial world models from sparse transitional episodic memories</a></td>
<td nowrap>cascaded WAM</td>
<td nowrap>world model</td>
<td nowrap>-</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap>-</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap><a href="https://openreview.net/forum?id=w3w7WVG4ks">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断世界预测是否能服务规划和动作验证。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=yDmb7xAfeb">WoW!: World Models in a Closed-Loop World</a></td>
<td nowrap>cascaded WAM</td>
<td nowrap>world model</td>
<td nowrap>-</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap>-</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap><a href="https://openreview.net/forum?id=yDmb7xAfeb">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>WAM</td>
<td nowrap>用于判断世界预测是否能服务规划和动作验证。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=Patx6MRipw">ENACT: Evaluating Embodied Cognition with World Modeling of Egocentric Interaction</a></td>
<td nowrap>cascaded WAM</td>
<td nowrap>world model</td>
<td nowrap>world model / RL / cascaded WAM</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap>-</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap><a href="https://openreview.net/forum?id=Patx6MRipw">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断世界预测是否能服务规划和动作验证。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/63978">Cross-Embodiment Robot Foundation World Models with Latent Actions</a></td>
<td nowrap>cascaded WAM</td>
<td nowrap>latent</td>
<td nowrap>world model / RL / cascaded WAM</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap>-</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/63978">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Humanoid-RL, WAM</td>
<td nowrap>用于判断世界预测是否能服务规划和动作验证。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62480">DDP-WM: Disentangled Dynamics Prediction for Efficient World Models</a></td>
<td nowrap>cascaded WAM</td>
<td nowrap>world model</td>
<td nowrap>-</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap>-</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62480">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断世界预测是否能服务规划和动作验证。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62543">RoboFlow4D: A Lightweight Flow World Model Toward Real-Time Flow-Guided Robotic Manipulation</a></td>
<td nowrap>cascaded WAM</td>
<td nowrap>4D</td>
<td nowrap>-</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap>-</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62543">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断世界预测是否能服务规划和动作验证。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64209">Learning Task-Sufficient World Models by Synergizing Agentic Exploration and Structured Modeling</a></td>
<td nowrap>cascaded WAM</td>
<td nowrap>world model</td>
<td nowrap>-</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap>-</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64209">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断世界预测是否能服务规划和动作验证。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2509.15536">SAMPO: Scale-wise Autoregression with Motion Prompt for Generative World Models</a></td>
<td nowrap>cascaded WAM</td>
<td nowrap>world model</td>
<td nowrap>-</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap>-</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap><a href="https://arxiv.org/abs/2509.15536">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断世界预测是否能服务规划和动作验证。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2505.05495">Learning 3D Persistent Embodied World Models</a></td>
<td nowrap>cascaded WAM</td>
<td nowrap>3D</td>
<td nowrap>-</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap>-</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap><a href="https://arxiv.org/abs/2505.05495">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断世界预测是否能服务规划和动作验证。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2505.20425">OSVI-WM: One-Shot Visual Imitation for Unseen Tasks using World-Model-Guided Trajectory Generation</a></td>
<td nowrap>cascaded WAM</td>
<td nowrap>world model</td>
<td nowrap>-</td>
<td nowrap>先预测未来再推导动作</td>
<td nowrap>-</td>
<td nowrap>先预测未来再推导动作</td>
<td nowrap><a href="https://arxiv.org/abs/2505.20425">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断世界预测是否能服务规划和动作验证。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2406.14540">IRASim: A Fine-Grained World Model for Robot Manipulation</a></td>
<td nowrap>cascaded WAM</td>
<td nowrap>world model</td>
<td nowrap>-</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap>-</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap><a href="https://arxiv.org/abs/2406.14540">paper</a></td>
<td nowrap><a href="https://gen-irasim.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断世界预测是否能服务规划和动作验证。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://ziweiwangthu.github.io/data/GWM.pdf">GWM: Towards Scalable Gaussian World Models for Robotic Manipulation</a></td>
<td nowrap>cascaded WAM</td>
<td nowrap>3D</td>
<td nowrap>-</td>
<td nowrap>评测</td>
<td nowrap>Sim/Benchmark</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap>-</td>
<td nowrap><a href="https://gaussian-world-model.github.io/">project</a></td>
<td nowrap><a href="https://github.com/Gaussian-World-Model/gaussianwm">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断世界预测是否能服务规划和动作验证。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.16806">DyWA: Dynamics-adaptive World Action Model for Generalizable Non-prehensile Manipulation</a></td>
<td nowrap>cascaded WAM</td>
<td nowrap>world model</td>
<td nowrap>world model / RL / cascaded WAM</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2503.16806">paper</a></td>
<td nowrap><a href="https://pku-epic.github.io/DyWA/">project</a></td>
<td nowrap><a href="https://github.com/jiangranlv/DyWA">code</a></td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于判断世界预测是否能服务规划和动作验证。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://openreview.net/pdf?id=mnwlhvmKMN">Learning 4D Embodied World Models</a></td>
<td nowrap>cascaded WAM</td>
<td nowrap>4D</td>
<td nowrap>-</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap>-</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap><a href="https://openreview.net/pdf?id=mnwlhvmKMN">paper</a> / <a href="https://arxiv.org/pdf/2504.20995">📄 Paper</a></td>
<td nowrap><a href="https://tesseractworld.github.io/">🌍 Web</a></td>
<td nowrap><a href="https://github.com/UMass-Embodied-AGI/TesserAct">💻 Code</a></td>
<td nowrap><a href="https://huggingface.co/anyeZHY/tesseract">tesseract</a></td>
<td nowrap>WAM</td>
<td nowrap>用于判断世界预测是否能服务规划和动作验证。</td>
</tr>
</tbody>
</table>

#### joint WAM

共 3 篇。

<table>
<thead>
<tr>
<th nowrap>会议/年份</th>
<th nowrap>论文/方法</th>
<th nowrap>WAM 类型</th>
<th nowrap>状态表示</th>
<th nowrap>动作接口</th>
<th nowrap>用途</th>
<th nowrap>Sim/Real</th>
<th nowrap>问题/目标</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>来源</th>
<th nowrap>调研判断</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=IvUM6UwYCJ">Empowering Multi-Robot Cooperation via Sequential World Models</a></td>
<td nowrap>joint WAM</td>
<td nowrap>world model</td>
<td nowrap>-</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap>Sim + Real</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap><a href="https://openreview.net/forum?id=IvUM6UwYCJ">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/zhaozijie2022/seqwm-marl">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断世界预测是否能服务规划和动作验证。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64447">Dual-Stream Diffusion for World-Model Augmented Vision-Language-Action Model</a></td>
<td nowrap>joint WAM</td>
<td nowrap>world model</td>
<td nowrap>VLA / diffusion policy / world model / joint WAM</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64447">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN, WAM</td>
<td nowrap>用于判断世界预测是否能服务规划和动作验证。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2507.11296">Diffusion-Based Imaginative Coordination for Bimanual Manipulation</a></td>
<td nowrap>joint WAM</td>
<td nowrap>world model</td>
<td nowrap>diffusion policy / world model / RL / joint WAM</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap>Sim + Real</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2507.11296">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/return-sleep/Diffusion_based_imaginative_Coordination">code</a></td>
<td nowrap>-</td>
<td nowrap>Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Efficient-VLA, EAI-Safety, WAM</td>
<td nowrap>用于判断世界预测是否能服务规划和动作验证。</td>
</tr>
</tbody>
</table>

#### video/latent world model

共 13 篇。

<table>
<thead>
<tr>
<th nowrap>会议/年份</th>
<th nowrap>论文/方法</th>
<th nowrap>WAM 类型</th>
<th nowrap>状态表示</th>
<th nowrap>动作接口</th>
<th nowrap>用途</th>
<th nowrap>Sim/Real</th>
<th nowrap>问题/目标</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>来源</th>
<th nowrap>调研判断</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=3q9vHEqsNx">FantasyWorld: Geometry-Consistent World Modeling via Unified Video and 3D Prediction</a></td>
<td nowrap>video/latent world model</td>
<td nowrap>video latents + implicit 3D field</td>
<td nowrap>-</td>
<td nowrap>从视频或隐空间预测未来</td>
<td nowrap>-</td>
<td nowrap>从视频或隐空间预测未来</td>
<td nowrap><a href="https://openreview.net/forum?id=3q9vHEqsNx">paper</a></td>
<td nowrap><a href="https://fantasy-amap.github.io/fantasy-world/">project</a></td>
<td nowrap><a href="https://github.com/Fantasy-AMAP/fantasy-world">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断世界预测是否能服务规划和动作验证。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=NQq9JLMfNN">Unified 3D Scene Understanding Through Physical World Modeling</a></td>
<td nowrap>video/latent world model</td>
<td nowrap>video/latent</td>
<td nowrap>-</td>
<td nowrap>从视频或隐空间预测未来</td>
<td nowrap>-</td>
<td nowrap>从视频或隐空间预测未来</td>
<td nowrap><a href="https://openreview.net/forum?id=NQq9JLMfNN">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断世界预测是否能服务规划和动作验证。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=pFyzqbUiF9">Vid2World: Crafting Video Diffusion Models to Interactive World Models</a></td>
<td nowrap>video/latent world model</td>
<td nowrap>video/latent</td>
<td nowrap>-</td>
<td nowrap>从视频或隐空间预测未来</td>
<td nowrap>-</td>
<td nowrap>从视频或隐空间预测未来</td>
<td nowrap><a href="https://openreview.net/forum?id=pFyzqbUiF9">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断世界预测是否能服务规划和动作验证。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=wcTuZG9P2o">EgoWorld: Translating Exocentric View to Egocentric View using Rich Exocentric Observations</a></td>
<td nowrap>video/latent world model</td>
<td nowrap>video/latent</td>
<td nowrap>-</td>
<td nowrap>从视频或隐空间预测未来</td>
<td nowrap>-</td>
<td nowrap>从视频或隐空间预测未来</td>
<td nowrap><a href="https://openreview.net/forum?id=wcTuZG9P2o">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断世界预测是否能服务规划和动作验证。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38905">LiDARCrafter: Dynamic 4D World Modeling from LiDAR Sequences</a></td>
<td nowrap>video/latent world model</td>
<td nowrap>4D LiDAR sequence</td>
<td nowrap>-</td>
<td nowrap>从视频或隐空间预测未来</td>
<td nowrap>-</td>
<td nowrap>从视频或隐空间预测未来</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38905">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/worldbench/LiDARCrafter">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断世界预测是否能服务规划和动作验证。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/65193">DreamDojo: A Real-Time Robot World Model from Large-Scale Human Videos</a></td>
<td nowrap>video/latent world model</td>
<td nowrap>video/latent</td>
<td nowrap>-</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap>-</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/65193">paper</a></td>
<td nowrap><a href="https://dreamdojo-world.github.io/">project</a></td>
<td nowrap><a href="https://github.com/NVIDIA/DreamDojo">code</a></td>
<td nowrap><a href="https://huggingface.co/nvidia/DreamDojo">DreamDojo</a></td>
<td nowrap>Humanoid-RL, WAM</td>
<td nowrap>用于判断世界预测是否能服务规划和动作验证。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66091">From Imagined Futures to Executable Actions: Mixture of Latent Actions for Robot Manipulation</a></td>
<td nowrap>video/latent world model</td>
<td nowrap>video/latent</td>
<td nowrap>world model / RL / video/latent world model</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66091">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断世界预测是否能服务规划和动作验证。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap>VideoVLA: Video Generators Can Be Generalizable Robot Manipulators</td>
<td nowrap>video/latent world model</td>
<td nowrap>video/latent</td>
<td nowrap>VLA / video/latent world model</td>
<td nowrap>从视频或隐空间预测未来</td>
<td nowrap>Sim + Real</td>
<td nowrap>从视频或隐空间预测未来</td>
<td nowrap>-</td>
<td nowrap><a href="https://videovla-nips2025.github.io/">project</a></td>
<td nowrap><a href="https://github.com/VideoVLA-Project/VideoVLA">code</a></td>
<td nowrap><a href="https://huggingface.co/VideoVLA/VideoVLA_Cogvideobase_Pretrained">pretrained model</a></td>
<td nowrap>EAI-VLA-VLN, WAM</td>
<td nowrap>用于判断世界预测是否能服务规划和动作验证。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2501.01895">EnerVerse: Envisioning Embodied Future Space for Robotics Manipulation</a></td>
<td nowrap>video/latent world model</td>
<td nowrap>video/latent</td>
<td nowrap>VLA / video/latent world model</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2501.01895">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于判断世界预测是否能服务规划和动作验证。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2507.04447">DreamVLA: A Vision-Language-Action Model Dreamed with Comprehensive World Knowledge</a></td>
<td nowrap>video/latent world model</td>
<td nowrap>video/latent</td>
<td nowrap>VLA / RL / video/latent world model</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://arxiv.org/abs/2507.04447">paper</a></td>
<td nowrap><a href="https://zhangwenyao1.github.io/DreamVLA/index.html">project</a></td>
<td nowrap><a href="https://github.com/Zhangwenyao1/DreamVLA">code</a></td>
<td nowrap><a href="https://huggingface.co/WenyaoZhang/DreamVLA">DreamVLA</a></td>
<td nowrap>Awesome-VLA</td>
<td nowrap>用于判断世界预测是否能服务规划和动作验证。</td>
</tr>
<tr>
<td nowrap>ICML 2025</td>
<td nowrap>Video Prediction Policy: A Generalist Robot Policy with Predictive Visual Representations</td>
<td nowrap>video/latent world model</td>
<td nowrap>video/latent</td>
<td nowrap>video/latent world model</td>
<td nowrap>从视频或隐空间预测未来</td>
<td nowrap>-</td>
<td nowrap>从视频或隐空间预测未来</td>
<td nowrap><a href="https://arxiv.org/abs/2412.14803">paper</a></td>
<td nowrap><a href="https://video-prediction-policy.github.io/">project</a></td>
<td nowrap><a href="https://github.com/roboterax/video-prediction-policy">code</a></td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN, WAM</td>
<td nowrap>用于判断世界预测是否能服务规划和动作验证。</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.11423">TASTE-Rob: Advancing Video Generation of Task-Oriented Hand-Object Interaction for Generalizable Robotic Manipulation</a></td>
<td nowrap>video/latent world model</td>
<td nowrap>video/latent</td>
<td nowrap>video/latent world model</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2503.11423">paper</a></td>
<td nowrap><a href="https://taste-rob.github.io/">project</a></td>
<td nowrap><a href="https://github.com/GAP-LAB-CUHK-SZ/TASTE-Rob">code</a></td>
<td nowrap>TASTE-Rob dataset</td>
<td nowrap>-</td>
<td nowrap>用于判断世界预测是否能服务规划和动作验证。</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://cvpr.thecvf.com/virtual/2025/poster/34942">GraphMimic: Graph-to-Graphs Generative Modeling from Videos for Policy Learning</a></td>
<td nowrap>video/latent world model</td>
<td nowrap>video/latent</td>
<td nowrap>video/latent world model</td>
<td nowrap>从视频或隐空间预测未来</td>
<td nowrap>-</td>
<td nowrap>从视频或隐空间预测未来</td>
<td nowrap><a href="https://cvpr.thecvf.com/virtual/2025/poster/34942">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断世界预测是否能服务规划和动作验证。</td>
</tr>
</tbody>
</table>

#### world model for VLA

共 7 篇。

<table>
<thead>
<tr>
<th nowrap>会议/年份</th>
<th nowrap>论文/方法</th>
<th nowrap>WAM 类型</th>
<th nowrap>状态表示</th>
<th nowrap>动作接口</th>
<th nowrap>用途</th>
<th nowrap>Sim/Real</th>
<th nowrap>问题/目标</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>来源</th>
<th nowrap>调研判断</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=fHLtSxDFKC">Genie Envisioner: A Unified World Foundation Platform for Robotic Manipulation</a></td>
<td nowrap>world model for VLA</td>
<td nowrap>world model</td>
<td nowrap>VLA / world model / RL / world model for VLA</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap>-</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap><a href="https://openreview.net/forum?id=fHLtSxDFKC">paper</a></td>
<td nowrap><a href="https://genie-envisioner.github.io/">project</a></td>
<td nowrap><a href="https://github.com/AgibotTech/Genie-Envisioner-V1">code</a></td>
<td nowrap><a href="https://huggingface.co/agibot-world/Genie-Envisioner-v1.0">Genie-Envisioner</a></td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于判断世界预测是否能服务规划和动作验证。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=LQv9LU2Ufg">RIG: Synergizing Reasoning and Imagination in End-to-End Generalist Policy</a></td>
<td nowrap>world model for VLA</td>
<td nowrap>world model</td>
<td nowrap>VLA / world model / RL / world model for VLA</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap>-</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap><a href="https://openreview.net/forum?id=LQv9LU2Ufg">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断世界预测是否能服务规划和动作验证。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=qE2FyvRvuF">WMPO: World Model-based Policy Optimization for Vision-Language-Action Models</a></td>
<td nowrap>world model for VLA</td>
<td nowrap>world model</td>
<td nowrap>VLA / world model / RL / world model for VLA</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap>Sim + Real</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap><a href="https://openreview.net/forum?id=qE2FyvRvuF">paper</a></td>
<td nowrap><a href="https://wm-po.github.io/">project</a></td>
<td nowrap><a href="https://github.com/WM-PO/WMPO">code</a></td>
<td nowrap><a href="https://huggingface.co/fangqi/WMPO">WMPO</a></td>
<td nowrap>WAM, RL-VLA</td>
<td nowrap>用于判断世界预测是否能服务规划和动作验证。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=wPEIStHxYH">Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning</a></td>
<td nowrap>video/latent world model</td>
<td nowrap>video/latent</td>
<td nowrap>VLA / world model / RL / video/latent world model</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap>-</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap><a href="https://openreview.net/forum?id=wPEIStHxYH">paper</a></td>
<td nowrap><a href="https://research.nvidia.com/labs/dir/cosmos-policy/cosmos_policy_index.html">project</a></td>
<td nowrap><a href="https://github.com/nvlabs/cosmos-policy">code</a></td>
<td nowrap><a href="https://huggingface.co/collections/nvidia/cosmos-policy">Cosmos Policy</a></td>
<td nowrap>EAI-VLA-VLN, WAM</td>
<td nowrap>用于判断世界预测是否能服务规划和动作验证。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38925">WorldAgen: Unified State-Action Prediction with Test-Time World Model Training</a></td>
<td nowrap>world model for VLA</td>
<td nowrap>world model</td>
<td nowrap>VLA / world model / RL / world model for VLA</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap>Sim/Benchmark</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38925">paper</a></td>
<td nowrap><a href="https://worldagen.github.io/">project</a></td>
<td nowrap><a href="https://github.com/mll-lab-nu/WorldAgen">code</a></td>
<td nowrap><a href="https://huggingface.co/MLL-Lab/worldagen">worldagen</a></td>
<td nowrap>-</td>
<td nowrap>用于判断世界预测是否能服务规划和动作验证。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66169">VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model</a></td>
<td nowrap>world model for VLA</td>
<td nowrap>world model</td>
<td nowrap>VLA / world model / RL / world model for VLA</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap>Real + world-model rollouts</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66169">paper</a></td>
<td nowrap><a href="https://sites.google.com/view/vla-w">project</a></td>
<td nowrap><a href="https://github.com/Robert-gyj/Ctrl-World">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于判断世界预测是否能服务规划和动作验证。</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2603.03195">CoWVLA: Chain of World: World Model Thinking in Latent Motion</a></td>
<td nowrap>world model for VLA / video-latent</td>
<td nowrap>video/latent</td>
<td nowrap>VLA / world model / RL / video/latent world model</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap>Sim + Real</td>
<td nowrap>用世界预测支持机器人决策</td>
<td nowrap><a href="https://arxiv.org/abs/2603.03195">paper</a></td>
<td nowrap><a href="https://fx-hit.github.io/cowvla-io/">project</a></td>
<td nowrap><a href="https://github.com/fx-hit/CoWVLA">code</a></td>
<td nowrap><a href="https://huggingface.co/hitfx/CoWVLA">CoWVLA</a></td>
<td nowrap>-</td>
<td nowrap>用于判断世界预测是否能服务规划和动作验证。</td>
</tr>
</tbody>
</table>

### Agentic Planning / 推理规划

这一方向强调任务分解、记忆、失败监控、约束/affordance planning 和自改进规划。它最贴近“agent 规划，小模型或传统方法执行”的系统路线。

子方向：任务分解、memory、failure monitor、constraint / affordance planning、self-improving planning。

共 89 篇。

<table>
<thead>
<tr>
<th nowrap>子方向</th>
<th nowrap>条目数</th>
<th nowrap>观察重点</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>任务分解</td>
<td nowrap>30</td>
<td nowrap>看高层指令如何拆成可执行步骤。</td>
</tr>
<tr>
<td nowrap>memory</td>
<td nowrap>10</td>
<td nowrap>看长期记忆、经验复用和环境状态保持。</td>
</tr>
<tr>
<td nowrap>failure monitor</td>
<td nowrap>8</td>
<td nowrap>看失败检测、恢复和闭环修正。</td>
</tr>
<tr>
<td nowrap>constraint / affordance planning</td>
<td nowrap>9</td>
<td nowrap>看约束、可供性和物理可执行性。</td>
</tr>
<tr>
<td nowrap>self-improving planning</td>
<td nowrap>32</td>
<td nowrap>看自我改进、测试时优化和经验沉淀。</td>
</tr>
</tbody>
</table>

#### 任务分解

共 30 篇。

<table>
<thead>
<tr>
<th nowrap>会议/年份</th>
<th nowrap>论文/方法</th>
<th nowrap>规划粒度</th>
<th nowrap>工具/记忆</th>
<th nowrap>反馈/自改进</th>
<th nowrap>执行接口</th>
<th nowrap>验证环境</th>
<th nowrap>问题/目标</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>来源</th>
<th nowrap>调研判断</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=8xTDnj39Ti">Vlaser: Vision-Language-Action Model with Synergistic Embodied Reasoning</a></td>
<td nowrap>任务分解</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA/action</td>
<td nowrap>-</td>
<td nowrap>把高层目标转为可执行步骤</td>
<td nowrap><a href="https://openreview.net/forum?id=8xTDnj39Ti">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=tWMfhoP3as">OneTwoVLA: A Unified Vision-Language-Action Model with Adaptive Reasoning</a></td>
<td nowrap>任务分解</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA/action</td>
<td nowrap>-</td>
<td nowrap>把高层目标转为可执行步骤</td>
<td nowrap><a href="https://openreview.net/forum?id=tWMfhoP3as">paper</a> / <a href="https://arxiv.org/abs/2506.19850">Unified Vision-Language-Action Model</a></td>
<td nowrap><a href="https://robertwyq.github.io/univla.github.io/">🌐</a></td>
<td nowrap><a href="https://github.com/baaivision/UniVLA">💻</a></td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=yngvAamNQi">From Seeing to Doing: Bridging Reasoning and Decision for Robotic Manipulation</a></td>
<td nowrap>任务分解</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>把高层目标转为可执行步骤</td>
<td nowrap><a href="https://openreview.net/forum?id=yngvAamNQi">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=nESyz4PvJL">VLMgineer: Vision-Language Models as Robotic Toolsmiths</a></td>
<td nowrap>任务分解</td>
<td nowrap>任务分解</td>
<td nowrap>-</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>把高层目标转为可执行步骤</td>
<td nowrap><a href="https://openreview.net/forum?id=nESyz4PvJL">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=3eTr9dGwJv">MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Models for Embodied Task Planning</a></td>
<td nowrap>任务分解</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>把高层目标转为可执行步骤</td>
<td nowrap><a href="https://openreview.net/forum?id=3eTr9dGwJv">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=8iPwqr6Adk">Theory of Space: Can Foundation Models Construct Spatial Beliefs through Active Exploration?</a></td>
<td nowrap>任务分解</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>把高层目标转为可执行步骤</td>
<td nowrap><a href="https://openreview.net/forum?id=8iPwqr6Adk">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=EEONns7ae4">Compositional Visual Planning via Inference-Time Diffusion Scaling</a></td>
<td nowrap>任务分解</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>把高层目标转为可执行步骤</td>
<td nowrap><a href="https://openreview.net/forum?id=EEONns7ae4">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=Y1VgLHbzCC">One Demo Is All It Takes: Planning Domain Derivation with LLMs from A Single Demonstration</a></td>
<td nowrap>任务分解</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>把高层目标转为可执行步骤</td>
<td nowrap><a href="https://openreview.net/forum?id=Y1VgLHbzCC">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=tkEmIJv1tB">OmniEVA: Embodied Versatile Planner via Task-Adaptive 3D-Grounded and Embodiment-aware Reasoning</a></td>
<td nowrap>任务分解</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>把高层目标转为可执行步骤</td>
<td nowrap><a href="https://openreview.net/forum?id=tkEmIJv1tB">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=3u6AkbWEls">ManipEvalAgent: Promptable and Efficient Evaluation Framework for Robotic Manipulation Policies</a></td>
<td nowrap>任务分解</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>把高层目标转为可执行步骤</td>
<td nowrap><a href="https://openreview.net/forum?id=3u6AkbWEls">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=9AA27en4go">Difference-Aware Retrieval Polices for Imitation Learning</a></td>
<td nowrap>任务分解</td>
<td nowrap>任务分解</td>
<td nowrap>-</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>把高层目标转为可执行步骤</td>
<td nowrap><a href="https://openreview.net/forum?id=9AA27en4go">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=d1wuA8oIH0">EquAct: An SE(3)-Equivariant Multi-Task Transformer for 3D Robotic Manipulation</a></td>
<td nowrap>任务分解</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>把高层目标转为可执行步骤</td>
<td nowrap><a href="https://openreview.net/forum?id=d1wuA8oIH0">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=jXDZJAfRZB">Seeing Across Views: Benchmarking Spatial Reasoning of Vision-Language Models in Robotic Scenes</a></td>
<td nowrap>任务分解</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>把高层目标转为可执行步骤</td>
<td nowrap><a href="https://openreview.net/forum?id=jXDZJAfRZB">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=vmBIF25KLf">REI-Bench: Can Embodied Agents Understand Vague Human Instructions in Task Planning?</a></td>
<td nowrap>任务分解</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>把高层目标转为可执行步骤</td>
<td nowrap><a href="https://openreview.net/forum?id=vmBIF25KLf">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=aCVfhY4Qen">PhyScensis: Physics-Augmented LLM Agents for Complex Physical Scene Arrangement</a></td>
<td nowrap>任务分解</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>把高层目标转为可执行步骤</td>
<td nowrap><a href="https://openreview.net/forum?id=aCVfhY4Qen">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=oJAIjUDxkZ">OmniActor: A Generalist GUI and Embodied Agent for 2D&amp;3D Worlds</a></td>
<td nowrap>任务分解</td>
<td nowrap>-</td>
<td nowrap>任务分解</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>把高层目标转为可执行步骤</td>
<td nowrap><a href="https://openreview.net/forum?id=oJAIjUDxkZ">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38896">GraphCoT-VLA: A 3D Spatial-Aware Reasoning Vision-Language-Action Model for Robotic Manipulation with Ambiguous Instructions</a></td>
<td nowrap>任务分解</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA/action</td>
<td nowrap>-</td>
<td nowrap>把高层目标转为可执行步骤</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38896">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38900">PhyPlan: Learning to Plan Tasks with Generalizable and Rapid Physical Reasoning for Embodied Manipulation</a></td>
<td nowrap>任务分解</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>把高层目标转为可执行步骤</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38900">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38906">Cook and Clean Together: Teaching Embodied Agents for Parallel Task Execution</a></td>
<td nowrap>任务分解</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>把高层目标转为可执行步骤</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38906">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38911">FoAM: Foresight-Augmented Multi-Task Imitation Policy for Robotic Manipulation</a></td>
<td nowrap>任务分解</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA/action</td>
<td nowrap>-</td>
<td nowrap>把高层目标转为可执行步骤</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38911">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38936">Zero-Shot Robotic Manipulation via 3D Gaussian Splatting-Enhanced Multimodal Retrieval-Augmented Generation</a></td>
<td nowrap>任务分解</td>
<td nowrap>任务分解</td>
<td nowrap>-</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>把高层目标转为可执行步骤</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38936">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Humanoid-RL, EAI-Safety, WAM</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38958">H-GAR: A Hierarchical Interaction Framework via Goal-Driven Observation-Action Refinement for Robotic Manipulation</a></td>
<td nowrap>任务分解</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA/action</td>
<td nowrap>-</td>
<td nowrap>把高层目标转为可执行步骤</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38958">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/60500">TapSampling: Inference-Time Sampling with a Task-Progress-Understanding Verifier for Robotic Manipulation</a></td>
<td nowrap>任务分解</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/60500">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/63250">Decompose and Recompose: Reasoning New Skills from Existing Abilities for Cross-Task Robotic Manipulation</a></td>
<td nowrap>任务分解</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/63250">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.09937">SAFE: Multitask Failure Detection for Vision-Language-Action Models</a></td>
<td nowrap>失败监控</td>
<td nowrap>-</td>
<td nowrap>失败监控</td>
<td nowrap>VLA/action</td>
<td nowrap>LIBERO, SimplerEnv, real-world Franka/WidowX rollouts</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://arxiv.org/abs/2506.09937">paper</a></td>
<td nowrap><a href="https://vla-safe.github.io/">project</a></td>
<td nowrap><a href="https://github.com/vla-safe/SAFE">code</a></td>
<td nowrap>-</td>
<td nowrap>Awesome-EAI, EAI-VLA-VLN, Humanoid-RL, EAI-Safety</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2510.21302">Towards Reliable Code-as-Policies: A Neuro-Symbolic Framework for Embodied Task Planning</a></td>
<td nowrap>任务分解</td>
<td nowrap>任务分解</td>
<td nowrap>-</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>把高层目标转为可执行步骤</td>
<td nowrap><a href="https://arxiv.org/abs/2510.21302">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2510.14968">RDD: Retrieval-Based Demonstration Decomposer for Planner Alignment in Long-Horizon Tasks</a></td>
<td nowrap>任务分解</td>
<td nowrap>任务分解</td>
<td nowrap>-</td>
<td nowrap>agent planner / planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>把高层目标转为可执行步骤</td>
<td nowrap><a href="https://arxiv.org/abs/2510.14968">paper</a></td>
<td nowrap><a href="https://rdd-neurips.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2507.21545">UniDomain: Pretraining a Unified PDDL Domain from Real-World Demonstrations for Generalizable Robot Task Planning</a></td>
<td nowrap>任务分解</td>
<td nowrap>-</td>
<td nowrap>任务分解</td>
<td nowrap>planning / reasoning / RL</td>
<td nowrap>-</td>
<td nowrap>把高层目标转为可执行步骤</td>
<td nowrap><a href="https://arxiv.org/abs/2507.21545">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.21230">World-aware Planning Narratives Enhance Large Vision-Language Model Planner</a></td>
<td nowrap>任务分解</td>
<td nowrap>-</td>
<td nowrap>任务分解</td>
<td nowrap>agent planner / planning / RL</td>
<td nowrap>-</td>
<td nowrap>把高层目标转为可执行步骤</td>
<td nowrap><a href="https://arxiv.org/abs/2506.21230">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2412.18194">VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics Manipulation with Long-Horizon Reasoning Tasks</a></td>
<td nowrap>任务分解</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA/action</td>
<td nowrap>100-task VLABench; interactive VLA/workflow + non-interactive VLM evaluation</td>
<td nowrap>提供评测任务和数据基准</td>
<td nowrap><a href="https://arxiv.org/abs/2412.18194">paper</a> / <a href="https://arxiv.org/pdf/2412.18194">📄 Paper</a></td>
<td nowrap><a href="https://vlabench.github.io/">project</a></td>
<td nowrap><a href="https://github.com/OpenMOSS/VLABench">💻 Code</a></td>
<td nowrap><a href="https://huggingface.co/VLABench">VLABench HF</a></td>
<td nowrap>HCP-Survey, Awesome-EAI, EAI-VLA-VLN, WAM</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
</tbody>
</table>

#### memory

共 10 篇。

<table>
<thead>
<tr>
<th nowrap>会议/年份</th>
<th nowrap>论文/方法</th>
<th nowrap>规划粒度</th>
<th nowrap>工具/记忆</th>
<th nowrap>反馈/自改进</th>
<th nowrap>执行接口</th>
<th nowrap>验证环境</th>
<th nowrap>问题/目标</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>来源</th>
<th nowrap>调研判断</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=1dH4ARGdwD">Scaling up Memory for Robotic Control via Experience Retrieval</a></td>
<td nowrap>记忆规划</td>
<td nowrap>记忆规划</td>
<td nowrap>-</td>
<td nowrap>VLA/action</td>
<td nowrap>-</td>
<td nowrap>增强长期任务记忆</td>
<td nowrap><a href="https://openreview.net/forum?id=1dH4ARGdwD">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=79BOATBal9">Planning with an Embodied Learnable Memory</a></td>
<td nowrap>记忆规划</td>
<td nowrap>记忆规划</td>
<td nowrap>-</td>
<td nowrap>memory</td>
<td nowrap>-</td>
<td nowrap>增强长期任务记忆</td>
<td nowrap><a href="https://openreview.net/forum?id=79BOATBal9">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=9cLPurIZMj">Memory, Benchmark &amp; Robots: A Benchmark for Solving Complex Tasks with Reinforcement Learning</a></td>
<td nowrap>记忆规划</td>
<td nowrap>记忆规划</td>
<td nowrap>-</td>
<td nowrap>memory</td>
<td nowrap>-</td>
<td nowrap>增强长期任务记忆</td>
<td nowrap><a href="https://openreview.net/forum?id=9cLPurIZMj">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=E5L43l5EIu">Embodied Agents Meet Personalization: Investigating Challenges and Solutions Through the Lens of Memory Utilization</a></td>
<td nowrap>记忆规划</td>
<td nowrap>记忆规划</td>
<td nowrap>-</td>
<td nowrap>memory</td>
<td nowrap>-</td>
<td nowrap>增强长期任务记忆</td>
<td nowrap><a href="https://openreview.net/forum?id=E5L43l5EIu">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-Safety</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/60897">HiMe: Hierarchical Embodied Memory for Long-Horizon Vision-Language-Action Control</a></td>
<td nowrap>记忆规划</td>
<td nowrap>记忆规划</td>
<td nowrap>-</td>
<td nowrap>VLA/action</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/60897">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66214">Spatial Memory for Out-of-Vision Manipulation in Vision-Language-Action</a></td>
<td nowrap>记忆规划</td>
<td nowrap>记忆规划</td>
<td nowrap>-</td>
<td nowrap>VLA/action</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66214">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2602.20200">OptimusVLA: Global Prior Meets Local Consistency: Dual-Memory Augmented Vision-Language-Action Model for Efficient Robotic Manipulation</a></td>
<td nowrap>记忆规划</td>
<td nowrap>dual memory: global prior memory + local behavior memory</td>
<td nowrap>-</td>
<td nowrap>VLA/action</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://arxiv.org/abs/2602.20200">paper</a></td>
<td nowrap><a href="https://cybertronagent.github.io/OptimusVLA.github.io/">🌐</a></td>
<td nowrap><a href="https://github.com/iLearn-Lab/CVPR26-OptimusVLA">code</a></td>
<td nowrap><a href="https://huggingface.co/iLearn-Lab/OptimusVLA_Memory">OptimusVLA_Memory</a></td>
<td nowrap>Efficient-VLA</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2501.00358">Embodied VideoAgent: Persistent Memory from Egocentric Videos and Embodied Sensors Enables Dynamic Scene Understanding</a></td>
<td nowrap>记忆规划</td>
<td nowrap>persistent object memory + history buffers + query_db/temporal_loc/spatial_loc/vqa</td>
<td nowrap>-</td>
<td nowrap>LLM tool calls + embodied action primitives</td>
<td nowrap>Ego4D-VQ3D, OpenEQA, EnvQA, real-world Franka demo</td>
<td nowrap>增强长期任务记忆</td>
<td nowrap><a href="https://arxiv.org/abs/2501.00358">paper</a></td>
<td nowrap><a href="https://embodied-videoagent.github.io/">project</a></td>
<td nowrap><a href="https://github.com/Embodied-VideoAgent/embodied-videoagent">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/1915">Towards Long-Horizon Vision-Language-Action System: Reasoning, Acting and Memory</a></td>
<td nowrap>记忆规划</td>
<td nowrap>记忆规划</td>
<td nowrap>-</td>
<td nowrap>VLA/action</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/1915">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICML 2025</td>
<td nowrap>SAM2Act:Integrating Visual Foundation Model with A Memory Architecture for Robotic Manipulation</td>
<td nowrap>记忆规划</td>
<td nowrap>记忆规划</td>
<td nowrap>-</td>
<td nowrap>memory</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2501.18564">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
</tbody>
</table>

#### failure monitor

共 8 篇。

<table>
<thead>
<tr>
<th nowrap>会议/年份</th>
<th nowrap>论文/方法</th>
<th nowrap>规划粒度</th>
<th nowrap>工具/记忆</th>
<th nowrap>反馈/自改进</th>
<th nowrap>执行接口</th>
<th nowrap>验证环境</th>
<th nowrap>问题/目标</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>来源</th>
<th nowrap>调研判断</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=N22lDHYrXe">Experience-based Knowledge Correction for Robust Planning in Minecraft</a></td>
<td nowrap>失败监控</td>
<td nowrap>-</td>
<td nowrap>失败监控</td>
<td nowrap>failure monitor</td>
<td nowrap>-</td>
<td nowrap>检测或恢复执行失败</td>
<td nowrap><a href="https://openreview.net/forum?id=N22lDHYrXe">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=WC6MJ5r5Bj">ReCAPA: Hierarchical Predictive Correction to Mitigate Cascading Failures</a></td>
<td nowrap>失败监控</td>
<td nowrap>-</td>
<td nowrap>失败监控</td>
<td nowrap>failure monitor</td>
<td nowrap>-</td>
<td nowrap>检测或恢复执行失败</td>
<td nowrap><a href="https://openreview.net/forum?id=WC6MJ5r5Bj">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=jr9hGWQioP">Self-Refining Vision Language Model for Robotic Failure Detection and Reasoning</a></td>
<td nowrap>失败监控</td>
<td nowrap>-</td>
<td nowrap>失败监控</td>
<td nowrap>failure monitor</td>
<td nowrap>-</td>
<td nowrap>检测或恢复执行失败</td>
<td nowrap><a href="https://openreview.net/forum?id=jr9hGWQioP">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61750">Sentinel-VLA: A Metacognitive VLA Model with Active Status Monitoring for Dynamic Reasoning and Error Recovery</a></td>
<td nowrap>失败监控</td>
<td nowrap>-</td>
<td nowrap>失败监控</td>
<td nowrap>VLA/action</td>
<td nowrap>-</td>
<td nowrap>发现并修复执行失败</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61750">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/63650">NeurVLA: Unleashing Failure-Handling Capability of Vision-Language-Action Models via Neural-Symbolic Reasoning</a></td>
<td nowrap>失败监控</td>
<td nowrap>-</td>
<td nowrap>失败监控</td>
<td nowrap>VLA/action</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/63650">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64203">Can VLMs Diagnose and Recover from VLA Manipulation Faults?</a></td>
<td nowrap>失败监控</td>
<td nowrap>-</td>
<td nowrap>失败监控</td>
<td nowrap>VLA/action</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64203">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2510.09459">Failure Prediction at Runtime for Generative Robot Policies</a></td>
<td nowrap>失败监控</td>
<td nowrap>-</td>
<td nowrap>失败监控</td>
<td nowrap>failure monitor</td>
<td nowrap>-</td>
<td nowrap>检测或恢复执行失败</td>
<td nowrap><a href="https://arxiv.org/abs/2510.09459">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2412.04455">Code-as-Monitor: Constraint-aware Visual Programming for Reactive and Proactive Robotic Failure Detection</a></td>
<td nowrap>失败监控</td>
<td nowrap>VLM-generated monitor code + constraint elements</td>
<td nowrap>失败监控</td>
<td nowrap>closed-loop monitor over open-loop policy</td>
<td nowrap>CLIPort, OmniGibson, real-world</td>
<td nowrap>检测或恢复执行失败</td>
<td nowrap><a href="https://arxiv.org/abs/2412.04455">paper</a></td>
<td nowrap><a href="https://zhoues.github.io/Code-as-Monitor/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>HCP-Survey, Awesome-EAI</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
</tbody>
</table>

#### constraint / affordance planning

共 9 篇。

<table>
<thead>
<tr>
<th nowrap>会议/年份</th>
<th nowrap>论文/方法</th>
<th nowrap>规划粒度</th>
<th nowrap>工具/记忆</th>
<th nowrap>反馈/自改进</th>
<th nowrap>执行接口</th>
<th nowrap>验证环境</th>
<th nowrap>问题/目标</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>来源</th>
<th nowrap>调研判断</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=enprG5H9aD">Towards Improvisational TAMP: Learning Low-Level Shortcuts in Abstract Planning Graphs</a></td>
<td nowrap>约束/affordance</td>
<td nowrap>-</td>
<td nowrap>约束/affordance</td>
<td nowrap>planning / affordance</td>
<td nowrap>-</td>
<td nowrap>约束动作可执行性</td>
<td nowrap><a href="https://openreview.net/forum?id=enprG5H9aD">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=kWCNhRdcDI">Natural Language PDDL (NL-PDDL) for Open-world Goal-oriented Commonsense Regression Planning in Embodied AI</a></td>
<td nowrap>约束/affordance</td>
<td nowrap>-</td>
<td nowrap>约束/affordance</td>
<td nowrap>planning / affordance</td>
<td nowrap>-</td>
<td nowrap>约束动作可执行性</td>
<td nowrap><a href="https://openreview.net/forum?id=kWCNhRdcDI">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=refcXHU1Nh">SafeFlowMatcher: Safe and Fast Planning using Flow Matching with Control Barrier Functions</a></td>
<td nowrap>约束/affordance</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA/action</td>
<td nowrap>-</td>
<td nowrap>约束动作可执行性</td>
<td nowrap><a href="https://openreview.net/forum?id=refcXHU1Nh">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=bGPDviEtZ1">MoMaGen: Generating Demonstrations under Soft and Hard Constraints for Multi-Step Bimanual Mobile Manipulation</a></td>
<td nowrap>约束/affordance</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>planning / affordance</td>
<td nowrap>-</td>
<td nowrap>约束动作可执行性</td>
<td nowrap><a href="https://openreview.net/forum?id=bGPDviEtZ1">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38907">A3D: Adaptive Affordance Assembly with Dual-Arm Manipulation</a></td>
<td nowrap>约束/affordance</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>planning / affordance</td>
<td nowrap>-</td>
<td nowrap>约束动作可执行性</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38907">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38909">Affordance-Guided Coarse-to-Fine Exploration for Base Placement in Open-Vocabulary Mobile Manipulation</a></td>
<td nowrap>约束/affordance</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>planning / affordance</td>
<td nowrap>-</td>
<td nowrap>约束动作可执行性</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38909">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38955">Gentle Manipulation Policy Learning via Demonstrations from VLM Planned Atomic Skills</a></td>
<td nowrap>约束/affordance</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA/action</td>
<td nowrap>-</td>
<td nowrap>约束动作可执行性</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38955">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap>InstructFlow: Adaptive Symbolic Constraint-Guided Code Generation for Long-Horizon Planning</td>
<td nowrap>约束/affordance</td>
<td nowrap>约束/affordance</td>
<td nowrap>-</td>
<td nowrap>flow matching / planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>约束动作可执行性</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/542">CoA-VLA: Improving Vision-Language-Action Models via Visual-Text Chain-of-Affordance</a></td>
<td nowrap>约束/affordance</td>
<td nowrap>-</td>
<td nowrap>约束/affordance</td>
<td nowrap>VLA/action</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/542">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
</tbody>
</table>

#### self-improving planning

共 32 篇。

<table>
<thead>
<tr>
<th nowrap>会议/年份</th>
<th nowrap>论文/方法</th>
<th nowrap>规划粒度</th>
<th nowrap>工具/记忆</th>
<th nowrap>反馈/自改进</th>
<th nowrap>执行接口</th>
<th nowrap>验证环境</th>
<th nowrap>问题/目标</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>来源</th>
<th nowrap>调研判断</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=SzUgx5r3wy">Self-Improving Loops for Visual Robotic Planning</a></td>
<td nowrap>自改进规划</td>
<td nowrap>-</td>
<td nowrap>自改进规划</td>
<td nowrap>planning / reasoning / RL</td>
<td nowrap>-</td>
<td nowrap>通过反馈自我改进规划</td>
<td nowrap><a href="https://openreview.net/forum?id=SzUgx5r3wy">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, EAI-Safety, WAM, RL-VLA</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=Vsy3nAnaX6">BOLT: Decision‑Aligned Distillation and Budget-Aware Routing for Constrained Multimodal QA on Robots</a></td>
<td nowrap>自改进规划</td>
<td nowrap>-</td>
<td nowrap>自改进规划</td>
<td nowrap>planning / reasoning / RL</td>
<td nowrap>-</td>
<td nowrap>通过反馈自我改进规划</td>
<td nowrap><a href="https://openreview.net/forum?id=Vsy3nAnaX6">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=eJcCW9oNfH">EVLP: Learning Unified Embodied Vision-Language Planner with Reinforced Supervised Fine-Tuning</a></td>
<td nowrap>自改进规划</td>
<td nowrap>-</td>
<td nowrap>自改进规划</td>
<td nowrap>planning / reasoning / RL</td>
<td nowrap>-</td>
<td nowrap>通过反馈自我改进规划</td>
<td nowrap><a href="https://openreview.net/forum?id=eJcCW9oNfH">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=i5wlozMFsQ">Embodied-R1: Reinforced Embodied Reasoning for General Robotic Manipulation</a></td>
<td nowrap>自改进规划</td>
<td nowrap>-</td>
<td nowrap>自改进规划</td>
<td nowrap>planning / reasoning / RL</td>
<td nowrap>-</td>
<td nowrap>通过反馈自我改进规划</td>
<td nowrap><a href="https://openreview.net/forum?id=i5wlozMFsQ">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38922">ManipLVM-R1: Reinforcement Learning for Reasoning in Embodied Manipulation with Large Vision-Language Models</a></td>
<td nowrap>自改进规划</td>
<td nowrap>-</td>
<td nowrap>自改进规划</td>
<td nowrap>planning / reasoning / RL</td>
<td nowrap>-</td>
<td nowrap>通过反馈自我改进规划</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38922">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61922">HALO: A Unified Vision-Language-Action Model for Embodied Multimodal Chain-of-Thought Reasoning</a></td>
<td nowrap>自改进规划</td>
<td nowrap>-</td>
<td nowrap>自改进规划</td>
<td nowrap>VLA/action</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61922">paper</a> / <a href="https://arxiv.org/abs/2506.19850">Unified Vision-Language-Action Model</a></td>
<td nowrap><a href="https://robertwyq.github.io/univla.github.io/">🌐</a></td>
<td nowrap><a href="https://github.com/baaivision/UniVLA">💻</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64290">Latent Reasoning VLA: Latent Thinking and Prediction for Vision-Language-Action Models</a></td>
<td nowrap>自改进规划</td>
<td nowrap>-</td>
<td nowrap>自改进规划</td>
<td nowrap>VLA/action</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64290">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61887">LaST0: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model</a></td>
<td nowrap>自改进规划</td>
<td nowrap>-</td>
<td nowrap>自改进规划</td>
<td nowrap>VLA/action</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61887">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/60801">LAGEA: Language Guided Embodied Agents for Robotic Manipulation</a></td>
<td nowrap>自改进规划</td>
<td nowrap>-</td>
<td nowrap>自改进规划</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/60801">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64055">Drift is a Sampling Error: SNR-Aware Power Distributions for Long-Horizon Robotic Planning</a></td>
<td nowrap>自改进规划</td>
<td nowrap>-</td>
<td nowrap>自改进规划</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>通过反馈自我改进规划</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64055">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2601.11404">ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models</a></td>
<td nowrap>自改进规划</td>
<td nowrap>-</td>
<td nowrap>自改进规划</td>
<td nowrap>VLA/action</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://arxiv.org/abs/2601.11404">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/AgibotTech/ACoT-VLA">code</a></td>
<td nowrap><a href="https://huggingface.co/datasets/agibot-world/AgiBotWorldChallenge-2026/tree/main/Reasoning2Action-Sim">Reasoning2Action-Sim</a></td>
<td nowrap>Awesome-EAI</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2601.09708">Fast-ThinkAct: Efficient Vision-Language-Action Reasoning via Verbalizable Latent Planning</a></td>
<td nowrap>自改进规划</td>
<td nowrap>-</td>
<td nowrap>自改进规划</td>
<td nowrap>VLA/action</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://arxiv.org/abs/2601.09708">paper</a></td>
<td nowrap><a href="https://research.nvidia.com/labs/twn/publication/cvpr_2026_fastthinkact/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.01953">Fast-in-Slow: A Dual-System VLA Model Unifying Fast Manipulation within Slow Reasoning</a></td>
<td nowrap>自改进规划</td>
<td nowrap>-</td>
<td nowrap>自改进规划</td>
<td nowrap>dual-system VLA: slow reasoning + high-frequency action module</td>
<td nowrap>RLBench + real-world AlphaBot/Agilex</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2506.01953">paper</a></td>
<td nowrap><a href="https://fast-in-slow.github.io/">project</a></td>
<td nowrap><a href="https://github.com/CHEN-H01/Fast-in-Slow">💻</a></td>
<td nowrap><a href="https://huggingface.co/chenhao01/fisvla/tree/main">checkpoint</a></td>
<td nowrap>EAI-VLA-VLN, Efficient-VLA</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2505.21906">ChatVLA-2: Vision-Language-Action Model with Open-World Reasoning</a></td>
<td nowrap>自改进规划</td>
<td nowrap>-</td>
<td nowrap>自改进规划</td>
<td nowrap>VLA/action</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://arxiv.org/abs/2505.21906">paper</a></td>
<td nowrap><a href="https://chatvla-2.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.17561">VLA-OS: Structuring and Dissecting Planning Representations and Paradigms in Vision-Language-Action Models</a></td>
<td nowrap>自改进规划</td>
<td nowrap>-</td>
<td nowrap>自改进规划</td>
<td nowrap>VLA/action</td>
<td nowrap>LIBERO, deformable real-world, Colosseum, FurnitureBench, DexArt, PerAct2</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://arxiv.org/abs/2506.17561">paper</a></td>
<td nowrap><a href="https://nus-lins-lab.github.io/vlaos/">project</a></td>
<td nowrap><a href="https://github.com/HeegerGao/VLA-OS">code</a></td>
<td nowrap><a href="https://huggingface.co/datasets/Linslab/VLA-OS-Dataset">VLA-OS-Dataset</a></td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2507.16815">ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning</a></td>
<td nowrap>自改进规划</td>
<td nowrap>-</td>
<td nowrap>reinforced visual latent planning with action-aligned rewards; self-correction</td>
<td nowrap>VLA/action</td>
<td nowrap>SimplerEnv, LIBERO, EgoPlan-Bench2, RoboVQA, OpenEQA</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://arxiv.org/abs/2507.16815">paper</a> / <a href="https://neurips.cc/virtual/2025/loc/san-diego/poster/119747">🔗</a></td>
<td nowrap><a href="https://jasper0314-huang.github.io/thinkact-vla/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN, RL-VLA</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2509.15155">Self-Improving Embodied Foundation Models</a></td>
<td nowrap>自改进规划</td>
<td nowrap>-</td>
<td nowrap>online RL with self-predicted reward + success detector</td>
<td nowrap>VLA/action</td>
<td nowrap>Simulated/Real-World LanguageTable, Aloha, BananaTable/Real2Sim</td>
<td nowrap>通过反馈自我改进规划</td>
<td nowrap><a href="https://arxiv.org/abs/2509.15155">paper</a> / <a href="https://arxiv.org/pdf/2509.15155">Generalist</a> / <a href="https://neurips.cc/virtual/2025/loc/san-diego/poster/118633">🔗</a></td>
<td nowrap><a href="https://self-improving-efms.github.io/">project</a> / <a href="https://self-improving-efms.github.io./">🔗</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, EAI-Safety, WAM, RL-VLA</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.09990">Chain-of-Action: Trajectory Autoregressive Modeling for Robotic Manipulation</a></td>
<td nowrap>自改进规划</td>
<td nowrap>-</td>
<td nowrap>自改进规划</td>
<td nowrap>closed-loop reverse autoregressive trajectory generation</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2506.09990">paper</a></td>
<td nowrap><a href="https://chain-of-action.github.io/">project</a></td>
<td nowrap><a href="https://github.com/ByteDance-Seed/Chain-of-Action">code</a></td>
<td nowrap><a href="https://huggingface.co/datasets/Solomonz/Chain-of-Action">dataset/model</a></td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2510.08044">Towards Reliable LLM-based Robots Planning via Combined Uncertainty Estimation</a></td>
<td nowrap>自改进规划</td>
<td nowrap>-</td>
<td nowrap>自改进规划</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>通过反馈自我改进规划</td>
<td nowrap><a href="https://arxiv.org/abs/2510.08044">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2507.00833">HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning</a></td>
<td nowrap>自改进规划</td>
<td nowrap>-</td>
<td nowrap>自改进规划</td>
<td nowrap>reasoning</td>
<td nowrap>20 tabletop bimanual dexterous tasks; DP/DP3 deployment</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2507.00833">paper</a> / <a href="https://arxiv.org/pdf/2507.00833">📄 Paper</a></td>
<td nowrap><a href="https://openhumanoidgen.github.io/">🌍 Web</a></td>
<td nowrap><a href="https://github.com/TeleHuman/HumanoidGen">code</a></td>
<td nowrap><a href="https://huggingface.co/datasets/TeleEmbodied/humanoidgen_dataset/tree/main/task_datasets">humanoidgen_dataset</a></td>
<td nowrap>Humanoid-RL, WAM</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2509.23829">DexFlyWheel: A Scalable and Self-improving Data Generation Framework for Dexterous Manipulation</a></td>
<td nowrap>自改进规划</td>
<td nowrap>-</td>
<td nowrap>自改进规划</td>
<td nowrap>self-improving planner</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2509.23829">paper</a></td>
<td nowrap><a href="https://dexflywheel.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2507.18276">Adaptive Articulated Object Manipulation On The Fly with Foundation Model Reasoning and Part Grounding</a></td>
<td nowrap>自改进规划</td>
<td nowrap>-</td>
<td nowrap>自改进规划</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2507.18276">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2505.01709">RoBridge: A Hierarchical Architecture Bridging Cognition and Execution for General Robotic Manipulation</a></td>
<td nowrap>自改进规划</td>
<td nowrap>-</td>
<td nowrap>自改进规划</td>
<td nowrap>planning</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2505.01709">paper</a></td>
<td nowrap><a href="https://abliao.github.io/RoBridge/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICML 2025</td>
<td nowrap>Efficient Robotic Policy Learning via Latent Space Backward Planning</td>
<td nowrap>自改进规划</td>
<td nowrap>-</td>
<td nowrap>自改进规划</td>
<td nowrap>VLA/action</td>
<td nowrap>-</td>
<td nowrap>提升推理或执行效率</td>
<td nowrap><a href="https://arxiv.org/abs/2505.06861">paper</a></td>
<td nowrap><a href="https://lbp-authors.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICML 2025</td>
<td nowrap>Closed-Loop Long-Horizon Robotic Planning via Equilibrium Sequence Modeling</td>
<td nowrap>自改进规划</td>
<td nowrap>-</td>
<td nowrap>自改进规划</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>通过反馈自我改进规划</td>
<td nowrap><a href="https://arxiv.org/pdf/2410.01440">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/Singularity0104/equilibrium-planner">project</a></td>
<td nowrap>-</td>
<td nowrap>Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Humanoid-RL, EAI-Safety, WAM, RL-VLA</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>ICML 2025</td>
<td nowrap>WOMD-Reasoning: A Large-Scale Dataset for Interaction Reasoning in Driving</td>
<td nowrap>自改进规划</td>
<td nowrap>-</td>
<td nowrap>自改进规划</td>
<td nowrap>VLA/action</td>
<td nowrap>Sim/Benchmark</td>
<td nowrap>提供训练/评测数据资源</td>
<td nowrap><a href="https://arxiv.org/abs/2407.04281">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/yhli123/WOMD-Reasoning">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://cvpr.thecvf.com/virtual/2025/poster/33233">CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models</a></td>
<td nowrap>自改进规划</td>
<td nowrap>-</td>
<td nowrap>自改进规划</td>
<td nowrap>VLA/action</td>
<td nowrap>Franka-Tabletop, LIBERO, Bridge V2</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://cvpr.thecvf.com/virtual/2025/poster/33233">paper</a></td>
<td nowrap><a href="https://cot-vla.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN, Awesome-VLA, WAM</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2411.18562">DexHandDiff: Interaction-aware Diffusion Planning for Adaptive Dexterous Manipulation</a></td>
<td nowrap>自改进规划</td>
<td nowrap>-</td>
<td nowrap>自改进规划</td>
<td nowrap>VLA/action</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2411.18562">paper</a></td>
<td nowrap><a href="https://dexdiffuser.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2502.21257">RoboBrain: A Unified Brain Model for Robotic Manipulation from Abstract to Concrete</a></td>
<td nowrap>自改进规划</td>
<td nowrap>-</td>
<td nowrap>自改进规划</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2502.21257">paper</a></td>
<td nowrap><a href="https://superrobobrain.github.io/robobrainv1/index.html">project</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://superrobobrain.github.io/robobrainv1/index.html">ShareRobot dataset/checkpoints</a></td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.08481">PhysVLM: Enabling Visual Language Models to Understand Robotic Physical Reachability</a></td>
<td nowrap>自改进规划</td>
<td nowrap>-</td>
<td nowrap>自改进规划</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>通过反馈自我改进规划</td>
<td nowrap><a href="https://arxiv.org/abs/2503.08481">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2411.16537">RoboSpatial: Teaching Spatial Understanding to 2D and 3D Vision-Language Models for Robotics</a></td>
<td nowrap>自改进规划</td>
<td nowrap>-</td>
<td nowrap>自改进规划</td>
<td nowrap>planning / reasoning / 3D representation</td>
<td nowrap>-</td>
<td nowrap>通过反馈自我改进规划</td>
<td nowrap><a href="https://arxiv.org/abs/2411.16537">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap>Tartan IMU: A Light Foundation Model for Inertial Positioning in Robotics</td>
<td nowrap>自改进规划</td>
<td nowrap>-</td>
<td nowrap>自改进规划</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>通过反馈自我改进规划</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估高层规划是否能落到可执行动作。</td>
</tr>
</tbody>
</table>

### 本体扩展 / 灵巧操作

本体扩展决定具身智能是否能从单机械臂走向人形、双臂、灵巧手和触觉接触任务。表中论文体现了动作空间、传感方式和控制目标随本体变化而复杂化。

子方向：humanoid、bimanual、dexterous hand、tactile/contact-rich、grasp。

共 72 篇。

<table>
<thead>
<tr>
<th nowrap>子方向</th>
<th nowrap>条目数</th>
<th nowrap>观察重点</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>humanoid</td>
<td nowrap>21</td>
<td nowrap>看全身控制、移动操作和人形本体泛化。</td>
</tr>
<tr>
<td nowrap>bimanual</td>
<td nowrap>11</td>
<td nowrap>看双臂协同、长程操作和协调控制。</td>
</tr>
<tr>
<td nowrap>dexterous hand</td>
<td nowrap>27</td>
<td nowrap>看灵巧手动作空间和抓取迁移。</td>
</tr>
<tr>
<td nowrap>tactile/contact-rich</td>
<td nowrap>13</td>
<td nowrap>看触觉、接触动力学和精细反馈。</td>
</tr>
</tbody>
</table>

#### humanoid

共 21 篇。

<table>
<thead>
<tr>
<th nowrap>会议/年份</th>
<th nowrap>论文/方法</th>
<th nowrap>本体类型</th>
<th nowrap>传感/接触</th>
<th nowrap>控制接口</th>
<th nowrap>训练方式</th>
<th nowrap>Sim/Real</th>
<th nowrap>问题/目标</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>来源</th>
<th nowrap>调研判断</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=OCJmVjyzN7">WholeBodyVLA: Towards Unified Latent VLA for Whole-body Loco-manipulation Control</a></td>
<td nowrap>人形/足式机器人</td>
<td nowrap>-</td>
<td nowrap>humanoid control / 人形/全身控制</td>
<td nowrap>humanoid control</td>
<td nowrap>-</td>
<td nowrap>提升复杂本体控制</td>
<td nowrap><a href="https://openreview.net/forum?id=OCJmVjyzN7">paper</a></td>
<td nowrap><a href="https://opendrivelab.com/WholeBodyVLA/">project</a></td>
<td nowrap><a href="https://github.com/OpenDriveLab/WholebodyVLA">code</a></td>
<td nowrap>-</td>
<td nowrap>Awesome-EAI, Humanoid-RL</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=aQWSEjcN9V">Endowing GPT-4 with a Humanoid Body: Building the Bridge Between Off-the-Shelf VLMs and the Physical World</a></td>
<td nowrap>人形/足式机器人</td>
<td nowrap>-</td>
<td nowrap>humanoid control / 人形/全身控制</td>
<td nowrap>humanoid control</td>
<td nowrap>-</td>
<td nowrap>提升复杂本体控制</td>
<td nowrap><a href="https://openreview.net/forum?id=aQWSEjcN9V">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Humanoid-RL</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=3UE3Aatcjy">HWC-Loco: A Hierarchical Whole-Body Control Approach to Robust Humanoid Locomotion</a></td>
<td nowrap>人形/足式机器人</td>
<td nowrap>-</td>
<td nowrap>humanoid control / 人形/全身控制</td>
<td nowrap>humanoid control</td>
<td nowrap>Sim + Real</td>
<td nowrap>提升复杂本体控制</td>
<td nowrap><a href="https://openreview.net/forum?id=3UE3Aatcjy">paper</a></td>
<td nowrap><a href="https://simonlinsx.github.io/HWC_Loco/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Humanoid-RL</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=6T3wJQhvc3">Task Tokens: A Flexible Approach to Adapting Behavior Foundation Models</a></td>
<td nowrap>人形/足式机器人</td>
<td nowrap>-</td>
<td nowrap>humanoid control / 人形/全身控制</td>
<td nowrap>humanoid control</td>
<td nowrap>-</td>
<td nowrap>提升复杂本体控制</td>
<td nowrap><a href="https://openreview.net/forum?id=6T3wJQhvc3">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=jkhl2oI0g5">BFM-Zero: A Promptable Behavioral Foundation Model for Humanoid Control Using Unsupervised Reinforcement Learning</a></td>
<td nowrap>人形/足式机器人</td>
<td nowrap>触觉/接触</td>
<td nowrap>humanoid control / 人形/全身控制</td>
<td nowrap>unsupervised RL / Forward-Backward latent model / sim2real</td>
<td nowrap>-</td>
<td nowrap>提升复杂本体控制</td>
<td nowrap><a href="https://openreview.net/forum?id=jkhl2oI0g5">paper</a></td>
<td nowrap><a href="https://lecar-lab.github.io/BFM-Zero/">project</a></td>
<td nowrap><a href="https://github.com/LeCAR-Lab/BFM-Zero">code</a></td>
<td nowrap>-</td>
<td nowrap>Humanoid-RL</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=k3Cyx3Uets">From Language to Locomotion: Retargeting-free Humanoid Control via Motion Latent Guidance</a></td>
<td nowrap>人形/足式机器人</td>
<td nowrap>-</td>
<td nowrap>language-conditioned motion latent / diffusion policy</td>
<td nowrap>humanoid control</td>
<td nowrap>-</td>
<td nowrap>提升复杂本体控制</td>
<td nowrap><a href="https://openreview.net/forum?id=k3Cyx3Uets">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/gentlefress/RoboGhost">code</a></td>
<td nowrap>-</td>
<td nowrap>Humanoid-RL</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=NEOTsyyYH7">Towards Bridging the Gap between Large-Scale Pretraining and Efficient Finetuning for Humanoid Control</a></td>
<td nowrap>人形/足式机器人</td>
<td nowrap>-</td>
<td nowrap>humanoid control / 人形/全身控制</td>
<td nowrap>off-policy SAC pretraining + model-based fine-tuning</td>
<td nowrap>-</td>
<td nowrap>提升复杂本体控制</td>
<td nowrap><a href="https://openreview.net/forum?id=NEOTsyyYH7">paper</a></td>
<td nowrap><a href="https://lift-humanoid.github.io/">project</a></td>
<td nowrap><a href="https://github.com/bigai-ai/LIFT-humanoid">code</a></td>
<td nowrap>-</td>
<td nowrap>Humanoid-RL</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=eSkDNIGbcd">Hierarchical Value-Decomposed Offline Reinforcement Learning for Whole-Body Control</a></td>
<td nowrap>人形/足式机器人</td>
<td nowrap>触觉/接触</td>
<td nowrap>humanoid control / 人形/全身控制</td>
<td nowrap>humanoid control</td>
<td nowrap>-</td>
<td nowrap>提升复杂本体控制</td>
<td nowrap><a href="https://openreview.net/forum?id=eSkDNIGbcd">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38908">Whole-Body Coordination for Dynamic Object Grasping with Legged Manipulators</a></td>
<td nowrap>四足机器人 + 机械臂</td>
<td nowrap>-</td>
<td nowrap>humanoid control / 人形/全身控制</td>
<td nowrap>humanoid control</td>
<td nowrap>Sim + Real</td>
<td nowrap>提升复杂本体控制</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38908">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>DQ-Bench</td>
<td nowrap>HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Robot-Learning, Humanoid-RL, EAI-Safety, WAM</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38918">Coordinated Humanoid Robot Locomotion with Symmetry Equivariant Reinforcement Learning Policy</a></td>
<td nowrap>人形/足式机器人</td>
<td nowrap>触觉/接触</td>
<td nowrap>humanoid control / 人形/全身控制</td>
<td nowrap>symmetry-equivariant DRL</td>
<td nowrap>Sim + Real / Unitree G1</td>
<td nowrap>提升复杂本体控制</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38918">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Humanoid-RL</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38924">FARM: Frame-Accelerated Augmentation and Residual Mixture-of-Experts for Physics-Based High-Dynamic Humanoid Control</a></td>
<td nowrap>人形/足式机器人</td>
<td nowrap>-</td>
<td nowrap>humanoid control / 人形/全身控制</td>
<td nowrap>humanoid control</td>
<td nowrap>-</td>
<td nowrap>提升复杂本体控制</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38924">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/Colin-Jing/FARM">code</a></td>
<td nowrap><a href="https://github.com/Colin-Jing/FARM">HDHM data</a></td>
<td nowrap>Humanoid-RL</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38927">ODYSSEY: Open-World Quadrupeds Exploration and Manipulation for Long-Horizon Tasks</a></td>
<td nowrap>四足机器人 + 机械臂</td>
<td nowrap>-</td>
<td nowrap>humanoid control / 人形/全身控制</td>
<td nowrap>humanoid control</td>
<td nowrap>-</td>
<td nowrap>提升复杂本体控制</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38927">paper</a></td>
<td nowrap><a href="https://kaijwang.github.io/odyssey.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38949">Keep On Going: Learning Robust Humanoid Motion Skills via Selective Adversarial Training</a></td>
<td nowrap>人形/足式机器人</td>
<td nowrap>-</td>
<td nowrap>humanoid control / 人形/全身控制</td>
<td nowrap>humanoid control</td>
<td nowrap>-</td>
<td nowrap>提升复杂本体控制</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38949">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Humanoid-RL</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38951">Towards Adaptive Humanoid Control via Multi-Behavior Distillation and Reinforced Fine-Tuning</a></td>
<td nowrap>人形/足式机器人</td>
<td nowrap>触觉/接触</td>
<td nowrap>humanoid control / 人形/全身控制</td>
<td nowrap>multi-behavior distillation + reinforced fine-tuning</td>
<td nowrap>Sim + Real / Unitree G1</td>
<td nowrap>提升复杂本体控制</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38951">paper</a></td>
<td nowrap><a href="https://ahc-humanoid.github.io">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Humanoid-RL</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62003">Scalable and General Whole-Body Control for Cross-Humanoid Locomotion</a></td>
<td nowrap>人形机器人</td>
<td nowrap>-</td>
<td nowrap>humanoid control / 人形/全身控制</td>
<td nowrap>cross-embodiment morphological randomization</td>
<td nowrap>12 simulated humanoids + 7 real robots</td>
<td nowrap>提升人形机器人控制</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62003">paper</a></td>
<td nowrap><a href="https://xhugwbc.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Awesome-EAI, Humanoid-RL</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/65120">Learning Transferable Interaction Primitives from Game Videos for Humanoids</a></td>
<td nowrap>人形机器人</td>
<td nowrap>-</td>
<td nowrap>humanoid control / 人形/全身控制</td>
<td nowrap>humanoid control</td>
<td nowrap>-</td>
<td nowrap>提升人形机器人控制</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/65120">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2511.15200">VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation</a></td>
<td nowrap>人形机器人</td>
<td nowrap>视觉</td>
<td nowrap>humanoid control / 人形/全身控制</td>
<td nowrap>humanoid control</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2511.15200">paper</a></td>
<td nowrap><a href="https://viral-humanoid.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Humanoid-RL</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2504.14305">Adversarial Locomotion and Motion Imitation for Humanoid Policy Learning</a></td>
<td nowrap>人形机器人</td>
<td nowrap>-</td>
<td nowrap>humanoid control / 人形/全身控制</td>
<td nowrap>humanoid control</td>
<td nowrap>-</td>
<td nowrap>提升人形机器人控制</td>
<td nowrap><a href="https://arxiv.org/abs/2504.14305">paper</a></td>
<td nowrap><a href="https://almi-humanoid.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Humanoid-RL</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.12779">From Experts to a Generalist: Toward General Whole-Body Control for Humanoid Robots</a></td>
<td nowrap>人形机器人</td>
<td nowrap>-</td>
<td nowrap>humanoid control / 人形/全身控制</td>
<td nowrap>humanoid control</td>
<td nowrap>-</td>
<td nowrap>提升人形机器人控制</td>
<td nowrap><a href="https://arxiv.org/abs/2506.12779">paper</a></td>
<td nowrap><a href="https://beingbeyond.github.io/BumbleBee/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Humanoid-RL</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://kungfubot.github.io/">KungfuBot: Physics-Based Humanoid Whole-Body Control for Learning Highly-Dynamic Skills</a></td>
<td nowrap>人形机器人</td>
<td nowrap>-</td>
<td nowrap>humanoid control / 人形/全身控制</td>
<td nowrap>humanoid control</td>
<td nowrap>-</td>
<td nowrap>提升人形机器人控制</td>
<td nowrap><a href="https://arxiv.org/abs/2506.12851">project</a></td>
<td nowrap><a href="https://kungfubot.github.io/">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Humanoid-RL</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://cvpr.thecvf.com/virtual/2025/poster/34565">Let Humanoid Robots Go Hiking! Integrative Skill Development over Complex Trails</a></td>
<td nowrap>人形机器人</td>
<td nowrap>-</td>
<td nowrap>humanoid control / 人形/全身控制</td>
<td nowrap>humanoid control</td>
<td nowrap>-</td>
<td nowrap>提升人形机器人控制</td>
<td nowrap><a href="https://cvpr.thecvf.com/virtual/2025/poster/34565">paper</a></td>
<td nowrap><a href="https://lego-h-humanoidrobothiking.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
</tbody>
</table>

#### bimanual

共 11 篇。

<table>
<thead>
<tr>
<th nowrap>会议/年份</th>
<th nowrap>论文/方法</th>
<th nowrap>本体类型</th>
<th nowrap>传感/接触</th>
<th nowrap>控制接口</th>
<th nowrap>训练方式</th>
<th nowrap>Sim/Real</th>
<th nowrap>问题/目标</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>来源</th>
<th nowrap>调研判断</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=jG9W6nAwVz">TwinVLA: Data-Efficient Bimanual Manipulation with Twin Single-Arm Vision-Language-Action Models</a></td>
<td nowrap>双臂机器人</td>
<td nowrap>视觉</td>
<td nowrap>bimanual policy / 双臂操作</td>
<td nowrap>bimanual policy</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://openreview.net/forum?id=jG9W6nAwVz">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=he86smZzRk">VLBiMan: Vision-Language Anchored One-Shot Demonstration Enables Generalizable Bimanual Robotic Manipulation</a></td>
<td nowrap>双臂机器人</td>
<td nowrap>视觉</td>
<td nowrap>bimanual policy / 双臂操作</td>
<td nowrap>bimanual policy</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://openreview.net/forum?id=he86smZzRk">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38926">LatentVLA: Taming Latent Space for Generalizable and Long-Horizon Bimanual Manipulation</a></td>
<td nowrap>双臂机器人</td>
<td nowrap>-</td>
<td nowrap>bimanual policy / 双臂操作</td>
<td nowrap>bimanual policy</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38926">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/63277">DexMachina: Functional Retargeting for Bimanual Dexterous Manipulation</a></td>
<td nowrap>双臂机器人</td>
<td nowrap>-</td>
<td nowrap>bimanual policy / 双臂操作</td>
<td nowrap>bimanual policy</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/63277">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66358">DECO: Decoupled Multimodal Diffusion Transformer for Bimanual Dexterous Manipulation with a Plugin Tactile Adapter</a></td>
<td nowrap>双臂机器人</td>
<td nowrap>触觉/接触</td>
<td nowrap>diffusion policy / tactile policy / diffusion transformer / 双臂操作</td>
<td nowrap>diffusion policy / tactile policy / diffusion transformer</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66358">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62192">RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation</a></td>
<td nowrap>双臂机器人</td>
<td nowrap>-</td>
<td nowrap>bimanual policy / 双臂操作</td>
<td nowrap>sim data generator / domain randomization / benchmark</td>
<td nowrap>Sim + Benchmark</td>
<td nowrap>提供评测任务和数据基准</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62192">paper</a> / <a href="https://arxiv.org/pdf/2506.18088">📄 Paper</a> / <a href="https://arxiv.org/abs/2506.18088">RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation</a></td>
<td nowrap><a href="https://robotwin-platform.github.io/">🌍 Web</a></td>
<td nowrap><a href="https://github.com/RoboTwin-Platform/RoboTwin">💻 Code</a> / <a href="https://github.com/robotwin-Platform/RoboTwin">💻</a></td>
<td nowrap><a href="https://huggingface.co/datasets/TianxingChen/RoboTwin2.0">📦 Dataset</a></td>
<td nowrap>EAI-Guide, EAI-VLA-VLN, Efficient-VLA, WAM, RL-VLA</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.09186">Rethinking Bimanual Robotic Manipulation: Learning with Decoupled Interaction Framework</a></td>
<td nowrap>双臂机器人</td>
<td nowrap>-</td>
<td nowrap>bimanual policy / 双臂操作</td>
<td nowrap>bimanual policy</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2503.09186">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2412.06779">AnyBimanual: Transferring Unimanual Policy for General Bimanual Manipulation</a></td>
<td nowrap>双臂机器人</td>
<td nowrap>-</td>
<td nowrap>bimanual policy / 双臂操作</td>
<td nowrap>unimanual-to-bimanual transfer / few bimanual demonstrations</td>
<td nowrap>Sim + Real</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2412.06779">paper</a></td>
<td nowrap><a href="https://anybimanual.github.io/">project</a></td>
<td nowrap><a href="https://github.com/Tengbo-Yu/AnyBimanual">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.23152">DexH2R: A Benchmark for Dynamic Dexterous Grasping in Human-to-Robot Handover</a></td>
<td nowrap>灵巧手/抓取</td>
<td nowrap>-</td>
<td nowrap>bimanual policy / 双臂操作</td>
<td nowrap>bimanual policy</td>
<td nowrap>Real + Benchmark</td>
<td nowrap>提供评测任务和数据基准</td>
<td nowrap><a href="https://arxiv.org/abs/2506.23152">paper</a></td>
<td nowrap><a href="https://dexh2r.github.io/">project</a></td>
<td nowrap><a href="https://github.com/4DVLab/DexH2R">code</a></td>
<td nowrap><a href="https://dexh2r.github.io/">DexH2R benchmark</a></td>
<td nowrap>-</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.10743">KStar Diffuser: Spatial-Temporal Graph Diffusion Policy with Kinematics Modeling for Bimanual Robotic Manipulation</a></td>
<td nowrap>双臂机器人</td>
<td nowrap>-</td>
<td nowrap>diffusion policy / 双臂操作</td>
<td nowrap>spatial-temporal graph diffusion policy + differentiable kinematics</td>
<td nowrap>Sim + Real</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2503.10743">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>HCP-Survey</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2501.04595">MobileH2R: Learning Generalizable Human to Mobile Robot Handover Exclusively from Scalable and Diverse Synthetic Data</a></td>
<td nowrap>灵巧手/抓取</td>
<td nowrap>-</td>
<td nowrap>bimanual policy / 双臂操作</td>
<td nowrap>synthetic data + 4D imitation learning</td>
<td nowrap>Sim training + Real evaluation</td>
<td nowrap>协调双臂协作操作</td>
<td nowrap><a href="https://arxiv.org/abs/2501.04595">paper</a></td>
<td nowrap><a href="https://mobileh2r.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Humanoid-RL</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
</tbody>
</table>

#### dexterous hand

共 27 篇。

<table>
<thead>
<tr>
<th nowrap>会议/年份</th>
<th nowrap>论文/方法</th>
<th nowrap>本体类型</th>
<th nowrap>传感/接触</th>
<th nowrap>控制接口</th>
<th nowrap>训练方式</th>
<th nowrap>Sim/Real</th>
<th nowrap>问题/目标</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>来源</th>
<th nowrap>调研判断</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=Bf4FeuW0Mr">DemoGrasp: Universal Dexterous Grasping from a Single Demonstration</a></td>
<td nowrap>灵巧手/抓取</td>
<td nowrap>-</td>
<td nowrap>dexterous manipulation / 灵巧手/抓取</td>
<td nowrap>single demonstration + RL trajectory editing</td>
<td nowrap>Sim + Real</td>
<td nowrap>提升灵巧操作能力</td>
<td nowrap><a href="https://openreview.net/forum?id=Bf4FeuW0Mr">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/BeingBeyond/DemoGrasp">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=80vjyj5o7l">DexNDM: Closing the Reality Gap for Dexterous In-Hand Rotation via Joint-Wise Neural Dynamics Model</a></td>
<td nowrap>灵巧手/抓取</td>
<td nowrap>-</td>
<td nowrap>dexterous manipulation / 灵巧手/抓取</td>
<td nowrap>sim policy + joint-wise neural dynamics model + real data adaptation</td>
<td nowrap>Sim-to-Real</td>
<td nowrap>提升灵巧操作能力</td>
<td nowrap><a href="https://openreview.net/forum?id=80vjyj5o7l">paper</a></td>
<td nowrap><a href="https://meowuu7.github.io/DexNDM/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=FFxkFMU89E">EgoDex: Learning Dexterous Manipulation from Large-Scale Egocentric Video</a></td>
<td nowrap>灵巧手/抓取</td>
<td nowrap>-</td>
<td nowrap>dexterous manipulation / 灵巧手/抓取</td>
<td nowrap>dexterous manipulation</td>
<td nowrap>-</td>
<td nowrap>提升灵巧操作能力</td>
<td nowrap><a href="https://openreview.net/forum?id=FFxkFMU89E">paper</a> / <a href="https://arxiv.org/pdf/2505.11709">📄 Paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/apple/ml-egodex">code/data</a></td>
<td nowrap><a href="https://github.com/apple/ml-egodex">EgoDex dataset/benchmark</a></td>
<td nowrap>Humanoid-RL, WAM</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=Kt9tJeOwjy">RFS: Reinforcement learning with Residual flow steering for dexterous manipulation</a></td>
<td nowrap>灵巧手/抓取</td>
<td nowrap>触觉/接触</td>
<td nowrap>dexterous manipulation / 灵巧手/抓取</td>
<td nowrap>dexterous manipulation</td>
<td nowrap>-</td>
<td nowrap>提升灵巧操作能力</td>
<td nowrap><a href="https://openreview.net/forum?id=Kt9tJeOwjy">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=NZDaMcpXZm">Learning to Grasp Anything By Playing with Random Toys</a></td>
<td nowrap>灵巧手/抓取</td>
<td nowrap>-</td>
<td nowrap>dexterous manipulation / 灵巧手/抓取</td>
<td nowrap>randomized toy demonstrations / object-centric visual policy</td>
<td nowrap>Sim + Real</td>
<td nowrap>提升灵巧操作能力</td>
<td nowrap><a href="https://openreview.net/forum?id=NZDaMcpXZm">paper</a></td>
<td nowrap><a href="https://lego-grasp.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Humanoid-RL</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=aemqAxScl9">SARM: Stage-Aware Reward Modeling for Long Horizon Robot Manipulation</a></td>
<td nowrap>灵巧手/抓取</td>
<td nowrap>-</td>
<td nowrap>dexterous manipulation / 灵巧手/抓取</td>
<td nowrap>dexterous manipulation</td>
<td nowrap>-</td>
<td nowrap>提升灵巧操作能力</td>
<td nowrap><a href="https://openreview.net/forum?id=aemqAxScl9">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=cVX3VqO8BO">UniHM: Unified Dexterous Hand Manipulation with Vision Language Model</a></td>
<td nowrap>灵巧手/抓取</td>
<td nowrap>视觉</td>
<td nowrap>dexterous manipulation / 灵巧手/抓取</td>
<td nowrap>dexterous manipulation</td>
<td nowrap>-</td>
<td nowrap>提升灵巧操作能力</td>
<td nowrap><a href="https://openreview.net/forum?id=cVX3VqO8BO">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=k8ovuXEQQu">Cross-Embodied Co-Design for Dexterous Hands</a></td>
<td nowrap>灵巧手/抓取</td>
<td nowrap>-</td>
<td nowrap>dexterous manipulation / 灵巧手/抓取</td>
<td nowrap>dexterous manipulation</td>
<td nowrap>-</td>
<td nowrap>提升灵巧操作能力</td>
<td nowrap><a href="https://openreview.net/forum?id=k8ovuXEQQu">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=tv0Sz8A9Tc">Robotic Manipulation by Imitating Generated Videos Without Physical Demonstrations</a></td>
<td nowrap>灵巧手/抓取</td>
<td nowrap>-</td>
<td nowrap>dexterous manipulation / 灵巧手/抓取</td>
<td nowrap>dexterous manipulation</td>
<td nowrap>-</td>
<td nowrap>提升灵巧操作能力</td>
<td nowrap><a href="https://openreview.net/forum?id=tv0Sz8A9Tc">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-Guide, HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Efficient-VLA, Robot-Learning, Humanoid-RL, EAI-Safety, WAM, RL-VLA</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=wySMuWHmt4">Primary-Fine Decoupling for Action Generation in Robotic Imitation</a></td>
<td nowrap>灵巧手/抓取</td>
<td nowrap>-</td>
<td nowrap>dexterous manipulation / 灵巧手/抓取</td>
<td nowrap>dexterous manipulation</td>
<td nowrap>-</td>
<td nowrap>提升灵巧操作能力</td>
<td nowrap><a href="https://openreview.net/forum?id=wySMuWHmt4">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=13jshGCK9i">D-REX: Differentiable Real-to-Sim-to-Real Engine for Learning Dexterous Grasping</a></td>
<td nowrap>灵巧手/抓取</td>
<td nowrap>-</td>
<td nowrap>dexterous manipulation / 灵巧手/抓取</td>
<td nowrap>differentiable real-to-sim-to-real / force-aware grasping</td>
<td nowrap>Real-to-Sim-to-Real</td>
<td nowrap>提升灵巧操作能力</td>
<td nowrap><a href="https://openreview.net/forum?id=13jshGCK9i">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/louhz/D-rex">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=RYwQ0xQcAh">Interaction-aware Representation Modeling With Co-Occurrence Consistency for Egocentric Hand-Object Parsing</a></td>
<td nowrap>灵巧手/抓取</td>
<td nowrap>-</td>
<td nowrap>dexterous manipulation / 灵巧手/抓取</td>
<td nowrap>dexterous manipulation</td>
<td nowrap>-</td>
<td nowrap>提升灵巧操作能力</td>
<td nowrap><a href="https://openreview.net/forum?id=RYwQ0xQcAh">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38873">GRIM: Task-Oriented Grasping with Conditioning on Generative Examples</a></td>
<td nowrap>灵巧手/抓取</td>
<td nowrap>-</td>
<td nowrap>dexterous manipulation / 灵巧手/抓取</td>
<td nowrap>dexterous manipulation</td>
<td nowrap>-</td>
<td nowrap>提升灵巧操作能力</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38873">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38874">Dexterous Manipulation Transfer via Progressive Kinematic-Dynamic Alignment</a></td>
<td nowrap>灵巧手/抓取</td>
<td nowrap>-</td>
<td nowrap>dexterous manipulation / 灵巧手/抓取</td>
<td nowrap>dexterous manipulation</td>
<td nowrap>-</td>
<td nowrap>提升灵巧操作能力</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38874">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Humanoid-RL, WAM</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38892">Learning Object-Centric Motion Priors from Human for Robotic Dexterous Manipulation</a></td>
<td nowrap>灵巧手/抓取</td>
<td nowrap>-</td>
<td nowrap>dexterous manipulation / 灵巧手/抓取</td>
<td nowrap>dexterous manipulation</td>
<td nowrap>-</td>
<td nowrap>提升灵巧操作能力</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38892">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38894">Real Garment Benchmark (RGBench): A Comprehensive Benchmark for Robotic Garment Manipulation Featuring a High-Fidelity Scalable Simulator</a></td>
<td nowrap>灵巧手/抓取</td>
<td nowrap>视觉</td>
<td nowrap>dexterous manipulation / 灵巧手/抓取</td>
<td nowrap>dexterous manipulation</td>
<td nowrap>Real garment data + simulator benchmark</td>
<td nowrap>提升灵巧操作能力</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38894">paper</a></td>
<td nowrap><a href="https://rgbench.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://rgbench.github.io/">RGBench</a></td>
<td nowrap>-</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38940">GraphGrasp: Lightweight and Efficient Graph-Guided 6-DoF Robotic Grasp Pose Estimation Network</a></td>
<td nowrap>灵巧手/抓取</td>
<td nowrap>-</td>
<td nowrap>dexterous manipulation / 灵巧手/抓取</td>
<td nowrap>dexterous manipulation</td>
<td nowrap>-</td>
<td nowrap>提升灵巧操作能力</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38940">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38953">DexGraspVLA: A Vision-Language-Action Framework Towards General Dexterous Grasping</a></td>
<td nowrap>灵巧手/抓取</td>
<td nowrap>视觉</td>
<td nowrap>VLM high-level planner + diffusion low-level controller</td>
<td nowrap>dexterous manipulation</td>
<td nowrap>-</td>
<td nowrap>提升灵巧操作能力</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38953">paper</a></td>
<td nowrap><a href="https://dexgraspvla.github.io/">project</a></td>
<td nowrap><a href="https://github.com/Psi-Robot/DexGraspVLA">code</a></td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN, Awesome-VLA</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38957">Effective Robotic Cloth Grasping Through Suppressing False Discoveries</a></td>
<td nowrap>灵巧手/抓取</td>
<td nowrap>-</td>
<td nowrap>dexterous manipulation / 灵巧手/抓取</td>
<td nowrap>dexterous manipulation</td>
<td nowrap>-</td>
<td nowrap>提升灵巧操作能力</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38957">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2603.22264">UniDex: A Robot Foundation Suite for Universal Dexterous Hand Control from Egocentric Human Videos</a></td>
<td nowrap>灵巧手/抓取</td>
<td nowrap>-</td>
<td nowrap>VLA / 灵巧手/抓取</td>
<td nowrap>3D VLA pretraining on UniDex-Dataset + task finetuning</td>
<td nowrap>-</td>
<td nowrap>提升灵巧操作能力</td>
<td nowrap><a href="https://arxiv.org/abs/2603.22264">paper</a></td>
<td nowrap><a href="https://unidex-ai.github.io/">project</a></td>
<td nowrap><a href="https://github.com/unidex-ai/UniDex">code</a></td>
<td nowrap><a href="https://unidex-ai.github.io/">UniDex-Dataset</a></td>
<td nowrap>-</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/pdf/2511.01276">Contact Map Transfer with Conditional Diffusion Model for Generalizable Dexterous Grasp Generation</a></td>
<td nowrap>灵巧手/抓取</td>
<td nowrap>触觉/接触</td>
<td nowrap>diffusion policy / 灵巧手/抓取</td>
<td nowrap>diffusion policy</td>
<td nowrap>-</td>
<td nowrap>提升灵巧操作能力</td>
<td nowrap><a href="https://arxiv.org/pdf/2511.01276">paper</a></td>
<td nowrap><a href="https://cmtdiffusion.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.02489">Grasp2Grasp: Vision-Based Dexterous Grasp Translation via Schrödinger Bridges</a></td>
<td nowrap>灵巧手/抓取</td>
<td nowrap>视觉</td>
<td nowrap>dexterous manipulation / 灵巧手/抓取</td>
<td nowrap>dexterous manipulation</td>
<td nowrap>-</td>
<td nowrap>提升灵巧操作能力</td>
<td nowrap><a href="https://arxiv.org/abs/2506.02489">paper</a></td>
<td nowrap><a href="https://grasp2grasp.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.19212">Scaffolding Dexterous Manipulation with Vision-Language Models</a></td>
<td nowrap>灵巧手/抓取</td>
<td nowrap>视觉</td>
<td nowrap>dexterous manipulation / 灵巧手/抓取</td>
<td nowrap>dexterous manipulation</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2506.19212">paper</a></td>
<td nowrap><a href="https://sites.google.com/view/dexterous-vlm-scaffolding">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2505.11032">DexGarmentLab: Dexterous Garment Manipulation Environment with Generalizable Policy</a></td>
<td nowrap>灵巧手/抓取</td>
<td nowrap>-</td>
<td nowrap>dexterous manipulation / 灵巧手/抓取</td>
<td nowrap>dexterous manipulation</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2505.11032">paper</a></td>
<td nowrap><a href="https://wayrise.github.io/DexGarmentLab/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2412.02699">UniGraspTransformer: Simplified Policy Distillation for Scalable Dexterous Robotic Grasping</a></td>
<td nowrap>灵巧手/抓取</td>
<td nowrap>-</td>
<td nowrap>dexterous manipulation / 灵巧手/抓取</td>
<td nowrap>dexterous manipulation</td>
<td nowrap>-</td>
<td nowrap>提升灵巧操作能力</td>
<td nowrap><a href="https://arxiv.org/abs/2412.02699">paper</a></td>
<td nowrap><a href="https://dexhand.github.io/UniGraspTransformer/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.08257">DexGrasp Anything: Towards Universal Robotic Dexterous Grasping with Physics Awareness</a></td>
<td nowrap>灵巧手/抓取</td>
<td nowrap>-</td>
<td nowrap>dexterous manipulation / 灵巧手/抓取</td>
<td nowrap>dexterous manipulation</td>
<td nowrap>-</td>
<td nowrap>提升灵巧操作能力</td>
<td nowrap><a href="https://arxiv.org/abs/2503.08257">paper</a></td>
<td nowrap><a href="https://dexgraspanything.github.io/">project</a></td>
<td nowrap><a href="https://github.com/4DVLab/DexGrasp-Anything">code</a></td>
<td nowrap>3.4M dexterous grasp poses / 15K objects</td>
<td nowrap>HCP-Survey, EAI-VLA-VLN</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://cvpr.thecvf.com/virtual/2025/poster/32440">ZeroGrasp: Zero-Shot Shape Reconstruction Enabled Robotic Grasping</a></td>
<td nowrap>灵巧手/抓取</td>
<td nowrap>-</td>
<td nowrap>dexterous manipulation / 灵巧手/抓取</td>
<td nowrap>dexterous manipulation</td>
<td nowrap>-</td>
<td nowrap>处理高自由度灵巧操作</td>
<td nowrap><a href="https://cvpr.thecvf.com/virtual/2025/poster/32440">paper</a></td>
<td nowrap><a href="https://sh8.io/#/zerograsp">project</a></td>
<td nowrap><a href="https://github.com/sh8/ZeroGrasp">code</a></td>
<td nowrap>synthetic dataset + GraspNet-1B evaluation</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
</tbody>
</table>

#### tactile/contact-rich

共 13 篇。

<table>
<thead>
<tr>
<th nowrap>会议/年份</th>
<th nowrap>论文/方法</th>
<th nowrap>本体类型</th>
<th nowrap>传感/接触</th>
<th nowrap>控制接口</th>
<th nowrap>训练方式</th>
<th nowrap>Sim/Real</th>
<th nowrap>问题/目标</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>来源</th>
<th nowrap>调研判断</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=dT3ZciXvNX">DexMove: Learning Tactile-Guided Non-Prehensile Manipulation with Dexterous Hands</a></td>
<td nowrap>触觉/接触操作</td>
<td nowrap>触觉/接触</td>
<td nowrap>tactile policy / 灵巧手/抓取</td>
<td nowrap>simulation trajectories + wearable visuotactile human contact data + flow policy</td>
<td nowrap>Sim + Real</td>
<td nowrap>引入触觉提升接触操作</td>
<td nowrap><a href="https://openreview.net/forum?id=dT3ZciXvNX">paper</a></td>
<td nowrap><a href="https://peilin-666.github.io/projects/DexMove/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=ndilONnABZ">AnyTouch 2: General Optical Tactile Representation Learning For Dynamic Tactile Perception</a></td>
<td nowrap>触觉/接触操作</td>
<td nowrap>触觉/接触</td>
<td nowrap>tactile policy / 触觉/接触</td>
<td nowrap>tactile policy</td>
<td nowrap>-</td>
<td nowrap>引入触觉提升接触操作</td>
<td nowrap><a href="https://openreview.net/forum?id=ndilONnABZ">paper</a></td>
<td nowrap><a href="https://gewu-lab.github.io/AnyTouch2/">project</a></td>
<td nowrap><a href="https://github.com/GeWu-Lab/AnyTouch2">code</a></td>
<td nowrap><a href="https://huggingface.co/collections/BAAI/touchd">ToucHD</a> / <a href="https://huggingface.co/xxuan01/AnyTouch2-Model">AnyTouch2 checkpoint</a></td>
<td nowrap>-</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=hU2gT2Ucua">APPLE: Toward General Active Perception via Reinforcement Learning</a></td>
<td nowrap>触觉/接触操作</td>
<td nowrap>触觉/接触</td>
<td nowrap>tactile policy / 触觉/接触</td>
<td nowrap>tactile policy</td>
<td nowrap>-</td>
<td nowrap>引入触觉提升接触操作</td>
<td nowrap><a href="https://openreview.net/forum?id=hU2gT2Ucua">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Awesome-EAI, WAM</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38882">STOLA: Self-Adaptive Touch-Language Framework for Tactile Commonsense Reasoning in Open-Ended Scenarios</a></td>
<td nowrap>触觉/接触操作</td>
<td nowrap>触觉/接触</td>
<td nowrap>tactile policy / 触觉/接触</td>
<td nowrap>tactile policy</td>
<td nowrap>-</td>
<td nowrap>引入触觉提升接触操作</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38882">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38915">TouchFormer: A Robust Transformer-based Framework for Multimodal Material Perception</a></td>
<td nowrap>触觉/接触操作</td>
<td nowrap>触觉/接触</td>
<td nowrap>tactile policy / 触觉/接触</td>
<td nowrap>tactile policy</td>
<td nowrap>-</td>
<td nowrap>引入触觉提升接触操作</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38915">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38956">Collaborative Representation Learning for Alignment of Tactile, Language, and Vision Modalities</a></td>
<td nowrap>触觉/接触操作</td>
<td nowrap>触觉/接触</td>
<td nowrap>tactile policy / 触觉/接触</td>
<td nowrap>tactile policy</td>
<td nowrap>-</td>
<td nowrap>引入触觉提升接触操作</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38956">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66793">Cross-Tactile Sensor Representation Learning</a></td>
<td nowrap>触觉/接触操作</td>
<td nowrap>触觉/接触</td>
<td nowrap>tactile policy / 触觉/接触</td>
<td nowrap>tactile policy</td>
<td nowrap>-</td>
<td nowrap>引入触觉提升接触操作</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66793">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/65669">Tabero: Learning Gentle Manipulation with Closed-Loop Force Feedback from Vision, Touch, and Language</a></td>
<td nowrap>触觉/接触操作</td>
<td nowrap>触觉/接触</td>
<td nowrap>decoupled force-position commands + fixed hybrid controller</td>
<td nowrap>tactile policy</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/65669">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/NathanWu7/Tabero">code</a></td>
<td nowrap>Tabero benchmark/model suite</td>
<td nowrap>-</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2505.22566">Universal Visuo-Tactile Video Understanding for Embodied Interaction</a></td>
<td nowrap>触觉/接触操作</td>
<td nowrap>触觉/接触</td>
<td nowrap>tactile policy / 触觉/接触</td>
<td nowrap>tactile policy</td>
<td nowrap>-</td>
<td nowrap>引入触觉提升接触操作</td>
<td nowrap><a href="https://arxiv.org/abs/2505.22566">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/IvanXie416/VTV-LLM">code</a></td>
<td nowrap><a href="https://huggingface.co/datasets/Ivan416/VBTS_video">VBTS_video</a> / <a href="https://huggingface.co/Ivan416/VBTS_video_encoder">VBTS encoder</a></td>
<td nowrap>-</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2510.21609">Enhancing Tactile-based Reinforcement Learning for Robotic Control</a></td>
<td nowrap>触觉/接触操作</td>
<td nowrap>触觉/接触</td>
<td nowrap>tactile policy / RL / 触觉/接触</td>
<td nowrap>tactile RL + self-supervised representation learning</td>
<td nowrap>-</td>
<td nowrap>引入触觉提升接触操作</td>
<td nowrap><a href="https://arxiv.org/abs/2510.21609">paper</a></td>
<td nowrap><a href="https://elle-miller.github.io/tactile_rl/">project</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://elle-miller.github.io/tactile_rl/">RoTO benchmark</a></td>
<td nowrap>-</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://taccel-simulator.github.io/assets/taccel-paper.pdf">Taccel: Scaling Up Vision-based Tactile Robotics via High-performance GPU Simulation</a></td>
<td nowrap>触觉/接触操作</td>
<td nowrap>触觉/接触</td>
<td nowrap>tactile policy / 触觉/接触</td>
<td nowrap>tactile policy</td>
<td nowrap>Simulation</td>
<td nowrap>引入触觉提升接触操作</td>
<td nowrap>-</td>
<td nowrap><a href="https://taccel-simulator.github.io/">project</a></td>
<td nowrap><a href="https://github.com/Taccel-Simulator/Taccel">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2511.16596">Toward Artificial Palpation: Representation Learning of Touch on Soft Bodies</a></td>
<td nowrap>触觉/接触操作</td>
<td nowrap>触觉/接触</td>
<td nowrap>tactile policy / 触觉/接触</td>
<td nowrap>tactile policy</td>
<td nowrap>-</td>
<td nowrap>处理触觉和接触丰富任务</td>
<td nowrap><a href="https://arxiv.org/abs/2511.16596">paper</a></td>
<td nowrap><a href="https://zoharri.github.io/artificial-palpation/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2507.15062v1">Touch in the Wild: Learning Fine-Grained Manipulation with a Portable Visuo-Tactile Gripper</a></td>
<td nowrap>触觉/接触操作</td>
<td nowrap>vision + tactile + proprioception</td>
<td nowrap>tactile policy / 触觉/接触</td>
<td nowrap>visuo-tactile pretraining + downstream imitation learning</td>
<td nowrap>Real / in-the-wild data + real robot tasks</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2507.15062v1">paper</a></td>
<td nowrap><a href="https://binghao-huang.github.io/touch_in_the_wild/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于观察本体差异如何改变控制和数据需求。</td>
</tr>
</tbody>
</table>

### 轻量化 / 评测 / 数据

这一方向决定能不能真实部署：端侧推理、缓存/量化/action tokenization、实时执行、sim2real、benchmark 和 safety evaluation 都是必需条件。

子方向：quantization/cache/tokenization、real-time execution、benchmark/dataset、sim2real、safety evaluation。

共 79 篇。

<table>
<thead>
<tr>
<th nowrap>子方向</th>
<th nowrap>条目数</th>
<th nowrap>观察重点</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>quantization/cache/tokenization</td>
<td nowrap>17</td>
<td nowrap>看端侧部署、缓存复用和 action token 效率。</td>
</tr>
<tr>
<td nowrap>real-time execution</td>
<td nowrap>6</td>
<td nowrap>看低延迟执行和实时策略推理。</td>
</tr>
<tr>
<td nowrap>benchmark/dataset</td>
<td nowrap>30</td>
<td nowrap>看数据覆盖、任务设计和评测可信度。</td>
</tr>
<tr>
<td nowrap>sim2real</td>
<td nowrap>17</td>
<td nowrap>看仿真到真实迁移和真实部署差距。</td>
</tr>
<tr>
<td nowrap>safety evaluation</td>
<td nowrap>9</td>
<td nowrap>看鲁棒性、安全性和部署风险评估。</td>
</tr>
</tbody>
</table>

#### quantization/cache/tokenization

共 17 篇。

<table>
<thead>
<tr>
<th nowrap>会议/年份</th>
<th nowrap>论文/方法</th>
<th nowrap>对象类型</th>
<th nowrap>效率指标</th>
<th nowrap>平台/硬件</th>
<th nowrap>覆盖任务</th>
<th nowrap>开放资源状态</th>
<th nowrap>问题/目标</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>来源</th>
<th nowrap>调研判断</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=E1K2Ph3LtS">MetaVLA: Unified Meta Co-Training for Efficient Embodied Adaptation</a></td>
<td nowrap>压缩/缓存/tokenization</td>
<td nowrap>tokenization</td>
<td nowrap>机器人部署/评测环境</td>
<td nowrap>提升推理或执行效率</td>
<td nowrap>-</td>
<td nowrap>提升推理或执行效率</td>
<td nowrap><a href="https://openreview.net/forum?id=E1K2Ph3LtS">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=RwdGIIjPlC">SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration</a></td>
<td nowrap>压缩/缓存/tokenization</td>
<td nowrap>tokenization</td>
<td nowrap>机器人部署/评测环境</td>
<td nowrap>提升推理或执行效率</td>
<td nowrap>-</td>
<td nowrap>提升推理或执行效率</td>
<td nowrap><a href="https://openreview.net/forum?id=RwdGIIjPlC">paper</a> / <a href="https://arxiv.org/abs/2506.12723">SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Efficient-VLA</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=TpL2nXanru">AutoQVLA: Not All Channels Are Equal in Vision-Language-Action Model's Quantization</a></td>
<td nowrap>压缩/缓存/tokenization</td>
<td nowrap>quantization</td>
<td nowrap>机器人部署/评测环境</td>
<td nowrap>提升推理或执行效率</td>
<td nowrap>-</td>
<td nowrap>提升推理或执行效率</td>
<td nowrap><a href="https://openreview.net/forum?id=TpL2nXanru">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=ea6j8k8Rnw">Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation</a></td>
<td nowrap>压缩/缓存/tokenization</td>
<td nowrap>tokenization</td>
<td nowrap>机器人部署/评测环境</td>
<td nowrap>提升推理或执行效率</td>
<td nowrap>-</td>
<td nowrap>提升推理或执行效率</td>
<td nowrap><a href="https://openreview.net/forum?id=ea6j8k8Rnw">paper</a> / <a href="https://arxiv.org/abs/2509.22093">Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN, Efficient-VLA</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=k6nTUFoqeT">FASTer: Toward Powerful and Efficient Autoregressive Vision–Language–Action Models with Learnable Action Tokenizer and Block-wise Decoding</a></td>
<td nowrap>压缩/缓存/tokenization</td>
<td nowrap>tokenization</td>
<td nowrap>机器人部署/评测环境</td>
<td nowrap>提升推理或执行效率</td>
<td nowrap>-</td>
<td nowrap>提升推理或执行效率</td>
<td nowrap><a href="https://openreview.net/forum?id=k6nTUFoqeT">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>HCP-Survey, Awesome-EAI, EAI-VLA-VLN, EAI-Safety, RL-VLA</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38880">FT-NCFM: An Influence-Aware Data Distillation Framework for Efficient VLA Models</a></td>
<td nowrap>压缩/缓存/tokenization</td>
<td nowrap>tokenization</td>
<td nowrap>机器人部署/评测环境</td>
<td nowrap>提升推理或执行效率</td>
<td nowrap>-</td>
<td nowrap>提升推理或执行效率</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38880">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38903">Towards Efficient and Robust Manipulation via Multi-Frame Vision-Language-Action Modeling</a></td>
<td nowrap>压缩/缓存/tokenization</td>
<td nowrap>tokenization</td>
<td nowrap>机器人部署/评测环境</td>
<td nowrap>提升推理或执行效率</td>
<td nowrap>-</td>
<td nowrap>提升推理或执行效率</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38903">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38904">SemanticVLA: Semantic-Aligned Sparsification and Enhancement for Efficient Robotic Manipulation</a></td>
<td nowrap>压缩/缓存/tokenization</td>
<td nowrap>tokenization</td>
<td nowrap>机器人部署/评测环境</td>
<td nowrap>提升推理或执行效率</td>
<td nowrap>-</td>
<td nowrap>提升推理或执行效率</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38904">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38931">VLA-Adapter: An Effective Paradigm for Tiny-Scale Vision-Language-Action Model</a></td>
<td nowrap>压缩/缓存/tokenization</td>
<td nowrap>tokenization</td>
<td nowrap>机器人部署/评测环境</td>
<td nowrap>提升推理或执行效率</td>
<td nowrap>Project+Code</td>
<td nowrap>提升推理或执行效率</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38931">paper</a> / <a href="https://arxiv.org/abs/2509.09372">VLA-Adapter: An Effective Paradigm for Tiny-Scale Vision-Language-Action Model</a></td>
<td nowrap><a href="https://vla-adapter.github.io/">🌐</a></td>
<td nowrap><a href="https://github.com/OpenHelix-Team/VLA-Adapter">💻</a></td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN, Awesome-VLA, Efficient-VLA, RL-VLA</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38945">MoLe-VLA: Dynamic Layer-skipping Vision Language Action Model via Mixture-of-Layers for Efficient Robot Manipulation</a></td>
<td nowrap>压缩/缓存/tokenization</td>
<td nowrap>dynamic layer skipping / mixture-of-layers; up to 5.6x compute reduction</td>
<td nowrap>机器人部署/评测环境</td>
<td nowrap>提升推理或执行效率</td>
<td nowrap>Project+Code</td>
<td nowrap>提升推理或执行效率</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38945">paper</a> / <a href="https://arxiv.org/abs/2503.20384">MoLe-VLA: Dynamic Layer-skipping Vision Language Action Model via Mixture-of-Layers for Efficient Robot Manipulation</a></td>
<td nowrap><a href="https://sites.google.com/view/mole-vla">🌐</a></td>
<td nowrap><a href="https://github.com/RoyZry98/MoLe-VLA-Pytorch/">💻</a></td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN, Efficient-VLA</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2602.20309">QuantVLA: Scale-Calibrated Post-Training Quantization for Vision-Language-Action Models</a></td>
<td nowrap>压缩/缓存/tokenization</td>
<td nowrap>PTQ; about 70% memory savings; 1.22x latency speedup</td>
<td nowrap>机器人部署/评测环境</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap>Project+Code</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://arxiv.org/abs/2602.20309">paper</a></td>
<td nowrap><a href="https://quantvla.github.io/">project</a></td>
<td nowrap><a href="https://github.com/AIoT-MLSys-Lab/QuantVLA">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.06072">BEAST: Efficient Tokenization of B-Splines Encoded Action Sequences for Imitation Learning</a></td>
<td nowrap>压缩/缓存/tokenization</td>
<td nowrap>tokenization</td>
<td nowrap>机器人部署/评测环境</td>
<td nowrap>提升推理或执行效率</td>
<td nowrap>-</td>
<td nowrap>提升推理或执行效率</td>
<td nowrap><a href="https://arxiv.org/abs/2506.06072">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.14259">Quantization-Free Autoregressive Action Transformer</a></td>
<td nowrap>压缩/缓存/tokenization</td>
<td nowrap>quantization-free continuous autoregressive action modeling</td>
<td nowrap>机器人部署/评测环境</td>
<td nowrap>降低模型部署成本</td>
<td nowrap>Code</td>
<td nowrap>降低模型部署成本</td>
<td nowrap><a href="https://arxiv.org/abs/2503.14259">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/ziyadsheeba/qfat">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.10100">EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models</a></td>
<td nowrap>压缩/缓存/tokenization</td>
<td nowrap>layer pruning + visual token selection + diffusion feature caching; 1.93x inference speedup</td>
<td nowrap>机器人部署/评测环境</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://arxiv.org/abs/2506.10100">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Efficient-VLA</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2502.02175">VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching</a></td>
<td nowrap>压缩/缓存/tokenization</td>
<td nowrap>cache</td>
<td nowrap>机器人部署/评测环境</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap>Project+Code</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://arxiv.org/abs/2502.02175">paper</a></td>
<td nowrap><a href="https://vla-cache.github.io/">project</a></td>
<td nowrap><a href="https://github.com/siyuhsu/vla-cache">💻</a></td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN, Efficient-VLA</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2507.01016">VQ-VLA: Improving Vision-Language-Action Models via Scaling Vector-Quantized Action Tokenizers</a></td>
<td nowrap>压缩/缓存/tokenization</td>
<td nowrap>quantization</td>
<td nowrap>机器人部署/评测环境</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap>Project+Code</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://arxiv.org/abs/2507.01016">paper</a></td>
<td nowrap><a href="https://xiaoxiao0406.github.io/vqvla.github.io">project</a> / <a href="https://xiaoxiao0406.github.io/vqvla.github.io/">🌐</a></td>
<td nowrap><a href="https://github.com/xiaoxiao0406/VQ-VLA">💻</a></td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN, Efficient-VLA</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2505.15304">Saliency-Aware Quantized Imitation Learning for Efficient Robotic Control</a></td>
<td nowrap>压缩/缓存/tokenization</td>
<td nowrap>quantization</td>
<td nowrap>机器人部署/评测环境</td>
<td nowrap>提升推理或执行效率</td>
<td nowrap>-</td>
<td nowrap>提升推理或执行效率</td>
<td nowrap><a href="https://arxiv.org/abs/2505.15304">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Efficient-VLA</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
</tbody>
</table>

#### real-time execution

共 6 篇。

<table>
<thead>
<tr>
<th nowrap>会议/年份</th>
<th nowrap>论文/方法</th>
<th nowrap>对象类型</th>
<th nowrap>效率指标</th>
<th nowrap>平台/硬件</th>
<th nowrap>覆盖任务</th>
<th nowrap>开放资源状态</th>
<th nowrap>问题/目标</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>来源</th>
<th nowrap>调研判断</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=INsLvSCJ4z">Time Optimal Execution of Action Chunk Policies Beyond Demonstration Speed</a></td>
<td nowrap>实时执行</td>
<td nowrap>real-time</td>
<td nowrap>机器人部署/评测环境</td>
<td nowrap>提升实时执行能力</td>
<td nowrap>-</td>
<td nowrap>提升实时执行能力</td>
<td nowrap><a href="https://openreview.net/forum?id=INsLvSCJ4z">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=mIeKe74W43">Mean Flow Policy with Instantaneous Velocity Constraint for One-step Action Generation</a></td>
<td nowrap>实时执行</td>
<td nowrap>real-time</td>
<td nowrap>机器人部署/评测环境</td>
<td nowrap>提升实时执行能力</td>
<td nowrap>-</td>
<td nowrap>提升实时执行能力</td>
<td nowrap><a href="https://openreview.net/forum?id=mIeKe74W43">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=r0RGJ1j9on">Real-Time Robot Execution with Masked Action Chunking</a></td>
<td nowrap>实时执行</td>
<td nowrap>real-time</td>
<td nowrap>机器人部署/评测环境</td>
<td nowrap>提升实时执行能力</td>
<td nowrap>-</td>
<td nowrap>提升实时执行能力</td>
<td nowrap><a href="https://openreview.net/forum?id=r0RGJ1j9on">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Efficient-VLA, Humanoid-RL, EAI-Safety, WAM</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://www.physicalintelligence.company/download/real_time_chunking.pdf">Real-Time Execution of Action Chunking Flow Policies</a></td>
<td nowrap>实时执行</td>
<td nowrap>real-time</td>
<td nowrap>机器人部署/评测环境</td>
<td nowrap>提升实时执行能力</td>
<td nowrap>Project</td>
<td nowrap>提升实时执行能力</td>
<td nowrap><a href="https://www.physicalintelligence.company/download/real_time_chunking.pdf">paper</a></td>
<td nowrap><a href="https://www.physicalintelligence.company/research/real_time_chunking">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Efficient-VLA, Humanoid-RL, EAI-Safety, WAM</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://www.arxiv.org/abs/2505.10646">Accelerating Visual-Policy Learning through Parallel Differentiable Simulation</a></td>
<td nowrap>实时执行</td>
<td nowrap>real-time</td>
<td nowrap>仿真/评测环境</td>
<td nowrap>提升实时执行能力</td>
<td nowrap>Project</td>
<td nowrap>提升实时执行能力</td>
<td nowrap><a href="https://www.arxiv.org/abs/2505.10646">paper</a></td>
<td nowrap><a href="https://haoxiangyou.github.io/Dva_website/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2508.00697">On-Device Diffusion Transformer Policy for Efficient Robot Manipulation</a></td>
<td nowrap>实时执行</td>
<td nowrap>on-device latency; pruning/distillation for real-time mobile deployment</td>
<td nowrap>机器人部署/评测环境</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2508.00697">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN, Efficient-VLA</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
</tbody>
</table>

#### benchmark/dataset

共 30 篇。

<table>
<thead>
<tr>
<th nowrap>会议/年份</th>
<th nowrap>论文/方法</th>
<th nowrap>对象类型</th>
<th nowrap>效率指标</th>
<th nowrap>平台/硬件</th>
<th nowrap>覆盖任务</th>
<th nowrap>开放资源状态</th>
<th nowrap>问题/目标</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>来源</th>
<th nowrap>调研判断</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=TRwQND3xpt">D2E: Scaling Vision-Action Pretraining on Desktop Data for Transfer to Embodied AI</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>仿真/评测环境</td>
<td nowrap>提供评测任务和数据基准</td>
<td nowrap>-</td>
<td nowrap>提供评测任务和数据基准</td>
<td nowrap><a href="https://openreview.net/forum?id=TRwQND3xpt">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=PGUC3mmMoi">RoboInter: A Holistic Intermediate Representation Suite Towards Robotic Manipulation</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>仿真/评测环境</td>
<td nowrap>提供评测任务和数据基准</td>
<td nowrap>-</td>
<td nowrap>提供评测任务和数据基准</td>
<td nowrap><a href="https://openreview.net/forum?id=PGUC3mmMoi">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=UUE6HEtjhu">AutoBio: A Simulation and Benchmark for Robotic Automation in Digital Biology Laboratory</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>仿真/评测环境</td>
<td nowrap>提供评测任务和数据基准</td>
<td nowrap>-</td>
<td nowrap>提供评测任务和数据基准</td>
<td nowrap><a href="https://openreview.net/forum?id=UUE6HEtjhu">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=azj53PLJRL">Image Quality Assessment for Embodied AI</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>仿真/评测环境</td>
<td nowrap>提供评测任务和数据基准</td>
<td nowrap>-</td>
<td nowrap>提供评测任务和数据基准</td>
<td nowrap><a href="https://openreview.net/forum?id=azj53PLJRL">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=tQJYKwc3n4">RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>仿真/评测环境</td>
<td nowrap>提供评测任务和数据基准</td>
<td nowrap>-</td>
<td nowrap>提供评测任务和数据基准</td>
<td nowrap><a href="https://openreview.net/forum?id=tQJYKwc3n4">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Humanoid-RL</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38875">H-RDT: Human Manipulation Enhanced Bimanual Robotic Manipulation</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>仿真/评测环境</td>
<td nowrap>提供评测任务和数据基准</td>
<td nowrap>-</td>
<td nowrap>提供评测任务和数据基准</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38875">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN, Humanoid-RL</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38883">PEOD: A Pixel-Aligned Event-RGB Benchmark for Object Detection Under Challenging Conditions</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>仿真/评测环境</td>
<td nowrap>提供评测任务和数据基准</td>
<td nowrap>-</td>
<td nowrap>提供评测任务和数据基准</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38883">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38913">SIAM: Towards Generalizable Articulated Object Modeling via Single Robot-Object Interaction</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>仿真/评测环境</td>
<td nowrap>提供评测任务和数据基准</td>
<td nowrap>-</td>
<td nowrap>提供评测任务和数据基准</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38913">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38923">VirtualEnv: A Platform for Embodied AI Research</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>仿真/评测环境</td>
<td nowrap>提供评测任务和数据基准</td>
<td nowrap>-</td>
<td nowrap>提供评测任务和数据基准</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38923">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38930">Lifelong Language-Conditioned Robotic Manipulation Learning</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>仿真/评测环境</td>
<td nowrap>提供评测任务和数据基准</td>
<td nowrap>-</td>
<td nowrap>提供评测任务和数据基准</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38930">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64411">AIR-VLA: Vision-Language-Action Systems for Aerial Manipulation</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>无人机/空中机器人</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64411">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Awesome-EAI</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/63391">DLO-Lab: Benchmarking Deformable Linear Object Manipulations with Differentiable Physics</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>仿真/评测环境</td>
<td nowrap>提供评测任务和数据基准</td>
<td nowrap>-</td>
<td nowrap>提供评测任务和数据基准</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/63391">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/63416">ManiSoft: Towards Vision-Language Manipulation for Soft Robotics</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>机器人部署/评测环境</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/63416">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64619">OXE-AugE: A Large-Scale Robot Augmentation of OXE for Scaling Cross-Embodiment Policy Learning</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>机器人部署/评测环境</td>
<td nowrap>提供可复用评测资源</td>
<td nowrap>-</td>
<td nowrap>提供可复用评测资源</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64619">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.07961">BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>机器人部署/评测环境</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap>Project+Code+Data/Bench</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2506.07961">paper</a></td>
<td nowrap><a href="https://bridgevla.github.io/">project</a></td>
<td nowrap><a href="https://github.com/BridgeVLA/BridgeVLA">code</a></td>
<td nowrap><a href="https://huggingface.co/datasets/LPY/BridgeVLA">BridgeVLA dataset</a></td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.14763">RobotSmith: Generative Robotic Tool Design for Acquisition of Complex Manipulation Skill</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>机器人部署/评测环境</td>
<td nowrap>tool-design manipulation across rigid, deformable, and fluid objects</td>
<td nowrap>Project+Code</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2506.14763">paper</a></td>
<td nowrap><a href="https://umass-embodied-agi.github.io/RobotSmith/">project</a></td>
<td nowrap><a href="https://github.com/UMass-Embodied-AGI/RobotSmith">code</a></td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2511.00940">URDF-Anything: Constructing Articulated Objects with 3D Multimodal Language Model</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>机器人部署/评测环境</td>
<td nowrap>提供可复用评测资源</td>
<td nowrap>-</td>
<td nowrap>提供可复用评测资源</td>
<td nowrap><a href="https://arxiv.org/abs/2511.00940">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.08822">FreqPolicy: Efficient Flow-based Visuomotor Policy via Frequency Consistency</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>机器人部署/评测环境</td>
<td nowrap>提升推理或执行效率</td>
<td nowrap>-</td>
<td nowrap>提升推理或执行效率</td>
<td nowrap><a href="https://arxiv.org/abs/2506.08822">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN, Efficient-VLA</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://www.arxiv.org/pdf/2506.06677">RoboCerebra: A Large-scale Benchmark for Long-horizon Robotic Manipulation Evaluation</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>仿真/评测环境</td>
<td nowrap>long-horizon household manipulation; 1,000 trajectories; 100 task variants; planning/reflection/memory evaluation</td>
<td nowrap>Project+Code+Data/Bench</td>
<td nowrap>提供评测任务和数据基准</td>
<td nowrap><a href="https://www.arxiv.org/pdf/2506.06677">paper</a> / <a href="https://arxiv.org/pdf/2506.06677">📄 Paper</a></td>
<td nowrap><a href="https://robocerebra.github.io/">🌍 Web</a></td>
<td nowrap><a href="https://github.com/qiuboxiang/RoboCerebra">project</a> / <a href="https://github.com/buaa-colalab/RoboCerebra">💻 Code</a></td>
<td nowrap><a href="https://huggingface.co/datasets/qiukingballball/RoboCerebra">RoboCerebra</a> / <a href="https://huggingface.co/datasets/qiukingballball/RoboCerebraBench">RoboCerebraBench</a></td>
<td nowrap>EAI-VLA-VLN, WAM</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://suturebot.github.io/static/SutureBot_NeurIPS_2025.pdf">SutureBot: A Precision Framework &amp; Benchmark For Autonomous End-to-End Suturing</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>da Vinci Research Kit (dVRK) Si; wrist cameras and endoscope</td>
<td nowrap>提供评测任务和数据基准</td>
<td nowrap>Project+Code+Data/Bench</td>
<td nowrap>提供评测任务和数据基准</td>
<td nowrap><a href="https://suturebot.github.io/static/SutureBot_NeurIPS_2025.pdf">paper</a></td>
<td nowrap><a href="https://suturebot.github.io/">project</a></td>
<td nowrap><a href="https://github.com/SutureBot/SutureBot/tree/ACT">code</a></td>
<td nowrap><a href="https://huggingface.co/datasets/jchen396/SutureBot">SutureBot dataset</a></td>
<td nowrap>-</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap>Embodied Crowd Counting</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>机器人部署/评测环境</td>
<td nowrap>提供可复用评测资源</td>
<td nowrap>-</td>
<td nowrap>提供可复用评测资源</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2412.06782">CARP: Coarse-to-Fine Autoregressive Prediction for Visuomotor Policy Learning</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>机器人部署/评测环境</td>
<td nowrap>提供可复用评测资源</td>
<td nowrap>Project</td>
<td nowrap>提供可复用评测资源</td>
<td nowrap><a href="https://arxiv.org/abs/2412.06782">paper</a></td>
<td nowrap><a href="https://carp-robot.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.16408">RoboFactory: Exploring Embodied Agent Collaboration with Compositional Constraints</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>仿真/评测环境</td>
<td nowrap>提供可复用评测资源</td>
<td nowrap>Project+Code+Data/Bench</td>
<td nowrap>提供可复用评测资源</td>
<td nowrap><a href="https://arxiv.org/abs/2503.16408">paper</a></td>
<td nowrap><a href="https://iranqin.github.io/robofactory/">project</a></td>
<td nowrap><a href="https://github.com/MARS-EAI/RoboFactory">code</a></td>
<td nowrap><a href="https://huggingface.co/datasets/FACEONG/RoboFactory_Dataset">RoboFactory_Dataset</a></td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2504.10414">HUMOTO: A 4D Dataset of Mocap Human Object Interactions</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>仿真/评测环境</td>
<td nowrap>提供训练/评测数据资源</td>
<td nowrap>Project</td>
<td nowrap>提供训练/评测数据资源</td>
<td nowrap><a href="https://arxiv.org/abs/2504.10414">paper</a></td>
<td nowrap><a href="https://jiaxin-lu.github.io/humoto/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Humanoid-RL</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2412.07215">RoboMM: All-in-One Multimodal Large Model for Robotic Manipulation</a></td>
<td nowrap>RoboMM multimodal manipulation model + RoboData dataset/evaluation system</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>机器人部署/评测环境</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap>Code+Data/Bench</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2412.07215">paper</a> / <a href="https://arxiv.org/pdf/2412.07215">📄 Paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/RoboUniview/RoboMM">💻 Code</a></td>
<td nowrap><a href="https://huggingface.co/datasets/liufanfanlff/RoboData">📦 Dataset</a></td>
<td nowrap>EAI-VLA-VLN, WAM</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.11117">Beyond the Destination: A Novel Benchmark for Exploration-Aware Embodied Question Answering</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>仿真/评测环境</td>
<td nowrap>EXPRESS-Bench; 777 exploration trajectories and 2,044 question-trajectory pairs</td>
<td nowrap>Code</td>
<td nowrap>提供评测任务和数据基准</td>
<td nowrap><a href="https://arxiv.org/abs/2503.11117">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/HCPLab-SYSU/EXPRESS-Bench">project</a></td>
<td nowrap>-</td>
<td nowrap>HCP-Survey</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/1787">RobAVA: A Large-scale Dataset and Baseline Towards Video based Robotic Arm Action Understanding</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>仿真/评测环境</td>
<td nowrap>提供训练/评测数据资源</td>
<td nowrap>-</td>
<td nowrap>提供训练/评测数据资源</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/1787">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/2215">RoboAnnotatorX: A Comprehensive and Universal Annotation Framework for Accurate Understanding of Long-horizon Robot Demonstration</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>机器人部署/评测环境</td>
<td nowrap>提供可复用评测资源</td>
<td nowrap>-</td>
<td nowrap>提供可复用评测资源</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/2215">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>ICML 2025</td>
<td nowrap>EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>仿真/评测环境</td>
<td nowrap>1,128 testing tasks across 4 environments; 6 agent capability subsets</td>
<td nowrap>Project+Code</td>
<td nowrap>提供评测任务和数据基准</td>
<td nowrap><a href="https://arxiv.org/abs/2502.09560">paper</a></td>
<td nowrap><a href="https://embodiedbench.github.io/">project</a></td>
<td nowrap><a href="https://github.com/EmbodiedBench/EmbodiedBench">code</a></td>
<td nowrap>-</td>
<td nowrap>HCP-Survey, EAI-Safety</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2411.18025">Pixel-aligned RGB-NIR Stereo Imaging and Dataset for Robot Vision</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>仿真/评测环境</td>
<td nowrap>提供训练/评测数据资源</td>
<td nowrap>-</td>
<td nowrap>提供训练/评测数据资源</td>
<td nowrap><a href="https://arxiv.org/abs/2411.18025">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
</tbody>
</table>

#### sim2real

共 17 篇。

<table>
<thead>
<tr>
<th nowrap>会议/年份</th>
<th nowrap>论文/方法</th>
<th nowrap>对象类型</th>
<th nowrap>效率指标</th>
<th nowrap>平台/硬件</th>
<th nowrap>覆盖任务</th>
<th nowrap>开放资源状态</th>
<th nowrap>问题/目标</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>来源</th>
<th nowrap>调研判断</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=W3Q2xvrZtx">PD$^{2}$GS: Part-Level Decoupling and Continuous Deformation of Articulated Objects via Gaussian Splatting</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>sim2real</td>
<td nowrap>仿真/评测环境</td>
<td nowrap>缩小仿真到真实差距</td>
<td nowrap>-</td>
<td nowrap>缩小仿真到真实差距</td>
<td nowrap><a href="https://openreview.net/forum?id=W3Q2xvrZtx">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=sWyX1BpeN4">Manipulation as in Simulation: Enabling Accurate Geometry Perception in Robots</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>sim2real</td>
<td nowrap>仿真/评测环境</td>
<td nowrap>缩小仿真到真实差距</td>
<td nowrap>-</td>
<td nowrap>缩小仿真到真实差距</td>
<td nowrap><a href="https://openreview.net/forum?id=sWyX1BpeN4">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=nAO9LcV7nE">Emergent Dexterity Via Diverse Resets and Large-Scale Reinforcement Learning</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>sim2real</td>
<td nowrap>仿真/评测环境</td>
<td nowrap>缩小仿真到真实差距</td>
<td nowrap>-</td>
<td nowrap>缩小仿真到真实差距</td>
<td nowrap><a href="https://openreview.net/forum?id=nAO9LcV7nE">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=H4SyKHjd4c">Sim2Real VLA: Zero-Shot Generalization of Synthesized Skills to Realistic Manipulation</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>sim2real</td>
<td nowrap>仿真/评测环境</td>
<td nowrap>缩小仿真到真实差距</td>
<td nowrap>-</td>
<td nowrap>缩小仿真到真实差距</td>
<td nowrap><a href="https://openreview.net/forum?id=H4SyKHjd4c">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-Guide, Octoday, HCP-Survey, EAI-VLA-VLN, Humanoid-RL</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=TmYcqOnxhN">Exo-Plore: Exploring Exoskeleton Control Space through Human-aligned Simulation</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>sim2real</td>
<td nowrap>仿真/评测环境</td>
<td nowrap>缩小仿真到真实差距</td>
<td nowrap>-</td>
<td nowrap>缩小仿真到真实差距</td>
<td nowrap><a href="https://openreview.net/forum?id=TmYcqOnxhN">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=yn9dzttHvT">Latent Adaptation of Foundation Policies for Sim-to-Real Transfer</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>sim2real</td>
<td nowrap>仿真/评测环境</td>
<td nowrap>缩小仿真到真实差距</td>
<td nowrap>-</td>
<td nowrap>缩小仿真到真实差距</td>
<td nowrap><a href="https://openreview.net/forum?id=yn9dzttHvT">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=OutljIofvS">RobotArena $\infty$: Unlimited Robot Benchmarking via Real-to-Sim Translation</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>sim2real</td>
<td nowrap>仿真/评测环境</td>
<td nowrap>缩小仿真到真实差距</td>
<td nowrap>-</td>
<td nowrap>缩小仿真到真实差距</td>
<td nowrap><a href="https://openreview.net/forum?id=OutljIofvS">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=xlr3NqxUqY">Contact-guided Real2Sim from Monocular Video with Planar Scene Primitives</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>sim2real</td>
<td nowrap>仿真/评测环境</td>
<td nowrap>缩小仿真到真实差距</td>
<td nowrap>-</td>
<td nowrap>缩小仿真到真实差距</td>
<td nowrap><a href="https://openreview.net/forum?id=xlr3NqxUqY">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Humanoid-RL</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66662">FlatLab: A Unified Methodology Framework and Simulation-Based Benchmark for Robotic Manipulation of Flat Objects</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>sim2real</td>
<td nowrap>仿真/评测环境</td>
<td nowrap>提供评测任务和数据基准</td>
<td nowrap>-</td>
<td nowrap>提供评测任务和数据基准</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66662">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2602.20871">GeCo-SRT: Geometry-aware Continual Adaptation for Robotic Cross-Task Sim-to-Real Transfer</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>sim2real</td>
<td nowrap>仿真/评测环境</td>
<td nowrap>缩小仿真到真实差距</td>
<td nowrap>Project</td>
<td nowrap>缩小仿真到真实差距</td>
<td nowrap><a href="https://arxiv.org/abs/2602.20871">paper</a></td>
<td nowrap><a href="https://namelesscrew.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2509.19626">EgoBridge: Domain Adaptation for Generalizable Imitation from Egocentric Human Data</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>sim2real</td>
<td nowrap>机器人部署/评测环境</td>
<td nowrap>缩小仿真到真实差距</td>
<td nowrap>Project</td>
<td nowrap>缩小仿真到真实差距</td>
<td nowrap><a href="https://arxiv.org/abs/2509.19626">paper</a></td>
<td nowrap><a href="https://ego-bridge.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap>DEAL: Diffusion Evolution Adversarial Learning for Sim-to-Real Transfer</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>仿真/评测环境</td>
<td nowrap>缩小仿真到真实差距</td>
<td nowrap>-</td>
<td nowrap>缩小仿真到真实差距</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2509.18631">Generalizable Domain Adaptation for Sim-and-Real Policy Co-Training</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>sim2real</td>
<td nowrap>机器人部署/评测环境</td>
<td nowrap>缩小仿真到真实差距</td>
<td nowrap>Project</td>
<td nowrap>缩小仿真到真实差距</td>
<td nowrap><a href="https://arxiv.org/abs/2509.18631">paper</a></td>
<td nowrap><a href="https://ot-sim2real.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2505.22634">LabUtopia: High-Fidelity Simulation and Hierarchical Benchmark for Scientific Embodied Agents</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>sim2real</td>
<td nowrap>仿真/评测环境</td>
<td nowrap>提供评测任务和数据基准</td>
<td nowrap>Project</td>
<td nowrap>提供评测任务和数据基准</td>
<td nowrap><a href="https://arxiv.org/abs/2505.22634">paper</a></td>
<td nowrap><a href="https://rui-li023.github.io/labutopia-site/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2507.01152">SonoGym: High Performance Simulation for Challenging Surgical Tasks with Robotic Ultrasound</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>sim2real</td>
<td nowrap>仿真/评测环境</td>
<td nowrap>缩小仿真到真实差距</td>
<td nowrap>Code</td>
<td nowrap>缩小仿真到真实差距</td>
<td nowrap><a href="https://arxiv.org/abs/2507.01152">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/SonoGym/SonoGym">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.22756">RoboPearls: Editable Video Simulation for Robot Manipulation</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>仿真/评测环境</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap>Project</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2506.22756">paper</a></td>
<td nowrap><a href="https://tangtaogo.github.io/RoboPearls/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2409.02920">RoboTwin: Dual-Arm Robot Benchmark with Generative Digital Twins (early version)</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>双臂机器人</td>
<td nowrap>提供评测任务和数据基准</td>
<td nowrap>Project+Code+Data/Bench</td>
<td nowrap>提供评测任务和数据基准</td>
<td nowrap><a href="https://arxiv.org/abs/2409.02920">paper</a></td>
<td nowrap><a href="https://robotwin-benchmark.github.io/early-version/">project</a></td>
<td nowrap><a href="https://github.com/RoboTwin-Platform/RoboTwin">code</a></td>
<td nowrap><a href="https://huggingface.co/datasets/TianxingChen/RoboTwin">RoboTwin dataset</a></td>
<td nowrap>EAI-Guide, EAI-VLA-VLN, Efficient-VLA, WAM, RL-VLA</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
</tbody>
</table>

#### safety evaluation

共 9 篇。

<table>
<thead>
<tr>
<th nowrap>会议/年份</th>
<th nowrap>论文/方法</th>
<th nowrap>对象类型</th>
<th nowrap>效率指标</th>
<th nowrap>平台/硬件</th>
<th nowrap>覆盖任务</th>
<th nowrap>开放资源状态</th>
<th nowrap>问题/目标</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>来源</th>
<th nowrap>调研判断</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=8s5jBVybhQ">Remotely Detectable Robot Policy Watermarking</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>safety</td>
<td nowrap>机器人部署/评测环境</td>
<td nowrap>评估鲁棒性和安全性</td>
<td nowrap>-</td>
<td nowrap>评估鲁棒性和安全性</td>
<td nowrap><a href="https://openreview.net/forum?id=8s5jBVybhQ">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=Gsrw1vxq1G">Uncovering Robot Vulnerabilities through Semantic Potential Fields</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>safety</td>
<td nowrap>机器人部署/评测环境</td>
<td nowrap>评估鲁棒性和安全性</td>
<td nowrap>-</td>
<td nowrap>评估鲁棒性和安全性</td>
<td nowrap><a href="https://openreview.net/forum?id=Gsrw1vxq1G">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/60472">Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>机器人部署/评测环境</td>
<td nowrap>评估鲁棒性和安全性</td>
<td nowrap>-</td>
<td nowrap>评估鲁棒性和安全性</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/60472">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62679">PACT: Self-Evolving Physical Safety Alignment for Diffusion Policies in Embodied Manipulation</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>safety</td>
<td nowrap>机器人部署/评测环境</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62679">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Awesome-VLA</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61584">SafeLab: An Interactive High-Fidelity Benchmark for Embodied Safety in Scientific Robotics</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>safety</td>
<td nowrap>仿真/评测环境</td>
<td nowrap>提供评测任务和数据基准</td>
<td nowrap>-</td>
<td nowrap>提供评测任务和数据基准</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61584">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64080">Dismantling the Illusion of Vision-Language-Action Models Competence via Explicit Distributional Shifts</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>机器人部署/评测环境</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap>-</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64080">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2510.13626">LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>机器人部署/评测环境</td>
<td nowrap>robustness benchmark with 10,030 tasks across 7 perturbation dimensions</td>
<td nowrap>Project+Code+Data/Bench</td>
<td nowrap>改进视觉语言到动作策略</td>
<td nowrap><a href="https://arxiv.org/abs/2510.13626">paper</a> / <a href="https://arxiv.org/pdf/2510.13626">📄 Paper</a></td>
<td nowrap><a href="https://sylvestf.github.io/LIBERO-plus/">project</a></td>
<td nowrap><a href="https://github.com/sylvestf/LIBERO-plus">💻 Code</a></td>
<td nowrap><a href="https://huggingface.co/datasets/Sylvest/LIBERO-plus">📦 Dataset</a></td>
<td nowrap>EAI-Safety, WAM</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.05294">A Smooth Sea Never Made a Skilled SAILOR: Robust Imitation via Learning to Search</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>safety</td>
<td nowrap>机器人部署/评测环境</td>
<td nowrap>评估鲁棒性和安全性</td>
<td nowrap>Project</td>
<td nowrap>评估鲁棒性和安全性</td>
<td nowrap><a href="https://arxiv.org/abs/2506.05294">paper</a></td>
<td nowrap><a href="https://gokul.dev/sailor/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.23725">PAC Bench: Do Foundation Models Understand Prerequisites for Executing Manipulation Policies?</a></td>
<td nowrap>benchmark/dataset</td>
<td nowrap>safety</td>
<td nowrap>机器人部署/评测环境</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap>-</td>
<td nowrap>提升机器人操作泛化和稳定性</td>
<td nowrap><a href="https://arxiv.org/abs/2506.23725">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>RL-VLA</td>
<td nowrap>用于评估部署效率、数据覆盖和评测可信度。</td>
</tr>
</tbody>
</table>


## 重点阅读顺序

1. 先看 VLN 和 Agentic Planning：确认“大范围规划”和“细粒度规划”分别解决什么。
2. 再看 VLA 和 WAM：区分“直接动作生成”和“先想象/预测再执行”。
3. 最后看本体扩展、轻量化、评测：这些决定路线能不能真实部署。

## 源仓库补充条目

以下条目来自本次保存的 README 快照，不并入 CCF-A 主表；它们用于跟踪 WAM 数据源和 RL-VLA 方法线索。

<table>
<thead>
<tr>
<th nowrap>条目</th>
<th nowrap>来源</th>
<th nowrap>方向</th>
<th nowrap>时间</th>
<th nowrap>资源</th>
<th nowrap>为什么跟踪</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>UnifoLM-WBT Dataset</td>
<td nowrap>WAM</td>
<td nowrap>WAM training data / robot-centric</td>
<td nowrap>2026-03</td>
<td nowrap><a href="https://huggingface.co/collections/unitreerobotics/unifolm-wbt-dataset">dataset</a></td>
<td nowrap>机器人中心数据源，适合后续看 WAM 训练数据覆盖。</td>
</tr>
<tr>
<td nowrap>DexUMI</td>
<td nowrap>WAM</td>
<td nowrap>UMI / dexterous manipulation data</td>
<td nowrap>2025-05</td>
<td nowrap><a href="https://arxiv.org/pdf/2505.21864">paper</a> / <a href="https://dex-umi.github.io/">web</a> / <a href="https://umi-data.github.io/">dataset</a> / <a href="https://github.com/real-stanford/DexUMI">code</a></td>
<td nowrap>手部交互数据源，连接 WAM 与灵巧操作。</td>
</tr>
<tr>
<td nowrap>InternData-A1 / InternVLA-A1</td>
<td nowrap>WAM</td>
<td nowrap>simulation + VLA data</td>
<td nowrap>2026-01</td>
<td nowrap><a href="https://arxiv.org/pdf/2601.02456">paper</a> / <a href="https://internrobotics.github.io/interndata-a1.github.io/">web</a> / <a href="https://huggingface.co/datasets/InternRobotics/InternData-A1">dataset</a> / <a href="https://github.com/InternRobotics/InternVLA-A1">code</a></td>
<td nowrap>同时有数据、模型和代码，适合作为 VLA/WAM 联合入口。</td>
</tr>
<tr>
<td nowrap>EgoDex</td>
<td nowrap>WAM</td>
<td nowrap>egocentric dexterous data</td>
<td nowrap>2025-05</td>
<td nowrap><a href="https://arxiv.org/pdf/2505.11709">paper</a> / <a href="https://github.com/apple/ml-egodex">dataset+code</a></td>
<td nowrap>第一视角灵巧操作数据，适合补足人类视频到机器人策略的链路。</td>
</tr>
<tr>
<td nowrap>ARM</td>
<td nowrap>RL-VLA</td>
<td nowrap>Offline RL-VLA / real robot</td>
<td nowrap>2026.4</td>
<td nowrap><a href="https://arxiv.org/pdf/2604.03037">paper</a> / <a href="https://aiming1998.github.io/ARM/">project</a></td>
<td nowrap>基于 GR00T N1.5 的真实机器人 RL-VLA 方法。</td>
</tr>
<tr>
<td nowrap>LaST-R1</td>
<td nowrap>RL-VLA</td>
<td nowrap>Online RL-VLA / simulation</td>
<td nowrap>2026.04</td>
<td nowrap><a href="https://arxiv.org/abs/2604.28192">paper</a></td>
<td nowrap>RL-VLA 在线训练线索，适合后续补到 VLA 微调方向。</td>
</tr>
<tr>
<td nowrap>POCO</td>
<td nowrap>RL-VLA</td>
<td nowrap>Offline + Online RL-VLA</td>
<td nowrap>2026.04</td>
<td nowrap><a href="https://arxiv.org/abs/2604.01860">paper</a> / <a href="https://cccedric.github.io/poco/">project</a></td>
<td nowrap>覆盖 sim 和 real，且连接 π0/Octo 与 RL 优化。</td>
</tr>
<tr>
<td nowrap>FASTER</td>
<td nowrap>RL-VLA</td>
<td nowrap>Test-time RL-VLA</td>
<td nowrap>2026.04</td>
<td nowrap><a href="https://arxiv.org/abs/2604.19730">paper</a></td>
<td nowrap>测试时 action optimization 线索，适合跟踪 VLA 执行期优化。</td>
</tr>
</tbody>
</table>

## 数据来源说明

GitHub 源仓库的元数据和 README 快照见 [`sources/github/repos.json`](sources/github/repos.json)；表格中的 `来源` 使用该文件里的 `id`。

<table>
<thead>
<tr>
<th nowrap>来源</th>
<th nowrap>用途</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap><a href="https://ccf.atom.im/">CCF 2026 推荐目录</a></td>
<td nowrap>核对 2026 版 CCF-A 人工智能会议口径。</td>
</tr>
<tr>
<td nowrap><a href="https://github.com/Songwxuan/Embodied-AI-Paper-TopConf">Songwxuan/Embodied-AI-Paper-TopConf</a></td>
<td nowrap>CCF-A 论文主来源，按会议和方向分类；论文、代码和项目页链接优先采用该仓库中已给出的资源。</td>
</tr>
<tr>
<td nowrap><a href="https://openreview.net/group?id=ICLR.cc/2026/Conference">ICLR 2026 OpenReview</a></td>
<td nowrap>核对 ICLR 2026 公开论文页和 PDF 资源。</td>
</tr>
<tr>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/issue/view/703">AAAI-26 Intelligent Robotics proceedings</a></td>
<td nowrap>核对并补入 AAAI 2026 机器人方向论文。</td>
</tr>
<tr>
<td nowrap><a href="https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln">jonyzhang2023/awesome-embodied-vla-va-vln</a></td>
<td nowrap>参考 VLA、WAM、VLN、VA 和 survey 的组织方式。</td>
</tr>
<tr>
<td nowrap><a href="https://github.com/OpenMOSS/Awesome-WAM">OpenMOSS/Awesome-WAM</a></td>
<td nowrap>参考 WAM 的 cascaded/joint、autoregressive/diffusion、evaluation/training data 分类。</td>
</tr>
<tr>
<td nowrap><a href="https://github.com/UCSB-AI/awesome-vision-language-navigation">UCSB-AI/awesome-vision-language-navigation</a></td>
<td nowrap>参考 VLN 的 dataset、evaluation、representation、action strategy、planning、asking for help 分类。</td>
</tr>
<tr>
<td nowrap><a href="https://github.com/DelinQu/awesome-vision-language-action-model">DelinQu/awesome-vision-language-action-model</a></td>
<td nowrap>参考 VLA 里程碑时间线。</td>
</tr>
<tr>
<td nowrap><a href="https://github.com/yueen-ma/Awesome-VLA">yueen-ma/Awesome-VLA</a></td>
<td nowrap>参考 VLA components、world models、reasoning、policy steering、low-level/high-level planners 分类。</td>
</tr>
</tbody>
</table>
