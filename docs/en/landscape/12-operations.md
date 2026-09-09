# Evaluation, safety, deployment and operations

[Home](../../../README.md) | [中文](../../zh-CN/landscape/12-operations.md) | [Landscape index](README.md)

How is single-task performance turned into measurable, recoverable and sustained system capability?

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
<td width="240" nowrap><a id="12-01"></a>Capability benchmarks and task evaluation<br><a href="../products/topics/12-01.md">Product details</a></td>
<td width="300">Measure capability under comparable conditions.</td>
<td width="320">Task design, generalization splits and statistical significance.</td>
<td width="320">Mapping to site tasks, acceptance conditions and regression suites.</td>
<td width="340">Success, coverage, variance and failure distribution.</td>
</tr>
<tr>
<td width="240" nowrap><a id="12-02"></a>Reliability and long-horizon testing<br><a href="../products/topics/12-02.md">Product details</a></td>
<td width="300">Expose failures accumulating during sustained operation.</td>
<td width="320">Error propagation, robustness and lifetime modeling.</td>
<td width="320">Aging tests, interruptions and spare-part service.</td>
<td width="340">Operating duration, failure frequency and recovery time.</td>
</tr>
<tr>
<td width="240" nowrap><a id="12-03"></a>Safety constraints and system protection<br><a href="../products/topics/12-03.md">Product details</a></td>
<td width="300">Limit hazardous actions and failure propagation.</td>
<td width="320">Safe control, constraint verification and risk awareness.</td>
<td width="320">Protection chains, emergency stops, isolation and responsibility boundaries.</td>
<td width="340">Constraint violations, response time and validation coverage.</td>
</tr>
<tr>
<td width="240" nowrap><a id="12-04"></a>Edge deployment and model updates<br><a href="../products/topics/12-04.md">Product details</a></td>
<td width="300">Run models reliably on target devices.</td>
<td width="320">Compression, caching, inference scheduling and online adaptation.</td>
<td width="320">Release management, staged updates, rollback and compatibility.</td>
<td width="340">End-to-end latency, resource use and regression results.</td>
</tr>
<tr>
<td width="240" nowrap><a id="12-05"></a>Takeover, diagnostics and recovery<br><a href="../products/topics/12-05.md">Product details</a></td>
<td width="300">Maintain controllable operation during failures.</td>
<td width="320">Anomaly detection, recovery policies and human-robot cooperation.</td>
<td width="320">Alerts, remote takeover, fault localization and resets.</td>
<td width="340">Intervention count, takeover delay and completion after recovery.</td>
</tr>
<tr>
<td width="240" nowrap><a id="12-06"></a>Fleet, service and operational metrics<br><a href="../products/topics/12-06.md">Product details</a></td>
<td width="300">Manage multi-robot tasks and ongoing service.</td>
<td width="320">Cooperative scheduling, queues and resource optimization.</td>
<td width="320">Work orders, availability, service cost and facility integration.</td>
<td width="340">Throughput, utilization, cost per task and downtime.</td>
</tr>
</tbody>
</table>

## Technical and product details

<a href="../products/comparisons/12-operations.md">Open 2 related comparison records</a>

Compare model-specific values, conditions, interfaces, research relationships and source issues. Full source excerpts and original exhibit links remain available underneath.

<a href="../products/references/09-04.md">Simulation, synthetic data and evaluation</a>

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
<td width="280" nowrap><a href="https://www.nist.gov/el/intelligent-systems-division-73500/robotic-grasping-and-manipulation-assembly">NIST</a></td>
<td width="300">Research institute / measurement and evaluation</td>
<td width="520">Performance-measurement research for grasping, manipulation and assembly.</td>
<td width="360">Research demonstration</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://robotwin-platform.github.io/">RoboTwin collaboration</a></td>
<td width="300">Universities, institutes and companies / data and evaluation</td>
<td width="520">Bimanual task generation, domain randomization and unified evaluation resources.</td>
<td width="360">Research demonstration; Code or data public; not reproduced here</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://www.open-rmf.org/">Open-RMF community</a></td>
<td width="300">Open-source ecosystem / multi-robot coordination</td>
<td width="520">Coordination framework for robot fleets and facility interactions.</td>
<td width="360">Code or data public; not reproduced here</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://foxglove.dev/">Foxglove</a></td>
<td width="300">Company / data and observability platform</td>
<td width="520">Tools for robot data recording, management and visualization.</td>
<td width="360">Product or developer documentation public</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://investors.gxo.com/news-releases/news-release-details/gxo-signs-industry-first-multi-year-agreement-agility-robotics">GXO / Agility Robotics</a></td>
<td width="300">Operator and vendor / logistics deployment</td>
<td width="520">The operator disclosed a Digit commercial deployment agreement and logistics setting in 2024.</td>
<td width="360">Operator-disclosed field deployment</td>
</tr>
</tbody>
</table>

Examples illustrate parts of this domain, not every subcategory or a market ranking. Open resources have not been run locally; product pages do not establish availability, integration compatibility or independent performance. [Evidence rules and sources](sources.md).

## Interfaces with the wider system

Read the comparison criteria above as interface contracts: specify the configuration, units, timing, failure behavior and responsible layer. A suitable component does not by itself demonstrate a working integrated robot. Compare the same workload and operating envelope before transferring a result between research and deployment.

## Related research catalog

- [safety evaluation](../deployment/safety-evaluation.md)
- [real-time execution](../deployment/real-time.md)

Source check: 2026-09-08
