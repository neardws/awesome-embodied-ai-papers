# 机器人模型、推理与规划

[首页](../../../README.zh-CN.md) | [英文](../../en/landscape/08-models.md) | [全景目录](README.md)

怎样连接语言理解、世界预测、技能与执行反馈？

本页区分细类问题、学术研究重点和产业交付重点。这些是编辑归纳的比较维度；下方代表性入口各有明确的能力与证据范围。

## 细类与问题

<table width="1520">
<thead>
<tr>
<th width="240" nowrap>细类</th>
<th width="300">解决的问题</th>
<th width="320">学界研究重点</th>
<th width="320">产业交付重点</th>
<th width="340">比较指标与接口</th>
</tr>
</thead>
<tbody>
<tr>
<td width="240" nowrap><a id="08-01"></a>视觉语言动作基础模型<br><a href="../products/topics/08-01.md">产品细节</a></td>
<td width="300">从多模态任务输入产生机器人动作。</td>
<td width="320">跨任务与跨本体泛化、动作编码。</td>
<td width="320">特定机器人适配、时延和失败处置。</td>
<td width="340">未见任务、未见场景与实机表现。</td>
</tr>
<tr>
<td width="240" nowrap><a id="08-02"></a>世界模型与行动后果预测<br><a href="../products/topics/08-02.md">产品细节</a></td>
<td width="300">预测动作后的环境状态。</td>
<td width="320">视频、潜在状态与动作联合建模。</td>
<td width="320">与控制器连接、误差识别与计算成本。</td>
<td width="340">行动条件预测误差与决策收益。</td>
</tr>
<tr>
<td width="240" nowrap><a id="08-03"></a>任务分解与技能规划<br><a href="../products/topics/08-03.md">产品细节</a></td>
<td width="300">把需求拆成有约束的可执行步骤。</td>
<td width="320">程序生成、可供性与任务运动联合规划。</td>
<td width="320">技能接口、先决条件与执行编排。</td>
<td width="340">可执行率、长任务完成率与人工介入。</td>
</tr>
<tr>
<td width="240" nowrap><a id="08-04"></a>长期记忆与个性化<br><a href="../products/topics/08-04.md">产品细节</a></td>
<td width="300">利用历史经验适应用户与环境。</td>
<td width="320">检索、记忆更新与遗忘控制。</td>
<td width="320">用户隔离、数据治理与版本管理。</td>
<td width="340">记忆有效性、更新代价与错误传播。</td>
</tr>
<tr>
<td width="240" nowrap><a id="08-05"></a>失败监测与恢复<br><a href="../products/topics/08-05.md">产品细节</a></td>
<td width="300">识别偏离目标并重新组织行动。</td>
<td width="320">异常解释、进度估计与恢复策略。</td>
<td width="320">监测接口、接管规则与安全退出。</td>
<td width="340">检出率、误报率与恢复后完成率。</td>
</tr>
<tr>
<td width="240" nowrap><a id="08-06"></a>分层智能体与混合系统<br><a href="../products/topics/08-06.md">产品细节</a></td>
<td width="300">连接慢推理、快速动作与传统控制。</td>
<td width="320">层级接口、不确定性传递与协同学习。</td>
<td width="320">时间预算、接口契约与失效隔离。</td>
<td width="340">全链路时延、约束满足与任务可靠性。</td>
</tr>
</tbody>
</table>

## 技术与产品细节

<a href="../products/comparisons/08-models.md">查看 9 条相关对照记录</a>

继续比较逐型号参数、工况、接口、研究关联和来源问题，并下钻查看完整技术摘录与原始展项链接。

<a href="../products/references/01-06.md">具身方案与未明确形态平台</a> · <a href="../products/references/09-01.md">具身基础模型与行为策略</a> · <a href="../products/references/09-02.md">世界模型与因果推理</a> · <a href="../products/references/09-06.md">企业智能体与AI服务</a>

## 研究、平台与产业代表

<table width="1460">
<thead>
<tr>
<th width="280" nowrap>参与者或项目</th>
<th width="300">角色</th>
<th width="520">有来源的能力</th>
<th width="360">证据状态</th>
</tr>
</thead>
<tbody>
<tr>
<td width="280" nowrap><a href="https://openvla.github.io/">OpenVLA 联合研究团队</a></td>
<td width="300">高校与企业 / 模型研究</td>
<td width="520">公开视觉语言动作模型、训练代码和多机器人实验。</td>
<td width="360">研究展示；代码或数据公开；本项目未复现</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://www.pi.website/blog/pi0">Physical Intelligence / π0</a></td>
<td width="300">企业 / 基础策略研究</td>
<td width="520">企业发布的通用机器人策略研究与任务演示。</td>
<td width="360">研究展示</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://say-can.github.io/">SayCan 研究团队</a></td>
<td width="300">企业研究 / 语言与技能规划</td>
<td width="520">通过技能可供性约束语言模型提出的行动。</td>
<td width="360">研究展示</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://voxposer.github.io/">VoxPoser 研究团队</a></td>
<td width="300">学术研究 / 空间规划</td>
<td width="520">将语言目标组织为空间价值表示与操作规划。</td>
<td width="360">研究展示；代码或数据公开；本项目未复现</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://danijar.com/project/daydreamer/">DayDreamer 研究团队</a></td>
<td width="300">研究协作 / 世界模型</td>
<td width="520">利用学习得到的世界模型开展实体机器人学习。</td>
<td width="360">研究展示；代码或数据公开；本项目未复现</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://github.com/OpenDriveLab/AgiBot-World">AgiBot World / OpenDriveLab</a></td>
<td width="300">学界与产业协作 / 数据和基础策略</td>
<td width="520">公开机器人操作数据、模型和开发资料。</td>
<td width="360">研究展示；代码或数据公开；本项目未复现</td>
</tr>
</tbody>
</table>

示例用于说明本板块中的部分实现，并非每个细类的完整名录或市场排名。公开资源未在本地复现；产品页不证明即时供货、接口互通或独立测试性能。[证据规则与来源](sources.md).

## 与其他环节的接口

将上表指标作为接口约定：写清配置、量纲、时序、失效行为和负责环节。部件能力不自动等于整机能力；把研究结果用于实际部署前，应对齐任务负载和适用工况。

## 关联论文方向

- [通用 VLA](../vla/generalist.md)
- [WAM / 世界模型](../wam/README.md)
- [智能体规划 / 推理规划](../planning/README.md)

来源核对日期：2026-09-08
