# Simulation and training infrastructure

[Home](../../../README.md) | [中文](../../zh-CN/landscape/11-simulation.md) | [Landscape index](README.md)

How can controlled experiments accelerate development while exposing what simulation cannot replace?

This page distinguishes subcategory questions, research priorities and industrial delivery concerns. These are editorial comparison axes; the cited examples below have narrower, explicitly described scopes.

## Subcategories and problems

<table width="1520">
<thead>
<tr>
<th width="240" nowrap>Subcategory</th>
<th width="300">Problem</th>
<th width="320">Research focus</th>
<th width="320">Industrial focus</th>
<th width="340">Comparison criteria</th>
</tr>
</thead>
<tbody>
<tr>
<td width="240" nowrap><a id="11-01"></a>Physics engines and contact solving<br><a href="../products/topics/11-01.md">Product details</a></td>
<td width="300">Compute motion, collision and contact responses.</td>
<td width="320">Differentiable physics, friction models and numerical stability.</td>
<td width="320">Solver speed, model calibration and asset compatibility.</td>
<td width="340">Contact error, stability and simulation throughput.</td>
</tr>
<tr>
<td width="240" nowrap><a id="11-02"></a>Digital twins and asset construction<br><a href="../products/topics/11-02.md">Product details</a></td>
<td width="300">Build digital representations of scenes, robots and objects.</td>
<td width="320">Reconstruction, parameter identification and automated asset generation.</td>
<td width="320">Asset quality, version maintenance and site consistency.</td>
<td width="340">Geometry and dynamics error, creation cost and update time.</td>
</tr>
<tr>
<td width="240" nowrap><a id="11-03"></a>Sensor simulation and synthetic data<br><a href="../products/topics/11-03.md">Product details</a></td>
<td width="300">Generate multimodal observations and labels.</td>
<td width="320">Rendering fidelity, tactile simulation and data mixing.</td>
<td width="320">Generation workflows, annotation standards and domain-gap assessment.</td>
<td width="340">Sensor gap, label quality and real-task benefit.</td>
</tr>
<tr>
<td width="240" nowrap><a id="11-04"></a>Parallel training and experiment management<br><a href="../products/topics/11-04.md">Product details</a></td>
<td width="300">Improve policy training and comparison efficiency.</td>
<td width="320">Distributed sampling, optimization stability and reproducibility.</td>
<td width="320">Resource scheduling, checkpoints, cost and pinned versions.</td>
<td width="340">Training budget, seed variance and reproducible runs.</td>
</tr>
<tr>
<td width="240" nowrap><a id="11-05"></a>Domain randomization and transfer<br><a href="../products/topics/11-05.md">Product details</a></td>
<td width="300">Reduce behavioral differences between simulation and hardware.</td>
<td width="320">Adaptive randomization, identification and residual learning.</td>
<td width="320">Real calibration, transfer tests and fallback behavior.</td>
<td width="340">Real-task success and data needed for transfer.</td>
</tr>
<tr>
<td width="240" nowrap><a id="11-06"></a>Software- and hardware-in-the-loop validation<br><a href="../products/topics/11-06.md">Product details</a></td>
<td width="300">Test control and communication chains before release.</td>
<td width="320">Co-simulation, temporal consistency and boundary coverage.</td>
<td width="320">Real controller integration, fault injection and regression tests.</td>
<td width="340">Timing error, fault coverage and repeatability.</td>
</tr>
</tbody>
</table>

## Technical and product details

<a href="../products/comparisons/11-simulation.md">Open 4 related comparison records</a>

Compare model-specific values, conditions, interfaces, research relationships and source issues. Full source excerpts and original exhibit links remain available underneath.

<a href="../products/references/09-04.md">Simulation, synthetic data and evaluation</a> · <a href="../products/references/11-01.md">Universities, institutes and research teams</a>

## Research, platforms and industrial examples

<table width="1460">
<thead>
<tr>
<th width="280" nowrap>Participant / project</th>
<th width="300">Role</th>
<th width="520">Documented contribution</th>
<th width="360">Evidence status</th>
</tr>
</thead>
<tbody>
<tr>
<td width="280" nowrap><a href="https://mujoco.org/">MuJoCo / Google DeepMind</a></td>
<td width="300">Company-backed open source / physics simulation</td>
<td width="520">Physics simulator used for robotics and contact-dynamics research.</td>
<td width="360">Code or data public; not reproduced here</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://isaac-sim.github.io/IsaacLab/main/index.html">NVIDIA Isaac Lab</a></td>
<td width="300">Company and community / training framework</td>
<td width="520">Simulation environments and training workflows for robot learning.</td>
<td width="360">Code or data public; not reproduced here</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://robotwin-platform.github.io/">RoboTwin collaboration</a></td>
<td width="300">Universities, institutes and companies / data and evaluation</td>
<td width="520">Bimanual task generation, domain randomization and unified evaluation resources.</td>
<td width="360">Research demonstration; Code or data public; not reproduced here</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://www.nvidia.com/en-us/industries/robotics/">NVIDIA robotics platform</a></td>
<td width="300">Company / compute and development platform</td>
<td width="520">Platform roles across training, simulation, accelerated robot software and edge inference.</td>
<td width="360">Product or developer documentation public</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://www.lightwheel.ai/">Lightwheel</a></td>
<td width="300">Company / simulation, data and evaluation</td>
<td width="520">Public descriptions of simulation assets, egocentric data and simulation evaluation platforms.</td>
<td width="360">Product or developer documentation public</td>
</tr>
</tbody>
</table>

Examples illustrate parts of this domain, not every subcategory or a market ranking. Open resources have not been run locally; product pages do not establish availability, integration compatibility or independent performance. [Evidence rules and sources](sources.md).

## Interfaces with the wider system

Read the comparison criteria above as interface contracts: specify the configuration, units, timing, failure behavior and responsible layer. A suitable component does not by itself demonstrate a working integrated robot. Compare the same workload and operating envelope before transferring a result between research and deployment.

## Related research catalog

- [sim2real](../deployment/sim2real.md)
- [video/latent world model](../wam/video-latent.md)

Source check: 2026-09-08
