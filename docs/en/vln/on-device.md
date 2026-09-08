# Low-cost / On-device Navigation

[Home](../../../README.md) | [中文](../../zh-CN/vln/on-device.md) | [Direction index](README.md)

Total: 3 papers.

<table width="3050">
<thead>
<tr>
<th width="120" nowrap>Venue/Year</th>
<th width="320">Paper/Method</th>
<th width="420">Abstract</th>
<th width="220">Task Type</th>
<th width="240">Environment</th>
<th width="260">Map/Memory</th>
<th width="300">Training/Feedback</th>
<th width="240">Sim/Real/Benchmark</th>
<th width="360">Paper Task/Goal</th>
<th width="110" nowrap>Paper</th>
<th width="110" nowrap>Project</th>
<th width="110" nowrap>Code</th>
<th width="240">Data/Bench</th>
</tr>
</thead>
<tbody>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2505.11886">Aux-Think: Exploring Reasoning Strategies for Data-Efficient Vision-Language Navigation</a></td>
<td width="420">Aux-Think systematically compares No/Pre/Post-Think reasoning strategies, finds that reasoning in VLN may collapse, and builds R2R-CoT-320k.</td>
<td width="220">data-efficient VLN reasoning</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">-</td>
<td width="300">reasoning strategy evaluation</td>
<td width="240">-</td>
<td width="360">Studies which reasoning strategies are actually useful in data-efficient VLN.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2505.11886">paper</a></td>
<td width="110" nowrap><a href="https://horizonrobotics.github.io/robot_lab/aux-think/">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">R2R-CoT-320k</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://openreview.net/pdf?id=5gptKWnVPF">Harnessing Input-Adaptive Inference for Efficient VLN</a></td>
<td width="420">This paper applies input-adaptive reasoning at three levels: viewpoint selection, early-exit thresholds, and history-view caching, reducing VLN computation by more than 2x.</td>
<td width="220">On-device/Low-cost</td>
<td width="240">mobile robot/navigation environment</td>
<td width="260">-</td>
<td width="300">efficient navigation</td>
<td width="240">7 VLN benchmarks</td>
<td width="360">Reduces the inference cost of history-aware transformer VLN agents while maintaining performance.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2508.09262">paper</a></td>
<td width="110" nowrap><a href="https://true-lab.ai/efficient_vln/">project</a></td>
<td width="110" nowrap><a href="https://github.com/secure-ai-systems-group/adaptive-vision-and-language-navigation">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2503.24065">COSMO: Combination of Selective Memorization for Low-cost Vision-and-Language Navigation</a></td>
<td width="420">COSMO combines state-space modules and transformer, and designs RSS and cross-modal selective memory to reduce VLN computational cost.</td>
<td width="220">On-device/Low-cost</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">-</td>
<td width="300">selective state-space memorization + transformer</td>
<td width="240">-</td>
<td width="360">Low-cost VLN model architecture</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2503.24065">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
</tbody>
</table>
