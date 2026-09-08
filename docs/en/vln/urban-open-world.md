# Urban / Open-world Navigation

[Home](../../../README.md) | [中文](../../zh-CN/vln/urban-open-world.md) | [Direction index](README.md)

Total: 20 papers.

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
<td width="120" nowrap>CVPR 2024</td>
<td width="320"><a href="https://openaccess.thecvf.com/content/CVPR2024/html/Khanna_GOAT-Bench_A_Benchmark_for_Multi-Modal_Lifelong_Navigation_CVPR_2024_paper.html">GOAT-Bench: A Benchmark for Multi-Modal Lifelong Navigation</a></td>
<td width="420">GOAT-Bench evaluates lifelong navigation with multimodal goals and open-ended object/place targets.</td>
<td width="220">Lifelong navigation benchmark</td>
<td width="240">open-world indoor scenes</td>
<td width="260">goal-conditioned memory</td>
<td width="300">benchmark evaluation</td>
<td width="240">GOAT-Bench</td>
<td width="360">Measure multimodal lifelong navigation beyond single instruction episodes.</td>
<td width="110" nowrap><a href="https://openaccess.thecvf.com/content/CVPR2024/papers/Khanna_GOAT-Bench_A_Benchmark_for_Multi-Modal_Lifelong_Navigation_CVPR_2024_paper.pdf">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ECCV 2024</td>
<td width="320"><a href="https://arxiv.org/pdf/2407.14758">DISCO: Embodied Navigation and Interaction via Differentiable Scene-Conditioned Options</a></td>
<td width="420">DISCO learns scene-conditioned options for embodied navigation and interaction in open environments.</td>
<td width="220">Navigation + interaction</td>
<td width="240">open embodied scenes</td>
<td width="260">scene-conditioned options</td>
<td width="300">option learning</td>
<td width="240">Embodied interaction benchmarks</td>
<td width="360">Tie navigation and interaction through reusable scene-conditioned options.</td>
<td width="110" nowrap><a href="https://arxiv.org/pdf/2407.14758">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=88RKxlFUNY">AutoFly: Vision-Language-Action Model for UAV Autonomous Navigation in the Wild</a></td>
<td width="420">AutoFly is an end-to-end UAV VLA model that uses pseudo-depth encoding and two-stage training to support continuous outdoor planning and obstacle avoidance.</td>
<td width="220">Open-world Environment</td>
<td width="240">UAV/urban environment</td>
<td width="260">-</td>
<td width="300">two-stage VLA training</td>
<td width="240">sim+real UAV</td>
<td width="360">Shifts from explicit route following to autonomous UAV navigation under coarse-grained instructions.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2602.09657">paper</a></td>
<td width="110" nowrap><a href="https://xiaolousun.github.io/AutoFly/">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=OKm3w71ymP">OpenFly: A Comprehensive Platform for Aerial Vision-Language Navigation</a></td>
<td width="420">OpenFly integrates UE, GTA V, Google Earth, and 3DGS to generate large-scale aerial VLN data and platforms.</td>
<td width="220">aerial VLN platform/benchmark</td>
<td width="240">UAV/urban environment</td>
<td width="260">-</td>
<td width="300">open-world navigation</td>
<td width="240">Benchmark</td>
<td width="360">Reduces the cost of collecting UAV VLN data and provides an aerial navigation evaluation platform.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=OKm3w71ymP">paper</a></td>
<td width="110" nowrap><a href="https://shailab-ipec.github.io/openfly/">project</a></td>
<td width="110" nowrap><a href="https://github.com/Eziotic/OpenFly">code</a></td>
<td width="240"><a href="https://shailab-ipec.github.io/openfly/">data</a></td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=qSak1Hjfdq">All-day Multi-scenes Lifelong Vision-and-Language Navigation with Tucker Adaptation</a></td>
<td width="420">TuKA represents multi-scene, multi-time navigation knowledge as Tucker-decomposition adapters, mitigating forgetting in all-day multi-scene VLN.</td>
<td width="220">lifelong VLN</td>
<td width="240">UAV/urban environment</td>
<td width="260">-</td>
<td width="300">Tucker Adaptation/parameter-efficient tuning</td>
<td width="240">-</td>
<td width="360">All-day multi-scene continual adaptation</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=qSak1Hjfdq">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=PaYo96rjij">Lifelong Embodied Navigation Learning</a></td>
<td width="420">Uni-Walker uses DE-LoRA to separate shared and task-specific navigation knowledge, supporting continual learning over multi-task sequences.</td>
<td width="220">lifelong embodied navigation</td>
<td width="240">UAV/urban environment</td>
<td width="260">-</td>
<td width="300">DE-LoRA continual learning</td>
<td width="240">-</td>
<td width="360">Continual learning of navigation skills</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=PaYo96rjij">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=hzf23XSDcs">CitySeeker: How Do VLMs Explore Embodied Urban Navigation with Implicit Human Needs?</a></td>
<td width="420">CitySeeker uses 6,440 trajectories across 8 cities to evaluate whether a VLM can turn implicit needs such as "I'm thirsty" into urban navigation goals.</td>
<td width="220">urban implicit-need navigation benchmark</td>
<td width="240">UAV/urban environment</td>
<td width="260">-</td>
<td width="300">open-world navigation</td>
<td width="240">Benchmark</td>
<td width="360">Evaluates a VLM's ability to understand implicit human needs in urban environments and find target places.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=hzf23XSDcs">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">CitySeeker 6,440 trajectories/8 cities</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38878">AerialVLA: A Vision-Language-Action Model for Aerial Navigation with Online Dialogue</a></td>
<td width="420">AerialVLA targets UAV vision-dialog navigation, supporting active questioning and route correction using historical landmarks.</td>
<td width="220">aerial visual dialogue navigation</td>
<td width="240">UAV</td>
<td width="260">-</td>
<td width="300">online dialogue VLA</td>
<td width="240">-</td>
<td width="360">Enables UAVs to reach goals through online dialogue and actively correct navigation.</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38878">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38885">History-Enhanced Two-Stage Transformer for Aerial Vision-and-Language Navigation</a></td>
<td width="420">HETT first uses historical grid maps for coarse target localization, then fine-grained visual analysis to optimize UAV actions.</td>
<td width="220">Open-world Environment</td>
<td width="240">large-scale urban UAV</td>
<td width="260">historical grid map</td>
<td width="300">coarse-to-fine two-stage transformer</td>
<td width="240">-</td>
<td width="360">Balances global environment reasoning and local scene understanding in aerial VLN.</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38885">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38897">RENEW: Risk- and Energy-Aware Navigation in Dynamic Waterways</a></td>
<td width="420">RENEW plans risk- and energy-aware paths for ASVs under dynamic water-flow disturbances and adds adaptive safety constraints.</td>
<td width="220">ASV global path planning</td>
<td width="240">dynamic waterways</td>
<td width="260">-</td>
<td width="300">risk/energy-aware planning</td>
<td width="240">-</td>
<td width="360">Water navigation rather than VLN</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38897">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38898">Towards Autonomous UAV Visual Object Search in City Space: Benchmark and Agentic Methodology</a></td>
<td width="420">CityAVOS provides 2,420 urban UAV visual target-search tasks and uses PRPSearcher for perception-reasoning-planning search.</td>
<td width="220">UAV visual object search benchmark</td>
<td width="240">UAV/urban environment</td>
<td width="260">3D cognitive/uncertainty/dynamic semantic maps</td>
<td width="300">open-world navigation</td>
<td width="240">Benchmark</td>
<td width="360">Enables UAVs to autonomously search for static target objects in urban spaces.</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38898">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">CityAVOS 2,420 tasks</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38916">UrbanNav: Learning Language-Guided Embodied Urban Navigation from Web-Scale Human Trajectories</a></td>
<td width="420">UrbanNav aligns webpage-scale urban walking videos with language trajectories, training agents to navigate cities by free-form language.</td>
<td width="220">language-guided urban navigation</td>
<td width="240">ground urban robot</td>
<td width="260">-</td>
<td width="300">open-world navigation</td>
<td width="240">-</td>
<td width="360">Supports last-mile robots in navigating unfamiliar urban streetscapes by natural language.</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38916">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/CASIA-IVA-Lab/UrbanNav">code</a></td>
<td width="240"><a href="https://huggingface.co/datasets/Vigar001/UrbanNav">hf</a></td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38917">Autonomous Vehicle Path Planning by Searching with Differentiable Simulation</a></td>
<td width="420">DSS uses the differentiable Waymax simulator as a state predictor and critic, searching autonomous-driving action sequences through gradients.</td>
<td width="220">autonomous driving path planning</td>
<td width="240">Waymax/traffic scenarios</td>
<td width="260">-</td>
<td width="300">differentiable simulation search</td>
<td width="240">-</td>
<td width="360">Autonomous-driving planning rather than VLN</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38917">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38920">Real-Time Path Planning for UAVs in Windy Environments Without Computational Fluid Dynamics</a></td>
<td width="420">GZS avoids CFD and uses point-cloud local topology plus physics-inspired wind-risk modeling for real-time UAV path planning.</td>
<td width="220">UAV real-time path planning</td>
<td width="240">windy cluttered 3D environments</td>
<td width="260">-</td>
<td width="300">zero-shot training-free planning</td>
<td width="240">-</td>
<td width="360">Performs onboard real-time UAV planning in windy 3D environments with obstacles.</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38920">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38938">ReflexDiffusion: Reflection-Enhanced Trajectory Planning for High-lateral-acceleration Scenarios in Autonomous Driving</a></td>
<td width="420">ReflexDiffusion adds reflective gradient adjustment during diffusion trajectory-planning inference to handle long-tail high-lateral-acceleration scenarios.</td>
<td width="220">autonomous driving trajectory planning</td>
<td width="240">high-lateral-acceleration driving</td>
<td width="260">-</td>
<td width="300">inference-stage diffusion reflection</td>
<td width="240">-</td>
<td width="360">Autonomous-driving planning rather than open VLN</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38938">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38941">Learning from Human Gaze: Human-like Robot Social Navigation in Dense Crowds</a></td>
<td width="420">GazeNav/Gaze2Nav uses human eye-tracking data to predict socially attended objects and injects that attention into motion planning in crowded spaces.</td>
<td width="220">social navigation</td>
<td width="240">dense crowds</td>
<td width="260">gaze/semantic attention</td>
<td width="300">open-world navigation</td>
<td width="240">GazeNav dataset</td>
<td width="360">Enables robots to perform more human-like social navigation in dense crowds.</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38941">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/63554">Plan in Sandbox, Navigate in Open Worlds: Learning Physics-Grounded Abstracted Experience for Embodied Navigation</a></td>
<td width="420">SAGE lets agents learn in a physically grounded semantic abstraction sandbox and then transfer to open-world navigation.</td>
<td width="220">Open-world Environment</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">-</td>
<td width="300">physics-grounded abstracted experience/RL</td>
<td width="240">-</td>
<td width="360">Uses abstract physical experience to reduce reliance on realistic simulation and improve open-world navigation.</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/63554">paper</a></td>
<td width="110" nowrap><a href="https://frankzxshen.github.io/SAGE">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2510.20685">C-NAV: Towards Self-Evolving Continual Object Navigation in Open World</a></td>
<td width="420">C-Nav proposes a continual ObjectNav benchmark and uses a dual-path anti-forgetting mechanism to learn new object categories while preserving old knowledge.</td>
<td width="220">continual ObjectNav benchmark</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">-</td>
<td width="300">dual-path anti-forgetting/RL</td>
<td width="240">-</td>
<td width="360">Continually learns object navigation for new target categories in dynamic open worlds.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2510.20685">paper</a></td>
<td width="110" nowrap><a href="https://bigtree765.github.io/C-Nav-project/">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2512.10046">SimWorld-Robotics: Synthesizing Photorealistic and Dynamic Urban Environments for Multimodal Robot Navigation and Collaboration</a></td>
<td width="420">SimWorld-Robotics uses UE5 procedural generation for dynamic cities and provides a multimodal instruction navigation and multi-robot search collaboration benchmark.</td>
<td width="220">urban simulation benchmark</td>
<td width="240">Unmanned vehicles/urban environments</td>
<td width="260">-</td>
<td width="300">open-world navigation</td>
<td width="240">Sim/Benchmark</td>
<td width="360">Builds large-scale realistic urban simulation to evaluate robot open-environment navigation and collaboration.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2512.10046">paper</a></td>
<td width="110" nowrap><a href="https://scai.cs.jhu.edu/projects/SimWorldRobotics/">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2408.15503">RoboSense: Large-scale Dataset and Benchmark for Egocentric Robot Perception and Navigation in Crowded and Unstructured Environments</a></td>
<td width="420">RoboSense provides multi-sensor egocentric data from cameras, LiDAR, fisheye cameras, and more, evaluating perception and navigation in crowded unstructured environments.</td>
<td width="220">Evaluation/Data</td>
<td width="240">crowded/unstructured egocentric robot environments</td>
<td width="260">-</td>
<td width="300">open-world navigation</td>
<td width="240">Benchmark</td>
<td width="360">Builds a dataset and benchmark for near-field perception and navigation of mobile robots.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2408.15503">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/suhaisheng/RoboSense">code</a></td>
<td width="240"><a href="https://huggingface.co/datasets/suhaisheng0527/RoboSense">hf</a></td>
</tr>
</tbody>
</table>
