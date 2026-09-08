# 传感与交互硬件

[首页](../../../README.zh-CN.md) | [英文](../../en/landscape/04-sensing.md) | [全景目录](README.md)

如何测量外部环境、身体状态与接触过程，并把多种信号对齐？

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
<td width="240" nowrap><a id="04-01"></a>图像、深度与三维视觉</td>
<td width="300">获取物体外观、形状与距离。</td>
<td width="320">遮挡、透明反光与主动视觉。</td>
<td width="320">标定、光照适应、接口与带宽。</td>
<td width="340">深度误差、视场、帧率与同步。</td>
</tr>
<tr>
<td width="240" nowrap><a id="04-02"></a>激光、雷达与测距</td>
<td width="300">支持远距离或复杂环境测量。</td>
<td width="320">多传感融合、动态目标与稀疏感知。</td>
<td width="320">安装遮挡、环境防护与成本。</td>
<td width="340">量程、角分辨率、回波条件与时延。</td>
</tr>
<tr>
<td width="240" nowrap><a id="04-03"></a>惯性、编码器与本体反馈</td>
<td width="300">估计机体姿态、关节位置和运动。</td>
<td width="320">漂移补偿、状态估计与传感容错。</td>
<td width="320">温漂、线缆、安装和时间同步。</td>
<td width="340">噪声、漂移、分辨率与更新率。</td>
</tr>
<tr>
<td width="240" nowrap><a id="04-04"></a>六维力与关节力矩</td>
<td width="300">判断接触载荷及外力。</td>
<td width="320">力估计、柔顺控制与碰撞识别。</td>
<td width="320">过载防护、标定与工业通信。</td>
<td width="340">量程、串扰、迟滞、采样率。</td>
</tr>
<tr>
<td width="240" nowrap><a id="04-05"></a>触觉阵列与电子皮肤</td>
<td width="300">感知接触分布、滑移和局部几何。</td>
<td width="320">跨传感器表示与视觉触觉融合。</td>
<td width="320">耐磨、表皮更换、布线与批次标定。</td>
<td width="340">触点覆盖、采样同步、滑移检测与耐久。</td>
</tr>
<tr>
<td width="240" nowrap><a id="04-06"></a>动作捕捉、语音与人机交互</td>
<td width="300">把人的动作和意图接入机器人。</td>
<td width="320">意图理解、重定向与多模态交互。</td>
<td width="320">佩戴舒适、遮挡、延迟与操作负担。</td>
<td width="340">跟踪误差、端到端时延与交互成功率。</td>
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
<td width="280" nowrap><a href="https://www.gelsight.com/product/digit-tactile-sensor/">GelSight DIGIT</a></td>
<td width="300">企业 / 触觉器件</td>
<td width="520">用于机器人操作研究的触觉传感器产品页。</td>
<td width="360">产品或开发资料公开</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://www.ati-ia.com/products/ft/sensors.aspx">ATI 六维力传感器</a></td>
<td width="300">企业 / 力传感器</td>
<td width="520">力与力矩测量系统及其工业、研究用途。</td>
<td width="360">产品或开发资料公开</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://www.unitree.com/g1/">宇树 G1</a></td>
<td width="300">企业 / 整机平台</td>
<td width="520">人形机体与可选配置的公开产品资料。</td>
<td width="360">产品或开发资料公开</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://umi-gripper.github.io/">UMI 研究团队</a></td>
<td width="300">学术研究 / 数据工具</td>
<td width="520">便携示教接口与人类示范到机器人策略的研究。</td>
<td width="360">研究展示；代码或数据公开；本项目未复现</td>
</tr>
</tbody>
</table>

示例用于说明本板块中的部分实现，并非每个细类的完整名录或市场排名。公开资源未在本地复现；产品页不证明即时供货、接口互通或独立测试性能。[证据规则与来源](sources.md).

## 与其他环节的接口

将上表指标作为接口约定：写清配置、量纲、时序、失效行为和负责环节。部件能力不自动等于整机能力；把研究结果用于实际部署前，应对齐任务负载和适用工况。

## 关联论文方向

- [触觉与接触丰富操作](../embodiment/tactile-contact.md)
- [地图与记忆](../vln/map-memory.md)

来源核对日期：2026-09-08
