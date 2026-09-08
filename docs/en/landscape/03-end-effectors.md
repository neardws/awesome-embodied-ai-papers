# End effectors and manipulation mechanisms

[Home](../../../README.md) | [中文](../../zh-CN/landscape/03-end-effectors.md) | [Landscape index](README.md)

How should contact mechanisms be matched to objects and processes beyond adding fingers?

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
<td width="240" nowrap><a id="03-01"></a>Parallel and adaptive grippers</td>
<td width="300">Hold objects with varying sizes or shapes.</td>
<td width="320">Grasp synthesis, compliance design and contact modeling.</td>
<td width="320">Fingertip tooling, life, grasp detection and interfaces.</td>
<td width="340">Opening, gripping force, mass and replaceable fingertips.</td>
</tr>
<tr>
<td width="240" nowrap><a id="03-02"></a>Suction, pneumatic and soft tools</td>
<td width="300">Handle sheets, fragile items and irregular shapes.</td>
<td width="320">Sealing contact, deformation and grasp feasibility.</td>
<td width="320">Air supply, leakage, contamination and consumable replacement.</td>
<td width="340">Surface compatibility, pressure differential and failure detection.</td>
</tr>
<tr>
<td width="240" nowrap><a id="03-03"></a>Multi-finger dexterous hands</td>
<td width="300">Reorient objects after grasping.</td>
<td width="320">High-dimensional learning, in-hand manipulation and hand transfer.</td>
<td width="320">Drive integration, durability, tactile placement and supply.</td>
<td width="340">Active versus total degrees of freedom, fingertip force and control interface.</td>
</tr>
<tr>
<td width="240" nowrap><a id="03-04"></a>Tendon-driven, underactuated and biomimetic mechanisms</td>
<td width="300">Reduce hand mass and actuator count.</td>
<td width="320">Coupling identification, hysteresis compensation and morphology computation.</td>
<td width="320">Tension adjustment, transmission service and consistency.</td>
<td width="340">Independent control dimensions, hysteresis, tension and life.</td>
</tr>
<tr>
<td width="240" nowrap><a id="03-05"></a>Tool changing and process tooling</td>
<td width="300">Switch between grasping, fastening and processing.</td>
<td width="320">Tool-use reasoning and contact-skill composition.</td>
<td width="320">Changer repeatability, utility connections and process qualification.</td>
<td width="340">Changeover time, connection reliability and tool calibration.</td>
</tr>
<tr>
<td width="240" nowrap><a id="03-06"></a>Bimanual and hand-arm coordination</td>
<td width="300">Support, hand over or assemble objects cooperatively.</td>
<td width="320">Coupled constraints, role assignment and coordination policies.</td>
<td width="320">Collision avoidance, synchronization and cell layout.</td>
<td width="340">Coordination success, contact forces and synchronization error.</td>
</tr>
</tbody>
</table>

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
<td width="280" nowrap><a href="https://arxiv.org/abs/2309.06440">LEAP Hand research team</a></td>
<td width="300">Academic research / open hardware</td>
<td width="520">Low-cost dexterous hand design and robot-learning experiments reported in the paper.</td>
<td width="360">Research demonstration</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://shadowrobot.com/dexterous-hand-series/">Shadow Robot dexterous hands</a></td>
<td width="300">Company / dexterous hardware</td>
<td width="520">Multi-finger hand families intended for research and development.</td>
<td width="360">Product or developer documentation public</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://franka.de/franka-research-3">Franka Research 3</a></td>
<td width="300">Company / research manipulator</td>
<td width="520">Research manipulator system and control integration entry point.</td>
<td width="360">Product or developer documentation public</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://umi-gripper.github.io/">UMI research team</a></td>
<td width="300">Academic research / data tools</td>
<td width="520">Portable teaching interface and transfer from human demonstrations to robot policies.</td>
<td width="360">Research demonstration; Code or data public; not reproduced here</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://www.inspire-robots.com/">Inspire Robots</a></td>
<td width="300">Company / miniature actuators and dexterous hands</td>
<td width="520">Miniature servo actuators, dexterous hand families and product documentation.</td>
<td width="360">Product or developer documentation public</td>
</tr>
</tbody>
</table>

Examples illustrate parts of this domain, not every subcategory or a market ranking. Open resources have not been run locally; product pages do not establish availability, integration compatibility or independent performance. [Evidence rules and sources](sources.md).

## Interfaces with the wider system

Read the comparison criteria above as interface contracts: specify the configuration, units, timing, failure behavior and responsible layer. A suitable component does not by itself demonstrate a working integrated robot. Compare the same workload and operating envelope before transferring a result between research and deployment.

## Related research catalog

- [dexterous hand](../embodiment/dexterous-hand.md)
- [bimanual](../embodiment/bimanual.md)

Source check: 2026-09-08
