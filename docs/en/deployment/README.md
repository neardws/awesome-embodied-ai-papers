# Efficiency / Evaluation / Data

[Home](../../../README.md) | [中文](../../zh-CN/deployment/README.md)

This direction determines whether systems can actually be deployed: on-device inference, caching/quantization/action tokenization, real-time execution, sim2real, benchmarks, and safety evaluation are all necessary conditions.

Subdirections: quantization/cache/tokenization, real-time execution, benchmark/dataset, sim2real, and safety evaluation.

Total: 105 papers.

<table width="1090">
<thead>
<tr>
<th width="280">Subdirection</th>
<th width="90" nowrap>Entries</th>
<th width="720">Focus</th>
</tr>
</thead>
<tbody>
<tr>
<td width="280">quantization/cache/tokenization</td>
<td width="90" nowrap>22</td>
<td width="720">Focus: on-device deployment, cache reuse, and action token efficiency.</td>
</tr>
<tr>
<td width="280">real-time execution</td>
<td width="90" nowrap>6</td>
<td width="720">Focus: low-latency execution and real-time policy inference.</td>
</tr>
<tr>
<td width="280">benchmark/dataset</td>
<td width="90" nowrap>44</td>
<td width="720">Focus: data coverage, task design, and evaluation credibility.</td>
</tr>
<tr>
<td width="280">sim2real</td>
<td width="90" nowrap>20</td>
<td width="720">Focus: sim-to-real transfer and the real-world deployment gap.</td>
</tr>
<tr>
<td width="280">safety evaluation</td>
<td width="90" nowrap>13</td>
<td width="720">Focus: robustness, safety, and deployment risk evaluation.</td>
</tr>
</tbody>
</table>


# Subdirection files

<table width="430">
<thead>
<tr>
<th width="340">Topic</th>
<th width="90" nowrap>Entries</th>
</tr>
</thead>
<tbody>
<tr>
<td width="340"><a href="quantization-cache-tokenization.md">quantization/cache/tokenization</a></td>
<td width="90" nowrap>22</td>
</tr>
<tr>
<td width="340"><a href="real-time.md">real-time execution</a></td>
<td width="90" nowrap>6</td>
</tr>
<tr>
<td width="340"><a href="benchmarks-datasets.md">benchmark/dataset</a></td>
<td width="90" nowrap>44</td>
</tr>
<tr>
<td width="340"><a href="sim2real.md">sim2real</a></td>
<td width="90" nowrap>20</td>
</tr>
<tr>
<td width="340"><a href="safety-evaluation.md">safety evaluation</a></td>
<td width="90" nowrap>13</td>
</tr>
</tbody>
</table>

<!-- landscape-links:start -->

## Research and industrial context

Explore the hardware, software and delivery questions connected with this research track.

<table width="1060">
<thead>
<tr>
<th width="300" nowrap>Landscape domain</th>
<th width="760">System question</th>
</tr>
</thead>
<tbody>
<tr>
<td width="300" nowrap><a href="../landscape/05-compute.md">Compute, communication and energy</a></td>
<td width="760">How can high-compute inference coexist with deterministic control on one robot?</td>
</tr>
<tr>
<td width="300" nowrap><a href="../landscape/09-systems.md">System software and integration platforms</a></td>
<td width="760">How are heterogeneous devices, models and skills composed into a developable and debuggable system?</td>
</tr>
<tr>
<td width="300" nowrap><a href="../landscape/10-data.md">Data collection and governance</a></td>
<td width="760">How are demonstrations and operational experience turned into reusable, traceable data assets?</td>
</tr>
<tr>
<td width="300" nowrap><a href="../landscape/11-simulation.md">Simulation and training infrastructure</a></td>
<td width="760">How can controlled experiments accelerate development while exposing what simulation cannot replace?</td>
</tr>
<tr>
<td width="300" nowrap><a href="../landscape/12-operations.md">Evaluation, safety, deployment and operations</a></td>
<td width="760">How is single-task performance turned into measurable, recoverable and sustained system capability?</td>
</tr>
<tr>
<td width="300" nowrap><a href="../landscape/13-manufacturing.md">Manufacturing, integration and delivery</a></td>
<td width="760">How can prototypes become manufacturable, serviceable deliverables with explicit configurations?</td>
</tr>
<tr>
<td width="300" nowrap><a href="../landscape/14-applications.md">Applications and solutions</a></td>
<td width="760">Which workflows do robots serve, and how is value measured through real tasks?</td>
</tr>
</tbody>
</table>

<!-- landscape-links:end -->
