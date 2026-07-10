<div align="center">

# 🤖 Awesome Embodied AI Papers

**A curated top-conference-oriented map of embodied AI research across VLN, VLA, WAM, planning, embodiment, and deployment.**

English | [Chinese](README.zh-CN.md)

[![Awesome](https://img.shields.io/badge/Awesome-Embodied%20AI-fc60a8?style=for-the-badge)](https://awesome.re)
[![Survey Entries](https://img.shields.io/badge/Survey%20Entries-707-0984e3?style=for-the-badge)](README.md)
[![Last Commit](https://img.shields.io/github/last-commit/neardws/awesome-embodied-ai-papers?style=for-the-badge&color=00b894)](https://github.com/neardws/awesome-embodied-ai-papers/commits)
[![Stars](https://img.shields.io/github/stars/neardws/awesome-embodied-ai-papers?style=for-the-badge&color=fdcb6e&logo=github)](https://github.com/neardws/awesome-embodied-ai-papers/stargazers)
[![Forks](https://img.shields.io/github/forks/neardws/awesome-embodied-ai-papers?style=for-the-badge&color=e17055&logo=github)](https://github.com/neardws/awesome-embodied-ai-papers/network/members)

Updated: 2026-07-10

</div>

## 📋 Table of Contents

| | Section | Description |
|:---:|:---|:---|
| 🏷️ | [Tag Legend](#tag-legend) | Tags used to group embodied AI directions |
| 🧭 | [Overall View](#overall-view) | High-level system route and field framing |
| 🗺️ | [Direction Overview](#direction-overview) | Six-track overview with paper counts |
| 🔎 | [Reading Order](#reading-order) | Suggested priority list for deeper reading |
| 🧾 | [Data Sources](#data-sources) | Source traceability and reference metadata |
| 🦿 | [Humanoid & Biped Hardware Reference](#humanoid--biped-hardware-reference) | Biped platforms and dexterous-hand configurations; papers are consolidated into the humanoid master table |
| 📚 | [Detailed Tables](#detailed-tables) | Paper-level tables by direction and subdirection |

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

### Taxonomy & Evidence Map

<p align="center">
  <img src="figs/embodied-ai-taxonomy-v3.svg" alt="Taxonomy and evidence map for 707 embodied AI papers across six directions and 29 subdirections." width="100%">
</p>

### Evolution & Method Lineage

<p align="center">
  <img src="figs/embodied-ai-lineage-v3.svg" alt="Evolution and method lineage for embodied AI methods from 2022 to 2026." width="100%">
</p>

### System Roadmap & Trend Matrix

<p align="center">
  <img src="figs/embodied-ai-system-roadmap-v3.svg" alt="System roadmap and trend matrix for embodied AI capability layers, method anchors, interface signals, and trend pressure." width="100%">
</p>

### Research Direction: Verifiable Closed-Loop Action

The next research thread worth highlighting is not a single module, but a closed loop: spatial memory supports planning, planning grounds executable action, world models verify consequences, and failure feedback updates the next plan.

<p align="center">
  <img src="figs/embodied-ai-closed-loop-action-v3.svg" alt="Research direction figure for embodied AI as verifiable closed-loop action across spatial memory, planning, action, world prediction, and failure feedback." width="100%">
</p>

| Direction | Trend |
| --- | --- |
| VLN | VLN is moving from discrete graph navigation toward continuous, memory-backed, physically executable, open-world navigation, while on-device variants are still early. |
| VLA | VLA growth is led by generalist policies and diffusion/flow action generation, with action representation, 3D grounding, online tuning, and safety becoming the practical bottlenecks. |
| WAM | WAM is emerging as an imagination and verification layer between planning and controllers, with cascaded and video/latent models ahead of fully joint world-action modeling. |
| Planning | Agentic planning is moving from instruction decomposition toward memory, failure monitoring, executable constraints, and self-improving loops. |
| Embodiment | Embodiment expansion tests whether policies survive new bodies, contacts, and coordination demands, with humanoid and dexterous-hand work leading the volume. |
| Deployment | Deployment work is led by benchmark/data credibility, efficiency, and sim2real transfer, with real-time execution and safety evaluation as smaller but necessary readiness checks. |

| Direction | Subdirection | Trend |
| --- | --- | --- |
| VLN | Continuous VLN | Continuous observations, multimodal goals, and online adaptation are replacing the clean discrete-graph assumption. |
| VLN | Map Memory | Semantic maps, topological memory, 3D memory, retrieval, and caching are becoming the navigation substrate. |
| VLN | Physically Executable Navigation | Navigation research is adding body constraints, dynamic scenes, and safety decoding so plans can be executed. |
| VLN | Urban / Open-world Navigation | The setting is expanding toward streets, crowds, implicit human needs, lifelong navigation, and open-world exploration. |
| VLN | Low-cost / On-device Navigation | The deployment track compresses navigation into smaller memories, cheaper data, and on-device inference. |
| VLA | generalist VLA | Generalist policies consolidate many tasks and datasets into reusable robot foundation policies. |
| VLA | action representation | Action tokens, waypoints, constraints, and motion primitives bridge language/image understanding with executable control. |
| VLA | diffusion/flow policy | Diffusion and flow models are becoming a major action-generation route for robust manipulation. |
| VLA | 3D grounding | Object-centric geometry, spatial localization, and affordance priors are moving VLA from pixels toward physical scenes. |
| VLA | online/RL fine-tuning | Post-pretraining adaptation uses RL, online feedback, and test-time optimization to close execution gaps. |
| VLA | Safety and Robustness | Robustness work is shifting from benchmark accuracy to attacks, uncertainty, unsafe actions, and physical failure modes. |
| WAM | cascaded WAM | Cascaded systems imagine or predict first, then act, making WAM easier to attach to existing planners and controllers. |
| WAM | joint WAM | Joint WAM is small but important because it tries to model vision, state, and action in one coupled system. |
| WAM | video/latent world model | Video and latent prediction are the main path for future-state imagination, reward shaping, and interactive simulation. |
| WAM | world model for VLA | World models are being used to improve VLA generalization, action selection, and failure recovery. |
| Planning | Task Decomposition | Planners translate high-level language into subgoals, programs, skills, or executable task graphs. |
| Planning | memory | Persistent scene, task, and personalization memory supports long-horizon interaction beyond a single episode. |
| Planning | failure monitor | Failure monitors make embodied agents detect, explain, and recover from execution errors instead of assuming success. |
| Planning | constraint / affordance planning | Constraints, affordances, PDDL-like structure, and code policies make high-level plans physically executable. |
| Planning | self-improving planning | Feedback, RL, reflection, and experience revision are turning planning into an iterative improvement loop. |
| Embodiment | humanoid | Humanoid work stresses whole-body control, mobile manipulation, sim2real transfer, and generalization across full-body skills. |
| Embodiment | bimanual | Bimanual research focuses on coordinated dual-arm manipulation and longer-horizon interaction. |
| Embodiment | dexterous hand | Dexterous-hand work expands grasping and manipulation into high-DOF action spaces and transfer-heavy settings. |
| Embodiment | tactile/contact-rich | Tactile and contact-rich research brings force, touch, and fine-grained feedback into manipulation policies. |
| Deployment | quantization/cache/tokenization | Efficiency work compresses models and action representations through quantization, caching, and tokenization. |
| Deployment | real-time execution | Real-time execution focuses on latency-aware control and edge deployment constraints. |
| Deployment | benchmark/dataset | Benchmarks and datasets define coverage, credibility, and whether progress is measurable across robots and tasks. |
| Deployment | sim2real | Sim2real work bridges generated/simulated assets, dynamics, and policies into physical robot execution. |
| Deployment | safety evaluation | Safety evaluation builds tests for physical risk, robustness, and alignment under embodied interaction. |

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
<td nowrap>92</td>
<td nowrap>VLN focuses on language goals, spatial maps, memory, exploration, and navigation decisions. The core problem is turning natural-language tasks into executable large-scale movement plans. Current survey entries show a shift from discrete navigation graphs toward continuous environments, physically executable navigation, open urban settings, and lower-cost on-device navigation.</td>
</tr>
<tr>
<td nowrap><code>VLA</code></td>
<td nowrap>VLA / Manipulation Policies</td>
<td nowrap>generalist VLA, action representation, diffusion/flow policy, 3D grounding, online/RL fine-tuning, safety/robustness</td>
<td nowrap>242</td>
<td nowrap>VLA is the main track for robotic arms and mobile manipulation, but it is not just an action head attached to a large model. Survey papers concentrate on action representation, diffusion/flow policies, 3D grounding, online/RL fine-tuning, and robustness.</td>
</tr>
<tr>
<td nowrap><code>WAM</code></td>
<td nowrap>WAM / World Models</td>
<td nowrap>cascaded WAM, joint WAM, video/latent world model, world model for VLA</td>
<td nowrap>70</td>
<td nowrap>WAM combines future world-state prediction with action generation and fits naturally between agent planning and low-level control. Its value is not replacing every controller, but providing an intermediate layer for imagination, verification, and recovery.</td>
</tr>
<tr>
<td nowrap><code>Planning</code></td>
<td nowrap>Agentic Planning / Reasoning and Planning</td>
<td nowrap>task decomposition, memory, failure monitor, constraint / affordance planning, self-improving planning</td>
<td nowrap>103</td>
<td nowrap>This direction emphasizes task decomposition, memory, failure monitoring, constraint/affordance planning, and self-improving planning. It is closest to the practical system route of agent planning plus smaller execution modules.</td>
</tr>
<tr>
<td nowrap><code>Embodiment</code></td>
<td nowrap>Embodiment Expansion / Dexterous Manipulation</td>
<td nowrap>humanoid, bimanual, dexterous hand, tactile/contact-rich</td>
<td nowrap>159</td>
<td nowrap>Embodiment expansion determines whether embodied AI can move beyond single-arm systems toward humanoids, bimanual robots, dexterous hands, and tactile/contact-rich tasks. These papers show how action spaces, sensing, and control objectives become more complex as the body changes.</td>
</tr>
<tr>
<td nowrap><code>Deployment</code></td>
<td nowrap>Efficiency / Evaluation / Data</td>
<td nowrap>quantization/cache/tokenization, real-time execution, benchmark/dataset, sim2real, safety evaluation</td>
<td nowrap>101</td>
<td nowrap>This direction determines whether systems can actually be deployed: on-device inference, caching/quantization/action tokenization, real-time execution, sim2real, benchmarks, and safety evaluation are all necessary conditions.</td>
</tr>
</tbody>
</table>

## Reading Order

1. Start with VLN and Agentic Planning to separate large-scale planning from fine-grained task planning.
2. Then read VLA and WAM to distinguish direct action generation from imagination/prediction before execution.
3. Finish with embodiment expansion, efficiency, and evaluation because they determine whether a route can be deployed on real robots.

## Data Sources

GitHub source repository metadata and README snapshots are recorded in [`sources/github/repos.json`](sources/github/repos.json); historical source IDs are kept there for traceability.

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
<tr>
<td nowrap><a href="https://www.unitree.com/H2plus/">Unitree official humanoid and dexterous-hand pages</a></td>
<td nowrap>Verify current H1/H1-2, G1, R1, H2/H2 Plus and modular hand specifications; living product figures were checked on 2026-07-10.</td>
</tr>
<tr>
<td nowrap><a href="https://open.agibot.com/docs/en/aimdk/a3/v3_1/dev_guide/01-a3_overview">AgiBot official product and AimDK documentation</a></td>
<td nowrap>Verify the bipedal A2, A3, X1 and X2 families, distinguish wheeled variants, and trace OmniHand/end-effector configurations.</td>
</tr>
</tbody>
</table>

## Detailed Tables

### VLN / Large-scale Navigation

VLN focuses on language goals, spatial maps, memory, exploration, and navigation decisions. The core problem is turning natural-language tasks into executable large-scale movement plans. Current survey entries show a shift from discrete navigation graphs toward continuous environments, physically executable navigation, open urban settings, and lower-cost on-device navigation.

Subdirections: continuous VLN, map memory, physically executable navigation, urban/open-world navigation, and low-cost/on-device navigation.

Total: 92 papers.

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
<td nowrap>39</td>
<td nowrap>Focus: whether navigation moves from discrete graphs toward continuous observations and real-time decisions.</td>
</tr>
<tr>
<td nowrap>Map Memory</td>
<td nowrap>23</td>
<td nowrap>Focus: map representation, semantic memory, caching, and retrieval.</td>
</tr>
<tr>
<td nowrap>Physically Executable Navigation</td>
<td nowrap>7</td>
<td nowrap>Focus: real embodiment constraints, dynamic environments, and safety decoding.</td>
</tr>
<tr>
<td nowrap>Urban / Open-world Navigation</td>
<td nowrap>20</td>
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

Total: 39 papers.

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
</tr>
</thead>
<tbody>
<tr>
<td nowrap>CoRL 2022</td>
<td nowrap><a href="https://scholar.google.com/scholar?q=LM-Nav%3A+Robotic+Navigation+with+Large+Pre-Trained+Models+of+Language%2C+Vision%2C+and+Action">LM-Nav: Robotic Navigation with Large Pre-Trained Models of Language, Vision, and Action</a></td>
<td nowrap>LM-Nav composes pretrained language, vision, and action models for robotic navigation.</td>
<td nowrap>Vision-language navigation</td>
<td nowrap>embodied navigation</td>
<td nowrap>language/spatial context</td>
<td nowrap>CoRL navigation method</td>
<td nowrap>VLN / embodied navigation benchmarks</td>
<td nowrap>Add CoRL navigation coverage.</td>
<td nowrap><a href="https://scholar.google.com/scholar?q=LM-Nav%3A+Robotic+Navigation+with+Large+Pre-Trained+Models+of+Language%2C+Vision%2C+and+Action">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CoRL 2020</td>
<td nowrap><a href="https://scholar.google.com/scholar?q=Vision-and-Dialog+Navigation">Vision-and-Dialog Navigation</a></td>
<td nowrap>Vision-and-Dialog Navigation extends VLN with dialog interaction during navigation.</td>
<td nowrap>Vision-language navigation</td>
<td nowrap>embodied navigation</td>
<td nowrap>language/spatial context</td>
<td nowrap>CoRL navigation method</td>
<td nowrap>VLN / embodied navigation benchmarks</td>
<td nowrap>Add CoRL navigation coverage.</td>
<td nowrap><a href="https://scholar.google.com/scholar?q=Vision-and-Dialog+Navigation">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CoRL 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2509.10454">GC-VLN: Instruction as Graph Constraints for Training-free Vision-and-Language Navigation</a></td>
<td nowrap>GC-VLN treats instructions as graph constraints for training-free VLN.</td>
<td nowrap>Vision-language navigation</td>
<td nowrap>embodied navigation</td>
<td nowrap>language/spatial context</td>
<td nowrap>CoRL navigation method</td>
<td nowrap>VLN / embodied navigation benchmarks</td>
<td nowrap>Add CoRL navigation coverage.</td>
<td nowrap><a href="https://arxiv.org/abs/2509.10454">paper</a></td>
<td nowrap><a href="https://bagh2178.github.io/GC-VLN/">project</a></td>
<td nowrap><a href="https://github.com/bagh2178/GC-VLN">code</a></td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CoRL 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2505.11350">Search-TTA: A Multimodal Test-Time Adaptation Framework for Visual Search in the Wild</a></td>
<td nowrap>Search-TTA adapts multimodal visual-search agents at test time in open environments.</td>
<td nowrap>Vision-language navigation</td>
<td nowrap>embodied navigation</td>
<td nowrap>language/spatial context</td>
<td nowrap>CoRL navigation method</td>
<td nowrap>VLN / embodied navigation benchmarks</td>
<td nowrap>Add CoRL navigation coverage.</td>
<td nowrap><a href="https://arxiv.org/abs/2505.11350">paper</a></td>
<td nowrap><a href="https://search-tta.github.io/">project</a></td>
<td nowrap><a href="https://github.com/marmotlab/Search-TTA-VLN">code</a></td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CVPR 2023</td>
<td nowrap><a href="https://openaccess.thecvf.com/content/CVPR2023/html/Gao_Adaptive_Zone-Aware_Hierarchical_Planner_for_Vision-Language_Navigation_CVPR_2023_paper.html">Adaptive Zone-Aware Hierarchical Planner for Vision-Language Navigation</a></td>
<td nowrap>AZHP plans navigation by adapting hierarchy and local zones for language-conditioned visual navigation.</td>
<td nowrap>Vision-language navigation</td>
<td nowrap>continuous indoor navigation</td>
<td nowrap>zone-aware hierarchical memory</td>
<td nowrap>hierarchical planning</td>
<td nowrap>VLN benchmarks</td>
<td nowrap>Use zone-level structure to make long-horizon VLN decisions more reliable.</td>
<td nowrap><a href="https://openaccess.thecvf.com/content/CVPR2023/papers/Gao_Adaptive_Zone-Aware_Hierarchical_Planner_for_Vision-Language_Navigation_CVPR_2023_paper.pdf">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICML 2024</td>
<td nowrap><a href="https://proceedings.mlr.press/v235/gao24p.html">Fast-Slow Test-Time Adaptation for Online Vision-and-Language Navigation</a></td>
<td nowrap>Fast-Slow TTA adapts VLN agents online using complementary fast and slow adaptation signals.</td>
<td nowrap>Online VLN</td>
<td nowrap>continuous navigation</td>
<td nowrap>episodic adaptation memory</td>
<td nowrap>test-time adaptation</td>
<td nowrap>VLN benchmarks</td>
<td nowrap>Improve online VLN robustness under distribution shift.</td>
<td nowrap><a href="https://proceedings.mlr.press/v235/gao24p/gao24p.pdf">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICRA 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2509.19480">OmniVLA: An Omni-Modal Vision-Language-Action Model for Robot Navigation</a></td>
<td nowrap>OmniVLA unifies language, goal images, and 2D pose goals, learning robot navigation policies through a VLA formulation.</td>
<td nowrap>Vision-language-action navigation</td>
<td nowrap>continuous navigation</td>
<td nowrap>multimodal goal context</td>
<td nowrap>navigation VLA training</td>
<td nowrap>Sim + Real</td>
<td nowrap>Train a generalizable navigation VLA with multimodal goal specifications.</td>
<td nowrap><a href="https://arxiv.org/abs/2509.19480">paper</a></td>
<td nowrap><a href="https://omnivla-nav.github.io/">project</a></td>
<td nowrap><a href="https://github.com/NHirose/OmniVLA">code</a></td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICRA 2025</td>
<td nowrap><a href="https://sites.google.com/view/opennav/home">Open-Nav: Exploring Zero-Shot Vision-and-Language Navigation in Continuous Environment with Open-Source LLMs</a></td>
<td nowrap>Open-Nav uses open-source LLMs for spatio-temporal chain-of-thought reasoning, progress estimation, and action decisions for zero-shot VLN in continuous environments.</td>
<td nowrap>Continuous VLN</td>
<td nowrap>continuous indoor environment</td>
<td nowrap>spatio-temporal CoT</td>
<td nowrap>zero-shot LLM planning</td>
<td nowrap>VLN-CE benchmark</td>
<td nowrap>Enable open-source LLMs to navigate continuous environments from language instructions.</td>
<td nowrap><a href="https://sites.google.com/view/opennav/home">paper</a></td>
<td nowrap><a href="https://sites.google.com/view/opennav/home">project</a></td>
<td nowrap><a href="https://github.com/YanyuanQiao/Open-Nav">code</a></td>
<td nowrap>-</td>
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
</tr>
</tbody>
</table>

#### Map Memory

Total: 23 papers.

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
</tr>
</thead>
<tbody>
<tr>
<td nowrap>CoRL 2024</td>
<td nowrap><a href="https://arxiv.org/abs/2407.07775">Mobility VLA: Multimodal Instruction Navigation with Long-Context VLMs and Topological Graphs</a></td>
<td nowrap>Mobility VLA combines long-context VLMs with topological graphs for instruction navigation.</td>
<td nowrap>Vision-language navigation</td>
<td nowrap>embodied navigation</td>
<td nowrap>language/spatial context</td>
<td nowrap>CoRL navigation method</td>
<td nowrap>VLN / embodied navigation benchmarks</td>
<td nowrap>Add CoRL navigation coverage.</td>
<td nowrap><a href="https://arxiv.org/abs/2407.07775">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ACL 2024</td>
<td nowrap><a href="https://aclanthology.org/2024.acl-long.529/">MapGPT: Map-Guided Prompting for Unified Vision-and-Language Navigation</a></td>
<td nowrap>MapGPT uses map-guided prompting to connect language instructions with spatial navigation decisions.</td>
<td nowrap>Vision-language navigation</td>
<td nowrap>indoor VLN</td>
<td nowrap>map-guided prompt memory</td>
<td nowrap>LLM prompting + navigation</td>
<td nowrap>VLN benchmarks</td>
<td nowrap>Use explicit maps to ground LLM navigation decisions.</td>
<td nowrap><a href="https://aclanthology.org/2024.acl-long.529.pdf">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CVPR 2024</td>
<td nowrap><a href="https://openaccess.thecvf.com/content/CVPR2024/html/Zhao_OVER-NAV_Elevating_Iterative_Vision-and-Language_Navigation_with_Open-Vocabulary_Detection_and_StructurEd_CVPR_2024_paper.html">OVER-NAV: Elevating Iterative Vision-and-Language Navigation with Open-Vocabulary Detection and Structured Representation</a></td>
<td nowrap>OVER-NAV combines open-vocabulary detection with structured scene memory for iterative VLN.</td>
<td nowrap>Vision-language navigation</td>
<td nowrap>indoor VLN</td>
<td nowrap>open-vocabulary structured memory</td>
<td nowrap>iterative navigation planning</td>
<td nowrap>VLN benchmarks</td>
<td nowrap>Improve VLN grounding with open-vocabulary object and scene structure.</td>
<td nowrap><a href="https://openaccess.thecvf.com/content/CVPR2024/papers/Zhao_OVER-NAV_Elevating_Iterative_Vision-and-Language_Navigation_with_Open-Vocabulary_Detection_and_StructurEd_CVPR_2024_paper.pdf">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CVPR 2024</td>
<td nowrap><a href="https://arxiv.org/abs/2403.14158">Volumetric Environment Representation for Vision-Language Navigation</a></td>
<td nowrap>VER builds volumetric scene representations to improve spatial memory and grounding in VLN.</td>
<td nowrap>Vision-language navigation</td>
<td nowrap>3D indoor navigation</td>
<td nowrap>volumetric map memory</td>
<td nowrap>3D representation learning</td>
<td nowrap>VLN benchmarks</td>
<td nowrap>Represent navigable space volumetrically for language-guided navigation.</td>
<td nowrap><a href="https://arxiv.org/abs/2403.14158">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>IROS 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2606.25497">SAGE-Nav: Leveraging LLM Planning and Alignment Fusion for Hierarchical Scene Graph-Guided Navigation</a></td>
<td nowrap>SAGE-Nav combines LLM high-level planning with hierarchical scene graphs to guide object-goal navigation.</td>
<td nowrap>Object-goal navigation</td>
<td nowrap>indoor navigation</td>
<td nowrap>hierarchical scene graph</td>
<td nowrap>LLM planning + alignment fusion</td>
<td nowrap>Benchmark</td>
<td nowrap>Ground language planning in target navigation through scene-graph memory.</td>
<td nowrap><a href="https://arxiv.org/abs/2606.25497">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>IROS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.02247">WMNav: Integrating Vision-Language Models into World Models for Object Goal Navigation</a></td>
<td nowrap>WMNav integrates VLMs into a navigation world model to predict future states and maintain navigation memory for better target search.</td>
<td nowrap>Object-goal navigation</td>
<td nowrap>indoor navigation</td>
<td nowrap>world-model memory</td>
<td nowrap>VLM-guided world model</td>
<td nowrap>Benchmark</td>
<td nowrap>Use world-model imagination and feedback to support object-goal navigation.</td>
<td nowrap><a href="https://arxiv.org/abs/2503.02247">paper</a></td>
<td nowrap><a href="https://b0b8k1ng.github.io/WMNav/">project</a></td>
<td nowrap><a href="https://github.com/B0B8K1ng/WMNavigation">code</a></td>
<td nowrap>-</td>
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
</tr>
</tbody>
</table>

#### Physically Executable Navigation

Total: 7 papers.

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
</tr>
</thead>
<tbody>
<tr>
<td nowrap>CVPR 2024</td>
<td nowrap><a href="https://openaccess.thecvf.com/content/CVPR2024/html/Ehsani_SPOC_Imitating_Shortest_Paths_in_Simulation_Enables_Effective_Navigation_and_CVPR_2024_paper.html">SPOC: Imitating Shortest Paths in Simulation Enables Effective Navigation and Manipulation in the Real World</a></td>
<td nowrap>SPOC trains embodied agents from simulated shortest paths and transfers the behavior to navigation and manipulation.</td>
<td nowrap>Navigation + manipulation</td>
<td nowrap>physical embodied environments</td>
<td nowrap>implicit spatial policy memory</td>
<td nowrap>imitation from shortest paths</td>
<td nowrap>Sim + Real</td>
<td nowrap>Convert shortest-path supervision into physically executable embodied behavior.</td>
<td nowrap><a href="https://openaccess.thecvf.com/content/CVPR2024/papers/Ehsani_SPOC_Imitating_Shortest_Paths_in_Simulation_Enables_Effective_Navigation_and_CVPR_2024_paper.pdf">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
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
</tr>
</tbody>
</table>

#### Urban / Open-world Navigation

Total: 20 papers.

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
</tr>
</thead>
<tbody>
<tr>
<td nowrap>CVPR 2024</td>
<td nowrap><a href="https://openaccess.thecvf.com/content/CVPR2024/html/Khanna_GOAT-Bench_A_Benchmark_for_Multi-Modal_Lifelong_Navigation_CVPR_2024_paper.html">GOAT-Bench: A Benchmark for Multi-Modal Lifelong Navigation</a></td>
<td nowrap>GOAT-Bench evaluates lifelong navigation with multimodal goals and open-ended object/place targets.</td>
<td nowrap>Lifelong navigation benchmark</td>
<td nowrap>open-world indoor scenes</td>
<td nowrap>goal-conditioned memory</td>
<td nowrap>benchmark evaluation</td>
<td nowrap>GOAT-Bench</td>
<td nowrap>Measure multimodal lifelong navigation beyond single instruction episodes.</td>
<td nowrap><a href="https://openaccess.thecvf.com/content/CVPR2024/papers/Khanna_GOAT-Bench_A_Benchmark_for_Multi-Modal_Lifelong_Navigation_CVPR_2024_paper.pdf">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ECCV 2024</td>
<td nowrap><a href="https://arxiv.org/pdf/2407.14758">DISCO: Embodied Navigation and Interaction via Differentiable Scene-Conditioned Options</a></td>
<td nowrap>DISCO learns scene-conditioned options for embodied navigation and interaction in open environments.</td>
<td nowrap>Navigation + interaction</td>
<td nowrap>open embodied scenes</td>
<td nowrap>scene-conditioned options</td>
<td nowrap>option learning</td>
<td nowrap>Embodied interaction benchmarks</td>
<td nowrap>Tie navigation and interaction through reusable scene-conditioned options.</td>
<td nowrap><a href="https://arxiv.org/pdf/2407.14758">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
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
</tr>
</tbody>
</table>

### VLA / Manipulation Policies

VLA is the main track for robotic arms and mobile manipulation, but it is not just an action head attached to a large model. Survey papers concentrate on action representation, diffusion/flow policies, 3D grounding, online/RL fine-tuning, and robustness.

Subdirections: generalist VLA, action representation, diffusion/flow policy, 3D grounding, online/RL fine-tuning, and safety/robustness.

Total: 242 papers.

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
<td nowrap>79</td>
<td nowrap>Focus: cross-task generalization, real-robot validation, and general manipulation ability.</td>
</tr>
<tr>
<td nowrap>action representation</td>
<td nowrap>28</td>
<td nowrap>Focus: action tokens, latent actions, chunking, and action-space design.</td>
</tr>
<tr>
<td nowrap>diffusion/flow policy</td>
<td nowrap>72</td>
<td nowrap>Focus: continuous action generation, stable control, and smooth execution.</td>
</tr>
<tr>
<td nowrap>3D grounding</td>
<td nowrap>35</td>
<td nowrap>Focus: point clouds, geometry, affordance, and manipulation localization.</td>
</tr>
<tr>
<td nowrap>online/RL fine-tuning</td>
<td nowrap>21</td>
<td nowrap>Focus: online RL, human-in-the-loop learning, and test-time adaptation.</td>
</tr>
<tr>
<td nowrap>Safety and Robustness</td>
<td nowrap>7</td>
<td nowrap>Focus: attack robustness, safety alignment, and risk exposure.</td>
</tr>
</tbody>
</table>

#### generalist VLA

Total: 79 papers.

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
</tr>
</thead>
<tbody>
<tr>
<td nowrap>CoRL 2022</td>
<td nowrap><a href="https://arxiv.org/abs/2109.12098">CLIPort: What and Where Pathways for Robotic Manipulation</a></td>
<td nowrap>CLIPort combines CLIP semantics with transport-style spatial manipulation policies.</td>
<td nowrap>CLIPort</td>
<td nowrap>robot action</td>
<td nowrap>VLA / generalist VLA</td>
<td nowrap>CoRL robot-learning method</td>
<td nowrap>robot policy</td>
<td nowrap>robot benchmarks</td>
<td nowrap>Add CoRL VLA coverage.</td>
<td nowrap><a href="https://arxiv.org/abs/2109.12098">paper</a></td>
<td nowrap><a href="https://cliport.github.io">project</a></td>
<td nowrap><a href="https://github.com/cliport/cliport">code</a></td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CoRL 2024</td>
<td nowrap><a href="https://arxiv.org/abs/2406.09246">OpenVLA: An Open-Source Vision-Language-Action Model</a></td>
<td nowrap>OpenVLA is an open-source VLA model for general robot manipulation.</td>
<td nowrap>OpenVLA</td>
<td nowrap>robot action</td>
<td nowrap>VLA / generalist VLA</td>
<td nowrap>CoRL robot-learning method</td>
<td nowrap>robot policy</td>
<td nowrap>robot benchmarks</td>
<td nowrap>Add CoRL VLA coverage.</td>
<td nowrap><a href="https://arxiv.org/abs/2406.09246">paper</a></td>
<td nowrap><a href="https://openvla.github.io">project</a></td>
<td nowrap><a href="https://github.com/openvla/openvla">code</a></td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CoRL 2023</td>
<td nowrap><a href="https://arxiv.org/abs/2307.15818">RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control</a></td>
<td nowrap>RT-2 transfers web-scale vision-language knowledge into robotic control.</td>
<td nowrap>RT-2</td>
<td nowrap>robot action</td>
<td nowrap>VLA / generalist VLA</td>
<td nowrap>CoRL robot-learning method</td>
<td nowrap>robot policy</td>
<td nowrap>robot benchmarks</td>
<td nowrap>Add CoRL VLA coverage.</td>
<td nowrap><a href="https://arxiv.org/abs/2307.15818">paper</a></td>
<td nowrap><a href="https://robotics-transformer2.github.io">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CoRL 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2508.19958">Long-VLA: Unleashing Long-Horizon Capability of Vision Language Action Model for Robot Manipulation</a></td>
<td nowrap>Long-VLA targets long-horizon robot manipulation with VLA policies.</td>
<td nowrap>Long-VLA</td>
<td nowrap>robot action</td>
<td nowrap>VLA / generalist VLA</td>
<td nowrap>CoRL robot-learning method</td>
<td nowrap>robot policy</td>
<td nowrap>robot benchmarks</td>
<td nowrap>Add CoRL VLA coverage.</td>
<td nowrap><a href="https://arxiv.org/abs/2508.19958">paper</a></td>
<td nowrap><a href="https://long-vla.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CoRL 2021</td>
<td nowrap><a href="https://arxiv.org/abs/2202.02005">BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning</a></td>
<td nowrap>BC-Z studies zero-shot task generalization with robotic imitation learning.</td>
<td nowrap>BC-Z</td>
<td nowrap>robot action</td>
<td nowrap>VLA / generalist VLA</td>
<td nowrap>CoRL robot-learning method</td>
<td nowrap>robot policy</td>
<td nowrap>robot benchmarks</td>
<td nowrap>Add CoRL VLA coverage.</td>
<td nowrap><a href="https://arxiv.org/abs/2202.02005">paper</a></td>
<td nowrap><a href="https://sites.google.com/view/bc-z/home">project</a></td>
<td nowrap><a href="https://github.com/google-research/tensor2robot/tree/master/research/bcz">code</a></td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CoRL 2022</td>
<td nowrap><a href="https://arxiv.org/abs/2209.04899">Hiveformer: Instruction-driven history-aware policies for robotic manipulations</a></td>
<td nowrap>Hiveformer builds history-aware instruction-conditioned policies for robotic manipulation.</td>
<td nowrap>Hiveformer</td>
<td nowrap>robot action</td>
<td nowrap>VLA / generalist VLA</td>
<td nowrap>CoRL robot-learning method</td>
<td nowrap>robot policy</td>
<td nowrap>robot benchmarks</td>
<td nowrap>Add CoRL VLA coverage.</td>
<td nowrap><a href="https://arxiv.org/abs/2209.04899">paper</a></td>
<td nowrap><a href="https://vlc-robot.github.io/hiveformer-corl/">project</a></td>
<td nowrap><a href="https://github.com/vlc-robot/hiveformer">code</a></td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CoRL 2023</td>
<td nowrap><a href="https://arxiv.org/abs/2303.00905">Open-World Object Manipulation using Pre-trained Vision-Language Models</a></td>
<td nowrap>MOO studies open-world object manipulation with pretrained vision-language models.</td>
<td nowrap>Open-World Object Manipulation using Pre-trained Vision-Language Models</td>
<td nowrap>robot action</td>
<td nowrap>VLA / generalist VLA</td>
<td nowrap>CoRL robot-learning method</td>
<td nowrap>robot policy</td>
<td nowrap>robot benchmarks</td>
<td nowrap>Add CoRL VLA coverage.</td>
<td nowrap><a href="https://arxiv.org/abs/2303.00905">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CoRL 2024</td>
<td nowrap><a href="https://arxiv.org/abs/2410.05273">HiRT: Enhancing Robotic Control with Hierarchical Robot Transformers</a></td>
<td nowrap>HiRT uses hierarchical robot transformers to improve robotic control.</td>
<td nowrap>HiRT</td>
<td nowrap>robot action</td>
<td nowrap>VLA / generalist VLA</td>
<td nowrap>CoRL robot-learning method</td>
<td nowrap>robot policy</td>
<td nowrap>robot benchmarks</td>
<td nowrap>Add CoRL VLA coverage.</td>
<td nowrap><a href="https://arxiv.org/abs/2410.05273">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CoRL 2023</td>
<td nowrap><a href="https://arxiv.org/abs/2307.14535">Scaling Up and Distilling Down: Language-Guided Robot Skill Acquisition</a></td>
<td nowrap>SUDD scales language-guided robot skill acquisition and distills it into executable policies.</td>
<td nowrap>Scaling Up and Distilling Down</td>
<td nowrap>robot action</td>
<td nowrap>VLA / generalist VLA</td>
<td nowrap>CoRL robot-learning method</td>
<td nowrap>robot policy</td>
<td nowrap>robot benchmarks</td>
<td nowrap>Add CoRL VLA coverage.</td>
<td nowrap><a href="https://arxiv.org/abs/2307.14535">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/real-stanford/scalingup">code</a></td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CVPR 2024</td>
<td nowrap><a href="https://openaccess.thecvf.com/content/CVPR2024/html/Li_ManipLLM_Embodied_Multimodal_Large_Language_Model_for_Object-Centric_Robotic_Manipulation_CVPR_2024_paper.html">ManipLLM: Embodied Multimodal Large Language Model for Object-Centric Robotic Manipulation</a></td>
<td nowrap>ManipLLM grounds multimodal language reasoning in object-centric robotic manipulation.</td>
<td nowrap>multimodal LLM</td>
<td nowrap>robot action</td>
<td nowrap>VLA / Generalist VLA</td>
<td nowrap>object-centric embodied reasoning</td>
<td nowrap>robot manipulation policy</td>
<td nowrap>simulation manipulation</td>
<td nowrap>Use multimodal LLM reasoning for object-centric manipulation.</td>
<td nowrap><a href="https://openaccess.thecvf.com/content/CVPR2024/papers/Li_ManipLLM_Embodied_Multimodal_Large_Language_Model_for_Object-Centric_Robotic_Manipulation_CVPR_2024_paper.pdf">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>NeurIPS 2024</td>
<td nowrap><a href="https://proceedings.neurips.cc/paper_files/paper/2024/hash/62203a74e233e933b160711e791e1a02-Abstract-Conference.html">PEAC: Unsupervised Pre-training for Cross-Embodiment Reinforcement Learning</a></td>
<td nowrap>PEAC pretrains policies across embodiments to improve transfer before downstream robot learning.</td>
<td nowrap>cross-embodiment policy</td>
<td nowrap>robot action</td>
<td nowrap>VLA / cross-embodiment</td>
<td nowrap>unsupervised pretraining</td>
<td nowrap>generalist robot policy</td>
<td nowrap>cross-embodiment benchmarks</td>
<td nowrap>Improve cross-embodiment policy transfer.</td>
<td nowrap><a href="https://proceedings.neurips.cc/paper_files/paper/2024/file/62203a74e233e933b160711e791e1a02-Paper-Conference.pdf">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://openaccess.thecvf.com/content/ICCV2025/html/Chen_CombatVLA_An_Efficient_Vision-Language-Action_Model_for_Combat_Tasks_in_3D_ICCV_2025_paper.html">CombatVLA: An Efficient Vision-Language-Action Model for Combat Tasks in 3D Action Role-Playing Games</a></td>
<td nowrap>CombatVLA studies efficient VLA control for real-time 3D game combat tasks.</td>
<td nowrap>CombatVLA</td>
<td nowrap>game action</td>
<td nowrap>VLA / Generalist VLA</td>
<td nowrap>efficient VLA control</td>
<td nowrap>real-time embodied agent</td>
<td nowrap>3D game tasks</td>
<td nowrap>Evaluate VLA-style action models in fast 3D interactive tasks.</td>
<td nowrap><a href="https://openaccess.thecvf.com/content/ICCV2025/papers/Chen_CombatVLA_An_Efficient_Vision-Language-Action_Model_for_Combat_Tasks_in_3D_ICCV_2025_paper.pdf">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICLR 2024</td>
<td nowrap><a href="https://openreview.net/forum?id=lFYj0oibGR">Vision-Language Foundation Models as Effective Robot Imitators</a></td>
<td nowrap>This work adapts vision-language foundation models as robot imitators for manipulation policies.</td>
<td nowrap>VLM foundation model</td>
<td nowrap>robot action</td>
<td nowrap>imitation learning</td>
<td nowrap>VLM-to-policy adaptation</td>
<td nowrap>robot imitation policy</td>
<td nowrap>robot manipulation benchmarks</td>
<td nowrap>Use pretrained VLMs as effective robot imitation learners.</td>
<td nowrap><a href="https://openreview.net/forum?id=lFYj0oibGR">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICLR 2023</td>
<td nowrap><a href="https://arxiv.org/abs/2311.01977">RT-Trajectory: Robotic Task Generalization via Hindsight Trajectory Sketches</a></td>
<td nowrap>RT-Trajectory uses hindsight trajectory sketches to improve robot task generalization.</td>
<td nowrap>robot policy</td>
<td nowrap>trajectory sketches</td>
<td nowrap>VLA / Generalist VLA</td>
<td nowrap>hindsight trajectory conditioning</td>
<td nowrap>generalist manipulation policy</td>
<td nowrap>robot manipulation tasks</td>
<td nowrap>Improve task generalization with trajectory sketch supervision.</td>
<td nowrap><a href="https://arxiv.org/abs/2311.01977">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICML 2023</td>
<td nowrap><a href="https://openreview.net/forum?id=nkDMZ8yqBt">VIMA: General Robot Manipulation with Multimodal Prompts</a></td>
<td nowrap>VIMA formulates robot manipulation as multimodal prompt-conditioned policy learning.</td>
<td nowrap>VIMA</td>
<td nowrap>manipulation action</td>
<td nowrap>multimodal prompt policy</td>
<td nowrap>prompt-conditioned imitation</td>
<td nowrap>generalist manipulation policy</td>
<td nowrap>VIMA-Bench</td>
<td nowrap>Use multimodal prompts to specify diverse manipulation tasks.</td>
<td nowrap><a href="https://openreview.net/forum?id=nkDMZ8yqBt">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICLR 2025</td>
<td nowrap><a href="https://proceedings.iclr.cc/paper_files/paper/2025/hash/8667f264f88c7938a73a53ab01eb1327-Abstract-Conference.html">TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies</a></td>
<td nowrap>TraceVLA adds visual trace prompts to improve spatial-temporal awareness in generalist robot policies.</td>
<td nowrap>generalist VLA</td>
<td nowrap>robot action</td>
<td nowrap>VLA / Generalist VLA</td>
<td nowrap>visual trace prompting</td>
<td nowrap>generalist robot policy</td>
<td nowrap>robot manipulation benchmarks</td>
<td nowrap>Enhance robot policy awareness with visual traces.</td>
<td nowrap><a href="https://proceedings.iclr.cc/paper_files/paper/2025/hash/8667f264f88c7938a73a53ab01eb1327-Abstract-Conference.html">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ECCV 2024</td>
<td nowrap><a href="https://openreview.net/forum?id=Sa7upAJOIN">QUAR-VLA: Vision-Language-Action Model for Quadruped Robots</a></td>
<td nowrap>QUAR-VLA extends VLA-style policy learning to quadruped robot control.</td>
<td nowrap>quadruped VLA</td>
<td nowrap>locomotion action</td>
<td nowrap>VLA / quadruped robots</td>
<td nowrap>vision-language-action control</td>
<td nowrap>quadruped policy</td>
<td nowrap>quadruped robot tasks</td>
<td nowrap>Apply VLA modeling to quadruped embodied control.</td>
<td nowrap><a href="https://openreview.net/forum?id=Sa7upAJOIN">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2508.05186">Learning to See and Act: Task-Aware Virtual View Exploration for Robotic Manipulation</a></td>
<td nowrap>This work uses task-aware virtual view exploration to improve perception and action in manipulation.</td>
<td nowrap>robot manipulation model</td>
<td nowrap>manipulation action</td>
<td nowrap>VLA / Generalist VLA</td>
<td nowrap>virtual-view exploration</td>
<td nowrap>robot manipulation policy</td>
<td nowrap>manipulation benchmarks</td>
<td nowrap>Use task-aware view exploration for better manipulation policy inputs.</td>
<td nowrap><a href="https://arxiv.org/abs/2508.05186">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>IROS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2409.12514">TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation</a></td>
<td nowrap>TinyVLA combines a compact VLA with diffusion policy to improve data efficiency and inference speed for robot manipulation.</td>
<td nowrap>TinyVLA</td>
<td nowrap>Diffusion action</td>
<td nowrap>VLA / Generalist VLA</td>
<td nowrap>compact VLA + diffusion policy</td>
<td nowrap>data-efficient VLA</td>
<td nowrap>Real robot manipulation</td>
<td nowrap>Build a smaller, faster, data-efficient VLA manipulation policy.</td>
<td nowrap><a href="https://arxiv.org/abs/2409.12514">paper</a></td>
<td nowrap><a href="https://tiny-vla.github.io/">project</a></td>
<td nowrap><a href="https://github.com/JayceWen/tinyvla">code</a></td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICLR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2502.05485">HAMSTER: Hierarchical Action Models For Open-World Robot Manipulation</a></td>
<td nowrap>HAMSTER uses hierarchical action models to connect high-level open-world manipulation decisions with executable low-level robot actions.</td>
<td nowrap>HAMSTER</td>
<td nowrap>hierarchical action</td>
<td nowrap>VLA / Generalist VLA</td>
<td nowrap>hierarchical action modeling</td>
<td nowrap>open-world manipulation policy</td>
<td nowrap>robot manipulation benchmarks</td>
<td nowrap>Build an open-world robot manipulation policy with explicit action hierarchy.</td>
<td nowrap><a href="https://arxiv.org/abs/2502.05485">paper</a></td>
<td nowrap><a href="https://hamster-robot.github.io/">project</a></td>
<td nowrap><a href="https://github.com/liyi14/HAMSTER_beta">code</a></td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICLR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2406.20095">LLaRA: Supercharging Robot Learning Data for Vision-Language Policy</a></td>
<td nowrap>LLaRA improves vision-language policy learning by converting and enriching robot learning data for VLA training.</td>
<td nowrap>LLaRA</td>
<td nowrap>policy action</td>
<td nowrap>VLA / Generalist VLA</td>
<td nowrap>robot-data augmentation for VLP/VLA</td>
<td nowrap>vision-language policy</td>
<td nowrap>robot learning datasets</td>
<td nowrap>Improve robot policy learning through stronger language-aligned training data.</td>
<td nowrap><a href="https://arxiv.org/abs/2406.20095">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/LostXine/LLaRA">code</a></td>
<td nowrap>-</td>
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
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64826">XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations</a></td>
<td nowrap>XR-1 learns unified vision-motion codes to train versatile VLA policies across heterogeneous robots, tasks, and demonstrations.</td>
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
</tr>
</tbody>
</table>

#### action representation

Total: 28 papers.

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
</tr>
</thead>
<tbody>
<tr>
<td nowrap>CoRL 2022</td>
<td nowrap><a href="https://arxiv.org/abs/2203.06173">Real-World Robot Learning with Masked Visual Pre-training</a></td>
<td nowrap>MVP uses masked visual pretraining for real-world robot learning.</td>
<td nowrap>Real-World Robot Learning with Masked Visual Pre-training</td>
<td nowrap>robot action</td>
<td nowrap>VLA / action representation</td>
<td nowrap>CoRL robot-learning method</td>
<td nowrap>robot policy</td>
<td nowrap>robot benchmarks</td>
<td nowrap>Add CoRL VLA coverage.</td>
<td nowrap><a href="https://arxiv.org/abs/2203.06173">paper</a></td>
<td nowrap><a href="https://tetexiao.com/projects/real-mvp">project</a></td>
<td nowrap><a href="https://github.com/ir413/mvp">code</a></td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CoRL 2022</td>
<td nowrap><a href="https://arxiv.org/abs/2203.12601">R3M: A Universal Visual Representation for Robot Manipulation</a></td>
<td nowrap>R3M learns a universal visual representation for robot manipulation.</td>
<td nowrap>R3M</td>
<td nowrap>robot action</td>
<td nowrap>VLA / action representation</td>
<td nowrap>CoRL robot-learning method</td>
<td nowrap>robot policy</td>
<td nowrap>robot benchmarks</td>
<td nowrap>Add CoRL VLA coverage.</td>
<td nowrap><a href="https://arxiv.org/abs/2203.12601">paper</a></td>
<td nowrap><a href="https://sites.google.com/view/robot-r3m/">project</a></td>
<td nowrap><a href="https://github.com/facebookresearch/r3m">code</a></td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CoRL 2023</td>
<td nowrap><a href="https://arxiv.org/abs/2306.10007">Robot Learning with Sensorimotor Pre-training</a></td>
<td nowrap>RPT uses sensorimotor pretraining for downstream robot learning.</td>
<td nowrap>Robot Learning with Sensorimotor Pre-training</td>
<td nowrap>robot action</td>
<td nowrap>VLA / action representation</td>
<td nowrap>CoRL robot-learning method</td>
<td nowrap>robot policy</td>
<td nowrap>robot benchmarks</td>
<td nowrap>Add CoRL VLA coverage.</td>
<td nowrap><a href="https://arxiv.org/abs/2306.10007">paper</a></td>
<td nowrap><a href="https://robotic-pretrained-transformer.github.io">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CoRL 2024</td>
<td nowrap><a href="https://arxiv.org/abs/2407.20179">Theia: Distilling Diverse Vision Foundation Models for Robot Learning</a></td>
<td nowrap>Theia distills diverse vision foundation models into robot-learning representations.</td>
<td nowrap>Theia</td>
<td nowrap>robot action</td>
<td nowrap>VLA / action representation</td>
<td nowrap>CoRL robot-learning method</td>
<td nowrap>robot policy</td>
<td nowrap>robot benchmarks</td>
<td nowrap>Add CoRL VLA coverage.</td>
<td nowrap><a href="https://arxiv.org/abs/2407.20179">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CoRL 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2509.07962">TA-VLA: Elucidating the Design Space of Torque-aware Vision-Language-Action Models</a></td>
<td nowrap>TA-VLA studies torque-aware action design for VLA models.</td>
<td nowrap>TA-VLA</td>
<td nowrap>robot action</td>
<td nowrap>VLA / action representation</td>
<td nowrap>CoRL robot-learning method</td>
<td nowrap>robot policy</td>
<td nowrap>robot benchmarks</td>
<td nowrap>Add CoRL VLA coverage.</td>
<td nowrap><a href="https://arxiv.org/abs/2509.07962">paper</a></td>
<td nowrap><a href="https://zzongzheng0918.github.io/Torque-Aware-VLA.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CoRL 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2508.01600">CLASS: Contrastive Learning via Action Sequence Supervision for Robot Manipulation</a></td>
<td nowrap>CLASS uses action-sequence supervision for contrastive robot manipulation learning.</td>
<td nowrap>CLASS</td>
<td nowrap>robot action</td>
<td nowrap>VLA / action representation</td>
<td nowrap>CoRL robot-learning method</td>
<td nowrap>robot policy</td>
<td nowrap>robot benchmarks</td>
<td nowrap>Add CoRL VLA coverage.</td>
<td nowrap><a href="https://arxiv.org/abs/2508.01600">paper</a></td>
<td nowrap><a href="https://class-robot.github.io/">project</a></td>
<td nowrap><a href="https://github.com/sean1295/CLASS/tree/main">code</a></td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CoRL 2021</td>
<td nowrap><a href="https://arxiv.org/abs/2010.14406">Transporter Networks: Rearranging the Visual World for Robotic Manipulation</a></td>
<td nowrap>Transporter Networks represent pick-and-place manipulation through spatial transport operations.</td>
<td nowrap>Transporter Networks</td>
<td nowrap>robot action</td>
<td nowrap>VLA / action representation</td>
<td nowrap>CoRL robot-learning method</td>
<td nowrap>robot policy</td>
<td nowrap>robot benchmarks</td>
<td nowrap>Add CoRL VLA coverage.</td>
<td nowrap><a href="https://arxiv.org/abs/2010.14406">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICLR 2024</td>
<td nowrap><a href="https://arxiv.org/abs/2310.08576">Learning to Act from Actionless Videos through Dense Correspondences</a></td>
<td nowrap>This work learns action representations from actionless videos using dense visual correspondences.</td>
<td nowrap>video pretraining</td>
<td nowrap>latent action</td>
<td nowrap>action representation / pretraining</td>
<td nowrap>dense correspondence learning</td>
<td nowrap>video-to-action representation</td>
<td nowrap>robot manipulation benchmarks</td>
<td nowrap>Recover reusable action structure without action labels.</td>
<td nowrap><a href="https://arxiv.org/abs/2310.08576">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICML 2024</td>
<td nowrap><a href="https://arxiv.org/abs/2402.07872">PIVOT: Iterative Visual Prompting Elicits Actionable Knowledge for VLMs</a></td>
<td nowrap>PIVOT elicits spatial and actionable knowledge from VLMs through iterative visual prompting.</td>
<td nowrap>VLM</td>
<td nowrap>actionable visual prompt</td>
<td nowrap>action representation / affordance</td>
<td nowrap>iterative visual prompting</td>
<td nowrap>VLM affordance reasoning</td>
<td nowrap>spatial action benchmarks</td>
<td nowrap>Extract actionable spatial knowledge from VLMs.</td>
<td nowrap><a href="https://arxiv.org/abs/2402.07872">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
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
</tr>
<tr>
<td nowrap>ICLR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2410.11758">Latent Action Pretraining from Videos</a></td>
<td nowrap>LAPA learns latent action abstractions from videos before transferring them to robot action generation.</td>
<td nowrap>LAPA</td>
<td nowrap>latent action</td>
<td nowrap>action representation / pretraining</td>
<td nowrap>latent action pretraining</td>
<td nowrap>video-to-action representation</td>
<td nowrap>robot manipulation benchmarks</td>
<td nowrap>Learn reusable latent actions from videos for downstream VLA policies.</td>
<td nowrap><a href="https://arxiv.org/abs/2410.11758">paper</a></td>
<td nowrap><a href="https://latentactionpretraining.github.io/">project</a></td>
<td nowrap><a href="https://github.com/LatentActionPretraining/LAPA">code</a></td>
<td nowrap><a href="https://huggingface.co/latent-action-pretraining/LAPA-7B-openx">hf</a></td>
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
</tr>
</tbody>
</table>

#### diffusion/flow policy

Total: 72 papers.

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
</tr>
</thead>
<tbody>
<tr>
<td nowrap>CoRL 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2509.04996">FLOWER: Democratizing Generalist Robot Policies with Efficient Vision-Language-Action Flow Policies</a></td>
<td nowrap>FLOWER builds efficient VLA flow policies for generalist robot control.</td>
<td nowrap>FLOWER</td>
<td nowrap>robot action</td>
<td nowrap>VLA / diffusion/flow policy</td>
<td nowrap>CoRL robot-learning method</td>
<td nowrap>robot policy</td>
<td nowrap>robot benchmarks</td>
<td nowrap>Add CoRL VLA coverage.</td>
<td nowrap><a href="https://arxiv.org/abs/2509.04996">paper</a></td>
<td nowrap><a href="https://intuitive-robots.github.io/flower_vla">project</a></td>
<td nowrap><a href="https://github.com/intuitive-robots/flower_vla_pret">code</a></td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CoRL 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2509.01819">ManiFlow: A General Robot Manipulation Policy via Consistency Flow Training</a></td>
<td nowrap>ManiFlow trains general robot manipulation policies with consistency flow.</td>
<td nowrap>ManiFlow</td>
<td nowrap>robot action</td>
<td nowrap>VLA / diffusion/flow policy</td>
<td nowrap>CoRL robot-learning method</td>
<td nowrap>robot policy</td>
<td nowrap>robot benchmarks</td>
<td nowrap>Add CoRL VLA coverage.</td>
<td nowrap><a href="https://arxiv.org/abs/2509.01819">paper</a></td>
<td nowrap><a href="https://maniflow-policy.github.io/">project</a></td>
<td nowrap><a href="https://github.com/geyan21/ManiFlow_Policy">code</a></td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CoRL 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2505.21851">Streaming Flow Policy: Simplifying diffusion/flow-matching policies by treating action trajectories as flow trajectories</a></td>
<td nowrap>Streaming Flow Policy treats action trajectories as flow trajectories for simpler policy generation.</td>
<td nowrap>Streaming Flow Policy</td>
<td nowrap>robot action</td>
<td nowrap>VLA / diffusion/flow policy</td>
<td nowrap>CoRL robot-learning method</td>
<td nowrap>robot policy</td>
<td nowrap>robot benchmarks</td>
<td nowrap>Add CoRL VLA coverage.</td>
<td nowrap><a href="https://arxiv.org/abs/2505.21851">paper</a></td>
<td nowrap><a href="https://siddancha.github.io/streaming-flow-policy/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CoRL 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2502.05855">DexVLA: Vision-Language Model with Plug-In Diffusion Expert for General Robot Control</a></td>
<td nowrap>DexVLA plugs a diffusion expert into a vision-language model for robot control.</td>
<td nowrap>DexVLA</td>
<td nowrap>robot action</td>
<td nowrap>VLA / diffusion/flow policy</td>
<td nowrap>CoRL robot-learning method</td>
<td nowrap>robot policy</td>
<td nowrap>robot benchmarks</td>
<td nowrap>Add CoRL VLA coverage.</td>
<td nowrap><a href="https://arxiv.org/abs/2502.05855">paper</a></td>
<td nowrap><a href="https://dex-vla.github.io">project</a></td>
<td nowrap><a href="https://github.com/juruobenruo/DexVLA">code</a></td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICML 2025</td>
<td nowrap><a href="https://diffusion-vla.github.io/">DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression</a></td>
<td nowrap>DiffusionVLA scales robot foundation models with unified diffusion and autoregressive generation.</td>
<td nowrap>DiffusionVLA</td>
<td nowrap>diffusion + AR action</td>
<td nowrap>VLA / diffusion-flow policy</td>
<td nowrap>unified diffusion and autoregression</td>
<td nowrap>robot foundation model</td>
<td nowrap>robot manipulation benchmarks</td>
<td nowrap>Scale VLA policy learning with diffusion and autoregressive modeling.</td>
<td nowrap><a href="https://diffusion-vla.github.io/">paper</a></td>
<td nowrap><a href="https://diffusion-vla.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICLR 2025</td>
<td nowrap><a href="https://openreview.net/forum?id=nDmwloEl3N">Efficient Diffusion Transformer Policies with Mixture of Expert Denoisers for Multitask Learning</a></td>
<td nowrap>This work uses mixture-of-expert denoisers to make diffusion transformer policies more efficient across tasks.</td>
<td nowrap>diffusion transformer policy</td>
<td nowrap>continuous action</td>
<td nowrap>VLA / diffusion-flow policy</td>
<td nowrap>MoE denoisers</td>
<td nowrap>multitask diffusion policy</td>
<td nowrap>robot manipulation tasks</td>
<td nowrap>Improve multitask diffusion policy efficiency.</td>
<td nowrap><a href="https://openreview.net/forum?id=nDmwloEl3N">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>AAAI 2025</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/33617">FlowPolicy: Enabling Fast and Robust 3D Flow-Based Policy via Consistency Flow Matching for Robot Manipulation</a></td>
<td nowrap>FlowPolicy applies consistency flow matching to fast and robust 3D robot manipulation policies.</td>
<td nowrap>3D flow policy</td>
<td nowrap>continuous 3D action</td>
<td nowrap>VLA / diffusion-flow policy</td>
<td nowrap>consistency flow matching</td>
<td nowrap>fast 3D manipulation policy</td>
<td nowrap>robot manipulation benchmarks</td>
<td nowrap>Build faster flow-based 3D manipulation policies.</td>
<td nowrap><a href="https://arxiv.org/abs/2412.04987">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://openreview.net/forum?id=asS4W7Yw5e">GauDP: Reinventing Multi-Agent Collaboration through Gaussian-Image Synergy in Diffusion Policies</a></td>
<td nowrap>GauDP uses Gaussian-image synergy inside diffusion policies for multi-agent collaboration.</td>
<td nowrap>diffusion policy</td>
<td nowrap>continuous action</td>
<td nowrap>VLA / diffusion-flow policy</td>
<td nowrap>Gaussian-image synergy</td>
<td nowrap>multi-agent diffusion policy</td>
<td nowrap>multi-agent manipulation tasks</td>
<td nowrap>Improve collaboration through diffusion policy representation.</td>
<td nowrap><a href="https://arxiv.org/pdf/2511.00998">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CVPR 2024</td>
<td nowrap><a href="https://openaccess.thecvf.com/content/CVPR2024/html/Ma_Hierarchical_Diffusion_Policy_for_Kinematics-Aware_Multi-Task_Robotic_Manipulation_CVPR_2024_paper.html">Hierarchical Diffusion Policy for Kinematics-Aware Multi-Task Robotic Manipulation</a></td>
<td nowrap>HDP combines hierarchy and kinematic awareness for multitask robotic manipulation with diffusion policies.</td>
<td nowrap>diffusion policy</td>
<td nowrap>continuous action</td>
<td nowrap>VLA / diffusion-flow policy</td>
<td nowrap>hierarchical kinematics-aware diffusion</td>
<td nowrap>multitask robot policy</td>
<td nowrap>robot manipulation benchmarks</td>
<td nowrap>Make diffusion policies kinematics-aware for multitask manipulation.</td>
<td nowrap><a href="https://openaccess.thecvf.com/content/CVPR2024/papers/Ma_Hierarchical_Diffusion_Policy_for_Kinematics-Aware_Multi-Task_Robotic_Manipulation_CVPR_2024_paper.pdf">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=H1KDMNOKQn">HybridVLA: Collaborative Diffusion and Autoregression in a Unified Vision-Language-Action Model</a></td>
<td nowrap>HybridVLA combines autoregressive token prediction and diffusion denoising in one VLA backbone to improve continuous robot action generation.</td>
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
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=UvQOcw2oCD">Unified Diffusion VLA: Vision-Language-Action Model via Joint Discrete Denosing Diffusion Process</a></td>
<td nowrap>Unified Diffusion VLA jointly denoises future visual tokens and action tokens so generation and control reinforce each other.</td>
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
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=2RIqqNqALN">When would Vision-Proprioception Policies Fail in Robotic Manipulation?</a></td>
<td nowrap>This study analyzes when vision-proprioception policies over-rely on proprioception and fail to use visual cues during robotic manipulation.</td>
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
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=BTe5VLBjPg">VITA: Vision-to-Action Flow Matching Policy</a></td>
<td nowrap>VITA uses flow matching from visual representations to action latents to reduce conditioning overhead in visuomotor policy generation.</td>
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
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=BvirMuKWV1">When a Robot is More Capable than a Human: Learning from Constrained Demonstrators</a></td>
<td nowrap>This work learns policies that can surpass constrained demonstrations by accounting for the demonstrator's limited action interface.</td>
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
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=IaGf8Eh5Uo">Reference Grounded Skill Discovery</a></td>
<td nowrap>Reference Grounded Skill Discovery uses reference motion representations to guide unsupervised skill learning in high-dimensional agents.</td>
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
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=KFu4p3pd11">Masked Generative Policy for Robotic Control</a></td>
<td nowrap>Masked Generative Policy tokenizes actions and uses masked transformer refinement for fast, coherent visuomotor control.</td>
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
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=P9PVdWyM3U">Policy Contrastive Decoding for Robotic Foundation Models</a></td>
<td nowrap>Policy Contrastive Decoding steers robotic foundation models at inference by contrasting actions from original and object-masked observations.</td>
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
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=PL0tJOfm7I">Demystifying Robot Diffusion Policies: Action Memorization and a Simple Lookup Table Alternative</a></td>
<td nowrap>This analysis argues that diffusion policies often behave like useful action lookup tables in sparse imitation settings.</td>
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
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=Q1CP0iAmOb">H$^3$DP: Triply‑Hierarchical Diffusion Policy for Visuomotor Learning</a></td>
<td nowrap>H^3DP couples depth-aware perception, multi-scale visual features, and hierarchical action denoising for visuomotor diffusion policies.</td>
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
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=TnLFRhLuZ6">Compose Your Policies! Improving Diffusion-based or Flow-based Robot Policies via Test-time Distribution-level Composition</a></td>
<td nowrap>This method composes diffusion or flow policy distributions at test time to improve behavior without additional training.</td>
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
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=VSWjHIveqZ">Abstracting Robot Manipulation Skills via Mixture-of-Experts Diffusion Policies</a></td>
<td nowrap>This work uses a mixture-of-experts diffusion policy to learn reusable skill bases and route actions to task-relevant experts.</td>
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
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=d08yOXs1Dl">SpikePingpong: Spike Vision-based Fast-Slow Pingpong Robot System</a></td>
<td nowrap>SpikePingpong combines event-based fast vision with slower control reasoning for high-speed robotic table-tennis behavior.</td>
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
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=dQ6d5bgXtM">Translating Flow to Policy via Hindsight Online Imitation</a></td>
<td nowrap>This method improves low-level policies from online rollouts by relabeling achieved outcomes as hindsight goals.</td>
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
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=iKJbmx1iuQ">Contractive Diffusion Policies</a></td>
<td nowrap>Contractive Diffusion Policies regularize diffusion sampling dynamics to make continuous-control action generation more stable.</td>
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
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38881">ManiLong-Shot: Interaction-Aware One-Shot Imitation Learning for Long-Horizon Manipulation</a></td>
<td nowrap>ManiLong-Shot decomposes long-horizon one-shot manipulation into interaction-aware primitives that can be transferred from demonstrations.</td>
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
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38889">Learning Diffusion Policy from Primitive Skills for Robot Manipulation</a></td>
<td nowrap>This work conditions diffusion policies on interpretable primitive skills to align short-horizon action generation for manipulation.</td>
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
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38912">Intention-Aware Diffusion Model for Pedestrian Trajectory Prediction</a></td>
<td nowrap>This model injects short- and long-term pedestrian intentions into diffusion-based trajectory prediction.</td>
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
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38919">MP1: MeanFlow Tames Policy Learning in 1-step for Robotic Manipulation</a></td>
<td nowrap>MP1 applies MeanFlow to point-cloud manipulation policies, generating action trajectories in one network evaluation.</td>
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
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38934">ForeDiffusion: Foresight-Conditioned Diffusion Policy via Future View Construction for Robot Manipulation</a></td>
<td nowrap>ForeDiffusion conditions diffusion policies on predicted future views to reduce error accumulation in manipulation.</td>
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
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38950">Bridging Scale Discrepancies in Robotic Control via Language-Based Action Representations</a></td>
<td nowrap>This work converts robot actions into language-based representations to reduce scale mismatch across tasks and platforms.</td>
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
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38959">D²PPO: Diffusion Policy Policy Optimization with Dispersive Loss</a></td>
<td nowrap>D2PPO adds dispersive-loss regularization to diffusion policy optimization to prevent representation collapse during manipulation learning.</td>
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
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62902">Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies</a></td>
<td nowrap>Discrete Diffusion VLA models discretized action chunks with in-backbone discrete diffusion for parallel, error-correcting VLA action decoding.</td>
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
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61717">STEP: Warm-Started Visuomotor Policies with Spatiotemporal Consistency Prediction</a></td>
<td nowrap>STEP warm-starts diffusion policies with spatiotemporally consistent actions to cut closed-loop inference latency.</td>
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
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61049">Learning Human-Robot Collaboration via Heterogeneous-Agent Lyapunov Policy Optimization</a></td>
<td nowrap>HALyPO stabilizes heterogeneous human-robot multi-agent policy optimization with Lyapunov-style disagreement control.</td>
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
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2509.00117">Emerging Risks from Embodied AI Require Urgent Policy Action</a></td>
<td nowrap>This policy analysis maps physical, surveillance, and societal risks from embodied AI and calls for targeted governance.</td>
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
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2512.00085">Hyper-GoalNet: Goal-Conditioned Manipulation Policy Learning with HyperNetworks</a></td>
<td nowrap>Hyper-GoalNet uses hypernetworks to generate goal-specific manipulation policy parameters from goal descriptions.</td>
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
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2505.13431">A Practical Guide for Incorporating Symmetry in Diffusion Policy</a></td>
<td nowrap>This guide evaluates lightweight ways to add symmetry priors to diffusion policies without full equivariant architectures.</td>
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
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2509.25822">Act to See, See to Act: Diffusion-Driven Perception-Action Interplay for Adaptive Policies</a></td>
<td nowrap>DP-AG models perception-action feedback with action-guided diffusion dynamics for more adaptive imitation policies.</td>
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
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2511.20906">DASIP: Dynamic Test-Time Compute Scaling for Robot Control with Stochastic Interpolant Policies</a></td>
<td nowrap>DASIP adjusts stochastic-interpolant policy compute at test time according to estimated manipulation difficulty.</td>
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
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.19757">Dita: Scaling Diffusion Transformer for Generalist Vision-Language-Action Policy</a></td>
<td nowrap>Dita scales diffusion transformers to denoise continuous action sequences inside a generalist VLA policy.</td>
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
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/1571">SD2Actor: Continuous State Decomposition via Diffusion Embeddings for Robotic Manipulation</a></td>
<td nowrap>SD2Actor decomposes object states with diffusion embeddings to generate zero-shot continuous manipulation actions.</td>
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
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2507.04331">Wavelet Policy: Lifting Scheme for Policy Learning in Long-Horizon Tasks</a></td>
<td nowrap>Wavelet Policy uses learnable multi-scale wavelet transforms to improve long-horizon policy learning.</td>
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
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://openaccess.thecvf.com/content/CVPR2025/papers/Tian_PDFactor_Learning_Tri-Perspective_View_Policy_Diffusion_Field_for_Multi-Task_Robotic_CVPR_2025_paper.pdf">PDFactor: Learning Tri-Perspective View Policy Diffusion Field for Multi-Task Robotic Manipulation</a></td>
<td nowrap>PDFactor represents 3D action distributions as tri-perspective diffusion fields for efficient multi-task manipulation.</td>
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
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2505.13091">Touch2Shape: Touch-Conditioned 3D Diffusion for Shape Exploration and Reconstruction</a></td>
<td nowrap>Touch2Shape conditions 3D diffusion on tactile observations to explore and reconstruct object shape.</td>
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
</tr>
</tbody>
</table>

#### 3D grounding

Total: 35 papers.

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
</tr>
</thead>
<tbody>
<tr>
<td nowrap>CoRL 2023</td>
<td nowrap><a href="https://arxiv.org/abs/2308.07931">Distilled Feature Fields Enable Few-Shot Language-Guided Manipulation</a></td>
<td nowrap>F3RM uses distilled feature fields for few-shot language-guided manipulation.</td>
<td nowrap>Distilled Feature Fields Enable Few-Shot Language-Guided Manipulation</td>
<td nowrap>robot action</td>
<td nowrap>VLA / 3D grounding</td>
<td nowrap>CoRL robot-learning method</td>
<td nowrap>robot policy</td>
<td nowrap>robot benchmarks</td>
<td nowrap>Add CoRL VLA coverage.</td>
<td nowrap><a href="https://arxiv.org/abs/2308.07931">paper</a></td>
<td nowrap><a href="https://f3rm.github.io">project</a></td>
<td nowrap><a href="https://github.com/f3rm/f3rm">code</a></td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CoRL 2023</td>
<td nowrap><a href="https://arxiv.org/abs/2306.14896">RVT: Robotic View Transformer for 3D Object Manipulation</a></td>
<td nowrap>RVT uses view-transformer representations for 3D object manipulation.</td>
<td nowrap>RVT</td>
<td nowrap>robot action</td>
<td nowrap>VLA / 3D grounding</td>
<td nowrap>CoRL robot-learning method</td>
<td nowrap>robot policy</td>
<td nowrap>robot benchmarks</td>
<td nowrap>Add CoRL VLA coverage.</td>
<td nowrap><a href="https://arxiv.org/abs/2306.14896">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CoRL 2022</td>
<td nowrap><a href="https://arxiv.org/abs/2209.05451">Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation</a></td>
<td nowrap>PerAct uses Perceiver-style 3D representations for multitask manipulation.</td>
<td nowrap>Perceiver-Actor</td>
<td nowrap>robot action</td>
<td nowrap>VLA / 3D grounding</td>
<td nowrap>CoRL robot-learning method</td>
<td nowrap>robot policy</td>
<td nowrap>robot benchmarks</td>
<td nowrap>Add CoRL VLA coverage.</td>
<td nowrap><a href="https://arxiv.org/abs/2209.05451">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CoRL 2023</td>
<td nowrap><a href="https://arxiv.org/abs/2306.17817">Act3D: 3D Feature Field Transformers for Multi-Task Robotic Manipulation</a></td>
<td nowrap>Act3D builds 3D feature-field transformers for multitask robotic manipulation.</td>
<td nowrap>Act3D</td>
<td nowrap>robot action</td>
<td nowrap>VLA / 3D grounding</td>
<td nowrap>CoRL robot-learning method</td>
<td nowrap>robot policy</td>
<td nowrap>robot benchmarks</td>
<td nowrap>Add CoRL VLA coverage.</td>
<td nowrap><a href="https://arxiv.org/abs/2306.17817">paper</a></td>
<td nowrap><a href="https://act3d.github.io">project</a></td>
<td nowrap><a href="https://github.com/zhouxian/act3d-chained-diffuser">code</a></td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICML 2024</td>
<td nowrap><a href="https://proceedings.mlr.press/v235/zhen24a.html">3D-VLA: A 3D Vision-Language-Action Generative World Model</a></td>
<td nowrap>3D-VLA builds a 3D generative world model for vision-language-action manipulation.</td>
<td nowrap>3D VLA</td>
<td nowrap>3D grounded action</td>
<td nowrap>3D grounding / world model</td>
<td nowrap>3D generative world modeling</td>
<td nowrap>3D VLA policy</td>
<td nowrap>robot manipulation benchmarks</td>
<td nowrap>Ground VLA action generation in 3D world representations.</td>
<td nowrap><a href="https://proceedings.mlr.press/v235/zhen24a/zhen24a.pdf">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>IROS 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2606.26800">SSI-Policy: Learning Structured Scene Interfaces for Vision-Language Robotic Manipulation</a></td>
<td nowrap>SSI-Policy connects vision-language reasoning with low-data robot manipulation policy learning through structured scene interfaces.</td>
<td nowrap>vision-language policy</td>
<td nowrap>continuous action</td>
<td nowrap>3D grounding / structured scene interface</td>
<td nowrap>scene-interface policy learning</td>
<td nowrap>structured VLA policy</td>
<td nowrap>Real robot manipulation</td>
<td nowrap>Use structured scene representations to improve low-data manipulation generalization.</td>
<td nowrap><a href="https://arxiv.org/abs/2606.26800">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICRA 2025</td>
<td nowrap><a href="https://kalie-vlm.github.io/">KALIE: Fine-Tuning Vision-Language Models for Open-World Manipulation without Robot Data</a></td>
<td nowrap>KALIE fine-tunes VLMs to predict language-conditioned point affordances, using synthetic data for open-world manipulation.</td>
<td nowrap>VLM</td>
<td nowrap>affordance point</td>
<td nowrap>3D grounding / affordance grounding</td>
<td nowrap>synthetic data fine-tuning</td>
<td nowrap>affordance-conditioned manipulation</td>
<td nowrap>Real robot manipulation</td>
<td nowrap>Learn language-conditioned affordances without real robot data.</td>
<td nowrap><a href="https://kalie-vlm.github.io/">paper</a></td>
<td nowrap><a href="https://kalie-vlm.github.io/">project</a></td>
<td nowrap><a href="https://github.com/gractang/kalie">code</a></td>
<td nowrap>-</td>
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
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38921">ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver</a></td>
<td nowrap>ReconVLA reconstructs target gaze regions to improve visual grounding in vision-language-action robot policies.</td>
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
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38939">Indoor Multi-View Radar Object Detection via 3D Bounding Box Diffusion</a></td>
<td nowrap>REXO lifts diffusion-based 3D bounding boxes into multi-view radar perception for indoor object detection.</td>
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
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38946">RaLD: Generating High-Resolution 3D Radar Point Clouds with Latent Diffusion</a></td>
<td nowrap>RaLD uses latent diffusion to generate denser, higher-resolution 3D radar point clouds.</td>
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
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38947">Grounding Actions in Camera Space: Observation-Centric Vision-Language-Action Policy</a></td>
<td nowrap>OC-VLA predicts actions in camera coordinates to reduce observation-action spatial inconsistency in VLA policies.</td>
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
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://neurips.cc/virtual/2025/loc/san-diego/poster/118141">Building 3D Representations and Generating Motions From a Single Image via Video-Generation</a></td>
<td nowrap>VGER uses video generation from a single RGB image to build 3D scene representations for collision-free motion.</td>
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
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/pdf/2504.21530">RoboGround: Robot Manipulation with Grounded Vision-Language Priors</a></td>
<td nowrap>RoboGround uses vision-language grounding masks as intermediate spatial priors for generalizable manipulation policies.</td>
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
</tr>
</tbody>
</table>

#### online/RL fine-tuning

Total: 21 papers.

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
</tr>
</thead>
<tbody>
<tr>
<td nowrap>CoRL 2023</td>
<td nowrap><a href="https://scholar.google.com/scholar?q=Q-transformer%3A+Scalable+offline+reinforcement+learning+via+autoregressive+q-functions">Q-transformer: Scalable offline reinforcement learning via autoregressive q-functions</a></td>
<td nowrap>Q-transformer scales offline RL for robot policies through autoregressive Q-functions.</td>
<td nowrap>Q-transformer</td>
<td nowrap>robot action</td>
<td nowrap>VLA / online/RL fine-tuning</td>
<td nowrap>CoRL robot-learning method</td>
<td nowrap>robot policy</td>
<td nowrap>robot benchmarks</td>
<td nowrap>Add CoRL VLA coverage.</td>
<td nowrap><a href="https://scholar.google.com/scholar?q=Q-transformer%3A+Scalable+offline+reinforcement+learning+via+autoregressive+q-functions">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CoRL 2024</td>
<td nowrap><a href="https://arxiv.org/abs/2410.13816">Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance</a></td>
<td nowrap>V-GPS improves robotic foundation models with value guidance.</td>
<td nowrap>Steering Your Generalists</td>
<td nowrap>robot action</td>
<td nowrap>VLA / online/RL fine-tuning</td>
<td nowrap>CoRL robot-learning method</td>
<td nowrap>robot policy</td>
<td nowrap>robot benchmarks</td>
<td nowrap>Add CoRL VLA coverage.</td>
<td nowrap><a href="https://arxiv.org/abs/2410.13816">paper</a></td>
<td nowrap><a href="https://nakamotoo.github.io/V-GPS">project</a></td>
<td nowrap><a href="https://github.com/nakamotoo/V-GPS">code</a></td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CoRL 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.16211">ControlVLA: Few-shot Object-centric Adaptation for Pre-trained Vision-Language-Action Models</a></td>
<td nowrap>ControlVLA adapts pretrained VLA models to object-centric tasks with few examples.</td>
<td nowrap>ControlVLA</td>
<td nowrap>robot action</td>
<td nowrap>VLA / online/RL fine-tuning</td>
<td nowrap>CoRL robot-learning method</td>
<td nowrap>robot policy</td>
<td nowrap>robot benchmarks</td>
<td nowrap>Add CoRL VLA coverage.</td>
<td nowrap><a href="https://arxiv.org/abs/2506.16211">paper</a></td>
<td nowrap><a href="https://controlvla.github.io/">project</a></td>
<td nowrap><a href="https://github.com/ControlVLA/ControlVLA">code</a></td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CoRL 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2508.02062">RICL: Adding In-Context Adaptability to Pre-Trained Vision-Language-Action Models</a></td>
<td nowrap>RICL adds in-context adaptability to pretrained VLA models.</td>
<td nowrap>RICL</td>
<td nowrap>robot action</td>
<td nowrap>VLA / online/RL fine-tuning</td>
<td nowrap>CoRL robot-learning method</td>
<td nowrap>robot policy</td>
<td nowrap>robot benchmarks</td>
<td nowrap>Add CoRL VLA coverage.</td>
<td nowrap><a href="https://arxiv.org/abs/2508.02062">paper</a></td>
<td nowrap><a href="https://ricl-vla.github.io/">project</a></td>
<td nowrap><a href="https://github.com/ricl-vla/ricl_openpi">code</a></td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CoRL 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.17811">RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models</a></td>
<td nowrap>RoboMonkey scales test-time sampling and verification for VLA policies.</td>
<td nowrap>RoboMonkey</td>
<td nowrap>robot action</td>
<td nowrap>VLA / online/RL fine-tuning</td>
<td nowrap>CoRL robot-learning method</td>
<td nowrap>robot policy</td>
<td nowrap>robot benchmarks</td>
<td nowrap>Add CoRL VLA coverage.</td>
<td nowrap><a href="https://arxiv.org/abs/2506.17811">paper</a></td>
<td nowrap><a href="https://robomonkey-vla.github.io/">project</a></td>
<td nowrap><a href="https://github.com/robomonkey-vla/RoboMonkey">code</a></td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICML 2024</td>
<td nowrap><a href="https://proceedings.mlr.press/v235/springenberg24a.html">Offline Actor-Critic Reinforcement Learning Scales to Large Models</a></td>
<td nowrap>This work studies scaling offline actor-critic reinforcement learning to large model policies.</td>
<td nowrap>large policy model</td>
<td nowrap>policy action</td>
<td nowrap>offline RL / VLA post-training</td>
<td nowrap>offline actor-critic</td>
<td nowrap>model-based or actor-critic RL</td>
<td nowrap>offline RL benchmarks</td>
<td nowrap>Understand how large policies can be improved with offline RL.</td>
<td nowrap><a href="https://arxiv.org/abs/2402.05546">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2512.23703">General Process Reward Modeling for Robotic Reinforcement Learning</a></td>
<td nowrap>GPRM builds process reward models for robotic reinforcement learning and policy improvement.</td>
<td nowrap>robot policy</td>
<td nowrap>robot action</td>
<td nowrap>VLA / RL / reward modeling</td>
<td nowrap>process reward modeling</td>
<td nowrap>robotic RL</td>
<td nowrap>robot RL benchmarks</td>
<td nowrap>Use process-level rewards to improve robotic policy learning.</td>
<td nowrap><a href="https://arxiv.org/abs/2512.23703">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>IROS 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2503.05833">Refined Policy Distillation: From VLA Generalists to RL Experts</a></td>
<td nowrap>RPD distills generalist VLAs such as Octo and OpenVLA into task-specialist policies through reinforcement learning.</td>
<td nowrap>Octo / OpenVLA</td>
<td nowrap>policy action</td>
<td nowrap>RL distillation / online fine-tuning</td>
<td nowrap>Refined Policy Distillation</td>
<td nowrap>RL expert policy</td>
<td nowrap>Sim + Real</td>
<td nowrap>Transfer generalist VLAs into stronger task-specialist policies.</td>
<td nowrap><a href="https://arxiv.org/abs/2503.05833">paper</a></td>
<td nowrap><a href="https://refined-policy-distillation.github.io/">project</a></td>
<td nowrap><a href="https://github.com/Refined-Policy-Distillation/RPD">code</a></td>
<td nowrap><a href="https://huggingface.co/Juelg">hf</a></td>
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
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38876">Steering Visuomotor Policy in Open Worlds via Cross-View Goal Alignment</a></td>
<td nowrap>This method lets users specify goals from their own camera view and aligns them to the agent view for open-world visuomotor control.</td>
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
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/63131">HIER: Human-in-the-Loop Imagination-Execution Refinement for General Real-World Vision-Language-Action Models</a></td>
<td nowrap>HIER iteratively refines real-world VLA behavior with human-in-the-loop imagination, execution, and feedback.</td>
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
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://openreview.net/forum?id=RkdTtznSAL">Real-World Reinforcement Learning of Active Perception Behaviors</a></td>
<td nowrap>This work trains active perception policies in the real world using privileged training signals and asymmetric advantage-weighted regression.</td>
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
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2505.19789">What Can RL Bring to VLA Generalization? An Empirical Study</a></td>
<td nowrap>RLVLA studies how PPO, GRPO, and DPO-style reinforcement learning affect VLA cross-task generalization.</td>
<td nowrap>OpenVLA</td>
<td nowrap>AR</td>
<td nowrap>VLA / RL / Online Fine-tuning</td>
<td nowrap>PPO / GRPO / DPO</td>
<td nowrap>Hybrid / MF</td>
<td nowrap>Sim ✓ (MT)</td>
<td nowrap>Measure what reinforcement learning contributes to VLA generalization.</td>
<td nowrap><a href="https://arxiv.org/abs/2505.19789">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/gen-robot/RL4VLA">code</a></td>
<td nowrap>-</td>
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
</tr>
</tbody>
</table>

#### Safety and Robustness

Total: 7 papers.

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
</tr>
</thead>
<tbody>
<tr>
<td nowrap>NeurIPS 2024</td>
<td nowrap><a href="https://proceedings.neurips.cc/paper_files/paper/2024/hash/d83fd70a31c64e020844ec80705ba87f-Abstract-Conference.html">Diffusion Policy Attacker: Crafting Adversarial Attacks for Diffusion-based Policies</a></td>
<td nowrap>DPA studies adversarial attacks against diffusion-based robot policies.</td>
<td nowrap>diffusion policy</td>
<td nowrap>continuous action</td>
<td nowrap>VLA / safety and robustness</td>
<td nowrap>diffusion policy attack</td>
<td nowrap>adversarial robustness evaluation</td>
<td nowrap>robot policy benchmarks</td>
<td nowrap>Evaluate attack surfaces in diffusion-based robot policies.</td>
<td nowrap><a href="https://arxiv.org/abs/2405.19424">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=OwinX7PI83">BEAT: Visual Backdoor Attacks on VLM-based Embodied Agents via Contrastive Trigger Learning</a></td>
<td nowrap>BEAT crafts visual backdoor attacks for VLM-based embodied agents using contrastive trigger learning.</td>
<td nowrap>VLM embodied agent</td>
<td nowrap>policy action</td>
<td nowrap>VLA / safety and robustness</td>
<td nowrap>contrastive trigger learning</td>
<td nowrap>backdoor attack evaluation</td>
<td nowrap>embodied agent benchmarks</td>
<td nowrap>Expose visual backdoor risks in embodied VLM agents.</td>
<td nowrap><a href="https://arxiv.org/abs/2510.27623">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICRA 2025</td>
<td nowrap><a href="https://ieeexplore.ieee.org/document/11128017/">Run-time Observation Interventions Make Vision-Language-Action Models More Visually Robust</a></td>
<td nowrap>BYOVLA identifies and edits task-irrelevant visual regions at runtime to make Octo/OpenVLA more robust to visual distractors.</td>
<td nowrap>Octo / OpenVLA</td>
<td nowrap>AR / policy action</td>
<td nowrap>VLA / safety and robustness</td>
<td nowrap>run-time observation intervention</td>
<td nowrap>robust VLA execution</td>
<td nowrap>Real robot manipulation</td>
<td nowrap>Reduce VLA failures caused by irrelevant visual perturbations during real-world deployment.</td>
<td nowrap><a href="https://ieeexplore.ieee.org/document/11128017/">paper</a></td>
<td nowrap><a href="https://aasherh.github.io/byovla/">project</a></td>
<td nowrap><a href="https://github.com/irom-princeton/byovla">code</a></td>
<td nowrap>-</td>
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
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.03480">SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning</a></td>
<td nowrap>SafeVLA aligns VLA policies with safety constraints through constrained reinforcement learning.</td>
<td nowrap>SPOC</td>
<td nowrap>AR</td>
<td nowrap>VLA / safety and robustness</td>
<td nowrap>PPO with constrained learning</td>
<td nowrap>On-policy / MF</td>
<td nowrap>Sim ✓ (ST)</td>
<td nowrap>Improve safety alignment of VLA policies before deployment.</td>
<td nowrap><a href="https://arxiv.org/abs/2503.03480">paper</a></td>
<td nowrap><a href="https://sites.google.com/view/pku-safevla">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
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
</tr>
</tbody>
</table>

### WAM / World Models

WAM combines future world-state prediction with action generation and fits naturally between agent planning and low-level control. Its value is not replacing every controller, but providing an intermediate layer for imagination, verification, and recovery.

Subdirections: cascaded WAM, joint WAM, video/latent world model, and world model for VLA.

Total: 70 papers.

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
<td nowrap>33</td>
<td nowrap>Look at the quality of future-video or latent-state prediction.</td>
</tr>
<tr>
<td nowrap>world model for VLA</td>
<td nowrap>10</td>
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
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ICRA 2025</td>
<td nowrap><a href="https://nvlabs.github.io/X-MOBILITY/">X-MOBILITY: End-To-End Generalizable Navigation via World Modeling</a></td>
<td nowrap>X-MOBILITY uses an autoregressive latent world model to separate world dynamics learning from action policy learning for zero-shot sim-to-real navigation.</td>
<td nowrap>navigation world model</td>
<td nowrap>latent future state</td>
<td nowrap>navigation action</td>
<td nowrap>navigation policy imagination</td>
<td nowrap>Sim + Real</td>
<td nowrap>Improve end-to-end navigation generalization and sim-to-real transfer through world modeling.</td>
<td nowrap><a href="https://nvlabs.github.io/X-MOBILITY/">paper</a></td>
<td nowrap><a href="https://nvlabs.github.io/X-MOBILITY/">project</a></td>
<td nowrap><a href="https://github.com/NVlabs/X-MOBILITY">code</a></td>
<td nowrap><a href="https://github.com/NVlabs/X-MOBILITY">data</a></td>
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
</tr>
</tbody>
</table>

#### video/latent world model

Total: 33 papers.

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
<th nowrap>Benchmark</th>
<th nowrap>Paper Task/Goal</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>CoRL 2025</td>
<td nowrap><a href="https://scholar.google.com/scholar?q=Gen2Act%3A+Human+Video+Generation+in+Novel+Scenarios+Enables+Generalizable+Robot+Manipulation">Gen2Act: Human Video Generation in Novel Scenarios Enables Generalizable Robot Manipulation</a></td>
<td nowrap>Gen2Act uses human video generation in novel scenarios to support generalizable robot manipulation.</td>
<td nowrap>world model</td>
<td nowrap>predicted/latent world state</td>
<td nowrap>robot action interface</td>
<td nowrap>world-model robot learning</td>
<td nowrap>robot benchmarks</td>
<td nowrap>Add CoRL world-model coverage.</td>
<td nowrap><a href="https://scholar.google.com/scholar?q=Gen2Act%3A+Human+Video+Generation+in+Novel+Scenarios+Enables+Generalizable+Robot+Manipulation">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>WAM / CoRL</td>
</tr>
<tr>
<td nowrap>CoRL 2024</td>
<td nowrap><a href="https://scholar.google.com/scholar?q=Flow+as+the+Cross-Domain+Manipulation+Interface">Flow as the Cross-Domain Manipulation Interface</a></td>
<td nowrap>Im2Flow2Act uses flow as a cross-domain interface between visual prediction and manipulation.</td>
<td nowrap>world model</td>
<td nowrap>predicted/latent world state</td>
<td nowrap>robot action interface</td>
<td nowrap>world-model robot learning</td>
<td nowrap>robot benchmarks</td>
<td nowrap>Add CoRL world-model coverage.</td>
<td nowrap><a href="https://scholar.google.com/scholar?q=Flow+as+the+Cross-Domain+Manipulation+Interface">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>WAM / CoRL</td>
</tr>
<tr>
<td nowrap>CoRL 2024</td>
<td nowrap><a href="https://scholar.google.com/scholar?q=Dreamitate%3A+Real-World+Visuomotor+Policy+Learning+via+Video+Generation">Dreamitate: Real-World Visuomotor Policy Learning via Video Generation</a></td>
<td nowrap>Dreamitate learns real-world visuomotor policies through video generation.</td>
<td nowrap>world model</td>
<td nowrap>predicted/latent world state</td>
<td nowrap>robot action interface</td>
<td nowrap>world-model robot learning</td>
<td nowrap>robot benchmarks</td>
<td nowrap>Add CoRL world-model coverage.</td>
<td nowrap><a href="https://scholar.google.com/scholar?q=Dreamitate%3A+Real-World+Visuomotor+Policy+Learning+via+Video+Generation">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>WAM / CoRL</td>
</tr>
<tr>
<td nowrap>CoRL 2025</td>
<td nowrap><a href="https://scholar.google.com/scholar?q=FLARE%3A+Robot+Learning+with+Implicit+World+Modeling">FLARE: Robot Learning with Implicit World Modeling</a></td>
<td nowrap>FLARE studies robot learning with implicit world modeling.</td>
<td nowrap>world model</td>
<td nowrap>predicted/latent world state</td>
<td nowrap>robot action interface</td>
<td nowrap>world-model robot learning</td>
<td nowrap>robot benchmarks</td>
<td nowrap>Add CoRL world-model coverage.</td>
<td nowrap><a href="https://scholar.google.com/scholar?q=FLARE%3A+Robot+Learning+with+Implicit+World+Modeling">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>WAM / CoRL</td>
</tr>
<tr>
<td nowrap>CoRL 2022</td>
<td nowrap><a href="https://arxiv.org/abs/2206.14176">DayDreamer: World Models for Physical Robot Learning</a></td>
<td nowrap>DayDreamer uses world models for physical robot learning.</td>
<td nowrap>world model</td>
<td nowrap>predicted/latent world state</td>
<td nowrap>robot action interface</td>
<td nowrap>world-model robot learning</td>
<td nowrap>robot benchmarks</td>
<td nowrap>Add CoRL world-model coverage.</td>
<td nowrap><a href="https://arxiv.org/abs/2206.14176">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>WAM, Awesome-VLA / CoRL</td>
</tr>
<tr>
<td nowrap>CoRL 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2508.03645">DiWA: Diffusion Policy Adaptation with World Models</a></td>
<td nowrap>DiWA adapts diffusion policies with world models.</td>
<td nowrap>world model</td>
<td nowrap>predicted/latent world state</td>
<td nowrap>robot action interface</td>
<td nowrap>world-model robot learning</td>
<td nowrap>robot benchmarks</td>
<td nowrap>Add CoRL world-model coverage.</td>
<td nowrap><a href="https://arxiv.org/abs/2508.03645">paper</a></td>
<td nowrap><a href="https://diwa.cs.uni-freiburg.de/">project</a></td>
<td nowrap><a href="https://github.com/acl21/diwa">code</a></td>
<td nowrap>-</td>
<td nowrap>EAI-VLA-VLN / CoRL</td>
</tr>
<tr>
<td nowrap>NeurIPS 2023</td>
<td nowrap><a href="https://arxiv.org/abs/2302.00111">Learning Universal Policies via Text-Guided Video Generation</a></td>
<td nowrap>This work learns policies by using text-guided video generation as an intermediate representation.</td>
<td nowrap>video/latent world model</td>
<td nowrap>text-guided generated video</td>
<td nowrap>video-conditioned action</td>
<td nowrap>policy learning from generated video</td>
<td nowrap>robot policy learning</td>
<td nowrap>robot manipulation tasks</td>
<td nowrap>Use generated videos as guidance for policy learning.</td>
<td nowrap><a href="https://arxiv.org/abs/2302.00111">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICLR 2024</td>
<td nowrap><a href="https://arxiv.org/abs/2310.10625">Video Language Planning</a></td>
<td nowrap>Video Language Planning uses video prediction and language goals to support planning.</td>
<td nowrap>video/latent world model</td>
<td nowrap>future video</td>
<td nowrap>language-conditioned plan/action</td>
<td nowrap>video-language planning</td>
<td nowrap>embodied planning</td>
<td nowrap>planning benchmarks</td>
<td nowrap>Plan with predicted video futures and language instructions.</td>
<td nowrap><a href="https://arxiv.org/abs/2310.10625">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=CKpqRFTRfc">MVISTA-4D: View-Consistent 4D World Model with Test-Time Action Inference for Robotic Manipulation</a></td>
<td nowrap>MVISTA-4D builds a view-consistent 4D world model and infers manipulation actions at test time.</td>
<td nowrap>video/latent world model</td>
<td nowrap>4D view-consistent world state</td>
<td nowrap>test-time action inference</td>
<td nowrap>4D world modeling</td>
<td nowrap>robot manipulation</td>
<td nowrap>robot manipulation benchmarks</td>
<td nowrap>Use 4D world prediction to infer robot actions.</td>
<td nowrap><a href="https://openreview.net/forum?id=CKpqRFTRfc">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICLR 2024</td>
<td nowrap><a href="https://arxiv.org/abs/2312.13139">Unleashing Large-Scale Video Generative Pre-training for Visual Robot Manipulation</a></td>
<td nowrap>This work transfers large-scale video generative pretraining to visual robot manipulation.</td>
<td nowrap>video/latent world model</td>
<td nowrap>pretrained video generative model</td>
<td nowrap>robot action head</td>
<td nowrap>video generative pretraining</td>
<td nowrap>visual robot manipulation</td>
<td nowrap>robot manipulation benchmarks</td>
<td nowrap>Leverage video generation pretraining for robot manipulation.</td>
<td nowrap><a href="https://arxiv.org/abs/2312.13139">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>NeurIPS 2024</td>
<td nowrap><a href="https://arxiv.org/abs/2411.18179">Prediction with Action: Visual Policy Learning via Joint Denoising Process</a></td>
<td nowrap>Prediction with Action jointly denoises future visual predictions and actions for policy learning.</td>
<td nowrap>video/latent world model</td>
<td nowrap>visual prediction latents</td>
<td nowrap>joint denoising action</td>
<td nowrap>joint video-action denoising</td>
<td nowrap>visual policy learning</td>
<td nowrap>robot policy benchmarks</td>
<td nowrap>Couple future prediction with action generation.</td>
<td nowrap><a href="https://arxiv.org/abs/2411.18179">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICLR 2025</td>
<td nowrap><a href="https://openreview.net/forum?id=3RSLW9YSgk">Dream to Manipulate: Compositional World Models Empowering Robot Imitation Learning with Imagination</a></td>
<td nowrap>Dream to Manipulate uses compositional world models to augment robot imitation learning with imagined rollouts.</td>
<td nowrap>video/latent world model</td>
<td nowrap>compositional imagined state</td>
<td nowrap>imitation action</td>
<td nowrap>world-model imagination</td>
<td nowrap>robot imitation learning</td>
<td nowrap>robot manipulation benchmarks</td>
<td nowrap>Use imagination to improve imitation learning.</td>
<td nowrap><a href="https://openreview.net/forum?id=3RSLW9YSgk">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>NeurIPS 2024</td>
<td nowrap><a href="https://proceedings.neurips.cc/paper_files/paper/2024/hash/6164b6e5352c139e9ddc1a98c09e4e4a-Abstract-Conference.html">PIVOT-R: Primitive-Driven Waypoint-Aware World Model for Robotic Manipulation</a></td>
<td nowrap>PIVOT-R uses primitive-driven waypoint-aware world modeling for robot manipulation.</td>
<td nowrap>video/latent world model</td>
<td nowrap>waypoint-aware predicted state</td>
<td nowrap>primitive action interface</td>
<td nowrap>world-model manipulation planning</td>
<td nowrap>robot manipulation</td>
<td nowrap>robot manipulation benchmarks</td>
<td nowrap>Predict waypoint-aware futures for manipulation primitives.</td>
<td nowrap><a href="https://proceedings.neurips.cc/paper_files/paper/2024/file/6164b6e5352c139e9ddc1a98c09e4e4a-Paper-Conference.pdf">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CVPR 2024</td>
<td nowrap><a href="https://openaccess.thecvf.com/content/CVPR2024/html/Wang_Driving_into_the_Future_Multiview_Visual_Forecasting_and_Planning_with_CVPR_2024_paper.html">Driving into the Future: Multiview Visual Forecasting and Planning with World Model for Autonomous Driving</a></td>
<td nowrap>This work uses multiview visual forecasting as a world model for autonomous-driving planning.</td>
<td nowrap>video/latent world model</td>
<td nowrap>multiview future video</td>
<td nowrap>driving plan/action</td>
<td nowrap>visual forecasting + planning</td>
<td nowrap>autonomous driving</td>
<td nowrap>driving benchmarks</td>
<td nowrap>Use future visual prediction to support driving plans.</td>
<td nowrap><a href="https://arxiv.org/abs/2311.17918">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>NeurIPS 2023</td>
<td nowrap><a href="https://proceedings.neurips.cc/paper_files/paper/2023/file/d9042abf40782fbce28901c1c9c0e8d8-Paper-Conference.pdf">Video Prediction Models as Rewards for Reinforcement Learning</a></td>
<td nowrap>This paper uses video prediction models to define rewards for reinforcement learning.</td>
<td nowrap>video/latent world model</td>
<td nowrap>predicted video</td>
<td nowrap>RL reward signal</td>
<td nowrap>video-prediction reward</td>
<td nowrap>reinforcement learning</td>
<td nowrap>RL benchmarks</td>
<td nowrap>Use video prediction quality as a reward signal.</td>
<td nowrap><a href="https://proceedings.neurips.cc/paper_files/paper/2023/file/d9042abf40782fbce28901c1c9c0e8d8-Paper-Conference.pdf">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ECCV 2024</td>
<td nowrap><a href="https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05914.pdf">Diffusion Reward: Learning Rewards via Conditional Video Diffusion</a></td>
<td nowrap>Diffusion Reward learns reward functions through conditional video diffusion.</td>
<td nowrap>video/latent world model</td>
<td nowrap>conditional generated video</td>
<td nowrap>reward signal</td>
<td nowrap>diffusion reward learning</td>
<td nowrap>reinforcement learning</td>
<td nowrap>RL/video benchmarks</td>
<td nowrap>Learn rewards through conditional video diffusion.</td>
<td nowrap><a href="https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05914.pdf">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2512.00961">Goal-Driven Reward by Video Diffusion Models for Reinforcement Learning</a></td>
<td nowrap>This work derives goal-driven rewards from video diffusion models for reinforcement learning.</td>
<td nowrap>video/latent world model</td>
<td nowrap>goal-conditioned video diffusion</td>
<td nowrap>reward signal</td>
<td nowrap>video diffusion reward</td>
<td nowrap>reinforcement learning</td>
<td nowrap>RL benchmarks</td>
<td nowrap>Use video diffusion models to shape goal-driven RL rewards.</td>
<td nowrap><a href="https://arxiv.org/abs/2512.00961">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICLR 2024</td>
<td nowrap><a href="https://arxiv.org/abs/2310.06114">Learning Interactive Real-World Simulators</a></td>
<td nowrap>This work learns interactive real-world simulators that can support action-conditioned prediction.</td>
<td nowrap>video/latent world model</td>
<td nowrap>interactive simulator state</td>
<td nowrap>action-conditioned simulation</td>
<td nowrap>learned world simulator</td>
<td nowrap>interactive environment modeling</td>
<td nowrap>simulation benchmarks</td>
<td nowrap>Learn action-conditioned simulators from real-world data.</td>
<td nowrap><a href="https://arxiv.org/abs/2310.06114">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICML 2024</td>
<td nowrap><a href="https://arxiv.org/abs/2402.15391">Genie: Generative Interactive Environments</a></td>
<td nowrap>Genie learns generative interactive environments from video and supports controllable latent actions.</td>
<td nowrap>video/latent world model</td>
<td nowrap>interactive video latent state</td>
<td nowrap>latent action</td>
<td nowrap>generative interactive world model</td>
<td nowrap>interactive environment modeling</td>
<td nowrap>video/game environments</td>
<td nowrap>Build controllable interactive environments from videos.</td>
<td nowrap><a href="https://arxiv.org/abs/2402.15391">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>IROS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.19842">ManiGaussian++: General Robotic Bimanual Manipulation with Hierarchical Gaussian World Model</a></td>
<td nowrap>ManiGaussian++ uses a hierarchical Gaussian world model to represent spatial state and interaction dynamics in bimanual manipulation.</td>
<td nowrap>Gaussian world model</td>
<td nowrap>hierarchical 3D Gaussian state</td>
<td nowrap>bimanual action</td>
<td nowrap>bimanual manipulation prediction</td>
<td nowrap>Sim + Real</td>
<td nowrap>-</td>
<td nowrap>Support general bimanual manipulation with a hierarchical 3D world model.</td>
<td nowrap><a href="https://arxiv.org/abs/2506.19842">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/April-Yz/ManiGaussian_bimanual">code</a></td>
<td nowrap>-</td>
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
<td nowrap>-</td>
<td nowrap>Address lack of explicit 3D grounding and spatial consistency in video world models.</td>
<td nowrap><a href="https://openreview.net/forum?id=3q9vHEqsNx">paper</a></td>
<td nowrap><a href="https://fantasy-amap.github.io/fantasy-world/">project</a></td>
<td nowrap><a href="https://github.com/Fantasy-AMAP/fantasy-world">code</a></td>
<td nowrap>-</td>
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
<td nowrap>-</td>
<td nowrap>Address fragmentation among 3D scene understanding tasks and the difficulty of sharing representations and transfer.</td>
<td nowrap><a href="https://openreview.net/forum?id=NQq9JLMfNN">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
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
<td nowrap>-</td>
<td nowrap>Address traditional world models requiring large amounts of domain-specific training and producing coarse predictions.</td>
<td nowrap><a href="https://openreview.net/forum?id=pFyzqbUiF9">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
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
<td nowrap>-</td>
<td nowrap>Address exocentric-to-egocentric conversion relying on synchronized multi-view data, camera poses, or initial egocentric frames.</td>
<td nowrap><a href="https://openreview.net/forum?id=wcTuZG9P2o">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
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
<td nowrap>-</td>
<td nowrap>Address controllability, temporal consistency, and standardized evaluation in autonomous-driving LiDAR world generation.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38905">paper</a></td>
<td nowrap><a href="https://lidarcrafter.github.io/">project</a></td>
<td nowrap><a href="https://github.com/worldbench/LiDARCrafter">code</a></td>
<td nowrap>nuScenes + scene/object/sequence metrics + HuggingFace weights</td>
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
<td nowrap>-</td>
<td nowrap>Address insufficient data coverage, scarce action labels, and difficulty simulating contact-rich tasks in robot world models.</td>
<td nowrap><a href="https://arxiv.org/abs/2602.06949">paper</a></td>
<td nowrap><a href="https://dreamdojo-world.github.io/">project</a></td>
<td nowrap><a href="https://github.com/NVIDIA/DreamDojo">code</a></td>
<td nowrap><a href="https://huggingface.co/nvidia/DreamDojo">hf</a></td>
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
<td nowrap>-</td>
<td nowrap>Address the difficulty of stably converting visually realistic generated future video frames into control actions.</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66091">paper</a></td>
<td nowrap><a href="https://logosroboticsgroup.github.io/MoLA/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
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
<td nowrap>-</td>
<td nowrap>Address insufficient joint modeling of visual imagination and action prediction in generalizable robotic manipulation.</td>
<td nowrap><a href="https://openreview.net/forum?id=UPHlqbZFZB">paper</a></td>
<td nowrap><a href="https://videovla-nips2025.github.io/">project</a></td>
<td nowrap><a href="https://github.com/VideoVLA-Project/VideoVLA">code</a></td>
<td nowrap>SIMPLER, OXE, Realman real-world eval</td>
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
<td nowrap>-</td>
<td nowrap>Address long-horizon future-space modeling, 3D grounding, and sim-to-real gaps in robotic manipulation.</td>
<td nowrap><a href="https://arxiv.org/abs/2501.01895">paper</a></td>
<td nowrap><a href="https://sites.google.com/view/enerverse">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
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
<td nowrap>-</td>
<td nowrap>Address redundant information in VLA image prediction and lack of key world knowledge.</td>
<td nowrap><a href="https://arxiv.org/abs/2507.04447">paper</a></td>
<td nowrap><a href="https://zhangwenyao1.github.io/DreamVLA/index.html">project</a></td>
<td nowrap><a href="https://github.com/Zhangwenyao1/DreamVLA">code</a></td>
<td nowrap><a href="https://huggingface.co/WenyaoZhang/DreamVLA">hf</a></td>
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
<td nowrap>-</td>
<td nowrap>Address static visual encoders ignoring dynamic information needed for embodied tasks.</td>
<td nowrap><a href="https://arxiv.org/abs/2412.14803">paper</a></td>
<td nowrap><a href="https://video-prediction-policy.github.io/">project</a></td>
<td nowrap><a href="https://github.com/roboterax/video-prediction-policy">code</a></td>
<td nowrap>-</td>
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
<td nowrap>-</td>
<td nowrap>Address insufficient robot imitation-learning quality caused by inconsistent viewpoints and interaction misalignment in hand-object interaction videos.</td>
<td nowrap><a href="https://arxiv.org/abs/2503.11423">paper</a></td>
<td nowrap><a href="https://taste-rob.github.io/">project</a></td>
<td nowrap><a href="https://github.com/GAP-LAB-CUHK-SZ/TASTE-Rob">code</a></td>
<td nowrap>TASTE-Rob 100,856 videos</td>
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
<td nowrap>-</td>
<td nowrap>Address the high cost of action-labeled robot data and the difficulty of learning skills from cross-embodiment videos.</td>
<td nowrap><a href="https://cvpr.thecvf.com/virtual/2025/poster/34942">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
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
</tr>
<tr>
<td nowrap>ICRA 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2509.22643">VLA-Reasoner: Reinforcing Robotic Reasoning and Generalization with World Model</a></td>
<td nowrap>VLA-Reasoner adds test-time long-horizon reasoning to existing VLAs through world-model rollouts and online MCTS.</td>
<td nowrap>world model for VLA</td>
<td nowrap>predicted future states</td>
<td nowrap>VLA action candidates</td>
<td nowrap>test-time search and verification</td>
<td nowrap>Sim + Real</td>
<td nowrap>Search future outcomes with a world model before executing actions.</td>
<td nowrap><a href="https://arxiv.org/abs/2509.22643">paper</a></td>
<td nowrap><a href="https://vla-reasoner.github.io/">project</a></td>
<td nowrap><a href="https://github.com/wkguo/VLA-Reasoner">code</a></td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICRA 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.10370">LUMOS: Language-Conditioned Imitation Learning with World Models</a></td>
<td nowrap>LUMOS practices language-conditioned long-horizon manipulation offline in a learned world-model latent space before transferring to real robots.</td>
<td nowrap>world model for VLA</td>
<td nowrap>latent world state</td>
<td nowrap>language-conditioned action</td>
<td nowrap>offline practice / imitation learning</td>
<td nowrap>Sim + Real</td>
<td nowrap>Use world-model practice to reduce real-robot data requirements.</td>
<td nowrap><a href="https://arxiv.org/abs/2503.10370">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
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
</tr>
</tbody>
</table>

### Agentic Planning / Reasoning and Planning

This direction emphasizes task decomposition, memory, failure monitoring, constraint/affordance planning, and self-improving planning. It is closest to the practical system route of agent planning plus smaller execution modules.

Subdirections: task decomposition, memory, failure monitor, constraint / affordance planning, and self-improving planning.

Total: 103 papers.

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
<td nowrap>40</td>
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
<td nowrap>11</td>
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

Total: 40 papers.

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
</tr>
</thead>
<tbody>
<tr>
<td nowrap>CoRL 2022</td>
<td nowrap><a href="https://arxiv.org/abs/2204.01691">Do As I Can, Not As I Say: Grounding Language in Robotic Affordances</a></td>
<td nowrap>SayCan grounds language-model plans in robotic affordance estimates.</td>
<td nowrap>Task Decomposition</td>
<td nowrap>language/scene context</td>
<td nowrap>execution feedback</td>
<td nowrap>robot action interface</td>
<td nowrap>embodied benchmarks</td>
<td nowrap>Add CoRL planning coverage.</td>
<td nowrap><a href="https://arxiv.org/abs/2204.01691">paper</a></td>
<td nowrap><a href="https://say-can.github.io">project</a></td>
<td nowrap><a href="https://github.com/google-research/google-research/tree/master/saycan">code</a></td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CoRL 2023</td>
<td nowrap><a href="https://scholar.google.com/scholar?q=SayPlan%3A+Grounding+Large+Language+Models+using+3D+Scene+Graphs+for+Scalable+Task+Planning">SayPlan: Grounding Large Language Models using 3D Scene Graphs for Scalable Task Planning</a></td>
<td nowrap>SayPlan grounds LLM task planning with 3D scene graphs.</td>
<td nowrap>Task Decomposition</td>
<td nowrap>language/scene context</td>
<td nowrap>execution feedback</td>
<td nowrap>robot action interface</td>
<td nowrap>embodied benchmarks</td>
<td nowrap>Add CoRL planning coverage.</td>
<td nowrap><a href="https://scholar.google.com/scholar?q=SayPlan%3A+Grounding+Large+Language+Models+using+3D+Scene+Graphs+for+Scalable+Task+Planning">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CoRL 2022</td>
<td nowrap><a href="https://scholar.google.com/scholar?q=Inner+Monologue%3A+Embodied+Reasoning+through+Planning+with+Language+Models">Inner Monologue: Embodied Reasoning through Planning with Language Models</a></td>
<td nowrap>Inner Monologue uses language-model planning and embodied feedback for robot reasoning.</td>
<td nowrap>Task Decomposition</td>
<td nowrap>language/scene context</td>
<td nowrap>execution feedback</td>
<td nowrap>robot action interface</td>
<td nowrap>embodied benchmarks</td>
<td nowrap>Add CoRL planning coverage.</td>
<td nowrap><a href="https://scholar.google.com/scholar?q=Inner+Monologue%3A+Embodied+Reasoning+through+Planning+with+Language+Models">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CoRL 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2509.08820">RoboChemist: Long-Horizon and Safety-Compliant Robotic Chemical Experimentation</a></td>
<td nowrap>RoboChemist plans long-horizon, safety-compliant robotic chemical experiments.</td>
<td nowrap>Task Decomposition</td>
<td nowrap>language/scene context</td>
<td nowrap>execution feedback</td>
<td nowrap>robot action interface</td>
<td nowrap>embodied benchmarks</td>
<td nowrap>Add CoRL planning coverage.</td>
<td nowrap><a href="https://arxiv.org/abs/2509.08820">paper</a></td>
<td nowrap><a href="https://zzongzheng0918.github.io/RoboChemist.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://openaccess.thecvf.com/content/CVPR2025/html/Yang_Magma_A_Foundation_Model_for_Multimodal_AI_Agents_CVPR_2025_paper.html">Magma: A Foundation Model for Multimodal AI Agents</a></td>
<td nowrap>Magma provides a multimodal foundation model for agents that need perception, reasoning, and action.</td>
<td nowrap>Task Decomposition</td>
<td nowrap>multimodal foundation model</td>
<td nowrap>agent feedback</td>
<td nowrap>agent action interface</td>
<td nowrap>multimodal agent benchmarks</td>
<td nowrap>Build a foundation model for multimodal agent tasks.</td>
<td nowrap><a href="https://openaccess.thecvf.com/content/CVPR2025/papers/Yang_Magma_A_Foundation_Model_for_Multimodal_AI_Agents_CVPR_2025_paper.pdf">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICML 2024</td>
<td nowrap><a href="https://proceedings.mlr.press/v235/huang24ae.html">LEO: Embodied Generalist Agent in 3D World</a></td>
<td nowrap>LEO is an embodied generalist agent for 3D-world understanding, reasoning, and task execution.</td>
<td nowrap>Task Decomposition</td>
<td nowrap>3D embodied memory</td>
<td nowrap>instruction feedback</td>
<td nowrap>embodied agent action</td>
<td nowrap>3D embodied benchmarks</td>
<td nowrap>Unify 3D perception and embodied instruction following.</td>
<td nowrap><a href="https://proceedings.mlr.press/v235/huang24ae/huang24ae.pdf">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CVPR 2024</td>
<td nowrap><a href="https://openaccess.thecvf.com/content/CVPR2024/html/Majumdar_OpenEQA_Embodied_Question_Answering_in_the_Era_of_Foundation_Models_CVPR_2024_paper.html">OpenEQA: Embodied Question Answering in the Era of Foundation Models</a></td>
<td nowrap>OpenEQA benchmarks embodied question answering with foundation models in real and simulated scenes.</td>
<td nowrap>Task Decomposition</td>
<td nowrap>scene memory + QA context</td>
<td nowrap>benchmark feedback</td>
<td nowrap>embodied QA interface</td>
<td nowrap>OpenEQA benchmark</td>
<td nowrap>Evaluate foundation models on embodied scene questions.</td>
<td nowrap><a href="https://openaccess.thecvf.com/content/CVPR2024/papers/Majumdar_OpenEQA_Embodied_Question_Answering_in_the_Era_of_Foundation_Models_CVPR_2024_paper.pdf">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>EMNLP 2025</td>
<td nowrap><a href="https://aclanthology.org/2025.emnlp-industry.149/">VestaBench: An Embodied Benchmark for Safe Long-Horizon Planning Under Multi-Constraint and Adversarial Settings</a></td>
<td nowrap>VestaBench evaluates safe long-horizon embodied planning under constraints and adversarial settings.</td>
<td nowrap>Task Decomposition</td>
<td nowrap>constraint-aware benchmark state</td>
<td nowrap>safety feedback</td>
<td nowrap>planner action interface</td>
<td nowrap>VestaBench</td>
<td nowrap>Benchmark safe long-horizon planning with multiple constraints.</td>
<td nowrap><a href="https://aclanthology.org/2025.emnlp-industry.149.pdf">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>NeurIPS 2024</td>
<td nowrap><a href="https://openreview.net/forum?id=iSwK1YqO7v">Embodied Agent Interface: Benchmarking LLMs for Embodied Decision Making</a></td>
<td nowrap>EAI benchmarks LLM decision making through a standardized embodied-agent interface.</td>
<td nowrap>Task Decomposition</td>
<td nowrap>agent interface context</td>
<td nowrap>benchmark feedback</td>
<td nowrap>embodied decision interface</td>
<td nowrap>EAI benchmark</td>
<td nowrap>Measure how LLMs make embodied decisions through a common interface.</td>
<td nowrap><a href="https://openreview.net/forum?id=iSwK1YqO7v">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>IROS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2406.11818">Embodied Instruction Following in Unknown Environments</a></td>
<td nowrap>EIF decomposes natural-language tasks into explorable and executable high-level plans in unknown household environments.</td>
<td nowrap>Task Decomposition</td>
<td nowrap>multimodal LLM planner</td>
<td nowrap>visual feedback + exploration</td>
<td nowrap>navigation and interaction policy</td>
<td nowrap>house-level scenes</td>
<td nowrap>Support long-horizon embodied instruction following in unknown environments.</td>
<td nowrap><a href="https://arxiv.org/abs/2406.11818">paper</a></td>
<td nowrap><a href="https://gary3410.github.io/eif_unknown/">project</a></td>
<td nowrap><a href="https://github.com/Gary3410/eif_unknown">code</a></td>
<td nowrap>-</td>
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
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38896">GraphCoT-VLA: A 3D Spatial-Aware Reasoning Vision-Language-Action Model for Robotic Manipulation with Ambiguous Instructions</a></td>
<td nowrap>Uses 3D spatial graph Chain-of-Thought reasoning to resolve ambiguous manipulation instructions into robust VLA actions.</td>
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
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38900">PhyPlan: Learning to Plan Tasks with Generalizable and Rapid Physical Reasoning for Embodied Manipulation</a></td>
<td nowrap>Learns fast generalizable physical reasoning for planning multi-step embodied manipulation tasks.</td>
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
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38906">Cook and Clean Together: Teaching Embodied Agents for Parallel Task Execution</a></td>
<td nowrap>Trains embodied agents to schedule and coordinate parallel subtasks for faster household task execution.</td>
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
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38911">FoAM: Foresight-Augmented Multi-Task Imitation Policy for Robotic Manipulation</a></td>
<td nowrap>Adds foresight about likely future states to multi-task imitation policies for more reliable robotic manipulation.</td>
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
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38936">Zero-Shot Robotic Manipulation via 3D Gaussian Splatting-Enhanced Multimodal Retrieval-Augmented Generation</a></td>
<td nowrap>Grounds zero-shot robotic manipulation by combining multimodal retrieval with 3D Gaussian Splatting scene representations.</td>
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
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38958">H-GAR: A Hierarchical Interaction Framework via Goal-Driven Observation-Action Refinement for Robotic Manipulation</a></td>
<td nowrap>Refines observations and actions hierarchically from goal cues to produce temporally coherent manipulation behavior.</td>
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
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/60500">TapSampling: Inference-Time Sampling with a Task-Progress-Understanding Verifier for Robotic Manipulation</a></td>
<td nowrap>Filters inference-time action samples with a task-progress verifier to select more successful manipulation rollouts.</td>
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
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/63250">Decompose and Recompose: Reasoning New Skills from Existing Abilities for Cross-Task Robotic Manipulation</a></td>
<td nowrap>Builds new manipulation skills by decomposing existing abilities and recomposing them for unseen cross-task goals.</td>
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
</tr>
</thead>
<tbody>
<tr>
<td nowrap>IROS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2410.11989">Dynamic Open-Vocabulary 3D Scene Graphs for Long-Term Language-Guided Mobile Manipulation</a></td>
<td nowrap>DovSG uses dynamic open-vocabulary 3D scene graphs to support long-term language tasks, environment updates, and mobile manipulation.</td>
<td nowrap>Memory Planning</td>
<td nowrap>dynamic 3D scene graph</td>
<td nowrap>long-term scene updates</td>
<td nowrap>mobile manipulation planner</td>
<td nowrap>Real robot</td>
<td nowrap>Maintain long-term task memory with open-vocabulary scene graphs.</td>
<td nowrap><a href="https://arxiv.org/abs/2410.11989">paper</a></td>
<td nowrap><a href="https://bjhyzj.github.io/dovsg-web/">project</a></td>
<td nowrap><a href="https://github.com/BJHYZJ/DovSG">code</a></td>
<td nowrap>-</td>
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
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=E5L43l5EIu">Embodied Agents Meet Personalization: Investigating Challenges and Solutions Through the Lens of Memory Utilization</a></td>
<td nowrap>Studies how memory enables personalized embodied assistance and organizes user-specific preferences and routines for future tasks.</td>
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
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/60897">HiMe: Hierarchical Embodied Memory for Long-Horizon Vision-Language-Action Control</a></td>
<td nowrap>Uses hierarchical embodied memory to coordinate planning, monitoring, and execution in long-horizon VLA control.</td>
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
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66214">Spatial Memory for Out-of-Vision Manipulation in Vision-Language-Action</a></td>
<td nowrap>Maintains spatial-semantic memory of unseen objects so VLA policies can manipulate targets outside the current view.</td>
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
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/1915">Towards Long-Horizon Vision-Language-Action System: Reasoning, Acting and Memory</a></td>
<td nowrap>Connects reasoning, action execution, and memory to support long-horizon VLA behavior in dynamic environments.</td>
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
</tr>
</thead>
<tbody>
<tr>
<td nowrap>ICRA 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2510.16281">Do What You Say: Grounding Language-Conditioned Robotic Actions with Vision-Language Models</a></td>
<td nowrap>This method checks at runtime whether a VLA's textual reasoning matches its action outcome before deciding whether to execute the action.</td>
<td nowrap>Failure Monitor</td>
<td nowrap>VLM reasoning checker</td>
<td nowrap>reasoning-action consistency</td>
<td nowrap>VLA action selection</td>
<td nowrap>Real robot manipulation</td>
<td nowrap>Detect whether the stated plan and executed action are consistent.</td>
<td nowrap><a href="https://arxiv.org/abs/2510.16281">paper</a></td>
<td nowrap><a href="https://yilin-wu98.github.io/steering-reasoning-vla/">project</a></td>
<td nowrap><a href="https://github.com/NVlabs/actalign">code</a></td>
<td nowrap><a href="https://github.com/NVlabs/actalign">data</a></td>
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
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61750">Sentinel-VLA: A Metacognitive VLA Model with Active Status Monitoring for Dynamic Reasoning and Error Recovery</a></td>
<td nowrap>Adds active status monitoring so a VLA model can detect execution problems and trigger recovery reasoning.</td>
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
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/63650">NeurVLA: Unleashing Failure-Handling Capability of Vision-Language-Action Models via Neural-Symbolic Reasoning</a></td>
<td nowrap>Uses neural-symbolic reasoning to diagnose failures and improve recovery behavior in VLA manipulation policies.</td>
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
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64203">Can VLMs Diagnose and Recover from VLA Manipulation Faults?</a></td>
<td nowrap>Evaluates whether VLMs can diagnose manipulation faults and guide recovery for failed VLA executions.</td>
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
</tr>
</tbody>
</table>

#### constraint / affordance planning

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
</tr>
</thead>
<tbody>
<tr>
<td nowrap>CoRL 2023</td>
<td nowrap><a href="https://arxiv.org/abs/2307.05973">VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models</a></td>
<td nowrap>VoxPoser composes 3D value maps from language models for manipulation planning.</td>
<td nowrap>Task Decomposition</td>
<td nowrap>language/scene context</td>
<td nowrap>execution feedback</td>
<td nowrap>robot action interface</td>
<td nowrap>embodied benchmarks</td>
<td nowrap>Add CoRL planning coverage.</td>
<td nowrap><a href="https://arxiv.org/abs/2307.05973">paper</a></td>
<td nowrap><a href="https://voxposer.github.io">project</a></td>
<td nowrap><a href="https://github.com/huangwl18/VoxPoser">code</a></td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICRA 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2408.14769">Points2Plans: From Point Clouds to Long-Horizon Plans with Composable Relational Dynamics</a></td>
<td nowrap>Points2Plans connects high-level plans with continuous parameter planning from point clouds and language instructions through relational dynamics.</td>
<td nowrap>Constraint / Affordance Planning</td>
<td nowrap>point-cloud relational dynamics</td>
<td nowrap>composable planning feedback</td>
<td nowrap>continuous parameter planner</td>
<td nowrap>Sim + Real</td>
<td nowrap>Ground language plans in executable 3D relational dynamics constraints.</td>
<td nowrap><a href="https://arxiv.org/abs/2408.14769">paper</a></td>
<td nowrap><a href="https://sites.google.com/stanford.edu/points2plans">project</a></td>
<td nowrap><a href="https://github.com/yixuanhuang98/Points2Plans">code</a></td>
<td nowrap>-</td>
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
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38907">A3D: Adaptive Affordance Assembly with Dual-Arm Manipulation</a></td>
<td nowrap>Learns adaptive affordances for dual-arm assembly, updating manipulation choices as object and task states change.</td>
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
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38909">Affordance-Guided Coarse-to-Fine Exploration for Base Placement in Open-Vocabulary Mobile Manipulation</a></td>
<td nowrap>Guides mobile-manipulator base placement with affordance priors followed by coarse-to-fine feasibility refinement.</td>
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
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38955">Gentle Manipulation Policy Learning via Demonstrations from VLM Planned Atomic Skills</a></td>
<td nowrap>Uses VLM-planned atomic skills as demonstrations to learn policies for gentle long-horizon manipulation.</td>
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
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38922">ManipLVM-R1: Reinforcement Learning for Reasoning in Embodied Manipulation with Large Vision-Language Models</a></td>
<td nowrap>Applies reinforcement learning to improve large vision-language models on affordance reasoning and embodied manipulation planning.</td>
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
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61922">HALO: A Unified Vision-Language-Action Model for Embodied Multimodal Chain-of-Thought Reasoning</a></td>
<td nowrap>Unifies language reasoning, visual prediction, and action generation as multimodal Chain-of-Thought for embodied VLA control.</td>
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
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61887">LaST0: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model</a></td>
<td nowrap>Represents reasoning as latent spatiotemporal Chain-of-Thought to improve robotic VLA planning with lower explicit reasoning cost.</td>
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
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/60801">LAGEA: Language Guided Embodied Agents for Robotic Manipulation</a></td>
<td nowrap>Uses language guidance and feedback to adapt embodied manipulation agents across tasks.</td>
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
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64055">Drift is a Sampling Error: SNR-Aware Power Distributions for Long-Horizon Robotic Planning</a></td>
<td nowrap>Frames planning drift as an inference-time sampling issue and uses SNR-aware power distributions for long-horizon planning.</td>
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
</tr>
<tr>
<td nowrap>ICML 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2410.01440">Closed-Loop Long-Horizon Robotic Planning via Equilibrium Sequence Modeling</a></td>
<td nowrap>Uses equilibrium sequence modeling to iteratively refine plans under feedback for closed-loop long-horizon robot planning.</td>
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
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://cvpr.thecvf.com/virtual/2025/poster/33233">CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models</a></td>
<td nowrap>Predicts visual Chain-of-Thought subgoals before actions to improve temporal reasoning and generalization in VLA models.</td>
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
</tr>
</tbody>
</table>

### Embodiment Expansion / Dexterous Manipulation

Embodiment expansion determines whether embodied AI can move beyond single-arm systems toward humanoids, bimanual robots, dexterous hands, and tactile/contact-rich tasks. These papers show how action spaces, sensing, and control objectives become more complex as the body changes.

Subdirections: humanoid, bimanual, dexterous hand, and tactile/contact-rich.

> [!TIP]
> Tables in this section combine a fixed total width with explicit per-column widths. Short metadata columns stay on one line; long analytical columns wrap within their assigned width. GitHub keeps the table horizontally scrollable on narrow screens.

Total: 159 papers.

<table width="960">
<thead>
<tr>
<th width="150" nowrap>Subdirection</th>
<th width="90" nowrap>Entries</th>
<th width="720">Focus</th>
</tr>
</thead>
<tbody>
<tr>
<td width="150" nowrap>humanoid</td>
<td width="90" nowrap>78</td>
<td width="720">Focus on whole-body control, mobile manipulation, and humanoid embodiment generalization.</td>
</tr>
<tr>
<td width="150" nowrap>bimanual</td>
<td width="90" nowrap>13</td>
<td width="720">Focus on bimanual coordination, long-horizon manipulation, and coordinated control.</td>
</tr>
<tr>
<td width="150" nowrap>dexterous hand</td>
<td width="90" nowrap>40</td>
<td width="720">Focus on dexterous-hand action spaces and grasp transfer.</td>
</tr>
<tr>
<td width="150" nowrap>tactile/contact-rich</td>
<td width="90" nowrap>28</td>
<td width="720">Focus on tactile sensing, contact dynamics, and fine-grained feedback.</td>
</tr>
</tbody>
</table>

#### Humanoid & Biped Hardware Reference

This section now serves only as a hardware index: Unitree and AgiBot biped models, lab-built platforms, and body-to-hand or body-to-gripper configurations. Papers are no longer duplicated in a separate table here. Venue, method, exact embodiment, evaluation setting, solved problem, current bottleneck, and future direction are consolidated into the single **humanoid paper master table** below. Specifications were checked through **2026-07-10**.

> [!IMPORTANT]
> “Body DoF” excludes optional end effectors unless a vendor explicitly reports a complete-system total. The biped tables intentionally exclude wheeled or fixed-base systems such as Unitree G1-D/R1-D/H2-D and AgiBot A2-W/G1/G2. `Sim Only` in the paper table means that only a robot model or URDF was used; it does not imply physical deployment.

##### Unitree biped models and specifications

<table width="1460">
<thead>
<tr>
<th width="170" nowrap>Model / role</th>
<th width="150">Height / weight</th>
<th width="150">Body DoF</th>
<th width="300">Joint, payload, and speed</th>
<th width="170">Battery / endurance</th>
<th width="300">Perception and compute</th>
<th width="220">Dexterous-hand form</th>
</tr>
</thead>
<tbody>
<tr>
<td width="170" nowrap><a href="https://www.unitree.com/h1/">H1</a><br>First full-size general humanoid</td>
<td width="150">About 180 cm / 47 kg</td>
<td width="150">Official total 19; 5 per leg and 4 per arm, expandable</td>
<td width="300">Knee about 360 N·m, hip 220 N·m, ankle 59 N·m, arm 75 N·m; listed speed 3.3 m/s</td>
<td width="170">15 Ah / 0.864 kWh, quick-release; no hourly endurance published</td>
<td width="300">3D LiDAR + depth camera; i5 platform PC + i7 development PC, optional i7/Orin NX</td>
<td width="220">Optional; no standard hand model specified</td>
</tr>
<tr>
<td width="170" nowrap><a href="https://www.unitree.com/h1/">H1-2</a><br>Higher-DoF whole-body manipulation version</td>
<td width="150">About 178 cm / 70 kg</td>
<td width="150">27; 6 per leg and 7 per arm</td>
<td width="300">Leg peak 360 N·m; shoulder/elbow about 120 N·m, wrist 30 N·m; arm payload about 21 kg peak / 7 kg rated; speed &lt;2 m/s</td>
<td width="170">15 Ah / 0.864 kWh, quick-release</td>
<td width="300">3D LiDAR + depth camera; i5+i7, with up to three optional Orin NX modules</td>
<td width="220">Dex5-1 or other dexterous hands explicitly optional</td>
</tr>
<tr>
<td width="170" nowrap><a href="https://www.unitree.com/g1/">G1 / G1 EDU</a><br>Compact research and education platform</td>
<td width="150">132 cm / about 35 kg, 35 kg+</td>
<td width="150">23 / 23–43; 6 per leg and 5 per arm; EDU can add waist, wrists, and hands</td>
<td width="300">Maximum knee torque 90 / 120 N·m; arm payload about 2 / 3 kg; current parameter table does not list speed</td>
<td width="170">9000 mAh quick-release battery; about 2 h</td>
<td width="300">Depth camera + 3D LiDAR; 8-core CPU, optional Orin on EDU</td>
<td width="220">None on base model; EDU can add a 7-DoF Dex3-1 per hand and 2-DoF wrists</td>
</tr>
<tr>
<td width="170" nowrap><a href="https://www.unitree.com/R1/">R1 AIR / R1 / R1 EDU</a><br>Ultra-light, lower-cost platform</td>
<td width="150">123 cm / about 27, 29, 29 kg</td>
<td width="150">20 / 26 / 26–40; 6 per leg and 4/5/5 per arm</td>
<td width="300">Arm payload about 2 kg; joint torque and mobility speed not published</td>
<td width="170">Quick-release lithium battery; about 1 h</td>
<td width="300">8-core processor; monocular on AIR, binocular on R1/EDU; optional 40–100 TOPS Orin on EDU</td>
<td width="220">Only EDU explicitly supports an optional dexterous hand</td>
</tr>
<tr>
<td width="170" nowrap><a href="https://www.unitree.com/H2/">H2 / H2 EDU</a><br>Full-size humanoid with a human-like head</td>
<td width="150">182 cm / about 70 kg</td>
<td width="150">31: 6 per leg, 7 per arm, 3 waist, 2 head</td>
<td width="300">Arm/leg peak torque 120/360 N·m; arm payload about 15 kg peak / 7 kg rated; speed not published</td>
<td width="170">15 Ah / 0.972 kWh; about 3 h</td>
<td width="300">Wide-FOV binocular camera; i5 on H2, additional i7 and optional Thor on EDU</td>
<td width="220">None on H2; multiple hand options on H2 EDU</td>
</tr>
<tr>
<td width="170" nowrap><a href="https://www.unitree.com/H2plus/">H2 Plus</a><br>NVIDIA Isaac GR00T full-stack research configuration</td>
<td width="150">182 cm / about 70 kg</td>
<td width="150">31 body DoF; 75 total with both hands</td>
<td width="300">Arm/leg peak torque 120/360 N·m; arm payload about 15 kg peak / 7 kg rated</td>
<td width="170">0.972 kWh; about 3 h</td>
<td width="300">i5+i7 + Jetson T5000; detailed page lists 2070 TFLOPS FP4 sparse and 128 GB unified memory; head stereo and optional wrist cameras</td>
<td width="220">Dual SharpaWave five-finger tactile hands, 22 active DoF each; 75 DoF system total</td>
</tr>
</tbody>
</table>

Scope notes: the R1 page labels a value of about 2 kg as “Arm Joint Torque,” but its footnote describes arm payload, so the table records payload and treats torque as unpublished. The H2 hero-page phrase “2070 TOPS” must also not be merged with the H2 Plus detailed specification of “2070 TFLOPS (FP4 sparse)” as if they were the same metric.

##### AgiBot biped models and specifications

<table width="1330">
<thead>
<tr>
<th width="170" nowrap>Model / status</th>
<th width="150">Height / weight</th>
<th width="130">Active DoF</th>
<th width="110">Speed</th>
<th width="180">Endurance</th>
<th width="350">Payload, compute, and perception</th>
<th width="240">Hand form</th>
</tr>
</thead>
<tbody>
<tr>
<td width="170" nowrap><a href="https://www.agibot.com/products/A2_Ultra">A2 Ultra</a><br>Flagship full-size biped</td>
<td width="150">169 cm / about 69 kg</td>
<td width="130">40 including both hands: 2 neck, 7 per arm, 6 per leg, 6 per hand</td>
<td width="110">Up to 1.2 m/s</td>
<td width="180">14.4 Ah; about 3 h standing and 1.5 h+ walking; charging or battery swapping</td>
<td width="350">About 2 kg per arm; 16-core CPU + Jetson AGX Orin 64 GB; LiDAR, RGB-D, RGB, and fisheye cameras</td>
<td width="240">Native 6-DoF hand per side; no tactile-array count published</td>
</tr>
<tr>
<td width="170" nowrap><a href="https://www.agibot.com/products/A2_Ultra">A2 Lite</a><br>Entry/performance full-size biped</td>
<td width="150">169 cm / about 64 kg</td>
<td width="130">23: 1 neck, 5 per arm, 6 per leg; hands excluded</td>
<td width="110">Up to 0.8 m/s</td>
<td width="180">14.4 Ah; about 4.5 h standing and 1.5 h+ walking</td>
<td width="350">About 2 kg per arm; 16-core CPU; no high-performance board or LiDAR/RGB-D/RGB/fisheye suite</td>
<td width="240">Soft cosmetic hands, not dexterous hands</td>
</tr>
<tr>
<td width="170" nowrap><a href="https://www.agibot.com/products/A2_Max">A2 Max</a><br>Marked “Coming soon”</td>
<td width="150">175 cm / 85 kg</td>
<td width="130">67 total / 53 active; 19 total / 12 active per hand</td>
<td width="110">1 m/s</td>
<td width="180">About 2 h with battery swapping</td>
<td width="350">40 kg across the full workspace; 8800 N leg thrust; 450 N·m peak dual-arm joint torque</td>
<td width="240">Industrial five-finger hand; pre-release status must be kept separate from shipping products</td>
</tr>
<tr>
<td width="170" nowrap><a href="https://www.agibot.com/products/A3">A3</a><br>2026 full-size biped</td>
<td width="150">173 cm / 55 kg</td>
<td width="130">31 body DoF excluding hands: 2 neck, 7 per arm, 3 waist, 6 per leg</td>
<td width="110">Daily maximum 1.8 m/s; laboratory 2.5 m/s; maximum running speed 5 m/s</td>
<td width="180">1152 Wh; about 10 h mixed duty, 6 h standing, and &gt;4 h continuous walking; battery swapping</td>
<td width="350">5 kg per arm; RK3588×2; stereo RGB, GPS, UWB, and shoulder touch sensors</td>
<td width="240">Standard silicone hands/fists with no active finger DoF; not dexterous hands</td>
</tr>
<tr>
<td width="170" nowrap><a href="https://www.agibot.com/products/X1">X1</a><br>Mid-size full-stack open-source biped</td>
<td width="150">130 cm / 33 kg</td>
<td width="130">34</td>
<td width="110">Up to 1 m/s</td>
<td width="180">About 2 h</td>
<td width="350">0.5 kg per arm; current page does not publish one unified compute/perception configuration</td>
<td width="240">OmniPicker adaptive gripper: 30 N, 120 mm stroke, 0.7 s cycle; not a five-finger hand</td>
</tr>
<tr>
<td width="170" nowrap><a href="https://www.agibot.com/products/X2">X2</a><br>Half-size base biped</td>
<td width="150">About 131 cm / 35 kg</td>
<td width="130">25: 0 neck, 5 per arm, 3 waist, 6 per leg</td>
<td width="110">Typical ≤0.8 m/s; up to 1.8 m/s; laboratory ≤2 m/s</td>
<td width="180">About 500 Wh; about 2 h at 0.5 m/s; swappable battery</td>
<td width="350">3 kg in specified poses and ≤1 kg over the full workspace; RK3588×2; interaction RGB but no LiDAR/RGB-D</td>
<td width="240">Base X2 does not support the Ultra-only OmniHand/OmniPicker option</td>
</tr>
<tr>
<td width="170" nowrap><a href="https://www.agibot.com/products/X2">X2 Ultra</a><br>Half-size high-spec biped</td>
<td width="150">About 131 cm / 39 kg</td>
<td width="130">30: 1 neck, 7 per arm, 3 waist, 6 per leg</td>
<td width="110">Typical ≤0.8 m/s; up to 1.8 m/s; laboratory ≤2 m/s</td>
<td width="180">About 500 Wh; about 2 h at 0.5 m/s; swappable battery and optional charging dock</td>
<td width="350">3 kg in specified poses and ≤1 kg over the full workspace; RK3588×2 + Orin NX 157 TOPS; LiDAR, RGB-D, front/rear RGB</td>
<td width="240">Optional OmniHand or OmniPicker; neither is standard</td>
</tr>
</tbody>
</table>

##### Lab-built biped platforms in papers

Here, “lab-built” means that the author team designed or manufactured the core mechanical and electrical platform and validated it on hardware. HumanPlus and OmniH2O therefore remain commercial H1 bodies with research-team wrist/hand integrations, rather than fully lab-built robots.

<table width="1400">
<thead>
<tr>
<th width="180" nowrap>Platform / venue</th>
<th width="150">Height / weight</th>
<th width="130">Active DoF</th>
<th width="360">Measured capability</th>
<th width="320">Compute / sensing</th>
<th width="260">Hand and correct classification</th>
</tr>
</thead>
<tbody>
<tr>
<td width="180" nowrap><a href="https://hybrid-robotics.berkeley.edu/publications/ICRA2025_Berkeley_Humanoid.pdf">Berkeley Humanoid</a><br>ICRA 2025</td>
<td width="150">0.85 m / 16 kg</td>
<td width="130">12 on the tested robot: 6 per leg</td>
<td width="360">364 m in a 10-minute campus walk and 96 m in a 5-minute trail test; no rated product endurance/payload</td>
<td width="320">Intel NUC, low-cost IMU, dual batteries; expansion interfaces for RGB-D/LiDAR</td>
<td width="260">The design discusses two 4-DoF arms, but the validated robot had no arms or hands; classify it as a lab-built biped locomotion platform</td>
</tr>
<tr>
<td width="180" nowrap><a href="https://lite.berkeley-humanoid.org/">Berkeley Humanoid Lite</a><br>RSS 2025</td>
<td width="150">0.8 m / 16 kg</td>
<td width="130">22 body DoF: 12 legs + 10 arms; grippers excluded</td>
<td width="360">6S 4000 mAh, about 30 minutes; demonstrates walking and teleoperated writing, block, and Rubik's-cube tasks</td>
<td width="320">Intel N95 mini PC + IMU; modular 3D-printed cycloidal gearboxes; hardware cost under $5,000</td>
<td width="260">Two 5-DoF arms with integrated grippers; not five-finger dexterous hands</td>
</tr>
<tr>
<td width="180" nowrap><a href="https://proceedings.mlr.press/v305/shi25a.html">ToddlerBot</a><br>CoRL 2025</td>
<td width="150">0.56 m / 3.4 kg</td>
<td width="130">30 body DoF: 7 per arm, 6 per leg, 2 neck, 2 waist; end effectors excluded</td>
<td width="360">Lifts 1.484 kg; practical battery duration about 2 h; the 19-minute continuous stepping test is a thermal/control test, not battery endurance</td>
<td width="320">Jetson Orin NX 16 GB, dual fisheye cameras, IMU, two microphones and speaker; system cost under $6,000</td>
<td width="260">Quick-change parallel gripper or compliant palm; not a five-finger dexterous hand</td>
</tr>
</tbody>
</table>

##### Humanoid-body and dexterous-hand configurations

<table width="1200">
<thead>
<tr>
<th width="200" nowrap>Vendor / end effector</th>
<th width="180">Form</th>
<th width="320">DoF and sensing</th>
<th width="180">Weight / force</th>
<th width="320">Explicit humanoid compatibility</th>
</tr>
</thead>
<tbody>
<tr>
<td width="200" nowrap><a href="https://www.unitree.com/Dex2-5/">Unitree Dex2/5</a></td>
<td width="180">Five-finger tendon hand for lightweight grasping and gestures</td>
<td width="320">10 motion DoF, 2 active DoF; no tactile array listed</td>
<td width="180">365 g; maximum grasp about 1.5 kg</td>
<td width="320">G1 and R1</td>
</tr>
<tr>
<td width="200" nowrap><a href="https://www.unitree.com/Dex3-1/">Unitree Dex3-1</a></td>
<td width="180">Three-finger force-controlled hand</td>
<td width="320">7 active DoF; up to 33 tactile sensing elements</td>
<td width="180">710 g; about 0.5 kg palm-down grasp</td>
<td width="320">G1, especially G1 EDU/flagship configurations</td>
</tr>
<tr>
<td width="200" nowrap><a href="https://www.unitree.com/Dex5-1/">Unitree Dex5-1 / Dex5-1P</a></td>
<td width="180">High-DoF five-finger hand</td>
<td width="320">20 DoF (16 active + 4 coupled); 94 pressure elements per hand on P</td>
<td width="180">About 1.1 kg; fingertip force about 10 N</td>
<td width="320">Explicit option on H1-2</td>
</tr>
<tr>
<td width="200" nowrap><a href="https://www.unitree.com/H2plus/">Dual SharpaWave hands</a></td>
<td width="180">Dense-tactile H2 Plus research configuration</td>
<td width="320">22 active DoF per hand; &gt;1000 tactile pixels per fingertip</td>
<td width="180">1.3 kg per hand; 150 N grip force and 20 N fingertip force</td>
<td width="320">H2 Plus; 31 body + 44 hand DoF = 75 system DoF</td>
</tr>
<tr>
<td width="200" nowrap><a href="https://www.agibot.com/products/OmniHand_O10">AgiBot OmniHand 2025</a></td>
<td width="180">Five-finger interaction/light-duty dexterous hand</td>
<td width="320">10 active / 16 total DoF; 400+ taxels on the tactile version</td>
<td width="180">≤550 g tactile version; typical fingertip force 5 N</td>
<td width="320">Official option on X2 Ultra; sold as an A2 retrofit but not part of the native A2 40-DoF count</td>
</tr>
<tr>
<td width="200" nowrap><a href="https://www.agibot.com/products/OmniHand_O12">AgiBot OmniHand Pro 2025</a></td>
<td width="180">Five-finger professional manipulation hand</td>
<td width="320">12 active / 19 total DoF; 150+ taxels, 3-axis fingertip force and 1-axis palm force</td>
<td width="180">≤750 g; typical fingertip force 20 N</td>
<td width="320">General robot/arm end effector; no current per-model evidence that it is standard on A3 or X1</td>
</tr>
<tr>
<td width="200" nowrap>AgiBot OmniPicker</td>
<td width="180">Adaptive two-finger gripper, not a dexterous hand</td>
<td width="320">120 mm stroke; 0.7 s open/close cycle</td>
<td width="180">0.43 kg; maximum clamping force 30 N</td>
<td width="320">Official X1 configuration and optional X2 Ultra end effector</td>
</tr>
</tbody>
</table>

Both ecosystems use the general pattern “walking body + replaceable end effector + vision/touch + optional high-performance compute,” but their product tiers differ. Unitree typically adds wrists, hands, and tactile sensing on EDU or high-spec versions, with H2 Plus becoming the complete dense-tactile reference stack. AgiBot A2 Ultra uses a native 6-DoF hand, X2 Ultra exposes OmniHand/OmniPicker as options, and standard A3 still uses non-actuated silicone hands. Comparisons therefore need to name the body version, end-effector model, active versus passive DoF, and whether tactile sensing is standard or optional.

#### humanoid

Total: 78 papers. This is the single humanoid paper master table. Every row was checked against the primary paper or official project material and distinguishes real hardware, simulated robot models, and non-robot virtual humans. CoRL 2024 papers are labeled by conference year even when the PMLR volume was published in 2025. **Current bottlenecks prioritize author-stated limitations; when a paper has no limitations section, the cell records a verifiable evaluation boundary. Future directions are research inferences from those boundaries, not quotations from the authors.** The two added evidence columns report the simulator/training stack and paper-reported quantitative details. **“Not disclosed” means the paper did not name the engine or metric; it is not backfilled from convention. Evidence from official code is explicitly qualified.**

<table width="2455">
<thead>
<tr>
<th width="105" nowrap>Venue/Year</th>
<th width="280">Paper/Method</th>
<th width="210">Direction/Method</th>
<th width="260">Exact Robot/Embodiment</th>
<th width="220">Simulation/Training Environment</th>
<th width="90">Evaluation</th>
<th width="300">Paper-Reported Details/Metrics</th>
<th width="330">Problem Solved</th>
<th width="330">Current Bottleneck</th>
<th width="330">Likely Next Direction (inference)</th>
</tr>
</thead>
<tbody>
<tr>
<td width="105" nowrap>CoRL 2024</td>
<td width="280"><a href="https://proceedings.mlr.press/v270/fu25a.html">HumanPlus: Humanoid Shadowing and Imitation from Humans</a></td>
<td width="210">Human retargeting + low-level imitation + high-level visuomotor policy</td>
<td width="260">Modified Unitree H1 (33 DoF); dual Inspire RH56DFX 6-DoF hands + 1-DoF wrists</td>
<td width="220">Simulator not disclosed; PPO low-level policy trained in physics simulation</td>
<td width="90">Sim→Real</td>
<td width="300">AMASS 40 h; low-level 50 Hz / PD 1 kHz; pose 25 fps, hands 10 fps</td>
<td width="330">Unifies human shadowing, skill imitation, and autonomous visuomotor tasks on a full-size humanoid</td>
<td width="330">Limited robot DoF, hand occlusion from a fixed head camera, pose/retargeting errors, and no long-range navigation</td>
<td width="330">Higher-DoF bodies, active viewpoints, robust pose estimation, and scaled demonstrations coupled with navigation</td>
</tr>
<tr>
<td width="105" nowrap>CVPR 2025 Oral</td>
<td width="280"><a href="https://openaccess.thecvf.com/content/CVPR2025/html/Pan_TokenHSI_Unified_Synthesis_of_Physical_Human-Scene_Interactions_through_Task_Tokenization_CVPR_2025_paper.html">TokenHSI: Unified Synthesis of Physical Human-Scene Interactions through Task Tokenization</a></td>
<td width="210">Task tokenization + physics-based reinforcement learning</td>
<td width="260">Physical human with a 32-dimensional controlled action space in Isaac Gym; no robot</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="90">Sim Only</td>
<td width="300">4,096 parallel envs; 50k PPO iterations for the base policy; 512 trials/task</td>
<td width="330">Uses a unified task representation to synthesize diverse physical human-scene interactions</td>
<td width="330">Relies on reward engineering and still needs human guidance for long-horizon tasks</td>
<td width="330">Automatic reward/task planning and transfer of interaction representations to real humanoids</td>
</tr>
<tr>
<td width="105" nowrap>CVPR 2025 Highlight</td>
<td width="280"><a href="https://openaccess.thecvf.com/content/CVPR2025/html/Xu_InterMimic_Towards_Universal_Whole-Body_Control_for_Physics-Based_Human-Object_Interactions_CVPR_2025_paper.html">InterMimic: Towards Universal Whole-Body Control for Physics-Based Human-Object Interactions</a></td>
<td width="210">Contact-aware universal whole-body interaction imitation</td>
<td width="260">SMPL/SMPL-X physical humans; Unitree G1 + Inspire hands only in downstream simulation</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="90">Sim Only</td>
<td width="300">30-Hz policy; about 10 h of OMOMO; 17 teachers</td>
<td width="330">Reproduces diverse human-object whole-body interactions in one controller</td>
<td width="330">MoCap errors and simplified G1 self-collision, contact rewards, and hand coupling leave real transfer unproven</td>
<td width="330">Complete contact, actuator, and hand models, followed by real-humanoid validation</td>
</tr>
<tr>
<td width="105" nowrap>ICLR 2025 Spotlight</td>
<td width="280"><a href="https://openreview.net/forum?id=pZISppZSTv">CLoSD: Closing the Loop between Simulation and Diffusion for multi-task character control</a></td>
<td width="210">Diffusion motion planning + closed-loop physics RL</td>
<td width="260">PHC/SMPL-compatible virtual human; no robot</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="90">Sim Only</td>
<td width="300">3,072 parallel envs; 10-step diffusion; about 3,500 frames/s on RTX 3090</td>
<td width="330">Closes the loop between text-conditioned motion generation and feedback-driven multi-task physical control</td>
<td width="330">No vision, exteroception, or height maps; mid/low-level skills and fixed feedback horizons still produce artifacts</td>
<td width="330">Scene perception, hierarchical long-horizon planning, and adaptive control horizons</td>
</tr>
<tr>
<td width="105" nowrap>ICLR 2024</td>
<td width="280"><a href="https://proceedings.iclr.cc/paper_files/paper/2024/hash/6a6ecedac816a24f92ad1f444b1edcb0-Abstract-Conference.html">Unified Human-Scene Interaction via Prompted Chain-of-Contacts</a></td>
<td width="210">Prompted contact chains + universal human-scene policy</td>
<td width="260">Generic physical human in Isaac Gym; no robot</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="90">Sim Only</td>
<td width="300">40 PartNet training objects; 40 PartNet + 10 ScanNet test scenes; 1,040 + 100 interaction plans</td>
<td width="330">Unifies sitting, lying, touching, and other human-scene interactions through contact sequences</td>
<td width="330">Objects are fixed and the LLM only generates contact plans offline</td>
<td width="330">Movable objects, online contact planning, and closed-loop execution on real humanoids</td>
</tr>
<tr>
<td width="105" nowrap>ICLR 2024</td>
<td width="280"><a href="https://openreview.net/forum?id=gd0lAEtWso">OmniControl: Control Any Joint at Any Time for Human Motion Generation</a></td>
<td width="210">Controllable diffusion under spatiotemporal joint constraints</td>
<td width="260">HumanML3D 22-joint / KIT-ML 21-joint skeletons; no robot</td>
<td width="220">No physics simulation; offline diffusion on HumanML3D / KIT-ML</td>
<td width="90">Offline Benchmarks</td>
<td width="300">14,646 / 3,911 motions; 196-frame sequences; DDPM T=1000</td>
<td width="330">Allows sparse control of arbitrary joints at arbitrary times</td>
<td width="330">Roughly 1,000 denoising steps; conflicting constraints yield unnatural motion and no dynamics guarantee</td>
<td width="330">Fast diffusion, constraint-feasibility checks, and physics projection</td>
</tr>
<tr>
<td width="105" nowrap>ICCV 2023</td>
<td width="280"><a href="https://openaccess.thecvf.com/content/ICCV2023/html/Karunratanakul_Guided_Motion_Diffusion_for_Controllable_Human_Motion_Synthesis_ICCV_2023_paper.html">Guided Motion Diffusion for Controllable Human Motion Synthesis</a></td>
<td width="210">Objective/classifier-guided motion diffusion</td>
<td width="260">HumanML3D human skeleton; no robot</td>
<td width="220">No physics simulation; offline DDPM</td>
<td width="90">Offline Benchmarks</td>
<td width="300">1,000 denoising steps; about 110 s/sample; RTX 3090</td>
<td width="330">Controls generated motion toward trajectories and positions without retraining the generator</td>
<td width="330">Needs hand-designed differentiable objectives or task classifiers and lacks contact dynamics</td>
<td width="330">Composable guidance that unifies scene, contact, and physics constraints</td>
</tr>
<tr>
<td width="105" nowrap>ICCV 2023 Oral</td>
<td width="280"><a href="https://openaccess.thecvf.com/content/ICCV2023/html/Yuan_PhysDiff_Physics-Guided_Human_Motion_Diffusion_Model_ICCV_2023_paper.html">PhysDiff: Physics-Guided Human Motion Diffusion Model</a></td>
<td width="210">Physics-controller projection inside diffusion sampling</td>
<td width="260">SMPL physical human in Isaac Gym; no robot</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="90">Sim Only</td>
<td width="300">50 diffusion steps; 4 physics projections; 51.6 s/motion (about 2.5× MDM)</td>
<td width="330">Reduces foot sliding, penetration, and imbalance in human-motion diffusion</td>
<td width="330">Physics projection makes inference roughly 2–3× slower and remains limited to virtual humans</td>
<td width="330">Lightweight or learned physics projection jointly trained with robot dynamics</td>
</tr>
<tr>
<td width="105" nowrap>ECCV 2024</td>
<td width="280"><a href="https://siplab.org/projects/MANIKIN">MANIKIN: Biomechanically Accurate Neural Inverse Kinematics for Human Motion Estimation</a></td>
<td width="210">Biomechanically constrained neural inverse kinematics</td>
<td width="260">Biomechanical SMPL human; real sparse-sensor input, no robot</td>
<td width="220">No physics simulation; PyTorch neural-analytic IK</td>
<td width="90">Real Sensor Data</td>
<td width="300">40-frame window; MANIKIN-S 580 FPS / L 30.5 / LN 0.81</td>
<td width="330">Recovers human motion from sparse observations while respecting biomechanical joint ranges</td>
<td width="330">Requires known body size and remains ambiguous for seated or cross-legged poses</td>
<td width="330">Calibration-free body shape, temporal uncertainty modeling, and multimodal observations</td>
</tr>
<tr>
<td width="105" nowrap>ECCV 2024</td>
<td width="280"><a href="https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/00248.pdf">EgoPoser: Robust Real-Time Egocentric Pose Estimation from Sparse and Intermittent Observations Everywhere</a></td>
<td width="210">Real-time pose estimation from sparse, intermittent head/hand observations</td>
<td width="260">First 22 SMPL-H joints; MR headset + controllers, no robot</td>
<td width="220">No physics simulation; offline pose estimation</td>
<td width="90">Real Sensor Data</td>
<td width="300">80-frame input; one RTX 3090; inference &gt;600 FPS</td>
<td width="330">Recovers full-body pose under intermittent observations across environments</td>
<td width="330">Assumes a single floor and provides no contact or physics consistency</td>
<td width="330">Multi-floor global localization, physics constraints, and richer wearable sensing</td>
</tr>
<tr>
<td width="105" nowrap>ECCV 2022</td>
<td width="280"><a href="https://siplab.org/projects/AvatarPoser">AvatarPoser: Articulated Full-Body Pose Tracking from Sparse Motion Sensing</a></td>
<td width="210">Transformer pose tracking from sparse head-and-hands sensing</td>
<td width="260">SMPL 22-joint avatar; Vive headset/controllers, no robot</td>
<td width="220">No physics simulation; offline pose tracking</td>
<td width="90">Real Sensor Data</td>
<td width="300">60 Hz; 40-frame input; up to 662 FPS; about 2 h training on RTX 3090</td>
<td width="330">Reconstructs full-body pose in real time from only three wearable devices</td>
<td width="330">Highly underdetermined, with limited real demonstrations and no ground-contact or dynamics constraints</td>
<td width="330">Explicit uncertainty, multimodal fusion, and contact-aware physics</td>
</tr>
<tr>
<td width="105" nowrap>arXiv 2025</td>
<td width="280"><a href="https://arxiv.org/abs/2510.08807">Humanoid Everyday: A Comprehensive Robotic Dataset for Open-World Humanoid Manipulation</a></td>
<td width="210">Large-scale real-world dataset and open-world evaluation</td>
<td width="260">Unitree G1 29 DoF + dual Dex3-1; Unitree H1 27 DoF + dual 6-DoF Inspire hands</td>
<td width="220">No simulated collection; real-robot data and cloud evaluation</td>
<td width="90">Real</td>
<td width="300">260×40 = 10,400 trajectories; 30 Hz; control latency reduced to 2 ms</td>
<td width="330">Provides 10.3k trajectories over 260 tasks to fill the data/evaluation gap for open-world humanoid manipulation</td>
<td width="330">Current imitation learning remains weak with 28-D actions and cloud evaluation lacks automatic reset</td>
<td width="330">Tactile pretraining, humanoid VLAs, automatic reset, and failure recovery</td>
</tr>
<tr>
<td width="105" nowrap>ICLR 2026</td>
<td width="280"><a href="https://openreview.net/forum?id=OCJmVjyzN7">WholeBodyVLA: Towards Unified Latent VLA for Whole-body Loco-manipulation Control</a></td>
<td width="210">Action-free egocentric-video latent VLA + RL controller</td>
<td width="260">AgiBot X2 prototype: dual 7-DoF arms, OmniPicker grippers, 6 DoF per leg, 1-DoF waist, D435i</td>
<td width="220">MuJoCo for controlled X2 ablations; LMO training engine not separately disclosed</td>
<td width="90">Sim+Real</td>
<td width="300">About 300 h egocentric data; VLA about 10 Hz / LMO 50 Hz; 8×H100 + 1×H100 for RL</td>
<td width="330">Unifies language understanding, target perception, locomotion, and manipulation in one latent space</td>
<td width="330">Long-horizon and dexterous tasks remain weak; small stance/orientation errors break pick-place; end effectors are grippers</td>
<td width="330">Memory and maps, active perception, precise footholds, and dexterous-hand/tactile integration</td>
</tr>
<tr>
<td width="105" nowrap>NeurIPS 2024</td>
<td width="280"><a href="https://proceedings.neurips.cc/paper_files/paper/2024/hash/215aeb07b5996c969c0123c3c6ee8f54-Abstract-Conference.html">HumanVLA: Towards Vision-Language Directed Object Rearrangement by Physical Humanoid</a></td>
<td width="210">State-based RL/AMP teacher distilled into an egocentric vision-language-action student</td>
<td width="260">Isaac Gym physical humanoid: 15 rigid bodies, 28 PD-actuated joints, spherical hands; no real robot</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="90">Sim Only</td>
<td width="300">Simulation 60 Hz / policy 30 Hz; 585 envs; teacher about 2 d on 8×V100, student 20k epochs</td>
<td width="330">Replaces privileged object/goal state with egocentric vision and language for general room-object rearrangement</td>
<td width="330">Spherical hands cannot manipulate small objects; one object per task; no explicit memory, planning, navigation, or multi-agent module</td>
<td width="330">Dexterous hands, long-horizon multi-object tasks, explicit memory/planning/navigation, and real-humanoid transfer</td>
</tr>
<tr>
<td width="105" nowrap>ICLR 2026</td>
<td width="280"><a href="https://openreview.net/forum?id=aQWSEjcN9V">Endowing GPT-4 with a Humanoid Body: Building the Bridge Between Off-the-Shelf VLMs and the Physical World</a></td>
<td width="210">VLM instruction compiler + diffusion motion executor (BiBo)</td>
<td width="260">PHC/CLoSD virtual humanoid in Isaac Gym; no real robot</td>
<td width="220">Isaac Gym Preview 4; InfiniGen/Blender scenes and PyVHACD collisions</td>
<td width="90">Sim Only</td>
<td width="300">100 scenes, 73 object classes; 24,545 train episodes; 20 FPS; online action &gt;20 Hz</td>
<td width="330">Turns natural language into executable humanoid motion parameters without fine-tuning GPT-4</td>
<td width="330">Small text-motion data, no scene geometry, and scope limited to human-scene interaction</td>
<td width="330">Larger motion corpora, geometry, hand-object and human-human interaction, and real-robot closure</td>
</tr>
<tr>
<td width="105" nowrap>ICLR 2026</td>
<td width="280"><a href="https://openreview.net/forum?id=3UE3Aatcjy">HWC-Loco: A Hierarchical Whole-Body Control Approach to Robust Humanoid Locomotion</a></td>
<td width="210">Hierarchical robust control balancing recovery and target tracking</td>
<td width="260">Unitree H1 (19-DoF primary hardware); Unitree G1 (23-DoF cross-embodiment)</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="90">Sim+Real</td>
<td width="300">4,096 envs; about 10k/8k/6k goal/recovery/high-level iterations; simulation and hardware at 100 Hz</td>
<td width="330">Dynamically trades locomotion tracking against safety recovery under train-deploy mismatch</td>
<td width="330">Discrete hierarchy switching, a fixed low-level policy, limited disturbance coverage, and H1 DoF constraints</td>
<td width="330">Jointly learned hierarchies, adversarial disturbances, and safe loco-manipulation</td>
</tr>
<tr>
<td width="105" nowrap>ICLR 2026</td>
<td width="280"><a href="https://openreview.net/forum?id=6T3wJQhvc3">Task Tokens: A Flexible Approach to Adapting Behavior Foundation Models</a></td>
<td width="210">Freeze the behavior foundation model and learn only task tokenizers/tokens</td>
<td width="260">69-DoF SMPL virtual humanoid; no robot</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="90">Sim Only</td>
<td width="300">Simulation 120 Hz / controller 30 Hz; 1,024 envs/seed; about 120M frames</td>
<td width="330">Adapts a behavior foundation model to new tasks with few trainable parameters</td>
<td width="330">Validated on one BFM with simplified hand rewards/observations, per-task encoders, and no Sim2Real</td>
<td width="330">Shared compositional tokens, continual learning, automatic task discovery, and real-robot adaptation</td>
</tr>
<tr>
<td width="105" nowrap>ICLR 2026</td>
<td width="280"><a href="https://openreview.net/forum?id=jkhl2oI0g5">BFM-Zero: A Promptable Behavioral Foundation Model for Humanoid Control Using Unsupervised Reinforcement Learning</a></td>
<td width="210">Promptable behavioral foundation model via unsupervised Forward-Backward RL</td>
<td width="260">Unitree G1 29-DoF primary hardware; Booster T1 supplemental; no finger control</td>
<td width="220">Isaac Lab training; MuJoCo cross-engine testing</td>
<td width="90">Sim+Real</td>
<td width="300">Simulation 200 Hz / control 50 Hz; 1,024 envs; about 192M environment steps</td>
<td width="330">Prompts one policy with motions, goals, or rewards for diverse whole-body skills</td>
<td width="330">Capability is bounded by the motion library and lacks online adaptation</td>
<td width="330">Behavior-data scaling laws, online post-training, and safe adaptation</td>
</tr>
<tr>
<td width="105" nowrap>ICLR 2026</td>
<td width="280"><a href="https://openreview.net/forum?id=k3Cyx3Uets">From Language to Locomotion: Retargeting-free Humanoid Control via Motion Latent Guidance</a></td>
<td width="210">Language-conditioned motion latents + direct action diffusion (RoboGhost)</td>
<td width="260">Unitree G1 with 23-DoF PD targets and Orin NX; no finger control</td>
<td width="220">Isaac Gym training; MuJoCo cross-engine testing</td>
<td width="90">Sim+Real</td>
<td width="300">50,378 motions; policy 50 Hz / low level 500 Hz; implicit 5.84 s vs explicit 17.85 s</td>
<td width="330">Bypasses human-motion decoding and retargeting to generate robot actions directly from language latents</td>
<td width="330">Unseen MotionMillion latents degrade and larger DiTs increase real-time latency</td>
<td width="330">Faster motion generators and multimodal latent spaces spanning vision and speech</td>
</tr>
<tr>
<td width="105" nowrap>ICLR 2026</td>
<td width="280"><a href="https://openreview.net/forum?id=NEOTsyyYH7">Towards Bridging the Gap between Large-Scale Pretraining and Efficient Finetuning for Humanoid Control</a></td>
<td width="210">Large-batch SAC pretraining + model-assisted fine-tuning (LIFT)</td>
<td width="260">Simulation: Booster T1 (12/23 DoF) and G1 (29 DoF); hardware only T1 12-DoF legs</td>
<td width="220">MuJoCo Playground pretraining; Brax fine-tuning/target simulation</td>
<td width="90">Sim+Real</td>
<td width="300">1,024 evaluation episodes (1,000 steps each); &lt;1 h pretraining on one RTX 4090; 50 Hz; 80–590 s real fine-tuning data</td>
<td width="330">Bridges large-scale off-policy pretraining and sample-efficient adaptation to new environments</td>
<td width="330">Requires human e-stop/reset, Vicon height, serial training; suffers IMU drift and uses proprioception only</td>
<td width="330">Automatic reset and safety, asynchronous fine-tuning, and visual/tactile feedback</td>
</tr>
<tr>
<td width="105" nowrap>AAAI 2026</td>
<td width="280"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38918">Coordinated Humanoid Robot Locomotion with Symmetry Equivariant Reinforcement Learning Policy</a></td>
<td width="210">Symmetry-equivariant reinforcement learning (SE-Policy)</td>
<td width="260">Unitree G1, 27-DoF body; no finger control</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="90">Sim+Real</td>
<td width="300">&gt;5k training iterations, about 4 h on RTX 4090; control rate not disclosed</td>
<td width="330">Builds left-right symmetry into the policy to improve coordinated locomotion and transfer</td>
<td width="330">Only one symmetric G1 velocity task; strict symmetry does not fit asymmetric tasks or loads</td>
<td width="330">Conditional/approximate symmetry, asymmetric manipulation, and cross-embodiment validation</td>
</tr>
<tr>
<td width="105" nowrap>AAAI 2026</td>
<td width="280"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38924">FARM: Frame-Accelerated Augmentation and Residual Mixture-of-Experts for Physics-Based High-Dynamic Humanoid Control</a></td>
<td width="210">Frame-accelerated augmentation + residual MoE</td>
<td width="260">Unnamed physics-based humanoid character in Isaac Lab; no real robot</td>
<td width="220">NVIDIA Isaac Lab</td>
<td width="90">Sim Only</td>
<td width="300">Unified 30 Hz; 3,593 clips averaging 9.4 s; about 6 h hard-sample training vs 35 h full data</td>
<td width="330">Augments high-dynamic motion data and fuses residual experts for better tracking</td>
<td width="330">Source data contains penetration, floating, and jitter artifacts; no hardware validation</td>
<td width="330">Physics-consistent data curation, contact-aware augmentation, and real-humanoid transfer</td>
</tr>
<tr>
<td width="105" nowrap>AAAI 2026</td>
<td width="280"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38949">Keep On Going: Learning Robust Humanoid Motion Skills via Selective Adversarial Training</a></td>
<td width="210">Selective adversarial disturbance training</td>
<td width="260">Unitree G1; no finger control</td>
<td width="220">Isaac Gym + Legged Gym</td>
<td width="90">Sim→Real</td>
<td width="300">Policy 50 Hz; terrain height map 10 Hz; about 6k/10k adversarial iterations</td>
<td width="330">Improves persistence under disturbances while preserving motion quality</td>
<td width="330">Does not cover environment-interaction disturbances and trades adversarial strength against agility</td>
<td width="330">Contact-level adversaries, adaptive disturbance budgets, and task-level safety constraints</td>
</tr>
<tr>
<td width="105" nowrap>AAAI 2026</td>
<td width="280"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38951">Towards Adaptive Humanoid Control via Multi-Behavior Distillation and Reinforced Fine-Tuning</a></td>
<td width="210">Multi-behavior distillation + reinforced real-world fine-tuning</td>
<td width="260">Unitree G1, 20 controlled DoF (waist excluded); no finger control</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="90">Sim→Real</td>
<td width="300">4,096 envs; 10k + 4k + 10k iterations; hardware policy 50 Hz / PD 500 Hz</td>
<td width="330">Distills multiple behaviors into one policy and continues adaptation on hardware</td>
<td width="330">Proprioception-only with limited behavior and environment coverage</td>
<td width="330">Exteroception, larger unified skill libraries, and safe online adaptation</td>
</tr>
<tr>
<td width="105" nowrap>ICML 2026</td>
<td width="280"><a href="https://icml.cc/virtual/2026/poster/62003">Scalable and General Whole-Body Control for Cross-Humanoid Locomotion</a></td>
<td width="210">Morphology-randomized general whole-body control (XHugWBC)</td>
<td width="260">12 simulated platforms/13 configs; 7 real variants: Booster T1, Fourier N1, Unitree G1 (23/29 DoF), AgiBot X2, Dobot Atom, Unitree H1-2; no unified hand control</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="90">Sim+Real</td>
<td width="300">12 simulated / 7 real embodiments; generalist about 85% of specialist; 0.6 m/s×10 s×5 trials/robot</td>
<td width="330">Transfers one whole-body locomotion framework across many humanoid morphologies</td>
<td width="330">Shared semantic commands compress embodiment-specific expressiveness; ranges and retargeting remain morphology dependent</td>
<td width="330">Morphology-aware action spaces, retargeting-free transfer, and cross-platform whole-body operation</td>
</tr>
<tr>
<td width="105" nowrap>ICML 2026</td>
<td width="280"><a href="https://openreview.net/forum?id=Gd2S0bJqNZ">Learning Transferable Interaction Primitives from Game Videos for Humanoid Locomotion</a></td>
<td width="210">Game-video VQ interaction primitives + physics policy (TRIP)</td>
<td width="260">Generic simulated humanoid using PULSE priors; no real robot</td>
<td width="220">Physics engine not disclosed; reuses PULSE prior/encoder/decoder</td>
<td width="90">Sim Only</td>
<td width="300">1,536 parallel envs; 32×32×3 height map covering 2×2 m²</td>
<td width="330">Extracts reusable interaction primitives from game videos for physical humanoid control</td>
<td width="330">Motion reconstruction errors, terrain-centric tasks, and no real-robot transfer</td>
<td width="330">First-person/depth input, object and tool interaction, and Sim2Real</td>
</tr>
<tr>
<td width="105" nowrap>CVPR 2026</td>
<td width="280"><a href="https://openaccess.thecvf.com/content/CVPR2026/html/He_VIRAL_Visual_Sim-to-Real_at_Scale_for_Humanoid_Loco-Manipulation_CVPR_2026_paper.html">VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation</a></td>
<td width="210">Privileged teacher + visual student distillation + DAgger/BC</td>
<td width="260">Unitree G1 29 DoF + dual 7-DoF Dex3-1 three-finger hands + RealSense D435i</td>
<td width="220">Isaac Lab (Isaac Sim stack); MuJoCo cross-engine evaluation</td>
<td width="90">Sim→Real</td>
<td width="300">Teacher 16×L40S / student 64×L40S; 200 simulated demos; 54/59 consecutive real cycles</td>
<td width="330">Scales training and zero-shot deployment of visual whole-body loco-manipulation</td>
<td width="330">Long-tail physics/tasks, reward engineering, hand simulation gaps, and up to 64 GPUs</td>
<td width="330">Mixed sim/real imitation data and humanoid visual-tactile foundation policies</td>
</tr>
<tr>
<td width="105" nowrap>NeurIPS 2025</td>
<td width="280"><a href="https://proceedings.neurips.cc/paper_files/paper/2025/hash/6b081a311e0b9c75590ba97b104a2ce3-Abstract-Conference.html">Adversarial Locomotion and Motion Imitation for Humanoid Policy Learning</a></td>
<td width="210">Adversarial upper/lower-body locomotion-imitation coupling (ALMI)</td>
<td width="260">Unitree H1-2 (21 controlled DoF); ROBOTERA XHAND fingers are VR-retargeted, not learned end-to-end by ALMI</td>
<td width="220">Isaac Gym training; MuJoCo data generation/evaluation</td>
<td width="90">Sim+Real</td>
<td width="300">4,096 envs; &gt;80k trajectories; hardware at 50 Hz; 1,122 CMU clips</td>
<td width="330">Tracks diverse upper- and whole-body expressive motions while maintaining stable locomotion</td>
<td width="330">Weak on dynamic dance; naively training one foundation model on all data degrades quality and efficiency</td>
<td width="330">Unified rewards and stronger architectures with end-to-end fingers/contact</td>
</tr>
<tr>
<td width="105" nowrap>NeurIPS 2025</td>
<td width="280"><a href="https://neurips.cc/virtual/2025/poster/117371">From Experts to a Generalist: Toward General Whole-Body Control for Humanoid Robots</a></td>
<td width="210">Expert clustering, real adaptation, and generalist distillation (BumbleBee)</td>
<td width="260">Unitree G1 29 DoF with 23 controlled DoF (wrists excluded)</td>
<td width="220">Isaac Gym training; MuJoCo cross-engine evaluation</td>
<td width="90">Sim+Real</td>
<td width="300">6 motion clusters; batch 4,096; 20 motions×8 real rollouts per iteration</td>
<td width="330">Reduces conflicts among agile motions and distills multiple experts into one whole-body controller</td>
<td width="330">Reference drift without GPS/VIO and a complex expert-to-real-to-distillation pipeline</td>
<td width="330">Accurate state estimation, online feedback, and simpler unified post-training</td>
</tr>
<tr>
<td width="105" nowrap>NeurIPS 2025</td>
<td width="280"><a href="https://proceedings.neurips.cc/paper_files/paper/2025/hash/5a0e51901cff2b42d379ec7869603e91-Abstract-Conference.html">KungfuBot: Physics-Based Humanoid Whole-Body Control for Learning Highly-Dynamic Skills</a></td>
<td width="210">Physics-based imitation + adaptive tracking curriculum</td>
<td width="260">Unitree G1 with 23 controlled DoF (wrists excluded)</td>
<td width="220">Isaac Gym training; MuJoCo sim-to-sim</td>
<td width="90">Sim→Real</td>
<td width="300">13 agile motions; 3 seeds×1,000 episodes; 27 h on one RTX 4090</td>
<td width="330">Tracks high-speed, highly dynamic human motions such as kung fu and dance</td>
<td width="330">No complex terrain or obstacles and still one policy per reference motion</td>
<td width="330">Perception-conditioned unified multi-skill policies and online motion composition</td>
</tr>
<tr>
<td width="105" nowrap>CVPR 2025</td>
<td width="280"><a href="https://openaccess.thecvf.com/content/CVPR2025/html/Lin_Let_Humanoids_Hike_Integrative_Skill_Development_on_Complex_Trails_CVPR_2025_paper.html">Let Humanoids Hike! Integrative Skill Development on Complex Trails</a></td>
<td width="210">Integrated perception, foothold, and balance skills for trails (LEGO-H)</td>
<td width="260">Unitree H1 and G1 in Isaac; lower-body position control, no hands</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="90">Sim Only</td>
<td width="300">10-D action; policy 50 Hz; simulated depth 10±2 Hz; simulation only</td>
<td width="330">Integrates perception, locomotion, and dynamic balance on complex trails</td>
<td width="330">Prototype is simulation-only, foot-contact centric, with no kilometer-scale, energy, or real-outdoor evaluation</td>
<td width="330">Real outdoor long-range trials, energy efficiency, full-body contact, and high-level route planning</td>
</tr>
<tr>
<td width="105" nowrap>RSS 2024</td>
<td width="280"><a href="https://www.roboticsproceedings.org/rss20/p107.html">Expressive Whole-Body Control for Humanoid Robots</a></td>
<td width="210">MoCap upper-body imitation + robust velocity tracking (ExBody)</td>
<td width="260">Unitree H1, 19 DoF; no dexterous-hand control</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="90">Sim→Real</td>
<td width="300">4,096 envs; 780 MoCap clips / 3.7 h; 20-s rollout</td>
<td width="330">Balances expressive upper-body motion and stable locomotion despite human-robot morphology mismatch</td>
<td width="330">Low-DoF mapping loses motion detail, requires a standing start, and lacks automatic recovery</td>
<td width="330">Higher-fidelity retargeting, automatic initialization, and fall recovery</td>
</tr>
<tr>
<td width="105" nowrap>RSS 2024</td>
<td width="280"><a href="https://www.roboticsproceedings.org/rss20/p061.html">HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation</a></td>
<td width="210">27-task whole-body locomotion/manipulation benchmark + hierarchical RL</td>
<td width="260">Primary Unitree H1 + dual Shadow Hands; also G1, Digit, Robotiq 2F-85, and 13-DoF Unitree-hand models</td>
<td width="220">MuJoCo; MJX for parallel reaching PPO</td>
<td width="90">Sim Only</td>
<td width="300">27 tasks (15 manipulation + 12 locomotion); up to 61 actuators; horizon 500–1,000; 448 taxels</td>
<td width="330">Provides a reproducible high-dimensional, long-horizon benchmark spanning locomotion and manipulation</td>
<td width="330">Baselines are state-only; vision/full-body touch are not systematically evaluated and environments remain simplified</td>
<td width="330">Multimodal baselines, more realistic digital twins, and standardized Sim2Real evaluation</td>
</tr>
<tr>
<td width="105" nowrap>CoRL 2025</td>
<td width="280"><a href="https://proceedings.mlr.press/v305/ze25a.html">TWIST: Teleoperated Whole-Body Imitation System</a></td>
<td width="210">MoCap retargeting + a single RL/BC whole-body controller</td>
<td width="260">Unitree G1 29-DoF primary hardware; Booster T1 only sim-to-sim; no separate hand model disclosed</td>
<td width="220">Isaac Gym training; MuJoCo for T1 sim-to-sim</td>
<td width="90">Sim+Real</td>
<td width="300">15k clips≈42 h + 150 clips≈0.5 h; teleoperation/policy 50 Hz; PD 1 kHz</td>
<td width="330">Uses human motion to teleoperate manipulation, legged manipulation, locomotion, and expressive behavior in one system</td>
<td width="330">No first-person visual or tactile feedback, dependence on non-portable MoCap, and hardware overheating</td>
<td width="330">Replace MoCap with RGB pose and train autonomous policies from egocentric plus tactile data</td>
</tr>
<tr>
<td width="105" nowrap>RSS 2023</td>
<td width="280"><a href="https://www.roboticsproceedings.org/rss19/p052.html">Robust and Versatile Bipedal Jumping Control through Reinforcement Learning</a></td>
<td width="210">Goal-conditioned policy + multi-stage reinforcement learning</td>
<td width="260">Cassie biped</td>
<td width="220">MuJoCo</td>
<td width="90">Sim→Real</td>
<td width="300">Policy 33 Hz; PD 2 kHz; 750 steps≈23 s</td>
<td width="330">Uses one policy for multi-direction/multi-height jumps, landing control, and disturbance recovery</td>
<td width="330">Combining jumping and standing yields some landing oscillation and there is no perceptive foothold selection</td>
<td width="330">Add perception and planning for autonomous foothold selection in unstructured environments</td>
</tr>
<tr>
<td width="105" nowrap>CoRL 2024</td>
<td width="280"><a href="https://proceedings.mlr.press/v270/cui25a.html">Adapting Humanoid Locomotion over Challenging Terrain via Two-Phase Training</a></td>
<td width="210">Two-phase RL + command curriculum + state estimation</td>
<td width="260">In-house Noetix N1: 18 DoF, 0.95 m, 23 kg; 10 leg joints controlled with arms locked</td>
<td width="220">Isaac Gym training; MuJoCo / PyBullet / Gazebo cross-engine</td>
<td width="90">Sim→Real</td>
<td width="300">4,096 envs; controller 100 Hz; PD 1 kHz</td>
<td width="330">Improves high-speed tracking, oscillation, and transfer for a small humanoid over challenging terrain</td>
<td width="330">No terrain perception; cross-robot transfer still needs complex rewards, randomization, and timing tuning</td>
<td width="330">Combine perception with imitation and reduce cross-platform tuning</td>
</tr>
<tr>
<td width="105" nowrap>IROS 2022</td>
<td width="280"><a href="https://doi.org/10.1109/IROS47612.2022.9981091">Adapting Rapid Motor Adaptation for Bipedal Robots</a></td>
<td width="210">Extrinsics estimation + adapted base policy (A-RMA)</td>
<td width="260">Cassie, 20 DoF / 10 actuated joints</td>
<td width="220">Cassie MuJoCo; MATLAB Simulink high-fidelity validation</td>
<td width="90">Sim→Real</td>
<td width="300">Policy 30 Hz; PD 2 kHz; 2,500 steps≈83 s; adaptation history about 2 s</td>
<td width="330">Adapts online to slippery/soft ground, planks, and roughly 40-kg towing</td>
<td width="330">Proprioception-only blind controller</td>
<td width="330">Fuse onboard vision with rapid dynamics adaptation</td>
</tr>
<tr>
<td width="105" nowrap>ICRA 2024</td>
<td width="280"><a href="https://doi.org/10.1109/ICRA57147.2024.10611621">Learning Vision-Based Bipedal Locomotion for Challenging Terrain</a></td>
<td width="210">Depth history + proprioception for local height-map prediction</td>
<td width="260">Cassie + RealSense D455 + Jetson Orin Nano</td>
<td width="220">MuJoCo</td>
<td width="90">Sim→Real</td>
<td width="300">Policy 50 Hz; PD 2 kHz; 30k episodes; D455 90 FPS / height map up to 200 Hz</td>
<td width="330">Lets a biped anticipate steps, stairs, and randomized blocks from vision</td>
<td width="330">Camera cannot see directly underfoot; foot collisions dominate failures and high steps saturate stance torque</td>
<td width="330">Wider/omnidirectional views, uncertainty awareness, and collision-constrained foothold planning</td>
</tr>
<tr>
<td width="105" nowrap>ICRA 2024</td>
<td width="280"><a href="https://doi.org/10.1109/ICRA57147.2024.10610449">HumanMimic: Learning Natural Locomotion and Transitions for Humanoid Robot via Wasserstein Adversarial Imitation</a></td>
<td width="210">Wasserstein adversarial imitation + unified motion retargeting</td>
<td width="260">Full-size JAXON humanoid model</td>
<td width="220">Isaac Gym training; Choreonoid + Hrpsys high-fidelity sim-to-sim</td>
<td width="90">Sim Only</td>
<td width="300">42.6 s of reference motion; about 30 h on one RTX 3090 Ti; no hardware</td>
<td width="330">Learns standing, push recovery, squat walking, straight-leg walking, running, and natural transitions</td>
<td width="330">Only simulation/high-fidelity sim-to-sim validation; no hardware transfer</td>
<td width="330">Transfer to real full-size humanoids with perception-driven skill switching</td>
</tr>
<tr>
<td width="105" nowrap>IROS 2022</td>
<td width="280"><a href="https://doi.org/10.1109/IROS47612.2022.9981884">Learning Dynamic Bipedal Walking Across Stepping Stones</a></td>
<td width="210">One-step RL controller + reachability predictor</td>
<td width="260">Cassie + fixed overhead RealSense D435 + ArUco markers</td>
<td width="220">Cassie simulator; underlying physics engine not disclosed</td>
<td width="90">Sim+Real</td>
<td width="300">Policy/clock 40 Hz; PD 2 kHz; about 50M interim samples; 8 stepping-stone patterns</td>
<td width="330">Selects reachable footholds online for dynamic stepping-stone traversal</td>
<td width="330">Depends on external camera/markers and mostly sees one step ahead</td>
<td width="330">Reduced-order planning, multi-step foresight, and onboard egocentric vision</td>
</tr>
<tr>
<td width="105" nowrap>CoRL 2024</td>
<td width="280"><a href="https://proceedings.mlr.press/v270/pandit25a.html">Learning Decentralized Multi-Biped Control for Payload Transport</a></td>
<td width="210">Shared decentralized multi-agent reinforcement learning</td>
<td width="260">Two/three real Cassies; simulation scaled to ten</td>
<td width="220">Custom multi-Cassie physics simulation; underlying engine not disclosed</td>
<td width="90">Sim→Real</td>
<td width="300">500 steps=10 s; train N=1–3, test N=2–10; 20–80 kg payloads and 0–100 N perturbations</td>
<td width="330">Lets varying numbers/configurations of bipeds transport a rigid payload without retraining</td>
<td width="330">Flat terrain only, at most three real robots, no cameras, and limited cost/fault/configuration generalization</td>
<td width="330">Rough terrain, heterogeneous bipeds, distributed sensing/communication, and fault tolerance</td>
</tr>
<tr>
<td width="105" nowrap>RSS 2025</td>
<td width="280"><a href="https://www.roboticsproceedings.org/rss21/p063.html">Learning Getting-Up Policies for Real-World Humanoid Robots</a></td>
<td width="210">Two-stage curriculum: discover, then smooth deployable get-up motions</td>
<td width="260">Unitree G1</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="90">Sim→Real</td>
<td width="300">Simulation 1 kHz / control 50 Hz; 4,096 envs; Stage I≈5B sampling steps; real 78.3% vs 41.7%</td>
<td width="330">Gets up from supine/prone poses on flat, slippery, deformable, sloped, grass, and snow surfaces</td>
<td width="330">Only supine and prone starts; arbitrary side-lying and cluttered contacts are not covered</td>
<td width="330">Arbitrary fall poses, contact sensing, and a continuous get-up-to-walk loop</td>
</tr>
<tr>
<td width="105" nowrap>IROS 2024</td>
<td width="280"><a href="https://doi.org/10.1109/IROS58592.2024.10802816">Bipedal Safe Navigation over Uncertain Rough Terrain: Unifying Terrain Mapping and Locomotion Stability</a></td>
<td width="210">GP terrain/deviation modeling + hierarchical safe navigation</td>
<td width="260">Agility Digit (MuJoCo model)</td>
<td width="220">MuJoCo</td>
<td width="90">Sim Only</td>
<td width="300">Three 20×20 m environments; 100 initial GP points + 10/step; 3 candidate trajectories/local target</td>
<td width="330">Jointly handles uncertain terrain mapping, motion deviation, and dynamically feasible footholds</td>
<td width="330">No hardware experiment</td>
<td width="330">Outdoor Digit hardware, onboard mapping, calibrated uncertainty, and safe foothold closure</td>
</tr>
<tr>
<td width="105" nowrap>IROS 2023</td>
<td width="280"><a href="https://doi.org/10.1109/IROS55552.2023.10342209">Overtaking Moving Obstacles with Digit: Path Following for Bipedal Robots via Model Predictive Contouring Control</a></td>
<td width="210">Model-predictive contouring control over speed, path error, and footholds</td>
<td width="260">Agility Digit</td>
<td width="220">MuJoCo</td>
<td width="90">Sim Only</td>
<td width="300">Simulation 2 kHz; MPCC 15 Hz; low-level QP 400 Hz; horizon 5; 12-ms mean solve</td>
<td width="330">Lets a biped trade path fidelity against speed to overtake moving obstacles</td>
<td width="330">High-fidelity simulation only and no complete safety corridor in cluttered 3D spaces</td>
<td width="330">Real Digit validation integrated with safe walking corridors</td>
</tr>
<tr>
<td width="105" nowrap>IROS 2023</td>
<td width="280"><a href="https://doi.org/10.1109/IROS55552.2023.10341263">Template Model Inspired Task Space Learning for Robust Bipedal Locomotion</a></td>
<td width="210">ALIP-inspired high-level RL + model-based low-level control</td>
<td width="260">Rabbit, Walker2D, and Digit (20 actuated joints)</td>
<td width="220">MuJoCo</td>
<td width="90">Sim Only</td>
<td width="300">Low level 1 kHz; high level 33 Hz; 300 steps=9 s; all three embodiments simulation-only</td>
<td width="330">Uses a unified low-dimensional task-space interface across biped morphologies</td>
<td width="330">No hardware validation on any embodiment; tasks focus on speed, slopes, and disturbances</td>
<td width="330">Digit hardware plus broader balance, stair, and stepping-stone tasks</td>
</tr>
<tr>
<td width="105" nowrap>RSS 2025</td>
<td width="280"><a href="https://www.roboticsproceedings.org/rss21/p070.html">HOMIE: Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit</a></td>
<td width="210">RL lower body + isomorphic arm exoskeleton + motion gloves</td>
<td width="260">Unitree G1 + dual Dex3-1 (7 DoF each) primary hardware; Fourier GR-1 in simulation/exoskeleton adaptation</td>
<td width="220">Isaac Gym training; Isaac Sim / Isaac Lab (GRUtopia) cross-engine</td>
<td width="90">Sim+Real</td>
<td width="300">4,096 envs; about 3 h on one RTX 4090; π_loco 50 Hz; D455≈30 Hz; IL loop 10 Hz</td>
<td width="330">Efficient low-cost cockpit teleoperation for large-workspace, contact-rich loco-manipulation</td>
<td width="330">Limited rough-terrain reliability, glove thumb ergonomics, force feedback, and waist teleoperation</td>
<td width="330">Better terrain skills, force/tactile feedback, waist control, and an autonomous data flywheel</td>
</tr>
<tr>
<td width="105" nowrap>RSS 2025</td>
<td width="280"><a href="https://www.roboticsproceedings.org/rss21/p061.html">AMO: Adaptive Motion Optimization for Hyper-Dexterous Humanoid Whole-Body Control</a></td>
<td width="210">Trajectory optimization + Sim2Real RL adapter</td>
<td width="260">Unitree G1 29 DoF + dual Dex3-1 (7 DoF each) + 3-DoF active head + ZED Mini</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="90">Sim+Real</td>
<td width="300">4,096 env×500 steps per evaluation; Orin NX inference at 50 Hz</td>
<td width="330">Expands whole-body workspace for squatting/bending/ground pickup under OOD commands</td>
<td width="330">Upper/lower-body decoupling limits dynamic coordination and arm generation ignores base state</td>
<td width="330">Balance-aware upper-body generation and unified whole-body contact control</td>
</tr>
<tr>
<td width="105" nowrap>RSS 2025</td>
<td width="280"><a href="https://www.roboticsproceedings.org/rss21/p067.html">A Unified and General Humanoid Whole-Body Controller for Fine-Grained Locomotion</a></td>
<td width="210">General command space + symmetry loss + intervention training (HugWBC)</td>
<td width="260">Unitree H1, 19 DoF; no independent finger policy</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="90">Sim→Real</td>
<td width="300">Control 50 Hz; 1,000 steps=20 s; about 16 h on one RTX 4090; 4,096-rollout robustness tests</td>
<td width="330">One controller unifies walk/run/stand/jump/hop and fine-grained gait parameters</td>
<td width="330">Still a low-level WBC with no autonomous planner; lateral commands and wear are H1-limited</td>
<td width="330">Cross-humanoid deployment with task-level planners</td>
</tr>
<tr>
<td width="105" nowrap>RSS 2025</td>
<td width="280"><a href="https://www.roboticsproceedings.org/rss21/p068.html">BeamDojo: Learning Agile Humanoid Locomotion on Sparse Footholds</a></td>
<td width="210">Polygon-foot sparse reward + dual critic + two-stage RL</td>
<td width="260">Unitree G1, 23 actuated DoF + Orin NX + Livox Mid-360; no dexterous hands</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="90">Sim→Real</td>
<td width="300">4,096 robots; policy 50 Hz / PD 500 Hz; LiDAR map 10 Hz; 20-cm stones, 45-cm max gap</td>
<td width="330">Achieves precise, disturbance-robust footholds on beams and stepping stones</td>
<td width="330">LiDAR odometry/map drift, hard-to-simulate dynamic support, and sharp degradation on tiny stones/large steps</td>
<td width="330">Uncertainty awareness, dynamic-support modeling, and stronger stride/balance objectives</td>
</tr>
<tr>
<td width="105" nowrap>CoRL 2024</td>
<td width="280"><a href="https://proceedings.mlr.press/v270/li25a.html">OKAMI: Teaching Humanoid Robots Manipulation Skills through Single Video Imitation</a></td>
<td width="210">Single RGB-D human video + object-aware retargeting + closed-loop policy</td>
<td width="260">Fourier GR-1 + dual Inspire dexterous hands (6 actuated DoF each)</td>
<td width="220">Main method does not rely on simulation; robosuite only for supplemental evaluation</td>
<td width="90">Sim+Real</td>
<td width="300">One RGB-D video/task; joints 400 Hz / high level 40 Hz; 10 s@30 fps reconstruction about 10 min</td>
<td width="330">Teaches fine bimanual manipulation from one video without robot teleoperation</td>
<td width="330">Upper-body tabletop scope, RGB-D dependence, and weak robustness to large object-shape changes</td>
<td width="330">Internet RGB video, stronger foundation vision models, and walking whole-body manipulation</td>
</tr>
<tr>
<td width="105" nowrap>CoRL 2024</td>
<td width="280"><a href="https://proceedings.mlr.press/v270/cheng25b.html">Open-TeleVision: Teleoperation with Immersive Active Visual Feedback</a></td>
<td width="210">Stereo visual feedback + active neck + arm/hand teleoperation</td>
<td width="260">H1 + dual Inspire hands + 2-DoF neck; GR-1 + jaw gripper + 3-DoF neck</td>
<td width="220">No physics simulation; real H1 / GR-1 data and ACT</td>
<td width="90">Real</td>
<td width="300">System 60 Hz; ACT 25k iterations / batch 45; mostly 20 demos/task (10 for can sorting)</td>
<td width="330">Improves collection efficiency and usability for long-horizon precise humanoid manipulation</td>
<td width="330">No tactile feedback or expert relabeling, and experiments do not use legged mobility</td>
<td width="330">Visual-tactile closure, mobile whole-body teleoperation, and cross-embodiment data</td>
</tr>
<tr>
<td width="105" nowrap>CoRL 2024 Oral</td>
<td width="280"><a href="https://proceedings.mlr.press/v270/zhang25a.html">WoCoCo: Learning Whole-Body Humanoid Control with Sequential Contacts</a></td>
<td width="210">Sequential contact stages + generic-reward end-to-end RL</td>
<td width="260">Unitree H1 (corroborated by official code/project, not named in main text); plus 22-DoF simulated dinosaur</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="90">Sim+Real</td>
<td width="300">Policy 50 Hz; PD 200 Hz; 4-Hz Butterworth low-pass; parallel-env count not disclosed</td>
<td width="330">Learns long-horizon multi-contact parkour, box transport, striking, and climbing without motion priors</td>
<td width="330">Contact sequences remain hand-specified, failures are not predicted, and stage switching needs contact sensing/observation</td>
<td width="330">Failure prediction, onboard sensing, and LLM/sampling-based high-level contact planning</td>
</tr>
<tr>
<td width="105" nowrap>ICRA 2025</td>
<td width="280"><a href="https://mobile-tv.github.io/">Mobile-TeleVision: Predictive Motion Priors for Humanoid Whole-Body Control</a></td>
<td width="210">Upper-body IK/retargeting + lower-body RL + CVAE predictive motion priors</td>
<td width="260">H1 + dual 6-DoF Inspire hands + active neck/stereo; GR-1 in simulation/cross-embodiment</td>
<td width="220">Simulator not disclosed; both H1 / GR-1 evaluated in simulation</td>
<td width="90">Sim+Real</td>
<td width="300">H1 50 Hz / GR-1 100 Hz; 1-s windows of 50/100 frames; CVAE latent=64; 20 trajectories≈30 min</td>
<td width="330">Combines precise high-DoF upper-body manipulation with robust locomotion</td>
<td width="330">Upper/lower decoupling limits agility; hardware DoF and multiple inputs burden the operator</td>
<td width="330">Unified whole-body policies, lower-burden interfaces, and fusion with autonomous visuomotor policies</td>
</tr>
<tr>
<td width="105" nowrap>RSS 2025</td>
<td width="280"><a href="https://www.roboticsproceedings.org/rss21/p065.html">LangWBC: Language-directed Humanoid Whole-Body Control via End-to-end Learning</a></td>
<td width="210">RL teacher→CVAE student, mapping CLIP text directly to joint actions</td>
<td width="260">Unitree G1, 27-D joint action; no finger control</td>
<td width="220">Physics engine not disclosed</td>
<td width="90">Sim+Real</td>
<td width="300">Teacher 50 Hz; 27-D actions; 15 unseen commands; 1,000-step stability test</td>
<td width="330">Directly drives and smoothly switches real humanoid whole-body motions from language without intermediate trajectories</td>
<td width="330">Only dozens of actions, no vision, locomotion-centric scope, and a VAE-induced Sim2Real gap</td>
<td width="330">Language-action foundation controllers, diffusion motion generation, and vision-conditioned loco-manipulation</td>
</tr>
<tr>
<td width="105" nowrap>RSS 2025</td>
<td width="280"><a href="https://www.roboticsproceedings.org/rss21/p066.html">ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills</a></td>
<td width="210">Learn residual dynamics from real trajectories and inject them into simulation fine-tuning</td>
<td width="260">Unitree G1, 29/23-DoF configurations; no finger control</td>
<td width="220">Isaac Gym source training; Isaac Sim / Genesis / real world as targets</td>
<td width="90">Sim→Real</td>
<td width="300">43 motions; three transfer routes; delta-action model removed at deployment</td>
<td width="330">Narrows the sim-real dynamics gap for kicking, jumping, dance, and other agile skills</td>
<td width="330">Real data collection risks overheating/damage, depends on MoCap, and a full 23-DoF residual model is data-heavy</td>
<td width="330">Damage-aware policies, MoCap-free alignment, and few-shot/online adaptation</td>
</tr>
<tr>
<td width="105" nowrap>ICRA 2026</td>
<td width="280"><a href="https://loco-hmc.github.io/">HMC: Learning Heterogeneous Meta-Control for Contact-Rich Loco-Manipulation</a></td>
<td width="210">Continuous MoE routing among position, impedance, and hybrid force-position experts</td>
<td width="260">Unitree G1, dual 7-DoF arms + D435i; no gripper/hand, uses bare end-effectors and friction</td>
<td width="220">No simulation; real-only imitation learning/control</td>
<td width="90">Real</td>
<td width="300">OpenTV head/hand tracking at 50 Hz; torque-space soft routing; &gt;50% relative gain</td>
<td width="330">Switches precision, compliance, and force modes across wiping, drawer pulling, and bottle lifting</td>
<td width="330">Small expert/task set and no long-horizon task-level autonomy</td>
<td width="330">More control experts, force/tactile closure, and integration with VLA/task planners</td>
</tr>
<tr>
<td width="105" nowrap>ICRA 2026</td>
<td width="280"><a href="https://arxiv.org/abs/2412.13196">ExBody2: Advanced Expressive Humanoid Whole-Body Control</a></td>
<td width="210">Data filtering + generalist/specialist pretrain-finetune + distillation</td>
<td width="260">Unitree G1, 23-D action; Orin NX at 50 Hz; no finger control</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="90">Sim+Real</td>
<td width="300">Policy 50 Hz / low level 500 Hz; 18–30 ms communication latency; 250 motions×5 seeds</td>
<td width="330">Stably reproduces long dances, sidesteps, boxing, squats, and expressive dynamic motions</td>
<td width="330">Generalist underperforms specialists and multiple specialists do not compose/switch smoothly</td>
<td width="330">Dynamic expert routing inside a unified general foundation controller</td>
</tr>
<tr>
<td width="105" nowrap>NeurIPS 2024 Spotlight</td>
<td width="280"><a href="https://papers.nips.cc/paper_files/paper/2024/file/90afd20dc776bc8849c31d61a0763a0b-Paper-Conference.pdf">Humanoid Locomotion as Next Token Prediction</a></td>
<td width="210">Causal-transformer autoregression over mixed sensorimotor sequences</td>
<td width="260">Agility Digit: 1.6 m, 45 kg, 36 DoF (20 actuated); no dexterous manipulation</td>
<td width="220">Agility simulator for trajectory collection; prior RL policies trained in Isaac Gym; MuJoCo for all simulation evaluation</td>
<td width="90">Sim+Real</td>
<td width="300">10k×10 s neural-policy trajectories (about 27.8 h) plus 20k×10 s model-based-controller trajectories; Transformer context=16</td>
<td width="330">Unifies neural, MPC, MoCap, and video data for zero-shot real walking from 27 hours of data</td>
<td width="330">Robustness still trails strong MPC/RL and large-scale video action extraction/cleaning is costly</td>
<td width="330">Scaled humanoid sensorimotor foundation models and missing-modality pretraining</td>
</tr>
<tr>
<td width="105" nowrap>RSS 2024</td>
<td width="280"><a href="https://www.roboticsproceedings.org/rss20/p058.html">Advancing Humanoid Locomotion: Mastering Challenging Terrains with Denoising World Model Learning</a></td>
<td width="210">Denoising world model (DWL) + end-to-end RL</td>
<td width="260">Robot Era XBot-S (1.2 m/38 kg/26 actuators) and XBot-L (1.65 m/57 kg/54 actuators)</td>
<td width="220">Isaac Gym training; MuJoCo state-estimation analysis</td>
<td width="90">Sim→Real</td>
<td width="300">Policy 100 Hz / PD 500 Hz; 12-D actions; zero-shot real XBot-S / XBot-L</td>
<td width="330">One zero-shot policy traverses snow, slopes, stairs, and highly uneven/deformable ground</td>
<td width="330">Leg-only control with fixed arms and proprioception-only deployment</td>
<td width="330">Integrate visual terrain perception, state denoising, and whole-body task control</td>
</tr>
<tr>
<td width="105" nowrap>RSS 2025</td>
<td width="280"><a href="https://www.roboticsproceedings.org/rss21/p069.html">Gait-Net-augmented Implicit Kino-dynamic MPC for Dynamic Variable-frequency Humanoid Locomotion over Discrete Terrains</a></td>
<td width="210">Gait-Net step-time prediction + implicit kinodynamic MPC</td>
<td width="260">In-house HECTOR V2: 24 DoF, 5 actuated joints/leg, 4/arm, 44-cm legs</td>
<td width="220">MATLAB / Simulink + Simscape Multibody</td>
<td width="90">Sim+Real</td>
<td width="300">15 simulations totaling 600 s; MPC 100 Hz / low level 1 kHz; randomized step time 150–400 ms</td>
<td width="330">Jointly adapts cadence, footholds, and contact forces over discrete obstacles/gaps</td>
<td width="330">Terrain constraints cover only the next step and hardware assumes a known terrain map</td>
<td width="330">Multi-step feasible regions, onboard online perception, and full-size long-horizon MPC</td>
</tr>
<tr>
<td width="105" nowrap>CoRL 2024</td>
<td width="280"><a href="https://openreview.net/forum?id=fs7ia3FqUM">Humanoid Parkour Learning</a></td>
<td width="210">End-to-end visual whole-body control + staged RL</td>
<td width="260">Unitree H1</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="90">Sim→Real</td>
<td width="300">4,096 robots; 10 obstacle types; vision 10 Hz / policy 50 Hz / PD 1 kHz</td>
<td width="330">One visual policy selects platform jumps, gap crossing, hurdles, stairs, and other parkour skills</td>
<td width="330">Hand-built training terrain, retraining for unseen terrain, and visual interference from complex arm motion</td>
<td width="330">Procedural open terrain, rapid real-scene adaptation, and joint parkour-manipulation training</td>
</tr>
<tr>
<td width="105" nowrap>ICRA 2025</td>
<td width="280"><a href="https://ieeexplore.ieee.org/document/11128333">Learning Humanoid Locomotion with Perceptive Internal Model</a></td>
<td width="210">Robot-centric elevation map + perceptive internal model (PIM)</td>
<td width="260">Unitree H1 (5 DoF/leg) and Fourier GR-1 (6 DoF/leg)</td>
<td width="220">Simulator not disclosed; training uses ground-truth terrain heights</td>
<td width="90">Sim→Real</td>
<td width="300">About 3 h training on one RTX 4090; real H1 and GR-1 under multiple sensor configurations</td>
<td width="330">Improves complex static-terrain locomotion across embodiments and sensor configurations</td>
<td width="330">Depends on local elevation maps/odometry and does not cover dynamic obstacles or long-range navigation</td>
<td width="330">Raw multimodal perception, dynamic-obstacle understanding, and global navigation</td>
</tr>
<tr>
<td width="105" nowrap>ICRA 2025</td>
<td width="280"><a href="https://ieeexplore.ieee.org/document/11127524">Berkeley Humanoid: A Research Platform for Learning-Based Control</a></td>
<td width="210">Low-cost hardware-simulation co-design + minimalist RL</td>
<td width="260">In-house Berkeley Humanoid (armless at paper stage)</td>
<td width="220">NVIDIA Isaac Lab</td>
<td width="90">Sim→Real</td>
<td width="300">Policy 50 Hz / state estimator 1 kHz / PD 25 kHz; real 364 m/10 min and 96 m/5 min</td>
<td width="330">Uses simulation-friendly hardware to close Sim2Real for long walks, trails, pushes, and one-leg hops</td>
<td width="330">History-free policy cannot identify systems online; bimanual loco-manipulation is not yet validated</td>
<td width="330">Add arms, online adaptation, and scalable real-world learning</td>
</tr>
<tr>
<td width="105" nowrap>IROS 2023</td>
<td width="280"><a href="https://ieeexplore.ieee.org/document/10342091/">Exploring Kinodynamic Fabrics for Reactive Whole-Body Control of Underactuated Humanoid Robots</a></td>
<td width="210">Priority-aware kinodynamic fabrics for kHz whole-body control</td>
<td width="260">Agility Robotics Digit</td>
<td width="220">MuJoCo</td>
<td width="90">Sim+Real</td>
<td width="300">0.81–1.06 ms/iteration vs QP 12.60–13.05 ms; collision threshold 14 N vs 7 N</td>
<td width="330">Composes obstacle avoidance, box carrying, throwing, and walking in real time</td>
<td width="330">Incomplete convergence/stability theory for underactuated hybrid systems and no standalone balance guarantee</td>
<td width="330">Fuse with terrain-adaptive MPC for reactivity, manipulation, and stability</td>
</tr>
<tr>
<td width="105" nowrap>IROS 2024</td>
<td width="280"><a href="https://ieeexplore.ieee.org/document/10802406/">Demonstrating a Robust Walking Algorithm for Underactuated Bipedal Robots in Non-flat, Non-stationary Environments</a></td>
<td width="210">Variable-height ALIP-MPC + virtual constraints + ankle torque</td>
<td width="260">Cassie, 20 DoF</td>
<td width="220">SimMechanics; FROST trajectories; CasADi optimization</td>
<td width="90">Sim+Real</td>
<td width="300">Controller 2 kHz; MPC &lt;500 μs; lateral foot-placement control &lt;5 μs</td>
<td width="330">Maintains real-time stable walking on changing slopes and moving ground</td>
<td width="330">Only three discrete nominal trajectories cover slopes and MPC is offloaded to a second computer</td>
<td width="330">Continuous terrain parameterization, perception-driven trajectories, and fully onboard MPC</td>
</tr>
<tr>
<td width="105" nowrap>CoRL 2024</td>
<td width="280"><a href="https://proceedings.mlr.press/v270/he25b.html">OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning</a></td>
<td width="210">Universal kinematic pose interface + sparse-state whole-body policy</td>
<td width="260">Unitree H1 + Damiao wrists + dual Inspire hands</td>
<td width="220">Paper says physics simulation; official implementation uses Isaac Gym</td>
<td width="90">Sim→Real</td>
<td width="300">PD 200 Hz / policy 50 Hz; ZED 60 fps; 20-ms end-to-end latency; about 40 min real demos for 6 tasks</td>
<td width="330">Enables dexterous whole-body teleoperation from consumer head/hand tracking and collects autonomous-task data</td>
<td width="330">Autonomous learning covers few tasks and depends on human retargeting and low-actuation hands</td>
<td width="330">Visual-tactile autonomous learning, long-horizon tasks, and higher-DoF hands</td>
</tr>
<tr>
<td width="105" nowrap>IROS 2024</td>
<td width="280"><a href="https://arxiv.org/abs/2403.04436">Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation</a></td>
<td width="210">Monocular human pose + real-time retargeting/imitation control (H2O)</td>
<td width="260">Unitree H1, 19 body DoF; no dexterous-hand task</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="90">Sim→Real</td>
<td width="300">About 40 h AMASS; about 8.5k filtered motions; policy 50 Hz / PD 200 Hz; 20–60 ms latency randomization</td>
<td width="330">Uses a standard camera to drive real-time whole-body motion on a full-size humanoid</td>
<td width="330">Monocular occlusion/pose errors and motion-only control without object/tactile closure</td>
<td width="330">Robust multi-view perception extended to interactive manipulation</td>
</tr>
<tr>
<td width="105" nowrap>ICRA 2025</td>
<td width="280"><a href="https://research.nvidia.com/labs/lpr/publication/he2025hover/">HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots</a></td>
<td width="210">Distills multiple control modes into one whole-body policy</td>
<td width="260">Unitree H1, 19 DoF; no hand-contact control</td>
<td width="220">NVIDIA Isaac Gym (original paper)</td>
<td width="90">Sim+Real</td>
<td width="300">15+ control modes; 25-step history; 5 seeds; 20 standing motions×5 hardware trials</td>
<td width="330">Provides one low-level interface that switches among velocity, position, and upper-body pose modes</td>
<td width="330">Limited to state/kinematic commands with no vision, task planning, or hand contact</td>
<td width="330">A standardized foundation-control interface beneath visual, tactile, and task policies</td>
</tr>
<tr>
<td width="105" nowrap>RSS 2025</td>
<td width="280"><a href="https://www.roboticsproceedings.org/rss21/p064.html">Learning Humanoid Standing-up Control across Diverse Postures</a></td>
<td width="210">Multi-critic, multi-terrain curriculum for standing up (HoST)</td>
<td width="260">Unitree G1</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="90">Sim→Real</td>
<td width="300">4,096 envs; policy 50 Hz; PD 200 Hz sim / 500 Hz real; reported 100% hardware success</td>
<td width="330">Stands up smoothly and robustly from diverse postures indoors and outdoors</td>
<td width="330">Focuses on standing up rather than an arbitrary fall-detect-recover-resume loop</td>
<td width="330">Unify with fall detection, contact recognition, and task resumption</td>
</tr>
<tr>
<td width="105" nowrap>CoRL 2025 Oral</td>
<td width="280"><a href="https://openreview.net/forum?id=FCpYuGtN4j">HuB: Learning Extreme Humanoid Balance</a></td>
<td width="210">Reference refinement + balance policy + Sim2Real robustness</td>
<td width="260">Unitree G1</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="90">Sim→Real</td>
<td width="300">29 DoF; 25-step history; 100 episodes/policy; hardware 50 Hz and 10 consecutive runs without reset</td>
<td width="330">Reproduces extreme quasi-static balances despite morphology/dynamics mismatch</td>
<td width="330">Primarily quasi-static balance and still limited by reference, sensing, and morphology mismatch</td>
<td width="330">Dynamic, multi-contact, manipulation-aware balance</td>
</tr>
<tr>
<td width="105" nowrap>CoRL 2025</td>
<td width="280"><a href="https://openreview.net/forum?id=H0EgeP3feg">Hand-Eye Autonomous Delivery: Learning Humanoid Navigation, Locomotion and Reaching</a></td>
<td width="210">Modular eye/hand-target navigation-locomotion-reaching (HEAD)</td>
<td width="260">Unitree G1; no grasping/finger control</td>
<td width="220">Isaac Gym training; MuJoCo sim-to-sim</td>
<td width="90">Sim+Real</td>
<td width="300">Policy 30 Hz / PD 120 Hz; ADT≈400 min; 24 real tasks at 71% success</td>
<td width="330">Learns autonomous navigation and reaching from human MoCap and AR-glasses data</td>
<td width="330">Reaches but does not grasp, precise stance placement is difficult, and perception/planning/control remain decoupled</td>
<td width="330">Closed-loop grasping, unified perception-action, and long-horizon delivery</td>
</tr>
<tr>
<td width="105" nowrap>CoRL 2025</td>
<td width="280"><a href="https://proceedings.mlr.press/v305/li25h.html">CLONE: Closed-Loop Whole-Body Humanoid Teleoperation for Long-Horizon Tasks</a></td>
<td width="210">MoE whole-body policy + LiDAR-odometry closed-loop correction</td>
<td width="260">Unitree G1; head/hand VR interface, no finger model</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="90">Sim+Real</td>
<td width="300">Teacher 8,192 env / 1M iterations; student 4,096 / 600k; policy 50 Hz / LiDAR 10 Hz / PD 1 kHz</td>
<td width="330">Reduces long-range teleoperation drift and enables long-horizon loco-manipulation data collection</td>
<td width="330">Depends on a VR head/hand interface and lacks fingers, touch, and autonomous task learning</td>
<td width="330">Dexterous hands/touch, lower-burden interfaces, and conversion from teleoperation to autonomy</td>
</tr>
<tr>
<td width="105" nowrap>CoRL 2025</td>
<td width="280"><a href="https://proceedings.mlr.press/v305/lin25c.html">Sim-to-Real Reinforcement Learning for Vision-Based Dexterous Manipulation on Humanoids</a></td>
<td width="210">Privileged RL + visual-policy distillation for dexterous manipulation</td>
<td width="260">Fourier GR-1 + dual Fourier Hands (6 actuated + 5 underactuated DoF each); supplemental Inspire Hands use 6 + 6</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="90">Sim→Real</td>
<td width="300">Dual Fourier Hands: 6 actuated + 5 underactuated DoF each; perception/policy 5 Hz; 3 tasks; calibration &lt;4 min</td>
<td width="330">Achieves vision-based multi-finger manipulation that generalizes to unseen objects</td>
<td width="330">Only three tasks, task-specific calibration/rewards, and gaps in head/third-person views and hand dynamics</td>
<td width="330">Scalable visual-tactile policies, general object representations, and multi-task post-training</td>
</tr>
<tr>
<td width="105" nowrap>CoRL 2025</td>
<td width="280"><a href="https://proceedings.mlr.press/v305/zhuang25b.html">Embrace Contacts: humanoid shadowing with full body ground contacts</a></td>
<td width="210">Discrete motion commands + stochastic full-body contact policy</td>
<td width="260">Unitree G1</td>
<td width="220">NVIDIA Isaac Lab</td>
<td width="90">Sim→Real</td>
<td width="300">4,096 robots; about 72 h on RTX 4090D; G1 policy 50 Hz / PD 1 kHz; high-level commands replayed open-loop from rosbag</td>
<td width="330">Enables torso/limb ground contacts for rolling, sitting up, and other shadowed motions</td>
<td width="330">Rigid-body collision simulation, data, and rewards are difficult; commands are discrete and task perception is absent</td>
<td width="330">Learned contact models, full-body touch, and online task-conditioned control</td>
</tr>
<tr>
<td width="105" nowrap>RSS 2025</td>
<td width="280"><a href="https://www.roboticsproceedings.org/rss21/p062.html">Demonstrating Berkeley Humanoid Lite: An Open-source, Accessible, and Customizable 3D-printed Humanoid Robot</a></td>
<td width="210">Low-cost open 3D-printed hardware + Sim2Real control</td>
<td width="260">In-house Berkeley Humanoid Lite: 0.8 m, 16 kg, 22 body DoF + simple grippers</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="90">Sim+Real</td>
<td width="300">0.8 m / 16 kg / 22 DoF; hardware &lt;$5k; policy 25 Hz; zero-shot hardware; 60-h endurance test</td>
<td width="330">Lowers a reproducible, maintainable humanoid research platform to about USD 5,000</td>
<td width="330">Limited payload, precision, and task complexity; no five-finger dexterous hands</td>
<td width="330">Community replication, multi-robot real data, and modular higher-performance end-effectors</td>
</tr>
<tr>
<td width="105" nowrap>CoRL 2025</td>
<td width="280"><a href="https://proceedings.mlr.press/v305/shi25a.html">ToddlerBot: Open-Source ML-Compatible Humanoid Platform for Loco-Manipulation</a></td>
<td width="210">Learning-oriented open hardware, digital twin, and teleoperation</td>
<td width="260">In-house ToddlerBot: 0.56 m, 3.4 kg, 30 DoF + parallel gripper/compliant palm</td>
<td width="220">MuJoCo / MJX; Brax also used for RL</td>
<td width="90">Sim+Real</td>
<td width="300">3×10^8 steps / 1,024 envs; 30-DoF feedback at 50 Hz; visual policy 10 Hz with &lt;0.1-s latency</td>
<td width="330">Unifies low-cost hardware, zero-shot Sim2Real, data collection, and two-robot long-horizon toy cleanup</td>
<td width="330">Limited to toy scale with modest payload, speed, and terrain capability</td>
<td width="330">Scale open data, platform replication, and larger collaborative loco-manipulation</td>
</tr>
<tr>
<td width="105" nowrap>RSS 2024</td>
<td width="280"><a href="https://www.roboticsproceedings.org/rss20/p103.html">Design and Control of a Bipedal Robotic Character</a></td>
<td width="210">Animation-engine commands + RL performance control</td>
<td width="260">Disney in-house bipedal character: 0.66 m, 15.4 kg, 5 DoF/leg + 4-DoF head; no arms/hands</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="90">Sim+Real</td>
<td width="300">Policy 50 Hz / actuator communication 600 Hz; 100k iterations; 8,192×24 samples/iter; about 10 h hardware without a fall</td>
<td width="330">Unifies artist-directed expressive motion with robust dynamic mobility</td>
<td width="330">Depends on animation/operators, targets entertainment, and lacks autonomous perception/tasks</td>
<td width="330">Combine expressive HRI with autonomous task-level mobility</td>
</tr>
<tr>
<td width="105" nowrap>CoRL 2024</td>
<td width="280"><a href="https://proceedings.mlr.press/v270/zhao25a.html">Bi-Level Motion Imitation for Humanoid Robots</a></td>
<td width="210">Bi-level imitation alternating policy and reference-MoCap optimization</td>
<td width="260">High-fidelity MIT Humanoid model in Isaac Gym</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="90">Sim Only</td>
<td width="300">18-D actions; 13 motions; policy 50 Hz; 4,096 envs; up to 3,000 iterations; simulation only</td>
<td width="330">Automatically modifies physically infeasible motion references to improve executable imitation</td>
<td width="330">Simulation-only, computationally heavy bi-level optimization, and limited motion coverage</td>
<td width="330">Online feasible retargeting, larger motion libraries, and real-hardware validation</td>
</tr>
</tbody>
</table>

##### Distilled Humanoid Research Directions

<table width="1850">
<thead>
<tr>
<th width="190">Direction</th>
<th width="300">Representative Work</th>
<th width="280">Typical Embodiments / End Effectors</th>
<th width="360">Progress</th>
<th width="360">Shared Bottleneck</th>
<th width="360">Next Trend</th>
</tr>
</thead>
<tbody>
<tr>
<td width="190">Rough-terrain and agile locomotion</td>
<td width="300">DWL, Humanoid Parkour, PIM, BeamDojo, Cassie Jumping</td>
<td width="280">H1/G1, Cassie, Digit, XBot, HECTOR V2</td>
<td width="360">Progressed from blind walking to visual footholds, parkour, jumping, and sparse supports</td>
<td width="360">Map drift, unseen-terrain generalization, energy, heat, and impact constraints</td>
<td width="360">Raw multimodal perception + online adaptation + joint planning/control learning</td>
</tr>
<tr>
<td width="190">Whole-body imitation and expressiveness</td>
<td width="300">HumanPlus, ExBody, TWIST, ALMI, KungfuBot, ExBody2</td>
<td width="280">H1/H1-2, G1, Booster T1</td>
<td width="360">Human motion now transfers to stable locomotion, dance, and agile skills</td>
<td width="360">Morphology/DoF mismatch, retargeting error, per-skill policies, and hardware damage</td>
<td width="360">Unified motion foundation controllers, retargeting-free representations, and damage-aware post-training</td>
</tr>
<tr>
<td width="190">Balance, getting up, and safe recovery</td>
<td width="300">HoST, Getting-Up, HuB, Keep On Going, HWC-Loco</td>
<td width="280">Mainly G1/H1</td>
<td width="360">Multi-surface getting-up, extreme balance, and disturbance resistance are feasible</td>
<td width="360">Limited fall poses, no failure prediction, and no automatic task resumption</td>
<td width="360">Fall detection—contact recognition—recovery—resume loops with safety critics</td>
</tr>
<tr>
<td width="190">Teleoperation and data flywheels</td>
<td width="300">Open-TeleVision, Mobile-TeleVision, TWIST, CLONE, HOMIE, Humanoid Everyday</td>
<td width="280">H1/G1, GR-1, Dex3-1/Inspire</td>
<td width="360">Expanded from upper-body tabletop control to long-horizon whole-body loco-manipulation and large datasets</td>
<td width="360">Operator burden, MoCap/VR dependence, no force/touch, drift, and reset cost</td>
<td width="360">Lower-burden multimodal teleoperation, visual-tactile feedback, and automated data loops</td>
</tr>
<tr>
<td width="190">Loco-manipulation and dexterous hands</td>
<td width="300">WholeBodyVLA, OKAMI, AMO, VIRAL, Vision-Based Dexterous RL</td>
<td width="280">AgiBot X2, G1+Dex3-1, GR-1+Inspire</td>
<td width="360">Locomotion, stance, bimanual control, and multi-finger manipulation are beginning to work together</td>
<td width="360">Hand simulation gap, precise stance, contact force, and long-horizon recovery</td>
<td width="360">Tactile VLAs, contact-aware world models, precise whole-body planning, and automatic recovery</td>
</tr>
<tr>
<td width="190">Language/VLM and generalist policies</td>
<td width="300">HumanVLA, BiBo, LangWBC, RoboGhost, BFM-Zero, HEAD</td>
<td width="280">Virtual humanoids and G1</td>
<td width="360">Language can prompt motions, goals, object rearrangement, and partial navigation/reaching</td>
<td width="360">Small action vocabularies, weak hand/contact models, and no true long-horizon grasping</td>
<td width="360">Unified language-vision-touch-action models with hierarchical long-horizon planning</td>
</tr>
<tr>
<td width="190">Cross-embodiment and open platforms</td>
<td width="300">XHugWBC, HumanoidBench, Berkeley Humanoid/Lite, ToddlerBot</td>
<td width="280">12+ simulated and multiple in-house/commercial platforms</td>
<td width="360">Cross-morphology control, standard benchmarks, and low-cost reproducible hardware are emerging</td>
<td width="360">Inconsistent morphology semantics, large hardware variation, and sim/hardware evaluation gaps</td>
<td width="360">Morphology-aware action spaces, common protocols, and cross-platform real data/evaluation</td>
</tr>
<tr>
<td width="190">Human-motion/interaction foundations</td>
<td width="300">TokenHSI, InterMimic, CLoSD, UniHSI, OmniControl, PhysDiff</td>
<td width="280">Virtual SMPL/SMPL-X/PHC humans</td>
<td width="360">Supplies upstream representations for motion, contact, pose, and task composition</td>
<td width="360">Most are not robots and lack real-robot actuators/hands, calibrated contact dynamics, and Sim2Real validation</td>
<td width="360">Connect generative human priors to real humanoid dynamics, contact, and safety loops</td>
</tr>
</tbody>
</table>

#### bimanual

Total: 13 papers.

<table width="2260">
<thead>
<tr>
<th width="110" nowrap>Venue/Year</th>
<th width="300">Paper/Method</th>
<th width="380">Abstract</th>
<th width="150">Embodiment Type</th>
<th width="180">Sensing/Contact</th>
<th width="180">Control Interface</th>
<th width="180">Training Mode</th>
<th width="100">Sim/Real</th>
<th width="340">Paper Task/Goal</th>
<th width="80">Paper</th>
<th width="80">Project</th>
<th width="80">Code</th>
<th width="100">Data/Bench</th>
</tr>
</thead>
<tbody>
<tr>
<td width="110" nowrap>ICLR 2025</td>
<td width="300"><a href="https://openreview.net/forum?id=yAzN4tz7oI">RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation</a></td>
<td width="380">RDT-1B scales diffusion policy learning for bimanual robotic manipulation.</td>
<td width="150">Bimanual manipulation</td>
<td width="180">vision + proprioception</td>
<td width="180">bimanual diffusion action</td>
<td width="180">diffusion foundation model</td>
<td width="100">Sim + Real</td>
<td width="340">Train a large diffusion foundation model for bimanual manipulation.</td>
<td width="80"><a href="https://arxiv.org/pdf/2410.07864">paper</a></td>
<td width="80">-</td>
<td width="80">-</td>
<td width="100">-</td>
</tr>
<tr>
<td width="110" nowrap>ICRA 2025</td>
<td width="300"><a href="https://dexmimicgen.github.io/">DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning</a></td>
<td width="380">DexMimicGen automatically generates large-scale bimanual dexterous manipulation demonstrations from a small number of human demonstrations across sim and real settings.</td>
<td width="150">Bimanual dexterous manipulation</td>
<td width="180">vision + proprioception</td>
<td width="180">bimanual action</td>
<td width="180">imitation data generation</td>
<td width="100">Sim + Real</td>
<td width="340">Reduce the data collection cost for bimanual dexterous manipulation demonstrations.</td>
<td width="80"><a href="https://dexmimicgen.github.io/">paper</a></td>
<td width="80"><a href="https://dexmimicgen.github.io/">project</a></td>
<td width="80"><a href="https://github.com/NVlabs/dexmimicgen/">code</a></td>
<td width="100">-</td>
</tr>
<tr>
<td width="110" nowrap>ICLR 2026</td>
<td width="300"><a href="https://openreview.net/forum?id=jG9W6nAwVz">TwinVLA: Data-Efficient Bimanual Manipulation with Twin Single-Arm Vision-Language-Action Models</a></td>
<td width="380">TwinVLA combines two pretrained single-arm VLAs into a bimanual VLA, achieving coordinated manipulation with a small amount of bimanual data.</td>
<td width="150">Bimanual Robot</td>
<td width="180">Vision</td>
<td width="180">twin single-arm VLA coordination</td>
<td width="180">compose pretrained single-arm VLAs + limited bimanual finetuning</td>
<td width="100">Sim + Real</td>
<td width="340">Addresses the lack of large-scale bimanual data and high fine-tuning cost in bimanual VLA training.</td>
<td width="80"><a href="https://openreview.net/forum?id=jG9W6nAwVz">paper</a></td>
<td width="80">-</td>
<td width="80">-</td>
<td width="100">-</td>
</tr>
<tr>
<td width="110" nowrap>ICLR 2026</td>
<td width="300"><a href="https://openreview.net/forum?id=he86smZzRk">VLBiMan: Vision-Language Anchored One-Shot Demonstration Enables Generalizable Bimanual Robotic Manipulation</a></td>
<td width="380">VLBiMan decomposes reusable bimanual skills from a single human demonstration and adapts to scene changes with vision-language anchors.</td>
<td width="150">Bimanual Robot</td>
<td width="180">Vision</td>
<td width="180">bimanual policy / bimanual manipulation</td>
<td width="180">one-shot demonstration + VLM grounding + geometric constraints</td>
<td width="100">Real</td>
<td width="340">Addresses how bimanual manipulation can generalize from very few demonstrations to different backgrounds, object positions, and distractor scenes.</td>
<td width="80"><a href="https://openreview.net/forum?id=he86smZzRk">paper</a></td>
<td width="80">-</td>
<td width="80">-</td>
<td width="100">-</td>
</tr>
<tr>
<td width="110" nowrap>AAAI 2026</td>
<td width="300"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38926">LatentVLA: Taming Latent Space for Generalizable and Long-Horizon Bimanual Manipulation</a></td>
<td width="380">LatentVLA structures the latent space of vision-language-action policies to improve generalization and long-horizon bimanual manipulation.</td>
<td width="150">Bimanual Robot</td>
<td width="180">-</td>
<td width="180">bimanual policy / bimanual manipulation</td>
<td width="180">latent-space VLA for long-horizon bimanual manipulation</td>
<td width="100">-</td>
<td width="340">Addresses VLA latent-space organization and generalizable control in long-horizon bimanual manipulation.</td>
<td width="80"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38926">paper</a></td>
<td width="80">-</td>
<td width="80">-</td>
<td width="100">-</td>
</tr>
<tr>
<td width="110" nowrap>ICML 2026</td>
<td width="300"><a href="https://icml.cc/virtual/2026/poster/63277">DexMachina: Functional Retargeting for Bimanual Dexterous Manipulation</a></td>
<td width="380">DexMachina retargets functional bimanual dexterous manipulation skills across hands and tools by preserving task-relevant effects.</td>
<td width="150">Bimanual Robot</td>
<td width="180">-</td>
<td width="180">bimanual policy / bimanual manipulation</td>
<td width="180">bimanual policy</td>
<td width="100">-</td>
<td width="340">-</td>
<td width="80"><a href="https://icml.cc/virtual/2026/poster/63277">paper</a></td>
<td width="80">-</td>
<td width="80">-</td>
<td width="100">-</td>
</tr>
<tr>
<td width="110" nowrap>ICML 2026</td>
<td width="300"><a href="https://icml.cc/virtual/2026/poster/66358">DECO: Decoupled Multimodal Diffusion Transformer for Bimanual Dexterous Manipulation with a Plugin Tactile Adapter</a></td>
<td width="380">DECO uses a decoupled multimodal diffusion Transformer with a tactile adapter to model vision, action, and touch for bimanual dexterous manipulation.</td>
<td width="150">Bimanual Robot</td>
<td width="180">tactile / contact</td>
<td width="180">diffusion policy / tactile policy / diffusion transformer / bimanual manipulation</td>
<td width="180">diffusion policy / tactile policy / diffusion transformer</td>
<td width="100">-</td>
<td width="340">-</td>
<td width="80"><a href="https://icml.cc/virtual/2026/poster/66358">paper</a></td>
<td width="80">-</td>
<td width="80">-</td>
<td width="100">-</td>
</tr>
<tr>
<td width="110" nowrap>ICML 2026</td>
<td width="300"><a href="https://icml.cc/virtual/2026/poster/62192">RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation</a></td>
<td width="380">RoboTwin 2.0 provides a strongly domain-randomized bimanual robot data generator and benchmark.</td>
<td width="150">Bimanual Robot</td>
<td width="180">-</td>
<td width="180">bimanual policy / bimanual manipulation</td>
<td width="180">sim data generator / domain randomization / benchmark</td>
<td width="100">Sim + Benchmark</td>
<td width="340">Addresses the lack of scalable simulation data and robust evaluation tasks for bimanual manipulation.</td>
<td width="80"><a href="https://icml.cc/virtual/2026/poster/62192">paper</a> / <a href="https://arxiv.org/pdf/2506.18088">paper</a> / <a href="https://arxiv.org/abs/2506.18088">paper</a></td>
<td width="80"><a href="https://robotwin-platform.github.io/">project</a></td>
<td width="80"><a href="https://github.com/robotwin-Platform/RoboTwin">code</a></td>
<td width="100"><a href="https://huggingface.co/datasets/TianxingChen/RoboTwin2.0">hf</a></td>
</tr>
<tr>
<td width="110" nowrap>ICCV 2025</td>
<td width="300"><a href="https://arxiv.org/abs/2503.09186">Rethinking Bimanual Robotic Manipulation: Learning with Decoupled Interaction Framework</a></td>
<td width="380">This paper separates bimanual tasks into coordinated and non-coordinated cases, improving learning with independent bimanual models plus a selective interaction module.</td>
<td width="150">Bimanual Robot</td>
<td width="180">-</td>
<td width="180">per-arm policies + selective interaction module</td>
<td width="180">decoupled interaction framework</td>
<td width="100">-</td>
<td width="340">Addresses integrated bimanual policies forcing early collaboration and ignoring non-cooperative subtasks.</td>
<td width="80"><a href="https://arxiv.org/abs/2503.09186">paper</a></td>
<td width="80">-</td>
<td width="80">-</td>
<td width="100">-</td>
</tr>
<tr>
<td width="110" nowrap>ICCV 2025</td>
<td width="300"><a href="https://arxiv.org/abs/2412.06779">AnyBimanual: Transferring Unimanual Policy for General Bimanual Manipulation</a></td>
<td width="380">AnyBimanual transfers pretrained single-arm policies to language-conditioned bimanual manipulation through skill management and a few bimanual demonstrations.</td>
<td width="150">Bimanual Robot</td>
<td width="180">-</td>
<td width="180">bimanual policy / bimanual manipulation</td>
<td width="180">unimanual-to-bimanual transfer + few bimanual demos</td>
<td width="100">Sim + Real</td>
<td width="340">Addresses expensive bimanual manipulation data and the difficulty of reusing single-arm policy knowledge.</td>
<td width="80"><a href="https://arxiv.org/abs/2412.06779">paper</a></td>
<td width="80"><a href="https://anybimanual.github.io/">project</a></td>
<td width="80"><a href="https://github.com/TengBoYu01/AnyBimanual">code</a></td>
<td width="100">-</td>
</tr>
<tr>
<td width="110" nowrap>ICCV 2025</td>
<td width="300"><a href="https://arxiv.org/abs/2506.23152">DexH2R: A Benchmark for Dynamic Dexterous Grasping in Human-to-Robot Handover</a></td>
<td width="380">DexH2R builds a real human-to-dexterous-hand handover dataset and benchmark covering dynamic objects, human hand motion, and visual annotations.</td>
<td width="150">Dexterous hand</td>
<td width="180">-</td>
<td width="180">bimanual policy / bimanual manipulation</td>
<td width="180">bimanual policy</td>
<td width="100">Real + Benchmark</td>
<td width="340">Addresses the lack of real high-quality datasets for dexterous grasping in dynamic human-robot handovers.</td>
<td width="80"><a href="https://arxiv.org/abs/2506.23152">paper</a></td>
<td width="80"><a href="https://dexh2r.github.io/">project</a></td>
<td width="80"><a href="https://github.com/4DVLab/DexH2R">code</a></td>
<td width="100">DexH2R benchmark</td>
</tr>
<tr>
<td width="110" nowrap>CVPR 2025</td>
<td width="300"><a href="https://arxiv.org/abs/2503.10743">Spatial-Temporal Graph Diffusion Policy with Kinematic Modeling for Bimanual Robotic Manipulation</a></td>
<td width="380">KStar Diffuser explicitly models robot structure and kinematic constraints with a spatiotemporal graph diffusion policy.</td>
<td width="150">Bimanual Robot</td>
<td width="180">-</td>
<td width="180">diffusion policy / bimanual manipulation</td>
<td width="180">spatial-temporal graph diffusion policy + differentiable kinematics</td>
<td width="100">Sim + Real</td>
<td width="340">Addresses action prediction in bimanual imitation learning ignoring robot structure, causing collisions and joint-constraint violations.</td>
<td width="80"><a href="https://arxiv.org/abs/2503.10743">paper</a></td>
<td width="80">-</td>
<td width="80">-</td>
<td width="100">-</td>
</tr>
<tr>
<td width="110" nowrap>CVPR 2025</td>
<td width="300"><a href="https://arxiv.org/abs/2501.04595">MobileH2R: Learning Generalizable Human to Mobile Robot Handover Exclusively from Scalable and Diverse Synthetic Data</a></td>
<td width="380">MobileH2R uses scalable synthetic human-motion data and 4D imitation learning to train mobile robots for object-receiving skills.</td>
<td width="150">mobile robot + manipulator</td>
<td width="180">-</td>
<td width="180">bimanual policy / bimanual manipulation</td>
<td width="180">synthetic data + 4D imitation learning</td>
<td width="100">Sim training + Real evaluation</td>
<td width="340">Addresses the large workspace and difficulty of collecting real demonstrations for mobile robots in human-to-robot handovers.</td>
<td width="80"><a href="https://arxiv.org/abs/2501.04595">paper</a></td>
<td width="80"><a href="https://mobileh2r.github.io/">project</a></td>
<td width="80">-</td>
<td width="100">-</td>
</tr>
</tbody>
</table>

**Research status matrix for dexterous hand and tactile/contact-rich work.**

<table width="1740">
<thead>
<tr>
<th width="160" nowrap>Research Theme</th>
<th width="280">Representative Question</th>
<th width="360">Solved / Relatively Mature</th>
<th width="360">Open Bottleneck</th>
<th width="280">Representative Papers</th>
<th width="300">Required Hardware Capability</th>
</tr>
</thead>
<tbody>
<tr>
<td width="160" nowrap>General dexterous grasping</td>
<td width="280">Arbitrary-object, language-conditioned, and task-oriented grasping</td>
<td width="360">Large-scale simulated grasping, cross-hand latent action spaces, and human-video pretraining now have multiple baselines</td>
<td width="360">Real-world generalization, physical feasibility, and contact observability remain unstable</td>
<td width="280">DexGraspVLA / XL-VLA / EgoScale / UniDex</td>
<td width="300">Multifinger hand, high DoF, vision/force feedback</td>
</tr>
<tr>
<td width="160" nowrap>In-hand manipulation</td>
<td width="280">Rotation, reorientation, and nonprehensile movement</td>
<td width="360">Simulation, small real-robot task settings, and tactile-reactive policies have working methods</td>
<td width="360">Contact-dynamics reality gap, sensor coverage, and long-horizon stability</td>
<td width="280">DexNDM / NoContactNoWorries / T-Rex / PP-Tac</td>
<td width="300">Dexterous hand, proprioception, contact/tactile feedback</td>
</tr>
<tr>
<td width="160" nowrap>Cross-hand transfer</td>
<td width="280">Policy transfer across different hand morphologies</td>
<td width="360">Latent/action retargeting is emerging</td>
<td width="360">Hand morphology mismatch, DoF mismatch, and data alignment</td>
<td width="280">UniDex / Grasp2Grasp / House of Dextra</td>
<td width="300">Multiple hand models and unified action representations</td>
</tr>
<tr>
<td width="160" nowrap>Human video to robot</td>
<td width="280">Ego video, Vision Pro, and VR data converted into robot trajectories</td>
<td width="360">Egocentric video and hand-tracking data chains are becoming common</td>
<td width="360">Human-to-robot hand mapping, missing contact, and real-robot fine-tuning cost</td>
<td width="280">EgoDex / UniDex</td>
<td width="300">VR/Vision Pro, hand tracking, teleoperation</td>
</tr>
<tr>
<td width="160" nowrap>Tactile representation</td>
<td width="280">Optical tactile, cross-sensor representation, and tactile-language alignment</td>
<td width="360">Single-sensor, cross-sensor, and foundation tactile representations have clear progress</td>
<td width="360">Cross-sensor generalization, dynamic force information, and real-time closed-loop control</td>
<td width="280">AnyTouch 2 / FTP-1 / ViTaS / VTV-LLM</td>
<td width="300">Optical tactile sensors, force feedback, multimodal synchronization</td>
</tr>
<tr>
<td width="160" nowrap>Contact-rich manipulation</td>
<td width="280">Insertion, sliding, cloth, soft-body, and gentle manipulation</td>
<td width="360">Specific tasks now have policies, data-collection systems, and tactile simulators</td>
<td width="360">Real contact uncertainty, sensor durability, task coverage, and transferable closed-loop control</td>
<td width="280">Tabero / Taccel / Touch in the Wild / FreeTacMan / exUMI</td>
<td width="300">Tactile array, force-controlled arm, simulation model</td>
</tr>
</tbody>
</table>

**Hardware, simulation, and benchmark landscape.**

_Current table mentions are counted once per paper row across the 40 dexterous-hand and 28 tactile/contact-rich papers below; they are README coverage signals, not bibliometric counts._

<table width="1460">
<thead>
<tr>
<th width="220">Platform / Component</th>
<th width="120">Current Table Mentions</th>
<th width="300">Typical Role</th>
<th width="220">Official / Code Links</th>
<th width="300">Simulator / SDK Fit Observed</th>
<th width="300">Takeaway</th>
</tr>
</thead>
<tbody>
<tr>
<td width="220">Franka Emika Panda / Franka Research 3</td>
<td width="120">16</td>
<td width="300">Most common carrier arm for dexterous hands, tactile grippers, and baseline grasping</td>
<td width="220"><a href="https://frankarobotics.github.io/docs/">FCI docs</a> / <a href="https://github.com/frankarobotics/franka_ros2">franka_ros2</a> / <a href="https://github.com/frankarobotics/franka_description">models</a></td>
<td width="300">Strong real-robot SDK/ROS2 and public URDF descriptions; hand mounts, tactile mounts, and sim controllers are usually paper-specific</td>
<td width="300">Best-supported arm baseline in the current survey, but not a complete hand+tactile stack by itself</td>
</tr>
<tr>
<td width="220">Intel RealSense RGB-D</td>
<td width="120">12</td>
<td width="300">External RGB-D perception for pose, point clouds, and policy input</td>
<td width="220"><a href="https://github.com/realsenseai/librealsense">librealsense</a></td>
<td width="300">Good SDK support for real rigs; it provides vision/depth, not contact or force sensing</td>
<td width="300">Low-risk default camera, but it does not solve contact observability</td>
</tr>
<tr>
<td width="220">Allegro Hand</td>
<td width="120">14</td>
<td width="300">Four-finger dexterous hand used for rotation, articulated-object manipulation, and cross-hand transfer</td>
<td width="220"><a href="https://www.allegrohand.com/">official</a> / <a href="https://github.com/simlabrobotics/allegro_hand_ros">ROS</a> / <a href="https://github.com/simlabrobotics/allegro_hand_ros_v4">ROS v4</a></td>
<td width="300">Public ROS stack and recurring Isaac Gym / MuJoCo / DexArt usage; dense tactile sensing is not standard and is added case by case</td>
<td width="300">Mature dexterous-hand research platform when tactile is not the primary requirement</td>
</tr>
<tr>
<td width="220">LEAP Hand</td>
<td width="120">10</td>
<td width="300">Low-cost 16-DoF dexterous hand for in-hand manipulation, retargeting, and sim-to-real</td>
<td width="220"><a href="https://github.com/leap-hand/LEAP_Hand_API">API</a> / <a href="https://github.com/leap-hand">GitHub org</a></td>
<td width="300">Public Python/C++/ROS/ROS2 API plus Isaac Gym and Isaac Lab repositories are visible; tactile is usually absent or external</td>
<td width="300">Strongest open SDK+sim evidence among low-cost hands in the current table</td>
</tr>
<tr>
<td width="220">Shadow Dexterous Hand</td>
<td width="120">9</td>
<td width="300">High-DoF anthropomorphic hand and benchmark embodiment</td>
<td width="220"><a href="https://shadowrobot.com/dexterous-hand-series/">official</a> / <a href="https://robotics.farama.org/envs/adroit_hand/index.html">Adroit</a></td>
<td width="300">Very common in MuJoCo/Adroit and Isaac Gym-style simulation; real hardware transfer is less plug-and-play and costly</td>
<td width="300">Good benchmark hand; procurement should be justified by need for high-end anthropomorphic hardware</td>
</tr>
<tr>
<td width="220">Inspire RH56 family</td>
<td width="120">8</td>
<td width="300">Commercial dexterous hand and humanoid end-effector</td>
<td width="220"><a href="https://en.inspire-robots.com/product-category/the-dexterous-hands">official</a> / <a href="https://support.unitree.com/home/en/G1_developer/inspire_dfx_dexterous_hand">Unitree G1 integration note</a></td>
<td width="300">Several papers use Inspire-family assets or real hands; public sim/ROS evidence is less unified than LEAP or Allegro</td>
<td width="300">Confirm exact model, tactile option, SDK, and ROS2 support before treating it as a lab default</td>
</tr>
<tr>
<td width="220">DIGIT / Digit 360 / OmniTact</td>
<td width="120">7</td>
<td width="300">Optical tactile sensing for tactile images, touch localization, and tactile representation learning</td>
<td width="220"><a href="https://digit.ml/digit.html">DIGIT</a> / <a href="https://github.com/facebookresearch/digit-interface">interface</a> / <a href="https://github.com/facebookresearch/tacto">TACTO</a></td>
<td width="300">Good open interface and TACTO simulation support; integration with dexterous hands or closed-loop policies remains custom</td>
<td width="300">Good entry point for optical tactile research, especially representation and dataset work</td>
</tr>
<tr>
<td width="220">GelSight / GelSight Mini</td>
<td width="120">6</td>
<td width="300">Commercial gel-based optical tactile sensing</td>
<td width="220"><a href="https://www.gelsight.com/gelsightmini/">official</a> / <a href="https://github.com/gelsightinc/gsrobotics">SDK</a></td>
<td width="300">Strong real sensor ecosystem; simulation is usually via TACTO/Taxim/TacEx/Taccel-style project pipelines rather than one universal stack</td>
<td width="300">Good tactile sensor choice, but robot mounting and closed-loop latency need project validation</td>
</tr>
<tr>
<td width="220">XHand / ROBOTERA</td>
<td width="120">6</td>
<td width="300">Commercial dexterous hand used in cross-hand and real-robot dexterity papers</td>
<td width="220"><a href="https://www.robotera.com/en/goods1/4.html">official</a></td>
<td width="300">Current papers show usage, but public SDK/ROS2 and reusable sim assets were not found in a unified public package</td>
<td width="300">Promising hardware, but platform risk is higher unless vendor SDK and sim assets are confirmed</td>
</tr>
<tr>
<td width="220">xArm / UFACTORY</td>
<td width="120">4</td>
<td width="300">Carrier arm for dexterous hands and teleoperation setups</td>
<td width="220"><a href="https://github.com/xArm-Developer/xarm_ros2">xarm_ros2</a> / <a href="https://github.com/xArm-developer/xarm_ros">xarm_ros</a></td>
<td width="300">Public ROS/ROS2 packages include simulation models and control demos; dexterous-hand mounting remains custom</td>
<td width="300">Cost-effective arm candidate when paired with a separately validated hand</td>
</tr>
<tr>
<td width="220">Apple Vision Pro / Meta Quest / GELLO</td>
<td width="120">Vision Pro 3; Meta Quest or VR 2; GELLO 2</td>
<td width="300">Human demonstration, hand tracking, VR teleoperation, and retargeting data chain</td>
<td width="220"><a href="https://developer.apple.com/documentation/visionos/tracking-and-visualizing-hand-movement">Apple hand tracking</a> / <a href="https://wuphilipp.github.io/gello_site/">GELLO</a> / <a href="https://github.com/wuphilipp/gello_software">GELLO code</a></td>
<td width="300">Useful for scalable motion data; contact, force, and hand-to-robot retargeting are still algorithmic bottlenecks</td>
<td width="300">Data collection stack, not a substitute for tactile or force feedback</td>
</tr>
<tr>
<td width="220">Robotiq 2F / parallel grippers</td>
<td width="120">2</td>
<td width="300">Baseline grasping hardware in non-dexterous rows</td>
<td width="220"><a href="https://robotiq.com/products/2f85-140-adaptive-robot-gripper">official</a></td>
<td width="300">Easy to simulate and deploy compared with dexterous hands; not a multi-finger manipulation platform</td>
<td width="300">Useful baseline, but should not be counted as dexterous-hand capability</td>
</tr>
<tr>
<td width="220">Sharpa Wave / Dexmate Vega-1</td>
<td width="120">2</td>
<td width="300">High-DoF tactile dexterous hand and bimanual tactile-reactive robot setup</td>
<td width="220"><a href="https://arxiv.org/abs/2602.16710">EgoScale</a> / <a href="https://arxiv.org/abs/2606.17055">T-Rex</a></td>
<td width="300">Public evidence comes from paper/project descriptions; reusable public SDK/ROS2 and sim assets were not found</td>
<td width="300">Promising tactile-dexterity evidence, but integration risk stays high until vendor assets and APIs are confirmed</td>
</tr>
<tr>
<td width="220">Custom visuo-tactile grippers / tactile skins</td>
<td width="120">8</td>
<td width="300">Robot-free tactile data collection, portable tactile grippers, and high-coverage contact sensing</td>
<td width="220"><a href="https://opendrivelab.com/FreeTacMan">FreeTacMan</a> / <a href="https://dex-skin.github.io/">DexSkin</a> / <a href="https://peilin-666.github.io/projects/PP-Tac/">PP-Tac</a></td>
<td width="300">Most systems publish project pages or code, but mechanical mounting, calibration, and runtime integration are project-specific</td>
<td width="300">Best current route for tactile data coverage; not yet a standard plug-and-play hand stack</td>
</tr>
</tbody>
</table>

<table width="1440">
<thead>
<tr>
<th width="200">Simulator / Framework</th>
<th width="120">Current Table Mentions</th>
<th width="300">Typical Use</th>
<th width="220">Official / Code Links</th>
<th width="300">Hardware Fit</th>
<th width="300">Open Gap</th>
</tr>
</thead>
<tbody>
<tr>
<td width="200">Isaac Gym</td>
<td width="120">11</td>
<td width="300">Large-scale RL, grasp filtering, and dexterous-hand policy training</td>
<td width="220"><a href="https://developer.nvidia.com/isaac-gym">official</a> / <a href="https://github.com/isaac-sim/IsaacGymEnvs">IsaacGymEnvs</a></td>
<td width="300">Strongest recurring fit for Allegro, LEAP, Shadow, and synthetic grasp pipelines in the current table</td>
<td width="300">NVIDIA marks Isaac Gym as legacy; new projects should check Isaac Lab migration cost</td>
</tr>
<tr>
<td width="200">Isaac Lab / Isaac Sim</td>
<td width="120">2</td>
<td width="300">Successor stack for robot learning, sensor simulation, and tactile-aware experiments</td>
<td width="220"><a href="https://developer.nvidia.com/isaac/lab">Isaac Lab</a> / <a href="https://github.com/isaac-sim/IsaacLab">code</a> / <a href="https://github.com/isaac-sim/IsaacSim">Isaac Sim</a></td>
<td width="300">Good fit for Franka-style arms and newer tactile simulation papers; asset import from URDF/MJCF/CAD is supported by Isaac Sim</td>
<td width="300">Dense tactile and dexterous-hand controllers still tend to be custom integrations</td>
</tr>
<tr>
<td width="200">MuJoCo / MJCF</td>
<td width="120">3</td>
<td width="300">Contact-rich dynamics, Adroit-style hand tasks, and compact reproducible benchmarks</td>
<td width="220"><a href="https://mujoco.org/">official</a> / <a href="https://github.com/google-deepmind/mujoco">code</a> / <a href="https://github.com/google-deepmind/mujoco_menagerie">Menagerie</a></td>
<td width="300">Strong for Shadow/Adroit and MJCF models; useful for reproducible task benchmarks</td>
<td width="300">High-fidelity optical tactile rendering and real-hand drivers are not standard out of the box</td>
</tr>
<tr>
<td width="200">SAPIEN / ManiSkill</td>
<td width="120">SAPIEN 2; ManiSkill 2</td>
<td width="300">Articulated objects, manipulation environments, and task/data generation</td>
<td width="220"><a href="https://sapien.ucsd.edu/">SAPIEN</a> / <a href="https://github.com/haosulab/SAPIEN">SAPIEN code</a> / <a href="https://github.com/mani-skill/ManiSkill">ManiSkill</a></td>
<td width="300">Good articulated-object and robot asset ecosystem; hand models depend on URDF/assets supplied by each work</td>
<td width="300">Less standardized for real dexterous-hand sim-to-real than arm/gripper manipulation</td>
</tr>
<tr>
<td width="200">Adroit / Gymnasium Robotics</td>
<td width="120">2</td>
<td width="300">Dexterous manipulation benchmark with Shadow Hand and arm tasks</td>
<td width="220"><a href="https://robotics.farama.org/envs/adroit_hand/index.html">docs</a> / <a href="https://github.com/Farama-Foundation/Gymnasium-Robotics">code</a></td>
<td width="300">Strong Shadow-Hand benchmark fit; useful for algorithm comparison</td>
<td width="300">Not a procurement or real-hardware SDK; task suite is narrower than real lab manipulation</td>
</tr>
<tr>
<td width="200">DexArt / MetaWorld</td>
<td width="120">DexArt 1; MetaWorld 1</td>
<td width="300">Task benchmark suites for articulated dexterity and manipulation policies</td>
<td width="220"><a href="https://www.chenbao.tech/dexart/">DexArt</a> / <a href="https://github.com/Kami-code/dexart-release">DexArt code</a> / <a href="https://meta-world.github.io/">MetaWorld</a></td>
<td width="300">Good for benchmark comparison; hardware embodiment is fixed by each environment</td>
<td width="300">Different observation/action conventions make cross-paper comparison hard</td>
</tr>
<tr>
<td width="200">TACTO</td>
<td width="120">1</td>
<td width="300">Vision-based tactile rendering for sensors such as DIGIT and OmniTact</td>
<td width="220"><a href="https://github.com/facebookresearch/tacto">code</a> / <a href="https://ai.meta.com/research/publications/tacto-a-fast-flexible-and-open-source-simulator-for-high-resolution-vision-based-tactile-sensors/">paper page</a></td>
<td width="300">Good for tactile-image simulation and perception pretraining; originally integrates with PyBullet</td>
<td width="300">Full dexterous-hand closed-loop contact dynamics remain custom</td>
</tr>
<tr>
<td width="200">Taccel</td>
<td width="120">1</td>
<td width="300">GPU tactile simulation for vision-based tactile robotics</td>
<td width="220"><a href="https://taccel-simulator.github.io/index.html">docs</a> / <a href="https://github.com/Taccel-Simulator">GitHub</a></td>
<td width="300">Supports URDF robot loading, tactile sensor config files, and high-throughput tactile simulation</td>
<td width="300">Newer ecosystem; real sensor calibration and broad benchmark adoption are still emerging</td>
</tr>
<tr>
<td width="200">PalpationSim</td>
<td width="120">1</td>
<td width="300">Soft-body palpation and tactile representation learning</td>
<td width="220"><a href="https://zoharri.github.io/artificial-palpation/">project</a> / <a href="https://github.com/zoharri/ArtificialPalpation">code</a></td>
<td width="300">Task-specific tactile simulation rather than a general dexterous-hand simulator</td>
<td width="300">Limited cross-paper reuse evidence in the current table</td>
</tr>
<tr>
<td width="200">RLBench / tactile_envs / custom tactile simulators</td>
<td width="120">3</td>
<td width="300">Multimodal policy consensus, visuo-tactile representation learning, and articulated-object tactile studies</td>
<td width="220"><a href="https://github.com/stepjam/RLBench">RLBench</a> / <a href="https://github.com/SkyRainWind/ViTaS">ViTaS code</a> / <a href="https://vi-tacman.github.io/">Vi-TacMan</a></td>
<td width="300">Useful for method comparison, but each work defines different tactile observations and robot embodiments</td>
<td width="300">Still weaker than a shared real-hand tactile benchmark for procurement decisions</td>
</tr>
</tbody>
</table>

<table width="1280">
<thead>
<tr>
<th width="180" nowrap>Hardware Family</th>
<th width="180">Compatibility Status</th>
<th width="360">Best-Matched Simulation / Data Stack Found</th>
<th width="220">Evidence Links</th>
<th width="340">Practical Note</th>
</tr>
</thead>
<tbody>
<tr>
<td width="180" nowrap>Franka + mounted hand or tactile gripper</td>
<td width="180">official arm; community/custom end-effector integration</td>
<td width="360">ROS2/libfranka for real robot; Isaac/MuJoCo/SAPIEN assets in paper pipelines</td>
<td width="220"><a href="https://frankarobotics.github.io/docs/">FCI docs</a> / <a href="https://github.com/frankarobotics/franka_ros2">franka_ros2</a> / <a href="https://github.com/frankarobotics/franka_description">models</a></td>
<td width="340">Arm support is mature, but each hand/sensor needs mechanical mounting, calibration, and controller integration</td>
</tr>
<tr>
<td width="180" nowrap>LEAP Hand</td>
<td width="180">official</td>
<td width="360">LEAP API, LEAP Isaac Gym, LEAP Isaac Lab, paper-specific MuJoCo/Isaac environments</td>
<td width="220"><a href="https://github.com/leap-hand/LEAP_Hand_API">API</a> / <a href="https://github.com/leap-hand/LEAP_Hand_Sim">Isaac Gym sim</a> / <a href="https://github.com/leap-hand/LEAP_Hand_Isaac_Lab">Isaac Lab sim</a></td>
<td width="340">Good for reproducible hand control; tactile sensing is not part of the default hand stack</td>
</tr>
<tr>
<td width="180" nowrap>Allegro Hand</td>
<td width="180">official/community</td>
<td width="360">ROS stack, Isaac Gym, MuJoCo, DexArt-style environments</td>
<td width="220"><a href="https://www.allegrohand.com/">official</a> / <a href="https://github.com/simlabrobotics/allegro_hand_ros">ROS</a> / <a href="https://github.com/Kami-code/dexart-release">DexArt</a></td>
<td width="340">Strong research precedent; sensorized fingertips or tactile arrays must be selected separately</td>
</tr>
<tr>
<td width="180" nowrap>Shadow Dexterous Hand</td>
<td width="180">community benchmark; official hardware</td>
<td width="360">MuJoCo/Adroit and Isaac Gym grasping environments</td>
<td width="220"><a href="https://shadowrobot.com/dexterous-hand-series/">official</a> / <a href="https://robotics.farama.org/envs/adroit_hand/index.html">Adroit docs</a> / <a href="https://github.com/Farama-Foundation/Gymnasium-Robotics">Gymnasium Robotics</a></td>
<td width="340">Benchmark compatibility is strong, but real-hardware procurement and transfer are heavier than LEAP/Allegro</td>
</tr>
<tr>
<td width="180" nowrap>Inspire / XHand</td>
<td width="180">unclear</td>
<td width="360">Paper-specific assets, real rigs, and humanoid integrations</td>
<td width="220"><a href="https://en.inspire-robots.com/product-category/the-dexterous-hands">Inspire</a> / <a href="https://support.unitree.com/home/en/G1_developer/inspire_dfx_dexterous_hand">Unitree G1 note</a> / <a href="https://www.robotera.com/en/goods1/4.html">ROBOTERA</a></td>
<td width="340">Do not assume compatibility; request URDF/MJCF, ROS2 driver, low-level control rate, and tactile API from vendor</td>
</tr>
<tr>
<td width="180" nowrap>GelSight / DIGIT optical tactile sensors</td>
<td width="180">official SDK; community sim</td>
<td width="360">Real SDKs plus TACTO/Taccel/Taxim/TacEx-style tactile simulation pipelines</td>
<td width="220"><a href="https://digit.ml/digit.html">DIGIT</a> / <a href="https://github.com/facebookresearch/digit-interface">DIGIT interface</a> / <a href="https://github.com/gelsightinc/gsrobotics">GelSight SDK</a> / <a href="https://github.com/facebookresearch/tacto">TACTO</a> / <a href="https://github.com/Taccel-Simulator">Taccel</a></td>
<td width="340">Good for tactile representation; closed-loop manipulation depends on latency, mounting, calibration, and synchronization</td>
</tr>
<tr>
<td width="180" nowrap>Vision Pro / VR / GELLO teleoperation</td>
<td width="180">official tracking; community teleoperation</td>
<td width="360">Hand tracking, VR controllers, GELLO joint-level teleop, and retargeting pipelines</td>
<td width="220"><a href="https://developer.apple.com/documentation/visionos/tracking-and-visualizing-hand-movement">Apple hand tracking</a> / <a href="https://wuphilipp.github.io/gello_site/">GELLO</a> / <a href="https://github.com/wuphilipp/gello_software">GELLO code</a></td>
<td width="340">Solves scalable motion capture better than contact capture; contact and force labels still need tactile/force instrumentation</td>
</tr>
</tbody>
</table>

<table width="1380">
<thead>
<tr>
<th width="220" nowrap>Benchmark / Dataset</th>
<th width="300">Main Scope</th>
<th width="300">Hardware / Sim Tie</th>
<th width="220">Link</th>
<th width="340">Use for This Survey</th>
</tr>
</thead>
<tbody>
<tr>
<td width="220" nowrap>Adroit</td>
<td width="300">Shadow-Hand manipulation tasks such as door, hammer, pen, and relocation</td>
<td width="300">MuJoCo / Gymnasium Robotics</td>
<td width="220"><a href="https://robotics.farama.org/envs/adroit_hand/index.html">docs</a></td>
<td width="340">Good algorithm benchmark, but not a unified real-hardware dataset</td>
</tr>
<tr>
<td width="220" nowrap>DexArt</td>
<td width="300">Dexterous manipulation with articulated objects</td>
<td width="300">Benchmark environment and training code</td>
<td width="220"><a href="https://www.chenbao.tech/dexart/">project</a> / <a href="https://github.com/Kami-code/dexart-release">code</a></td>
<td width="340">Useful for articulated-object dexterity; embodiment and task definitions are benchmark-specific</td>
</tr>
<tr>
<td width="220" nowrap>GraspNet-1Billion</td>
<td width="300">Large-scale 6D parallel-gripper grasp detection</td>
<td width="300">RealSense/Kinect RGB-D scenes; parallel-jaw grasp labels</td>
<td width="220"><a href="https://graspnet.net/">project</a> / <a href="https://github.com/graspnet/graspnetAPI">API</a></td>
<td width="340">Important grasping baseline, but not a dexterous-hand manipulation benchmark</td>
</tr>
<tr>
<td width="220" nowrap>DexYCB</td>
<td width="300">Human hand grasping, 6D object pose, hand pose, and handover-related tasks</td>
<td width="300">YCB objects and multi-view real data</td>
<td width="220"><a href="https://dex-ycb.github.io/">project</a> / <a href="https://github.com/NVlabs/dex-ycb-toolkit">toolkit</a></td>
<td width="340">Useful for human hand-object perception and grasp transfer, not a robot control benchmark by itself</td>
</tr>
<tr>
<td width="220" nowrap>OakInk / OakInk2</td>
<td width="300">Hand-object interaction, affordance, and bimanual task data</td>
<td width="300">Human demonstrations and object/hand annotations</td>
<td width="220"><a href="https://oakink.net/">OakInk</a> / <a href="https://github.com/oakink/OakInk2">OakInk2 code</a></td>
<td width="340">Good for human-to-robot priors; robot embodiment retargeting remains separate</td>
</tr>
<tr>
<td width="220" nowrap>ARCTIC</td>
<td width="300">Bimanual articulated hand-object manipulation with dynamic contact</td>
<td width="300">Human video and 3D hand/object meshes</td>
<td width="220"><a href="https://arctic.is.tue.mpg.de/">project</a> / <a href="https://github.com/zc-alexfan/arctic">code</a></td>
<td width="340">Strong contact-rich human data; not directly a robot-hardware benchmark</td>
</tr>
<tr>
<td width="220" nowrap>UniDex-Dataset</td>
<td width="300">Egocentric-video-derived trajectories across multiple dexterous hands</td>
<td width="300">Eight dexterous hands, retargeting, and robot-centric trajectories</td>
<td width="220"><a href="https://unidex-ai.github.io/">project</a> / <a href="https://github.com/unidex-ai/UniDex">code</a></td>
<td width="340">Most relevant current attempt at cross-hand normalization, but still new and retargeting-heavy</td>
</tr>
<tr>
<td width="220" nowrap>DexGraspNet / DexGrasp Anything</td>
<td width="300">Large-scale simulated dexterous grasp poses</td>
<td width="300">ShadowHand-style grasp synthesis and physics filtering</td>
<td width="220"><a href="https://pku-epic.github.io/DexGraspNet/">DexGraspNet</a> / <a href="https://dexgraspanything.github.io/">DGA</a></td>
<td width="340">Useful for grasp generation; less complete for long-horizon contact-rich control</td>
</tr>
<tr>
<td width="220" nowrap>ZeroGrasp-11B</td>
<td width="300">Shape reconstruction plus 6D grasp annotations</td>
<td width="300">RGB-D, Objaverse-LVIS, Franka/Robotiq evaluation</td>
<td width="220"><a href="https://sh8.io/#/zerograsp">project</a> / <a href="https://github.com/sh8/ZeroGrasp">code</a></td>
<td width="340">Strong grasping data point, but parallel-gripper rather than dexterous-hand control</td>
</tr>
<tr>
<td width="220" nowrap>RoboTwin 2.0</td>
<td width="300">Bimanual manipulation data generation and benchmark</td>
<td width="300">Simulation benchmark with dual-arm configurations</td>
<td width="220"><a href="https://robotwin-platform.github.io/">project</a> / <a href="https://github.com/robotwin-Platform/robotwin">code</a></td>
<td width="340">Relevant for bimanual setup comparison; not tactile-first or hand-model-unified</td>
</tr>
<tr>
<td width="220" nowrap>MFR Benchmark</td>
<td width="300">Multi-finger dexterous manipulation tasks</td>
<td width="300">Allegro hand and optional arm configurations in Isaac Gym</td>
<td width="220"><a href="https://github.com/UM-ARM-Lab/MFR_benchmark">code</a></td>
<td width="340">Useful candidate benchmark for hand control if the lab standardizes on Allegro/Isaac Gym</td>
</tr>
<tr>
<td width="220" nowrap>YCB-Slide</td>
<td width="300">Sliding-touch localization</td>
<td width="300">DIGIT tactile images and YCB objects</td>
<td width="220"><a href="https://suddhu.github.io/midastouch-tactile/">project</a> / <a href="https://github.com/facebookresearch/MidasTouch">code</a></td>
<td width="340">Good tactile-localization benchmark; not a full manipulation benchmark</td>
</tr>
<tr>
<td width="220" nowrap>ToucHD / AnyTouch 2 / Sparsh</td>
<td width="300">General tactile representation learning across sensors and dynamics</td>
<td width="300">GelSight, DIGIT, FastUMI, ToucHD, and related tactile datasets</td>
<td width="220"><a href="https://github.com/GeWu-Lab/AnyTouch2">AnyTouch 2</a> / <a href="https://github.com/facebookresearch/sparsh">Sparsh</a> / <a href="https://huggingface.co/datasets/BAAI/ToucHD-Sim">ToucHD-Sim</a></td>
<td width="340">Good for representation pretraining; downstream robot policy transfer still needs task-specific data</td>
</tr>
<tr>
<td width="220" nowrap>VTV150K / VTV-LLM</td>
<td width="300">Visuo-tactile video understanding and tactile QA</td>
<td width="300">GelSight Mini, DIGIT, and Tac3D video frames</td>
<td width="220"><a href="https://github.com/IvanXie416/VTV-LLM">code</a> / <a href="https://arxiv.org/abs/2505.22566">paper</a></td>
<td width="340">Good tactile-language benchmark; not a closed-loop manipulation benchmark</td>
</tr>
<tr>
<td width="220" nowrap>Touch in the Wild</td>
<td width="300">Portable visuo-tactile gripper demonstrations for fine-grained manipulation</td>
<td width="300">Custom tactile gripper, GoPro sync, ROS2 tactile logs</td>
<td width="220"><a href="https://binghao-huang.github.io/touch_in_the_wild/">project</a></td>
<td width="340">Closest current tactile manipulation dataset in this table, but hardware is custom</td>
</tr>
<tr>
<td width="220" nowrap>T-Rex Dataset</td>
<td width="300">Tactile-synchronized bimanual dexterous manipulation</td>
<td width="300">Dexmate Vega-1 + Sharpa Wave hands; synchronized RGB, tactile signals, robot state, actions, and language</td>
<td width="220"><a href="https://arxiv.org/abs/2606.17055">paper</a> / <a href="https://tactile-reactive-dexterous.github.io/">project</a></td>
<td width="340">Important tactile-reactive dataset; public reusable assets should be checked before depending on it</td>
</tr>
<tr>
<td width="220" nowrap>FTP-1 Dataset / MTTS</td>
<td width="300">Cross-sensor foundation tactile policy pretraining</td>
<td width="300">26 data sources, 21 tactile sensors, image/array/state tactile inputs</td>
<td width="220"><a href="https://arxiv.org/abs/2606.13102">paper</a> / <a href="https://ftp1-policy.github.io/">project</a></td>
<td width="340">Best current evidence for sensor-heterogeneous tactile pretraining; downstream deployment still needs target-sensor finetuning</td>
</tr>
<tr>
<td width="220" nowrap>FreeTacMan</td>
<td width="300">Robot-free visuo-tactile data collection for contact-rich manipulation</td>
<td width="300">Handheld modular visuo-tactile gripper; Piper/Franka quick-swap mounts</td>
<td width="220"><a href="https://opendrivelab.com/FreeTacMan">project</a> / <a href="https://github.com/OpenDriveLab/FreeTacMan">code</a></td>
<td width="340">Strong data-collection benchmark candidate; not itself a fixed dexterous-hand policy benchmark</td>
</tr>
<tr>
<td width="220" nowrap>exUMI</td>
<td width="300">Extensible UMI-style tactile robot teaching</td>
<td width="300">AR MoCap, rotary encoder, modular visuo-tactile sensing, automated calibration</td>
<td width="220"><a href="https://proceedings.mlr.press/v305/xu25e.html">PMLR</a> / <a href="https://silicx.github.io/exUMI/">project</a></td>
<td width="340">Good tactile teaching-system evidence; still custom hardware rather than a universal tactile-hand standard</td>
</tr>
<tr>
<td width="220" nowrap>Vi-TacMan articulated-object suite</td>
<td width="300">Vision-to-touch articulated-object manipulation</td>
<td width="300">50,000+ simulated objects plus real Kinova Gen3 + GelSight-type tactile experiments</td>
<td width="220"><a href="https://arxiv.org/abs/2510.06339">paper</a> / <a href="https://vi-tacman.github.io/">project</a></td>
<td width="340">Useful for tactile articulated-object control; still not a full long-horizon household manipulation benchmark</td>
</tr>
</tbody>
</table>

#### dexterous hand

Total: 40 papers.

<table width="2830">
<thead>
<tr>
<th width="110" nowrap>Venue/Year</th>
<th width="280">Paper/Method</th>
<th width="280">Research Problem</th>
<th width="260">Solved / Progress</th>
<th width="260">Open Limitation</th>
<th width="200">Hand Model</th>
<th width="160">DoF / Actuation</th>
<th width="200">Tactile Setup</th>
<th width="220">Carrier Platform</th>
<th width="220">Simulation / Data</th>
<th width="240">Teleop / VR Data Chain</th>
<th width="220">SDK / ROS / Code</th>
<th width="180">Evidence Links</th>
</tr>
</thead>
<tbody>
<tr>
<td width="110" nowrap>CoRL 2023</td>
<td width="280"><a href="https://arxiv.org/abs/2309.09979">General In-hand Object Rotation with Vision and Touch</a></td>
<td width="280">Generalize fingertip in-hand rotation across object shapes and axes using vision, touch, and proprioception.</td>
<td width="260">RotateIt trains in Isaac Gym with privileged object properties and distills to a real visuotactile/proprioceptive policy.</td>
<td width="260">Uses low-dimensional contact locations rather than full tactile images; broader long-horizon contact-rich manipulation remains open.</td>
<td width="200">Allegro Hand</td>
<td width="160">16 joints; position commands at 20 Hz; PD torque at 300 Hz</td>
<td width="200">4 omnidirectional vision-based touch sensors at the fingertips; contact-location input</td>
<td width="220">Allegro Hand + Intel RealSense D435</td>
<td width="220">Isaac Gym; curated object datasets; sim-to-real</td>
<td width="240">-</td>
<td width="220">-</td>
<td width="180"><a href="https://arxiv.org/abs/2309.09979">paper</a> / <a href="https://haozhi.io/rotateit/">project</a> / <a href="https://proceedings.mlr.press/v229/qi23a.html">pmlr</a></td>
</tr>
<tr>
<td width="110" nowrap>CoRL 2023</td>
<td width="280"><a href="https://arxiv.org/abs/2311.05779">Language-guided Robot Grasping: CLIP-based Referring Grasp Synthesis in Clutter</a></td>
<td width="280">Language-conditioned grasp synthesis in cluttered indoor scenes.</td>
<td width="260">CROG builds an OCID-based referring-grasp benchmark and learns 4-DoF grasp poses from image-text pairs.</td>
<td width="260">Targets top-down 4-DoF parallel-jaw grasps, not dexterous-hand control.</td>
<td width="200">-</td>
<td width="160">4-DoF grasp poses</td>
<td width="200">-</td>
<td width="220">dual UR5e manipulators + parallel-jaw grippers + Kinect</td>
<td width="220">OCID-derived clutter benchmark; simulation and hardware experiments</td>
<td width="240">-</td>
<td width="220">code</td>
<td width="180"><a href="https://arxiv.org/abs/2311.05779">paper</a> / <a href="https://proceedings.mlr.press/v229/tziafas23a.html">pmlr</a> / <a href="https://github.com/HilbertXu/CROG">code</a></td>
</tr>
<tr>
<td width="110" nowrap>CoRL 2023</td>
<td width="280"><a href="https://openreview.net/forum?id=3mKb5iyZ2V">Reasoning Tuning Grasp: Adapting Multi-Modal Large Language Models for Robotic Grasping</a></td>
<td width="280">Adapt multimodal LLMs to output numerical grasp poses for robotic grasping.</td>
<td width="260">Validated on a grasping benchmark and real-world grasping experiments for robot-arm grasp pose prediction.</td>
<td width="260">-</td>
<td width="200">-</td>
<td width="160">grasp poses for robot arms</td>
<td width="200">-</td>
<td width="220">robot arms</td>
<td width="220">grasping benchmark + real-world grasping experiments</td>
<td width="240">-</td>
<td width="220">-</td>
<td width="180"><a href="https://openreview.net/forum?id=3mKb5iyZ2V">paper</a> / <a href="https://www.jinxuanxu.com/">author page</a></td>
</tr>
<tr>
<td width="110" nowrap>CoRL 2025</td>
<td width="280"><a href="https://arxiv.org/abs/2505.03233">GraspVLA: a Grasping Foundation Model Pre-trained on Billion-scale Synthetic Action Data</a></td>
<td width="280">Scale general robotic grasping with synthetic action pretraining.</td>
<td width="260">Pretrains on SynGrasp-1B generated with synthetic trajectories, photorealistic rendering, and physics validation.</td>
<td width="260">Uses gripper-centric grasping; paper notes smooth-object slip where tactile feedback may help.</td>
<td width="200">parallel gripper / Robotiq 2F-85 in transfer demo</td>
<td width="160">-</td>
<td width="200">-</td>
<td width="220">Franka Emika Panda + RealSense D435i; UR5e + Robotiq 2F-85 in simulation transfer</td>
<td width="220">SynGrasp-1B; CuRobo trajectory generation; Isaac Sim rendering; MuJoCo validation</td>
<td width="240">-</td>
<td width="220">code; real-world controller link in repo</td>
<td width="180"><a href="https://arxiv.org/abs/2505.03233">paper</a> / <a href="https://pku-epic.github.io/GraspVLA-web/">project</a> / <a href="https://github.com/PKU-EPIC/GraspVLA">code</a></td>
</tr>
<tr>
<td width="110" nowrap>CVPR 2025</td>
<td width="280"><a href="https://openaccess.thecvf.com/content/CVPR2025/html/Li_ManipTrans_Efficient_Dexterous_Bimanual_Manipulation_Transfer_via_Residual_Learning_CVPR_2025_paper.html">ManipTrans: Efficient Dexterous Bimanual Manipulation Transfer via Residual Learning</a></td>
<td width="280">Transfer human bimanual manipulation motions to dexterous robotic hands.</td>
<td width="260">Builds DexManipNet by transferring hand-object motions to dexterous hands in Isaac Gym with residual learning.</td>
<td width="260">MoCap lacks tactile feedback; real-world deployment and fine contact remain difficult.</td>
<td width="200">Shadow Hand; Inspire hand; MANO hand; Allegro in comparison</td>
<td width="160">varies by hand morphology</td>
<td width="200">-</td>
<td width="220">dexterous bimanual simulation setup</td>
<td width="220">DexManipNet; human MoCap; Isaac Gym</td>
<td width="240">human MoCap retargeting / residual transfer</td>
<td width="220">-</td>
<td width="180"><a href="https://openaccess.thecvf.com/content/CVPR2025/papers/Li_ManipTrans_Efficient_Dexterous_Bimanual_Manipulation_Transfer_via_Residual_Learning_CVPR_2025_paper.pdf">paper</a></td>
</tr>
<tr>
<td width="110" nowrap>ICML 2024</td>
<td width="280"><a href="https://proceedings.mlr.press/v235/he24o.html">DynSyn: Dynamical Synergistic Representation for Efficient Learning and Control in Overactuated Embodied Systems</a></td>
<td width="280">Reduce control complexity for overactuated embodied systems.</td>
<td width="260">Learns dynamical synergies for efficient control across musculoskeletal control tasks.</td>
<td width="260">Not a paper about a specific dexterous-hand hardware platform.</td>
<td width="200">-</td>
<td width="160">overactuated control systems</td>
<td width="200">-</td>
<td width="220">musculoskeletal models</td>
<td width="220">control benchmarks</td>
<td width="240">-</td>
<td width="220">-</td>
<td width="180"><a href="https://proceedings.mlr.press/v235/he24o/he24o.pdf">paper</a></td>
</tr>
<tr>
<td width="110" nowrap>ICCV 2025</td>
<td width="280"><a href="https://openaccess.thecvf.com/content/ICCV2025/html/He_DexVLG_Dexterous_Vision-Language-Grasp_Model_at_Scale_ICCV_2025_paper.html">DexVLG: Dexterous Vision-Language-Grasp Model at Scale</a></td>
<td width="280">Instruction-aligned part-aware dexterous grasp generation from single-view RGB-D.</td>
<td width="260">Creates DexGraspNet 3.0 with 170M grasp poses across 174K objects and trains a VLM with a flow-matching grasp head.</td>
<td width="260">Generated grasp ranking and some real-world unsafe grasps remain limitations.</td>
<td width="200">ShadowHand</td>
<td width="160">22-D hand pose in model</td>
<td width="200">-</td>
<td width="220">ShadowHand on UR10e + Intel RealSense D415 wrist camera</td>
<td width="220">DexGraspNet 3.0; Isaac Gym part-aware grasp benchmark</td>
<td width="240">-</td>
<td width="220">-</td>
<td width="180"><a href="https://arxiv.org/pdf/2507.02747">paper</a></td>
</tr>
<tr>
<td width="110" nowrap>IROS 2026</td>
<td width="280"><a href="https://arxiv.org/abs/2606.24450">NoContactNoWorries: Estimating Contact through Vision and Proprioception for In-Hand Dexterous Manipulation</a></td>
<td width="280">Estimate fingertip contact without tactile hardware for in-hand dexterous manipulation.</td>
<td width="260">Predicts four fingertip binary contact signals from wrist RGB-D and proprioception and evaluates closed-loop substitution for tactile sensing.</td>
<td width="260">Does not estimate dense contact maps, slip, force distribution, or local stability cues.</td>
<td width="200">LEAP Hand</td>
<td width="160">16-D joint state and commanded joint state</td>
<td width="200">vision+proprioception contact estimation; four binary fingertip contact labels; FSRs for hardware evaluation</td>
<td width="220">LEAP Hand + wrist-mounted Intel RealSense D455</td>
<td width="220">NVIDIA Isaac Gym / PhysX contact labels; real LEAP Hand evaluation</td>
<td width="240">-</td>
<td width="220">-</td>
<td width="180"><a href="https://arxiv.org/abs/2606.24450">paper</a> / <a href="https://soham2560.github.io/no-contact-no-worries/">project</a></td>
</tr>
<tr>
<td width="110" nowrap>ICLR 2026</td>
<td width="280"><a href="https://openreview.net/forum?id=Bf4FeuW0Mr">DemoGrasp: Universal Dexterous Grasping from a Single Demonstration</a></td>
<td width="280">Learn universal dexterous grasping from one successful demonstration.</td>
<td width="260">The released repo trains RL policies from a single demonstration and includes Inspire-hand assets/checkpoints.</td>
<td width="260">-</td>
<td width="200">Inspire tactile hand asset (`inspire_tac`)</td>
<td width="160">-</td>
<td width="200">-</td>
<td width="220">Franka + Inspire hand config (`fr3_inspire_tac`)</td>
<td width="220">IsaacGym Preview 4; Union YCB/UniDex assets; single-demo RL</td>
<td width="240">single demonstration trajectory</td>
<td width="220">code</td>
<td width="180"><a href="https://openreview.net/forum?id=Bf4FeuW0Mr">paper</a> / <a href="https://github.com/BeingBeyond/DemoGrasp">code</a></td>
</tr>
<tr>
<td width="110" nowrap>ICLR 2026</td>
<td width="280"><a href="https://openreview.net/forum?id=80vjyj5o7l">DexNDM: Closing the Reality Gap for Dexterous In-Hand Rotation via Joint-Wise Neural Dynamics Model</a></td>
<td width="280">Close the sim-to-real dynamics gap for generalized in-hand rotation.</td>
<td width="260">Uses joint-wise neural dynamics plus a residual policy to improve real-world in-air rotation across object shapes, wrist orientations, and rotation axes.</td>
<td width="260">Still depends on real transition data; tactile integration is listed as future work, and prior tactile baselines could not be directly replicated on LEAP.</td>
<td width="200">LEAP Hand; Allegro appears in baseline comparison</td>
<td width="160">-</td>
<td width="200">-</td>
<td width="220">LEAP Hand + Franka arm</td>
<td width="220">Isaac Gym simulation; 4,000 real-world training trajectories; autonomous real transition collection</td>
<td width="240">Meta Quest 3 / BunnyVisionPro-derived teleoperation for assembly demos</td>
<td width="220">supplemental code referenced in paper; public project</td>
<td width="180"><a href="https://arxiv.org/abs/2510.08556">paper</a> / <a href="https://meowuu7.github.io/DexNDM/">project</a></td>
</tr>
<tr>
<td width="110" nowrap>ICLR 2026</td>
<td width="280"><a href="https://openreview.net/forum?id=FFxkFMU89E">EgoDex: Learning Dexterous Manipulation from Large-Scale Egocentric Video</a></td>
<td width="280">Provide large-scale egocentric human manipulation data for dexterous policy learning.</td>
<td width="260">Collects 829 hours of 30 Hz 1080p video with 3D hand/head/upper-body pose and language annotations across 194 tabletop tasks.</td>
<td width="260">Human hands/MANO annotations still require retargeting or policy learning for robot hand execution.</td>
<td width="200">human hands / MANO annotations</td>
<td width="160">3D hand-pose annotations; robot-hand DoF not applicable</td>
<td width="200">-</td>
<td width="220">Apple Vision Pro / ARKit capture</td>
<td width="220">EgoDex dataset and benchmark; train/test/additional splits</td>
<td width="240">Apple Vision Pro + ARKit egocentric hand tracking</td>
<td width="220">code/data access scripts</td>
<td width="180"><a href="https://arxiv.org/pdf/2505.11709">paper</a> / <a href="https://github.com/apple/ml-egodex">code</a></td>
</tr>
<tr>
<td width="110" nowrap>ICLR 2026</td>
<td width="280"><a href="https://openreview.net/forum?id=Kt9tJeOwjy">RFS: Reinforcement learning with Residual flow steering for dexterous manipulation</a></td>
<td width="280">RL fine-tuning for dexterous manipulation with residual flow steering.</td>
<td width="260">Adapts pretrained flow-matching policies with PPO/offline residual RL, improving six simulated tasks and real Franka-LEAP grasp/pick-place.</td>
<td width="260">Still needs simulation pretraining plus limited real corrective demonstrations; no tactile hardware is reported.</td>
<td width="200">LEAP Hand</td>
<td width="160">-</td>
<td width="200">-</td>
<td width="220">Franka arm + LEAP Hand</td>
<td width="220">six simulated tasks; sim-to-real pipeline; about 400 Apple Vision Pro AR demos per task; 50 SpaceMouse corrective demos</td>
<td width="240">Apple Vision Pro AR teleoperation; SpaceMouse corrective intervention</td>
<td width="220">project</td>
<td width="180"><a href="https://arxiv.org/abs/2602.01789">paper</a> / <a href="https://weirdlabuw.github.io/rfs/">project</a></td>
</tr>
<tr>
<td width="110" nowrap>ICLR 2026</td>
<td width="280"><a href="https://openreview.net/forum?id=NZDaMcpXZm">Learning to Grasp Anything By Playing with Random Toys</a></td>
<td width="280">Train grasp policies on randomized toys and test zero-shot generalization to real objects.</td>
<td width="260">Reports 80% zero-shot success in ManiSkill YCB simulation, 67% real Franka DROID success on YCB, and 51% real H1-2 plus dexterous hands success.</td>
<td width="260">Checked project page does not state the exact dexterous-hand model, DoF, tactile setup, or SDK.</td>
<td width="200">-</td>
<td width="160">-</td>
<td width="200">-</td>
<td width="220">Franka DROID; H1-2 humanoid with dexterous hands</td>
<td width="220">250 randomized toys; 1,500 Franka toy demos; 500 H1-2 toy demos; ManiSkill/YCB evaluation</td>
<td width="240">teleoperated data collection is implied by demos; exact device not stated</td>
<td width="220">project</td>
<td width="180"><a href="https://openreview.net/forum?id=NZDaMcpXZm">paper</a> / <a href="https://lego-grasp.github.io/">project</a></td>
</tr>
<tr>
<td width="110" nowrap>ICLR 2026</td>
<td width="280"><a href="https://openreview.net/forum?id=aemqAxScl9">SARM: Stage-Aware Reward Modeling for Long Horizon Robot Manipulation</a></td>
<td width="280">Stage-aware reward modeling for long-horizon robot manipulation.</td>
<td width="260">Uses stage labels to filter/reweight demonstrations and reports 83% T-shirt folding from flattened state and 67% from crumpled state.</td>
<td width="260">Not a dexterous-hand hardware paper; depends on large teleoperated video-action datasets and visual reward estimation.</td>
<td width="200">-</td>
<td width="160">-</td>
<td width="200">-</td>
<td width="220">YAM 7-DoF bimanual robot</td>
<td width="220">200 hours of T-shirt folding demonstrations; top and wrist camera videos; joint states/actions; Pi0/LeRobot training</td>
<td width="240">GELLO teleoperation</td>
<td width="220">code; LeRobot integration</td>
<td width="180"><a href="https://arxiv.org/abs/2509.25358">paper</a> / <a href="https://qianzhong-chen.github.io/sarm.github.io/">project</a> / <a href="https://github.com/xdofai/opensarm">code</a> / <a href="https://github.com/huggingface/lerobot/blob/main/docs/source/sarm.mdx">LeRobot</a></td>
</tr>
<tr>
<td width="110" nowrap>ICLR 2026</td>
<td width="280"><a href="https://openreview.net/forum?id=cVX3VqO8BO">UniHM: Unified Dexterous Hand Manipulation with Vision Language Model</a></td>
<td width="280">Unified dexterous-hand manipulation with a vision-language model.</td>
<td width="260">Trains a morphology-agnostic hand codebook/VLM from HOI data and validates cross-embodiment manipulation in simulation and real trials.</td>
<td width="260">Uses RGB-D only; no tactile/force sensing, simplified contact modeling, and hand-token scale remain open limitations.</td>
<td width="200">Shadow, Allegro, Schunk/SVH, LEAP, Ability, Panda gripper retargeting; real Panda Hand, XHand, Inspire Hand</td>
<td width="160">real setup: 2-DoF Panda Hand, 12-DoF XHand, 6-DoF Inspire Hand</td>
<td width="200">-</td>
<td width="220">7-DoF Franka arm + ZED RGB-D camera</td>
<td width="220">DexYCB and OakInk; SAPIEN visualization/simulation checks; HOI-to-robot retargeting</td>
<td width="240">human-object interaction data; no massive real teleoperation dataset</td>
<td width="220">code</td>
<td width="180"><a href="https://arxiv.org/abs/2603.00732">paper</a> / <a href="https://unihm.github.io/">project</a> / <a href="https://github.com/Zhenhao-Zhang/UniHM">code</a></td>
</tr>
<tr>
<td width="110" nowrap>ICLR 2026</td>
<td width="280"><a href="https://openreview.net/forum?id=k8ovuXEQQu">House Of Dextra : Cross-Embodied Co-Design for Dexterous Hands</a></td>
<td width="280">Cross-embodied co-design for dexterous hands.</td>
<td width="260">Searches morphology and policy jointly, then fabricates modular hands and deploys morphology-conditioned policies zero-shot in the real world.</td>
<td width="260">Closed-loop policy is blind: no camera, object-state, or tactile feedback; morphology search is still task-family specific.</td>
<td width="200">generated modular hands; LEAP baseline</td>
<td width="160">variable 3-5 fingers; 2-3 actuated joints / 3-4 servo motors per finger; Dynamixel XL330-M288-T servos</td>
<td width="200">no camera or tactile feedback</td>
<td width="220">modular 3D-printed robot hands; fixed-wrist hand platform</td>
<td width="220">2,000-8,000 generated hand variants; 2,048 parallel evaluations; PPO morphology-conditioned simulation-to-real</td>
<td width="240">-</td>
<td width="220">project/build guide</td>
<td width="180"><a href="https://arxiv.org/abs/2512.03743">paper</a> / <a href="https://an-axolotl.github.io/HouseofDextra/">project</a></td>
</tr>
<tr>
<td width="110" nowrap>ICLR 2026</td>
<td width="280"><a href="https://openreview.net/forum?id=tv0Sz8A9Tc">Robotic Manipulation by Imitating Generated Videos Without Physical Demonstrations</a></td>
<td width="280">Robot manipulation from generated videos without physical demonstrations.</td>
<td width="260">RIGVid extracts 6D object trajectories from filtered generated videos and reports 85% success over four real tasks versus 50% for ReKep.</td>
<td width="260">Not a dexterous-hand paper; failures are mainly from monocular depth and pose-estimation errors, with one reported gripper slip case.</td>
<td width="200">-</td>
<td width="160">parallel-jaw end-effector implied by grasp/retarget pipeline</td>
<td width="200">-</td>
<td width="220">xArm7 robot arm + stationary Orbbec Femto Bolt RGB-D camera</td>
<td width="220">generated videos; VLM filtering; monocular depth; FoundationPose 6D tracking; four real-world tasks</td>
<td width="240">no physical demonstrations; generated-video imitation</td>
<td width="220">project</td>
<td width="180"><a href="https://arxiv.org/abs/2507.00990">paper</a> / <a href="https://rigvid-robot.github.io/">project</a></td>
</tr>
<tr>
<td width="110" nowrap>ICLR 2026</td>
<td width="280"><a href="https://openreview.net/forum?id=wySMuWHmt4">Primary-Fine Decoupling for Action Generation in Robotic Imitation</a></td>
<td width="280">Action generation for robotic imitation via primary/fine decoupling.</td>
<td width="260">PF-DAG outperforms imitation baselines across 56 Adroit/DexArt/MetaWorld tasks and real tactile manipulation tasks.</td>
<td width="260">Real failures still occur under out-of-distribution object placements and intermittent tactile noise.</td>
<td width="200">Shadow Hand, Allegro Hand in simulation; ROBOTERA XHand in real tasks</td>
<td width="160">real XHand setup uses 12-DoF hand; xArm adds 7 DoF</td>
<td width="200">5 fingertips, 120 tactile taxels per fingertip, 3D force vector readings</td>
<td width="220">UFACTORY xArm7 + two-finger gripper; xArm + ROBOTERA XHand</td>
<td width="220">Adroit/DexArt/MetaWorld; MuJoCo/IsaacGym; scripted/RL expert demos; real point cloud/proprioception/tactile logs</td>
<td width="240">GELLO for xArm gripper; Meta Quest 3 hand tracking + AnyTeleop retargeting for XHand</td>
<td width="220">code</td>
<td width="180"><a href="https://arxiv.org/abs/2602.21684">paper</a> / <a href="https://xiaohanlei.github.io/projects/PF-DAG/">project</a> / <a href="https://github.com/XiaohanLei/PF-DAG">code</a></td>
</tr>
<tr>
<td width="110" nowrap>ICLR 2026</td>
<td width="280"><a href="https://openreview.net/forum?id=13jshGCK9i">D-REX: Differentiable Real-to-Sim-to-Real Engine for Learning Dexterous Grasping</a></td>
<td width="280">Differentiable real-to-sim-to-real learning for dexterous grasping.</td>
<td width="260">Builds differentiable MuJoCo/MJCF digital twins, identifies object mass, and trains force-aware grasping policies from human RGB demonstrations.</td>
<td width="260">Current scope is rigid-body and object-specific; force-control effectiveness is unknown for linkage-driven hands such as Inspire.</td>
<td width="200">Allegro Hand; LEAP Hand</td>
<td width="160">both hands have 16 independently actuated DoF; direct-drive brushless motors; LEAP current/torque limiting</td>
<td width="200">no tactile array; uses visual 6D pose plus actuator current/torque limits for force-aware control</td>
<td width="220">7-DoF Franka Emika Panda + Allegro/LEAP; Intel RealSense D435i or iPhone scanning</td>
<td width="220">MuJoCo differentiable physics; MJCF assets from Gaussian/mesh reconstruction; Dex-Retargeting human RGB demos</td>
<td width="240">human RGB videos to robot demonstrations via Dex-Retargeting</td>
<td width="220">code</td>
<td width="180"><a href="https://arxiv.org/abs/2603.01151">paper</a> / <a href="https://drex.github.io/">project</a> / <a href="https://github.com/louhz/D-rex">code</a></td>
</tr>
<tr>
<td width="110" nowrap>ICLR 2026</td>
<td width="280"><a href="https://openreview.net/forum?id=RYwQ0xQcAh">Interaction-aware Representation Modeling With Co-Occurrence Consistency for Egocentric Hand-Object Parsing</a></td>
<td width="280">Egocentric hand-object parsing with interaction-aware representations.</td>
<td width="260">InterFormer improves egocentric hand-object segmentation on EgoHOS in-domain/OOD and mini-HOI4D by modeling contact-aware queries and co-occurrence consistency.</td>
<td width="260">Perception-only method; not a robot dexterous-hand, tactile, control, or SDK contribution.</td>
<td width="200">-</td>
<td width="160">-</td>
<td width="200">vision-based hand-object contact parsing, not tactile sensing</td>
<td width="220">-</td>
<td width="220">EgoHOS; mini-HOI4D; egocentric images with hand/object masks</td>
<td width="240">egocentric human interaction data</td>
<td width="220">code/models promised on paper acceptance</td>
<td width="180"><a href="https://arxiv.org/abs/2602.20597">paper</a> / <a href="https://github.com/yuggiehk/InterFormer">code</a></td>
</tr>
<tr>
<td width="110" nowrap>AAAI 2026</td>
<td width="280"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38873">GRIM: Task-Oriented Grasping with Conditioning on Generative Examples</a></td>
<td width="280">Task-oriented grasping conditioned on generative examples.</td>
<td width="260">Uses web images, human demos, and generative examples as a small memory to transfer 6D task-oriented parallel-jaw grasps; validates on TaskGrasp and Kinova Gen3 Lite.</td>
<td width="260">Not a dexterous-hand hardware paper; semantic alignment quality and generated/web example fidelity remain key failure sources.</td>
<td width="200">-</td>
<td width="160">6D parallel-jaw gripper pose</td>
<td width="200">-</td>
<td width="220">Kinova Gen3 Lite manipulator</td>
<td width="220">TaskGrasp; 210 memory instances from 180 generated frames, 15 web images, and 15 human demonstrations</td>
<td width="240">web images, human demonstrations, and generated videos</td>
<td width="220">project/code/data</td>
<td width="180"><a href="https://arxiv.org/abs/2506.15607">paper</a> / <a href="https://grim-tog.github.io/">project</a></td>
</tr>
<tr>
<td width="110" nowrap>AAAI 2026</td>
<td width="280"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38874">Dexterous Manipulation Transfer via Progressive Kinematic-Dynamic Alignment</a></td>
<td width="280">Dexterous manipulation transfer via kinematic/dynamic alignment.</td>
<td width="260">Transfers human manipulation videos through staged kinematic and dynamic/contact alignment, reaching about 73% average transfer success.</td>
<td width="260">Larger hands such as Allegro and LEAP still struggle on small or slender objects; dynamic multi-contact changes remain future work.</td>
<td width="200">Adroit Hand, Allegro Hand, LEAP Hand</td>
<td width="160">16 DoF for LEAP/Allegro; 24 DoF for Adroit</td>
<td width="200">contact points/contact rewards from datasets or simulation, not tactile hardware</td>
<td width="220">LEAP Hand on robot arm for real-world demonstration</td>
<td width="220">GRAB, DexYCB, ARCTIC; simulated transfer with contact/dynamics optimization</td>
<td width="240">offline human video/demonstration datasets</td>
<td width="220">-</td>
<td width="180"><a href="https://arxiv.org/abs/2511.10987">paper</a> / <a href="https://ojs.aaai.org/index.php/AAAI/article/view/38874">AAAI</a></td>
</tr>
<tr>
<td width="110" nowrap>AAAI 2026</td>
<td width="280"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38892">Learning Object-Centric Motion Priors from Human for Robotic Dexterous Manipulation</a></td>
<td width="280">Learn object-centric motion priors from human motion for robotic dexterous manipulation.</td>
<td width="260">Predicts future hand-object states from HOI data, then uses the object-centric prior to guide RL on grasping, articulated-object, and obstacle tasks.</td>
<td width="260">No tactile sensors; contact is from SAPIEN collision checks, and deployment depends on object pose tracking/calibration.</td>
<td width="200">PSYONIC Ability Hand, ROBOTERA XHand1, Inspire Hand</td>
<td width="160">-</td>
<td width="200">simulation collision contact, not tactile sensing</td>
<td width="220">two xArm-7 arms + dexterous hands + RealSense D435i</td>
<td width="220">DexYCB and ARCTIC HOI data; SAPIEN3/OpenAI-Gymnasium; 1,024 parallel environments</td>
<td width="240">human-object interaction datasets, not online teleoperation</td>
<td width="220">-</td>
<td width="180"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38892">paper</a></td>
</tr>
<tr>
<td width="110" nowrap>AAAI 2026</td>
<td width="280"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38894">Real Garment Benchmark (RGBench): A Comprehensive Benchmark for Robotic Garment Manipulation Featuring a High-Fidelity Scalable Simulator</a></td>
<td width="280">Benchmark and simulate robotic garment manipulation.</td>
<td width="260">RGBench provides 6000+ garment meshes, a high-performance simulator, and measured real garment dynamics for evaluation.</td>
<td width="260">Garment-simulation benchmark rather than dexterous-hand hardware paper.</td>
<td width="200">-</td>
<td width="160">-</td>
<td width="200">-</td>
<td width="220">robotic garment manipulation benchmark</td>
<td width="220">6000+ garment meshes; measured real dynamics; scalable simulator</td>
<td width="240">-</td>
<td width="220">code</td>
<td width="180"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38894">paper</a> / <a href="https://rgbench.github.io/">project</a> / <a href="https://github.com/hwk0809/RGBench">code</a></td>
</tr>
<tr>
<td width="110" nowrap>AAAI 2026</td>
<td width="280"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38940">GraphGrasp: Lightweight and Efficient Graph-Guided 6-DoF Robotic Grasp Pose Estimation Network</a></td>
<td width="280">Lightweight graph-guided 6-DoF robotic grasp pose estimation.</td>
<td width="260">Evaluates graph-guided 6-DoF grasp pose prediction on GraspNet-1Billion and real-world grasp pose detection with fewer parameters than baselines.</td>
<td width="260">Parallel-gripper pose estimator rather than dexterous-hand hardware; no tactile/contact-rich policy is reported.</td>
<td width="200">-</td>
<td width="160">6-DoF parallel-gripper pose and opening width</td>
<td width="200">-</td>
<td width="220">Intel RealSense D435 used for real-world grasp-pose detection</td>
<td width="220">GraspNet-1Billion dataset; point-cloud graph grasp prediction</td>
<td width="240">-</td>
<td width="220">code</td>
<td width="180"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38940">paper</a> / <a href="https://github.com/BIT-robot-group/GraphGrasp">code</a></td>
</tr>
<tr>
<td width="110" nowrap>AAAI 2026</td>
<td width="280"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38953">DexGraspVLA: A Vision-Language-Action Framework Towards General Dexterous Grasping</a></td>
<td width="280">Language-guided general dexterous grasping in clutter.</td>
<td width="260">Uses a pretrained VLM planner and diffusion action controller; AAAI page reports 90+% success in unseen cluttered scenes.</td>
<td width="260">Hardware-related code is not open-sourced; public repo exposes non-hardware controller/planner code and a small demo dataset.</td>
<td width="200">-</td>
<td width="160">13-DoF right arm+hand action/state in released demo data</td>
<td width="200">-</td>
<td width="220">-</td>
<td width="220">51 human demonstration samples in Zarr example; real deployment logs; diffusion controller</td>
<td width="240">human demonstration data; optional manual bbox mode</td>
<td width="220">code; planner/controller configs; no hardware code</td>
<td width="180"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38953">paper</a> / <a href="https://dexgraspvla.github.io/">project</a> / <a href="https://github.com/Psi-Robot/DexGraspVLA">code</a></td>
</tr>
<tr>
<td width="110" nowrap>AAAI 2026</td>
<td width="280"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38957">Effective Robotic Cloth Grasping Through Suppressing False Discoveries</a></td>
<td width="280">Robotic cloth grasping through false-discovery suppression.</td>
<td width="260">Combines annotation-free cloth segmentation with depth/wrinkle-based grasp point selection and deploys a Baxter cloth storage system.</td>
<td width="260">Not a dexterous-hand paper; method is cloth-specific, vision/depth based, and does not use tactile feedback.</td>
<td width="200">-</td>
<td width="160">-</td>
<td width="200">-</td>
<td width="220">Baxter robot with RGB-D/depth perception</td>
<td width="220">real cluttered-cloth experiments; unsupervised segmentation; depth wrinkle analysis</td>
<td width="240">-</td>
<td width="220">-</td>
<td width="180"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38957">paper</a></td>
</tr>
<tr>
<td width="110" nowrap>CVPR 2026</td>
<td width="280"><a href="https://arxiv.org/abs/2603.22264">UniDex: A Robot Foundation Suite for Universal Dexterous Hand Control from Egocentric Human Videos</a></td>
<td width="280">Universal dexterous-hand control from egocentric human videos.</td>
<td width="260">Builds UniDex-Dataset with 50K trajectories across eight dexterous hands and trains a 3D VLA policy.</td>
<td width="260">Retargeting human videos to each target robot hand remains necessary.</td>
<td width="200">Allegro, Ability, Inspire, Leap, Oymotion, Shadow, Wuji, XHand</td>
<td width="160">8 hands, 6-24 DoFs</td>
<td width="200">-</td>
<td width="220">Franka Panda arm + RealSense L515 in described setup; multiple hand embodiments</td>
<td width="220">UniDex-Dataset; H2O / HOI4D / HOT3D / TACO retargeting; 50K trajectories</td>
<td width="240">egocentric videos; human-in-the-loop retargeting; Apple Vision Pro teleoperation for downstream demos</td>
<td width="220">code; retargeting scripts; Hugging Face dataset</td>
<td width="180"><a href="https://arxiv.org/abs/2603.22264">paper</a> / <a href="https://unidex-ai.github.io/">project</a> / <a href="https://github.com/unidex-ai/UniDex">code</a> / <a href="https://huggingface.co/UniDex-ai/UniDex">hf</a></td>
</tr>
<tr>
<td width="110" nowrap>NeurIPS 2025</td>
<td width="280"><a href="https://arxiv.org/pdf/2511.01276">Generalizable Dexterous Grasp Generation via Contact Map Transfer</a></td>
<td width="280">Generate dexterous grasps by transferring contact maps.</td>
<td width="260">Uses contact-map-conditioned diffusion and evaluates ShadowHand grasps in Isaac Gym; real demo uses Inspire hand on a humanoid platform.</td>
<td width="260">Tactile sensing is not used as hardware feedback; contact maps are generation conditions.</td>
<td width="200">ShadowHand for training/evaluation; Inspire hand for real demo</td>
<td width="160">ShadowHand k=24 in formulation; 6-DOF hand-root execution pose</td>
<td width="200">contact maps, not tactile sensors</td>
<td width="220">humanoid platform with Inspire hand; ZED head camera + two RealSense cameras</td>
<td width="220">Isaac Gym success metrics; contact-map diffusion</td>
<td width="240">human-to-robot grasp retargeting from prior pipeline</td>
<td width="220">code</td>
<td width="180"><a href="https://arxiv.org/pdf/2511.01276">paper</a> / <a href="https://cmtdiffusion.github.io/">project</a> / <a href="https://github.com/Yiyao-Ma/cmtdiffusion">code</a></td>
</tr>
<tr>
<td width="110" nowrap>NeurIPS 2025</td>
<td width="280"><a href="https://arxiv.org/abs/2506.02489">Grasp2Grasp: Vision-Based Dexterous Grasp Translation via Schrödinger Bridges</a></td>
<td width="280">Translate functional grasp intent across hand morphologies.</td>
<td width="260">Uses Schrodinger Bridge translation across Human-&gt;Allegro, Human-&gt;Shadow, and Shadow-&gt;Allegro settings.</td>
<td width="260">Focuses on grasp translation, not full long-horizon manipulation or tactile feedback.</td>
<td width="200">human hand, Allegro Hand, Shadow Hand</td>
<td width="160">Allegro 16 DoFs; Shadow 22 DoFs</td>
<td width="200">-</td>
<td width="220">simulation evaluation in Isaac Gym</td>
<td width="220">vision-conditioned grasp translation; Isaac Gym success tests</td>
<td width="240">cross-hand translation, not teleoperation</td>
<td width="220">code</td>
<td width="180"><a href="https://arxiv.org/abs/2506.02489">paper</a> / <a href="https://grasp2grasp.github.io/">project</a> / <a href="https://github.com/n3il666/grasp2grasp">code</a></td>
</tr>
<tr>
<td width="110" nowrap>NeurIPS 2025</td>
<td width="280"><a href="https://arxiv.org/abs/2506.19212">Scaffolding Dexterous Manipulation with Vision-Language Models</a></td>
<td width="280">Use VLM-generated scaffolds to train dexterous manipulation policies.</td>
<td width="260">Generates keypoint/wrist/object trajectories with VLMs, then trains residual closed-loop RL policies in simulation and transfers to real hardware.</td>
<td width="260">Failures still stem from incomplete trajectory tracking and VLM keypoint errors.</td>
<td width="200">Allegro Hand</td>
<td width="160">16-DoF Allegro hand</td>
<td width="200">-</td>
<td width="220">16-DoF Allegro + 7-DoF KUKA LBR iiwa 14 + ZED 1 stereo camera</td>
<td width="220">ManiSkill simulation; eight simulated tasks; real-world three-task evaluation</td>
<td width="240">no human demonstrations; VLM-generated trajectories</td>
<td width="220">code; ROS launch snippets for ZED and Allegro</td>
<td width="180"><a href="https://arxiv.org/abs/2506.19212">paper</a> / <a href="https://sites.google.com/view/dexterous-vlm-scaffolding">project</a> / <a href="https://github.com/vdebakker/vlm-scaffolding">code</a></td>
</tr>
<tr>
<td width="110" nowrap>NeurIPS 2025</td>
<td width="280"><a href="https://arxiv.org/abs/2505.11032">DexGarmentLab: Dexterous Garment Manipulation Environment with Generalizable Policy</a></td>
<td width="280">Dexterous bimanual garment manipulation environment and policy learning.</td>
<td width="260">Provides 15 garment tasks across 8 categories, assets, IsaacSim environment, and HALO policy; real setup uses RealMan arms with PsiBot hands.</td>
<td width="260">Single-garment tasks only; challenging garment geometry and accurate grasping/placement remain limitations.</td>
<td width="200">ShadowHand in simulation; PsiBot G0-R in real setup</td>
<td width="160">ShadowHand 24 finger joints; real PsiBot G0-R listed as 6-DoF robotic hand</td>
<td width="200">-</td>
<td width="220">two UR10e + ShadowHands in simulation; two RealMan RM75-6F + PsiBot G0-R + RealSense D435 in real setup</td>
<td width="220">IsaacSim 4.5.0; DexGarmentLab assets/dataset; Hugging Face assets</td>
<td width="240">Leap Motion teleoperation guidance; trajectory retargeting from one demo</td>
<td width="220">code; Hugging Face assets</td>
<td width="180"><a href="https://arxiv.org/abs/2505.11032">paper</a> / <a href="https://wayrise.github.io/DexGarmentLab/">project</a> / <a href="https://github.com/wayrise/DexGarmentLab">code</a> / <a href="https://huggingface.co/datasets/wayrise/DexGarmentLab">hf</a></td>
</tr>
<tr>
<td width="110" nowrap>CVPR 2025</td>
<td width="280"><a href="https://arxiv.org/abs/2412.02699">UniGraspTransformer: Simplified Policy Distillation for Scalable Dexterous Robotic Grasping</a></td>
<td width="280">Scale policy distillation for dexterous robotic grasping.</td>
<td width="260">Trains per-object RL experts in Isaac Gym and distills them into a Transformer policy for Shadow Hand grasping.</td>
<td width="260">Primarily simulation/state- and vision-based evaluation; no tactile hardware is reported.</td>
<td width="200">Shadow Hand</td>
<td width="160">18 active finger DoFs + 6 wrist DoFs; 24 action actuators</td>
<td width="200">-</td>
<td width="220">simulated Shadow Hand tabletop grasping</td>
<td width="220">Isaac Gym 3.0; expert trajectories; policy distillation</td>
<td width="240">-</td>
<td width="220">code; IsaacGym assets/models</td>
<td width="180"><a href="https://arxiv.org/abs/2412.02699">paper</a> / <a href="https://dexhand.github.io/UniGraspTransformer/">project</a> / <a href="https://github.com/microsoft/UniGraspTransformer">code</a></td>
</tr>
<tr>
<td width="110" nowrap>CVPR 2025</td>
<td width="280"><a href="https://arxiv.org/abs/2503.08257">DexGrasp Anything: Towards Universal Robotic Dexterous Grasping with Physics Awareness</a></td>
<td width="280">Generate physically usable dexterous grasps for arbitrary objects.</td>
<td width="260">Adds physics constraints to diffusion generation and releases a DGA dataset with 3.4M grasp poses for 15K+ objects.</td>
<td width="260">Tactile feedback integration is noted as future work; real execution is mainly post-grasp stability / IK demonstrations.</td>
<td width="200">ShadowHand</td>
<td width="160">24-D ShadowHand pose in formulation</td>
<td width="200">-</td>
<td width="220">real ShadowHand robot for qualitative deployment</td>
<td width="220">DGA dataset; Real+Sim; Isaac Gym filtering/evaluation; Hugging Face dataset</td>
<td width="240">GRAB-to-robot retargeting used in dataset construction</td>
<td width="220">code; dataset; checkpoints</td>
<td width="180"><a href="https://arxiv.org/abs/2503.08257">paper</a> / <a href="https://dexgraspanything.github.io/">project</a> / <a href="https://github.com/4DVLab/DexGrasp-Anything">code</a> / <a href="https://huggingface.co/datasets/GaussionZhong/DexGrasp-Anything">hf</a></td>
</tr>
<tr>
<td width="110" nowrap>CVPR 2025</td>
<td width="280"><a href="https://cvpr.thecvf.com/virtual/2025/poster/32440">ZeroGrasp: Zero-Shot Shape Reconstruction Enabled Robotic Grasping</a></td>
<td width="280">Use zero-shot shape reconstruction to support robotic grasping.</td>
<td width="260">Jointly predicts 3D shape reconstruction and 6D grasp poses, trained with ZeroGrasp-11B and evaluated on GraspNet-1B plus real Franka/Robotiq experiments.</td>
<td width="260">Parallel-gripper grasping, not dexterous-hand hardware; depends on RGB-D reconstruction quality under occlusion.</td>
<td width="200">-</td>
<td width="160">two-finger parallel gripper model; Robotiq 2F-85 in real setup</td>
<td width="200">-</td>
<td width="220">Franka Emika Panda + Robotiq 2F-85</td>
<td width="220">ZeroGrasp-11B: 1M RGB-D images, 11.3B 6D grasp annotations, 12K Objaverse-LVIS objects; GraspNet-1B benchmark</td>
<td width="240">-</td>
<td width="220">code</td>
<td width="180"><a href="https://arxiv.org/abs/2504.10857">paper</a> / <a href="https://cvpr.thecvf.com/virtual/2025/poster/32440">CVPR</a> / <a href="https://sh8.io/#/zerograsp">project</a> / <a href="https://github.com/sh8/ZeroGrasp">code</a></td>
</tr>
<tr>
<td width="110" nowrap>arXiv 2026</td>
<td width="280"><a href="https://arxiv.org/abs/2602.16710">EgoScale: Scaling Dexterous Manipulation with Diverse Egocentric Human Data</a></td>
<td width="280">Scale human-to-robot transfer for high-DoF dexterous manipulation.</td>
<td width="260">Trains a VLA model on 20,854 hours of action-labeled egocentric human video and uses aligned human-robot mid-training for dexterous transfer.</td>
<td width="260">No formal venue was found; exact deployed hand models are not stated on the arXiv abstract page.</td>
<td width="200">22-DoF dexterous robotic hand; lower-DoF transfer hands</td>
<td width="160">22 DoF for the main reported hand</td>
<td width="200">-</td>
<td width="220">real dexterous robot setups</td>
<td width="220">20,854 hours of action-labeled egocentric human video; aligned human-robot mid-training</td>
<td width="240">human-to-robot transfer from egocentric video</td>
<td width="220">project page</td>
<td width="180"><a href="https://arxiv.org/abs/2602.16710">paper</a> / <a href="https://research.nvidia.com/labs/gear/egoscale/">project</a></td>
</tr>
<tr>
<td width="110" nowrap>CVPR 2026</td>
<td width="280"><a href="https://openaccess.thecvf.com/content/CVPR2026/papers/Jiang_Cross-Hand_Latent_Representation_for_Vision-Language-Action_Models_CVPR_2026_paper.pdf">XL-VLA: Cross-Hand Latent Representation for Vision-Language-Action Models</a></td>
<td width="280">Share one VLA action space across different dexterous hands.</td>
<td width="260">Learns a latent action representation that decodes into different dexterous hand joint trajectories.</td>
<td width="260">Requires per-hand encoders/decoders; tactile sensing is not reported as a core input.</td>
<td width="200">Ability Hand, Paxini DexH13, X-Hand1, Inspire hand</td>
<td width="160">hand-specific DoFs</td>
<td width="200">-</td>
<td width="220">multi-hand real robot settings</td>
<td width="220">cross-hand VLA training and latent action evaluation</td>
<td width="240">retargeting through latent action decoders</td>
<td width="220">code</td>
<td width="180"><a href="https://xl-vla.github.io/">project</a> / <a href="https://github.com/EmptyBlueBox/DexLatent">code</a> / <a href="https://openaccess.thecvf.com/content/CVPR2026/papers/Jiang_Cross-Hand_Latent_Representation_for_Vision-Language-Action_Models_CVPR_2026_paper.pdf">paper</a></td>
</tr>
<tr>
<td width="110" nowrap>ECCV 2026</td>
<td width="280"><a href="https://arxiv.org/abs/2512.13644">World Models for Learning Dexterous Hand-Object Interactions from Human Videos</a></td>
<td width="280">Predict future dexterous hand-object interaction states from human videos.</td>
<td width="260">DexWM uses finger keypoints and a hand-consistency loss, training on over 900 hours of human and non-dexterous robot data.</td>
<td width="260">World-model planning remains action-optimization-heavy; tactile sensing is not reported.</td>
<td width="200">Allegro gripper / hand</td>
<td width="160">-</td>
<td width="200">-</td>
<td width="220">Franka Panda arm with Allegro gripper</td>
<td width="220">900+ hours of human and non-dexterous robot data; RoboCasa fine-tuning noted on the project page</td>
<td width="240">finger-keypoint action representation from egocentric videos</td>
<td width="220">-</td>
<td width="180"><a href="https://raktimgg.github.io/dexwm/">project</a> / <a href="https://arxiv.org/abs/2512.13644">paper</a></td>
</tr>
<tr>
<td width="110" nowrap>arXiv 2026</td>
<td width="280"><a href="https://arxiv.org/abs/2512.24210">GR-Dexter Technical Report</a></td>
<td width="280">Build a bimanual VLA stack around high-DoF dexterous hands.</td>
<td width="260">Combines ByteDexter V2 hardware, bimanual teleoperation, and co-training with robot, vision-language, and cross-embodiment data.</td>
<td width="260">Technical report rather than a formal venue paper; reproducible public dataset/SDK coverage needs checking before platform adoption.</td>
<td width="200">ByteDexter V2</td>
<td width="160">21 DoF; five fingertips with high-density piezoresistive normal-force arrays</td>
<td width="200">piezoresistive fingertip arrays</td>
<td width="220">two Franka arms with ByteDexter V2 hands</td>
<td width="220">teleoperated robot trajectories plus cross-embodiment and vision-language data</td>
<td width="240">Manus Metagloves, Meta Quest tracking, whole-body control retargeting</td>
<td width="220">project page</td>
<td width="180"><a href="https://byte-dexter.github.io/gr-dexter/">project</a> / <a href="https://arxiv.org/abs/2512.24210">paper</a></td>
</tr>
<tr>
<td width="110" nowrap>arXiv 2025</td>
<td width="280"><a href="https://arxiv.org/abs/2511.01177">Scaling Cross-Embodiment World Models for Dexterous Manipulation</a></td>
<td width="280">Use world models as a shared interface across hand morphologies.</td>
<td width="260">Represents hands and objects as 3D particles, trains on diverse simulated robot hands plus real human hands, and uses model-based planning on new hardware.</td>
<td width="260">No formal venue was found; exact per-hand SDK and tactile configuration are not specified in the abstract evidence.</td>
<td width="200">multiple simulated robot hands and real human hands</td>
<td width="160">varied DoFs</td>
<td width="200">-</td>
<td width="220">novel hardware deployment reported, exact public model not found</td>
<td width="220">simulated exploration data plus real human-hand data</td>
<td width="240">particle-based cross-embodiment action representation</td>
<td width="220">-</td>
<td width="180"><a href="https://arxiv.org/abs/2511.01177">paper</a></td>
</tr>
</tbody>
</table>

#### tactile/contact-rich

Total: 28 papers.

<table width="2770">
<thead>
<tr>
<th width="110" nowrap>Venue/Year</th>
<th width="280">Paper/Method</th>
<th width="260">Research Problem</th>
<th width="180">Tactile Type</th>
<th width="200">Tactile Density / Location</th>
<th width="140" nowrap>Closed-loop Control?</th>
<th width="240">Manipulation Task</th>
<th width="200">Hardware Used</th>
<th width="200">Carrier Platform</th>
<th width="220">Simulation / Dataset</th>
<th width="260">Solved</th>
<th width="260">Open Limitation</th>
<th width="220">Code / Data / Project</th>
</tr>
</thead>
<tbody>
<tr>
<td width="110" nowrap>CoRL 2024</td>
<td width="280"><a href="https://arxiv.org/abs/2410.24091">3D-ViTac: Learning Fine-Grained Manipulation with Visuo-Tactile Sensing</a></td>
<td width="260">Fine-grained manipulation with 3D visual-tactile point representations.</td>
<td width="180">visuo-tactile</td>
<td width="200">four tactile pads, each 16x16 / 256 units, 3 mm^2 per sensing point; 1,024 tactile units across the bimanual system</td>
<td width="140" nowrap>yes</td>
<td width="240">egg steaming, insertion, grape retrieval, and other fine-grained manipulation tasks</td>
<td width="200">3D-ViTac visuo-tactile pads on soft fin-shaped grippers; RealSense RGB-D cameras</td>
<td width="200">bimanual teleoperation system with two master robots and two puppet robots</td>
<td width="220">real robot demonstrations at 10 Hz; tactile sensors, multi-view RGB-D, actions and joint states; hardware tutorial/code</td>
<td width="260">Represents touch as 3D tactile points and uses them for policy learning in fine manipulation.</td>
<td width="260">Hardware is custom and task demonstrations are limited to the reported bimanual setup.</td>
<td width="220"><a href="https://arxiv.org/abs/2410.24091">paper</a> / <a href="https://binghao-huang.github.io/3D-ViTac/">project</a> / <a href="https://github.com/binghao-huang/3D-ViTac_Tactile_Hardware">hardware</a></td>
</tr>
<tr>
<td width="110" nowrap>CoRL 2023</td>
<td width="280"><a href="https://arxiv.org/abs/2210.14210">Midastouch: Monte-carlo inference over distributions across sliding touch</a></td>
<td width="260">Localize a vision-based tactile sensor on an object surface from sliding touch.</td>
<td width="180">optical tactile</td>
<td width="200">DIGIT tactile images / local heightmaps during sliding contact</td>
<td width="140" nowrap>no</td>
<td width="240">sliding-touch object localization and YCB-Slide interactions</td>
<td width="200">DIGIT / vision-based tactile sensor</td>
<td width="200">tactile sensor sliding on YCB objects</td>
<td width="220">YCB-Slide real + simulated sliding-touch dataset</td>
<td width="260">Performs online global localization from posed tactile images and learned tactile geometry codes.</td>
<td width="260">Manipulation is localization-centric, not a full closed-loop dexterous policy.</td>
<td width="220"><a href="https://arxiv.org/abs/2210.14210">paper</a> / <a href="https://suddhu.github.io/midastouch-tactile/">project</a> / <a href="https://github.com/facebookresearch/MidasTouch">code</a></td>
</tr>
<tr>
<td width="110" nowrap>CoRL 2023</td>
<td width="280"><a href="https://proceedings.mlr.press/v205/zhong23a.html">Touching a NeRF: Leveraging Neural Radiance Fields for Tactile Sensory Data Generation</a></td>
<td width="260">Generate tactile sensory data using object NeRF representations.</td>
<td width="180">optical tactile</td>
<td width="200">DIGIT tactile images; simulated DIGIT via TACTO; OmniTact transfer experiment</td>
<td width="140" nowrap>no</td>
<td width="240">tactile data generation / perception training</td>
<td width="200">DIGIT sensor attached to robot end effector; OmniTact in simulated transfer test</td>
<td width="200">robot end-effector tactile data collection setup</td>
<td width="220">YCB objects; NeRF-rendered RGB-D; cGAN tactile generation; 398 real touches / 19,900 frames; simulated TACTO dataset</td>
<td width="260">Generates tactile images for novel object views and improves tactile classification with generated data.</td>
<td width="260">Requires training a NeRF per object; focuses on rigid objects and data generation, not closed-loop control.</td>
<td width="220"><a href="https://proceedings.mlr.press/v205/zhong23a.html">paper</a> / <a href="https://proceedings.mlr.press/v205/zhong23a/zhong23a.pdf">pdf</a></td>
</tr>
<tr>
<td width="110" nowrap>CoRL 2021</td>
<td width="280"><a href="https://arxiv.org/abs/2012.05205">Tactile object pose estimation from the first touch with geometric contact rendering</a></td>
<td width="260">Estimate object pose from a single tactile contact.</td>
<td width="180">optical tactile</td>
<td width="200">first-touch tactile imprint/contact observation</td>
<td width="140" nowrap>no</td>
<td width="240">object pose estimation from first touch</td>
<td width="200">-</td>
<td width="200">-</td>
<td width="220">geometric contact rendering; real tactile localization page</td>
<td width="260">Uses geometric contact rendering to infer object pose from first touch.</td>
<td width="260">Mainly pose estimation; full manipulation policy and tactile density remain unspecified.</td>
<td width="220"><a href="https://arxiv.org/abs/2012.05205">paper</a> / <a href="https://proceedings.mlr.press/v155/villalonga21a.html">pmlr</a> / <a href="http://mcube.mit.edu/research/tactile_loc_first_touch.html">project</a></td>
</tr>
<tr>
<td width="110" nowrap>CoRL 2023</td>
<td width="280"><a href="https://arxiv.org/abs/2210.01116">That Sounds Right: Auditory Self-Supervision for Dynamic Robot Manipulation</a></td>
<td width="260">Use contact audio as self-supervision for dynamic manipulation.</td>
<td width="180">audio/contact</td>
<td width="200">audio events from robot-object contact</td>
<td width="140" nowrap>yes</td>
<td width="240">dynamic manipulation tasks with auditory feedback</td>
<td width="200">-</td>
<td width="200">robot manipulation setup</td>
<td width="220">audio-robot-learning project data/code page</td>
<td width="260">Uses auditory contact cues to supervise dynamic manipulation without manual labels.</td>
<td width="260">Audio is indirect contact sensing and does not provide dense tactile force fields.</td>
<td width="220"><a href="https://arxiv.org/abs/2210.01116">paper</a> / <a href="https://audio-robot-learning.github.io">project</a></td>
</tr>
<tr>
<td width="110" nowrap>ICLR 2026</td>
<td width="280"><a href="https://openreview.net/forum?id=dT3ZciXvNX">DexMove: Learning Tactile-Guided Non-Prehensile Manipulation with Dexterous Hands</a></td>
<td width="260">Learn tactile-guided non-prehensile object moving with dexterous hands.</td>
<td width="180">optical tactile</td>
<td width="200">wearable multi-finger vision-based tactile sensors; marker displacement on PP-Tac-based gel surface</td>
<td width="140" nowrap>yes</td>
<td width="240">non-prehensile tabletop object moving; sorting/tidying demos</td>
<td width="200">wearable visuo-tactile device for human contact data; PP-Tac-derived tactile sensor</td>
<td width="200">-</td>
<td width="220">physics-simulation trajectory pruning and force augmentation; human tactile demonstrations; flow policy</td>
<td width="260">Manipulates six objects with 77.8% real-world success and combines synthesized force-aware trajectories with tactile demonstrations.</td>
<td width="260">Public project page does not state the target robot hand model/DoF or robot SDK.</td>
<td width="220"><a href="https://openreview.net/forum?id=dT3ZciXvNX">paper</a> / <a href="https://peilin-666.github.io/projects/DexMove/">project</a> / <a href="https://github.com/bigai-ai/PP-Tac/tree/main">PP-Tac code</a></td>
</tr>
<tr>
<td width="110" nowrap>ICLR 2026</td>
<td width="280"><a href="https://openreview.net/forum?id=ndilONnABZ">AnyTouch 2: General Optical Tactile Representation Learning For Dynamic Tactile Perception</a></td>
<td width="260">Learn general optical tactile representations for dynamic tactile perception.</td>
<td width="180">optical tactile / force/torque</td>
<td width="200">ToucHD dynamic tactile data; Sparsh GelSight/DIGIT force and pose datasets; FastUMI tactile gripper data</td>
<td width="140" nowrap>yes</td>
<td width="240">tactile grasping, whiteboard wiping, USB insertion, chip moving</td>
<td width="200">GelSight, DIGIT, FastUMI grippers with tactile sensors, ToucHD collection hardware</td>
<td width="200">real manipulation setups</td>
<td width="220">ToucHD; Sparsh; Touch-and-Go; Cloth; real manipulation data</td>
<td width="260">Learns force-aware dynamic tactile features across datasets and sensors.</td>
<td width="260">Cross-sensor generalization is improving but still depends on available paired datasets.</td>
<td width="220"><a href="https://openreview.net/forum?id=ndilONnABZ">paper</a> / <a href="https://gewu-lab.github.io/AnyTouch2/">project</a> / <a href="https://github.com/GeWu-Lab/AnyTouch2">code</a> / <a href="https://huggingface.co/collections/BAAI/touchd">hf</a></td>
</tr>
<tr>
<td width="110" nowrap>ICLR 2026</td>
<td width="280"><a href="https://openreview.net/forum?id=hU2gT2Ucua">APPLE: Toward General Active Perception via Reinforcement Learning</a></td>
<td width="260">General active perception policy learning, including tactile exploration.</td>
<td width="180">binary contact</td>
<td width="200">Tactile MNIST-style active tactile observations</td>
<td width="140" nowrap>yes</td>
<td width="240">active perception / tactile exploration</td>
<td width="200">-</td>
<td width="200">-</td>
<td width="220">Tactile MNIST benchmark and active perception tasks</td>
<td width="260">Trains active policies that acquire sparse tactile information for classification/regression.</td>
<td width="260">Not a contact-rich manipulation hardware paper.</td>
<td width="220"><a href="https://openreview.net/forum?id=hU2gT2Ucua">paper</a> / <a href="https://timschneider42.github.io/apple">project</a></td>
</tr>
<tr>
<td width="110" nowrap>AAAI 2026</td>
<td width="280"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38882">STOLA: Self-Adaptive Touch-Language Framework for Tactile Commonsense Reasoning in Open-Ended Scenarios</a></td>
<td width="260">Touch-language commonsense reasoning in open-ended scenarios.</td>
<td width="180">touch-language</td>
<td width="200">individual tactile images and tactile time-series; GelSight and GelSight Mini configurations</td>
<td width="140" nowrap>no</td>
<td width="240">open-ended tactile commonsense QA and reasoning</td>
<td width="200">GelSight / GelSight Mini data sources</td>
<td width="200">-</td>
<td width="220">PHYSICLEAR, TactileBench, Touch100k-derived/self-constructed tactile instruction data</td>
<td width="260">Introduces MoE-based touch-language reasoning and a free-form tactile commonsense benchmark covering 8 properties and 4 interaction characteristics.</td>
<td width="260">Representation/reasoning benchmark only; no closed-loop robot control or tactile manipulation hardware.</td>
<td width="220"><a href="https://arxiv.org/abs/2505.04201">paper</a> / <a href="https://cocacola-lab.github.io/SToLa-Page/">project</a></td>
</tr>
<tr>
<td width="110" nowrap>AAAI 2026</td>
<td width="280"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38915">TouchFormer: A Robust Transformer-based Framework for Multimodal Material Perception</a></td>
<td width="260">Robust multimodal material perception.</td>
<td width="180">force/torque</td>
<td width="200">uSkin fingertip measuring normal force, friction force, and acceleration; multimodal sound/touch sequences</td>
<td width="140" nowrap>no</td>
<td width="240">vision-free material classification and material sorting</td>
<td width="200">uSkin tactile fingertip; RealMan RM65-B 6-DoF arm with TESOLLO hand for sorting demo</td>
<td width="200">RealMan RM65-B + TESOLLO</td>
<td width="220">LMTHM and FISHM material datasets; FISHM fine-tuning after LMTHM training</td>
<td width="260">Improves robust multimodal material perception under noisy/missing modalities and validates a robot material-sorting scenario.</td>
<td width="260">Perception-guided sorting demo, not a closed-loop force-control manipulation policy.</td>
<td width="220"><a href="https://arxiv.org/abs/2511.19509">paper</a></td>
</tr>
<tr>
<td width="110" nowrap>AAAI 2026</td>
<td width="280"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38956">Collaborative Representation Learning for Alignment of Tactile, Language, and Vision Modalities</a></td>
<td width="260">Align tactile, language, and vision representations.</td>
<td width="180">visuo-tactile / touch-language</td>
<td width="200">GelSight, DIGIT, DuraGel, GelSight Mini datasets; TacQuad includes about 55k samples</td>
<td width="140" nowrap>no</td>
<td width="240">cross-modal representation learning</td>
<td width="200">GelSight/DIGIT-style tactile image datasets</td>
<td width="200">-</td>
<td width="220">TAG, Octopi, TacQuad and other real-world tactile datasets; RSS evaluation framework</td>
<td width="260">TLV-CoRe uses SAM/UBA to reduce sensor-specific bias and improve sensor-agnostic tactile-language-vision alignment.</td>
<td width="260">No real-time robot or real manipulation evaluation is reported; expanding to real-time tasks is stated as future work.</td>
<td width="220"><a href="https://arxiv.org/abs/2511.11512">paper</a> / <a href="https://ojs.aaai.org/index.php/AAAI/article/view/38956">AAAI</a></td>
</tr>
<tr>
<td width="110" nowrap>ICML 2026</td>
<td width="280"><a href="https://icml.cc/virtual/2026/poster/66793">Cross-Tactile Sensor Representation Learning</a></td>
<td width="260">Sensor-agnostic tactile representation learning across visuo-tactile sensors.</td>
<td width="180">visuo-tactile</td>
<td width="200">aligned synthetic data across sensor domains + real multimodal tactile data</td>
<td width="140" nowrap>no</td>
<td width="240">cross-sensor tactile representation learning</td>
<td width="200">-</td>
<td width="200">-</td>
<td width="220">synthetic aligned tactile data + real multimodal tactile data</td>
<td width="260">Uses a Cross-Sensor Modulator and two-stage training for multi-sensor generalization.</td>
<td width="260">-</td>
<td width="220"><a href="https://icml.cc/virtual/2026/poster/66793">paper</a></td>
</tr>
<tr>
<td width="110" nowrap>ICML 2026</td>
<td width="280"><a href="https://icml.cc/virtual/2026/poster/65669">Tabero: Learning Gentle Manipulation with Closed-Loop Force Feedback from Vision, Touch, and Language</a></td>
<td width="260">Learn gentle manipulation from vision, touch, language, and force feedback.</td>
<td width="180">force/torque / visuo-tactile / touch-language</td>
<td width="200">simulated GelSight 320x240 RGB tactile images; left/right fingertip 3D force vectors; synchronized at 20 Hz</td>
<td width="140" nowrap>yes</td>
<td width="240">gentle vs firm grasp/manipulation with force control</td>
<td width="200">tactile-equipped Franka gripper in Isaac Lab/Isaac Sim</td>
<td width="200">Franka-style tactile gripper simulation</td>
<td width="220">Tabero benchmark/model suite; replayed open-source trajectories with vision/tactile/force/language/actions; LeRobot/OpenPI conversion</td>
<td width="260">Force-position controller maintains task success while reducing average grip force by over 70% under gentle instructions.</td>
<td width="260">Current framework does not yet solve ultra-gentle regimes or real-world physical deployment.</td>
<td width="220"><a href="https://arxiv.org/abs/2605.27886">paper</a> / <a href="https://github.com/NathanWu7/Tabero">code</a></td>
</tr>
<tr>
<td width="110" nowrap>NeurIPS 2025</td>
<td width="280"><a href="https://arxiv.org/abs/2505.22566">Universal Visuo-Tactile Video Understanding for Embodied Interaction</a></td>
<td width="260">Vision-tactile-language video understanding for embodied interaction.</td>
<td width="180">visuo-tactile / touch-language</td>
<td width="200">VTV150K: 150,000 frames, 100 objects, GelSight Mini + DIGIT + Tac3D; hardness/protrusion/elasticity/friction labels</td>
<td width="140" nowrap>no</td>
<td width="240">tactile video understanding and tactile-language QA</td>
<td width="200">GelSight Mini, DIGIT, Tac3D</td>
<td width="200">dataset collection setup</td>
<td width="220">VTV150K / VBTS video dataset</td>
<td width="260">Builds VTV-LLM and VTV150K for cross-sensor tactile-language-video understanding.</td>
<td width="260">Representation-focused; no closed-loop manipulation policy in the checked evidence.</td>
<td width="220"><a href="https://arxiv.org/abs/2505.22566">paper</a> / <a href="https://github.com/IvanXie416/VTV-LLM">code</a> / <a href="https://huggingface.co/datasets/Ivan416/VBTS_video">hf</a></td>
</tr>
<tr>
<td width="110" nowrap>NeurIPS 2025</td>
<td width="280"><a href="https://arxiv.org/abs/2510.21609">Enhancing Tactile-based Reinforcement Learning for Robotic Control</a></td>
<td width="260">Improve tactile RL with sparse binary contacts and self-supervised representation learning.</td>
<td width="180">binary contact</td>
<td width="200">proprioception + 17 binary contacts in simulation</td>
<td width="140" nowrap>yes</td>
<td width="240">find object, ball bouncing, Baoding ball rotation</td>
<td width="200">Allegro Hand, ORCA Hand, Shadow Dexterous Hand, Shadow Dexterous Hand Lite, Franka</td>
<td width="200">RoTO simulated embodiments</td>
<td width="220">RoTO benchmark; simulation</td>
<td width="260">Shows blind simulated dexterity with sparse contacts and SSL objectives across tactile-diverse tasks.</td>
<td width="260">Simulation benchmark; real sensor durability and sim-to-real remain open.</td>
<td width="220"><a href="https://arxiv.org/abs/2510.21609">paper</a> / <a href="https://elle-miller.github.io/tactile_rl/">project</a> / <a href="https://github.com/elle-miller/roto">code</a></td>
</tr>
<tr>
<td width="110" nowrap>NeurIPS 2025</td>
<td width="280"><a href="https://taccel-simulator.github.io/assets/taccel-paper.pdf">Taccel: Scaling Up Vision-based Tactile Robotics via High-performance GPU Simulation</a></td>
<td width="260">Scale vision-based tactile robotics through high-performance GPU simulation.</td>
<td width="180">optical tactile</td>
<td width="200">vision-based tactile sensor models; sensor-elastomer / tactile-robot configs</td>
<td width="140" nowrap>yes</td>
<td width="240">peg insertion, grasping, deformable object, tactile-informed manipulation</td>
<td width="200">simulated vision-based tactile sensors and tactile robots</td>
<td width="200">GPU simulator, not a fixed robot platform</td>
<td width="220">Taccel GPU simulator; IPC + ABD modeling; docs/code</td>
<td width="260">Provides a fast simulator and APIs for tactile robot models and policy data generation.</td>
<td width="260">Simulation fidelity-to-hardware transfer still needs task-specific validation.</td>
<td width="220"><a href="https://taccel-simulator.github.io/assets/taccel-paper.pdf">paper</a> / <a href="https://taccel-simulator.github.io/">project</a> / <a href="https://github.com/Taccel-Simulator/Taccel">code</a></td>
</tr>
<tr>
<td width="110" nowrap>NeurIPS 2025</td>
<td width="280"><a href="https://arxiv.org/abs/2511.16596">Toward Artificial Palpation: Representation Learning of Touch on Soft Bodies</a></td>
<td width="260">Learn tactile representations for soft-body palpation.</td>
<td width="180">force/torque</td>
<td width="200">single Xela uSkin tactile sensor with 30 3D force sensors at 85 Hz; PalpationSim models 16 2D sensor points</td>
<td width="140" nowrap>no</td>
<td width="240">automatic poking / palpation; MRI reconstruction and change detection</td>
<td width="200">Franka Emika Panda arm with mounted Xela uSkin tactile sensor</td>
<td width="200">Franka Emika Panda palpation setup</td>
<td width="220">PalpationSim 2D FEM; real soft-body + MRI dataset; 30M instantaneous sensor readings; Zenodo data</td>
<td width="260">Learns representations from palpation sequences and releases simulation/real data.</td>
<td width="260">Simulation is explicitly not realistic; no sensor-motion planning is solved, and medical-grade deployment is not solved.</td>
<td width="220"><a href="https://arxiv.org/abs/2511.16596">paper</a> / <a href="https://zoharri.github.io/artificial-palpation/">project</a> / <a href="https://github.com/zoharri/ArtificialPalpation">code</a> / <a href="https://zenodo.org/records/17608184">data</a></td>
</tr>
<tr>
<td width="110" nowrap>NeurIPS 2025</td>
<td width="280"><a href="https://arxiv.org/abs/2507.15062v1">Touch in the Wild: Learning Fine-Grained Manipulation with a Portable Visuo-Tactile Gripper</a></td>
<td width="260">Collect in-the-wild visuo-tactile demonstrations and learn fine-grained manipulation policies.</td>
<td width="180">visuo-tactile</td>
<td width="200">two 12x32 tactile pads forming 1x24x32 tactile image; tactile stream 23 Hz; GoPro Hero 9 60 Hz with QR synchronization</td>
<td width="140" nowrap>yes</td>
<td width="240">test-tube insertion, pencil insertion, fluid transfer, whiteboard erasing</td>
<td width="200">portable handheld visuo-tactile gripper with soft fin-shaped fingers and Arduino-based PCB</td>
<td width="200">xArm 850 with same sensor configuration; handheld gripper for data collection</td>
<td width="220">2.6M visuo-tactile pairs, 2,700+ demonstrations, 43 tasks, 12 environments; ROS2 tactile logs; diffusion policy training</td>
<td width="260">Shows tactile pretraining improves data efficiency and robustness under occlusion/disturbance.</td>
<td width="260">Portable hardware helps data collection but still needs task-specific policy training.</td>
<td width="220"><a href="https://arxiv.org/abs/2507.15062v1">paper</a> / <a href="https://binghao-huang.github.io/touch_in_the_wild/">project</a> / <a href="https://github.com/YolandaXinyueZhu/touch_in_the_wild">code</a> / <a href="https://huggingface.co/datasets/binghaohuang-robot/touch_in_the_wild-dataset">hf</a></td>
</tr>
<tr>
<td width="110" nowrap>arXiv 2026</td>
<td width="280"><a href="https://arxiv.org/abs/2606.17055">T-Rex: Tactile-Reactive Dexterous Manipulation</a></td>
<td width="260">Tactile-reactive dexterous manipulation with high-frequency touch.</td>
<td width="180">force/torque tactile</td>
<td width="200">6D force/torque vectors from all 10 fingers</td>
<td width="140" nowrap>yes</td>
<td width="240">12 manipulation tasks requiring delicate force control and deformable-object handling</td>
<td width="200">Dexmate Vega-1 bimanual robot with two Sharpa Wave dexterous hands; ZED cameras; Manus/VIVE teleoperation</td>
<td width="200">Dexmate Vega-1 bimanual robot</td>
<td width="220">100 h synchronized RGB/tactile/state/action/language data; 7,755 episodes; 200+ objects; 22 motor primitives</td>
<td width="260">Uses a variable-rate Mixture-of-Transformers policy and temporal tactile VQ-VAE for tactile-reactive control.</td>
<td width="260">Paper notes tactile sensor distortion/calibration drift and lack of dense palm sensing.</td>
<td width="220"><a href="https://arxiv.org/abs/2606.17055">paper</a> / <a href="https://tactile-reactive-dexterous.github.io/">project</a></td>
</tr>
<tr>
<td width="110" nowrap>arXiv 2026</td>
<td width="280"><a href="https://arxiv.org/abs/2606.13102">FTP-1: A Foundation Tactile Policy for Generalizable Robot Manipulation</a></td>
<td width="260">Train a generalist tactile policy across heterogeneous tactile sensors and robots.</td>
<td width="180">image / array / state tactile</td>
<td width="200">MTTS data spanning 21 tactile sensors and 26 data sources</td>
<td width="140" nowrap>yes</td>
<td width="240">contact-rich manipulation across five hardware configurations</td>
<td width="200">heterogeneous tactile sensors and embodiments</td>
<td width="200">five downstream hardware configurations</td>
<td width="220">about 3,000 h tactile manipulation data from 26 sources and 21 sensors</td>
<td width="260">Shows a shared tactile expert can transfer to seen and unseen tactile sensors after downstream adaptation.</td>
<td width="260">Downstream tasks still need finetuning; general tactile servoing remains task- and hardware-dependent.</td>
<td width="220"><a href="https://arxiv.org/abs/2606.13102">paper</a> / <a href="https://ftp1-policy.github.io/">project</a> / <a href="https://github.com/michaelyuancb/ftp1-policy">code</a></td>
</tr>
<tr>
<td width="110" nowrap>ICRA 2026</td>
<td width="280"><a href="https://opendrivelab.com/FreeTacMan">FreeTacMan: Robot-free Human-centric Visuo-Tactile Data Collection System for Generalizable Contact-Rich Manipulation</a></td>
<td width="260">Collect scalable human-centric visuo-tactile data without a robot during data capture.</td>
<td width="180">visuo-tactile</td>
<td width="200">portable tactile gripper observations; public page does not state a full taxel map</td>
<td width="140" nowrap>yes</td>
<td width="240">50 contact-rich manipulation tasks with robot-policy transfer</td>
<td width="200">FreeTacMan portable visuo-tactile gripper; quick-swap mounts for Piper and Franka</td>
<td width="200">robot-free human collection, then Piper/Franka robot deployment</td>
<td width="220">3M+ visuo-tactile pairs and 10k+ trajectories across 50 tasks</td>
<td width="260">Decouples tactile data collection from robot hardware and reports higher robot success than vision-only baselines.</td>
<td width="260">Sensor density and robot-side SDK details are not fully specified on the checked public page.</td>
<td width="220"><a href="https://opendrivelab.com/FreeTacMan">project</a> / <a href="https://github.com/OpenDriveLab/FreeTacMan">code</a></td>
</tr>
<tr>
<td width="110" nowrap>ICRA 2026</td>
<td width="280"><a href="https://arxiv.org/abs/2602.11643">ViTaS: Building Embodied Tactile Foundation Model via Visuo-Tactile Simulation</a></td>
<td width="260">Pretrain tactile policies using visuo-tactile simulation and soft visual-tactile fusion.</td>
<td width="180">visuo-tactile</td>
<td width="200">3D-ViTaC tactile sensors with 16x16x1 tactile maps</td>
<td width="140" nowrap>yes</td>
<td width="240">12 simulated and 3 real-world tactile manipulation environments</td>
<td width="200">3D-ViTaC tactile sensors attached to a gripper; Galaxea-R1 setup with ZED 2 and RealSense D435i in checked evidence</td>
<td width="200">Galaxea-R1 robot setup</td>
<td width="220">ViTaS simulated tactile environments and three real-world evaluations</td>
<td width="260">Uses contrastive soft fusion to bridge visual and tactile representations for policy learning.</td>
<td width="260">Real coverage is smaller than simulation coverage, and tactile hardware is custom.</td>
<td width="220"><a href="https://arxiv.org/abs/2602.11643">paper</a> / <a href="https://skyrainwind.github.io/ViTaS/index.html">project</a> / <a href="https://github.com/SkyRainWind/ViTaS">code</a></td>
</tr>
<tr>
<td width="110" nowrap>ICRA 2026</td>
<td width="280"><a href="https://arxiv.org/abs/2510.06339">Vi-TacMan: Making Vision and Tactile Sensing Complementary for Vision-based Manipulation</a></td>
<td width="260">Combine vision-based action proposals with tactile refinement for articulated-object manipulation.</td>
<td width="180">vision + optical tactile</td>
<td width="200">GelSight-type tactile sensors replacing the gripper pads</td>
<td width="140" nowrap>yes</td>
<td width="240">articulated-object manipulation under visual ambiguity</td>
<td width="200">Kinova Gen3 7-DoF arm with GelSight-style tactile gripper pads</td>
<td width="200">Kinova Gen3</td>
<td width="220">50k+ simulated and real articulated-object interactions</td>
<td width="260">Uses vision to propose grasps/directions and tactile feedback to refine execution.</td>
<td width="260">Generalization beyond the reported articulated-object suite and tactile gripper geometry remains open.</td>
<td width="220"><a href="https://arxiv.org/abs/2510.06339">paper</a> / <a href="https://vi-tacman.github.io/">project</a></td>
</tr>
<tr>
<td width="110" nowrap>CoRL 2025</td>
<td width="280"><a href="https://proceedings.mlr.press/v305/xu25e.html">exUMI: Extensible Visuo-Tactile Teleoperation for Learning Diverse Skills</a></td>
<td width="260">Build an extensible UMI-style teleoperation stack with tactile sensing and calibration.</td>
<td width="180">visuo-tactile</td>
<td width="200">modular tactile sensing; over 1M tactile frames reported</td>
<td width="140" nowrap>yes</td>
<td width="240">diverse manipulation skills collected by extensible teleoperation</td>
<td width="200">exUMI handheld interface with AR MoCap, rotary encoder, modular visuo-tactile sensing, and automated calibration</td>
<td width="200">UMI-style robot deployment pipeline</td>
<td width="220">real teleoperation data with 100% reported data usability and over 1M tactile frames</td>
<td width="260">Improves tactile-aware teleoperation data quality through modular sensing and automated calibration.</td>
<td width="260">Exact downstream robot/hardware coverage varies by setup and must be checked before reuse.</td>
<td width="220"><a href="https://proceedings.mlr.press/v305/xu25e.html">pmlr</a> / <a href="https://silicx.github.io/exUMI/">project</a> / <a href="https://github.com/silicx/exUMI">code</a></td>
</tr>
<tr>
<td width="110" nowrap>CoRL 2025</td>
<td width="280"><a href="https://proceedings.mlr.press/v305/wistreich25a.html">DexSkin: High-Coverage Conformable Robot Skin for Learning Dexterous Manipulation</a></td>
<td width="260">Provide high-coverage conformable tactile skin for manipulation learning.</td>
<td width="180">capacitive tactile skin</td>
<td width="200">conformable sensorized finger surfaces on a parallel-jaw gripper</td>
<td width="140" nowrap>yes</td>
<td width="240">in-hand reorientation and elastic-band wrapping</td>
<td width="200">DexSkin capacitive electronic skin on parallel-jaw gripper fingers</td>
<td width="200">parallel-jaw gripper manipulation setup</td>
<td width="220">real robot calibration/model-transfer experiments and online RL</td>
<td width="260">Shows broad finger-surface tactile coverage can support model transfer and online RL for dexterous behaviors.</td>
<td width="260">Not a full multi-finger dexterous-hand benchmark; broader robot-hand integration remains to be proven.</td>
<td width="220"><a href="https://proceedings.mlr.press/v305/wistreich25a.html">pmlr</a> / <a href="https://dex-skin.github.io/">project</a> / <a href="https://github.com/sdwistreich/dexskin">code</a></td>
</tr>
<tr>
<td width="110" nowrap>RSS 2025</td>
<td width="280"><a href="https://arxiv.org/abs/2504.16649">PP-Tac: Paper Picking Using Tactile Feedback</a></td>
<td width="260">Use fingertip tactile feedback for paper picking and slip-aware force control.</td>
<td width="180">optical tactile</td>
<td width="200">four fingertip-mounted round R-Tac tactile sensors</td>
<td width="140" nowrap>yes</td>
<td width="240">paper picking with slip detection, online force control, trajectory synthesis, and diffusion policy</td>
<td width="200">R-Tac / PP-Tac tactile fingertips</td>
<td width="200">Franka Research 3 robot arm</td>
<td width="220">real tactile demonstrations and policy training; no public tactile/physics simulator found</td>
<td width="260">Reports robust paper picking by combining tactile slip detection, force control, and diffusion policy learning.</td>
<td width="260">Task is narrow and paper-focused; tactile hardware generalization beyond the reported setup is unproven.</td>
<td width="220"><a href="https://arxiv.org/abs/2504.16649">paper</a> / <a href="https://www.roboticsproceedings.org/rss21/p056.pdf">rss</a> / <a href="https://peilin-666.github.io/projects/PP-Tac/">project</a> / <a href="https://github.com/bigai-ai/PP-Tac">code</a></td>
</tr>
<tr>
<td width="110" nowrap>ICRA 2026</td>
<td width="280"><a href="https://arxiv.org/abs/2509.23468">Multi-Modal Manipulation via Multi-Modal Policy Consensus</a></td>
<td width="260">Fuse modality-specific policies for robust manipulation under sensor corruption.</td>
<td width="180">vision + tactile + proprioception</td>
<td width="200">tactile stream used as one policy modality; exact sensor density not found in checked abstract/project evidence</td>
<td width="140" nowrap>yes</td>
<td width="240">RLBench simulation plus real occluded picking, in-hand spoon reorientation, and puzzle insertion tasks</td>
<td width="200">multi-modal robot manipulation setup; exact tactile sensor model not found in checked public evidence</td>
<td width="200">real robot platform plus RLBench simulation</td>
<td width="220">RLBench simulated tasks and real multi-modal manipulation demonstrations</td>
<td width="260">Uses adaptive policy consensus to keep control robust when individual modalities are corrupted.</td>
<td width="260">Public evidence does not fully specify tactile hardware density/model or SDK.</td>
<td width="220"><a href="https://arxiv.org/abs/2509.23468">paper</a> / <a href="https://policyconsensus.github.io/">project</a> / <a href="https://openreview.net/forum?id=CJDU8IvF3y">openreview</a></td>
</tr>
<tr>
<td width="110" nowrap>arXiv 2026</td>
<td width="280"><a href="https://arxiv.org/abs/2602.06001">Visuo-Tactile World Models for Robot Manipulation</a></td>
<td width="260">Use a visuo-tactile world model to predict contact dynamics for manipulation.</td>
<td width="180">visuo-tactile</td>
<td width="200">Digit 360 tactile sensors used as fingertips on an Allegro Hand</td>
<td width="140" nowrap>yes</td>
<td width="240">zero-shot real-robot manipulation under occlusion and contact uncertainty</td>
<td width="200">Digit 360 tactile fingertips on Allegro Hand</td>
<td width="200">Franka Panda arm with Allegro Hand</td>
<td width="220">limited real demonstrations; Sparsh-X tactile embeddings and Cosmos RGB embeddings</td>
<td width="260">Improves object permanence and laws-of-motion compliance through tactile-conditioned world modeling.</td>
<td width="260">Demonstration scale is limited and the pipeline depends on pretrained embeddings and sensor-specific calibration.</td>
<td width="220"><a href="https://arxiv.org/abs/2602.06001">paper</a> / <a href="https://carolinahiguera.github.io/vtml/">project</a></td>
</tr>
</tbody>
</table>

### Efficiency / Evaluation / Data

This direction determines whether systems can actually be deployed: on-device inference, caching/quantization/action tokenization, real-time execution, sim2real, benchmarks, and safety evaluation are all necessary conditions.

Subdirections: quantization/cache/tokenization, real-time execution, benchmark/dataset, sim2real, and safety evaluation.

Total: 101 papers.

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
<td nowrap>22</td>
<td nowrap>Focus: on-device deployment, cache reuse, and action token efficiency.</td>
</tr>
<tr>
<td nowrap>real-time execution</td>
<td nowrap>6</td>
<td nowrap>Focus: low-latency execution and real-time policy inference.</td>
</tr>
<tr>
<td nowrap>benchmark/dataset</td>
<td nowrap>42</td>
<td nowrap>Focus: data coverage, task design, and evaluation credibility.</td>
</tr>
<tr>
<td nowrap>sim2real</td>
<td nowrap>18</td>
<td nowrap>Focus: sim-to-real transfer and the real-world deployment gap.</td>
</tr>
<tr>
<td nowrap>safety evaluation</td>
<td nowrap>13</td>
<td nowrap>Focus: robustness, safety, and deployment risk evaluation.</td>
</tr>
</tbody>
</table>

#### quantization/cache/tokenization

Total: 22 papers.

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
</tr>
</thead>
<tbody>
<tr>
<td nowrap>CoRL 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2509.23655">Focusing on What Matters: Object-Agent-centric Tokenization for Vision Language Action models</a></td>
<td nowrap>This work studies object-agent-centric tokenization for efficient VLA models.</td>
<td nowrap>quantization/cache/tokenization</td>
<td nowrap>deployment/evaluation coverage</td>
<td nowrap>robot/simulator platform</td>
<td nowrap>embodied robot tasks</td>
<td nowrap>source-listed resource</td>
<td nowrap>Add CoRL deployment/evaluation coverage.</td>
<td nowrap><a href="https://arxiv.org/abs/2509.23655">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2509.05614">SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning</a></td>
<td nowrap>Uses action-aware self-speculative pruning to accelerate VLA inference while preserving action quality.</td>
<td nowrap>compression/cache/tokenization</td>
<td nowrap>self-speculative pruning</td>
<td nowrap>robot deployment/evaluation environment</td>
<td nowrap>VLA manipulation</td>
<td nowrap>-</td>
<td nowrap>Addresses redundant computation in VLA action generation.</td>
<td nowrap><a href="https://arxiv.org/abs/2509.05614">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>EMNLP 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2507.22424">Spec-VLA: Speculative Decoding for Vision-Language-Action Models with Relaxed Acceptance</a></td>
<td nowrap>Applies relaxed speculative decoding to accelerate VLA action generation.</td>
<td nowrap>compression/cache/tokenization</td>
<td nowrap>speculative decoding</td>
<td nowrap>robot deployment/evaluation environment</td>
<td nowrap>VLA manipulation</td>
<td nowrap>-</td>
<td nowrap>Addresses slow autoregressive VLA decoding during robot execution.</td>
<td nowrap><a href="https://arxiv.org/abs/2507.22424">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>NeurIPS 2024</td>
<td nowrap><a href="https://arxiv.org/abs/2411.02359">DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution</a></td>
<td nowrap>Uses dynamic inference to reduce multimodal VLA computation during robot execution.</td>
<td nowrap>compression/cache/tokenization</td>
<td nowrap>dynamic inference</td>
<td nowrap>robot deployment/evaluation environment</td>
<td nowrap>robot execution</td>
<td nowrap>Code</td>
<td nowrap>Addresses unnecessary computation in multimodal VLA inference.</td>
<td nowrap><a href="https://arxiv.org/abs/2411.02359">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://github.com/yueyang130/DeeR-VLA">code</a></td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>NeurIPS 2024</td>
<td nowrap><a href="https://arxiv.org/abs/2406.04339">RoboMamba: Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation</a></td>
<td nowrap>Uses a Mamba/state-space architecture to make VLA robot reasoning and manipulation more efficient.</td>
<td nowrap>efficient architecture</td>
<td nowrap>state-space model backbone</td>
<td nowrap>robot deployment/evaluation environment</td>
<td nowrap>robot reasoning and manipulation</td>
<td nowrap>Project+Code</td>
<td nowrap>Addresses Transformer efficiency bottlenecks in VLA policies.</td>
<td nowrap><a href="https://arxiv.org/abs/2406.04339">paper</a></td>
<td nowrap><a href="https://sites.google.com/view/robomamba-web">project</a></td>
<td nowrap><a href="https://github.com/lmzpai/roboMamba">code</a></td>
<td nowrap>-</td>
</tr>
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
</tr>
</tbody>
</table>

#### benchmark/dataset

Total: 42 papers.

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
</tr>
</thead>
<tbody>
<tr>
<td nowrap>CoRL 2023</td>
<td nowrap><a href="https://scholar.google.com/scholar?q=Behavior-1K%3A+A+Benchmark+for+Embodied+AI+with+1%2C000+Everyday+Activities+and+Realistic+Simulation">Behavior-1K: A Benchmark for Embodied AI with 1,000 Everyday Activities and Realistic Simulation</a></td>
<td nowrap>Behavior-1K benchmarks embodied AI on 1,000 everyday activities in realistic simulation.</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>deployment/evaluation coverage</td>
<td nowrap>robot/simulator platform</td>
<td nowrap>embodied robot tasks</td>
<td nowrap>source-listed resource</td>
<td nowrap>Add CoRL deployment/evaluation coverage.</td>
<td nowrap><a href="https://scholar.google.com/scholar?q=Behavior-1K%3A+A+Benchmark+for+Embodied+AI+with+1%2C000+Everyday+Activities+and+Realistic+Simulation">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CoRL 2022</td>
<td nowrap><a href="https://scholar.google.com/scholar?q=iGibson+2.0%3A+Object-Centric+Simulation+for+Robot+Learning+of+Everyday+Household+Tasks">iGibson 2.0: Object-Centric Simulation for Robot Learning of Everyday Household Tasks</a></td>
<td nowrap>iGibson 2.0 provides object-centric simulation for robot learning in household tasks.</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>deployment/evaluation coverage</td>
<td nowrap>robot/simulator platform</td>
<td nowrap>embodied robot tasks</td>
<td nowrap>source-listed resource</td>
<td nowrap>Add CoRL deployment/evaluation coverage.</td>
<td nowrap><a href="https://scholar.google.com/scholar?q=iGibson+2.0%3A+Object-Centric+Simulation+for+Robot+Learning+of+Everyday+Household+Tasks">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CoRL 2017</td>
<td nowrap><a href="https://scholar.google.com/scholar?q=CARLA%3A+An+Open+Urban+Driving+Simulator">CARLA: An Open Urban Driving Simulator</a></td>
<td nowrap>CARLA is an open urban driving simulator used for embodied driving evaluation.</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>deployment/evaluation coverage</td>
<td nowrap>robot/simulator platform</td>
<td nowrap>embodied robot tasks</td>
<td nowrap>source-listed resource</td>
<td nowrap>Add CoRL deployment/evaluation coverage.</td>
<td nowrap><a href="https://scholar.google.com/scholar?q=CARLA%3A+An+Open+Urban+Driving+Simulator">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://openaccess.thecvf.com/content/ICCV2025/html/Zhong_UnrealZoo_Enriching_Photo-realistic_Virtual_Worlds_for_Embodied_AI_ICCV_2025_paper.html">UnrealZoo: Enriching Photo-realistic Virtual Worlds for Embodied AI</a></td>
<td nowrap>UnrealZoo expands photorealistic virtual worlds for embodied AI training and evaluation.</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>virtual-world coverage</td>
<td nowrap>simulation platform</td>
<td nowrap>embodied navigation and interaction</td>
<td nowrap>open virtual-world resource</td>
<td nowrap>Provide richer simulation environments for embodied AI.</td>
<td nowrap><a href="https://openaccess.thecvf.com/content/ICCV2025/papers/Zhong_UnrealZoo_Enriching_Photo-realistic_Virtual_Worlds_for_Embodied_AI_ICCV_2025_paper.pdf">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://openaccess.thecvf.com/content/CVPR2025/html/Chen_ActiveGAMER_Active_GAussian_Mapping_through_Efficient_Rendering_CVPR_2025_paper.html">ActiveGAMER: Active GAussian Mapping through Efficient Rendering</a></td>
<td nowrap>ActiveGAMER performs active Gaussian mapping with efficient rendering for embodied scene understanding.</td>
<td nowrap>mapping/evaluation</td>
<td nowrap>mapping efficiency</td>
<td nowrap>Gaussian mapping pipeline</td>
<td nowrap>active mapping</td>
<td nowrap>mapping benchmark/resource</td>
<td nowrap>Improve active mapping efficiency for embodied agents.</td>
<td nowrap><a href="https://openaccess.thecvf.com/content/CVPR2025/papers/Chen_ActiveGAMER_Active_Gaussian_Mapping_through_Efficient_Rendering_CVPR_2025_paper.pdf">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CVPR 2024</td>
<td nowrap><a href="https://openaccess.thecvf.com/content/CVPR2024/html/Yang_Holodeck_Language_Guided_Generation_of_3D_Embodied_AI_Environments_CVPR_2024_paper.html">Holodeck: Language Guided Generation of 3D Embodied AI Environments</a></td>
<td nowrap>Holodeck generates 3D embodied AI environments from language guidance.</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>3D environment diversity</td>
<td nowrap>language-to-environment generator</td>
<td nowrap>environment generation</td>
<td nowrap>3D embodied environments</td>
<td nowrap>Generate diverse 3D scenes for embodied AI evaluation.</td>
<td nowrap><a href="https://openaccess.thecvf.com/content/CVPR2024/papers/Yang_Holodeck_Language_Guided_Generation_of_3D_Embodied_AI_Environments_CVPR_2024_paper.pdf">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>NeurIPS 2022</td>
<td nowrap><a href="https://proceedings.neurips.cc/paper_files/paper/2022/hash/27c546ab1e4f1d7d638e6a8dfbad9a07-Abstract-Conference.html">ProcTHOR: Large-Scale Embodied AI Using Procedural Generation</a></td>
<td nowrap>ProcTHOR uses procedural generation to create large-scale embodied AI environments.</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>procedural scene diversity</td>
<td nowrap>AI2-THOR environment generation</td>
<td nowrap>navigation and interaction tasks</td>
<td nowrap>ProcTHOR</td>
<td nowrap>Scale embodied-AI evaluation with generated houses.</td>
<td nowrap><a href="https://proceedings.neurips.cc/paper_files/paper/2022/file/27c546ab1e4f1d7d638e6a8dfbad9a07-Paper-Conference.pdf">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CVPR 2024</td>
<td nowrap><a href="https://openaccess.thecvf.com/content/CVPR2024/html/Wang_EmbodiedScan_A_Holistic_Multi-Modal_3D_Perception_Suite_Towards_Embodied_AI_CVPR_2024_paper.html">EmbodiedScan: A Holistic Multi-Modal 3D Perception Suite Towards Embodied AI</a></td>
<td nowrap>EmbodiedScan provides a multimodal 3D perception suite for embodied AI.</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>multi-modal 3D perception coverage</td>
<td nowrap>dataset + benchmark</td>
<td nowrap>3D perception tasks</td>
<td nowrap>EmbodiedScan</td>
<td nowrap>Benchmark holistic 3D perception for embodied agents.</td>
<td nowrap><a href="https://openaccess.thecvf.com/content/CVPR2024/papers/Wang_EmbodiedScan_A_Holistic_Multi-Modal_3D_Perception_Suite_Towards_Embodied_AI_CVPR_2024_paper.pdf">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ECCV 2024</td>
<td nowrap><a href="https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/01610.pdf">ReALFRED: An Embodied Instruction Following Benchmark in Photo-Realistic Environments</a></td>
<td nowrap>ReALFRED benchmarks embodied instruction following in photorealistic environments.</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>photorealistic instruction-following coverage</td>
<td nowrap>benchmark</td>
<td nowrap>instruction following</td>
<td nowrap>ReALFRED</td>
<td nowrap>Evaluate embodied instruction following in realistic scenes.</td>
<td nowrap><a href="https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/01610.pdf">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICRA 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2509.14687">RealMirror: A Comprehensive, Open-Source Vision-Language-Action Platform for Embodied AI</a></td>
<td nowrap>RealMirror provides a platform for VLA data collection, simulation, training, evaluation, and zero-shot sim-to-real transfer.</td>
<td nowrap>VLA platform / benchmark</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>simulation/evaluation environment</td>
<td nowrap>humanoid VLA research</td>
<td nowrap>project/code/models available</td>
<td nowrap>Lowers the barrier to VLA data, training, and evaluation.</td>
<td nowrap><a href="https://arxiv.org/abs/2509.14687">paper</a></td>
<td nowrap><a href="https://terminators2025.github.io/RealMirror.github.io/">project</a></td>
<td nowrap><a href="https://github.com/terminators2025/RealMirror">code</a></td>
<td nowrap><a href="https://huggingface.co/zte-terminators/realmirror-model-ckpt">hf</a></td>
</tr>
<tr>
<td nowrap>IROS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2412.05313">lambda: A Benchmark for Data-Efficiency in Long-Horizon Indoor Mobile Manipulation Robotics</a></td>
<td nowrap>The lambda benchmark evaluates long-horizon indoor mobile manipulation for data efficiency, language tasks, and multi-room scenes.</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>data efficiency</td>
<td nowrap>indoor mobile manipulation benchmark</td>
<td nowrap>long-horizon mobile manipulation</td>
<td nowrap>project/code/data available</td>
<td nowrap>Fills the gap in data-efficiency evaluation for long-horizon mobile manipulation.</td>
<td nowrap><a href="https://arxiv.org/abs/2412.05313">paper</a></td>
<td nowrap><a href="https://lambdabenchmark.github.io/">project</a></td>
<td nowrap><a href="https://github.com/h2r/LAMBDA">code</a></td>
<td nowrap><a href="https://github.com/h2r/LAMBDA">data</a></td>
</tr>
<tr>
<td nowrap>ICRA 2025</td>
<td nowrap><a href="https://github.com/BAAI-DCAI/SpatialBot">SpatialBot: Precise Spatial Understanding with Vision Language Models</a></td>
<td nowrap>SpatialBot targets precise VLM spatial understanding with embodied data, SpatialQA, and SpatialBench.</td>
<td nowrap>spatial understanding benchmark</td>
<td nowrap>benchmark/dataset</td>
<td nowrap>VLM spatial reasoning</td>
<td nowrap>embodied spatial QA</td>
<td nowrap>model/data/benchmark available</td>
<td nowrap>Evaluates whether VLMs have precise spatial understanding for robot manipulation.</td>
<td nowrap><a href="https://github.com/BAAI-DCAI/SpatialBot">paper</a></td>
<td nowrap><a href="https://github.com/BAAI-DCAI/SpatialBot">project</a></td>
<td nowrap><a href="https://github.com/BAAI-DCAI/SpatialBot">code</a></td>
<td nowrap><a href="https://github.com/BAAI-DCAI/SpatialBot">data</a></td>
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
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38875">H-RDT: Human Manipulation Enhanced Bimanual Robotic Manipulation</a></td>
<td nowrap>Leverages egocentric human manipulation data to pretrain a diffusion-transformer policy for stronger bimanual robot manipulation.</td>
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
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38883">PEOD: A Pixel-Aligned Event-RGB Benchmark for Object Detection Under Challenging Conditions</a></td>
<td nowrap>Provides a high-resolution pixel-aligned Event-RGB object-detection benchmark for low-light, overexposed, and high-speed scenes.</td>
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
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38913">SIAM: Towards Generalizable Articulated Object Modeling via Single Robot-Object Interaction</a></td>
<td nowrap>Infers articulated-object part segmentation, kinematics, and URDF-style models from a single robot-object interaction.</td>
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
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38923">VirtualEnv: A Platform for Embodied AI Research</a></td>
<td nowrap>Provides an Unreal Engine 5 simulation platform for evaluating LLM/VLM agents in interactive embodied tasks.</td>
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
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38930">Lifelong Language-Conditioned Robotic Manipulation Learning</a></td>
<td nowrap>Introduces SkillsCrafter for continual language-conditioned manipulation while reducing catastrophic forgetting across skills.</td>
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
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64411">AIR-VLA: Vision-Language-Action Systems for Aerial Manipulation</a></td>
<td nowrap>Builds a simulation, dataset, and benchmark for VLA/VLM evaluation on aerial manipulation systems.</td>
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
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/63391">DLO-Lab: Benchmarking Deformable Linear Object Manipulations with Differentiable Physics</a></td>
<td nowrap>Provides a differentiable-physics simulator and benchmark for deformable linear-object manipulation and sim-to-real study.</td>
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
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/63416">ManiSoft: Towards Vision-Language Manipulation for Soft Robotics</a></td>
<td nowrap>Provides a soft-arm simulation benchmark with language-conditioned tasks and expert trajectories for vision-language manipulation.</td>
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
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64619">OXE-AugE: A Large-Scale Robot Augmentation of OXE for Scaling Cross-Embodiment Policy Learning</a></td>
<td nowrap>Augments Open X-Embodiment with diverse robot embodiments to scale cross-embodiment policy learning.</td>
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
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.08367">Embodied Crowd Counting</a></td>
<td nowrap>Defines embodied crowd counting with a drone simulator, ECCD dataset, and zero-shot navigation baseline.</td>
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
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/1787">RobAVA: A Large-scale Dataset and Baseline Towards Video based Robotic Arm Action Understanding</a></td>
<td nowrap>Provides a large-scale video dataset and baseline for robotic arm action understanding.</td>
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
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/2215">RoboAnnotatorX: A Comprehensive and Universal Annotation Framework for Accurate Understanding of Long-horizon Robot Demonstration</a></td>
<td nowrap>Provides a multimodal annotation framework for producing rich labels from long-horizon robot demonstrations.</td>
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
</tr>
</tbody>
</table>

#### sim2real

Total: 18 papers.

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
</tr>
</thead>
<tbody>
<tr>
<td nowrap>CoRL 2018</td>
<td nowrap><a href="https://scholar.google.com/scholar?q=Sim-to-Real+Reinforcement+Learning+for+Deformable+Object+Manipulation">Sim-to-Real Reinforcement Learning for Deformable Object Manipulation</a></td>
<td nowrap>This work transfers reinforcement learning from simulation to deformable object manipulation.</td>
<td nowrap>sim2real</td>
<td nowrap>deployment/evaluation coverage</td>
<td nowrap>robot/simulator platform</td>
<td nowrap>embodied robot tasks</td>
<td nowrap>source-listed resource</td>
<td nowrap>Add CoRL deployment/evaluation coverage.</td>
<td nowrap><a href="https://scholar.google.com/scholar?q=Sim-to-Real+Reinforcement+Learning+for+Deformable+Object+Manipulation">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
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
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/66662">FlatLab: A Unified Methodology Framework and Simulation-Based Benchmark for Robotic Manipulation of Flat Objects</a></td>
<td nowrap>Provides a unified framework and simulation benchmark for manipulating flat objects with varied geometry and material.</td>
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
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://openreview.net/forum?id=284GWLFtjU">DEAL: Diffusion Evolution Adversarial Learning for Sim-to-Real Transfer</a></td>
<td nowrap>Combines diffusion evolution and adversarial learning to tune simulators and reduce the sim-to-real gap for RL controllers.</td>
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
</tr>
</tbody>
</table>

#### safety evaluation

Total: 13 papers.

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
</tr>
</thead>
<tbody>
<tr>
<td nowrap>CoRL 2024</td>
<td nowrap><a href="https://scholar.google.com/scholar?q=DriveVLM%3A+The+Convergence+of+Autonomous+Driving+and+Large+Vision-Language+Models">DriveVLM: The Convergence of Autonomous Driving and Large Vision-Language Models</a></td>
<td nowrap>DriveVLM studies autonomous driving through large vision-language models.</td>
<td nowrap>safety evaluation</td>
<td nowrap>deployment/evaluation coverage</td>
<td nowrap>robot/simulator platform</td>
<td nowrap>embodied robot tasks</td>
<td nowrap>source-listed resource</td>
<td nowrap>Add CoRL deployment/evaluation coverage.</td>
<td nowrap><a href="https://scholar.google.com/scholar?q=DriveVLM%3A+The+Convergence+of+Autonomous+Driving+and+Large+Vision-Language+Models">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICLR 2025</td>
<td nowrap><a href="https://proceedings.iclr.cc/paper_files/paper/2025/file/5ab848771ff8c9c47aac4128e2ef9f4e-Paper-Conference.pdf">HASARD: A Benchmark for Vision-Based Safe Reinforcement Learning in Embodied Agents</a></td>
<td nowrap>HASARD benchmarks vision-based safe reinforcement learning for embodied agents.</td>
<td nowrap>safety evaluation</td>
<td nowrap>safe-RL benchmark coverage</td>
<td nowrap>benchmark platform</td>
<td nowrap>vision-based safe RL</td>
<td nowrap>HASARD</td>
<td nowrap>Evaluate safe RL agents under embodied visual observations.</td>
<td nowrap><a href="https://arxiv.org/abs/2503.08241">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>NeurIPS 2022</td>
<td nowrap><a href="https://openreview.net/forum?id=dwi57JI_-K&noteId=pfmgIWaQAoN">SafeBench: A Benchmarking Platform for Safety Evaluation of Autonomous Vehicles</a></td>
<td nowrap>SafeBench provides a benchmark platform for autonomous-vehicle safety evaluation.</td>
<td nowrap>safety evaluation</td>
<td nowrap>autonomous driving safety scenarios</td>
<td nowrap>benchmark platform</td>
<td nowrap>driving safety evaluation</td>
<td nowrap>SafeBench</td>
<td nowrap>Evaluate safety risks in autonomous driving scenarios.</td>
<td nowrap><a href="https://arxiv.org/abs/2206.09682">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>IROS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2410.15185">Semantically Safe Robot Manipulation: From Semantic Scene Understanding to Motion Safeguards</a></td>
<td nowrap>Uses LLM commonsense reasoning to identify semantic risks and map them into robot manipulation safety filters.</td>
<td nowrap>semantic safety layer</td>
<td nowrap>safety evaluation</td>
<td nowrap>robot manipulation safety</td>
<td nowrap>semantic scene understanding + safeguards</td>
<td nowrap>project available</td>
<td nowrap>Adds semantic risk reasoning to the robot manipulation safety loop.</td>
<td nowrap><a href="https://arxiv.org/abs/2410.15185">paper</a></td>
<td nowrap><a href="https://utiasdsl.github.io/semantic-manipulation/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
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
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/60472">Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds</a></td>
<td nowrap>Fuses diverse point-cloud inputs with 2D observations to improve VLA robustness across simulator, sensor, and real domains.</td>
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
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/62679">PACT: Self-Evolving Physical Safety Alignment for Diffusion Policies in Embodied Manipulation</a></td>
<td nowrap>Post-trains diffusion policies with physical-constraint alignment to reduce safety violations without demonstrations or rewards.</td>
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
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61584">SafeLab: An Interactive High-Fidelity Benchmark for Embodied Safety in Scientific Robotics</a></td>
<td nowrap>Provides a high-fidelity lab simulation benchmark with safety tasks, calibrated assets, and expert trajectories.</td>
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
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64080">Dismantling the Illusion of Vision-Language-Action Models Competence via Explicit Distributional Shifts</a></td>
<td nowrap>Introduces LIBERO-Gen to expose VLA brittleness under explicit semantic and environmental distribution shifts.</td>
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
</tr>
</tbody>
</table>


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
