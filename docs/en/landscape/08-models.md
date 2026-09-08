# Robot models, reasoning and planning

[Home](../../../README.md) | [中文](../../zh-CN/landscape/08-models.md) | [Landscape index](README.md)

How are language understanding, world prediction, skills and execution feedback connected?

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
<td width="240" nowrap><a id="08-01"></a>Vision-language-action foundation models</td>
<td width="300">Generate robot actions from multimodal task inputs.</td>
<td width="320">Cross-task and cross-body generalization, action encoding.</td>
<td width="320">Robot-specific adaptation, latency and failure handling.</td>
<td width="340">Unseen tasks, unseen scenes and physical-robot performance.</td>
</tr>
<tr>
<td width="240" nowrap><a id="08-02"></a>World models and action consequence prediction</td>
<td width="300">Predict environmental states after actions.</td>
<td width="320">Joint video, latent-state and action modeling.</td>
<td width="320">Controller interfaces, error detection and compute cost.</td>
<td width="340">Action-conditioned prediction error and decision benefit.</td>
</tr>
<tr>
<td width="240" nowrap><a id="08-03"></a>Task decomposition and skill planning</td>
<td width="300">Decompose requests into constrained executable steps.</td>
<td width="320">Program generation, affordances and task-motion planning.</td>
<td width="320">Skill interfaces, preconditions and orchestration.</td>
<td width="340">Executability, long-task completion and human intervention.</td>
</tr>
<tr>
<td width="240" nowrap><a id="08-04"></a>Long-term memory and personalization</td>
<td width="300">Adapt to users and environments using past experience.</td>
<td width="320">Retrieval, memory updates and forgetting control.</td>
<td width="320">User isolation, data governance and versioning.</td>
<td width="340">Memory utility, update cost and error propagation.</td>
</tr>
<tr>
<td width="240" nowrap><a id="08-05"></a>Failure monitoring and recovery</td>
<td width="300">Detect deviations and reorganize actions.</td>
<td width="320">Anomaly explanations, progress estimation and recovery policies.</td>
<td width="320">Monitoring interfaces, takeover rules and safe exits.</td>
<td width="340">Detection, false alarms and completion after recovery.</td>
</tr>
<tr>
<td width="240" nowrap><a id="08-06"></a>Hierarchical agents and hybrid systems</td>
<td width="300">Connect slow reasoning, fast actions and classical control.</td>
<td width="320">Hierarchical interfaces, uncertainty propagation and joint learning.</td>
<td width="320">Timing budgets, interface contracts and fault isolation.</td>
<td width="340">Full-chain latency, constraint satisfaction and task reliability.</td>
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
<td width="280" nowrap><a href="https://openvla.github.io/">OpenVLA research collaboration</a></td>
<td width="300">Universities and companies / model research</td>
<td width="520">Public vision-language-action model, training code and multi-robot experiments.</td>
<td width="360">Research demonstration; Code or data public; not reproduced here</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://www.pi.website/blog/pi0">Physical Intelligence / pi0</a></td>
<td width="300">Company / foundation-policy research</td>
<td width="520">Company-published generalist robot policy research and task demonstrations.</td>
<td width="360">Research demonstration</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://say-can.github.io/">SayCan research team</a></td>
<td width="300">Industrial research / language and skill planning</td>
<td width="520">Grounds language-proposed actions using skill affordances.</td>
<td width="360">Research demonstration</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://voxposer.github.io/">VoxPoser research team</a></td>
<td width="300">Academic research / spatial planning</td>
<td width="520">Connects language goals with spatial value representations and manipulation planning.</td>
<td width="360">Research demonstration; Code or data public; not reproduced here</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://danijar.com/project/daydreamer/">DayDreamer research team</a></td>
<td width="300">Research collaboration / world models</td>
<td width="520">Studies physical robot learning with learned world models.</td>
<td width="360">Research demonstration; Code or data public; not reproduced here</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://github.com/OpenDriveLab/AgiBot-World">AgiBot World / OpenDriveLab</a></td>
<td width="300">Academic-industrial collaboration / data and foundation policies</td>
<td width="520">Public manipulation data, models and development resources.</td>
<td width="360">Research demonstration; Code or data public; not reproduced here</td>
</tr>
</tbody>
</table>

Examples illustrate parts of this domain, not every subcategory or a market ranking. Open resources have not been run locally; product pages do not establish availability, integration compatibility or independent performance. [Evidence rules and sources](sources.md).

## Interfaces with the wider system

Read the comparison criteria above as interface contracts: specify the configuration, units, timing, failure behavior and responsible layer. A suitable component does not by itself demonstrate a working integrated robot. Compare the same workload and operating envelope before transferring a result between research and deployment.

## Related research catalog

- [generalist VLA](../vla/generalist.md)
- [WAM / World Models](../wam/README.md)
- [Agentic Planning / Reasoning and Planning](../planning/README.md)

Source check: 2026-09-08
