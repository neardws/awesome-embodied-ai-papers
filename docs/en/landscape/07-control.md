# Motion control and action learning

[Home](../../../README.md) | [中文](../../zh-CN/landscape/07-control.md) | [Landscape index](README.md)

How are task goals converted into continuous, stable and dynamically feasible actions?

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
<td width="240" nowrap><a id="07-01"></a>Kinematics and trajectory planning<br><a href="../products/topics/07-01.md">Product details</a></td>
<td width="300">Find reachable and collision-free motion paths.</td>
<td width="320">Constraint solving, sampling and optimization planning.</td>
<td width="320">Robot models, collision geometry and execution timing.</td>
<td width="340">Planning success, computation time and collision margins.</td>
</tr>
<tr>
<td width="240" nowrap><a id="07-02"></a>Model predictive and optimal control<br><a href="../products/topics/07-02.md">Product details</a></td>
<td width="300">Adapt actions under dynamics constraints in a receding horizon.</td>
<td width="320">Model error, constrained optimization and stability.</td>
<td width="320">Real-time solving, state estimation and degraded operation.</td>
<td width="340">Worst-case solve time, tracking error and constraint violations.</td>
</tr>
<tr>
<td width="240" nowrap><a id="07-03"></a>Force, impedance and contact control<br><a href="../products/topics/07-03.md">Product details</a></td>
<td width="300">Regulate force and compliance during contact.</td>
<td width="320">Contact transitions, unknown stiffness and safe exploration.</td>
<td width="320">Process tuning, sensor calibration and overload protection.</td>
<td width="340">Force error, overshoot and damage rate.</td>
</tr>
<tr>
<td width="240" nowrap><a id="07-04"></a>Legged and whole-body coordination<br><a href="../products/topics/07-04.md">Product details</a></td>
<td width="300">Coordinate balance, locomotion, arms and contacts.</td>
<td width="320">Motion imitation, foothold planning and multi-contact optimization.</td>
<td width="320">Body limits, thermal load and fall recovery.</td>
<td width="340">Terrain completion, energy use and recovery capability.</td>
</tr>
<tr>
<td width="240" nowrap><a id="07-05"></a>Imitation, diffusion and flow policies<br><a href="../products/topics/07-05.md">Product details</a></td>
<td width="300">Learn multimodal action distributions from demonstrations.</td>
<td width="320">Action representations, temporal modeling and compounding error.</td>
<td width="320">Collection cost, inference latency and control-rate matching.</td>
<td width="340">Success, action smoothness and end-to-end latency.</td>
</tr>
<tr>
<td width="240" nowrap><a id="07-06"></a>Reinforcement learning and online adaptation<br><a href="../products/topics/07-06.md">Product details</a></td>
<td width="300">Improve policies through feedback and adapt to changes.</td>
<td width="320">Reward design, sample efficiency and safe learning.</td>
<td width="320">Real-world trial cost, takeover and rollback.</td>
<td width="340">Additional interactions, risk exposure and sustained performance.</td>
</tr>
</tbody>
</table>

## Technical and product details

<a href="../products/comparisons/07-control.md">Open 1 related comparison records</a>

Compare model-specific values, conditions, interfaces, research relationships and source issues. Full source excerpts and original exhibit links remain available underneath.

<a href="../products/references/02-02.md">Collaborative arms and adaptive force control</a>

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
<td width="280" nowrap><a href="https://moveit.ai/">MoveIt / PickNik</a></td>
<td width="300">Community and company / manipulation software</td>
<td width="520">Motion planning, kinematics, perception and execution interfaces, with a commercial support offering.</td>
<td width="360">Code or data public; not reproduced here; Product or developer documentation public</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://github.com/ros-controls/ros2_control">ros2_control community</a></td>
<td width="300">Open-source community / control framework</td>
<td width="520">Open framework connecting controllers and robot hardware interfaces.</td>
<td width="360">Code or data public; not reproduced here</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://diffusion-policy.cs.columbia.edu/">Diffusion Policy research team</a></td>
<td width="300">Academic and industrial research / action learning</td>
<td width="520">Generates visuomotor action sequences through conditional diffusion.</td>
<td width="360">Research demonstration; Code or data public; not reproduced here</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://franka.de/franka-research-3">Franka Research 3</a></td>
<td width="300">Company / research manipulator</td>
<td width="520">Research manipulator system and control integration entry point.</td>
<td width="360">Product or developer documentation public</td>
</tr>
</tbody>
</table>

Examples illustrate parts of this domain, not every subcategory or a market ranking. Open resources have not been run locally; product pages do not establish availability, integration compatibility or independent performance. [Evidence rules and sources](sources.md).

## Interfaces with the wider system

Read the comparison criteria above as interface contracts: specify the configuration, units, timing, failure behavior and responsible layer. A suitable component does not by itself demonstrate a working integrated robot. Compare the same workload and operating envelope before transferring a result between research and deployment.

## Related research catalog

- [diffusion/flow policy](../vla/diffusion-flow.md)
- [humanoid](../embodiment/humanoid.md)

Source check: 2026-09-08
