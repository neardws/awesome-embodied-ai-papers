# 末端与操作机构

[首页](../../../README.zh-CN.md) | [英文](../../en/landscape/03-end-effectors.md) | [全景目录](README.md)

如何根据物体与工艺选择接触方式，而非只增加手指数量？

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
<td width="240" nowrap><a id="03-01"></a>平行与自适应夹爪</td>
<td width="300">稳定夹持尺寸或形状不同的物体。</td>
<td width="320">抓取生成、柔顺设计与接触建模。</td>
<td width="320">指尖工装、寿命、夹持检测与接口。</td>
<td width="340">开口、夹持力、质量与可替换指尖。</td>
</tr>
<tr>
<td width="240" nowrap><a id="03-02"></a>吸附、气动与柔性末端</td>
<td width="300">处理薄片、易损或不规则物体。</td>
<td width="320">密封接触、材料形变与抓取可行性。</td>
<td width="320">气源、泄漏、污染与耗材更换。</td>
<td width="340">表面适应性、压差、抓取失败检测。</td>
</tr>
<tr>
<td width="240" nowrap><a id="03-03"></a>多指灵巧手</td>
<td width="300">在抓取后继续调整物体姿态。</td>
<td width="320">高维动作学习、手内操作与跨手迁移。</td>
<td width="320">驱动集成、耐久性、触觉布置与供货。</td>
<td width="340">主动与总自由度、指尖力、控制接口。</td>
</tr>
<tr>
<td width="240" nowrap><a id="03-04"></a>绳驱、欠驱动与仿生结构</td>
<td width="300">降低手部重量与驱动数量。</td>
<td width="320">耦合辨识、迟滞补偿与形态计算。</td>
<td width="320">张力调节、传动维护与一致性。</td>
<td width="340">独立可控维度、迟滞、张力与寿命。</td>
</tr>
<tr>
<td width="240" nowrap><a id="03-05"></a>工具快换与工艺末端</td>
<td width="300">在抓取、拧紧、加工等工序间切换。</td>
<td width="320">工具使用推理与接触技能组合。</td>
<td width="320">快换定位、介质连接、工艺认证。</td>
<td width="340">换装时间、连接可靠性与工具标定。</td>
</tr>
<tr>
<td width="240" nowrap><a id="03-06"></a>双手与手臂协同</td>
<td width="300">共同支撑、交接或装配物体。</td>
<td width="320">耦合约束、角色分工与协调策略。</td>
<td width="320">碰撞规避、同步控制与工位布局。</td>
<td width="340">协调成功率、接触力、同步误差。</td>
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
<td width="280" nowrap><a href="https://arxiv.org/abs/2309.06440">LEAP Hand 研究团队</a></td>
<td width="300">学术研究 / 开放硬件</td>
<td width="520">低成本灵巧手设计及论文中的机器人学习实验。</td>
<td width="360">研究展示</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://shadowrobot.com/dexterous-hand-series/">Shadow Robot 灵巧手</a></td>
<td width="300">企业 / 灵巧操作硬件</td>
<td width="520">面向研究开发的多指灵巧手系列。</td>
<td width="360">产品或开发资料公开</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://franka.de/franka-research-3">Franka Research 3</a></td>
<td width="300">企业 / 研究型机械臂</td>
<td width="520">面向研究开发的机械臂系统与控制接入入口。</td>
<td width="360">产品或开发资料公开</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://umi-gripper.github.io/">UMI 研究团队</a></td>
<td width="300">学术研究 / 数据工具</td>
<td width="520">便携示教接口与人类示范到机器人策略的研究。</td>
<td width="360">研究展示；代码或数据公开；本项目未复现</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://www.inspire-robots.com/">因时机器人</a></td>
<td width="300">企业 / 微型执行器与灵巧手</td>
<td width="520">微型伺服电缸、灵巧手系列与产品资料入口。</td>
<td width="360">产品或开发资料公开</td>
</tr>
</tbody>
</table>

示例用于说明本板块中的部分实现，并非每个细类的完整名录或市场排名。公开资源未在本地复现；产品页不证明即时供货、接口互通或独立测试性能。[证据规则与来源](sources.md).

## 与其他环节的接口

将上表指标作为接口约定：写清配置、量纲、时序、失效行为和负责环节。部件能力不自动等于整机能力；把研究结果用于实际部署前，应对齐任务负载和适用工况。

## 关联论文方向

- [灵巧手](../embodiment/dexterous-hand.md)
- [双臂操作](../embodiment/bimanual.md)

来源核对日期：2026-09-08
