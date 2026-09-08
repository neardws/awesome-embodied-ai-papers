# 低成本与端侧导航

[首页](../../../README.zh-CN.md) | [英文](../../en/vln/on-device.md) | [方向目录](README.md)

共 3 篇。

<table width="3050">
<thead>
<tr>
<th width="120" nowrap>会议/年份</th>
<th width="320">论文/方法</th>
<th width="420">摘要</th>
<th width="220">任务类型</th>
<th width="240">环境</th>
<th width="260">地图/记忆</th>
<th width="300">训练/反馈</th>
<th width="240">仿真/实机/基准</th>
<th width="360">论文任务/目标</th>
<th width="110" nowrap>论文</th>
<th width="110" nowrap>项目</th>
<th width="110" nowrap>代码</th>
<th width="240">数据/基准</th>
</tr>
</thead>
<tbody>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2505.11886">Aux-Think: Exploring Reasoning Strategies for Data-Efficient Vision-Language Navigation</a></td>
<td width="420">Aux-Think 系统比较 No/Pre/Post-Think 推理策略，发现 VLN 中推理可能坍缩并构建 R2R-CoT-320k。</td>
<td width="220">数据高效视觉语言导航推理</td>
<td width="240">移动机器人/移动操作</td>
<td width="260">-</td>
<td width="300">推理策略评测</td>
<td width="240">-</td>
<td width="360">研究数据高效 VLN 中何种推理策略真正有用。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2505.11886">论文</a></td>
<td width="110" nowrap><a href="https://horizonrobotics.github.io/robot_lab/aux-think/">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">R2R-CoT-320k</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://openreview.net/pdf?id=5gptKWnVPF">Harnessing Input-Adaptive Inference for Efficient VLN</a></td>
<td width="420">该文在视角选择、提前退出阈值和历史视图缓存三个层面做输入自适应推理，使 VLN 计算量降低 2 倍以上。</td>
<td width="220">端侧/低成本</td>
<td width="240">移动机器人/导航环境</td>
<td width="260">-</td>
<td width="300">高效导航</td>
<td width="240">7 个视觉语言导航基准</td>
<td width="360">在保持性能的同时降低历史感知 Transformer 视觉语言导航智能体的推理成本。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2508.09262">论文</a></td>
<td width="110" nowrap><a href="https://true-lab.ai/efficient_vln/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/secure-ai-systems-group/adaptive-vision-and-language-navigation">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2503.24065">COSMO: Combination of Selective Memorization for Low-cost Vision-and-Language Navigation</a></td>
<td width="420">COSMO 结合状态空间模块和 Transformer，并设计 RSS 与跨模态选择记忆以降低 VLN 计算成本。</td>
<td width="220">端侧/低成本</td>
<td width="240">移动机器人/移动操作</td>
<td width="260">-</td>
<td width="300">选择性状态空间记忆 + Transformer</td>
<td width="240">-</td>
<td width="360">低成本 VLN 模型结构</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2503.24065">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
</tbody>
</table>
