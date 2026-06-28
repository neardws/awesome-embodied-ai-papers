<div align="center">

# 🤖 Awesome Embodied AI Frontier Survey

**A curated top-conference-oriented map of embodied AI research across VLN, VLA, WAM, planning, embodiment, and deployment.**

English | [Chinese](README.zh-CN.md)

[![Awesome](https://img.shields.io/badge/Awesome-Embodied%20AI-fc60a8?style=for-the-badge)](https://awesome.re)
[![Survey Entries](https://img.shields.io/badge/Survey%20Entries-568-0984e3?style=for-the-badge)](README.md)
[![Last Commit](https://img.shields.io/github/last-commit/neardws/embodied-ai-frontier-survey?style=for-the-badge&color=00b894)](https://github.com/neardws/embodied-ai-frontier-survey/commits)
[![Stars](https://img.shields.io/github/stars/neardws/embodied-ai-frontier-survey?style=for-the-badge&color=fdcb6e&logo=github)](https://github.com/neardws/embodied-ai-frontier-survey/stargazers)
[![Forks](https://img.shields.io/github/forks/neardws/embodied-ai-frontier-survey?style=for-the-badge&color=e17055&logo=github)](https://github.com/neardws/embodied-ai-frontier-survey/network/members)

Updated: 2026-06-28

</div>

## 📋 Table of Contents

| | Section | Description |
|:---:|:---|:---|
| 🏷️ | [Tag Legend](#tag-legend) | Tags used to group embodied AI directions |
| 🧭 | [Overall View](#overall-view) | High-level system route and field framing |
| 🗺️ | [Direction Overview](#direction-overview) | Six-track overview with paper counts |
| 📚 | [Detailed Tables](#detailed-tables) | Paper-level tables by direction and subdirection |
| 🔎 | [Reading Order](#reading-order) | Suggested priority list for deeper reading |
| 🧾 | [Data Sources](#data-sources) | Source traceability and reference metadata |

> [!NOTE]
> Entries are scoped to reviewed public sources, including CCF-A venues and robotics flagship conferences such as ICRA/IROS.

> [!TIP]
> Missing papers or resources can be suggested through Issues or Pull Requests.

## Tag Legend

| Tag | Meaning |
| --- | --- |
| `VLN` | Large-scale navigation |
| `VLA` | Vision-language-action manipulation policies |
| `WAM` | World action models |
| `Planning` | Task decomposition, memory, failure recovery, and constrained planning |
| `Embodiment` | Humanoids, bimanual systems, dexterous hands, and tactile interaction |
| `Deployment` | Efficiency, evaluation, data, sim2real, and safety |

## Overall View

The current embodied AI frontier can be grouped into six tracks: large-scale VLN, VLA manipulation policies, WAM/world models, agentic planning, embodiment expansion, and deployment-oriented efficiency/evaluation/data.

The system direction worth tracking is:

```text
task understanding and fine-grained planning agent
        -> WAM / world model for imagination, verification, and failure prediction
        -> small VLA, diffusion policy, skill library, or classical controller
        -> local robot safety loop
```

The reason is straightforward: monolithic VLA models matter, but real robots also need interpretable planning, executable constraints, low-latency control, failure recovery, and on-device autonomy.

## Direction Overview

<table>
<thead>
<tr>
<th nowrap>Tag</th>
<th nowrap>Direction</th>
<th nowrap>Subdirection</th>
<th nowrap>Entries</th>
<th nowrap>Takeaway</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap><code>VLN</code></td>
<td nowrap>VLN / Large-scale Navigation</td>
<td nowrap>continuous VLN, map memory, physically executable navigation, urban/open-world navigation, low-cost/on-device navigation</td>
<td nowrap>79</td>
<td nowrap>VLN focuses on language goals, spatial maps, memory, exploration, and navigation decisions. The core problem is turning natural-language tasks into executable large-scale movement plans. Current survey entries show a shift from discrete navigation graphs toward continuous environments, physically executable navigation, open urban settings, and lower-cost on-device navigation.</td>
</tr>
<tr>
<td nowrap><code>VLA</code></td>
<td nowrap>VLA / Manipulation Policies</td>
<td nowrap>generalist VLA, action representation, diffusion/flow policy, 3D grounding, online/RL fine-tuning, safety/robustness</td>
<td nowrap>187</td>
<td nowrap>VLA is the main track for robotic arms and mobile manipulation, but it is not just an action head attached to a large model. Survey papers concentrate on action representation, diffusion/flow policies, 3D grounding, online/RL fine-tuning, and robustness.</td>
</tr>
<tr>
<td nowrap><code>WAM</code></td>
<td nowrap>WAM / World Models</td>
<td nowrap>cascaded WAM, joint WAM, video/latent world model, world model for VLA, world model evaluation</td>
<td nowrap>50</td>
<td nowrap>WAM combines future world-state prediction with action generation and fits naturally between agent planning and low-level control. Its value is not replacing every controller, but providing an intermediate layer for imagination, verification, and recovery.</td>
</tr>
<tr>
<td nowrap><code>Planning</code></td>
<td nowrap>Agentic Planning / Reasoning and Planning</td>
<td nowrap>task decomposition, memory, failure monitor, constraint / affordance planning, self-improving planning</td>
<td nowrap>93</td>
<td nowrap>This direction emphasizes task decomposition, memory, failure monitoring, constraint/affordance planning, and self-improving planning. It is closest to the practical system route of agent planning plus smaller execution modules.</td>
</tr>
<tr>
<td nowrap><code>Embodiment</code></td>
<td nowrap>Embodiment Expansion / Dexterous Manipulation</td>
<td nowrap>humanoid, bimanual, dexterous hand, tactile/contact-rich, grasping</td>
<td nowrap>75</td>
<td nowrap>Embodiment expansion determines whether embodied AI can move beyond single-arm systems toward humanoids, bimanual robots, dexterous hands, and tactile/contact-rich tasks. These papers show how action spaces, sensing, and control objectives become more complex as the body changes.</td>
</tr>
<tr>
<td nowrap><code>Deployment</code></td>
<td nowrap>Efficiency / Evaluation / Data</td>
<td nowrap>quantization/cache/tokenization, real-time execution, benchmark/dataset, sim2real, safety evaluation</td>
<td nowrap>83</td>
<td nowrap>This direction determines whether systems can actually be deployed: on-device inference, caching/quantization/action tokenization, real-time execution, sim2real, benchmarks, and safety evaluation are all necessary conditions.</td>
</tr>
</tbody>
</table>

## Detailed Tables

### VLN / Large-scale Navigation

VLN focuses on language goals, spatial maps, memory, exploration, and navigation decisions. The core problem is turning natural-language tasks into executable large-scale movement plans. Current survey entries show a shift from discrete navigation graphs toward continuous environments, physically executable navigation, open urban settings, and lower-cost on-device navigation.

Subdirections: continuous VLN, map memory, physically executable navigation, urban/open-world navigation, and low-cost/on-device navigation.

Total: 79 papers.

<table>
<thead>
<tr>
<th nowrap>Subdirection</th>
<th nowrap>Entries</th>
<th nowrap>Focus</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>Continuous VLN</td>
<td nowrap>33</td>
<td nowrap>Focus: whether navigation moves from discrete graphs toward continuous observations and real-time decisions.</td>
</tr>
<tr>
<td nowrap>Map Memory</td>
<td nowrap>19</td>
<td nowrap>Focus: map representation, semantic memory, caching, and retrieval.</td>
</tr>
<tr>
<td nowrap>Physically Executable Navigation</td>
<td nowrap>6</td>
<td nowrap>Focus: real embodiment constraints, dynamic environments, and safety decoding.</td>
</tr>
<tr>
<td nowrap>Urban / Open-world Navigation</td>
<td nowrap>18</td>
<td nowrap>Focus: open worlds, cities, crowded environments, and long-horizon navigation.</td>
</tr>
<tr>
<td nowrap>Low-cost / On-device Navigation</td>
<td nowrap>3</td>
<td nowrap>Focus: on-device inference, low-cost memory, and data efficiency.</td>
</tr>
</tbody>
</table>

#### Continuous VLN

Total: 33 papers.

<table>
<thead>
<tr>
<th nowrap>Venue/Year</th>
<th nowrap>Paper/Method</th>
<th nowrap>Abstract</th>
<th nowrap>Task Type</th>
<th nowrap>Environment</th>
<th nowrap>Map/Memory</th>
<th nowrap>Training/Feedback</th>
<th nowrap>Sim/Real/Benchmark</th>
<th nowrap>Paper Task/Goal</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>Source</th>
<th nowrap>Survey Note</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ICRA 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2509.19480">OmniVLA: An Omni-Modal Vision-Language-Action Model for Robot Navigation</a></td>
<td nowrap>OmniVLA 统一语言、目标图像和 2D pose 等目标规格，用 VLA 方式学习机器人导航策略。</td>
<td nowrap>Vision-language-action navigation</td>
<td nowrap>continuous navigation</td>
<td nowrap>multimodal goal context</td>
<td nowrap>navigation VLA training</td>
<td nowrap>Sim + Real</td>
<td nowrap>用多模态目标表达训练可泛化导航 VLA。</td>
<td nowrap><a href="https://arxiv.org/abs/2509.19480">paper</a></td>
<td nowrap><a href="https://omnivla-nav.github.io/">project</a></td>
<td nowrap><a href="https://github.com/NHirose/OmniVLA">code</a></td>
<td nowrap>-</td>
<td nowrap>ICRA/IROS</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>ICRA 2025</td>
<td nowrap><a href="https://sites.google.com/view/opennav/home">Open-Nav: Exploring Zero-Shot Vision-and-Language Navigation in Continuous Environment with Open-Source LLMs</a></td>
<td nowrap>Open-Nav 用开源 LLM 做时空 CoT、进度估计和动作决策，面向连续环境零样本 VLN。</td>
<td nowrap>Continuous VLN</td>
<td nowrap>continuous indoor environment</td>
<td nowrap>spatio-temporal CoT</td>
<td nowrap>zero-shot LLM planning</td>
<td nowrap>VLN-CE benchmark</td>
<td nowrap>让开源 LLM 在连续环境中按语言指令导航。</td>
<td nowrap><a href="https://sites.google.com/view/opennav/home">paper</a></td>
<td nowrap><a href="https://sites.google.com/view/opennav/home">project</a></td>
<td nowrap><a href="https://github.com/YanyuanQiao/Open-Nav">code</a></td>
<td nowrap>-</td>
<td nowrap>ICRA/IROS</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=kkBOIsrCXh">Embodied Navigation Foundation Model</a></td>
<td nowrap>NavFoM trains a unified navigation foundation model on 8 million cross-embodiment navigation samples, covering VLN, goal search, tracking, and autonomous driving.</td>
<td nowrap>continuous VLN</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>multimodal history/trajectory context</td>
<td nowrap>large-scale supervised pretraining</td>
<td nowrap>cross-embodiment benchmark</td>
<td nowrap>Cross-embodiment and cross-task generalization</td>
<td nowrap><a href="https://openreview.net/forum?id=kkBOIsrCXh">paper</a></td>
<td nowrap><a href="https://pku-epic.github.io/NavFoM-Web/">project</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://pku-epic.github.io/NavFoM-Web/">data</a></td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=GK4rznYwhn">Ground Slow, Move Fast: A Dual-System Foundation Model for Generalizable Vision-Language Navigation</a></td>
<td nowrap>DualVLN combines a slow vision-language global planner with a fast diffusion-based low-level controller to improve smooth execution for continuous real-world VLN.</td>
<td nowrap>continuous VLN</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>VLM waypoint planner + diffusion policy</td>
<td nowrap>sim+real robot</td>
<td nowrap>Addresses fragmented actions, high latency, and poor dynamic obstacle avoidance in end-to-end VLN.</td>
<td nowrap><a href="https://openreview.net/forum?id=GK4rznYwhn">paper</a></td>
<td nowrap><a href="https://internrobotics.github.io/internvla-n1-dualvln.github.io/">project</a></td>
<td nowrap><a href="https://github.com/InternRobotics/InternNav">code</a></td>
<td nowrap>InternData-N1</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=eqcDckWHik">CompassNav: Steering From Path Imitation to Decision Understanding In Navigation</a></td>
<td nowrap>CompassNav shifts from trajectory imitation to action-feasibility understanding, improving VLN decisions with Compass-Data-22k and gap-aware training.</td>
<td nowrap>continuous VLN</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>RFT + action feasibility supervision</td>
<td nowrap>Compass-Data-22k</td>
<td nowrap>From path imitation to decision understanding</td>
<td nowrap><a href="https://openreview.net/forum?id=eqcDckWHik">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=pFh5ygjN3V">M$^3$E: Continual Vision-and-Language Navigation via Mixture of Macro and Micro Experts</a></td>
<td nowrap>M3E separately models macro scene experts and micro perception experts, mitigating catastrophic forgetting in continual VLN cross-environment adaptation.</td>
<td nowrap>Continual VLN</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>hierarchical MoE continual learning</td>
<td nowrap>-</td>
<td nowrap>Cross-environment continual learning and anti-forgetting</td>
<td nowrap><a href="https://openreview.net/forum?id=pFh5ygjN3V">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=zGtTQTD1zu">OmniNav: A Unified Framework for Prospective Exploration and Visual-Language Navigation</a></td>
<td nowrap>OmniNav uses a unified waypoint policy to handle instruction-goal navigation, object-goal navigation, point-goal navigation, and frontier exploration.</td>
<td nowrap>Unified Navigation/Exploration</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>continuous waypoint policy</td>
<td nowrap>real-time 5Hz deployment claimed</td>
<td nowrap>Unifies multiple navigation paradigms and supports low-latency continuous-space waypoint outputs.</td>
<td nowrap><a href="https://openreview.net/forum?id=zGtTQTD1zu">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=0c7nAZjyr5">From Seeing to Experiencing: Scaling Navigation Foundation Models with Reinforcement Learning</a></td>
<td nowrap>S2E post-trains offline video-pretrained navigation models with reinforcement learning to learn action consequences, obstacle avoidance, and urban interaction behaviors.</td>
<td nowrap>continuous VLN</td>
<td nowrap>urban/dynamic environment</td>
<td nowrap>-</td>
<td nowrap>offline pretraining + RL post-training</td>
<td nowrap>-</td>
<td nowrap>Interactive safe navigation generalization</td>
<td nowrap><a href="https://openreview.net/forum?id=0c7nAZjyr5">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=apaLoTumdO">CE-Nav: Flow-Guided Reinforcement Refinement for Cross-Embodiment Local Navigation</a></td>
<td nowrap>CE-Nav first uses a flow model to learn cross-embodiment feasible action distributions, then refines them with RL for specific robot dynamics.</td>
<td nowrap>Cross-embodiment Local Navigation</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>IL + RL, conditional normalizing flow</td>
<td nowrap>-</td>
<td nowrap>Cross-morphology local navigation generalization</td>
<td nowrap><a href="https://openreview.net/forum?id=apaLoTumdO">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=bMrH2PFMsi">CoNavBench: Collaborative Long-Horizon Vision-Language Navigation Benchmark</a></td>
<td nowrap>CoNavBench provides 4,048 single-agent/collaborative long-horizon VLN episodes for evaluating handoffs, congestion, and collaborative navigation.</td>
<td nowrap>Collaborative Long-horizon VLN Benchmark</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>VLN policy</td>
<td nowrap>Benchmark</td>
<td nowrap>Collaborative VLN evaluation</td>
<td nowrap><a href="https://openreview.net/forum?id=bMrH2PFMsi">paper</a></td>
<td nowrap><a href="https://navcraft.github.io">project</a></td>
<td nowrap>-</td>
<td nowrap>CoNavBench/NavCraft</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38886">NaVLA$^2$: A Vision-Language-Audio-Action Model for Multimodal Instruction Navigation</a></td>
<td nowrap>NaVLA2 proposes the MINav task, using language, image, and audio cues to disambiguate navigation instructions and build 43.9K episodes.</td>
<td nowrap>Multimodal Instruction Navigation</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>vision-language-audio-action policy</td>
<td nowrap>MINav benchmark</td>
<td nowrap>Addresses target grounding ambiguity caused by language-only instructions being insufficient in scenes with multiple similar objects.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38886">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38888">VPN: Visual Prompt Navigation</a></td>
<td nowrap>VPN replaces natural-language instructions with 2D top-down visual prompts and extends R2R/R2R-CE to form the VP dataset.</td>
<td nowrap>visual prompt navigation</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>top-view map prompt</td>
<td nowrap>VLN policy</td>
<td nowrap>R2R-VP/R2R-CE-VP</td>
<td nowrap>Studies navigation guided by user-drawn/marked visual path prompts.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38888">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38891">SeqWalker: Sequential-Horizon Vision-and-Language Navigation with Hierarchical Planning</a></td>
<td nowrap>SeqWalker targets long-horizon multi-task instructions, using high-level sub-instruction selection and low-level exploration verification to reduce information overload.</td>
<td nowrap>Long-horizon/Sequential VLN</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>hierarchical planning</td>
<td nowrap>-</td>
<td nowrap>Long-instruction decomposition and execution</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38891">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38895">UNeMo: Collaborative Visual-Language Reasoning and Navigation via a Multimodal World Model</a></td>
<td nowrap>UNeMo jointly optimizes visual state reasoning and navigation decisions with a multimodal world model, filling the gap in VLN methods that reason only with language.</td>
<td nowrap>World-model VLN</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>multimodal world model collaborative optimization</td>
<td nowrap>-</td>
<td nowrap>Addresses the separation between LLM reasoning modules and navigation policies, and the lack of visual reasoning.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38895">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38914">DNOI-4DRO: Deep 4D Radar Odometry with Differentiable Neural-Optimization Iterations</a></td>
<td nowrap>DNOI-4DRO combines a 4D radar motion-flow network with differentiable Gauss-Newton optimization to improve radar odometry accuracy.</td>
<td nowrap>4D radar odometry, not VLN</td>
<td nowrap>Mobile robot/autonomous-driving radar localization</td>
<td nowrap>-</td>
<td nowrap>differentiable neural optimization</td>
<td nowrap>VoD/Snail-Radar</td>
<td nowrap>Addresses self-localization/odometry estimation in sparse 4D radar point clouds.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38914">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38954">Run, Ruminate, and Regulate: A Dual-process Thinking System for Vision-and-Language Navigation</a></td>
<td nowrap>R3 combines fast execution, slow LLM reflection, and a regulation module to improve zero-shot VLN reasoning and efficiency.</td>
<td nowrap>continuous VLN</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>dual-process LLM reasoning</td>
<td nowrap>-</td>
<td nowrap>Zero-shot VLN reasoning efficiency and performance</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38954">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61535">AdaNav: Adaptive Reasoning with Uncertainty for Vision-Language Navigation</a></td>
<td nowrap>AdaNav triggers uncertainty-aware reasoning with action entropy, avoiding extra computation and performance loss from fixed-interval reasoning.</td>
<td nowrap>continuous VLN</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>uncertainty-adaptive reasoning + RL refinement</td>
<td nowrap>-</td>
<td nowrap>Adaptive reasoning trigger</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61535">paper</a></td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61535">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64780">Instruction Decomposition and Action Alignment for Vision-Language Navigation</a></td>
<td nowrap>IDEAL-VLN decomposes long instructions into causal execution chains and performs action alignment to reduce irrelevant text interference and visual token latency.</td>
<td nowrap>continuous VLN</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>instruction decomposition + action alignment</td>
<td nowrap>-</td>
<td nowrap>Long-horizon instruction decomposition and execution</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64780">paper</a></td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64780">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/65809">TIC-VLA: A Think-in-Control Vision-Language-Action Model for Robot Navigation in Dynamic Environments</a></td>
<td nowrap>TIC-VLA explicitly models semantic reasoning latency and feeds delayed vision-language states into real-time action control.</td>
<td nowrap>VLA robot navigation</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>latency-aware VLA control</td>
<td nowrap>-</td>
<td nowrap>Enables language instruction following and real-time reactive control in dynamic human environments.</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/65809">paper</a></td>
<td nowrap><a href="https://ucla-mobility.github.io/TIC-VLA/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61357">Hydra-Nav: Object Navigation via Adaptive Dual-Process Reasoning</a></td>
<td nowrap>Hydra-Nav adaptively switches between slow history-based reasoning and fast reactions in object navigation, balancing success rate and computational efficiency.</td>
<td nowrap>ObjectNav</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>adaptive dual-process VLM reasoning</td>
<td nowrap>-</td>
<td nowrap>Addresses weak spatiotemporal reasoning and high reasoning overhead in unseen object navigation.</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61357">paper</a></td>
<td nowrap><a href="https://zixuan-wang99.github.io/Hydra-Nav/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/60775">SafeDec: Constrained Decoding for Safe Autoregressive Generalist Robot Navigation Policies</a></td>
<td nowrap>SafeDec performs constraint decoding for autoregressive robot navigation policies, enforcing safety constraints while generating action sequences.</td>
<td nowrap>Safety-constrained robot navigation</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>constrained decoding</td>
<td nowrap>-</td>
<td nowrap>Adds explicit safety correctness to physically executable general navigation policies.</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/60775">paper</a></td>
<td nowrap><a href="https://constrained-robot-fms.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2511.20620">Wanderland: Geometrically Grounded Simulation for Open-World Embodied AI</a></td>
<td nowrap>Wanderland is a real-to-sim framework that uses multi-sensor capture and geometrically reliable reconstruction to build open-world navigation simulation benchmarks.</td>
<td nowrap>Simulation/evaluation platform</td>
<td nowrap>Open-city simulation</td>
<td nowrap>-</td>
<td nowrap>planning / RL</td>
<td nowrap>Sim/Benchmark</td>
<td nowrap>Provides a geometrically grounded open-city closed-loop evaluation environment for embodied AI.</td>
<td nowrap><a href="https://arxiv.org/abs/2511.20620">paper</a></td>
<td nowrap><a href="https://ai4ce.github.io/wanderland/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2512.04069">SpaceTools: Tool-Augmented Spatial Reasoning via Double Interactive RL</a></td>
<td nowrap>SpaceTools uses dual-interaction RL to learn tool calls for depth, segmentation, pose, and other tools to enhance VLM metric spatial reasoning.</td>
<td nowrap>Tool-augmented spatial reasoning</td>
<td nowrap>mobile robot/navigation environment</td>
<td nowrap>-</td>
<td nowrap>double interactive RL</td>
<td nowrap>-</td>
<td nowrap>Addresses VLMs' lack of precise metric ability in embodied spatial reasoning.</td>
<td nowrap><a href="https://arxiv.org/abs/2512.04069">paper</a></td>
<td nowrap><a href="https://spacetools.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2512.17907">Dexterous World Models</a></td>
<td nowrap>DWM is a scene-action-conditioned video diffusion world model that uses hand actions to drive static 3D scenes into dynamic interaction videos.</td>
<td nowrap>Dexterous-interaction world model, not VLN</td>
<td nowrap>egocentric hand-scene interaction</td>
<td nowrap>-</td>
<td nowrap>world model / planning / RL</td>
<td nowrap>-</td>
<td nowrap>Predicts dynamic changes after dexterous human-hand interaction with 3D scenes.</td>
<td nowrap><a href="https://arxiv.org/abs/2512.17907">paper</a></td>
<td nowrap><a href="https://snuvclab.github.io/dwm/">project</a></td>
<td nowrap><a href="https://github.com/snuvclab/dwm">code</a></td>
<td nowrap>-</td>
<td nowrap>HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Humanoid-RL, WAM</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2508.09423">Distilling LLM Prior to Flow Model for Generalizable Agent’s Imagination in Object Goal Navigation</a></td>
<td nowrap>GOAL distills LLM spatial priors into a flow model, using generative semantic-map imagination to support ObjectNav.</td>
<td nowrap>ObjectNav/semantic map imagination</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>flow matching + LLM prior</td>
<td nowrap>-</td>
<td nowrap>Completes unobserved areas in unseen indoor environments to improve object-goal navigation.</td>
<td nowrap><a href="https://arxiv.org/abs/2508.09423">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/Badi-Li/GOAL">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2511.17225">TP-MDDN: Task-Preferenced Multi-Demand-Driven Navigation with Autonomous Decision-Making</a></td>
<td nowrap>TP-MDDN proposes a multi-demand, preference-aware long-horizon navigation benchmark and uses AWMSystem to decompose demands, select goals, monitor state, and correct errors.</td>
<td nowrap>multi-demand-driven navigation benchmark</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>MASMap 3D point cloud + 2D semantic map</td>
<td nowrap>LLM/MLLM autonomous decision system</td>
<td nowrap>-</td>
<td nowrap>Addresses long-horizon demand-driven navigation under multiple sub-demands and explicit preference constraints.</td>
<td nowrap><a href="https://arxiv.org/abs/2511.17225">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.06630">Active Test-time Vision-Language Navigation</a></td>
<td nowrap>ATENA actively learns at test time and reduces uncertainty with entropy minimization, reducing accumulated errors when VLN is deployed in new environments.</td>
<td nowrap>continuous VLN</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>test-time active learning/adaptation</td>
<td nowrap>-</td>
<td nowrap>Performs VLN test-time adaptation without external feedback.</td>
<td nowrap><a href="https://arxiv.org/abs/2506.06630">paper</a></td>
<td nowrap><a href="https://kuai-lab.github.io/neurips2025atena/">project</a></td>
<td nowrap><a href="https://github.com/kuai-lab/NeurIPS25_att_vln">code</a></td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2510.00441">Seeing through Uncertainty: Robust Task-Oriented Optimization in Visual Navigation</a></td>
<td nowrap>NeuRO couples perception networks with task-level robust optimization to handle noise and OOD generalization in few-shot visual navigation.</td>
<td nowrap>Open-world Environment</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>learning-to-optimize robust optimization</td>
<td nowrap>-</td>
<td nowrap>Addresses overfitting in long-horizon multi-goal visual navigation policies under data scarcity.</td>
<td nowrap><a href="https://arxiv.org/abs/2510.00441">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/PyyWill/NeuRO">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.18525">RoboTron-Nav: A Unified Framework for Embodied Navigation Integrating Perception, Planning, and Prediction</a></td>
<td nowrap>RoboTron-Nav integrates perception, planning, and prediction through multitask collaboration between navigation and embodied QA, reducing history redundancy.</td>
<td nowrap>Open-world Environment</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>multitask navigation + EQA</td>
<td nowrap>-</td>
<td nowrap>Improves perception, planning, and prediction in unseen environments for language-guided visual navigation.</td>
<td nowrap><a href="https://arxiv.org/abs/2503.18525">paper</a></td>
<td nowrap><a href="https://yvfengzhong.github.io/RoboTron-Nav">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2412.05552">SAME: Learning Generic Language-Guided Visual Navigation with State-Adaptive Mixture of Experts</a></td>
<td nowrap>SAME uses state-adaptive MoE to unify high-level category search and low-level language-guided navigation.</td>
<td nowrap>generic language-guided visual navigation</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>state-adaptive MoE</td>
<td nowrap>-</td>
<td nowrap>Learns a general policy that can be shared across multiple categories of language-guided navigation tasks.</td>
<td nowrap><a href="https://arxiv.org/abs/2412.05552">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/GengzeZhou/SAME">code</a></td>
<td nowrap>-</td>
<td nowrap>Awesome-VLA, EAI-Safety</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/1984">Embodied Navigation with Auxiliary Task of Action Description Prediction</a></td>
<td nowrap>This paper uses language descriptions of actions as an auxiliary RL task, allowing the navigation policy to explain its own actions while maintaining performance.</td>
<td nowrap>Open-world Environment</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>RL + action description auxiliary task</td>
<td nowrap>-</td>
<td nowrap>Interpretable navigation action prediction</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/1984">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2412.10439">CogNav: Cognitive Process Modeling for Object Goal Navigation with LLMs</a></td>
<td nowrap>CogNav uses an LLM to model goal memory and cognitive update processes, strengthening high-level decision-making in ObjectNav.</td>
<td nowrap>ObjectNav</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>cognitive memory</td>
<td nowrap>LLM planning</td>
<td nowrap>-</td>
<td nowrap>Enables an ObjectNav agent to have human-like cognitive map updates and goal reasoning.</td>
<td nowrap><a href="https://arxiv.org/abs/2412.10439">paper</a></td>
<td nowrap><a href="https://yhancao.github.io/CogNav/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.11081">MoMa-Kitchen: A 100K+ Benchmark for Affordance-Grounded Last-Mile Navigation in Mobile Manipulation</a></td>
<td nowrap>MoMa-Kitchen provides 100K+ kitchen samples, annotating the final navigation stop pose that benefits subsequent manipulation.</td>
<td nowrap>mobile manipulation last-mile navigation benchmark</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>affordance-grounded labels</td>
<td nowrap>affordance</td>
<td nowrap>Benchmark</td>
<td nowrap>Evaluates whether mobile manipulation can stop at a manipulable position after approaching the target.</td>
<td nowrap><a href="https://arxiv.org/abs/2503.11081">paper</a></td>
<td nowrap><a href="https://momakitchen.github.io/">project</a></td>
<td nowrap><a href="https://github.com/MoMaKitchen/MoMaKitchen">code</a></td>
<td nowrap><a href="https://huggingface.co/datasets/IPEC-COMMUNITY/MoMa-Kitchen-Data">hf</a></td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
</tbody>
</table>

#### Map Memory

Total: 19 papers.

<table>
<thead>
<tr>
<th nowrap>Venue/Year</th>
<th nowrap>Paper/Method</th>
<th nowrap>Abstract</th>
<th nowrap>Task Type</th>
<th nowrap>Environment</th>
<th nowrap>Map/Memory</th>
<th nowrap>Training/Feedback</th>
<th nowrap>Sim/Real/Benchmark</th>
<th nowrap>Paper Task/Goal</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>Source</th>
<th nowrap>Survey Note</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>IROS 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2606.25497">SAGE-Nav: Leveraging LLM Planning and Alignment Fusion for Hierarchical Scene Graph-Guided Navigation</a></td>
<td nowrap>SAGE-Nav 结合 LLM 高层规划和层级场景图，引导 object-goal navigation。</td>
<td nowrap>Object-goal navigation</td>
<td nowrap>indoor navigation</td>
<td nowrap>hierarchical scene graph</td>
<td nowrap>LLM planning + alignment fusion</td>
<td nowrap>Benchmark</td>
<td nowrap>用场景图记忆把语言规划落到目标导航。</td>
<td nowrap><a href="https://arxiv.org/abs/2606.25497">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>ICRA/IROS</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>IROS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.02247">WMNav: Integrating Vision-Language Models into World Models for Object Goal Navigation</a></td>
<td nowrap>WMNav 将 VLM 接入导航世界模型，预测未来状态并维护导航记忆以提升目标搜索。</td>
<td nowrap>Object-goal navigation</td>
<td nowrap>indoor navigation</td>
<td nowrap>world-model memory</td>
<td nowrap>VLM-guided world model</td>
<td nowrap>Benchmark</td>
<td nowrap>用世界模型想象和反馈支持 object-goal navigation。</td>
<td nowrap><a href="https://arxiv.org/abs/2503.02247">paper</a></td>
<td nowrap><a href="https://b0b8k1ng.github.io/WMNav/">project</a></td>
<td nowrap><a href="https://github.com/B0B8K1ng/WMNavigation">code</a></td>
<td nowrap>-</td>
<td nowrap>ICRA/IROS</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=HB6KvsqcAn">Towards Physically Executable 3D Gaussian for Embodied Navigation</a></td>
<td nowrap>SAGE-3D upgrades 3DGS into a navigation-environment representation with object semantics and physical executability.</td>
<td nowrap>Map/memory</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>semantic and physically aligned 3D Gaussian</td>
<td nowrap>3DGS environment construction</td>
<td nowrap>-</td>
<td nowrap>3DGS-executable navigation environment</td>
<td nowrap><a href="https://openreview.net/forum?id=HB6KvsqcAn">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=LPv59noPAy">Uncertainty-Aware Gaussian Map for Vision-Language Navigation</a></td>
<td nowrap>This paper builds a semantic Gaussian Map and explicitly encodes geometric, semantic, and appearance uncertainty to guide VLN actions.</td>
<td nowrap>Map/memory</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>uncertainty-aware semantic Gaussian map</td>
<td nowrap>uncertainty-informed policy</td>
<td nowrap>-</td>
<td nowrap>Uses perception uncertainty in VLN decisions instead of ignoring ambiguous observations.</td>
<td nowrap><a href="https://openreview.net/forum?id=LPv59noPAy">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>HCP-Survey, WAM</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=RnuB0Nlbd5">JanusVLN: Decoupling Semantics and Spatiality with Dual Implicit Memory for Vision-Language Navigation</a></td>
<td nowrap>JanusVLN uses dual implicit memories to separately model semantic and spatial information, reducing redundancy and spatial loss from explicit text/frame memories.</td>
<td nowrap>Map/memory</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>Map/memory</td>
<td nowrap>dual implicit neural memory; KV-cache incremental update</td>
<td nowrap>VLN benchmark</td>
<td nowrap>Addresses explicit memory bloat and spatial information loss in MLLM-VLN.</td>
<td nowrap><a href="https://openreview.net/forum?id=RnuB0Nlbd5">paper</a></td>
<td nowrap><a href="https://miv-xjtu.github.io/JanusVLN.github.io/">project</a></td>
<td nowrap><a href="https://github.com/MIV-XJTU/JanusVLN">code</a></td>
<td nowrap><a href="https://miv-xjtu.github.io/JanusVLN.github.io/">data</a></td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=li1vfqDzRD">Emergence of Spatial Representation in an Actor-Critic Agent with Hippocampus-Inspired Sequence Generator</a></td>
<td nowrap>This paper uses a hippocampus-inspired sequence generator as a temporal memory buffer to explain the emergence of spatial representations in actor-critic navigation agents.</td>
<td nowrap>Neuro-inspired visual navigation/RL</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>hippocampus-inspired temporal sequence memory</td>
<td nowrap>actor-critic RL</td>
<td nowrap>-</td>
<td nowrap>Studies how spatial representations emerge from sequence-memory mechanisms in continuous maze visual navigation.</td>
<td nowrap><a href="https://openreview.net/forum?id=li1vfqDzRD">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=KcC5mwfGf0">GRL-SNAM: Geometric Reinforcement Learning with Differential Hamiltonians for Navigation and Mapping in Unknown Environments</a></td>
<td nowrap>GRL-SNAM uses local perception to construct a Hamiltonian energy landscape, jointly navigating and mapping in unknown environments without building a global map.</td>
<td nowrap>simultaneous navigation and mapping</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>local energy landscape/no global map</td>
<td nowrap>geometric RL</td>
<td nowrap>-</td>
<td nowrap>Performs simultaneous navigation and mapping in unknown environments.</td>
<td nowrap><a href="https://openreview.net/forum?id=KcC5mwfGf0">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38884">RflyPano: A Panoramic Benchmark for Ultra-low Altitude UAV Localization Powered by RflySim</a></td>
<td nowrap>RflyPano is a panoramic dataset for UAV visual localization below 120 meters, generated from RflySim with four fisheye cameras.</td>
<td nowrap>UAV localization benchmark</td>
<td nowrap>Ultra-low-altitude UAV / RflySim simulation</td>
<td nowrap>Evaluation/data rather than map memory</td>
<td nowrap>localization</td>
<td nowrap>Benchmark</td>
<td nowrap>Provides a panoramic visual localization benchmark for low-altitude UAV scenarios with unreliable GNSS.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38884">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/DUNDAI1998/RflyPano">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38887">MHED-SLAM: Multi-Scale Hybrid Encoding-Based Decoupled SLAM</a></td>
<td nowrap>MHED-SLAM uses multiscale hybrid encoding and decoupled geometry/color modeling to improve NeRF-SLAM mapping and tracking quality.</td>
<td nowrap>SLAM</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>neural scene representation</td>
<td nowrap>NeRF/TSDF SLAM</td>
<td nowrap>-</td>
<td nowrap>Visual SLAM mapping and localization</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38887">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38893">LOG-Nav: Efficient Layout-Aware Object-Goal Navigation with Hierarchical Planning</a></td>
<td nowrap>LOG-Nav uses global topological layout maps and local scene memory for hierarchical planning, improving multi-room ObjectNav efficiency.</td>
<td nowrap>ObjectNav</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>topological layout map + local scene memory</td>
<td nowrap>LLM hierarchical planning/no costly training</td>
<td nowrap>-</td>
<td nowrap>Enables an LLM agent to efficiently find objects in complex indoor multi-room environments.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38893">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38899">PanoNav: Mapless Zero-Shot Object Navigation with Panoramic Scene Parsing and Dynamic Memory</a></td>
<td nowrap>PanoNav uses RGB-only panoramic scene parsing and dynamic memory to achieve map-free zero-shot ObjectNav.</td>
<td nowrap>zero-shot ObjectNav</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>dynamic memory/mapless RGB-only</td>
<td nowrap>MLLM reasoning</td>
<td nowrap>-</td>
<td nowrap>Performs zero-shot object navigation without depth or prebuilt maps.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38899">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38901">Lightweight Adaptive Topological Layout and Semantic Mapping in Vision-and-Language Navigation on Websites</a></td>
<td nowrap>ATLAS builds a lightweight adaptive topological layout and semantic graph for website VLN, improving web navigation accuracy and inference speed.</td>
<td nowrap>Map/memory</td>
<td nowrap>Web navigation, not physical robotics</td>
<td nowrap>adaptive topological layout + semantic map</td>
<td nowrap>LLM web navigation</td>
<td nowrap>-</td>
<td nowrap>Addresses navigation and QA for web agents in open, dynamic webpage structures.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38901">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38929">Expand Your SCOPE: Semantic Cognition over Potential-Based Exploration for Embodied Visual Navigation</a></td>
<td nowrap>SCOPE models the relationship between local observations and navigation goals with frontier boundaries and potential-based exploration, performing zero-shot visual navigation.</td>
<td nowrap>zero-shot embodied visual navigation</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>frontier/potential-based semantic memory</td>
<td nowrap>zero-shot framework</td>
<td nowrap>-</td>
<td nowrap>Improves long-horizon planning for goal-directed exploration in unknown environments.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38929">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38948">Agent Journey Beyond RGB: Hierarchical Semantic-Spatial Representation Enrichment for Vision-and-Language Navigation</a></td>
<td nowrap>SUSA fuses non-RGB representations with hierarchical semantic understanding and spatial awareness to strengthen semantic-spatial grounding in VLN.</td>
<td nowrap>Map/memory</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>hierarchical semantic-spatial representation</td>
<td nowrap>representation enrichment</td>
<td nowrap>-</td>
<td nowrap>Addresses insufficient use of multimodal environment representations in egocentric VLN.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38948">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64902">MapDream: Task-Driven Map Learning for Vision-Language Navigation</a></td>
<td nowrap>MapDream formulates map building as task-driven BEV image autoregressive generation rather than manual map reconstruction.</td>
<td nowrap>Map/memory</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>learned task-driven BEV map</td>
<td nowrap>map-in-the-loop autoregressive BEV synthesis</td>
<td nowrap>-</td>
<td nowrap>Learns map representations that directly serve navigation goals.</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64902">paper</a></td>
<td nowrap><a href="https://horizonrobotics.github.io/robot_lab/mapdream/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2605.01736">GLMap: Multi-Scale Gaussian-Language Map for Zero-shot Embodied Navigation and Reasoning</a></td>
<td nowrap>GLMap uses multiscale semantic units to store natural-language descriptions and 3D Gaussian simultaneously, enabling zero-shot navigation and reasoning.</td>
<td nowrap>Map/memory</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>multi-scale Gaussian-language map</td>
<td nowrap>zero-shot navigation/reasoning</td>
<td nowrap>-</td>
<td nowrap>Provides large models with a geometrically explicit, semantically multiscale 3D map interface.</td>
<td nowrap><a href="https://arxiv.org/abs/2605.01736">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/sx-zhang/GLMap">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2510.18546">EfficientNav: Towards On-Device Object-Goal Navigation with Navigation Map Caching and Retrieval</a></td>
<td nowrap>EfficientNav uses navigation-map caching and retrieval to reduce long prompts and latency when local small LLMs perform ObjectNav.</td>
<td nowrap>on-device ObjectNav</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>navigation map caching/retrieval</td>
<td nowrap>small LLM planning</td>
<td nowrap>-</td>
<td nowrap>Efficiently performs zero-shot ObjectNav on edge devices.</td>
<td nowrap><a href="https://arxiv.org/abs/2510.18546">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/PKU-SEC-Lab/EfficientNav">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2507.04047">Move to Understand a 3D Scene: Bridging Visual Grounding and Exploration for Efficient and Versatile Embodied Navigation</a></td>
<td nowrap>MTU3D combines active exploration with 3D vision-language grounding, letting the agent complete scene understanding through movement.</td>
<td nowrap>active 3D scene understanding/navigation</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>3D-VL active perception</td>
<td nowrap>3D representation</td>
<td nowrap>-</td>
<td nowrap>Decides where to look to improve 3D scene grounding and navigation efficiency.</td>
<td nowrap><a href="https://arxiv.org/abs/2507.04047">paper</a></td>
<td nowrap><a href="https://mtu3d.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/944">NavQ: Learning a Q-Model for Foresighted Vision-and-Language Navigation</a></td>
<td nowrap>NavQ trains a Q-model on large-scale unlabeled trajectories to estimate future visible information for candidate actions and support look-ahead decisions.</td>
<td nowrap>Map/memory</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>foresighted Q-feature from trajectory data</td>
<td nowrap>Q-learning on unlabeled trajectories</td>
<td nowrap>-</td>
<td nowrap>Look-ahead VLN decision-making</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/944">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
</tbody>
</table>

#### Physically Executable Navigation

Total: 6 papers.

<table>
<thead>
<tr>
<th nowrap>Venue/Year</th>
<th nowrap>Paper/Method</th>
<th nowrap>Abstract</th>
<th nowrap>Task Type</th>
<th nowrap>Environment</th>
<th nowrap>Map/Memory</th>
<th nowrap>Training/Feedback</th>
<th nowrap>Sim/Real/Benchmark</th>
<th nowrap>Paper Task/Goal</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>Source</th>
<th nowrap>Survey Note</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38942">CorrectNav: Self-Correction Flywheel Empowers Vision-Language-Action Navigation Model</a></td>
<td nowrap>CorrectNav automatically generates perception and action self-correction data from model error trajectories, then post-trains VLA navigation models.</td>
<td nowrap>VLA navigation self-correction</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>self-correction flywheel/post-training</td>
<td nowrap>-</td>
<td nowrap>Enables VLA navigation models to recover after deviating from the correct trajectory.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38942">paper</a></td>
<td nowrap><a href="https://correctnav.github.io/">project</a></td>
<td nowrap><a href="https://github.com/owlet914/CorrectNav">code</a></td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64257">SC$^{2}$-WM: A Self-Correcting World Model with Closed-Loop Feedback for Vision-and-Language Navigation in Continuous Environments</a></td>
<td nowrap>SC2-WM uses world-model look-ahead to generate internal feedback, correcting state drift and plans in a closed loop during VLN-CE inference.</td>
<td nowrap>World-model Navigation</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>world-model foresight/internal feedback</td>
<td nowrap>closed-loop self-correcting world model</td>
<td nowrap>-</td>
<td nowrap>Addresses the inability of open-loop execution in continuous VLN to detect and correct internal state drift.</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64257">paper</a></td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64257">project</a></td>
<td nowrap><a href="https://github.com/sunrise-ikun/SC2_WM">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2507.13019">Rethinking the Embodied Gap in Vision-and-Language Navigation: A Holistic Study of Physical and Visual Disparities</a></td>
<td nowrap>VLN-PE systematically evaluates how visual and physical differences across humanoid, quadruped, and wheeled robots affect VLN.</td>
<td nowrap>physical VLN evaluation</td>
<td nowrap>humanoid/quadruped/wheeled robots</td>
<td nowrap>-</td>
<td nowrap>embodied navigation</td>
<td nowrap>physical robotic settings</td>
<td nowrap>Measures the embodied gap between ideal VLN assumptions and real robot execution.</td>
<td nowrap><a href="https://arxiv.org/abs/2507.13019">paper</a></td>
<td nowrap><a href="https://crystalsixone.github.io/vln_pe.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.23468">NavMorph: A Self-Evolving World Model for Vision-and-Language Navigation in Continuous Environments</a></td>
<td nowrap>NavMorph uses a self-evolving world model and contextual evolving memory to model VLN-CE environment dynamics ahead of time and refine policies.</td>
<td nowrap>World-model Navigation</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>contextual evolution memory</td>
<td nowrap>self-evolving world model/RL</td>
<td nowrap>-</td>
<td nowrap>Improves adaptive planning for continuous VLN in new environments and process changes.</td>
<td nowrap><a href="https://arxiv.org/abs/2506.23468">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/Feliciaxyao/NavMorph">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/299">3D Gaussian Map with Open-Set Semantic Grouping for Vision-Language Navigation</a></td>
<td nowrap>This paper uses open-set semantic grouping to unify 3D geometric priors and open semantics in a Gaussian map.</td>
<td nowrap>Map/memory</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>3D Gaussian map + open-set semantic grouping</td>
<td nowrap>3D representation</td>
<td nowrap>-</td>
<td nowrap>Open-semantic 3D map for VLN</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/299">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/1792">monoVLN: Bridging the Observation Gap between Monocular and Panoramic Vision and Language Navigation</a></td>
<td nowrap>monoVLN uses 3DGS to complete missing regions in monocular RGBD observations, narrowing the observation gap between monocular robots and panoramic VLN settings.</td>
<td nowrap>monocular VLN</td>
<td nowrap>monocular RGBD robot</td>
<td nowrap>3DGS implicit partial completion</td>
<td nowrap>embodied navigation</td>
<td nowrap>-</td>
<td nowrap>Enables robots with only a monocular camera to perform VLN that originally relied on panoramic observations.</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/1792">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
</tbody>
</table>

#### Urban / Open-world Navigation

Total: 18 papers.

<table>
<thead>
<tr>
<th nowrap>Venue/Year</th>
<th nowrap>Paper/Method</th>
<th nowrap>Abstract</th>
<th nowrap>Task Type</th>
<th nowrap>Environment</th>
<th nowrap>Map/Memory</th>
<th nowrap>Training/Feedback</th>
<th nowrap>Sim/Real/Benchmark</th>
<th nowrap>Paper Task/Goal</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>Source</th>
<th nowrap>Survey Note</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=88RKxlFUNY">AutoFly: Vision-Language-Action Model for UAV Autonomous Navigation in the Wild</a></td>
<td nowrap>AutoFly is an end-to-end UAV VLA model that uses pseudo-depth encoding and two-stage training to support continuous outdoor planning and obstacle avoidance.</td>
<td nowrap>Open-world Environment</td>
<td nowrap>UAV/urban environment</td>
<td nowrap>-</td>
<td nowrap>two-stage VLA training</td>
<td nowrap>sim+real UAV</td>
<td nowrap>Shifts from explicit route following to autonomous UAV navigation under coarse-grained instructions.</td>
<td nowrap><a href="https://arxiv.org/abs/2602.09657">paper</a></td>
<td nowrap><a href="https://xiaolousun.github.io/AutoFly/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=OKm3w71ymP">OpenFly: A Comprehensive Platform for Aerial Vision-Language Navigation</a></td>
<td nowrap>OpenFly integrates UE, GTA V, Google Earth, and 3DGS to generate large-scale aerial VLN data and platforms.</td>
<td nowrap>aerial VLN platform/benchmark</td>
<td nowrap>UAV/urban environment</td>
<td nowrap>-</td>
<td nowrap>open-world navigation</td>
<td nowrap>Benchmark</td>
<td nowrap>Reduces the cost of collecting UAV VLN data and provides an aerial navigation evaluation platform.</td>
<td nowrap><a href="https://openreview.net/forum?id=OKm3w71ymP">paper</a></td>
<td nowrap><a href="https://shailab-ipec.github.io/openfly/">project</a></td>
<td nowrap><a href="https://github.com/Eziotic/OpenFly">code</a></td>
<td nowrap><a href="https://shailab-ipec.github.io/openfly/">data</a></td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=qSak1Hjfdq">All-day Multi-scenes Lifelong Vision-and-Language Navigation with Tucker Adaptation</a></td>
<td nowrap>TuKA represents multi-scene, multi-time navigation knowledge as Tucker-decomposition adapters, mitigating forgetting in all-day multi-scene VLN.</td>
<td nowrap>lifelong VLN</td>
<td nowrap>UAV/urban environment</td>
<td nowrap>-</td>
<td nowrap>Tucker Adaptation/parameter-efficient tuning</td>
<td nowrap>-</td>
<td nowrap>All-day multi-scene continual adaptation</td>
<td nowrap><a href="https://openreview.net/forum?id=qSak1Hjfdq">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=PaYo96rjij">Lifelong Embodied Navigation Learning</a></td>
<td nowrap>Uni-Walker uses DE-LoRA to separate shared and task-specific navigation knowledge, supporting continual learning over multi-task sequences.</td>
<td nowrap>lifelong embodied navigation</td>
<td nowrap>UAV/urban environment</td>
<td nowrap>-</td>
<td nowrap>DE-LoRA continual learning</td>
<td nowrap>-</td>
<td nowrap>Continual learning of navigation skills</td>
<td nowrap><a href="https://openreview.net/forum?id=PaYo96rjij">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=hzf23XSDcs">CitySeeker: How Do VLMs Explore Embodied Urban Navigation with Implicit Human Needs?</a></td>
<td nowrap>CitySeeker uses 6,440 trajectories across 8 cities to evaluate whether a VLM can turn implicit needs such as "I'm thirsty" into urban navigation goals.</td>
<td nowrap>urban implicit-need navigation benchmark</td>
<td nowrap>UAV/urban environment</td>
<td nowrap>-</td>
<td nowrap>open-world navigation</td>
<td nowrap>Benchmark</td>
<td nowrap>Evaluates a VLM's ability to understand implicit human needs in urban environments and find target places.</td>
<td nowrap><a href="https://openreview.net/forum?id=hzf23XSDcs">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>CitySeeker 6,440 trajectories/8 cities</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38878">AerialVLA: A Vision-Language-Action Model for Aerial Navigation with Online Dialogue</a></td>
<td nowrap>AerialVLA targets UAV vision-dialog navigation, supporting active questioning and route correction using historical landmarks.</td>
<td nowrap>aerial visual dialogue navigation</td>
<td nowrap>UAV</td>
<td nowrap>-</td>
<td nowrap>online dialogue VLA</td>
<td nowrap>-</td>
<td nowrap>Enables UAVs to reach goals through online dialogue and actively correct navigation.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38878">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38885">History-Enhanced Two-Stage Transformer for Aerial Vision-and-Language Navigation</a></td>
<td nowrap>HETT first uses historical grid maps for coarse target localization, then fine-grained visual analysis to optimize UAV actions.</td>
<td nowrap>Open-world Environment</td>
<td nowrap>large-scale urban UAV</td>
<td nowrap>historical grid map</td>
<td nowrap>coarse-to-fine two-stage transformer</td>
<td nowrap>-</td>
<td nowrap>Balances global environment reasoning and local scene understanding in aerial VLN.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38885">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38897">RENEW: Risk- and Energy-Aware Navigation in Dynamic Waterways</a></td>
<td nowrap>RENEW plans risk- and energy-aware paths for ASVs under dynamic water-flow disturbances and adds adaptive safety constraints.</td>
<td nowrap>ASV global path planning</td>
<td nowrap>dynamic waterways</td>
<td nowrap>-</td>
<td nowrap>risk/energy-aware planning</td>
<td nowrap>-</td>
<td nowrap>Water navigation rather than VLN</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38897">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38898">Towards Autonomous UAV Visual Object Search in City Space: Benchmark and Agentic Methodology</a></td>
<td nowrap>CityAVOS provides 2,420 urban UAV visual target-search tasks and uses PRPSearcher for perception-reasoning-planning search.</td>
<td nowrap>UAV visual object search benchmark</td>
<td nowrap>UAV/urban environment</td>
<td nowrap>3D cognitive/uncertainty/dynamic semantic maps</td>
<td nowrap>open-world navigation</td>
<td nowrap>Benchmark</td>
<td nowrap>Enables UAVs to autonomously search for static target objects in urban spaces.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38898">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>CityAVOS 2,420 tasks</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38916">UrbanNav: Learning Language-Guided Embodied Urban Navigation from Web-Scale Human Trajectories</a></td>
<td nowrap>UrbanNav aligns webpage-scale urban walking videos with language trajectories, training agents to navigate cities by free-form language.</td>
<td nowrap>language-guided urban navigation</td>
<td nowrap>ground urban robot</td>
<td nowrap>-</td>
<td nowrap>open-world navigation</td>
<td nowrap>-</td>
<td nowrap>Supports last-mile robots in navigating unfamiliar urban streetscapes by natural language.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38916">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/CASIA-IVA-Lab/UrbanNav">code</a></td>
<td nowrap><a href="https://huggingface.co/datasets/Vigar001/UrbanNav">hf</a></td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38917">Autonomous Vehicle Path Planning by Searching with Differentiable Simulation</a></td>
<td nowrap>DSS uses the differentiable Waymax simulator as a state predictor and critic, searching autonomous-driving action sequences through gradients.</td>
<td nowrap>autonomous driving path planning</td>
<td nowrap>Waymax/traffic scenarios</td>
<td nowrap>-</td>
<td nowrap>differentiable simulation search</td>
<td nowrap>-</td>
<td nowrap>Autonomous-driving planning rather than VLN</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38917">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38920">Real-Time Path Planning for UAVs in Windy Environments Without Computational Fluid Dynamics</a></td>
<td nowrap>GZS avoids CFD and uses point-cloud local topology plus physics-inspired wind-risk modeling for real-time UAV path planning.</td>
<td nowrap>UAV real-time path planning</td>
<td nowrap>windy cluttered 3D environments</td>
<td nowrap>-</td>
<td nowrap>zero-shot training-free planning</td>
<td nowrap>-</td>
<td nowrap>Performs onboard real-time UAV planning in windy 3D environments with obstacles.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38920">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Efficient-VLA, Humanoid-RL, EAI-Safety, WAM</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38938">ReflexDiffusion: Reflection-Enhanced Trajectory Planning for High-lateral-acceleration Scenarios in Autonomous Driving</a></td>
<td nowrap>ReflexDiffusion adds reflective gradient adjustment during diffusion trajectory-planning inference to handle long-tail high-lateral-acceleration scenarios.</td>
<td nowrap>autonomous driving trajectory planning</td>
<td nowrap>high-lateral-acceleration driving</td>
<td nowrap>-</td>
<td nowrap>inference-stage diffusion reflection</td>
<td nowrap>-</td>
<td nowrap>Autonomous-driving planning rather than open VLN</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38938">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38941">Learning from Human Gaze: Human-like Robot Social Navigation in Dense Crowds</a></td>
<td nowrap>GazeNav/Gaze2Nav uses human eye-tracking data to predict socially attended objects and injects that attention into motion planning in crowded spaces.</td>
<td nowrap>social navigation</td>
<td nowrap>dense crowds</td>
<td nowrap>gaze/semantic attention</td>
<td nowrap>open-world navigation</td>
<td nowrap>GazeNav dataset</td>
<td nowrap>Enables robots to perform more human-like social navigation in dense crowds.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38941">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/63554">Plan in Sandbox, Navigate in Open Worlds: Learning Physics-Grounded Abstracted Experience for Embodied Navigation</a></td>
<td nowrap>SAGE lets agents learn in a physically grounded semantic abstraction sandbox and then transfer to open-world navigation.</td>
<td nowrap>Open-world Environment</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>physics-grounded abstracted experience/RL</td>
<td nowrap>-</td>
<td nowrap>Uses abstract physical experience to reduce reliance on realistic simulation and improve open-world navigation.</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/63554">paper</a></td>
<td nowrap><a href="https://frankzxshen.github.io/SAGE">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2510.20685">C-NAV: Towards Self-Evolving Continual Object Navigation in Open World</a></td>
<td nowrap>C-Nav proposes a continual ObjectNav benchmark and uses a dual-path anti-forgetting mechanism to learn new object categories while preserving old knowledge.</td>
<td nowrap>continual ObjectNav benchmark</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>dual-path anti-forgetting/RL</td>
<td nowrap>-</td>
<td nowrap>Continually learns object navigation for new target categories in dynamic open worlds.</td>
<td nowrap><a href="https://arxiv.org/abs/2510.20685">paper</a></td>
<td nowrap><a href="https://bigtree765.github.io/C-Nav-project/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2512.10046">SimWorld-Robotics: Synthesizing Photorealistic and Dynamic Urban Environments for Multimodal Robot Navigation and Collaboration</a></td>
<td nowrap>SimWorld-Robotics uses UE5 procedural generation for dynamic cities and provides a multimodal instruction navigation and multi-robot search collaboration benchmark.</td>
<td nowrap>urban simulation benchmark</td>
<td nowrap>Unmanned vehicles/urban environments</td>
<td nowrap>-</td>
<td nowrap>open-world navigation</td>
<td nowrap>Sim/Benchmark</td>
<td nowrap>Builds large-scale realistic urban simulation to evaluate robot open-environment navigation and collaboration.</td>
<td nowrap><a href="https://arxiv.org/abs/2512.10046">paper</a></td>
<td nowrap><a href="https://scai.cs.jhu.edu/projects/SimWorldRobotics/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2408.15503">RoboSense: Large-scale Dataset and Benchmark for Egocentric Robot Perception and Navigation in Crowded and Unstructured Environments</a></td>
<td nowrap>RoboSense provides multi-sensor egocentric data from cameras, LiDAR, fisheye cameras, and more, evaluating perception and navigation in crowded unstructured environments.</td>
<td nowrap>Evaluation/Data</td>
<td nowrap>crowded/unstructured egocentric robot environments</td>
<td nowrap>-</td>
<td nowrap>open-world navigation</td>
<td nowrap>Benchmark</td>
<td nowrap>Builds a dataset and benchmark for near-field perception and navigation of mobile robots.</td>
<td nowrap><a href="https://arxiv.org/abs/2408.15503">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/suhaisheng/RoboSense">code</a></td>
<td nowrap><a href="https://huggingface.co/datasets/suhaisheng0527/RoboSense">hf</a></td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
</tbody>
</table>

#### Low-cost / On-device Navigation

Total: 3 papers.

<table>
<thead>
<tr>
<th nowrap>Venue/Year</th>
<th nowrap>Paper/Method</th>
<th nowrap>Abstract</th>
<th nowrap>Task Type</th>
<th nowrap>Environment</th>
<th nowrap>Map/Memory</th>
<th nowrap>Training/Feedback</th>
<th nowrap>Sim/Real/Benchmark</th>
<th nowrap>Paper Task/Goal</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>Source</th>
<th nowrap>Survey Note</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2505.11886">Aux-Think: Exploring Reasoning Strategies for Data-Efficient Vision-Language Navigation</a></td>
<td nowrap>Aux-Think systematically compares No/Pre/Post-Think reasoning strategies, finds that reasoning in VLN may collapse, and builds R2R-CoT-320k.</td>
<td nowrap>data-efficient VLN reasoning</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>reasoning strategy evaluation</td>
<td nowrap>-</td>
<td nowrap>Studies which reasoning strategies are actually useful in data-efficient VLN.</td>
<td nowrap><a href="https://arxiv.org/abs/2505.11886">paper</a></td>
<td nowrap><a href="https://horizonrobotics.github.io/robot_lab/aux-think/">project</a></td>
<td nowrap>-</td>
<td nowrap>R2R-CoT-320k</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://openreview.net/pdf?id=5gptKWnVPF">Harnessing Input-Adaptive Inference for Efficient VLN</a></td>
<td nowrap>This paper applies input-adaptive reasoning at three levels: viewpoint selection, early-exit thresholds, and history-view caching, reducing VLN computation by more than 2x.</td>
<td nowrap>On-device/Low-cost</td>
<td nowrap>mobile robot/navigation environment</td>
<td nowrap>-</td>
<td nowrap>efficient navigation</td>
<td nowrap>7 VLN benchmarks</td>
<td nowrap>Reduces the inference cost of history-aware transformer VLN agents while maintaining performance.</td>
<td nowrap><a href="https://arxiv.org/abs/2508.09262">paper</a></td>
<td nowrap><a href="https://true-lab.ai/efficient_vln/">project</a></td>
<td nowrap><a href="https://github.com/secure-ai-systems-group/adaptive-vision-and-language-navigation">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.24065">COSMO: Combination of Selective Memorization for Low-cost Vision-and-Language Navigation</a></td>
<td nowrap>COSMO combines state-space modules and transformer, and designs RSS and cross-modal selective memory to reduce VLN computational cost.</td>
<td nowrap>On-device/Low-cost</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>selective state-space memorization + transformer</td>
<td nowrap>-</td>
<td nowrap>Low-cost VLN model architecture</td>
<td nowrap><a href="https://arxiv.org/abs/2503.24065">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to judge whether navigation is moving toward continuous, physical, and cross-scene settings.</td>
</tr>
</tbody>
</table>

### VLA / Manipulation Policies

VLA is the main track for robotic arms and mobile manipulation, but it is not just an action head attached to a large model. Survey papers concentrate on action representation, diffusion/flow policies, 3D grounding, online/RL fine-tuning, and robustness.

Subdirections: generalist VLA, action representation, diffusion/flow policy, 3D grounding, online/RL fine-tuning, and safety/robustness.

Total: 187 papers.

<table>
<thead>
<tr>
<th nowrap>Subdirection</th>
<th nowrap>Entries</th>
<th nowrap>Focus</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>generalist VLA</td>
<td nowrap>59</td>
<td nowrap>Focus: cross-task generalization, real-robot validation, and general manipulation ability.</td>
</tr>
<tr>
<td nowrap>action representation</td>
<td nowrap>18</td>
<td nowrap>Focus: action tokens, latent actions, chunking, and action-space design.</td>
</tr>
<tr>
<td nowrap>diffusion/flow policy</td>
<td nowrap>63</td>
<td nowrap>Focus: continuous action generation, stable control, and smooth execution.</td>
</tr>
<tr>
<td nowrap>3D grounding</td>
<td nowrap>30</td>
<td nowrap>Focus: point clouds, geometry, affordance, and manipulation localization.</td>
</tr>
<tr>
<td nowrap>online/RL fine-tuning</td>
<td nowrap>13</td>
<td nowrap>Focus: online RL, human-in-the-loop learning, and test-time adaptation.</td>
</tr>
<tr>
<td nowrap>Safety and Robustness</td>
<td nowrap>4</td>
<td nowrap>Focus: attack robustness, safety alignment, and risk exposure.</td>
</tr>
</tbody>
</table>

#### generalist VLA

Total: 59 papers.

<table>
<thead>
<tr>
<th nowrap>Venue/Year</th>
<th nowrap>Paper/Method</th>
<th nowrap>Abstract</th>
<th nowrap>Base VLA</th>
<th nowrap>Action</th>
<th nowrap>Training/Feedback</th>
<th nowrap>Algorithm</th>
<th nowrap>Policy/Type</th>
<th nowrap>Sim/Real</th>
<th nowrap>Paper Task/Goal</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>Source</th>
<th nowrap>Survey Note</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>IROS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2409.12514">TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation</a></td>
<td nowrap>TinyVLA 用小型 VLA 和 diffusion policy 提升机器人操作的数据效率与推理速度。</td>
<td nowrap>TinyVLA</td>
<td nowrap>Diffusion action</td>
<td nowrap>VLA / Generalist VLA</td>
<td nowrap>compact VLA + diffusion policy</td>
<td nowrap>data-efficient VLA</td>
<td nowrap>Real robot manipulation</td>
<td nowrap>构建更小、更快的数据高效 VLA 操作策略。</td>
<td nowrap><a href="https://arxiv.org/abs/2409.12514">paper</a></td>
<td nowrap><a href="https://tiny-vla.github.io/">project</a></td>
<td nowrap><a href="https://github.com/JayceWen/tinyvla">code</a></td>
<td nowrap>-</td>
<td nowrap>ICRA/IROS</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=54U3XHf7qq">MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation</a></td>
<td nowrap>It proposes a VLA with working memory and a long-term perceptual-cognitive memory bank, enabling long-horizon manipulation to use historical context when generating actions.</td>
<td nowrap>VLM + diffusion action expert</td>
<td nowrap>Diffusion action sequences</td>
<td nowrap>VLA / Generalist VLA</td>
<td nowrap>Cognition-Memory-Action + Perceptual-Cognitive Memory Bank</td>
<td nowrap>memory-conditioned VLA</td>
<td nowrap>Sim + Real</td>
<td nowrap>Historical memory modeling for long-horizon robot manipulation.</td>
<td nowrap><a href="https://openreview.net/forum?id=54U3XHf7qq">paper</a></td>
<td nowrap><a href="https://shihao1895.github.io/MemoryVLA">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=DdrsHWobR1">Disentangled Robot Learning via Separate Forward and Inverse Dynamics Pretraining</a></td>
<td nowrap>DeFI decouples visual forward dynamics and inverse dynamics pretraining, then jointly fine-tunes them for action prediction.</td>
<td nowrap>DeFI</td>
<td nowrap>latent action / inverse dynamics</td>
<td nowrap>VLA / Generalist VLA</td>
<td nowrap>GFDM + GIDM disentangled pretraining</td>
<td nowrap>forward-inverse dynamics VLA</td>
<td nowrap>Sim + Real</td>
<td nowrap>Improve generalization by decoupling video prediction and action prediction.</td>
<td nowrap><a href="https://openreview.net/forum?id=DdrsHWobR1">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=IBJtOltTbx">Hybrid Training for Vision-Language-Action Models</a></td>
<td nowrap>HyT lets the VLA learn from CoT reasoning trajectories while allowing direct action output at test time to keep inference fast.</td>
<td nowrap>-</td>
<td nowrap>AR/direct action</td>
<td nowrap>VLA / Generalist VLA</td>
<td nowrap>Hybrid Training</td>
<td nowrap>CoT-trained direct-action VLA</td>
<td nowrap>Sim + Real</td>
<td nowrap>Reduce VLA inference latency while retaining reasoning benefits.</td>
<td nowrap><a href="https://openreview.net/forum?id=IBJtOltTbx">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=LYyoRqf0Ij">End-to-end Listen, Look, Speak and Act</a></td>
<td nowrap>ELLSA uses SA-MoE to perceive and generate vision, text, speech, and actions within a single architecture.</td>
<td nowrap>ELLSA</td>
<td nowrap>multimodal action generation</td>
<td nowrap>VLA / Generalist VLA</td>
<td nowrap>SA-MoE</td>
<td nowrap>full-duplex omni-modal VLA</td>
<td nowrap>speech-interaction + robot benchmarks</td>
<td nowrap>End-to-end multimodal interaction and action generation.</td>
<td nowrap><a href="https://openreview.net/forum?id=LYyoRqf0Ij">paper</a></td>
<td nowrap><a href="https://anonymous.4open.science/r/LLSA-E821">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Humanoid-RL, EAI-Safety</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=OJh7oBCYhL">RoboOmni: Proactive Robot Manipulation in Omni-modal Context</a></td>
<td nowrap>RoboOmni proactively infers intent from speech, ambient sound, and visual cues, then executes manipulation.</td>
<td nowrap>omni-modal LLM</td>
<td nowrap>executor action</td>
<td nowrap>VLA / Generalist VLA</td>
<td nowrap>Perceiver-Thinker-Talker-Executor</td>
<td nowrap>proactive omni-modal VLA</td>
<td nowrap>-</td>
<td nowrap>Proactive robot manipulation in cross-modal context.</td>
<td nowrap><a href="https://openreview.net/forum?id=OJh7oBCYhL">paper</a> / <a href="https://arxiv.org/pdf/2510.23763">paper</a></td>
<td nowrap><a href="https://openmoss.github.io/RoboOmni/">project</a></td>
<td nowrap><a href="https://github.com/OpenMOSS/RoboOmni">code</a></td>
<td nowrap><a href="https://huggingface.co/OpenMOSS-Team/RoboOmni">hf</a> / <a href="https://huggingface.co/datasets/fnlp/OmniAction">hf</a></td>
<td nowrap>WAM</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=PklMD8PwUy">Unified Vision-Language-Action Model</a></td>
<td nowrap>UniVLA unifies vision, language, and actions as discrete token sequences and uses world-model post-training to improve long-horizon policy learning.</td>
<td nowrap>UniVLA</td>
<td nowrap>discrete token AR</td>
<td nowrap>VLA / Efficient/Lightweight VLA</td>
<td nowrap>unified multimodal token modeling + world-model post-training</td>
<td nowrap>autoregressive unified VLA</td>
<td nowrap>CALVIN/LIBERO/SimplerEnv + ALOHA real</td>
<td nowrap>Addresses the problem that traditional VLAs over-rely on VLM semantics and ignore temporal causal structure in vision.</td>
<td nowrap><a href="https://openreview.net/forum?id=PklMD8PwUy">paper</a> / <a href="https://arxiv.org/abs/2503.10631">paper</a> / <a href="https://arxiv.org/abs/2506.19850">paper</a></td>
<td nowrap><a href="https://hybrid-vla.github.io/">project</a> / <a href="https://robertwyq.github.io/univla.github.io/">project</a></td>
<td nowrap><a href="https://github.com/PKU-HMI-Lab/Hybrid-VLA">code</a> / <a href="https://github.com/baaivision/UniVLA">code</a></td>
<td nowrap>CALVIN/LIBERO/SimplerEnv/ALOHA</td>
<td nowrap>HCP-Survey, EAI-VLA-VLN, Awesome-VLA, Efficient-VLA</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=T3i7Ifeatk">Align-Then-stEer: Adapting the Vision-Language Action Models through Unified Latent Guidance</a></td>
<td nowrap>ATE first aligns different action spaces, then uses a unified latent space to guide diffusion/flow VLA adaptation to new tasks and embodiments.</td>
<td nowrap>pretrained diffusion/flow VLA</td>
<td nowrap>latent action guidance</td>
<td nowrap>VLA / Efficient/Lightweight VLA</td>
<td nowrap>Align-Then-stEer / reverse-KL VAE latent alignment</td>
<td nowrap>plug-in adaptation</td>
<td nowrap>Sim + Real</td>
<td nowrap>Addresses action-distribution mismatch and high data/compute cost in downstream adaptation of pretrained VLAs.</td>
<td nowrap><a href="https://openreview.net/forum?id=T3i7Ifeatk">paper</a> / <a href="https://arxiv.org/abs/2509.02055">paper</a></td>
<td nowrap><a href="https://align-then-steer.github.io/">project</a></td>
<td nowrap><a href="https://github.com/TeleHuman/Align-Then-Steer">code</a></td>
<td nowrap>-</td>
<td nowrap>Efficient-VLA</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=UD4Rw8MOEK">Verifier-free Test-Time Sampling for Vision Language Action Models</a></td>
<td nowrap>MG-Select uses KL confidence from the model's internal masked reference action distribution to select action candidates at test time.</td>
<td nowrap>-</td>
<td nowrap>AR candidate selection</td>
<td nowrap>VLA / Generalist VLA</td>
<td nowrap>MG-Select / masking distribution guided selection</td>
<td nowrap>verifier-free test-time scaling</td>
<td nowrap>Sim + Real</td>
<td nowrap>Test-time action selection without an extra verifier.</td>
<td nowrap><a href="https://openreview.net/forum?id=UD4Rw8MOEK">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=kt51kZH4aG">X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model</a></td>
<td nowrap>X-VLA uses embodiment-specific soft prompts and a flow-matching Transformer to learn general control across robot platforms.</td>
<td nowrap>X-VLA</td>
<td nowrap>flow-matching continuous action</td>
<td nowrap>VLA / Generalist VLA</td>
<td nowrap>embodiment-specific soft prompts</td>
<td nowrap>cross-embodiment VLA</td>
<td nowrap>6 sim envs + 3 real platforms</td>
<td nowrap>Cross-embodiment VLA training and generalization.</td>
<td nowrap><a href="https://openreview.net/forum?id=kt51kZH4aG">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=tc2UsBeODW">VLM4VLA: Revisiting Vision-Language-Models in Vision-Language-Action Models</a></td>
<td nowrap>VLM4VLA systematically compares transfer performance when different VLMs serve as VLA backbones, showing that general VLM capability does not directly predict control performance.</td>
<td nowrap>VLM4VLA minimal adapter</td>
<td nowrap>policy action</td>
<td nowrap>VLA / Generalist VLA</td>
<td nowrap>minimal VLM-to-VLA adaptation + embodied capability ablation</td>
<td nowrap>benchmark/adaptation pipeline</td>
<td nowrap>3 benchmarks</td>
<td nowrap>Evaluate the real contribution of the VLM backbone to VLA control.</td>
<td nowrap><a href="https://openreview.net/forum?id=tc2UsBeODW">paper</a></td>
<td nowrap><a href="https://cladernyjorn.github.io/VLM4VLA.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=tsxwloasw5">Vision-Language-Action Instruction Tuning: From Understanding to Manipulation</a></td>
<td nowrap>InstructVLA uses VLA instruction tuning to preserve VLM reasoning capability while improving fine-grained manipulation performance.</td>
<td nowrap>InstructVLA</td>
<td nowrap>AR/action generation</td>
<td nowrap>VLA / RL/Online Fine-tuning</td>
<td nowrap>VLA-IT + MoE adaptation</td>
<td nowrap>end-to-end instruction-tuned VLA</td>
<td nowrap>-</td>
<td nowrap>Addresses the tradeoff between visual-language understanding and action generation in VLAs, and their tendency to forget pretrained capabilities.</td>
<td nowrap><a href="https://openreview.net/forum?id=tsxwloasw5">paper</a> / <a href="https://arxiv.org/abs/2507.17520">paper</a></td>
<td nowrap><a href="https://yangs03.github.io/InstructVLA_Home/">project</a></td>
<td nowrap><a href="https://github.com/InternRobotics/InstructVLA">code</a></td>
<td nowrap>650K VLA-IT dataset</td>
<td nowrap>EAI-Guide, HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Efficient-VLA, Robot-Learning, Humanoid-RL, EAI-Safety, EAI-ROS, WAM, RL-VLA</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=KcJ9U0x6kO">HAMLET: Switch Your Vision-Language-Action Model into a History-Aware Policy</a></td>
<td nowrap>HAMLET uses moment tokens and a lightweight memory module to turn a current-frame-only VLA into a history-aware policy.</td>
<td nowrap>GR00T N1.5 / pretrained VLA</td>
<td nowrap>history-aware action prediction</td>
<td nowrap>VLA / Generalist VLA</td>
<td nowrap>moment tokens + time-contrastive init + memory module</td>
<td nowrap>history-aware VLA adapter</td>
<td nowrap>RoboCasa/LIBERO + real</td>
<td nowrap>Long-horizon manipulation with historical dependencies.</td>
<td nowrap><a href="https://openreview.net/forum?id=KcJ9U0x6kO">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38902">DiTEA: Mixture-of-Experts for Vision-Language-Action Model in Robotic Manipulation</a></td>
<td nowrap>DiTEA adds Action MoE and task-instruction gating to a diffusion VLA action head to reduce multi-task forgetting.</td>
<td nowrap>diffusion-based VLA</td>
<td nowrap>Diffusion</td>
<td nowrap>VLA / Generalist VLA</td>
<td nowrap>Diffusion Transformer Action MoE + Task-Instruction Gate</td>
<td nowrap>MoE VLA</td>
<td nowrap>Sim + Real</td>
<td nowrap>Instruction following and forgetting resistance for multi-task diffusion VLAs.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38902">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38910">TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for Vision-Language-Action Models</a></td>
<td nowrap>TTF-VLA fuses historical and current visual tokens without training, improving VLA reasoning quality under noise and temporal scenarios.</td>
<td nowrap>OpenVLA / VLA-Cache</td>
<td nowrap>token-level inference enhancement</td>
<td nowrap>VLA / Generalist VLA</td>
<td nowrap>Temporal Token Fusion + pixel difference + attention relevance</td>
<td nowrap>training-free inference plugin</td>
<td nowrap>LIBERO + SimplerEnv + Real</td>
<td nowrap>Temporal visual token fusion.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38910">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62813">Being-H0: Vision-Language-Action Pretraining from Large-Scale Human Videos</a></td>
<td nowrap>Being-H0 performs physical instruction tuning and hand-motion tokenization on large-scale human-hand videos, then transfers to dexterous manipulation.</td>
<td nowrap>Being-H0</td>
<td nowrap>part-level motion tokens / AR</td>
<td nowrap>VLA / RL/Online Fine-tuning</td>
<td nowrap>physical instruction tuning + hand motion tokenization</td>
<td nowrap>dexterous VLA</td>
<td nowrap>human video pretrain + real robot</td>
<td nowrap>Addresses VLA dependence on expensive robot demonstrations and weak generalization in dexterous manipulation.</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62813">paper</a> / <a href="https://arxiv.org/pdf/2507.15597">paper</a> / <a href="https://arxiv.org/abs/2507.15597">paper</a></td>
<td nowrap><a href="https://beingbeyond.github.io/Being-H0">project</a> / <a href="https://beingbeyond.github.io/Being-H0/">project</a></td>
<td nowrap><a href="https://github.com/BeingBeyond/Being-H0">code</a></td>
<td nowrap>BeingBeyond h0_post_train dataset</td>
<td nowrap>EAI-Guide, HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Efficient-VLA, Robot-Learning, Humanoid-RL, EAI-Safety, EAI-ROS, WAM, RL-VLA</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/60980">RA-VLA: Retrieval-Augmented VLA for Test-Time Adaptation</a></td>
<td nowrap>RA-VLA uses behavior-aligned retrieval and a grounded execution pipeline for training-free test-time adaptation to new task distributions.</td>
<td nowrap>RA-VLA</td>
<td nowrap>retrieval-grounded action</td>
<td nowrap>VLA / Generalist VLA</td>
<td nowrap>behavior-aligned retrieval + grounded execution</td>
<td nowrap>test-time adaptation VLA</td>
<td nowrap>LIBERO + UR5e real</td>
<td nowrap>Training-free test-time adaptation.</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/60980">paper</a></td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/60980">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62270">A Generalist Pair-wise Progress Critic Model for Vision-Language-Action Robots</a></td>
<td nowrap>VLAC unifies the action policy and pairwise task-progress critic in an autoregressive architecture, providing intrinsic rewards for RL.</td>
<td nowrap>VLAC</td>
<td nowrap>AR</td>
<td nowrap>VLA / RL/Online Fine-tuning</td>
<td nowrap>pair-wise progress critic + intrinsic reward RL</td>
<td nowrap>action-critic VLA</td>
<td nowrap>diverse tasks + real RL</td>
<td nowrap>General task-progress assessment and action generation.</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62270">paper</a></td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62270">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62528">Bring My Cup! Personalizing Vision-Language-Action Models with Visual Attentive Prompting</a></td>
<td nowrap>VAP uses a small number of reference images as visual memory, injecting target-instance attention into a frozen VLA to execute personalized instructions.</td>
<td nowrap>frozen VLA</td>
<td nowrap>visual-prompted action</td>
<td nowrap>VLA / Generalist VLA</td>
<td nowrap>Visual Attentive Prompting</td>
<td nowrap>training-free personalization adapter</td>
<td nowrap>Personalized-SIMPLER/Personalized-VLABench + real</td>
<td nowrap>Personalized object manipulation.</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62528">paper</a></td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62528">project</a></td>
<td nowrap>-</td>
<td nowrap>Personalized-SIMPLER</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66596">From Abstraction to Instantiation: Learning Behavioral Representation for Vision-Language-Action Model</a></td>
<td nowrap>BehaviorVLA learns long-horizon behavior representations and decodes them by execution phase into precise actions to improve out-of-distribution generalization.</td>
<td nowrap>BehaviorVLA</td>
<td nowrap>AR / behavior-conditioned decoding</td>
<td nowrap>VLA / Generalist VLA</td>
<td nowrap>VBE + PBD</td>
<td nowrap>behavior-representation VLA</td>
<td nowrap>RoboTwin2/LIBERO/CALVIN + real sim2real</td>
<td nowrap>Temporally consistent behavior representation.</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66596">paper</a></td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66596">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61157">VLA-ATTC: Adaptive Test-Time Compute for VLA Models with Relative Action Critic Model</a></td>
<td nowrap>VLA-ATTC triggers test-time thinking with uncertainty and uses a relative-action critic to pick the best candidate action.</td>
<td nowrap>PI0.5 / VLA</td>
<td nowrap>candidate action selection</td>
<td nowrap>VLA / Generalist VLA</td>
<td nowrap>adaptive TTC + Relative Action Critic</td>
<td nowrap>test-time compute VLA</td>
<td nowrap>LIBERO-LONG</td>
<td nowrap>Adaptive test-time computation and action selection.</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61157">paper</a></td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61157">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66066">SCALE: Self-uncertainty Conditioned Adaptive Looking and Execution for Vision-Language-Action Models</a></td>
<td nowrap>SCALE uses the VLA's own uncertainty to jointly regulate visual perception and action exploration/exploitation in a single forward pass.</td>
<td nowrap>generic VLA</td>
<td nowrap>adaptive execution</td>
<td nowrap>VLA / RL/Online Fine-tuning</td>
<td nowrap>self-uncertainty conditioned adaptive looking/execution</td>
<td nowrap>training-free single-pass inference strategy</td>
<td nowrap>Sim + Real</td>
<td nowrap>Training-free robust execution at test time.</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66066">paper</a></td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66066">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Efficient-VLA, Robot-Learning, Humanoid-RL, EAI-Safety, WAM, RL-VLA</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64826">XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>VLA / Generalist VLA</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64826">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66510">Escaping the Diversity Trap in Robotic Manipulation via Anchor-Centric Adaptation</a></td>
<td nowrap>ACA shows that blindly pursuing demonstration diversity under a small budget causes density gaps, then adapts by repeating anchor demonstrations and expanding boundaries.</td>
<td nowrap>VLA adaptation</td>
<td nowrap>residual updates</td>
<td nowrap>generalist VLA / general-purpose VLA</td>
<td nowrap>Anchor-Centric Adaptation</td>
<td nowrap>data-efficient real-robot adaptation</td>
<td nowrap>Real</td>
<td nowrap>Low-budget embodiment adaptation.</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66510">paper</a></td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66510">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/63997">Embodied Interpretability: Linking Causal Understanding to Generalization in Vision-Language-Action Models</a></td>
<td nowrap>This paper uses interventional masking to estimate the causal effect of visual regions on action prediction and uses NMR to predict generalization.</td>
<td nowrap>-</td>
<td nowrap>diagnostic not action representation</td>
<td nowrap>VLA / Generalist VLA</td>
<td nowrap>ISS + NMR</td>
<td nowrap>interpretability/diagnostic</td>
<td nowrap>manipulation tasks</td>
<td nowrap>Causal attribution and generalization diagnosis for VLAs.</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/63997">paper</a></td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/63997">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2511.04555">Evo-1: Lightweight Vision-Language-Action Model with Preserved Semantic Alignment</a></td>
<td nowrap>Evo-1 targets lightweight VLAs, preserving language-vision semantic alignment and manipulation ability while compressing model size.</td>
<td nowrap>Evo-1</td>
<td nowrap>-</td>
<td nowrap>VLA / Efficient/Lightweight VLA</td>
<td nowrap>-</td>
<td nowrap>lightweight VLA</td>
<td nowrap>-</td>
<td nowrap>Preserving semantic alignment in lightweight VLAs.</td>
<td nowrap><a href="https://arxiv.org/abs/2511.04555">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/MINT-SJTU/Evo-1">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2512.09928">HiF-VLA: Hindsight, Insight and Foresight through Motion Representation for Vision-Language-Action Models</a></td>
<td nowrap>HiF-VLA introduces hindsight, insight, and foresight through motion representations to improve VLA understanding of action processes.</td>
<td nowrap>HiF-VLA</td>
<td nowrap>motion representation</td>
<td nowrap>VLA / Generalist VLA</td>
<td nowrap>hindsight/insight/foresight motion modeling</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Motion-representation-enhanced VLA.</td>
<td nowrap><a href="https://arxiv.org/abs/2512.09928">paper</a></td>
<td nowrap><a href="https://hifvla.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2603.12193">SaPaVe: Towards Active Perception and Manipulation in Vision-Language-Action Models for Robotics</a></td>
<td nowrap>SaPaVe combines active perception and manipulation, enabling a VLA to look before acting in uncertain scenes.</td>
<td nowrap>SaPaVe</td>
<td nowrap>AR</td>
<td nowrap>VLA / Generalist VLA</td>
<td nowrap>active perception + manipulation</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Active-perception-driven manipulation.</td>
<td nowrap><a href="https://arxiv.org/abs/2603.12193">paper</a></td>
<td nowrap><a href="https://lmzpai.github.io/SaPaVe">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2601.12796">Contact-Aware Neural Dynamics</a></td>
<td nowrap>This paper learns contact-aware neural dynamics for modeling state changes in contact-rich manipulation.</td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>contact-rich dynamics / robot manipulation</td>
<td nowrap>contact-aware neural dynamics</td>
<td nowrap>dynamics model, not generalist VLA</td>
<td nowrap>-</td>
<td nowrap>Contact-aware dynamics modeling.</td>
<td nowrap><a href="https://arxiv.org/abs/2601.12796">paper</a></td>
<td nowrap><a href="https://changwei-jing.github.io/neural-physics/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Awesome-EAI, EAI-VLA-VLN</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2508.21046">CogVLA: Cognition-Aligned Vision-Language-Action Model via Instruction-Driven Routing &amp; Sparsification</a></td>
<td nowrap>CogVLA reduces VLA post-training overhead and improves efficiency through instruction-driven routing and sparsification.</td>
<td nowrap>CogVLA</td>
<td nowrap>AR</td>
<td nowrap>VLA / Efficient/Lightweight VLA</td>
<td nowrap>instruction-driven routing + sparsification</td>
<td nowrap>efficient VLA</td>
<td nowrap>-</td>
<td nowrap>Addresses the high post-training and deployment compute cost of large VLM-based VLAs.</td>
<td nowrap><a href="https://arxiv.org/abs/2508.21046">paper</a></td>
<td nowrap><a href="https://jiutian-vl.github.io/CogVLA-page/">project</a></td>
<td nowrap><a href="https://github.com/JiuTian-VL/CogVLA">code</a></td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN, Efficient-VLA</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2505.15660">Exploring the Limits of Vision-Language-Action Manipulation in Cross-task Generalization</a></td>
<td nowrap>This paper systematically evaluates the cross-task generalization limits of VLAs and proposes AGNOSTOS/X-ICM-related methods to improve generalization.</td>
<td nowrap>AGNOSTOS / X-ICM</td>
<td nowrap>-</td>
<td nowrap>VLA / Generalist VLA</td>
<td nowrap>-</td>
<td nowrap>cross-task generalization study</td>
<td nowrap>-</td>
<td nowrap>Evaluation of cross-task generalization boundaries.</td>
<td nowrap><a href="https://arxiv.org/abs/2505.15660">paper</a> / <a href="https://arxiv.org/pdf/2505.15660">paper</a></td>
<td nowrap><a href="https://jiaming-zhou.github.io/AGNOSTOS/">project</a> / <a href="https://jiaming-zhou.github.io/AGNOSTOS">project</a></td>
<td nowrap><a href="https://github.com/jiaming-zhou/X-ICM">code</a></td>
<td nowrap>-</td>
<td nowrap>WAM</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2505.15517">Robo2VLM: Improving Visual Question Answering using Large-Scale Robot Manipulation Data</a></td>
<td nowrap>Robo2VLM uses large-scale robot manipulation data to improve VLM/VQA understanding of object states and actionability.</td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>VLA / Generalist VLA</td>
<td nowrap>-</td>
<td nowrap>robot-data-enhanced VLM/VQA, not action policy</td>
<td nowrap>-</td>
<td nowrap>Enhancing visual question answering with robot manipulation data.</td>
<td nowrap><a href="https://arxiv.org/abs/2505.15517">paper</a></td>
<td nowrap><a href="https://berkeleyautomation.github.io/robo2vlm/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.22242">4D-VLA: Spatiotemporal Vision-Language-Action Pretraining with Cross-Scene Calibration</a></td>
<td nowrap>4D-VLA mitigates state/coordinate confusion in cross-scene pretraining through RGB-D sequences, coordinate alignment, and memory-bank sampling.</td>
<td nowrap>4D-VLA</td>
<td nowrap>AR</td>
<td nowrap>VLA / Generalist VLA</td>
<td nowrap>4D spatiotemporal pretraining + cross-scene calibration + memory bank sampling</td>
<td nowrap>-</td>
<td nowrap>Sim + Real</td>
<td nowrap>Addresses action distribution divergence caused by incomplete inputs in multi-source robot-data pretraining.</td>
<td nowrap><a href="https://arxiv.org/abs/2506.22242">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/LogosRoboticsGroup/4D-VLA">code</a></td>
<td nowrap>MV-Bench</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2510.24194">Blindfolded Experts Generalize Better: Insights from Robotic Manipulation and Videogames</a></td>
<td nowrap>This paper studies why experts with reduced visual dependence generalize better in robotic manipulation and games.</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA / Generalist VLA</td>
<td nowrap>blindfolded expert / reduced observation analysis</td>
<td nowrap>generalization analysis</td>
<td nowrap>-</td>
<td nowrap>Relationship between visual dependence and generalization.</td>
<td nowrap><a href="https://arxiv.org/abs/2510.24194">paper</a></td>
<td nowrap><a href="https://sites.google.com/view/blindfoldedexperts/home">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2510.11321">HiMaCon: Discovering Hierarchical Manipulation Concepts from Unlabeled Multi-Modal Data</a></td>
<td nowrap>HiMaCon discovers hierarchical manipulation concepts from unlabeled multimodal data for structured representation of robot skills.</td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>VLA / Generalist VLA</td>
<td nowrap>hierarchical manipulation concept discovery</td>
<td nowrap>concept representation</td>
<td nowrap>Sim/Benchmark confirmed</td>
<td nowrap>Unlabeled hierarchical manipulation-concept discovery.</td>
<td nowrap><a href="https://arxiv.org/abs/2510.11321">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2505.23705">Knowledge Insulating Vision-Language-Action Models: Train Fast, Run Fast, Generalize Better</a></td>
<td nowrap>This paper reduces VLA training and inference cost through knowledge isolation while improving generalization.</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA / Generalist VLA</td>
<td nowrap>knowledge insulation</td>
<td nowrap>efficient/generalist VLA</td>
<td nowrap>-</td>
<td nowrap>Faster training, faster inference, and improved generalization.</td>
<td nowrap><a href="https://arxiv.org/abs/2505.23705">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://openreview.net/forum?id=3XuUnUEI7e">Diversifying Parallel Ergodic Search: A Signature Kernel Evolution Strategy</a></td>
<td nowrap>This paper uses a signature-kernel evolution strategy to improve trajectory diversity and exploration efficiency in parallel ergodic search.</td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>generalist VLA / general-purpose VLA</td>
<td nowrap>Signature Kernel Evolution Strategy</td>
<td nowrap>trajectory optimization/search, not VLA</td>
<td nowrap>robotic benchmarks</td>
<td nowrap>Diverse parallel ergodic search.</td>
<td nowrap><a href="https://openreview.net/forum?id=3XuUnUEI7e">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/1325">FedVLA: Federated Vision-Language-Action Learning with Dual Gating Mixture-of-Experts for Robotic Manipulation</a></td>
<td nowrap>FedVLA trains VLAs on multi-client robot data using federated learning and dual-gated MoE.</td>
<td nowrap>FedVLA</td>
<td nowrap>AR</td>
<td nowrap>VLA / Efficient/Lightweight VLA</td>
<td nowrap>federated learning + dual-gating MoE</td>
<td nowrap>federated VLA</td>
<td nowrap>-</td>
<td nowrap>Privacy-preserving/multi-client VLA learning.</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/1325">paper</a> / <a href="https://arxiv.org/abs/2508.02190">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Efficient-VLA</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/225">PASG: A Closed-Loop Framework for Automated Geometric Primitive Extraction and Semantic Anchoring in Robotic Manipulation</a></td>
<td nowrap>PASG automatically extracts geometric primitives and anchors them with VLM semantics, connecting geometric affordances with task semantics.</td>
<td nowrap>VLM/Qwen2.5VL-PA</td>
<td nowrap>-</td>
<td nowrap>VLA / Generalist VLA</td>
<td nowrap>Primitive-Aware Semantic Grounding</td>
<td nowrap>semantic-affordance grounding framework</td>
<td nowrap>benchmark</td>
<td nowrap>Anchoring geometric primitives and semantic affordances.</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/225">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>spatial-semantic reasoning benchmark</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.07087">iManip: Skill-Incremental Learning for Robotic Manipulation</a></td>
<td nowrap>iManip targets skill-incremental learning for robot manipulation, preserving old skills when new skills are added.</td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>generalist VLA / general-purpose VLA</td>
<td nowrap>incremental skill learning</td>
<td nowrap>skill-incremental manipulation</td>
<td nowrap>-</td>
<td nowrap>Incremental learning for robot skills.</td>
<td nowrap><a href="https://arxiv.org/abs/2503.07087">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/972">4D Visual Pre-training for Robot Learning</a></td>
<td nowrap>FVP sets visual pretraining as next-point-cloud prediction and uses a diffusion model to improve real-robot 3D representations and imitation-learning success rates.</td>
<td nowrap>FVP + DP3</td>
<td nowrap>3D policy support</td>
<td nowrap>generalist VLA / general-purpose VLA</td>
<td nowrap>next-point-cloud prediction diffusion pretraining</td>
<td nowrap>4D visual pretraining</td>
<td nowrap>Real manipulation</td>
<td nowrap>4D/point-cloud visual pretraining.</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/972">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICML 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2502.19417">Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models</a></td>
<td nowrap>Hi Robot uses a hierarchical VLA to decompose open-ended instructions into high-level planning and low-level action execution.</td>
<td nowrap>hierarchical VLA</td>
<td nowrap>AR</td>
<td nowrap>VLA / Generalist VLA</td>
<td nowrap>hierarchical policy/planning</td>
<td nowrap>open-ended instruction following</td>
<td nowrap>-</td>
<td nowrap>Open-ended hierarchical instruction following.</td>
<td nowrap><a href="https://arxiv.org/abs/2502.19417">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICML 2025</td>
<td nowrap><a href="https://arxiv.org/pdf/2503.03734">OTTER: A Vision-Language-Action Model with Text-Aware Visual Feature Extraction</a></td>
<td nowrap>OTTER uses text-aware visual feature extraction to make VLAs focus on image information relevant to the language goal.</td>
<td nowrap>OTTER</td>
<td nowrap>AR</td>
<td nowrap>VLA / Generalist VLA</td>
<td nowrap>text-aware visual feature extraction</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Text-aware visual feature extraction.</td>
<td nowrap><a href="https://arxiv.org/pdf/2503.03734">paper</a></td>
<td nowrap><a href="https://ottervla.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICML 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2501.18867">UP-VLA: A Unified Understanding and Prediction Model for Embodied Agent</a></td>
<td nowrap>UP-VLA unifies understanding and prediction tasks, giving embodied agents both semantic understanding and future/action prediction capability.</td>
<td nowrap>UP-VLA</td>
<td nowrap>-</td>
<td nowrap>VLA / Generalist VLA</td>
<td nowrap>-</td>
<td nowrap>unified understanding-prediction model</td>
<td nowrap>-</td>
<td nowrap>Unified modeling of embodied understanding and prediction.</td>
<td nowrap><a href="https://arxiv.org/abs/2501.18867">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/CladernyJorn/UP-VLA">code</a></td>
<td nowrap>-</td>
<td nowrap>Awesome-EAI, Awesome-VLA</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICML 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2411.18825">ELEMENTAL: Interactive Learning from Demonstrations and Vision-Language Models for Reward Design in Robotics</a></td>
<td nowrap>ELEMENTAL combines demonstration interaction with VLM-generated/improved robot reward design.</td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>interactive learning / reward design</td>
<td nowrap>demonstrations + VLM reward design</td>
<td nowrap>reward learning, not generalist VLA</td>
<td nowrap>-</td>
<td nowrap>Interactive reward design.</td>
<td nowrap><a href="https://arxiv.org/abs/2411.18825">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICML 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2410.22391">A Large Recurrent Action Model: xLSTM enables Fast Inference for Robotics Tasks</a></td>
<td nowrap>LRAM replaces Transformers with xLSTM to build a large action model, enabling faster inference and long-sequence extrapolation.</td>
<td nowrap>LRAM</td>
<td nowrap>sequence action model</td>
<td nowrap>VLA / Generalist VLA</td>
<td nowrap>xLSTM recurrent action model</td>
<td nowrap>large recurrent action model</td>
<td nowrap>-</td>
<td nowrap>Addresses slow inference of Transformer-based large action models in real-time robot tasks.</td>
<td nowrap><a href="https://arxiv.org/abs/2410.22391">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/ml-jku/LRAM">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICML 2025</td>
<td nowrap><a href="https://arxiv.org/pdf/2502.13142">Pre-training Auto-regressive Robotic Models with 4D Representations</a></td>
<td nowrap>ARM4R uses 4D representation pretraining for autoregressive robot models to improve spatiotemporal understanding and manipulation generalization.</td>
<td nowrap>ARM4R</td>
<td nowrap>AR</td>
<td nowrap>generalist VLA / efficient/lightweight VLA</td>
<td nowrap>4D representation pretraining</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Autoregressive pretraining with 4D representations.</td>
<td nowrap><a href="https://arxiv.org/pdf/2502.13142">paper</a></td>
<td nowrap><a href="https://arm4r.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Efficient-VLA, Humanoid-RL, WAM</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICML 2025</td>
<td nowrap><a href="https://www.arxiv.org/pdf/2506.03863">STAR: Learning Diverse Robot Skill Abstractions through Rotation-Augmented Vector Quantization</a></td>
<td nowrap>STAR uses rotation-augmented residual skill quantization and a causal skill transformer to learn discrete skill abstraction and composition.</td>
<td nowrap>-</td>
<td nowrap>discrete skill tokens</td>
<td nowrap>generalist VLA / RL/online fine-tuning</td>
<td nowrap>RaRSQ + causal skill transformer</td>
<td nowrap>skill abstraction</td>
<td nowrap>LIBERO + Real</td>
<td nowrap>Addresses codebook collapse in VQ-style skill abstraction and insufficient modeling of causal skill composition.</td>
<td nowrap><a href="https://www.arxiv.org/pdf/2506.03863">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/iLearn-Lab/ICML25-STAR">code</a></td>
<td nowrap>-</td>
<td nowrap>EAI-Guide, Octoday, HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Efficient-VLA, Robot-Learning, Humanoid-RL, EAI-Safety, RL-VLA</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2501.10105">UniAct: Universal Actions For Enhanced Embodied Foundation Models</a></td>
<td nowrap>UniAct introduces universal actions as a cross-task/cross-embodiment action interface to strengthen embodied foundation models.</td>
<td nowrap>UniAct</td>
<td nowrap>universal actions</td>
<td nowrap>VLA / Generalist VLA</td>
<td nowrap>universal action representation</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Universal action representation.</td>
<td nowrap><a href="https://arxiv.org/abs/2501.10105">paper</a></td>
<td nowrap><a href="https://2toinf.github.io/UniAct/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Awesome-EAI, Humanoid-RL</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.13446">MoManipVLA: Transferring Vision-language-action Models for General Mobile Manipulation</a></td>
<td nowrap>MoManipVLA transfers VLA to mobile manipulation scenarios for general manipulation that coordinates navigation and robotic arms.</td>
<td nowrap>MoManipVLA</td>
<td nowrap>-</td>
<td nowrap>VLA / Efficient/Lightweight VLA</td>
<td nowrap>-</td>
<td nowrap>mobile manipulation VLA transfer</td>
<td nowrap>-</td>
<td nowrap>General mobile-manipulation transfer.</td>
<td nowrap><a href="https://arxiv.org/abs/2503.13446">paper</a></td>
<td nowrap><a href="https://gary3410.github.io/momanipVLA/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN, Efficient-VLA</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.06960">A Data-Centric Revisit of Pre-Trained Vision Models for Robot Learning</a></td>
<td nowrap>This paper reevaluates the role of pretrained visual models in robot learning from a data-centric perspective.</td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>VLA / Generalist VLA</td>
<td nowrap>-</td>
<td nowrap>data-centric robot visual pretraining study</td>
<td nowrap>-</td>
<td nowrap>Data-factor evaluation of pretrained visual models.</td>
<td nowrap><a href="https://arxiv.org/abs/2503.06960">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/CVMI-Lab/SlotMIM">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2504.00420">Think Small, Act Big: Primitive Prompt Learning for Lifelong Robot Manipulation</a></td>
<td nowrap>PPL uses reusable primitive prompts to support continual acquisition of new skills in lifelong robot learning.</td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>VLA / Generalist VLA</td>
<td nowrap>Primitive Prompt Learning</td>
<td nowrap>lifelong robot manipulation</td>
<td nowrap>Sim + Real</td>
<td nowrap>Lifelong learning with reusable primitive prompts.</td>
<td nowrap><a href="https://arxiv.org/abs/2504.00420">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://cvpr.thecvf.com/virtual/2025/poster/32789">Phoenix: A Motion-based Self-Reflection Framework for Fine-grained Robotic Action Correction</a></td>
<td nowrap>Phoenix connects MLLM semantic reflection and low-level diffusion policies with motion instructions, enabling fine-grained action correction.</td>
<td nowrap>MLLM + motion-conditioned diffusion policy</td>
<td nowrap>Diffusion correction</td>
<td nowrap>VLA / Generalist VLA</td>
<td nowrap>dual-process motion adjustment + motion-conditioned diffusion policy</td>
<td nowrap>self-reflection/action correction</td>
<td nowrap>-</td>
<td nowrap>Fine-grained robot action correction.</td>
<td nowrap><a href="https://cvpr.thecvf.com/virtual/2025/poster/32789">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2406.14235">Mitigating the Human-Robot Domain Discrepancy in Visual Pre-training for Robotic Manipulation</a></td>
<td nowrap>This paper mitigates the domain gap between human-video visual pretraining and robotic manipulation.</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA / Generalist VLA</td>
<td nowrap>human-robot domain discrepancy mitigation</td>
<td nowrap>visual pretraining for manipulation</td>
<td nowrap>-</td>
<td nowrap>Human-robot domain gap in visual pretraining.</td>
<td nowrap><a href="https://arxiv.org/abs/2406.14235">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2505.02166">CrayonRobo: Object-Centric Prompt-Driven Vision-Language-Action Model for Robotic Manipulation</a></td>
<td nowrap>CrayonRobo uses object-centric 2D visual prompts overlaid on images to express contact poses and motion directions for guiding long-horizon manipulation.</td>
<td nowrap>-</td>
<td nowrap>SE(3) contact pose + motion direction</td>
<td nowrap>VLA / Efficient/Lightweight VLA</td>
<td nowrap>object-centric visual-language prompts</td>
<td nowrap>-</td>
<td nowrap>Sim + Real</td>
<td nowrap>Addresses ambiguity in language goals and the fact that image/video goals can be too fine-grained and poor at expressing action constraints.</td>
<td nowrap><a href="https://arxiv.org/abs/2505.02166">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/clorislili/CrayonRobo">code</a></td>
<td nowrap>-</td>
<td nowrap>HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Efficient-VLA, Robot-Learning, Humanoid-RL, EAI-Safety</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/html/2505.00693">Robotic Visual Instruction</a></td>
<td nowrap>RoVI/VIEW uses hand-drawn object-centric 2D symbolic instructions to express spatial-temporal constraints and convert them into 3D manipulation actions.</td>
<td nowrap>VIEW pipeline with VLMs</td>
<td nowrap>3D action sequences</td>
<td nowrap>VLA / RL/Online Fine-tuning</td>
<td nowrap>Robotic Visual Instruction + Visual Instruction Embodied Workflow</td>
<td nowrap>-</td>
<td nowrap>Sim + Real</td>
<td nowrap>Addresses insufficient spatial precision in natural-language robot instructions and the inconvenience of speech in public scenes.</td>
<td nowrap><a href="https://arxiv.org/html/2505.00693">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>open-source RoVI dataset</td>
<td nowrap>EAI-Guide, HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Efficient-VLA, Robot-Learning, Humanoid-RL, EAI-Safety, WAM, RL-VLA</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2411.17662">RoboPEPP: Vision-Based Robot Pose and Joint Angle Estimation through Embedding Predictive Pre-Training</a></td>
<td nowrap>RoboPEPP uses embedding predictive pre-training to estimate robot poses and joint angles from vision.</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>generalist VLA / general-purpose VLA</td>
<td nowrap>embedding predictive pre-training</td>
<td nowrap>robot pose/joint estimation pretraining, not generalist VLA</td>
<td nowrap>-</td>
<td nowrap>Visual robot-pose and joint estimation.</td>
<td nowrap><a href="https://arxiv.org/abs/2411.17662">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2504.06961">Two by Two: Learning Multi-Task Pairwise Objects Assembly for Generalizable Robot Manipulation</a></td>
<td nowrap>2BY2 builds a dataset of everyday paired-object assembly and uses two-step SE(3) pose estimation to complete multi-task assembly.</td>
<td nowrap>-</td>
<td nowrap>SE(3) pose</td>
<td nowrap>generalist VLA / general-purpose VLA</td>
<td nowrap>two-step SE(3) pose estimation with equivariant features</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Addresses the fact that existing assembly datasets skew toward geometric fragments/industrial parts and do not cover functional relationships among everyday objects.</td>
<td nowrap><a href="https://arxiv.org/abs/2504.06961">paper</a></td>
<td nowrap><a href="https://tea-lab.github.io/TwoByTwo/">project</a></td>
<td nowrap><a href="https://github.com/TEA-Lab/TwoByTWo">code</a></td>
<td nowrap>2BY2 dataset</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.11269">Prof. Robot: Differentiable Robot Rendering Without Static and Self-Collisions</a></td>
<td nowrap>Prof. Robot provides differentiable robot rendering that avoids static and self-collisions for robot vision/geometric learning.</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>generalist VLA / general-purpose VLA</td>
<td nowrap>collision-free differentiable robot rendering</td>
<td nowrap>differentiable rendering/tooling, not VLA</td>
<td nowrap>-</td>
<td nowrap>Differentiable robot rendering.</td>
<td nowrap><a href="https://arxiv.org/abs/2503.11269">paper</a></td>
<td nowrap><a href="https://www.qrcat.cn/prof-robot/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
</tbody>
</table>

#### action representation

Total: 18 papers.

<table>
<thead>
<tr>
<th nowrap>Venue/Year</th>
<th nowrap>Paper/Method</th>
<th nowrap>Abstract</th>
<th nowrap>Base VLA</th>
<th nowrap>Action</th>
<th nowrap>Training/Feedback</th>
<th nowrap>Algorithm</th>
<th nowrap>Policy/Type</th>
<th nowrap>Sim/Real</th>
<th nowrap>Paper Task/Goal</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>Source</th>
<th nowrap>Survey Note</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=y5CaJb17Fn">villa-X: Enhancing Latent Action Modeling in Vision-Language-Action Models</a></td>
<td nowrap>villa-X learns and uses latent actions as motion abstractions in VLA pretraining, enabling zero-shot generation of latent action plans.</td>
<td nowrap>ViLLA/villa-X</td>
<td nowrap>latent action</td>
<td nowrap>action representation / action representation/tokenization</td>
<td nowrap>latent action modeling for VLA pretraining</td>
<td nowrap>Vision-Language-Latent-Action</td>
<td nowrap>SIMPLER + two real setups</td>
<td nowrap>Latent-action pretraining.</td>
<td nowrap><a href="https://openreview.net/forum?id=y5CaJb17Fn">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN, WAM</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=IZHk6BXBST">Rodrigues Network for Learning Robot Actions</a></td>
<td nowrap>RodriNet injects kinematic structural priors into the action network through a learnable Neural Rodrigues Operator.</td>
<td nowrap>-</td>
<td nowrap>kinematics-aware action representation</td>
<td nowrap>action representation / action representation/tokenization</td>
<td nowrap>Neural Rodrigues Operator + RodriNet</td>
<td nowrap>action network architecture</td>
<td nowrap>synthetic + imitation benchmarks + hand reconstruction</td>
<td nowrap>Kinematic structure modeling for robot actions.</td>
<td nowrap><a href="https://openreview.net/forum?id=IZHk6BXBST">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38937">Actor-Critic for Continuous Action Chunks: A Reinforcement Learning Framework for Long-Horizon Robotic Manipulation with Sparse Reward</a></td>
<td nowrap>AC3 directly learns continuous action chunks with actor-critic and stabilizes training through asymmetric updates on successful trajectories and in-chunk n-step returns.</td>
<td nowrap>-</td>
<td nowrap>continuous action chunks</td>
<td nowrap>RL / sparse reward</td>
<td nowrap>AC3</td>
<td nowrap>actor-critic chunk policy</td>
<td nowrap>BiGym + RLBench</td>
<td nowrap>Sparse-reward long-horizon continuous action-chunk learning.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38937">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN, EAI-Safety, RL-VLA</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/60681">DyGRO-VLA: Cross-Task Scaling of Vision-Language-Action Models via Dynamic Grouped Residual Optimization</a></td>
<td nowrap>DyGRO-VLA first learns cross-task latent representations, then uses dynamic grouping RL residuals to optimize multi-task VLAs.</td>
<td nowrap>DyGRO-VLA</td>
<td nowrap>residual policy optimization</td>
<td nowrap>RL/online fine-tuning</td>
<td nowrap>Dynamic Grouped Residual Optimization</td>
<td nowrap>cross-task RL-optimized VLA</td>
<td nowrap>LIBERO/RoboTwin2 + Real</td>
<td nowrap>Cross-task VLA RL optimization.</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/60681">paper</a></td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/60681">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61232">LARA: Latent Action Representation Alignment for Vision-Language-Action Models</a></td>
<td nowrap>LARA jointly optimizes a latent action model and a VLA so human-video latent actions better align with real action trajectories.</td>
<td nowrap>LARA plug-in</td>
<td nowrap>latent action representation</td>
<td nowrap>VLA / Action Representation/Tokenization</td>
<td nowrap>LAM-VLA representation alignment</td>
<td nowrap>pre/post-training enhancement</td>
<td nowrap>3 sim + 1 real benchmark</td>
<td nowrap>Latent-action alignment.</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61232">paper</a></td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61232">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62908">From Noise to Intent: Anchoring Generative VLA Policies with Residual Bridges</a></td>
<td nowrap>ResVLA changes generated actions from noise generation to intent-anchored residual refinement, separating low-frequency intent from high-frequency local dynamics.</td>
<td nowrap>ResVLA</td>
<td nowrap>Diffusion / residual bridge</td>
<td nowrap>VLA / Action Representation/Tokenization</td>
<td nowrap>low-frequency intent anchor + high-frequency residual diffusion bridge</td>
<td nowrap>generative VLA policy</td>
<td nowrap>LIBERO/LIBERO-Plus</td>
<td nowrap>Generative action-decoding stability.</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62908">paper</a></td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62908">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/65967">Demystifying Action Space Design for Robotic Manipulation Policies</a></td>
<td nowrap>This paper uses 13k+ real rollouts and 500+ models to systematically analyze the effects of absolute/incremental and joint/task-space action designs.</td>
<td nowrap>-</td>
<td nowrap>delta actions preferred</td>
<td nowrap>action representation / action representation/tokenization</td>
<td nowrap>large-scale action-space empirical study</td>
<td nowrap>action-space design study</td>
<td nowrap>Real bimanual robot</td>
<td nowrap>Action-space design principles.</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/65967">paper</a></td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/65967">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66520">FocalPolicy: Frequency-Optimized Chunking and Locally Anchored Flow Matching for Coherent Visuomotor Policy</a></td>
<td nowrap>FocalPolicy uses frequency-domain optimization of chunking and locally anchored flow matching to improve coherence across long-horizon action chunks.</td>
<td nowrap>visuomotor policy</td>
<td nowrap>Diffusion / Flow action chunks</td>
<td nowrap>flow matching / diffusion/flow policy</td>
<td nowrap>Frequency-Optimized Chunking + Locally Anchored Flow Matching</td>
<td nowrap>flow-matching visuomotor policy</td>
<td nowrap>-</td>
<td nowrap>Coherence across action chunks.</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66520">paper</a></td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66520">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62176">GeoMoLa: Geometry-Aware Motion Latents for Learning Robust Manipulation Policies</a></td>
<td nowrap>GeoMoLa learns discrete motion latent codes by predicting 4D geometric changes in point clouds during manipulation.</td>
<td nowrap>GeoMoLa</td>
<td nowrap>discrete motion latent codes</td>
<td nowrap>action representation / action representation/tokenization</td>
<td nowrap>geometry-aware point-cloud evolution objective</td>
<td nowrap>motion latent policy</td>
<td nowrap>benchmarks + Real</td>
<td nowrap>Geometry-aware action latents.</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62176">paper</a></td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62176">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2604.04161">Adaptive Action Chunking at Inference-time for Vision-Language-Action Models</a></td>
<td nowrap>AAC uses action entropy at inference time to dynamically select action-chunk length, balancing reactivity and continuity.</td>
<td nowrap>generic VLA</td>
<td nowrap>adaptive action chunks</td>
<td nowrap>VLA / Action Representation/Tokenization</td>
<td nowrap>action entropy based AAC</td>
<td nowrap>inference-time adaptation</td>
<td nowrap>Sim + Real</td>
<td nowrap>Adaptive action chunking at inference time.</td>
<td nowrap><a href="https://arxiv.org/abs/2604.04161">paper</a></td>
<td nowrap><a href="https://lance-lot.github.io/adaptive-chunking.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2603.10158">Cross-Hand Latent Representation for Vision-Language-Action Models</a></td>
<td nowrap>XL-VLA/DexLatent learns latent representations across different dexterous hands, allowing a single policy to transfer across hand morphologies.</td>
<td nowrap>XL-VLA / DexLatent</td>
<td nowrap>cross-hand latent representation</td>
<td nowrap>VLA / Action Representation/Tokenization</td>
<td nowrap>DexLatent</td>
<td nowrap>cross-embodiment dexterous VLA</td>
<td nowrap>-</td>
<td nowrap>Addresses different action spaces across multi-fingered dexterous hands and the difficulty of cross-hand policy transfer.</td>
<td nowrap><a href="https://arxiv.org/abs/2603.10158">paper</a></td>
<td nowrap><a href="https://xl-vla.github.io/">project</a></td>
<td nowrap><a href="https://github.com/EmptyBlueBox/DexLatent">code</a></td>
<td nowrap>-</td>
<td nowrap>Efficient-VLA</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.16685">Compliant Residual DAgger: Improving Real-World Contact-Rich Manipulation with Human Corrections</a></td>
<td nowrap>CR-DAgger improves contact-rich manipulation from human delta corrections through a compliant intervention interface and a force-feedback residual policy.</td>
<td nowrap>-</td>
<td nowrap>delta action corrections / residual policy</td>
<td nowrap>DAgger / human corrections</td>
<td nowrap>Compliant Residual DAgger</td>
<td nowrap>human-in-the-loop residual policy</td>
<td nowrap>Real</td>
<td nowrap>Addresses the difficulty of collecting DAgger correction data and stabilizing policy updates in real contact-rich manipulation.</td>
<td nowrap><a href="https://arxiv.org/abs/2506.16685">paper</a></td>
<td nowrap><a href="https://compliant-residual-dagger.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2510.25138">Learning Spatial-Aware Manipulation Ordering</a></td>
<td nowrap>OrderMind learns manipulation priority for each object in cluttered scenes directly from spatial context.</td>
<td nowrap>OrderMind</td>
<td nowrap>manipulation order priorities</td>
<td nowrap>VLA / Action Representation/Tokenization</td>
<td nowrap>spatial graph encoder + temporal priority structuring</td>
<td nowrap>ordering policy</td>
<td nowrap>benchmark + Real</td>
<td nowrap>Addresses collisions or occlusions caused by incorrect manipulation order in cluttered environments.</td>
<td nowrap><a href="https://arxiv.org/abs/2510.25138">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/yyxssm/OrderMind">code</a></td>
<td nowrap>Manipulation Ordering Benchmark</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2509.15607">PRIMT: Preference-based Reinforcement Learning with Multimodal Feedback and Trajectory Synthesis from Foundation Models</a></td>
<td nowrap>PRIMT uses LLM/VLM multimodal synthetic preference feedback and trajectory synthesis to reduce PbRL dependence on human feedback.</td>
<td nowrap>-</td>
<td nowrap>RL policy actions</td>
<td nowrap>preference-based RL / multimodal synthetic feedback</td>
<td nowrap>PRIMT + neuro-symbolic fusion + trajectory synthesis</td>
<td nowrap>PbRL framework</td>
<td nowrap>2 locomotion + 6 manipulation benchmarks</td>
<td nowrap>Addresses heavy human feedback, query ambiguity, and difficult credit assignment in preference RL.</td>
<td nowrap><a href="https://arxiv.org/abs/2509.15607">paper</a></td>
<td nowrap><a href="https://primt25.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2502.01218">Provable Ordering and Continuity in Vision-Language Pretraining for Generalizable Embodied Agents</a></td>
<td nowrap>AcTOL learns ordered continuous vision-language representations using inter-frame semantic ordering and local Brownian-bridge continuity constraints.</td>
<td nowrap>AcTOL features</td>
<td nowrap>pretraining representation</td>
<td nowrap>VLA / Action Representation/Tokenization</td>
<td nowrap>Action Temporal Coherence Learning</td>
<td nowrap>VL pretraining for embodied agents</td>
<td nowrap>-</td>
<td nowrap>Ordered continuous vision-language pretraining.</td>
<td nowrap><a href="https://arxiv.org/abs/2502.01218">paper</a></td>
<td nowrap><a href="https://actol-pretrain.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2508.05941">Latent Policy Barrier: Learning Robust Visuomotor Policies by Staying In-Distribution</a></td>
<td nowrap>LPB uses expert demonstration latent embeddings as implicit safety boundaries, optimizing future latents at inference time to stay within the expert distribution.</td>
<td nowrap>LPB</td>
<td nowrap>Diffusion policy + latent barrier correction</td>
<td nowrap>action representation / action representation/tokenization</td>
<td nowrap>Latent Policy Barrier + dynamics model</td>
<td nowrap>robust visuomotor policy</td>
<td nowrap>Sim + Real</td>
<td nowrap>Addresses behavioral-cloning visuomotor policies gradually drifting away from expert trajectories due to covariate shift.</td>
<td nowrap><a href="https://arxiv.org/abs/2508.05941">paper</a></td>
<td nowrap><a href="https://project-latentpolicybarrier.github.io/">project</a></td>
<td nowrap><a href="https://github.com/zhanyisun/lpb">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2412.04445">Moto: Latent Motion Token as the Bridging Language for Robot Manipulation</a></td>
<td nowrap>Moto converts videos into latent motion tokens and uses Moto-GPT autoregressive pretraining to transfer video motion knowledge to robot control.</td>
<td nowrap>Moto-GPT</td>
<td nowrap>latent motion tokens</td>
<td nowrap>VLA / action tokenization / action representation/tokenization</td>
<td nowrap>Latent Motion Tokenizer + Moto-GPT autoregression</td>
<td nowrap>video-pretrained motion-token policy</td>
<td nowrap>-</td>
<td nowrap>Addresses the lack of action-labeled robot data and the difficulty of directly using motion knowledge from video data.</td>
<td nowrap><a href="https://arxiv.org/abs/2412.04445">paper</a></td>
<td nowrap><a href="https://chenyi99.github.io/moto/">project</a></td>
<td nowrap><a href="https://github.com/TencentARC/Moto">code</a></td>
<td nowrap><a href="https://huggingface.co/TencentARC/Moto">hf</a></td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2411.14519">Tra-MoE: Learning Trajectory Prediction Model from Multiple Domains for Adaptive Policy Conditioning</a></td>
<td nowrap>Tra-MoE learns an MoE prediction model from multi-domain trajectories and adaptively adjusts policy conditioning with predicted trajectories.</td>
<td nowrap>Tra-MoE</td>
<td nowrap>trajectory prediction / policy conditioning</td>
<td nowrap>action representation / action representation/tokenization</td>
<td nowrap>Mixture-of-Experts trajectory model</td>
<td nowrap>adaptive policy conditioning</td>
<td nowrap>-</td>
<td nowrap>Multi-domain trajectory prediction and policy conditioning.</td>
<td nowrap><a href="https://arxiv.org/abs/2411.14519">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/MCG-NJU/Tra-MoE">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
</tbody>
</table>

#### diffusion/flow policy

Total: 63 papers.

<table>
<thead>
<tr>
<th nowrap>Venue/Year</th>
<th nowrap>Paper/Method</th>
<th nowrap>Abstract</th>
<th nowrap>Base VLA</th>
<th nowrap>Action</th>
<th nowrap>Training/Feedback</th>
<th nowrap>Algorithm</th>
<th nowrap>Policy/Type</th>
<th nowrap>Sim/Real</th>
<th nowrap>Paper Task/Goal</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>Source</th>
<th nowrap>Survey Note</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=H1KDMNOKQn">HybridVLA: Collaborative Diffusion and Autoregression in a Unified Vision-Language-Action Model</a></td>
<td nowrap>-</td>
<td nowrap>No specific base VLA specified.</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=H1KDMNOKQn">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=UvQOcw2oCD">Unified Diffusion VLA: Vision-Language-Action Model via Joint Discrete Denosing Diffusion Process</a></td>
<td nowrap>-</td>
<td nowrap>No specific base VLA specified.</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=UvQOcw2oCD">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>WAM</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=1vXMfIYFZp">Master Skill Learning with Policy-Grounded Synergy of LLM-based Reward Shaping and Exploring</a></td>
<td nowrap>Master Skill Learning uses reinforcement learning, preference feedback, or post-training signals to improve robot policies.</td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>RL / offline RL</td>
<td nowrap>RL fine-tuning / policy optimization</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=1vXMfIYFZp">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=2RIqqNqALN">When would Vision-Proprioception Policies Fail in Robotic Manipulation?</a></td>
<td nowrap>-</td>
<td nowrap>No specific base VLA specified.</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=2RIqqNqALN">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=AmczI1k3Yk">Capturing Visual Environment Structure Correlates with Control Performance</a></td>
<td nowrap>Capturing Visual Environment Structure Correlates connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>3D/spatial representation learning</td>
<td nowrap>3D-grounded policy/perception</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=AmczI1k3Yk">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=BTe5VLBjPg">VITA: Vision-to-Action Flow Matching Policy</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>Flow matching policy</td>
<td nowrap>Flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=BTe5VLBjPg">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=BvirMuKWV1">When a Robot is More Capable than a Human: Learning from Constrained Demonstrators</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=BvirMuKWV1">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=FqDmvMZish">Autonomous Functional Play with Correspondence-Driven Trajectory Warping</a></td>
<td nowrap>Autonomous Functional Play connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>3D keypoint grounding</td>
<td nowrap>3D-grounded policy/perception</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=FqDmvMZish">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=IaGf8Eh5Uo">Reference Grounded Skill Discovery</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=IaGf8Eh5Uo">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=KFu4p3pd11">Masked Generative Policy for Robotic Control</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=KFu4p3pd11">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=OeDwYtp8n1">Learning Video Generation for Robotic Manipulation with Collaborative Trajectory Control</a></td>
<td nowrap>Learning Video Generation for Robotic Manipulation uses video generation/prediction or future rendering to learn robot interaction dynamics.</td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=OeDwYtp8n1">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=P9PVdWyM3U">Policy Contrastive Decoding for Robotic Foundation Models</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=P9PVdWyM3U">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=PL0tJOfm7I">Demystifying Robot Diffusion Policies: Action Memorization and a Simple Lookup Table Alternative</a></td>
<td nowrap>-</td>
<td nowrap>No specific base VLA specified.</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=PL0tJOfm7I">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=Q1CP0iAmOb">H$^3$DP: Triply‑Hierarchical Diffusion Policy for Visuomotor Learning</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>5 simulation benchmarks + real Galaxea R1</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=Q1CP0iAmOb">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=TnLFRhLuZ6">Compose Your Policies! Improving Diffusion-based or Flow-based Robot Policies via Test-time Distribution-level Composition</a></td>
<td nowrap>-</td>
<td nowrap>No specific base VLA specified.</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>GPC; test-time distribution-level policy composition</td>
<td nowrap>Flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=TnLFRhLuZ6">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=VSWjHIveqZ">Abstracting Robot Manipulation Skills via Mixture-of-Experts Diffusion Policies</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=VSWjHIveqZ">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=WVliGyFwZv">Accelerated co-design of robots through morphological pretraining</a></td>
<td nowrap>Accelerated co-design of robots through morphological pretraining uses reinforcement learning, preference feedback, or post-training signals to improve robot policies.</td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>RL / offline RL</td>
<td nowrap>RL fine-tuning / policy optimization</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=WVliGyFwZv">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=aoorNQFpM6">VER: Vision Expert Transformer for Robot Learning via Foundation Distillation and Dynamic Routing</a></td>
<td nowrap>VER provides open-source tools, data formats, or benchmark interfaces for end-to-end robot learning.</td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=aoorNQFpM6">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Awesome-VLA</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=d08yOXs1Dl">SpikePingpong: Spike Vision-based Fast-Slow Pingpong Robot System</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=d08yOXs1Dl">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=dQ6d5bgXtM">Translating Flow to Policy via Hindsight Online Imitation</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy / RL/online fine-tuning</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=dQ6d5bgXtM">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=eWe8zqGvs5">Cortical Policy: A Dual-Stream View Transformer for Robotic Manipulation</a></td>
<td nowrap>Cortical Policy connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>3D keypoint grounding</td>
<td nowrap>3D-grounded policy/perception</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=eWe8zqGvs5">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=iKJbmx1iuQ">Contractive Diffusion Policies</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=iKJbmx1iuQ">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=kIYNtxE13h">Scalable Exploration for High-Dimensional Continuous Control via Value-Guided Flow</a></td>
<td nowrap>Scalable Exploration for High-Dimensional Continuous Control uses reinforcement learning, preference feedback, or post-training signals to improve robot policies.</td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>RL / offline RL</td>
<td nowrap>RL fine-tuning / policy optimization</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=kIYNtxE13h">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=w3Ik8HUyTT">ViPRA: Video Prediction for Robot Actions</a></td>
<td nowrap>ViPRA uses video generation/prediction or future rendering to learn robot interaction dynamics.</td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>Generative action modeling</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=w3Ik8HUyTT">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=AcTsKglDdh">DataMIL: Selecting Data for Robot Imitation Learning with Datamodels</a></td>
<td nowrap>DataMIL provides open-source tools, data formats, or benchmark interfaces for end-to-end robot learning.</td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=AcTsKglDdh">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=COrUdVuInH">MIMIC: Mask-Injected Manipulation Video Generation with Interaction Control</a></td>
<td nowrap>MIMIC uses video generation/prediction or future rendering to learn robot interaction dynamics.</td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=COrUdVuInH">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>WAM</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=CiZMMAFQR3">LeRobot: An Open-Source Library for End-to-End Robot Learning</a></td>
<td nowrap>LeRobot provides open-source tools, data formats, or benchmark interfaces for end-to-end robot learning.</td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>simulation + real hardware</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=CiZMMAFQR3">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN, Awesome-VLA, Efficient-VLA, Robot-Learning, WAM</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38881">ManiLong-Shot: Interaction-Aware One-Shot Imitation Learning for Long-Horizon Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38881">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38889">Learning Diffusion Policy from Primitive Skills for Robot Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38889">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38912">Intention-Aware Diffusion Model for Pedestrian Trajectory Prediction</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38912">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Humanoid-RL</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38919">MP1: MeanFlow Tames Policy Learning in 1-step for Robotic Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>Flow matching policy</td>
<td nowrap>Flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38919">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38934">ForeDiffusion: Foresight-Conditioned Diffusion Policy via Future View Construction for Robot Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38934">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38944">Balancing Signal and Variance: Adaptive Offline RL Post-Training for VLA Flow Models</a></td>
<td nowrap>Balancing Signal and Variance uses reinforcement learning, preference feedback, or post-training signals to improve robot policies.</td>
<td nowrap>π₀</td>
<td nowrap>Flow</td>
<td nowrap>diffusion/flow policy / RL/online fine-tuning / Reward D</td>
<td nowrap>ARFM</td>
<td nowrap>Off-Policy / MF</td>
<td nowrap>Sim ✓ / Real ✓</td>
<td nowrap>-</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38944">paper</a> / <a href="https://arxiv.org/pdf/2509.04063">paper</a> / <a href="https://arxiv.org/abs/2509.04063">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Efficient-VLA, RL-VLA</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38950">Bridging Scale Discrepancies in Robotic Control via Language-Based Action Representations</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38950">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38959">D²PPO: Diffusion Policy Policy Optimization with Dispersive Loss</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>PPO</td>
<td nowrap>RL fine-tuning / policy optimization</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38959">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62902">Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies</a></td>
<td nowrap>-</td>
<td nowrap>No specific base VLA specified.</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>VLA / diffusion policy / diffusion/flow policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62902">paper</a> / <a href="https://arxiv.org/abs/2508.20072">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN, Efficient-VLA</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61717">STEP: Warm-Started Visuomotor Policies with Spatiotemporal Consistency Prediction</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61717">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>HCP-Survey, EAI-VLA-VLN, Humanoid-RL</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61049">Learning Human-Robot Collaboration via Heterogeneous-Agent Lyapunov Policy Optimization</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Sim/Benchmark</td>
<td nowrap>-</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61049">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2511.15605">SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models</a></td>
<td nowrap>SRPO uses reinforcement learning, preference feedback, or post-training signals to improve robot policies.</td>
<td nowrap>OpenVLA* / π₀ / π₀-Fast</td>
<td nowrap>AR / Flow</td>
<td nowrap>VLA / RL/online fine-tuning / Reward D</td>
<td nowrap>SRPO</td>
<td nowrap>Hybrid / MF (MB-Reward but MF-RL)</td>
<td nowrap>Sim ✓(MT) / Real ✓(MT)</td>
<td nowrap>-</td>
<td nowrap><a href="https://arxiv.org/abs/2511.15605">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>WAM, RL-VLA</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2507.01961">AC-DiT: Adaptive Coordination Diffusion Transformer for Mobile Manipulation</a></td>
<td nowrap>AC-DiT connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>VLA / diffusion policy / diffusion transformer / diffusion/flow policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://arxiv.org/abs/2507.01961">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2510.20406">PointMapPolicy: Structured Point Cloud Processing for Multi-Modal Imitation Learning</a></td>
<td nowrap>PointMapPolicy connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>VLA / diffusion/flow policy</td>
<td nowrap>PPO</td>
<td nowrap>Diffusion policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://arxiv.org/abs/2510.20406">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2509.00117">Emerging Risks from Embodied AI Require Urgent Policy Action</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-Safety</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.07127">Human-assisted Robotic Policy Refinement via Action Preference Optimization</a></td>
<td nowrap>Human-assisted Robotic Policy Refinement uses reinforcement learning, preference feedback, or post-training signals to improve robot policies.</td>
<td nowrap>No specific base VLA specified.</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>Preference optimization</td>
<td nowrap>RL fine-tuning / policy optimization</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://arxiv.org/abs/2506.07127">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2512.00085">Hyper-GoalNet: Goal-Conditioned Manipulation Policy Learning with HyperNetworks</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://arxiv.org/abs/2512.00085">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2505.22094">ReinFlow: Fine-tuning Flow Matching Policy with Online Reinforcement Learning</a></td>
<td nowrap>ReinFlow uses reinforcement learning, preference feedback, or post-training signals to improve robot policies.</td>
<td nowrap>-</td>
<td nowrap>AR / Flow</td>
<td nowrap>flow matching / RL / RL/online fine-tuning</td>
<td nowrap>Flow matching policy</td>
<td nowrap>RL fine-tuning / policy optimization</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://arxiv.org/abs/2505.22094">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>RL-VLA</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2505.13431">A Practical Guide for Incorporating Symmetry in Diffusion Policy</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion policy / diffusion/flow policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://arxiv.org/abs/2505.13431">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2509.25822">Act to See, See to Act: Diffusion-Driven Perception-Action Interplay for Adaptive Policies</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion policy / diffusion/flow policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://arxiv.org/abs/2509.25822">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2511.20906">DASIP: Dynamic Test-Time Compute Scaling for Robot Control with Stochastic Interpolant Policies</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>Flow matching policy</td>
<td nowrap>Flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://arxiv.org/abs/2511.20906">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.13922">DynaGuide: Steering Diffusion Polices with Active Dynamic Guidance</a></td>
<td nowrap>DynaGuide uses reinforcement learning, preference feedback, or post-training signals to improve robot policies.</td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion policy / diffusion/flow policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>RL fine-tuning / policy optimization</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://arxiv.org/abs/2506.13922">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.19757">Dita: Scaling Diffusion Transformer for Generalist Vision-Language-Action Policy</a></td>
<td nowrap>-</td>
<td nowrap>No specific base VLA specified.</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>VLA / diffusion policy / diffusion transformer / diffusion/flow policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>LIBERO + SimplerEnv + real Franka</td>
<td nowrap>-</td>
<td nowrap><a href="https://arxiv.org/abs/2503.19757">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/1571">SD2Actor: Continuous State Decomposition via Diffusion Embeddings for Robotic Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>VLA / diffusion policy / diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/1571">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2507.06224">EC-Flow: Enabling Versatile Robotic Manipulation from Action-Unlabeled Videos via Embodiment-Centric Flow</a></td>
<td nowrap>EC-Flow provides open-source tools, data formats, or benchmark interfaces for end-to-end robot learning.</td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>flow matching / diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Sim/Benchmark</td>
<td nowrap>-</td>
<td nowrap><a href="https://arxiv.org/abs/2507.06224">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.13217">Dense Policy: Bidirectional Autoregressive Learning of Actions</a></td>
<td nowrap>Dense Policy uses action tokens, mask generation, or autoregressive modeling to improve robot control.</td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>autoregressive policy / diffusion/flow policy</td>
<td nowrap>Generative action modeling</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Addresses the efficiency and consistency of robot action representation and long-horizon action prediction.</td>
<td nowrap><a href="https://arxiv.org/abs/2503.13217">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2507.06710">Spatial-Temporal Aware Visuomotor Diffusion Policy Learning</a></td>
<td nowrap>Spatial-Temporal Aware Visuomotor Diffusion Policy Learning connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>diffusion policy / diffusion/flow policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://arxiv.org/abs/2507.06710">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>HCP-Survey, EAI-VLA-VLN, Awesome-VLA, EAI-Safety</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2507.04331">Wavelet Policy: Lifting Scheme for Policy Learning in Long-Horizon Tasks</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://arxiv.org/abs/2507.04331">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICML 2025</td>
<td nowrap><a href="https://arxiv.org/pdf/2502.01800">Flow-based Domain Randomization for Learning and Sequencing Robotic Skills</a></td>
<td nowrap>Flow-based Domain Randomization uses reinforcement learning, preference feedback, or post-training signals to improve robot policies.</td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>flow matching / diffusion/flow policy</td>
<td nowrap>Flow matching policy</td>
<td nowrap>RL fine-tuning / policy optimization</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://arxiv.org/pdf/2502.01800">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN, Efficient-VLA, EAI-ROS</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICML 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.01885">Learning Policy Committees for Effective Personalization in MDPs with Diverse Tasks</a></td>
<td nowrap>Learning Policy Committees for Effective Personalization in MDPs uses reinforcement learning, preference feedback, or post-training signals to improve robot policies.</td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>diffusion/flow policy</td>
<td nowrap>RL / offline RL</td>
<td nowrap>RL fine-tuning / policy optimization</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://arxiv.org/abs/2503.01885">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2411.18623">Lift3D Foundation Policy: Lifting 2D Large-Scale Pretrained Models for Robust 3D Robotic Manipulation</a></td>
<td nowrap>Lift3D Foundation Policy studies VLA robustness under multimodal perturbations, adversarial inputs, or distribution shifts.</td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>3D representation / diffusion/flow policy</td>
<td nowrap>Generative action modeling</td>
<td nowrap>3D-grounded policy/perception</td>
<td nowrap>simulation benchmarks + real FR3</td>
<td nowrap>-</td>
<td nowrap><a href="https://arxiv.org/abs/2411.18623">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://openaccess.thecvf.com/content/CVPR2025/papers/Tian_PDFactor_Learning_Tri-Perspective_View_Policy_Diffusion_Field_for_Multi-Task_Robotic_CVPR_2025_paper.pdf">PDFactor: Learning Tri-Perspective View Policy Diffusion Field for Multi-Task Robotic Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>diffusion policy / diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://openaccess.thecvf.com/content/CVPR2025/papers/Tian_PDFactor_Learning_Tri-Perspective_View_Policy_Diffusion_Field_for_Multi-Task_Robotic_CVPR_2025_paper.pdf">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.16201">FlowRAM: Grounding Flow Matching Policy with Region-Aware Mamba Framework for Robotic Manipulation</a></td>
<td nowrap>FlowRAM connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>flow matching / diffusion/flow policy</td>
<td nowrap>Flow matching policy</td>
<td nowrap>Flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://arxiv.org/abs/2506.16201">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Efficient-VLA</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2411.18369">G3Flow: Generative 3D Semantic Flow for Pose-aware and Generalizable Object Manipulation</a></td>
<td nowrap>G3Flow connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>flow matching / 3D representation / diffusion/flow policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://arxiv.org/abs/2411.18369">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>RoboTwin_Benchmark tasks</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2412.03142">AffordDP: Generalizable Diffusion Policy with Transferable Affordance</a></td>
<td nowrap>AffordDP connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion policy / affordance / diffusion/flow policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>Sim + Real</td>
<td nowrap>-</td>
<td nowrap><a href="https://arxiv.org/abs/2412.03142">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2505.13091">Touch2Shape: Touch-Conditioned 3D Diffusion for Shape Exploration and Reconstruction</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>diffusion policy / 3D representation / diffusion/flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://arxiv.org/abs/2505.13091">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
</tbody>
</table>

#### 3D grounding

Total: 30 papers.

<table>
<thead>
<tr>
<th nowrap>Venue/Year</th>
<th nowrap>Paper/Method</th>
<th nowrap>Abstract</th>
<th nowrap>Base VLA</th>
<th nowrap>Action</th>
<th nowrap>Training/Feedback</th>
<th nowrap>Algorithm</th>
<th nowrap>Policy/Type</th>
<th nowrap>Sim/Real</th>
<th nowrap>Paper Task/Goal</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>Source</th>
<th nowrap>Survey Note</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>IROS 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2606.26800">SSI-Policy: Learning Structured Scene Interfaces for Vision-Language Robotic Manipulation</a></td>
<td nowrap>SSI-Policy 用结构化场景接口连接视觉语言推理和低数据机器人操作策略学习。</td>
<td nowrap>vision-language policy</td>
<td nowrap>continuous action</td>
<td nowrap>3D grounding / structured scene interface</td>
<td nowrap>scene-interface policy learning</td>
<td nowrap>structured VLA policy</td>
<td nowrap>Real robot manipulation</td>
<td nowrap>用结构化场景表示提升低数据机器人操作泛化。</td>
<td nowrap><a href="https://arxiv.org/abs/2606.26800">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>ICRA/IROS</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICRA 2025</td>
<td nowrap><a href="https://kalie-vlm.github.io/">KALIE: Fine-Tuning Vision-Language Models for Open-World Manipulation without Robot Data</a></td>
<td nowrap>KALIE 用 VLM 预测语言条件点式 affordance，通过合成数据支持开放世界机器人操作。</td>
<td nowrap>VLM</td>
<td nowrap>affordance point</td>
<td nowrap>3D grounding / affordance grounding</td>
<td nowrap>synthetic data fine-tuning</td>
<td nowrap>affordance-conditioned manipulation</td>
<td nowrap>Real robot manipulation</td>
<td nowrap>不用真实机器人数据学习语言条件 affordance。</td>
<td nowrap><a href="https://kalie-vlm.github.io/">paper</a></td>
<td nowrap><a href="https://kalie-vlm.github.io/">project</a></td>
<td nowrap><a href="https://github.com/gractang/kalie">code</a></td>
<td nowrap>-</td>
<td nowrap>ICRA/IROS</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=7M6ryCABIc">PixelVLA: Advancing Pixel-level Understanding in Vision-Language-Action Model</a></td>
<td nowrap>PixelVLA connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td nowrap>No specific base VLA specified.</td>
<td nowrap>3D/spatial grounding</td>
<td nowrap>3D representation / 3D grounding</td>
<td nowrap>-</td>
<td nowrap>3D-grounded policy/perception</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=7M6ryCABIc">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=eKhOrQWAVJ">Spatially Guided Training for Vision-Language-Action Model</a></td>
<td nowrap>Spatially Guided Training connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td nowrap>No specific base VLA specified.</td>
<td nowrap>3D/spatial grounding</td>
<td nowrap>3D representation / 3D grounding</td>
<td nowrap>3D/spatial representation learning</td>
<td nowrap>3D-grounded policy/perception</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=eKhOrQWAVJ">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=euMVC1DO4k">Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model</a></td>
<td nowrap>Spatial Forcing connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td nowrap>No specific base VLA specified.</td>
<td nowrap>3D/spatial grounding</td>
<td nowrap>3D representation / 3D grounding</td>
<td nowrap>3D/spatial representation learning</td>
<td nowrap>3D-grounded policy/perception</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=euMVC1DO4k">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=fzmittHfq3">From Spatial to Actions: Grounding Vision-Language-Action Model in Spatial Foundation Priors</a></td>
<td nowrap>From Spatial to Actions connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td nowrap>No specific base VLA specified.</td>
<td nowrap>3D/spatial grounding</td>
<td nowrap>3D representation / 3D grounding</td>
<td nowrap>3D/spatial representation learning</td>
<td nowrap>3D-grounded policy/perception</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=fzmittHfq3">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=18gC6pZVVc">Geometry-aware 4D Video Generation for Robot Manipulation</a></td>
<td nowrap>Geometry-aware 4D Video Generation uses video generation/prediction or future rendering to learn robot interaction dynamics.</td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>3D representation / 3D grounding</td>
<td nowrap>3D/spatial representation learning</td>
<td nowrap>3D-grounded policy/perception</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=18gC6pZVVc">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>HCP-Survey, Awesome-EAI, Humanoid-RL, WAM</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=WXFfMLyB6y">Generalizable Coarse-to-Fine Robot Manipulation via Language-Aligned 3D Keypoints</a></td>
<td nowrap>Generalizable Coarse-to-Fine Robot Manipulation connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>3D representation / 3D grounding</td>
<td nowrap>3D keypoint grounding</td>
<td nowrap>3D-grounded policy/perception</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=WXFfMLyB6y">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=ggofj6tyr3">Geometry-aware Policy Imitation</a></td>
<td nowrap>Geometry-aware Policy Imitation connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>3D representation / 3D grounding</td>
<td nowrap>Diffusion policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=ggofj6tyr3">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>HCP-Survey, Awesome-EAI, Humanoid-RL, WAM</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=qXfRXfAHOK">PA3FF:Learning Part-Aware Dense 3D Feature Field For Generalizable Articulated Object Manipulation</a></td>
<td nowrap>PA3FF connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>3D representation / 3D grounding</td>
<td nowrap>Diffusion policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=qXfRXfAHOK">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=z8BN7KyaPl">RAVEN: End-to-end Equivariant Robot Learning with RGB Cameras</a></td>
<td nowrap>RAVEN connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>3D representation / 3D grounding</td>
<td nowrap>3D/spatial representation learning</td>
<td nowrap>3D-grounded policy/perception</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=z8BN7KyaPl">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=DE5ZJtR4bg">On the Generalization Capacities of MLLMs for Spatial Intelligence</a></td>
<td nowrap>On the Generalization Capacities of MLLMs connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td nowrap>-</td>
<td nowrap>3D/spatial grounding</td>
<td nowrap>3D representation / 3D grounding</td>
<td nowrap>3D/spatial representation learning</td>
<td nowrap>3D-grounded policy/perception</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=DE5ZJtR4bg">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38921">ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver</a></td>
<td nowrap>-</td>
<td nowrap>No specific base VLA specified.</td>
<td nowrap>3D/spatial grounding</td>
<td nowrap>3D representation / 3D grounding</td>
<td nowrap>-</td>
<td nowrap>3D-grounded policy/perception</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38921">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38939">Indoor Multi-View Radar Object Detection via 3D Bounding Box Diffusion</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>3D representation / diffusion/flow policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38939">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38946">RaLD: Generating High-Resolution 3D Radar Point Clouds with Latent Diffusion</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>AR / Diffusion / Flow</td>
<td nowrap>3D representation / diffusion/flow policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38946">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38947">Grounding Actions in Camera Space: Observation-Centric Vision-Language-Action Policy</a></td>
<td nowrap>-</td>
<td nowrap>No specific base VLA specified.</td>
<td nowrap>3D/spatial grounding</td>
<td nowrap>3D representation / 3D grounding</td>
<td nowrap>-</td>
<td nowrap>3D-grounded policy/perception</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38947">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2510.24261">DynaRend: Learning 3D Dynamics via Masked Future Rendering for Robotic Manipulation</a></td>
<td nowrap>DynaRend uses video generation/prediction or future rendering to learn robot interaction dynamics.</td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>3D representation / 3D grounding</td>
<td nowrap>Generative action modeling</td>
<td nowrap>3D-grounded policy/perception</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://arxiv.org/abs/2510.24261">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://neurips.cc/virtual/2025/loc/san-diego/poster/118141">Building 3D Representations and Generating Motions From a Single Image via Video-Generation</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>3D representation / 3D grounding</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://neurips.cc/virtual/2025/loc/san-diego/poster/118141">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2504.12636">A0: An Affordance-Aware Hierarchical Model for General Robotic Manipulation</a></td>
<td nowrap>A0 connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>VLA / affordance / 3D grounding</td>
<td nowrap>Flow matching policy</td>
<td nowrap>Flow policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://arxiv.org/abs/2504.12636">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2408.10123v1">Learning Precise Affordances from Egocentric Videos for Robotic Manipulation</a></td>
<td nowrap>Learning Precise Affordances from Egocentric Videos connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>affordance / 3D grounding</td>
<td nowrap>Affordance grounding</td>
<td nowrap>3D-grounded policy/perception</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://arxiv.org/abs/2408.10123v1">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2412.04380">EmbodiedOcc: Embodied 3D Occupancy Prediction for Vision-based Online Scene Understanding</a></td>
<td nowrap>EmbodiedOcc connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td nowrap>-</td>
<td nowrap>3D/spatial grounding</td>
<td nowrap>3D representation / RL/online fine-tuning</td>
<td nowrap>3D/spatial representation learning</td>
<td nowrap>3D-grounded policy/perception</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://arxiv.org/abs/2412.04380">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2504.08531">Embodied Image Captioning: Self-supervised Learning Agents for Spatially Coherent Image Descriptions</a></td>
<td nowrap>Embodied Image Captioning connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>3D grounding</td>
<td nowrap>3D/spatial representation learning</td>
<td nowrap>3D-grounded policy/perception</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://arxiv.org/abs/2504.08531">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICML 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.10745">Unifying 2D and 3D Vision-Language Understanding</a></td>
<td nowrap>Unifying 2D and 3D Vision-Language Understanding connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td nowrap>-</td>
<td nowrap>3D/spatial grounding</td>
<td nowrap>3D representation / 3D grounding</td>
<td nowrap>-</td>
<td nowrap>3D-grounded policy/perception</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://arxiv.org/abs/2503.10745">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICML 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2505.04119">GAPrompt: Geometry-Aware Point Cloud Prompt for 3D Vision Model</a></td>
<td nowrap>GAPrompt connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>3D representation / 3D grounding</td>
<td nowrap>3D/spatial representation learning</td>
<td nowrap>3D-grounded policy/perception</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://arxiv.org/abs/2505.04119">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2412.00174">SOLAMI: Social Vision-Language-Action Modeling for Immersive Interaction with 3D Autonomous Characters</a></td>
<td nowrap>SOLAMI connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td nowrap>No specific base VLA specified.</td>
<td nowrap>AR</td>
<td nowrap>VLA / 3D representation / 3D grounding</td>
<td nowrap>-</td>
<td nowrap>3D-grounded policy/perception</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://arxiv.org/abs/2412.00174">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2501.03841">OmniManip: Towards General Robotic Manipulation via Object-Centric Interaction Primitives as Spatial Constraints</a></td>
<td nowrap>OmniManip connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td nowrap>No specific base VLA specified.</td>
<td nowrap>AR</td>
<td nowrap>VLA / 3D grounding</td>
<td nowrap>Affordance grounding</td>
<td nowrap>3D-grounded policy/perception</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://arxiv.org/abs/2501.03841">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/pdf/2504.21530">RoboGround: Robot Manipulation with Grounded Vision-Language Priors</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA / 3D grounding</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2406.18158">3D-MVP: 3D Multiview Pretraining for Robotic Manipulation</a></td>
<td nowrap>3D-MVP connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td nowrap>-</td>
<td nowrap>3D/spatial grounding</td>
<td nowrap>3D representation / 3D grounding</td>
<td nowrap>Generative action modeling</td>
<td nowrap>3D-grounded policy/perception</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://arxiv.org/abs/2406.18158">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.07135">VidBot: Learning Generalizable 3D Actions from In-the-Wild 2D Human Videos for Zero-Shot Robotic Manipulation</a></td>
<td nowrap>VidBot connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>3D representation / 3D grounding</td>
<td nowrap>Diffusion policy</td>
<td nowrap>Diffusion policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://arxiv.org/abs/2503.07135">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2412.05507">AutoURDF: Unsupervised Robot Modeling from Point Cloud Frames Using Cluster Registration</a></td>
<td nowrap>AutoURDF connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td nowrap>-</td>
<td nowrap>3D/spatial grounding</td>
<td nowrap>3D grounding</td>
<td nowrap>3D/spatial representation learning</td>
<td nowrap>3D-grounded policy/perception</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://arxiv.org/abs/2412.05507">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
</tbody>
</table>

#### online/RL fine-tuning

Total: 13 papers.

<table>
<thead>
<tr>
<th nowrap>Venue/Year</th>
<th nowrap>Paper/Method</th>
<th nowrap>Abstract</th>
<th nowrap>Base VLA</th>
<th nowrap>Action</th>
<th nowrap>Training/Feedback</th>
<th nowrap>Algorithm</th>
<th nowrap>Policy/Type</th>
<th nowrap>Sim/Real</th>
<th nowrap>Paper Task/Goal</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>Source</th>
<th nowrap>Survey Note</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>IROS 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2503.05833">Refined Policy Distillation: From VLA Generalists to RL Experts</a></td>
<td nowrap>RPD 将 Octo/OpenVLA 等通用 VLA 通过 RL 蒸馏成任务专家策略。</td>
<td nowrap>Octo / OpenVLA</td>
<td nowrap>policy action</td>
<td nowrap>RL distillation / online fine-tuning</td>
<td nowrap>Refined Policy Distillation</td>
<td nowrap>RL expert policy</td>
<td nowrap>Sim + Real</td>
<td nowrap>把通用 VLA 迁移为更强的任务专家策略。</td>
<td nowrap><a href="https://arxiv.org/abs/2503.05833">paper</a></td>
<td nowrap><a href="https://refined-policy-distillation.github.io/">project</a></td>
<td nowrap><a href="https://github.com/Refined-Policy-Distillation/RPD">code</a></td>
<td nowrap><a href="https://huggingface.co/Juelg">hf</a></td>
<td nowrap>ICRA/IROS</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=ULTWUuGhC3">Interleave-VLA: Enhancing Robot Manipulation with Image-Text Interleaved Instructions</a></td>
<td nowrap>Interleave-VLA provides open-source tools, data formats, or benchmark interfaces for end-to-end robot learning.</td>
<td nowrap>No specific base VLA specified.</td>
<td nowrap>policy action</td>
<td nowrap>VLA / RL / Online Fine-tuning</td>
<td nowrap>-</td>
<td nowrap>RL fine-tuning / policy optimization</td>
<td nowrap>SIMPLER + VIMA-Bench + real FANUC</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=ULTWUuGhC3">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Interleaved X-Embodiment; 210k trajectories</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=eUGoqrZ6Ea">Self-Improving Vision-Language-Action Models with Data Generation via Residual RL</a></td>
<td nowrap>Self-Improving Vision-Language-Action Models with Data Generation uses reinforcement learning, preference feedback, or post-training signals to improve robot policies.</td>
<td nowrap>No specific base VLA specified.</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>VLA / RL / Online Fine-tuning</td>
<td nowrap>PLD residual RL + SFT distillation</td>
<td nowrap>Off-policy residual RL</td>
<td nowrap>LIBERO + SimplerEnv + real Franka/YAM</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=eUGoqrZ6Ea">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, EAI-Safety, WAM, RL-VLA</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=sFO9d6XSlf">Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting</a></td>
<td nowrap>Actions as Language provides open-source tools, data formats, or benchmark interfaces for end-to-end robot learning.</td>
<td nowrap>No specific base VLA specified.</td>
<td nowrap>policy action</td>
<td nowrap>VLA / RL / Online Fine-tuning</td>
<td nowrap>VLM2VLA; language action representation + LoRA</td>
<td nowrap>RL fine-tuning / policy optimization</td>
<td nowrap>800+ real robot experiments</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=sFO9d6XSlf">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=GrsoLVNy3Y">Cross-Embodiment Offline Reinforcement Learning for Heterogeneous Robot Datasets</a></td>
<td nowrap>Cross-Embodiment Offline Reinforcement Learning uses reinforcement learning, preference feedback, or post-training signals to improve robot policies.</td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>VLA / RL / Online Fine-tuning</td>
<td nowrap>offline RL + morphology grouping</td>
<td nowrap>RL fine-tuning / policy optimization</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=GrsoLVNy3Y">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>16 robot-platform locomotion dataset suite</td>
<td nowrap>HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Humanoid-RL, WAM</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=ITeuGb2bYg">Policy Likelihood-based Query Sampling and Critic-Exploited Reset for Efficient Preference-based Reinforcement Learning</a></td>
<td nowrap>Policy Likelihood-based Query Sampling and Critic-Exploited Reset uses reinforcement learning, preference feedback, or post-training signals to improve robot policies.</td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>VLA / RL / Online Fine-tuning</td>
<td nowrap>RL / offline RL</td>
<td nowrap>RL fine-tuning / policy optimization</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=ITeuGb2bYg">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=TQhSodCM4r">SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning</a></td>
<td nowrap>SimpleVLA-RL uses reinforcement learning, preference feedback, or post-training signals to improve robot policies.</td>
<td nowrap>OpenVLA-OFT</td>
<td nowrap>AR</td>
<td nowrap>VLA / RL / RL/online fine-tuning / Reward S</td>
<td nowrap>GRPO</td>
<td nowrap>On-Policy / MF</td>
<td nowrap>Sim ✓ (MT) / Real ✓ (ST)</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=TQhSodCM4r">paper</a> / <a href="https://arxiv.org/pdf/2509.09674">paper</a> / <a href="https://arxiv.org/abs/2509.09674">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN, Efficient-VLA, RL-VLA</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=uWJwQ5SZoM">Robust Fine-tuning of Vision-Language-Action Robot Policies via Parameter Merging</a></td>
<td nowrap>Robust Fine-tuning of Vision-Language-Action Robot Policies studies VLA robustness under multimodal perturbations, adversarial inputs, or distribution shifts.</td>
<td nowrap>No specific base VLA specified.</td>
<td nowrap>AR</td>
<td nowrap>VLA / RL / Online Fine-tuning</td>
<td nowrap>-</td>
<td nowrap>RL fine-tuning / policy optimization</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=uWJwQ5SZoM">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=dc90uPqxWF">World2Minecraft: Occupancy-Driven simulated scenes Construction</a></td>
<td nowrap>World2Minecraft connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td nowrap>-</td>
<td nowrap>3D/spatial grounding</td>
<td nowrap>VLA / RL / Online Fine-tuning</td>
<td nowrap>3D/spatial representation learning</td>
<td nowrap>RL fine-tuning / policy optimization</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=dc90uPqxWF">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38876">Steering Visuomotor Policy in Open Worlds via Cross-View Goal Alignment</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>policy action</td>
<td nowrap>VLA / RL / Online Fine-tuning</td>
<td nowrap>-</td>
<td nowrap>RL fine-tuning / policy optimization</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38876">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/63131">HIER: Human-in-the-Loop Imagination-Execution Refinement for General Real-World Vision-Language-Action Models</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA / RL / Online Fine-tuning</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/63131">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://openreview.net/forum?id=RkdTtznSAL">Real-World Reinforcement Learning of Active Perception Behaviors</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>AR</td>
<td nowrap>RL / Online Fine-tuning</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=RkdTtznSAL">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Efficient-VLA, Robot-Learning, Humanoid-RL, EAI-Safety, WAM, RL-VLA</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICML 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2505.07395">ReinboT: Amplifying Robot Visual-Language Manipulation with Reinforcement Learning</a></td>
<td nowrap>ReinboT uses reinforcement learning, preference feedback, or post-training signals to improve robot policies.</td>
<td nowrap>ReinboT</td>
<td nowrap>AR</td>
<td nowrap>VLA / RL / Online Fine-tuning</td>
<td nowrap>DT + RTG</td>
<td nowrap>Off-Policy / MF</td>
<td nowrap>Sim + Real</td>
<td nowrap>-</td>
<td nowrap><a href="https://arxiv.org/abs/2505.07395">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>RL-VLA</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
</tbody>
</table>

#### Safety and Robustness

Total: 4 papers.

<table>
<thead>
<tr>
<th nowrap>Venue/Year</th>
<th nowrap>Paper/Method</th>
<th nowrap>Abstract</th>
<th nowrap>Base VLA</th>
<th nowrap>Action</th>
<th nowrap>Training/Feedback</th>
<th nowrap>Algorithm</th>
<th nowrap>Policy/Type</th>
<th nowrap>Sim/Real</th>
<th nowrap>Paper Task/Goal</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>Source</th>
<th nowrap>Survey Note</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ICRA 2025</td>
<td nowrap><a href="https://ieeexplore.ieee.org/document/11128017/">Run-time Observation Interventions Make Vision-Language-Action Models More Visually Robust</a></td>
<td nowrap>BYOVLA 在运行时识别并编辑任务无关视觉区域，提升 Octo/OpenVLA 对视觉干扰的鲁棒性。</td>
<td nowrap>Octo / OpenVLA</td>
<td nowrap>AR / policy action</td>
<td nowrap>VLA / safety and robustness</td>
<td nowrap>run-time observation intervention</td>
<td nowrap>robust VLA execution</td>
<td nowrap>Real robot manipulation</td>
<td nowrap>降低真实部署中无关视觉扰动导致的 VLA 失败。</td>
<td nowrap><a href="https://ieeexplore.ieee.org/document/11128017/">paper</a></td>
<td nowrap><a href="https://aasherh.github.io/byovla/">project</a></td>
<td nowrap><a href="https://github.com/irom-princeton/byovla">code</a></td>
<td nowrap>-</td>
<td nowrap>ICRA/IROS</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=cS6xizdYD5">On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations</a></td>
<td nowrap>On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations studies VLA robustness under multimodal perturbations, adversarial inputs, or distribution shifts.</td>
<td nowrap>π0 / OpenVLA</td>
<td nowrap>Diffusion / Flow</td>
<td nowrap>VLA / safety / safety and robustness</td>
<td nowrap>RobustVLA; 17 perturbations across 4 modalities</td>
<td nowrap>Flow policy</td>
<td nowrap>LIBERO + real FR5</td>
<td nowrap>-</td>
<td nowrap><a href="https://openreview.net/forum?id=cS6xizdYD5">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2505.16640">BadVLA: Towards Backdoor Attacks on Vision-Language-Action Models via Objective-Decoupled Optimization</a></td>
<td nowrap>BadVLA studies how to inject backdoor triggers into VLAs and affect robot action outputs.</td>
<td nowrap>No specific base VLA specified.</td>
<td nowrap>AR</td>
<td nowrap>VLA / safety and robustness</td>
<td nowrap>objective-decoupled backdoor attack</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Constructs and evaluates backdoor attacks against VLA robot policies.</td>
<td nowrap><a href="https://arxiv.org/abs/2505.16640">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-Safety</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2411.13587">Exploring the Adversarial Vulnerabilities of Vision-Language-Action Models in Robotics</a></td>
<td nowrap>Exploring the Adversarial Vulnerabilities of Vision-Language-Action Models in Robotics studies VLA robustness under multimodal perturbations, adversarial inputs, or distribution shifts.</td>
<td nowrap>No specific base VLA specified.</td>
<td nowrap>AR</td>
<td nowrap>VLA / safety and robustness</td>
<td nowrap>UADA / UPA / TMA adversarial attacks</td>
<td nowrap>3D-grounded policy/perception</td>
<td nowrap>simulation + physical setup</td>
<td nowrap>-</td>
<td nowrap><a href="https://arxiv.org/abs/2411.13587">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>LIBERO + BridgeData V2 attack assets</td>
<td nowrap>EAI-Safety</td>
<td nowrap>Used to compare VLA progress in generalization, action representation, and execution stability.</td>
</tr>
</tbody>
</table>

### WAM / World Models

WAM combines future world-state prediction with action generation and fits naturally between agent planning and low-level control. Its value is not replacing every controller, but providing an intermediate layer for imagination, verification, and recovery.

Subdirections: cascaded WAM, joint WAM, video/latent world model, world model for VLA, and world model evaluation.

Total: 51 papers.

<table>
<thead>
<tr>
<th nowrap>Subdirection</th>
<th nowrap>Entries</th>
<th nowrap>Focus</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>cascaded WAM</td>
<td nowrap>24</td>
<td nowrap>Look at the hierarchical pipeline that imagines first and acts later.</td>
</tr>
<tr>
<td nowrap>joint WAM</td>
<td nowrap>3</td>
<td nowrap>Look at joint modeling of vision, state, and action.</td>
</tr>
<tr>
<td nowrap>video/latent world model</td>
<td nowrap>14</td>
<td nowrap>Look at the quality of future-video or latent-state prediction.</td>
</tr>
<tr>
<td nowrap>world model for VLA</td>
<td nowrap>9</td>
<td nowrap>Look at how world models support VLA decision-making.</td>
</tr>
</tbody>
</table>

#### cascaded WAM

Total: 24 papers.

<table>
<thead>
<tr>
<th nowrap>Venue/Year</th>
<th nowrap>Paper/Method</th>
<th nowrap>Abstract</th>
<th nowrap>WAM Type</th>
<th nowrap>State Representation</th>
<th nowrap>Action Interface</th>
<th nowrap>Use</th>
<th nowrap>Sim/Real</th>
<th nowrap>Paper Task/Goal</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>Source</th>
<th nowrap>Survey Note</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ICRA 2025</td>
<td nowrap><a href="https://nvlabs.github.io/X-MOBILITY/">X-MOBILITY: End-To-End Generalizable Navigation via World Modeling</a></td>
<td nowrap>X-MOBILITY 用自回归 latent world model 解耦世界动态学习和动作策略，支持 zero-shot sim2real 导航。</td>
<td nowrap>navigation world model</td>
<td nowrap>latent future state</td>
<td nowrap>navigation action</td>
<td nowrap>navigation policy imagination</td>
<td nowrap>Sim + Real</td>
<td nowrap>通过世界模型提升端到端导航泛化和 sim2real。</td>
<td nowrap><a href="https://nvlabs.github.io/X-MOBILITY/">paper</a></td>
<td nowrap><a href="https://nvlabs.github.io/X-MOBILITY/">project</a></td>
<td nowrap><a href="https://github.com/NVlabs/X-MOBILITY">code</a></td>
<td nowrap><a href="https://github.com/NVlabs/X-MOBILITY">data</a></td>
<td nowrap>ICRA/IROS</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=748bHL2BAv">Ctrl-World: A Controllable Generative World Model for Robot Manipulation</a></td>
<td nowrap>Build a controllable multi-view robotic world model, using imagined rollouts to evaluate and improve generalist robot policies.</td>
<td nowrap>cascaded WAM</td>
<td nowrap>Multi-view video world model</td>
<td nowrap>frame-level action conditioning</td>
<td nowrap>policy evaluation + synthetic improvement</td>
<td nowrap>Real robot data/DROID</td>
<td nowrap>Address the problem that real rollouts for generalist robot policies under new objects and new instructions are expensive and hard to scale.</td>
<td nowrap><a href="https://openreview.net/forum?id=748bHL2BAv">paper</a></td>
<td nowrap><a href="https://ctrl-world.github.io/">project</a></td>
<td nowrap><a href="https://github.com/Robert-gyj/Ctrl-World">code</a></td>
<td nowrap><a href="https://huggingface.co/yjguo/Ctrl-World">hf</a></td>
<td nowrap>WAM</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=0GNBqoYcAP">Context and Diversity Matter: The Emergence of In-Context Learning in World Models</a></td>
<td nowrap>Study how world models identify or learn new environment dynamics from in-context examples.</td>
<td nowrap>cascaded WAM</td>
<td nowrap>environment dynamics/world-model latent</td>
<td nowrap>-</td>
<td nowrap>ICL dynamics prediction</td>
<td nowrap>sim/analysis</td>
<td nowrap>Address the poor adaptability of static world models when facing new environments or rare configurations.</td>
<td nowrap><a href="https://openreview.net/forum?id=0GNBqoYcAP">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=4HZgkwVVFO">NeMo-map: Neural Implicit Flow Fields for Spatio-Temporal Motion Mapping</a></td>
<td nowrap>Use neural implicit functions to continuously model site-specific spatiotemporal motion flow fields.</td>
<td nowrap>spatio-temporal motion world model</td>
<td nowrap>implicit neural flow field</td>
<td nowrap>-</td>
<td nowrap>motion mapping/navigation safety</td>
<td nowrap>public motion datasets</td>
<td nowrap>Address the high cost of discrete sampling and offline construction for dynamic motion maps in human environments.</td>
<td nowrap><a href="https://openreview.net/forum?id=4HZgkwVVFO">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=8UZpmrxoLG">Astra: General Interactive World Model with Autoregressive Denoising</a></td>
<td nowrap>Use an autoregressive denoising video model to generate long-horizon future worlds controllable by actions.</td>
<td nowrap>cascaded WAM</td>
<td nowrap>video world model</td>
<td nowrap>action-aware adapter</td>
<td nowrap>interactive future prediction</td>
<td nowrap>robot + driving scenarios</td>
<td nowrap>Address long-horizon future prediction from historical observations and actions in general scenarios.</td>
<td nowrap><a href="https://openreview.net/forum?id=8UZpmrxoLG">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=LQD1MrnbxH">Test-Time Mixture of World Models for Embodied Agents in Dynamic Environments</a></td>
<td nowrap>Dynamically route and combine multiple world models at test time to adapt to changing environments.</td>
<td nowrap>cascaded WAM</td>
<td nowrap>mixture of world models</td>
<td nowrap>agent action/API</td>
<td nowrap>test-time adaptation for embodied reasoning</td>
<td nowrap>dynamic embodied env benchmarks</td>
<td nowrap>Address insufficient world-model composition and continual adaptation for embodied agents in unseen dynamic environments.</td>
<td nowrap><a href="https://openreview.net/forum?id=LQD1MrnbxH">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Humanoid-RL, EAI-Safety, WAM, RL-VLA</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=MPabX9LEds">Learning Massively Multitask World Models for Continuous Control</a></td>
<td nowrap>Newt pretrains and online-optimizes a language-conditioned world model across 200 continuous-control tasks.</td>
<td nowrap>cascaded WAM</td>
<td nowrap>language-conditioned multitask latent world model</td>
<td nowrap>continuous control actions</td>
<td nowrap>online RL pretraining/fine-tuning</td>
<td nowrap>-</td>
<td nowrap>Address poor scalability of online RL across multitask continuous control and multiple embodiments.</td>
<td nowrap><a href="https://openreview.net/forum?id=MPabX9LEds">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>200-task benchmark</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=a1zfcaNTkM">ExoPredicator: Learning Abstract Models of Dynamic Worlds for Robot Planning</a></td>
<td nowrap>Learn symbolic states and endogenous/exogenous causal processes for long-horizon robot planning.</td>
<td nowrap>cascaded WAM</td>
<td nowrap>abstract symbolic state + causal processes</td>
<td nowrap>symbolic/endogenous actions</td>
<td nowrap>long-horizon planning</td>
<td nowrap>simulated tabletop</td>
<td nowrap>Address concurrent environment changes and action effects in robot planning.</td>
<td nowrap><a href="https://openreview.net/forum?id=a1zfcaNTkM">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=oBXfPyi47m">Efficient Reinforcement Learning by Guiding World Models with Non-Curated Data</a></td>
<td nowrap>Use reward-free, cross-embodiment, mixed-quality offline data to guide world models and improve online RL sample efficiency.</td>
<td nowrap>cascaded WAM</td>
<td nowrap>world model from offline/online data</td>
<td nowrap>visuomotor RL actions</td>
<td nowrap>sample-efficient online RL</td>
<td nowrap>72 visuomotor tasks/6 embodiments</td>
<td nowrap>Address distribution shift that makes directly fine-tuning world models with uncurated offline data ineffective for improving RL.</td>
<td nowrap><a href="https://openreview.net/forum?id=oBXfPyi47m">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=qmEyJadwHA">Object-Centric World Models from Few-Shot Annotations for Sample-Efficient Reinforcement Learning</a></td>
<td nowrap>OC-STORM uses a small amount of annotations to extract object-centric representations and improve sample efficiency for pixel-based MBRL.</td>
<td nowrap>cascaded WAM</td>
<td nowrap>object-centric latent</td>
<td nowrap>RL actions</td>
<td nowrap>sample-efficient MBRL</td>
<td nowrap>-</td>
<td nowrap>Address low sample efficiency caused by pixel-level world models ignoring small but critical objects.</td>
<td nowrap><a href="https://openreview.net/forum?id=qmEyJadwHA">paper</a></td>
<td nowrap><a href="https://oc-storm.weipuzhang.com">project</a></td>
<td nowrap>-</td>
<td nowrap>Atari 100k, Hollow Knight</td>
<td nowrap>HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Efficient-VLA, Robot-Learning, Humanoid-RL, EAI-Safety</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=w3w7WVG4ks">Building spatial world models from sparse transitional episodic memories</a></td>
<td nowrap>ESWM builds spatial cognitive maps from sparse discrete episodic memories and predicts unobserved transitions.</td>
<td nowrap>cascaded WAM</td>
<td nowrap>episodic spatial latent map</td>
<td nowrap>navigation transitions</td>
<td nowrap>exploration/navigation planning</td>
<td nowrap>simulated spatial environments</td>
<td nowrap>Address the need for long continuous trajectories when building maps with spatial world models.</td>
<td nowrap><a href="https://openreview.net/forum?id=w3w7WVG4ks">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=yDmb7xAfeb">World-In-World: World Models in a Closed-Loop World</a></td>
<td nowrap>Provide a closed-loop platform to evaluate whether world models truly improve embodied task success.</td>
<td nowrap>world model evaluation/closed-loop WAM</td>
<td nowrap>heterogeneous WMs</td>
<td nowrap>standardized action API</td>
<td nowrap>closed-loop planning/evaluation</td>
<td nowrap>-</td>
<td nowrap>Address world-model evaluations biased toward open-loop visual quality and lacking closed-loop metrics for task success.</td>
<td nowrap><a href="https://openreview.net/forum?id=yDmb7xAfeb">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>World-In-World benchmark</td>
<td nowrap>WAM</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=Patx6MRipw">ENACT: Evaluating Embodied Cognition with World Modeling of Egocentric Interaction</a></td>
<td nowrap>ENACT uses egocentric interaction sequence reordering tasks to evaluate VLMs' forward and inverse world-modeling ability.</td>
<td nowrap>world model evaluation</td>
<td nowrap>egocentric state/action sequences</td>
<td nowrap>inverse world modeling actions</td>
<td nowrap>benchmark/evaluation</td>
<td nowrap>-</td>
<td nowrap>Address how to evaluate whether VLMs have embodied cognition and interactive world-modeling ability.</td>
<td nowrap><a href="https://openreview.net/forum?id=Patx6MRipw">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>ENACT</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/63978">Cross-Embodiment Robot Foundation World Models with Latent Actions</a></td>
<td nowrap>LAC-WM trains a cross-embodiment robotic world model using a unified latent action space.</td>
<td nowrap>cascaded WAM</td>
<td nowrap>latent action-conditioned world model</td>
<td nowrap>unified latent actions</td>
<td nowrap>cross-embodiment adaptation</td>
<td nowrap>dexterous manipulation benchmark</td>
<td nowrap>Address poor generalization of world models to new embodiments caused by inconsistent action spaces across robots.</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/63978">paper</a></td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/63978">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Humanoid-RL, WAM</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62480">DDP-WM: Disentangled Dynamics Prediction for Efficient World Models</a></td>
<td nowrap>DDP-WM disentangles primary dynamics from background updates to improve real-time inference and planning efficiency in world models.</td>
<td nowrap>cascaded WAM</td>
<td nowrap>disentangled latent dynamics</td>
<td nowrap>MPC/planner</td>
<td nowrap>efficient planning</td>
<td nowrap>navigation/tabletop/deformable benchmarks</td>
<td nowrap>Address high computational cost and poor real-time deployability of dense Transformer world models.</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62480">paper</a></td>
<td nowrap><a href="https://hcplab-sysu.github.io/DDP-WM">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62543">RoboFlow4D: A Lightweight Flow World Model Toward Real-Time Flow-Guided Robotic Manipulation</a></td>
<td nowrap>RoboFlow4D directly predicts multi-frame 3D flow and uses flow to guide real-time robotic manipulation.</td>
<td nowrap>cascaded WAM</td>
<td nowrap>multi-frame 3D flow</td>
<td nowrap>flow-guided action policy</td>
<td nowrap>real-time manipulation planning</td>
<td nowrap>Sim + Real</td>
<td nowrap>Address high overhead and poor real-time performance in modular predict-flow-plan pipelines for 3D manipulation.</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62543">paper</a></td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62543">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64209">Learning Task-Sufficient World Models by Synergizing Agentic Exploration and Structured Modeling</a></td>
<td nowrap>Learn task-sufficient and compact world-model representations through active exploration and structured modeling.</td>
<td nowrap>cascaded WAM</td>
<td nowrap>task-sufficient structured latent</td>
<td nowrap>agentic exploration/actions</td>
<td nowrap>sample-efficient control/generalization</td>
<td nowrap>continuous control + manipulation benchmarks</td>
<td nowrap>Address general visual/latent world models retaining too many control-irrelevant factors, hurting generalization efficiency.</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64209">paper</a></td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64209">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2509.15536">SAMPO: Scale-wise Autoregression with Motion PrOmpt for Generative World Models</a></td>
<td nowrap>SAMPO combines scale-wise visual autoregression, causal next-frame modeling, and motion prompts to generate action-conditioned futures.</td>
<td nowrap>cascaded WAM</td>
<td nowrap>video tokens + motion prompt</td>
<td nowrap>action-conditioned video prediction</td>
<td nowrap>model-based control/video prediction</td>
<td nowrap>robot/world-model benchmarks</td>
<td nowrap>Address damaged spatial structure, inefficient decoding, and insufficient motion modeling in autoregressive world models.</td>
<td nowrap><a href="https://arxiv.org/abs/2509.15536">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2505.05495">Learning 3D Persistent Embodied World Models</a></td>
<td nowrap>Learn an embodied world model with explicit 3D memory to simulate long-horizon future observations more consistently.</td>
<td nowrap>cascaded WAM</td>
<td nowrap>RGB-D video + persistent 3D map</td>
<td nowrap>future action-conditioned observation prediction</td>
<td nowrap>planning/policy learning</td>
<td nowrap>embodied applications</td>
<td nowrap>Address lack of unobserved-scene memory and inconsistent long-horizon planning in video world models.</td>
<td nowrap><a href="https://arxiv.org/abs/2505.05495">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2505.20425">OSVI-WM: One-Shot Visual Imitation for Unseen Tasks using World-Model-Guided Trajectory Generation</a></td>
<td nowrap>Use a world model to generate latent states and action trajectories for one-shot visual imitation on unseen tasks.</td>
<td nowrap>cascaded WAM</td>
<td nowrap>latent states/trajectory</td>
<td nowrap>decoded physical waypoints</td>
<td nowrap>one-shot imitation</td>
<td nowrap>2 sim benchmarks + 3 real robot platforms</td>
<td nowrap>Address poor generalization of one-shot visual imitation to new tasks with different semantics or structures.</td>
<td nowrap><a href="https://arxiv.org/abs/2505.20425">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/raktimgg/OSVI-WM">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2406.14540">IRASim: A Fine-Grained World Model for Robot Manipulation</a></td>
<td nowrap>IRASim uses a frame-by-frame action-conditioned diffusion Transformer to generate fine-grained robot-object interaction videos.</td>
<td nowrap>cascaded WAM</td>
<td nowrap>action-conditioned video</td>
<td nowrap>robot action trajectories/frame-level conditioning</td>
<td nowrap>fine-grained manipulation simulation</td>
<td nowrap>robot manipulation datasets</td>
<td nowrap>Address the difficulty of precise action-visual frame alignment and fine-grained interaction prediction in robotic manipulation.</td>
<td nowrap><a href="https://arxiv.org/abs/2406.14540">paper</a></td>
<td nowrap><a href="https://gen-irasim.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://ziweiwangthu.github.io/data/GWM.pdf">GWM: Towards Scalable Gaussian World Models for Robotic Manipulation</a></td>
<td nowrap>GWM uses 3D Gaussian primitives to predict future 3D scenes after robot actions.</td>
<td nowrap>cascaded WAM</td>
<td nowrap>3D Gaussian splats latent</td>
<td nowrap>robot action-conditioned Gaussian propagation</td>
<td nowrap>imitation representation + MBRL simulator</td>
<td nowrap>Sim + Real</td>
<td nowrap>Address lack of stable 3D geometric information in image world models, making it difficult to support policy training.</td>
<td nowrap><a href="https://arxiv.org/abs/2507.07954">paper</a></td>
<td nowrap><a href="https://gaussian-world-model.github.io/">project</a></td>
<td nowrap><a href="https://github.com/Gaussian-World-Model/gaussianwm">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.16806">DyWA: Dynamics-adaptive World Action Model for Generalizable Non-prehensile Manipulation</a></td>
<td nowrap>DyWA jointly predicts future states and adapts to dynamics changes, improving generalization for non-prehensile manipulation.</td>
<td nowrap>cascaded WAM</td>
<td nowrap>single-view point cloud + geometry/state/physics</td>
<td nowrap>world action model</td>
<td nowrap>non-prehensile manipulation</td>
<td nowrap>Sim + Real</td>
<td nowrap>Address generalization challenges in non-prehensile manipulation under varying object mass, table friction, and single-view partial observability.</td>
<td nowrap><a href="https://arxiv.org/abs/2503.16806">paper</a></td>
<td nowrap><a href="https://pku-epic.github.io/DyWA/">project</a></td>
<td nowrap><a href="https://github.com/jiangranlv/DyWA">code</a></td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://openreview.net/pdf?id=mnwlhvmKMN">Learning 4D Embodied World Models</a></td>
<td nowrap>TesserAct predicts action-evolving 4D dynamic mesh worlds from images and language.</td>
<td nowrap>cascaded WAM</td>
<td nowrap>4D dynamic mesh</td>
<td nowrap>inverse dynamics/policy execution</td>
<td nowrap>4D prediction + policy learning</td>
<td nowrap>dataset + embodied tasks</td>
<td nowrap>Address lack of precise 3D geometry and temporal dynamics in 2D video world models, making inverse dynamics hard to learn.</td>
<td nowrap><a href="https://openreview.net/pdf?id=mnwlhvmKMN">paper</a> / <a href="https://arxiv.org/pdf/2504.20995">paper</a></td>
<td nowrap><a href="https://tesseractworld.github.io/">project</a></td>
<td nowrap><a href="https://github.com/UMass-Embodied-AGI/TesserAct">code</a></td>
<td nowrap><a href="https://huggingface.co/anyeZHY/tesseract">hf</a></td>
<td nowrap>WAM</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
</tbody>
</table>

#### joint WAM

Total: 3 papers.

<table>
<thead>
<tr>
<th nowrap>Venue/Year</th>
<th nowrap>Paper/Method</th>
<th nowrap>Abstract</th>
<th nowrap>WAM Type</th>
<th nowrap>State Representation</th>
<th nowrap>Action Interface</th>
<th nowrap>Use</th>
<th nowrap>Sim/Real</th>
<th nowrap>Paper Task/Goal</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>Source</th>
<th nowrap>Survey Note</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=IvUM6UwYCJ">Empowering Multi-Robot Cooperation via Sequential World Models</a></td>
<td nowrap>SeqWM uses an autoregressive agent-wise world model to reduce the complexity of modeling joint dynamics for multi-robot systems.</td>
<td nowrap>joint WAM</td>
<td nowrap>sequential agent-wise world models</td>
<td nowrap>multi-agent RL actions</td>
<td nowrap>multi-robot cooperation/planning</td>
<td nowrap>Sim + Real</td>
<td nowrap>Address complex joint dynamics in physical multi-robot cooperation and poor scalability of MBRL.</td>
<td nowrap><a href="https://openreview.net/forum?id=IvUM6UwYCJ">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/zhaozijie2022/seqwm-marl">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64447">Dual-Stream Diffusion for World-Model Augmented Vision-Language-Action Model</a></td>
<td nowrap>DUST uses a dual-stream diffusion Transformer to model vision and action separately while sharing cross-modal information.</td>
<td nowrap>joint WAM</td>
<td nowrap>vision tokens + action tokens</td>
<td nowrap>diffusion/flow-matching action tokens</td>
<td nowrap>world-model augmented VLA</td>
<td nowrap>RoboCasa, GR-1, Franka Research 3</td>
<td nowrap>Address training difficulties from visual-action modality differences when jointly predicting states and actions in VLA.</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64447">paper</a></td>
<td nowrap><a href="https://periphanes.github.io/dust/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN, WAM</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2507.11296">Diffusion-Based Imaginative Coordination for Bimanual Manipulation</a></td>
<td nowrap>Improve bimanual manipulation coordination through joint video and action diffusion prediction.</td>
<td nowrap>joint WAM</td>
<td nowrap>multi-frame latent future states</td>
<td nowrap>diffusion action prediction</td>
<td nowrap>bimanual coordination</td>
<td nowrap>ALOHA + RoboTwin + Real</td>
<td nowrap>Address policy-learning difficulty caused by high-dimensional action spaces and complex coordination in bimanual manipulation.</td>
<td nowrap><a href="https://arxiv.org/abs/2507.11296">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/return-sleep/Diffusion_based_imaginative_Coordination">code</a></td>
<td nowrap>-</td>
<td nowrap>Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Efficient-VLA, EAI-Safety, WAM</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
</tbody>
</table>

#### video/latent world model

Total: 14 papers.

<table>
<thead>
<tr>
<th nowrap>Venue/Year</th>
<th nowrap>Paper/Method</th>
<th nowrap>Abstract</th>
<th nowrap>WAM Type</th>
<th nowrap>State Representation</th>
<th nowrap>Action Interface</th>
<th nowrap>Use</th>
<th nowrap>Sim/Real</th>
<th nowrap>Paper Task/Goal</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>Source</th>
<th nowrap>Survey Note</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>IROS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.19842">ManiGaussian++: General Robotic Bimanual Manipulation with Hierarchical Gaussian World Model</a></td>
<td nowrap>ManiGaussian++ 用层级 Gaussian world model 建模双臂操作中的空间状态和交互动态。</td>
<td nowrap>Gaussian world model</td>
<td nowrap>hierarchical 3D Gaussian state</td>
<td nowrap>bimanual action</td>
<td nowrap>bimanual manipulation prediction</td>
<td nowrap>Sim + Real</td>
<td nowrap>用层级 3D 世界模型支持通用双臂操作。</td>
<td nowrap><a href="https://arxiv.org/abs/2506.19842">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/April-Yz/ManiGaussian_bimanual">code</a></td>
<td nowrap>-</td>
<td nowrap>ICRA/IROS</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=3q9vHEqsNx">FantasyWorld: Geometry-Consistent World Modeling via Unified Video and 3D Prediction</a></td>
<td nowrap>Add a geometry branch to a frozen video foundation model to jointly predict video latents and implicit 3D fields.</td>
<td nowrap>video/latent world model</td>
<td nowrap>video latents + implicit 3D field</td>
<td nowrap>-</td>
<td nowrap>3D-aware video/world representation</td>
<td nowrap>3D reasoning benchmarks</td>
<td nowrap>Address lack of explicit 3D grounding and spatial consistency in video world models.</td>
<td nowrap><a href="https://openreview.net/forum?id=3q9vHEqsNx">paper</a></td>
<td nowrap><a href="https://fantasy-amap.github.io/fantasy-world/">project</a></td>
<td nowrap><a href="https://github.com/Fantasy-AMAP/fantasy-world">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=NQq9JLMfNN">Unified 3D Scene Understanding Through Physical World Modeling</a></td>
<td nowrap>3WM unifies 3D tasks such as depth, novel-view synthesis, and object manipulation as physical world-model reasoning.</td>
<td nowrap>video/latent world model</td>
<td nowrap>probabilistic graph of RGB/flow/camera pose etc.</td>
<td nowrap>prompt/inference pathways</td>
<td nowrap>unified 3D understanding and interaction</td>
<td nowrap>multi-dataset 3D tasks</td>
<td nowrap>Address fragmentation among 3D scene understanding tasks and the difficulty of sharing representations and transfer.</td>
<td nowrap><a href="https://openreview.net/forum?id=NQq9JLMfNN">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=pFyzqbUiF9">Vid2World: Crafting Video Diffusion Models to Interactive World Models</a></td>
<td nowrap>Vid2World causalizes pretrained video diffusion models and adds action guidance, turning them into interactive world models.</td>
<td nowrap>video/latent world model</td>
<td nowrap>causalized video diffusion latents</td>
<td nowrap>causal action guidance</td>
<td nowrap>interactive world modeling</td>
<td nowrap>sequential decision benchmarks</td>
<td nowrap>Address traditional world models requiring large amounts of domain-specific training and producing coarse predictions.</td>
<td nowrap><a href="https://openreview.net/forum?id=pFyzqbUiF9">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=wcTuZG9P2o">EgoWorld: Translating Exocentric View to Egocentric View using Rich Exocentric Observations</a></td>
<td nowrap>EgoWorld reconstructs the egocentric view from exocentric observations using point clouds, 3D hand poses, and text.</td>
<td nowrap>video/latent world model</td>
<td nowrap>point cloud + 3D hand pose + text</td>
<td nowrap>-</td>
<td nowrap>egocentric view/world reconstruction for manipulation</td>
<td nowrap>AR/VR/robotics settings</td>
<td nowrap>Address exocentric-to-egocentric conversion relying on synchronized multi-view data, camera poses, or initial egocentric frames.</td>
<td nowrap><a href="https://openreview.net/forum?id=wcTuZG9P2o">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38905">LiDARCrafter: Dynamic 4D World Modeling from LiDAR Sequences</a></td>
<td nowrap>LiDARCrafter generates controllable 4D LiDAR sequences using language-to-ego-scene graphs and a three-branch diffusion model.</td>
<td nowrap>video/latent world model</td>
<td nowrap>4D LiDAR sequence/layout</td>
<td nowrap>-</td>
<td nowrap>LiDAR generation/editing/evaluation</td>
<td nowrap>nuScenes benchmark</td>
<td nowrap>Address controllability, temporal consistency, and standardized evaluation in autonomous-driving LiDAR world generation.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38905">paper</a></td>
<td nowrap><a href="https://lidarcrafter.github.io/">project</a></td>
<td nowrap><a href="https://github.com/worldbench/LiDARCrafter">code</a></td>
<td nowrap>nuScenes + scene/object/sequence metrics + HuggingFace weights</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/65193">DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos</a></td>
<td nowrap>DreamDojo learns a latent-action-driven robot world model from 44,000 hours of human first-person videos.</td>
<td nowrap>video/latent world model</td>
<td nowrap>video world model + continuous latent actions</td>
<td nowrap>-</td>
<td nowrap>teleoperation/policy evaluation/model-based planning</td>
<td nowrap>OOD robot benchmarks</td>
<td nowrap>Address insufficient data coverage, scarce action labels, and difficulty simulating contact-rich tasks in robot world models.</td>
<td nowrap><a href="https://arxiv.org/abs/2602.06949">paper</a></td>
<td nowrap><a href="https://dreamdojo-world.github.io/">project</a></td>
<td nowrap><a href="https://github.com/NVIDIA/DreamDojo">code</a></td>
<td nowrap><a href="https://huggingface.co/nvidia/DreamDojo">hf</a></td>
<td nowrap>Humanoid-RL, WAM</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66091">From Imagined Futures to Executable Actions: Mixture of Latent Actions for Robot Manipulation</a></td>
<td nowrap>MoLA uses multiple inverse-dynamics models to convert imagined videos into executable mixtures of latent actions.</td>
<td nowrap>video/latent world model</td>
<td nowrap>imagined future videos + latent actions</td>
<td nowrap>mixture of latent actions from inverse dynamics</td>
<td nowrap>video-to-action execution</td>
<td nowrap>LIBERO, CALVIN, LIBERO-Plus + Real</td>
<td nowrap>Address the difficulty of stably converting visually realistic generated future video frames into control actions.</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66091">paper</a></td>
<td nowrap><a href="https://logosroboticsgroup.github.io/MoLA/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://openreview.net/forum?id=UPHlqbZFZB">VideoVLA: Video Generators Can Be Generalizable Robot Manipulators</a></td>
<td nowrap>VideoVLA turns a large video generation model into a robot VLA that predicts both actions and future visual outcomes.</td>
<td nowrap>video/latent world model</td>
<td nowrap>video/language/action tokens</td>
<td nowrap>action sequence prediction</td>
<td nowrap>generalizable manipulation</td>
<td nowrap>Sim + Real</td>
<td nowrap>Address insufficient joint modeling of visual imagination and action prediction in generalizable robotic manipulation.</td>
<td nowrap><a href="https://openreview.net/forum?id=UPHlqbZFZB">paper</a></td>
<td nowrap><a href="https://videovla-nips2025.github.io/">project</a></td>
<td nowrap><a href="https://github.com/VideoVLA-Project/VideoVLA">code</a></td>
<td nowrap>SIMPLER, OXE, Realman real-world eval</td>
<td nowrap>EAI-VLA-VLN, WAM</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2501.01895">EnerVerse: Envisioning Embodied Future Space for Robotics Manipulation</a></td>
<td nowrap>EnerVerse uses multi-view video diffusion and a 4D data engine to predict embodied future space and convert it into actions.</td>
<td nowrap>video/latent world model</td>
<td nowrap>multi-view video/4D world representations</td>
<td nowrap>EnerVerse-A policy head/action chunks</td>
<td nowrap>robot manipulation foundation model</td>
<td nowrap>Sim + Real</td>
<td nowrap>Address long-horizon future-space modeling, 3D grounding, and sim-to-real gaps in robotic manipulation.</td>
<td nowrap><a href="https://arxiv.org/abs/2501.01895">paper</a></td>
<td nowrap><a href="https://sites.google.com/view/enerverse">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2507.04447">DreamVLA: A Vision-Language-Action Model Dreamed with Comprehensive World Knowledge</a></td>
<td nowrap>DreamVLA predicts dynamic, spatial, and semantic world knowledge, then uses inverse dynamics to generate actions.</td>
<td nowrap>video/latent world model</td>
<td nowrap>dynamic/spatial/semantic world knowledge</td>
<td nowrap>diffusion transformer action prediction</td>
<td nowrap>VLA manipulation</td>
<td nowrap>CALVIN + Real</td>
<td nowrap>Address redundant information in VLA image prediction and lack of key world knowledge.</td>
<td nowrap><a href="https://arxiv.org/abs/2507.04447">paper</a></td>
<td nowrap><a href="https://zhangwenyao1.github.io/DreamVLA/index.html">project</a></td>
<td nowrap><a href="https://github.com/Zhangwenyao1/DreamVLA">code</a></td>
<td nowrap><a href="https://huggingface.co/WenyaoZhang/DreamVLA">hf</a></td>
<td nowrap>Awesome-VLA</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
<tr>
<td nowrap>ICML 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2412.14803">Video Prediction Policy: A Generalist Robot Policy with Predictive Visual Representations</a></td>
<td nowrap>VPP uses internal future representations from a video diffusion model to learn an implicit inverse-dynamics policy.</td>
<td nowrap>video/latent world model</td>
<td nowrap>predictive visual representations from VDM</td>
<td nowrap>implicit inverse dynamics</td>
<td nowrap>generalist robot policy</td>
<td nowrap>CALVIN + real dexterous tasks</td>
<td nowrap>Address static visual encoders ignoring dynamic information needed for embodied tasks.</td>
<td nowrap><a href="https://arxiv.org/abs/2412.14803">paper</a></td>
<td nowrap><a href="https://video-prediction-policy.github.io/">project</a></td>
<td nowrap><a href="https://github.com/roboterax/video-prediction-policy">code</a></td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN, WAM</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.11423">TASTE-Rob: Advancing Video Generation of Task-Oriented Hand-Object Interaction for Generalizable Robotic Manipulation</a></td>
<td nowrap>TASTE-Rob provides egocentric hand-object interaction video data aligned with language instructions and uses pose refinement to improve video generation.</td>
<td nowrap>video/latent world model</td>
<td nowrap>egocentric hand-object videos</td>
<td nowrap>video demonstrations for imitation</td>
<td nowrap>task-oriented video generation/manipulation</td>
<td nowrap>-</td>
<td nowrap>Address insufficient robot imitation-learning quality caused by inconsistent viewpoints and interaction misalignment in hand-object interaction videos.</td>
<td nowrap><a href="https://arxiv.org/abs/2503.11423">paper</a></td>
<td nowrap><a href="https://taste-rob.github.io/">project</a></td>
<td nowrap><a href="https://github.com/GAP-LAB-CUHK-SZ/TASTE-Rob">code</a></td>
<td nowrap>TASTE-Rob 100,856 videos</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://cvpr.thecvf.com/virtual/2025/poster/34942">GraphMimic: Graph-to-Graphs Generative Modeling from Videos for Policy Learning</a></td>
<td nowrap>GraphMimic abstracts video frames into object and visual action graphs, then generates future graphs as policy conditions.</td>
<td nowrap>video/latent world model</td>
<td nowrap>object/action graphs</td>
<td nowrap>policy conditioned on generated future graphs</td>
<td nowrap>policy learning from videos</td>
<td nowrap>Sim + Real + cross-embodiment</td>
<td nowrap>Address the high cost of action-labeled robot data and the difficulty of learning skills from cross-embodiment videos.</td>
<td nowrap><a href="https://cvpr.thecvf.com/virtual/2025/poster/34942">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
</tbody>
</table>

#### world model for VLA

Total: 10 papers.

<table>
<thead>
<tr>
<th nowrap>Venue/Year</th>
<th nowrap>Paper/Method</th>
<th nowrap>Abstract</th>
<th nowrap>WAM Type</th>
<th nowrap>State Representation</th>
<th nowrap>Action Interface</th>
<th nowrap>Use</th>
<th nowrap>Sim/Real</th>
<th nowrap>Paper Task/Goal</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>Source</th>
<th nowrap>Survey Note</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ECCV 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2602.10098">VLA-JEPA: Enhancing Vision-Language-Action Model with Latent World Model</a></td>
<td nowrap>VLA-JEPA uses JEPA-style latent future-state prediction to pretrain VLA policies without leaking future frames into the input.</td>
<td nowrap>latent world model for VLA</td>
<td nowrap>future-frame latent targets</td>
<td nowrap>latent action tokens + action-head fine-tuning</td>
<td nowrap>VLA pretraining/generalization</td>
<td nowrap>LIBERO, LIBERO-Plus, SimplerEnv, real Franka</td>
<td nowrap>Address appearance bias, nuisance motion, and information leakage in video-pretrained VLA policies.</td>
<td nowrap><a href="https://arxiv.org/abs/2602.10098">paper</a></td>
<td nowrap><a href="https://ginwind.github.io/VLA-JEPA/">project</a></td>
<td nowrap><a href="https://github.com/ginwind/VLA-JEPA">code</a></td>
<td nowrap><a href="https://huggingface.co/ginwind/VLA-JEPA">hf</a></td>
<td nowrap>WAM</td>
<td nowrap>Used to judge whether latent world prediction improves VLA sample efficiency, robustness, and generalization.</td>
</tr>
<tr>
<td nowrap>ICRA 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2509.22643">VLA-Reasoner: Reinforcing Robotic Reasoning and Generalization with World Model</a></td>
<td nowrap>VLA-Reasoner 用世界模型 rollout 和在线 MCTS 为现有 VLA 加入测试时长程推理。</td>
<td nowrap>world model for VLA</td>
<td nowrap>predicted future states</td>
<td nowrap>VLA action candidates</td>
<td nowrap>test-time search and verification</td>
<td nowrap>Sim + Real</td>
<td nowrap>在动作执行前通过世界模型搜索未来结果。</td>
<td nowrap><a href="https://arxiv.org/abs/2509.22643">paper</a></td>
<td nowrap><a href="https://vla-reasoner.github.io/">project</a></td>
<td nowrap><a href="https://github.com/wkguo/VLA-Reasoner">code</a></td>
<td nowrap>-</td>
<td nowrap>ICRA/IROS</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
<tr>
<td nowrap>ICRA 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.10370">LUMOS: Language-Conditioned Imitation Learning with World Models</a></td>
<td nowrap>LUMOS 在 learned world model latent space 中离线练习语言条件长时程 manipulation，再迁移到真机。</td>
<td nowrap>world model for VLA</td>
<td nowrap>latent world state</td>
<td nowrap>language-conditioned action</td>
<td nowrap>offline practice / imitation learning</td>
<td nowrap>Sim + Real</td>
<td nowrap>用世界模型练习降低真实机器人数据需求。</td>
<td nowrap><a href="https://arxiv.org/abs/2503.10370">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>ICRA/IROS</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=fHLtSxDFKC">Genie Envisioner: A Unified World Foundation Platform for Robotic Manipulation</a></td>
<td nowrap>GE jointly learns visual representations and action policies within a video generation framework, supporting cross-embodiment manipulation.</td>
<td nowrap>world model for VLA</td>
<td nowrap>structured video latent</td>
<td nowrap>GE-Act flow-matching decoder/action trajectories</td>
<td nowrap>world foundation platform + policy inference</td>
<td nowrap>-</td>
<td nowrap>Address the separation of world modeling and action policies in robotic manipulation, and the high cost of supervision for generalization.</td>
<td nowrap><a href="https://openreview.net/forum?id=fHLtSxDFKC">paper</a></td>
<td nowrap><a href="https://genie-envisioner.github.io/">project</a></td>
<td nowrap><a href="https://github.com/AgibotTech/Genie-Envisioner-V1">code</a></td>
<td nowrap>&gt;1M manipulation episodes + released benchmarks</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=LQv9LU2Ufg">RIG: Synergizing Reasoning and Imagination in End-to-End Generalist Policy</a></td>
<td nowrap>RIG jointly learns reasoning, action, and next-image imagination in an end-to-end generalist policy.</td>
<td nowrap>world model for VLA</td>
<td nowrap>reasoning + next-image/world dynamics</td>
<td nowrap>reason-then-act with imagined outcome</td>
<td nowrap>self-correction/test-time scaling</td>
<td nowrap>generalist embodied policy benchmarks</td>
<td nowrap>Address embodied agents having only reasoning or imagination as a single capability and inefficient system-level composition.</td>
<td nowrap><a href="https://openreview.net/forum?id=LQv9LU2Ufg">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=qE2FyvRvuF">WMPO: World Model-based Policy Optimization for Vision-Language-Action Models</a></td>
<td nowrap>WMPO performs on-policy GRPO for VLA in imagination using a pixel-level world model.</td>
<td nowrap>world model for VLA</td>
<td nowrap>pixel-based imagined trajectories</td>
<td nowrap>VLA policy actions/GRPO</td>
<td nowrap>imagination-only policy optimization</td>
<td nowrap>Sim + Real</td>
<td nowrap>Address VLA reliance on expert demonstrations and the high sampling cost of real-robot RL.</td>
<td nowrap><a href="https://openreview.net/forum?id=qE2FyvRvuF">paper</a></td>
<td nowrap><a href="https://wm-po.github.io/">project</a></td>
<td nowrap><a href="https://github.com/WM-PO/WMPO">code</a></td>
<td nowrap><a href="https://huggingface.co/fangqi/WMPO">hf</a></td>
<td nowrap>WAM, RL-VLA</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=wPEIStHxYH">Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning</a></td>
<td nowrap>Cosmos Policy fine-tunes a pretrained video model in one stage so it generates actions, future states, and values for planning.</td>
<td nowrap>world model for VLA / video-policy world model</td>
<td nowrap>video model latent frames for actions/states/values</td>
<td nowrap>latent-frame action generation + planning</td>
<td nowrap>visuomotor control/planning</td>
<td nowrap>-</td>
<td nowrap>Address the need for complex multi-stage training and extra action architectures when using video models for robot policies.</td>
<td nowrap><a href="https://openreview.net/forum?id=wPEIStHxYH">paper</a></td>
<td nowrap><a href="https://research.nvidia.com/labs/dir/cosmos-policy/cosmos_policy_index.html">project</a></td>
<td nowrap><a href="https://github.com/nvlabs/cosmos-policy">code</a></td>
<td nowrap>LIBERO, RoboCasa, real bimanual tasks</td>
<td nowrap>EAI-VLA-VLN, WAM</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38925">WorldAgen: Unified State-Action Prediction with Test-Time World Model Training</a></td>
<td nowrap>WorldAgen uses a shared Transformer to predict future states and actions simultaneously, and trains the world model at test time to adapt to new environments.</td>
<td nowrap>world model for VLA</td>
<td nowrap>past state-action trajectories</td>
<td nowrap>agent-model action head + exploratory actions</td>
<td nowrap>test-time adaptation for VLA</td>
<td nowrap>Sim/Benchmark</td>
<td nowrap>Address poor generalization when deploying VLA to new object configurations or dynamics environments under static pretraining.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38925">paper</a></td>
<td nowrap><a href="https://worldagen.github.io/">project</a></td>
<td nowrap><a href="https://github.com/mll-lab-nu/WorldAgen">code</a></td>
<td nowrap>CALVIN, LIBERO</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66169">VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model</a></td>
<td nowrap>VLAW iteratively improves an action-conditioned video world model with real rollouts, then generates synthetic data to improve VLA.</td>
<td nowrap>world model for VLA</td>
<td nowrap>action-conditioned video world model</td>
<td nowrap>VLA actions + generated rollouts</td>
<td nowrap>iterative VLA/world-model co-improvement</td>
<td nowrap>Real + synthetic rollouts</td>
<td nowrap>Address expensive real rollouts and insufficient physical fidelity of existing world models for directly improving policies.</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66169">paper</a></td>
<td nowrap><a href="https://sites.google.com/view/vla-w">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2603.03195">Chain of World: World Model Thinking in Latent Motion</a></td>
<td nowrap>CoWVLA uses a video VAE to extract continuous latent motion chains and jointly fine-tunes them with discrete action prediction.</td>
<td nowrap>world model for VLA / latent motion</td>
<td nowrap>structure and motion latents</td>
<td nowrap>autoregressive action sequence decoder</td>
<td nowrap>VLA pretraining/fine-tuning</td>
<td nowrap>robot simulation benchmarks</td>
<td nowrap>Address redundant background reconstruction in world-model VLA and lack of continuous temporal dynamics in latent-action VLA.</td>
<td nowrap><a href="https://arxiv.org/abs/2603.03195">paper</a></td>
<td nowrap><a href="https://fx-hit.github.io/cowvla-io/">project</a></td>
<td nowrap><a href="https://github.com/fx-hit/CoWVLA">code</a></td>
<td nowrap><a href="https://huggingface.co/hitfx/CoWVLA">hf</a></td>
<td nowrap>-</td>
<td nowrap>Used to judge whether world prediction can support planning and action verification.</td>
</tr>
</tbody>
</table>

### Agentic Planning / Reasoning and Planning

This direction emphasizes task decomposition, memory, failure monitoring, constraint/affordance planning, and self-improving planning. It is closest to the practical system route of agent planning plus smaller execution modules.

Subdirections: task decomposition, memory, failure monitor, constraint / affordance planning, and self-improving planning.

Total: 93 papers.

<table>
<thead>
<tr>
<th nowrap>Subdirection</th>
<th nowrap>Entries</th>
<th nowrap>Focus</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>Task Decomposition</td>
<td nowrap>31</td>
<td nowrap>Examines how high-level instructions are decomposed into executable steps.</td>
</tr>
<tr>
<td nowrap>memory</td>
<td nowrap>11</td>
<td nowrap>Examines long-term memory, experience reuse, and maintaining environment state.</td>
</tr>
<tr>
<td nowrap>failure monitor</td>
<td nowrap>9</td>
<td nowrap>Examines failure detection, recovery, and closed-loop correction.</td>
</tr>
<tr>
<td nowrap>constraint / affordance planning</td>
<td nowrap>10</td>
<td nowrap>Examines constraints, affordances, and physical executability.</td>
</tr>
<tr>
<td nowrap>self-improving planning</td>
<td nowrap>32</td>
<td nowrap>Examines self-improvement, test-time optimization, and accumulation of experience.</td>
</tr>
</tbody>
</table>

#### Task Decomposition

Total: 31 papers.

<table>
<thead>
<tr>
<th nowrap>Venue/Year</th>
<th nowrap>Paper/Method</th>
<th nowrap>Abstract</th>
<th nowrap>Planning Granularity</th>
<th nowrap>Tool/Memory</th>
<th nowrap>Feedback/Self-Improvement</th>
<th nowrap>Execution Interface</th>
<th nowrap>Validation Environment</th>
<th nowrap>Paper Task/Goal</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>Source</th>
<th nowrap>Survey Note</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>IROS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2406.11818">Embodied Instruction Following in Unknown Environments</a></td>
<td nowrap>EIF 在未知家庭环境中把自然语言任务分解为可探索、可执行的高层计划。</td>
<td nowrap>Task Decomposition</td>
<td nowrap>multimodal LLM planner</td>
<td nowrap>visual feedback + exploration</td>
<td nowrap>navigation and interaction policy</td>
<td nowrap>house-level scenes</td>
<td nowrap>未知环境下的长程具身指令跟随。</td>
<td nowrap><a href="https://arxiv.org/abs/2406.11818">paper</a></td>
<td nowrap><a href="https://gary3410.github.io/eif_unknown/">project</a></td>
<td nowrap><a href="https://github.com/Gary3410/eif_unknown">code</a></td>
<td nowrap>-</td>
<td nowrap>ICRA/IROS</td>
<td nowrap>Used to judge whether agentic planning can decompose tasks, maintain memory, detect failure, and recover.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=8xTDnj39Ti">Vlaser: Vision-Language-Action Model with Synergistic Embodied Reasoning</a></td>
<td nowrap>Proposes Vlaser, combining upstream embodied reasoning with downstream VLA policy learning.</td>
<td nowrap>Task Decomposition</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA/action</td>
<td nowrap>Benchmarks for spatial reasoning, embodied grounding, QA, task planning, and related tasks.</td>
<td nowrap>Bridges embodied reasoning and VLA policy learning.</td>
<td nowrap><a href="https://openreview.net/forum?id=8xTDnj39Ti">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=tWMfhoP3as">OneTwoVLA: A Unified Vision-Language-Action Model with Adaptive Reasoning</a></td>
<td nowrap>Unifies System One action and System Two reasoning, with adaptive switching across execution stages.</td>
<td nowrap>Task Decomposition</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>unified VLA/action</td>
<td nowrap>-</td>
<td nowrap>Unifies fast action and explicit reasoning at critical moments in VLA.</td>
<td nowrap><a href="https://openreview.net/forum?id=tWMfhoP3as">paper</a> / <a href="https://arxiv.org/abs/2506.19850">paper</a></td>
<td nowrap><a href="https://robertwyq.github.io/univla.github.io/">project</a></td>
<td nowrap><a href="https://github.com/baaivision/UniVLA">code</a></td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=yngvAamNQi">From Seeing to Doing: Bridging Reasoning and Decision for Robotic Manipulation</a></td>
<td nowrap>Uses spatial-relation reasoning to generate intermediate representations that guide robotic manipulation decisions.</td>
<td nowrap>Task Decomposition</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>Bridges visual understanding and manipulation decisions through spatial-relation reasoning.</td>
<td nowrap><a href="https://openreview.net/forum?id=yngvAamNQi">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=nESyz4PvJL">VLMgineer: Vision-Language Models as Robotic Toolsmiths</a></td>
<td nowrap>Automatically has the VLM design and use tools, shifting control difficulty to tool geometry design.</td>
<td nowrap>Task Decomposition</td>
<td nowrap>tool design/use</td>
<td nowrap>-</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>Uses a VLM to automatically generate tools usable by robots.</td>
<td nowrap><a href="https://openreview.net/forum?id=nESyz4PvJL">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=3eTr9dGwJv">MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Models for Embodied Task Planning</a></td>
<td nowrap>Builds a unified scene graph covering space, function, parts, and state for embodied task planning.</td>
<td nowrap>Task Decomposition</td>
<td nowrap>state-aware scene graph</td>
<td nowrap>-</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>Supports navigation-manipulation planning with a unified scene graph.</td>
<td nowrap><a href="https://openreview.net/forum?id=3eTr9dGwJv">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=8iPwqr6Adk">Theory of Space: Can Foundation Models Construct Spatial Beliefs through Active Exploration?</a></td>
<td nowrap>Proposes Theory of Space to evaluate whether models can actively explore and maintain spatial beliefs.</td>
<td nowrap>active exploration / spatial beliefs</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>Evaluates active construction and revision of spatial beliefs.</td>
<td nowrap><a href="https://openreview.net/forum?id=8iPwqr6Adk">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=EEONns7ae4">Compositional Visual Planning via Inference-Time Diffusion Scaling</a></td>
<td nowrap>Uses diffusion composition scaling at inference time to generate stable long-horizon visual plans.</td>
<td nowrap>long-horizon visual planning</td>
<td nowrap>-</td>
<td nowrap>inference-time scaling</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>Addresses unstable segment stitching in long-horizon planning with diffusion policies.</td>
<td nowrap><a href="https://openreview.net/forum?id=EEONns7ae4">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=Y1VgLHbzCC">One Demo Is All It Takes: Planning Domain Derivation with LLMs from A Single Demonstration</a></td>
<td nowrap>Uses a single demonstration trajectory and an LLM to automatically induce PDDL predicates and actions.</td>
<td nowrap>Task Decomposition</td>
<td nowrap>LLM + PDDL domain induction</td>
<td nowrap>-</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>Automatically derives a symbolic planning domain from a single demonstration.</td>
<td nowrap><a href="https://openreview.net/forum?id=Y1VgLHbzCC">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=tkEmIJv1tB">OmniEVA: Embodied Versatile Planner via Task-Adaptive 3D-Grounded and Embodiment-aware Reasoning</a></td>
<td nowrap>Builds a general embodied planner via task-adaptive 3D grounding and embodiment-constraint reasoning.</td>
<td nowrap>3D-grounded embodied planning</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>planner with embodiment constraints</td>
<td nowrap>-</td>
<td nowrap>Addresses the lack of geometric adaptability and robot embodiment constraints in MLLM planning.</td>
<td nowrap><a href="https://openreview.net/forum?id=tkEmIJv1tB">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=3u6AkbWEls">ManipEvalAgent: Promptable and Efficient Evaluation Framework for Robotic Manipulation Policies</a></td>
<td nowrap>Uses a small number of multi-round executions for fast, promptable evaluation of manipulation policies.</td>
<td nowrap>Task Decomposition</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>Efficiently evaluates robotic manipulation policies.</td>
<td nowrap><a href="https://openreview.net/forum?id=3u6AkbWEls">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=9AA27en4go">Difference-Aware Retrieval Policies for Imitation Learning</a></td>
<td nowrap>Proposes DARP, using difference-aware retrieval to mitigate out-of-distribution generalization in behavior cloning.</td>
<td nowrap>Task Decomposition</td>
<td nowrap>retrieval policy</td>
<td nowrap>-</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>Addresses state shift and accumulated errors when deploying imitation learning.</td>
<td nowrap><a href="https://openreview.net/forum?id=9AA27en4go">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=d1wuA8oIH0">EquAct: An SE(3)-Equivariant Multi-Task Transformer for 3D Robotic Manipulation</a></td>
<td nowrap>Uses an SE(3)-equivariant Transformer to improve generalization of 3D multi-task manipulation to changes in object pose.</td>
<td nowrap>3D manipulation policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>SE(3)-equivariant multi-task manipulation generalization</td>
<td nowrap><a href="https://openreview.net/forum?id=d1wuA8oIH0">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=jXDZJAfRZB">Seeing Across Views: Benchmarking Spatial Reasoning of Vision-Language Models in Robotic Scenes</a></td>
<td nowrap>Proposes MV-RoboBench to evaluate multi-view robotic spatial reasoning in VLMs.</td>
<td nowrap>Task Decomposition</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>Evaluates whether VLMs can fuse multi-camera views to perform robotic spatial reasoning.</td>
<td nowrap><a href="https://openreview.net/forum?id=jXDZJAfRZB">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>MV-RoboBench</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=vmBIF25KLf">REI-Bench: Can Embodied Agents Understand Vague Human Instructions in Task Planning?</a></td>
<td nowrap>Builds REI-Bench to evaluate embodied agents' ability to understand ambiguous referring expressions and plan tasks.</td>
<td nowrap>Task Decomposition</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>embodied task planning under ambiguous human instructions</td>
<td nowrap><a href="https://openreview.net/forum?id=vmBIF25KLf">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>REI-Bench</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=aCVfhY4Qen">PhyScensis: Physics-Augmented LLM Agents for Complex Physical Scene Arrangement</a></td>
<td nowrap>Automatically generates interactive 3D scene layouts and introduces a physics-enhanced LLM agent.</td>
<td nowrap>Task Decomposition</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>physics-enhanced complex scene arrangement planning</td>
<td nowrap><a href="https://openreview.net/forum?id=aCVfhY4Qen">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=oJAIjUDxkZ">OmniActor: A Generalist GUI and Embodied Agent for 2D&amp;3D Worlds</a></td>
<td nowrap>Uses a hierarchical heterogeneous MoE to unify 2D/3D agents for GUI and embodied tasks.</td>
<td nowrap>Task Decomposition</td>
<td nowrap>-</td>
<td nowrap>Task Decomposition</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>Unifies 2D GUI and 3D embodied task execution.</td>
<td nowrap><a href="https://arxiv.org/abs/2509.02322">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/UITron-hub/OmniActor">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38896">GraphCoT-VLA: A 3D Spatial-Aware Reasoning Vision-Language-Action Model for Robotic Manipulation with Ambiguous Instructions</a></td>
<td nowrap>-</td>
<td nowrap>Task Decomposition</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA/action</td>
<td nowrap>-</td>
<td nowrap>3D spatial-reasoning VLA under ambiguous instructions</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38896">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38900">PhyPlan: Learning to Plan Tasks with Generalizable and Rapid Physical Reasoning for Embodied Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>Task Decomposition</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>physics-reasoning-driven manipulation task planning</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38900">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38906">Cook and Clean Together: Teaching Embodied Agents for Parallel Task Execution</a></td>
<td nowrap>-</td>
<td nowrap>parallel task execution</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>parallel task execution planning</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38906">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38911">FoAM: Foresight-Augmented Multi-Task Imitation Policy for Robotic Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>Task Decomposition</td>
<td nowrap>-</td>
<td nowrap>foresight augmentation</td>
<td nowrap>VLA/action</td>
<td nowrap>-</td>
<td nowrap>lookahead-enhanced multi-task manipulation imitation</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38911">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38936">Zero-Shot Robotic Manipulation via 3D Gaussian Splatting-Enhanced Multimodal Retrieval-Augmented Generation</a></td>
<td nowrap>-</td>
<td nowrap>Task Decomposition</td>
<td nowrap>3D Gaussian Splatting + multimodal RAG</td>
<td nowrap>-</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>Enhances multimodal RAG with 3DGS to support zero-shot robotic manipulation.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38936">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Humanoid-RL, EAI-Safety, WAM</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38958">H-GAR: A Hierarchical Interaction Framework via Goal-Driven Observation-Action Refinement for Robotic Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>hierarchical observation-action refinement</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA/action</td>
<td nowrap>-</td>
<td nowrap>Performs hierarchical manipulation interaction through goal-driven observation-action refinement.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38958">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/60500">TapSampling: Inference-Time Sampling with a Task-Progress-Understanding Verifier for Robotic Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>Task Decomposition</td>
<td nowrap>-</td>
<td nowrap>inference-time verifier</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>Uses a task-progress-aware verifier to filter manipulation samples at inference time.</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/60500">paper</a></td>
<td nowrap><a href="https://aipixel.github.io/TapSampling/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/63250">Decompose and Recompose: Reasoning New Skills from Existing Abilities for Cross-Task Robotic Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>Task Decomposition</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>Reasons over existing skills to compose new manipulation skills.</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/63250">paper</a></td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/63250">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.09937">SAFE: Multitask Failure Detection for Vision-Language-Action Models</a></td>
<td nowrap>Proposes SAFE, a multi-task failure detector that enables VLA to detect failures in new tasks in time.</td>
<td nowrap>Failure Monitor</td>
<td nowrap>-</td>
<td nowrap>Failure Monitor</td>
<td nowrap>VLA/action</td>
<td nowrap>LIBERO, SimplerEnv, real-world Franka/WidowX rollouts</td>
<td nowrap>multi-task VLA failure detection</td>
<td nowrap><a href="https://arxiv.org/abs/2506.09937">paper</a></td>
<td nowrap><a href="https://vla-safe.github.io/">project</a></td>
<td nowrap><a href="https://github.com/vla-safe/SAFE">code</a></td>
<td nowrap>-</td>
<td nowrap>Awesome-EAI, EAI-VLA-VLN, Humanoid-RL, EAI-Safety</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2510.21302">Towards Reliable Code-as-Policies: A Neuro-Symbolic Framework for Embodied Task Planning</a></td>
<td nowrap>Adds symbolic verification and interactive checking to code-as-policies generation.</td>
<td nowrap>Task Decomposition</td>
<td nowrap>neuro-symbolic verification</td>
<td nowrap>interactive validation</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>Addresses insufficient grounding of LLM-generated control code in dynamic or partially observable environments.</td>
<td nowrap><a href="https://arxiv.org/abs/2510.21302">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2510.14968">RDD: Retrieval-Based Demonstration Decomposer for Planner Alignment in Long-Horizon Tasks</a></td>
<td nowrap>Uses a retrieval-based demonstration decomposer to automatically generate subtasks aligned with low-level policies.</td>
<td nowrap>Task Decomposition</td>
<td nowrap>retrieval-based demonstration decomposition</td>
<td nowrap>-</td>
<td nowrap>agent planner / planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>Addresses mismatch between subtask decomposition and execution policies in long-horizon VLA planners.</td>
<td nowrap><a href="https://arxiv.org/abs/2510.14968">paper</a></td>
<td nowrap><a href="https://rdd-neurips.github.io/">project</a></td>
<td nowrap><a href="https://github.com/tasl-lab/Retrieval-Demonstration-Decomposer">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2507.21545">UniDomain: Pretraining a Unified PDDL Domain from Real-World Demonstrations for Generalizable Robot Task Planning</a></td>
<td nowrap>Pretrains a unified PDDL domain from 12,393 manipulation videos for online task planning.</td>
<td nowrap>Task Decomposition</td>
<td nowrap>unified PDDL domain</td>
<td nowrap>Task Decomposition</td>
<td nowrap>planning / reasoning / RL</td>
<td nowrap>real manipulation demonstration videos and online planning</td>
<td nowrap>Addresses the dependence of symbolic planning on manually crafted narrow domains and its poor generalization.</td>
<td nowrap><a href="https://arxiv.org/abs/2507.21545">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.21230">World-aware Planning Narratives Enhance Large Vision-Language Model Planner</a></td>
<td nowrap>Injects environmental context into an LVLM planner through world-aware planning narratives.</td>
<td nowrap>Task Decomposition</td>
<td nowrap>-</td>
<td nowrap>world-aware planning narrative enhancement</td>
<td nowrap>agent planner / planning / RL</td>
<td nowrap>-</td>
<td nowrap>Addresses insufficient model understanding of environmental context and multi-step goals in long-horizon interaction.</td>
<td nowrap><a href="https://arxiv.org/abs/2506.21230">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2412.18194">VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics Manipulation with Long-Horizon Reasoning Tasks</a></td>
<td nowrap>Provides a VLA benchmark for long-horizon reasoning in language-conditioned manipulation.</td>
<td nowrap>Task Decomposition</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>VLA/action</td>
<td nowrap>100-task VLABench; interactive VLA/workflow + non-interactive VLM evaluation</td>
<td nowrap>Evaluates general VLA capabilities on long-horizon language-conditioned manipulation tasks.</td>
<td nowrap><a href="https://arxiv.org/abs/2412.18194">paper</a> / <a href="https://arxiv.org/pdf/2412.18194">paper</a></td>
<td nowrap><a href="https://vlabench.github.io/">project</a></td>
<td nowrap><a href="https://github.com/OpenMOSS/VLABench">code</a></td>
<td nowrap>VLABench HF</td>
<td nowrap>HCP-Survey, Awesome-EAI, EAI-VLA-VLN, WAM</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
</tbody>
</table>

#### memory

Total: 11 papers.

<table>
<thead>
<tr>
<th nowrap>Venue/Year</th>
<th nowrap>Paper/Method</th>
<th nowrap>Abstract</th>
<th nowrap>Planning Granularity</th>
<th nowrap>Tool/Memory</th>
<th nowrap>Feedback/Self-Improvement</th>
<th nowrap>Execution Interface</th>
<th nowrap>Validation Environment</th>
<th nowrap>Paper Task/Goal</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>Source</th>
<th nowrap>Survey Note</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>IROS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2410.11989">Dynamic Open-Vocabulary 3D Scene Graphs for Long-Term Language-Guided Mobile Manipulation</a></td>
<td nowrap>DovSG 用动态开放词汇 3D scene graph 支撑长期语言任务、环境更新和移动操作。</td>
<td nowrap>Memory Planning</td>
<td nowrap>dynamic 3D scene graph</td>
<td nowrap>long-term scene updates</td>
<td nowrap>mobile manipulation planner</td>
<td nowrap>Real robot</td>
<td nowrap>用开放词汇场景图维护长期任务记忆。</td>
<td nowrap><a href="https://arxiv.org/abs/2410.11989">paper</a></td>
<td nowrap><a href="https://bjhyzj.github.io/dovsg-web/">project</a></td>
<td nowrap><a href="https://github.com/BJHYZJ/DovSG">code</a></td>
<td nowrap>-</td>
<td nowrap>ICRA/IROS</td>
<td nowrap>Used to judge whether agentic planning can decompose tasks, maintain memory, detect failure, and recover.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=1dH4ARGdwD">Scaling up Memory for Robotic Control via Experience Retrieval</a></td>
<td nowrap>MemER fine-tunes a VLM to retrieve task-relevant keyframes, enabling VLA to handle minute-scale long-horizon memory tasks.</td>
<td nowrap>Memory Planning</td>
<td nowrap>experience retrieval/keyframe memory</td>
<td nowrap>-</td>
<td nowrap>VLA/action</td>
<td nowrap>-</td>
<td nowrap>Addresses retrieval and reuse of long-duration experiential memory in robot control.</td>
<td nowrap><a href="https://openreview.net/forum?id=1dH4ARGdwD">paper</a></td>
<td nowrap><a href="https://jen-pan.github.io/memer/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=79BOATBal9">Planning with an Embodied Learnable Memory</a></td>
<td nowrap>EPM uses a VLM to maintain textual scene memory through additions, deletions, and edits for LLM planning.</td>
<td nowrap>Memory Planning</td>
<td nowrap>Embodied Perception Memory</td>
<td nowrap>-</td>
<td nowrap>memory</td>
<td nowrap>PARTNR / dynamic indoor mobile manipulation</td>
<td nowrap>Addresses memory updates and planner access to environment state in dynamic household mobile manipulation.</td>
<td nowrap><a href="https://openreview.net/forum?id=79BOATBal9">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=9cLPurIZMj">Memory, Benchmark &amp; Robots: A Benchmark for Solving Complex Tasks with Reinforcement Learning</a></td>
<td nowrap>Proposes MIKASA/MIKASA-Robo to evaluate RL agents on memory-intensive task capabilities.</td>
<td nowrap>Memory Planning</td>
<td nowrap>Memory Planning</td>
<td nowrap>-</td>
<td nowrap>memory</td>
<td nowrap>-</td>
<td nowrap>Provides standardized evaluation of memory capabilities in robotic manipulation.</td>
<td nowrap><a href="https://openreview.net/forum?id=9cLPurIZMj">paper</a></td>
<td nowrap><a href="https://sites.google.com/view/memorybenchrobots/">project</a></td>
<td nowrap><a href="https://github.com/CognitiveAISystems/MIKASA-Robo">code</a></td>
<td nowrap>MIKASA/MIKASA-Robo</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=E5L43l5EIu">Embodied Agents Meet Personalization: Investigating Challenges and Solutions Through the Lens of Memory Utilization</a></td>
<td nowrap>-</td>
<td nowrap>Memory Planning</td>
<td nowrap>Memory Planning</td>
<td nowrap>-</td>
<td nowrap>memory</td>
<td nowrap>-</td>
<td nowrap>enhances long-term task memory</td>
<td nowrap><a href="https://openreview.net/forum?id=E5L43l5EIu">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-Safety</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/60897">HiMe: Hierarchical Embodied Memory for Long-Horizon Vision-Language-Action Control</a></td>
<td nowrap>-</td>
<td nowrap>Memory Planning</td>
<td nowrap>Memory Planning</td>
<td nowrap>-</td>
<td nowrap>VLA/action</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/60897">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66214">Spatial Memory for Out-of-Vision Manipulation in Vision-Language-Action</a></td>
<td nowrap>-</td>
<td nowrap>Memory Planning</td>
<td nowrap>Memory Planning</td>
<td nowrap>-</td>
<td nowrap>VLA/action</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66214">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2602.20200">Global Prior Meets Local Consistency: Dual-Memory Augmented Vision-Language-Action Model for Efficient Robotic Manipulation</a></td>
<td nowrap>Uses global prior memory and local behavior memory to improve the efficiency and robustness of VLA action generation.</td>
<td nowrap>Memory Planning</td>
<td nowrap>dual memory</td>
<td nowrap>-</td>
<td nowrap>VLA/action</td>
<td nowrap>-</td>
<td nowrap>Addresses inefficient VLA action generation and unstable conditioning.</td>
<td nowrap><a href="https://arxiv.org/abs/2602.20200">paper</a></td>
<td nowrap><a href="https://cybertronagent.github.io/OptimusVLA.github.io/">project</a></td>
<td nowrap><a href="https://github.com/iLearn-Lab/CVPR26-OptimusVLA">code</a></td>
<td nowrap><a href="https://huggingface.co/iLearn-Lab/OptimusVLA_Memory">hf</a></td>
<td nowrap>Efficient-VLA</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2501.00358">Embodied VideoAgent: Persistent Memory from Egocentric Videos and Embodied Sensors Enables Dynamic Scene Understanding</a></td>
<td nowrap>Builds persistent scene memory from egocentric video, depth, and pose.</td>
<td nowrap>Memory Planning</td>
<td nowrap>persistent object memory + tool queries</td>
<td nowrap>-</td>
<td nowrap>LLM tool calls + embodied action primitives</td>
<td nowrap>Ego4D-VQ3D, OpenEQA, EnvQA, real-world Franka demo</td>
<td nowrap>Addresses long-term memory and object-state updates in dynamic 3D scene understanding.</td>
<td nowrap><a href="https://arxiv.org/abs/2501.00358">paper</a></td>
<td nowrap><a href="https://embodied-videoagent.github.io/">project</a></td>
<td nowrap><a href="https://github.com/Embodied-VideoAgent/embodied-videoagent">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/1915">Towards Long-Horizon Vision-Language-Action System: Reasoning, Acting and Memory</a></td>
<td nowrap>-</td>
<td nowrap>Memory Planning</td>
<td nowrap>Memory Planning</td>
<td nowrap>-</td>
<td nowrap>VLA/action</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/1915">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICML 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2501.18564">SAM2Act: Integrating Visual Foundation Model with a Memory Architecture for Robotic Manipulation</a></td>
<td nowrap>SAM2Act combines a vision foundation model with a memory architecture to improve multi-task manipulation generalization.</td>
<td nowrap>Memory Planning</td>
<td nowrap>Memory Planning</td>
<td nowrap>-</td>
<td nowrap>memory</td>
<td nowrap>-</td>
<td nowrap>Addresses insufficient generalization and spatial memory in manipulation policies for dynamic environments.</td>
<td nowrap><a href="https://arxiv.org/abs/2501.18564">paper</a></td>
<td nowrap><a href="https://sam2act.github.io">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
</tbody>
</table>

#### failure monitor

Total: 9 papers.

<table>
<thead>
<tr>
<th nowrap>Venue/Year</th>
<th nowrap>Paper/Method</th>
<th nowrap>Abstract</th>
<th nowrap>Planning Granularity</th>
<th nowrap>Tool/Memory</th>
<th nowrap>Feedback/Self-Improvement</th>
<th nowrap>Execution Interface</th>
<th nowrap>Validation Environment</th>
<th nowrap>Paper Task/Goal</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>Source</th>
<th nowrap>Survey Note</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ICRA 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2510.16281">Do What You Say: Grounding Language-Conditioned Robotic Actions with Vision-Language Models</a></td>
<td nowrap>该方法运行时检查 VLA 文本推理和动作结果是否一致，再选择是否执行动作。</td>
<td nowrap>Failure Monitor</td>
<td nowrap>VLM reasoning checker</td>
<td nowrap>reasoning-action consistency</td>
<td nowrap>VLA action selection</td>
<td nowrap>Real robot manipulation</td>
<td nowrap>检测“说的计划”和“做的动作”是否一致。</td>
<td nowrap><a href="https://arxiv.org/abs/2510.16281">paper</a></td>
<td nowrap><a href="https://yilin-wu98.github.io/steering-reasoning-vla/">project</a></td>
<td nowrap><a href="https://github.com/NVlabs/actalign">code</a></td>
<td nowrap><a href="https://github.com/NVlabs/actalign">data</a></td>
<td nowrap>ICRA/IROS</td>
<td nowrap>Used to judge whether agentic planning can decompose tasks, maintain memory, detect failure, and recover.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=N22lDHYrXe">Experience-based Knowledge Correction for Robust Planning in Minecraft</a></td>
<td nowrap>XENON revises dependency graphs and action knowledge from experience to improve the robustness of long-horizon planning in Minecraft.</td>
<td nowrap>Failure Monitor</td>
<td nowrap>experience-based knowledge correction</td>
<td nowrap>Failure Monitor</td>
<td nowrap>failure monitor</td>
<td nowrap>Minecraft</td>
<td nowrap>Addresses incorrect initial LLM knowledge that is difficult to correct through feedback.</td>
<td nowrap><a href="https://openreview.net/forum?id=N22lDHYrXe">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=WC6MJ5r5Bj">ReCAPA: Hierarchical Predictive Correction to Mitigate Cascading Failures</a></td>
<td nowrap>ReCAPA predicts and corrects deviations at the action, subgoal, and trajectory levels to suppress cascading failures.</td>
<td nowrap>Failure Monitor</td>
<td nowrap>-</td>
<td nowrap>hierarchical predictive correction</td>
<td nowrap>failure monitor</td>
<td nowrap>-</td>
<td nowrap>Addresses propagation of local errors through multi-step VLA execution.</td>
<td nowrap><a href="https://arxiv.org/abs/2604.21232">paper</a></td>
<td nowrap><a href="https://sunandreas0437-svg.github.io/recapa-project-page/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=jr9hGWQioP">Self-Refining Vision Language Model for Robotic Failure Detection and Reasoning</a></td>
<td nowrap>ARMOR models failure detection and natural-language cause explanation as a multi-round self-refinement task.</td>
<td nowrap>Failure Monitor</td>
<td nowrap>-</td>
<td nowrap>self-refinement</td>
<td nowrap>failure monitor</td>
<td nowrap>-</td>
<td nowrap>Addresses subtle, combinatorial real-robot failures with scarce annotations.</td>
<td nowrap><a href="https://arxiv.org/abs/2602.12405">paper</a></td>
<td nowrap><a href="https://sites.google.com/utexas.edu/armor">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61750">Sentinel-VLA: A Metacognitive VLA Model with Active Status Monitoring for Dynamic Reasoning and Error Recovery</a></td>
<td nowrap>-</td>
<td nowrap>Failure Monitor</td>
<td nowrap>-</td>
<td nowrap>Failure Monitor</td>
<td nowrap>VLA/action</td>
<td nowrap>-</td>
<td nowrap>detects and repairs execution failures</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61750">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/63650">NeurVLA: Unleashing Failure-Handling Capability of Vision-Language-Action Models via Neural-Symbolic Reasoning</a></td>
<td nowrap>-</td>
<td nowrap>Failure Monitor</td>
<td nowrap>-</td>
<td nowrap>Failure Monitor</td>
<td nowrap>VLA/action</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/63650">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64203">Can VLMs Diagnose and Recover from VLA Manipulation Faults?</a></td>
<td nowrap>-</td>
<td nowrap>Failure Monitor</td>
<td nowrap>-</td>
<td nowrap>Failure Monitor</td>
<td nowrap>VLA/action</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64203">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2510.09459">Failure Prediction at Runtime for Generative Robot Policies</a></td>
<td nowrap>FIPER predicts runtime failures of generative imitation policies without requiring failure data.</td>
<td nowrap>Failure Monitor</td>
<td nowrap>-</td>
<td nowrap>runtime failure prediction</td>
<td nowrap>failure monitor</td>
<td nowrap>-</td>
<td nowrap>Addresses early failure prediction when deploying diffusion/flow manipulation policies.</td>
<td nowrap><a href="https://arxiv.org/abs/2510.09459">paper</a></td>
<td nowrap><a href="https://tum-lsy.github.io/fiper_website">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2412.04455">Code-as-Monitor: Constraint-aware Visual Programming for Reactive and Proactive Robotic Failure Detection</a></td>
<td nowrap>Uses a VLM to generate constraint-monitoring code for both reactive and preventive failure detection.</td>
<td nowrap>Failure Monitor</td>
<td nowrap>VLM-generated monitor code + constraint elements</td>
<td nowrap>Failure Monitor</td>
<td nowrap>closed-loop monitor over open-loop policy</td>
<td nowrap>CLIPort, OmniGibson, real-world</td>
<td nowrap>Addresses real-time detection and prevention of open-set robot failures.</td>
<td nowrap><a href="https://arxiv.org/abs/2412.04455">paper</a></td>
<td nowrap><a href="https://zhoues.github.io/Code-as-Monitor/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>HCP-Survey, Awesome-EAI</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
</tbody>
</table>

#### constraint / affordance planning

Total: 10 papers.

<table>
<thead>
<tr>
<th nowrap>Venue/Year</th>
<th nowrap>Paper/Method</th>
<th nowrap>Abstract</th>
<th nowrap>Planning Granularity</th>
<th nowrap>Tool/Memory</th>
<th nowrap>Feedback/Self-Improvement</th>
<th nowrap>Execution Interface</th>
<th nowrap>Validation Environment</th>
<th nowrap>Paper Task/Goal</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>Source</th>
<th nowrap>Survey Note</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ICRA 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2408.14769">Points2Plans: From Point Clouds to Long-Horizon Plans with Composable Relational Dynamics</a></td>
<td nowrap>Points2Plans 从点云和语言指令出发，用关系动力学连接高层计划和连续参数规划。</td>
<td nowrap>Constraint / Affordance Planning</td>
<td nowrap>point-cloud relational dynamics</td>
<td nowrap>composable planning feedback</td>
<td nowrap>continuous parameter planner</td>
<td nowrap>Sim + Real</td>
<td nowrap>把语言计划落到可执行的 3D 关系动力学约束。</td>
<td nowrap><a href="https://arxiv.org/abs/2408.14769">paper</a></td>
<td nowrap><a href="https://sites.google.com/stanford.edu/points2plans">project</a></td>
<td nowrap><a href="https://github.com/yixuanhuang98/Points2Plans">code</a></td>
<td nowrap>-</td>
<td nowrap>ICRA/IROS</td>
<td nowrap>Used to judge whether agentic planning can decompose tasks, maintain memory, detect failure, and recover.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=enprG5H9aD">SLAP: Shortcut Learning for Abstract Planning</a></td>
<td nowrap>SLAP automatically discovers low-level shortcut options from existing TAMP options.</td>
<td nowrap>TAMP option/shortcut learning</td>
<td nowrap>-</td>
<td nowrap>Constraint/Affordance</td>
<td nowrap>planning / affordance</td>
<td nowrap>-</td>
<td nowrap>Addresses the reliance of TAMP abstract actions on manual definitions and the resulting limited behavior space.</td>
<td nowrap><a href="https://openreview.net/forum?id=enprG5H9aD">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=kWCNhRdcDI">Natural Language PDDL (NL-PDDL) for Open-world Goal-oriented Commonsense Regression Planning in Embodied AI</a></td>
<td nowrap>Uses natural-language PDDL for open-world goal-regression planning.</td>
<td nowrap>commonsense regression planning</td>
<td nowrap>NL-PDDL</td>
<td nowrap>Constraint/Affordance</td>
<td nowrap>planning / affordance</td>
<td nowrap>-</td>
<td nowrap>Addresses long-horizon causal planning in open worlds with partial observability and incomplete knowledge.</td>
<td nowrap><a href="https://openreview.net/forum?id=kWCNhRdcDI">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=refcXHU1Nh">SafeFlowMatcher: Safe and Fast Planning using Flow Matching with Control Barrier Functions</a></td>
<td nowrap>Combines a flow matching planner with control barrier functions to ensure fast and safe planning.</td>
<td nowrap>Constraint/Affordance</td>
<td nowrap>CBF safety constraints</td>
<td nowrap>prediction-correction integrator</td>
<td nowrap>VLA/action</td>
<td nowrap>-</td>
<td nowrap>Addresses the lack of formal safety constraints in generative path planning.</td>
<td nowrap><a href="https://openreview.net/forum?id=refcXHU1Nh">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=bGPDviEtZ1">MoMaGen: Generating Demonstrations under Soft and Hard Constraints for Multi-Step Bimanual Mobile Manipulation</a></td>
<td nowrap>Automatically generates multi-step bimanual mobile-manipulation demonstrations under soft and hard constraints.</td>
<td nowrap>constraint-conditioned demonstration generation</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>planning / affordance</td>
<td nowrap>-</td>
<td nowrap>Addresses the high cost of collecting multi-step bimanual mobile-manipulation demonstrations.</td>
<td nowrap><a href="https://openreview.net/forum?id=bGPDviEtZ1">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38907">A3D: Adaptive Affordance Assembly with Dual-Arm Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>Constraint/Affordance</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>planning / affordance</td>
<td nowrap>-</td>
<td nowrap>dual-arm adaptive affordance assembly</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38907">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38909">Affordance-Guided Coarse-to-Fine Exploration for Base Placement in Open-Vocabulary Mobile Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>coarse-to-fine base placement</td>
<td nowrap>affordance guidance</td>
<td nowrap>-</td>
<td nowrap>planning / affordance</td>
<td nowrap>-</td>
<td nowrap>Uses affordances to guide base-placement exploration in open-vocabulary mobile manipulation.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38909">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38955">Gentle Manipulation Policy Learning via Demonstrations from VLM Planned Atomic Skills</a></td>
<td nowrap>-</td>
<td nowrap>Constraint/Affordance</td>
<td nowrap>VLM-planned atomic skills</td>
<td nowrap>-</td>
<td nowrap>VLA/action</td>
<td nowrap>-</td>
<td nowrap>gentle manipulation policy learning</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38955">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://openreview.net/forum?id=wr47LsSUjH">InstructFlow: Adaptive Symbolic Constraint-Guided Code Generation for Long-Horizon Planning</a></td>
<td nowrap>InstructFlow uses symbolic feedback flows to inject failure-induced constraints into instruction graphs and code generation.</td>
<td nowrap>Constraint/Affordance</td>
<td nowrap>Constraint/Affordance</td>
<td nowrap>failure diagnosis + symbolic constraints</td>
<td nowrap>flow matching / planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>Addresses hallucinated long-horizon planning code from LLMs, physical infeasibility, and poor failure recovery.</td>
<td nowrap><a href="https://openreview.net/forum?id=wr47LsSUjH">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/chiht21/InstructFlow">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/542">CoA-VLA: Improving Vision-Language-Action Models via Visual-Text Chain-of-Affordance</a></td>
<td nowrap>Uses visual-text affordance chains to enhance VLA reasoning at test time.</td>
<td nowrap>Constraint/Affordance</td>
<td nowrap>-</td>
<td nowrap>test-time affordance reasoning</td>
<td nowrap>VLA/action</td>
<td nowrap>-</td>
<td nowrap>Addresses insufficient self-driven affordance reasoning and robust action in VLA.</td>
<td nowrap><a href="https://openaccess.thecvf.com/content/ICCV2025/papers/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.pdf">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
</tbody>
</table>

#### self-improving planning

Total: 32 papers.

<table>
<thead>
<tr>
<th nowrap>Venue/Year</th>
<th nowrap>Paper/Method</th>
<th nowrap>Abstract</th>
<th nowrap>Planning Granularity</th>
<th nowrap>Tool/Memory</th>
<th nowrap>Feedback/Self-Improvement</th>
<th nowrap>Execution Interface</th>
<th nowrap>Validation Environment</th>
<th nowrap>Paper Task/Goal</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>Source</th>
<th nowrap>Survey Note</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=SzUgx5r3wy">Self-Improving Loops for Visual Robotic Planning</a></td>
<td nowrap>Enables a visual robot planner to continually improve through online self-collected behavior.</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>-</td>
<td nowrap>self-improving online loop</td>
<td nowrap>planning / reasoning / RL</td>
<td nowrap>-</td>
<td nowrap>Addresses poor generalization of visual generative planners to unseen tasks.</td>
<td nowrap><a href="https://openreview.net/forum?id=SzUgx5r3wy">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, EAI-Safety, WAM, RL-VLA</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=Vsy3nAnaX6">BOLT: Decision‑Aligned Distillation and Budget-Aware Routing for Constrained Multimodal QA on Robots</a></td>
<td nowrap>Satisfies robotic multimodal QA constraints through decision-alignment distillation and budget-aware routing.</td>
<td nowrap>constrained multimodal QA routing</td>
<td nowrap>-</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>planning / reasoning / RL</td>
<td nowrap>-</td>
<td nowrap>decision quality and efficiency under robot constraints</td>
<td nowrap><a href="https://openreview.net/forum?id=Vsy3nAnaX6">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=eJcCW9oNfH">EVLP: Learning Unified Embodied Vision-Language Planner with Reinforced Supervised Fine-Tuning</a></td>
<td nowrap>EVLP jointly generates language reasoning and visual imagination, and learns planning through reinforced supervised fine-tuning.</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>-</td>
<td nowrap>reinforced supervised fine-tuning</td>
<td nowrap>embodied vision-language planner</td>
<td nowrap>-</td>
<td nowrap>Addresses inconsistency between language logic and visual spatial planning in long-horizon manipulation.</td>
<td nowrap><a href="https://openreview.net/forum?id=eJcCW9oNfH">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=i5wlozMFsQ">Embodied-R1: Reinforced Embodied Reasoning for General Robotic Manipulation</a></td>
<td nowrap>Uses pointing as an embodiment-agnostic intermediate representation to train a 3B embodied-reasoning VLM.</td>
<td nowrap>embodied reasoning/pointing</td>
<td nowrap>-</td>
<td nowrap>reinforced reasoning</td>
<td nowrap>planning / reasoning / RL</td>
<td nowrap>-</td>
<td nowrap>Addresses the seeing-to-doing gap between high-level vision-language understanding and low-level action primitives.</td>
<td nowrap><a href="https://openreview.net/forum?id=i5wlozMFsQ">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38922">ManipLVM-R1: Reinforcement Learning for Reasoning in Embodied Manipulation with Large Vision-Language Models</a></td>
<td nowrap>-</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>-</td>
<td nowrap>RL for embodied manipulation reasoning</td>
<td nowrap>planning / reasoning / RL</td>
<td nowrap>-</td>
<td nowrap>Uses reinforcement learning to improve embodied manipulation reasoning in large vision-language models.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38922">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61922">HALO: A Unified Vision-Language-Action Model for Embodied Multimodal Chain-of-Thought Reasoning</a></td>
<td nowrap>-</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>-</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>VLA/action</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61922">paper</a> / <a href="https://arxiv.org/abs/2506.19850">paper</a></td>
<td nowrap><a href="https://robertwyq.github.io/univla.github.io/">project</a></td>
<td nowrap><a href="https://github.com/baaivision/UniVLA">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64290">Latent Reasoning VLA: Latent Thinking and Prediction for Vision-Language-Action Models</a></td>
<td nowrap>LaRA-VLA internalizes multimodal CoT as continuous latent variables to reduce reasoning latency.</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>-</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>VLA/action</td>
<td nowrap>-</td>
<td nowrap>Addresses the high cost of explicit CoT reasoning and the mismatch between discrete representations and continuous control.</td>
<td nowrap><a href="https://arxiv.org/abs/2602.01166">paper</a></td>
<td nowrap><a href="https://loveju1y.github.io/Latent-Reasoning-VLA/">project</a></td>
<td nowrap><a href="https://github.com/LoveJu1y/LaRA-VLA">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61887">LaST0: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model</a></td>
<td nowrap>-</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>-</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>VLA/action</td>
<td nowrap>-</td>
<td nowrap>Uses latent spatiotemporal CoT to support robotic VLA reasoning.</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61887">paper</a></td>
<td nowrap><a href="https://vla-last0.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/60801">LAGEA: Language Guided Embodied Agents for Robotic Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>-</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/60801">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64055">Drift is a Sampling Error: SNR-Aware Power Distributions for Long-Horizon Robotic Planning</a></td>
<td nowrap>-</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>-</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>self-improves planning through feedback</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64055">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2601.11404">ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models</a></td>
<td nowrap>Proposes Action CoT, using fine-grained action reasoning directly as an intermediate representation for VLA.</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>-</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>VLA/action</td>
<td nowrap>-</td>
<td nowrap>Addresses the inability of language/visual intermediate reasoning to fully convey fine-grained action information.</td>
<td nowrap><a href="https://arxiv.org/abs/2601.11404">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Reasoning2Action-Sim</td>
<td nowrap>Awesome-EAI</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2601.09708">Fast-ThinkAct: Efficient Vision-Language-Action Reasoning via Verbalizable Latent Planning</a></td>
<td nowrap>Uses verbalizable latent planning to distill explicit CoT, reducing latency while preserving performance.</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>-</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>VLA/action</td>
<td nowrap>-</td>
<td nowrap>Addresses slow execution caused by overly long explicit CoT in reasoning-based VLA.</td>
<td nowrap><a href="https://arxiv.org/abs/2601.09708">paper</a></td>
<td nowrap><a href="https://jasper0314-huang.github.io/fast-thinkact/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.01953">Fast-in-Slow: A Dual-System VLA Model Unifying Fast Manipulation within Slow Reasoning</a></td>
<td nowrap>Builds a dual-system VLA from a slow VLM reasoning module and a high-speed action module.</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>-</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>dual-system VLA: slow reasoning + high-frequency action module</td>
<td nowrap>RLBench + AlphaBot/Agilex real robot</td>
<td nowrap>Addresses the difficulty of balancing high-level reasoning and high-frequency control in complex manipulation.</td>
<td nowrap><a href="https://arxiv.org/abs/2506.01953">paper</a></td>
<td nowrap><a href="https://fast-in-slow.github.io/">project</a></td>
<td nowrap><a href="https://github.com/CHEN-H01/Fast-in-Slow">code</a></td>
<td nowrap><a href="https://huggingface.co/chenhao01/fisvla/tree/main">hf</a></td>
<td nowrap>EAI-VLA-VLN, Efficient-VLA</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2505.21906">ChatVLA-2: Vision-Language-Action Model with Open-World Embodied Reasoning from Pretrained Knowledge</a></td>
<td nowrap>Preserves the open-world knowledge of a pretrained VLM and converts it into executable actions.</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>-</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>VLA/action</td>
<td nowrap>-</td>
<td nowrap>Addresses the loss of open-world reasoning ability after VLA fine-tuning.</td>
<td nowrap><a href="https://arxiv.org/abs/2505.21906">paper</a></td>
<td nowrap><a href="https://chatvla-2.github.io/">project</a></td>
<td nowrap><a href="https://github.com/tutujingyugang1/ChatVLA_public">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.17561">VLA-OS: Structuring and Dissecting Planning Representations and Paradigms in Vision-Language-Action Models</a></td>
<td nowrap>Systematically compares how task-planning representations, paradigms, and data sources affect VLA performance.</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>-</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>VLA/action</td>
<td nowrap>LIBERO, Colosseum, FurnitureBench, DexArt, etc.</td>
<td nowrap>Addresses the difficulty of attributing the sources of planning improvements in VLA.</td>
<td nowrap><a href="https://arxiv.org/abs/2506.17561">paper</a></td>
<td nowrap><a href="https://nus-lins-lab.github.io/vlaos/">project</a></td>
<td nowrap><a href="https://github.com/HeegerGao/VLA-OS">code</a></td>
<td nowrap><a href="https://huggingface.co/datasets/Linslab/VLA-OS-Dataset">hf</a></td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2507.16815">ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning</a></td>
<td nowrap>Uses action-aligned visual rewards to reinforce high-level visual latent planning.</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>-</td>
<td nowrap>reinforced visual latent planning</td>
<td nowrap>VLA/action</td>
<td nowrap>SimplerEnv, LIBERO, EgoPlan-Bench2, RoboVQA, OpenEQA</td>
<td nowrap>Addresses the lack of explicit multi-step reasoning and complex-task adaptability in VLA.</td>
<td nowrap><a href="https://arxiv.org/abs/2507.16815">paper</a> / <a href="https://neurips.cc/virtual/2025/loc/san-diego/poster/119747">paper</a></td>
<td nowrap><a href="https://jasper0314-huang.github.io/thinkact-vla/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN, RL-VLA</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2509.15155">Self-Improving Embodied Foundation Models</a></td>
<td nowrap>Uses steps-to-go prediction to produce rewards and success detectors, enabling robots to improve through self-practice.</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>-</td>
<td nowrap>online RL with self-predicted reward + success detector</td>
<td nowrap>VLA/action</td>
<td nowrap>Simulated/Real-World LanguageTable, Aloha, BananaTable/Real2Sim</td>
<td nowrap>Addresses the reliance of low-level control in embodied foundation models mainly on behavior cloning.</td>
<td nowrap><a href="https://arxiv.org/abs/2509.15155">paper</a> / <a href="https://arxiv.org/pdf/2509.15155">paper</a> / <a href="https://neurips.cc/virtual/2025/loc/san-diego/poster/118633">paper</a></td>
<td nowrap><a href="https://self-improving-efms.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, EAI-Safety, WAM, RL-VLA</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.09990">Chain-of-Action: Trajectory Autoregressive Modeling for Robotic Manipulation</a></td>
<td nowrap>Autoregressively generates complete manipulation trajectories through reverse action-level CoT.</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>-</td>
<td nowrap>action-level CoT/backward trajectory reasoning</td>
<td nowrap>closed-loop reverse autoregressive trajectory generation</td>
<td nowrap>To be filled in</td>
<td nowrap>Addresses the lack of global-goal constraints in direct forward action prediction.</td>
<td nowrap><a href="https://arxiv.org/abs/2506.09990">paper</a></td>
<td nowrap><a href="https://chain-of-action.github.io/">project</a></td>
<td nowrap><a href="https://github.com/ByteDance-Seed/Chain-of-Action">code</a></td>
<td nowrap><a href="https://huggingface.co/datasets/Solomonz/Chain-of-Action">hf</a></td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2510.08044">Towards Reliable LLM-based Robot Planning via Combined Uncertainty Estimation</a></td>
<td nowrap>CURE decomposes cognitive and intrinsic uncertainty to improve the reliability of LLM robotic planning.</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>-</td>
<td nowrap>combined uncertainty estimation</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>Addresses overconfident and unsafe plans caused by LLM hallucinations.</td>
<td nowrap><a href="https://arxiv.org/abs/2510.08044">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2507.00833">HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning</a></td>
<td nowrap>Uses atomic dexterous manipulations and LLM reasoning to automatically generate bimanual dexterous manipulation tasks and demonstrations.</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>-</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>reasoning</td>
<td nowrap>20 tabletop bimanual dexterous tasks; DP/DP3 deployment</td>
<td nowrap>Addresses the lack of humanoid bimanual dexterous manipulation simulation tasks and high-quality data.</td>
<td nowrap><a href="https://arxiv.org/abs/2507.00833">paper</a> / <a href="https://arxiv.org/pdf/2507.00833">paper</a></td>
<td nowrap><a href="https://openhumanoidgen.github.io/">project</a></td>
<td nowrap><a href="https://github.com/TeleHuman/HumanoidGen">code</a></td>
<td nowrap>humanoidgen_dataset/model</td>
<td nowrap>Humanoid-RL, WAM</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2509.23829">DexFlyWheel: A Scalable and Self-improving Data Generation Framework for Dexterous Manipulation</a></td>
<td nowrap>Continuously expands dexterous manipulation data through a closed loop of IL, RL, and data filtering.</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>-</td>
<td nowrap>self-improving data generation flywheel</td>
<td nowrap>self-improving planner</td>
<td nowrap>-</td>
<td nowrap>Addresses insufficient scale, diversity, and generalization in dexterous manipulation data.</td>
<td nowrap><a href="https://arxiv.org/abs/2509.23829">paper</a></td>
<td nowrap><a href="https://dexflywheel.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2507.18276">Adaptive Articulated Object Manipulation On The Fly with Foundation Model Reasoning and Part Grounding</a></td>
<td nowrap>AdaRPG combines foundation-model reasoning and part grounding for adaptive manipulation of articulated objects.</td>
<td nowrap>adaptive articulated object manipulation</td>
<td nowrap>foundation reasoning + part grounding</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>Addresses adaptive manipulation of articulated objects with invisible structures and varied functional mechanisms.</td>
<td nowrap><a href="https://arxiv.org/abs/2507.18276">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2505.01709">RoBridge: A Hierarchical Architecture Bridging Cognition and Execution for General Robotic Manipulation</a></td>
<td nowrap>RoBridge bridges open-environment manipulation with a high-level cognitive planner and low-level execution module.</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>-</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>planning</td>
<td nowrap>-</td>
<td nowrap>Addresses the difficulty of balancing cognitive capability and execution skill in general-purpose manipulation.</td>
<td nowrap><a href="https://arxiv.org/abs/2505.01709">paper</a></td>
<td nowrap><a href="https://abliao.github.io/RoBridge/">project</a></td>
<td nowrap><a href="https://github.com/abliao/RoBridge">code</a></td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICML 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2505.06861">Efficient Robotic Policy Learning via Latent Space Backward Planning</a></td>
<td nowrap>Backward-plans coarse subgoals in latent space to improve the efficiency and accuracy of policy learning.</td>
<td nowrap>latent-space backward planning</td>
<td nowrap>-</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>VLA/action</td>
<td nowrap>-</td>
<td nowrap>Addresses expensive computation and error accumulation in pixel-level world-model planning.</td>
<td nowrap><a href="https://arxiv.org/abs/2505.06861">paper</a></td>
<td nowrap><a href="https://lbp-authors.github.io/">project</a></td>
<td nowrap><a href="https://github.com/Dstate/LBP">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICML 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2410.01440">Closed-Loop Long-Horizon Robotic Planning via Equilibrium Sequence Modeling</a></td>
<td nowrap>-</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>-</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>Uses equilibrium sequence modeling for closed-loop long-horizon robot planning.</td>
<td nowrap><a href="https://arxiv.org/abs/2410.01440">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/Singularity0104/equilibrium-planner">code</a></td>
<td nowrap>-</td>
<td nowrap>Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Humanoid-RL, EAI-Safety, WAM, RL-VLA</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>ICML 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2407.04281">WOMD-Reasoning: A Large-Scale Dataset for Interaction Reasoning in Driving</a></td>
<td nowrap>Builds a traffic-interaction reasoning QA dataset based on the Waymo Open Motion Dataset.</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>-</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>VLA/action</td>
<td nowrap>Sim/Benchmark</td>
<td nowrap>Addresses the lack of rule-triggered interaction-reasoning data in autonomous driving scenarios.</td>
<td nowrap><a href="https://arxiv.org/abs/2407.04281">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/yhli123/WOMD-Reasoning">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://cvpr.thecvf.com/virtual/2025/poster/33233">CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models</a></td>
<td nowrap>-</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>-</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>VLA/action</td>
<td nowrap>Confirmed on Franka-Tabletop, LIBERO, and Bridge V2.</td>
<td nowrap>Uses visual CoT to improve VLA manipulation generalization and long-horizon reasoning.</td>
<td nowrap><a href="https://cvpr.thecvf.com/virtual/2025/poster/33233">paper</a></td>
<td nowrap><a href="https://cot-vla.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN, Awesome-VLA, WAM</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2411.18562">DexHandDiff: Interaction-aware Diffusion Planning for Adaptive Dexterous Manipulation</a></td>
<td nowrap>Uses interaction-aware two-stage diffusion planning to model pre-contact alignment and post-contact control.</td>
<td nowrap>interaction-aware diffusion planning</td>
<td nowrap>-</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>VLA/action</td>
<td nowrap>-</td>
<td nowrap>Addresses ghost states and complex-contact adaptability in diffusion planning for dexterous manipulation.</td>
<td nowrap><a href="https://arxiv.org/abs/2411.18562">paper</a></td>
<td nowrap><a href="https://dexdiffuser.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2502.21257">RoboBrain: A Unified Brain Model for Robotic Manipulation from Abstract to Concrete</a></td>
<td nowrap>RoboBrain unifies three robot-brain capabilities: planning, affordance perception, and trajectory prediction.</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>-</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>Addresses MLLMs' lack of abstract-to-concrete robotic capability in long-horizon manipulation.</td>
<td nowrap><a href="https://arxiv.org/abs/2502.21257">paper</a></td>
<td nowrap><a href="https://superrobobrain.github.io/robobrainv1/index.html">project</a></td>
<td nowrap><a href="https://github.com/FlagOpen/RoboBrain">code</a></td>
<td nowrap><a href="https://huggingface.co/datasets/BAAI/ShareRobot">hf</a></td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.08481">PhysVLM: Enabling Visual Language Models to Understand Robotic Physical Reachability</a></td>
<td nowrap>Uses S-P Map to encode different robots' reachability into VLM visual reasoning.</td>
<td nowrap>physical reachability reasoning</td>
<td nowrap>-</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>robot reachability understanding</td>
<td nowrap><a href="https://arxiv.org/abs/2503.08481">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2411.16537">RoboSpatial: Teaching Spatial Understanding to 2D and 3D Vision-Language Models for Robotics</a></td>
<td nowrap>Builds RoboSpatial to train/evaluate robotic spatial understanding in 2D and 3D VLMs.</td>
<td nowrap>robot spatial understanding</td>
<td nowrap>-</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>planning / reasoning / 3D representation</td>
<td nowrap>-</td>
<td nowrap>Addresses the lack of robot-needed spatial reasoning in general vision-language data.</td>
<td nowrap><a href="https://arxiv.org/abs/2411.16537">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>RoboSpatial</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_Tartan_IMU_A_Light_Foundation_Model_for_Inertial_Positioning_in_CVPR_2025_paper.pdf">Tartan IMU: A Light Foundation Model for Inertial Positioning in Robotics</a></td>
<td nowrap>Pretrains a lightweight IMU foundation model and applies it to inertial positioning through adapters.</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>-</td>
<td nowrap>Self-improving Planning</td>
<td nowrap>planning / reasoning</td>
<td nowrap>-</td>
<td nowrap>Addresses insufficient generalization across moving bodies and scenes in robot inertial positioning.</td>
<td nowrap><a href="https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_Tartan_IMU_A_Light_Foundation_Model_for_Inertial_Positioning_in_CVPR_2025_paper.pdf">paper</a></td>
<td nowrap><a href="https://superodometry.com/tartanimu">project</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://huggingface.co/datasets/raphael-blanchard/TartanIMU">hf</a></td>
<td nowrap>-</td>
<td nowrap>Used to evaluate whether high-level planning can land in executable actions.</td>
</tr>
</tbody>
</table>

### Embodiment Expansion / Dexterous Manipulation

Embodiment expansion determines whether embodied AI can move beyond single-arm systems toward humanoids, bimanual robots, dexterous hands, and tactile/contact-rich tasks. These papers show how action spaces, sensing, and control objectives become more complex as the body changes.

Subdirections: humanoid, bimanual, dexterous hand, tactile/contact-rich, and grasping.

Total: 75 papers.

<table>
<thead>
<tr>
<th nowrap>Subdirection</th>
<th nowrap>Entries</th>
<th nowrap>Focus</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>humanoid</td>
<td nowrap>22</td>
<td nowrap>Focus on whole-body control, mobile manipulation, and humanoid embodiment generalization.</td>
</tr>
<tr>
<td nowrap>bimanual</td>
<td nowrap>12</td>
<td nowrap>Focus on bimanual coordination, long-horizon manipulation, and coordinated control.</td>
</tr>
<tr>
<td nowrap>dexterous hand</td>
<td nowrap>28</td>
<td nowrap>Focus on dexterous-hand action spaces and grasp transfer.</td>
</tr>
<tr>
<td nowrap>tactile/contact-rich</td>
<td nowrap>13</td>
<td nowrap>Focus on tactile sensing, contact dynamics, and fine-grained feedback.</td>
</tr>
</tbody>
</table>

#### humanoid

Total: 22 papers.

<table>
<thead>
<tr>
<th nowrap>Venue/Year</th>
<th nowrap>Paper/Method</th>
<th nowrap>Abstract</th>
<th nowrap>Embodiment Type</th>
<th nowrap>Sensing/Contact</th>
<th nowrap>Control Interface</th>
<th nowrap>Training Mode</th>
<th nowrap>Sim/Real</th>
<th nowrap>Paper Task/Goal</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>Source</th>
<th nowrap>Survey Note</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ICRA 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2510.08807">Humanoid Everyday: A Comprehensive Robotic Dataset for Open-World Humanoid Manipulation</a></td>
<td nowrap>Humanoid Everyday 提供 260 类开放世界人形操作任务，覆盖移动、交互、操作和多模态传感。</td>
<td nowrap>Humanoid</td>
<td nowrap>RGB-D / LiDAR / tactile / language</td>
<td nowrap>whole-body manipulation</td>
<td nowrap>large-scale dataset / benchmark</td>
<td nowrap>Real</td>
<td nowrap>补足人形机器人开放世界操作数据和评测。</td>
<td nowrap><a href="https://arxiv.org/abs/2510.08807">paper</a></td>
<td nowrap><a href="https://humanoideveryday.github.io/">project</a></td>
<td nowrap><a href="https://github.com/physical-superintelligence-lab/Humanoid-Everyday">code</a></td>
<td nowrap><a href="https://huggingface.co/datasets/USC-PSI-Lab/humanoid-everyday">hf</a></td>
<td nowrap>ICRA/IROS</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=OCJmVjyzN7">WholeBodyVLA: Towards Unified Latent VLA for Whole-body Loco-manipulation Control</a></td>
<td nowrap>Learn a unified latent-space VLA from egocentric videos, enabling humanoid robots to perform large-workspace vision-language whole-body loco-manipulation.</td>
<td nowrap>Humanoid/Legged Robot</td>
<td nowrap>Vision + language + proprioceptive state</td>
<td nowrap>humanoid control / humanoid / whole-body control</td>
<td nowrap>action-free egocentric video latent VLA + RL controller</td>
<td nowrap>Sim + Real</td>
<td nowrap>Addresses manipulation-aware locomotion, data scarcity, and unstable low-level control in humanoid loco-manipulation.</td>
<td nowrap><a href="https://openreview.net/forum?id=OCJmVjyzN7">paper</a></td>
<td nowrap><a href="https://opendrivelab.com/WholeBodyVLA/">project</a></td>
<td nowrap><a href="https://github.com/OpenDriveLab/WholebodyVLA">code</a></td>
<td nowrap>-</td>
<td nowrap>Awesome-EAI, Humanoid-RL</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=aQWSEjcN9V">Endowing GPT-4 with a Humanoid Body: Building the Bridge Between Off-the-Shelf VLMs and the Physical World</a></td>
<td nowrap>BiBo uses off-the-shelf VLMs to compile high-level instructions into low-level control parameters and drives humanoid bodies with a diffusion motion actuator.</td>
<td nowrap>Humanoid/Legged Robot</td>
<td nowrap>Vision + language + physical feedback</td>
<td nowrap>VLM instruction compiler + diffusion motion executor</td>
<td nowrap>off-the-shelf VLM + diffusion executor</td>
<td nowrap>-</td>
<td nowrap>Addresses how to have GPT-4/VLM control humanoid agents without additional fine-tuning data.</td>
<td nowrap><a href="https://openreview.net/forum?id=aQWSEjcN9V">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Humanoid-RL</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=3UE3Aatcjy">HWC-Loco: A Hierarchical Whole-Body Control Approach to Robust Humanoid Locomotion</a></td>
<td nowrap>HWC-Loco frames humanoid locomotion control as robust optimization and uses a hierarchical policy to dynamically trade off safety recovery and target tracking.</td>
<td nowrap>Humanoid/Legged Robot</td>
<td nowrap>-</td>
<td nowrap>humanoid control / humanoid / whole-body control</td>
<td nowrap>hierarchical robust whole-body RL/control</td>
<td nowrap>Sim + Real</td>
<td nowrap>Addresses robust whole-body walking control for humanoid robots under train-deploy mismatch.</td>
<td nowrap><a href="https://openreview.net/forum?id=3UE3Aatcjy">paper</a></td>
<td nowrap><a href="https://simonlinsx.github.io/HWC_Loco/">project</a></td>
<td nowrap><a href="https://github.com/EDEM-AI/HWC_Loco">code</a></td>
<td nowrap>-</td>
<td nowrap>Humanoid-RL</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=6T3wJQhvc3">Task Tokens: A Flexible Approach to Adapting Behavior Foundation Models</a></td>
<td nowrap>Task Tokens freezes the behavior foundation model and trains only the task tokenizer/tokens for low-parameter adaptation to specific humanoid tasks.</td>
<td nowrap>Humanoid/Legged Robot</td>
<td nowrap>-</td>
<td nowrap>task-token-conditioned behavior foundation model</td>
<td nowrap>frozen BFM + task-specific tokenizer</td>
<td nowrap>-</td>
<td nowrap>Addresses BFM's reliance on prompt engineering for new tasks and low adaptation efficiency.</td>
<td nowrap><a href="https://openreview.net/forum?id=6T3wJQhvc3">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=jkhl2oI0g5">BFM-Zero: A Promptable Behavioral Foundation Model for Humanoid Control Using Unsupervised Reinforcement Learning</a></td>
<td nowrap>BFM-Zero learns a shared latent space via unsupervised RL, enabling a single humanoid policy to be prompted by motions, goals, or rewards.</td>
<td nowrap>Humanoid/Legged Robot</td>
<td nowrap>proprioceptive state / goal / reward prompts</td>
<td nowrap>humanoid control / humanoid / whole-body control</td>
<td nowrap>unsupervised RL + Forward-Backward latent model</td>
<td nowrap>Sim + Real / Unitree G1</td>
<td nowrap>Addresses the promptable generalist policy problem for humanoid multitask whole-body control without retraining.</td>
<td nowrap><a href="https://openreview.net/forum?id=jkhl2oI0g5">paper</a></td>
<td nowrap><a href="https://lecar-lab.github.io/BFM-Zero/">project</a></td>
<td nowrap><a href="https://github.com/LeCAR-Lab/BFM-Zero">code</a></td>
<td nowrap>-</td>
<td nowrap>Humanoid-RL</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=k3Cyx3Uets">From Language to Locomotion: Retargeting-free Humanoid Control via Motion Latent Guidance</a></td>
<td nowrap>RoboGhost bypasses human-motion decoding and retargeting, directly generating executable humanoid motions from language-conditioned motion latents.</td>
<td nowrap>Humanoid/Legged Robot</td>
<td nowrap>-</td>
<td nowrap>language-conditioned motion latent + diffusion policy</td>
<td nowrap>retargeting-free diffusion action policy</td>
<td nowrap>-</td>
<td nowrap>Addresses retargeting errors, high latency, and weak semantic-control coupling in the natural-language-to-humanoid-motion-control pipeline.</td>
<td nowrap><a href="https://openreview.net/forum?id=k3Cyx3Uets">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/gentlefress/RoboGhost">code</a></td>
<td nowrap>-</td>
<td nowrap>Humanoid-RL</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=NEOTsyyYH7">Towards Bridging the Gap between Large-Scale Pretraining and Efficient Finetuning for Humanoid Control</a></td>
<td nowrap>LIFT uses large-batch SAC for large-scale humanoid pretraining, then applies model-assisted fine-tuning for sample-efficient adaptation.</td>
<td nowrap>Humanoid/Legged Robot</td>
<td nowrap>-</td>
<td nowrap>humanoid control / humanoid / whole-body control</td>
<td nowrap>off-policy SAC pretraining + model-based fine-tuning</td>
<td nowrap>Sim + Real</td>
<td nowrap>Addresses the gap between large-scale pretraining and efficient fine-tuning in new environments for humanoid control.</td>
<td nowrap><a href="https://openreview.net/forum?id=NEOTsyyYH7">paper</a></td>
<td nowrap><a href="https://lift-humanoid.github.io/">project</a></td>
<td nowrap><a href="https://github.com/bigai-ai/LIFT-humanoid">code</a></td>
<td nowrap>-</td>
<td nowrap>Humanoid-RL</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=eSkDNIGbcd">Hierarchical Value-Decomposed Offline Reinforcement Learning for Whole-Body Control</a></td>
<td nowrap>-</td>
<td nowrap>Humanoid/Legged Robot</td>
<td nowrap>tactile / contact</td>
<td nowrap>humanoid control / humanoid / whole-body control</td>
<td nowrap>humanoid control</td>
<td nowrap>-</td>
<td nowrap>Improves complex embodiment control</td>
<td nowrap><a href="https://openreview.net/forum?id=eSkDNIGbcd">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38908">Whole-Body Coordination for Dynamic Object Grasping with Legged Manipulators</a></td>
<td nowrap>-</td>
<td nowrap>quadruped / legged mobile base + manipulator</td>
<td nowrap>-</td>
<td nowrap>whole-body coordination for dynamic grasping</td>
<td nowrap>humanoid control</td>
<td nowrap>Sim + Real</td>
<td nowrap>Addresses whole-body coordination between the mobile base and manipulator when a legged mobile manipulator grasps dynamic targets.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38908">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Robot-Learning, Humanoid-RL, EAI-Safety, WAM</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38918">Coordinated Humanoid Robot Locomotion with Symmetry Equivariant Reinforcement Learning Policy</a></td>
<td nowrap>-</td>
<td nowrap>Humanoid/Legged Robot</td>
<td nowrap>proprioceptive state + foot contact</td>
<td nowrap>humanoid control / humanoid / whole-body control</td>
<td nowrap>symmetry-equivariant DRL</td>
<td nowrap>Sim + Real / Unitree G1</td>
<td nowrap>Addresses learning coordinated gaits for humanoid robots using symmetry-equivariant structure.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38918">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Humanoid-RL</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38924">FARM: Frame-Accelerated Augmentation and Residual Mixture-of-Experts for Physics-Based High-Dynamic Humanoid Control</a></td>
<td nowrap>-</td>
<td nowrap>Humanoid/Legged Robot</td>
<td nowrap>-</td>
<td nowrap>humanoid control / humanoid / whole-body control</td>
<td nowrap>frame-accelerated augmentation + residual MoE</td>
<td nowrap>-</td>
<td nowrap>Addresses data augmentation and expert residual fusion for controlling highly dynamic skills of humanoids in physics simulation.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38924">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/Colin-Jing/FARM">code</a></td>
<td nowrap>HDHM data</td>
<td nowrap>Humanoid-RL</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38927">ODYSSEY: Open-World Quadrupeds Exploration and Manipulation for Long-Horizon Tasks</a></td>
<td nowrap>-</td>
<td nowrap>quadruped robot + manipulator</td>
<td nowrap>-</td>
<td nowrap>humanoid control / humanoid / whole-body control</td>
<td nowrap>humanoid control</td>
<td nowrap>-</td>
<td nowrap>Addresses long-horizon exploration and manipulation tasks for quadruped robots in the open world.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38927">paper</a></td>
<td nowrap><a href="https://kaijwang.github.io/odyssey.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38949">Keep On Going: Learning Robust Humanoid Motion Skills via Selective Adversarial Training</a></td>
<td nowrap>-</td>
<td nowrap>Humanoid/Legged Robot</td>
<td nowrap>-</td>
<td nowrap>humanoid control / humanoid / whole-body control</td>
<td nowrap>selective adversarial training</td>
<td nowrap>-</td>
<td nowrap>Addresses robustness and sustained execution of humanoid motion skills under disturbances.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38949">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Humanoid-RL</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38951">Towards Adaptive Humanoid Control via Multi-Behavior Distillation and Reinforced Fine-Tuning</a></td>
<td nowrap>-</td>
<td nowrap>Humanoid/Legged Robot</td>
<td nowrap>tactile / contact</td>
<td nowrap>humanoid control / humanoid / whole-body control</td>
<td nowrap>multi-behavior distillation + reinforced fine-tuning</td>
<td nowrap>Sim + Real / Unitree G1</td>
<td nowrap>Addresses adaptive fine-tuning on real robots after distilling multi-behavior humanoid control policies.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38951">paper</a></td>
<td nowrap><a href="https://ahc-humanoid.github.io">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Humanoid-RL</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62003">Scalable and General Whole-Body Control for Cross-Humanoid Locomotion</a></td>
<td nowrap>-</td>
<td nowrap>Humanoid Robot</td>
<td nowrap>-</td>
<td nowrap>humanoid control / humanoid / whole-body control</td>
<td nowrap>cross-embodiment morphological randomization</td>
<td nowrap>12 simulated humanoids + 7 real robots</td>
<td nowrap>Addresses scalable general-purpose whole-body walking control across diverse humanoid morphologies.</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62003">paper</a></td>
<td nowrap><a href="https://xhugwbc.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Awesome-EAI, Humanoid-RL</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/65120">Learning Transferable Interaction Primitives from Game Videos for Humanoids</a></td>
<td nowrap>-</td>
<td nowrap>Humanoid Robot</td>
<td nowrap>-</td>
<td nowrap>humanoid control / humanoid / whole-body control</td>
<td nowrap>humanoid control</td>
<td nowrap>-</td>
<td nowrap>Improves humanoid robot control</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/65120">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2511.15200">VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation</a></td>
<td nowrap>VIRAL trains a visual student policy in simulation and deploys it zero-shot to real humanoid robots, enabling scalable visual sim-to-real loco-manipulation.</td>
<td nowrap>Humanoid Robot</td>
<td nowrap>Vision</td>
<td nowrap>humanoid control / humanoid / whole-body control</td>
<td nowrap>privileged RL teacher + visual student distillation + DAgger/BC</td>
<td nowrap>Sim training + Real zero-shot</td>
<td nowrap>Addresses the difficulty of transferring visual loco-manipulation skills for humanoid robots from simulation to real hardware.</td>
<td nowrap><a href="https://arxiv.org/abs/2511.15200">paper</a></td>
<td nowrap><a href="https://viral-humanoid.github.io/">project</a></td>
<td nowrap><a href="https://github.com/NVlabs/GR00T-VisualSim2Real">code</a></td>
<td nowrap>-</td>
<td nowrap>Humanoid-RL</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2504.14305">Adversarial Locomotion and Motion Imitation for Humanoid Policy Learning</a></td>
<td nowrap>ALMI uses adversarial learning for upper and lower bodies, allowing the lower body to maintain stable walking while the upper body tracks diverse motions.</td>
<td nowrap>Humanoid Robot</td>
<td nowrap>-</td>
<td nowrap>humanoid control / humanoid / whole-body control</td>
<td nowrap>adversarial locomotion + motion imitation</td>
<td nowrap>Sim + Real</td>
<td nowrap>Addresses humanoid robots maintaining stable locomotion while performing expressive whole-body motion imitation.</td>
<td nowrap><a href="https://arxiv.org/abs/2504.14305">paper</a></td>
<td nowrap><a href="https://almi-humanoid.github.io/">project</a></td>
<td nowrap><a href="https://github.com/TeleHuman/ALMI-Open">code</a></td>
<td nowrap><a href="https://huggingface.co/datasets/TeleEmbodied/ALMI-X">hf</a></td>
<td nowrap>Humanoid-RL</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.12779">From Experts to a Generalist: Toward General Whole-Body Control for Humanoid Robots</a></td>
<td nowrap>BumbleBee first trains multiple experts by clustering, then adapts with real data and distills them into a unified humanoid whole-body controller.</td>
<td nowrap>Humanoid Robot</td>
<td nowrap>-</td>
<td nowrap>humanoid control / humanoid / whole-body control</td>
<td nowrap>expert-generalist distillation + sim-to-real adaptation</td>
<td nowrap>Sim + Real</td>
<td nowrap>Addresses the difficulty of training general policies caused by conflicting control requirements across diverse agile humanoid motions.</td>
<td nowrap><a href="https://arxiv.org/abs/2506.12779">paper</a></td>
<td nowrap><a href="https://beingbeyond.github.io/BumbleBee/">project</a></td>
<td nowrap><a href="https://github.com/BeingBeyond/BumbleBee">code</a></td>
<td nowrap>-</td>
<td nowrap>Humanoid-RL</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://kungfubot.github.io/">KungfuBot: Physics-Based Humanoid Whole-Body Control for Learning Highly-Dynamic Skills</a></td>
<td nowrap>KungfuBot enables humanoid robots to learn highly dynamic skills such as kung fu and dance through motion processing, retargeting, and an adaptive tracking curriculum.</td>
<td nowrap>Humanoid Robot</td>
<td nowrap>-</td>
<td nowrap>humanoid control / humanoid / whole-body control</td>
<td nowrap>physics-based imitation + adaptive curriculum</td>
<td nowrap>-</td>
<td nowrap>Addresses the difficulty existing whole-body motion imitation has in tracking high-speed, highly dynamic human motions.</td>
<td nowrap><a href="https://arxiv.org/abs/2506.12851">paper</a></td>
<td nowrap><a href="https://kungfubot.github.io/">project</a></td>
<td nowrap><a href="https://github.com/TeleHuman/PBHC">code</a></td>
<td nowrap>-</td>
<td nowrap>Humanoid-RL</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://cvpr.thecvf.com/virtual/2025/poster/34565">Let Humanoids Hike! Integrative Skill Development on Complex Trails</a></td>
<td nowrap>-</td>
<td nowrap>Humanoid Robot</td>
<td nowrap>-</td>
<td nowrap>humanoid control / humanoid / whole-body control</td>
<td nowrap>humanoid control</td>
<td nowrap>-</td>
<td nowrap>Addresses integrating perception, locomotion, and balance skills for humanoid robots on complex mountain roads/trails.</td>
<td nowrap><a href="https://cvpr.thecvf.com/virtual/2025/poster/34565">paper</a></td>
<td nowrap><a href="https://lego-h-humanoidrobothiking.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
</tbody>
</table>

#### bimanual

Total: 12 papers.

<table>
<thead>
<tr>
<th nowrap>Venue/Year</th>
<th nowrap>Paper/Method</th>
<th nowrap>Abstract</th>
<th nowrap>Embodiment Type</th>
<th nowrap>Sensing/Contact</th>
<th nowrap>Control Interface</th>
<th nowrap>Training Mode</th>
<th nowrap>Sim/Real</th>
<th nowrap>Paper Task/Goal</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>Source</th>
<th nowrap>Survey Note</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ICRA 2025</td>
<td nowrap><a href="https://dexmimicgen.github.io/">DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning</a></td>
<td nowrap>DexMimicGen 从少量人类示教自动生成大规模双臂灵巧操作 demonstrations，并覆盖 sim/real。</td>
<td nowrap>Bimanual dexterous manipulation</td>
<td nowrap>vision + proprioception</td>
<td nowrap>bimanual action</td>
<td nowrap>imitation data generation</td>
<td nowrap>Sim + Real</td>
<td nowrap>降低双臂灵巧操作示教数据采集成本。</td>
<td nowrap><a href="https://dexmimicgen.github.io/">paper</a></td>
<td nowrap><a href="https://dexmimicgen.github.io/">project</a></td>
<td nowrap><a href="https://github.com/NVlabs/dexmimicgen/">code</a></td>
<td nowrap>-</td>
<td nowrap>ICRA/IROS</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=jG9W6nAwVz">TwinVLA: Data-Efficient Bimanual Manipulation with Twin Single-Arm Vision-Language-Action Models</a></td>
<td nowrap>TwinVLA combines two pretrained single-arm VLAs into a bimanual VLA, achieving coordinated manipulation with a small amount of bimanual data.</td>
<td nowrap>Bimanual Robot</td>
<td nowrap>Vision</td>
<td nowrap>twin single-arm VLA coordination</td>
<td nowrap>compose pretrained single-arm VLAs + limited bimanual finetuning</td>
<td nowrap>Sim + Real</td>
<td nowrap>Addresses the lack of large-scale bimanual data and high fine-tuning cost in bimanual VLA training.</td>
<td nowrap><a href="https://openreview.net/forum?id=jG9W6nAwVz">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=he86smZzRk">VLBiMan: Vision-Language Anchored One-Shot Demonstration Enables Generalizable Bimanual Robotic Manipulation</a></td>
<td nowrap>VLBiMan decomposes reusable bimanual skills from a single human demonstration and adapts to scene changes with vision-language anchors.</td>
<td nowrap>Bimanual Robot</td>
<td nowrap>Vision</td>
<td nowrap>bimanual policy / bimanual manipulation</td>
<td nowrap>one-shot demonstration + VLM grounding + geometric constraints</td>
<td nowrap>Real</td>
<td nowrap>Addresses how bimanual manipulation can generalize from very few demonstrations to different backgrounds, object positions, and distractor scenes.</td>
<td nowrap><a href="https://openreview.net/forum?id=he86smZzRk">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38926">LatentVLA: Taming Latent Space for Generalizable and Long-Horizon Bimanual Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>Bimanual Robot</td>
<td nowrap>-</td>
<td nowrap>bimanual policy / bimanual manipulation</td>
<td nowrap>latent-space VLA for long-horizon bimanual manipulation</td>
<td nowrap>-</td>
<td nowrap>Addresses VLA latent-space organization and generalizable control in long-horizon bimanual manipulation.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38926">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/63277">DexMachina: Functional Retargeting for Bimanual Dexterous Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>Bimanual Robot</td>
<td nowrap>-</td>
<td nowrap>bimanual policy / bimanual manipulation</td>
<td nowrap>bimanual policy</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/63277">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66358">DECO: Decoupled Multimodal Diffusion Transformer for Bimanual Dexterous Manipulation with a Plugin Tactile Adapter</a></td>
<td nowrap>-</td>
<td nowrap>Bimanual Robot</td>
<td nowrap>tactile / contact</td>
<td nowrap>diffusion policy / tactile policy / diffusion transformer / bimanual manipulation</td>
<td nowrap>diffusion policy / tactile policy / diffusion transformer</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66358">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62192">RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation</a></td>
<td nowrap>RoboTwin 2.0 provides a strongly domain-randomized bimanual robot data generator and benchmark.</td>
<td nowrap>Bimanual Robot</td>
<td nowrap>-</td>
<td nowrap>bimanual policy / bimanual manipulation</td>
<td nowrap>sim data generator / domain randomization / benchmark</td>
<td nowrap>Sim + Benchmark</td>
<td nowrap>Addresses the lack of scalable simulation data and robust evaluation tasks for bimanual manipulation.</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62192">paper</a> / <a href="https://arxiv.org/pdf/2506.18088">paper</a> / <a href="https://arxiv.org/abs/2506.18088">paper</a></td>
<td nowrap><a href="https://robotwin-platform.github.io/">project</a></td>
<td nowrap><a href="https://github.com/robotwin-Platform/RoboTwin">code</a></td>
<td nowrap><a href="https://huggingface.co/datasets/TianxingChen/RoboTwin2.0">hf</a></td>
<td nowrap>EAI-Guide, EAI-VLA-VLN, Efficient-VLA, WAM, RL-VLA</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.09186">Rethinking Bimanual Robotic Manipulation: Learning with Decoupled Interaction Framework</a></td>
<td nowrap>This paper separates bimanual tasks into coordinated and non-coordinated cases, improving learning with independent bimanual models plus a selective interaction module.</td>
<td nowrap>Bimanual Robot</td>
<td nowrap>-</td>
<td nowrap>per-arm policies + selective interaction module</td>
<td nowrap>decoupled interaction framework</td>
<td nowrap>-</td>
<td nowrap>Addresses integrated bimanual policies forcing early collaboration and ignoring non-cooperative subtasks.</td>
<td nowrap><a href="https://arxiv.org/abs/2503.09186">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2412.06779">AnyBimanual: Transferring Unimanual Policy for General Bimanual Manipulation</a></td>
<td nowrap>AnyBimanual transfers pretrained single-arm policies to language-conditioned bimanual manipulation through skill management and a few bimanual demonstrations.</td>
<td nowrap>Bimanual Robot</td>
<td nowrap>-</td>
<td nowrap>bimanual policy / bimanual manipulation</td>
<td nowrap>unimanual-to-bimanual transfer + few bimanual demos</td>
<td nowrap>Sim + Real</td>
<td nowrap>Addresses expensive bimanual manipulation data and the difficulty of reusing single-arm policy knowledge.</td>
<td nowrap><a href="https://arxiv.org/abs/2412.06779">paper</a></td>
<td nowrap><a href="https://anybimanual.github.io/">project</a></td>
<td nowrap><a href="https://github.com/TengBoYu01/AnyBimanual">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.23152">DexH2R: A Benchmark for Dynamic Dexterous Grasping in Human-to-Robot Handover</a></td>
<td nowrap>DexH2R builds a real human-to-dexterous-hand handover dataset and benchmark covering dynamic objects, human hand motion, and visual annotations.</td>
<td nowrap>Dexterous hand</td>
<td nowrap>-</td>
<td nowrap>bimanual policy / bimanual manipulation</td>
<td nowrap>bimanual policy</td>
<td nowrap>Real + Benchmark</td>
<td nowrap>Addresses the lack of real high-quality datasets for dexterous grasping in dynamic human-robot handovers.</td>
<td nowrap><a href="https://arxiv.org/abs/2506.23152">paper</a></td>
<td nowrap><a href="https://dexh2r.github.io/">project</a></td>
<td nowrap><a href="https://github.com/4DVLab/DexH2R">code</a></td>
<td nowrap>DexH2R benchmark</td>
<td nowrap>-</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.10743">Spatial-Temporal Graph Diffusion Policy with Kinematic Modeling for Bimanual Robotic Manipulation</a></td>
<td nowrap>KStar Diffuser explicitly models robot structure and kinematic constraints with a spatiotemporal graph diffusion policy.</td>
<td nowrap>Bimanual Robot</td>
<td nowrap>-</td>
<td nowrap>diffusion policy / bimanual manipulation</td>
<td nowrap>spatial-temporal graph diffusion policy + differentiable kinematics</td>
<td nowrap>Sim + Real</td>
<td nowrap>Addresses action prediction in bimanual imitation learning ignoring robot structure, causing collisions and joint-constraint violations.</td>
<td nowrap><a href="https://arxiv.org/abs/2503.10743">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>HCP-Survey</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2501.04595">MobileH2R: Learning Generalizable Human to Mobile Robot Handover Exclusively from Scalable and Diverse Synthetic Data</a></td>
<td nowrap>MobileH2R uses scalable synthetic human-motion data and 4D imitation learning to train mobile robots for object-receiving skills.</td>
<td nowrap>mobile robot + manipulator</td>
<td nowrap>-</td>
<td nowrap>bimanual policy / bimanual manipulation</td>
<td nowrap>synthetic data + 4D imitation learning</td>
<td nowrap>Sim training + Real evaluation</td>
<td nowrap>Addresses the large workspace and difficulty of collecting real demonstrations for mobile robots in human-to-robot handovers.</td>
<td nowrap><a href="https://arxiv.org/abs/2501.04595">paper</a></td>
<td nowrap><a href="https://mobileh2r.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Humanoid-RL</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
</tbody>
</table>

#### dexterous hand

Total: 28 papers.

<table>
<thead>
<tr>
<th nowrap>Venue/Year</th>
<th nowrap>Paper/Method</th>
<th nowrap>Abstract</th>
<th nowrap>Embodiment Type</th>
<th nowrap>Sensing/Contact</th>
<th nowrap>Control Interface</th>
<th nowrap>Training Mode</th>
<th nowrap>Sim/Real</th>
<th nowrap>Paper Task/Goal</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>Source</th>
<th nowrap>Survey Note</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>IROS 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2606.24450">NoContactNoWorries: Estimating Contact through Vision and Proprioception for In-Hand Dexterous Manipulation</a></td>
<td nowrap>NoContactNoWorries 不依赖触觉硬件，用视觉和本体感知估计灵巧手接触状态。</td>
<td nowrap>Dexterous hand</td>
<td nowrap>vision + proprioception contact estimation</td>
<td nowrap>in-hand manipulation</td>
<td nowrap>contact representation learning</td>
<td nowrap>Real</td>
<td nowrap>用低成本感知补足灵巧手接触反馈。</td>
<td nowrap><a href="https://arxiv.org/abs/2606.24450">paper</a></td>
<td nowrap><a href="https://soham2560.github.io/no-contact-no-worries/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>ICRA/IROS</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=Bf4FeuW0Mr">DemoGrasp: Universal Dexterous Grasping from a Single Demonstration</a></td>
<td nowrap>DemoGrasp starts from a single successful grasp trajectory, edits wrist poses and finger joints, and uses RL to optimize general grasping.</td>
<td nowrap>Dexterous Hand/Grasping</td>
<td nowrap>-</td>
<td nowrap>dexterous manipulation / dexterous hand / grasping</td>
<td nowrap>single demonstration + RL trajectory editing</td>
<td nowrap>Sim + Real</td>
<td nowrap>Addresses high-dimensional long-horizon exploration and complex reward-curriculum design in general dexterous-hand grasping.</td>
<td nowrap><a href="https://openreview.net/forum?id=Bf4FeuW0Mr">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/BeingBeyond/DemoGrasp">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=80vjyj5o7l">DexNDM: Closing the Reality Gap for Dexterous In-Hand Rotation via Joint-Wise Neural Dynamics Model</a></td>
<td nowrap>DexNDM uses a joint-level neural dynamics model to correct simulation policies with a small amount of real data, enabling generalized in-hand object rotation.</td>
<td nowrap>Dexterous Hand/Grasping</td>
<td nowrap>-</td>
<td nowrap>dexterous manipulation / dexterous hand / grasping</td>
<td nowrap>sim policy + joint-wise neural dynamics model + real-data adaptation</td>
<td nowrap>Sim-to-Real</td>
<td nowrap>Addresses the contact-dynamics reality gap from simulation to real-world in-hand rotation for dexterous hands.</td>
<td nowrap><a href="https://openreview.net/forum?id=80vjyj5o7l">paper</a></td>
<td nowrap><a href="https://meowuu7.github.io/DexNDM/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=FFxkFMU89E">EgoDex: Learning Dexterous Manipulation from Large-Scale Egocentric Video</a></td>
<td nowrap>EgoDex collects 829 hours of egocentric video and 3D finger tracking with Apple Vision Pro to support dexterous manipulation learning.</td>
<td nowrap>Dexterous Hand/Grasping</td>
<td nowrap>egocentric RGB/video + 3D hand tracking</td>
<td nowrap>dexterous manipulation / dexterous hand / grasping</td>
<td nowrap>large-scale egocentric video pretraining</td>
<td nowrap>-</td>
<td nowrap>Addresses the lack of internet-scale data with hand-pose annotations for dexterous manipulation.</td>
<td nowrap><a href="https://openreview.net/forum?id=FFxkFMU89E">paper</a> / <a href="https://arxiv.org/pdf/2505.11709">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/apple/ml-egodex">code</a></td>
<td nowrap>EgoDex dataset/benchmark</td>
<td nowrap>Humanoid-RL, WAM</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=Kt9tJeOwjy">RFS: Reinforcement learning with Residual flow steering for dexterous manipulation</a></td>
<td nowrap>RFS fine-tunes pretrained flow-matching dexterous manipulation policies with residual actions and delayed flow-time-variable reinforcement learning.</td>
<td nowrap>Dexterous Hand/Grasping</td>
<td nowrap>tactile / contact</td>
<td nowrap>residual action + flow steering</td>
<td nowrap>RL with Residual Flow Steering over pretrained flow policy</td>
<td nowrap>-</td>
<td nowrap>Addresses poor deployment generalization of generative imitation policies while preserving pretrained exploration ability during fine-tuning.</td>
<td nowrap><a href="https://openreview.net/forum?id=Kt9tJeOwjy">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=NZDaMcpXZm">Learning to Grasp Anything By Playing with Random Toys</a></td>
<td nowrap>This paper shows that robots can learn zero-shot-generalizable grasping policies from random toys composed of a small number of shape primitives.</td>
<td nowrap>Dexterous Hand/Grasping</td>
<td nowrap>Vision + proprioceptive state</td>
<td nowrap>dexterous manipulation / dexterous hand / grasping</td>
<td nowrap>random toy training + object-centric visual representation</td>
<td nowrap>Sim + Real</td>
<td nowrap>Addresses poor generalization of robot grasping policies to novel objects.</td>
<td nowrap><a href="https://openreview.net/forum?id=NZDaMcpXZm">paper</a></td>
<td nowrap><a href="https://lego-grasp.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Humanoid-RL</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=aemqAxScl9">SARM: Stage-Aware Reward Modeling for Long Horizon Robot Manipulation</a></td>
<td nowrap>SARM uses a stage-aware video reward model and language subtask annotations to provide stable supervision for long-horizon contact-rich/deformable-object manipulation.</td>
<td nowrap>Dexterous Hand/Grasping</td>
<td nowrap>-</td>
<td nowrap>dexterous manipulation / dexterous hand / grasping</td>
<td nowrap>stage-aware video reward modeling + reward-aligned BC</td>
<td nowrap>-</td>
<td nowrap>Addresses inconsistent demonstration quality and hard-to-align reward labels in long-horizon contact-rich manipulation.</td>
<td nowrap><a href="https://openreview.net/forum?id=aemqAxScl9">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=cVX3VqO8BO">UniHM: Unified Dexterous Hand Manipulation with Vision Language Model</a></td>
<td nowrap>UniHM uses a unified hand tokenizer and VLA to generate manipulation sequences across dexterous-hand morphologies from open-language instructions.</td>
<td nowrap>Dexterous Hand/Grasping</td>
<td nowrap>Vision + language + hand-object interaction</td>
<td nowrap>VLM/VLA + Unified Hand-Dexterous Tokenizer</td>
<td nowrap>human-object interaction data</td>
<td nowrap>-</td>
<td nowrap>Addresses unified feasible manipulation planning across different dexterous-hand morphologies under free-form language guidance.</td>
<td nowrap><a href="https://openreview.net/forum?id=cVX3VqO8BO">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=k8ovuXEQQu">House Of Dextra : Cross-Embodied Co-Design for Dexterous Hands</a></td>
<td nowrap>House of Dextra jointly searches dexterous-hand morphologies and control policies, and can rapidly fabricate and deploy new hand designs.</td>
<td nowrap>designable dexterous hands</td>
<td nowrap>-</td>
<td nowrap>dexterous manipulation / dexterous hand / grasping</td>
<td nowrap>morphology-conditioned cross-embodied control</td>
<td nowrap>Sim + Real</td>
<td nowrap>Addresses the need to co-design hand hardware morphology and control policy in dexterous manipulation.</td>
<td nowrap><a href="https://openreview.net/forum?id=k8ovuXEQQu">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=tv0Sz8A9Tc">Robotic Manipulation by Imitating Generated Videos Without Physical Demonstrations</a></td>
<td nowrap>RIGVid enables robots to execute manipulation without real demonstrations by using generated videos, VLM filtering, and 6D trajectory retargeting.</td>
<td nowrap>Dexterous Hand/Grasping</td>
<td nowrap>Vision + language</td>
<td nowrap>dexterous manipulation / dexterous hand / grasping</td>
<td nowrap>generated-video imitation + VLM filtering + pose tracking</td>
<td nowrap>Real evaluation</td>
<td nowrap>Addresses how to obtain executable robot manipulation trajectories from generated videos without physical demonstrations.</td>
<td nowrap><a href="https://openreview.net/forum?id=tv0Sz8A9Tc">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-Guide, HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Efficient-VLA, Robot-Learning, Humanoid-RL, EAI-Safety, WAM, RL-VLA</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=wySMuWHmt4">Primary-Fine Decoupling for Action Generation in Robotic Imitation</a></td>
<td nowrap>PF-DAG first selects discrete coarse action modes, then uses MeanFlow to generate fine-grained actions, reducing mode switching.</td>
<td nowrap>Dexterous Hand/Grasping</td>
<td nowrap>-</td>
<td nowrap>primary-fine action generation</td>
<td nowrap>discrete action chunk modes + mode-conditioned MeanFlow</td>
<td nowrap>-</td>
<td nowrap>Addresses detail loss from discretization and unstable continuous generation under multimodal action-sequence distributions in robot imitation learning.</td>
<td nowrap><a href="https://openreview.net/forum?id=wySMuWHmt4">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=13jshGCK9i">D-REX: Differentiable Real-to-Sim-to-Real Engine for Learning Dexterous Grasping</a></td>
<td nowrap>D-REX uses a Gaussian Splat differentiable engine to identify object mass from real observations and jointly learn force-aware grasping policies.</td>
<td nowrap>Dexterous Hand/Grasping</td>
<td nowrap>-</td>
<td nowrap>dexterous manipulation / dexterous hand / grasping</td>
<td nowrap>differentiable real-to-sim-to-real + force-aware grasping</td>
<td nowrap>Real-to-Sim-to-Real</td>
<td nowrap>Addresses physical-parameter identification and the sim-to-real dynamics gap in dexterous grasping.</td>
<td nowrap><a href="https://openreview.net/forum?id=13jshGCK9i">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=RYwQ0xQcAh">Interaction-aware Representation Modeling With Co-Occurrence Consistency for Egocentric Hand-Object Parsing</a></td>
<td nowrap>This paper improves egocentric hand-object parsing with interaction-aware representations and co-occurrence consistency, reducing physically inconsistent predictions.</td>
<td nowrap>egocentric hand-object perception</td>
<td nowrap>-</td>
<td nowrap>dexterous manipulation / dexterous hand / grasping</td>
<td nowrap>interaction-aware representation modeling</td>
<td nowrap>-</td>
<td nowrap>Addresses fine-grained segmentation/parsing of hands and active objects in egocentric embodied perception.</td>
<td nowrap><a href="https://openreview.net/forum?id=RYwQ0xQcAh">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38873">GRIM: Task-Oriented Grasping with Conditioning on Generative Examples</a></td>
<td nowrap>-</td>
<td nowrap>Dexterous Hand/Grasping</td>
<td nowrap>-</td>
<td nowrap>dexterous manipulation / dexterous hand / grasping</td>
<td nowrap>conditioning on generative examples</td>
<td nowrap>-</td>
<td nowrap>Addresses how to use generated examples as conditions to select suitable grasps for task-oriented grasping.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38873">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38874">Dexterous Manipulation Transfer via Progressive Kinematic-Dynamic Alignment</a></td>
<td nowrap>-</td>
<td nowrap>Dexterous Hand/Grasping</td>
<td nowrap>-</td>
<td nowrap>dexterous manipulation / dexterous hand / grasping</td>
<td nowrap>progressive kinematic-dynamic alignment</td>
<td nowrap>-</td>
<td nowrap>Addresses progressive kinematic and dynamic alignment when transferring dexterous manipulation policies across morphologies/environments.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38874">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Awesome-VLA, Humanoid-RL, WAM</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38892">Learning Object-Centric Motion Priors from Human for Robotic Dexterous Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>Dexterous Hand/Grasping</td>
<td nowrap>-</td>
<td nowrap>dexterous manipulation / dexterous hand / grasping</td>
<td nowrap>human-derived object-centric motion priors</td>
<td nowrap>-</td>
<td nowrap>Addresses how to learn object-centric motion priors from human motion and transfer them to robotic dexterous manipulation.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38892">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38894">Real Garment Benchmark (RGBench): A Comprehensive Benchmark for Robotic Garment Manipulation Featuring a High-Fidelity Scalable Simulator</a></td>
<td nowrap>RGBench provides real garment data, a high-fidelity scalable simulator, and a garment manipulation benchmark.</td>
<td nowrap>garment manipulation robot / bimanual</td>
<td nowrap>Vision</td>
<td nowrap>dexterous manipulation / dexterous hand / grasping</td>
<td nowrap>dexterous manipulation</td>
<td nowrap>Real garment data + simulator benchmark</td>
<td nowrap>Addresses the lack of real data, high-fidelity simulation, and unified evaluation for robotic garment manipulation.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38894">paper</a></td>
<td nowrap><a href="https://rgbench.github.io/">project</a></td>
<td nowrap><a href="https://github.com/hwk0809/RGBench">code</a></td>
<td nowrap><a href="https://rgbench.github.io/">benchmarks</a></td>
<td nowrap>-</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38940">GraphGrasp: Lightweight and Efficient Graph-Guided 6-DoF Robotic Grasp Pose Estimation Network</a></td>
<td nowrap>-</td>
<td nowrap>mainly robotic grasping / grippers</td>
<td nowrap>-</td>
<td nowrap>6-DoF grasp pose estimation</td>
<td nowrap>graph-guided network</td>
<td nowrap>-</td>
<td nowrap>Addresses lightweight and efficient 6-DoF robotic grasp-pose estimation.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38940">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38953">DexGraspVLA: A Vision-Language-Action Framework Towards General Dexterous Grasping</a></td>
<td nowrap>-</td>
<td nowrap>Dexterous Hand/Grasping</td>
<td nowrap>Vision + language</td>
<td nowrap>VLM high-level planner + diffusion low-level controller</td>
<td nowrap>dexterous manipulation</td>
<td nowrap>-</td>
<td nowrap>Addresses planning and low-level control for general dexterous grasping under vision-language instructions.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38953">paper</a></td>
<td nowrap><a href="https://dexgraspvla.github.io/">project</a></td>
<td nowrap><a href="https://github.com/Psi-Robot/DexGraspVLA">code</a></td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN, Awesome-VLA</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38957">Effective Robotic Cloth Grasping Through Suppressing False Discoveries</a></td>
<td nowrap>-</td>
<td nowrap>cloth-grasping robot</td>
<td nowrap>-</td>
<td nowrap>dexterous manipulation / dexterous hand / grasping</td>
<td nowrap>false-discovery suppression</td>
<td nowrap>-</td>
<td nowrap>Addresses unreliable grasp points caused by false detections/false discoveries in cloth grasping.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38957">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2603.22264">UniDex: A Robot Foundation Suite for Universal Dexterous Hand Control from Egocentric Human Videos</a></td>
<td nowrap>UniDex retargets egocentric human videos into 50K trajectories across 8 dexterous-hand datasets and trains a unified 3D VLA policy.</td>
<td nowrap>Dexterous Hand/Grasping</td>
<td nowrap>egocentric video + 3D point cloud + language</td>
<td nowrap>VLA / dexterous hand / grasping</td>
<td nowrap>3D VLA pretraining on UniDex-Dataset + task finetuning</td>
<td nowrap>human video-derived robot trajectories + downstream real/sim tasks</td>
<td nowrap>Addresses expensive real teleoperation data, heterogeneous hand morphologies, and high-dimensional control challenges in dexterous-hand control.</td>
<td nowrap><a href="https://arxiv.org/abs/2603.22264">paper</a></td>
<td nowrap><a href="https://unidex-ai.github.io/">project</a></td>
<td nowrap><a href="https://github.com/unidex-ai/UniDex">code</a></td>
<td nowrap><a href="https://huggingface.co/UniDex-ai/UniDex">hf</a></td>
<td nowrap>-</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/pdf/2511.01276">Generalizable Dexterous Grasp Generation via Contact Map Transfer</a></td>
<td nowrap>-</td>
<td nowrap>Dexterous Hand/Grasping</td>
<td nowrap>tactile / contact</td>
<td nowrap>conditional diffusion grasp generation</td>
<td nowrap>diffusion policy</td>
<td nowrap>-</td>
<td nowrap>Addresses generating generalizable dexterous grasps through contact-map transfer.</td>
<td nowrap><a href="https://arxiv.org/pdf/2511.01276">paper</a></td>
<td nowrap><a href="https://cmtdiffusion.github.io/">project</a></td>
<td nowrap><a href="https://github.com/Yiyao-Ma/cmtdiffusion">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.02489">Grasp2Grasp: Vision-Based Dexterous Grasp Translation via Schrödinger Bridges</a></td>
<td nowrap>Grasp2Grasp uses Schrödinger Bridge for vision-conditioned, functionally equivalent grasp transfer across different robotic hands.</td>
<td nowrap>Dexterous Hand/Grasping</td>
<td nowrap>Vision</td>
<td nowrap>dexterous manipulation / dexterous hand / grasping</td>
<td nowrap>score/flow matching + physics-informed costs</td>
<td nowrap>-</td>
<td nowrap>Addresses transferring grasp intent across different dexterous-hand morphologies without paired demonstrations or hand-shape simulation.</td>
<td nowrap><a href="https://arxiv.org/abs/2506.02489">paper</a></td>
<td nowrap><a href="https://grasp2grasp.github.io/">project</a></td>
<td nowrap><a href="https://github.com/n3il666/grasp2grasp">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.19212">Scaffolding Dexterous Manipulation with Vision-Language Models</a></td>
<td nowrap>This paper uses a VLM to generate sufficiently coarse scaffold trajectories/object poses that guide RL for dexterous manipulation.</td>
<td nowrap>Dexterous Hand/Grasping</td>
<td nowrap>Vision</td>
<td nowrap>dexterous manipulation / dexterous hand / grasping</td>
<td nowrap>VLM scaffolding + RL refinement</td>
<td nowrap>Simulation</td>
<td nowrap>Addresses the lack of scalable reference trajectories and task rewards for dexterous-hand RL.</td>
<td nowrap><a href="https://arxiv.org/abs/2506.19212">paper</a></td>
<td nowrap><a href="https://sites.google.com/view/dexterous-vlm-scaffolding">project</a></td>
<td nowrap><a href="https://github.com/vdebakker/vlm-scaffolding">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2505.11032">DexGarmentLab: Dexterous Garment Manipulation Environment with Generalizable Policy</a></td>
<td nowrap>DexGarmentLab builds an environment, 3D assets, and generalizable policies for bimanual dexterous garment manipulation.</td>
<td nowrap>bimanual / dexterous-hand garment manipulation</td>
<td nowrap>-</td>
<td nowrap>dexterous manipulation / dexterous hand / grasping</td>
<td nowrap>dexterous manipulation</td>
<td nowrap>Simulation benchmark</td>
<td nowrap>Addresses the lack of realistic simulation environments and efficient data-generation policies for dexterous garment manipulation.</td>
<td nowrap><a href="https://arxiv.org/abs/2505.11032">paper</a></td>
<td nowrap><a href="https://wayrise.github.io/DexGarmentLab/">project</a></td>
<td nowrap><a href="https://github.com/wayrise/DexGarmentLab">code</a></td>
<td nowrap><a href="https://huggingface.co/datasets/wayrise/DexGarmentLab">hf</a></td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2412.02699">UniGraspTransformer: Simplified Policy Distillation for Scalable Dexterous Robotic Grasping</a></td>
<td nowrap>UniGraspTransformer first trains expert trajectories for individual objects with RL, then distills them into a unified Transformer grasping network.</td>
<td nowrap>Dexterous Hand/Grasping</td>
<td nowrap>-</td>
<td nowrap>dexterous manipulation / dexterous hand / grasping</td>
<td nowrap>RL expert trajectories + policy distillation</td>
<td nowrap>state-based + vision-based eval</td>
<td nowrap>Addresses complex large-scale dexterous grasping training pipelines that are hard to scale to many objects.</td>
<td nowrap><a href="https://arxiv.org/abs/2412.02699">paper</a></td>
<td nowrap><a href="https://dexhand.github.io/UniGraspTransformer/">project</a></td>
<td nowrap><a href="https://github.com/microsoft/UniGraspTransformer">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.08257">DexGrasp Anything: Towards Universal Robotic Dexterous Grasping with Physics Awareness</a></td>
<td nowrap>DexGrasp Anything incorporates physical constraints into diffusion grasp generation and releases 3.4M grasp poses / 15K object data.</td>
<td nowrap>Dexterous Hand/Grasping</td>
<td nowrap>-</td>
<td nowrap>dexterous manipulation / dexterous hand / grasping</td>
<td nowrap>physics-aware diffusion grasp generation</td>
<td nowrap>-</td>
<td nowrap>Addresses the quality and physical usability of general dexterous grasp-pose generation for arbitrary objects.</td>
<td nowrap><a href="https://arxiv.org/abs/2503.08257">paper</a></td>
<td nowrap><a href="https://dexgraspanything.github.io/">project</a></td>
<td nowrap><a href="https://github.com/4DVLab/DexGrasp-Anything">code</a></td>
<td nowrap><a href="https://huggingface.co/datasets/GaussionZhong/DexGrasp-Anything">hf</a></td>
<td nowrap>HCP-Survey, EAI-VLA-VLN</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://cvpr.thecvf.com/virtual/2025/poster/32440">ZeroGrasp: Zero-Shot Shape Reconstruction Enabled Robotic Grasping</a></td>
<td nowrap>-</td>
<td nowrap>Dexterous Hand/Grasping</td>
<td nowrap>-</td>
<td nowrap>dexterous manipulation / dexterous hand / grasping</td>
<td nowrap>dexterous manipulation</td>
<td nowrap>-</td>
<td nowrap>Addresses zero-shot shape reconstruction for assisted robotic grasping.</td>
<td nowrap><a href="https://cvpr.thecvf.com/virtual/2025/poster/32440">paper</a></td>
<td nowrap><a href="https://sh8.io/#/zerograsp">project</a></td>
<td nowrap><a href="https://github.com/sh8/ZeroGrasp">code</a></td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
</tbody>
</table>

#### tactile/contact-rich

Total: 13 papers.

<table>
<thead>
<tr>
<th nowrap>Venue/Year</th>
<th nowrap>Paper/Method</th>
<th nowrap>Abstract</th>
<th nowrap>Embodiment Type</th>
<th nowrap>Sensing/Contact</th>
<th nowrap>Control Interface</th>
<th nowrap>Training Mode</th>
<th nowrap>Sim/Real</th>
<th nowrap>Paper Task/Goal</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>Source</th>
<th nowrap>Survey Note</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=dT3ZciXvNX">DexMove: Learning Tactile-Guided Non-Prehensile Manipulation with Dexterous Hands</a></td>
<td nowrap>DexMove combines simulation trajectories with wearable visuotactile human-contact data and trains a flow policy for dexterous-hand nonprehensile object moving.</td>
<td nowrap>dexterous-hand nonprehensile manipulation</td>
<td nowrap>vision-based tactile + contact</td>
<td nowrap>tactile policy / dexterous hand / grasping</td>
<td nowrap>simulation trajectories + wearable visuotactile human contact data + flow policy</td>
<td nowrap>Sim + Real</td>
<td nowrap>Addresses the lack of contact-aware data and wrist-finger coordination policies for dexterous-hand nonprehensile manipulation.</td>
<td nowrap><a href="https://openreview.net/forum?id=dT3ZciXvNX">paper</a></td>
<td nowrap><a href="https://peilin-666.github.io/projects/DexMove/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=ndilONnABZ">AnyTouch 2: General Optical Tactile Representation Learning For Dynamic Tactile Perception</a></td>
<td nowrap>AnyTouch 2 uses ToucHD large-scale dynamic tactile data to learn general force-aware representations across optical tactile sensors.</td>
<td nowrap>Tactile/Contact-rich Manipulation</td>
<td nowrap>tactile / contact</td>
<td nowrap>tactile policy / tactile / contact</td>
<td nowrap>ToucHD pretraining + dynamic tactile representation learning</td>
<td nowrap>-</td>
<td nowrap>Addresses tactile models overfocusing on static properties and lacking dynamic tactile and force information.</td>
<td nowrap><a href="https://openreview.net/forum?id=ndilONnABZ">paper</a></td>
<td nowrap><a href="https://gewu-lab.github.io/AnyTouch2/">project</a></td>
<td nowrap><a href="https://github.com/GeWu-Lab/AnyTouch2">code</a></td>
<td nowrap><a href="https://huggingface.co/collections/BAAI/touchd">hf</a></td>
<td nowrap>-</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=hU2gT2Ucua">APPLE: Toward General Active Perception via Reinforcement Learning</a></td>
<td nowrap>APPLE jointly trains a Transformer perception module and decision policy, using RL to actively acquire sparse information such as tactile signals.</td>
<td nowrap>Tactile/Contact-rich Manipulation</td>
<td nowrap>tactile / contact</td>
<td nowrap>tactile policy / tactile / contact</td>
<td nowrap>RL joint perception-policy learning</td>
<td nowrap>Tactile MNIST / active perception benchmarks</td>
<td nowrap>Addresses active perception methods being strongly task-bound and lacking generalization.</td>
<td nowrap><a href="https://openreview.net/forum?id=hU2gT2Ucua">paper</a></td>
<td nowrap><a href="https://timschneider42.github.io/apple">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Awesome-EAI, WAM</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38882">STOLA: Self-Adaptive Touch-Language Framework for Tactile Commonsense Reasoning in Open-Ended Scenarios</a></td>
<td nowrap>-</td>
<td nowrap>Tactile/Contact-rich Manipulation</td>
<td nowrap>tactile / contact</td>
<td nowrap>tactile policy / tactile / contact</td>
<td nowrap>touch-language reasoning framework</td>
<td nowrap>-</td>
<td nowrap>Addresses commonsense reasoning that combines touch and language in open-world scenes.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38882">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38915">TouchFormer: A Robust Transformer-based Framework for Multimodal Material Perception</a></td>
<td nowrap>-</td>
<td nowrap>Tactile/Contact-rich Manipulation</td>
<td nowrap>tactile + vision / multimodal</td>
<td nowrap>perception model</td>
<td nowrap>Transformer-based material perception</td>
<td nowrap>-</td>
<td nowrap>Addresses robust recognition for multimodal material perception such as vision/tactile sensing.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38915">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38956">Collaborative Representation Learning for Alignment of Tactile, Language, and Vision Modalities</a></td>
<td nowrap>-</td>
<td nowrap>Tactile/Contact-rich Manipulation</td>
<td nowrap>tactile + vision + language</td>
<td nowrap>tactile policy / tactile / contact</td>
<td nowrap>collaborative multimodal representation learning</td>
<td nowrap>-</td>
<td nowrap>Addresses representation alignment across tactile, language, and vision modalities.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38956">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66793">Cross-Tactile Sensor Representation Learning</a></td>
<td nowrap>-</td>
<td nowrap>Tactile/Contact-rich Manipulation</td>
<td nowrap>tactile / contact</td>
<td nowrap>tactile policy / tactile / contact</td>
<td nowrap>tactile policy</td>
<td nowrap>-</td>
<td nowrap>Introduces tactile sensing to improve contact manipulation.</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66793">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/65669">Tabero: Learning Gentle Manipulation with Closed-Loop Force Feedback from Vision, Touch, and Language</a></td>
<td nowrap>-</td>
<td nowrap>Tactile/Contact-rich Manipulation</td>
<td nowrap>vision + touch + language + force feedback</td>
<td nowrap>decoupled force-position commands + hybrid controller</td>
<td nowrap>tactile policy</td>
<td nowrap>-</td>
<td nowrap>Addresses learning gentle manipulation with closed-loop force feedback from vision, touch, and language.</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/65669">paper</a></td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/65669">project</a></td>
<td nowrap><a href="https://github.com/NathanWu7/Tabero">code</a></td>
<td nowrap>Tabero benchmark/model suite</td>
<td nowrap>-</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2505.22566">Universal Visuo-Tactile Video Understanding for Embodied Interaction</a></td>
<td nowrap>VTV-LLM trains a general vision-tactile-language understanding model with VTV150K video-tactile data.</td>
<td nowrap>Tactile/Contact-rich Manipulation</td>
<td nowrap>tactile / contact</td>
<td nowrap>visuo-tactile-language understanding model</td>
<td nowrap>VTV150K multimodal pretraining</td>
<td nowrap>-</td>
<td nowrap>Addresses the difficulty of jointly understanding tactile information with vision and language in embodied interaction.</td>
<td nowrap><a href="https://arxiv.org/abs/2505.22566">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/IvanXie416/VTV-LLM">code</a></td>
<td nowrap><a href="https://huggingface.co/datasets/Ivan416/VBTS_video">hf</a></td>
<td nowrap>-</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2510.21609">Enhancing Tactile-based Reinforcement Learning for Robotic Control</a></td>
<td nowrap>This paper uses self-supervised representation learning and sparse binary tactile signals to improve tactile RL dexterity in complex contact tasks.</td>
<td nowrap>Tactile/Contact-rich Manipulation</td>
<td nowrap>proprioception + sparse binary contacts</td>
<td nowrap>tactile policy / RL / tactile / contact</td>
<td nowrap>tactile RL + self-supervised representation learning</td>
<td nowrap>-</td>
<td nowrap>Addresses unstable tactile RL performance and overreliance on ideal state information.</td>
<td nowrap><a href="https://arxiv.org/abs/2510.21609">paper</a></td>
<td nowrap><a href="https://elle-miller.github.io/tactile_rl/">project</a></td>
<td nowrap><a href="https://github.com/elle-miller/roto">code</a></td>
<td nowrap>RoTO benchmark</td>
<td nowrap>-</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://taccel-simulator.github.io/assets/taccel-paper.pdf">Taccel: Scaling Up Vision-based Tactile Robotics via High-performance GPU Simulation</a></td>
<td nowrap>-</td>
<td nowrap>Tactile/Contact-rich Manipulation</td>
<td nowrap>tactile / contact</td>
<td nowrap>tactile policy / tactile / contact</td>
<td nowrap>GPU tactile simulation</td>
<td nowrap>Simulation</td>
<td nowrap>Addresses the difficulty of scaling robot training with visuotactile sensing in high-performance simulation.</td>
<td nowrap><a href="https://taccel-simulator.github.io/assets/taccel-paper.pdf">paper</a></td>
<td nowrap><a href="https://taccel-simulator.github.io/">project</a></td>
<td nowrap><a href="https://github.com/Taccel-Simulator/Taccel">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2511.16596">Toward Artificial Palpation: Representation Learning of Touch on Soft Bodies</a></td>
<td nowrap>This paper uses a self-supervised encoder to learn representations from soft palpation sequences for tactile imaging and change detection.</td>
<td nowrap>Tactile/Contact-rich Manipulation</td>
<td nowrap>tactile / contact</td>
<td nowrap>tactile policy / tactile / contact</td>
<td nowrap>self-supervised tactile representation learning</td>
<td nowrap>Simulation + Real soft-body/MRI dataset</td>
<td nowrap>Addresses how to learn representations from tactile measurements for downstream tasks in soft medical palpation.</td>
<td nowrap><a href="https://arxiv.org/abs/2511.16596">paper</a></td>
<td nowrap><a href="https://zoharri.github.io/artificial-palpation/">project</a></td>
<td nowrap><a href="https://github.com/zoharri/ArtificialPalpation">code</a></td>
<td nowrap><a href="https://zenodo.org/records/17608184">data</a></td>
<td nowrap>-</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2507.15062v1">Touch in the Wild: Learning Fine-Grained Manipulation with a Portable Visuo-Tactile Gripper</a></td>
<td nowrap>Touch in the Wild collects in-the-wild demonstrations with a portable visuotactile gripper and learns interpretable cross-modal representations to improve fine manipulation policies.</td>
<td nowrap>portable visuotactile gripper + robotic manipulation</td>
<td nowrap>vision + tactile + proprioception</td>
<td nowrap>tactile policy / tactile / contact</td>
<td nowrap>visuo-tactile pretraining + downstream imitation learning</td>
<td nowrap>Real / in-the-wild data + real robot tasks</td>
<td nowrap>Addresses missing tactile data in human demonstration collection and inefficient learning of fine manipulation policies.</td>
<td nowrap><a href="https://arxiv.org/abs/2507.15062v1">paper</a></td>
<td nowrap><a href="https://binghao-huang.github.io/touch_in_the_wild/">project</a></td>
<td nowrap><a href="https://github.com/YolandaXinyueZhu/touch_in_the_wild">code</a></td>
<td nowrap><a href="https://huggingface.co/datasets/binghaohuang-robot/touch_in_the_wild-dataset">hf</a></td>
<td nowrap>-</td>
<td nowrap>Used to observe how embodiment differences change control and data requirements.</td>
</tr>
</tbody>
</table>

### Efficiency / Evaluation / Data

This direction determines whether systems can actually be deployed: on-device inference, caching/quantization/action tokenization, real-time execution, sim2real, benchmarks, and safety evaluation are all necessary conditions.

Subdirections: quantization/cache/tokenization, real-time execution, benchmark/dataset, sim2real, and safety evaluation.

Total: 83 papers.

<table>
<thead>
<tr>
<th nowrap>Subdirection</th>
<th nowrap>Entries</th>
<th nowrap>Focus</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>quantization/cache/tokenization</td>
<td nowrap>17</td>
<td nowrap>Focus: on-device deployment, cache reuse, and action token efficiency.</td>
</tr>
<tr>
<td nowrap>real-time execution</td>
<td nowrap>6</td>
<td nowrap>Focus: low-latency execution and real-time policy inference.</td>
</tr>
<tr>
<td nowrap>benchmark/dataset</td>
<td nowrap>33</td>
<td nowrap>Focus: data coverage, task design, and evaluation credibility.</td>
</tr>
<tr>
<td nowrap>sim2real</td>
<td nowrap>17</td>
<td nowrap>Focus: sim-to-real transfer and the real-world deployment gap.</td>
</tr>
<tr>
<td nowrap>safety evaluation</td>
<td nowrap>10</td>
<td nowrap>Focus: robustness, safety, and deployment risk evaluation.</td>
</tr>
</tbody>
</table>

#### quantization/cache/tokenization

Total: 17 papers.

<table>
<thead>
<tr>
<th nowrap>Venue/Year</th>
<th nowrap>Paper/Method</th>
<th nowrap>Abstract</th>
<th nowrap>Object Type</th>
<th nowrap>Efficiency Metric</th>
<th nowrap>Platform/Hardware</th>
<th nowrap>Covered Tasks</th>
<th nowrap>Open Resource Status</th>
<th nowrap>Paper Task/Goal</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>Source</th>
<th nowrap>Survey Note</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=E1K2Ph3LtS">MetaVLA: Unified Meta Co-Training for Efficient Embodied Adaptation</a></td>
<td nowrap>Uses meta co-training to merge multi-task adaptation into low-cost post-training, reducing VLA fine-tuning compute and improving LIBERO generalization.</td>
<td nowrap>compression/cache/tokenization</td>
<td nowrap>meta co-training</td>
<td nowrap>robot deployment/evaluation environment</td>
<td nowrap>LIBERO manipulation</td>
<td nowrap>Code planned</td>
<td nowrap>Addresses the high cost and weak generalization of VLA task adaptation.</td>
<td nowrap><a href="https://openreview.net/forum?id=E1K2Ph3LtS">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=RwdGIIjPlC">SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration</a></td>
<td nowrap>Uses action-aware model scheduling and spatiotemporal semantic token pruning to speed up VLA in LIBERO/SimplerEnv without performance loss.</td>
<td nowrap>compression/cache/tokenization</td>
<td nowrap>model scheduling + token pruning</td>
<td nowrap>robot deployment/evaluation environment</td>
<td nowrap>LIBERO, SimplerEnv</td>
<td nowrap>-</td>
<td nowrap>Addresses temporal and visual redundancy in VLA sequential decision-making.</td>
<td nowrap><a href="https://openreview.net/forum?id=RwdGIIjPlC">paper</a> / <a href="https://arxiv.org/abs/2506.12723">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Efficient-VLA</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=TpL2nXanru">QVLA: Not All Channels Are Equal in Vision-Language-Action Model&#x27;s Quantization</a></td>
<td nowrap>Proposes action-sensitive per-channel mixed-bit quantization to compress VLA to low memory while preserving success rate.</td>
<td nowrap>compression/cache/tokenization</td>
<td nowrap>channel-wise action-centric quantization/pruning</td>
<td nowrap>resource-constrained robot hardware</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Addresses why LLM-style uniform quantization is unsuitable for accumulated robot action errors.</td>
<td nowrap><a href="https://openreview.net/forum?id=TpL2nXanru">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=ea6j8k8Rnw">Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation</a></td>
<td nowrap>Dynamically adjusts the visual token retention rate based on recent action trajectories to reduce inference latency for long-horizon VLA manipulation.</td>
<td nowrap>compression/cache/tokenization</td>
<td nowrap>action-aware dynamic visual token pruning</td>
<td nowrap>robot deployment/evaluation environment</td>
<td nowrap>LIBERO + real-world manipulation</td>
<td nowrap>-</td>
<td nowrap>Addresses the mismatch between fixed pruning and phase-dependent visual redundancy during manipulation.</td>
<td nowrap><a href="https://openreview.net/forum?id=ea6j8k8Rnw">paper</a> / <a href="https://arxiv.org/abs/2509.22093">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN, Efficient-VLA</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=k6nTUFoqeT">FASTer: Toward Powerful and Efficient Autoregressive Vision–Language–Action Models with Learnable Action Tokenizer and Block-wise Decoding</a></td>
<td nowrap>Uses a learnable action tokenizer and block-wise decoding to improve action compression, speed, and task performance in autoregressive VLA.</td>
<td nowrap>compression/cache/tokenization</td>
<td nowrap>learnable action tokenizer + block-wise decoding</td>
<td nowrap>robot deployment/evaluation environment</td>
<td nowrap>sim+real manipulation</td>
<td nowrap>-</td>
<td nowrap>Addresses the tradeoff between reconstruction quality and inference efficiency in action tokenization.</td>
<td nowrap><a href="https://openreview.net/forum?id=k6nTUFoqeT">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>HCP-Survey, Awesome-EAI, EAI-VLA-VLN, EAI-Safety, RL-VLA</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38880">FT-NCFM: An Influence-Aware Data Distillation Framework for Efficient VLA Models</a></td>
<td nowrap>Uses causal attribution and adversarial NCFM to distill high-value VLA data, allowing a small coreset to approach full-data training performance.</td>
<td nowrap>compression/cache/tokenization</td>
<td nowrap>data distillation</td>
<td nowrap>robot deployment/evaluation environment</td>
<td nowrap>-</td>
<td nowrap>Code+Data planned</td>
<td nowrap>Addresses the high training cost caused by VLA reliance on large-scale redundant data.</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38903">CronusVLA: Towards Efficient and Robust Manipulation via Multi-Frame Vision-Language-Action Modeling</a></td>
<td nowrap>CronusVLA improves VLA manipulation robustness through multi-frame historical feature aggregation while controlling multi-frame inference cost.</td>
<td nowrap>compression/cache/tokenization</td>
<td nowrap>tokenization</td>
<td nowrap>robot deployment/evaluation environment</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Addresses the inability of single-frame VLA to use historical observations and the high latency of directly inputting multiple frames.</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38904">SemanticVLA: Semantic-Aligned Sparsification and Enhancement for Efficient Robotic Manipulation</a></td>
<td nowrap>Improves VLA manipulation efficiency and success rate through semantically aligned visual sparsification, hierarchical fusion, and action coupling.</td>
<td nowrap>compression/cache/tokenization</td>
<td nowrap>semantic-aligned sparsification</td>
<td nowrap>robot deployment/evaluation environment</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Addresses how visual redundancy and shallow instruction-vision alignment affect robot manipulation.</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/JiuTian-VL/SemanticVLA">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38931">VLA-Adapter: An Effective Paradigm for Tiny-Scale Vision-Language-Action Model</a></td>
<td nowrap>Uses a small-scale VLA adaptation paradigm to preserve robot manipulation ability at smaller model sizes.</td>
<td nowrap>compression/cache/tokenization</td>
<td nowrap>tiny-scale VLA adapter</td>
<td nowrap>robot deployment/evaluation environment</td>
<td nowrap>-</td>
<td nowrap>Project+Code</td>
<td nowrap>Addresses how tiny-scale VLA can be effectively adapted to manipulation tasks.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38931">paper</a> / <a href="https://arxiv.org/abs/2509.09372">paper</a></td>
<td nowrap><a href="https://vla-adapter.github.io/">project</a></td>
<td nowrap><a href="https://github.com/OpenHelix-Team/VLA-Adapter">code</a></td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN, Awesome-VLA, Efficient-VLA, RL-VLA</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38945">MoLe-VLA: Dynamic Layer-skipping Vision Language Action Model via Mixture-of-Layers for Efficient Robot Manipulation</a></td>
<td nowrap>Uses mixture-of-layers dynamic layer skipping to reduce VLA compute while preserving manipulation success rate.</td>
<td nowrap>compression/cache/tokenization</td>
<td nowrap>dynamic layer skipping / up to 5.6x compute reduction</td>
<td nowrap>robot deployment/evaluation environment</td>
<td nowrap>-</td>
<td nowrap>Project+Code</td>
<td nowrap>Addresses the fact that different samples/steps in VLA inference do not need to pass through all layers.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38945">paper</a> / <a href="https://arxiv.org/abs/2503.20384">paper</a></td>
<td nowrap><a href="https://sites.google.com/view/mole-vla">project</a></td>
<td nowrap><a href="https://github.com/RoyZry98/MoLe-VLA-Pytorch/">code</a></td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN, Efficient-VLA</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2602.20309">QuantVLA: Scale-Calibrated Post-Training Quantization for Vision-Language-Action Models</a></td>
<td nowrap>Proposes training-free PTQ quantization for the VLA language backbone and DiT action head, significantly saving memory.</td>
<td nowrap>compression/cache/tokenization</td>
<td nowrap>PTQ</td>
<td nowrap>compute/memory/power constrained deployment</td>
<td nowrap>-</td>
<td nowrap>Project+Code</td>
<td nowrap>Addresses quantization for large VLA models under low-compute/low-power deployment.</td>
<td nowrap><a href="https://arxiv.org/abs/2602.20309">paper</a></td>
<td nowrap><a href="https://quantvla.github.io/">project</a></td>
<td nowrap><a href="https://github.com/AIoT-MLSys-Lab/QuantVLA">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.06072">BEAST: Efficient Tokenization of B-Splines Encoded Action Sequences for Imitation Learning</a></td>
<td nowrap>Encodes action sequences as fixed-length tokens with B-splines, avoiding separate tokenizer training and generating smooth high-frequency control.</td>
<td nowrap>compression/cache/tokenization</td>
<td nowrap>B-spline action tokenizer</td>
<td nowrap>robot deployment/evaluation environment</td>
<td nowrap>166 sim tasks + 8 real tasks</td>
<td nowrap>-</td>
<td nowrap>Addresses the cost of action-sequence tokenization in imitation learning and the need for trajectory smoothness.</td>
<td nowrap><a href="https://arxiv.org/abs/2506.06072">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.14259">Quantization-Free Autoregressive Action Transformer</a></td>
<td nowrap>Uses a continuous infinite-vocabulary Transformer to model actions directly, avoiding damage to action-space structure from discrete quantization.</td>
<td nowrap>continuous autoregressive action modeling</td>
<td nowrap>quantization-free continuous autoregressive action modeling</td>
<td nowrap>robot deployment/evaluation environment</td>
<td nowrap>Reduce model deployment cost.</td>
<td nowrap>Code</td>
<td nowrap>Addresses how discrete action codes limit continuous control in autoregressive imitation learning.</td>
<td nowrap><a href="https://arxiv.org/abs/2503.14259">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.10100">EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models</a></td>
<td nowrap>Achieves training-free VLA acceleration and compression through language-layer pruning, visual token selection, and diffusion feature caching.</td>
<td nowrap>compression/cache/tokenization</td>
<td nowrap>layer pruning + visual token selection + diffusion cache</td>
<td nowrap>robot deployment/evaluation environment</td>
<td nowrap>CogACT/SIMPLER</td>
<td nowrap>-</td>
<td nowrap>Addresses redundancy across language, vision, and action-head components in the VLA pipeline.</td>
<td nowrap><a href="https://arxiv.org/abs/2506.10100">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Efficient-VLA</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2502.02175">VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching</a></td>
<td nowrap>Adaptively reuses the KV cache of static visual tokens in adjacent frames to improve VLA control frequency.</td>
<td nowrap>compression/cache/tokenization</td>
<td nowrap>adaptive visual token KV caching</td>
<td nowrap>robot deployment/evaluation environment</td>
<td nowrap>LIBERO, SIMPLER, real robot</td>
<td nowrap>Project+Code</td>
<td nowrap>Addresses repeated per-frame visual computation in real-time robot control.</td>
<td nowrap><a href="https://arxiv.org/abs/2502.02175">paper</a></td>
<td nowrap><a href="https://vla-cache.github.io/">project</a></td>
<td nowrap><a href="https://github.com/siyuhsu/vla-cache">code</a></td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN, Efficient-VLA</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2507.01016">VQ-VLA: Improving Vision-Language-Action Models via Scaling Vector-Quantized Action Tokenizers</a></td>
<td nowrap>Trains a VQ action tokenizer on large-scale synthetic/real trajectories to improve VLA inference speed and long-horizon action quality.</td>
<td nowrap>compression/cache/tokenization</td>
<td nowrap>vector-quantized action tokenizer</td>
<td nowrap>robot deployment/evaluation environment</td>
<td nowrap>-</td>
<td nowrap>Project+Code</td>
<td nowrap>Addresses insufficient data scale and weak generalization for action tokenizers.</td>
<td nowrap><a href="https://arxiv.org/abs/2507.01016">paper</a></td>
<td nowrap><a href="https://xiaoxiao0406.github.io/vqvla.github.io">project</a> / <a href="https://xiaoxiao0406.github.io/vqvla.github.io/">project</a></td>
<td nowrap><a href="https://github.com/xiaoxiao0406/VQ-VLA">code</a></td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN, Efficient-VLA</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2505.15304">Saliency-Aware Quantized Imitation Learning for Efficient Robotic Control</a></td>
<td nowrap>Uses saliency-aware quantization to compress imitation learning policies, balancing efficient control and task performance.</td>
<td nowrap>compression/cache/tokenization</td>
<td nowrap>saliency-aware quantized imitation learning</td>
<td nowrap>robot deployment/evaluation environment</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Addresses the loss of key perception/action information when quantizing robot control policies.</td>
<td nowrap><a href="https://arxiv.org/abs/2505.15304">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Efficient-VLA</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
</tbody>
</table>

#### real-time execution

Total: 6 papers.

<table>
<thead>
<tr>
<th nowrap>Venue/Year</th>
<th nowrap>Paper/Method</th>
<th nowrap>Abstract</th>
<th nowrap>Object Type</th>
<th nowrap>Efficiency Metric</th>
<th nowrap>Platform/Hardware</th>
<th nowrap>Covered Tasks</th>
<th nowrap>Open Resource Status</th>
<th nowrap>Paper Task/Goal</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>Source</th>
<th nowrap>Survey Note</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=INsLvSCJ4z">Time Optimal Execution of Action Chunk Policies Beyond Demonstration Speed</a></td>
<td nowrap>Optimizes action chunk policy execution time beyond demonstration speed while preserving action feasibility.</td>
<td nowrap>real-time execution</td>
<td nowrap>time-optimal execution</td>
<td nowrap>robot deployment/evaluation environment</td>
<td nowrap>action chunk policy execution</td>
<td nowrap>-</td>
<td nowrap>Addresses action chunk policy execution being limited by demonstration speed.</td>
<td nowrap><a href="https://openreview.net/forum?id=INsLvSCJ4z">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=mIeKe74W43">Mean Flow Policy with Instantaneous Velocity Constraint for One-step Action Generation</a></td>
<td nowrap>Adds instantaneous velocity constraints to mean flow policy to enable one-step action generation and executable control.</td>
<td nowrap>real-time execution</td>
<td nowrap>one-step action generation + velocity constraint</td>
<td nowrap>robot deployment/evaluation environment</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Addresses slow multi-step sampling and missing velocity constraints in flow policy.</td>
<td nowrap><a href="https://openreview.net/forum?id=mIeKe74W43">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=r0RGJ1j9on">Real-Time Robot Execution with Masked Action Chunking</a></td>
<td nowrap>Uses masked action chunking to support real-time robot execution and reduce mismatch between chunk inference and control.</td>
<td nowrap>real-time execution</td>
<td nowrap>masked action chunking</td>
<td nowrap>robot deployment/evaluation environment</td>
<td nowrap>real-time robot execution</td>
<td nowrap>-</td>
<td nowrap>Addresses latency in real-time closed-loop execution of action chunking policies.</td>
<td nowrap><a href="https://openreview.net/forum?id=r0RGJ1j9on">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Efficient-VLA, Humanoid-RL, EAI-Safety, WAM</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://www.physicalintelligence.company/download/real_time_chunking.pdf">Real-Time Execution of Action Chunking Flow Policies</a></td>
<td nowrap>Physical Intelligence proposes a real-time execution mechanism for action chunking flow policy.</td>
<td nowrap>real-time execution</td>
<td nowrap>real-time</td>
<td nowrap>robot deployment/evaluation environment</td>
<td nowrap>-</td>
<td nowrap>Project</td>
<td nowrap>Addresses how to execute action chunks generated by flow policy stably with low latency.</td>
<td nowrap><a href="https://www.physicalintelligence.company/download/real_time_chunking.pdf">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>HCP-Survey, Awesome-EAI, EAI-VLA-VLN, Efficient-VLA, Humanoid-RL, EAI-Safety, WAM</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://www.arxiv.org/abs/2505.10646">Accelerating Visual-Policy Learning through Parallel Differentiable Simulation</a></td>
<td nowrap>Uses parallel differentiable simulation to accelerate visual policy learning and training feedback.</td>
<td nowrap>parallel differentiable simulation</td>
<td nowrap>real-time</td>
<td nowrap>simulation</td>
<td nowrap>-</td>
<td nowrap>Project</td>
<td nowrap>Addresses slow training of visual policies in real/serial simulation.</td>
<td nowrap><a href="https://www.arxiv.org/abs/2505.10646">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2508.00697">On-Device Diffusion Transformer Policy for Efficient Robot Manipulation</a></td>
<td nowrap>Deploys diffusion transformer policy to on-device real-time robot manipulation through pruning/distillation.</td>
<td nowrap>real-time execution</td>
<td nowrap>latency + pruning/distillation</td>
<td nowrap>on-device/mobile robot hardware</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Addresses excessive latency of Diffusion Transformer Policy on edge devices.</td>
<td nowrap><a href="https://arxiv.org/abs/2508.00697">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN, Efficient-VLA</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
</tbody>
</table>

#### benchmark/dataset

Total: 33 papers.

<table>
<thead>
<tr>
<th nowrap>Venue/Year</th>
<th nowrap>Paper/Method</th>
<th nowrap>Abstract</th>
<th nowrap>Object Type</th>
<th nowrap>Efficiency Metric</th>
<th nowrap>Platform/Hardware</th>
<th nowrap>Covered Tasks</th>
<th nowrap>Open Resource Status</th>
<th nowrap>Paper Task/Goal</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>Source</th>
<th nowrap>Survey Note</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ICRA 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2509.14687">RealMirror: A Comprehensive, Open-Source Vision-Language-Action Platform for Embodied AI</a></td>
<td nowrap>RealMirror 提供 VLA 数据采集、仿真、训练、评测和 zero-shot sim2real 平台。</td>
<td nowrap>VLA platform / benchmark</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>simulation/evaluation environment</td>
<td nowrap>humanoid VLA research</td>
<td nowrap>project/code/models available</td>
<td nowrap>降低 VLA 数据、训练和评测门槛。</td>
<td nowrap><a href="https://arxiv.org/abs/2509.14687">paper</a></td>
<td nowrap><a href="https://terminators2025.github.io/RealMirror.github.io/">project</a></td>
<td nowrap><a href="https://github.com/terminators2025/RealMirror">code</a></td>
<td nowrap><a href="https://huggingface.co/zte-terminators/realmirror-model-ckpt">hf</a></td>
<td nowrap>ICRA/IROS</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>IROS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2412.05313">lambda: A Benchmark for Data-Efficiency in Long-Horizon Indoor Mobile Manipulation Robotics</a></td>
<td nowrap>lambda benchmark 评测长程室内移动操作在数据效率、语言任务和多房间场景下的表现。</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>data efficiency</td>
<td nowrap>indoor mobile manipulation benchmark</td>
<td nowrap>long-horizon mobile manipulation</td>
<td nowrap>project/code/data available</td>
<td nowrap>补足长程移动操作数据效率评测。</td>
<td nowrap><a href="https://arxiv.org/abs/2412.05313">paper</a></td>
<td nowrap><a href="https://lambdabenchmark.github.io/">project</a></td>
<td nowrap><a href="https://github.com/h2r/LAMBDA">code</a></td>
<td nowrap><a href="https://github.com/h2r/LAMBDA">data</a></td>
<td nowrap>ICRA/IROS</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>ICRA 2025</td>
<td nowrap><a href="https://github.com/BAAI-DCAI/SpatialBot">SpatialBot: Precise Spatial Understanding with Vision Language Models</a></td>
<td nowrap>SpatialBot 面向 VLM 精确空间理解，提供 embodiment 数据、SpatialQA 和 SpatialBench。</td>
<td nowrap>spatial understanding benchmark</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>VLM spatial reasoning</td>
<td nowrap>embodied spatial QA</td>
<td nowrap>model/data/benchmark available</td>
<td nowrap>评测 VLM 是否具备可用于机器人操作的精确空间理解。</td>
<td nowrap><a href="https://github.com/BAAI-DCAI/SpatialBot">paper</a></td>
<td nowrap><a href="https://github.com/BAAI-DCAI/SpatialBot">project</a></td>
<td nowrap><a href="https://github.com/BAAI-DCAI/SpatialBot">code</a></td>
<td nowrap><a href="https://github.com/BAAI-DCAI/SpatialBot">data</a></td>
<td nowrap>ICRA/IROS</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=TRwQND3xpt">D2E: Scaling Vision-Action Pretraining on Desktop Data for Transfer to Embodied AI</a></td>
<td nowrap>Uses desktop interaction data to scale vision-action pretraining and transfer it to embodied tasks.</td>
<td nowrap>desktop-to-embodied dataset/pretraining</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>simulation/evaluation environment</td>
<td nowrap>vision-action transfer</td>
<td nowrap>-</td>
<td nowrap>Addresses how to use desktop data for pretraining when robot data is scarce.</td>
<td nowrap><a href="https://openreview.net/forum?id=TRwQND3xpt">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=PGUC3mmMoi">RoboInter: A Holistic Intermediate Representation Suite Towards Robotic Manipulation</a></td>
<td nowrap>Builds a suite of intermediate representations for robot manipulation to unify evaluation of understanding, planning, and action.</td>
<td nowrap>intermediate representation suite</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>simulation/evaluation environment</td>
<td nowrap>robotic manipulation</td>
<td nowrap>-</td>
<td nowrap>Addresses the lack of reusable intermediate-representation benchmarks for manipulation learning.</td>
<td nowrap><a href="https://openreview.net/forum?id=PGUC3mmMoi">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=UUE6HEtjhu">AutoBio: A Simulation and Benchmark for Robotic Automation in Digital Biology Laboratory</a></td>
<td nowrap>Provides simulation and benchmarks for robot automation in digital biology labs.</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>digital biology laboratory simulation</td>
<td nowrap>lab automation</td>
<td nowrap>-</td>
<td nowrap>Addresses the lack of simulation and evaluation environments for biology-lab automation.</td>
<td nowrap><a href="https://openreview.net/forum?id=UUE6HEtjhu">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=azj53PLJRL">Image Quality Assessment for Embodied AI</a></td>
<td nowrap>Studies embodied AI observation image quality assessment and its impact on task performance.</td>
<td nowrap>image quality benchmark</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>simulation/evaluation environment</td>
<td nowrap>embodied perception/evaluation</td>
<td nowrap>-</td>
<td nowrap>Addresses the lack of task-relevant evaluation for embodied perception input quality.</td>
<td nowrap><a href="https://openreview.net/forum?id=azj53PLJRL">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=tQJYKwc3n4">RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots</a></td>
<td nowrap>Provides a large-scale home-scene simulation framework for training and evaluating general-purpose robots.</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>RoboCasa simulation</td>
<td nowrap>generalist household robotics</td>
<td nowrap>-</td>
<td nowrap>Addresses the lack of diverse, long-horizon, scalable simulation benchmarks for general-purpose robots.</td>
<td nowrap><a href="https://openreview.net/forum?id=tQJYKwc3n4">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Humanoid-RL</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38875">H-RDT: Human Manipulation Enhanced Bimanual Robotic Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>simulation/evaluation environment</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38875">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN, Humanoid-RL</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38883">PEOD: A Pixel-Aligned Event-RGB Benchmark for Object Detection Under Challenging Conditions</a></td>
<td nowrap>-</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>simulation/evaluation environment</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38883">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38913">SIAM: Towards Generalizable Articulated Object Modeling via Single Robot-Object Interaction</a></td>
<td nowrap>-</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>simulation/evaluation environment</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38913">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38923">VirtualEnv: A Platform for Embodied AI Research</a></td>
<td nowrap>-</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>simulation/evaluation environment</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38923">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38930">Lifelong Language-Conditioned Robotic Manipulation Learning</a></td>
<td nowrap>-</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>simulation/evaluation environment</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38930">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64411">AIR-VLA: Vision-Language-Action Systems for Aerial Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>UAV / aerial robot</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64411">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Awesome-EAI</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/63391">DLO-Lab: Benchmarking Deformable Linear Object Manipulations with Differentiable Physics</a></td>
<td nowrap>-</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>simulation/evaluation environment</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/63391">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/63416">ManiSoft: Towards Vision-Language Manipulation for Soft Robotics</a></td>
<td nowrap>-</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>robot deployment/evaluation environment</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/63416">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64619">OXE-AugE: A Large-Scale Robot Augmentation of OXE for Scaling Cross-Embodiment Policy Learning</a></td>
<td nowrap>-</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>robot deployment/evaluation environment</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64619">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.07961">BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models</a></td>
<td nowrap>Uses input-output alignment and the BridgeVLA dataset to improve the learning efficiency of VLM-to-3D manipulation policies.</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>robot deployment/evaluation environment</td>
<td nowrap>3D manipulation</td>
<td nowrap>Project+Code+Data/Bench</td>
<td nowrap>Addresses input-output space mismatch when VLMs learn 3D manipulation.</td>
<td nowrap><a href="https://arxiv.org/abs/2506.07961">paper</a></td>
<td nowrap><a href="https://bridgevla.github.io/">project</a></td>
<td nowrap><a href="https://github.com/BridgeVLA/BridgeVLA">code</a></td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.14763">RobotSmith: Generative Robotic Tool Design for Acquisition of Complex Manipulation Skills</a></td>
<td nowrap>Uses generative tool design to give robots complex manipulation skills for rigid, deformable, and fluid objects.</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>robot deployment/evaluation environment</td>
<td nowrap>tool-design manipulation</td>
<td nowrap>Project+Code</td>
<td nowrap>Addresses the need for robots to use task-specific tools to complete complex manipulation.</td>
<td nowrap><a href="https://arxiv.org/abs/2506.14763">paper</a></td>
<td nowrap><a href="https://umass-embodied-agi.github.io/RobotSmith/">project</a></td>
<td nowrap><a href="https://github.com/UMass-Embodied-AGI/RobotSmith">code</a></td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2511.00940">URDF-Anything: Constructing Articulated Objects with 3D Multimodal Language Model</a></td>
<td nowrap>Uses a 3D multimodal language model to construct articulated-object URDFs from multimodal inputs.</td>
<td nowrap>articulated object URDF construction</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>robot deployment/evaluation environment</td>
<td nowrap>3D object modeling for simulation</td>
<td nowrap>-</td>
<td nowrap>Addresses the high cost of building articulated object URDFs for simulation/robot interaction.</td>
<td nowrap><a href="https://arxiv.org/abs/2511.00940">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.08822">FreqPolicy: Efficient Flow-based Visuomotor Policy via Frequency Consistency</a></td>
<td nowrap>Uses frequency consistency constraints to improve the efficiency and stability of flow-based visuomotor policies.</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>frequency consistency</td>
<td nowrap>robot deployment/evaluation environment</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Addresses high-frequency/low-frequency action inconsistency in flow policy for visuomotor control.</td>
<td nowrap><a href="https://arxiv.org/abs/2506.08822">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN, Efficient-VLA</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://www.arxiv.org/pdf/2506.06677">RoboCerebra: A Large-scale Benchmark for Long-horizon Robotic Manipulation Evaluation</a></td>
<td nowrap>Provides a long-horizon home robot manipulation benchmark for evaluating planning, reflection, and memory.</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>simulation/evaluation environment</td>
<td nowrap>100 task variants / 1,000 trajectories</td>
<td nowrap>Project+Code+Data/Bench</td>
<td nowrap>Addresses the lack of systematic evaluation for long-horizon robot manipulation.</td>
<td nowrap><a href="https://www.arxiv.org/pdf/2506.06677">paper</a> / <a href="https://arxiv.org/pdf/2506.06677">paper</a></td>
<td nowrap><a href="https://robocerebra.github.io/">project</a></td>
<td nowrap><a href="https://github.com/qiuboxiang/RoboCerebra">code</a> / <a href="https://github.com/buaa-colalab/RoboCerebra">code</a></td>
<td nowrap><a href="https://huggingface.co/datasets/qiukingballball/RoboCerebra">hf</a> / <a href="https://huggingface.co/datasets/qiukingballball/RoboCerebraBench">hf</a></td>
<td nowrap>EAI-VLA-VLN, WAM</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://suturebot.github.io/static/SutureBot_NeurIPS_2025.pdf">SutureBot: A Precision Framework &amp; Benchmark For Autonomous End-to-End Suturing</a></td>
<td nowrap>Provides a dVRK end-to-end autonomous suturing framework, dataset, and fine-grained evaluation benchmark.</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>dVRK Si + wrist cameras/endoscope</td>
<td nowrap>-</td>
<td nowrap>Project+Code+Data/Bench</td>
<td nowrap>Addresses the lack of end-to-end benchmarks and data for autonomous robotic suturing.</td>
<td nowrap><a href="https://suturebot.github.io/static/SutureBot_NeurIPS_2025.pdf">paper</a></td>
<td nowrap><a href="https://suturebot.github.io/">project</a></td>
<td nowrap><a href="https://github.com/SutureBot/SutureBot/tree/ACT">code</a></td>
<td nowrap><a href="https://huggingface.co/datasets/jchen396/SutureBot">hf</a></td>
<td nowrap>-</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.08367">Embodied Crowd Counting</a></td>
<td nowrap>-</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>robot deployment/evaluation environment</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://arxiv.org/abs/2503.08367">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2412.06782">CARP: Visuomotor Policy Learning via Coarse-to-Fine Autoregressive Prediction</a></td>
<td nowrap>Improves visuomotor policy learning through coarse-to-fine autoregressive prediction.</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>robot deployment/evaluation environment</td>
<td nowrap>-</td>
<td nowrap>Project</td>
<td nowrap>Addresses the difficulty of direct continuous robot action prediction and long-horizon error accumulation.</td>
<td nowrap><a href="https://arxiv.org/abs/2412.06782">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.16408">RoboFactory: Exploring Embodied Agent Collaboration with Compositional Constraints</a></td>
<td nowrap>Builds a collaborative simulation and dataset for multiple embodied agents with compositional constraints.</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>simulation</td>
<td nowrap>-</td>
<td nowrap>Project+Code+Data/Bench</td>
<td nowrap>Addresses insufficient evaluation of compositional constraints in embodied agent collaboration tasks.</td>
<td nowrap><a href="https://arxiv.org/abs/2503.16408">paper</a></td>
<td nowrap><a href="https://iranqin.github.io/robofactory/">project</a></td>
<td nowrap><a href="https://github.com/MARS-EAI/RoboFactory">code</a></td>
<td nowrap><a href="https://huggingface.co/datasets/FACEONG/RoboFactory_Dataset">hf</a></td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2504.10414">HUMOTO: A 4D Dataset of Mocap Human Object Interactions</a></td>
<td nowrap>Provides a 4D motion-capture dataset for human-object interaction.</td>
<td nowrap>4D mocap HOI dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>simulation/evaluation environment</td>
<td nowrap>-</td>
<td nowrap>Project</td>
<td nowrap>Addresses the shortage of dynamic data for humans manipulating objects.</td>
<td nowrap><a href="https://arxiv.org/abs/2504.10414">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Humanoid-RL</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2412.07215">RoboTron-Mani: All-in-One Multimodal Large Model for Robotic Manipulation</a></td>
<td nowrap>Proposes the RoboTron-Mani model and RoboData, using multimodal data to support robot manipulation.</td>
<td nowrap>RoboTron-Mani + RoboData</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>robot deployment/evaluation environment</td>
<td nowrap>-</td>
<td nowrap>Code+Data/Bench</td>
<td nowrap>Addresses the need for unified multimodal training and evaluation data for robot manipulation models.</td>
<td nowrap><a href="https://arxiv.org/abs/2412.07215">paper</a> / <a href="https://arxiv.org/pdf/2412.07215">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/RoboUniview/RoboMM">code</a></td>
<td nowrap><a href="https://huggingface.co/datasets/liufanfanlff/RoboData">hf</a></td>
<td nowrap>EAI-VLA-VLN, WAM</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.11117">Beyond the Destination: A Novel Benchmark for Exploration-Aware Embodied Question Answering</a></td>
<td nowrap>Proposes EXPRESS-Bench, which binds exploration trajectories with QA to evaluate embodied QA.</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>simulation/evaluation environment</td>
<td nowrap>777 trajectories / 2,044 QA pairs</td>
<td nowrap>Code</td>
<td nowrap>Addresses EQA focusing only on destinations and not evaluating the exploration process.</td>
<td nowrap><a href="https://arxiv.org/abs/2503.11117">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EXPRESS-Bench</td>
<td nowrap>HCP-Survey</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/1787">RobAVA: A Large-scale Dataset and Baseline Towards Video based Robotic Arm Action Understanding</a></td>
<td nowrap>-</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>simulation/evaluation environment</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Provide training/evaluation data resources.</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/1787">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/2215">RoboAnnotatorX: A Comprehensive and Universal Annotation Framework for Accurate Understanding of Long-horizon Robot Demonstration</a></td>
<td nowrap>-</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>robot deployment/evaluation environment</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/2215">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>ICML 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2502.09560">EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents</a></td>
<td nowrap>Comprehensively evaluates MLLMs' navigation, interaction, and reasoning abilities in visually driven embodied agents.</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>simulation/evaluation environment</td>
<td nowrap>1,128 tasks / 4 environments / 6 capability subsets</td>
<td nowrap>Project+Code</td>
<td nowrap>Addresses the lack of unified benchmarks for embodied capabilities of multimodal large models.</td>
<td nowrap><a href="https://arxiv.org/abs/2502.09560">paper</a></td>
<td nowrap><a href="https://embodiedbench.github.io/">project</a></td>
<td nowrap><a href="https://github.com/EmbodiedBench/EmbodiedBench">code</a></td>
<td nowrap>-</td>
<td nowrap>HCP-Survey, EAI-Safety</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2411.18025">Pixel-aligned RGB-NIR Stereo Imaging and Dataset for Robot Vision</a></td>
<td nowrap>Provides a pixel-aligned RGB-NIR binocular imaging system and robot vision dataset.</td>
<td nowrap>RGB-NIR stereo dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>simulation/evaluation environment</td>
<td nowrap>robot vision</td>
<td nowrap>-</td>
<td nowrap>Addresses the lack of aligned data for robot vision under visible-light/NIR fusion.</td>
<td nowrap><a href="https://arxiv.org/abs/2411.18025">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
</tbody>
</table>

#### sim2real

Total: 17 papers.

<table>
<thead>
<tr>
<th nowrap>Venue/Year</th>
<th nowrap>Paper/Method</th>
<th nowrap>Abstract</th>
<th nowrap>Object Type</th>
<th nowrap>Efficiency Metric</th>
<th nowrap>Platform/Hardware</th>
<th nowrap>Covered Tasks</th>
<th nowrap>Open Resource Status</th>
<th nowrap>Paper Task/Goal</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>Source</th>
<th nowrap>Survey Note</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=W3Q2xvrZtx">PD$^{2}$GS: Part-Level Decoupling and Continuous Deformation of Articulated Objects via Gaussian Splatting</a></td>
<td nowrap>Models articulated objects using part-level disentanglement and continuously deformable Gaussian representations.</td>
<td nowrap>articulated object Gaussian Splatting</td>
<td nowrap>sim2real</td>
<td nowrap>simulation/evaluation environment</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Addresses deformable modeling of articulated objects in real/simulated settings.</td>
<td nowrap><a href="https://openreview.net/forum?id=W3Q2xvrZtx">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=sWyX1BpeN4">Manipulation as in Simulation: Enabling Accurate Geometry Perception in Robots</a></td>
<td nowrap>Enables robots to obtain simulation-like accurate geometric perception to improve real-world manipulation.</td>
<td nowrap>geometry perception for manipulation</td>
<td nowrap>sim2real</td>
<td nowrap>simulation/evaluation environment</td>
<td nowrap>real robot manipulation</td>
<td nowrap>-</td>
<td nowrap>Addresses the sim2real manipulation gap caused by geometric perception noise on real robots.</td>
<td nowrap><a href="https://openreview.net/forum?id=sWyX1BpeN4">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=nAO9LcV7nE">Emergent Dexterity Via Diverse Resets and Large-Scale Reinforcement Learning</a></td>
<td nowrap>Elicits dexterous manipulation abilities through diverse resets and large-scale RL training.</td>
<td nowrap>dexterous RL</td>
<td nowrap>sim2real</td>
<td nowrap>sim + robot hand likely</td>
<td nowrap>dexterous manipulation</td>
<td nowrap>-</td>
<td nowrap>Addresses training dexterous manipulation policies in simulation for recovery from complex states.</td>
<td nowrap><a href="https://openreview.net/forum?id=nAO9LcV7nE">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=H4SyKHjd4c">Sim2Real VLA: Zero-Shot Generalization of Synthesized Skills to Realistic Manipulation</a></td>
<td nowrap>Transfers synthetically skill-trained VLA zero-shot to photorealistic manipulation environments.</td>
<td nowrap>sim2real VLA</td>
<td nowrap>sim2real</td>
<td nowrap>simulation/evaluation environment</td>
<td nowrap>realistic manipulation</td>
<td nowrap>-</td>
<td nowrap>Addresses generalization from synthetic skills to real robot manipulation.</td>
<td nowrap><a href="https://openreview.net/forum?id=H4SyKHjd4c">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-Guide, Octoday, HCP-Survey, EAI-VLA-VLN, Humanoid-RL</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=TmYcqOnxhN">Exo-Plore: Exploring Exoskeleton Control Space through Human-aligned Simulation</a></td>
<td nowrap>Uses human-aligned simulation to explore exoskeleton control spaces.</td>
<td nowrap>exoskeleton control</td>
<td nowrap>sim2real</td>
<td nowrap>human-aligned simulation/exoskeleton</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Addresses the difficulty of safely and efficiently exploring exoskeleton control policies.</td>
<td nowrap><a href="https://openreview.net/forum?id=TmYcqOnxhN">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=yn9dzttHvT">Latent Adaptation of Foundation Policies for Sim-to-Real Transfer</a></td>
<td nowrap>Adapts foundation policy in latent space to perform sim-to-real transfer.</td>
<td nowrap>latent policy adaptation</td>
<td nowrap>sim2real</td>
<td nowrap>simulation/evaluation environment</td>
<td nowrap>sim-to-real policy transfer</td>
<td nowrap>-</td>
<td nowrap>Addresses performance degradation of foundation robot policies under real-domain distribution shifts.</td>
<td nowrap><a href="https://openreview.net/forum?id=yn9dzttHvT">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=OutljIofvS">RobotArena ∞: Scalable Robot Benchmarking via Real-to-Sim Translation</a></td>
<td nowrap>Expands evaluable benchmarks for real robot scenes through real-to-sim translation.</td>
<td nowrap>real-to-sim benchmark</td>
<td nowrap>sim2real</td>
<td nowrap>simulation/evaluation environment</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Addresses the high cost of scaling real robot benchmarks.</td>
<td nowrap><a href="https://openreview.net/forum?id=OutljIofvS">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=xlr3NqxUqY">Contact-guided Real2Sim from Monocular Video with Planar Scene Primitives</a></td>
<td nowrap>Reconstructs real2sim scenes from monocular video using contact cues and planar scene primitives.</td>
<td nowrap>contact-guided Real2Sim</td>
<td nowrap>sim2real</td>
<td nowrap>monocular video</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Addresses the lack of physical contact constraints when converting monocular video to simulation.</td>
<td nowrap><a href="https://openreview.net/forum?id=xlr3NqxUqY">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Humanoid-RL</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66662">FlatLab: A Unified Methodology Framework and Simulation-Based Benchmark for Robotic Manipulation of Flat Objects</a></td>
<td nowrap>-</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>sim2real</td>
<td nowrap>simulation/evaluation environment</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66662">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2602.20871">GeCo-SRT: Geometry-aware Continual Adaptation for Robotic Cross-Task Sim-to-Real Transfer</a></td>
<td nowrap>Uses geometry-aware continual adaptation to support cross-task sim-to-real transfer.</td>
<td nowrap>continual sim-to-real adaptation</td>
<td nowrap>sim2real</td>
<td nowrap>simulation/evaluation environment</td>
<td nowrap>-</td>
<td nowrap>Project</td>
<td nowrap>Addresses geometric differences and continual adaptation in cross-task real-world transfer of robot policies.</td>
<td nowrap><a href="https://arxiv.org/abs/2602.20871">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2509.19626">EgoBridge: Domain Adaptation for Generalizable Imitation from Egocentric Human Data</a></td>
<td nowrap>Applies domain adaptation to egocentric human data for generalizable robot imitation learning.</td>
<td nowrap>human-to-robot domain adaptation</td>
<td nowrap>sim2real</td>
<td nowrap>robot deployment/evaluation environment</td>
<td nowrap>-</td>
<td nowrap>Project</td>
<td nowrap>Addresses the domain gap from egocentric human data to robot policies.</td>
<td nowrap><a href="https://arxiv.org/abs/2509.19626">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://openreview.net/forum?id=284GWLFtjU">DEAL: Diffusion Evolution Adversarial Learning for Sim-to-Real Transfer</a></td>
<td nowrap>-</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>simulation/evaluation environment</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>reduce sim-to-real gap</td>
<td nowrap><a href="https://openreview.net/forum?id=284GWLFtjU">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2509.18631">Generalizable Domain Adaptation for Sim-and-Real Policy Co-Training</a></td>
<td nowrap>Uses sim-and-real policy co-training to improve cross-domain generalization.</td>
<td nowrap>domain adaptation / co-training</td>
<td nowrap>sim2real</td>
<td nowrap>robot deployment/evaluation environment</td>
<td nowrap>-</td>
<td nowrap>Project</td>
<td nowrap>Addresses how domain shift affects policy generalization when jointly training on simulated and real data.</td>
<td nowrap><a href="https://arxiv.org/abs/2509.18631">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2505.22634">LabUtopia: High-Fidelity Simulation and Hierarchical Benchmark for Scientific Embodied Agents</a></td>
<td nowrap>Provides high-fidelity simulation, scene generation, and hierarchical benchmarks for scientific labs.</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>sim2real</td>
<td nowrap>LabSim</td>
<td nowrap>30 lab tasks / 200+ assets</td>
<td nowrap>Project</td>
<td nowrap>Addresses the lack of simulation and evaluation for complex experimental workflows in scientific embodied agents.</td>
<td nowrap><a href="https://arxiv.org/abs/2505.22634">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2507.01152">SonoGym: High Performance Simulation for Challenging Surgical Tasks with Robotic Ultrasound</a></td>
<td nowrap>Provides parallelizable simulation environments and tasks for robotic ultrasound surgery.</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>sim2real</td>
<td nowrap>robotic ultrasound</td>
<td nowrap>-</td>
<td nowrap>Code</td>
<td nowrap>Addresses the lack of realistic and efficient simulation training environments for robotic ultrasound navigation/reconstruction.</td>
<td nowrap><a href="https://arxiv.org/abs/2507.01152">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/SonoGym/SonoGym">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.22756">RoboPearls: Editable Video Simulation for Robot Manipulation</a></td>
<td nowrap>Uses 3DGS to build editable, photorealistic robot manipulation simulations from demonstration videos.</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>editable video simulation</td>
<td nowrap>simulation/evaluation environment</td>
<td nowrap>-</td>
<td nowrap>Project</td>
<td nowrap>Addresses expensive real demonstration collection and the large sim2real gap in traditional simulation.</td>
<td nowrap><a href="https://arxiv.org/abs/2506.22756">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2409.02920">RoboTwin: Dual-Arm Robot Benchmark with Generative Digital Twins (early version)</a></td>
<td nowrap>Uses generative digital twins to create dual-arm manipulation data and a real-aligned evaluation platform.</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>dual-arm robot / COBOT Magic</td>
<td nowrap>-</td>
<td nowrap>Project+Code+Data/Bench</td>
<td nowrap>Addresses the scarcity of dual-arm manipulation data and the mismatch between simulation evaluation and reality.</td>
<td nowrap><a href="https://arxiv.org/abs/2409.02920">paper</a></td>
<td nowrap><a href="https://robotwin-benchmark.github.io/early-version/">project</a></td>
<td nowrap><a href="https://github.com/RoboTwin-Platform/RoboTwin">code</a></td>
<td nowrap><a href="https://huggingface.co/datasets/TianxingChen/RoboTwin">hf</a></td>
<td nowrap>EAI-Guide, EAI-VLA-VLN, Efficient-VLA, WAM, RL-VLA</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
</tbody>
</table>

#### safety evaluation

Total: 10 papers.

<table>
<thead>
<tr>
<th nowrap>Venue/Year</th>
<th nowrap>Paper/Method</th>
<th nowrap>Abstract</th>
<th nowrap>Object Type</th>
<th nowrap>Efficiency Metric</th>
<th nowrap>Platform/Hardware</th>
<th nowrap>Covered Tasks</th>
<th nowrap>Open Resource Status</th>
<th nowrap>Paper Task/Goal</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
<th nowrap>Source</th>
<th nowrap>Survey Note</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>IROS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2410.15185">Semantically Safe Robot Manipulation: From Semantic Scene Understanding to Motion Safeguards</a></td>
<td nowrap>该文用 LLM 推理 commonsense 语义风险，并把语义风险映射为机器人操作安全过滤。</td>
<td nowrap>semantic safety layer</td>
<td nowrap>safety evaluation</td>
<td nowrap>robot manipulation safety</td>
<td nowrap>semantic scene understanding + safeguards</td>
<td nowrap>project available</td>
<td nowrap>将语义风险纳入机器人操作安全闭环。</td>
<td nowrap><a href="https://arxiv.org/abs/2410.15185">paper</a></td>
<td nowrap><a href="https://utiasdsl.github.io/semantic-manipulation/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>ICRA/IROS</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=8s5jBVybhQ">Remotely Detectable Robot Policy Watermarking</a></td>
<td nowrap>Proposes CoNoCo to detect robot policy watermarks from remote video/mocap observations without affecting the action distribution.</td>
<td nowrap>policy watermarking</td>
<td nowrap>safety</td>
<td nowrap>robot deployment/evaluation environment</td>
<td nowrap>remote safety/provenance detection</td>
<td nowrap>-</td>
<td nowrap>Addresses remote verification of robot policy intellectual property and unauthorized use.</td>
<td nowrap><a href="https://openreview.net/forum?id=8s5jBVybhQ">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=Gsrw1vxq1G">RoboMD: Uncovering Robot Vulnerabilities through Semantic Potential Fields</a></td>
<td nowrap>RoboMD actively searches for vulnerable regions in semantic visual embedding potential fields for safety discovery and retraining.</td>
<td nowrap>vulnerability discovery</td>
<td nowrap>safety</td>
<td nowrap>robot deployment/evaluation environment</td>
<td nowrap>manipulation robustness</td>
<td nowrap>-</td>
<td nowrap>Addresses expensive vulnerability testing on real robots and the difficulty of enumerating unknown perturbations.</td>
<td nowrap><a href="https://openreview.net/forum?id=Gsrw1vxq1G">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/60472">Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds</a></td>
<td nowrap>-</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>robot deployment/evaluation environment</td>
<td nowrap>Evaluate robustness and safety.</td>
<td nowrap>-</td>
<td nowrap>Evaluate robustness and safety.</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/60472">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62679">PACT: Self-Evolving Physical Safety Alignment for Diffusion Policies in Embodied Manipulation</a></td>
<td nowrap>-</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>safety</td>
<td nowrap>robot deployment/evaluation environment</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62679">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Awesome-VLA</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61584">SafeLab: An Interactive High-Fidelity Benchmark for Embodied Safety in Scientific Robotics</a></td>
<td nowrap>-</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>safety</td>
<td nowrap>simulation/evaluation environment</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61584">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64080">Dismantling the Illusion of Vision-Language-Action Models Competence via Explicit Distributional Shifts</a></td>
<td nowrap>-</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>robot deployment/evaluation environment</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64080">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2510.13626">LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models</a></td>
<td nowrap>Systematically reveals VLA robustness failures through seven perturbation types and 10,030 tasks.</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>robot deployment/evaluation environment</td>
<td nowrap>7 perturbation dimensions / 10,030 tasks</td>
<td nowrap>Project+Code+Data/Bench</td>
<td nowrap>Addresses VLA scoring high on standard benchmarks while remaining vulnerable to real-world perturbations.</td>
<td nowrap><a href="https://arxiv.org/abs/2510.13626">paper</a> / <a href="https://arxiv.org/pdf/2510.13626">paper</a></td>
<td nowrap><a href="https://sylvestf.github.io/LIBERO-plus/">project</a></td>
<td nowrap><a href="https://github.com/sylvestf/LIBERO-plus">code</a></td>
<td nowrap><a href="https://huggingface.co/datasets/Sylvest/LIBERO-plus">hf</a></td>
<td nowrap>EAI-Safety, WAM</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.05294">A Smooth Sea Never Made a Skilled SAILOR: Robust Imitation via Learning to Search</a></td>
<td nowrap>SAILOR learns search, world models, and reward models from demonstrations so imitation policies can recover from erroneous states.</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>safety</td>
<td nowrap>robot deployment/evaluation environment</td>
<td nowrap>12 visual manipulation tasks</td>
<td nowrap>Project</td>
<td nowrap>Addresses behavior cloning's inability to recover after leaving the demonstration distribution.</td>
<td nowrap><a href="https://arxiv.org/abs/2506.05294">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/arnavkj1995/SAILOR">code</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.23725">PAC Bench: Do Foundation Models Understand Prerequisites for Executing Manipulation Policies?</a></td>
<td nowrap>PAC Bench evaluates whether VLMs understand manipulation prerequisites such as object properties, affordances, and constraints.</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>safety</td>
<td nowrap>robot deployment/evaluation environment</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Addresses the unverified low-level physical prerequisites behind high-level robot abilities of foundation models.</td>
<td nowrap><a href="https://arxiv.org/abs/2506.23725">paper</a></td>
<td nowrap><a href="https://pacbench.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>30k annotations / 673 images / 100 scenarios / 120 sim constraints</td>
<td nowrap>RL-VLA</td>
<td nowrap>Used to evaluate deployment efficiency, data coverage, and benchmark credibility.</td>
</tr>
</tbody>
</table>


## Reading Order

1. Start with VLN and Agentic Planning to separate large-scale planning from fine-grained task planning.
2. Then read VLA and WAM to distinguish direct action generation from imagination/prediction before execution.
3. Finish with embodiment expansion, efficiency, and evaluation because they determine whether a route can be deployed on real robots.

## Additional Source Entries

The following entries come from archived README snapshots and are not merged into the direction main tables; they are kept for tracking WAM data sources and RL-VLA method leads.

<table>
<thead>
<tr>
<th nowrap>Entry</th>
<th nowrap>Source</th>
<th nowrap>Direction</th>
<th nowrap>Date</th>
<th nowrap>Resource</th>
<th nowrap>Why Track</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>UnifoLM-WBT Dataset</td>
<td nowrap>WAM</td>
<td nowrap>WAM training data / robot-centric</td>
<td nowrap>2026-03</td>
<td nowrap><a href="https://huggingface.co/collections/unitreerobotics/unifolm-wbt-dataset">dataset</a></td>
<td nowrap>Robot-centric data source, suitable for later tracking WAM training data coverage.</td>
</tr>
<tr>
<td nowrap>DexUMI</td>
<td nowrap>WAM</td>
<td nowrap>UMI / dexterous manipulation data</td>
<td nowrap>2025-05</td>
<td nowrap><a href="https://arxiv.org/pdf/2505.21864">paper</a> / <a href="https://dex-umi.github.io/">web</a> / <a href="https://umi-data.github.io/">dataset</a> / <a href="https://github.com/real-stanford/DexUMI">code</a></td>
<td nowrap>Hand-interaction data source connecting WAM and dexterous manipulation.</td>
</tr>
<tr>
<td nowrap>InternData-A1 / InternVLA-A1</td>
<td nowrap>WAM</td>
<td nowrap>simulation + VLA data</td>
<td nowrap>2026-01</td>
<td nowrap><a href="https://arxiv.org/pdf/2601.02456">paper</a> / <a href="https://internrobotics.github.io/interndata-a1.github.io/">web</a> / <a href="https://huggingface.co/datasets/InternRobotics/InternData-A1">dataset</a> / <a href="https://github.com/InternRobotics/InternVLA-A1">code</a></td>
<td nowrap>Includes data, models, and code, making it suitable as a joint VLA/WAM entry point.</td>
</tr>
<tr>
<td nowrap>EgoDex</td>
<td nowrap>WAM</td>
<td nowrap>egocentric dexterous data</td>
<td nowrap>2025-05</td>
<td nowrap><a href="https://arxiv.org/pdf/2505.11709">paper</a> / <a href="https://github.com/apple/ml-egodex">dataset+code</a></td>
<td nowrap>Egocentric dexterous manipulation data, useful for filling the path from human video to robot policy.</td>
</tr>
<tr>
<td nowrap>ARM</td>
<td nowrap>RL-VLA</td>
<td nowrap>Offline RL-VLA / real robot</td>
<td nowrap>2026.4</td>
<td nowrap><a href="https://arxiv.org/pdf/2604.03037">paper</a> / <a href="https://aiming1998.github.io/ARM/">project</a></td>
<td nowrap>Real-robot RL-VLA method based on GR00T N1.5.</td>
</tr>
<tr>
<td nowrap>LaST-R1</td>
<td nowrap>RL-VLA</td>
<td nowrap>Online RL-VLA / simulation</td>
<td nowrap>2026.04</td>
<td nowrap><a href="https://arxiv.org/abs/2604.28192">paper</a></td>
<td nowrap>Online RL-VLA training signal, suitable for later adding to the VLA fine-tuning direction.</td>
</tr>
<tr>
<td nowrap>POCO</td>
<td nowrap>RL-VLA</td>
<td nowrap>Offline + Online RL-VLA</td>
<td nowrap>2026.04</td>
<td nowrap><a href="https://arxiv.org/abs/2604.01860">paper</a> / <a href="https://cccedric.github.io/poco/">project</a></td>
<td nowrap>Covers sim and real, and connects π0/Octo with RL optimization.</td>
</tr>
<tr>
<td nowrap>FASTER</td>
<td nowrap>RL-VLA</td>
<td nowrap>Test-time RL-VLA</td>
<td nowrap>2026.04</td>
<td nowrap><a href="https://arxiv.org/abs/2604.19730">paper</a></td>
<td nowrap>Test-time action optimization signal, suitable for tracking execution-time VLA optimization.</td>
</tr>
</tbody>
</table>

## Data Sources

GitHub source repository metadata and README snapshots are recorded in [`sources/github/repos.json`](sources/github/repos.json); the `Source` column in the tables uses the `id` values from that file.

<table>
<thead>
<tr>
<th nowrap>Source</th>
<th nowrap>Use</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap><a href="https://ccf.atom.im/">CCF 2026 Recommended List</a></td>
<td nowrap>Verify the 2026 CCF-A artificial intelligence conference classification.</td>
</tr>
<tr>
<td nowrap><a href="https://github.com/Songwxuan/Embodied-AI-Paper-TopConf">Songwxuan/Embodied-AI-Paper-TopConf</a></td>
<td nowrap>Main source for CCF-A papers, classified by conference and direction; paper, code, and project-page links preferentially use resources already provided in that repository.</td>
</tr>
<tr>
<td nowrap><a href="https://openreview.net/group?id=ICLR.cc/2026/Conference">ICLR 2026 OpenReview</a></td>
<td nowrap>Verify ICLR 2026 public paper pages and PDF resources.</td>
</tr>
<tr>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/issue/view/703">AAAI-26 Intelligent Robotics proceedings</a></td>
<td nowrap>Verify and add AAAI 2026 robotics-track papers.</td>
</tr>
<tr>
<td nowrap><a href="https://ras.papercept.net/conferences/scripts/start.pl">IEEE RAS PaperCept programs</a></td>
<td nowrap>Verify ICRA 2026 and IROS 2025 official program entries; ICRA 2025 PaperCept returned access denied in this environment.</td>
</tr>
<tr>
<td nowrap><a href="https://arxiv.org/">arXiv and author project pages for ICRA/IROS papers</a></td>
<td nowrap>Cross-check ICRA 2025 and IROS 2026 papers when official proceedings or full paper lists are not yet publicly stable.</td>
</tr>
<tr>
<td nowrap><a href="https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln">jonyzhang2023/awesome-embodied-vla-va-vln</a></td>
<td nowrap>Reference the organization of VLA, WAM, VLN, VA, and surveys.</td>
</tr>
<tr>
<td nowrap><a href="https://github.com/OpenMOSS/Awesome-WAM">OpenMOSS/Awesome-WAM</a></td>
<td nowrap>Reference WAM categories such as cascaded/joint, autoregressive/diffusion, and evaluation/training data.</td>
</tr>
<tr>
<td nowrap><a href="https://github.com/UCSB-AI/awesome-vision-language-navigation">UCSB-AI/awesome-vision-language-navigation</a></td>
<td nowrap>Reference VLN categories such as dataset, evaluation, representation, action strategy, planning, and asking for help.</td>
</tr>
<tr>
<td nowrap><a href="https://github.com/DelinQu/awesome-vision-language-action-model">DelinQu/awesome-vision-language-action-model</a></td>
<td nowrap>Reference the VLA milestone timeline.</td>
</tr>
<tr>
<td nowrap><a href="https://github.com/yueen-ma/Awesome-VLA">yueen-ma/Awesome-VLA</a></td>
<td nowrap>Reference VLA categories such as components, world models, reasoning, policy steering, and low-level/high-level planners.</td>
</tr>
</tbody>
</table>
