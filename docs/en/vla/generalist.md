# generalist VLA

[Home](../../../README.md) | [中文](../../zh-CN/vla/generalist.md) | [Direction index](README.md)

Total: 80 papers.

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
<td width="120" nowrap>LangRob @ CoRL 2023</td>
<td width="320"><a href="https://openreview.net/forum?id=3mKb5iyZ2V">Reasoning Tuning Grasp: Adapting Multi-Modal Large Language Models for Robotic Grasping</a></td>
<td width="420">Tunes an MLLM to reason about and emit numerical planar grasp poses for a two-finger gripper.</td>
<td width="230">LLaVA-7B-v0 + CLIP ViT-L/14</td>
<td width="240">image grasp point [x,y] + end-effector rotation</td>
<td width="300">Cornell: 885 images/240 objects with 74 reasoning categories; LoRA reasoning tuning; 135 real trials</td>
<td width="260">reasoning-tuned multimodal LLM grasp prediction</td>
<td width="240">parallel-gripper grasp-pose VLM; not a dexterous-hand controller</td>
<td width="200">offline benchmark + Real; no physics simulator</td>
<td width="360">Cornell image/object accuracy 84.05±0.78/77.02±0.93%; real LoRA 113/135 = 83.7%</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=3mKb5iyZ2V">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">Cornell Grasp Dataset; 27 unseen objects × 5 poses</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2022</td>
<td width="320"><a href="https://arxiv.org/abs/2109.12098">CLIPort: What and Where Pathways for Robotic Manipulation</a></td>
<td width="420">CLIPort combines CLIP semantics with transport-style spatial manipulation policies.</td>
<td width="230">CLIPort</td>
<td width="240">robot action</td>
<td width="300">VLA / generalist VLA</td>
<td width="260">CoRL robot-learning method</td>
<td width="240">robot policy</td>
<td width="200">robot benchmarks</td>
<td width="360">Add CoRL VLA coverage.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2109.12098">paper</a></td>
<td width="110" nowrap><a href="https://cliport.github.io">project</a></td>
<td width="110" nowrap><a href="https://github.com/cliport/cliport">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2024</td>
<td width="320"><a href="https://arxiv.org/abs/2406.09246">OpenVLA: An Open-Source Vision-Language-Action Model</a></td>
<td width="420">OpenVLA is an open-source VLA model for general robot manipulation.</td>
<td width="230">OpenVLA</td>
<td width="240">robot action</td>
<td width="300">VLA / generalist VLA</td>
<td width="260">CoRL robot-learning method</td>
<td width="240">robot policy</td>
<td width="200">robot benchmarks</td>
<td width="360">Add CoRL VLA coverage.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2406.09246">paper</a></td>
<td width="110" nowrap><a href="https://openvla.github.io">project</a></td>
<td width="110" nowrap><a href="https://github.com/openvla/openvla">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2023</td>
<td width="320"><a href="https://arxiv.org/abs/2307.15818">RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control</a></td>
<td width="420">RT-2 transfers web-scale vision-language knowledge into robotic control.</td>
<td width="230">RT-2</td>
<td width="240">robot action</td>
<td width="300">VLA / generalist VLA</td>
<td width="260">CoRL robot-learning method</td>
<td width="240">robot policy</td>
<td width="200">robot benchmarks</td>
<td width="360">Add CoRL VLA coverage.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2307.15818">paper</a></td>
<td width="110" nowrap><a href="https://robotics-transformer2.github.io">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2508.19958">Long-VLA: Unleashing Long-Horizon Capability of Vision Language Action Model for Robot Manipulation</a></td>
<td width="420">Long-VLA targets long-horizon robot manipulation with VLA policies.</td>
<td width="230">Long-VLA</td>
<td width="240">robot action</td>
<td width="300">VLA / generalist VLA</td>
<td width="260">CoRL robot-learning method</td>
<td width="240">robot policy</td>
<td width="200">robot benchmarks</td>
<td width="360">Add CoRL VLA coverage.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2508.19958">paper</a></td>
<td width="110" nowrap><a href="https://long-vla.github.io/">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2021</td>
<td width="320"><a href="https://arxiv.org/abs/2202.02005">BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning</a></td>
<td width="420">BC-Z studies zero-shot task generalization with robotic imitation learning.</td>
<td width="230">BC-Z</td>
<td width="240">robot action</td>
<td width="300">VLA / generalist VLA</td>
<td width="260">CoRL robot-learning method</td>
<td width="240">robot policy</td>
<td width="200">robot benchmarks</td>
<td width="360">Add CoRL VLA coverage.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2202.02005">paper</a></td>
<td width="110" nowrap><a href="https://sites.google.com/view/bc-z/home">project</a></td>
<td width="110" nowrap><a href="https://github.com/google-research/tensor2robot/tree/master/research/bcz">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2022</td>
<td width="320"><a href="https://arxiv.org/abs/2209.04899">Hiveformer: Instruction-driven history-aware policies for robotic manipulations</a></td>
<td width="420">Hiveformer builds history-aware instruction-conditioned policies for robotic manipulation.</td>
<td width="230">Hiveformer</td>
<td width="240">robot action</td>
<td width="300">VLA / generalist VLA</td>
<td width="260">CoRL robot-learning method</td>
<td width="240">robot policy</td>
<td width="200">robot benchmarks</td>
<td width="360">Add CoRL VLA coverage.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2209.04899">paper</a></td>
<td width="110" nowrap><a href="https://vlc-robot.github.io/hiveformer-corl/">project</a></td>
<td width="110" nowrap><a href="https://github.com/vlc-robot/hiveformer">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2023</td>
<td width="320"><a href="https://arxiv.org/abs/2303.00905">Open-World Object Manipulation using Pre-trained Vision-Language Models</a></td>
<td width="420">MOO studies open-world object manipulation with pretrained vision-language models.</td>
<td width="230">Open-World Object Manipulation using Pre-trained Vision-Language Models</td>
<td width="240">robot action</td>
<td width="300">VLA / generalist VLA</td>
<td width="260">CoRL robot-learning method</td>
<td width="240">robot policy</td>
<td width="200">robot benchmarks</td>
<td width="360">Add CoRL VLA coverage.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2303.00905">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2024</td>
<td width="320"><a href="https://arxiv.org/abs/2410.05273">HiRT: Enhancing Robotic Control with Hierarchical Robot Transformers</a></td>
<td width="420">HiRT uses hierarchical robot transformers to improve robotic control.</td>
<td width="230">HiRT</td>
<td width="240">robot action</td>
<td width="300">VLA / generalist VLA</td>
<td width="260">CoRL robot-learning method</td>
<td width="240">robot policy</td>
<td width="200">robot benchmarks</td>
<td width="360">Add CoRL VLA coverage.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2410.05273">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2023</td>
<td width="320"><a href="https://arxiv.org/abs/2307.14535">Scaling Up and Distilling Down: Language-Guided Robot Skill Acquisition</a></td>
<td width="420">SUDD scales language-guided robot skill acquisition and distills it into executable policies.</td>
<td width="230">Scaling Up and Distilling Down</td>
<td width="240">robot action</td>
<td width="300">VLA / generalist VLA</td>
<td width="260">CoRL robot-learning method</td>
<td width="240">robot policy</td>
<td width="200">robot benchmarks</td>
<td width="360">Add CoRL VLA coverage.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2307.14535">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/real-stanford/scalingup">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2024</td>
<td width="320"><a href="https://openaccess.thecvf.com/content/CVPR2024/html/Li_ManipLLM_Embodied_Multimodal_Large_Language_Model_for_Object-Centric_Robotic_Manipulation_CVPR_2024_paper.html">ManipLLM: Embodied Multimodal Large Language Model for Object-Centric Robotic Manipulation</a></td>
<td width="420">ManipLLM grounds multimodal language reasoning in object-centric robotic manipulation.</td>
<td width="230">multimodal LLM</td>
<td width="240">robot action</td>
<td width="300">VLA / Generalist VLA</td>
<td width="260">object-centric embodied reasoning</td>
<td width="240">robot manipulation policy</td>
<td width="200">simulation manipulation</td>
<td width="360">Use multimodal LLM reasoning for object-centric manipulation.</td>
<td width="110" nowrap><a href="https://openaccess.thecvf.com/content/CVPR2024/papers/Li_ManipLLM_Embodied_Multimodal_Large_Language_Model_for_Object-Centric_Robotic_Manipulation_CVPR_2024_paper.pdf">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2024</td>
<td width="320"><a href="https://proceedings.neurips.cc/paper_files/paper/2024/hash/62203a74e233e933b160711e791e1a02-Abstract-Conference.html">PEAC: Unsupervised Pre-training for Cross-Embodiment Reinforcement Learning</a></td>
<td width="420">PEAC pretrains policies across embodiments to improve transfer before downstream robot learning.</td>
<td width="230">cross-embodiment policy</td>
<td width="240">robot action</td>
<td width="300">VLA / cross-embodiment</td>
<td width="260">unsupervised pretraining</td>
<td width="240">generalist robot policy</td>
<td width="200">cross-embodiment benchmarks</td>
<td width="360">Improve cross-embodiment policy transfer.</td>
<td width="110" nowrap><a href="https://proceedings.neurips.cc/paper_files/paper/2024/file/62203a74e233e933b160711e791e1a02-Paper-Conference.pdf">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://openaccess.thecvf.com/content/ICCV2025/html/Chen_CombatVLA_An_Efficient_Vision-Language-Action_Model_for_Combat_Tasks_in_3D_ICCV_2025_paper.html">CombatVLA: An Efficient Vision-Language-Action Model for Combat Tasks in 3D Action Role-Playing Games</a></td>
<td width="420">CombatVLA studies efficient VLA control for real-time 3D game combat tasks.</td>
<td width="230">CombatVLA</td>
<td width="240">game action</td>
<td width="300">VLA / Generalist VLA</td>
<td width="260">efficient VLA control</td>
<td width="240">real-time embodied agent</td>
<td width="200">3D game tasks</td>
<td width="360">Evaluate VLA-style action models in fast 3D interactive tasks.</td>
<td width="110" nowrap><a href="https://openaccess.thecvf.com/content/ICCV2025/papers/Chen_CombatVLA_An_Efficient_Vision-Language-Action_Model_for_Combat_Tasks_in_3D_ICCV_2025_paper.pdf">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2024</td>
<td width="320"><a href="https://openreview.net/forum?id=lFYj0oibGR">Vision-Language Foundation Models as Effective Robot Imitators</a></td>
<td width="420">This work adapts vision-language foundation models as robot imitators for manipulation policies.</td>
<td width="230">VLM foundation model</td>
<td width="240">robot action</td>
<td width="300">imitation learning</td>
<td width="260">VLM-to-policy adaptation</td>
<td width="240">robot imitation policy</td>
<td width="200">robot manipulation benchmarks</td>
<td width="360">Use pretrained VLMs as effective robot imitation learners.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=lFYj0oibGR">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2023</td>
<td width="320"><a href="https://arxiv.org/abs/2311.01977">RT-Trajectory: Robotic Task Generalization via Hindsight Trajectory Sketches</a></td>
<td width="420">RT-Trajectory uses hindsight trajectory sketches to improve robot task generalization.</td>
<td width="230">robot policy</td>
<td width="240">trajectory sketches</td>
<td width="300">VLA / Generalist VLA</td>
<td width="260">hindsight trajectory conditioning</td>
<td width="240">generalist manipulation policy</td>
<td width="200">robot manipulation tasks</td>
<td width="360">Improve task generalization with trajectory sketch supervision.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2311.01977">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2023</td>
<td width="320"><a href="https://openreview.net/forum?id=nkDMZ8yqBt">VIMA: General Robot Manipulation with Multimodal Prompts</a></td>
<td width="420">VIMA formulates robot manipulation as multimodal prompt-conditioned policy learning.</td>
<td width="230">VIMA</td>
<td width="240">manipulation action</td>
<td width="300">multimodal prompt policy</td>
<td width="260">prompt-conditioned imitation</td>
<td width="240">generalist manipulation policy</td>
<td width="200">VIMA-Bench</td>
<td width="360">Use multimodal prompts to specify diverse manipulation tasks.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=nkDMZ8yqBt">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2025</td>
<td width="320"><a href="https://proceedings.iclr.cc/paper_files/paper/2025/hash/8667f264f88c7938a73a53ab01eb1327-Abstract-Conference.html">TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies</a></td>
<td width="420">TraceVLA adds visual trace prompts to improve spatial-temporal awareness in generalist robot policies.</td>
<td width="230">generalist VLA</td>
<td width="240">robot action</td>
<td width="300">VLA / Generalist VLA</td>
<td width="260">visual trace prompting</td>
<td width="240">generalist robot policy</td>
<td width="200">robot manipulation benchmarks</td>
<td width="360">Enhance robot policy awareness with visual traces.</td>
<td width="110" nowrap><a href="https://proceedings.iclr.cc/paper_files/paper/2025/hash/8667f264f88c7938a73a53ab01eb1327-Abstract-Conference.html">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ECCV 2024</td>
<td width="320"><a href="https://openreview.net/forum?id=Sa7upAJOIN">QUAR-VLA: Vision-Language-Action Model for Quadruped Robots</a></td>
<td width="420">QUAR-VLA extends VLA-style policy learning to quadruped robot control.</td>
<td width="230">quadruped VLA</td>
<td width="240">locomotion action</td>
<td width="300">VLA / quadruped robots</td>
<td width="260">vision-language-action control</td>
<td width="240">quadruped policy</td>
<td width="200">quadruped robot tasks</td>
<td width="360">Apply VLA modeling to quadruped embodied control.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=Sa7upAJOIN">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2508.05186">Learning to See and Act: Task-Aware Virtual View Exploration for Robotic Manipulation</a></td>
<td width="420">This work uses task-aware virtual view exploration to improve perception and action in manipulation.</td>
<td width="230">robot manipulation model</td>
<td width="240">manipulation action</td>
<td width="300">VLA / Generalist VLA</td>
<td width="260">virtual-view exploration</td>
<td width="240">robot manipulation policy</td>
<td width="200">manipulation benchmarks</td>
<td width="360">Use task-aware view exploration for better manipulation policy inputs.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2508.05186">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>IROS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2409.12514">TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation</a></td>
<td width="420">TinyVLA combines a compact VLA with diffusion policy to improve data efficiency and inference speed for robot manipulation.</td>
<td width="230">TinyVLA</td>
<td width="240">Diffusion action</td>
<td width="300">VLA / Generalist VLA</td>
<td width="260">compact VLA + diffusion policy</td>
<td width="240">data-efficient VLA</td>
<td width="200">Real robot manipulation</td>
<td width="360">Build a smaller, faster, data-efficient VLA manipulation policy.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2409.12514">paper</a></td>
<td width="110" nowrap><a href="https://tiny-vla.github.io/">project</a></td>
<td width="110" nowrap><a href="https://github.com/JayceWen/tinyvla">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2502.05485">HAMSTER: Hierarchical Action Models For Open-World Robot Manipulation</a></td>
<td width="420">HAMSTER uses hierarchical action models to connect high-level open-world manipulation decisions with executable low-level robot actions.</td>
<td width="230">HAMSTER</td>
<td width="240">hierarchical action</td>
<td width="300">VLA / Generalist VLA</td>
<td width="260">hierarchical action modeling</td>
<td width="240">open-world manipulation policy</td>
<td width="200">robot manipulation benchmarks</td>
<td width="360">Build an open-world robot manipulation policy with explicit action hierarchy.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2502.05485">paper</a></td>
<td width="110" nowrap><a href="https://hamster-robot.github.io/">project</a></td>
<td width="110" nowrap><a href="https://github.com/liyi14/HAMSTER_beta">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2406.20095">LLaRA: Supercharging Robot Learning Data for Vision-Language Policy</a></td>
<td width="420">LLaRA improves vision-language policy learning by converting and enriching robot learning data for VLA training.</td>
<td width="230">LLaRA</td>
<td width="240">policy action</td>
<td width="300">VLA / Generalist VLA</td>
<td width="260">robot-data augmentation for VLP/VLA</td>
<td width="240">vision-language policy</td>
<td width="200">robot learning datasets</td>
<td width="360">Improve robot policy learning through stronger language-aligned training data.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2406.20095">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/LostXine/LLaRA">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=54U3XHf7qq">MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation</a></td>
<td width="420">It proposes a VLA with working memory and a long-term perceptual-cognitive memory bank, enabling long-horizon manipulation to use historical context when generating actions.</td>
<td width="230">VLM + diffusion action expert</td>
<td width="240">Diffusion action sequences</td>
<td width="300">VLA / Generalist VLA</td>
<td width="260">Cognition-Memory-Action + Perceptual-Cognitive Memory Bank</td>
<td width="240">memory-conditioned VLA</td>
<td width="200">Sim + Real</td>
<td width="360">Historical memory modeling for long-horizon robot manipulation.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=54U3XHf7qq">paper</a></td>
<td width="110" nowrap><a href="https://shihao1895.github.io/MemoryVLA">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=DdrsHWobR1">Disentangled Robot Learning via Separate Forward and Inverse Dynamics Pretraining</a></td>
<td width="420">DeFI decouples visual forward dynamics and inverse dynamics pretraining, then jointly fine-tunes them for action prediction.</td>
<td width="230">DeFI</td>
<td width="240">latent action / inverse dynamics</td>
<td width="300">VLA / Generalist VLA</td>
<td width="260">GFDM + GIDM disentangled pretraining</td>
<td width="240">forward-inverse dynamics VLA</td>
<td width="200">Sim + Real</td>
<td width="360">Improve generalization by decoupling video prediction and action prediction.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=DdrsHWobR1">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=IBJtOltTbx">Hybrid Training for Vision-Language-Action Models</a></td>
<td width="420">HyT lets the VLA learn from CoT reasoning trajectories while allowing direct action output at test time to keep inference fast.</td>
<td width="230">-</td>
<td width="240">AR/direct action</td>
<td width="300">VLA / Generalist VLA</td>
<td width="260">Hybrid Training</td>
<td width="240">CoT-trained direct-action VLA</td>
<td width="200">Sim + Real</td>
<td width="360">Reduce VLA inference latency while retaining reasoning benefits.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=IBJtOltTbx">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=LYyoRqf0Ij">End-to-end Listen, Look, Speak and Act</a></td>
<td width="420">ELLSA uses SA-MoE to perceive and generate vision, text, speech, and actions within a single architecture.</td>
<td width="230">ELLSA</td>
<td width="240">multimodal action generation</td>
<td width="300">VLA / Generalist VLA</td>
<td width="260">SA-MoE</td>
<td width="240">full-duplex omni-modal VLA</td>
<td width="200">speech-interaction + robot benchmarks</td>
<td width="360">End-to-end multimodal interaction and action generation.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=LYyoRqf0Ij">paper</a></td>
<td width="110" nowrap><a href="https://anonymous.4open.science/r/LLSA-E821">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=OJh7oBCYhL">RoboOmni: Proactive Robot Manipulation in Omni-modal Context</a></td>
<td width="420">RoboOmni proactively infers intent from speech, ambient sound, and visual cues, then executes manipulation.</td>
<td width="230">omni-modal LLM</td>
<td width="240">executor action</td>
<td width="300">VLA / Generalist VLA</td>
<td width="260">Perceiver-Thinker-Talker-Executor</td>
<td width="240">proactive omni-modal VLA</td>
<td width="200">-</td>
<td width="360">Proactive robot manipulation in cross-modal context.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=OJh7oBCYhL">paper</a> / <a href="https://arxiv.org/pdf/2510.23763">paper</a></td>
<td width="110" nowrap><a href="https://openmoss.github.io/RoboOmni/">project</a></td>
<td width="110" nowrap><a href="https://github.com/OpenMOSS/RoboOmni">code</a></td>
<td width="240"><a href="https://huggingface.co/OpenMOSS-Team/RoboOmni">hf</a> / <a href="https://huggingface.co/datasets/fnlp/OmniAction">hf</a></td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=PklMD8PwUy">Unified Vision-Language-Action Model</a></td>
<td width="420">UniVLA unifies vision, language, and actions as discrete token sequences and uses world-model post-training to improve long-horizon policy learning.</td>
<td width="230">UniVLA</td>
<td width="240">discrete token AR</td>
<td width="300">VLA / Efficient/Lightweight VLA</td>
<td width="260">unified multimodal token modeling + world-model post-training</td>
<td width="240">autoregressive unified VLA</td>
<td width="200">CALVIN/LIBERO/SimplerEnv + ALOHA real</td>
<td width="360">Addresses the problem that traditional VLAs over-rely on VLM semantics and ignore temporal causal structure in vision.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=PklMD8PwUy">paper</a> / <a href="https://arxiv.org/abs/2503.10631">paper</a> / <a href="https://arxiv.org/abs/2506.19850">paper</a></td>
<td width="110" nowrap><a href="https://hybrid-vla.github.io/">project</a> / <a href="https://robertwyq.github.io/univla.github.io/">project</a></td>
<td width="110" nowrap><a href="https://github.com/PKU-HMI-Lab/Hybrid-VLA">code</a> / <a href="https://github.com/baaivision/UniVLA">code</a></td>
<td width="240">CALVIN/LIBERO/SimplerEnv/ALOHA</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=T3i7Ifeatk">Align-Then-stEer: Adapting the Vision-Language Action Models through Unified Latent Guidance</a></td>
<td width="420">ATE first aligns different action spaces, then uses a unified latent space to guide diffusion/flow VLA adaptation to new tasks and embodiments.</td>
<td width="230">pretrained diffusion/flow VLA</td>
<td width="240">latent action guidance</td>
<td width="300">VLA / Efficient/Lightweight VLA</td>
<td width="260">Align-Then-stEer / reverse-KL VAE latent alignment</td>
<td width="240">plug-in adaptation</td>
<td width="200">Sim + Real</td>
<td width="360">Addresses action-distribution mismatch and high data/compute cost in downstream adaptation of pretrained VLAs.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=T3i7Ifeatk">paper</a> / <a href="https://arxiv.org/abs/2509.02055">paper</a></td>
<td width="110" nowrap><a href="https://align-then-steer.github.io/">project</a></td>
<td width="110" nowrap><a href="https://github.com/TeleHuman/Align-Then-Steer">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=UD4Rw8MOEK">Verifier-free Test-Time Sampling for Vision Language Action Models</a></td>
<td width="420">MG-Select uses KL confidence from the model's internal masked reference action distribution to select action candidates at test time.</td>
<td width="230">-</td>
<td width="240">AR candidate selection</td>
<td width="300">VLA / Generalist VLA</td>
<td width="260">MG-Select / masking distribution guided selection</td>
<td width="240">verifier-free test-time scaling</td>
<td width="200">Sim + Real</td>
<td width="360">Test-time action selection without an extra verifier.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=UD4Rw8MOEK">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=kt51kZH4aG">X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model</a></td>
<td width="420">X-VLA uses embodiment-specific soft prompts and a flow-matching Transformer to learn general control across robot platforms.</td>
<td width="230">X-VLA</td>
<td width="240">flow-matching continuous action</td>
<td width="300">VLA / Generalist VLA</td>
<td width="260">embodiment-specific soft prompts</td>
<td width="240">cross-embodiment VLA</td>
<td width="200">6 sim envs + 3 real platforms</td>
<td width="360">Cross-embodiment VLA training and generalization.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=kt51kZH4aG">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=tc2UsBeODW">VLM4VLA: Revisiting Vision-Language-Models in Vision-Language-Action Models</a></td>
<td width="420">VLM4VLA systematically compares transfer performance when different VLMs serve as VLA backbones, showing that general VLM capability does not directly predict control performance.</td>
<td width="230">VLM4VLA minimal adapter</td>
<td width="240">policy action</td>
<td width="300">VLA / Generalist VLA</td>
<td width="260">minimal VLM-to-VLA adaptation + embodied capability ablation</td>
<td width="240">benchmark/adaptation pipeline</td>
<td width="200">3 benchmarks</td>
<td width="360">Evaluate the real contribution of the VLM backbone to VLA control.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=tc2UsBeODW">paper</a></td>
<td width="110" nowrap><a href="https://cladernyjorn.github.io/VLM4VLA.github.io/">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=tsxwloasw5">Vision-Language-Action Instruction Tuning: From Understanding to Manipulation</a></td>
<td width="420">InstructVLA uses VLA instruction tuning to preserve VLM reasoning capability while improving fine-grained manipulation performance.</td>
<td width="230">InstructVLA</td>
<td width="240">AR/action generation</td>
<td width="300">VLA / RL/Online Fine-tuning</td>
<td width="260">VLA-IT + MoE adaptation</td>
<td width="240">end-to-end instruction-tuned VLA</td>
<td width="200">-</td>
<td width="360">Addresses the tradeoff between visual-language understanding and action generation in VLAs, and their tendency to forget pretrained capabilities.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=tsxwloasw5">paper</a> / <a href="https://arxiv.org/abs/2507.17520">paper</a></td>
<td width="110" nowrap><a href="https://yangs03.github.io/InstructVLA_Home/">project</a></td>
<td width="110" nowrap><a href="https://github.com/InternRobotics/InstructVLA">code</a></td>
<td width="240">650K VLA-IT dataset</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=KcJ9U0x6kO">HAMLET: Switch Your Vision-Language-Action Model into a History-Aware Policy</a></td>
<td width="420">HAMLET uses moment tokens and a lightweight memory module to turn a current-frame-only VLA into a history-aware policy.</td>
<td width="230">GR00T N1.5 / pretrained VLA</td>
<td width="240">history-aware action prediction</td>
<td width="300">VLA / Generalist VLA</td>
<td width="260">moment tokens + time-contrastive init + memory module</td>
<td width="240">history-aware VLA adapter</td>
<td width="200">RoboCasa/LIBERO + real</td>
<td width="360">Long-horizon manipulation with historical dependencies.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=KcJ9U0x6kO">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38902">DiTEA: Mixture-of-Experts for Vision-Language-Action Model in Robotic Manipulation</a></td>
<td width="420">DiTEA adds Action MoE and task-instruction gating to a diffusion VLA action head to reduce multi-task forgetting.</td>
<td width="230">diffusion-based VLA</td>
<td width="240">Diffusion</td>
<td width="300">VLA / Generalist VLA</td>
<td width="260">Diffusion Transformer Action MoE + Task-Instruction Gate</td>
<td width="240">MoE VLA</td>
<td width="200">Sim + Real</td>
<td width="360">Instruction following and forgetting resistance for multi-task diffusion VLAs.</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38902">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38910">TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for Vision-Language-Action Models</a></td>
<td width="420">TTF-VLA fuses historical and current visual tokens without training, improving VLA reasoning quality under noise and temporal scenarios.</td>
<td width="230">OpenVLA / VLA-Cache</td>
<td width="240">token-level inference enhancement</td>
<td width="300">VLA / Generalist VLA</td>
<td width="260">Temporal Token Fusion + pixel difference + attention relevance</td>
<td width="240">training-free inference plugin</td>
<td width="200">LIBERO + SimplerEnv + Real</td>
<td width="360">Temporal visual token fusion.</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38910">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/62813">Being-H0: Vision-Language-Action Pretraining from Large-Scale Human Videos</a></td>
<td width="420">Being-H0 performs physical instruction tuning and hand-motion tokenization on large-scale human-hand videos, then transfers to dexterous manipulation.</td>
<td width="230">Being-H0</td>
<td width="240">part-level motion tokens / AR</td>
<td width="300">VLA / RL/Online Fine-tuning</td>
<td width="260">physical instruction tuning + hand motion tokenization</td>
<td width="240">dexterous VLA</td>
<td width="200">human video pretrain + real robot</td>
<td width="360">Addresses VLA dependence on expensive robot demonstrations and weak generalization in dexterous manipulation.</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/62813">paper</a> / <a href="https://arxiv.org/pdf/2507.15597">paper</a> / <a href="https://arxiv.org/abs/2507.15597">paper</a></td>
<td width="110" nowrap><a href="https://beingbeyond.github.io/Being-H0">project</a> / <a href="https://beingbeyond.github.io/Being-H0/">project</a></td>
<td width="110" nowrap><a href="https://github.com/BeingBeyond/Being-H0">code</a></td>
<td width="240">BeingBeyond h0_post_train dataset</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/60980">RA-VLA: Retrieval-Augmented VLA for Test-Time Adaptation</a></td>
<td width="420">RA-VLA uses behavior-aligned retrieval and a grounded execution pipeline for training-free test-time adaptation to new task distributions.</td>
<td width="230">RA-VLA</td>
<td width="240">retrieval-grounded action</td>
<td width="300">VLA / Generalist VLA</td>
<td width="260">behavior-aligned retrieval + grounded execution</td>
<td width="240">test-time adaptation VLA</td>
<td width="200">LIBERO + UR5e real</td>
<td width="360">Training-free test-time adaptation.</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/60980">paper</a></td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/60980">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/62270">A Generalist Pair-wise Progress Critic Model for Vision-Language-Action Robots</a></td>
<td width="420">VLAC unifies the action policy and pairwise task-progress critic in an autoregressive architecture, providing intrinsic rewards for RL.</td>
<td width="230">VLAC</td>
<td width="240">AR</td>
<td width="300">VLA / RL/Online Fine-tuning</td>
<td width="260">pair-wise progress critic + intrinsic reward RL</td>
<td width="240">action-critic VLA</td>
<td width="200">diverse tasks + real RL</td>
<td width="360">General task-progress assessment and action generation.</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/62270">paper</a></td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/62270">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/62528">Bring My Cup! Personalizing Vision-Language-Action Models with Visual Attentive Prompting</a></td>
<td width="420">VAP uses a small number of reference images as visual memory, injecting target-instance attention into a frozen VLA to execute personalized instructions.</td>
<td width="230">frozen VLA</td>
<td width="240">visual-prompted action</td>
<td width="300">VLA / Generalist VLA</td>
<td width="260">Visual Attentive Prompting</td>
<td width="240">training-free personalization adapter</td>
<td width="200">Personalized-SIMPLER/Personalized-VLABench + real</td>
<td width="360">Personalized object manipulation.</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/62528">paper</a></td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/62528">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">Personalized-SIMPLER</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/66596">From Abstraction to Instantiation: Learning Behavioral Representation for Vision-Language-Action Model</a></td>
<td width="420">BehaviorVLA learns long-horizon behavior representations and decodes them by execution phase into precise actions to improve out-of-distribution generalization.</td>
<td width="230">BehaviorVLA</td>
<td width="240">AR / behavior-conditioned decoding</td>
<td width="300">VLA / Generalist VLA</td>
<td width="260">VBE + PBD</td>
<td width="240">behavior-representation VLA</td>
<td width="200">RoboTwin2/LIBERO/CALVIN + real sim2real</td>
<td width="360">Temporally consistent behavior representation.</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/66596">paper</a></td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/66596">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/61157">VLA-ATTC: Adaptive Test-Time Compute for VLA Models with Relative Action Critic Model</a></td>
<td width="420">VLA-ATTC triggers test-time thinking with uncertainty and uses a relative-action critic to pick the best candidate action.</td>
<td width="230">PI0.5 / VLA</td>
<td width="240">candidate action selection</td>
<td width="300">VLA / Generalist VLA</td>
<td width="260">adaptive TTC + Relative Action Critic</td>
<td width="240">test-time compute VLA</td>
<td width="200">LIBERO-LONG</td>
<td width="360">Adaptive test-time computation and action selection.</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/61157">paper</a></td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/61157">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/66066">SCALE: Self-uncertainty Conditioned Adaptive Looking and Execution for Vision-Language-Action Models</a></td>
<td width="420">SCALE uses the VLA's own uncertainty to jointly regulate visual perception and action exploration/exploitation in a single forward pass.</td>
<td width="230">generic VLA</td>
<td width="240">adaptive execution</td>
<td width="300">VLA / RL/Online Fine-tuning</td>
<td width="260">self-uncertainty conditioned adaptive looking/execution</td>
<td width="240">training-free single-pass inference strategy</td>
<td width="200">Sim + Real</td>
<td width="360">Training-free robust execution at test time.</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/66066">paper</a></td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/66066">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/64826">XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations</a></td>
<td width="420">XR-1 learns unified vision-motion codes to train versatile VLA policies across heterogeneous robots, tasks, and demonstrations.</td>
<td width="230">-</td>
<td width="240">AR</td>
<td width="300">VLA / Generalist VLA</td>
<td width="260">-</td>
<td width="240">-</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/64826">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/66510">Escaping the Diversity Trap in Robotic Manipulation via Anchor-Centric Adaptation</a></td>
<td width="420">ACA shows that blindly pursuing demonstration diversity under a small budget causes density gaps, then adapts by repeating anchor demonstrations and expanding boundaries.</td>
<td width="230">VLA adaptation</td>
<td width="240">residual updates</td>
<td width="300">generalist VLA / general-purpose VLA</td>
<td width="260">Anchor-Centric Adaptation</td>
<td width="240">data-efficient real-robot adaptation</td>
<td width="200">Real</td>
<td width="360">Low-budget embodiment adaptation.</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/66510">paper</a></td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/66510">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/63997">Embodied Interpretability: Linking Causal Understanding to Generalization in Vision-Language-Action Models</a></td>
<td width="420">This paper uses interventional masking to estimate the causal effect of visual regions on action prediction and uses NMR to predict generalization.</td>
<td width="230">-</td>
<td width="240">diagnostic not action representation</td>
<td width="300">VLA / Generalist VLA</td>
<td width="260">ISS + NMR</td>
<td width="240">interpretability/diagnostic</td>
<td width="200">manipulation tasks</td>
<td width="360">Causal attribution and generalization diagnosis for VLAs.</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/63997">paper</a></td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/63997">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2511.04555">Evo-1: Lightweight Vision-Language-Action Model with Preserved Semantic Alignment</a></td>
<td width="420">Evo-1 targets lightweight VLAs, preserving language-vision semantic alignment and manipulation ability while compressing model size.</td>
<td width="230">Evo-1</td>
<td width="240">-</td>
<td width="300">VLA / Efficient/Lightweight VLA</td>
<td width="260">-</td>
<td width="240">lightweight VLA</td>
<td width="200">-</td>
<td width="360">Preserving semantic alignment in lightweight VLAs.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2511.04555">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/MINT-SJTU/Evo-1">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2512.09928">HiF-VLA: Hindsight, Insight and Foresight through Motion Representation for Vision-Language-Action Models</a></td>
<td width="420">HiF-VLA introduces hindsight, insight, and foresight through motion representations to improve VLA understanding of action processes.</td>
<td width="230">HiF-VLA</td>
<td width="240">motion representation</td>
<td width="300">VLA / Generalist VLA</td>
<td width="260">hindsight/insight/foresight motion modeling</td>
<td width="240">-</td>
<td width="200">-</td>
<td width="360">Motion-representation-enhanced VLA.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2512.09928">paper</a></td>
<td width="110" nowrap><a href="https://hifvla.github.io/">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2603.12193">SaPaVe: Towards Active Perception and Manipulation in Vision-Language-Action Models for Robotics</a></td>
<td width="420">SaPaVe combines active perception and manipulation, enabling a VLA to look before acting in uncertain scenes.</td>
<td width="230">SaPaVe</td>
<td width="240">AR</td>
<td width="300">VLA / Generalist VLA</td>
<td width="260">active perception + manipulation</td>
<td width="240">-</td>
<td width="200">-</td>
<td width="360">Active-perception-driven manipulation.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2603.12193">paper</a></td>
<td width="110" nowrap><a href="https://lmzpai.github.io/SaPaVe">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2601.12796">Contact-Aware Neural Dynamics</a></td>
<td width="420">This paper learns contact-aware neural dynamics for modeling state changes in contact-rich manipulation.</td>
<td width="230">-</td>
<td width="240">AR</td>
<td width="300">contact-rich dynamics / robot manipulation</td>
<td width="260">contact-aware neural dynamics</td>
<td width="240">dynamics model, not generalist VLA</td>
<td width="200">-</td>
<td width="360">Contact-aware dynamics modeling.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2601.12796">paper</a></td>
<td width="110" nowrap><a href="https://changwei-jing.github.io/neural-physics/">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2508.21046">CogVLA: Cognition-Aligned Vision-Language-Action Model via Instruction-Driven Routing &amp; Sparsification</a></td>
<td width="420">CogVLA reduces VLA post-training overhead and improves efficiency through instruction-driven routing and sparsification.</td>
<td width="230">CogVLA</td>
<td width="240">AR</td>
<td width="300">VLA / Efficient/Lightweight VLA</td>
<td width="260">instruction-driven routing + sparsification</td>
<td width="240">efficient VLA</td>
<td width="200">-</td>
<td width="360">Addresses the high post-training and deployment compute cost of large VLM-based VLAs.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2508.21046">paper</a></td>
<td width="110" nowrap><a href="https://jiutian-vl.github.io/CogVLA-page/">project</a></td>
<td width="110" nowrap><a href="https://github.com/JiuTian-VL/CogVLA">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2505.15660">Exploring the Limits of Vision-Language-Action Manipulation in Cross-task Generalization</a></td>
<td width="420">This paper systematically evaluates the cross-task generalization limits of VLAs and proposes AGNOSTOS/X-ICM-related methods to improve generalization.</td>
<td width="230">AGNOSTOS / X-ICM</td>
<td width="240">-</td>
<td width="300">VLA / Generalist VLA</td>
<td width="260">-</td>
<td width="240">cross-task generalization study</td>
<td width="200">-</td>
<td width="360">Evaluation of cross-task generalization boundaries.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2505.15660">paper</a> / <a href="https://arxiv.org/pdf/2505.15660">paper</a></td>
<td width="110" nowrap><a href="https://jiaming-zhou.github.io/AGNOSTOS/">project</a> / <a href="https://jiaming-zhou.github.io/AGNOSTOS">project</a></td>
<td width="110" nowrap><a href="https://github.com/jiaming-zhou/X-ICM">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2505.15517">Robo2VLM: Improving Visual Question Answering using Large-Scale Robot Manipulation Data</a></td>
<td width="420">Robo2VLM uses large-scale robot manipulation data to improve VLM/VQA understanding of object states and actionability.</td>
<td width="230">-</td>
<td width="240">AR</td>
<td width="300">VLA / Generalist VLA</td>
<td width="260">-</td>
<td width="240">robot-data-enhanced VLM/VQA, not action policy</td>
<td width="200">-</td>
<td width="360">Enhancing visual question answering with robot manipulation data.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2505.15517">paper</a></td>
<td width="110" nowrap><a href="https://berkeleyautomation.github.io/robo2vlm/">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2506.22242">4D-VLA: Spatiotemporal Vision-Language-Action Pretraining with Cross-Scene Calibration</a></td>
<td width="420">4D-VLA mitigates state/coordinate confusion in cross-scene pretraining through RGB-D sequences, coordinate alignment, and memory-bank sampling.</td>
<td width="230">4D-VLA</td>
<td width="240">AR</td>
<td width="300">VLA / Generalist VLA</td>
<td width="260">4D spatiotemporal pretraining + cross-scene calibration + memory bank sampling</td>
<td width="240">-</td>
<td width="200">Sim + Real</td>
<td width="360">Addresses action distribution divergence caused by incomplete inputs in multi-source robot-data pretraining.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2506.22242">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/LogosRoboticsGroup/4D-VLA">code</a></td>
<td width="240">MV-Bench</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2510.24194">Blindfolded Experts Generalize Better: Insights from Robotic Manipulation and Videogames</a></td>
<td width="420">This paper studies why experts with reduced visual dependence generalize better in robotic manipulation and games.</td>
<td width="230">-</td>
<td width="240">-</td>
<td width="300">VLA / Generalist VLA</td>
<td width="260">blindfolded expert / reduced observation analysis</td>
<td width="240">generalization analysis</td>
<td width="200">-</td>
<td width="360">Relationship between visual dependence and generalization.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2510.24194">paper</a></td>
<td width="110" nowrap><a href="https://sites.google.com/view/blindfoldedexperts/home">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2510.11321">HiMaCon: Discovering Hierarchical Manipulation Concepts from Unlabeled Multi-Modal Data</a></td>
<td width="420">HiMaCon discovers hierarchical manipulation concepts from unlabeled multimodal data for structured representation of robot skills.</td>
<td width="230">-</td>
<td width="240">AR</td>
<td width="300">VLA / Generalist VLA</td>
<td width="260">hierarchical manipulation concept discovery</td>
<td width="240">concept representation</td>
<td width="200">Sim/Benchmark confirmed</td>
<td width="360">Unlabeled hierarchical manipulation-concept discovery.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2510.11321">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2505.23705">Knowledge Insulating Vision-Language-Action Models: Train Fast, Run Fast, Generalize Better</a></td>
<td width="420">This paper reduces VLA training and inference cost through knowledge isolation while improving generalization.</td>
<td width="230">-</td>
<td width="240">-</td>
<td width="300">VLA / Generalist VLA</td>
<td width="260">knowledge insulation</td>
<td width="240">efficient/generalist VLA</td>
<td width="200">-</td>
<td width="360">Faster training, faster inference, and improved generalization.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2505.23705">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://openreview.net/forum?id=3XuUnUEI7e">Diversifying Parallel Ergodic Search: A Signature Kernel Evolution Strategy</a></td>
<td width="420">This paper uses a signature-kernel evolution strategy to improve trajectory diversity and exploration efficiency in parallel ergodic search.</td>
<td width="230">-</td>
<td width="240">AR</td>
<td width="300">generalist VLA / general-purpose VLA</td>
<td width="260">Signature Kernel Evolution Strategy</td>
<td width="240">trajectory optimization/search, not VLA</td>
<td width="200">robotic benchmarks</td>
<td width="360">Diverse parallel ergodic search.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=3XuUnUEI7e">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://iccv.thecvf.com/virtual/2025/poster/1325">FedVLA: Federated Vision-Language-Action Learning with Dual Gating Mixture-of-Experts for Robotic Manipulation</a></td>
<td width="420">FedVLA trains VLAs on multi-client robot data using federated learning and dual-gated MoE.</td>
<td width="230">FedVLA</td>
<td width="240">AR</td>
<td width="300">VLA / Efficient/Lightweight VLA</td>
<td width="260">federated learning + dual-gating MoE</td>
<td width="240">federated VLA</td>
<td width="200">-</td>
<td width="360">Privacy-preserving/multi-client VLA learning.</td>
<td width="110" nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/1325">paper</a> / <a href="https://arxiv.org/abs/2508.02190">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://iccv.thecvf.com/virtual/2025/poster/225">PASG: A Closed-Loop Framework for Automated Geometric Primitive Extraction and Semantic Anchoring in Robotic Manipulation</a></td>
<td width="420">PASG automatically extracts geometric primitives and anchors them with VLM semantics, connecting geometric affordances with task semantics.</td>
<td width="230">VLM/Qwen2.5VL-PA</td>
<td width="240">-</td>
<td width="300">VLA / Generalist VLA</td>
<td width="260">Primitive-Aware Semantic Grounding</td>
<td width="240">semantic-affordance grounding framework</td>
<td width="200">benchmark</td>
<td width="360">Anchoring geometric primitives and semantic affordances.</td>
<td width="110" nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/225">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">spatial-semantic reasoning benchmark</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2503.07087">iManip: Skill-Incremental Learning for Robotic Manipulation</a></td>
<td width="420">iManip targets skill-incremental learning for robot manipulation, preserving old skills when new skills are added.</td>
<td width="230">-</td>
<td width="240">AR</td>
<td width="300">generalist VLA / general-purpose VLA</td>
<td width="260">incremental skill learning</td>
<td width="240">skill-incremental manipulation</td>
<td width="200">-</td>
<td width="360">Incremental learning for robot skills.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2503.07087">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://iccv.thecvf.com/virtual/2025/poster/972">4D Visual Pre-training for Robot Learning</a></td>
<td width="420">FVP sets visual pretraining as next-point-cloud prediction and uses a diffusion model to improve real-robot 3D representations and imitation-learning success rates.</td>
<td width="230">FVP + DP3</td>
<td width="240">3D policy support</td>
<td width="300">generalist VLA / general-purpose VLA</td>
<td width="260">next-point-cloud prediction diffusion pretraining</td>
<td width="240">4D visual pretraining</td>
<td width="200">Real manipulation</td>
<td width="360">4D/point-cloud visual pretraining.</td>
<td width="110" nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/972">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2502.19417">Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models</a></td>
<td width="420">Hi Robot uses a hierarchical VLA to decompose open-ended instructions into high-level planning and low-level action execution.</td>
<td width="230">hierarchical VLA</td>
<td width="240">AR</td>
<td width="300">VLA / Generalist VLA</td>
<td width="260">hierarchical policy/planning</td>
<td width="240">open-ended instruction following</td>
<td width="200">-</td>
<td width="360">Open-ended hierarchical instruction following.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2502.19417">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2025</td>
<td width="320"><a href="https://arxiv.org/pdf/2503.03734">OTTER: A Vision-Language-Action Model with Text-Aware Visual Feature Extraction</a></td>
<td width="420">OTTER uses text-aware visual feature extraction to make VLAs focus on image information relevant to the language goal.</td>
<td width="230">OTTER</td>
<td width="240">AR</td>
<td width="300">VLA / Generalist VLA</td>
<td width="260">text-aware visual feature extraction</td>
<td width="240">-</td>
<td width="200">-</td>
<td width="360">Text-aware visual feature extraction.</td>
<td width="110" nowrap><a href="https://arxiv.org/pdf/2503.03734">paper</a></td>
<td width="110" nowrap><a href="https://ottervla.github.io/">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2501.18867">UP-VLA: A Unified Understanding and Prediction Model for Embodied Agent</a></td>
<td width="420">UP-VLA unifies understanding and prediction tasks, giving embodied agents both semantic understanding and future/action prediction capability.</td>
<td width="230">UP-VLA</td>
<td width="240">-</td>
<td width="300">VLA / Generalist VLA</td>
<td width="260">-</td>
<td width="240">unified understanding-prediction model</td>
<td width="200">-</td>
<td width="360">Unified modeling of embodied understanding and prediction.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2501.18867">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/CladernyJorn/UP-VLA">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2411.18825">ELEMENTAL: Interactive Learning from Demonstrations and Vision-Language Models for Reward Design in Robotics</a></td>
<td width="420">ELEMENTAL combines demonstration interaction with VLM-generated/improved robot reward design.</td>
<td width="230">-</td>
<td width="240">AR</td>
<td width="300">interactive learning / reward design</td>
<td width="260">demonstrations + VLM reward design</td>
<td width="240">reward learning, not generalist VLA</td>
<td width="200">-</td>
<td width="360">Interactive reward design.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2411.18825">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2410.22391">A Large Recurrent Action Model: xLSTM enables Fast Inference for Robotics Tasks</a></td>
<td width="420">LRAM replaces Transformers with xLSTM to build a large action model, enabling faster inference and long-sequence extrapolation.</td>
<td width="230">LRAM</td>
<td width="240">sequence action model</td>
<td width="300">VLA / Generalist VLA</td>
<td width="260">xLSTM recurrent action model</td>
<td width="240">large recurrent action model</td>
<td width="200">-</td>
<td width="360">Addresses slow inference of Transformer-based large action models in real-time robot tasks.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2410.22391">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/ml-jku/LRAM">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2025</td>
<td width="320"><a href="https://arxiv.org/pdf/2502.13142">Pre-training Auto-regressive Robotic Models with 4D Representations</a></td>
<td width="420">ARM4R uses 4D representation pretraining for autoregressive robot models to improve spatiotemporal understanding and manipulation generalization.</td>
<td width="230">ARM4R</td>
<td width="240">AR</td>
<td width="300">generalist VLA / efficient/lightweight VLA</td>
<td width="260">4D representation pretraining</td>
<td width="240">-</td>
<td width="200">-</td>
<td width="360">Autoregressive pretraining with 4D representations.</td>
<td width="110" nowrap><a href="https://arxiv.org/pdf/2502.13142">paper</a></td>
<td width="110" nowrap><a href="https://arm4r.github.io/">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2025</td>
<td width="320"><a href="https://www.arxiv.org/pdf/2506.03863">STAR: Learning Diverse Robot Skill Abstractions through Rotation-Augmented Vector Quantization</a></td>
<td width="420">STAR uses rotation-augmented residual skill quantization and a causal skill transformer to learn discrete skill abstraction and composition.</td>
<td width="230">-</td>
<td width="240">discrete skill tokens</td>
<td width="300">generalist VLA / RL/online fine-tuning</td>
<td width="260">RaRSQ + causal skill transformer</td>
<td width="240">skill abstraction</td>
<td width="200">LIBERO + Real</td>
<td width="360">Addresses codebook collapse in VQ-style skill abstraction and insufficient modeling of causal skill composition.</td>
<td width="110" nowrap><a href="https://www.arxiv.org/pdf/2506.03863">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/iLearn-Lab/ICML25-STAR">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2501.10105">UniAct: Universal Actions For Enhanced Embodied Foundation Models</a></td>
<td width="420">UniAct introduces universal actions as a cross-task/cross-embodiment action interface to strengthen embodied foundation models.</td>
<td width="230">UniAct</td>
<td width="240">universal actions</td>
<td width="300">VLA / Generalist VLA</td>
<td width="260">universal action representation</td>
<td width="240">-</td>
<td width="200">-</td>
<td width="360">Universal action representation.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2501.10105">paper</a></td>
<td width="110" nowrap><a href="https://2toinf.github.io/UniAct/">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2503.13446">MoManipVLA: Transferring Vision-language-action Models for General Mobile Manipulation</a></td>
<td width="420">MoManipVLA transfers VLA to mobile manipulation scenarios for general manipulation that coordinates navigation and robotic arms.</td>
<td width="230">MoManipVLA</td>
<td width="240">-</td>
<td width="300">VLA / Efficient/Lightweight VLA</td>
<td width="260">-</td>
<td width="240">mobile manipulation VLA transfer</td>
<td width="200">-</td>
<td width="360">General mobile-manipulation transfer.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2503.13446">paper</a></td>
<td width="110" nowrap><a href="https://gary3410.github.io/momanipVLA/">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2503.06960">A Data-Centric Revisit of Pre-Trained Vision Models for Robot Learning</a></td>
<td width="420">This paper reevaluates the role of pretrained visual models in robot learning from a data-centric perspective.</td>
<td width="230">-</td>
<td width="240">AR</td>
<td width="300">VLA / Generalist VLA</td>
<td width="260">-</td>
<td width="240">data-centric robot visual pretraining study</td>
<td width="200">-</td>
<td width="360">Data-factor evaluation of pretrained visual models.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2503.06960">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/CVMI-Lab/SlotMIM">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2504.00420">Think Small, Act Big: Primitive Prompt Learning for Lifelong Robot Manipulation</a></td>
<td width="420">PPL uses reusable primitive prompts to support continual acquisition of new skills in lifelong robot learning.</td>
<td width="230">-</td>
<td width="240">AR</td>
<td width="300">VLA / Generalist VLA</td>
<td width="260">Primitive Prompt Learning</td>
<td width="240">lifelong robot manipulation</td>
<td width="200">Sim + Real</td>
<td width="360">Lifelong learning with reusable primitive prompts.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2504.00420">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://cvpr.thecvf.com/virtual/2025/poster/32789">Phoenix: A Motion-based Self-Reflection Framework for Fine-grained Robotic Action Correction</a></td>
<td width="420">Phoenix connects MLLM semantic reflection and low-level diffusion policies with motion instructions, enabling fine-grained action correction.</td>
<td width="230">MLLM + motion-conditioned diffusion policy</td>
<td width="240">Diffusion correction</td>
<td width="300">VLA / Generalist VLA</td>
<td width="260">dual-process motion adjustment + motion-conditioned diffusion policy</td>
<td width="240">self-reflection/action correction</td>
<td width="200">-</td>
<td width="360">Fine-grained robot action correction.</td>
<td width="110" nowrap><a href="https://cvpr.thecvf.com/virtual/2025/poster/32789">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2406.14235">Mitigating the Human-Robot Domain Discrepancy in Visual Pre-training for Robotic Manipulation</a></td>
<td width="420">This paper mitigates the domain gap between human-video visual pretraining and robotic manipulation.</td>
<td width="230">-</td>
<td width="240">-</td>
<td width="300">VLA / Generalist VLA</td>
<td width="260">human-robot domain discrepancy mitigation</td>
<td width="240">visual pretraining for manipulation</td>
<td width="200">-</td>
<td width="360">Human-robot domain gap in visual pretraining.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2406.14235">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2505.02166">CrayonRobo: Object-Centric Prompt-Driven Vision-Language-Action Model for Robotic Manipulation</a></td>
<td width="420">CrayonRobo uses object-centric 2D visual prompts overlaid on images to express contact poses and motion directions for guiding long-horizon manipulation.</td>
<td width="230">-</td>
<td width="240">SE(3) contact pose + motion direction</td>
<td width="300">VLA / Efficient/Lightweight VLA</td>
<td width="260">object-centric visual-language prompts</td>
<td width="240">-</td>
<td width="200">Sim + Real</td>
<td width="360">Addresses ambiguity in language goals and the fact that image/video goals can be too fine-grained and poor at expressing action constraints.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2505.02166">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/clorislili/CrayonRobo">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/html/2505.00693">Robotic Visual Instruction</a></td>
<td width="420">RoVI/VIEW uses hand-drawn object-centric 2D symbolic instructions to express spatial-temporal constraints and convert them into 3D manipulation actions.</td>
<td width="230">VIEW pipeline with VLMs</td>
<td width="240">3D action sequences</td>
<td width="300">VLA / RL/Online Fine-tuning</td>
<td width="260">Robotic Visual Instruction + Visual Instruction Embodied Workflow</td>
<td width="240">-</td>
<td width="200">Sim + Real</td>
<td width="360">Addresses insufficient spatial precision in natural-language robot instructions and the inconvenience of speech in public scenes.</td>
<td width="110" nowrap><a href="https://arxiv.org/html/2505.00693">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">open-source RoVI dataset</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2411.17662">RoboPEPP: Vision-Based Robot Pose and Joint Angle Estimation through Embedding Predictive Pre-Training</a></td>
<td width="420">RoboPEPP uses embedding predictive pre-training to estimate robot poses and joint angles from vision.</td>
<td width="230">-</td>
<td width="240">-</td>
<td width="300">generalist VLA / general-purpose VLA</td>
<td width="260">embedding predictive pre-training</td>
<td width="240">robot pose/joint estimation pretraining, not generalist VLA</td>
<td width="200">-</td>
<td width="360">Visual robot-pose and joint estimation.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2411.17662">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2504.06961">Two by Two: Learning Multi-Task Pairwise Objects Assembly for Generalizable Robot Manipulation</a></td>
<td width="420">2BY2 builds a dataset of everyday paired-object assembly and uses two-step SE(3) pose estimation to complete multi-task assembly.</td>
<td width="230">-</td>
<td width="240">SE(3) pose</td>
<td width="300">generalist VLA / general-purpose VLA</td>
<td width="260">two-step SE(3) pose estimation with equivariant features</td>
<td width="240">-</td>
<td width="200">-</td>
<td width="360">Addresses the fact that existing assembly datasets skew toward geometric fragments/industrial parts and do not cover functional relationships among everyday objects.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2504.06961">paper</a></td>
<td width="110" nowrap><a href="https://tea-lab.github.io/TwoByTwo/">project</a></td>
<td width="110" nowrap><a href="https://github.com/TEA-Lab/TwoByTWo">code</a></td>
<td width="240">2BY2 dataset</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2503.11269">Prof. Robot: Differentiable Robot Rendering Without Static and Self-Collisions</a></td>
<td width="420">Prof. Robot provides differentiable robot rendering that avoids static and self-collisions for robot vision/geometric learning.</td>
<td width="230">-</td>
<td width="240">-</td>
<td width="300">generalist VLA / general-purpose VLA</td>
<td width="260">collision-free differentiable robot rendering</td>
<td width="240">differentiable rendering/tooling, not VLA</td>
<td width="200">-</td>
<td width="360">Differentiable robot rendering.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2503.11269">paper</a></td>
<td width="110" nowrap><a href="https://www.qrcat.cn/prof-robot/">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
</tbody>
</table>
