# joint WAM

[Home](../../../README.md) | [中文](../../zh-CN/wam/joint.md) | [Direction index](README.md)

Total: 3 papers.

<table width="3110">
<thead>
<tr>
<th width="120" nowrap>Venue/Year</th>
<th width="320">Paper/Method</th>
<th width="420">Abstract</th>
<th width="220">WAM Type</th>
<th width="280">State Representation</th>
<th width="260">Action Interface</th>
<th width="360">Use</th>
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
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=IvUM6UwYCJ">Empowering Multi-Robot Cooperation via Sequential World Models</a></td>
<td width="420">SeqWM uses an autoregressive agent-wise world model to reduce the complexity of modeling joint dynamics for multi-robot systems.</td>
<td width="220">joint WAM</td>
<td width="280">sequential agent-wise world models</td>
<td width="260">multi-agent RL actions</td>
<td width="360">multi-robot cooperation/planning</td>
<td width="200">Sim + Real</td>
<td width="360">Address complex joint dynamics in physical multi-robot cooperation and poor scalability of MBRL.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=IvUM6UwYCJ">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/zhaozijie2022/seqwm-marl">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/64447">Dual-Stream Diffusion for World-Model Augmented Vision-Language-Action Model</a></td>
<td width="420">DUST uses a dual-stream diffusion Transformer to model vision and action separately while sharing cross-modal information.</td>
<td width="220">joint WAM</td>
<td width="280">vision tokens + action tokens</td>
<td width="260">diffusion/flow-matching action tokens</td>
<td width="360">world-model augmented VLA</td>
<td width="200">RoboCasa, GR-1, Franka Research 3</td>
<td width="360">Address training difficulties from visual-action modality differences when jointly predicting states and actions in VLA.</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/64447">paper</a></td>
<td width="110" nowrap><a href="https://periphanes.github.io/dust/">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2507.11296">Diffusion-Based Imaginative Coordination for Bimanual Manipulation</a></td>
<td width="420">Improve bimanual manipulation coordination through joint video and action diffusion prediction.</td>
<td width="220">joint WAM</td>
<td width="280">multi-frame latent future states</td>
<td width="260">diffusion action prediction</td>
<td width="360">bimanual coordination</td>
<td width="200">ALOHA + RoboTwin + Real</td>
<td width="360">Address policy-learning difficulty caused by high-dimensional action spaces and complex coordination in bimanual manipulation.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2507.11296">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/return-sleep/Diffusion_based_imaginative_Coordination">code</a></td>
<td width="240">-</td>
</tr>
</tbody>
</table>
