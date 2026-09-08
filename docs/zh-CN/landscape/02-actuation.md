# 执行与精密传动

[首页](../../../README.zh-CN.md) | [英文](../../en/landscape/02-actuation.md) | [全景目录](README.md)

怎样把电能变成可控的力与运动，并在冲击、温升和磨损下保持性能？

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
<td width="240" nowrap><a id="02-01"></a>电机与直接驱动</td>
<td width="300">提供可调的力矩与转速。</td>
<td width="320">力矩密度、反驱性与驱控协同设计。</td>
<td width="320">热设计、绕组制造与一致性。</td>
<td width="340">持续与峰值力矩、效率曲线、温升。</td>
</tr>
<tr>
<td width="240" nowrap><a id="02-02"></a>谐波、行星与摆线减速</td>
<td width="300">在体积约束下放大力矩。</td>
<td width="320">摩擦、回差补偿与传动柔性建模。</td>
<td width="320">寿命、精度、冲击承载与批次差异。</td>
<td width="340">减速比、回差、刚度与疲劳工况。</td>
</tr>
<tr>
<td width="240" nowrap><a id="02-03"></a>丝杠与线性执行器</td>
<td width="300">产生直线推力与精密位移。</td>
<td width="320">非线性摩擦、载荷估计与结构优化。</td>
<td width="320">润滑、密封、安装与轴向寿命。</td>
<td width="340">额定推力、行程、速度与工作循环。</td>
</tr>
<tr>
<td width="240" nowrap><a id="02-04"></a>一体化关节模组</td>
<td width="300">把电机、传动、驱动与传感封装为关节。</td>
<td width="320">模块化本体与动力学辨识。</td>
<td width="320">线束、散热、总线与更换效率。</td>
<td width="340">关节接口、质量、持续输出与总线时延。</td>
</tr>
<tr>
<td width="240" nowrap><a id="02-05"></a>伺服驱动与底层控制</td>
<td width="300">把电流、速度与位置指令稳定执行。</td>
<td width="320">高带宽控制、扰动观测与力矩估计。</td>
<td width="320">保护机制、实时性与参数整定。</td>
<td width="340">控制周期、抖动、反馈分辨率。</td>
</tr>
<tr>
<td width="240" nowrap><a id="02-06"></a>支承、制动与运动连接</td>
<td width="300">保障关节承载、停机保持与运动供能。</td>
<td width="320">接触磨损、失效预测与轻量结构。</td>
<td width="320">轴承、制动器、拖链、线束与密封配套。</td>
<td width="340">承载寿命、弯折寿命、防护与维护周期。</td>
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
<td width="280" nowrap><a href="https://www.harmonicdrive.net/products">Harmonic Drive</a></td>
<td width="300">企业 / 传动与执行器</td>
<td width="520">精密齿轮、旋转与直线执行器、伺服驱动产品类别。</td>
<td width="360">产品或开发资料公开</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://www.ti.com/applications/industrial/robotics/overview.html">德州仪器机器人设计资源</a></td>
<td width="300">企业 / 电子与控制部件</td>
<td width="520">机器人电子、驱动、传感和通信设计入口。</td>
<td width="360">产品或开发资料公开</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://toddlerbot.github.io/">ToddlerBot（斯坦福大学）</a></td>
<td width="300">高校 / 开放本体研究</td>
<td width="520">公开本体设计、装配资料和运动操作研究。</td>
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

- [人形机器人](../embodiment/humanoid.md)
- [人形与双足硬件参考](../embodiment/hardware.md)

来源核对日期：2026-09-08
