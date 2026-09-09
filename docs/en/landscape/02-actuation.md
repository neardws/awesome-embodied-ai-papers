# Actuation and precision transmission

[Home](../../../README.md) | [中文](../../zh-CN/landscape/02-actuation.md) | [Landscape index](README.md)

How is electrical energy converted into controllable force and motion under impact, heat and wear?

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
<td width="240" nowrap><a id="02-01"></a>Motors and direct drives<br><a href="../products/topics/02-01.md">Product details</a></td>
<td width="300">Provide controllable torque and speed.</td>
<td width="320">Torque density, backdrivability and co-design.</td>
<td width="320">Thermal design, winding production and consistency.</td>
<td width="340">Continuous versus peak torque, efficiency curves and heating.</td>
</tr>
<tr>
<td width="240" nowrap><a id="02-02"></a>Strain-wave, planetary and cycloidal gearing<br><a href="../products/topics/02-02.md">Product details</a></td>
<td width="300">Multiply torque within a compact envelope.</td>
<td width="320">Friction, backlash compensation and compliance modeling.</td>
<td width="320">Life, precision, impact tolerance and batch variation.</td>
<td width="340">Ratio, backlash, stiffness and fatigue conditions.</td>
</tr>
<tr>
<td width="240" nowrap><a id="02-03"></a>Screws and linear actuators<br><a href="../products/topics/02-03.md">Product details</a></td>
<td width="300">Generate linear thrust and precise displacement.</td>
<td width="320">Nonlinear friction, load estimation and structural optimization.</td>
<td width="320">Lubrication, sealing, mounting and axial life.</td>
<td width="340">Rated thrust, stroke, speed and duty cycle.</td>
</tr>
<tr>
<td width="240" nowrap><a id="02-04"></a>Integrated joint modules<br><a href="../products/topics/02-04.md">Product details</a></td>
<td width="300">Package motor, transmission, drive and sensing as a joint.</td>
<td width="320">Modular bodies and dynamics identification.</td>
<td width="320">Wiring, heat removal, buses and replacement effort.</td>
<td width="340">Joint interface, mass, sustained output and bus latency.</td>
</tr>
<tr>
<td width="240" nowrap><a id="02-05"></a>Servo drives and low-level control<br><a href="../products/topics/02-05.md">Product details</a></td>
<td width="300">Execute current, velocity and position commands stably.</td>
<td width="320">High-bandwidth control, disturbance observers and torque estimation.</td>
<td width="320">Protection, real-time behavior and tuning.</td>
<td width="340">Control period, jitter and feedback resolution.</td>
</tr>
<tr>
<td width="240" nowrap><a id="02-06"></a>Bearings, brakes and moving connections<br><a href="../products/topics/02-06.md">Product details</a></td>
<td width="300">Support loads, hold safely at rest and route moving power.</td>
<td width="320">Contact wear, failure prediction and lightweight structures.</td>
<td width="320">Bearings, brakes, cable carriers, harnesses and seals.</td>
<td width="340">Load life, flex life, protection and service intervals.</td>
</tr>
</tbody>
</table>

## Technical and product details

<a href="../products/comparisons/02-actuation.md">Open 20 related comparison records</a>

Compare model-specific values, conditions, interfaces, research relationships and source issues. Full source excerpts and original exhibit links remain available underneath.

<a href="../products/references/06-03.md">Integrated joints and actuator modules</a> · <a href="../products/references/06-04.md">Frameless, miniature and direct-drive motors</a> · <a href="../products/references/06-05.md">Servo drives and motion control</a> · <a href="../products/references/06-06.md">Strain-wave reducers</a> · <a href="../products/references/06-07.md">Planetary, cycloidal and precision reducers</a> · <a href="../products/references/06-08.md">Screws and linear actuators</a> · <a href="../products/references/06-09.md">Bearings and precision supports</a> · <a href="../products/references/06-10.md">Brakes and clutches</a> · <a href="../products/references/06-11.md">Cable carriers, cables and harnesses</a> · <a href="../products/references/06-12.md">Seals and joint protection</a>

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
<td width="280" nowrap><a href="https://www.harmonicdrive.net/products">Harmonic Drive</a></td>
<td width="300">Company / transmission and actuators</td>
<td width="520">Precision gearing, rotary and linear actuators, and servo-drive product families.</td>
<td width="360">Product or developer documentation public</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://www.ti.com/applications/industrial/robotics/overview.html">Texas Instruments robotics design resources</a></td>
<td width="300">Company / electronics and control components</td>
<td width="520">Design resources for robot electronics, drives, sensing and communication.</td>
<td width="360">Product or developer documentation public</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://toddlerbot.github.io/">ToddlerBot (Stanford University)</a></td>
<td width="300">University / open robot research</td>
<td width="520">Published robot design, assembly resources and loco-manipulation research.</td>
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

- [humanoid](../embodiment/humanoid.md)
- [Humanoid & Biped Hardware Reference](../embodiment/hardware.md)

Source check: 2026-09-08
