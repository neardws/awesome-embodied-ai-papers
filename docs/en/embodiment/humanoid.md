# humanoid

[Home](../../../README.md) | [中文](../../zh-CN/embodiment/humanoid.md) | [Direction index](README.md)

Total: 78 papers. This is the single humanoid paper master table. Every row was checked against the primary paper or official project material and distinguishes real hardware, simulated robot models, and non-robot virtual humans. CoRL 2024 papers are labeled by conference year even when the PMLR volume was published in 2025. **Current bottlenecks prioritize author-stated limitations; when a paper has no limitations section, the cell records a verifiable evaluation boundary. Future directions are research inferences from those boundaries, not quotations from the authors.** The evidence columns report the simulator/training stack, benchmarks or datasets and their disclosed scale, training compute and wall-clock evidence, the training pipeline, and paper-reported quantitative details. **“Not disclosed” means the paper or official implementation did not report the item; it is not backfilled from convention. “Not applicable” is reserved for methods that do not use that resource or training stage. Evidence from official code is explicitly qualified.**

## Humanoid resource audit: counting method

Snapshot date: **2026-07-13**. Frequencies below count distinct papers, not raw mentions. A paper can contribute to multiple hardware, simulator, dataset, or training-stage rows, but the same normalized item is counted at most once per paper. Robot bodies, end effectors, compute hardware, physics engines, robot-learning frameworks, and auxiliary tools remain separate layers. Model names are preserved when disclosed: for example, H1 and H1-2 are separate, as are Isaac Gym, Isaac Lab, Isaac Sim, MuJoCo, and MJX. Long-tail rows retain every normalized single-paper item. The 78 paper rows below are the traceability ledger for all counts.

### Robot bodies and platforms used

<table width="1620">
<thead>
<tr>
<th width="240" nowrap>Normalized platform</th>
<th width="100">Papers</th>
<th width="280">Paper-table evaluation mix</th>
<th width="500">Platform information</th>
<th width="500">Counting boundary</th>
</tr>
</thead>
<tbody>
<tr>
<td width="240" nowrap><a href="https://www.unitree.com/g1/">Unitree G1</a></td>
<td width="100">29</td>
<td width="280">3 Sim Only; 2 Real; 14 Sim+Real; 10 Sim→Real</td>
<td width="500">Compact research humanoid; papers use different 23/27/29-DoF control or body configurations and optional hands.</td>
<td width="500">Counts explicit G1 mentions, including simulated G1 models; does not merge H1, H1-2, or unspecified Unitree hands.</td>
</tr>
<tr>
<td width="240" nowrap><a href="https://www.unitree.com/h1/">Unitree H1</a></td>
<td width="100">15</td>
<td width="280">2 Sim Only; 2 Real; 4 Sim+Real; 7 Sim→Real</td>
<td width="500">Full-size humanoid used for locomotion, whole-body control, teleoperation, and manipulation; paper-specific modifications range from 19 to 33 DoF.</td>
<td width="500">Counts H1 only; the explicitly named H1-2 version is a separate row.</td>
</tr>
<tr>
<td width="240" nowrap><a href="https://www.fftai.com/products-gr1">Fourier GR-1</a></td>
<td width="100">6</td>
<td width="280">1 Real; 3 Sim+Real; 2 Sim→Real</td>
<td width="500">Human-sized 44-joint platform; the surveyed papers use it for teleoperation, loco-manipulation, and cross-embodiment evaluation.</td>
<td width="500">Counts GR-1 bodies; Fourier hands and the Fourier N1 platform remain separate hardware.</td>
</tr>
<tr>
<td width="240" nowrap><a href="https://arxiv.org/abs/1809.07279">Agility Cassie</a></td>
<td width="100">6</td>
<td width="280">2 Sim+Real; 4 Sim→Real</td>
<td width="500">Underactuated biped research platform without arms, used primarily for locomotion, jumping, terrain adaptation, and multi-biped control.</td>
<td width="500">Counts physical Cassie and explicitly named Cassie simulator/model use.</td>
</tr>
<tr>
<td width="240" nowrap><a href="https://www.agilityrobotics.com/solutions/digit/spec-sheet">Agility Digit</a></td>
<td width="100">6</td>
<td width="280">4 Sim Only; 2 Sim+Real</td>
<td width="500">Armed bipedal humanoid used in navigation, locomotion, control, and tokenized locomotion studies.</td>
<td width="500">Counts Digit bodies/models; it is not merged with Cassie despite the shared vendor lineage.</td>
</tr>
<tr>
<td width="240" nowrap><a href="https://www.booster.tech/open-source/">Booster T1</a></td>
<td width="100">4</td>
<td width="280">4 Sim+Real</td>
<td width="500">Developer-oriented humanoid used for cross-embodiment learning, pretraining/finetuning, and sim-to-sim comparison.</td>
<td width="500">Counts explicit T1 use; it is not merged with unrelated N1 platform names.</td>
</tr>
<tr>
<td width="240" nowrap><a href="https://www.unitree.com/h1/">Unitree H1-2</a></td>
<td width="100">2</td>
<td width="280">2 Sim+Real</td>
<td width="500">Higher-DoF H1-family version appearing in cross-humanoid locomotion and high-dynamic imitation.</td>
<td width="500">Kept separate from H1 because the papers explicitly name H1-2.</td>
</tr>
<tr>
<td width="240" nowrap><a href="https://www.agibot.com/products/X2">AgiBot X2</a></td>
<td width="100">2</td>
<td width="280">2 Sim+Real</td>
<td width="500">Half-size biped used for whole-body VLA and cross-humanoid control; one paper uses an X2 prototype with OmniPicker grippers.</td>
<td width="500">Counts X2 bodies only; OmniPicker is counted as an end effector.</td>
</tr>
<tr>
<td width="240" nowrap>Long tail (1 paper each)</td>
<td width="100">14 items</td>
<td width="280">Mixed Sim Only / Sim+Real / Sim→Real</td>
<td width="500">Dobot Atom; Fourier N1; Noetix N1; JAXON; Rabbit; Walker2D; Berkeley Humanoid; Berkeley Humanoid Lite; ToddlerBot; Robot Era XBot-S; Robot Era XBot-L; HECTOR V2; Disney bipedal character; MIT Humanoid.</td>
<td width="500">Each normalized body/model appears in exactly one paper; similarly named N1 platforms are not merged.</td>
</tr>
</tbody>
</table>

### Named hands, wrists, and grippers used

<table width="1420">
<thead>
<tr>
<th width="260" nowrap>Normalized end effector</th>
<th width="100">Papers</th>
<th width="500">Hardware information</th>
<th width="560">Counting boundary</th>
</tr>
</thead>
<tbody>
<tr>
<td width="260" nowrap>Inspire hand family</td>
<td width="100">8</td>
<td width="500">Six-actuator dexterous hands used on modified H1, GR-1, and simulated G1 configurations.</td>
<td width="560">One paper explicitly names RH56DFX; seven say only Inspire hand(s). The family total is shown, while model-level uncertainty is retained.</td>
</tr>
<tr>
<td width="260" nowrap><a href="https://www.unitree.com/Dex3-1/">Unitree Dex3-1</a></td>
<td width="100">4</td>
<td width="500">Seven-actuator three-finger hand used for G1 manipulation, teleoperation, and visual sim-to-real.</td>
<td width="560">Counts explicit Dex3-1 only; generic 13-DoF Unitree-hand models remain in the long tail.</td>
</tr>
<tr>
<td width="260" nowrap>Long tail (1 paper each)</td>
<td width="100">7 items</td>
<td width="500">Shadow Hand; ROBOTERA XHAND; Fourier Hand; Robotiq 2F-85; OmniPicker; a 13-DoF Unitree-hand model; Damiao wrist.</td>
<td width="560">Unnamed jaw, parallel, or simple grippers are described in paper rows but are not promoted to a named-product count.</td>
</tr>
</tbody>
</table>

### Simulation and training environments used

<table width="1740">
<thead>
<tr>
<th width="250" nowrap>Normalized environment</th>
<th width="100">Papers</th>
<th width="260">Layer / developer</th>
<th width="560">Role in the surveyed papers</th>
<th width="570">Counting boundary</th>
</tr>
</thead>
<tbody>
<tr>
<td width="250" nowrap><a href="https://developer.nvidia.com/isaac-gym/download">NVIDIA Isaac Gym</a></td>
<td width="100">44</td>
<td width="260">GPU physics/RL environment; NVIDIA</td>
<td width="560">Massively parallel policy training, motion imitation, locomotion, whole-body control, and source-domain sim-to-real training.</td>
<td width="570">Includes Preview 4 and official-code-qualified use; excludes Isaac Lab and Isaac Sim.</td>
</tr>
<tr>
<td width="250" nowrap><a href="https://mujoco.org/">MuJoCo</a></td>
<td width="100">22</td>
<td width="260">General-purpose contact physics engine; Google DeepMind</td>
<td width="560">Primary biped simulation, cross-engine validation, sim-to-sim tests, and target-domain evaluation.</td>
<td width="570">Counts MuJoCo and MuJoCo Playground mentions; MJX is reported separately.</td>
</tr>
<tr>
<td width="250" nowrap><a href="https://developer.nvidia.com/isaac/lab">NVIDIA Isaac Lab</a></td>
<td width="100">6</td>
<td width="260">Robot-learning framework; NVIDIA</td>
<td width="560">Scalable RL/imitation workflows and higher-fidelity robot-learning tasks, generally on the Isaac Sim stack.</td>
<td width="570">Counted as a framework even when the same paper also names Isaac Sim; not merged into Isaac Gym.</td>
</tr>
<tr>
<td width="250" nowrap><a href="https://developer.nvidia.com/isaac/sim/">NVIDIA Isaac Sim</a></td>
<td width="100">3</td>
<td width="260">Robotics simulation/synthetic-data framework; NVIDIA</td>
<td width="560">Cross-engine target evaluation, high-fidelity simulation, and alignment against source-trained policies.</td>
<td width="570">Kept separate from Isaac Lab and legacy Isaac Gym.</td>
</tr>
<tr>
<td width="250" nowrap><a href="https://mujoco.readthedocs.io/en/latest/mjx.html">MJX</a></td>
<td width="100">2</td>
<td width="260">JAX-accelerated MuJoCo implementation; Google DeepMind</td>
<td width="560">Parallel PPO/RL execution for HumanoidBench and ToddlerBot.</td>
<td width="570">Counted only when MJX is named, not inferred from ordinary MuJoCo use.</td>
</tr>
<tr>
<td width="250" nowrap><a href="https://github.com/google/brax">Brax</a></td>
<td width="100">2</td>
<td width="260">JAX RL/training library; Google</td>
<td width="560">Fine-tuning/target simulation and accelerator-oriented RL training.</td>
<td width="570">Recorded as a training/simulation layer; not collapsed into MuJoCo or MJX.</td>
</tr>
<tr>
<td width="250" nowrap><a href="https://www.mathworks.com/products/simulink.html">MATLAB / Simulink</a></td>
<td width="100">2</td>
<td width="260">Modeling/control environment; MathWorks</td>
<td width="560">High-fidelity validation and model-based humanoid/biped control.</td>
<td width="570">Simscape Multibody and legacy SimMechanics are retained as named sublayers in the long tail.</td>
</tr>
<tr>
<td width="250" nowrap>Cassie-specific simulator</td>
<td width="100">2</td>
<td width="260">Platform-specific simulation layer</td>
<td width="560">Cassie policy training and stepping-stone locomotion evaluation.</td>
<td width="570">One row explicitly uses Cassie MuJoCo; another does not disclose the underlying physics engine, so both wrapper and engine evidence are retained.</td>
</tr>
<tr>
<td width="250" nowrap>Long tail (1 paper each)</td>
<td width="100">12 items</td>
<td width="260">Mixed engines, frameworks, and tools</td>
<td width="560">PyBullet; Gazebo; Legged Gym; Genesis; robosuite; Simscape Multibody; SimMechanics; Choreonoid; Hrpsys; GRUtopia; Agility simulator; custom multi-Cassie simulation.</td>
<td width="570">Auxiliary scene/collision tools InfiniGen, Blender, and PyVHACD are tracked separately in the relevant paper row rather than treated as the primary physics engine.</td>
</tr>
<tr>
<td width="250" nowrap>Underlying engine not disclosed</td>
<td width="100">7</td>
<td width="260">Evidence-status category</td>
<td width="560">The paper reports physics simulation or a named wrapper but does not identify the underlying engine.</td>
<td width="570">This category can overlap a named platform-specific simulator; no conventional engine is backfilled.</td>
</tr>
<tr>
<td width="250" nowrap>No physics simulation in main workflow</td>
<td width="100">8</td>
<td width="260">Evidence-status category</td>
<td width="560">Offline motion/pose work, real-only data collection, teleoperation, or real-only control.</td>
<td width="570">Supplemental simulation is still recorded in the paper row when the main method itself is real-only.</td>
</tr>
</tbody>
</table>

### Benchmarks and datasets used

Dataset counts are also non-exclusive. Source collections nested inside AMASS are reported both under AMASS and under their explicitly named source dataset, because the paper-level evidence names both layers. Dataset scale is kept in its original unit; motion hours, clips, trajectories, frames, tasks, and scenes are never added together.

<table width="1740">
<thead>
<tr>
<th width="250" nowrap>Normalized dataset / benchmark</th>
<th width="100">Papers</th>
<th width="420">Public or paper-reported scale</th>
<th width="430">Use in the surveyed papers</th>
<th width="540">Counting boundary</th>
</tr>
</thead>
<tbody>
<tr>
<td width="250" nowrap><a href="https://amass.is.tue.mpg.de/">AMASS</a></td>
<td width="100">21</td>
<td width="420">Official release: more than 40 h, more than 300 subjects, and more than 11,000 motions.</td>
<td width="430">Human-motion priors, retargeting, policy tracking, teleoperation priors, diffusion training, and out-of-distribution evaluation.</td>
<td width="540">Counts explicit AMASS mentions. Paper-specific subsets range from selected clips to about 14k retargeted sequences; the full-release scale is not substituted for a paper subset.</td>
</tr>
<tr>
<td width="250" nowrap>CMU MoCap / AMASS-CMU subset</td>
<td width="100">10</td>
<td width="420">Paper-specific subsets include 175 OOD motions, 318 locomotion sequences/3,729.18 s, 780 clips/13,383 s, or 1,919 sequences.</td>
<td width="430">Pose estimation, locomotion imitation, expressive control, evaluation, and extreme-contact motion references.</td>
<td width="540">Nested CMU-via-AMASS use can also contribute to the AMASS count; incompatible paper-specific subset sizes remain separate.</td>
</tr>
<tr>
<td width="250" nowrap><a href="https://github.com/EricGuo5513/HumanML3D">HumanML3D</a></td>
<td width="100">7</td>
<td width="420">14,616 motions and 44,970 descriptions in the official repository; two paper rows report a 14,646-motion preprocessing variant.</td>
<td width="430">Text-to-motion generation, diffusion, language-conditioned locomotion, and annotation transfer.</td>
<td width="540">The two reported motion totals are preserved rather than silently reconciled.</td>
</tr>
<tr>
<td width="250" nowrap>OMOMO</td>
<td width="100">5</td>
<td width="420">One paper reports 15 objects and about 10 h; other papers use smaller or combined subsets without restating the full scale.</td>
<td width="430">Human-object interaction, whole-body rearrangement, teleoperation, and navigation/reaching motion data.</td>
<td width="540">Counts only explicit OMOMO use; the reported subset scale remains paper-specific.</td>
</tr>
<tr>
<td width="250" nowrap>SAMP</td>
<td width="100">3</td>
<td width="420">One paper reports 100 min; another reports 30 min for a combined OMOMO+SAMP subset.</td>
<td width="430">Human-scene interaction and rearrangement motion priors.</td>
<td width="540">The combined 30-min subset is not attributed wholly to either source.</td>
</tr>
<tr>
<td width="250" nowrap>LAFAN1 / LAFAN</td>
<td width="100">3</td>
<td width="420">BFM-Zero reports 40 several-minute LAFAN1 motions; the other papers do not restate a source-wide scale.</td>
<td width="430">Locomotion regularization, recovery, and high-dynamic reference motions.</td>
<td width="540">LAFAN and LAFAN1 labels are normalized as one family while the spelling used by each paper remains in the master row.</td>
</tr>
<tr>
<td width="250" nowrap>BMLrub</td>
<td width="100">3</td>
<td width="420">AMASS source subset; absolute subset sizes are not restated by the three papers.</td>
<td width="430">Sparse-tracker pose and inverse-kinematics training.</td>
<td width="540">Can overlap AMASS; counted only when BMLrub is explicitly named.</td>
</tr>
<tr>
<td width="250" nowrap>HDM05</td>
<td width="100">2</td>
<td width="420">AMASS source subset; the two papers report a 90/10 sequence split but not the absolute count.</td>
<td width="430">Sparse egocentric and VR full-body pose estimation.</td>
<td width="540">Can overlap AMASS; counted only when HDM05 is explicitly named.</td>
</tr>
<tr>
<td width="250" nowrap>Named long tail (1 paper each)</td>
<td width="100">30 labels</td>
<td width="420">Scale is recorded in the corresponding paper row whenever disclosed.</td>
<td width="430">TokenHSI motion set; InterAct; BEHAVE; HODome; IMHD; HIMO; ScenePlan; PartNet; ScanNet; CIRCLE; KIT-ML; HumanAct12; UESTC; HPS; Humanoid Everyday; AgiBot World; HITR; MaskedMimic; MotionMillion; HDHM; cross-embodiment benchmark; ALMI-X; LEGO-H; HumanoidBench; MPI; SFU MoCap; CLONED; ADT; OmniH2O-6; DeepMimic/FLD MoCap.</td>
<td width="540">Procedural terrains, unnamed self-collected demonstrations, and unnamed simulation-generated buffers remain described in the paper rows but are not invented as named datasets.</td>
</tr>
</tbody>
</table>

### Training compute and time disclosure

<table width="1560">
<thead>
<tr>
<th width="340" nowrap>Evidence status</th>
<th width="120">Papers</th>
<th width="140">Coverage</th>
<th width="480">What is counted</th>
<th width="480">Interpretation</th>
</tr>
</thead>
<tbody>
<tr>
<td width="340" nowrap>Specific accelerator named anywhere in the pipeline</td>
<td width="120">33 / 78</td>
<td width="140">42.3%</td>
<td width="480">A named RTX/A-series/H100/V100/L40S-class GPU appears in the compute cell.</td>
<td width="480">Includes preprocessing, simulator benchmarking, or deployment hardware when that is all the paper discloses; it is not automatically a training-GPU claim.</td>
</tr>
<tr>
<td width="340" nowrap>Specific training accelerator disclosed</td>
<td width="120">29 / 78</td>
<td width="140">37.2%</td>
<td width="480">The named accelerator is explicitly tied to policy/model training, fine-tuning, or distillation.</td>
<td width="480">Excludes HumanPlus pose-processing RTX 4090, OKAMI reconstruction RTX 3090, Berkeley simulator throughput A4500, and Hand-Eye deployment RTX 4090.</td>
</tr>
<tr>
<td width="340" nowrap>Quantitative training wall-clock disclosed</td>
<td width="120">21 / 78</td>
<td width="140">26.9%</td>
<td width="480">A training, pretraining, fine-tuning, search, or policy-learning duration is reported in minutes, hours, or days.</td>
<td width="480">Data collection, controller runtime, video preprocessing, and actuator durability are not counted as training wall-clock.</td>
</tr>
<tr>
<td width="340" nowrap>GPU-hours directly reported or safely derived</td>
<td width="120">17 / 78</td>
<td width="140">21.8%</td>
<td width="480">Both accelerator count and wall-clock are available, or the paper directly reports GPU-hours/GPU-days.</td>
<td width="480">Derived values are labeled in the paper row; ranges and separate teacher/student stages remain separate.</td>
</tr>
<tr>
<td width="340" nowrap>Steps / iterations / epochs but no wall-clock</td>
<td width="120">25 / 78</td>
<td width="140">32.1%</td>
<td width="480">The paper reports a quantitative training budget but not an elapsed training time.</td>
<td width="480">These budgets are preserved as reported and are never converted to hours.</td>
</tr>
<tr>
<td width="340" nowrap>Training compute not applicable</td>
<td width="120">3 / 78</td>
<td width="140">3.8%</td>
<td width="480">The method uses no learned-model training.</td>
<td width="480">The rows report online controller/solver runtime instead: MPCC, kinodynamic fabrics, or model-based walking control.</td>
</tr>
</tbody>
</table>

### Training workflow distribution

The categories below are stage-level and non-exclusive: a single system can pretrain a teacher, distill a student, fine-tune with reinforcement learning, and then apply system identification before deployment.

<table width="1420">
<thead>
<tr>
<th width="360" nowrap>Normalized workflow stage</th>
<th width="120">Papers</th>
<th width="940">Typical pipeline in this corpus</th>
</tr>
</thead>
<tbody>
<tr>
<td width="360" nowrap>Reinforcement learning</td>
<td width="120">58</td>
<td width="940">PPO/IPPO/SAC-style motion tracking, locomotion, whole-body control, teacher policies, or task learning.</td>
</tr>
<tr>
<td width="360" nowrap>Imitation learning / behavior cloning / DAgger</td>
<td width="120">27</td>
<td width="940">Motion imitation, teacher-to-student transfer, teleoperation demonstrations, ACT/diffusion-policy behavior cloning, or online aggregation.</td>
</tr>
<tr>
<td width="360" nowrap>Fine-tuning / adaptation</td>
<td width="120">23</td>
<td width="940">Task tokens, residual/world-model adaptation, difficult-sample fine-tuning, real-data refinement, target-terrain continuation, or specialist adaptation.</td>
</tr>
<tr>
<td width="360" nowrap>Pretraining / pretrained-module reuse</td>
<td width="120">21</td>
<td width="940">Motion priors, foundation policies, latent action/motion models, privileged policies, or pretrained diffusion/VLA components precede the task stage.</td>
</tr>
<tr>
<td width="360" nowrap>Data generation / collection / retargeting</td>
<td width="120">20</td>
<td width="940">MoCap/video retargeting, simulator rollouts, trajectory optimization, teleoperation, adversarial trajectory generation, or real-to-sim collection.</td>
</tr>
<tr>
<td width="360" nowrap>Distillation / teacher-student transfer</td>
<td width="120">15</td>
<td width="940">Privileged teacher → deployable student, multi-expert → generalist, or oracle perception → onboard perception.</td>
</tr>
<tr>
<td width="360" nowrap>Domain randomization / system identification</td>
<td width="120">13</td>
<td width="940">Dynamics/contact/sensor randomization, explicit real-to-sim calibration, or learned delta-action alignment before transfer.</td>
</tr>
<tr>
<td width="360" nowrap>Supervised learning</td>
<td width="120">7</td>
<td width="940">Pose/IK predictors, autoregressive controllers, height-map perception, gait timing, or other labeled regression/classification stages.</td>
</tr>
<tr>
<td width="360" nowrap>Explicit post-training</td>
<td width="120">4</td>
<td width="940">A pretrained behavior/foundation/general policy is subsequently refined by latent adaptation, adversarial robustness training, real-data distillation, or aligned-simulator fine-tuning.</td>
</tr>
<tr>
<td width="360" nowrap>Classical optimization / no-training stage</td>
<td width="120">6</td>
<td width="940">IK refinement, GP/RRT* planning, MPCC, trajectory optimization, kinodynamic fabrics, or FROST/ALIP-MPC; three papers have no learned-model training at all.</td>
</tr>
</tbody>
</table>

<table width="3345">
<thead>
<tr>
<th width="105" nowrap>Venue/Year</th>
<th width="280">Paper/Method</th>
<th width="210">Direction/Method</th>
<th width="260">Exact Robot/Embodiment</th>
<th width="220">Simulation/Training Environment</th>
<th width="300">Benchmarks / Datasets (Scale)</th>
<th width="260">Training Compute / Time</th>
<th width="330">Training Pipeline</th>
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
<td width="300">AMASS (40 h of human motion); 6 real-world tasks, up to 40 demonstrations per task</td>
<td width="260">RTX 4090 reported for real-time pose processing; policy-training GPU count and wall-clock time not disclosed</td>
<td width="330">Reinforcement learning + imitation learning: retarget AMASS → train PPO shadowing policy in simulation → human shadowing collects demonstrations → supervised behavior cloning of task policies</td>
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
<td width="300">TokenHSI motion set: 84 sequences from AMASS, OMOMO, and SAMP; 12 HSI tasks</td>
<td width="260">4,096 environments; 50k iterations for base policies; GPU model and wall-clock time not disclosed</td>
<td width="330">Reinforcement learning + parameter-efficient adaptation: train unified PPO base skills → freeze shared policy → train new task tokenizers/heads for compositions and geometry variants</td>
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
<td width="300">InterAct subsets: OMOMO (15 objects, about 10 h; primary), plus BEHAVE, HODome, IMHD, and HIMO</td>
<td width="260">8,192 environments; GPU model and wall-clock time not disclosed</td>
<td width="330">Imitation learning + distillation + fine-tuning: train 17 subject teachers → online DAgger/behavior cloning distillation → PPO fine-tune the universal student</td>
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
<td width="300">HumanML3D (14,616 motions / 44,970 captions); AMASS for the PHC tracking prior</td>
<td width="260">DiP: 1×RTX 3090, 600k diffusion steps; tracker: 1×A100, 62k PPO epochs + 4k closed-loop fine-tuning epochs; wall-clock time not disclosed</td>
<td width="330">Pretraining + reinforcement fine-tuning: train text-motion diffusion planner → train PHC tracker on AMASS → closed-loop fine-tune planner/tracker interaction</td>
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
<td width="300">ScenePlan: 40 PartNet training objects; 40 PartNet + 10 ScanNet test scenes; 1,040 + 100 plans; SAMP (100 min) and CIRCLE motion data</td>
<td width="260">1×NVIDIA A100; 8,192 environments; wall-clock time not disclosed</td>
<td width="330">Data generation + reinforcement learning: GPT generates Chain-of-Contacts plans → PPO trains one AMP-style unified controller → execute language-produced plans</td>
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
<td width="300">HumanML3D (14,646 motions); KIT-ML (3,911 motions)</td>
<td width="260">1×RTX A5000, 29 h (29 GPU-hours, derived); 250k iterations</td>
<td width="330">Fine-tuning: initialize from pretrained MDM → jointly fine-tune motion diffusion and realism-guidance branches with spatial conditioning</td>
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
<td width="300">HumanML3D (14,646 motions / 44,970 annotations)</td>
<td width="260">1×RTX 3090; trajectory model 4.34 GPU-hours + motion model 34.7 GPU-hours (about 39.04 GPU-hours reported in total)</td>
<td width="330">From-scratch diffusion training: train trajectory DPM and motion DPM → apply dense objective/classifier guidance at sampling time; no task-specific retraining</td>
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
<td width="300">HumanML3D (14,616 motions / 44,970 descriptions); HumanAct12 (about 1,200 clips, 12 classes); UESTC (25k samples, 40 classes)</td>
<td width="260">8,192 environments; PPO projector trained for 4,000 epochs; GPU model and wall-clock time not disclosed</td>
<td width="330">Pretraining/reuse + reinforcement learning: reuse pretrained motion diffusion → train PPO motion-imitation projector on the HumanML3D/AMASS split → insert physics projections during denoising</td>
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
<td width="300">AMASS CMU, BMLrub, and MPI subsets; real-world VR MoCap test set; subset sizes not restated</td>
<td width="260">NVIDIA GeForce GTX 4090 GPU(s), as reported; count and wall-clock time not disclosed</td>
<td width="330">Supervised training: learn swivel-angle/body-shape predictors from sparse trackers → analytic biomechanical IK exactly reconstructs end-effector positions</td>
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
<td width="300">AMASS CMU/BMLrub/HDM05 (90/10 sequence split); HPS for in-the-wild testing; absolute scale not restated</td>
<td width="260">1×NVIDIA GeForce GTX 3090; training wall-clock time not disclosed</td>
<td width="330">Supervised learning: synthesize sparse/intermittent head-hand observations from AMASS → train SlowFast pose/shape estimator → stream real sensor poses at inference</td>
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
<td width="300">AMASS CMU, BMLrub, and HDM05 subsets; subset sizes not restated</td>
<td width="260">1×NVIDIA GeForce GTX 3090, about 2 h (about 2 GPU-hours, derived)</td>
<td width="330">Supervised learning + classical optimization: train Transformer pose tracker on AMASS → apply five-step inverse-kinematics hand refinement at inference</td>
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
<td width="300">Humanoid Everyday: 10,400 trajectories, over 3M frames, 260 tasks, 7 categories, 40 episodes/task at 30 Hz</td>
<td width="260">Baseline GPU models, counts, and training time not disclosed; data collection used an 11th-gen Intel i7 laptop</td>
<td width="330">Imitation learning / VLA fine-tuning: teleoperate and collect multimodal trajectories → train DP/DP3/ACT baselines or two-stage VLA fine-tuning (full dataset → category/task adaptation) → cloud real-robot evaluation</td>
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
<td width="300">About 300 h of self-collected egocentric locomotion video; AgiBot World manipulation data; 3 tasks × 50 teleoperation trajectories</td>
<td width="260">LAM/VLA: 8×H100 (30k/20k/10k steps); LMO RL: 1×H100; wall-clock time not disclosed</td>
<td width="330">Pretraining + LoRA fine-tuning + RL: pretrain locomotion/manipulation LAMs → pretrain Prismatic-7B VLA on latent labels → LoRA fine-tune on teleoperation → fixed LMO RL controller executes lower body</td>
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
<td width="300">HITR: 615 tasks (552 train / 63 test), 50 static + 34 movable objects; OMOMO + SAMP motion data (30 min total)</td>
<td width="260">Teacher: 8×Tesla V100, about 2 d (about 384 GPU-hours, derived); student: 2 GPUs, about 1 d (about 48 GPU-hours, derived; model not disclosed)</td>
<td width="330">Reinforcement learning + distillation: train privileged PPO/AMP rearrangement teacher → DAgger behavior-clone egocentric vision-language student → deploy student in simulation</td>
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
<td width="300">HumanML3D: 24,545 train episodes / 66,633 captions and 4,646 test episodes / 12,536 captions; 100 synthetic scenes, 73 object classes</td>
<td width="260">CUDA backend; GPU model/count and training time not disclosed; executor trained up to 3,000 epochs</td>
<td width="330">From-scratch executor training; no VLM fine-tuning: train conditional motion-diffusion executor on HumanML3D → off-the-shelf GPT-4o compiles structured commands → closed-loop physics execution</td>
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
<td width="300">CMU MoCap locomotion subset: 318 sequences, 3,729.18 s</td>
<td width="260">1×RTX 4090; goal policy about 10 h, recovery policy about 8 h, high-level policy under 6 h (same values in GPU-hours, derived)</td>
<td width="330">Reinforcement learning: train goal-tracking policy with adversarial human-motion alignment → train extreme-case recovery policy → freeze both and train high-level selector</td>
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
<td width="300">Five downstream tasks on pretrained MaskedMimic; about 120M frames per seed; base BFM motion-capture scale not restated</td>
<td width="260">1×A100 or V100 per seed, about 1–2 GPU-days (24–48 GPU-hours, derived); 5 seeds; 4,000 epochs / 1,024 environments</td>
<td width="330">Parameter-efficient RL adaptation: freeze pretrained MaskedMimic BFM → train about 200k-parameter task encoder with PPO → combine learned token with existing prompts</td>
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
<td width="300">LAFAN1: 40 several-minute motions for training; AMASS-CMU: 175 OOD motions + 10 selected poses for evaluation</td>
<td width="260">1,024 environments; 3M gradient steps; GPU model and wall-clock time not disclosed</td>
<td width="330">Unsupervised pretraining + optional post-training: off-policy FB-CPR with MoCap regularization and domain randomization → zero-shot prompting → CEM/trajectory optimization for few-shot latent adaptation</td>
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
<td width="300">MotionMillion: 50,378 motions; unseen MotionMillion latents used for generalization tests</td>
<td width="260">GPU model/count and training wall-clock time not disclosed</td>
<td width="330">Pretraining + reinforcement learning: learn language-aligned motion latents from MotionMillion → train retargeting-free robot policy under motion-latent guidance → MuJoCo and real-G1 transfer</td>
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
<td width="300">No named public training dataset; 1,024 × 1,000-step evaluation episodes; real fine-tuning uses 80–590 s of interaction data</td>
<td width="260">1×RTX 4090; SAC pretraining about 0.5 h after tuning (about 0.5 GPU-hours, derived); about 10 h hyperparameter search (about 10 GPU-hours, derived); real fine-tuning takes multiple wall-clock hours</td>
<td width="330">Pretraining + model-based fine-tuning: large-batch SAC pretraining → physics-informed world-model pretraining → alternate deterministic real data collection, world-model updates, and imagined SAC rollouts</td>
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
<td width="300">No named public benchmark/dataset; velocity-tracking task on Unitree G1</td>
<td width="260">RTX 4090, about 4 h and over 5k iterations; GPU count not disclosed, so GPU-hours are not computable</td>
<td width="330">Reinforcement learning from scratch: embed exact left-right equivariance/invariance into PPO actor/critic → domain-randomized simulation → zero-shot real deployment</td>
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
<td width="300">HDHM: 3,593 clips, mean 9.4 s, curated from five sources; AMASS-train/test for training and evaluation</td>
<td width="260">1×RTX 4090; hard-sample fine-tuning 6 h (6 GPU-hours, derived) versus 35 h full-data training (35 GPU-hours, derived)</td>
<td width="330">Fine-tuning: mine AMASS failures with a frozen base controller → frame-accelerate hard clips → freeze backbone and train output MLP plus residual MoE → evaluate zero-shot on HDHM</td>
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
<td width="300">No named public training dataset; perceptive-locomotion and whole-body-control task suites</td>
<td width="260">About 6k attack-policy / 10k motion-policy iterations; GPU model and wall-clock time not disclosed</td>
<td width="330">Post-training / adversarial reinforcement learning: initialize a pretrained motion policy → alternate selective attack-policy optimization and robust motion-policy updates → zero-shot real deployment</td>
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
<td width="300">Retargeted recovery MoCap + LAFAN1 locomotion data; dataset scale not disclosed</td>
<td width="260">4,096 environments; final 10k-iteration fine-tuning uses 2×RTX 4090; earlier 10k policy + 4k distillation GPU/time not disclosed</td>
<td width="330">Distillation + reinforced fine-tuning: train recovery and walking specialists → DAgger multi-behavior distillation → PPO multi-task terrain fine-tuning with behavior-specific critics</td>
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
<td width="300">Cross-embodiment benchmark: 12 simulated humanoids / 13 configurations and 7 real robot variants</td>
<td width="260">GPU model/count and training wall-clock time not disclosed</td>
<td width="330">Generalist pretraining + optional fine-tuning: generate physics-consistent randomized morphologies → train one structure-aware PPO policy → zero-shot deployment; generalist weights can initialize per-robot fine-tuning</td>
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
<td width="300">Unlabeled game-video dataset; scale not disclosed; PULSE motion prior is based on AMASS</td>
<td width="260">1,536 parallel environments; GPU model/count and wall-clock time not disclosed</td>
<td width="330">Pretraining/reuse + reinforcement learning: reuse PULSE motion prior → learn VQ interaction primitives from game videos → align video/terrain context latents → train physics policy to select primitives</td>
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
<td width="300">200 teleoperated simulation demonstrations used for reference-state initialization; no real-world training data</td>
<td width="260">Teacher: 16× NVIDIA L40S; visual student: 64× L40S; wall time not disclosed</td>
<td width="330">Pretraining + RL + imitation/distillation: pretrained HOMIE WBC → privileged PPO teacher → DAgger/BC visual student → domain randomization and system identification → zero-shot real deployment</td>
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
<td width="300">ALMI-X: &gt;80k MuJoCo trajectories, about 4 s / 200 steps each, generated from AMASS motions; CMU MoCap evaluation: 1,122 clips</td>
<td width="260">GPU model/count not disclosed; three adversarial iterations total about 17 h</td>
<td width="330">RL + supervised pretraining: adversarial lower/upper-body PPO → collect ALMI-X → train an autoregressive Transformer foundation controller by supervised learning</td>
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
<td width="300">Filtered AMASS: 8,179 trajectories in six clusters; HumanML3D supplies text annotations; 20 motions×8 real rollouts per cluster/iteration</td>
<td width="260">Two desktops, each with 1× RTX 4090 and 64 GB RAM; wall time not disclosed</td>
<td width="330">Pretraining + fine-tuning + post-training/distillation: general PPO tracker → cluster-specific experts → real-data delta-action refinement → DAgger knowledge distillation into one generalist</td>
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
<td width="300">13 high-dynamic reference motions assembled from AMASS, LAFAN, and human-video motion processing</td>
<td width="260">1× NVIDIA RTX 4090; 27 h/model = 27 GPU-hours (derived)</td>
<td width="330">RL from scratch / motion imitation: video and motion-dataset processing → IK retargeting and physical filtering → asymmetric actor-critic PPO with adaptive tracking curriculum → Sim2Real</td>
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
<td width="300">LEGO-H Humanoid Hiking Benchmark: five procedural trail families (RandomMix, Ditch, Hurdle, Gap, Forest); no external dataset</td>
<td width="260">1× NVIDIA A40; oracle policy about 18 GPU-hours; unified policy about 2 GPU-days</td>
<td width="330">RL + privileged distillation: train oracle locomotion policy with PPO → distill into vision-conditioned TC-ViTs navigation/locomotion policy with hierarchical losses</td>
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
<td width="300">CMU MoCap subset: 780 clips / 13,383 s (about 3.7 h)</td>
<td width="260">GPU model/count and wall time not disclosed; 4,096 parallel environments</td>
<td width="330">RL motion imitation: filter and retarget CMU MoCap → goal-conditioned PPO with reference-state initialization → domain randomization → zero-shot H1 deployment</td>
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
<td width="300">HumanoidBench: 27 tasks (15 manipulation + 12 locomotion), horizons 500–1,000, up to 61 actuators and 448 tactile taxels</td>
<td width="260">GPU model/count not disclosed; baselines about 48 h; MJX reaching pretraining: 2B steps/36 h (one hand), 4B/60 h (two hands)</td>
<td width="330">Benchmark training: train flat RL baselines (DreamerV3, TD-MPC2, SAC, PPO); hierarchical variant pretrains frozen MJX PPO reaching policies, then trains a high-level policy</td>
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
<td width="300">AMASS + OMOMO: &gt;15,000 clips / about 42 h; in-house MoCap: 150 clips / about 0.5 h; separate 50-clip evaluation set</td>
<td width="260">GPU model/count and wall time not disclosed</td>
<td width="330">RL + behavior cloning: offline/online MoCap → retargeted humanoid-motion corpus → unified PPO teacher with future privileged frames plus BC → real-time teleoperation</td>
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
<td width="300">No external dataset; one jumping-in-place reference animation and procedurally sampled multi-axis jump goals</td>
<td width="260">GPU model/count and wall time not disclosed; PPO stages use 6k, 12k, and 20k iterations with 65,536 samples/iteration</td>
<td width="330">RL from scratch: single-goal jump imitation → multi-goal fine-tuning → dynamics-randomized fine-tuning → zero-shot Cassie deployment</td>
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
<td width="300">No external dataset; procedural planes, steps, slopes, and stairs with a terrain/velocity curriculum</td>
<td width="260">GPU model/count and wall time not disclosed; 4,096 environments; episode length 3,000; 2 training epochs/update</td>
<td width="330">Two-phase RL: reference-gait PPO on easier terrain → remove imitation reward and continue curriculum RL on harder terrain with latent state estimation → domain randomization → Sim2Real</td>
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
<td width="300">No external dataset; HZD-generated reference gaits plus procedurally randomized terrain, dynamics, and commands</td>
<td width="260">GPU model/count and wall time not disclosed; adaptation module 2,000 iterations and PPO fine-tuning 2,000 iterations, batch 65,536</td>
<td width="330">Pretraining + supervised adaptation + RL fine-tuning: train privileged base policy → regress extrinsics from state/action history → freeze adapter and fine-tune base with PPO → zero-shot deployment</td>
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
<td width="300">Simulation-generated height-map dataset: 30,000 episodes with 848×480 depth resized to 128×128, robot state, and ground-truth local height map</td>
<td width="260">Locomotion PPO: 80 CPU cores on dual Xeon Platinum 8280; GPU/time for height-map predictor not disclosed</td>
<td width="330">RL + supervised learning: train height-map-conditioned locomotion policy → generate simulated depth/height-map episodes → supervise two-stage height-map predictor → domain-randomized zero-shot transfer</td>
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
<td width="300">42.6 s reference set: stand 5.1 s, squat walk 8.0 s, normal walk 14.2 s, run 15.3 s; sourced from CMU/SFU MoCap, manual design, and an existing controller</td>
<td width="260">1× NVIDIA RTX 3090 Ti; about 30 h = about 30 GPU-hours (derived)</td>
<td width="330">RL adversarial imitation: retarget mixed reference motions → PPO policy plus Wasserstein critic with soft-boundary loss → high-fidelity sim-to-sim evaluation</td>
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
<td width="300">Eight designed stepping-stone benchmark patterns; reachability-model data are simulation-generated, with policy learning compared at about 50M samples</td>
<td width="260">GPU model/count and wall time not disclosed</td>
<td width="330">Pretraining + RL + supervised learning: bootstrap dynamics module → fine-tune footstep policy with PPO → collect simulated touchdown data → train reachability predictor → camera-guided real deployment</td>
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
<td width="300">No external dataset; procedural one-to-three-Cassie carrier configurations, 500-step/10-s episodes; train N=1–3 and test N=2–10</td>
<td width="260">GPU model/count not disclosed; decentralized three-robot policy about 245 h to peak reward (centralized baseline about 1,000 h)</td>
<td width="330">Multi-agent RL from scratch: generate randomized carrier/command/perturbation episodes → shared decentralized IPPO policy → zero-shot transfer across robot counts/configurations</td>
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
<td width="300">Stage-II posture set: 20k randomized supine poses; Stage I uses canonical supine/prone starts and generates reference get-up trajectories</td>
<td width="260">1× RTX 4090 or L40S; 4,096 environments; Stage I about 5B simulation steps, Stage II 20k steps; wall time not disclosed</td>
<td width="330">Two-stage RL: discover get-up/roll-over trajectories under weak constraints → slow/interpolate trajectories → train strongly regularized tracking policy with full collisions and terrain randomization → Sim2Real</td>
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
<td width="300">Three 20×20 m terrain maps (2,500 points each); terrain GP starts from 500 points and receives 10 samples/step; three candidate local trajectories</td>
<td width="260">GPU model/count and training wall time not disclosed</td>
<td width="330">Classical optimization + GP learning: offline fit motion-deviation GP → online terrain-GP updates → locomotion-aware global/local RRT* planning → MuJoCo evaluation</td>
<td width="90">Sim Only</td>
<td width="300">Three 20×20 m environments (2,500 points each); 500 initial GP points + 10/step; 3 candidate trajectories/local target</td>
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
<td width="300">Not applicable: no learned benchmark or training dataset; evaluates curved-path tracking and one moving-obstacle overtaking case</td>
<td width="260">Not applicable (no learned policy); MPCC runs at 15 Hz with about 12 ms mean solve time</td>
<td width="330">No training / classical optimization: online MPCC selects speed/path-progress and footsteps → trajectory generator → low-level QP tracking</td>
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
<td width="300">No external dataset; simulation-generated episodes across Rabbit, Walker2D, and Digit, capped at 300 steps / 9 s</td>
<td width="260">GPU model/count and wall time not disclosed</td>
<td width="330">RL from scratch: train ALIP-inspired high-level PPO task-space policy → generate swing-foot/body commands → track them with model-based low-level controller</td>
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
<td width="300">No motion-prior dataset; cockpit-collected task demonstrations are used for an autonomous imitation policy, count not disclosed</td>
<td width="260">1× NVIDIA RTX 4090; 4,096 environments; about 3 h = about 3 GPU-hours (derived)</td>
<td width="330">RL from scratch + optional imitation: curriculum PPO for locomotion/squat under arbitrary upper-body poses → zero-shot deployment → cockpit demonstrations → autonomous imitation policy</td>
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
<td width="300">Hybrid AMO dataset: trajectory-optimized lower-body motions conditioned on sampled torso/locomotion commands plus AMASS arm commands; size not disclosed</td>
<td width="260">Training GPU model/count and wall time not disclosed; 4,096 environments; Jetson Orin NX runs deployment at 50 Hz</td>
<td width="330">Data generation + RL distillation + imitation: trajectory optimization → train AMO adapter → privileged teacher/student lower-body RL → optional teleoperation rollouts and ACT behavior cloning</td>
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
<td width="300">No external dataset; procedurally sampled locomotion, gait, body-pose, and upper-body intervention commands</td>
<td width="260">1× NVIDIA RTX 4090; about 16 h = about 16 GPU-hours (derived)</td>
<td width="330">RL from scratch: asymmetric actor-critic PPO over unified command space → symmetry loss and gait curriculum → upper-body intervention curriculum → zero-shot H1 deployment</td>
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
<td width="300">No external dataset; five procedural sparse-foothold terrain families over 8 curriculum levels; 15×15 local height maps</td>
<td width="260">GPU model/count and wall time not disclosed; 4,096 parallel robots</td>
<td width="330">Two-stage RL: PPO/double-critic learning on flat dynamics with task-terrain perception and soft foothold penalties → fine-tune under hard task-terrain contacts → noisy LiDAR-map Sim2Real</td>
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
<td width="300">One RGB-D human demonstration for each of six tasks; OKAMI rollouts train ACT with 50 trajectories (Sprinkle-salt) or 100 (Bagging)</td>
<td width="260">Human reconstruction: 1× RTX 3090 24 GB, about 10 min for a 10-s/30-fps video; policy-training time not disclosed</td>
<td width="330">Data generation + behavior cloning: VLM/object tracking and human reconstruction → object-aware whole-body retargeting → robot rollouts → ACT closed-loop visuomotor policy</td>
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
<td width="300">Five task/robot datasets: 10 demonstrations each for H1/GR-1 can sorting; 20 each for can insertion, folding, and unloading</td>
<td width="260">1× NVIDIA RTX 4090; ACT uses batch 45 for 25k iterations; wall time not disclosed</td>
<td width="330">Imitation learning: immersive stereo teleoperation → collect real demonstrations → fine-tune DINOv2 visual features within ACT → real closed-loop evaluation</td>
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
<td width="300">No external dataset; procedurally generated contact-stage/task-goal episodes for four humanoid tasks plus one 22-DoF dinosaur task</td>
<td width="260">GPU model/count, parallel-environment count, and wall time not disclosed</td>
<td width="330">RL from scratch: decompose task into sequential contact stages → task-agnostic curiosity/contact rewards → PPO without randomization → continue with domain randomization and regularization → Sim2Real</td>
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
<td width="300">AMASS-derived human-motion data; exact training subset/scale not disclosed; tabletop evaluation uses 20 trajectories (about 30 min)</td>
<td width="260">GPU and training wall time not disclosed</td>
<td width="330">Pretraining + RL: retarget human motions → train CVAE predictive motion prior → PPO lower-body policy; IK/retargeted upper-body control → real deployment</td>
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
<td width="300">HumanML3D text-motion dataset; exact retargeted training subset/scale not disclosed</td>
<td width="260">GPU and wall time not disclosed; student uses 1,024 environments, an about-500k state-action buffer, and reports results at 10k iterations</td>
<td width="330">RL + distillation: retarget MoCap → PPO motion-tracking teacher → DAgger/behavior-cloned CLIP-conditioned CVAE student → zero-shot real deployment</td>
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
<td width="300">43 video-derived motions for simulation evaluation; real post-training uses 100 motion clips plus 10 min of locomotion data (full 23-DoF delta model estimated to need &gt;400 clips)</td>
<td width="260">GPU and training wall time not disclosed</td>
<td width="330">Pretraining + post-training/fine-tuning: video → TRAM reconstruction/retargeting → PPO tracking policy → real rollouts → delta-action model → aligned-simulator fine-tuning → deploy without delta model</td>
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
<td width="300">Real position-only and multi-expert demonstrations; exact trajectory count/duration not disclosed; three contact-rich tasks used for quantitative evaluation</td>
<td width="260">GPU and training wall time not disclosed</td>
<td width="330">Imitation pretraining + fine-tuning: pretrain transformer trunk/position expert on position-only data → unfreeze all heads → behavior-clone smaller multi-expert demonstrations with soft MoE routing</td>
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
<td width="300">CMU MoCap: 1,919 sequences; D50 and D250 subsets used in data-curation ablations</td>
<td width="260">GPU and training wall time not disclosed</td>
<td width="330">RL + distillation + fine-tuning: retarget MoCap → PPO teacher/base policy → filter infeasible motions → generalist policy → DAgger student → task-specialist fine-tuning</td>
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
<td width="300">10k neural-policy trajectories × 10 s; two 10k model-controller sets × 10 s; about 1k KIT/AMASS MoCap trajectories; YouTube-video count not disclosed</td>
<td width="260">GPU and training wall time not disclosed</td>
<td width="330">Training from scratch (offline autoregressive modeling): collect/retarget mixed sensorimotor trajectories → mask missing modalities → jointly train causal transformer by next-token prediction → zero-shot real rollout</td>
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
<td width="300">No named external dataset; procedural terrain evaluations cover slopes, stairs, snow, and uneven/deformable ground; training-sample count not disclosed</td>
<td width="260">GPU and wall time not disclosed; 12,288 environments, 2 learning epochs/update, 2,400-step episodes</td>
<td width="330">Training from scratch (RL): asymmetric PPO actor-critic + GRU denoising world model/state reconstruction + domain randomization → zero-shot real deployment</td>
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
<td width="300">No named public dataset; evaluation reports 15 simulations totaling 600 s plus real discrete-terrain trials</td>
<td width="260">Training hardware and wall time not disclosed</td>
<td width="330">Supervised learning + classical optimization: generate variable-frequency gait examples → train lightweight Gait-Net for step duration → embed predictions in sequential-convex kinodynamic MPC</td>
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
<td width="300">No motion-prior dataset; 10 procedurally generated terrain/obstacle types; four hardest tasks receive real-world success-rate evaluation</td>
<td width="260">DAgger vision distillation uses 4× RTX 3090; wall time not disclosed</td>
<td width="330">Training from scratch + distillation: fractal-terrain gait pretraining → privileged oracle parkour RL/curriculum → 4-GPU DAgger distillation of depth student → zero-shot real deployment</td>
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
<td width="300">No named external dataset; synthetic ground-truth terrain-height observations; evaluated on H1 and GR-1 across indoor/outdoor terrain and sensor setups</td>
<td width="260">1× RTX 4090 for about 3 h (derived: about 3 GPU-hours)</td>
<td width="330">Training from scratch (single-stage RL): ground-truth elevation observations → HIM/PPO perceptive policy with domain randomization → LiDAR elevation-map inference → zero-shot deployment</td>
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
<td width="300">No named external dataset; procedurally randomized locomotion terrain and hardware walking/hopping tests</td>
<td width="260">NVIDIA RTX A4500 simulator benchmark exceeds 90k steps/s; actual training GPU allocation and wall time not disclosed</td>
<td width="330">Training from scratch (RL): minimalist PPO locomotion policy + light dynamics/contact randomization → zero-shot real transfer</td>
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
<td width="300">No training dataset; simulation/real task suite covers obstacle avoidance, box carrying/throwing, and walking</td>
<td width="260">Not applicable (no learned-model training); controller runtime is 0.81–1.06 ms/iteration</td>
<td width="330">No training / classical optimization: specify task fabrics → compose priorities → solve desired joint accelerations online → execute whole-body controller</td>
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
<td width="300">No learning dataset; three offline nominal trajectories cover level, uphill, and downhill conditions; hardware includes constrained footholds and a moving walkway</td>
<td width="260">Not applicable (no learned-model training); MPC runtime is &lt;500 μs and lateral foot placement &lt;5 μs</td>
<td width="330">No training / classical optimization: generate FROST full-order trajectories offline → variable-height ALIP-MPC + virtual constraints/ankle torque → real-time hardware control</td>
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
<td width="300">Retargeted/augmented AMASS: about 14k sequences; OmniH2O-6: six tasks, 40 min of 30-Hz teleoperated RGB-D/control data</td>
<td width="260">Training GPU and wall time not disclosed</td>
<td width="330">RL + distillation + imitation learning: train privileged motion imitator on AMASS → DAgger sparse-state student → real teleoperation/data collection → diffusion-policy LfD for autonomous tasks</td>
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
<td width="300">AMASS: 40 h / about 13k source motions → about 10k retargeted → about 8.5k embodiment-feasible sequences after sim-to-data filtering</td>
<td width="260">GPU and training wall time not disclosed</td>
<td width="330">RL: fit/retarget AMASS → PPO privileged imitator filters infeasible sequences → train robust goal-conditioned PPO policy with domain randomization → zero-shot real teleoperation</td>
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
<td width="300">Retargeted feasible AMASS subset Q̂; exact sequence count not disclosed; 20 standing sequences used for real tracking evaluation</td>
<td width="260">GPU and training wall time not disclosed</td>
<td width="330">RL + distillation: retarget/filter AMASS → PPO oracle full-motion imitator → DAgger student with mode/sparsity masks → zero-shot multi-mode real controller</td>
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
<td width="300">No external dataset; four simulated terrain families (ground, platform, wall, slope); 1,250 evaluation episodes per terrain/policy</td>
<td width="260">GPU and wall time not disclosed; 4,096 environments, 500-step rollouts, 50 steps/environment per iteration</td>
<td width="330">Training from scratch (RL): multi-critic PPO + vertical-force exploration curriculum + action-bound curriculum/smoothness regularization + domain randomization → direct real transfer</td>
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
<td width="300">Six video-derived balance motions (Deep Squat, Ne Zha, Swallow Balance, Bruce Lee’s Kick, Single-Leg Stand, High Knees); clip count/duration not disclosed</td>
<td width="260">GPU and training wall time not disclosed</td>
<td width="330">RL + distillation: video → WHAM/SMPL retargeting and reference refinement → balance-aware PPO teacher → DAgger student → robustness training → zero-shot real deployment</td>
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
<td width="300">Low-level: AMASS+OMOMO, 1,363 clips / about 5 h; navigation: ADT 400 min, 200 human clips/room (about 4 s each), and 24 lab-robot training clips (about 30 s each)</td>
<td width="260">Training GPU/time not disclosed; whole-body configurations train 50k epochs; RTX 4090 is reported for deployment, not training</td>
<td width="330">Mixed modular training: single-stage adversarial imitation RL low-level controller + DINO/transformer navigation trained on human/robot/ADT data + model-based reaching → integrated real deployment</td>
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
<td width="300">CLONED: 345 motions, built from 149 curated AMASS sequences, 14 custom MoCap sequences, motion editing, and procedural 6-D wrist-target augmentation</td>
<td width="260">Teacher: 1× A800, about 24 h (derived: about 24 GPU-hours); student: 1× RTX 3090 Ti, about 48 h (derived: about 48 GPU-hours)</td>
<td width="330">RL + distillation: PPO privileged teacher (8,192 envs / 1M iterations) → DAgger MoE student (4,096 envs / 600k iterations) → LiDAR-odometry closed-loop deployment</td>
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
<td width="300">Three-task benchmark (grasp-and-reach, box lift, bimanual handover); 10-object ablation; &lt;30 s task-aware initialization data/task and &lt;4 min real-to-sim calibration</td>
<td width="260">GPU and training wall time not disclosed</td>
<td width="330">RL + distillation: automated real-to-sim tuning → task-specialist PPO with contact/object rewards → filter successful rollouts → distill task generalist with diffusion policy → visual sim-to-real transfer</td>
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
<td width="300">Extreme-action set: five references spanning three motion types—CMU get-up, KIT crawling, and three internet-video dance/martial-arts motions</td>
<td width="260">1× RTX 4090D, about 72 h, 4,096 robots (derived: about 72 GPU-hours)</td>
<td width="330">Training from scratch (RL): retarget AMASS/internet motions → transformer command encoder + multi-critic PPO/advantage mixing → domain randomization → zero-shot full-body-contact deployment</td>
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
<td width="300">No named learning benchmark; locomotion policy plus actuator/arm evaluations, including a 60-h actuator durability test (not training time)</td>
<td width="260">GPU and training wall time not disclosed</td>
<td width="330">Training from scratch (RL): PPO locomotion with domain randomization → zero-shot hardware transfer; separate SteamVR/Pink IK teleoperation is non-learning</td>
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
<td width="300">Two manipulation tasks use 60 demonstrations each (about 20 min collection); walking uses 3×10^8 simulated timesteps</td>
<td width="260">GPU and wall time not disclosed; PPO uses 1,024 environments / 3×10^8 timesteps; diffusion policy has 100 training diffusion steps</td>
<td width="330">System identification → PPO walking policy for zero-shot transfer; teleoperated leader-follower demonstrations → RGB diffusion policy → chain manipulation and locomotion skills</td>
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
<td width="300">Artist-authored references: one standing policy, one walking policy, and several single-motion episodic policies; exact clip count/duration not disclosed</td>
<td width="260">Per policy: 1× RTX 4090 for about 2 days / 100k iterations / 8,192×24 samples per iteration (derived: about 48 GPU-hours)</td>
<td width="330">Training from scratch (RL): author animation/reference motions → separate PPO standing, walking, and episodic policies → freeze weights → animation engine blends policies and artist commands</td>
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
<td width="300">DeepMimic/FLD MoCap: 13 motions × 10 trajectories × 240 steps</td>
<td width="260">GPU and wall time not disclosed; SCAE 5k iterations, PPO policy up to 3k iterations / 4,096 environments, BMI fine-tuning 50 iterations</td>
<td width="330">Pretraining + bi-level fine-tuning: train SCAE latent dynamics → PPO motion policy → alternate decoder/reference optimization with policy optimization → simulation evaluation</td>
<td width="90">Sim Only</td>
<td width="300">18-D actions; 13 motions; policy 50 Hz; 4,096 envs; up to 3,000 iterations; simulation only</td>
<td width="330">Automatically modifies physically infeasible motion references to improve executable imitation</td>
<td width="330">Simulation-only, computationally heavy bi-level optimization, and limited motion coverage</td>
<td width="330">Online feasible retargeting, larger motion libraries, and real-hardware validation</td>
</tr>
</tbody>
</table>

## Distilled Humanoid Research Directions

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
