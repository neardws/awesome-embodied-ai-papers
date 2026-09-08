# safety evaluation

[Home](../../../README.md) | [中文](../../zh-CN/deployment/safety-evaluation.md) | [Direction index](README.md)

Total: 13 papers.

<table width="3090">
<thead>
<tr>
<th width="120" nowrap>Venue/Year</th>
<th width="320">Paper/Method</th>
<th width="420">Abstract</th>
<th width="240">Object Type</th>
<th width="280">Efficiency Metric</th>
<th width="280">Platform/Hardware</th>
<th width="280">Covered Tasks</th>
<th width="220">Open Resource Status</th>
<th width="360">Paper Task/Goal</th>
<th width="110" nowrap>Paper</th>
<th width="110" nowrap>Project</th>
<th width="110" nowrap>Code</th>
<th width="240">Data/Bench</th>
</tr>
</thead>
<tbody>
<tr>
<td width="120" nowrap>CoRL 2024</td>
<td width="320"><a href="https://scholar.google.com/scholar?q=DriveVLM%3A+The+Convergence+of+Autonomous+Driving+and+Large+Vision-Language+Models">DriveVLM: The Convergence of Autonomous Driving and Large Vision-Language Models</a></td>
<td width="420">DriveVLM studies autonomous driving through large vision-language models.</td>
<td width="240">safety evaluation</td>
<td width="280">deployment/evaluation coverage</td>
<td width="280">robot/simulator platform</td>
<td width="280">embodied robot tasks</td>
<td width="220">source-listed resource</td>
<td width="360">Add CoRL deployment/evaluation coverage.</td>
<td width="110" nowrap><a href="https://scholar.google.com/scholar?q=DriveVLM%3A+The+Convergence+of+Autonomous+Driving+and+Large+Vision-Language+Models">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2025</td>
<td width="320"><a href="https://proceedings.iclr.cc/paper_files/paper/2025/file/5ab848771ff8c9c47aac4128e2ef9f4e-Paper-Conference.pdf">HASARD: A Benchmark for Vision-Based Safe Reinforcement Learning in Embodied Agents</a></td>
<td width="420">HASARD benchmarks vision-based safe reinforcement learning for embodied agents.</td>
<td width="240">safety evaluation</td>
<td width="280">safe-RL benchmark coverage</td>
<td width="280">benchmark platform</td>
<td width="280">vision-based safe RL</td>
<td width="220">HASARD</td>
<td width="360">Evaluate safe RL agents under embodied visual observations.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2503.08241">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2022</td>
<td width="320"><a href="https://openreview.net/forum?id=dwi57JI_-K&noteId=pfmgIWaQAoN">SafeBench: A Benchmarking Platform for Safety Evaluation of Autonomous Vehicles</a></td>
<td width="420">SafeBench provides a benchmark platform for autonomous-vehicle safety evaluation.</td>
<td width="240">safety evaluation</td>
<td width="280">autonomous driving safety scenarios</td>
<td width="280">benchmark platform</td>
<td width="280">driving safety evaluation</td>
<td width="220">SafeBench</td>
<td width="360">Evaluate safety risks in autonomous driving scenarios.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2206.09682">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>IROS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2410.15185">Semantically Safe Robot Manipulation: From Semantic Scene Understanding to Motion Safeguards</a></td>
<td width="420">Uses LLM commonsense reasoning to identify semantic risks and map them into robot manipulation safety filters.</td>
<td width="240">semantic safety layer</td>
<td width="280">safety evaluation</td>
<td width="280">robot manipulation safety</td>
<td width="280">semantic scene understanding + safeguards</td>
<td width="220">project available</td>
<td width="360">Adds semantic risk reasoning to the robot manipulation safety loop.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2410.15185">paper</a></td>
<td width="110" nowrap><a href="https://utiasdsl.github.io/semantic-manipulation/">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=8s5jBVybhQ">Remotely Detectable Robot Policy Watermarking</a></td>
<td width="420">Proposes CoNoCo to detect robot policy watermarks from remote video/mocap observations without affecting the action distribution.</td>
<td width="240">policy watermarking</td>
<td width="280">safety</td>
<td width="280">robot deployment/evaluation environment</td>
<td width="280">remote safety/provenance detection</td>
<td width="220">-</td>
<td width="360">Addresses remote verification of robot policy intellectual property and unauthorized use.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=8s5jBVybhQ">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=Gsrw1vxq1G">RoboMD: Uncovering Robot Vulnerabilities through Semantic Potential Fields</a></td>
<td width="420">RoboMD actively searches for vulnerable regions in semantic visual embedding potential fields for safety discovery and retraining.</td>
<td width="240">vulnerability discovery</td>
<td width="280">safety</td>
<td width="280">robot deployment/evaluation environment</td>
<td width="280">manipulation robustness</td>
<td width="220">-</td>
<td width="360">Addresses expensive vulnerability testing on real robots and the difficulty of enumerating unknown perturbations.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=Gsrw1vxq1G">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/60472">Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds</a></td>
<td width="420">Fuses diverse point-cloud inputs with 2D observations to improve VLA robustness across simulator, sensor, and real domains.</td>
<td width="240">benchmark/dataset</td>
<td width="280">benchmark/dataset</td>
<td width="280">robot deployment/evaluation environment</td>
<td width="280">Evaluate robustness and safety.</td>
<td width="220">-</td>
<td width="360">Evaluate robustness and safety.</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/60472">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/62679">PACT: Self-Evolving Physical Safety Alignment for Diffusion Policies in Embodied Manipulation</a></td>
<td width="420">Post-trains diffusion policies with physical-constraint alignment to reduce safety violations without demonstrations or rewards.</td>
<td width="240">benchmark/dataset</td>
<td width="280">safety</td>
<td width="280">robot deployment/evaluation environment</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/62679">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/61584">SafeLab: An Interactive High-Fidelity Benchmark for Embodied Safety in Scientific Robotics</a></td>
<td width="420">Provides a high-fidelity lab simulation benchmark with safety tasks, calibrated assets, and expert trajectories.</td>
<td width="240">benchmark/dataset</td>
<td width="280">safety</td>
<td width="280">simulation/evaluation environment</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/61584">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/64080">Dismantling the Illusion of Vision-Language-Action Models Competence via Explicit Distributional Shifts</a></td>
<td width="420">Introduces LIBERO-Gen to expose VLA brittleness under explicit semantic and environmental distribution shifts.</td>
<td width="240">benchmark/dataset</td>
<td width="280">benchmark/dataset</td>
<td width="280">robot deployment/evaluation environment</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/64080">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2510.13626">LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models</a></td>
<td width="420">Systematically reveals VLA robustness failures through seven perturbation types and 10,030 tasks.</td>
<td width="240">benchmark/dataset</td>
<td width="280">benchmark/dataset</td>
<td width="280">robot deployment/evaluation environment</td>
<td width="280">7 perturbation dimensions / 10,030 tasks</td>
<td width="220">Project+Code+Data/Bench</td>
<td width="360">Addresses VLA scoring high on standard benchmarks while remaining vulnerable to real-world perturbations.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2510.13626">paper</a> / <a href="https://arxiv.org/pdf/2510.13626">paper</a></td>
<td width="110" nowrap><a href="https://sylvestf.github.io/LIBERO-plus/">project</a></td>
<td width="110" nowrap><a href="https://github.com/sylvestf/LIBERO-plus">code</a></td>
<td width="240"><a href="https://huggingface.co/datasets/Sylvest/LIBERO-plus">hf</a></td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2506.05294">A Smooth Sea Never Made a Skilled SAILOR: Robust Imitation via Learning to Search</a></td>
<td width="420">SAILOR learns search, world models, and reward models from demonstrations so imitation policies can recover from erroneous states.</td>
<td width="240">benchmark/dataset</td>
<td width="280">safety</td>
<td width="280">robot deployment/evaluation environment</td>
<td width="280">12 visual manipulation tasks</td>
<td width="220">Project</td>
<td width="360">Addresses behavior cloning's inability to recover after leaving the demonstration distribution.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2506.05294">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/arnavkj1995/SAILOR">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2506.23725">PAC Bench: Do Foundation Models Understand Prerequisites for Executing Manipulation Policies?</a></td>
<td width="420">PAC Bench evaluates whether VLMs understand manipulation prerequisites such as object properties, affordances, and constraints.</td>
<td width="240">benchmark/dataset</td>
<td width="280">safety</td>
<td width="280">robot deployment/evaluation environment</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">Addresses the unverified low-level physical prerequisites behind high-level robot abilities of foundation models.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2506.23725">paper</a></td>
<td width="110" nowrap><a href="https://pacbench.github.io/">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">30k annotations / 673 images / 100 scenarios / 120 sim constraints</td>
</tr>
</tbody>
</table>
