# 系统软件与集成平台

[首页](../../../README.zh-CN.md) | [英文](../../en/landscape/09-systems.md) | [全景目录](README.md)

如何把异构设备、模型和技能组成可开发、可调试的机器人系统？

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
<td width="240" nowrap><a id="09-01"></a>操作系统与通信中间件</td>
<td width="300">组织进程、消息与分布式组件。</td>
<td width="320">实时通信、模块化与系统架构。</td>
<td width="320">版本支持、部署配置与兼容性。</td>
<td width="340">消息时延、服务生命周期与可诊断性。</td>
</tr>
<tr>
<td width="240" nowrap><a id="09-02"></a>驱动、硬件抽象与控制接口</td>
<td width="300">统一传感读取与执行器命令。</td>
<td width="320">接口抽象、控制切换与仿真实机一致性。</td>
<td width="320">驱动维护、校准、故障码与设备支持。</td>
<td width="340">接口覆盖、状态语义与时序一致性。</td>
</tr>
<tr>
<td width="240" nowrap><a id="09-03"></a>导航与操作软件栈</td>
<td width="300">组合感知、规划与控制模块。</td>
<td width="320">可插拔算法与端到端系统比较。</td>
<td width="320">场景整定、机器人适配与稳定版本。</td>
<td width="340">集成成本、任务完成率与异常处理。</td>
</tr>
<tr>
<td width="240" nowrap><a id="09-04"></a>技能库、行为树与工作流</td>
<td width="300">表达任务顺序、并发与恢复。</td>
<td width="320">技能组合、形式约束与层级决策。</td>
<td width="320">可视化编排、接口版本与操作权限。</td>
<td width="340">技能复用率、失败定位与恢复路径。</td>
</tr>
<tr>
<td width="240" nowrap><a id="09-05"></a>开发、调试与可观测性</td>
<td width="300">解释系统运行中的数据与故障。</td>
<td width="320">因果调试、日志压缩与可解释执行。</td>
<td width="320">回放、可视化、报警与远程诊断。</td>
<td width="340">复现故障时间、日志完整性与排障成本。</td>
</tr>
<tr>
<td width="240" nowrap><a id="09-06"></a>设施对接与多机协调</td>
<td width="300">让机器人与电梯、门禁、机队协同。</td>
<td width="320">多智能体调度、冲突消解与协作。</td>
<td width="320">设施协议、任务系统、交通与权限。</td>
<td width="340">拥堵、吞吐、资源等待与异常恢复。</td>
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
<td width="280" nowrap><a href="https://github.com/ros2/ros2">ROS 2 社区</a></td>
<td width="300">开源社区 / 中间件</td>
<td width="520">机器人软件生态的主仓库与组件入口。</td>
<td width="360">代码或数据公开；本项目未复现</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://github.com/ros-controls/ros2_control">ros2_control 社区</a></td>
<td width="300">开源社区 / 控制框架</td>
<td width="520">控制器与机器人硬件接口的开源框架。</td>
<td width="360">代码或数据公开；本项目未复现</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://moveit.ai/">MoveIt / PickNik</a></td>
<td width="300">开源社区与企业 / 操作软件</td>
<td width="520">运动规划、运动学、感知和执行接口；另有商业支持入口。</td>
<td width="360">代码或数据公开；本项目未复现；产品或开发资料公开</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://docs.nav2.org/rolling/">Nav2 社区</a></td>
<td width="300">开源社区 / 自主导航</td>
<td width="520">导航软件框架及其规划、控制和行为组织接口。</td>
<td width="360">代码或数据公开；本项目未复现</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://www.open-rmf.org/">Open-RMF 社区</a></td>
<td width="300">开源生态 / 多机协调</td>
<td width="520">机器人机队与设施交互的协调框架。</td>
<td width="360">代码或数据公开；本项目未复现</td>
</tr>
</tbody>
</table>

示例用于说明本板块中的部分实现，并非每个细类的完整名录或市场排名。公开资源未在本地复现；产品页不证明即时供货、接口互通或独立测试性能。[证据规则与来源](sources.md).

## 与其他环节的接口

将上表指标作为接口约定：写清配置、量纲、时序、失效行为和负责环节。部件能力不自动等于整机能力；把研究结果用于实际部署前，应对齐任务负载和适用工况。

## 关联论文方向

- [约束与可供性规划](../planning/constraint-affordance.md)
- [实时执行](../deployment/real-time.md)

来源核对日期：2026-09-08
