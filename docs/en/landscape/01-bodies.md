# Robot bodies and form factors

[Home](../../../README.md) | [中文](../../zh-CN/landscape/01-bodies.md) | [Landscape index](README.md)

Which body fits a task, balancing reach, mobility, cost and reliability?

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
<td width="240" nowrap><a id="01-01"></a>Bipeds and general-purpose humanoids</td>
<td width="300">Move and manipulate in human-scale spaces.</td>
<td width="320">Whole-body coordination, balance and morphology transfer.</td>
<td width="320">Fall protection, thermal management, service and reliable delivery.</td>
<td width="340">Sustained payload, workspace and recovery time.</td>
</tr>
<tr>
<td width="240" nowrap><a id="01-02"></a>Wheeled bimanual mobile manipulators</td>
<td width="300">Connect navigation, positioning and bimanual work.</td>
<td width="320">Joint base-arm planning and long-horizon policies.</td>
<td width="320">Base localization, lifts and workstation interfaces.</td>
<td width="340">Positioning error, task success and cycle time.</td>
</tr>
<tr>
<td width="240" nowrap><a id="01-03"></a>Quadrupeds and wheeled-legged robots</td>
<td width="300">Traverse stairs, slopes and uneven ground.</td>
<td width="320">Terrain adaptation and visual locomotion.</td>
<td width="320">Inspection payloads, protection and endurance.</td>
<td width="340">Terrain envelope, payload conditions and mission endurance.</td>
</tr>
<tr>
<td width="240" nowrap><a id="01-04"></a>Fixed industrial and collaborative arms</td>
<td width="300">Perform repetitive or flexible work in constrained cells.</td>
<td width="320">Fine manipulation, force control and skill transfer.</td>
<td width="320">Throughput, repeatability, tooling and integration service.</td>
<td width="340">Workspace, repeatability and force-control interfaces.</td>
</tr>
<tr>
<td width="240" nowrap><a id="01-05"></a>Small open and educational platforms</td>
<td width="300">Lower barriers to experiments, teaching and reproduction.</td>
<td width="320">Reproducible bodies and low-cost policy learning.</td>
<td width="320">Assembly, spares, documentation and developer support.</td>
<td width="340">Bill of materials, assembly process and openness scope.</td>
</tr>
<tr>
<td width="240" nowrap><a id="01-06"></a>Specialized, soft and wearable bodies</td>
<td width="300">Fit confined, compliant or human-coupled tasks.</td>
<td width="320">Morphology design, human-robot dynamics and soft modeling.</td>
<td width="320">Task-specific mechanics, comfort and maintenance.</td>
<td width="340">Intended users or settings, mechanical limits and validation conditions.</td>
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
<td width="280" nowrap><a href="https://toddlerbot.github.io/">ToddlerBot (Stanford University)</a></td>
<td width="300">University / open robot research</td>
<td width="520">Published robot design, assembly resources and loco-manipulation research.</td>
<td width="360">Research demonstration; Code or data public; not reproduced here</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://www.unitree.com/g1/">Unitree G1</a></td>
<td width="300">Company / robot platform</td>
<td width="520">Public product information for a humanoid body and optional configurations.</td>
<td width="360">Product or developer documentation public</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://franka.de/franka-research-3">Franka Research 3</a></td>
<td width="300">Company / research manipulator</td>
<td width="520">Research manipulator system and control integration entry point.</td>
<td width="360">Product or developer documentation public</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://www.universal-robots.com/products/">Universal Robots</a></td>
<td width="300">Company / collaborative manipulators</td>
<td width="520">Collaborative manipulator products and automation integration entry points.</td>
<td width="360">Product or developer documentation public</td>
</tr>
</tbody>
</table>

Examples illustrate parts of this domain, not every subcategory or a market ranking. Open resources have not been run locally; product pages do not establish availability, integration compatibility or independent performance. [Evidence rules and sources](sources.md).

## Interfaces with the wider system

Read the comparison criteria above as interface contracts: specify the configuration, units, timing, failure behavior and responsible layer. A suitable component does not by itself demonstrate a working integrated robot. Compare the same workload and operating envelope before transferring a result between research and deployment.

## Related research catalog

- [humanoid](../embodiment/humanoid.md)
- [bimanual](../embodiment/bimanual.md)
- [Physically Executable Navigation](../vln/physically-executable.md)

Source check: 2026-09-08
