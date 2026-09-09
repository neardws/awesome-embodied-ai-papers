# System software and integration platforms

[Home](../../../README.md) | [中文](../../zh-CN/landscape/09-systems.md) | [Landscape index](README.md)

How are heterogeneous devices, models and skills composed into a developable and debuggable system?

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
<td width="240" nowrap><a id="09-01"></a>Operating systems and communication middleware<br><a href="../products/topics/09-01.md">Product details</a></td>
<td width="300">Organize processes, messages and distributed components.</td>
<td width="320">Real-time communication, modularity and system architecture.</td>
<td width="320">Version support, deployment configuration and compatibility.</td>
<td width="340">Message latency, service lifecycle and diagnosability.</td>
</tr>
<tr>
<td width="240" nowrap><a id="09-02"></a>Drivers, hardware abstraction and control interfaces<br><a href="../products/topics/09-02.md">Product details</a></td>
<td width="300">Unify sensor reads and actuator commands.</td>
<td width="320">Interface abstraction, controller switching and sim-real consistency.</td>
<td width="320">Driver maintenance, calibration, fault codes and device support.</td>
<td width="340">Interface coverage, state semantics and timing consistency.</td>
</tr>
<tr>
<td width="240" nowrap><a id="09-03"></a>Navigation and manipulation stacks<br><a href="../products/topics/09-03.md">Product details</a></td>
<td width="300">Combine perception, planning and control modules.</td>
<td width="320">Pluggable algorithms and end-to-end system comparison.</td>
<td width="320">Site tuning, robot adaptation and stable releases.</td>
<td width="340">Integration cost, completion and exception handling.</td>
</tr>
<tr>
<td width="240" nowrap><a id="09-04"></a>Skill libraries, behavior trees and workflows<br><a href="../products/topics/09-04.md">Product details</a></td>
<td width="300">Express task order, concurrency and recovery.</td>
<td width="320">Skill composition, formal constraints and hierarchical decisions.</td>
<td width="320">Visual orchestration, interface versions and operator permissions.</td>
<td width="340">Skill reuse, failure localization and recovery paths.</td>
</tr>
<tr>
<td width="240" nowrap><a id="09-05"></a>Development, debugging and observability<br><a href="../products/topics/09-05.md">Product details</a></td>
<td width="300">Explain runtime data and failures.</td>
<td width="320">Causal debugging, log compression and interpretable execution.</td>
<td width="320">Replay, visualization, alerts and remote diagnostics.</td>
<td width="340">Time to reproduce failures, log completeness and diagnosis cost.</td>
</tr>
<tr>
<td width="240" nowrap><a id="09-06"></a>Facility integration and multi-robot coordination<br><a href="../products/topics/09-06.md">Product details</a></td>
<td width="300">Coordinate robots with lifts, doors and fleets.</td>
<td width="320">Multi-agent scheduling, conflict resolution and cooperation.</td>
<td width="320">Facility protocols, task systems, traffic and permissions.</td>
<td width="340">Congestion, throughput, resource waits and exception recovery.</td>
</tr>
</tbody>
</table>

## Technical and product details

<a href="../products/comparisons/09-systems.md">Open 3 related comparison records</a>

Compare model-specific values, conditions, interfaces, research relationships and source issues. Full source excerpts and original exhibit links remain available underneath.

<a href="../products/references/09-05.md">Robot operating systems and skill platforms</a> · <a href="../products/references/09-06.md">Enterprise agents and AI services</a>

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
<td width="280" nowrap><a href="https://github.com/ros2/ros2">ROS 2 community</a></td>
<td width="300">Open-source community / middleware</td>
<td width="520">Primary repository and component entry points for the robot software ecosystem.</td>
<td width="360">Code or data public; not reproduced here</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://github.com/ros-controls/ros2_control">ros2_control community</a></td>
<td width="300">Open-source community / control framework</td>
<td width="520">Open framework connecting controllers and robot hardware interfaces.</td>
<td width="360">Code or data public; not reproduced here</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://moveit.ai/">MoveIt / PickNik</a></td>
<td width="300">Community and company / manipulation software</td>
<td width="520">Motion planning, kinematics, perception and execution interfaces, with a commercial support offering.</td>
<td width="360">Code or data public; not reproduced here; Product or developer documentation public</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://docs.nav2.org/rolling/">Nav2 community</a></td>
<td width="300">Open-source community / autonomous navigation</td>
<td width="520">Navigation framework with planning, control and behavior interfaces.</td>
<td width="360">Code or data public; not reproduced here</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://www.open-rmf.org/">Open-RMF community</a></td>
<td width="300">Open-source ecosystem / multi-robot coordination</td>
<td width="520">Coordination framework for robot fleets and facility interactions.</td>
<td width="360">Code or data public; not reproduced here</td>
</tr>
</tbody>
</table>

Examples illustrate parts of this domain, not every subcategory or a market ranking. Open resources have not been run locally; product pages do not establish availability, integration compatibility or independent performance. [Evidence rules and sources](sources.md).

## Interfaces with the wider system

Read the comparison criteria above as interface contracts: specify the configuration, units, timing, failure behavior and responsible layer. A suitable component does not by itself demonstrate a working integrated robot. Compare the same workload and operating envelope before transferring a result between research and deployment.

## Related research catalog

- [constraint / affordance planning](../planning/constraint-affordance.md)
- [real-time execution](../deployment/real-time.md)

Source check: 2026-09-08
