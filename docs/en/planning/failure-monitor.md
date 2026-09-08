# failure monitor

[Home](../../../README.md) | [中文](../../zh-CN/planning/failure-monitor.md) | [Direction index](README.md)

Total: 9 papers.

<table width="3110">
<thead>
<tr>
<th width="120" nowrap>Venue/Year</th>
<th width="320">Paper/Method</th>
<th width="420">Abstract</th>
<th width="240">Planning Granularity</th>
<th width="260">Tool/Memory</th>
<th width="300">Feedback/Self-Improvement</th>
<th width="260">Execution Interface</th>
<th width="260">Validation Environment</th>
<th width="360">Paper Task/Goal</th>
<th width="110" nowrap>Paper</th>
<th width="110" nowrap>Project</th>
<th width="110" nowrap>Code</th>
<th width="240">Data/Bench</th>
</tr>
</thead>
<tbody>
<tr>
<td width="120" nowrap>ICRA 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2510.16281">Do What You Say: Grounding Language-Conditioned Robotic Actions with Vision-Language Models</a></td>
<td width="420">This method checks at runtime whether a VLA's textual reasoning matches its action outcome before deciding whether to execute the action.</td>
<td width="240">Failure Monitor</td>
<td width="260">VLM reasoning checker</td>
<td width="300">reasoning-action consistency</td>
<td width="260">VLA action selection</td>
<td width="260">Real robot manipulation</td>
<td width="360">Detect whether the stated plan and executed action are consistent.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2510.16281">paper</a></td>
<td width="110" nowrap><a href="https://yilin-wu98.github.io/steering-reasoning-vla/">project</a></td>
<td width="110" nowrap><a href="https://github.com/NVlabs/actalign">code</a></td>
<td width="240"><a href="https://github.com/NVlabs/actalign">data</a></td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=N22lDHYrXe">Experience-based Knowledge Correction for Robust Planning in Minecraft</a></td>
<td width="420">XENON revises dependency graphs and action knowledge from experience to improve the robustness of long-horizon planning in Minecraft.</td>
<td width="240">Failure Monitor</td>
<td width="260">experience-based knowledge correction</td>
<td width="300">Failure Monitor</td>
<td width="260">failure monitor</td>
<td width="260">Minecraft</td>
<td width="360">Addresses incorrect initial LLM knowledge that is difficult to correct through feedback.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=N22lDHYrXe">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=WC6MJ5r5Bj">ReCAPA: Hierarchical Predictive Correction to Mitigate Cascading Failures</a></td>
<td width="420">ReCAPA predicts and corrects deviations at the action, subgoal, and trajectory levels to suppress cascading failures.</td>
<td width="240">Failure Monitor</td>
<td width="260">-</td>
<td width="300">hierarchical predictive correction</td>
<td width="260">failure monitor</td>
<td width="260">-</td>
<td width="360">Addresses propagation of local errors through multi-step VLA execution.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2604.21232">paper</a></td>
<td width="110" nowrap><a href="https://sunandreas0437-svg.github.io/recapa-project-page/">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=jr9hGWQioP">Self-Refining Vision Language Model for Robotic Failure Detection and Reasoning</a></td>
<td width="420">ARMOR models failure detection and natural-language cause explanation as a multi-round self-refinement task.</td>
<td width="240">Failure Monitor</td>
<td width="260">-</td>
<td width="300">self-refinement</td>
<td width="260">failure monitor</td>
<td width="260">-</td>
<td width="360">Addresses subtle, combinatorial real-robot failures with scarce annotations.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2602.12405">paper</a></td>
<td width="110" nowrap><a href="https://sites.google.com/utexas.edu/armor">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/61750">Sentinel-VLA: A Metacognitive VLA Model with Active Status Monitoring for Dynamic Reasoning and Error Recovery</a></td>
<td width="420">Adds active status monitoring so a VLA model can detect execution problems and trigger recovery reasoning.</td>
<td width="240">Failure Monitor</td>
<td width="260">-</td>
<td width="300">Failure Monitor</td>
<td width="260">VLA/action</td>
<td width="260">-</td>
<td width="360">detects and repairs execution failures</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/61750">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/63650">NeurVLA: Unleashing Failure-Handling Capability of Vision-Language-Action Models via Neural-Symbolic Reasoning</a></td>
<td width="420">Uses neural-symbolic reasoning to diagnose failures and improve recovery behavior in VLA manipulation policies.</td>
<td width="240">Failure Monitor</td>
<td width="260">-</td>
<td width="300">Failure Monitor</td>
<td width="260">VLA/action</td>
<td width="260">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/63650">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/64203">Can VLMs Diagnose and Recover from VLA Manipulation Faults?</a></td>
<td width="420">Evaluates whether VLMs can diagnose manipulation faults and guide recovery for failed VLA executions.</td>
<td width="240">Failure Monitor</td>
<td width="260">-</td>
<td width="300">Failure Monitor</td>
<td width="260">VLA/action</td>
<td width="260">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/64203">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2510.09459">Failure Prediction at Runtime for Generative Robot Policies</a></td>
<td width="420">FIPER predicts runtime failures of generative imitation policies without requiring failure data.</td>
<td width="240">Failure Monitor</td>
<td width="260">-</td>
<td width="300">runtime failure prediction</td>
<td width="260">failure monitor</td>
<td width="260">-</td>
<td width="360">Addresses early failure prediction when deploying diffusion/flow manipulation policies.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2510.09459">paper</a></td>
<td width="110" nowrap><a href="https://tum-lsy.github.io/fiper_website">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2412.04455">Code-as-Monitor: Constraint-aware Visual Programming for Reactive and Proactive Robotic Failure Detection</a></td>
<td width="420">Uses a VLM to generate constraint-monitoring code for both reactive and preventive failure detection.</td>
<td width="240">Failure Monitor</td>
<td width="260">VLM-generated monitor code + constraint elements</td>
<td width="300">Failure Monitor</td>
<td width="260">closed-loop monitor over open-loop policy</td>
<td width="260">CLIPort, OmniGibson, real-world</td>
<td width="360">Addresses real-time detection and prevention of open-set robot failures.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2412.04455">paper</a></td>
<td width="110" nowrap><a href="https://zhoues.github.io/Code-as-Monitor/">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
</tbody>
</table>
