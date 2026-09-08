# 源仓库补充条目

[首页](../../README.zh-CN.md) | [英文](../en/additional-sources.md)

以下条目来自本次保存的 README 快照，不并入方向主表；它们用于跟踪 WAM 数据源和 RL-VLA 方法线索。

<table width="1580">
<thead>
<tr>
<th width="250">条目</th>
<th width="320">来源</th>
<th width="240">方向</th>
<th width="110" nowrap>时间</th>
<th width="200">资源</th>
<th width="460">为什么跟踪</th>
</tr>
</thead>
<tbody>
<tr>
<td width="250">UnifoLM-WBT Dataset</td>
<td width="320">WAM</td>
<td width="240">WAM 训练数据 / 以机器人为中心</td>
<td width="110" nowrap>2026-03</td>
<td width="200"><a href="https://huggingface.co/collections/unitreerobotics/unifolm-wbt-dataset">数据集</a></td>
<td width="460">机器人中心数据源，适合后续看 WAM 训练数据覆盖。</td>
</tr>
<tr>
<td width="250">DexUMI</td>
<td width="320">WAM</td>
<td width="240">UMI / 灵巧操作数据</td>
<td width="110" nowrap>2025-05</td>
<td width="200"><a href="https://arxiv.org/pdf/2505.21864">论文</a> / <a href="https://dex-umi.github.io/">网页</a> / <a href="https://umi-data.github.io/">数据集</a> / <a href="https://github.com/real-stanford/DexUMI">代码</a></td>
<td width="460">手部交互数据源，连接 WAM 与灵巧操作。</td>
</tr>
<tr>
<td width="250">InternData-A1 / InternVLA-A1</td>
<td width="320">WAM</td>
<td width="240">仿真 + VLA 数据</td>
<td width="110" nowrap>2026-01</td>
<td width="200"><a href="https://arxiv.org/pdf/2601.02456">论文</a> / <a href="https://internrobotics.github.io/interndata-a1.github.io/">网页</a> / <a href="https://huggingface.co/datasets/InternRobotics/InternData-A1">数据集</a> / <a href="https://github.com/InternRobotics/InternVLA-A1">代码</a></td>
<td width="460">同时有数据、模型和代码，适合作为 VLA/WAM 联合入口。</td>
</tr>
<tr>
<td width="250">ARM</td>
<td width="320">RL-VLA</td>
<td width="240">离线 RL-VLA / 真实机器人</td>
<td width="110" nowrap>2026.4</td>
<td width="200"><a href="https://arxiv.org/pdf/2604.03037">论文</a> / <a href="https://aiming1998.github.io/ARM/">项目</a></td>
<td width="460">基于 GR00T N1.5 的真实机器人 RL-VLA 方法。</td>
</tr>
<tr>
<td width="250">LaST-R1</td>
<td width="320">RL-VLA</td>
<td width="240">在线 RL-VLA / 仿真</td>
<td width="110" nowrap>2026.04</td>
<td width="200"><a href="https://arxiv.org/abs/2604.28192">论文</a></td>
<td width="460">RL-VLA 在线训练线索，适合后续补到 VLA 微调方向。</td>
</tr>
<tr>
<td width="250">POCO</td>
<td width="320">RL-VLA</td>
<td width="240">离线 + 在线 RL-VLA</td>
<td width="110" nowrap>2026.04</td>
<td width="200"><a href="https://arxiv.org/abs/2604.01860">论文</a> / <a href="https://cccedric.github.io/poco/">项目</a></td>
<td width="460">覆盖仿真和实机，且连接 π0/Octo 与强化学习优化。</td>
</tr>
<tr>
<td width="250">FASTER</td>
<td width="320">RL-VLA</td>
<td width="240">测试时 RL-VLA</td>
<td width="110" nowrap>2026.04</td>
<td width="200"><a href="https://arxiv.org/abs/2604.19730">论文</a></td>
<td width="460">测试时动作优化线索，适合跟踪 VLA 执行期优化。</td>
</tr>
</tbody>
</table>
