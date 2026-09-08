# Perception, localization and spatial representations

[Home](../../../README.md) | [中文](../../zh-CN/landscape/06-perception.md) | [Landscape index](README.md)

How are sensor streams converted into states usable by navigation, planning and manipulation?

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
<td width="240" nowrap><a id="06-01"></a>Object recognition and open-vocabulary perception</td>
<td width="300">Identify task-relevant objects and properties.</td>
<td width="320">Open categories, referring expressions and out-of-distribution recognition.</td>
<td width="320">False detections, site data and inference cost.</td>
<td width="340">Task-relevant recall, false detections and latency.</td>
</tr>
<tr>
<td width="240" nowrap><a id="06-02"></a>Pose, geometry and affordances</td>
<td width="300">Locate graspable, contactable and actionable regions.</td>
<td width="320">Geometry-semantic fusion, pose estimation and contact priors.</td>
<td width="320">Calibration, occlusion handling and end-effector alignment.</td>
<td width="340">Pose error, reachability and downstream task success.</td>
</tr>
<tr>
<td width="240" nowrap><a id="06-03"></a>Localization, mapping and state estimation</td>
<td width="300">Maintain robot position relative to its environment.</td>
<td width="320">Multimodal fusion, loop closure and dynamic-scene estimation.</td>
<td width="320">Initialization, relocalization, map maintenance and degradation handling.</td>
<td width="340">Drift, relocalization time and availability.</td>
</tr>
<tr>
<td width="240" nowrap><a id="06-04"></a>3D reconstruction and scene representations</td>
<td width="300">Build queryable spatial models.</td>
<td width="320">Neural fields, Gaussian representations and geometric consistency.</td>
<td width="320">Mapping speed, storage, updates and tool interfaces.</td>
<td width="340">Geometry accuracy, update cost and query latency.</td>
</tr>
<tr>
<td width="240" nowrap><a id="06-05"></a>Semantic maps and spatial memory</td>
<td width="300">Retain scene knowledge across time and tasks.</td>
<td width="320">Topological graphs, retrieval memory and long-term consistency.</td>
<td width="320">Map versions, object changes and operational maintenance.</td>
<td width="340">Memory consistency, retrieval quality and task benefit.</td>
</tr>
<tr>
<td width="240" nowrap><a id="06-06"></a>Active perception and uncertainty</td>
<td width="300">Choose where to look next and when to reobserve.</td>
<td width="320">Information gain, exploration and uncertainty calibration.</td>
<td width="320">Sensing budgets, safe motion and anomaly triggers.</td>
<td width="340">Observation cost, calibration error and failure reduction.</td>
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
<td width="280" nowrap><a href="https://docs.nav2.org/rolling/">Nav2 community</a></td>
<td width="300">Open-source community / autonomous navigation</td>
<td width="520">Navigation framework with planning, control and behavior interfaces.</td>
<td width="360">Code or data public; not reproduced here</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://robotic-view-transformer.github.io/">RVT research team</a></td>
<td width="300">Research collaboration / 3D manipulation</td>
<td width="520">Multi-view representations and policies for 3D manipulation.</td>
<td width="360">Research demonstration; Code or data public; not reproduced here</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://voxposer.github.io/">VoxPoser research team</a></td>
<td width="300">Academic research / spatial planning</td>
<td width="520">Connects language goals with spatial value representations and manipulation planning.</td>
<td width="360">Research demonstration; Code or data public; not reproduced here</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://www.nvidia.com/en-us/industries/robotics/">NVIDIA robotics platform</a></td>
<td width="300">Company / compute and development platform</td>
<td width="520">Platform roles across training, simulation, accelerated robot software and edge inference.</td>
<td width="360">Product or developer documentation public</td>
</tr>
</tbody>
</table>

Examples illustrate parts of this domain, not every subcategory or a market ranking. Open resources have not been run locally; product pages do not establish availability, integration compatibility or independent performance. [Evidence rules and sources](sources.md).

## Interfaces with the wider system

Read the comparison criteria above as interface contracts: specify the configuration, units, timing, failure behavior and responsible layer. A suitable component does not by itself demonstrate a working integrated robot. Compare the same workload and operating envelope before transferring a result between research and deployment.

## Related research catalog

- [Map Memory](../vln/map-memory.md)
- [3D grounding](../vla/3d-grounding.md)

Source check: 2026-09-08
