# 运动控制与动作学习

[首页](../../../README.zh-CN.md) | [英文](../../en/landscape/07-control.md) | [全景目录](README.md)

如何把任务目标转成连续、稳定且符合动力学的动作？

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
<td width="240" nowrap><a id="07-01"></a>运动学与轨迹规划</td>
<td width="300">寻找可达、无碰撞的动作路径。</td>
<td width="320">约束求解、采样与优化规划。</td>
<td width="320">机器人模型、碰撞几何与执行时间参数化。</td>
<td width="340">规划成功率、计算时间与碰撞余量。</td>
</tr>
<tr>
<td width="240" nowrap><a id="07-02"></a>模型预测与最优控制</td>
<td width="300">在动力学约束下滚动调整动作。</td>
<td width="320">模型误差、约束优化与稳定性。</td>
<td width="320">实时求解、状态估计与故障降级。</td>
<td width="340">求解最坏时延、跟踪误差与约束违反。</td>
</tr>
<tr>
<td width="240" nowrap><a id="07-03"></a>力控、阻抗与接触控制</td>
<td width="300">在接触中控制力与柔顺性。</td>
<td width="320">接触切换、未知刚度与安全探索。</td>
<td width="320">工艺整定、传感标定与过载保护。</td>
<td width="340">接触力误差、超调与损伤率。</td>
</tr>
<tr>
<td width="240" nowrap><a id="07-04"></a>腿式与全身协调控制</td>
<td width="300">协调平衡、行走、手臂与接触点。</td>
<td width="320">运动模仿、落脚规划与多接触优化。</td>
<td width="320">本体约束、热负载、跌倒恢复。</td>
<td width="340">地形通过率、能耗与恢复能力。</td>
</tr>
<tr>
<td width="240" nowrap><a id="07-05"></a>模仿与扩散、流动作策略</td>
<td width="300">从示范学习多模态动作分布。</td>
<td width="320">动作表示、时间建模与误差累积。</td>
<td width="320">采集成本、推理时延与控制频率匹配。</td>
<td width="340">成功率、动作平滑性与端到端时延。</td>
</tr>
<tr>
<td width="240" nowrap><a id="07-06"></a>强化学习与在线适应</td>
<td width="300">通过反馈改进策略并适应变化。</td>
<td width="320">奖励设计、样本效率与安全学习。</td>
<td width="320">真实试错成本、接管与回滚。</td>
<td width="340">新增交互量、风险暴露与持续性能。</td>
</tr>
</tbody>
</table>

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
<td width="280" nowrap><a href="https://moveit.ai/">MoveIt / PickNik</a></td>
<td width="300">开源社区与企业 / 操作软件</td>
<td width="520">运动规划、运动学、感知和执行接口；另有商业支持入口。</td>
<td width="360">代码或数据公开；本项目未复现；产品或开发资料公开</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://github.com/ros-controls/ros2_control">ros2_control 社区</a></td>
<td width="300">开源社区 / 控制框架</td>
<td width="520">控制器与机器人硬件接口的开源框架。</td>
<td width="360">代码或数据公开；本项目未复现</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://diffusion-policy.cs.columbia.edu/">Diffusion Policy 研究团队</a></td>
<td width="300">学界与产业研究 / 动作学习</td>
<td width="520">以条件扩散生成视觉运动动作序列。</td>
<td width="360">研究展示；代码或数据公开；本项目未复现</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://franka.de/franka-research-3">Franka Research 3</a></td>
<td width="300">企业 / 研究型机械臂</td>
<td width="520">面向研究开发的机械臂系统与控制接入入口。</td>
<td width="360">产品或开发资料公开</td>
</tr>
</tbody>
</table>

示例用于说明本板块中的部分实现，并非每个细类的完整名录或市场排名。公开资源未在本地复现；产品页不证明即时供货、接口互通或独立测试性能。[证据规则与来源](sources.md).

## 与其他环节的接口

将上表指标作为接口约定：写清配置、量纲、时序、失效行为和负责环节。部件能力不自动等于整机能力；把研究结果用于实际部署前，应对齐任务负载和适用工况。

## 关联论文方向

- [扩散与流策略](../vla/diffusion-flow.md)
- [人形机器人](../embodiment/humanoid.md)

来源核对日期：2026-09-08
