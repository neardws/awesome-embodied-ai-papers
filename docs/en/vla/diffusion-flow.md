# diffusion/flow policy

[Home](../../../README.md) | [中文](../../zh-CN/vla/diffusion-flow.md) | [Direction index](README.md)

Total: 72 papers.

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
<td width="120" nowrap>CoRL 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2509.04996">FLOWER: Democratizing Generalist Robot Policies with Efficient Vision-Language-Action Flow Policies</a></td>
<td width="420">FLOWER builds efficient VLA flow policies for generalist robot control.</td>
<td width="230">FLOWER</td>
<td width="240">robot action</td>
<td width="300">VLA / diffusion/flow policy</td>
<td width="260">CoRL robot-learning method</td>
<td width="240">robot policy</td>
<td width="200">robot benchmarks</td>
<td width="360">Add CoRL VLA coverage.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2509.04996">paper</a></td>
<td width="110" nowrap><a href="https://intuitive-robots.github.io/flower_vla">project</a></td>
<td width="110" nowrap><a href="https://github.com/intuitive-robots/flower_vla_pret">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2509.01819">ManiFlow: A General Robot Manipulation Policy via Consistency Flow Training</a></td>
<td width="420">ManiFlow trains general robot manipulation policies with consistency flow.</td>
<td width="230">ManiFlow</td>
<td width="240">robot action</td>
<td width="300">VLA / diffusion/flow policy</td>
<td width="260">CoRL robot-learning method</td>
<td width="240">robot policy</td>
<td width="200">robot benchmarks</td>
<td width="360">Add CoRL VLA coverage.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2509.01819">paper</a></td>
<td width="110" nowrap><a href="https://maniflow-policy.github.io/">project</a></td>
<td width="110" nowrap><a href="https://github.com/geyan21/ManiFlow_Policy">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2505.21851">Streaming Flow Policy: Simplifying diffusion/flow-matching policies by treating action trajectories as flow trajectories</a></td>
<td width="420">Streaming Flow Policy treats action trajectories as flow trajectories for simpler policy generation.</td>
<td width="230">Streaming Flow Policy</td>
<td width="240">robot action</td>
<td width="300">VLA / diffusion/flow policy</td>
<td width="260">CoRL robot-learning method</td>
<td width="240">robot policy</td>
<td width="200">robot benchmarks</td>
<td width="360">Add CoRL VLA coverage.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2505.21851">paper</a></td>
<td width="110" nowrap><a href="https://siddancha.github.io/streaming-flow-policy/">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2502.05855">DexVLA: Vision-Language Model with Plug-In Diffusion Expert for General Robot Control</a></td>
<td width="420">DexVLA plugs a diffusion expert into a vision-language model for robot control.</td>
<td width="230">DexVLA</td>
<td width="240">robot action</td>
<td width="300">VLA / diffusion/flow policy</td>
<td width="260">CoRL robot-learning method</td>
<td width="240">robot policy</td>
<td width="200">robot benchmarks</td>
<td width="360">Add CoRL VLA coverage.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2502.05855">paper</a></td>
<td width="110" nowrap><a href="https://dex-vla.github.io">project</a></td>
<td width="110" nowrap><a href="https://github.com/juruobenruo/DexVLA">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2025</td>
<td width="320"><a href="https://diffusion-vla.github.io/">DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression</a></td>
<td width="420">DiffusionVLA scales robot foundation models with unified diffusion and autoregressive generation.</td>
<td width="230">DiffusionVLA</td>
<td width="240">diffusion + AR action</td>
<td width="300">VLA / diffusion-flow policy</td>
<td width="260">unified diffusion and autoregression</td>
<td width="240">robot foundation model</td>
<td width="200">robot manipulation benchmarks</td>
<td width="360">Scale VLA policy learning with diffusion and autoregressive modeling.</td>
<td width="110" nowrap><a href="https://diffusion-vla.github.io/">paper</a></td>
<td width="110" nowrap><a href="https://diffusion-vla.github.io/">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2025</td>
<td width="320"><a href="https://openreview.net/forum?id=nDmwloEl3N">Efficient Diffusion Transformer Policies with Mixture of Expert Denoisers for Multitask Learning</a></td>
<td width="420">This work uses mixture-of-expert denoisers to make diffusion transformer policies more efficient across tasks.</td>
<td width="230">diffusion transformer policy</td>
<td width="240">continuous action</td>
<td width="300">VLA / diffusion-flow policy</td>
<td width="260">MoE denoisers</td>
<td width="240">multitask diffusion policy</td>
<td width="200">robot manipulation tasks</td>
<td width="360">Improve multitask diffusion policy efficiency.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=nDmwloEl3N">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2025</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/33617">FlowPolicy: Enabling Fast and Robust 3D Flow-Based Policy via Consistency Flow Matching for Robot Manipulation</a></td>
<td width="420">FlowPolicy applies consistency flow matching to fast and robust 3D robot manipulation policies.</td>
<td width="230">3D flow policy</td>
<td width="240">continuous 3D action</td>
<td width="300">VLA / diffusion-flow policy</td>
<td width="260">consistency flow matching</td>
<td width="240">fast 3D manipulation policy</td>
<td width="200">robot manipulation benchmarks</td>
<td width="360">Build faster flow-based 3D manipulation policies.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2412.04987">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://openreview.net/forum?id=asS4W7Yw5e">GauDP: Reinventing Multi-Agent Collaboration through Gaussian-Image Synergy in Diffusion Policies</a></td>
<td width="420">GauDP uses Gaussian-image synergy inside diffusion policies for multi-agent collaboration.</td>
<td width="230">diffusion policy</td>
<td width="240">continuous action</td>
<td width="300">VLA / diffusion-flow policy</td>
<td width="260">Gaussian-image synergy</td>
<td width="240">multi-agent diffusion policy</td>
<td width="200">multi-agent manipulation tasks</td>
<td width="360">Improve collaboration through diffusion policy representation.</td>
<td width="110" nowrap><a href="https://arxiv.org/pdf/2511.00998">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2024</td>
<td width="320"><a href="https://openaccess.thecvf.com/content/CVPR2024/html/Ma_Hierarchical_Diffusion_Policy_for_Kinematics-Aware_Multi-Task_Robotic_Manipulation_CVPR_2024_paper.html">Hierarchical Diffusion Policy for Kinematics-Aware Multi-Task Robotic Manipulation</a></td>
<td width="420">HDP combines hierarchy and kinematic awareness for multitask robotic manipulation with diffusion policies.</td>
<td width="230">diffusion policy</td>
<td width="240">continuous action</td>
<td width="300">VLA / diffusion-flow policy</td>
<td width="260">hierarchical kinematics-aware diffusion</td>
<td width="240">multitask robot policy</td>
<td width="200">robot manipulation benchmarks</td>
<td width="360">Make diffusion policies kinematics-aware for multitask manipulation.</td>
<td width="110" nowrap><a href="https://openaccess.thecvf.com/content/CVPR2024/papers/Ma_Hierarchical_Diffusion_Policy_for_Kinematics-Aware_Multi-Task_Robotic_Manipulation_CVPR_2024_paper.pdf">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=H1KDMNOKQn">HybridVLA: Collaborative Diffusion and Autoregression in a Unified Vision-Language-Action Model</a></td>
<td width="420">HybridVLA combines autoregressive token prediction and diffusion denoising in one VLA backbone to improve continuous robot action generation.</td>
<td width="230">No specific base VLA specified.</td>
<td width="240">Diffusion / Flow</td>
<td width="300">diffusion/flow policy</td>
<td width="260">Diffusion policy</td>
<td width="240">Diffusion policy</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=H1KDMNOKQn">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=UvQOcw2oCD">Unified Diffusion VLA: Vision-Language-Action Model via Joint Discrete Denosing Diffusion Process</a></td>
<td width="420">Unified Diffusion VLA jointly denoises future visual tokens and action tokens so generation and control reinforce each other.</td>
<td width="230">No specific base VLA specified.</td>
<td width="240">Diffusion / Flow</td>
<td width="300">diffusion/flow policy</td>
<td width="260">Diffusion policy</td>
<td width="240">Diffusion policy</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=UvQOcw2oCD">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=1vXMfIYFZp">Master Skill Learning with Policy-Grounded Synergy of LLM-based Reward Shaping and Exploring</a></td>
<td width="420">Master Skill Learning uses reinforcement learning, preference feedback, or post-training signals to improve robot policies.</td>
<td width="230">-</td>
<td width="240">AR / Diffusion / Flow</td>
<td width="300">diffusion/flow policy</td>
<td width="260">RL / offline RL</td>
<td width="240">RL fine-tuning / policy optimization</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=1vXMfIYFZp">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=2RIqqNqALN">When would Vision-Proprioception Policies Fail in Robotic Manipulation?</a></td>
<td width="420">This study analyzes when vision-proprioception policies over-rely on proprioception and fail to use visual cues during robotic manipulation.</td>
<td width="230">No specific base VLA specified.</td>
<td width="240">Diffusion / Flow</td>
<td width="300">diffusion/flow policy</td>
<td width="260">-</td>
<td width="240">-</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=2RIqqNqALN">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=AmczI1k3Yk">Capturing Visual Environment Structure Correlates with Control Performance</a></td>
<td width="420">Capturing Visual Environment Structure Correlates connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td width="230">-</td>
<td width="240">Diffusion / Flow</td>
<td width="300">diffusion/flow policy</td>
<td width="260">3D/spatial representation learning</td>
<td width="240">3D-grounded policy/perception</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=AmczI1k3Yk">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=BTe5VLBjPg">VITA: Vision-to-Action Flow Matching Policy</a></td>
<td width="420">VITA uses flow matching from visual representations to action latents to reduce conditioning overhead in visuomotor policy generation.</td>
<td width="230">-</td>
<td width="240">Diffusion / Flow</td>
<td width="300">diffusion/flow policy</td>
<td width="260">Flow matching policy</td>
<td width="240">Flow policy</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=BTe5VLBjPg">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=BvirMuKWV1">When a Robot is More Capable than a Human: Learning from Constrained Demonstrators</a></td>
<td width="420">This work learns policies that can surpass constrained demonstrations by accounting for the demonstrator's limited action interface.</td>
<td width="230">-</td>
<td width="240">AR / Diffusion / Flow</td>
<td width="300">diffusion/flow policy</td>
<td width="260">-</td>
<td width="240">-</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=BvirMuKWV1">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=FqDmvMZish">Autonomous Functional Play with Correspondence-Driven Trajectory Warping</a></td>
<td width="420">Autonomous Functional Play connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td width="230">-</td>
<td width="240">AR / Diffusion / Flow</td>
<td width="300">diffusion/flow policy</td>
<td width="260">3D keypoint grounding</td>
<td width="240">3D-grounded policy/perception</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=FqDmvMZish">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=IaGf8Eh5Uo">Reference Grounded Skill Discovery</a></td>
<td width="420">Reference Grounded Skill Discovery uses reference motion representations to guide unsupervised skill learning in high-dimensional agents.</td>
<td width="230">-</td>
<td width="240">Diffusion / Flow</td>
<td width="300">diffusion/flow policy</td>
<td width="260">-</td>
<td width="240">-</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=IaGf8Eh5Uo">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=KFu4p3pd11">Masked Generative Policy for Robotic Control</a></td>
<td width="420">Masked Generative Policy tokenizes actions and uses masked transformer refinement for fast, coherent visuomotor control.</td>
<td width="230">-</td>
<td width="240">Diffusion / Flow</td>
<td width="300">diffusion/flow policy</td>
<td width="260">Diffusion policy</td>
<td width="240">Diffusion policy</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=KFu4p3pd11">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=OeDwYtp8n1">Learning Video Generation for Robotic Manipulation with Collaborative Trajectory Control</a></td>
<td width="420">Learning Video Generation for Robotic Manipulation uses video generation/prediction or future rendering to learn robot interaction dynamics.</td>
<td width="230">-</td>
<td width="240">AR / Diffusion / Flow</td>
<td width="300">diffusion/flow policy</td>
<td width="260">Diffusion policy</td>
<td width="240">Diffusion policy</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=OeDwYtp8n1">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=P9PVdWyM3U">Policy Contrastive Decoding for Robotic Foundation Models</a></td>
<td width="420">Policy Contrastive Decoding steers robotic foundation models at inference by contrasting actions from original and object-masked observations.</td>
<td width="230">-</td>
<td width="240">Diffusion / Flow</td>
<td width="300">diffusion/flow policy</td>
<td width="260">Diffusion policy</td>
<td width="240">Diffusion policy</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=P9PVdWyM3U">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=PL0tJOfm7I">Demystifying Robot Diffusion Policies: Action Memorization and a Simple Lookup Table Alternative</a></td>
<td width="420">This analysis argues that diffusion policies often behave like useful action lookup tables in sparse imitation settings.</td>
<td width="230">No specific base VLA specified.</td>
<td width="240">Diffusion / Flow</td>
<td width="300">diffusion/flow policy</td>
<td width="260">Diffusion policy</td>
<td width="240">Diffusion policy</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=PL0tJOfm7I">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=Q1CP0iAmOb">H$^3$DP: Triply‑Hierarchical Diffusion Policy for Visuomotor Learning</a></td>
<td width="420">H^3DP couples depth-aware perception, multi-scale visual features, and hierarchical action denoising for visuomotor diffusion policies.</td>
<td width="230">-</td>
<td width="240">AR / Diffusion / Flow</td>
<td width="300">diffusion/flow policy</td>
<td width="260">Diffusion policy</td>
<td width="240">Diffusion policy</td>
<td width="200">5 simulation benchmarks + real Galaxea R1</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=Q1CP0iAmOb">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=TnLFRhLuZ6">Compose Your Policies! Improving Diffusion-based or Flow-based Robot Policies via Test-time Distribution-level Composition</a></td>
<td width="420">This method composes diffusion or flow policy distributions at test time to improve behavior without additional training.</td>
<td width="230">No specific base VLA specified.</td>
<td width="240">Diffusion / Flow</td>
<td width="300">diffusion/flow policy</td>
<td width="260">GPC; test-time distribution-level policy composition</td>
<td width="240">Flow policy</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=TnLFRhLuZ6">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=VSWjHIveqZ">Abstracting Robot Manipulation Skills via Mixture-of-Experts Diffusion Policies</a></td>
<td width="420">This work uses a mixture-of-experts diffusion policy to learn reusable skill bases and route actions to task-relevant experts.</td>
<td width="230">-</td>
<td width="240">Diffusion / Flow</td>
<td width="300">diffusion/flow policy</td>
<td width="260">Diffusion policy</td>
<td width="240">Diffusion policy</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=VSWjHIveqZ">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=WVliGyFwZv">Accelerated co-design of robots through morphological pretraining</a></td>
<td width="420">Accelerated co-design of robots through morphological pretraining uses reinforcement learning, preference feedback, or post-training signals to improve robot policies.</td>
<td width="230">-</td>
<td width="240">Diffusion / Flow</td>
<td width="300">diffusion/flow policy</td>
<td width="260">RL / offline RL</td>
<td width="240">RL fine-tuning / policy optimization</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=WVliGyFwZv">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=aoorNQFpM6">VER: Vision Expert Transformer for Robot Learning via Foundation Distillation and Dynamic Routing</a></td>
<td width="420">VER provides open-source tools, data formats, or benchmark interfaces for end-to-end robot learning.</td>
<td width="230">-</td>
<td width="240">AR / Diffusion / Flow</td>
<td width="300">diffusion/flow policy</td>
<td width="260">-</td>
<td width="240">-</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=aoorNQFpM6">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=d08yOXs1Dl">SpikePingpong: Spike Vision-based Fast-Slow Pingpong Robot System</a></td>
<td width="420">SpikePingpong combines event-based fast vision with slower control reasoning for high-speed robotic table-tennis behavior.</td>
<td width="230">-</td>
<td width="240">Diffusion / Flow</td>
<td width="300">diffusion/flow policy</td>
<td width="260">-</td>
<td width="240">-</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=d08yOXs1Dl">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=dQ6d5bgXtM">Translating Flow to Policy via Hindsight Online Imitation</a></td>
<td width="420">This method improves low-level policies from online rollouts by relabeling achieved outcomes as hindsight goals.</td>
<td width="230">-</td>
<td width="240">Diffusion / Flow</td>
<td width="300">diffusion/flow policy / RL/online fine-tuning</td>
<td width="260">-</td>
<td width="240">-</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=dQ6d5bgXtM">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=eWe8zqGvs5">Cortical Policy: A Dual-Stream View Transformer for Robotic Manipulation</a></td>
<td width="420">Cortical Policy connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td width="230">-</td>
<td width="240">Diffusion / Flow</td>
<td width="300">diffusion/flow policy</td>
<td width="260">3D keypoint grounding</td>
<td width="240">3D-grounded policy/perception</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=eWe8zqGvs5">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=iKJbmx1iuQ">Contractive Diffusion Policies</a></td>
<td width="420">Contractive Diffusion Policies regularize diffusion sampling dynamics to make continuous-control action generation more stable.</td>
<td width="230">-</td>
<td width="240">Diffusion / Flow</td>
<td width="300">diffusion/flow policy</td>
<td width="260">Diffusion policy</td>
<td width="240">Diffusion policy</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=iKJbmx1iuQ">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=kIYNtxE13h">Scalable Exploration for High-Dimensional Continuous Control via Value-Guided Flow</a></td>
<td width="420">Scalable Exploration for High-Dimensional Continuous Control uses reinforcement learning, preference feedback, or post-training signals to improve robot policies.</td>
<td width="230">-</td>
<td width="240">Diffusion / Flow</td>
<td width="300">diffusion/flow policy</td>
<td width="260">RL / offline RL</td>
<td width="240">RL fine-tuning / policy optimization</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=kIYNtxE13h">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=w3Ik8HUyTT">ViPRA: Video Prediction for Robot Actions</a></td>
<td width="420">ViPRA uses video generation/prediction or future rendering to learn robot interaction dynamics.</td>
<td width="230">-</td>
<td width="240">Diffusion / Flow</td>
<td width="300">diffusion/flow policy</td>
<td width="260">Generative action modeling</td>
<td width="240">-</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=w3Ik8HUyTT">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=AcTsKglDdh">DataMIL: Selecting Data for Robot Imitation Learning with Datamodels</a></td>
<td width="420">DataMIL provides open-source tools, data formats, or benchmark interfaces for end-to-end robot learning.</td>
<td width="230">-</td>
<td width="240">AR / Diffusion / Flow</td>
<td width="300">diffusion/flow policy</td>
<td width="260">-</td>
<td width="240">-</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=AcTsKglDdh">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=COrUdVuInH">MIMIC: Mask-Injected Manipulation Video Generation with Interaction Control</a></td>
<td width="420">MIMIC uses video generation/prediction or future rendering to learn robot interaction dynamics.</td>
<td width="230">-</td>
<td width="240">Diffusion / Flow</td>
<td width="300">diffusion/flow policy</td>
<td width="260">Diffusion policy</td>
<td width="240">Diffusion policy</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=COrUdVuInH">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=CiZMMAFQR3">LeRobot: An Open-Source Library for End-to-End Robot Learning</a></td>
<td width="420">LeRobot provides open-source tools, data formats, or benchmark interfaces for end-to-end robot learning.</td>
<td width="230">-</td>
<td width="240">AR / Diffusion / Flow</td>
<td width="300">diffusion/flow policy</td>
<td width="260">-</td>
<td width="240">-</td>
<td width="200">simulation + real hardware</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=CiZMMAFQR3">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38881">ManiLong-Shot: Interaction-Aware One-Shot Imitation Learning for Long-Horizon Manipulation</a></td>
<td width="420">ManiLong-Shot decomposes long-horizon one-shot manipulation into interaction-aware primitives that can be transferred from demonstrations.</td>
<td width="230">-</td>
<td width="240">AR / Diffusion / Flow</td>
<td width="300">diffusion/flow policy</td>
<td width="260">-</td>
<td width="240">-</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38881">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38889">Learning Diffusion Policy from Primitive Skills for Robot Manipulation</a></td>
<td width="420">This work conditions diffusion policies on interpretable primitive skills to align short-horizon action generation for manipulation.</td>
<td width="230">-</td>
<td width="240">AR / Diffusion / Flow</td>
<td width="300">diffusion/flow policy</td>
<td width="260">Diffusion policy</td>
<td width="240">Diffusion policy</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38889">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38912">Intention-Aware Diffusion Model for Pedestrian Trajectory Prediction</a></td>
<td width="420">This model injects short- and long-term pedestrian intentions into diffusion-based trajectory prediction.</td>
<td width="230">-</td>
<td width="240">AR / Diffusion / Flow</td>
<td width="300">diffusion/flow policy</td>
<td width="260">Diffusion policy</td>
<td width="240">Diffusion policy</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38912">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38919">MP1: MeanFlow Tames Policy Learning in 1-step for Robotic Manipulation</a></td>
<td width="420">MP1 applies MeanFlow to point-cloud manipulation policies, generating action trajectories in one network evaluation.</td>
<td width="230">-</td>
<td width="240">AR / Diffusion / Flow</td>
<td width="300">diffusion/flow policy</td>
<td width="260">Flow matching policy</td>
<td width="240">Flow policy</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38919">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38934">ForeDiffusion: Foresight-Conditioned Diffusion Policy via Future View Construction for Robot Manipulation</a></td>
<td width="420">ForeDiffusion conditions diffusion policies on predicted future views to reduce error accumulation in manipulation.</td>
<td width="230">-</td>
<td width="240">Diffusion / Flow</td>
<td width="300">diffusion/flow policy</td>
<td width="260">Diffusion policy</td>
<td width="240">Diffusion policy</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38934">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38944">Balancing Signal and Variance: Adaptive Offline RL Post-Training for VLA Flow Models</a></td>
<td width="420">Balancing Signal and Variance uses reinforcement learning, preference feedback, or post-training signals to improve robot policies.</td>
<td width="230">π₀</td>
<td width="240">Flow</td>
<td width="300">diffusion/flow policy / RL/online fine-tuning / Reward D</td>
<td width="260">ARFM</td>
<td width="240">Off-Policy / MF</td>
<td width="200">Sim ✓ / Real ✓</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38944">paper</a> / <a href="https://arxiv.org/pdf/2509.04063">paper</a> / <a href="https://arxiv.org/abs/2509.04063">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38950">Bridging Scale Discrepancies in Robotic Control via Language-Based Action Representations</a></td>
<td width="420">This work converts robot actions into language-based representations to reduce scale mismatch across tasks and platforms.</td>
<td width="230">-</td>
<td width="240">Diffusion / Flow</td>
<td width="300">diffusion/flow policy</td>
<td width="260">-</td>
<td width="240">-</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38950">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38959">D²PPO: Diffusion Policy Policy Optimization with Dispersive Loss</a></td>
<td width="420">D2PPO adds dispersive-loss regularization to diffusion policy optimization to prevent representation collapse during manipulation learning.</td>
<td width="230">-</td>
<td width="240">Diffusion / Flow</td>
<td width="300">diffusion/flow policy</td>
<td width="260">PPO</td>
<td width="240">RL fine-tuning / policy optimization</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38959">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/62902">Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies</a></td>
<td width="420">Discrete Diffusion VLA models discretized action chunks with in-backbone discrete diffusion for parallel, error-correcting VLA action decoding.</td>
<td width="230">No specific base VLA specified.</td>
<td width="240">Diffusion / Flow</td>
<td width="300">VLA / diffusion policy / diffusion/flow policy</td>
<td width="260">Diffusion policy</td>
<td width="240">Diffusion policy</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/62902">paper</a> / <a href="https://arxiv.org/abs/2508.20072">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/61717">STEP: Warm-Started Visuomotor Policies with Spatiotemporal Consistency Prediction</a></td>
<td width="420">STEP warm-starts diffusion policies with spatiotemporally consistent actions to cut closed-loop inference latency.</td>
<td width="230">-</td>
<td width="240">AR / Diffusion / Flow</td>
<td width="300">diffusion/flow policy</td>
<td width="260">-</td>
<td width="240">-</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/61717">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/61049">Learning Human-Robot Collaboration via Heterogeneous-Agent Lyapunov Policy Optimization</a></td>
<td width="420">HALyPO stabilizes heterogeneous human-robot multi-agent policy optimization with Lyapunov-style disagreement control.</td>
<td width="230">-</td>
<td width="240">AR / Diffusion / Flow</td>
<td width="300">diffusion/flow policy</td>
<td width="260">-</td>
<td width="240">-</td>
<td width="200">Sim/Benchmark</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/61049">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2511.15605">SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models</a></td>
<td width="420">SRPO uses reinforcement learning, preference feedback, or post-training signals to improve robot policies.</td>
<td width="230">OpenVLA* / π₀ / π₀-Fast</td>
<td width="240">AR / Flow</td>
<td width="300">VLA / RL/online fine-tuning / Reward D</td>
<td width="260">SRPO</td>
<td width="240">Hybrid / MF (MB-Reward but MF-RL)</td>
<td width="200">Sim ✓(MT) / Real ✓(MT)</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2511.15605">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2507.01961">AC-DiT: Adaptive Coordination Diffusion Transformer for Mobile Manipulation</a></td>
<td width="420">AC-DiT connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td width="230">-</td>
<td width="240">Diffusion / Flow</td>
<td width="300">VLA / diffusion policy / diffusion transformer / diffusion/flow policy</td>
<td width="260">Diffusion policy</td>
<td width="240">Diffusion policy</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2507.01961">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2510.20406">PointMapPolicy: Structured Point Cloud Processing for Multi-Modal Imitation Learning</a></td>
<td width="420">PointMapPolicy connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td width="230">-</td>
<td width="240">AR / Diffusion / Flow</td>
<td width="300">VLA / diffusion/flow policy</td>
<td width="260">PPO</td>
<td width="240">Diffusion policy</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2510.20406">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2509.00117">Emerging Risks from Embodied AI Require Urgent Policy Action</a></td>
<td width="420">This policy analysis maps physical, surveillance, and societal risks from embodied AI and calls for targeted governance.</td>
<td width="230">-</td>
<td width="240">Diffusion / Flow</td>
<td width="300">diffusion/flow policy</td>
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
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2506.07127">Human-assisted Robotic Policy Refinement via Action Preference Optimization</a></td>
<td width="420">Human-assisted Robotic Policy Refinement uses reinforcement learning, preference feedback, or post-training signals to improve robot policies.</td>
<td width="230">No specific base VLA specified.</td>
<td width="240">Diffusion / Flow</td>
<td width="300">diffusion/flow policy</td>
<td width="260">Preference optimization</td>
<td width="240">RL fine-tuning / policy optimization</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2506.07127">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2512.00085">Hyper-GoalNet: Goal-Conditioned Manipulation Policy Learning with HyperNetworks</a></td>
<td width="420">Hyper-GoalNet uses hypernetworks to generate goal-specific manipulation policy parameters from goal descriptions.</td>
<td width="230">-</td>
<td width="240">AR / Diffusion / Flow</td>
<td width="300">diffusion/flow policy</td>
<td width="260">-</td>
<td width="240">-</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2512.00085">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2505.22094">ReinFlow: Fine-tuning Flow Matching Policy with Online Reinforcement Learning</a></td>
<td width="420">ReinFlow uses reinforcement learning, preference feedback, or post-training signals to improve robot policies.</td>
<td width="230">-</td>
<td width="240">AR / Flow</td>
<td width="300">flow matching / RL / RL/online fine-tuning</td>
<td width="260">Flow matching policy</td>
<td width="240">RL fine-tuning / policy optimization</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2505.22094">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2505.13431">A Practical Guide for Incorporating Symmetry in Diffusion Policy</a></td>
<td width="420">This guide evaluates lightweight ways to add symmetry priors to diffusion policies without full equivariant architectures.</td>
<td width="230">-</td>
<td width="240">Diffusion / Flow</td>
<td width="300">diffusion policy / diffusion/flow policy</td>
<td width="260">Diffusion policy</td>
<td width="240">Diffusion policy</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2505.13431">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2509.25822">Act to See, See to Act: Diffusion-Driven Perception-Action Interplay for Adaptive Policies</a></td>
<td width="420">DP-AG models perception-action feedback with action-guided diffusion dynamics for more adaptive imitation policies.</td>
<td width="230">-</td>
<td width="240">Diffusion / Flow</td>
<td width="300">diffusion policy / diffusion/flow policy</td>
<td width="260">Diffusion policy</td>
<td width="240">Diffusion policy</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2509.25822">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2511.20906">DASIP: Dynamic Test-Time Compute Scaling for Robot Control with Stochastic Interpolant Policies</a></td>
<td width="420">DASIP adjusts stochastic-interpolant policy compute at test time according to estimated manipulation difficulty.</td>
<td width="230">-</td>
<td width="240">AR / Diffusion / Flow</td>
<td width="300">diffusion/flow policy</td>
<td width="260">Flow matching policy</td>
<td width="240">Flow policy</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2511.20906">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2506.13922">DynaGuide: Steering Diffusion Polices with Active Dynamic Guidance</a></td>
<td width="420">DynaGuide uses reinforcement learning, preference feedback, or post-training signals to improve robot policies.</td>
<td width="230">-</td>
<td width="240">Diffusion / Flow</td>
<td width="300">diffusion policy / diffusion/flow policy</td>
<td width="260">Diffusion policy</td>
<td width="240">RL fine-tuning / policy optimization</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2506.13922">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2503.19757">Dita: Scaling Diffusion Transformer for Generalist Vision-Language-Action Policy</a></td>
<td width="420">Dita scales diffusion transformers to denoise continuous action sequences inside a generalist VLA policy.</td>
<td width="230">No specific base VLA specified.</td>
<td width="240">Diffusion / Flow</td>
<td width="300">VLA / diffusion policy / diffusion transformer / diffusion/flow policy</td>
<td width="260">Diffusion policy</td>
<td width="240">Diffusion policy</td>
<td width="200">LIBERO + SimplerEnv + real Franka</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2503.19757">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://iccv.thecvf.com/virtual/2025/poster/1571">SD2Actor: Continuous State Decomposition via Diffusion Embeddings for Robotic Manipulation</a></td>
<td width="420">SD2Actor decomposes object states with diffusion embeddings to generate zero-shot continuous manipulation actions.</td>
<td width="230">-</td>
<td width="240">Diffusion / Flow</td>
<td width="300">VLA / diffusion policy / diffusion/flow policy</td>
<td width="260">-</td>
<td width="240">-</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/1571">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2507.06224">EC-Flow: Enabling Versatile Robotic Manipulation from Action-Unlabeled Videos via Embodiment-Centric Flow</a></td>
<td width="420">EC-Flow provides open-source tools, data formats, or benchmark interfaces for end-to-end robot learning.</td>
<td width="230">-</td>
<td width="240">Diffusion / Flow</td>
<td width="300">flow matching / diffusion/flow policy</td>
<td width="260">-</td>
<td width="240">-</td>
<td width="200">Sim/Benchmark</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2507.06224">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2503.13217">Dense Policy: Bidirectional Autoregressive Learning of Actions</a></td>
<td width="420">Dense Policy uses action tokens, mask generation, or autoregressive modeling to improve robot control.</td>
<td width="230">-</td>
<td width="240">AR / Diffusion / Flow</td>
<td width="300">autoregressive policy / diffusion/flow policy</td>
<td width="260">Generative action modeling</td>
<td width="240">-</td>
<td width="200">-</td>
<td width="360">Addresses the efficiency and consistency of robot action representation and long-horizon action prediction.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2503.13217">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2507.06710">Spatial-Temporal Aware Visuomotor Diffusion Policy Learning</a></td>
<td width="420">Spatial-Temporal Aware Visuomotor Diffusion Policy Learning connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td width="230">-</td>
<td width="240">AR / Diffusion / Flow</td>
<td width="300">diffusion policy / diffusion/flow policy</td>
<td width="260">Diffusion policy</td>
<td width="240">Diffusion policy</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2507.06710">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2507.04331">Wavelet Policy: Lifting Scheme for Policy Learning in Long-Horizon Tasks</a></td>
<td width="420">Wavelet Policy uses learnable multi-scale wavelet transforms to improve long-horizon policy learning.</td>
<td width="230">-</td>
<td width="240">AR / Diffusion / Flow</td>
<td width="300">diffusion/flow policy</td>
<td width="260">-</td>
<td width="240">-</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2507.04331">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2025</td>
<td width="320"><a href="https://arxiv.org/pdf/2502.01800">Flow-based Domain Randomization for Learning and Sequencing Robotic Skills</a></td>
<td width="420">Flow-based Domain Randomization uses reinforcement learning, preference feedback, or post-training signals to improve robot policies.</td>
<td width="230">-</td>
<td width="240">AR / Diffusion / Flow</td>
<td width="300">flow matching / diffusion/flow policy</td>
<td width="260">Flow matching policy</td>
<td width="240">RL fine-tuning / policy optimization</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/pdf/2502.01800">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2503.01885">Learning Policy Committees for Effective Personalization in MDPs with Diverse Tasks</a></td>
<td width="420">Learning Policy Committees for Effective Personalization in MDPs uses reinforcement learning, preference feedback, or post-training signals to improve robot policies.</td>
<td width="230">-</td>
<td width="240">AR / Diffusion / Flow</td>
<td width="300">diffusion/flow policy</td>
<td width="260">RL / offline RL</td>
<td width="240">RL fine-tuning / policy optimization</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2503.01885">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2411.18623">Lift3D Foundation Policy: Lifting 2D Large-Scale Pretrained Models for Robust 3D Robotic Manipulation</a></td>
<td width="420">Lift3D Foundation Policy studies VLA robustness under multimodal perturbations, adversarial inputs, or distribution shifts.</td>
<td width="230">-</td>
<td width="240">Diffusion / Flow</td>
<td width="300">3D representation / diffusion/flow policy</td>
<td width="260">Generative action modeling</td>
<td width="240">3D-grounded policy/perception</td>
<td width="200">simulation benchmarks + real FR3</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2411.18623">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://openaccess.thecvf.com/content/CVPR2025/papers/Tian_PDFactor_Learning_Tri-Perspective_View_Policy_Diffusion_Field_for_Multi-Task_Robotic_CVPR_2025_paper.pdf">PDFactor: Learning Tri-Perspective View Policy Diffusion Field for Multi-Task Robotic Manipulation</a></td>
<td width="420">PDFactor represents 3D action distributions as tri-perspective diffusion fields for efficient multi-task manipulation.</td>
<td width="230">-</td>
<td width="240">AR / Diffusion / Flow</td>
<td width="300">diffusion policy / diffusion/flow policy</td>
<td width="260">-</td>
<td width="240">-</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openaccess.thecvf.com/content/CVPR2025/papers/Tian_PDFactor_Learning_Tri-Perspective_View_Policy_Diffusion_Field_for_Multi-Task_Robotic_CVPR_2025_paper.pdf">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2506.16201">FlowRAM: Grounding Flow Matching Policy with Region-Aware Mamba Framework for Robotic Manipulation</a></td>
<td width="420">FlowRAM connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td width="230">-</td>
<td width="240">AR / Diffusion / Flow</td>
<td width="300">flow matching / diffusion/flow policy</td>
<td width="260">Flow matching policy</td>
<td width="240">Flow policy</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2506.16201">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2411.18369">G3Flow: Generative 3D Semantic Flow for Pose-aware and Generalizable Object Manipulation</a></td>
<td width="420">G3Flow connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td width="230">-</td>
<td width="240">AR / Diffusion / Flow</td>
<td width="300">flow matching / 3D representation / diffusion/flow policy</td>
<td width="260">Diffusion policy</td>
<td width="240">Diffusion policy</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2411.18369">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">RoboTwin_Benchmark tasks</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2412.03142">AffordDP: Generalizable Diffusion Policy with Transferable Affordance</a></td>
<td width="420">AffordDP connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td width="230">-</td>
<td width="240">Diffusion / Flow</td>
<td width="300">diffusion policy / affordance / diffusion/flow policy</td>
<td width="260">Diffusion policy</td>
<td width="240">Diffusion policy</td>
<td width="200">Sim + Real</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2412.03142">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2505.13091">Touch2Shape: Touch-Conditioned 3D Diffusion for Shape Exploration and Reconstruction</a></td>
<td width="420">Touch2Shape conditions 3D diffusion on tactile observations to explore and reconstruct object shape.</td>
<td width="230">-</td>
<td width="240">Diffusion / Flow</td>
<td width="300">diffusion policy / 3D representation / diffusion/flow policy</td>
<td width="260">-</td>
<td width="240">-</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2505.13091">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
</tbody>
</table>
