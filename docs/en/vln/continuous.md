# Continuous VLN

[Home](../../../README.md) | [中文](../../zh-CN/vln/continuous.md) | [Direction index](README.md)

Total: 39 papers.

<table width="3050">
<thead>
<tr>
<th width="120" nowrap>Venue/Year</th>
<th width="320">Paper/Method</th>
<th width="420">Abstract</th>
<th width="220">Task Type</th>
<th width="240">Environment</th>
<th width="260">Map/Memory</th>
<th width="300">Training/Feedback</th>
<th width="240">Sim/Real/Benchmark</th>
<th width="360">Paper Task/Goal</th>
<th width="110" nowrap>Paper</th>
<th width="110" nowrap>Project</th>
<th width="110" nowrap>Code</th>
<th width="240">Data/Bench</th>
</tr>
</thead>
<tbody>
<tr>
<td width="120" nowrap>CoRL 2022</td>
<td width="320"><a href="https://scholar.google.com/scholar?q=LM-Nav%3A+Robotic+Navigation+with+Large+Pre-Trained+Models+of+Language%2C+Vision%2C+and+Action">LM-Nav: Robotic Navigation with Large Pre-Trained Models of Language, Vision, and Action</a></td>
<td width="420">LM-Nav composes pretrained language, vision, and action models for robotic navigation.</td>
<td width="220">Vision-language navigation</td>
<td width="240">embodied navigation</td>
<td width="260">language/spatial context</td>
<td width="300">CoRL navigation method</td>
<td width="240">VLN / embodied navigation benchmarks</td>
<td width="360">Add CoRL navigation coverage.</td>
<td width="110" nowrap><a href="https://scholar.google.com/scholar?q=LM-Nav%3A+Robotic+Navigation+with+Large+Pre-Trained+Models+of+Language%2C+Vision%2C+and+Action">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2020</td>
<td width="320"><a href="https://scholar.google.com/scholar?q=Vision-and-Dialog+Navigation">Vision-and-Dialog Navigation</a></td>
<td width="420">Vision-and-Dialog Navigation extends VLN with dialog interaction during navigation.</td>
<td width="220">Vision-language navigation</td>
<td width="240">embodied navigation</td>
<td width="260">language/spatial context</td>
<td width="300">CoRL navigation method</td>
<td width="240">VLN / embodied navigation benchmarks</td>
<td width="360">Add CoRL navigation coverage.</td>
<td width="110" nowrap><a href="https://scholar.google.com/scholar?q=Vision-and-Dialog+Navigation">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2509.10454">GC-VLN: Instruction as Graph Constraints for Training-free Vision-and-Language Navigation</a></td>
<td width="420">GC-VLN treats instructions as graph constraints for training-free VLN.</td>
<td width="220">Vision-language navigation</td>
<td width="240">embodied navigation</td>
<td width="260">language/spatial context</td>
<td width="300">CoRL navigation method</td>
<td width="240">VLN / embodied navigation benchmarks</td>
<td width="360">Add CoRL navigation coverage.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2509.10454">paper</a></td>
<td width="110" nowrap><a href="https://bagh2178.github.io/GC-VLN/">project</a></td>
<td width="110" nowrap><a href="https://github.com/bagh2178/GC-VLN">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2505.11350">Search-TTA: A Multimodal Test-Time Adaptation Framework for Visual Search in the Wild</a></td>
<td width="420">Search-TTA adapts multimodal visual-search agents at test time in open environments.</td>
<td width="220">Vision-language navigation</td>
<td width="240">embodied navigation</td>
<td width="260">language/spatial context</td>
<td width="300">CoRL navigation method</td>
<td width="240">VLN / embodied navigation benchmarks</td>
<td width="360">Add CoRL navigation coverage.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2505.11350">paper</a></td>
<td width="110" nowrap><a href="https://search-tta.github.io/">project</a></td>
<td width="110" nowrap><a href="https://github.com/marmotlab/Search-TTA-VLN">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2023</td>
<td width="320"><a href="https://openaccess.thecvf.com/content/CVPR2023/html/Gao_Adaptive_Zone-Aware_Hierarchical_Planner_for_Vision-Language_Navigation_CVPR_2023_paper.html">Adaptive Zone-Aware Hierarchical Planner for Vision-Language Navigation</a></td>
<td width="420">AZHP plans navigation by adapting hierarchy and local zones for language-conditioned visual navigation.</td>
<td width="220">Vision-language navigation</td>
<td width="240">continuous indoor navigation</td>
<td width="260">zone-aware hierarchical memory</td>
<td width="300">hierarchical planning</td>
<td width="240">VLN benchmarks</td>
<td width="360">Use zone-level structure to make long-horizon VLN decisions more reliable.</td>
<td width="110" nowrap><a href="https://openaccess.thecvf.com/content/CVPR2023/papers/Gao_Adaptive_Zone-Aware_Hierarchical_Planner_for_Vision-Language_Navigation_CVPR_2023_paper.pdf">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2024</td>
<td width="320"><a href="https://proceedings.mlr.press/v235/gao24p.html">Fast-Slow Test-Time Adaptation for Online Vision-and-Language Navigation</a></td>
<td width="420">Fast-Slow TTA adapts VLN agents online using complementary fast and slow adaptation signals.</td>
<td width="220">Online VLN</td>
<td width="240">continuous navigation</td>
<td width="260">episodic adaptation memory</td>
<td width="300">test-time adaptation</td>
<td width="240">VLN benchmarks</td>
<td width="360">Improve online VLN robustness under distribution shift.</td>
<td width="110" nowrap><a href="https://proceedings.mlr.press/v235/gao24p/gao24p.pdf">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICRA 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2509.19480">OmniVLA: An Omni-Modal Vision-Language-Action Model for Robot Navigation</a></td>
<td width="420">OmniVLA unifies language, goal images, and 2D pose goals, learning robot navigation policies through a VLA formulation.</td>
<td width="220">Vision-language-action navigation</td>
<td width="240">continuous navigation</td>
<td width="260">multimodal goal context</td>
<td width="300">navigation VLA training</td>
<td width="240">Sim + Real</td>
<td width="360">Train a generalizable navigation VLA with multimodal goal specifications.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2509.19480">paper</a></td>
<td width="110" nowrap><a href="https://omnivla-nav.github.io/">project</a></td>
<td width="110" nowrap><a href="https://github.com/NHirose/OmniVLA">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICRA 2025</td>
<td width="320"><a href="https://sites.google.com/view/opennav/home">Open-Nav: Exploring Zero-Shot Vision-and-Language Navigation in Continuous Environment with Open-Source LLMs</a></td>
<td width="420">Open-Nav uses open-source LLMs for spatio-temporal chain-of-thought reasoning, progress estimation, and action decisions for zero-shot VLN in continuous environments.</td>
<td width="220">Continuous VLN</td>
<td width="240">continuous indoor environment</td>
<td width="260">spatio-temporal CoT</td>
<td width="300">zero-shot LLM planning</td>
<td width="240">VLN-CE benchmark</td>
<td width="360">Enable open-source LLMs to navigate continuous environments from language instructions.</td>
<td width="110" nowrap><a href="https://sites.google.com/view/opennav/home">paper</a></td>
<td width="110" nowrap><a href="https://sites.google.com/view/opennav/home">project</a></td>
<td width="110" nowrap><a href="https://github.com/YanyuanQiao/Open-Nav">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=kkBOIsrCXh">Embodied Navigation Foundation Model</a></td>
<td width="420">NavFoM trains a unified navigation foundation model on 8 million cross-embodiment navigation samples, covering VLN, goal search, tracking, and autonomous driving.</td>
<td width="220">continuous VLN</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">multimodal history/trajectory context</td>
<td width="300">large-scale supervised pretraining</td>
<td width="240">cross-embodiment benchmark</td>
<td width="360">Cross-embodiment and cross-task generalization</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=kkBOIsrCXh">paper</a></td>
<td width="110" nowrap><a href="https://pku-epic.github.io/NavFoM-Web/">project</a></td>
<td width="110" nowrap>-</td>
<td width="240"><a href="https://pku-epic.github.io/NavFoM-Web/">data</a></td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=GK4rznYwhn">Ground Slow, Move Fast: A Dual-System Foundation Model for Generalizable Vision-Language Navigation</a></td>
<td width="420">DualVLN combines a slow vision-language global planner with a fast diffusion-based low-level controller to improve smooth execution for continuous real-world VLN.</td>
<td width="220">continuous VLN</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">-</td>
<td width="300">VLM waypoint planner + diffusion policy</td>
<td width="240">sim+real robot</td>
<td width="360">Addresses fragmented actions, high latency, and poor dynamic obstacle avoidance in end-to-end VLN.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=GK4rznYwhn">paper</a></td>
<td width="110" nowrap><a href="https://internrobotics.github.io/internvla-n1-dualvln.github.io/">project</a></td>
<td width="110" nowrap><a href="https://github.com/InternRobotics/InternNav">code</a></td>
<td width="240">InternData-N1</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=eqcDckWHik">CompassNav: Steering From Path Imitation to Decision Understanding In Navigation</a></td>
<td width="420">CompassNav shifts from trajectory imitation to action-feasibility understanding, improving VLN decisions with Compass-Data-22k and gap-aware training.</td>
<td width="220">continuous VLN</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">-</td>
<td width="300">RFT + action feasibility supervision</td>
<td width="240">Compass-Data-22k</td>
<td width="360">From path imitation to decision understanding</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=eqcDckWHik">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=pFh5ygjN3V">M$^3$E: Continual Vision-and-Language Navigation via Mixture of Macro and Micro Experts</a></td>
<td width="420">M3E separately models macro scene experts and micro perception experts, mitigating catastrophic forgetting in continual VLN cross-environment adaptation.</td>
<td width="220">Continual VLN</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">-</td>
<td width="300">hierarchical MoE continual learning</td>
<td width="240">-</td>
<td width="360">Cross-environment continual learning and anti-forgetting</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=pFh5ygjN3V">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=zGtTQTD1zu">OmniNav: A Unified Framework for Prospective Exploration and Visual-Language Navigation</a></td>
<td width="420">OmniNav uses a unified waypoint policy to handle instruction-goal navigation, object-goal navigation, point-goal navigation, and frontier exploration.</td>
<td width="220">Unified Navigation/Exploration</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">-</td>
<td width="300">continuous waypoint policy</td>
<td width="240">real-time 5Hz deployment claimed</td>
<td width="360">Unifies multiple navigation paradigms and supports low-latency continuous-space waypoint outputs.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=zGtTQTD1zu">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=0c7nAZjyr5">From Seeing to Experiencing: Scaling Navigation Foundation Models with Reinforcement Learning</a></td>
<td width="420">S2E post-trains offline video-pretrained navigation models with reinforcement learning to learn action consequences, obstacle avoidance, and urban interaction behaviors.</td>
<td width="220">continuous VLN</td>
<td width="240">urban/dynamic environment</td>
<td width="260">-</td>
<td width="300">offline pretraining + RL post-training</td>
<td width="240">-</td>
<td width="360">Interactive safe navigation generalization</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=0c7nAZjyr5">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=apaLoTumdO">CE-Nav: Flow-Guided Reinforcement Refinement for Cross-Embodiment Local Navigation</a></td>
<td width="420">CE-Nav first uses a flow model to learn cross-embodiment feasible action distributions, then refines them with RL for specific robot dynamics.</td>
<td width="220">Cross-embodiment Local Navigation</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">-</td>
<td width="300">IL + RL, conditional normalizing flow</td>
<td width="240">-</td>
<td width="360">Cross-morphology local navigation generalization</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=apaLoTumdO">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=bMrH2PFMsi">CoNavBench: Collaborative Long-Horizon Vision-Language Navigation Benchmark</a></td>
<td width="420">CoNavBench provides 4,048 single-agent/collaborative long-horizon VLN episodes for evaluating handoffs, congestion, and collaborative navigation.</td>
<td width="220">Collaborative Long-horizon VLN Benchmark</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">-</td>
<td width="300">VLN policy</td>
<td width="240">Benchmark</td>
<td width="360">Collaborative VLN evaluation</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=bMrH2PFMsi">paper</a></td>
<td width="110" nowrap><a href="https://navcraft.github.io">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">CoNavBench/NavCraft</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38886">NaVLA$^2$: A Vision-Language-Audio-Action Model for Multimodal Instruction Navigation</a></td>
<td width="420">NaVLA2 proposes the MINav task, using language, image, and audio cues to disambiguate navigation instructions and build 43.9K episodes.</td>
<td width="220">Multimodal Instruction Navigation</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">-</td>
<td width="300">vision-language-audio-action policy</td>
<td width="240">MINav benchmark</td>
<td width="360">Addresses target grounding ambiguity caused by language-only instructions being insufficient in scenes with multiple similar objects.</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38886">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38888">VPN: Visual Prompt Navigation</a></td>
<td width="420">VPN replaces natural-language instructions with 2D top-down visual prompts and extends R2R/R2R-CE to form the VP dataset.</td>
<td width="220">visual prompt navigation</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">top-view map prompt</td>
<td width="300">VLN policy</td>
<td width="240">R2R-VP/R2R-CE-VP</td>
<td width="360">Studies navigation guided by user-drawn/marked visual path prompts.</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38888">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38891">SeqWalker: Sequential-Horizon Vision-and-Language Navigation with Hierarchical Planning</a></td>
<td width="420">SeqWalker targets long-horizon multi-task instructions, using high-level sub-instruction selection and low-level exploration verification to reduce information overload.</td>
<td width="220">Long-horizon/Sequential VLN</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">-</td>
<td width="300">hierarchical planning</td>
<td width="240">-</td>
<td width="360">Long-instruction decomposition and execution</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38891">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38895">UNeMo: Collaborative Visual-Language Reasoning and Navigation via a Multimodal World Model</a></td>
<td width="420">UNeMo jointly optimizes visual state reasoning and navigation decisions with a multimodal world model, filling the gap in VLN methods that reason only with language.</td>
<td width="220">World-model VLN</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">-</td>
<td width="300">multimodal world model collaborative optimization</td>
<td width="240">-</td>
<td width="360">Addresses the separation between LLM reasoning modules and navigation policies, and the lack of visual reasoning.</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38895">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38914">DNOI-4DRO: Deep 4D Radar Odometry with Differentiable Neural-Optimization Iterations</a></td>
<td width="420">DNOI-4DRO combines a 4D radar motion-flow network with differentiable Gauss-Newton optimization to improve radar odometry accuracy.</td>
<td width="220">4D radar odometry, not VLN</td>
<td width="240">Mobile robot/autonomous-driving radar localization</td>
<td width="260">-</td>
<td width="300">differentiable neural optimization</td>
<td width="240">VoD/Snail-Radar</td>
<td width="360">Addresses self-localization/odometry estimation in sparse 4D radar point clouds.</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38914">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38954">Run, Ruminate, and Regulate: A Dual-process Thinking System for Vision-and-Language Navigation</a></td>
<td width="420">R3 combines fast execution, slow LLM reflection, and a regulation module to improve zero-shot VLN reasoning and efficiency.</td>
<td width="220">continuous VLN</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">-</td>
<td width="300">dual-process LLM reasoning</td>
<td width="240">-</td>
<td width="360">Zero-shot VLN reasoning efficiency and performance</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38954">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/61535">AdaNav: Adaptive Reasoning with Uncertainty for Vision-Language Navigation</a></td>
<td width="420">AdaNav triggers uncertainty-aware reasoning with action entropy, avoiding extra computation and performance loss from fixed-interval reasoning.</td>
<td width="220">continuous VLN</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">-</td>
<td width="300">uncertainty-adaptive reasoning + RL refinement</td>
<td width="240">-</td>
<td width="360">Adaptive reasoning trigger</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/61535">paper</a></td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/61535">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/64780">Instruction Decomposition and Action Alignment for Vision-Language Navigation</a></td>
<td width="420">IDEAL-VLN decomposes long instructions into causal execution chains and performs action alignment to reduce irrelevant text interference and visual token latency.</td>
<td width="220">continuous VLN</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">-</td>
<td width="300">instruction decomposition + action alignment</td>
<td width="240">-</td>
<td width="360">Long-horizon instruction decomposition and execution</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/64780">paper</a></td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/64780">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/65809">TIC-VLA: A Think-in-Control Vision-Language-Action Model for Robot Navigation in Dynamic Environments</a></td>
<td width="420">TIC-VLA explicitly models semantic reasoning latency and feeds delayed vision-language states into real-time action control.</td>
<td width="220">VLA robot navigation</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">-</td>
<td width="300">latency-aware VLA control</td>
<td width="240">-</td>
<td width="360">Enables language instruction following and real-time reactive control in dynamic human environments.</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/65809">paper</a></td>
<td width="110" nowrap><a href="https://ucla-mobility.github.io/TIC-VLA/">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/61357">Hydra-Nav: Object Navigation via Adaptive Dual-Process Reasoning</a></td>
<td width="420">Hydra-Nav adaptively switches between slow history-based reasoning and fast reactions in object navigation, balancing success rate and computational efficiency.</td>
<td width="220">ObjectNav</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">-</td>
<td width="300">adaptive dual-process VLM reasoning</td>
<td width="240">-</td>
<td width="360">Addresses weak spatiotemporal reasoning and high reasoning overhead in unseen object navigation.</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/61357">paper</a></td>
<td width="110" nowrap><a href="https://zixuan-wang99.github.io/Hydra-Nav/">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/60775">SafeDec: Constrained Decoding for Safe Autoregressive Generalist Robot Navigation Policies</a></td>
<td width="420">SafeDec performs constraint decoding for autoregressive robot navigation policies, enforcing safety constraints while generating action sequences.</td>
<td width="220">Safety-constrained robot navigation</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">-</td>
<td width="300">constrained decoding</td>
<td width="240">-</td>
<td width="360">Adds explicit safety correctness to physically executable general navigation policies.</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/60775">paper</a></td>
<td width="110" nowrap><a href="https://constrained-robot-fms.github.io/">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2511.20620">Wanderland: Geometrically Grounded Simulation for Open-World Embodied AI</a></td>
<td width="420">Wanderland is a real-to-sim framework that uses multi-sensor capture and geometrically reliable reconstruction to build open-world navigation simulation benchmarks.</td>
<td width="220">Simulation/evaluation platform</td>
<td width="240">Open-city simulation</td>
<td width="260">-</td>
<td width="300">planning / RL</td>
<td width="240">Sim/Benchmark</td>
<td width="360">Provides a geometrically grounded open-city closed-loop evaluation environment for embodied AI.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2511.20620">paper</a></td>
<td width="110" nowrap><a href="https://ai4ce.github.io/wanderland/">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2512.04069">SpaceTools: Tool-Augmented Spatial Reasoning via Double Interactive RL</a></td>
<td width="420">SpaceTools uses dual-interaction RL to learn tool calls for depth, segmentation, pose, and other tools to enhance VLM metric spatial reasoning.</td>
<td width="220">Tool-augmented spatial reasoning</td>
<td width="240">mobile robot/navigation environment</td>
<td width="260">-</td>
<td width="300">double interactive RL</td>
<td width="240">-</td>
<td width="360">Addresses VLMs' lack of precise metric ability in embodied spatial reasoning.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2512.04069">paper</a></td>
<td width="110" nowrap><a href="https://spacetools.github.io/">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2512.17907">Dexterous World Models</a></td>
<td width="420">DWM is a scene-action-conditioned video diffusion world model that uses hand actions to drive static 3D scenes into dynamic interaction videos.</td>
<td width="220">Dexterous-interaction world model, not VLN</td>
<td width="240">egocentric hand-scene interaction</td>
<td width="260">-</td>
<td width="300">world model / planning / RL</td>
<td width="240">-</td>
<td width="360">Predicts dynamic changes after dexterous human-hand interaction with 3D scenes.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2512.17907">paper</a></td>
<td width="110" nowrap><a href="https://snuvclab.github.io/dwm/">project</a></td>
<td width="110" nowrap><a href="https://github.com/snuvclab/dwm">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2508.09423">Distilling LLM Prior to Flow Model for Generalizable Agent’s Imagination in Object Goal Navigation</a></td>
<td width="420">GOAL distills LLM spatial priors into a flow model, using generative semantic-map imagination to support ObjectNav.</td>
<td width="220">ObjectNav/semantic map imagination</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">-</td>
<td width="300">flow matching + LLM prior</td>
<td width="240">-</td>
<td width="360">Completes unobserved areas in unseen indoor environments to improve object-goal navigation.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2508.09423">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/Badi-Li/GOAL">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2511.17225">TP-MDDN: Task-Preferenced Multi-Demand-Driven Navigation with Autonomous Decision-Making</a></td>
<td width="420">TP-MDDN proposes a multi-demand, preference-aware long-horizon navigation benchmark and uses AWMSystem to decompose demands, select goals, monitor state, and correct errors.</td>
<td width="220">multi-demand-driven navigation benchmark</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">MASMap 3D point cloud + 2D semantic map</td>
<td width="300">LLM/MLLM autonomous decision system</td>
<td width="240">-</td>
<td width="360">Addresses long-horizon demand-driven navigation under multiple sub-demands and explicit preference constraints.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2511.17225">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2506.06630">Active Test-time Vision-Language Navigation</a></td>
<td width="420">ATENA actively learns at test time and reduces uncertainty with entropy minimization, reducing accumulated errors when VLN is deployed in new environments.</td>
<td width="220">continuous VLN</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">-</td>
<td width="300">test-time active learning/adaptation</td>
<td width="240">-</td>
<td width="360">Performs VLN test-time adaptation without external feedback.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2506.06630">paper</a></td>
<td width="110" nowrap><a href="https://kuai-lab.github.io/neurips2025atena/">project</a></td>
<td width="110" nowrap><a href="https://github.com/kuai-lab/NeurIPS25_att_vln">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2510.00441">Seeing through Uncertainty: Robust Task-Oriented Optimization in Visual Navigation</a></td>
<td width="420">NeuRO couples perception networks with task-level robust optimization to handle noise and OOD generalization in few-shot visual navigation.</td>
<td width="220">Open-world Environment</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">-</td>
<td width="300">learning-to-optimize robust optimization</td>
<td width="240">-</td>
<td width="360">Addresses overfitting in long-horizon multi-goal visual navigation policies under data scarcity.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2510.00441">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/PyyWill/NeuRO">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2503.18525">RoboTron-Nav: A Unified Framework for Embodied Navigation Integrating Perception, Planning, and Prediction</a></td>
<td width="420">RoboTron-Nav integrates perception, planning, and prediction through multitask collaboration between navigation and embodied QA, reducing history redundancy.</td>
<td width="220">Open-world Environment</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">-</td>
<td width="300">multitask navigation + EQA</td>
<td width="240">-</td>
<td width="360">Improves perception, planning, and prediction in unseen environments for language-guided visual navigation.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2503.18525">paper</a></td>
<td width="110" nowrap><a href="https://yvfengzhong.github.io/RoboTron-Nav">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2412.05552">SAME: Learning Generic Language-Guided Visual Navigation with State-Adaptive Mixture of Experts</a></td>
<td width="420">SAME uses state-adaptive MoE to unify high-level category search and low-level language-guided navigation.</td>
<td width="220">generic language-guided visual navigation</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">-</td>
<td width="300">state-adaptive MoE</td>
<td width="240">-</td>
<td width="360">Learns a general policy that can be shared across multiple categories of language-guided navigation tasks.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2412.05552">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/GengzeZhou/SAME">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://iccv.thecvf.com/virtual/2025/poster/1984">Embodied Navigation with Auxiliary Task of Action Description Prediction</a></td>
<td width="420">This paper uses language descriptions of actions as an auxiliary RL task, allowing the navigation policy to explain its own actions while maintaining performance.</td>
<td width="220">Open-world Environment</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">-</td>
<td width="300">RL + action description auxiliary task</td>
<td width="240">-</td>
<td width="360">Interpretable navigation action prediction</td>
<td width="110" nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/1984">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2412.10439">CogNav: Cognitive Process Modeling for Object Goal Navigation with LLMs</a></td>
<td width="420">CogNav uses an LLM to model goal memory and cognitive update processes, strengthening high-level decision-making in ObjectNav.</td>
<td width="220">ObjectNav</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">cognitive memory</td>
<td width="300">LLM planning</td>
<td width="240">-</td>
<td width="360">Enables an ObjectNav agent to have human-like cognitive map updates and goal reasoning.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2412.10439">paper</a></td>
<td width="110" nowrap><a href="https://yhancao.github.io/CogNav/">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2503.11081">MoMa-Kitchen: A 100K+ Benchmark for Affordance-Grounded Last-Mile Navigation in Mobile Manipulation</a></td>
<td width="420">MoMa-Kitchen provides 100K+ kitchen samples, annotating the final navigation stop pose that benefits subsequent manipulation.</td>
<td width="220">mobile manipulation last-mile navigation benchmark</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">affordance-grounded labels</td>
<td width="300">affordance</td>
<td width="240">Benchmark</td>
<td width="360">Evaluates whether mobile manipulation can stop at a manipulable position after approaching the target.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2503.11081">paper</a></td>
<td width="110" nowrap><a href="https://momakitchen.github.io/">project</a></td>
<td width="110" nowrap><a href="https://github.com/MoMaKitchen/MoMaKitchen">code</a></td>
<td width="240"><a href="https://huggingface.co/datasets/IPEC-COMMUNITY/MoMa-Kitchen-Data">hf</a></td>
</tr>
</tbody>
</table>
