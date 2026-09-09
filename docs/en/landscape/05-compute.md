# Compute, communication and energy

[Home](../../../README.md) | [中文](../../zh-CN/landscape/05-compute.md) | [Landscape index](README.md)

How can high-compute inference coexist with deterministic control on one robot?

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
<td width="240" nowrap><a id="05-01"></a>Inference chips and heterogeneous acceleration<br><a href="../products/topics/05-01.md">Product details</a></td>
<td width="300">Execute perception and policy models on-device.</td>
<td width="320">Compression, compilation and model-hardware co-design.</td>
<td width="320">Operator support, toolchains, memory and supply.</td>
<td width="340">Measured target-model latency, memory and power.</td>
</tr>
<tr>
<td width="240" nowrap><a id="05-02"></a>Edge computers and domain controllers<br><a href="../products/topics/05-02.md">Product details</a></td>
<td width="300">Host sensors, models and system services together.</td>
<td width="320">Multi-task scheduling, compute hierarchy and resource sharing.</td>
<td width="320">Cooling, connectors, vibration tolerance and remote management.</td>
<td width="340">Latency under concurrency, thermal steady state and interfaces.</td>
</tr>
<tr>
<td width="240" nowrap><a id="05-03"></a>Real-time microcontrollers and power drives<br><a href="../products/topics/05-03.md">Product details</a></td>
<td width="300">Maintain low-level loops and motor protection.</td>
<td width="320">Real-time scheduling, robust control and fault detection.</td>
<td width="320">Current sampling, protection chains and firmware maintenance.</td>
<td width="340">Worst-case control period, jitter and fault response.</td>
</tr>
<tr>
<td width="240" nowrap><a id="05-04"></a>On-robot buses and industrial networks<br><a href="../products/topics/05-04.md">Product details</a></td>
<td width="300">Transport time-sensitive states and commands.</td>
<td width="320">Networked control and clock synchronization.</td>
<td width="320">Wiring, compatibility, diagnostics and electromagnetic conditions.</td>
<td width="340">End-to-end delay, packet loss, synchronization and recovery.</td>
</tr>
<tr>
<td width="240" nowrap><a id="05-05"></a>Wireless, cloud-edge and remote connectivity<br><a href="../products/topics/05-05.md">Product details</a></td>
<td width="300">Support teleoperation, updates and cross-device collaboration.</td>
<td width="320">Delay compensation, offloading and disconnected autonomy.</td>
<td width="320">Coverage, bandwidth, identity management and rollback.</td>
<td width="340">Offline behavior, uplink load and takeover delay.</td>
</tr>
<tr>
<td width="240" nowrap><a id="05-06"></a>Batteries, power conversion and thermal management<br><a href="../products/topics/05-06.md">Product details</a></td>
<td width="300">Deliver stable energy during sustained tasks.</td>
<td width="320">Energy modeling, energy-aware planning and thermal control.</td>
<td width="320">Battery management, charging or swapping, cooling and life.</td>
<td width="340">Mission endurance, peak current, heating and cycle life.</td>
</tr>
</tbody>
</table>

## Technical and product details

<a href="../products/comparisons/05-compute.md">Open 23 related comparison records</a>

Compare model-specific values, conditions, interfaces, research relationships and source issues. Full source excerpts and original exhibit links remain available underneath.

<a href="../products/references/03-06.md">Mobile charging services</a> · <a href="../products/references/08-01.md">AI chips and heterogeneous computing</a> · <a href="../products/references/08-02.md">Edge computers and robot controllers</a> · <a href="../products/references/08-03.md">MCUs and power semiconductors</a> · <a href="../products/references/08-04.md">Industrial and wireless communication</a> · <a href="../products/references/08-05.md">Electronic components and sensing chips</a> · <a href="../products/references/08-06.md">Batteries, BMS and smart charging</a> · <a href="../products/references/08-07.md">Power supplies and drive modules</a>

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
<td width="280" nowrap><a href="https://www.nvidia.com/en-us/industries/robotics/">NVIDIA robotics platform</a></td>
<td width="300">Company / compute and development platform</td>
<td width="520">Platform roles across training, simulation, accelerated robot software and edge inference.</td>
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
</tbody>
</table>

Examples illustrate parts of this domain, not every subcategory or a market ranking. Open resources have not been run locally; product pages do not establish availability, integration compatibility or independent performance. [Evidence rules and sources](sources.md).

## Interfaces with the wider system

Read the comparison criteria above as interface contracts: specify the configuration, units, timing, failure behavior and responsible layer. A suitable component does not by itself demonstrate a working integrated robot. Compare the same workload and operating envelope before transferring a result between research and deployment.

## Related research catalog

- [real-time execution](../deployment/real-time.md)
- [quantization/cache/tokenization](../deployment/quantization-cache-tokenization.md)

Source check: 2026-09-08
