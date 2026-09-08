# Map Memory

[Home](../../../README.md) | [中文](../../zh-CN/vln/map-memory.md) | [Direction index](README.md)

Total: 23 papers.

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
<td width="120" nowrap>CoRL 2024</td>
<td width="320"><a href="https://arxiv.org/abs/2407.07775">Mobility VLA: Multimodal Instruction Navigation with Long-Context VLMs and Topological Graphs</a></td>
<td width="420">Mobility VLA combines long-context VLMs with topological graphs for instruction navigation.</td>
<td width="220">Vision-language navigation</td>
<td width="240">embodied navigation</td>
<td width="260">language/spatial context</td>
<td width="300">CoRL navigation method</td>
<td width="240">VLN / embodied navigation benchmarks</td>
<td width="360">Add CoRL navigation coverage.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2407.07775">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ACL 2024</td>
<td width="320"><a href="https://aclanthology.org/2024.acl-long.529/">MapGPT: Map-Guided Prompting for Unified Vision-and-Language Navigation</a></td>
<td width="420">MapGPT uses map-guided prompting to connect language instructions with spatial navigation decisions.</td>
<td width="220">Vision-language navigation</td>
<td width="240">indoor VLN</td>
<td width="260">map-guided prompt memory</td>
<td width="300">LLM prompting + navigation</td>
<td width="240">VLN benchmarks</td>
<td width="360">Use explicit maps to ground LLM navigation decisions.</td>
<td width="110" nowrap><a href="https://aclanthology.org/2024.acl-long.529.pdf">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2024</td>
<td width="320"><a href="https://openaccess.thecvf.com/content/CVPR2024/html/Zhao_OVER-NAV_Elevating_Iterative_Vision-and-Language_Navigation_with_Open-Vocabulary_Detection_and_StructurEd_CVPR_2024_paper.html">OVER-NAV: Elevating Iterative Vision-and-Language Navigation with Open-Vocabulary Detection and Structured Representation</a></td>
<td width="420">OVER-NAV combines open-vocabulary detection with structured scene memory for iterative VLN.</td>
<td width="220">Vision-language navigation</td>
<td width="240">indoor VLN</td>
<td width="260">open-vocabulary structured memory</td>
<td width="300">iterative navigation planning</td>
<td width="240">VLN benchmarks</td>
<td width="360">Improve VLN grounding with open-vocabulary object and scene structure.</td>
<td width="110" nowrap><a href="https://openaccess.thecvf.com/content/CVPR2024/papers/Zhao_OVER-NAV_Elevating_Iterative_Vision-and-Language_Navigation_with_Open-Vocabulary_Detection_and_StructurEd_CVPR_2024_paper.pdf">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2024</td>
<td width="320"><a href="https://arxiv.org/abs/2403.14158">Volumetric Environment Representation for Vision-Language Navigation</a></td>
<td width="420">VER builds volumetric scene representations to improve spatial memory and grounding in VLN.</td>
<td width="220">Vision-language navigation</td>
<td width="240">3D indoor navigation</td>
<td width="260">volumetric map memory</td>
<td width="300">3D representation learning</td>
<td width="240">VLN benchmarks</td>
<td width="360">Represent navigable space volumetrically for language-guided navigation.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2403.14158">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>IROS 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2606.25497">SAGE-Nav: Leveraging LLM Planning and Alignment Fusion for Hierarchical Scene Graph-Guided Navigation</a></td>
<td width="420">SAGE-Nav combines LLM high-level planning with hierarchical scene graphs to guide object-goal navigation.</td>
<td width="220">Object-goal navigation</td>
<td width="240">indoor navigation</td>
<td width="260">hierarchical scene graph</td>
<td width="300">LLM planning + alignment fusion</td>
<td width="240">Benchmark</td>
<td width="360">Ground language planning in target navigation through scene-graph memory.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2606.25497">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>IROS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2503.02247">WMNav: Integrating Vision-Language Models into World Models for Object Goal Navigation</a></td>
<td width="420">WMNav integrates VLMs into a navigation world model to predict future states and maintain navigation memory for better target search.</td>
<td width="220">Object-goal navigation</td>
<td width="240">indoor navigation</td>
<td width="260">world-model memory</td>
<td width="300">VLM-guided world model</td>
<td width="240">Benchmark</td>
<td width="360">Use world-model imagination and feedback to support object-goal navigation.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2503.02247">paper</a></td>
<td width="110" nowrap><a href="https://b0b8k1ng.github.io/WMNav/">project</a></td>
<td width="110" nowrap><a href="https://github.com/B0B8K1ng/WMNavigation">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=HB6KvsqcAn">Towards Physically Executable 3D Gaussian for Embodied Navigation</a></td>
<td width="420">SAGE-3D upgrades 3DGS into a navigation-environment representation with object semantics and physical executability.</td>
<td width="220">Map/memory</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">semantic and physically aligned 3D Gaussian</td>
<td width="300">3DGS environment construction</td>
<td width="240">-</td>
<td width="360">3DGS-executable navigation environment</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=HB6KvsqcAn">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=LPv59noPAy">Uncertainty-Aware Gaussian Map for Vision-Language Navigation</a></td>
<td width="420">This paper builds a semantic Gaussian Map and explicitly encodes geometric, semantic, and appearance uncertainty to guide VLN actions.</td>
<td width="220">Map/memory</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">uncertainty-aware semantic Gaussian map</td>
<td width="300">uncertainty-informed policy</td>
<td width="240">-</td>
<td width="360">Uses perception uncertainty in VLN decisions instead of ignoring ambiguous observations.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=LPv59noPAy">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=RnuB0Nlbd5">JanusVLN: Decoupling Semantics and Spatiality with Dual Implicit Memory for Vision-Language Navigation</a></td>
<td width="420">JanusVLN uses dual implicit memories to separately model semantic and spatial information, reducing redundancy and spatial loss from explicit text/frame memories.</td>
<td width="220">Map/memory</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">Map/memory</td>
<td width="300">dual implicit neural memory; KV-cache incremental update</td>
<td width="240">VLN benchmark</td>
<td width="360">Addresses explicit memory bloat and spatial information loss in MLLM-VLN.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=RnuB0Nlbd5">paper</a></td>
<td width="110" nowrap><a href="https://miv-xjtu.github.io/JanusVLN.github.io/">project</a></td>
<td width="110" nowrap><a href="https://github.com/MIV-XJTU/JanusVLN">code</a></td>
<td width="240"><a href="https://miv-xjtu.github.io/JanusVLN.github.io/">data</a></td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=li1vfqDzRD">Emergence of Spatial Representation in an Actor-Critic Agent with Hippocampus-Inspired Sequence Generator</a></td>
<td width="420">This paper uses a hippocampus-inspired sequence generator as a temporal memory buffer to explain the emergence of spatial representations in actor-critic navigation agents.</td>
<td width="220">Neuro-inspired visual navigation/RL</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">hippocampus-inspired temporal sequence memory</td>
<td width="300">actor-critic RL</td>
<td width="240">-</td>
<td width="360">Studies how spatial representations emerge from sequence-memory mechanisms in continuous maze visual navigation.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=li1vfqDzRD">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=KcC5mwfGf0">GRL-SNAM: Geometric Reinforcement Learning with Differential Hamiltonians for Navigation and Mapping in Unknown Environments</a></td>
<td width="420">GRL-SNAM uses local perception to construct a Hamiltonian energy landscape, jointly navigating and mapping in unknown environments without building a global map.</td>
<td width="220">simultaneous navigation and mapping</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">local energy landscape/no global map</td>
<td width="300">geometric RL</td>
<td width="240">-</td>
<td width="360">Performs simultaneous navigation and mapping in unknown environments.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=KcC5mwfGf0">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38884">RflyPano: A Panoramic Benchmark for Ultra-low Altitude UAV Localization Powered by RflySim</a></td>
<td width="420">RflyPano is a panoramic dataset for UAV visual localization below 120 meters, generated from RflySim with four fisheye cameras.</td>
<td width="220">UAV localization benchmark</td>
<td width="240">Ultra-low-altitude UAV / RflySim simulation</td>
<td width="260">Evaluation/data rather than map memory</td>
<td width="300">localization</td>
<td width="240">Benchmark</td>
<td width="360">Provides a panoramic visual localization benchmark for low-altitude UAV scenarios with unreliable GNSS.</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38884">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/DUNDAI1998/RflyPano">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38887">MHED-SLAM: Multi-Scale Hybrid Encoding-Based Decoupled SLAM</a></td>
<td width="420">MHED-SLAM uses multiscale hybrid encoding and decoupled geometry/color modeling to improve NeRF-SLAM mapping and tracking quality.</td>
<td width="220">SLAM</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">neural scene representation</td>
<td width="300">NeRF/TSDF SLAM</td>
<td width="240">-</td>
<td width="360">Visual SLAM mapping and localization</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38887">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38893">LOG-Nav: Efficient Layout-Aware Object-Goal Navigation with Hierarchical Planning</a></td>
<td width="420">LOG-Nav uses global topological layout maps and local scene memory for hierarchical planning, improving multi-room ObjectNav efficiency.</td>
<td width="220">ObjectNav</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">topological layout map + local scene memory</td>
<td width="300">LLM hierarchical planning/no costly training</td>
<td width="240">-</td>
<td width="360">Enables an LLM agent to efficiently find objects in complex indoor multi-room environments.</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38893">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38899">PanoNav: Mapless Zero-Shot Object Navigation with Panoramic Scene Parsing and Dynamic Memory</a></td>
<td width="420">PanoNav uses RGB-only panoramic scene parsing and dynamic memory to achieve map-free zero-shot ObjectNav.</td>
<td width="220">zero-shot ObjectNav</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">dynamic memory/mapless RGB-only</td>
<td width="300">MLLM reasoning</td>
<td width="240">-</td>
<td width="360">Performs zero-shot object navigation without depth or prebuilt maps.</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38899">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38901">Lightweight Adaptive Topological Layout and Semantic Mapping in Vision-and-Language Navigation on Websites</a></td>
<td width="420">ATLAS builds a lightweight adaptive topological layout and semantic graph for website VLN, improving web navigation accuracy and inference speed.</td>
<td width="220">Map/memory</td>
<td width="240">Web navigation, not physical robotics</td>
<td width="260">adaptive topological layout + semantic map</td>
<td width="300">LLM web navigation</td>
<td width="240">-</td>
<td width="360">Addresses navigation and QA for web agents in open, dynamic webpage structures.</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38901">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38929">Expand Your SCOPE: Semantic Cognition over Potential-Based Exploration for Embodied Visual Navigation</a></td>
<td width="420">SCOPE models the relationship between local observations and navigation goals with frontier boundaries and potential-based exploration, performing zero-shot visual navigation.</td>
<td width="220">zero-shot embodied visual navigation</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">frontier/potential-based semantic memory</td>
<td width="300">zero-shot framework</td>
<td width="240">-</td>
<td width="360">Improves long-horizon planning for goal-directed exploration in unknown environments.</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38929">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38948">Agent Journey Beyond RGB: Hierarchical Semantic-Spatial Representation Enrichment for Vision-and-Language Navigation</a></td>
<td width="420">SUSA fuses non-RGB representations with hierarchical semantic understanding and spatial awareness to strengthen semantic-spatial grounding in VLN.</td>
<td width="220">Map/memory</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">hierarchical semantic-spatial representation</td>
<td width="300">representation enrichment</td>
<td width="240">-</td>
<td width="360">Addresses insufficient use of multimodal environment representations in egocentric VLN.</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38948">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/64902">MapDream: Task-Driven Map Learning for Vision-Language Navigation</a></td>
<td width="420">MapDream formulates map building as task-driven BEV image autoregressive generation rather than manual map reconstruction.</td>
<td width="220">Map/memory</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">learned task-driven BEV map</td>
<td width="300">map-in-the-loop autoregressive BEV synthesis</td>
<td width="240">-</td>
<td width="360">Learns map representations that directly serve navigation goals.</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/64902">paper</a></td>
<td width="110" nowrap><a href="https://horizonrobotics.github.io/robot_lab/mapdream/">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2605.01736">GLMap: Multi-Scale Gaussian-Language Map for Zero-shot Embodied Navigation and Reasoning</a></td>
<td width="420">GLMap uses multiscale semantic units to store natural-language descriptions and 3D Gaussian simultaneously, enabling zero-shot navigation and reasoning.</td>
<td width="220">Map/memory</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">multi-scale Gaussian-language map</td>
<td width="300">zero-shot navigation/reasoning</td>
<td width="240">-</td>
<td width="360">Provides large models with a geometrically explicit, semantically multiscale 3D map interface.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2605.01736">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/sx-zhang/GLMap">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2510.18546">EfficientNav: Towards On-Device Object-Goal Navigation with Navigation Map Caching and Retrieval</a></td>
<td width="420">EfficientNav uses navigation-map caching and retrieval to reduce long prompts and latency when local small LLMs perform ObjectNav.</td>
<td width="220">on-device ObjectNav</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">navigation map caching/retrieval</td>
<td width="300">small LLM planning</td>
<td width="240">-</td>
<td width="360">Efficiently performs zero-shot ObjectNav on edge devices.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2510.18546">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/PKU-SEC-Lab/EfficientNav">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2507.04047">Move to Understand a 3D Scene: Bridging Visual Grounding and Exploration for Efficient and Versatile Embodied Navigation</a></td>
<td width="420">MTU3D combines active exploration with 3D vision-language grounding, letting the agent complete scene understanding through movement.</td>
<td width="220">active 3D scene understanding/navigation</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">3D-VL active perception</td>
<td width="300">3D representation</td>
<td width="240">-</td>
<td width="360">Decides where to look to improve 3D scene grounding and navigation efficiency.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2507.04047">paper</a></td>
<td width="110" nowrap><a href="https://mtu3d.github.io/">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://iccv.thecvf.com/virtual/2025/poster/944">NavQ: Learning a Q-Model for Foresighted Vision-and-Language Navigation</a></td>
<td width="420">NavQ trains a Q-model on large-scale unlabeled trajectories to estimate future visible information for candidate actions and support look-ahead decisions.</td>
<td width="220">Map/memory</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">foresighted Q-feature from trajectory data</td>
<td width="300">Q-learning on unlabeled trajectories</td>
<td width="240">-</td>
<td width="360">Look-ahead VLN decision-making</td>
<td width="110" nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/944">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
</tbody>
</table>
