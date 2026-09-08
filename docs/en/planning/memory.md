# memory

[Home](../../../README.md) | [中文](../../zh-CN/planning/memory.md) | [Direction index](README.md)

Total: 11 papers.

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
<td width="120" nowrap>IROS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2410.11989">Dynamic Open-Vocabulary 3D Scene Graphs for Long-Term Language-Guided Mobile Manipulation</a></td>
<td width="420">DovSG uses dynamic open-vocabulary 3D scene graphs to support long-term language tasks, environment updates, and mobile manipulation.</td>
<td width="240">Memory Planning</td>
<td width="260">dynamic 3D scene graph</td>
<td width="300">long-term scene updates</td>
<td width="260">mobile manipulation planner</td>
<td width="260">Real robot</td>
<td width="360">Maintain long-term task memory with open-vocabulary scene graphs.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2410.11989">paper</a></td>
<td width="110" nowrap><a href="https://bjhyzj.github.io/dovsg-web/">project</a></td>
<td width="110" nowrap><a href="https://github.com/BJHYZJ/DovSG">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=1dH4ARGdwD">Scaling up Memory for Robotic Control via Experience Retrieval</a></td>
<td width="420">MemER fine-tunes a VLM to retrieve task-relevant keyframes, enabling VLA to handle minute-scale long-horizon memory tasks.</td>
<td width="240">Memory Planning</td>
<td width="260">experience retrieval/keyframe memory</td>
<td width="300">-</td>
<td width="260">VLA/action</td>
<td width="260">-</td>
<td width="360">Addresses retrieval and reuse of long-duration experiential memory in robot control.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=1dH4ARGdwD">paper</a></td>
<td width="110" nowrap><a href="https://jen-pan.github.io/memer/">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=79BOATBal9">Planning with an Embodied Learnable Memory</a></td>
<td width="420">EPM uses a VLM to maintain textual scene memory through additions, deletions, and edits for LLM planning.</td>
<td width="240">Memory Planning</td>
<td width="260">Embodied Perception Memory</td>
<td width="300">-</td>
<td width="260">memory</td>
<td width="260">PARTNR / dynamic indoor mobile manipulation</td>
<td width="360">Addresses memory updates and planner access to environment state in dynamic household mobile manipulation.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=79BOATBal9">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=9cLPurIZMj">Memory, Benchmark &amp; Robots: A Benchmark for Solving Complex Tasks with Reinforcement Learning</a></td>
<td width="420">Proposes MIKASA/MIKASA-Robo to evaluate RL agents on memory-intensive task capabilities.</td>
<td width="240">Memory Planning</td>
<td width="260">Memory Planning</td>
<td width="300">-</td>
<td width="260">memory</td>
<td width="260">-</td>
<td width="360">Provides standardized evaluation of memory capabilities in robotic manipulation.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=9cLPurIZMj">paper</a></td>
<td width="110" nowrap><a href="https://sites.google.com/view/memorybenchrobots/">project</a></td>
<td width="110" nowrap><a href="https://github.com/CognitiveAISystems/MIKASA-Robo">code</a></td>
<td width="240">MIKASA/MIKASA-Robo</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=E5L43l5EIu">Embodied Agents Meet Personalization: Investigating Challenges and Solutions Through the Lens of Memory Utilization</a></td>
<td width="420">Studies how memory enables personalized embodied assistance and organizes user-specific preferences and routines for future tasks.</td>
<td width="240">Memory Planning</td>
<td width="260">Memory Planning</td>
<td width="300">-</td>
<td width="260">memory</td>
<td width="260">-</td>
<td width="360">enhances long-term task memory</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=E5L43l5EIu">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/60897">HiMe: Hierarchical Embodied Memory for Long-Horizon Vision-Language-Action Control</a></td>
<td width="420">Uses hierarchical embodied memory to coordinate planning, monitoring, and execution in long-horizon VLA control.</td>
<td width="240">Memory Planning</td>
<td width="260">Memory Planning</td>
<td width="300">-</td>
<td width="260">VLA/action</td>
<td width="260">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/60897">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/66214">Spatial Memory for Out-of-Vision Manipulation in Vision-Language-Action</a></td>
<td width="420">Maintains spatial-semantic memory of unseen objects so VLA policies can manipulate targets outside the current view.</td>
<td width="240">Memory Planning</td>
<td width="260">Memory Planning</td>
<td width="300">-</td>
<td width="260">VLA/action</td>
<td width="260">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/66214">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2602.20200">Global Prior Meets Local Consistency: Dual-Memory Augmented Vision-Language-Action Model for Efficient Robotic Manipulation</a></td>
<td width="420">Uses global prior memory and local behavior memory to improve the efficiency and robustness of VLA action generation.</td>
<td width="240">Memory Planning</td>
<td width="260">dual memory</td>
<td width="300">-</td>
<td width="260">VLA/action</td>
<td width="260">-</td>
<td width="360">Addresses inefficient VLA action generation and unstable conditioning.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2602.20200">paper</a></td>
<td width="110" nowrap><a href="https://cybertronagent.github.io/OptimusVLA.github.io/">project</a></td>
<td width="110" nowrap><a href="https://github.com/iLearn-Lab/CVPR26-OptimusVLA">code</a></td>
<td width="240"><a href="https://huggingface.co/iLearn-Lab/OptimusVLA_Memory">hf</a></td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2501.00358">Embodied VideoAgent: Persistent Memory from Egocentric Videos and Embodied Sensors Enables Dynamic Scene Understanding</a></td>
<td width="420">Builds persistent scene memory from egocentric video, depth, and pose.</td>
<td width="240">Memory Planning</td>
<td width="260">persistent object memory + tool queries</td>
<td width="300">-</td>
<td width="260">LLM tool calls + embodied action primitives</td>
<td width="260">Ego4D-VQ3D, OpenEQA, EnvQA, real-world Franka demo</td>
<td width="360">Addresses long-term memory and object-state updates in dynamic 3D scene understanding.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2501.00358">paper</a></td>
<td width="110" nowrap><a href="https://embodied-videoagent.github.io/">project</a></td>
<td width="110" nowrap><a href="https://github.com/Embodied-VideoAgent/embodied-videoagent">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://iccv.thecvf.com/virtual/2025/poster/1915">Towards Long-Horizon Vision-Language-Action System: Reasoning, Acting and Memory</a></td>
<td width="420">Connects reasoning, action execution, and memory to support long-horizon VLA behavior in dynamic environments.</td>
<td width="240">Memory Planning</td>
<td width="260">Memory Planning</td>
<td width="300">-</td>
<td width="260">VLA/action</td>
<td width="260">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/1915">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2501.18564">SAM2Act: Integrating Visual Foundation Model with a Memory Architecture for Robotic Manipulation</a></td>
<td width="420">SAM2Act combines a vision foundation model with a memory architecture to improve multi-task manipulation generalization.</td>
<td width="240">Memory Planning</td>
<td width="260">Memory Planning</td>
<td width="300">-</td>
<td width="260">memory</td>
<td width="260">-</td>
<td width="360">Addresses insufficient generalization and spatial memory in manipulation policies for dynamic environments.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2501.18564">paper</a></td>
<td width="110" nowrap><a href="https://sam2act.github.io">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
</tbody>
</table>
