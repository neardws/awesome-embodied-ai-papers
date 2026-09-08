# 计算、通信与能源

[首页](../../../README.zh-CN.md) | [英文](../../en/landscape/05-compute.md) | [全景目录](README.md)

怎样把高算力推理与确定性控制放进同一台机器人？

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
<td width="240" nowrap><a id="05-01"></a>推理芯片与异构加速</td>
<td width="300">在设备上执行感知与策略模型。</td>
<td width="320">压缩、编译与模型硬件协同。</td>
<td width="320">算子支持、工具链、内存与供货。</td>
<td width="340">目标模型实测时延、内存与功耗。</td>
</tr>
<tr>
<td width="240" nowrap><a id="05-02"></a>边缘计算与域控制器</td>
<td width="300">承载多传感、多模型与系统服务。</td>
<td width="320">多任务调度、计算分层与资源共享。</td>
<td width="320">散热、连接器、抗振与远程管理。</td>
<td width="340">并发负载下时延、热稳态与接口数量。</td>
</tr>
<tr>
<td width="240" nowrap><a id="05-03"></a>实时微控制与功率驱动</td>
<td width="300">保持底层闭环与电机保护。</td>
<td width="320">实时调度、控制鲁棒性与故障检测。</td>
<td width="320">电流采样、保护链路与固件维护。</td>
<td width="340">最坏控制周期、抖动与故障响应。</td>
</tr>
<tr>
<td width="240" nowrap><a id="05-04"></a>机内总线与工业网络</td>
<td width="300">传送有时限的状态与指令。</td>
<td width="320">网络化控制与时间同步。</td>
<td width="320">布线、兼容性、诊断与电磁环境。</td>
<td width="340">端到端延迟、丢包、同步与恢复。</td>
</tr>
<tr>
<td width="240" nowrap><a id="05-05"></a>无线、云边与远程连接</td>
<td width="300">支持遥操作、更新和跨设备协作。</td>
<td width="320">延迟补偿、任务卸载与断连自治。</td>
<td width="320">覆盖、带宽、身份管理与回滚。</td>
<td width="340">断网行为、回传负载与接管时延。</td>
</tr>
<tr>
<td width="240" nowrap><a id="05-06"></a>电池、电源与热管理</td>
<td width="300">在持续任务中稳定供能。</td>
<td width="320">能耗建模、能量感知规划与热控制。</td>
<td width="320">电池管理、充换电、散热与寿命。</td>
<td width="340">任务续航、峰值电流、温升与循环寿命。</td>
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
<td width="280" nowrap><a href="https://www.nvidia.com/en-us/industries/robotics/">NVIDIA 机器人平台</a></td>
<td width="300">企业 / 计算与开发平台</td>
<td width="520">训练、仿真、机器人软件加速和端侧推理的平台分工。</td>
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
</tbody>
</table>

示例用于说明本板块中的部分实现，并非每个细类的完整名录或市场排名。公开资源未在本地复现；产品页不证明即时供货、接口互通或独立测试性能。[证据规则与来源](sources.md).

## 与其他环节的接口

将上表指标作为接口约定：写清配置、量纲、时序、失效行为和负责环节。部件能力不自动等于整机能力；把研究结果用于实际部署前，应对齐任务负载和适用工况。

## 关联论文方向

- [实时执行](../deployment/real-time.md)
- [量化、缓存与词元化](../deployment/quantization-cache-tokenization.md)

来源核对日期：2026-09-08
