# 3D grounding

[Home](../../../README.md) | [中文](../../zh-CN/vla/3d-grounding.md) | [Direction index](README.md)

Total: 41 papers.

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
<td width="120" nowrap>CoRL 2023</td>
<td width="320"><a href="https://arxiv.org/abs/2311.05779">Language-guided Robot Grasping: CLIP-based Referring Grasp Synthesis in Clutter (CROG)</a></td>
<td width="420">Grounds a language-referred target in clutter and predicts a top-down two-finger grasp.</td>
<td width="230">CLIP-based referring segmentation</td>
<td width="240">4-DoF grasp [x,y,yaw,width]</td>
<td width="300">OCID-VLG: 1,763 RGB-D scenes, 75K grasp rectangles, 89.6K language-mask-grasp samples; Gazebo + real trials</td>
<td width="260">joint language segmentation and grasp synthesis</td>
<td width="240">language grounding + parallel-gripper grasping; not dexterous-hand control</td>
<td width="200">Gazebo + Real</td>
<td width="360">Sim grounding/task success: isolated 76/62%, clutter 60/42%; real 65/23.9% and 60/20%</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2311.05779">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/HilbertXu/CROG">code</a></td>
<td width="240">OCID-VLG</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=RYwQ0xQcAh">Interaction-aware Representation Modeling With Co-Occurrence Consistency for Egocentric Hand-Object Parsing (InterFormer)</a></td>
<td width="420">Parses hands and interacted objects from egocentric RGB while reducing implausible hand-object co-occurrence.</td>
<td width="230">-</td>
<td width="240">2D hand/object segmentation masks; perception only</td>
<td width="300">EgoHOS: 8,993 train/1,124 val/1,126 in-domain/500 OOD; mini-HOI4D: 1,095 images</td>
<td width="260">interaction-aware segmentation + co-occurrence consistency</td>
<td width="240">egocentric HOI grounding; no robot, 3D action, or control</td>
<td width="200">offline real images; no simulator</td>
<td width="360">EgoHOS in-domain/OOD mIoU 73.22/72.82%; mini-HOI4D 66.07%; interaction-illusion rate 2.19→1.55%</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=RYwQ0xQcAh">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/yuggiehk/InterFormer">code</a></td>
<td width="240">EgoHOS / mini-HOI4D</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38873">GRIM: Task-Oriented Grasping with Conditioning on Generative Examples</a></td>
<td width="420">Retrieves task-oriented grasp examples and transfers their functional grasp geometry to a novel scene object.</td>
<td width="230">AnyGrasp candidates + generated/web/human examples</td>
<td width="240">6-DoF two-finger grasp pose</td>
<td width="300">No physics training; memory has 210 examples (180 generated frames + 15 web + 15 human); TaskGrasp offline test + real robot</td>
<td width="260">hand-object reconstruction + semantic 3D alignment/ICP + grasp reranking</td>
<td width="240">task-oriented parallel-gripper grasp retrieval</td>
<td width="200">offline benchmark + Real; no simulator</td>
<td width="360">TaskGrasp mAP all/held-out object/held-out task 0.67/0.65/0.64; Kinova Gen3 Lite real 39/50 = 78%</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38873">paper</a></td>
<td width="110" nowrap><a href="https://grim-tog.github.io/">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">210-example memory / TaskGrasp</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38940">GraphGrasp: Lightweight and Efficient Graph-Guided 6-DoF Robotic Grasp Pose Estimation Network</a></td>
<td width="420">Predicts efficient 6-DoF two-contact grasps in clutter with graph-guided point-cloud reasoning.</td>
<td width="230">-</td>
<td width="240">rotation + translation + parallel-gripper opening width</td>
<td width="300">GraspNet-1Billion RealSense split: 190 scenes × 256 views; 15K input points; no physics simulator</td>
<td width="260">scene/object/grasp graph network with force-closure and collision scoring</td>
<td width="240">point-cloud 6-DoF parallel-gripper grasp estimation</td>
<td width="200">offline benchmark + Real</td>
<td width="360">Seen/similar/novel AP 64.88/56.91/24.83; 3.2M parameters; UR3 real mean grasp success 92.1% (trial count undisclosed)</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38940">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/BIT-robot-group/GraphGrasp">code</a></td>
<td width="240">GraspNet-1Billion</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38957">Effective Robotic Cloth Grasping Through Suppressing False Discoveries</a></td>
<td width="420">Localizes reliable grasp points on cluttered garments by suppressing false segmentation discoveries and using depth wrinkles.</td>
<td width="230">-</td>
<td width="240">single RGB-D grasp point + vertical parallel-jaw pickup</td>
<td width="300">No simulator; 7 garments; 640 train/440 validation RGB scenes; 50 real pile-clearing trials</td>
<td width="260">unsupervised RGB segmentation + false-discovery suppression + depth-wrinkle grasp scoring</td>
<td width="240">cloth perception/grasp-point grounding; Baxter gripper, not dexterous hand</td>
<td width="200">Real only</td>
<td width="360">Segmentation mFDR 0%; grasp success/pile-clearing 94%; +20/+14/+28 pp over three segmentation baselines</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38957">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">7-garment RGB-D dataset</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://cvpr.thecvf.com/virtual/2025/poster/32440">ZeroGrasp: Zero-Shot Shape Reconstruction Enabled Robotic Grasping</a></td>
<td width="420">Combines single-view shape reconstruction, occlusion/spatial reasoning, and 6-DoF grasp prediction.</td>
<td width="230">ZeroGrasp reconstruction + grasp network</td>
<td width="240">6-DoF Robotiq 2F-85 parallel-gripper grasp</td>
<td width="300">ZeroGrasp-11B arXiv version: 1M RGB-D, 12K Objaverse-LVIS objects, 11.3B physics-validated grasps; Isaac Gym labels/filtering</td>
<td width="260">3D shape reconstruction + spatial relation reasoning + grasp pose estimation</td>
<td width="240">zero-shot parallel-gripper grasping; not dexterous-hand control</td>
<td width="200">Isaac Gym label validation + Real</td>
<td width="360">GraspNet AP seen/similar/novel 70.53/62.51/26.46; pretrain+FT 72.43/65.45/28.49; real 75% vs 56.25%</td>
<td width="110" nowrap><a href="https://cvpr.thecvf.com/virtual/2025/poster/32440">paper</a></td>
<td width="110" nowrap><a href="https://sh8.io/#/zerograsp">project</a></td>
<td width="110" nowrap><a href="https://github.com/sh8/ZeroGrasp">code</a></td>
<td width="240">ZeroGrasp-11B (CVPR page reports 8.9B; arXiv reports 11.3B annotations)</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2023</td>
<td width="320"><a href="https://arxiv.org/abs/2308.07931">Distilled Feature Fields Enable Few-Shot Language-Guided Manipulation</a></td>
<td width="420">F3RM uses distilled feature fields for few-shot language-guided manipulation.</td>
<td width="230">Distilled Feature Fields Enable Few-Shot Language-Guided Manipulation</td>
<td width="240">robot action</td>
<td width="300">VLA / 3D grounding</td>
<td width="260">CoRL robot-learning method</td>
<td width="240">robot policy</td>
<td width="200">robot benchmarks</td>
<td width="360">Add CoRL VLA coverage.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2308.07931">paper</a></td>
<td width="110" nowrap><a href="https://f3rm.github.io">project</a></td>
<td width="110" nowrap><a href="https://github.com/f3rm/f3rm">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2023</td>
<td width="320"><a href="https://arxiv.org/abs/2306.14896">RVT: Robotic View Transformer for 3D Object Manipulation</a></td>
<td width="420">RVT uses view-transformer representations for 3D object manipulation.</td>
<td width="230">RVT</td>
<td width="240">robot action</td>
<td width="300">VLA / 3D grounding</td>
<td width="260">CoRL robot-learning method</td>
<td width="240">robot policy</td>
<td width="200">robot benchmarks</td>
<td width="360">Add CoRL VLA coverage.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2306.14896">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2022</td>
<td width="320"><a href="https://arxiv.org/abs/2209.05451">Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation</a></td>
<td width="420">PerAct uses Perceiver-style 3D representations for multitask manipulation.</td>
<td width="230">Perceiver-Actor</td>
<td width="240">robot action</td>
<td width="300">VLA / 3D grounding</td>
<td width="260">CoRL robot-learning method</td>
<td width="240">robot policy</td>
<td width="200">robot benchmarks</td>
<td width="360">Add CoRL VLA coverage.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2209.05451">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2023</td>
<td width="320"><a href="https://arxiv.org/abs/2306.17817">Act3D: 3D Feature Field Transformers for Multi-Task Robotic Manipulation</a></td>
<td width="420">Act3D builds 3D feature-field transformers for multitask robotic manipulation.</td>
<td width="230">Act3D</td>
<td width="240">robot action</td>
<td width="300">VLA / 3D grounding</td>
<td width="260">CoRL robot-learning method</td>
<td width="240">robot policy</td>
<td width="200">robot benchmarks</td>
<td width="360">Add CoRL VLA coverage.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2306.17817">paper</a></td>
<td width="110" nowrap><a href="https://act3d.github.io">project</a></td>
<td width="110" nowrap><a href="https://github.com/zhouxian/act3d-chained-diffuser">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2024</td>
<td width="320"><a href="https://proceedings.mlr.press/v235/zhen24a.html">3D-VLA: A 3D Vision-Language-Action Generative World Model</a></td>
<td width="420">3D-VLA builds a 3D generative world model for vision-language-action manipulation.</td>
<td width="230">3D VLA</td>
<td width="240">3D grounded action</td>
<td width="300">3D grounding / world model</td>
<td width="260">3D generative world modeling</td>
<td width="240">3D VLA policy</td>
<td width="200">robot manipulation benchmarks</td>
<td width="360">Ground VLA action generation in 3D world representations.</td>
<td width="110" nowrap><a href="https://proceedings.mlr.press/v235/zhen24a/zhen24a.pdf">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>IROS 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2606.26800">SSI-Policy: Learning Structured Scene Interfaces for Vision-Language Robotic Manipulation</a></td>
<td width="420">SSI-Policy connects vision-language reasoning with low-data robot manipulation policy learning through structured scene interfaces.</td>
<td width="230">vision-language policy</td>
<td width="240">continuous action</td>
<td width="300">3D grounding / structured scene interface</td>
<td width="260">scene-interface policy learning</td>
<td width="240">structured VLA policy</td>
<td width="200">Real robot manipulation</td>
<td width="360">Use structured scene representations to improve low-data manipulation generalization.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2606.26800">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICRA 2025</td>
<td width="320"><a href="https://kalie-vlm.github.io/">KALIE: Fine-Tuning Vision-Language Models for Open-World Manipulation without Robot Data</a></td>
<td width="420">KALIE fine-tunes VLMs to predict language-conditioned point affordances, using synthetic data for open-world manipulation.</td>
<td width="230">VLM</td>
<td width="240">affordance point</td>
<td width="300">3D grounding / affordance grounding</td>
<td width="260">synthetic data fine-tuning</td>
<td width="240">affordance-conditioned manipulation</td>
<td width="200">Real robot manipulation</td>
<td width="360">Learn language-conditioned affordances without real robot data.</td>
<td width="110" nowrap><a href="https://kalie-vlm.github.io/">paper</a></td>
<td width="110" nowrap><a href="https://kalie-vlm.github.io/">project</a></td>
<td width="110" nowrap><a href="https://github.com/gractang/kalie">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=7M6ryCABIc">PixelVLA: Advancing Pixel-level Understanding in Vision-Language-Action Model</a></td>
<td width="420">PixelVLA connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td width="230">No specific base VLA specified.</td>
<td width="240">3D/spatial grounding</td>
<td width="300">3D representation / 3D grounding</td>
<td width="260">-</td>
<td width="240">3D-grounded policy/perception</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=7M6ryCABIc">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=eKhOrQWAVJ">Spatially Guided Training for Vision-Language-Action Model</a></td>
<td width="420">Spatially Guided Training connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td width="230">No specific base VLA specified.</td>
<td width="240">3D/spatial grounding</td>
<td width="300">3D representation / 3D grounding</td>
<td width="260">3D/spatial representation learning</td>
<td width="240">3D-grounded policy/perception</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=eKhOrQWAVJ">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=euMVC1DO4k">Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model</a></td>
<td width="420">Spatial Forcing connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td width="230">No specific base VLA specified.</td>
<td width="240">3D/spatial grounding</td>
<td width="300">3D representation / 3D grounding</td>
<td width="260">3D/spatial representation learning</td>
<td width="240">3D-grounded policy/perception</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=euMVC1DO4k">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=fzmittHfq3">From Spatial to Actions: Grounding Vision-Language-Action Model in Spatial Foundation Priors</a></td>
<td width="420">From Spatial to Actions connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td width="230">No specific base VLA specified.</td>
<td width="240">3D/spatial grounding</td>
<td width="300">3D representation / 3D grounding</td>
<td width="260">3D/spatial representation learning</td>
<td width="240">3D-grounded policy/perception</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=fzmittHfq3">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=18gC6pZVVc">Geometry-aware 4D Video Generation for Robot Manipulation</a></td>
<td width="420">Geometry-aware 4D Video Generation uses video generation/prediction or future rendering to learn robot interaction dynamics.</td>
<td width="230">-</td>
<td width="240">AR</td>
<td width="300">3D representation / 3D grounding</td>
<td width="260">3D/spatial representation learning</td>
<td width="240">3D-grounded policy/perception</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=18gC6pZVVc">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=WXFfMLyB6y">Generalizable Coarse-to-Fine Robot Manipulation via Language-Aligned 3D Keypoints</a></td>
<td width="420">Generalizable Coarse-to-Fine Robot Manipulation connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td width="230">-</td>
<td width="240">AR</td>
<td width="300">3D representation / 3D grounding</td>
<td width="260">3D keypoint grounding</td>
<td width="240">3D-grounded policy/perception</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=WXFfMLyB6y">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=ggofj6tyr3">Geometry-aware Policy Imitation</a></td>
<td width="420">Geometry-aware Policy Imitation connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td width="230">-</td>
<td width="240">AR</td>
<td width="300">3D representation / 3D grounding</td>
<td width="260">Diffusion policy</td>
<td width="240">Diffusion policy</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=ggofj6tyr3">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=qXfRXfAHOK">PA3FF:Learning Part-Aware Dense 3D Feature Field For Generalizable Articulated Object Manipulation</a></td>
<td width="420">PA3FF connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td width="230">-</td>
<td width="240">AR</td>
<td width="300">3D representation / 3D grounding</td>
<td width="260">Diffusion policy</td>
<td width="240">Diffusion policy</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=qXfRXfAHOK">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=z8BN7KyaPl">RAVEN: End-to-end Equivariant Robot Learning with RGB Cameras</a></td>
<td width="420">RAVEN connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td width="230">-</td>
<td width="240">AR</td>
<td width="300">3D representation / 3D grounding</td>
<td width="260">3D/spatial representation learning</td>
<td width="240">3D-grounded policy/perception</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=z8BN7KyaPl">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=DE5ZJtR4bg">On the Generalization Capacities of MLLMs for Spatial Intelligence</a></td>
<td width="420">On the Generalization Capacities of MLLMs connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td width="230">-</td>
<td width="240">3D/spatial grounding</td>
<td width="300">3D representation / 3D grounding</td>
<td width="260">3D/spatial representation learning</td>
<td width="240">3D-grounded policy/perception</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=DE5ZJtR4bg">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38921">ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver</a></td>
<td width="420">ReconVLA reconstructs target gaze regions to improve visual grounding in vision-language-action robot policies.</td>
<td width="230">No specific base VLA specified.</td>
<td width="240">3D/spatial grounding</td>
<td width="300">3D representation / 3D grounding</td>
<td width="260">-</td>
<td width="240">3D-grounded policy/perception</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38921">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38939">Indoor Multi-View Radar Object Detection via 3D Bounding Box Diffusion</a></td>
<td width="420">REXO lifts diffusion-based 3D bounding boxes into multi-view radar perception for indoor object detection.</td>
<td width="230">-</td>
<td width="240">AR / Diffusion / Flow</td>
<td width="300">3D representation / diffusion/flow policy</td>
<td width="260">Diffusion policy</td>
<td width="240">Diffusion policy</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38939">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38946">RaLD: Generating High-Resolution 3D Radar Point Clouds with Latent Diffusion</a></td>
<td width="420">RaLD uses latent diffusion to generate denser, higher-resolution 3D radar point clouds.</td>
<td width="230">-</td>
<td width="240">AR / Diffusion / Flow</td>
<td width="300">3D representation / diffusion/flow policy</td>
<td width="260">Diffusion policy</td>
<td width="240">Diffusion policy</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38946">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38947">Grounding Actions in Camera Space: Observation-Centric Vision-Language-Action Policy</a></td>
<td width="420">OC-VLA predicts actions in camera coordinates to reduce observation-action spatial inconsistency in VLA policies.</td>
<td width="230">No specific base VLA specified.</td>
<td width="240">3D/spatial grounding</td>
<td width="300">3D representation / 3D grounding</td>
<td width="260">-</td>
<td width="240">3D-grounded policy/perception</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38947">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2510.24261">DynaRend: Learning 3D Dynamics via Masked Future Rendering for Robotic Manipulation</a></td>
<td width="420">DynaRend uses video generation/prediction or future rendering to learn robot interaction dynamics.</td>
<td width="230">-</td>
<td width="240">AR</td>
<td width="300">3D representation / 3D grounding</td>
<td width="260">Generative action modeling</td>
<td width="240">3D-grounded policy/perception</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2510.24261">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://neurips.cc/virtual/2025/loc/san-diego/poster/118141">Building 3D Representations and Generating Motions From a Single Image via Video-Generation</a></td>
<td width="420">VGER uses video generation from a single RGB image to build 3D scene representations for collision-free motion.</td>
<td width="230">-</td>
<td width="240">-</td>
<td width="300">3D representation / 3D grounding</td>
<td width="260">-</td>
<td width="240">-</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://neurips.cc/virtual/2025/loc/san-diego/poster/118141">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2504.12636">A0: An Affordance-Aware Hierarchical Model for General Robotic Manipulation</a></td>
<td width="420">A0 connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td width="230">-</td>
<td width="240">AR</td>
<td width="300">VLA / affordance / 3D grounding</td>
<td width="260">Flow matching policy</td>
<td width="240">Flow policy</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2504.12636">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2408.10123v1">Learning Precise Affordances from Egocentric Videos for Robotic Manipulation</a></td>
<td width="420">Learning Precise Affordances from Egocentric Videos connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td width="230">-</td>
<td width="240">AR</td>
<td width="300">affordance / 3D grounding</td>
<td width="260">Affordance grounding</td>
<td width="240">3D-grounded policy/perception</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2408.10123v1">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2412.04380">EmbodiedOcc: Embodied 3D Occupancy Prediction for Vision-based Online Scene Understanding</a></td>
<td width="420">EmbodiedOcc connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td width="230">-</td>
<td width="240">3D/spatial grounding</td>
<td width="300">3D representation / RL/online fine-tuning</td>
<td width="260">3D/spatial representation learning</td>
<td width="240">3D-grounded policy/perception</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2412.04380">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2504.08531">Embodied Image Captioning: Self-supervised Learning Agents for Spatially Coherent Image Descriptions</a></td>
<td width="420">Embodied Image Captioning connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td width="230">-</td>
<td width="240">AR</td>
<td width="300">3D grounding</td>
<td width="260">3D/spatial representation learning</td>
<td width="240">3D-grounded policy/perception</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2504.08531">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2503.10745">Unifying 2D and 3D Vision-Language Understanding</a></td>
<td width="420">Unifying 2D and 3D Vision-Language Understanding connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td width="230">-</td>
<td width="240">3D/spatial grounding</td>
<td width="300">3D representation / 3D grounding</td>
<td width="260">-</td>
<td width="240">3D-grounded policy/perception</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2503.10745">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2505.04119">GAPrompt: Geometry-Aware Point Cloud Prompt for 3D Vision Model</a></td>
<td width="420">GAPrompt connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td width="230">-</td>
<td width="240">AR</td>
<td width="300">3D representation / 3D grounding</td>
<td width="260">3D/spatial representation learning</td>
<td width="240">3D-grounded policy/perception</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2505.04119">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2412.00174">SOLAMI: Social Vision-Language-Action Modeling for Immersive Interaction with 3D Autonomous Characters</a></td>
<td width="420">SOLAMI connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td width="230">No specific base VLA specified.</td>
<td width="240">AR</td>
<td width="300">VLA / 3D representation / 3D grounding</td>
<td width="260">-</td>
<td width="240">3D-grounded policy/perception</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2412.00174">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2501.03841">OmniManip: Towards General Robotic Manipulation via Object-Centric Interaction Primitives as Spatial Constraints</a></td>
<td width="420">OmniManip connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td width="230">No specific base VLA specified.</td>
<td width="240">AR</td>
<td width="300">VLA / 3D grounding</td>
<td width="260">Affordance grounding</td>
<td width="240">3D-grounded policy/perception</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2501.03841">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/pdf/2504.21530">RoboGround: Robot Manipulation with Grounded Vision-Language Priors</a></td>
<td width="420">RoboGround uses vision-language grounding masks as intermediate spatial priors for generalizable manipulation policies.</td>
<td width="230">-</td>
<td width="240">-</td>
<td width="300">VLA / 3D grounding</td>
<td width="260">-</td>
<td width="240">-</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2406.18158">3D-MVP: 3D Multiview Pretraining for Robotic Manipulation</a></td>
<td width="420">3D-MVP connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td width="230">-</td>
<td width="240">3D/spatial grounding</td>
<td width="300">3D representation / 3D grounding</td>
<td width="260">Generative action modeling</td>
<td width="240">3D-grounded policy/perception</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2406.18158">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2503.07135">VidBot: Learning Generalizable 3D Actions from In-the-Wild 2D Human Videos for Zero-Shot Robotic Manipulation</a></td>
<td width="420">VidBot connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td width="230">-</td>
<td width="240">AR</td>
<td width="300">3D representation / 3D grounding</td>
<td width="260">Diffusion policy</td>
<td width="240">Diffusion policy</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2503.07135">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2412.05507">AutoURDF: Unsupervised Robot Modeling from Point Cloud Frames Using Cluster Registration</a></td>
<td width="420">AutoURDF connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td width="230">-</td>
<td width="240">3D/spatial grounding</td>
<td width="300">3D grounding</td>
<td width="260">3D/spatial representation learning</td>
<td width="240">3D-grounded policy/perception</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2412.05507">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
</tbody>
</table>
