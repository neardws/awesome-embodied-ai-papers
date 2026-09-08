# sim2real

[Home](../../../README.md) | [中文](../../zh-CN/deployment/sim2real.md) | [Direction index](README.md)

Total: 20 papers.

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
<td width="120" nowrap>CoRL 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2505.03233">GraspVLA: a Grasping Foundation Model Pre-trained on Billion-scale Synthetic Action Data</a></td>
<td width="420">Pretrains a language-conditioned closed-loop grasp VLA on synthetic action data and transfers it to real robots.</td>
<td width="240">open-vocabulary parallel-gripper grasping</td>
<td width="280">SynGrasp-1B: 10M trajectories/~1B frames; real mean 84.7%; 5 Hz model execution; 5K synthetic trajectories adapt a new embodiment/view</td>
<td width="280">Main: Franka Panda + original two-finger gripper (fingers extended 2 cm), D435 front + D415i side; adaptation: UR5e + Robotiq 2F-85</td>
<td width="280">language-conditioned closed-loop grasping and embodiment/view adaptation</td>
<td width="220"><a href="https://pku-epic.github.io/GraspVLA-web/">project</a> / <a href="https://github.com/PKU-EPIC/GraspVLA">code</a></td>
<td width="360">Use billion-scale synthetic action supervision to reduce real grasp data; real overall/language/arbitrary/transparent success 93.3/93.3/93.3/86.6%</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2505.03233">paper</a></td>
<td width="110" nowrap><a href="https://pku-epic.github.io/GraspVLA-web/">project</a></td>
<td width="110" nowrap><a href="https://github.com/PKU-EPIC/GraspVLA">code</a></td>
<td width="240">SynGrasp-1B; CuRobo planning + MuJoCo physics validation + Isaac Sim rendering; LIBERO evaluation</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://openaccess.thecvf.com/content/CVPR2025/html/Wang_MobileH2R_Learning_Generalizable_Human_to_Mobile_Robot_Handover_Exclusively_from_CVPR_2025_paper.html">MobileH2R: Learning Generalizable Human to Mobile Robot Handover Exclusively from Scalable and Diverse Synthetic Data</a></td>
<td width="420">Trains mobile human-to-robot object reception exclusively from scalable synthetic human motion and 4D imitation learning.</td>
<td width="240">mobile manipulation / human-to-robot handover</td>
<td width="280">100K+ synthetic demonstrations; real simple/complex success 80.0/63.3% vs baseline 40.0/30.0% over 30 trials/setting</td>
<td width="280">Galbot G1 mobile base + single left 7-DoF arm + gripper</td>
<td width="280">whole-body approach and object reception from humans</td>
<td width="220"><a href="https://mobileh2r.github.io/">project</a></td>
<td width="360">Bridge a large mobile workspace without collecting real handover demonstrations; this is not bimanual manipulation.</td>
<td width="110" nowrap><a href="https://openaccess.thecvf.com/content/CVPR2025/html/Wang_MobileH2R_Learning_Generalizable_Human_to_Mobile_Robot_Handover_Exclusively_from_CVPR_2025_paper.html">paper</a></td>
<td width="110" nowrap><a href="https://mobileh2r.github.io/">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">MobileH2R-Sim (PyBullet + Ray); 8,836 ShapeNet objects</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2018</td>
<td width="320"><a href="https://scholar.google.com/scholar?q=Sim-to-Real+Reinforcement+Learning+for+Deformable+Object+Manipulation">Sim-to-Real Reinforcement Learning for Deformable Object Manipulation</a></td>
<td width="420">This work transfers reinforcement learning from simulation to deformable object manipulation.</td>
<td width="240">sim2real</td>
<td width="280">deployment/evaluation coverage</td>
<td width="280">robot/simulator platform</td>
<td width="280">embodied robot tasks</td>
<td width="220">source-listed resource</td>
<td width="360">Add CoRL deployment/evaluation coverage.</td>
<td width="110" nowrap><a href="https://scholar.google.com/scholar?q=Sim-to-Real+Reinforcement+Learning+for+Deformable+Object+Manipulation">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=W3Q2xvrZtx">PD$^{2}$GS: Part-Level Decoupling and Continuous Deformation of Articulated Objects via Gaussian Splatting</a></td>
<td width="420">Models articulated objects using part-level disentanglement and continuously deformable Gaussian representations.</td>
<td width="240">articulated object Gaussian Splatting</td>
<td width="280">sim2real</td>
<td width="280">simulation/evaluation environment</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">Addresses deformable modeling of articulated objects in real/simulated settings.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=W3Q2xvrZtx">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=sWyX1BpeN4">Manipulation as in Simulation: Enabling Accurate Geometry Perception in Robots</a></td>
<td width="420">Enables robots to obtain simulation-like accurate geometric perception to improve real-world manipulation.</td>
<td width="240">geometry perception for manipulation</td>
<td width="280">sim2real</td>
<td width="280">simulation/evaluation environment</td>
<td width="280">real robot manipulation</td>
<td width="220">-</td>
<td width="360">Addresses the sim2real manipulation gap caused by geometric perception noise on real robots.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=sWyX1BpeN4">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=nAO9LcV7nE">Emergent Dexterity Via Diverse Resets and Large-Scale Reinforcement Learning</a></td>
<td width="420">Elicits dexterous manipulation abilities through diverse resets and large-scale RL training.</td>
<td width="240">dexterous RL</td>
<td width="280">sim2real</td>
<td width="280">sim + robot hand likely</td>
<td width="280">dexterous manipulation</td>
<td width="220">-</td>
<td width="360">Addresses training dexterous manipulation policies in simulation for recovery from complex states.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=nAO9LcV7nE">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=H4SyKHjd4c">Sim2Real VLA: Zero-Shot Generalization of Synthesized Skills to Realistic Manipulation</a></td>
<td width="420">Transfers synthetically skill-trained VLA zero-shot to photorealistic manipulation environments.</td>
<td width="240">sim2real VLA</td>
<td width="280">sim2real</td>
<td width="280">simulation/evaluation environment</td>
<td width="280">realistic manipulation</td>
<td width="220">-</td>
<td width="360">Addresses generalization from synthetic skills to real robot manipulation.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=H4SyKHjd4c">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=TmYcqOnxhN">Exo-Plore: Exploring Exoskeleton Control Space through Human-aligned Simulation</a></td>
<td width="420">Uses human-aligned simulation to explore exoskeleton control spaces.</td>
<td width="240">exoskeleton control</td>
<td width="280">sim2real</td>
<td width="280">human-aligned simulation/exoskeleton</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">Addresses the difficulty of safely and efficiently exploring exoskeleton control policies.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=TmYcqOnxhN">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=yn9dzttHvT">Latent Adaptation of Foundation Policies for Sim-to-Real Transfer</a></td>
<td width="420">Adapts foundation policy in latent space to perform sim-to-real transfer.</td>
<td width="240">latent policy adaptation</td>
<td width="280">sim2real</td>
<td width="280">simulation/evaluation environment</td>
<td width="280">sim-to-real policy transfer</td>
<td width="220">-</td>
<td width="360">Addresses performance degradation of foundation robot policies under real-domain distribution shifts.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=yn9dzttHvT">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=OutljIofvS">RobotArena ∞: Scalable Robot Benchmarking via Real-to-Sim Translation</a></td>
<td width="420">Expands evaluable benchmarks for real robot scenes through real-to-sim translation.</td>
<td width="240">real-to-sim benchmark</td>
<td width="280">sim2real</td>
<td width="280">simulation/evaluation environment</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">Addresses the high cost of scaling real robot benchmarks.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=OutljIofvS">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=xlr3NqxUqY">Contact-guided Real2Sim from Monocular Video with Planar Scene Primitives</a></td>
<td width="420">Reconstructs real2sim scenes from monocular video using contact cues and planar scene primitives.</td>
<td width="240">contact-guided Real2Sim</td>
<td width="280">sim2real</td>
<td width="280">monocular video</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">Addresses the lack of physical contact constraints when converting monocular video to simulation.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=xlr3NqxUqY">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/66662">FlatLab: A Unified Methodology Framework and Simulation-Based Benchmark for Robotic Manipulation of Flat Objects</a></td>
<td width="420">Provides a unified framework and simulation benchmark for manipulating flat objects with varied geometry and material.</td>
<td width="240">benchmark/dataset</td>
<td width="280">sim2real</td>
<td width="280">simulation/evaluation environment</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/66662">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2602.20871">GeCo-SRT: Geometry-aware Continual Adaptation for Robotic Cross-Task Sim-to-Real Transfer</a></td>
<td width="420">Uses geometry-aware continual adaptation to support cross-task sim-to-real transfer.</td>
<td width="240">continual sim-to-real adaptation</td>
<td width="280">sim2real</td>
<td width="280">simulation/evaluation environment</td>
<td width="280">-</td>
<td width="220">Project</td>
<td width="360">Addresses geometric differences and continual adaptation in cross-task real-world transfer of robot policies.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2602.20871">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2509.19626">EgoBridge: Domain Adaptation for Generalizable Imitation from Egocentric Human Data</a></td>
<td width="420">Applies domain adaptation to egocentric human data for generalizable robot imitation learning.</td>
<td width="240">human-to-robot domain adaptation</td>
<td width="280">sim2real</td>
<td width="280">robot deployment/evaluation environment</td>
<td width="280">-</td>
<td width="220">Project</td>
<td width="360">Addresses the domain gap from egocentric human data to robot policies.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2509.19626">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://openreview.net/forum?id=284GWLFtjU">DEAL: Diffusion Evolution Adversarial Learning for Sim-to-Real Transfer</a></td>
<td width="420">Combines diffusion evolution and adversarial learning to tune simulators and reduce the sim-to-real gap for RL controllers.</td>
<td width="240">benchmark/dataset</td>
<td width="280">benchmark/dataset</td>
<td width="280">simulation/evaluation environment</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">reduce sim-to-real gap</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=284GWLFtjU">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2509.18631">Generalizable Domain Adaptation for Sim-and-Real Policy Co-Training</a></td>
<td width="420">Uses sim-and-real policy co-training to improve cross-domain generalization.</td>
<td width="240">domain adaptation / co-training</td>
<td width="280">sim2real</td>
<td width="280">robot deployment/evaluation environment</td>
<td width="280">-</td>
<td width="220">Project</td>
<td width="360">Addresses how domain shift affects policy generalization when jointly training on simulated and real data.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2509.18631">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2505.22634">LabUtopia: High-Fidelity Simulation and Hierarchical Benchmark for Scientific Embodied Agents</a></td>
<td width="420">Provides high-fidelity simulation, scene generation, and hierarchical benchmarks for scientific labs.</td>
<td width="240">benchmark/dataset</td>
<td width="280">sim2real</td>
<td width="280">LabSim</td>
<td width="280">30 lab tasks / 200+ assets</td>
<td width="220">Project</td>
<td width="360">Addresses the lack of simulation and evaluation for complex experimental workflows in scientific embodied agents.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2505.22634">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2507.01152">SonoGym: High Performance Simulation for Challenging Surgical Tasks with Robotic Ultrasound</a></td>
<td width="420">Provides parallelizable simulation environments and tasks for robotic ultrasound surgery.</td>
<td width="240">benchmark/dataset</td>
<td width="280">sim2real</td>
<td width="280">robotic ultrasound</td>
<td width="280">-</td>
<td width="220">Code</td>
<td width="360">Addresses the lack of realistic and efficient simulation training environments for robotic ultrasound navigation/reconstruction.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2507.01152">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/SonoGym/SonoGym">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2506.22756">RoboPearls: Editable Video Simulation for Robot Manipulation</a></td>
<td width="420">Uses 3DGS to build editable, photorealistic robot manipulation simulations from demonstration videos.</td>
<td width="240">benchmark/dataset</td>
<td width="280">editable video simulation</td>
<td width="280">simulation/evaluation environment</td>
<td width="280">-</td>
<td width="220">Project</td>
<td width="360">Addresses expensive real demonstration collection and the large sim2real gap in traditional simulation.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2506.22756">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2409.02920">RoboTwin: Dual-Arm Robot Benchmark with Generative Digital Twins (early version)</a></td>
<td width="420">Uses generative digital twins to create dual-arm manipulation data and a real-aligned evaluation platform.</td>
<td width="240">benchmark/dataset</td>
<td width="280">benchmark/dataset</td>
<td width="280">dual-arm robot / COBOT Magic</td>
<td width="280">-</td>
<td width="220">Project+Code+Data/Bench</td>
<td width="360">Addresses the scarcity of dual-arm manipulation data and the mismatch between simulation evaluation and reality.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2409.02920">paper</a></td>
<td width="110" nowrap><a href="https://robotwin-benchmark.github.io/early-version/">project</a></td>
<td width="110" nowrap><a href="https://github.com/RoboTwin-Platform/RoboTwin">code</a></td>
<td width="240"><a href="https://huggingface.co/datasets/TianxingChen/RoboTwin">hf</a></td>
</tr>
</tbody>
</table>
