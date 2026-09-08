# Safety and Robustness

[Home](../../../README.md) | [中文](../../zh-CN/vla/safety-robustness.md) | [Direction index](README.md)

Total: 7 papers.

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
<td width="120" nowrap>NeurIPS 2024</td>
<td width="320"><a href="https://proceedings.neurips.cc/paper_files/paper/2024/hash/d83fd70a31c64e020844ec80705ba87f-Abstract-Conference.html">Diffusion Policy Attacker: Crafting Adversarial Attacks for Diffusion-based Policies</a></td>
<td width="420">DPA studies adversarial attacks against diffusion-based robot policies.</td>
<td width="230">diffusion policy</td>
<td width="240">continuous action</td>
<td width="300">VLA / safety and robustness</td>
<td width="260">diffusion policy attack</td>
<td width="240">adversarial robustness evaluation</td>
<td width="200">robot policy benchmarks</td>
<td width="360">Evaluate attack surfaces in diffusion-based robot policies.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2405.19424">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=OwinX7PI83">BEAT: Visual Backdoor Attacks on VLM-based Embodied Agents via Contrastive Trigger Learning</a></td>
<td width="420">BEAT crafts visual backdoor attacks for VLM-based embodied agents using contrastive trigger learning.</td>
<td width="230">VLM embodied agent</td>
<td width="240">policy action</td>
<td width="300">VLA / safety and robustness</td>
<td width="260">contrastive trigger learning</td>
<td width="240">backdoor attack evaluation</td>
<td width="200">embodied agent benchmarks</td>
<td width="360">Expose visual backdoor risks in embodied VLM agents.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2510.27623">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICRA 2025</td>
<td width="320"><a href="https://ieeexplore.ieee.org/document/11128017/">Run-time Observation Interventions Make Vision-Language-Action Models More Visually Robust</a></td>
<td width="420">BYOVLA identifies and edits task-irrelevant visual regions at runtime to make Octo/OpenVLA more robust to visual distractors.</td>
<td width="230">Octo / OpenVLA</td>
<td width="240">AR / policy action</td>
<td width="300">VLA / safety and robustness</td>
<td width="260">run-time observation intervention</td>
<td width="240">robust VLA execution</td>
<td width="200">Real robot manipulation</td>
<td width="360">Reduce VLA failures caused by irrelevant visual perturbations during real-world deployment.</td>
<td width="110" nowrap><a href="https://ieeexplore.ieee.org/document/11128017/">paper</a></td>
<td width="110" nowrap><a href="https://aasherh.github.io/byovla/">project</a></td>
<td width="110" nowrap><a href="https://github.com/irom-princeton/byovla">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=cS6xizdYD5">On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations</a></td>
<td width="420">On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations studies VLA robustness under multimodal perturbations, adversarial inputs, or distribution shifts.</td>
<td width="230">π0 / OpenVLA</td>
<td width="240">Diffusion / Flow</td>
<td width="300">VLA / safety / safety and robustness</td>
<td width="260">RobustVLA; 17 perturbations across 4 modalities</td>
<td width="240">Flow policy</td>
<td width="200">LIBERO + real FR5</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=cS6xizdYD5">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2503.03480">SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning</a></td>
<td width="420">SafeVLA aligns VLA policies with safety constraints through constrained reinforcement learning.</td>
<td width="230">SPOC</td>
<td width="240">AR</td>
<td width="300">VLA / safety and robustness</td>
<td width="260">PPO with constrained learning</td>
<td width="240">On-policy / MF</td>
<td width="200">Sim ✓ (ST)</td>
<td width="360">Improve safety alignment of VLA policies before deployment.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2503.03480">paper</a></td>
<td width="110" nowrap><a href="https://sites.google.com/view/pku-safevla">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2505.16640">BadVLA: Towards Backdoor Attacks on Vision-Language-Action Models via Objective-Decoupled Optimization</a></td>
<td width="420">BadVLA studies how to inject backdoor triggers into VLAs and affect robot action outputs.</td>
<td width="230">No specific base VLA specified.</td>
<td width="240">AR</td>
<td width="300">VLA / safety and robustness</td>
<td width="260">objective-decoupled backdoor attack</td>
<td width="240">-</td>
<td width="200">-</td>
<td width="360">Constructs and evaluates backdoor attacks against VLA robot policies.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2505.16640">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2411.13587">Exploring the Adversarial Vulnerabilities of Vision-Language-Action Models in Robotics</a></td>
<td width="420">Exploring the Adversarial Vulnerabilities of Vision-Language-Action Models in Robotics studies VLA robustness under multimodal perturbations, adversarial inputs, or distribution shifts.</td>
<td width="230">No specific base VLA specified.</td>
<td width="240">AR</td>
<td width="300">VLA / safety and robustness</td>
<td width="260">UADA / UPA / TMA adversarial attacks</td>
<td width="240">3D-grounded policy/perception</td>
<td width="200">simulation + physical setup</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2411.13587">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">LIBERO + BridgeData V2 attack assets</td>
</tr>
</tbody>
</table>
