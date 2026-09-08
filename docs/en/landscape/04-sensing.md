# Sensing and interaction hardware

[Home](../../../README.md) | [中文](../../zh-CN/landscape/04-sensing.md) | [Landscape index](README.md)

How are environment, body and contact signals measured and aligned?

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
<td width="240" nowrap><a id="04-01"></a>Imaging, depth and 3D vision</td>
<td width="300">Capture appearance, geometry and distance.</td>
<td width="320">Occlusion, transparent or reflective objects and active vision.</td>
<td width="320">Calibration, lighting tolerance, interfaces and bandwidth.</td>
<td width="340">Depth error, field of view, frame rate and synchronization.</td>
</tr>
<tr>
<td width="240" nowrap><a id="04-02"></a>LiDAR, radar and ranging</td>
<td width="300">Support ranging over distance and difficult environments.</td>
<td width="320">Sensor fusion, moving targets and sparse perception.</td>
<td width="320">Mounting occlusion, environmental protection and cost.</td>
<td width="340">Range, angular resolution, return conditions and latency.</td>
</tr>
<tr>
<td width="240" nowrap><a id="04-03"></a>Inertial, encoder and proprioceptive sensing</td>
<td width="300">Estimate body attitude, joint positions and motion.</td>
<td width="320">Drift correction, state estimation and sensor fault tolerance.</td>
<td width="320">Thermal drift, wiring, mounting and time synchronization.</td>
<td width="340">Noise, drift, resolution and update rate.</td>
</tr>
<tr>
<td width="240" nowrap><a id="04-04"></a>Force/torque and joint-torque sensing</td>
<td width="300">Measure contact loads and external forces.</td>
<td width="320">Force estimation, compliance control and collision detection.</td>
<td width="320">Overload protection, calibration and industrial communication.</td>
<td width="340">Range, cross-talk, hysteresis and sample rate.</td>
</tr>
<tr>
<td width="240" nowrap><a id="04-05"></a>Tactile arrays and electronic skin</td>
<td width="300">Sense contact distribution, slip and local geometry.</td>
<td width="320">Cross-sensor representations and visuotactile fusion.</td>
<td width="320">Wear, replaceable skin, wiring and batch calibration.</td>
<td width="340">Taxel coverage, synchronization, slip detection and durability.</td>
</tr>
<tr>
<td width="240" nowrap><a id="04-06"></a>Motion capture, speech and human interfaces</td>
<td width="300">Connect human motion and intent to robots.</td>
<td width="320">Intent understanding, retargeting and multimodal interaction.</td>
<td width="320">Comfort, occlusion, latency and operator burden.</td>
<td width="340">Tracking error, end-to-end latency and interaction success.</td>
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
<td width="280" nowrap><a href="https://www.gelsight.com/product/digit-tactile-sensor/">GelSight DIGIT</a></td>
<td width="300">Company / tactile device</td>
<td width="520">Product page for a tactile sensor used in manipulation research.</td>
<td width="360">Product or developer documentation public</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://www.ati-ia.com/products/ft/sensors.aspx">ATI force/torque sensors</a></td>
<td width="300">Company / force sensing</td>
<td width="520">Force/torque measurement systems and their industrial and research uses.</td>
<td width="360">Product or developer documentation public</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://www.unitree.com/g1/">Unitree G1</a></td>
<td width="300">Company / robot platform</td>
<td width="520">Public product information for a humanoid body and optional configurations.</td>
<td width="360">Product or developer documentation public</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://umi-gripper.github.io/">UMI research team</a></td>
<td width="300">Academic research / data tools</td>
<td width="520">Portable teaching interface and transfer from human demonstrations to robot policies.</td>
<td width="360">Research demonstration; Code or data public; not reproduced here</td>
</tr>
</tbody>
</table>

Examples illustrate parts of this domain, not every subcategory or a market ranking. Open resources have not been run locally; product pages do not establish availability, integration compatibility or independent performance. [Evidence rules and sources](sources.md).

## Interfaces with the wider system

Read the comparison criteria above as interface contracts: specify the configuration, units, timing, failure behavior and responsible layer. A suitable component does not by itself demonstrate a working integrated robot. Compare the same workload and operating envelope before transferring a result between research and deployment.

## Related research catalog

- [tactile/contact-rich](../embodiment/tactile-contact.md)
- [Map Memory](../vln/map-memory.md)

Source check: 2026-09-08
