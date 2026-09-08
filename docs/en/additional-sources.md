# Additional Source Entries

[Home](../../README.md) | [中文](../zh-CN/additional-sources.md)

The following entries come from archived README snapshots and are not merged into the direction main tables; they are kept for tracking WAM data sources and RL-VLA method leads.

<table width="1580">
<thead>
<tr>
<th width="250">Entry</th>
<th width="320">Source</th>
<th width="240">Direction</th>
<th width="110" nowrap>Date</th>
<th width="200">Resource</th>
<th width="460">Why Track</th>
</tr>
</thead>
<tbody>
<tr>
<td width="250">UnifoLM-WBT Dataset</td>
<td width="320">WAM</td>
<td width="240">WAM training data / robot-centric</td>
<td width="110" nowrap>2026-03</td>
<td width="200"><a href="https://huggingface.co/collections/unitreerobotics/unifolm-wbt-dataset">dataset</a></td>
<td width="460">Robot-centric data source, suitable for later tracking WAM training data coverage.</td>
</tr>
<tr>
<td width="250">DexUMI</td>
<td width="320">WAM</td>
<td width="240">UMI / dexterous manipulation data</td>
<td width="110" nowrap>2025-05</td>
<td width="200"><a href="https://arxiv.org/pdf/2505.21864">paper</a> / <a href="https://dex-umi.github.io/">web</a> / <a href="https://umi-data.github.io/">dataset</a> / <a href="https://github.com/real-stanford/DexUMI">code</a></td>
<td width="460">Hand-interaction data source connecting WAM and dexterous manipulation.</td>
</tr>
<tr>
<td width="250">InternData-A1 / InternVLA-A1</td>
<td width="320">WAM</td>
<td width="240">simulation + VLA data</td>
<td width="110" nowrap>2026-01</td>
<td width="200"><a href="https://arxiv.org/pdf/2601.02456">paper</a> / <a href="https://internrobotics.github.io/interndata-a1.github.io/">web</a> / <a href="https://huggingface.co/datasets/InternRobotics/InternData-A1">dataset</a> / <a href="https://github.com/InternRobotics/InternVLA-A1">code</a></td>
<td width="460">Includes data, models, and code, making it suitable as a joint VLA/WAM entry point.</td>
</tr>
<tr>
<td width="250">ARM</td>
<td width="320">RL-VLA</td>
<td width="240">Offline RL-VLA / real robot</td>
<td width="110" nowrap>2026.4</td>
<td width="200"><a href="https://arxiv.org/pdf/2604.03037">paper</a> / <a href="https://aiming1998.github.io/ARM/">project</a></td>
<td width="460">Real-robot RL-VLA method based on GR00T N1.5.</td>
</tr>
<tr>
<td width="250">LaST-R1</td>
<td width="320">RL-VLA</td>
<td width="240">Online RL-VLA / simulation</td>
<td width="110" nowrap>2026.04</td>
<td width="200"><a href="https://arxiv.org/abs/2604.28192">paper</a></td>
<td width="460">Online RL-VLA training signal, suitable for later adding to the VLA fine-tuning direction.</td>
</tr>
<tr>
<td width="250">POCO</td>
<td width="320">RL-VLA</td>
<td width="240">Offline + Online RL-VLA</td>
<td width="110" nowrap>2026.04</td>
<td width="200"><a href="https://arxiv.org/abs/2604.01860">paper</a> / <a href="https://cccedric.github.io/poco/">project</a></td>
<td width="460">Covers sim and real, and connects π0/Octo with RL optimization.</td>
</tr>
<tr>
<td width="250">FASTER</td>
<td width="320">RL-VLA</td>
<td width="240">Test-time RL-VLA</td>
<td width="110" nowrap>2026.04</td>
<td width="200"><a href="https://arxiv.org/abs/2604.19730">paper</a></td>
<td width="460">Test-time action optimization signal, suitable for tracking execution-time VLA optimization.</td>
</tr>
</tbody>
</table>
