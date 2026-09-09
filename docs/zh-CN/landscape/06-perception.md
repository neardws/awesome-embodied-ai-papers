# 感知、定位与空间表示

[首页](../../../README.zh-CN.md) | [英文](../../en/landscape/06-perception.md) | [全景目录](README.md)

怎样把传感数据转换为可供导航、规划和操作使用的状态？

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
<td width="240" nowrap><a id="06-01"></a>目标识别与开放词汇感知<br><a href="../products/topics/06-01.md">产品细节</a></td>
<td width="300">找到任务相关物体及其属性。</td>
<td width="320">开放类别、指代表达与分布外识别。</td>
<td width="320">误检控制、现场数据与推理成本。</td>
<td width="340">任务相关召回、误检与时延。</td>
</tr>
<tr>
<td width="240" nowrap><a id="06-02"></a>位姿、几何与可供性<br><a href="../products/topics/06-02.md">产品细节</a></td>
<td width="300">定位可抓取、可接触和可操作部位。</td>
<td width="320">几何语义融合、姿态估计与接触先验。</td>
<td width="320">标定、遮挡处理与末端对齐。</td>
<td width="340">位姿误差、可达性与下游任务成功。</td>
</tr>
<tr>
<td width="240" nowrap><a id="06-03"></a>定位建图与状态估计<br><a href="../products/topics/06-03.md">产品细节</a></td>
<td width="300">维护机器人相对环境的位置。</td>
<td width="320">多模态融合、回环和动态场景估计。</td>
<td width="320">初始化、重定位、地图维护与退化处理。</td>
<td width="340">漂移、重定位时间与可用率。</td>
</tr>
<tr>
<td width="240" nowrap><a id="06-04"></a>三维重建与场景表征<br><a href="../products/topics/06-04.md">产品细节</a></td>
<td width="300">构建可查询的空间模型。</td>
<td width="320">神经场、高斯表示与几何一致性。</td>
<td width="320">建图速度、存储、更新与工具接口。</td>
<td width="340">几何精度、更新开销与查询时延。</td>
</tr>
<tr>
<td width="240" nowrap><a id="06-05"></a>语义地图与空间记忆<br><a href="../products/topics/06-05.md">产品细节</a></td>
<td width="300">保留跨时刻、跨任务的场景知识。</td>
<td width="320">拓扑图、检索记忆与长期一致性。</td>
<td width="320">地图版本、对象变化与运行维护。</td>
<td width="340">记忆一致性、检索效果与任务增益。</td>
</tr>
<tr>
<td width="240" nowrap><a id="06-06"></a>主动感知与不确定性<br><a href="../products/topics/06-06.md">产品细节</a></td>
<td width="300">决定下一步看哪里及何时重新观测。</td>
<td width="320">信息增益、探索与不确定性校准。</td>
<td width="320">传感预算、安全运动与异常触发。</td>
<td width="340">观测成本、校准误差与失败减少量。</td>
</tr>
</tbody>
</table>

## 技术与产品细节

<a href="../products/comparisons/06-perception.md">查看 1 条相关对照记录</a>

继续比较逐型号参数、工况、接口、研究关联和来源问题，并下钻查看完整技术摘录与原始展项链接。

<a href="../products/references/04-03.md">移动底盘与自主导航载体</a> · <a href="../products/references/07-07.md">图像传感与视觉识别</a> · <a href="../products/references/07-08.md">SLAM与空间感知模组</a>

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
<td width="280" nowrap><a href="https://docs.nav2.org/rolling/">Nav2 社区</a></td>
<td width="300">开源社区 / 自主导航</td>
<td width="520">导航软件框架及其规划、控制和行为组织接口。</td>
<td width="360">代码或数据公开；本项目未复现</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://robotic-view-transformer.github.io/">RVT 研究团队</a></td>
<td width="300">研究协作 / 三维操作</td>
<td width="520">面向三维操作的多视角表示与策略研究。</td>
<td width="360">研究展示；代码或数据公开；本项目未复现</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://voxposer.github.io/">VoxPoser 研究团队</a></td>
<td width="300">学术研究 / 空间规划</td>
<td width="520">将语言目标组织为空间价值表示与操作规划。</td>
<td width="360">研究展示；代码或数据公开；本项目未复现</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://www.nvidia.com/en-us/industries/robotics/">NVIDIA 机器人平台</a></td>
<td width="300">企业 / 计算与开发平台</td>
<td width="520">训练、仿真、机器人软件加速和端侧推理的平台分工。</td>
<td width="360">产品或开发资料公开</td>
</tr>
</tbody>
</table>

示例用于说明本板块中的部分实现，并非每个细类的完整名录或市场排名。公开资源未在本地复现；产品页不证明即时供货、接口互通或独立测试性能。[证据规则与来源](sources.md).

## 与其他环节的接口

将上表指标作为接口约定：写清配置、量纲、时序、失效行为和负责环节。部件能力不自动等于整机能力；把研究结果用于实际部署前，应对齐任务负载和适用工况。

## 关联论文方向

- [地图与记忆](../vln/map-memory.md)
- [三维空间落地](../vla/3d-grounding.md)

来源核对日期：2026-09-08
