# benchmark/dataset

[Home](../../../README.md) | [中文](../../zh-CN/deployment/benchmarks-datasets.md) | [Direction index](README.md)

Total: 44 papers.

<table width="3090">
<thead>
<tr>
<th width="120" nowrap>Venue/Year</th>
<th width="320">Paper/Method</th>
<th width="420">Abstract</th>
<th width="240">Object Type</th>
<th width="280">Efficiency Metric</th>
<th width="280">Platform/Hardware</th>
<th width="280">Covered Tasks</th>
<th width="220">Open Resource Status</th>
<th width="360">Paper Task/Goal</th>
<th width="110" nowrap>Paper</th>
<th width="110" nowrap>Project</th>
<th width="110" nowrap>Code</th>
<th width="240">Data/Bench</th>
</tr>
</thead>
<tbody>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2505.11709">EgoDex: Learning Dexterous Manipulation from Large-Scale Egocentric Video</a></td>
<td width="420">Provides large-scale first-person human hand-object video and a future hand-trajectory prediction benchmark.</td>
<td width="240">human egocentric dexterous HOI dataset</td>
<td width="280">829 h, 338K episodes, 90M 1080p frames, 194 tasks, ~2 TB; data at 30 Hz</td>
<td width="280">Apple Vision Pro (visionOS 2/ARKit); no robot or simulator</td>
<td width="280">194 human tabletop interactions; 48-D two-hand trajectory prediction</td>
<td width="220"><a href="https://github.com/apple/ml-egodex">code/data</a></td>
<td width="360">At 2 s, EncDec+FM K=10 average/final error is 0.038/0.041 m; human-to-robot retargeting is future work, not evaluated</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2505.11709">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/apple/ml-egodex">code</a></td>
<td width="240">EgoDex</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38894">Real Garment Benchmark (RGBench): A Comprehensive Benchmark for Robotic Garment Manipulation Featuring a High-Fidelity Scalable Simulator</a></td>
<td width="420">Benchmarks real-garment simulation fidelity and supplies a scalable FEM GPU simulator and garment assets.</td>
<td width="240">garment/deformable-object simulator benchmark</td>
<td width="280">6K+ meshes, 10+ materials/100+ subtypes; 2.7 ms minimum step; 3–7× faster than Isaac Sim and up to 65× vs MuJoCo at 20K vertices</td>
<td width="280">dual AGILEX Piper or dual JAKA K1 + DH PGC-50-35 grippers; RealSense L515</td>
<td width="280">grasp, fling, fold; simulator fidelity rather than a learned policy</td>
<td width="220"><a href="https://rgbench.github.io/">project</a> / <a href="https://github.com/hwk0809/RGBench">code</a></td>
<td width="360">GarmentDynamics reduces average simulation error by ~20%; grasp/fold Chamfer distance improves by up to 35/58%</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38894">paper</a></td>
<td width="110" nowrap><a href="https://rgbench.github.io/">project</a></td>
<td width="110" nowrap><a href="https://github.com/hwk0809/RGBench">code</a></td>
<td width="240">RGBench / GarmentDynamics; compared with MuJoCo, PyBullet, Isaac Sim</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2023</td>
<td width="320"><a href="https://scholar.google.com/scholar?q=Behavior-1K%3A+A+Benchmark+for+Embodied+AI+with+1%2C000+Everyday+Activities+and+Realistic+Simulation">Behavior-1K: A Benchmark for Embodied AI with 1,000 Everyday Activities and Realistic Simulation</a></td>
<td width="420">Behavior-1K benchmarks embodied AI on 1,000 everyday activities in realistic simulation.</td>
<td width="240">benchmark/dataset</td>
<td width="280">deployment/evaluation coverage</td>
<td width="280">robot/simulator platform</td>
<td width="280">embodied robot tasks</td>
<td width="220">source-listed resource</td>
<td width="360">Add CoRL deployment/evaluation coverage.</td>
<td width="110" nowrap><a href="https://scholar.google.com/scholar?q=Behavior-1K%3A+A+Benchmark+for+Embodied+AI+with+1%2C000+Everyday+Activities+and+Realistic+Simulation">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2022</td>
<td width="320"><a href="https://scholar.google.com/scholar?q=iGibson+2.0%3A+Object-Centric+Simulation+for+Robot+Learning+of+Everyday+Household+Tasks">iGibson 2.0: Object-Centric Simulation for Robot Learning of Everyday Household Tasks</a></td>
<td width="420">iGibson 2.0 provides object-centric simulation for robot learning in household tasks.</td>
<td width="240">benchmark/dataset</td>
<td width="280">deployment/evaluation coverage</td>
<td width="280">robot/simulator platform</td>
<td width="280">embodied robot tasks</td>
<td width="220">source-listed resource</td>
<td width="360">Add CoRL deployment/evaluation coverage.</td>
<td width="110" nowrap><a href="https://scholar.google.com/scholar?q=iGibson+2.0%3A+Object-Centric+Simulation+for+Robot+Learning+of+Everyday+Household+Tasks">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2017</td>
<td width="320"><a href="https://scholar.google.com/scholar?q=CARLA%3A+An+Open+Urban+Driving+Simulator">CARLA: An Open Urban Driving Simulator</a></td>
<td width="420">CARLA is an open urban driving simulator used for embodied driving evaluation.</td>
<td width="240">benchmark/dataset</td>
<td width="280">deployment/evaluation coverage</td>
<td width="280">robot/simulator platform</td>
<td width="280">embodied robot tasks</td>
<td width="220">source-listed resource</td>
<td width="360">Add CoRL deployment/evaluation coverage.</td>
<td width="110" nowrap><a href="https://scholar.google.com/scholar?q=CARLA%3A+An+Open+Urban+Driving+Simulator">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://openaccess.thecvf.com/content/ICCV2025/html/Zhong_UnrealZoo_Enriching_Photo-realistic_Virtual_Worlds_for_Embodied_AI_ICCV_2025_paper.html">UnrealZoo: Enriching Photo-realistic Virtual Worlds for Embodied AI</a></td>
<td width="420">UnrealZoo expands photorealistic virtual worlds for embodied AI training and evaluation.</td>
<td width="240">benchmark/dataset</td>
<td width="280">virtual-world coverage</td>
<td width="280">simulation platform</td>
<td width="280">embodied navigation and interaction</td>
<td width="220">open virtual-world resource</td>
<td width="360">Provide richer simulation environments for embodied AI.</td>
<td width="110" nowrap><a href="https://openaccess.thecvf.com/content/ICCV2025/papers/Zhong_UnrealZoo_Enriching_Photo-realistic_Virtual_Worlds_for_Embodied_AI_ICCV_2025_paper.pdf">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://openaccess.thecvf.com/content/CVPR2025/html/Chen_ActiveGAMER_Active_GAussian_Mapping_through_Efficient_Rendering_CVPR_2025_paper.html">ActiveGAMER: Active GAussian Mapping through Efficient Rendering</a></td>
<td width="420">ActiveGAMER performs active Gaussian mapping with efficient rendering for embodied scene understanding.</td>
<td width="240">mapping/evaluation</td>
<td width="280">mapping efficiency</td>
<td width="280">Gaussian mapping pipeline</td>
<td width="280">active mapping</td>
<td width="220">mapping benchmark/resource</td>
<td width="360">Improve active mapping efficiency for embodied agents.</td>
<td width="110" nowrap><a href="https://openaccess.thecvf.com/content/CVPR2025/papers/Chen_ActiveGAMER_Active_Gaussian_Mapping_through_Efficient_Rendering_CVPR_2025_paper.pdf">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2024</td>
<td width="320"><a href="https://openaccess.thecvf.com/content/CVPR2024/html/Yang_Holodeck_Language_Guided_Generation_of_3D_Embodied_AI_Environments_CVPR_2024_paper.html">Holodeck: Language Guided Generation of 3D Embodied AI Environments</a></td>
<td width="420">Holodeck generates 3D embodied AI environments from language guidance.</td>
<td width="240">benchmark/dataset</td>
<td width="280">3D environment diversity</td>
<td width="280">language-to-environment generator</td>
<td width="280">environment generation</td>
<td width="220">3D embodied environments</td>
<td width="360">Generate diverse 3D scenes for embodied AI evaluation.</td>
<td width="110" nowrap><a href="https://openaccess.thecvf.com/content/CVPR2024/papers/Yang_Holodeck_Language_Guided_Generation_of_3D_Embodied_AI_Environments_CVPR_2024_paper.pdf">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2022</td>
<td width="320"><a href="https://proceedings.neurips.cc/paper_files/paper/2022/hash/27c546ab1e4f1d7d638e6a8dfbad9a07-Abstract-Conference.html">ProcTHOR: Large-Scale Embodied AI Using Procedural Generation</a></td>
<td width="420">ProcTHOR uses procedural generation to create large-scale embodied AI environments.</td>
<td width="240">benchmark/dataset</td>
<td width="280">procedural scene diversity</td>
<td width="280">AI2-THOR environment generation</td>
<td width="280">navigation and interaction tasks</td>
<td width="220">ProcTHOR</td>
<td width="360">Scale embodied-AI evaluation with generated houses.</td>
<td width="110" nowrap><a href="https://proceedings.neurips.cc/paper_files/paper/2022/file/27c546ab1e4f1d7d638e6a8dfbad9a07-Paper-Conference.pdf">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2024</td>
<td width="320"><a href="https://openaccess.thecvf.com/content/CVPR2024/html/Wang_EmbodiedScan_A_Holistic_Multi-Modal_3D_Perception_Suite_Towards_Embodied_AI_CVPR_2024_paper.html">EmbodiedScan: A Holistic Multi-Modal 3D Perception Suite Towards Embodied AI</a></td>
<td width="420">EmbodiedScan provides a multimodal 3D perception suite for embodied AI.</td>
<td width="240">benchmark/dataset</td>
<td width="280">multi-modal 3D perception coverage</td>
<td width="280">dataset + benchmark</td>
<td width="280">3D perception tasks</td>
<td width="220">EmbodiedScan</td>
<td width="360">Benchmark holistic 3D perception for embodied agents.</td>
<td width="110" nowrap><a href="https://openaccess.thecvf.com/content/CVPR2024/papers/Wang_EmbodiedScan_A_Holistic_Multi-Modal_3D_Perception_Suite_Towards_Embodied_AI_CVPR_2024_paper.pdf">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ECCV 2024</td>
<td width="320"><a href="https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/01610.pdf">ReALFRED: An Embodied Instruction Following Benchmark in Photo-Realistic Environments</a></td>
<td width="420">ReALFRED benchmarks embodied instruction following in photorealistic environments.</td>
<td width="240">benchmark/dataset</td>
<td width="280">photorealistic instruction-following coverage</td>
<td width="280">benchmark</td>
<td width="280">instruction following</td>
<td width="220">ReALFRED</td>
<td width="360">Evaluate embodied instruction following in realistic scenes.</td>
<td width="110" nowrap><a href="https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/01610.pdf">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICRA 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2509.14687">RealMirror: A Comprehensive, Open-Source Vision-Language-Action Platform for Embodied AI</a></td>
<td width="420">RealMirror provides a platform for VLA data collection, simulation, training, evaluation, and zero-shot sim-to-real transfer.</td>
<td width="240">VLA platform / benchmark</td>
<td width="280">benchmark/dataset</td>
<td width="280">simulation/evaluation environment</td>
<td width="280">humanoid VLA research</td>
<td width="220">project/code/models available</td>
<td width="360">Lowers the barrier to VLA data, training, and evaluation.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2509.14687">paper</a></td>
<td width="110" nowrap><a href="https://terminators2025.github.io/RealMirror.github.io/">project</a></td>
<td width="110" nowrap><a href="https://github.com/terminators2025/RealMirror">code</a></td>
<td width="240"><a href="https://huggingface.co/zte-terminators/realmirror-model-ckpt">hf</a></td>
</tr>
<tr>
<td width="120" nowrap>IROS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2412.05313">lambda: A Benchmark for Data-Efficiency in Long-Horizon Indoor Mobile Manipulation Robotics</a></td>
<td width="420">The lambda benchmark evaluates long-horizon indoor mobile manipulation for data efficiency, language tasks, and multi-room scenes.</td>
<td width="240">benchmark/dataset</td>
<td width="280">data efficiency</td>
<td width="280">indoor mobile manipulation benchmark</td>
<td width="280">long-horizon mobile manipulation</td>
<td width="220">project/code/data available</td>
<td width="360">Fills the gap in data-efficiency evaluation for long-horizon mobile manipulation.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2412.05313">paper</a></td>
<td width="110" nowrap><a href="https://lambdabenchmark.github.io/">project</a></td>
<td width="110" nowrap><a href="https://github.com/h2r/LAMBDA">code</a></td>
<td width="240"><a href="https://github.com/h2r/LAMBDA">data</a></td>
</tr>
<tr>
<td width="120" nowrap>ICRA 2025</td>
<td width="320"><a href="https://github.com/BAAI-DCAI/SpatialBot">SpatialBot: Precise Spatial Understanding with Vision Language Models</a></td>
<td width="420">SpatialBot targets precise VLM spatial understanding with embodied data, SpatialQA, and SpatialBench.</td>
<td width="240">spatial understanding benchmark</td>
<td width="280">benchmark/dataset</td>
<td width="280">VLM spatial reasoning</td>
<td width="280">embodied spatial QA</td>
<td width="220">model/data/benchmark available</td>
<td width="360">Evaluates whether VLMs have precise spatial understanding for robot manipulation.</td>
<td width="110" nowrap><a href="https://github.com/BAAI-DCAI/SpatialBot">paper</a></td>
<td width="110" nowrap><a href="https://github.com/BAAI-DCAI/SpatialBot">project</a></td>
<td width="110" nowrap><a href="https://github.com/BAAI-DCAI/SpatialBot">code</a></td>
<td width="240"><a href="https://github.com/BAAI-DCAI/SpatialBot">data</a></td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=TRwQND3xpt">D2E: Scaling Vision-Action Pretraining on Desktop Data for Transfer to Embodied AI</a></td>
<td width="420">Uses desktop interaction data to scale vision-action pretraining and transfer it to embodied tasks.</td>
<td width="240">desktop-to-embodied dataset/pretraining</td>
<td width="280">benchmark/dataset</td>
<td width="280">simulation/evaluation environment</td>
<td width="280">vision-action transfer</td>
<td width="220">-</td>
<td width="360">Addresses how to use desktop data for pretraining when robot data is scarce.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=TRwQND3xpt">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=PGUC3mmMoi">RoboInter: A Holistic Intermediate Representation Suite Towards Robotic Manipulation</a></td>
<td width="420">Builds a suite of intermediate representations for robot manipulation to unify evaluation of understanding, planning, and action.</td>
<td width="240">intermediate representation suite</td>
<td width="280">benchmark/dataset</td>
<td width="280">simulation/evaluation environment</td>
<td width="280">robotic manipulation</td>
<td width="220">-</td>
<td width="360">Addresses the lack of reusable intermediate-representation benchmarks for manipulation learning.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=PGUC3mmMoi">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=UUE6HEtjhu">AutoBio: A Simulation and Benchmark for Robotic Automation in Digital Biology Laboratory</a></td>
<td width="420">Provides simulation and benchmarks for robot automation in digital biology labs.</td>
<td width="240">benchmark/dataset</td>
<td width="280">benchmark/dataset</td>
<td width="280">digital biology laboratory simulation</td>
<td width="280">lab automation</td>
<td width="220">-</td>
<td width="360">Addresses the lack of simulation and evaluation environments for biology-lab automation.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=UUE6HEtjhu">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=azj53PLJRL">Image Quality Assessment for Embodied AI</a></td>
<td width="420">Studies embodied AI observation image quality assessment and its impact on task performance.</td>
<td width="240">image quality benchmark</td>
<td width="280">benchmark/dataset</td>
<td width="280">simulation/evaluation environment</td>
<td width="280">embodied perception/evaluation</td>
<td width="220">-</td>
<td width="360">Addresses the lack of task-relevant evaluation for embodied perception input quality.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=azj53PLJRL">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=tQJYKwc3n4">RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots</a></td>
<td width="420">Provides a large-scale home-scene simulation framework for training and evaluating general-purpose robots.</td>
<td width="240">benchmark/dataset</td>
<td width="280">benchmark/dataset</td>
<td width="280">RoboCasa simulation</td>
<td width="280">generalist household robotics</td>
<td width="220">-</td>
<td width="360">Addresses the lack of diverse, long-horizon, scalable simulation benchmarks for general-purpose robots.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=tQJYKwc3n4">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38875">H-RDT: Human Manipulation Enhanced Bimanual Robotic Manipulation</a></td>
<td width="420">Leverages egocentric human manipulation data to pretrain a diffusion-transformer policy for stronger bimanual robot manipulation.</td>
<td width="240">benchmark/dataset</td>
<td width="280">benchmark/dataset</td>
<td width="280">simulation/evaluation environment</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38875">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38883">PEOD: A Pixel-Aligned Event-RGB Benchmark for Object Detection Under Challenging Conditions</a></td>
<td width="420">Provides a high-resolution pixel-aligned Event-RGB object-detection benchmark for low-light, overexposed, and high-speed scenes.</td>
<td width="240">benchmark/dataset</td>
<td width="280">benchmark/dataset</td>
<td width="280">simulation/evaluation environment</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38883">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38913">SIAM: Towards Generalizable Articulated Object Modeling via Single Robot-Object Interaction</a></td>
<td width="420">Infers articulated-object part segmentation, kinematics, and URDF-style models from a single robot-object interaction.</td>
<td width="240">benchmark/dataset</td>
<td width="280">benchmark/dataset</td>
<td width="280">simulation/evaluation environment</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38913">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38923">VirtualEnv: A Platform for Embodied AI Research</a></td>
<td width="420">Provides an Unreal Engine 5 simulation platform for evaluating LLM/VLM agents in interactive embodied tasks.</td>
<td width="240">benchmark/dataset</td>
<td width="280">benchmark/dataset</td>
<td width="280">simulation/evaluation environment</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38923">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38930">Lifelong Language-Conditioned Robotic Manipulation Learning</a></td>
<td width="420">Introduces SkillsCrafter for continual language-conditioned manipulation while reducing catastrophic forgetting across skills.</td>
<td width="240">benchmark/dataset</td>
<td width="280">benchmark/dataset</td>
<td width="280">simulation/evaluation environment</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38930">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/64411">AIR-VLA: Vision-Language-Action Systems for Aerial Manipulation</a></td>
<td width="420">Builds a simulation, dataset, and benchmark for VLA/VLM evaluation on aerial manipulation systems.</td>
<td width="240">benchmark/dataset</td>
<td width="280">benchmark/dataset</td>
<td width="280">UAV / aerial robot</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/64411">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/63391">DLO-Lab: Benchmarking Deformable Linear Object Manipulations with Differentiable Physics</a></td>
<td width="420">Provides a differentiable-physics simulator and benchmark for deformable linear-object manipulation and sim-to-real study.</td>
<td width="240">benchmark/dataset</td>
<td width="280">benchmark/dataset</td>
<td width="280">simulation/evaluation environment</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/63391">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/63416">ManiSoft: Towards Vision-Language Manipulation for Soft Robotics</a></td>
<td width="420">Provides a soft-arm simulation benchmark with language-conditioned tasks and expert trajectories for vision-language manipulation.</td>
<td width="240">benchmark/dataset</td>
<td width="280">benchmark/dataset</td>
<td width="280">robot deployment/evaluation environment</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/63416">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/64619">OXE-AugE: A Large-Scale Robot Augmentation of OXE for Scaling Cross-Embodiment Policy Learning</a></td>
<td width="420">Augments Open X-Embodiment with diverse robot embodiments to scale cross-embodiment policy learning.</td>
<td width="240">benchmark/dataset</td>
<td width="280">benchmark/dataset</td>
<td width="280">robot deployment/evaluation environment</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/64619">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2506.07961">BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models</a></td>
<td width="420">Uses input-output alignment and the BridgeVLA dataset to improve the learning efficiency of VLM-to-3D manipulation policies.</td>
<td width="240">benchmark/dataset</td>
<td width="280">benchmark/dataset</td>
<td width="280">robot deployment/evaluation environment</td>
<td width="280">3D manipulation</td>
<td width="220">Project+Code+Data/Bench</td>
<td width="360">Addresses input-output space mismatch when VLMs learn 3D manipulation.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2506.07961">paper</a></td>
<td width="110" nowrap><a href="https://bridgevla.github.io/">project</a></td>
<td width="110" nowrap><a href="https://github.com/BridgeVLA/BridgeVLA">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2506.14763">RobotSmith: Generative Robotic Tool Design for Acquisition of Complex Manipulation Skills</a></td>
<td width="420">Uses generative tool design to give robots complex manipulation skills for rigid, deformable, and fluid objects.</td>
<td width="240">benchmark/dataset</td>
<td width="280">benchmark/dataset</td>
<td width="280">robot deployment/evaluation environment</td>
<td width="280">tool-design manipulation</td>
<td width="220">Project+Code</td>
<td width="360">Addresses the need for robots to use task-specific tools to complete complex manipulation.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2506.14763">paper</a></td>
<td width="110" nowrap><a href="https://umass-embodied-agi.github.io/RobotSmith/">project</a></td>
<td width="110" nowrap><a href="https://github.com/UMass-Embodied-AGI/RobotSmith">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2511.00940">URDF-Anything: Constructing Articulated Objects with 3D Multimodal Language Model</a></td>
<td width="420">Uses a 3D multimodal language model to construct articulated-object URDFs from multimodal inputs.</td>
<td width="240">articulated object URDF construction</td>
<td width="280">benchmark/dataset</td>
<td width="280">robot deployment/evaluation environment</td>
<td width="280">3D object modeling for simulation</td>
<td width="220">-</td>
<td width="360">Addresses the high cost of building articulated object URDFs for simulation/robot interaction.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2511.00940">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2506.08822">FreqPolicy: Efficient Flow-based Visuomotor Policy via Frequency Consistency</a></td>
<td width="420">Uses frequency consistency constraints to improve the efficiency and stability of flow-based visuomotor policies.</td>
<td width="240">benchmark/dataset</td>
<td width="280">frequency consistency</td>
<td width="280">robot deployment/evaluation environment</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">Addresses high-frequency/low-frequency action inconsistency in flow policy for visuomotor control.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2506.08822">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://www.arxiv.org/pdf/2506.06677">RoboCerebra: A Large-scale Benchmark for Long-horizon Robotic Manipulation Evaluation</a></td>
<td width="420">Provides a long-horizon home robot manipulation benchmark for evaluating planning, reflection, and memory.</td>
<td width="240">benchmark/dataset</td>
<td width="280">benchmark/dataset</td>
<td width="280">simulation/evaluation environment</td>
<td width="280">100 task variants / 1,000 trajectories</td>
<td width="220">Project+Code+Data/Bench</td>
<td width="360">Addresses the lack of systematic evaluation for long-horizon robot manipulation.</td>
<td width="110" nowrap><a href="https://www.arxiv.org/pdf/2506.06677">paper</a> / <a href="https://arxiv.org/pdf/2506.06677">paper</a></td>
<td width="110" nowrap><a href="https://robocerebra.github.io/">project</a></td>
<td width="110" nowrap><a href="https://github.com/qiuboxiang/RoboCerebra">code</a> / <a href="https://github.com/buaa-colalab/RoboCerebra">code</a></td>
<td width="240"><a href="https://huggingface.co/datasets/qiukingballball/RoboCerebra">hf</a> / <a href="https://huggingface.co/datasets/qiukingballball/RoboCerebraBench">hf</a></td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://suturebot.github.io/static/SutureBot_NeurIPS_2025.pdf">SutureBot: A Precision Framework &amp; Benchmark For Autonomous End-to-End Suturing</a></td>
<td width="420">Provides a dVRK end-to-end autonomous suturing framework, dataset, and fine-grained evaluation benchmark.</td>
<td width="240">benchmark/dataset</td>
<td width="280">benchmark/dataset</td>
<td width="280">dVRK Si + wrist cameras/endoscope</td>
<td width="280">-</td>
<td width="220">Project+Code+Data/Bench</td>
<td width="360">Addresses the lack of end-to-end benchmarks and data for autonomous robotic suturing.</td>
<td width="110" nowrap><a href="https://suturebot.github.io/static/SutureBot_NeurIPS_2025.pdf">paper</a></td>
<td width="110" nowrap><a href="https://suturebot.github.io/">project</a></td>
<td width="110" nowrap><a href="https://github.com/SutureBot/SutureBot/tree/ACT">code</a></td>
<td width="240"><a href="https://huggingface.co/datasets/jchen396/SutureBot">hf</a></td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2503.08367">Embodied Crowd Counting</a></td>
<td width="420">Defines embodied crowd counting with a drone simulator, ECCD dataset, and zero-shot navigation baseline.</td>
<td width="240">benchmark/dataset</td>
<td width="280">benchmark/dataset</td>
<td width="280">robot deployment/evaluation environment</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2503.08367">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2412.06782">CARP: Visuomotor Policy Learning via Coarse-to-Fine Autoregressive Prediction</a></td>
<td width="420">Improves visuomotor policy learning through coarse-to-fine autoregressive prediction.</td>
<td width="240">benchmark/dataset</td>
<td width="280">benchmark/dataset</td>
<td width="280">robot deployment/evaluation environment</td>
<td width="280">-</td>
<td width="220">Project</td>
<td width="360">Addresses the difficulty of direct continuous robot action prediction and long-horizon error accumulation.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2412.06782">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2503.16408">RoboFactory: Exploring Embodied Agent Collaboration with Compositional Constraints</a></td>
<td width="420">Builds a collaborative simulation and dataset for multiple embodied agents with compositional constraints.</td>
<td width="240">benchmark/dataset</td>
<td width="280">benchmark/dataset</td>
<td width="280">simulation</td>
<td width="280">-</td>
<td width="220">Project+Code+Data/Bench</td>
<td width="360">Addresses insufficient evaluation of compositional constraints in embodied agent collaboration tasks.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2503.16408">paper</a></td>
<td width="110" nowrap><a href="https://iranqin.github.io/robofactory/">project</a></td>
<td width="110" nowrap><a href="https://github.com/MARS-EAI/RoboFactory">code</a></td>
<td width="240"><a href="https://huggingface.co/datasets/FACEONG/RoboFactory_Dataset">hf</a></td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2504.10414">HUMOTO: A 4D Dataset of Mocap Human Object Interactions</a></td>
<td width="420">Provides a 4D motion-capture dataset for human-object interaction.</td>
<td width="240">4D mocap HOI dataset</td>
<td width="280">benchmark/dataset</td>
<td width="280">simulation/evaluation environment</td>
<td width="280">-</td>
<td width="220">Project</td>
<td width="360">Addresses the shortage of dynamic data for humans manipulating objects.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2504.10414">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2412.07215">RoboTron-Mani: All-in-One Multimodal Large Model for Robotic Manipulation</a></td>
<td width="420">Proposes the RoboTron-Mani model and RoboData, using multimodal data to support robot manipulation.</td>
<td width="240">RoboTron-Mani + RoboData</td>
<td width="280">benchmark/dataset</td>
<td width="280">robot deployment/evaluation environment</td>
<td width="280">-</td>
<td width="220">Code+Data/Bench</td>
<td width="360">Addresses the need for unified multimodal training and evaluation data for robot manipulation models.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2412.07215">paper</a> / <a href="https://arxiv.org/pdf/2412.07215">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/RoboUniview/RoboMM">code</a></td>
<td width="240"><a href="https://huggingface.co/datasets/liufanfanlff/RoboData">hf</a></td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2503.11117">Beyond the Destination: A Novel Benchmark for Exploration-Aware Embodied Question Answering</a></td>
<td width="420">Proposes EXPRESS-Bench, which binds exploration trajectories with QA to evaluate embodied QA.</td>
<td width="240">benchmark/dataset</td>
<td width="280">benchmark/dataset</td>
<td width="280">simulation/evaluation environment</td>
<td width="280">777 trajectories / 2,044 QA pairs</td>
<td width="220">Code</td>
<td width="360">Addresses EQA focusing only on destinations and not evaluating the exploration process.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2503.11117">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">EXPRESS-Bench</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://iccv.thecvf.com/virtual/2025/poster/1787">RobAVA: A Large-scale Dataset and Baseline Towards Video based Robotic Arm Action Understanding</a></td>
<td width="420">Provides a large-scale video dataset and baseline for robotic arm action understanding.</td>
<td width="240">benchmark/dataset</td>
<td width="280">benchmark/dataset</td>
<td width="280">simulation/evaluation environment</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">Provide training/evaluation data resources.</td>
<td width="110" nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/1787">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://iccv.thecvf.com/virtual/2025/poster/2215">RoboAnnotatorX: A Comprehensive and Universal Annotation Framework for Accurate Understanding of Long-horizon Robot Demonstration</a></td>
<td width="420">Provides a multimodal annotation framework for producing rich labels from long-horizon robot demonstrations.</td>
<td width="240">benchmark/dataset</td>
<td width="280">benchmark/dataset</td>
<td width="280">robot deployment/evaluation environment</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/2215">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2502.09560">EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents</a></td>
<td width="420">Comprehensively evaluates MLLMs' navigation, interaction, and reasoning abilities in visually driven embodied agents.</td>
<td width="240">benchmark/dataset</td>
<td width="280">benchmark/dataset</td>
<td width="280">simulation/evaluation environment</td>
<td width="280">1,128 tasks / 4 environments / 6 capability subsets</td>
<td width="220">Project+Code</td>
<td width="360">Addresses the lack of unified benchmarks for embodied capabilities of multimodal large models.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2502.09560">paper</a></td>
<td width="110" nowrap><a href="https://embodiedbench.github.io/">project</a></td>
<td width="110" nowrap><a href="https://github.com/EmbodiedBench/EmbodiedBench">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2411.18025">Pixel-aligned RGB-NIR Stereo Imaging and Dataset for Robot Vision</a></td>
<td width="420">Provides a pixel-aligned RGB-NIR binocular imaging system and robot vision dataset.</td>
<td width="240">RGB-NIR stereo dataset</td>
<td width="280">benchmark/dataset</td>
<td width="280">simulation/evaluation environment</td>
<td width="280">robot vision</td>
<td width="220">-</td>
<td width="360">Addresses the lack of aligned data for robot vision under visible-light/NIR fusion.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2411.18025">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
</tbody>
</table>
