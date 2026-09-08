# Manufacturing, integration and delivery

[Home](../../../README.md) | [中文](../../zh-CN/landscape/13-manufacturing.md) | [Landscape index](README.md)

How can prototypes become manufacturable, serviceable deliverables with explicit configurations?

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
<td width="240" nowrap><a id="13-01"></a>Structural materials and precision manufacturing</td>
<td width="300">Meet strength, weight and dimensional requirements.</td>
<td width="320">Lightweight structures, materials design and topology optimization.</td>
<td width="320">Process capability, finishing and tolerance control.</td>
<td width="340">Mass, tolerances, fatigue and material batches.</td>
</tr>
<tr>
<td width="240" nowrap><a id="13-02"></a>Additive manufacturing and rapid iteration</td>
<td width="300">Shorten design validation and prototype fabrication cycles.</td>
<td width="320">Complex structures, compliant devices and multi-material design.</td>
<td width="320">Process selection, post-processing and consistency.</td>
<td width="340">Prototype lead time, strength anisotropy and rework rate.</td>
</tr>
<tr>
<td width="240" nowrap><a id="13-03"></a>Assembly, calibration and factory tests</td>
<td width="300">Reduce performance variation between units.</td>
<td width="320">Automated calibration, identification and error propagation.</td>
<td width="320">Assembly processes, test fixtures and traceable records.</td>
<td width="340">Calibration residuals, yield and consistency.</td>
</tr>
<tr>
<td width="240" nowrap><a id="13-04"></a>Supply chain and configuration management</td>
<td width="300">Control component changes and system consequences.</td>
<td width="320">Substitution-friendly design and modular architectures.</td>
<td width="320">Bills of materials, alternatives, versions and lead times.</td>
<td width="340">Configuration traceability, substitution validation and service compatibility.</td>
</tr>
<tr>
<td width="240" nowrap><a id="13-05"></a>System integration and workstation adaptation</td>
<td width="300">Integrate robots into actual business workflows.</td>
<td width="320">Task modeling, human-robot cooperation and hybrid automation.</td>
<td width="320">Tooling, site interfaces, commissioning and acceptance.</td>
<td width="340">Retrofit time, stable cycle time and exception handling.</td>
</tr>
<tr>
<td width="240" nowrap><a id="13-06"></a>Service, training and lifecycle support</td>
<td width="300">Maintain equipment and workforce readiness over time.</td>
<td width="320">Predictive maintenance, serviceability design and skill transfer.</td>
<td width="320">Spares, training, repair procedures and version support.</td>
<td width="340">Repair time, maintenance cost and support period.</td>
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
<td width="280" nowrap><a href="https://www.protolabs.com/industries/robotics/">Protolabs</a></td>
<td width="300">Company / manufacturing services</td>
<td width="520">Machining, additive manufacturing and molding services for robot parts.</td>
<td width="360">Product or developer documentation public</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://www.harmonicdrive.net/products">Harmonic Drive</a></td>
<td width="300">Company / transmission and actuators</td>
<td width="520">Precision gearing, rotary and linear actuators, and servo-drive product families.</td>
<td width="360">Product or developer documentation public</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://toddlerbot.github.io/">ToddlerBot (Stanford University)</a></td>
<td width="300">University / open robot research</td>
<td width="520">Published robot design, assembly resources and loco-manipulation research.</td>
<td width="360">Research demonstration; Code or data public; not reproduced here</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://www.nist.gov/el/intelligent-systems-division-73500/robotic-grasping-and-manipulation-assembly">NIST</a></td>
<td width="300">Research institute / measurement and evaluation</td>
<td width="520">Performance-measurement research for grasping, manipulation and assembly.</td>
<td width="360">Research demonstration</td>
</tr>
</tbody>
</table>

Examples illustrate parts of this domain, not every subcategory or a market ranking. Open resources have not been run locally; product pages do not establish availability, integration compatibility or independent performance. [Evidence rules and sources](sources.md).

## Interfaces with the wider system

Read the comparison criteria above as interface contracts: specify the configuration, units, timing, failure behavior and responsible layer. A suitable component does not by itself demonstrate a working integrated robot. Compare the same workload and operating envelope before transferring a result between research and deployment.

## Related research catalog

- [sim2real](../deployment/sim2real.md)
- [Humanoid & Biped Hardware Reference](../embodiment/hardware.md)

Source check: 2026-09-08
