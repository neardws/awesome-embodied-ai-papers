# VLA / 操作策略

[首页](../../../README.zh-CN.md) | [英文](../../en/vla/README.md)

VLA 是机械臂和移动操作的主战场，但它不只是“大模型接动作头”。调研论文集中在动作表示、扩散与流策略、三维空间落地、在线/强化学习微调和安全鲁棒性上。

子方向：通用 VLA、动作表示、扩散与流策略、三维空间落地、在线/强化学习微调、安全鲁棒性。

共 251 篇。

<table width="1090">
<thead>
<tr>
<th width="280">子方向</th>
<th width="90" nowrap>条目数</th>
<th width="720">观察重点</th>
</tr>
</thead>
<tbody>
<tr>
<td width="280">通用 VLA</td>
<td width="90" nowrap>80</td>
<td width="720">看跨任务泛化、真实机器人验证和通用操作能力。</td>
</tr>
<tr>
<td width="280">动作表示</td>
<td width="90" nowrap>30</td>
<td width="720">看动作词元、潜在动作、分块和动作空间设计。</td>
</tr>
<tr>
<td width="280">扩散与流策略</td>
<td width="90" nowrap>72</td>
<td width="720">看连续动作生成、稳定控制和执行平滑性。</td>
</tr>
<tr>
<td width="280">三维空间落地</td>
<td width="90" nowrap>41</td>
<td width="720">看点云、几何、可供性与操作定位。</td>
</tr>
<tr>
<td width="280">在线/强化学习微调</td>
<td width="90" nowrap>21</td>
<td width="720">看在线强化、人在回路和测试时适配。</td>
</tr>
<tr>
<td width="280">安全鲁棒性</td>
<td width="90" nowrap>7</td>
<td width="720">看攻击鲁棒、安全对齐和风险暴露。</td>
</tr>
</tbody>
</table>


# 子方向文件

<table width="430">
<thead>
<tr>
<th width="340">主题</th>
<th width="90" nowrap>条目数</th>
</tr>
</thead>
<tbody>
<tr>
<td width="340"><a href="generalist.md">通用 VLA</a></td>
<td width="90" nowrap>80</td>
</tr>
<tr>
<td width="340"><a href="action-representation.md">动作表示</a></td>
<td width="90" nowrap>30</td>
</tr>
<tr>
<td width="340"><a href="diffusion-flow.md">扩散与流策略</a></td>
<td width="90" nowrap>72</td>
</tr>
<tr>
<td width="340"><a href="3d-grounding.md">三维空间落地</a></td>
<td width="90" nowrap>41</td>
</tr>
<tr>
<td width="340"><a href="online-rl.md">在线与强化学习微调</a></td>
<td width="90" nowrap>21</td>
</tr>
<tr>
<td width="340"><a href="safety-robustness.md">安全性与鲁棒性</a></td>
<td width="90" nowrap>7</td>
</tr>
</tbody>
</table>

<!-- landscape-links:start -->

## 学术与产业关联

从以下板块继续查看与本研究方向相关的硬件、软件和交付问题。

<table width="1060">
<thead>
<tr>
<th width="300" nowrap>全景板块</th>
<th width="760">系统问题</th>
</tr>
</thead>
<tbody>
<tr>
<td width="300" nowrap><a href="../landscape/06-perception.md">感知、定位与空间表示</a></td>
<td width="760">怎样把传感数据转换为可供导航、规划和操作使用的状态？</td>
</tr>
<tr>
<td width="300" nowrap><a href="../landscape/07-control.md">运动控制与动作学习</a></td>
<td width="760">如何把任务目标转成连续、稳定且符合动力学的动作？</td>
</tr>
<tr>
<td width="300" nowrap><a href="../landscape/08-models.md">机器人模型、推理与规划</a></td>
<td width="760">怎样连接语言理解、世界预测、技能与执行反馈？</td>
</tr>
<tr>
<td width="300" nowrap><a href="../landscape/10-data.md">数据采集与治理</a></td>
<td width="760">怎样把分散的演示与运行经验变成可复用、可追溯的数据资产？</td>
</tr>
</tbody>
</table>

<!-- landscape-links:end -->
