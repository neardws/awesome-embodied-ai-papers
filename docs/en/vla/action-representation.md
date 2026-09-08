# action representation

[Home](../../../README.md) | [中文](../../zh-CN/vla/action-representation.md) | [Direction index](README.md)

Total: 30 papers.

<table width="3260">
<thead>
<tr>
<th width="120" nowrap>Venue/Year</th>
<th width="320">Paper/Method</th>
<th width="420">Abstract</th>
<th width="230">Base VLA</th>
<th width="240">Action</th>
<th width="300">Training/Feedback</th>
<th width="260">Algorithm</th>
<th width="240">Policy/Type</th>
<th width="200">Sim/Real</th>
<th width="360">Paper Task/Goal</th>
<th width="110" nowrap>Paper</th>
<th width="110" nowrap>Project</th>
<th width="110" nowrap>Code</th>
<th width="240">Data/Bench</th>
</tr>
</thead>
<tbody>
<tr>
<td width="120" nowrap>ICML 2024</td>
<td width="320"><a href="https://proceedings.mlr.press/v235/he24o.html">DynSyn: Dynamical Synergistic Representation for Efficient Learning and Control in Overactuated Embodied Systems</a></td>
<td width="420">Learns low-dimensional dynamical synergies for highly overactuated musculoskeletal control.</td>
<td width="230">- (non-robot musculoskeletal models)</td>
<td width="240">muscle excitation: MyoHand R39 / Arm-Locate R81, compressed through a learned synergy</td>
<td width="300">MuJoCo + MyoSuite; ~5×10^5 frames for synergy extraction; ~3M RL steps/task, 5 seeds</td>
<td width="260">unsupervised dynamical synergy representation + downstream RL</td>
<td width="240">Sim-only latent action representation; not physical robot-hand hardware</td>
<td width="200">Sim only</td>
<td width="360">Controls MS-HUMAN-700, Arm-Locate, and MyoHand-Reorient100; reports return/sample-efficiency curves rather than a stable grasp success rate</td>
<td width="110" nowrap><a href="https://proceedings.mlr.press/v235/he24o.html">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">MuJoCo/MyoSuite; 100 MyoHand object geometries</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=tv0Sz8A9Tc">Robotic Manipulation by Imitating Generated Videos Without Physical Demonstrations (RIGVid)</a></td>
<td width="420">Turns generated task videos into executable robot trajectories without physical demonstrations or policy training.</td>
<td width="230">Kling/Sora video generators + FoundationPose</td>
<td width="240">tracked object 6-DoF trajectory → retargeted end-effector 6-DoF trajectory</td>
<td width="300">4 tasks; 10 generated videos per task/source; no physics simulator and no robot-policy dataset</td>
<td width="260">video filtering + object tracking + fixed gripper-object transform retargeting</td>
<td width="240">generated-video-to-action representation; xArm7 and ALOHA; ordinary grippers</td>
<td width="200">Real only; no Sim2Real physics pipeline</td>
<td width="360">Filtered Kling v1.6: 100/80/90/70% across four tasks; overall 85% vs ReKep 50%; ALOHA pouring 80%, xArm 100%</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=tv0Sz8A9Tc">paper</a></td>
<td width="110" nowrap><a href="https://rigvid-robot.github.io/">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">generated videos only; no physical demonstrations</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2022</td>
<td width="320"><a href="https://arxiv.org/abs/2203.06173">Real-World Robot Learning with Masked Visual Pre-training</a></td>
<td width="420">MVP uses masked visual pretraining for real-world robot learning.</td>
<td width="230">Real-World Robot Learning with Masked Visual Pre-training</td>
<td width="240">robot action</td>
<td width="300">VLA / action representation</td>
<td width="260">CoRL robot-learning method</td>
<td width="240">robot policy</td>
<td width="200">robot benchmarks</td>
<td width="360">Add CoRL VLA coverage.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2203.06173">paper</a></td>
<td width="110" nowrap><a href="https://tetexiao.com/projects/real-mvp">project</a></td>
<td width="110" nowrap><a href="https://github.com/ir413/mvp">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2022</td>
<td width="320"><a href="https://arxiv.org/abs/2203.12601">R3M: A Universal Visual Representation for Robot Manipulation</a></td>
<td width="420">R3M learns a universal visual representation for robot manipulation.</td>
<td width="230">R3M</td>
<td width="240">robot action</td>
<td width="300">VLA / action representation</td>
<td width="260">CoRL robot-learning method</td>
<td width="240">robot policy</td>
<td width="200">robot benchmarks</td>
<td width="360">Add CoRL VLA coverage.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2203.12601">paper</a></td>
<td width="110" nowrap><a href="https://sites.google.com/view/robot-r3m/">project</a></td>
<td width="110" nowrap><a href="https://github.com/facebookresearch/r3m">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2023</td>
<td width="320"><a href="https://arxiv.org/abs/2306.10007">Robot Learning with Sensorimotor Pre-training</a></td>
<td width="420">RPT uses sensorimotor pretraining for downstream robot learning.</td>
<td width="230">Robot Learning with Sensorimotor Pre-training</td>
<td width="240">robot action</td>
<td width="300">VLA / action representation</td>
<td width="260">CoRL robot-learning method</td>
<td width="240">robot policy</td>
<td width="200">robot benchmarks</td>
<td width="360">Add CoRL VLA coverage.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2306.10007">paper</a></td>
<td width="110" nowrap><a href="https://robotic-pretrained-transformer.github.io">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2024</td>
<td width="320"><a href="https://arxiv.org/abs/2407.20179">Theia: Distilling Diverse Vision Foundation Models for Robot Learning</a></td>
<td width="420">Theia distills diverse vision foundation models into robot-learning representations.</td>
<td width="230">Theia</td>
<td width="240">robot action</td>
<td width="300">VLA / action representation</td>
<td width="260">CoRL robot-learning method</td>
<td width="240">robot policy</td>
<td width="200">robot benchmarks</td>
<td width="360">Add CoRL VLA coverage.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2407.20179">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2509.07962">TA-VLA: Elucidating the Design Space of Torque-aware Vision-Language-Action Models</a></td>
<td width="420">TA-VLA studies torque-aware action design for VLA models.</td>
<td width="230">TA-VLA</td>
<td width="240">robot action</td>
<td width="300">VLA / action representation</td>
<td width="260">CoRL robot-learning method</td>
<td width="240">robot policy</td>
<td width="200">robot benchmarks</td>
<td width="360">Add CoRL VLA coverage.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2509.07962">paper</a></td>
<td width="110" nowrap><a href="https://zzongzheng0918.github.io/Torque-Aware-VLA.github.io/">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2508.01600">CLASS: Contrastive Learning via Action Sequence Supervision for Robot Manipulation</a></td>
<td width="420">CLASS uses action-sequence supervision for contrastive robot manipulation learning.</td>
<td width="230">CLASS</td>
<td width="240">robot action</td>
<td width="300">VLA / action representation</td>
<td width="260">CoRL robot-learning method</td>
<td width="240">robot policy</td>
<td width="200">robot benchmarks</td>
<td width="360">Add CoRL VLA coverage.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2508.01600">paper</a></td>
<td width="110" nowrap><a href="https://class-robot.github.io/">project</a></td>
<td width="110" nowrap><a href="https://github.com/sean1295/CLASS/tree/main">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2021</td>
<td width="320"><a href="https://arxiv.org/abs/2010.14406">Transporter Networks: Rearranging the Visual World for Robotic Manipulation</a></td>
<td width="420">Transporter Networks represent pick-and-place manipulation through spatial transport operations.</td>
<td width="230">Transporter Networks</td>
<td width="240">robot action</td>
<td width="300">VLA / action representation</td>
<td width="260">CoRL robot-learning method</td>
<td width="240">robot policy</td>
<td width="200">robot benchmarks</td>
<td width="360">Add CoRL VLA coverage.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2010.14406">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2024</td>
<td width="320"><a href="https://arxiv.org/abs/2310.08576">Learning to Act from Actionless Videos through Dense Correspondences</a></td>
<td width="420">This work learns action representations from actionless videos using dense visual correspondences.</td>
<td width="230">video pretraining</td>
<td width="240">latent action</td>
<td width="300">action representation / pretraining</td>
<td width="260">dense correspondence learning</td>
<td width="240">video-to-action representation</td>
<td width="200">robot manipulation benchmarks</td>
<td width="360">Recover reusable action structure without action labels.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2310.08576">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2024</td>
<td width="320"><a href="https://arxiv.org/abs/2402.07872">PIVOT: Iterative Visual Prompting Elicits Actionable Knowledge for VLMs</a></td>
<td width="420">PIVOT elicits spatial and actionable knowledge from VLMs through iterative visual prompting.</td>
<td width="230">VLM</td>
<td width="240">actionable visual prompt</td>
<td width="300">action representation / affordance</td>
<td width="260">iterative visual prompting</td>
<td width="240">VLM affordance reasoning</td>
<td width="200">spatial action benchmarks</td>
<td width="360">Extract actionable spatial knowledge from VLMs.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2402.07872">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=y5CaJb17Fn">villa-X: Enhancing Latent Action Modeling in Vision-Language-Action Models</a></td>
<td width="420">villa-X learns and uses latent actions as motion abstractions in VLA pretraining, enabling zero-shot generation of latent action plans.</td>
<td width="230">ViLLA/villa-X</td>
<td width="240">latent action</td>
<td width="300">action representation / action representation/tokenization</td>
<td width="260">latent action modeling for VLA pretraining</td>
<td width="240">Vision-Language-Latent-Action</td>
<td width="200">SIMPLER + two real setups</td>
<td width="360">Latent-action pretraining.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=y5CaJb17Fn">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2410.11758">Latent Action Pretraining from Videos</a></td>
<td width="420">LAPA learns latent action abstractions from videos before transferring them to robot action generation.</td>
<td width="230">LAPA</td>
<td width="240">latent action</td>
<td width="300">action representation / pretraining</td>
<td width="260">latent action pretraining</td>
<td width="240">video-to-action representation</td>
<td width="200">robot manipulation benchmarks</td>
<td width="360">Learn reusable latent actions from videos for downstream VLA policies.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2410.11758">paper</a></td>
<td width="110" nowrap><a href="https://latentactionpretraining.github.io/">project</a></td>
<td width="110" nowrap><a href="https://github.com/LatentActionPretraining/LAPA">code</a></td>
<td width="240"><a href="https://huggingface.co/latent-action-pretraining/LAPA-7B-openx">hf</a></td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=IZHk6BXBST">Rodrigues Network for Learning Robot Actions</a></td>
<td width="420">RodriNet injects kinematic structural priors into the action network through a learnable Neural Rodrigues Operator.</td>
<td width="230">-</td>
<td width="240">kinematics-aware action representation</td>
<td width="300">action representation / action representation/tokenization</td>
<td width="260">Neural Rodrigues Operator + RodriNet</td>
<td width="240">action network architecture</td>
<td width="200">synthetic + imitation benchmarks + hand reconstruction</td>
<td width="360">Kinematic structure modeling for robot actions.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=IZHk6BXBST">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38937">Actor-Critic for Continuous Action Chunks: A Reinforcement Learning Framework for Long-Horizon Robotic Manipulation with Sparse Reward</a></td>
<td width="420">AC3 directly learns continuous action chunks with actor-critic and stabilizes training through asymmetric updates on successful trajectories and in-chunk n-step returns.</td>
<td width="230">-</td>
<td width="240">continuous action chunks</td>
<td width="300">RL / sparse reward</td>
<td width="260">AC3</td>
<td width="240">actor-critic chunk policy</td>
<td width="200">BiGym + RLBench</td>
<td width="360">Sparse-reward long-horizon continuous action-chunk learning.</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38937">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/60681">DyGRO-VLA: Cross-Task Scaling of Vision-Language-Action Models via Dynamic Grouped Residual Optimization</a></td>
<td width="420">DyGRO-VLA first learns cross-task latent representations, then uses dynamic grouping RL residuals to optimize multi-task VLAs.</td>
<td width="230">DyGRO-VLA</td>
<td width="240">residual policy optimization</td>
<td width="300">RL/online fine-tuning</td>
<td width="260">Dynamic Grouped Residual Optimization</td>
<td width="240">cross-task RL-optimized VLA</td>
<td width="200">LIBERO/RoboTwin2 + Real</td>
<td width="360">Cross-task VLA RL optimization.</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/60681">paper</a></td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/60681">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/61232">LARA: Latent Action Representation Alignment for Vision-Language-Action Models</a></td>
<td width="420">LARA jointly optimizes a latent action model and a VLA so human-video latent actions better align with real action trajectories.</td>
<td width="230">LARA plug-in</td>
<td width="240">latent action representation</td>
<td width="300">VLA / Action Representation/Tokenization</td>
<td width="260">LAM-VLA representation alignment</td>
<td width="240">pre/post-training enhancement</td>
<td width="200">3 sim + 1 real benchmark</td>
<td width="360">Latent-action alignment.</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/61232">paper</a></td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/61232">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/62908">From Noise to Intent: Anchoring Generative VLA Policies with Residual Bridges</a></td>
<td width="420">ResVLA changes generated actions from noise generation to intent-anchored residual refinement, separating low-frequency intent from high-frequency local dynamics.</td>
<td width="230">ResVLA</td>
<td width="240">Diffusion / residual bridge</td>
<td width="300">VLA / Action Representation/Tokenization</td>
<td width="260">low-frequency intent anchor + high-frequency residual diffusion bridge</td>
<td width="240">generative VLA policy</td>
<td width="200">LIBERO/LIBERO-Plus</td>
<td width="360">Generative action-decoding stability.</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/62908">paper</a></td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/62908">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/65967">Demystifying Action Space Design for Robotic Manipulation Policies</a></td>
<td width="420">This paper uses 13k+ real rollouts and 500+ models to systematically analyze the effects of absolute/incremental and joint/task-space action designs.</td>
<td width="230">-</td>
<td width="240">delta actions preferred</td>
<td width="300">action representation / action representation/tokenization</td>
<td width="260">large-scale action-space empirical study</td>
<td width="240">action-space design study</td>
<td width="200">Real bimanual robot</td>
<td width="360">Action-space design principles.</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/65967">paper</a></td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/65967">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/66520">FocalPolicy: Frequency-Optimized Chunking and Locally Anchored Flow Matching for Coherent Visuomotor Policy</a></td>
<td width="420">FocalPolicy uses frequency-domain optimization of chunking and locally anchored flow matching to improve coherence across long-horizon action chunks.</td>
<td width="230">visuomotor policy</td>
<td width="240">Diffusion / Flow action chunks</td>
<td width="300">flow matching / diffusion/flow policy</td>
<td width="260">Frequency-Optimized Chunking + Locally Anchored Flow Matching</td>
<td width="240">flow-matching visuomotor policy</td>
<td width="200">-</td>
<td width="360">Coherence across action chunks.</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/66520">paper</a></td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/66520">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/62176">GeoMoLa: Geometry-Aware Motion Latents for Learning Robust Manipulation Policies</a></td>
<td width="420">GeoMoLa learns discrete motion latent codes by predicting 4D geometric changes in point clouds during manipulation.</td>
<td width="230">GeoMoLa</td>
<td width="240">discrete motion latent codes</td>
<td width="300">action representation / action representation/tokenization</td>
<td width="260">geometry-aware point-cloud evolution objective</td>
<td width="240">motion latent policy</td>
<td width="200">benchmarks + Real</td>
<td width="360">Geometry-aware action latents.</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/62176">paper</a></td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/62176">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2604.04161">Adaptive Action Chunking at Inference-time for Vision-Language-Action Models</a></td>
<td width="420">AAC uses action entropy at inference time to dynamically select action-chunk length, balancing reactivity and continuity.</td>
<td width="230">generic VLA</td>
<td width="240">adaptive action chunks</td>
<td width="300">VLA / Action Representation/Tokenization</td>
<td width="260">action entropy based AAC</td>
<td width="240">inference-time adaptation</td>
<td width="200">Sim + Real</td>
<td width="360">Adaptive action chunking at inference time.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2604.04161">paper</a></td>
<td width="110" nowrap><a href="https://lance-lot.github.io/adaptive-chunking.github.io/">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2603.10158">Cross-Hand Latent Representation for Vision-Language-Action Models</a></td>
<td width="420">XL-VLA/DexLatent learns latent representations across different dexterous hands, allowing a single policy to transfer across hand morphologies.</td>
<td width="230">XL-VLA / DexLatent</td>
<td width="240">cross-hand latent representation</td>
<td width="300">VLA / Action Representation/Tokenization</td>
<td width="260">DexLatent</td>
<td width="240">cross-embodiment dexterous VLA</td>
<td width="200">-</td>
<td width="360">Addresses different action spaces across multi-fingered dexterous hands and the difficulty of cross-hand policy transfer.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2603.10158">paper</a></td>
<td width="110" nowrap><a href="https://xl-vla.github.io/">project</a></td>
<td width="110" nowrap><a href="https://github.com/EmptyBlueBox/DexLatent">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2506.16685">Compliant Residual DAgger: Improving Real-World Contact-Rich Manipulation with Human Corrections</a></td>
<td width="420">CR-DAgger improves contact-rich manipulation from human delta corrections through a compliant intervention interface and a force-feedback residual policy.</td>
<td width="230">-</td>
<td width="240">delta action corrections / residual policy</td>
<td width="300">DAgger / human corrections</td>
<td width="260">Compliant Residual DAgger</td>
<td width="240">human-in-the-loop residual policy</td>
<td width="200">Real</td>
<td width="360">Addresses the difficulty of collecting DAgger correction data and stabilizing policy updates in real contact-rich manipulation.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2506.16685">paper</a></td>
<td width="110" nowrap><a href="https://compliant-residual-dagger.github.io/">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2510.25138">Learning Spatial-Aware Manipulation Ordering</a></td>
<td width="420">OrderMind learns manipulation priority for each object in cluttered scenes directly from spatial context.</td>
<td width="230">OrderMind</td>
<td width="240">manipulation order priorities</td>
<td width="300">VLA / Action Representation/Tokenization</td>
<td width="260">spatial graph encoder + temporal priority structuring</td>
<td width="240">ordering policy</td>
<td width="200">benchmark + Real</td>
<td width="360">Addresses collisions or occlusions caused by incorrect manipulation order in cluttered environments.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2510.25138">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/yyxssm/OrderMind">code</a></td>
<td width="240">Manipulation Ordering Benchmark</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2509.15607">PRIMT: Preference-based Reinforcement Learning with Multimodal Feedback and Trajectory Synthesis from Foundation Models</a></td>
<td width="420">PRIMT uses LLM/VLM multimodal synthetic preference feedback and trajectory synthesis to reduce PbRL dependence on human feedback.</td>
<td width="230">-</td>
<td width="240">RL policy actions</td>
<td width="300">preference-based RL / multimodal synthetic feedback</td>
<td width="260">PRIMT + neuro-symbolic fusion + trajectory synthesis</td>
<td width="240">PbRL framework</td>
<td width="200">2 locomotion + 6 manipulation benchmarks</td>
<td width="360">Addresses heavy human feedback, query ambiguity, and difficult credit assignment in preference RL.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2509.15607">paper</a></td>
<td width="110" nowrap><a href="https://primt25.github.io/">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2502.01218">Provable Ordering and Continuity in Vision-Language Pretraining for Generalizable Embodied Agents</a></td>
<td width="420">AcTOL learns ordered continuous vision-language representations using inter-frame semantic ordering and local Brownian-bridge continuity constraints.</td>
<td width="230">AcTOL features</td>
<td width="240">pretraining representation</td>
<td width="300">VLA / Action Representation/Tokenization</td>
<td width="260">Action Temporal Coherence Learning</td>
<td width="240">VL pretraining for embodied agents</td>
<td width="200">-</td>
<td width="360">Ordered continuous vision-language pretraining.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2502.01218">paper</a></td>
<td width="110" nowrap><a href="https://actol-pretrain.github.io/">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2508.05941">Latent Policy Barrier: Learning Robust Visuomotor Policies by Staying In-Distribution</a></td>
<td width="420">LPB uses expert demonstration latent embeddings as implicit safety boundaries, optimizing future latents at inference time to stay within the expert distribution.</td>
<td width="230">LPB</td>
<td width="240">Diffusion policy + latent barrier correction</td>
<td width="300">action representation / action representation/tokenization</td>
<td width="260">Latent Policy Barrier + dynamics model</td>
<td width="240">robust visuomotor policy</td>
<td width="200">Sim + Real</td>
<td width="360">Addresses behavioral-cloning visuomotor policies gradually drifting away from expert trajectories due to covariate shift.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2508.05941">paper</a></td>
<td width="110" nowrap><a href="https://project-latentpolicybarrier.github.io/">project</a></td>
<td width="110" nowrap><a href="https://github.com/zhanyisun/lpb">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2412.04445">Moto: Latent Motion Token as the Bridging Language for Robot Manipulation</a></td>
<td width="420">Moto converts videos into latent motion tokens and uses Moto-GPT autoregressive pretraining to transfer video motion knowledge to robot control.</td>
<td width="230">Moto-GPT</td>
<td width="240">latent motion tokens</td>
<td width="300">VLA / action tokenization / action representation/tokenization</td>
<td width="260">Latent Motion Tokenizer + Moto-GPT autoregression</td>
<td width="240">video-pretrained motion-token policy</td>
<td width="200">-</td>
<td width="360">Addresses the lack of action-labeled robot data and the difficulty of directly using motion knowledge from video data.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2412.04445">paper</a></td>
<td width="110" nowrap><a href="https://chenyi99.github.io/moto/">project</a></td>
<td width="110" nowrap><a href="https://github.com/TencentARC/Moto">code</a></td>
<td width="240"><a href="https://huggingface.co/TencentARC/Moto">hf</a></td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2411.14519">Tra-MoE: Learning Trajectory Prediction Model from Multiple Domains for Adaptive Policy Conditioning</a></td>
<td width="420">Tra-MoE learns an MoE prediction model from multi-domain trajectories and adaptively adjusts policy conditioning with predicted trajectories.</td>
<td width="230">Tra-MoE</td>
<td width="240">trajectory prediction / policy conditioning</td>
<td width="300">action representation / action representation/tokenization</td>
<td width="260">Mixture-of-Experts trajectory model</td>
<td width="240">adaptive policy conditioning</td>
<td width="200">-</td>
<td width="360">Multi-domain trajectory prediction and policy conditioning.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2411.14519">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/MCG-NJU/Tra-MoE">code</a></td>
<td width="240">-</td>
</tr>
</tbody>
</table>
