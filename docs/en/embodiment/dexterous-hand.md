# dexterous hand

[Home](../../../README.md) | [中文](../../zh-CN/embodiment/dexterous-hand.md) | [Direction index](README.md)

Total: 28 papers.

The direction-specific columns below separate exact hardware, skill/contact mode, tactile sensing, action/control, simulation and data scale, transfer path, human-data chain, and reported metrics. “Not disclosed” means the checked paper/project sources do not state the item; simulated contact labels are not counted as tactile hardware.

<table width="3380">
<thead>
<tr>
<th width="100" nowrap>Venue</th>
<th width="260">Paper</th>
<th width="230">Research Problem</th>
<th width="230">Solved / Progress</th>
<th width="240">Open Limitation</th>
<th width="280">Exact Hand / Arm / Carrier</th>
<th width="160">DoF / Actuation</th>
<th width="220">Skill / Contact Mode</th>
<th width="180">Tactile Setup</th>
<th width="210">Action Space / Control Rate</th>
<th width="330">Simulation / Training Environment + Data Scale</th>
<th width="240">Sim2Real / Retargeting Path</th>
<th width="220">Teleop / Human Data Chain</th>
<th width="300">Core Metric</th>
<th width="180">Resources</th>
</tr>
</thead>
<tbody>
<tr>
<td width="100" nowrap>CoRL 2023</td>
<td width="260"><a href="https://arxiv.org/abs/2309.09979">General In-hand Object Rotation with Vision and Touch</a></td>
<td width="230">Generalize fingertip in-hand rotation across object shapes and commanded axes.</td>
<td width="230">RotateIt combines vision, low-dimensional touch, and proprioception in a distilled closed-loop policy that transfers directly to hardware.</td>
<td width="240">Uses discretized contact locations rather than full tactile images; objects must fit the hand and the frozen policy cannot learn from deployment.</td>
<td width="280">Allegro Hand; Intel RealSense D435; four fingertip omnidirectional vision-based touch sensors</td>
<td width="160">16 hand joints; position controlled</td>
<td width="220">Continuous fingertip in-hand rotation about x/y/z axes; multi-contact finger gaiting</td>
<td width="180">Four optical fingertip sensors; policy uses 8-bin contact locations, not raw tactile images</td>
<td width="210">16-D joint targets at 20 Hz; PD torque loop at 300 Hz</td>
<td width="330">Isaac Gym; objects curated from EGAD, Google Scanned Objects, YCB, and ContactDB; 15 held-out OOD objects; no human demonstrations</td>
<td width="240">Privileged PPO oracle → visuotactile Transformer distillation with domain/randomized depth → direct real deployment</td>
<td width="220">None</td>
<td width="300">Real x-axis ContactLoc rotation reward 102.36 vs 79.37 without touch; OOD reward drop 15.4% vs 41.6% for proprioception-only</td>
<td width="180"><a href="https://arxiv.org/abs/2309.09979">paper</a> / <a href="https://haozhi.io/rotateit/">project</a> / <a href="https://proceedings.mlr.press/v229/qi23a.html">PMLR</a></td>
</tr>
<tr>
<td width="100" nowrap>CVPR 2025</td>
<td width="260"><a href="https://openaccess.thecvf.com/content/CVPR2025/html/Li_ManipTrans_Efficient_Dexterous_Bimanual_Manipulation_Transfer_via_Residual_Learning_CVPR_2025_paper.html">ManipTrans: Efficient Dexterous Bimanual Manipulation Transfer via Residual Learning</a></td>
<td width="230">Transfer long, contact-rich human single- and bimanual manipulation trajectories to heterogeneous robot hands.</td>
<td width="230">Separates morphology-level imitation from contact-aware residual RL and builds DexManipNet.</td>
<td width="240">Deformable/oversized MoCap is excluded; real deployment is qualitative trajectory replay, without quantified closed-loop tactile control.</td>
<td width="280">Sim: bimanual Shadow, MANO, Inspire, Allegro. Real: two 7-DoF RealMan arms + two upgraded Inspire Hands</td>
<td width="160">Sim hands: 22/22/12/16 DoF; real Inspire: 6 DoF each</td>
<td width="220">Pen capping, bottle unscrewing, articulated-object and coordinated bimanual manipulation; contact-force residual refinement</td>
<td width="180">Sim fingertip contact forces; real Inspire hands include tactile sensors, but closed-loop use is not reported</td>
<td width="210">Per hand: K joint PD targets + 6-D wrist force; Isaac Gym step 1/60 s</td>
<td width="330">Isaac Gym, 4,096 parallel environments; DexManipNet: 61 tasks, 3.3K episodes, 1.2K objects, 1.34M frames, including about 600 bimanual sequences</td>
<td width="240">MoCap → hand-trajectory imitation → object/contact residual RL; 12-DoF simulated Inspire is fitted to 6-DoF real Inspire for replay</td>
<td width="220">OakInk-V2 optical MoCap; FAOVR VR/HITL; GRAB and ARCTIC sequences</td>
<td width="300">Single/bimanual transfer SR 58.1/39.5% vs 47.8/13.9% for Retarget+Residual; real-robot evidence is qualitative</td>
<td width="180"><a href="https://openaccess.thecvf.com/content/CVPR2025/papers/Li_ManipTrans_Efficient_Dexterous_Bimanual_Manipulation_Transfer_via_Residual_Learning_CVPR_2025_paper.pdf">paper</a> / <a href="https://openaccess.thecvf.com/content/CVPR2025/html/Li_ManipTrans_Efficient_Dexterous_Bimanual_Manipulation_Transfer_via_Residual_Learning_CVPR_2025_paper.html">CVF</a></td>
</tr>
<tr>
<td width="100" nowrap>ICCV 2025</td>
<td width="260"><a href="https://openaccess.thecvf.com/content/ICCV2025/html/He_DexVLG_Dexterous_Vision-Language-Grasp_Model_at_Scale_ICCV_2025_paper.html">DexVLG: Dexterous Vision-Language-Grasp Model at Scale</a></td>
<td width="230">Generate instruction-aligned, part-aware dexterous grasps from one RGB-D view.</td>
<td width="230">Trains a VLM plus flow-matching pose head on DexGraspNet 3.0 and executes semantic grasps on hardware.</td>
<td width="240">Floating-hand training ignores arm workspace; unsafe samples require filtering and the model lacks an effective pose-ranking mechanism.</td>
<td width="280">ShadowHand on UR10e; wrist-mounted Intel RealSense D415</td>
<td width="160">22 hand joint angles + 6-D wrist pose</td>
<td width="220">Static functional grasp pose; part-, style-, and optional finger-contact-mode conditioned lifting</td>
<td width="180">None; contact modes are synthetic labels, not tactile sensing</td>
<td width="210">Grasp g = translation + SO(3) rotation + 22 joint angles; motion-planned execution; rate not disclosed</td>
<td width="330">DexGraspNet 3.0: 170M pose-caption pairs across 174K Objaverse objects; Isaac Gym validation; Blender D415 rendering; 230 epochs on 64 RTX 4090 GPUs</td>
<td width="240">Synthetic pose learning → single-view colored point cloud inference → safety filtering and motion planning on the real UR10e</td>
<td width="220">No human demonstrations; SAMesh and GPT-4o generate part semantics/captions</td>
<td width="300">Sim success seen/unseen/SamPart3D: 87.7/79.1/76.3%; real simple objects: 80% success and 75% part accuracy, trial count not stated</td>
<td width="180"><a href="https://arxiv.org/pdf/2507.02747">paper</a> / <a href="https://jiaweihe.com/dexvlg">project</a> / <a href="https://openaccess.thecvf.com/content/ICCV2025/html/He_DexVLG_Dexterous_Vision-Language-Grasp_Model_at_Scale_ICCV_2025_paper.html">CVF</a></td>
</tr>
<tr>
<td width="100" nowrap>ICCV 2025</td>
<td width="260"><a href="https://openaccess.thecvf.com/content/ICCV2025/html/Wang_DexH2R_A_Benchmark_for_Dynamic_Dexterous_Grasping_in_Human-to-Robot_Handover_ICCV_2025_paper.html">DexH2R: A Benchmark for Dynamic Dexterous Grasping in Human-to-Robot Handover</a></td>
<td width="230">Generate safe receiver-hand approach trajectories for dynamic human-to-robot handover.</td>
<td width="230">Provides a real multimodal handover benchmark and compares autoregressive, 2-D diffusion, and 3-D diffusion approaches.</td>
<td width="240">This is one robot arm/right hand receiving from a human, not robot bimanual manipulation; hard-mode success and safety remain low.</td>
<td width="280">UR10e + right ShadowHand; 12 external RGB cameras, four Azure Kinects, two wrist RealSense D455 cameras</td>
<td width="160">Hardware 24 DoF; modeled state uses 22 joints + global SE(3)</td>
<td width="220">Moving-object receiver grasp; goal-pose preparation, reactive approach, and final alignment</td>
<td width="180">None reported</td>
<td width="210">Predicts future sequences of global SE(3) + 22-D articulation states; control frequency not disclosed</td>
<td width="330">4,282 real handovers / 456K frames, 39 people, 56 objects; split 2,888/591/803; DexGraspNet pretraining and Isaac Gym stability screening</td>
<td width="240">Synthetic grasp pretraining + Isaac stability filter → real-data fine-tuning → real receiver execution</td>
<td width="220">&lt;50 ms glove teleoperation captures robot receiver motion; human giver remains external</td>
<td width="300">Easy MotionNet/DP3 success 71.1/66.3%; Hard 26.6/27.1%, with safety 15.4/33.7%</td>
<td width="180"><a href="https://openaccess.thecvf.com/content/ICCV2025/html/Wang_DexH2R_A_Benchmark_for_Dynamic_Dexterous_Grasping_in_Human-to-Robot_Handover_ICCV_2025_paper.html">paper</a> / <a href="https://dexh2r.github.io/">project</a> / <a href="https://github.com/4DVLab/DexH2R">code</a></td>
</tr>
<tr>
<td width="100" nowrap>IROS 2026</td>
<td width="260"><a href="https://arxiv.org/abs/2606.24450">NoContactNoWorries: Estimating Contact through Vision and Proprioception for In-Hand Dexterous Manipulation</a></td>
<td width="230">Recover fingertip contact without tactile hardware under wrist-camera self-occlusion.</td>
<td width="230">Predicts four binary contact states from RGB-D plus actual/commanded joints and substitutes them for oracle touch in closed-loop rotation.</td>
<td width="240">Only fixed fingertip binary contacts are modeled—no dense map, slip, force distribution, or task-general contact representation.</td>
<td width="280">LEAP Hand + wrist-mounted Intel RealSense D455; thin FSRs used only to score hardware predictions</td>
<td width="160">16-D hand state/command</td>
<td width="220">In-hand rotation with predicted fingertip contact; multi-contact closed-loop control</td>
<td width="180">Four FSRs provide ground truth only and are removed during policy inference/deployment</td>
<td width="210">Relative joint targets at 20 Hz; RGB-D at 30 Hz; compiled predictor latency 8 ms</td>
<td width="330">Isaac Gym/PhysX; five training geometries × 50 rollouts × 15 s × 30 Hz ≈ 22.5K labeled frames; physics/perception randomization</td>
<td width="240">PhysX binary contact supervision → visuo-proprioceptive predictor → direct real policy using pseudo-touch</td>
<td width="220">None</td>
<td width="300">Real F1 0.71–0.84 on seen objects and 0.80/0.74 on novel objects; under occlusion Full 0.85 vs vision-only 0.51</td>
<td width="180"><a href="https://arxiv.org/abs/2606.24450">paper</a> / <a href="https://soham2560.github.io/no-contact-no-worries/">project</a></td>
</tr>
<tr>
<td width="100" nowrap>ICLR 2026</td>
<td width="260"><a href="https://openreview.net/forum?id=Bf4FeuW0Mr">DemoGrasp: Universal Dexterous Grasping from a Single Demonstration</a></td>
<td width="230">Learn universal closed-loop dexterous grasping from one successful seed trajectory.</td>
<td width="230">Edits wrist and finger actions in a compact one-step RL problem, then distills successful rollouts to vision policies.</td>
<td width="240">The single edit is fixed for an episode, limiting recovery from large execution errors despite some vision-policy regrasp behavior.</td>
<td width="280">Sim: Shadow, Inspire, SVH, Allegro, DClaw, Panda gripper. Real: 7-DoF FR3 + Inspire + two RealSense D435i</td>
<td width="160">Real Inspire: 6 active + 6 passive joints</td>
<td width="220">Tabletop grasp/lift, including small and thin objects; occasional finger-table contact is allowed</td>
<td width="180">None reported</td>
<td width="210">RL edit = wrist SE(3) transform + hand-joint deltas; low-level 60 Hz, vision policy 3 Hz</td>
<td width="330">Isaac Gym; one seed trajectory; trained on 3,200 DexGraspNet objects or 175 cross-dataset objects; 35K successful rollouts for sampling/BC comparison</td>
<td width="240">Single sim demonstration → RL trajectory editor → rendered successful rollouts → flow-matching vision policy → real FR3</td>
<td width="220">Seed may be teleoperated or scripted; core real policy does not require a large human dataset</td>
<td width="300">Vision success 90.1% on unseen categories; real 110 unseen objects 86.5% overall (95.3% normal, 71.1% small/thin)</td>
<td width="180"><a href="https://openreview.net/forum?id=Bf4FeuW0Mr">paper</a> / <a href="https://beingbeyond.github.io/DemoGrasp/">project</a> / <a href="https://github.com/BeingBeyond/DemoGrasp">code</a></td>
</tr>
<tr>
<td width="100" nowrap>ICLR 2026</td>
<td width="260"><a href="https://openreview.net/forum?id=80vjyj5o7l">DexNDM: Closing the Reality Gap for Dexterous In-Hand Rotation via Joint-Wise Neural Dynamics Model</a></td>
<td width="230">Close the interaction-dynamics gap for generalized in-air rotation across objects, axes, and wrist poses.</td>
<td width="230">Learns joint-wise real dynamics from autonomous loaded interactions and trains a residual compensator over a sim policy.</td>
<td width="240">Still needs substantial real transition collection; the dynamics model omits object shape and tactile feedback.</td>
<td width="280">7-DoF Franka arm + LEAP Hand; Chaos Box loaded-interaction rig</td>
<td width="160">LEAP 16 DoF; position controlled</td>
<td width="220">Unsupported in-air rotation over multiple axes and wrist orientations; rapidly changing whole-hand contacts</td>
<td width="180">None; tactile integration is future work</td>
<td width="210">16-D relative joint targets at 20 Hz</td>
<td width="330">Isaac Gym PPO teacher and BC policy; 24K real Chaos Box transition trajectories; Genesis/MuJoCo cross-simulator tests</td>
<td width="240">Sim policy → autonomous real loaded transitions → joint-wise neural dynamics → residual policy → real deployment</td>
<td width="220">Core rotation pipeline is autonomous; Meta Quest 3 arm teleoperation only demonstrates a downstream application</td>
<td width="300">Representative real x/y/z rotation: 6.35/11.32/8.61 rad; cross-simulator tests expose residual domain sensitivity</td>
<td width="180"><a href="https://arxiv.org/abs/2510.08556">paper</a> / <a href="https://meowuu7.github.io/DexNDM/">project</a></td>
</tr>
<tr>
<td width="100" nowrap>ICLR 2026</td>
<td width="260"><a href="https://openreview.net/forum?id=Kt9tJeOwjy">RFS: Reinforcement learning with Residual flow steering for dexterous manipulation</a></td>
<td width="230">Fine-tune multimodal flow policies without destroying pretrained behaviors.</td>
<td width="230">Combines latent flow steering for global mode changes with bounded residual actions for local correction.</td>
<td width="240">Still requires simulation pretraining and real corrective demonstrations; unseen-object success remains below seen-object performance.</td>
<td width="280">7-DoF Franka arm + LEAP Hand under Cartesian impedance control</td>
<td width="160">Hand DoF not stated in the checked paper</td>
<td width="220">Six sim tasks; real grasp and pick-place with contact-sensitive finger adjustment</td>
<td width="180">No real tactile hardware; sim observation includes binary fingertip contact</td>
<td width="210">10 Hz; residual bounded to 1.5 cm Cartesian translation and 0.05 rad finger motion</td>
<td width="330">Isaac Lab; six tasks with about 400 Vision Pro demos/task; 1,000 sim distillation demos for each real task; 50 real SpaceMouse corrections</td>
<td width="240">State RL in Isaac Lab → point-cloud policy distillation/randomization → zero-shot real → offline residual/flow correction</td>
<td width="220">Vision Pro teleoperation; SpaceMouse provides bounded corrective interventions</td>
<td width="300">Sim average 0.87; real seen grasp/pick-place 90/80%, unseen 70/74%; zero-shot baselines 40/30% on unseen</td>
<td width="180"><a href="https://arxiv.org/abs/2602.01789">paper</a> / <a href="https://weirdlabuw.github.io/rfs/">project</a></td>
</tr>
<tr>
<td width="100" nowrap>ICLR 2026</td>
<td width="260"><a href="https://openreview.net/forum?id=NZDaMcpXZm">Learning to Grasp Anything By Playing with Random Toys</a></td>
<td width="230">Acquire object-general tabletop grasping from a small vocabulary of randomly assembled primitive toys.</td>
<td width="230">LEGO uses detection pooling to learn object-centric features and transfers from toy data to YCB/everyday objects on gripper and humanoid hands.</td>
<td width="240">Still requires embodiment-specific demonstrations; H1-2 success is about 51%, and hardware issues affected some Inspire thumb joints.</td>
<td width="280">Sim: Franka + gripper. Real: Panda + Robotiq 2F-85; Unitree H1-2 left 7-DoF arm + Inspire RH56DFTP</td>
<td width="160">Franka 7+1; Inspire 6 active DoF / 12 linked joints</td>
<td width="220">Tabletop grasp-and-lift; zero-shot object generalization from spheres/cuboids/cylinders/rings</td>
<td width="180">Inspire has pressure sensors, but LEGO does not use tactile input</td>
<td width="210">Absolute joint/state actions: Franka 8-D, H1-2 40-D; 16-step history → 16-action chunk; rate not disclosed</td>
<td width="330">ManiSkill/SAPIEN: 2,500 sim demonstrations from 250 toys; real: 1,500 Franka demos and 500 H1-2 demos</td>
<td width="240">Toy-domain behavior cloning with object masks → direct embodiment-specific real training/evaluation; no sim-to-real policy transfer to H1-2</td>
<td width="220">ManiSkill scripted/teleop data; Meta Quest 3 for Franka; Apple Vision Pro + Unitree XR Teleoperate for H1-2</td>
<td width="300">Sim YCB 80%; real Franka 66.67%; real H1-2 50.77% over 13 objects (five trials/object)</td>
<td width="180"><a href="https://arxiv.org/abs/2510.12866">paper</a> / <a href="https://lego-grasp.github.io/">project</a></td>
</tr>
<tr>
<td width="100" nowrap>ICLR 2026</td>
<td width="260"><a href="https://openreview.net/forum?id=cVX3VqO8BO">UniHM: Unified Dexterous Hand Manipulation with Vision Language Model</a></td>
<td width="230">Generate open-vocabulary, multi-step hand-object interaction across hand morphologies.</td>
<td width="230">Learns a shared discrete action codebook and refines decoded trajectories with object-centric physical constraints.</td>
<td width="240">Uses RGB-D without tactile/force sensing; contact modeling is simplified and every new hand still needs a morphology-specific encoder/decoder.</td>
<td width="280">Retargets Shadow, Allegro, SVH, LEAP, Panda (Ability in appendix); real 7-DoF Franka + Panda/XHand/Inspire + ZED</td>
<td width="160">Real hands: Panda 2, XHand 12, Inspire 6 DoF</td>
<td width="220">Open-vocabulary grasp, pick-place, pull-push, and open-close interaction sequences</td>
<td width="180">None; contact comes from geometry/collision constraints</td>
<td width="210">8,192-entry VQ codebook → hand-specific joint trajectory → Gauss-Newton refinement; rate not disclosed</td>
<td width="330">DexYCB 582K frames and OakInk-Image 230K frames; 80/20 seen/unseen split; SAPIEN is used only to visualize/validate generated sequences</td>
<td width="240">Human HOI → shared hand tokens → morphology decoder/retargeting → object-trajectory conditioning and physical refinement → real execution</td>
<td width="220">Offline DexYCB/OakInk human interaction data; no large real-robot teleoperation set</td>
<td width="300">Real seen success grasp/pick-place/pull-push/open-close 65/50/60/55%; unseen 60/35/55/45%</td>
<td width="180"><a href="https://arxiv.org/abs/2603.00732">paper</a> / <a href="https://unihm.github.io/">project</a> / <a href="https://github.com/Zhenhao-Zhang/UniHM">code</a></td>
</tr>
<tr>
<td width="100" nowrap>ICLR 2026</td>
<td width="260"><a href="https://openreview.net/forum?id=k8ovuXEQQu">House Of Dextra: Cross-Embodied Co-Design for Dexterous Hands</a></td>
<td width="230">Jointly search hand morphology and control without making each candidate prohibitively expensive.</td>
<td width="230">Uses graph-grammar design search and a morphology-conditioned PPO policy, then fabricates four modular hands for zero-shot real deployment.</td>
<td width="240">Blind proprioception-only control limits object-state estimation; morphology search remains task-family specific and the simulator is not named.</td>
<td width="280">Generated fixed-wrist modular hands; LEAP baseline; four real 3D-printed hands using Dynamixel XL330-M288-T servos</td>
<td width="160">3–5 fingers; 2–3 actuated joints / 3–4 servos per finger</td>
<td width="220">Blind in-hand rotation; sim-only grasping and object flipping; encoder-resistance contact effects are implicit</td>
<td width="180">None; no camera or tactile feedback</td>
<td width="210">Masked joint-position commands; closed-loop proprioception; control rate not disclosed</td>
<td width="330">Simulator not disclosed; 2,000–8,000 generated morphologies, 50×40 search evaluations, 2,048 parallel randomized environments; PPO</td>
<td width="240">Cross-embodiment co-search → domain-randomized blind policy → programmatic fabrication → PID tuning → zero-shot real</td>
<td width="220">None</td>
<td width="300">Optimal 3-finger hand rotates 15/17 unseen objects; anthropomorphic and 4-finger hands 3/17; best sim search reaches 3.3 rad/s</td>
<td width="180"><a href="https://arxiv.org/abs/2512.03743">paper</a> / <a href="https://an-axolotl.github.io/HouseofDextra/">project</a></td>
</tr>
<tr>
<td width="100" nowrap>ICLR 2026</td>
<td width="260"><a href="https://openreview.net/forum?id=wySMuWHmt4">Primary-Fine Decoupling for Action Generation in Robotic Imitation</a></td>
<td width="230">Represent multimodal demonstrations without averaging modes or switching incoherently between them.</td>
<td width="230">PF-DAG predicts a discrete primary mode and a continuous fine action, improving low- and high-DoF imitation.</td>
<td width="240">Real failures remain under OOD object placement and intermittent tactile noise; benchmarks do not share one uniform engine.</td>
<td width="280">Sim: Adroit Shadow, DexArt Allegro, MetaWorld gripper. Real: xArm + gripper or xArm + ROBOTERA XHand + RealSense L515</td>
<td width="160">Real: arm+gripper 7+1; arm+XHand 7+12 DoF</td>
<td width="220">56 grasp/manipulation tasks; real pick cube, place toy, wipe table, and tactile bin placement</td>
<td width="180">XHand: 5 fingertips × 120 taxels × 3-D force vector; no tactile on gripper tasks</td>
<td width="210">Absolute joint positions at 30 Hz: 8-D or 19-D</td>
<td width="330">56 Adroit/DexArt/MetaWorld tasks; 10 expert demos/task for Adroit/MetaWorld and 90 for DexArt; paper does not give one engine mapping for all suites</td>
<td width="240">No sim-to-real transfer claim; the same primary/fine architecture is trained separately on real demonstrations</td>
<td width="220">GELLO for xArm+gripper; Meta Quest 3 hand tracking + AnyTeleop retargeting for XHand</td>
<td width="300">56-task overall success 79.6%; real four-task success 70/90/70/80%</td>
<td width="180"><a href="https://arxiv.org/abs/2602.21684">paper</a> / <a href="https://xiaohanlei.github.io/projects/PF-DAG/">project</a> / <a href="https://github.com/XiaohanLei/PF-DAG">code</a></td>
</tr>
<tr>
<td width="100" nowrap>ICLR 2026</td>
<td width="260"><a href="https://openreview.net/forum?id=13jshGCK9i">D-REX: Differentiable Real-to-Sim-to-Real Engine for Learning Dexterous Grasping</a></td>
<td width="230">Build object-specific digital twins and identify dynamics for force-aware dexterous grasping.</td>
<td width="230">Differentiates through reconstructed MuJoCo scenes to identify object mass and learn policies from retargeted human RGB videos.</td>
<td width="240">Evidence is rigid-body and object specific; the appendix describes LEAP actuation inconsistently, and small objects remain limited by pose/mesh error and finger size.</td>
<td width="280">7-DoF Franka Panda + Allegro Hand or LEAP Hand; RealSense D435i or iPhone capture</td>
<td width="160">Both hands: 16 independently actuated DoF</td>
<td width="220">Object-specific grasp/lift with position- and force-aware contact control</td>
<td width="180">No tactile array; uses visual pose plus motor current/torque limits as force proxy</td>
<td width="210">16-D joint targets plus contact/force conditioning; control rate not disclosed; single-pose inference is ~0.5 s and is not a control frequency</td>
<td width="330">MuJoCo differentiable physics + Brax policy training + GradSim reconstruction; about 300 scene images and 200–300 grasp poses per object</td>
<td width="240">Real scan → Gaussian/mesh digital twin → differentiable mass ID → human-video retargeting → force-aware sim policy → real</td>
<td width="220">Human RGB videos → hand/object pose extraction → Dex-Retargeting to robot demonstrations</td>
<td width="300">Average real success 86% vs 75/76% baselines; OOD objects score 9/10, 10/10, and 9/10</td>
<td width="180"><a href="https://arxiv.org/abs/2603.01151">paper</a> / <a href="https://drex.github.io/">project</a> / <a href="https://github.com/louhz/D-rex">code</a></td>
</tr>
<tr>
<td width="100" nowrap>AAAI 2026</td>
<td width="260"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38874">Dexterous Manipulation Transfer via Progressive Kinematic-Dynamic Alignment</a></td>
<td width="230">Transfer human manipulation videos to different dexterous hands with stable contact dynamics.</td>
<td width="230">PKDA combines kinematic retargeting, thumb-guided pre-grasp, residual contact RL, and wrist trajectory planning.</td>
<td width="240">Allegro/LEAP struggle with small or slender objects; changing multi-contact dynamics remain open and real results are qualitative.</td>
<td width="280">Sim: Adroit, Allegro, LEAP Hands. Real: UR10 arm + LEAP Hand</td>
<td width="160">Adroit 24; Allegro/LEAP 16 DoF</td>
<td width="220">Grasp, in-hand/articulated manipulation, and object-following with changing fingertip contacts</td>
<td width="180">No tactile hardware; contact points/rewards come from video estimates and simulation</td>
<td width="210">Action first 6 dimensions control wrist, remainder finger joints; MuJoCo control at 120 Hz</td>
<td width="330">MuJoCo; about 600 GRAB, 40 TCDM, 10 DexYCB, 10 TACO, and 5 self-captured trajectories</td>
<td width="240">Video perception → hand retargeting → MuJoCo residual RL/contact alignment → wrist planning → open-loop real replay</td>
<td width="220">Offline human videos/datasets; no online teleoperation</td>
<td width="300">Transfer success Adroit/Allegro/LEAP 77.5/72.5/67.5%; real LEAP deployment is qualitative only</td>
<td width="180"><a href="https://arxiv.org/abs/2511.10987">paper</a> / <a href="https://ojs.aaai.org/index.php/AAAI/article/view/38874">AAAI</a></td>
</tr>
<tr>
<td width="100" nowrap>AAAI 2026</td>
<td width="260"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38892">Learning Object-Centric Motion Priors from Human for Robotic Dexterous Manipulation</a></td>
<td width="230">Learn reusable object-centric motion priors from HOI data without task-specific reward engineering.</td>
<td width="230">A GPT-2 motion predictor supplies future hand-object states; object-following rewards guide PPO across grasping, articulation, obstacle avoidance, and hand embodiments.</td>
<td width="240">Requires tracked 6-DoF object poses, calibrated retargeting, and per-hand system identification; contact comes from collision checks, not touch.</td>
<td width="280">Dual xArm-7; each arm mounts a PSYONIC Ability, ROBOTERA XHand1, or Inspire hand; RealSense D435i</td>
<td width="160">7 DoF/arm; hand DoF not stated</td>
<td width="220">Grasp/lift, articulated-object rotation, collision-free grasping, cross-hand transfer</td>
<td width="180">None; SAPIEN collision contact only</td>
<td width="210">Delta end-effector pose + delta hand-joint positions; rate not stated</td>
<td width="330">SAPIEN3 + OpenAI Gymnasium; 1,024 parallel environments; PPO for 1M steps; DexYCB and ARCTIC HOI data</td>
<td width="240">HOI prediction → embodiment-specific retargeting → PPO with system identification and domain randomization → zero-shot real</td>
<td width="220">Offline DexYCB/ARCTIC human-object data; no online teleoperation</td>
<td width="300">Grasp sim/real 84%/77%; articulation 66%/53%; obstacle grasp 66%/63%</td>
<td width="180"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38892">AAAI</a></td>
</tr>
<tr>
<td width="100" nowrap>AAAI 2026</td>
<td width="260"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38953">DexGraspVLA: A Vision-Language-Action Framework Towards General Dexterous Grasping</a></td>
<td width="230">Generalize language-guided dexterous grasping across unseen objects, clutter, lighting, and backgrounds.</td>
<td width="230">A pretrained VLM plans target boxes/masks; a DINOv2-conditioned DiT controller executes grasping, long-horizon, and nonprehensile tasks.</td>
<td width="240">Real-only evaluation uses one arm-hand stack and no tactile input; hardware code is not public.</td>
<td width="280">7-DoF RealMan RM75-6F + 6-DoF PsiBot G0-R; wrist RealSense D405C + head RealSense D435</td>
<td width="160">13 DoF total: 7 arm + 6 hand</td>
<td width="220">Cluttered grasp/lift, repeated attempts, long-horizon task chains, nonprehensile grasping</td>
<td width="180">None</td>
<td width="210">13-D target joint angles; DiT action chunks at 20 Hz</td>
<td width="330">Real-only; 2,094 successful grasp demos/36 objects, plus 1,029 nonprehensile demos/32 objects</td>
<td width="240">Not applicable: trained and evaluated on the real platform</td>
<td width="220">Kinesthetic human demonstrations; planner converts language/RGB into invariant masks</td>
<td width="300">Single attempt 90.8%; ≤3 attempts 96.9%; long-horizon 89.6%; nonprehensile 84.7%</td>
<td width="180"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38953">paper</a> / <a href="https://dexgraspvla.github.io/">project</a> / <a href="https://github.com/Psi-Robot/DexGraspVLA">code</a></td>
</tr>
<tr>
<td width="100" nowrap>CVPR 2026</td>
<td width="260"><a href="https://arxiv.org/abs/2603.22264">UniDex: A Robot Foundation Suite for Universal Dexterous Hand Control from Egocentric Human Videos</a></td>
<td width="230">Reduce robot-demo cost and unify control across heterogeneous dexterous hands.</td>
<td width="230">UniDex-Dataset, the 82-D FAAS action space, UniDex-VLA, and UniDex-Cap form one human-video-to-robot stack.</td>
<td width="240">Still needs human-in-the-loop retargeting and per-hand actuator mappings; tactile/force feedback is absent.</td>
<td width="280">Dataset: Allegro, Ability, Inspire, LEAP, OYMotion, Shadow, Wuji, XHand; real Franka + Inspire/Wuji/OYMotion + RealSense L515</td>
<td width="160">8 hands; 6–24 active DoF</td>
<td width="220">Five tool-use/multistage tasks; contact-preserving cross-hand transfer</td>
<td width="180">None</td>
<td width="210">82-D FAAS action chunks; robot control rate not stated</td>
<td width="330">52K trajectories/9M frames from H2O, HOI4D, HOT3D, TACO and other egocentric data; PyBullet IK; 5 real tasks × 50 demos</td>
<td width="240">Fingertip/contact alignment + human-in-loop correction + masked-hand point clouds; FAAS then decodes to each hand</td>
<td width="220">Human videos at 30 fps; Apple Vision Pro/OpenTeleVision and UniDex-Cap for downstream demos</td>
<td width="300">Average progress 81%, success 76%; π0 38%/35%; zero-shot cross-hand success 60% and 40%</td>
<td width="180"><a href="https://arxiv.org/abs/2603.22264">paper</a> / <a href="https://unidex-ai.github.io/">project</a> / <a href="https://github.com/unidex-ai/UniDex">code</a> / <a href="https://huggingface.co/UniDex-ai/UniDex">data</a></td>
</tr>
<tr>
<td width="100" nowrap>NeurIPS 2025</td>
<td width="260"><a href="https://arxiv.org/abs/2511.01276">Contact Map Transfer with Conditional Diffusion Model for Generalizable Dexterous Grasp Generation</a></td>
<td width="230">Generate stable, task-conditioned grasps on novel objects without optimizing every grasp from scratch.</td>
<td width="230">Cascaded diffusion transfers contact, part, and direction maps from shape templates, then robust grasp recovery optimizes the hand pose.</td>
<td width="240">Depends on same-category templates; no tactile feedback; the exact custom humanoid and Inspire-hand model are not disclosed.</td>
<td width="280">Sim ShadowHand; real custom humanoid + Inspire hand; ZED head camera + two RealSense cameras</td>
<td width="160">Shadow: 24 hand parameters + 6-D root; real hand DoF not stated</td>
<td width="220">Static task-conditioned power/functional grasp generation via object contact maps</td>
<td width="180">None; contact maps are geometric conditions</td>
<td width="210">24-D hand configuration + SE(3) hand-root pose; execution rate not stated</td>
<td width="330">CapGrasp: ~1.8K objects/~50K template–novel pairs; Isaac Gym for stability filtering/evaluation</td>
<td width="240">Template-map transfer + grasp recovery; real Inspire execution pipeline is not separately specified</td>
<td width="220">No teleoperation; grasp templates/data are offline</td>
<td width="300">Seen/unseen SR 79.32%/74.14%; task consistency 83.60%/79.28%; real success 70%</td>
<td width="180"><a href="https://arxiv.org/abs/2511.01276">paper</a> / <a href="https://cmtdiffusion.github.io/">project</a> / <a href="https://github.com/Yiyao-Ma/cmtdiffusion">code</a></td>
</tr>
<tr>
<td width="100" nowrap>NeurIPS 2025</td>
<td width="260"><a href="https://arxiv.org/abs/2506.02489">Grasp2Grasp: Vision-Based Dexterous Grasp Translation via Schrödinger Bridges</a></td>
<td width="230">Translate functional grasps across human and robot hand morphologies.</td>
<td width="230">A vision-conditioned Schrödinger Bridge learns Human→Allegro, Human→Shadow, and Shadow→Allegro grasp mappings.</td>
<td width="240">A new hand requires target-domain training; evaluation is simulation-only, static-grasp-only, and touch-free.</td>
<td width="280">Simulated human hand, Allegro Hand, and Shadow Hand; no carrier arm</td>
<td width="160">Human 20; Allegro 16; Shadow 22 + SE(3) base</td>
<td width="220">Cross-morphology static grasp translation and stability/contact preservation</td>
<td width="180">None</td>
<td width="210">Hand joint pose + SE(3) base pose generation; no control rate</td>
<td width="330">MultiGripperGrasp: 30.4M grasps, 11 manipulators, 345 objects; Warp Jacobian + Isaac Gym stability tests</td>
<td width="240">Simulation-only cross-hand translation; no real transfer</td>
<td width="220">Human grasp poses in the dataset; no teleoperation</td>
<td width="300">Cross-hand SR 77.23%/45.15%/79.98% (mean 67.45%); ~0.8 s per grasp</td>
<td width="180"><a href="https://arxiv.org/abs/2506.02489">paper</a> / <a href="https://grasp2grasp.github.io/">project</a> / <a href="https://github.com/n3il666/grasp2grasp">code</a></td>
</tr>
<tr>
<td width="100" nowrap>NeurIPS 2025</td>
<td width="260"><a href="https://arxiv.org/abs/2506.19212">Scaffolding Dexterous Manipulation with Vision-Language Models</a></td>
<td width="230">Replace task-specific rewards/demonstrations with VLM-generated manipulation scaffolds.</td>
<td width="230">A VLM proposes keypoints and wrist/object trajectories; residual closed-loop RL tracks them and transfers zero-shot to hardware.</td>
<td width="240">VLM keypoint and trajectory errors still dominate; only three real tasks, without tactile/force feedback.</td>
<td width="280">16-DoF Allegro + 7-DoF KUKA LBR iiwa 14 + table-mounted ZED 1 stereo camera</td>
<td width="160">23 DoF total: 7 arm + 16 hand</td>
<td width="220">Placement, articulated opening, sliding/hammering, scissors/pliers manipulation</td>
<td width="180">None</td>
<td width="210">Wrist SE(3) + finger positions/residuals; policy 60 Hz, physics 120 Hz</td>
<td width="330">ManiSkill3/ReplicaCAD; 2,048 environments; 8 tasks; 100 initial states × 20 rollouts × 3 seeds</td>
<td width="240">Digital twin + domain randomization; low-level policy trains entirely in simulation</td>
<td width="220">No human demos; plans come from VLM queries on one RGB-D scene</td>
<td width="300">Sim mean 72%, refined 81%; real placement/slide/hammer 90%/85%/65% (20 trials each)</td>
<td width="180"><a href="https://arxiv.org/abs/2506.19212">paper</a> / <a href="https://sites.google.com/view/dexterous-vlm-scaffolding">project</a> / <a href="https://github.com/vdebakker/vlm-scaffolding">code</a></td>
</tr>
<tr>
<td width="100" nowrap>NeurIPS 2025</td>
<td width="260"><a href="https://arxiv.org/abs/2505.11032">DexGarmentLab: Dexterous Garment Manipulation Environment with Generalizable Policy</a></td>
<td width="230">Provide scalable bimanual dexterous garment tasks, data generation, and sim-to-real policies.</td>
<td width="230">DexGarmentLab supplies garment assets/15 task scenes; HALO uses affordance grounding and shape-adaptive diffusion trajectories.</td>
<td width="240">Covers one garment at a time; deformable sim-to-real, target-region grasping, and precise placement remain weak.</td>
<td width="280">Sim: dual UR10e + ShadowHands. Real A: dual RealMan RM75-6F + PsiBot G0-R + D435. Real B: dual UR10e + ShadowHands + Azure Kinect</td>
<td width="160">Sim action 60-D; real A 7-DoF arm + 6-DoF hand/side</td>
<td width="220">Bimanual fling, fold, hang, wear, and garment–environment interaction</td>
<td width="180">None</td>
<td width="210">Per side: 6-D arm pose + 24 hand joints; rate not stated</td>
<td width="330">Isaac Sim 4.5.0; 2,500+ garments/8 categories/15 tasks; one seed demo expanded to 100 demos/task</td>
<td width="240">Matched UR10e/Shadow digital twin; 15 real demos/task raise the two real tests to 13/15</td>
<td width="220">Leap Motion supplies one ShadowHand seed; automated execution expands demonstrations</td>
<td width="300">Real A: 13/15, 13/15, 11/15, 14/15. Real B sim-only: 8/15, 9/15; +15 real: 13/15, 13/15</td>
<td width="180"><a href="https://arxiv.org/abs/2505.11032">paper</a> / <a href="https://wayrise.github.io/DexGarmentLab/">project</a> / <a href="https://github.com/wayrise/DexGarmentLab">code</a> / <a href="https://huggingface.co/datasets/wayrise/DexGarmentLab">data</a></td>
</tr>
<tr>
<td width="100" nowrap>CVPR 2025</td>
<td width="260"><a href="https://arxiv.org/abs/2412.02699">UniGraspTransformer: Simplified Policy Distillation for Scalable Dexterous Robotic Grasping</a></td>
<td width="230">Distill thousands of object-specific grasp experts into one scalable policy.</td>
<td width="230">Per-object PPO teachers generate trajectories; a Transformer student handles state- and point-cloud-based seen/unseen-object grasping.</td>
<td width="240">ShadowHand simulation only; no real transfer or tactile feedback, and the state setting assumes object state.</td>
<td width="280">Floating simulated Shadow Hand over a tabletop; no carrier arm</td>
<td width="160">24 actuators: 6 wrist + 18 active finger DoF</td>
<td width="220">Approach, enveloping grasp, lift to a target height</td>
<td width="180">None</td>
<td width="210">24-D: wrist force/torque (6) + finger joint positions (18); rate not stated</td>
<td width="330">Isaac Gym 3.0; 3,200 objects; 3.2M successful trajectories, each 200 steps</td>
<td width="240">Simulation-only; no sim-to-real path</td>
<td width="220">No human/teleoperation data</td>
<td width="300">State seen/same-category/unseen 91.2%/89.2%/88.3%; vision 88.9%/87.3%/86.8%</td>
<td width="180"><a href="https://arxiv.org/abs/2412.02699">paper</a> / <a href="https://dexhand.github.io/UniGraspTransformer/">project</a> / <a href="https://github.com/microsoft/UniGraspTransformer">code</a></td>
</tr>
<tr>
<td width="100" nowrap>CVPR 2025</td>
<td width="260"><a href="https://arxiv.org/abs/2503.08257">DexGrasp Anything: Towards Universal Robotic Dexterous Grasping with Physics Awareness</a></td>
<td width="230">Generate diverse, physically stable dexterous grasps for arbitrary objects.</td>
<td width="230">Physics-aware diffusion adds penetration/contact constraints and an LLM object prior; DGA scales data to 3.40M poses.</td>
<td width="240">No tactile feedback; real ShadowHand tests are qualitative, and the carrier hardware/control rate are not disclosed.</td>
<td width="280">ShadowHand in data, Isaac Gym evaluation, and qualitative real deployment; carrier not stated</td>
<td width="160">24-D hand pose + global rotation/translation</td>
<td width="220">Static universal grasp-pose generation and six-direction stability</td>
<td width="180">None</td>
<td width="210">Generates q∈R24 plus global R,t; no online control rate</td>
<td width="330">DGA: 3.40M poses/15,698 objects; Isaac Gym filtering/evaluation; curated real+sim sources</td>
<td width="240">GRAB human poses are retargeted to ShadowHand; real pre-grasp execution follows a prior pipeline</td>
<td width="220">Offline GRAB human capture; no online teleoperation</td>
<td width="300">LLM variant MultiDex Suc.6/Suc.1 79.1%/98.1%; cross-dataset Suc.6 58.6%/53.4%</td>
<td width="180"><a href="https://arxiv.org/abs/2503.08257">paper</a> / <a href="https://dexgraspanything.github.io/">project</a> / <a href="https://github.com/4DVLab/DexGrasp-Anything">code</a> / <a href="https://huggingface.co/datasets/GaussionZhong/DexGrasp-Anything">data</a></td>
</tr>
<tr>
<td width="100" nowrap>arXiv 2025 (v2 2026)</td>
<td width="260"><a href="https://arxiv.org/abs/2602.16710">EgoScale: Scaling Dexterous Manipulation with Diverse Egocentric Human Data</a></td>
<td width="230">Scale egocentric human-video pretraining to high-DoF robot dexterity and new embodiments.</td>
<td width="230">Large human pretraining, aligned human–robot mid-training, and small robot post-training enable one-shot tasks and G1 transfer.</td>
<td width="240">No simulation or tactile feedback; the recipe is data-heavy, control rate is unstated, and no formal venue was found.</td>
<td width="280">Galaxea R1Pro, dual 7-DoF arms + dual 22-DoF Sharpa Wave; transfer: Unitree G1 + 7-DoF tri-finger; OAK cameras</td>
<td width="160">R1Pro: 7 arm + 22 hand/side; G1 hand: 7</td>
<td width="220">Bimanual long-horizon dexterity, one-shot adaptation, cross-embodiment tool/object tasks</td>
<td width="180">None reported</td>
<td width="210">Per arm relative SE(3) + hand joints; rate not stated</td>
<td width="330">Real-only: Stage I 20,854 h/9,869 scenes/6,015 tasks/43,237 objects; Stage II 50 h human + 4 h robot; post-train 100 robot demos</td>
<td width="240">Human wrists/hands retarget to Sharpa space; embodiment adapters align the G1 hand/action space</td>
<td width="220">Action-labeled egocentric human video + aligned human/robot play data</td>
<td width="300">R1Pro completion/success .83/.56 vs no pretrain .24/.02; G1 two tasks .83/.67 and .88/.50</td>
<td width="180"><a href="https://arxiv.org/abs/2602.16710">paper</a> / <a href="https://research.nvidia.com/labs/gear/egoscale/">project</a></td>
</tr>
<tr>
<td width="100" nowrap>CVPR 2026</td>
<td width="260"><a href="https://openaccess.thecvf.com/content/CVPR2026/papers/Jiang_Cross-Hand_Latent_Representation_for_Vision-Language-Action_Models_CVPR_2026_paper.pdf">Cross-Hand Latent Representation for Vision-Language-Action Models (XL-VLA)</a></td>
<td width="230">Share one VLA action space across hands with different joint structures.</td>
<td width="230">A shared 32-D latent plus hand-specific encoders/decoders supports four-hand co-training and zero-shot hand–task combinations.</td>
<td width="240">Still needs per-hand adapters and demonstrations; real-only evaluation has no tactile feedback.</td>
<td width="280">Bimanual xArm7 with Ability, Inspire, X-Hand1, or Paxini DexH13; Unitree G1 cross-robot test</td>
<td width="160">Ability 12(6 mimic), Inspire 12(6), XHand 12, Paxini 16(3)</td>
<td width="220">Ten bimanual dexterous tasks; cross-hand trajectory replay/contact preservation</td>
<td width="180">None</td>
<td width="210">64 absolute joint commands at 20 Hz (3.2 s), encoded to 32-D latent</td>
<td width="330">Real-only: 10 tasks × 4 hands × 50 demos = 2,000 demos/~2M state–action pairs</td>
<td width="240">FK-regularized shared latent decodes directly to each hand; no simulator</td>
<td width="220">Apple Vision Pro with Bunny-VisionPro teleoperation</td>
<td width="300">Mean 0.72 vs π0 0.32; Ability/Inspire/Paxini/XHand .73/.68/.78/.70; G1 ~.825 vs .525</td>
<td width="180"><a href="https://openaccess.thecvf.com/content/CVPR2026/papers/Jiang_Cross-Hand_Latent_Representation_for_Vision-Language-Action_Models_CVPR_2026_paper.pdf">paper</a> / <a href="https://xl-vla.github.io/">project</a> / <a href="https://github.com/EmptyBlueBox/DexLatent">code</a></td>
</tr>
<tr>
<td width="100" nowrap>ECCV 2026</td>
<td width="260"><a href="https://arxiv.org/abs/2512.13644">World Models for Learning Dexterous Hand-Object Interactions from Human Videos (DexWM)</a></td>
<td width="230">Learn dexterous interaction dynamics from human video for goal-conditioned robot planning.</td>
<td width="230">Dense hand-keypoint actions and a hand-consistency loss let one latent world model support CEM/MPC planning and zero-shot real grasping.</td>
<td width="240">Default CEM planning takes 168 s/episode; no tactile input, and RoboCasa uses only the right active hand.</td>
<td width="280">RoboCasa: dual Franka + dual Allegro, right side active. Real: Franka Panda + Allegro hand</td>
<td width="160">Planner: 7 arm + 16 hand = 23 joints</td>
<td width="220">Reach, grasp, place; image-goal planning with predicted hand–object motion</td>
<td width="180">None</td>
<td width="210">World action 132-D MANO/camera keypoints at 5 Hz; planner outputs 23-D joints</td>
<td width="330">EgoDex 829 h + DROID ~100 h pretrain; RoboCasa ~4 h random exploration fine-tune; no real fine-tune</td>
<td width="240">Allegro maps to the five-finger keypoint space; CEM/MPC executes joint targets zero-shot on real hardware</td>
<td width="220">EgoDex human Vision Pro video + DROID robot video; RoboCasa data need no teleop</td>
<td width="300">Sim reach/grasp/place 72%/28%/58% vs DP 16%/8%/0%; real 10/12 (83%); default planning 168 s</td>
<td width="180"><a href="https://arxiv.org/abs/2512.13644">paper</a> / <a href="https://raktimgg.github.io/dexwm/">project</a></td>
</tr>
<tr>
<td width="100" nowrap>arXiv 2026</td>
<td width="260"><a href="https://arxiv.org/abs/2512.24210">GR-Dexter Technical Report</a></td>
<td width="230">Build a bimanual VLA stack for 21-DoF anthropomorphic hands despite scarce robot data.</td>
<td width="230">ByteDexter V2, whole-hand teleoperation, and robot/VL/cross-embodiment/human co-training form a 56-DoF real stack.</td>
<td width="240">Technical report with no public code/dataset/SDK; fingertip tactile arrays are not used by the reported VLA.</td>
<td width="280">Dual Franka Research 3 + dual ByteDexter V2; Meta Quest headset/controllers + Manus Metagloves</td>
<td width="160">21 mechanical/16 active per hand; 56 total mechanical DoF</td>
<td width="220">Bimanual makeup decluttering, long-horizon tool use, generalizable pick-and-place</td>
<td width="180">Five high-density piezoresistive fingertip normal-force arrays/hand; not policy input</td>
<td width="210">88-D: arm joints/EE poses + 16 hand joints/side + fingertip positions; rate not stated</td>
<td width="330">Real-only; ~20 h own data per experiment; ActionNet ~140 h, OpenLoong 100K+, RoboMIND 107K demos, human video 800+ h</td>
<td width="240">No sim; camera standardization + fingertip-centric retargeting aligns external embodiments to ByteDexter</td>
<td width="220">Meta Quest + Manus bimanual teleop; egocentric human trajectories</td>
<td width="300">Makeup basic/OOD .97/.89 vs plain .96/.64; pick-place basic/unseen-object/unseen-instruction .93/.85/.83</td>
<td width="180"><a href="https://arxiv.org/abs/2512.24210">paper</a> / <a href="https://byte-dexter.github.io/gr-dexter/">project</a></td>
</tr>
<tr>
<td width="100" nowrap>arXiv 2025</td>
<td width="260"><a href="https://arxiv.org/abs/2511.01177">Scaling Cross-Embodiment World Models for Dexterous Manipulation</a></td>
<td width="230">Unify dynamics/data and planning across hands with incompatible kinematics and action spaces.</td>
<td width="230">Hand/object particles and displacement actions let one GNN world model co-train on simulated robots and real human hands, then plan on unseen hardware.</td>
<td width="240">Only pushing and plasticine primitives are tested; no tactile input, binary success rate, or formal venue.</td>
<td width="280">Sim: Ability, Allegro, XHand, LEAP, Shadow + second Shadow variant. Real: xArm7 + Ability or XHand + four RealSense cameras</td>
<td width="160">Hands: 6/16/12/16/24 DoF</td>
<td width="220">Rigid pushing; plasticine ThumbPinch, FingersPinch, PalmPress</td>
<td width="180">None</td>
<td width="210">Hand/object particles + EE displacement fields; CEM; rate not stated</td>
<td width="330">SAPIEN rigid pushing + Rewarped plasticine; 100 random trajectories/task; real human data 30 min per primitive</td>
<td width="240">Forward kinematics maps joints to shared particles; same world model plans on Ability/XHand without target fine-tuning</td>
<td width="220">Real human-hand demonstrations; no robot teleoperation</td>
<td width="300">Co-train CD/EMD (×10⁻³): Ability 6.95/4.92 vs human-only 7.15/5.23; XHand 6.85/4.78 vs 7.22/5.18</td>
<td width="180"><a href="https://arxiv.org/abs/2511.01177">paper</a></td>
</tr>
</tbody>
</table>
