# tactile/contact-rich

[Home](../../../README.md) | [中文](../../zh-CN/embodiment/tactile-contact.md) | [Direction index](README.md)

Total: 28 papers.

The direction-specific columns separate sensor specification, fusion location, feedback stage/rate, and tactile-specific gain. “Not disclosed” means the checked paper or official project source did not provide that detail.

<table width="3520">
<thead>
<tr>
<th width="100" nowrap>Venue/Year</th>
<th width="260">Paper/Method</th>
<th width="230">Research Problem</th>
<th width="300">Exact Robot / End Effector / Sensor</th>
<th width="280">Tactile Signal Specification</th>
<th width="220">Contact / Perception Task</th>
<th width="300">Fusion Architecture / Location</th>
<th width="220">Closed-loop Stage / Control Rate</th>
<th width="200">Action / Control Interface</th>
<th width="330">Simulation / Training Environment + Data Scale</th>
<th width="110">Sim / Real Role</th>
<th width="320">Core Tactile-Gain / Task Metric</th>
<th width="230">Solved / Progress</th>
<th width="240">Limitation</th>
<th width="180">Resources</th>
</tr>
</thead>
<tbody>
<tr>
<td width="100" nowrap>CoRL 2024</td>
<td width="260"><a href="https://arxiv.org/abs/2410.24091">3D-ViTac: Learning Fine-Grained Manipulation with Visuo-Tactile Sensing</a></td>
<td width="230">Learn fine manipulation from spatially aligned vision and touch.</td>
<td width="300">Dual master-puppet arms; soft fin two-finger grippers; four custom Velostat pads; multi-view RealSense RGB-D.</td>
<td width="280">Four 16x16 pads (1,024 points total), 3 mm² per point; tactile ROS publishes at 30 Hz (sensor maximum 32.2 FPS), synchronized demonstrations at 10 Hz.</td>
<td width="220">Four fine-manipulation tasks including egg steaming, insertion, and grape retrieval.</td>
<td width="300">3D tactile points and RGB-D point clouds are encoded by PointNet++ and fused before the diffusion policy.</td>
<td width="220">Closed-loop rollout; policy rate is not separately disclosed. Tactile ROS publishes at 30 Hz (sensor maximum 32.2 FPS); synchronized demonstrations are 10 Hz.</td>
<td width="200">Joint/action chunks for both puppet arms and grippers.</td>
<td width="330">Real-only; 30/30/30/50 demonstrations across four tasks; 20 evaluation trials per task.</td>
<td width="110">Real only</td>
<td width="320">Four-task SR 85/80/90/85% versus RGB-only 50/45/45/60%.</td>
<td width="230">Turns distributed touch into a common 3D point representation for precise policy learning.</td>
<td width="240">Custom bimanual hardware and a four-task evaluation limit portability and breadth.</td>
<td width="180"><a href="https://arxiv.org/abs/2410.24091">paper</a> / <a href="https://binghao-huang.github.io/3D-ViTac/">project</a> / <a href="https://github.com/binghao-huang/3D-ViTac_Tactile_Hardware">hardware</a></td>
</tr>
<tr>
<td width="100" nowrap>CoRL 2022</td>
<td width="260"><a href="https://arxiv.org/abs/2210.14210">MidasTouch: Monte-Carlo Inference over Distributions across Sliding Touch</a></td>
<td width="230">Globally localize a tactile sensor on an object during sliding contact.</td>
<td width="300">Hand-held DIGIT with OptiTrack tracking; no robot executes manipulation.</td>
<td width="280">DIGIT 240x320 RGB tactile images; real stream 30 Hz; online inference about 10 Hz.</td>
<td width="220">Sliding-touch localization on YCB objects.</td>
<td width="300">Tactile image to local height map and learned geometry code; a particle filter integrates pose hypotheses over time.</td>
<td width="220">Online state-estimation loop at about 10 Hz; no robot manipulation-control loop.</td>
<td width="200">Human-guided sliding; the method outputs the sensor pose distribution.</td>
<td width="330">TACTO: 40 YCB objects x 5,000 contacts = 200k; YCB-Slide: 50 simulated and 50 real sequences.</td>
<td width="110">Simulation training + real evaluation</td>
<td width="320">Final simulated/real errors: 0.74 cm / 9.43° and 1.97 cm / 21.48°.</td>
<td width="230">Provides online global localization from tactile-only sliding observations.</td>
<td width="240">Requires known object geometry and human-guided contact; it is not a closed-loop manipulation policy.</td>
<td width="180"><a href="https://arxiv.org/abs/2210.14210">paper</a> / <a href="https://suddhu.github.io/midastouch-tactile/">project</a> / <a href="https://github.com/facebookresearch/MidasTouch">code</a></td>
</tr>
<tr>
<td width="100" nowrap>CoRL 2022</td>
<td width="260"><a href="https://proceedings.mlr.press/v205/zhong23a.html">Touching a NeRF: Leveraging Neural Radiance Fields for Tactile Sensory Data Generation</a></td>
<td width="230">Generate useful tactile observations from visual object models to reduce real touch collection.</td>
<td width="300">Franka Panda with DIGIT and Intel RealSense D415; OmniTact appears only in simulated transfer tests.</td>
<td width="280">DIGIT optical tactile images; 398 real touches yield 19,900 frames; capture rate is not separately disclosed.</td>
<td width="220">Tactile image generation and downstream object classification.</td>
<td width="300">A per-object NeRF renders RGB-D; a conditional GAN maps rendered geometry to tactile images used for classifier augmentation.</td>
<td width="220">No closed-loop control; robot contact is used only for dataset acquisition.</td>
<td width="200">Scripted end-effector contacts; the learned output is a tactile image/class label.</td>
<td width="330">TACTO with PyBullet + PyRender: 27 YCB objects x 500 contacts; real: 9 objects, 398 touches, 19.9k frames.</td>
<td width="110">Simulation augmentation + real evaluation</td>
<td width="320">Classifier accuracy rises 85→96% in simulation and 74→83% on real data.</td>
<td width="230">Uses visual NeRF geometry to synthesize tactile data that improves tactile perception.</td>
<td width="240">Needs a NeRF per object, targets rigid objects, and does not learn contact-rich control.</td>
<td width="180"><a href="https://proceedings.mlr.press/v205/zhong23a.html">paper</a> / <a href="https://proceedings.mlr.press/v205/zhong23a/zhong23a.pdf">pdf</a></td>
</tr>
<tr>
<td width="100" nowrap>CoRL 2020 (PMLR 2021)</td>
<td width="260"><a href="https://arxiv.org/abs/2012.05205">Tactile object pose estimation from the first touch with geometric contact rendering</a></td>
<td width="230">Estimate object pose from one tactile imprint with little real training data.</td>
<td width="300">Fixed GelSlim sensor and four-axis positioning stage; no autonomous robot policy.</td>
<td width="280">GelSlim 470x470 at 90 Hz; network input 200x200; rendered/contact depth range 0–2 mm.</td>
<td width="220">First-touch object-pose estimation.</td>
<td width="300">A geometric contact renderer produces training imprints for a tactile-only pose estimator.</td>
<td width="220">No; one contact is observed and then pose is estimated.</td>
<td width="200">Programmed stage contact followed by feed-forward pose prediction.</td>
<td width="330">Custom geometric renderer; at least 150 real touches and 5k–20k simulated samples per object.</td>
<td width="110">Simulation training + real evaluation</td>
<td width="320">Pin-object median translation error is 4.8 mm; additional per-object pose errors are reported in the paper.</td>
<td width="230">Shows geometry-based synthetic contacts can support accurate first-touch localization.</td>
<td width="240">Object-specific training and a fixed contact setup do not cover sequential manipulation.</td>
<td width="180"><a href="https://arxiv.org/abs/2012.05205">paper</a> / <a href="https://proceedings.mlr.press/v155/villalonga21a.html">PMLR</a> / <a href="http://mcube.mit.edu/research/tactile_loc_first_touch.html">project</a></td>
</tr>
<tr>
<td width="100" nowrap>CoRL 2022</td>
<td width="260"><a href="https://arxiv.org/abs/2210.01116">That Sounds Right: Auditory Self-Supervision for Dynamic Robot Manipulation</a></td>
<td width="230">Use contact sound as self-supervision for selecting dynamic manipulation behavior.</td>
<td width="300">UR10 arm with a contact microphone; no taxel-based tactile sensor.</td>
<td width="280">Four-second audio at 44.1 kHz, downsampled to 11 kHz; contact events are acoustic rather than spatial taxels.</td>
<td width="220">Dynamic contact behaviors selected from sound goals.</td>
<td width="300">A BYOL-style audio encoder maps a target sound to a parameterized motion primitive.</td>
<td width="220">One audio-to-primitive mapping is made before execution; the resulting motion is open-loop.</td>
<td width="200">Select and execute a parameterized dynamic motion primitive.</td>
<td width="330">No simulation; about 25k real robot behaviors with synchronized contact audio.</td>
<td width="110">Real only</td>
<td width="320">Evaluated with audio/trajectory MSE and DTW; no manipulation success rate is reported.</td>
<td width="230">Learns dynamic behavior selection without manual semantic labels by exploiting contact audio.</td>
<td width="240">Audio is indirect contact sensing, and execution does not close the loop on sound.</td>
<td width="180"><a href="https://arxiv.org/abs/2210.01116">paper</a> / <a href="https://audio-robot-learning.github.io">project</a></td>
</tr>
<tr>
<td width="100" nowrap>ICLR 2026</td>
<td width="260"><a href="https://openreview.net/forum?id=dT3ZciXvNX">DexMove: Learning Tactile-Guided Non-Prehensile Manipulation with Dexterous Hands</a></td>
<td width="230">Learn non-prehensile object motion from scarce tactile demonstrations.</td>
<td width="300">Franka Research 3, Allegro Hand, RealSense D435i, and R-Tac-derived wearable/fingertip tactile hardware.</td>
<td width="280">Each finger tracks 33 markers in four displacement directions at 30 FPS.</td>
<td width="220">Move six tabletop objects without grasping; sorting and tidying demonstrations.</td>
<td width="300">TaFo-Net encodes tactile force cues and fuses them with visual/proprioceptive state in a flow policy.</td>
<td width="220">Closed-loop robot policy at 30 Hz.</td>
<td width="200">Flow-policy arm/hand action trajectories for the FR3 + Allegro system.</td>
<td width="330">MuJoCo: 352 layouts and 412k contact configurations; about 300k human tactile frames for force-aware learning.</td>
<td width="110">Simulation augmentation + real execution</td>
<td width="320">Real success is 77.8% across six objects, 36.6 percentage points above the reported ablation.</td>
<td width="230">Combines pruned synthetic trajectories with real tactile demonstrations for non-prehensile dexterity.</td>
<td width="240">Evidence covers six objects and sensor-specific calibration; broader objects and hands remain untested.</td>
<td width="180"><a href="https://openreview.net/forum?id=dT3ZciXvNX">paper</a> / <a href="https://peilin-666.github.io/projects/DexMove/">project</a> / <a href="https://github.com/bigai-ai/PP-Tac/tree/main">sensor code</a></td>
</tr>
<tr>
<td width="100" nowrap>ICLR 2026</td>
<td width="260"><a href="https://openreview.net/forum?id=ndilONnABZ">AnyTouch 2: General Optical Tactile Representation Learning For Dynamic Tactile Perception</a></td>
<td width="230">Learn dynamic tactile representations that transfer across optical sensors and robot tasks.</td>
<td width="300">Multi-sensor pretraining; downstream Piper + GelSight Mini/DIGIT and xArm6 + GelSight Mini setups.</td>
<td width="280">Dynamic optical streams are mostly 30 Hz; GelSight Mini is 18 Hz in the reported setup.</td>
<td width="220">Grasping, whiteboard wiping, USB insertion, and chip moving.</td>
<td width="300">An attentive pooler forms tactile features; features are concatenated with vision before a diffusion policy.</td>
<td width="220">Closed-loop downstream policy at 3 Hz.</td>
<td width="200">Diffusion-policy action chunks for the downstream arm/gripper.</td>
<td width="330">IMPM + Blender synthetic 1,118,896; real tactile 584,842; force-labeled 722,436; total 2,426,174 samples.</td>
<td width="110">Mixed simulation/real pretraining + real control</td>
<td width="320">Reported task SRs span 0.25–0.85: 0.75/0.80, 0.85/0.80, 0.30/0.25, and 0.85 across sensor/settings.</td>
<td width="230">Improves dynamic, force-aware transfer across several optical tactile sensors.</td>
<td width="240">Cross-sensor performance is uneven and the downstream controller runs at only 3 Hz.</td>
<td width="180"><a href="https://openreview.net/forum?id=ndilONnABZ">paper</a> / <a href="https://gewu-lab.github.io/AnyTouch2/">project</a> / <a href="https://github.com/GeWu-Lab/AnyTouch2">code</a> / <a href="https://huggingface.co/collections/BAAI/touchd">data</a></td>
</tr>
<tr>
<td width="100" nowrap>ICLR 2026</td>
<td width="260"><a href="https://openreview.net/forum?id=hU2gT2Ucua">APPLE: Toward General Active Perception via Reinforcement Learning</a></td>
<td width="230">Learn a general policy that actively acquires informative tactile observations.</td>
<td width="300">No physical robot; simulated GelSight Mini and Myrmex-style sensing.</td>
<td width="280">Taxim GelSight Mini observations are 32x32; MHSB Myrmex observations are 16x16, not binary contacts.</td>
<td width="220">Active tactile exploration for classification/regression, including Tactile-MNIST.</td>
<td width="300">A ViT plus probe position feeds a temporal transformer policy/value model.</td>
<td width="220">Closed-loop active perception, not manipulation control; interaction rate is not disclosed.</td>
<td width="200">The RL agent selects the next probing/contact action.</td>
<td width="330">Simulation only; Taxim and MHSB tasks trained for 5M/10M environment steps.</td>
<td width="110">Simulation only</td>
<td width="320">Tactile-MNIST final accuracy is about 87/89% in two settings versus 74% for random exploration.</td>
<td width="230">Generalizes active information-gathering policies across tactile perception tasks.</td>
<td width="240">No physical robot, contact-rich manipulation, or hardware sim-to-real evaluation.</td>
<td width="180"><a href="https://openreview.net/forum?id=hU2gT2Ucua">paper</a> / <a href="https://timschneider42.github.io/apple">project</a></td>
</tr>
<tr>
<td width="100" nowrap>AAAI 2026</td>
<td width="260"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38882">STOLA: Self-Adaptive Touch-Language Framework for Tactile Commonsense Reasoning in Open-Ended Scenarios</a></td>
<td width="230">Answer open-ended tactile commonsense questions across sensors and interaction sequences.</td>
<td width="300">No robot; offline GelSight and GelSight Mini images/time series from public and constructed datasets.</td>
<td width="280">Single tactile images and temporal tactile sequences; spatial density and acquisition rate vary by source and are not unified.</td>
<td width="220">Open-ended tactile QA over eight properties and four interaction characteristics.</td>
<td width="300">A tactile encoder and adapter condition Vicuna; a mixture-of-experts layer adapts touch-language reasoning.</td>
<td width="220">No closed-loop robot control; offline inference only.</td>
<td width="200">Free-form language generation from tactile observations and prompts.</td>
<td width="330">Touch100k + PHYSICLEAR + 5k self-built instructions; TactileBench contains 600 QA items; no physics simulation.</td>
<td width="110">Real offline datasets</td>
<td width="320">PHYSICLEAR CIDEr reaches 195.03; additional QA/reasoning metrics are reported on TactileBench.</td>
<td width="230">Extends tactile-language evaluation from fixed labels to open-ended commonsense reasoning.</td>
<td width="240">Benchmark reasoning is not validated in real-time robot manipulation.</td>
<td width="180"><a href="https://arxiv.org/abs/2505.04201">paper</a> / <a href="https://cocacola-lab.github.io/SToLa-Page/">project</a></td>
</tr>
<tr>
<td width="100" nowrap>AAAI 2026</td>
<td width="260"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38915">TouchFormer: A Robust Transformer-based Framework for Multimodal Material Perception</a></td>
<td width="230">Recognize materials robustly when touch, inertial, or audio modalities are noisy or missing.</td>
<td width="300">RealMan RM65-B arm, TESOLLO Gripper-3F, uSkin fingertip, 12-DoF IMU, and contact audio.</td>
<td width="280">uSkin normal/friction force, 12-DoF inertial features, and audio sequences; rates are not disclosed.</td>
<td width="220">Material classification and a perception-guided sorting demonstration.</td>
<td width="300">Adaptive gating plus self- and cross-attention fuses touch, IMU, and audio features.</td>
<td width="220">No manipulation feedback loop; the classifier selects material/sorting behavior.</td>
<td width="200">Material label followed by a preprogrammed sorting action.</td>
<td width="330">LMTHM reports 965 samples over 193 materials; FISHM is used for real multimodal fine-tuning/evaluation.</td>
<td width="110">Real offline perception + real demo</td>
<td width="320">Reported classification accuracy is 91.47% / 89.54% in the two principal benchmark settings.</td>
<td width="230">Maintains material perception under noisy or missing modalities and demonstrates robot sorting.</td>
<td width="240">The robot demo uses perception for selection, not closed-loop contact or force control.</td>
<td width="180"><a href="https://arxiv.org/abs/2511.19509">paper</a></td>
</tr>
<tr>
<td width="100" nowrap>AAAI 2026</td>
<td width="260"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38956">Collaborative Representation Learning for Alignment of Tactile, Language, and Vision Modalities</a></td>
<td width="230">Align touch, language, and vision while suppressing sensor-specific bias.</td>
<td width="300">No robot; GelSight, DIGIT, DuraGel, and GelSight Mini data from eight offline datasets.</td>
<td width="280">Real tactile-image datasets of about 9.3k/8.3k/7.2k/250k/4.5k/39k/39k/55k samples.</td>
<td width="220">Cross-sensor material recognition and tactile-language-vision retrieval/alignment.</td>
<td width="300">OpenCLIP-L with a unified bias adapter and contrastive objectives aligns the three modalities.</td>
<td width="220">No; offline representation learning and evaluation.</td>
<td width="200">Embedding, retrieval, and classification outputs only.</td>
<td width="330">Eight real tactile datasets, including TAG and TacQuad; no physics simulation.</td>
<td width="110">Real offline datasets</td>
<td width="320">Cross-sensor material recognition reaches 55.59% in the reported setting.</td>
<td width="230">Improves sensor-agnostic tactile-language-vision alignment across heterogeneous datasets.</td>
<td width="240">No real-time robot, manipulation, or closed-loop sensor feedback evaluation.</td>
<td width="180"><a href="https://arxiv.org/abs/2511.11512">paper</a> / <a href="https://ojs.aaai.org/index.php/AAAI/article/view/38956">AAAI</a></td>
</tr>
<tr>
<td width="100" nowrap>ICML 2026</td>
<td width="260"><a href="https://icml.cc/virtual/2026/poster/66793">Cross-Tactile Sensor Representation Learning</a></td>
<td width="230">Transfer tactile representations between optical sensors with different image domains.</td>
<td width="300">No robot; aligned synthetic sensor domains and real tactile datasets.</td>
<td width="280">SITR contains 50k aligned simulated samples (5 sensors x 10k); TAG contributes about 250k real samples, with other real sources.</td>
<td width="220">Cross-sensor tactile recognition and representation transfer.</td>
<td width="300">A Cross-Sensor Modulator is learned on aligned synthetic data, then adapted with real multimodal tactile data.</td>
<td width="220">No; offline pretraining and evaluation.</td>
<td width="200">Feature embedding and downstream classifier outputs.</td>
<td width="330">SITR 50k simulated aligned samples plus TAG 250k and other real tactile datasets.</td>
<td width="110">Simulation alignment + real evaluation</td>
<td width="320">DIGIT↔GelSight Mini transfer improves by roughly 20 percentage points in the reported comparison.</td>
<td width="230">Uses aligned simulation to reduce the domain gap between tactile sensor appearances.</td>
<td width="240">No robot-control or closed-loop manipulation validation.</td>
<td width="180"><a href="https://icml.cc/virtual/2026/poster/66793">paper</a></td>
</tr>
<tr>
<td width="100" nowrap>ICML 2026</td>
<td width="260"><a href="https://icml.cc/virtual/2026/poster/65669">Tabero: Learning Gentle Manipulation with Closed-Loop Force Feedback from Vision, Touch, and Language</a></td>
<td width="230">Execute gentle versus firm instructions while preserving task success and limiting grip force.</td>
<td width="300">Simulated Franka Panda arm/hand with two GelSight fingertips in Isaac Lab/Isaac Sim.</td>
<td width="280">Each simulated GelSight is 320x240 RGB with an 11x9 marker grid; two fingertip 3D force vectors; synchronized at 20 Hz.</td>
<td width="220">Gentle and firm grasp/manipulation under language-conditioned force constraints.</td>
<td width="300">A tactile TCN and cross-attention condition Pi0; a low-level admittance force-position controller executes commands.</td>
<td width="220">Policy observations at 20 Hz; low-level admittance force-position loop, whose inner rate is not disclosed.</td>
<td width="200">Pi0 produces motion/force targets for the admittance controller.</td>
<td width="330">Isaac Lab/Isaac Sim + Taxim; open-source LIBERO trajectories are replayed; exact trajectory count is not disclosed.</td>
<td width="110">Simulation only</td>
<td width="320">In Task A, success is 0.87/0.79 while average grip force drops from 31.3 N to 8.5 N; average reduction exceeds 70%.</td>
<td width="230">Adds language-conditioned force feedback without sacrificing most task success.</td>
<td width="240">Ultra-gentle regimes and physical deployment are not demonstrated.</td>
<td width="180"><a href="https://arxiv.org/abs/2605.27886">paper</a> / <a href="https://github.com/NathanWu7/Tabero">code</a></td>
</tr>
<tr>
<td width="100" nowrap>NeurIPS 2025</td>
<td width="260"><a href="https://arxiv.org/abs/2505.22566">Universal Visuo-Tactile Video Understanding for Embodied Interaction</a></td>
<td width="230">Understand dynamic touch jointly with video and language across tactile sensors.</td>
<td width="300">No robot; human-collected GelSight Mini, DIGIT, and Tac3D videos.</td>
<td width="280">VTV150K has 150k frames over 100 objects and three sensors, with hardness/protrusion/elasticity/friction labels.</td>
<td width="220">Tactile-video property recognition and tactile-language QA.</td>
<td width="300">VideoMAE features with flow masking condition a Qwen language model for video-touch reasoning.</td>
<td width="220">No; offline video understanding.</td>
<td width="200">Property prediction and language answers, not robot actions.</td>
<td width="330">No simulation; 100 objects x 5 videos, totaling 150k real frames.</td>
<td width="110">Real offline dataset</td>
<td width="320">VTV-LLM average score is 60.4 across the reported understanding benchmarks.</td>
<td width="230">Introduces a multi-sensor tactile-video-language dataset and universal video model.</td>
<td width="240">No closed-loop manipulation or robot-hardware evaluation.</td>
<td width="180"><a href="https://arxiv.org/abs/2505.22566">paper</a> / <a href="https://github.com/IvanXie416/VTV-LLM">code</a> / <a href="https://huggingface.co/datasets/Ivan416/VBTS_video">data</a></td>
</tr>
<tr>
<td width="100" nowrap>NeurIPS 2025</td>
<td width="260"><a href="https://arxiv.org/abs/2510.21609">Enhancing Tactile-based Reinforcement Learning for Robotic Control</a></td>
<td width="230">Make sparse contact signals useful for blind reinforcement-learning control.</td>
<td width="300">Isaac Lab only: Franka for Find; fixed Shadow Dexterous Hand for Bounce and Baoding; no Allegro/ORCA hardware evaluation.</td>
<td width="280">Find uses 9-D state + 2 binary contacts; Shadow tasks use 20-D hand state + 17 link contacts; physics 120 Hz, policy 60 Hz.</td>
<td width="220">Find an object, bounce a ball, and rotate Baoding balls without vision.</td>
<td width="300">PPO fuses proprioception and sparse contacts; self-supervised auxiliary objectives regularize the policy encoder.</td>
<td width="220">Closed-loop simulated control at 60 Hz with 120 Hz physics.</td>
<td width="200">Continuous PPO motor actions; low-level actuator mode is task dependent.</td>
<td width="330">Isaac Lab RoTO benchmark; simulation only; task-specific training horizon is not uniformly disclosed.</td>
<td width="110">Simulation only</td>
<td width="320">Find time 1.4 s vs 1.9 s; Bounce 79 vs 69 hits/10 s; Baoding 17 vs 5 rotations in the reported comparisons.</td>
<td width="230">Shows self-supervision can improve blind dexterity from very sparse binary contacts.</td>
<td width="240">No real tactile hardware, durability study, or sim-to-real result.</td>
<td width="180"><a href="https://arxiv.org/abs/2510.21609">paper</a> / <a href="https://elle-miller.github.io/tactile_rl/">project</a> / <a href="https://github.com/elle-miller/roto">code</a></td>
</tr>
<tr>
<td width="100" nowrap>NeurIPS 2025</td>
<td width="260"><a href="https://taccel-simulator.github.io/assets/taccel-paper.pdf">Taccel: Scaling Up Vision-based Tactile Robotics via High-performance GPU Simulation</a></td>
<td width="230">Scale deformable vision-based tactile simulation for robot learning.</td>
<td width="300">Simulated optical tactile robots; sim-to-real classifier uses Robotiq 2F-85 + GelSight.</td>
<td width="280">Task-dependent elastomer images; dual-GelSight peg setup runs 4,096 environments; five-finger model has 17 gel surfaces.</td>
<td width="220">Peg insertion, tactile classification, and multi-finger grasping/manipulation.</td>
<td width="300">Warp-based ABD + IPC simulate contact and tactile images; learned policies/classifiers consume the rendered signals.</td>
<td width="220">Closed-loop in simulated control tasks; no single global control rate is disclosed.</td>
<td width="200">Task-specific RL motor actions or classifier outputs.</td>
<td width="330">Taccel GPU simulator; dual-GelSight peg: 4,096 envs at 915 FPS; multi-hand study uses about 14k grasps.</td>
<td width="110">Simulation primary + limited real transfer</td>
<td width="320">Real classifier accuracy is 70.94%; four reported grasp SRs are 44.56/44.61/54.30/42.54%.</td>
<td width="230">Provides high-throughput deformable tactile simulation and robot/sensor APIs.</td>
<td width="240">Hardware transfer remains task- and calibration-specific despite limited sim-to-real evidence.</td>
<td width="180"><a href="https://taccel-simulator.github.io/assets/taccel-paper.pdf">paper</a> / <a href="https://taccel-simulator.github.io/">project</a> / <a href="https://github.com/Taccel-Simulator/Taccel">code</a></td>
</tr>
<tr>
<td width="100" nowrap>NeurIPS 2025</td>
<td width="260"><a href="https://arxiv.org/abs/2511.16596">Toward Artificial Palpation: Representation Learning of Touch on Soft Bodies</a></td>
<td width="230">Learn representations of internal soft-body structure from palpation sequences.</td>
<td width="300">Franka Emika Panda with one XELA uSkin sensor.</td>
<td width="280">Thirty 3-axis force cells at 85 Hz; acquisition uses a 3.8 N low-level force target.</td>
<td width="220">Automated poking/palpation, MRI reconstruction, and change detection.</td>
<td width="300">Force and robot-pose sequences feed MLP/GRU representation models.</td>
<td width="220">Only the data-collection controller closes a 3.8 N force loop; learned inference has no motion-planning loop.</td>
<td width="200">Programmed poke positions with low-level force regulation.</td>
<td width="330">PalpationSim 2D FEM; real: about 550 phantoms, 60k pokes, and 30M instantaneous readings.</td>
<td width="110">Simulation + real perception</td>
<td width="320">Size error 23%, center-of-mass error 2.4 mm, and change-detection F1 74.4%.</td>
<td width="230">Connects sequential touch to soft-body reconstruction and releases simulation/real datasets.</td>
<td width="240">The simulator is explicitly simplified; sensor-motion planning and clinical validation are unsolved.</td>
<td width="180"><a href="https://arxiv.org/abs/2511.16596">paper</a> / <a href="https://zoharri.github.io/artificial-palpation/">project</a> / <a href="https://github.com/zoharri/ArtificialPalpation">code</a> / <a href="https://zenodo.org/records/17608184">data</a></td>
</tr>
<tr>
<td width="100" nowrap>NeurIPS 2025</td>
<td width="260"><a href="https://arxiv.org/abs/2507.15062v1">Touch in the Wild: Learning Fine-Grained Manipulation with a Portable Visuo-Tactile Gripper</a></td>
<td width="230">Collect portable in-the-wild touch demonstrations and transfer them to precise robot policies.</td>
<td width="300">Hand-held soft-fin tactile gripper for collection; xArm 850 with the same gripper for policy deployment; GoPro Hero 9.</td>
<td width="280">Two 12x32 pads form a 1x24x32 tactile image, 2 mm² per taxel, at 23 Hz; GoPro video at 60 Hz.</td>
<td width="220">Test-tube/pencil insertion, fluid transfer, and whiteboard erasing.</td>
<td width="300">A tactile CNN and visual ViT are fused by cross-attention before a diffusion policy.</td>
<td width="220">Closed-loop diffusion policy; policy rate is not reported; tactile/video streams are 23/60 Hz.</td>
<td width="200">Arm/gripper action chunks from the diffusion policy.</td>
<td width="330">Real-only: 2.6M visuo-tactile pairs, 2,700+ demonstrations, 43 tasks, and 12 environments.</td>
<td width="110">Real collection + real deployment</td>
<td width="320">Four-task SR 0.85/0.85/0.90/0.70 versus vision-only 0.25/0.45/0.55/0.55.</td>
<td width="230">Portable data and tactile pretraining improve data efficiency and robustness to visual degradation.</td>
<td width="240">Each downstream task still requires policy training on the custom gripper.</td>
<td width="180"><a href="https://arxiv.org/abs/2507.15062v1">paper</a> / <a href="https://binghao-huang.github.io/touch_in_the_wild/">project</a> / <a href="https://github.com/YolandaXinyueZhu/touch_in_the_wild">code</a> / <a href="https://huggingface.co/datasets/binghaohuang-robot/touch_in_the_wild-dataset">data</a></td>
</tr>
<tr>
<td width="100" nowrap>arXiv 2026</td>
<td width="260"><a href="https://arxiv.org/abs/2606.17055">T-Rex: Tactile-Reactive Dexterous Manipulation</a></td>
<td width="230">Make a bimanual dexterous policy react to touch faster than its vision/action backbone.</td>
<td width="300">Fixed-base Dexmate Vega-1 (14 arm joints) with two 22-DoF Sharpa Wave hands; ZED cameras.</td>
<td width="280">All ten fingers provide deformation-depth maps and 6-axis wrenches; logged with RGB/state/action at 30 Hz.</td>
<td width="220">Twelve delicate-force and deformable-object manipulation tasks.</td>
<td width="300">A temporal tactile VQ-VAE feeds a three-expert asynchronous Mixture-of-Transformers; the tactile expert refines actions.</td>
<td width="220">Action expert about 5 Hz, tactile expert about 20 Hz, PID at 300 Hz; synchronized demonstrations at 30 Hz.</td>
<td width="200">Bimanual arm/hand action chunks refined asynchronously by touch and tracked by PID.</td>
<td width="330">Real-only: 100 h, 7,755 episodes, 207 objects, 22 motor primitives; plus 22,889 h human video pretraining.</td>
<td width="110">Real only</td>
<td width="320">Average SR across 12 tasks is 65% versus 35% for the baseline and 42% without tactile input.</td>
<td width="230">Separates slow semantic actions from fast tactile reactions for bimanual dexterity.</td>
<td width="240">Sensor distortion/calibration drift and missing dense palm sensing remain limiting.</td>
<td width="180"><a href="https://arxiv.org/abs/2606.17055">paper</a> / <a href="https://tactile-rex.github.io/">project</a></td>
</tr>
<tr>
<td width="100" nowrap>arXiv 2026</td>
<td width="260"><a href="https://arxiv.org/abs/2606.13102">FTP-1: A Generalist Foundation Tactile Policy Across Tactile Sensors for Contact-Rich Manipulation</a></td>
<td width="230">Train one tactile expert across heterogeneous sensor formats and robot embodiments.</td>
<td width="300">Five downstream configurations spanning UniVTAC simulation and Sharpa/Dexmate, Flexiv, and Franka real platforms.</td>
<td width="280">MTTS covers 21 sensors/26 sources: 7 image, 5 array, and 9 state sensors mapped into 24 sensor slots.</td>
<td width="220">General contact-rich manipulation across seen and unseen tactile hardware.</td>
<td width="300">A 300M-parameter tactile Transformer conditions the action expert through a one-way interface.</td>
<td width="220">High-level tactile-conditioned closed loop; force servo and control rate are not reported.</td>
<td width="200">A downstream action expert outputs robot-specific actions conditioned on FTP-1 features.</td>
<td width="330">About 3,000 h from 26 sources and 21 sensors; mixed UniVTAC simulation and real robot data.</td>
<td width="110">Simulation + real pretraining/evaluation</td>
<td width="320">Simulation 66.66% vs 49.16%; seen-real 62.5% vs 45.3%; unseen-real average 46.6% vs 15%.</td>
<td width="230">Demonstrates shared tactile pretraining across sensor modalities and unseen downstream sensors.</td>
<td width="240">Downstream fine-tuning is still required, and FTP-1 is not a general force-servo controller.</td>
<td width="180"><a href="https://arxiv.org/abs/2606.13102">paper</a> / <a href="https://ftp1-policy.github.io/">project</a> / <a href="https://github.com/michaelyuancb/ftp1-policy">code</a></td>
</tr>
<tr>
<td width="100" nowrap>ICRA 2026</td>
<td width="260"><a href="https://opendrivelab.com/FreeTacMan">FreeTacMan: Robot-free Visuo-Tactile Data Collection System for Contact-rich Manipulation</a></td>
<td width="230">Scale contact-rich demonstrations by removing the robot from data collection.</td>
<td width="300">Hand-held dual-finger McTac device for collection; 6-DoF Piper arm for learned-policy deployment.</td>
<td width="280">McTac cameras 640x480 at 30 Hz; fisheye video 30 Hz; NOKOV tracking 240 Hz; synchronized records at 30 Hz.</td>
<td width="220">Fifty contact-rich tasks followed by robot-policy transfer.</td>
<td width="300">ResNet tactile features receive CLIP-style pretraining; touch and vision are concatenated before ACT.</td>
<td width="220">Closed-loop ACT policy on Piper; policy execution rate is not disclosed.</td>
<td width="200">ACT arm/gripper action chunks for the Piper platform.</td>
<td width="330">No simulation; 3M+ visuo-tactile pairs and 10k+ trajectories across 50 real tasks.</td>
<td width="110">Robot-free real collection + real robot deployment</td>
<td width="320">Overall SR follows the reported ablation ladder 21%→55%→71% with tactile data/pretraining.</td>
<td width="230">Decouples tactile demonstration collection from a specific robot and improves policy transfer.</td>
<td width="240">Reported control results center on Piper, and policy frequency/hardware generality remain incompletely specified.</td>
<td width="180"><a href="https://opendrivelab.com/FreeTacMan">project</a> / <a href="https://github.com/OpenDriveLab/FreeTacMan">code</a></td>
</tr>
<tr>
<td width="100" nowrap>ICRA 2026</td>
<td width="260"><a href="https://arxiv.org/abs/2602.11643">ViTaS: Visual Tactile Soft Fusion Contrastive Learning for Visuomotor Learning</a></td>
<td width="230">Pretrain visuomotor policies that use tactile information without hard feature alignment.</td>
<td width="300">Real Galaxea-R1 with ZED 2 and 3D-ViTaC gripper; simulated parallel grippers and five-finger hand.</td>
<td width="280">Simulation uses 32x32x3 maps or five 3x3x3 fingertip arrays; real 3D-ViTaC is 16x16x1.</td>
<td width="220">Twelve tasks in five simulated environments and three real tactile tasks.</td>
<td width="300">Soft-fusion contrastive learning precedes CVAE/PPO/diffusion-policy heads.</td>
<td width="220">Closed-loop learned policies; execution rate is not disclosed.</td>
<td width="200">PPO motor actions for RL or CVAE/diffusion action distributions for imitation learning.</td>
<td width="330">Simulation: 12 tasks across Gymnasium, robosuite, Insertion, Mobile Catching, and Block Spinning environments; RL 3M steps, IL 50 demos/task. Real Galaxea-R1: 100 teleoperated trajectories/task.</td>
<td width="110">Separate simulation and real training/evaluation; not Sim2Real</td>
<td width="320">Simulation average 91.4% vs 71.5%; removing touch 92.5→60.9%; real average 46% vs DP 30%.</td>
<td width="230">Soft contrastive fusion improves tactile visuomotor learning across RL, IL, and separately trained real-world policies.</td>
<td width="240">Real evaluation has only three tasks and relies on custom tactile hardware.</td>
<td width="180"><a href="https://arxiv.org/abs/2602.11643">paper</a> / <a href="https://skyrainwind.github.io/ViTaS/index.html">project</a> / <a href="https://github.com/SkyRainWind/ViTaS">code</a></td>
</tr>
<tr>
<td width="100" nowrap>ICRA 2026</td>
<td width="260"><a href="https://arxiv.org/abs/2510.06339">Vi-TacMan: Articulated Object Manipulation via Vision and Touch</a></td>
<td width="230">Use vision for global initialization and touch for precise articulated-object execution.</td>
<td width="300">Kinova Gen3, two custom GelSight-style gripper pads, Intel RealSense Femto Bolt.</td>
<td width="280">Marker-based optical tactile images; registration-based tactile controller runs at 50 Hz.</td>
<td width="220">Manipulate articulated objects under visual pose/direction ambiguity.</td>
<td width="300">DINOv3/SAM2 provide visual grasp proposals; PointNet/vMF predicts direction; tactile Kabsch registration refines execution.</td>
<td width="220">Vision initializes grasp/direction once; execution then uses a tactile-only 50 Hz loop.</td>
<td width="200">Cartesian direction/pose corrections from tactile registration.</td>
<td width="330">SAPIEN: 385 objects and 55,241 visual displacement samples; real: 4 objects x 5 views; no tactile physics simulator reported.</td>
<td width="110">Simulation for visual module + real tactile execution</td>
<td width="320">Unseen-object direction error is 8.13°; real robot results are qualitative and report no success rate.</td>
<td width="230">Assigns complementary roles to global vision and local tactile feedback.</td>
<td width="240">Real evaluation lacks quantitative SR and covers few articulated objects.</td>
<td width="180"><a href="https://arxiv.org/abs/2510.06339">paper</a> / <a href="https://vi-tacman.github.io/">project</a></td>
</tr>
<tr>
<td width="100" nowrap>CoRL 2025</td>
<td width="260"><a href="https://proceedings.mlr.press/v305/xu25e.html">exUMI: Extensible Robot Teaching System with Action-aware Task-agnostic Tactile Representation</a></td>
<td width="230">Collect calibrated tactile demonstrations and learn reusable action-aware touch features.</td>
<td width="300">Teaching device: Meta Quest 3, rotary encoder, Orange Pi, and two 9DTact sensors; deployment: Flexiv Rizon 4 + Grav gripper + GoPro.</td>
<td width="280">Two 9DTact grayscale streams resized to 224x224; over 1M aligned frames, including 480k touch frames / 5 h.</td>
<td width="220">Four diverse contact-rich skills collected with an extensible UMI-style device.</td>
<td width="300">TPP uses a VAE, Transformer, and latent diffusion model; its tactile embedding is concatenated into a diffusion policy.</td>
<td width="220">Closed-loop diffusion policy at 10 Hz.</td>
<td width="200">End-effector and gripper action chunks from the diffusion policy.</td>
<td width="330">Real-only: 10 environments, 300+ objects, over 1M aligned frames; 480k tactile frames / 5 h.</td>
<td width="110">Real teaching + real deployment</td>
<td width="320">Across 20 trials per task, TPP SR is 85/60/95/80% on the four tasks.</td>
<td width="230">Improves tactile teaching data quality and transfers task-agnostic touch representations to policies.</td>
<td width="240">The custom teaching/deployment stack still needs setup-specific calibration.</td>
<td width="180"><a href="https://proceedings.mlr.press/v305/xu25e.html">PMLR</a> / <a href="https://silicx.github.io/exUMI/">project</a> / <a href="https://github.com/silicx/exUMI">code</a></td>
</tr>
<tr>
<td width="100" nowrap>CoRL 2025</td>
<td width="260"><a href="https://proceedings.mlr.press/v305/wistreich25a.html">DexSkin: High-Coverage Conformable Robotic Skin for Learning Contact-Rich Manipulation</a></td>
<td width="230">Give a simple gripper broad contact coverage for learning contact-rich behaviors.</td>
<td width="300">Franka Panda, SSG-48 parallel gripper with DexSkin on both fingers, and RealSense D415.</td>
<td width="280">60 capacitive taxels per finger (120 total), 294° coverage, 30 Hz, 0–2.5 N; force RMSE 0.086 N.</td>
<td width="220">In-hand pen reorientation under disturbance, berry handling, and elastic-band manipulation.</td>
<td width="300">Calibrated tactile vectors are fused with vision/proprioception in diffusion-policy and online-RL pipelines.</td>
<td width="220">Closed-loop diffusion policy at 20 Hz; online RL is also tactile-conditioned.</td>
<td width="200">Arm/gripper policy actions using high-coverage finger contact.</td>
<td width="330">Real-only; 50 demonstrations for diffusion-policy tasks plus calibration/model-transfer and online-RL runs.</td>
<td width="110">Real only</td>
<td width="320">Pen perturbation: 19/20 vs 0/20 without touch; intact-berry rate 60% vs 20%.</td>
<td width="230">Shows conformable high-coverage skin can support model transfer and learned reactive behaviors.</td>
<td width="240">Evaluated on a parallel-jaw gripper rather than a full multi-finger hand.</td>
<td width="180"><a href="https://proceedings.mlr.press/v305/wistreich25a.html">PMLR</a> / <a href="https://dex-skin.github.io/">project</a> / <a href="https://github.com/sdwistreich/dexskin">code</a></td>
</tr>
<tr>
<td width="100" nowrap>RSS 2025</td>
<td width="260"><a href="https://arxiv.org/abs/2504.16649">PP-Tac: Paper Picking Using Tactile Feedback in Dexterous Robotic Hands</a></td>
<td width="230">Pick one or several paper sheets using slip-aware fingertip feedback.</td>
<td width="300">Franka Research 3 with a custom 16-DoF four-finger hand and four R-Tac fingertips.</td>
<td width="280">OV9281 640x480, up to 120 Hz, about 100 ms latency, 2 mm gel layer.</td>
<td width="220">Paper picking with slip detection, online grip-force adjustment, and learned trajectories.</td>
<td width="300">Tactile depth and 152-D proprioception condition a diffusion policy; detected slip triggers force increase.</td>
<td width="220">Slip-triggered force feedback is closed-loop; diffusion-policy rate is not disclosed.</td>
<td width="200">Arm/16-DoF hand action sequence with online grip-force increments.</td>
<td width="330">500k rigid grasp sequences x 100 frames for policy training; no tactile physics simulator; real tactile evaluation.</td>
<td width="110">Generated rigid sequences + real evaluation</td>
<td width="320">Overall success 87.5%; selecting exactly 1/3/5/7 sheets succeeds 90/75/30/5%.</td>
<td width="230">Combines tactile depth, slip detection, force adjustment, and diffusion control for paper separation.</td>
<td width="240">The task is narrow; performance drops sharply for thicker sheet counts, and sensing has notable latency.</td>
<td width="180"><a href="https://arxiv.org/abs/2504.16649">paper</a> / <a href="https://www.roboticsproceedings.org/rss21/p056.pdf">RSS</a> / <a href="https://peilin-666.github.io/projects/PP-Tac/">project</a> / <a href="https://github.com/bigai-ai/PP-Tac">code</a></td>
</tr>
<tr>
<td width="100" nowrap>ICRA 2026</td>
<td width="260"><a href="https://arxiv.org/abs/2509.23468">Multi-Modal Manipulation via Multi-Modal Policy Consensus</a></td>
<td width="230">Remain robust when vision, touch, or proprioception is corrupted by avoiding early feature fusion.</td>
<td width="300">UR5e, two RealSense D415 streams at 96x128, and FlexiTac pads on both gripper fingers.</td>
<td width="280">Each FlexiTac pad is 12x32 with 2 mm spatial pitch; tactile sampling rate is not disclosed.</td>
<td width="220">Four RLBench tasks and real occluded picking, spoon reorientation, and puzzle insertion/manipulation.</td>
<td width="300">Each modality has a DDPM score expert; a router combines their action distributions at policy-consensus time.</td>
<td width="220">Closed-loop policy; execution rate is not disclosed.</td>
<td width="200">Consensus diffusion action trajectory for the arm/gripper.</td>
<td width="330">RLBench: 4 tasks, 200 demonstrations, 200 unseen tests; real demonstrations: 80/60/50 across three collections.</td>
<td width="110">Simulation + real evaluation</td>
<td width="320">Simulation average SR 0.66 vs 0.56 for feature concatenation; four real settings score 0.65/0.75/0.58/0.45.</td>
<td width="230">Action-space consensus preserves useful modalities when another sensor is unreliable.</td>
<td width="240">Control rate and some low-level hardware details are undisclosed; real coverage is small.</td>
<td width="180"><a href="https://arxiv.org/abs/2509.23468">paper</a> / <a href="https://policyconsensus.github.io/">project</a> / <a href="https://openreview.net/forum?id=CJDU8IvF3y">OpenReview</a></td>
</tr>
<tr>
<td width="100" nowrap>arXiv 2026</td>
<td width="260"><a href="https://arxiv.org/abs/2602.06001">Visuo-Tactile World Models for Robot Manipulation</a></td>
<td width="230">Predict contact dynamics under occlusion and use the model to plan real robot motion.</td>
<td width="300">Franka Panda, Allegro Hand, and four DIGIT 360 fingertips.</td>
<td width="280">Touch at 30 FPS; vision/action trajectory chunks execute at 6 Hz.</td>
<td width="220">Real-robot reach, push, reach-push, wipe, and stack under contact uncertainty.</td>
<td width="300">Cosmos visual and Sparsh-X tactile embeddings feed a 12-layer Transformer world model; CEM searches action chunks.</td>
<td width="220">No tactile feedback inside a trajectory chunk; chunks execute open-loop at 6 Hz, so this is not a tactile servo loop.</td>
<td width="200">CEM-selected open-loop action chunks for arm/hand motion.</td>
<td width="330">Real-only: 124 demonstrations / 112k training points; validation 26 demonstrations / 17k points.</td>
<td width="110">Real only</td>
<td width="320">V-WM→VT-WM SR: Reach 100→100, Push 83→92, Reach-Push 69→93, Wipe 70→92, Stack 75→83%.</td>
<td width="230">Touch improves object permanence and contact-dynamics prediction for model-based planning.</td>
<td width="240">CEM planning is computationally expensive, data are limited, and execution remains open-loop within each chunk.</td>
<td width="180"><a href="https://arxiv.org/abs/2602.06001">paper</a> / <a href="https://carolinahiguera.github.io/vtml/">project</a></td>
</tr>
</tbody>
</table>
