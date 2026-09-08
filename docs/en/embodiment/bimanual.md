# bimanual

[Home](../../../README.md) | [中文](../../zh-CN/embodiment/bimanual.md) | [Direction index](README.md)

Total: 12 papers. DexH2R was moved to dexterous hand because the robot receiver is a single UR10e + ShadowHand; MobileH2R was moved to sim2real because it controls a mobile base and one left arm rather than two robot arms. SARM was moved here from dexterous hand because its platform is a dual-YAM parallel-gripper system.

The direction-specific fields distinguish the physical dual-arm embodiment, inter-arm coupling, action interface, simulator/data role, and coordination evidence. “Not disclosed” is used when the paper does not identify a model, engine, rate, or metric; it is not inferred from a neighboring benchmark.

<table width="3040">
<thead>
<tr>
<th width="100" nowrap>Venue/Year</th>
<th width="270">Paper/Method</th>
<th width="260">Problem/Goal</th>
<th width="300">Exact Embodiment/End-Effectors</th>
<th width="180">Sensing/Contact</th>
<th width="300">Bimanual Coupling/Task Division</th>
<th width="200">Control/Action Interface</th>
<th width="200">Training Method</th>
<th width="360">Simulation/Training Environment + Data Scale</th>
<th width="110">Sim/Real Role</th>
<th width="330">Coordination/Generalization Metrics</th>
<th width="250">Evidence Boundary</th>
<th width="180">Resources</th>
</tr>
</thead>
<tbody>
<tr>
<td width="100" nowrap>ICLR 2025</td>
<td width="270"><a href="https://openreview.net/forum?id=yAzN4tz7oI">RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation</a></td>
<td width="260">Scale a language-conditioned bimanual diffusion policy across heterogeneous robot datasets, then adapt it with limited target demonstrations.</td>
<td width="300">AgileX Cobot Mobile ALOHA; dual 6-DoF arms and two 0–80 mm parallel grippers. The mobile base carries the rig but is not controlled by the policy.</td>
<td width="180">Front RGB + two wrist RGB cameras; dual-arm/gripper proprioception; no tactile sensing reported.</td>
<td width="300">One diffusion policy jointly predicts both arm/gripper chunks; no fixed leader/follower. Tasks include handover, folding, and hand-specified pouring.</td>
<td width="200">Joint-position action chunks for both 6-DoF arms and two grippers.</td>
<td width="200">Multi-embodiment diffusion pretraining followed by target ALOHA fine-tuning.</td>
<td width="360">No unified simulator. Pretraining uses 46 datasets, &gt;1M trajectories, and 21 TB; target ALOHA tuning covers 300+ tasks, 6K+ trajectories, and 3M+ frames.</td>
<td width="110">Target Real; mixed-source pretraining; not a Sim2Real pipeline</td>
<td width="330">Combined evaluation 68.2%; Handover 40%, Fold Shorts 68%, Robot Dog 76%; two specified-hand pouring variants reach 100%/87.5% total success.</td>
<td width="250">Target evaluation is real-only and several long-horizon tasks remain below 70%; the mobile base is outside the learned action space.</td>
<td width="180"><a href="https://openreview.net/forum?id=yAzN4tz7oI">OpenReview</a> / <a href="https://arxiv.org/abs/2410.07864">arXiv</a></td>
</tr>
<tr>
<td width="100" nowrap>ICRA 2025</td>
<td width="270"><a href="https://dexmimicgen.github.io/">DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning</a></td>
<td width="260">Generate large bimanual imitation datasets from a few seed demonstrations while preserving parallel, coordinated, and sequential constraints.</td>
<td width="300">Simulation: dual Franka Panda + parallel grippers, dual Franka + unnamed dexterous hands, and Fourier GR-1 + unnamed dexterous hands. Real: Fourier GR1 + dual 6-DoF Inspire hands.</td>
<td width="180">Simulation state/vision; real head/external RealSense D435i RGB-D plus robot state.</td>
<td width="300">Left/right subtask queues encode parallel execution, shared-object transforms with synchronous completion, or explicit sequential ordering.</td>
<td width="200">Object-centric transformed dual-arm demonstrations used to train imitation policies.</td>
<td width="200">Seed-demo segmentation + automated MimicGen-style generation + imitation learning.</td>
<td width="360">robosuite + MuJoCo: 9 tasks, 60 seeds, 1,000 generated demos/task (9K main; 21K total reported). BiGym: 3×1,000. Real can sorting: 4 seeds → 40 successful digital-twin demos.</td>
<td width="110">Sim primary; one real-to-sim-to-real task</td>
<td width="330">Sim success: Piece Assembly 80.7%, Threading 69.3%, Transport 83.3%, Tray Lift 88.7%, Can Sorting 97.3%. Real can sorting: generated data 90% vs four seeds 0% over 20 trials.</td>
<td width="250">Real validation covers one task; the simulated dexterous-hand models are not named.</td>
<td width="180"><a href="https://dexmimicgen.github.io/">paper/project</a> / <a href="https://github.com/NVlabs/dexmimicgen/">code</a></td>
</tr>
<tr>
<td width="100" nowrap>ICLR 2026</td>
<td width="270"><a href="https://openreview.net/forum?id=jG9W6nAwVz">TwinVLA: Data-Efficient Bimanual Manipulation with Twin Single-Arm Vision-Language-Action Models</a></td>
<td width="260">Reuse single-arm VLA pretraining when large bimanual datasets are unavailable.</td>
<td width="300">Real self-developed Anubis: dual 6-DoF arms + ALOHA-style transparent parallel grippers; three-wheel base unused. Tabletop-Sim uses ALOHA2 assets.</td>
<td width="180">Shared egocentric RGB; one RealSense D405 at each wrist; per-arm proprioception.</td>
<td width="300">Two arm-specific branches share language/ego inputs; Joint Attention exchanges cross-arm tokens and layer-level MoE emits separate action chunks.</td>
<td width="200">Separate left/right action chunks from two coordinated VLA branches.</td>
<td width="200">Copy SingleVLA weights, then fine-tune each target task with 50 bimanual episodes.</td>
<td width="360">SingleVLA: ~0.5M OXE demos/~800 h. RoboTwin 2.0/SAPIEN: 50 tasks × 50 demos. Tabletop-Sim/dm_control: 5 × 50. Real: 50 episodes/task.</td>
<td width="110">Pretrain + separate Sim/Real evaluation; not Sim2Real</td>
<td width="330">Real five-task mean 71.0%; RoboTwin Easy/Hard 42.0/8.9%; Tabletop-Sim Easy/Hard 75.8/42.9%. Removing Joint Attention costs 27.0 pp on real tasks.</td>
<td width="250">No bimanual pretraining; hard-split success is low and each target task still needs 50 demonstrations.</td>
<td width="180"><a href="https://openreview.net/forum?id=jG9W6nAwVz">paper</a> / <a href="https://jellyho.github.io/TwinVLA/">project</a></td>
</tr>
<tr>
<td width="100" nowrap>ICLR 2026</td>
<td width="270"><a href="https://openreview.net/forum?id=he86smZzRk">VLBiMan: Vision-Language Anchored One-Shot Demonstration Enables Generalizable Bimanual Robotic Manipulation</a></td>
<td width="260">Generalize bimanual skills from one kinesthetic demonstration under object, scene, and dynamic-distractor changes.</td>
<td width="300">Main: dual Aubo-i5 6-DoF arms + DH-Robotics 80 mm parallel grippers. Transfer: dual Rokae xMate CR73 + Jodell RG75-3004 75 mm grippers.</td>
<td width="180">Kingfisher R-6000 third-person stereo; no wrist camera, force, or tactile sensor.</td>
<td width="300">Decomposes per-arm atomic skills and inter-arm dependencies; supports synchronous/asynchronous execution with VLM anchors, IK, and collision constraints.</td>
<td width="200">Sparse 6-DoF end-effector waypoints + binary gripper state; replay through IK/control APIs. Camera and state recording is 10 Hz; execution rate is not disclosed.</td>
<td width="200">One kinesthetic seed/task + VLM grounding + constrained trajectory composition; no learned task policy.</td>
<td width="360">No simulator or training dataset. Main platform: 10 tasks, one seed each, 25 trials/setting. Transfer platform: 4 tasks, 20 trials/setting.</td>
<td width="110">Real only</td>
<td width="330">Main six tasks: 85.3/78.0% same/new object without disturbance and 69.3/59.3% with disturbance. Cross-embodiment: 83.8/76.3% and 70.0/58.8%. Maximal synchronization shortens execution ~22%.</td>
<td width="250">Initial-grasp execution accounts for 45% of failures and dual-arm coordination 21%; evidence remains one seed per task.</td>
<td width="180"><a href="https://openreview.net/forum?id=he86smZzRk">paper</a></td>
</tr>
<tr>
<td width="100" nowrap>ICLR 2026</td>
<td width="270"><a href="https://openreview.net/forum?id=aemqAxScl9">SARM: Stage-Aware Reward Modeling for Long Horizon Robot Manipulation</a></td>
<td width="260">Learn a stage-aware reward that filters and reweights demonstrations for long-horizon bimanual tasks.</td>
<td width="300">Dual YAM arms + parallel grippers. Main text says 7 DoF/arm while Appendix A.2 and vendor specification say 6 DoF/arm; gripper model is not disclosed.</td>
<td width="180">Top + two wrist RealSense D405 cameras; joint states/actions; no tactile sensing.</td>
<td width="300">A joint bimanual policy executes folding and dishwasher unloading/handover; stage labels model progress but the paper does not define a fixed leader/follower arm.</td>
<td width="200">Dual-arm joint-angle commands; demonstrations recorded at 30 fps; policy control rate not disclosed.</td>
<td width="200">Stage-aware reward modeling + reward-aware behavior cloning/filtering on GELLO demonstrations.</td>
<td width="360">Main experiments are real-only: 200 h total T-shirt folding data, 20 h subset; reward model uses 200 dense + 500 sparse trajectories. MuJoCo/300 demos appear only in a separate appendix DiffQL pick-place study.</td>
<td width="110">Main Real only</td>
<td width="330">Reward-demo MSE 0.009 and rollout Spearman ρ=0.94. RA-BC folding: simple 12/12, medium 10/12 (83%), hard 8/12 (67%); ReWiND gives 50%/25% on medium/hard.</td>
<td width="250">The paper conflicts on arm DoF; the main long-horizon system has no simulation transfer or dexterous hand.</td>
<td width="180"><a href="https://openreview.net/forum?id=aemqAxScl9">paper</a> / <a href="https://qianzhong-chen.github.io/sarm.github.io/">project</a> / <a href="https://github.com/xdofai/opensarm">code</a></td>
</tr>
<tr>
<td width="100" nowrap>AAAI 2026</td>
<td width="270"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38926">LatentVLA: Taming Latent Space for Generalizable and Long-Horizon Bimanual Manipulation</a></td>
<td width="260">Structure a continuous VLA latent action space for long-horizon bimanual planning and generalization.</td>
<td width="300">Paper does not disclose the robot, arm, or end-effector brands/models; it specifies a 14-D bimanual proprioception/action interface.</td>
<td width="180">Language + vision + 14-D proprioception; camera and contact-sensor models not disclosed.</td>
<td width="300">TA-LAM learns a joint language/action latent and LADT plans a long action sequence; no explicit fixed left/right task split.</td>
<td width="200">Expert head decodes joint latent plans into 14-D bimanual action sequences.</td>
<td width="200">Multi-source latent pretraining followed by eight-task bimanual fine-tuning.</td>
<td width="360">52 sources, &gt;2.5M sequences; AgiBot World Beta + LatentVLA-Dexterous contribute ~0.5M. Eight real tasks add 1,600 h. Sim evaluation: RoboTwin 1.0, SIMPLER, CALVIN; engines/versions not disclosed.</td>
<td width="110">Mixed pretraining; Sim + Real evaluation; not one Sim2Real pipeline</td>
<td width="330">Real eight-task mean 63.8%, OOD 56%, 20-demo few-shot 61%; SIMPLER 65.7%; CALVIN average length 3.52; RoboTwin per-task range 33.7–98.3%.</td>
<td width="250">Physical hardware and benchmark engine versions are undisclosed; cross-benchmark numbers are not directly comparable.</td>
<td width="180"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38926">article</a> / <a href="https://ojs.aaai.org/index.php/AAAI/article/download/38926/42888">PDF</a></td>
</tr>
<tr>
<td width="100" nowrap>ICML 2026</td>
<td width="270"><a href="https://icml.cc/virtual/2026/poster/63277">DexMachina: Functional Retargeting for Bimanual Dexterous Manipulation</a></td>
<td width="260">Retarget functional human bimanual manipulation across dexterous hand morphologies while preserving task effects.</td>
<td width="300">Two floating dexterous hands, each augmented with a 6-DoF wrist; core experiments use Inspire, Allegro, ROBOTERA XHand, and SCHUNK 5-finger hands. No robot arms or physical hardware.</td>
<td width="180">Privileged object state, joint targets, finger-object distances, and contact force.</td>
<td width="300">One state-based PPO policy controls both hands; motion/contact rewards induce task-dependent role allocation rather than an explicit left/right split.</td>
<td width="200">Retargeted wrist-base motion + policy residuals for wrist and finger actions.</td>
<td width="200">PPO with task/motion/contact rewards and a decaying virtual object-controller curriculum.</td>
<td width="360">Genesis; ARCTIC provides 5 articulated objects and 7 human bimanual clips (one clip/task). Usually 12K parallel environments, 5 seeds, and 20 evaluation episodes/checkpoint.</td>
<td width="110">Sim only</td>
<td width="330">Reported “success” is articulated-part ADD-AUC: Allegro long-horizon tasks 83.0/81.1/87.1/75.4%; XHand 72.4/66.2/89.0/80.3%.</td>
<td width="250">No real/Sim2Real validation; URDF inertia/collision quality can dominate transfer, and ADD-AUC is not binary task success.</td>
<td width="180"><a href="https://icml.cc/virtual/2026/poster/63277">ICML</a> / <a href="https://arxiv.org/abs/2505.24853">paper</a> / <a href="https://project-dexmachina.github.io/">project</a></td>
</tr>
<tr>
<td width="100" nowrap>ICML 2026</td>
<td width="270"><a href="https://icml.cc/virtual/2026/poster/66358">DECO: Decoupled Multimodal Diffusion Transformer for Bimanual Dexterous Manipulation with a Plugin Tactile Adapter</a></td>
<td width="260">Add tactile feedback to a bimanual humanoid diffusion policy without retraining the vision-action backbone.</td>
<td width="300">Unitree H1-2 upper body: 14 arm DoF + dual Inspire RH56DFTP hands (6 DoF each); self-developed active stereo head adds yaw/pitch.</td>
<td width="180">Stereo vision; 17 tactile pads/hand, 1,062 contact points total, value range 0–4096.</td>
<td width="300">One joint 28-joint action-chunk policy; role division is task-dependent (hold/place, hold/open, or simultaneous plug/socket alignment), not two independent policies.</td>
<td width="200">28 arm/hand/head joint actions; data at 30 Hz; chunk length 32 and execution chunk 16.</td>
<td width="200">Decoupled multimodal diffusion Transformer + tactile cross-attention LoRA adapter.</td>
<td width="360">No simulator. DECO-50 real teleoperation: 4 scenarios, 28 subtasks, 8,021 successful trajectories, ~48.704 successful hours, ~5M frames; &gt;2,000 real rollouts.</td>
<td width="110">Real only</td>
<td width="330">Vision-only mean 72.25%; tactile DECO.p 82.50% (+10.25 pp). Contact-heavy Waste Disposal + Assembly improve from 53.13% to 73.13% (+20 pp); Assembly total is 55/80.</td>
<td width="250">Torso and lower body are not policy-controlled; evaluation spans four scenarios. Main Table 4 prints 55/100, but Table 1 and Appendix Table 14 support 55/80.</td>
<td width="180"><a href="https://icml.cc/virtual/2026/poster/66358">ICML</a> / <a href="https://arxiv.org/abs/2602.05513">paper</a> / <a href="https://huggingface.co/datasets/BAAI-Humanoid/DECO-50">data</a></td>
</tr>
<tr>
<td width="100" nowrap>ICML 2026</td>
<td width="270"><a href="https://icml.cc/virtual/2026/poster/62192">RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation</a></td>
<td width="260">Scale bimanual expert data across tasks and embodiments and test policy robustness under strong domain randomization.</td>
<td width="300">Sim pairs: Aloha-AgileX, ARX-X5, Piper, Franka-Panda, and UR5-WSG; only Panda/WSG grippers are explicitly mapped. Real: COBOT-Magic dual-arm platform; gripper model undisclosed.</td>
<td width="180">Visual/state benchmark observations; no standardized tactile sensor reported.</td>
<td width="300">Object-centric skill API tags left/right arms and supports sequential handover, synchronous/parallel execution, and heterogeneous pairings; no fixed leader arm.</td>
<td width="200">Expert skill programs generate data; ACT/DP/DP3/RDT/π0-style learned policies are benchmarked.</td>
<td width="200">Domain-randomized expert generation, robustness pretraining, and policy benchmarking.</td>
<td width="360">SAPIEN 3.0.0b1; 50 tasks, 5 embodiments, 731 objects/147 classes, &gt;100K trajectories. Standard benchmark: 50 demos/task; robustness: 32×300; real: 10 demos/task + 1K randomized sim/task.</td>
<td width="110">Sim + Real + Benchmark</td>
<td width="330">Automatic collection 60.5% mean (52.2% baseline). Benchmark Easy/Hard: π0 46.4/16.3%, DP3 55.2/5.0%. Synthetic augmentation improves four real settings by 13.5–33.0 pp (24.4 pp mean).</td>
<td width="250">Several gripper mappings and the real gripper are undisclosed; no separate collision, intervention, or coordination-rate metric.</td>
<td width="180"><a href="https://arxiv.org/abs/2506.18088">paper</a> / <a href="https://robotwin-platform.github.io/">project</a> / <a href="https://github.com/RoboTwin-Platform/RoboTwin">code</a> / <a href="https://huggingface.co/datasets/TianxingChen/RoboTwin2.0">data</a></td>
</tr>
<tr>
<td width="100" nowrap>ICCV 2025</td>
<td width="270"><a href="https://openaccess.thecvf.com/content/ICCV2025/html/Jiang_Rethinking_Bimanual_Robotic_Manipulation_Learning_with_Decoupled_Interaction_Framework_ICCV_2025_paper.html">Rethinking Bimanual Robotic Manipulation: Learning with Decoupled Interaction Framework</a></td>
<td width="260">Avoid forcing full inter-arm coupling on tasks or phases that can be learned independently.</td>
<td width="300">Sim: RoboTwin dual-arm embodiment; the paper does not name its robot/grippers. Real: AgileX Cobot Magic dual arms; gripper model undisclosed.</td>
<td width="180">Single third-person RealSense L515 point cloud + per-arm robot state; no tactile sensing.</td>
<td width="300">Independent per-arm policies exchange the opposite arm’s state feature; a selective interaction module predicts scale/bias to vary coupling by task phase.</td>
<td width="200">Each arm consumes its point cloud + 7-D state and predicts a 7-D action.</td>
<td width="200">Decoupled imitation learning with selective inter-arm feature modulation.</td>
<td width="360">SAPIEN + RoboTwin: 7 tasks, usually 50 demos/task; two tasks also use 100/150/200. Real: four tasks and 50 high-quality teleoperation demos; paper does not say total vs per-task.</td>
<td width="110">Sim + Real</td>
<td width="330">Sim mean 0.789 vs DP3 0.554; coordinated/non-coordinated 0.700/0.824 vs 0.465/0.590. Real 45/60 = 75% vs DP3 27/60 = 45%.</td>
<td width="250">Sim robot/grippers and real gripper are not specified; no quantitative collision, intervention, or execution-time metric.</td>
<td width="180"><a href="https://openaccess.thecvf.com/content/ICCV2025/html/Jiang_Rethinking_Bimanual_Robotic_Manipulation_Learning_with_Decoupled_Interaction_Framework_ICCV_2025_paper.html">CVF</a> / <a href="https://arxiv.org/abs/2503.09186">arXiv</a></td>
</tr>
<tr>
<td width="100" nowrap>ICCV 2025</td>
<td width="270"><a href="https://openaccess.thecvf.com/content/ICCV2025/html/Lu_AnyBimanual_Transferring_Unimanual_Policy_for_General_Bimanual_Manipulation_ICCV_2025_paper.html">AnyBimanual: Transferring Unimanual Policy for General Bimanual Manipulation</a></td>
<td width="260">Compose pretrained single-arm skills into general language-conditioned bimanual manipulation with few bimanual demonstrations.</td>
<td width="300">Sim: dual 7-DoF Franka Panda + Panda two-finger grippers. Real: dual UR5e + Robotiq 2F-85 grippers.</td>
<td width="180">RealSense L515 RGB-D → shared 3D voxel scene; robot state; no tactile sensing.</td>
<td width="300">Two single-arm policy copies are dynamically scheduled by a Skill Manager; Visual Aligner assigns each arm a soft voxel region. No fixed leader/follower.</td>
<td width="200">Language-selected single-arm skill primitives composed into synchronous/asynchronous dual-arm actions.</td>
<td width="200">Pretrain on 18 single-arm tasks; fine-tune on bimanual demonstrations.</td>
<td width="360">RLBench2 + PyRep + CoppeliaSim 4.1: 12 tasks × 20 or 100 demos (240/1,200), 100 test episodes/task. Real: 9 tasks × 30 demos (270); few-shot 9×5.</td>
<td width="110">Sim + Real</td>
<td width="330">Sim 100-demo mean 32.00% vs PerAct2 14.67% (+17.33 pp). Real: 55/65 = 84.62%; five-demo/task real setting 53.33%.</td>
<td width="250">Simulation success remains 32%; no collision/intervention metric. The ~1.5 min figure is demonstration collection + keyframe extraction, not execution time.</td>
<td width="180"><a href="https://openaccess.thecvf.com/content/ICCV2025/html/Lu_AnyBimanual_Transferring_Unimanual_Policy_for_General_Bimanual_Manipulation_ICCV_2025_paper.html">CVF</a> / <a href="https://anybimanual.github.io/">project</a> / <a href="https://github.com/TengBoYu01/AnyBimanual">code</a></td>
</tr>
<tr>
<td width="100" nowrap>CVPR 2025</td>
<td width="270"><a href="https://openaccess.thecvf.com/content/CVPR2025/html/Lv_Spatial-Temporal_Graph_Diffusion_Policy_with_Kinematic_Modeling_for_Bimanual_Robotic_CVPR_2025_paper.html">Spatial-Temporal Graph Diffusion Policy with Kinematic Modeling for Bimanual Robotic Manipulation (KStar Diffuser)</a></td>
<td width="260">Make bimanual diffusion actions respect robot structure and joint kinematics to reduce interference and infeasible poses.</td>
<td width="300">Sim: dual Franka Panda + parallel grippers. Real: Cobot AgileX ALOHA with dual 6-DoF arms; gripper model not disclosed.</td>
<td width="180">Language + multiview RGB-D; no tactile sensing reported.</td>
<td width="300">A dynamic spatial-temporal graph connects both arms’ joints across time; the policy jointly generates two end-effector trajectories rather than assigning a fixed leader.</td>
<td width="200">Two 6-D end-effector pose trajectories + gripper open/close; differentiable FK regularizes predicted poses.</td>
<td width="200">Graph-conditioned diffusion imitation learning with a kinematic regularizer.</td>
<td width="360">RLBench2 (underlying engine not restated): 5 tasks, 20/100 demos/task, 100 trials × 3 seeds. Real ALOHA: 2 tasks, 100 demos/task, 15 evaluations/task.</td>
<td width="110">Sim + Real</td>
<td width="330">100-demo sim mean 68.2±2.1%; tasks 83.0/98.7/27.0/43.7/89.0%. Real Lift Plate 66.7±5.3%, Handover 19.7±5.3%, mean 43.1±17.8%.</td>
<td width="250">Handover remains weak; the paper’s main text and appendix describe the handover_item_easy arm order differently, so the table does not resolve it.</td>
<td width="180"><a href="https://openaccess.thecvf.com/content/CVPR2025/html/Lv_Spatial-Temporal_Graph_Diffusion_Policy_with_Kinematic_Modeling_for_Bimanual_Robotic_CVPR_2025_paper.html">CVF</a> / <a href="https://arxiv.org/abs/2503.10743">arXiv</a></td>
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

_Current table mentions are counted once per paper row across the 28 dexterous-hand and 28 tactile/contact-rich papers below; they are README coverage signals, not bibliometric counts._

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
<td width="120">17</td>
<td width="300">Most common carrier arm for dexterous hands, tactile grippers, and baseline grasping</td>
<td width="220"><a href="https://frankarobotics.github.io/docs/">FCI docs</a> / <a href="https://github.com/frankarobotics/franka_ros2">franka_ros2</a> / <a href="https://github.com/frankarobotics/franka_description">models</a></td>
<td width="300">Strong real-robot SDK/ROS2 and public URDF descriptions; hand mounts, tactile mounts, and sim controllers are usually paper-specific</td>
<td width="300">Best-supported arm baseline in the current survey, but not a complete hand+tactile stack by itself</td>
</tr>
<tr>
<td width="220">Intel RealSense RGB-D</td>
<td width="120">19</td>
<td width="300">External RGB-D perception for pose, point clouds, and policy input</td>
<td width="220"><a href="https://github.com/realsenseai/librealsense">librealsense</a></td>
<td width="300">Good SDK support for real rigs; it provides vision/depth, not contact or force sensing</td>
<td width="300">Low-risk default camera, but it does not solve contact observability</td>
</tr>
<tr>
<td width="220">Allegro Hand</td>
<td width="120">15</td>
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
<td width="120">14</td>
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
<td width="120">9</td>
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
<td width="120">6</td>
<td width="300">Carrier arm for dexterous hands and teleoperation setups</td>
<td width="220"><a href="https://github.com/xArm-Developer/xarm_ros2">xarm_ros2</a> / <a href="https://github.com/xArm-developer/xarm_ros">xarm_ros</a></td>
<td width="300">Public ROS/ROS2 packages include simulation models and control demos; dexterous-hand mounting remains custom</td>
<td width="300">Cost-effective arm candidate when paired with a separately validated hand</td>
</tr>
<tr>
<td width="220">Apple Vision Pro / Meta Quest / GELLO</td>
<td width="120">Vision Pro 5; Meta Quest or VR 6; GELLO 1</td>
<td width="300">Human demonstration, hand tracking, VR teleoperation, and retargeting data chain</td>
<td width="220"><a href="https://developer.apple.com/documentation/visionos/tracking-and-visualizing-hand-movement">Apple hand tracking</a> / <a href="https://wuphilipp.github.io/gello_site/">GELLO</a> / <a href="https://github.com/wuphilipp/gello_software">GELLO code</a></td>
<td width="300">Useful for scalable motion data; contact, force, and hand-to-robot retargeting are still algorithmic bottlenecks</td>
<td width="300">Data collection stack, not a substitute for tactile or force feedback</td>
</tr>
<tr>
<td width="220">Robotiq 2F / parallel grippers</td>
<td width="120">4</td>
<td width="300">Baseline grasping hardware in non-dexterous rows</td>
<td width="220"><a href="https://robotiq.com/products/2f85-140-adaptive-robot-gripper">official</a></td>
<td width="300">Easy to simulate and deploy compared with dexterous hands; not a multi-finger manipulation platform</td>
<td width="300">Useful baseline, but should not be counted as dexterous-hand capability</td>
</tr>
<tr>
<td width="220">Sharpa Wave / Dexmate Vega-1</td>
<td width="120">3</td>
<td width="300">High-DoF tactile dexterous hand and bimanual tactile-reactive robot setup</td>
<td width="220"><a href="https://arxiv.org/abs/2602.16710">EgoScale</a> / <a href="https://arxiv.org/abs/2606.17055">T-Rex</a></td>
<td width="300">Public evidence comes from paper/project descriptions; reusable public SDK/ROS2 and sim assets were not found</td>
<td width="300">Promising tactile-dexterity evidence, but integration risk stays high until vendor assets and APIs are confirmed</td>
</tr>
<tr>
<td width="220">Custom visuo-tactile grippers / tactile skins</td>
<td width="120">12</td>
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
<td width="120">4</td>
<td width="300">Successor stack for robot learning, sensor simulation, and tactile-aware experiments</td>
<td width="220"><a href="https://developer.nvidia.com/isaac/lab">Isaac Lab</a> / <a href="https://github.com/isaac-sim/IsaacLab">code</a> / <a href="https://github.com/isaac-sim/IsaacSim">Isaac Sim</a></td>
<td width="300">Good fit for Franka-style arms and newer tactile simulation papers; asset import from URDF/MJCF/CAD is supported by Isaac Sim</td>
<td width="300">Dense tactile and dexterous-hand controllers still tend to be custom integrations</td>
</tr>
<tr>
<td width="200">MuJoCo / MJCF</td>
<td width="120">4</td>
<td width="300">Contact-rich dynamics, Adroit-style hand tasks, and compact reproducible benchmarks</td>
<td width="220"><a href="https://mujoco.org/">official</a> / <a href="https://github.com/google-deepmind/mujoco">code</a> / <a href="https://github.com/google-deepmind/mujoco_menagerie">Menagerie</a></td>
<td width="300">Strong for Shadow/Adroit and MJCF models; useful for reproducible task benchmarks</td>
<td width="300">High-fidelity optical tactile rendering and real-hand drivers are not standard out of the box</td>
</tr>
<tr>
<td width="200">SAPIEN / ManiSkill</td>
<td width="120">SAPIEN 5; ManiSkill 2</td>
<td width="300">Articulated objects, manipulation environments, and task/data generation</td>
<td width="220"><a href="https://sapien.ucsd.edu/">SAPIEN</a> / <a href="https://github.com/haosulab/SAPIEN">SAPIEN code</a> / <a href="https://github.com/mani-skill/ManiSkill">ManiSkill</a></td>
<td width="300">Good articulated-object and robot asset ecosystem; hand models depend on URDF/assets supplied by each work</td>
<td width="300">Less standardized for real dexterous-hand sim-to-real than arm/gripper manipulation</td>
</tr>
<tr>
<td width="200">Adroit / Gymnasium Robotics</td>
<td width="120">Adroit 2; Gymnasium 1</td>
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
<td width="120">2</td>
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
