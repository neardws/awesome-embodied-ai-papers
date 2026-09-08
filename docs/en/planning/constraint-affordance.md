# constraint / affordance planning

[Home](../../../README.md) | [中文](../../zh-CN/planning/constraint-affordance.md) | [Direction index](README.md)

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
<td width="120" nowrap>CoRL 2023</td>
<td width="320"><a href="https://arxiv.org/abs/2307.05973">VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models</a></td>
<td width="420">VoxPoser composes 3D value maps from language models for manipulation planning.</td>
<td width="240">Task Decomposition</td>
<td width="260">language/scene context</td>
<td width="300">execution feedback</td>
<td width="260">robot action interface</td>
<td width="260">embodied benchmarks</td>
<td width="360">Add CoRL planning coverage.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2307.05973">paper</a></td>
<td width="110" nowrap><a href="https://voxposer.github.io">project</a></td>
<td width="110" nowrap><a href="https://github.com/huangwl18/VoxPoser">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICRA 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2408.14769">Points2Plans: From Point Clouds to Long-Horizon Plans with Composable Relational Dynamics</a></td>
<td width="420">Points2Plans connects high-level plans with continuous parameter planning from point clouds and language instructions through relational dynamics.</td>
<td width="240">Constraint / Affordance Planning</td>
<td width="260">point-cloud relational dynamics</td>
<td width="300">composable planning feedback</td>
<td width="260">continuous parameter planner</td>
<td width="260">Sim + Real</td>
<td width="360">Ground language plans in executable 3D relational dynamics constraints.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2408.14769">paper</a></td>
<td width="110" nowrap><a href="https://sites.google.com/stanford.edu/points2plans">project</a></td>
<td width="110" nowrap><a href="https://github.com/yixuanhuang98/Points2Plans">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=enprG5H9aD">SLAP: Shortcut Learning for Abstract Planning</a></td>
<td width="420">SLAP automatically discovers low-level shortcut options from existing TAMP options.</td>
<td width="240">TAMP option/shortcut learning</td>
<td width="260">-</td>
<td width="300">Constraint/Affordance</td>
<td width="260">planning / affordance</td>
<td width="260">-</td>
<td width="360">Addresses the reliance of TAMP abstract actions on manual definitions and the resulting limited behavior space.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=enprG5H9aD">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=kWCNhRdcDI">Natural Language PDDL (NL-PDDL) for Open-world Goal-oriented Commonsense Regression Planning in Embodied AI</a></td>
<td width="420">Uses natural-language PDDL for open-world goal-regression planning.</td>
<td width="240">commonsense regression planning</td>
<td width="260">NL-PDDL</td>
<td width="300">Constraint/Affordance</td>
<td width="260">planning / affordance</td>
<td width="260">-</td>
<td width="360">Addresses long-horizon causal planning in open worlds with partial observability and incomplete knowledge.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=kWCNhRdcDI">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=refcXHU1Nh">SafeFlowMatcher: Safe and Fast Planning using Flow Matching with Control Barrier Functions</a></td>
<td width="420">Combines a flow matching planner with control barrier functions to ensure fast and safe planning.</td>
<td width="240">Constraint/Affordance</td>
<td width="260">CBF safety constraints</td>
<td width="300">prediction-correction integrator</td>
<td width="260">VLA/action</td>
<td width="260">-</td>
<td width="360">Addresses the lack of formal safety constraints in generative path planning.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=refcXHU1Nh">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=bGPDviEtZ1">MoMaGen: Generating Demonstrations under Soft and Hard Constraints for Multi-Step Bimanual Mobile Manipulation</a></td>
<td width="420">Automatically generates multi-step bimanual mobile-manipulation demonstrations under soft and hard constraints.</td>
<td width="240">constraint-conditioned demonstration generation</td>
<td width="260">-</td>
<td width="300">-</td>
<td width="260">planning / affordance</td>
<td width="260">-</td>
<td width="360">Addresses the high cost of collecting multi-step bimanual mobile-manipulation demonstrations.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=bGPDviEtZ1">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38907">A3D: Adaptive Affordance Assembly with Dual-Arm Manipulation</a></td>
<td width="420">Learns adaptive affordances for dual-arm assembly, updating manipulation choices as object and task states change.</td>
<td width="240">Constraint/Affordance</td>
<td width="260">-</td>
<td width="300">-</td>
<td width="260">planning / affordance</td>
<td width="260">-</td>
<td width="360">dual-arm adaptive affordance assembly</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38907">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38909">Affordance-Guided Coarse-to-Fine Exploration for Base Placement in Open-Vocabulary Mobile Manipulation</a></td>
<td width="420">Guides mobile-manipulator base placement with affordance priors followed by coarse-to-fine feasibility refinement.</td>
<td width="240">coarse-to-fine base placement</td>
<td width="260">affordance guidance</td>
<td width="300">-</td>
<td width="260">planning / affordance</td>
<td width="260">-</td>
<td width="360">Uses affordances to guide base-placement exploration in open-vocabulary mobile manipulation.</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38909">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38955">Gentle Manipulation Policy Learning via Demonstrations from VLM Planned Atomic Skills</a></td>
<td width="420">Uses VLM-planned atomic skills as demonstrations to learn policies for gentle long-horizon manipulation.</td>
<td width="240">Constraint/Affordance</td>
<td width="260">VLM-planned atomic skills</td>
<td width="300">-</td>
<td width="260">VLA/action</td>
<td width="260">-</td>
<td width="360">gentle manipulation policy learning</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38955">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://openreview.net/forum?id=wr47LsSUjH">InstructFlow: Adaptive Symbolic Constraint-Guided Code Generation for Long-Horizon Planning</a></td>
<td width="420">InstructFlow uses symbolic feedback flows to inject failure-induced constraints into instruction graphs and code generation.</td>
<td width="240">Constraint/Affordance</td>
<td width="260">Constraint/Affordance</td>
<td width="300">failure diagnosis + symbolic constraints</td>
<td width="260">flow matching / planning / reasoning</td>
<td width="260">-</td>
<td width="360">Addresses hallucinated long-horizon planning code from LLMs, physical infeasibility, and poor failure recovery.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=wr47LsSUjH">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/chiht21/InstructFlow">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://iccv.thecvf.com/virtual/2025/poster/542">CoA-VLA: Improving Vision-Language-Action Models via Visual-Text Chain-of-Affordance</a></td>
<td width="420">Uses visual-text affordance chains to enhance VLA reasoning at test time.</td>
<td width="240">Constraint/Affordance</td>
<td width="260">-</td>
<td width="300">test-time affordance reasoning</td>
<td width="260">VLA/action</td>
<td width="260">-</td>
<td width="360">Addresses insufficient self-driven affordance reasoning and robust action in VLA.</td>
<td width="110" nowrap><a href="https://openaccess.thecvf.com/content/ICCV2025/papers/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.pdf">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
</tbody>
</table>
