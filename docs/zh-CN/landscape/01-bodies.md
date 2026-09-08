# 整机与本体形态

[首页](../../../README.zh-CN.md) | [英文](../../en/landscape/01-bodies.md) | [全景目录](README.md)

什么身体适合什么任务，如何平衡可达空间、运动能力、成本与可靠性？

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
<td width="240" nowrap><a id="01-01"></a>双足与通用人形</td>
<td width="300">在人类尺度空间中移动并操作。</td>
<td width="320">全身协调、平衡与跨形态迁移。</td>
<td width="320">跌倒防护、热管理、维修与稳定交付。</td>
<td width="340">持续负载、工作空间、故障恢复时间。</td>
</tr>
<tr>
<td width="240" nowrap><a id="01-02"></a>轮式双臂与移动操作</td>
<td width="300">把导航、站位和双臂操作连成任务。</td>
<td width="320">基座与手臂联合规划、长时程策略。</td>
<td width="320">底盘定位、升降结构、工位接口。</td>
<td width="340">定位误差、操作成功率、任务周期。</td>
</tr>
<tr>
<td width="240" nowrap><a id="01-03"></a>四足与轮足</td>
<td width="300">在楼梯、坡面和不平地面移动。</td>
<td width="320">地形适应、视觉运动控制。</td>
<td width="320">巡检载荷、防护与续航管理。</td>
<td width="340">地形边界、载荷工况、任务续航。</td>
</tr>
<tr>
<td width="240" nowrap><a id="01-04"></a>固定工业与协作机械臂</td>
<td width="300">在受限工位完成重复或柔性操作。</td>
<td width="320">精细操作、力控与技能迁移。</td>
<td width="320">节拍、重复定位、工装和集成维护。</td>
<td width="340">工作空间、重复精度、力控接口。</td>
</tr>
<tr>
<td width="240" nowrap><a id="01-05"></a>小型开放与教学平台</td>
<td width="300">降低实验、教学和复现门槛。</td>
<td width="320">可复现本体、低成本策略学习。</td>
<td width="320">易装配、备件、文档与开发支持。</td>
<td width="340">物料成本、装配步骤、开放范围。</td>
</tr>
<tr>
<td width="240" nowrap><a id="01-06"></a>专用、柔性与可穿戴本体</td>
<td width="300">适配狭窄、柔性或人体耦合任务。</td>
<td width="320">形态设计、人机动力学与柔性建模。</td>
<td width="320">任务专用结构、佩戴舒适与维护。</td>
<td width="340">适用人群或场景、力学边界、验证条件。</td>
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
<td width="280" nowrap><a href="https://toddlerbot.github.io/">ToddlerBot（斯坦福大学）</a></td>
<td width="300">高校 / 开放本体研究</td>
<td width="520">公开本体设计、装配资料和运动操作研究。</td>
<td width="360">研究展示；代码或数据公开；本项目未复现</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://www.unitree.com/g1/">宇树 G1</a></td>
<td width="300">企业 / 整机平台</td>
<td width="520">人形机体与可选配置的公开产品资料。</td>
<td width="360">产品或开发资料公开</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://franka.de/franka-research-3">Franka Research 3</a></td>
<td width="300">企业 / 研究型机械臂</td>
<td width="520">面向研究开发的机械臂系统与控制接入入口。</td>
<td width="360">产品或开发资料公开</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://www.universal-robots.com/products/">Universal Robots</a></td>
<td width="300">企业 / 协作机械臂</td>
<td width="520">协作机械臂产品与自动化集成入口。</td>
<td width="360">产品或开发资料公开</td>
</tr>
</tbody>
</table>

示例用于说明本板块中的部分实现，并非每个细类的完整名录或市场排名。公开资源未在本地复现；产品页不证明即时供货、接口互通或独立测试性能。[证据规则与来源](sources.md).

## 与其他环节的接口

将上表指标作为接口约定：写清配置、量纲、时序、失效行为和负责环节。部件能力不自动等于整机能力；把研究结果用于实际部署前，应对齐任务负载和适用工况。

## 关联论文方向

- [人形机器人](../embodiment/humanoid.md)
- [双臂操作](../embodiment/bimanual.md)
- [物理可执行导航](../vln/physically-executable.md)

来源核对日期：2026-09-08
