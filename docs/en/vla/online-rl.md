# online/RL fine-tuning

[Home](../../../README.md) | [中文](../../zh-CN/vla/online-rl.md) | [Direction index](README.md)

Total: 21 papers.

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
<td width="320"><a href="https://scholar.google.com/scholar?q=Q-transformer%3A+Scalable+offline+reinforcement+learning+via+autoregressive+q-functions">Q-transformer: Scalable offline reinforcement learning via autoregressive q-functions</a></td>
<td width="420">Q-transformer scales offline RL for robot policies through autoregressive Q-functions.</td>
<td width="230">Q-transformer</td>
<td width="240">robot action</td>
<td width="300">VLA / online/RL fine-tuning</td>
<td width="260">CoRL robot-learning method</td>
<td width="240">robot policy</td>
<td width="200">robot benchmarks</td>
<td width="360">Add CoRL VLA coverage.</td>
<td width="110" nowrap><a href="https://scholar.google.com/scholar?q=Q-transformer%3A+Scalable+offline+reinforcement+learning+via+autoregressive+q-functions">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2024</td>
<td width="320"><a href="https://arxiv.org/abs/2410.13816">Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance</a></td>
<td width="420">V-GPS improves robotic foundation models with value guidance.</td>
<td width="230">Steering Your Generalists</td>
<td width="240">robot action</td>
<td width="300">VLA / online/RL fine-tuning</td>
<td width="260">CoRL robot-learning method</td>
<td width="240">robot policy</td>
<td width="200">robot benchmarks</td>
<td width="360">Add CoRL VLA coverage.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2410.13816">paper</a></td>
<td width="110" nowrap><a href="https://nakamotoo.github.io/V-GPS">project</a></td>
<td width="110" nowrap><a href="https://github.com/nakamotoo/V-GPS">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2506.16211">ControlVLA: Few-shot Object-centric Adaptation for Pre-trained Vision-Language-Action Models</a></td>
<td width="420">ControlVLA adapts pretrained VLA models to object-centric tasks with few examples.</td>
<td width="230">ControlVLA</td>
<td width="240">robot action</td>
<td width="300">VLA / online/RL fine-tuning</td>
<td width="260">CoRL robot-learning method</td>
<td width="240">robot policy</td>
<td width="200">robot benchmarks</td>
<td width="360">Add CoRL VLA coverage.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2506.16211">paper</a></td>
<td width="110" nowrap><a href="https://controlvla.github.io/">project</a></td>
<td width="110" nowrap><a href="https://github.com/ControlVLA/ControlVLA">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2508.02062">RICL: Adding In-Context Adaptability to Pre-Trained Vision-Language-Action Models</a></td>
<td width="420">RICL adds in-context adaptability to pretrained VLA models.</td>
<td width="230">RICL</td>
<td width="240">robot action</td>
<td width="300">VLA / online/RL fine-tuning</td>
<td width="260">CoRL robot-learning method</td>
<td width="240">robot policy</td>
<td width="200">robot benchmarks</td>
<td width="360">Add CoRL VLA coverage.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2508.02062">paper</a></td>
<td width="110" nowrap><a href="https://ricl-vla.github.io/">project</a></td>
<td width="110" nowrap><a href="https://github.com/ricl-vla/ricl_openpi">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2506.17811">RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models</a></td>
<td width="420">RoboMonkey scales test-time sampling and verification for VLA policies.</td>
<td width="230">RoboMonkey</td>
<td width="240">robot action</td>
<td width="300">VLA / online/RL fine-tuning</td>
<td width="260">CoRL robot-learning method</td>
<td width="240">robot policy</td>
<td width="200">robot benchmarks</td>
<td width="360">Add CoRL VLA coverage.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2506.17811">paper</a></td>
<td width="110" nowrap><a href="https://robomonkey-vla.github.io/">project</a></td>
<td width="110" nowrap><a href="https://github.com/robomonkey-vla/RoboMonkey">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2024</td>
<td width="320"><a href="https://proceedings.mlr.press/v235/springenberg24a.html">Offline Actor-Critic Reinforcement Learning Scales to Large Models</a></td>
<td width="420">This work studies scaling offline actor-critic reinforcement learning to large model policies.</td>
<td width="230">large policy model</td>
<td width="240">policy action</td>
<td width="300">offline RL / VLA post-training</td>
<td width="260">offline actor-critic</td>
<td width="240">model-based or actor-critic RL</td>
<td width="200">offline RL benchmarks</td>
<td width="360">Understand how large policies can be improved with offline RL.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2402.05546">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2512.23703">General Process Reward Modeling for Robotic Reinforcement Learning</a></td>
<td width="420">GPRM builds process reward models for robotic reinforcement learning and policy improvement.</td>
<td width="230">robot policy</td>
<td width="240">robot action</td>
<td width="300">VLA / RL / reward modeling</td>
<td width="260">process reward modeling</td>
<td width="240">robotic RL</td>
<td width="200">robot RL benchmarks</td>
<td width="360">Use process-level rewards to improve robotic policy learning.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2512.23703">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>IROS 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2503.05833">Refined Policy Distillation: From VLA Generalists to RL Experts</a></td>
<td width="420">RPD distills generalist VLAs such as Octo and OpenVLA into task-specialist policies through reinforcement learning.</td>
<td width="230">Octo / OpenVLA</td>
<td width="240">policy action</td>
<td width="300">RL distillation / online fine-tuning</td>
<td width="260">Refined Policy Distillation</td>
<td width="240">RL expert policy</td>
<td width="200">Sim + Real</td>
<td width="360">Transfer generalist VLAs into stronger task-specialist policies.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2503.05833">paper</a></td>
<td width="110" nowrap><a href="https://refined-policy-distillation.github.io/">project</a></td>
<td width="110" nowrap><a href="https://github.com/Refined-Policy-Distillation/RPD">code</a></td>
<td width="240"><a href="https://huggingface.co/Juelg">hf</a></td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=ULTWUuGhC3">Interleave-VLA: Enhancing Robot Manipulation with Image-Text Interleaved Instructions</a></td>
<td width="420">Interleave-VLA provides open-source tools, data formats, or benchmark interfaces for end-to-end robot learning.</td>
<td width="230">No specific base VLA specified.</td>
<td width="240">policy action</td>
<td width="300">VLA / RL / Online Fine-tuning</td>
<td width="260">-</td>
<td width="240">RL fine-tuning / policy optimization</td>
<td width="200">SIMPLER + VIMA-Bench + real FANUC</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=ULTWUuGhC3">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">Interleaved X-Embodiment; 210k trajectories</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=eUGoqrZ6Ea">Self-Improving Vision-Language-Action Models with Data Generation via Residual RL</a></td>
<td width="420">Self-Improving Vision-Language-Action Models with Data Generation uses reinforcement learning, preference feedback, or post-training signals to improve robot policies.</td>
<td width="230">No specific base VLA specified.</td>
<td width="240">Diffusion / Flow</td>
<td width="300">VLA / RL / Online Fine-tuning</td>
<td width="260">PLD residual RL + SFT distillation</td>
<td width="240">Off-policy residual RL</td>
<td width="200">LIBERO + SimplerEnv + real Franka/YAM</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=eUGoqrZ6Ea">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=sFO9d6XSlf">Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting</a></td>
<td width="420">Actions as Language provides open-source tools, data formats, or benchmark interfaces for end-to-end robot learning.</td>
<td width="230">No specific base VLA specified.</td>
<td width="240">policy action</td>
<td width="300">VLA / RL / Online Fine-tuning</td>
<td width="260">VLM2VLA; language action representation + LoRA</td>
<td width="240">RL fine-tuning / policy optimization</td>
<td width="200">800+ real robot experiments</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=sFO9d6XSlf">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=GrsoLVNy3Y">Cross-Embodiment Offline Reinforcement Learning for Heterogeneous Robot Datasets</a></td>
<td width="420">Cross-Embodiment Offline Reinforcement Learning uses reinforcement learning, preference feedback, or post-training signals to improve robot policies.</td>
<td width="230">-</td>
<td width="240">AR</td>
<td width="300">VLA / RL / Online Fine-tuning</td>
<td width="260">offline RL + morphology grouping</td>
<td width="240">RL fine-tuning / policy optimization</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=GrsoLVNy3Y">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">16 robot-platform locomotion dataset suite</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=ITeuGb2bYg">Policy Likelihood-based Query Sampling and Critic-Exploited Reset for Efficient Preference-based Reinforcement Learning</a></td>
<td width="420">Policy Likelihood-based Query Sampling and Critic-Exploited Reset uses reinforcement learning, preference feedback, or post-training signals to improve robot policies.</td>
<td width="230">-</td>
<td width="240">AR</td>
<td width="300">VLA / RL / Online Fine-tuning</td>
<td width="260">RL / offline RL</td>
<td width="240">RL fine-tuning / policy optimization</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=ITeuGb2bYg">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=TQhSodCM4r">SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning</a></td>
<td width="420">SimpleVLA-RL uses reinforcement learning, preference feedback, or post-training signals to improve robot policies.</td>
<td width="230">OpenVLA-OFT</td>
<td width="240">AR</td>
<td width="300">VLA / RL / RL/online fine-tuning / Reward S</td>
<td width="260">GRPO</td>
<td width="240">On-Policy / MF</td>
<td width="200">Sim ✓ (MT) / Real ✓ (ST)</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=TQhSodCM4r">paper</a> / <a href="https://arxiv.org/pdf/2509.09674">paper</a> / <a href="https://arxiv.org/abs/2509.09674">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=uWJwQ5SZoM">Robust Fine-tuning of Vision-Language-Action Robot Policies via Parameter Merging</a></td>
<td width="420">Robust Fine-tuning of Vision-Language-Action Robot Policies studies VLA robustness under multimodal perturbations, adversarial inputs, or distribution shifts.</td>
<td width="230">No specific base VLA specified.</td>
<td width="240">AR</td>
<td width="300">VLA / RL / Online Fine-tuning</td>
<td width="260">-</td>
<td width="240">RL fine-tuning / policy optimization</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=uWJwQ5SZoM">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=dc90uPqxWF">World2Minecraft: Occupancy-Driven simulated scenes Construction</a></td>
<td width="420">World2Minecraft connects 3D geometry, spatial localization, or affordance priors to robot perception and manipulation.</td>
<td width="230">-</td>
<td width="240">3D/spatial grounding</td>
<td width="300">VLA / RL / Online Fine-tuning</td>
<td width="260">3D/spatial representation learning</td>
<td width="240">RL fine-tuning / policy optimization</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=dc90uPqxWF">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38876">Steering Visuomotor Policy in Open Worlds via Cross-View Goal Alignment</a></td>
<td width="420">This method lets users specify goals from their own camera view and aligns them to the agent view for open-world visuomotor control.</td>
<td width="230">-</td>
<td width="240">policy action</td>
<td width="300">VLA / RL / Online Fine-tuning</td>
<td width="260">-</td>
<td width="240">RL fine-tuning / policy optimization</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38876">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/63131">HIER: Human-in-the-Loop Imagination-Execution Refinement for General Real-World Vision-Language-Action Models</a></td>
<td width="420">HIER iteratively refines real-world VLA behavior with human-in-the-loop imagination, execution, and feedback.</td>
<td width="230">-</td>
<td width="240">-</td>
<td width="300">VLA / RL / Online Fine-tuning</td>
<td width="260">-</td>
<td width="240">-</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/63131">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://openreview.net/forum?id=RkdTtznSAL">Real-World Reinforcement Learning of Active Perception Behaviors</a></td>
<td width="420">This work trains active perception policies in the real world using privileged training signals and asymmetric advantage-weighted regression.</td>
<td width="230">-</td>
<td width="240">AR</td>
<td width="300">RL / Online Fine-tuning</td>
<td width="260">-</td>
<td width="240">-</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=RkdTtznSAL">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2505.19789">What Can RL Bring to VLA Generalization? An Empirical Study</a></td>
<td width="420">RLVLA studies how PPO, GRPO, and DPO-style reinforcement learning affect VLA cross-task generalization.</td>
<td width="230">OpenVLA</td>
<td width="240">AR</td>
<td width="300">VLA / RL / Online Fine-tuning</td>
<td width="260">PPO / GRPO / DPO</td>
<td width="240">Hybrid / MF</td>
<td width="200">Sim ✓ (MT)</td>
<td width="360">Measure what reinforcement learning contributes to VLA generalization.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2505.19789">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/gen-robot/RL4VLA">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2505.07395">ReinboT: Amplifying Robot Visual-Language Manipulation with Reinforcement Learning</a></td>
<td width="420">ReinboT uses reinforcement learning, preference feedback, or post-training signals to improve robot policies.</td>
<td width="230">ReinboT</td>
<td width="240">AR</td>
<td width="300">VLA / RL / Online Fine-tuning</td>
<td width="260">DT + RTG</td>
<td width="240">Off-Policy / MF</td>
<td width="200">Sim + Real</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2505.07395">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
</tbody>
</table>
