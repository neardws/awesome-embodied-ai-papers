# 轻量化 / 评测 / 数据

[首页](../../../README.zh-CN.md) | [英文](../../en/deployment/README.md)

这一方向决定能不能真实部署：端侧推理、缓存/量化/动作词元化、实时执行、仿真到现实、基准和安全评测都是必需条件。

子方向：量化/缓存/词元化、实时执行、基准/数据集、仿真到现实、安全评测。

共 105 篇。

<table width="1090">
<thead>
<tr>
<th width="280">子方向</th>
<th width="90" nowrap>条目数</th>
<th width="720">观察重点</th>
</tr>
</thead>
<tbody>
<tr>
<td width="280">量化/缓存/词元化</td>
<td width="90" nowrap>22</td>
<td width="720">看端侧部署、缓存复用和动作词元效率。</td>
</tr>
<tr>
<td width="280">实时执行</td>
<td width="90" nowrap>6</td>
<td width="720">看低延迟执行和实时策略推理。</td>
</tr>
<tr>
<td width="280">基准/数据集</td>
<td width="90" nowrap>44</td>
<td width="720">看数据覆盖、任务设计和评测可信度。</td>
</tr>
<tr>
<td width="280">仿真到现实</td>
<td width="90" nowrap>20</td>
<td width="720">看仿真到真实迁移和真实部署差距。</td>
</tr>
<tr>
<td width="280">安全评测</td>
<td width="90" nowrap>13</td>
<td width="720">看鲁棒性、安全性和部署风险评估。</td>
</tr>
</tbody>
</table>


# 子方向文件

<table width="430">
<thead>
<tr>
<th width="340">主题</th>
<th width="90" nowrap>条目数</th>
</tr>
</thead>
<tbody>
<tr>
<td width="340"><a href="quantization-cache-tokenization.md">量化、缓存与词元化</a></td>
<td width="90" nowrap>22</td>
</tr>
<tr>
<td width="340"><a href="real-time.md">实时执行</a></td>
<td width="90" nowrap>6</td>
</tr>
<tr>
<td width="340"><a href="benchmarks-datasets.md">基准与数据集</a></td>
<td width="90" nowrap>44</td>
</tr>
<tr>
<td width="340"><a href="sim2real.md">仿真到现实</a></td>
<td width="90" nowrap>20</td>
</tr>
<tr>
<td width="340"><a href="safety-evaluation.md">安全评测</a></td>
<td width="90" nowrap>13</td>
</tr>
</tbody>
</table>

<!-- landscape-links:start -->

## 学术与产业关联

从以下板块继续查看与本研究方向相关的硬件、软件和交付问题。

<table width="1060">
<thead>
<tr>
<th width="300" nowrap>全景板块</th>
<th width="760">系统问题</th>
</tr>
</thead>
<tbody>
<tr>
<td width="300" nowrap><a href="../landscape/05-compute.md">计算、通信与能源</a></td>
<td width="760">怎样把高算力推理与确定性控制放进同一台机器人？</td>
</tr>
<tr>
<td width="300" nowrap><a href="../landscape/09-systems.md">系统软件与集成平台</a></td>
<td width="760">如何把异构设备、模型和技能组成可开发、可调试的机器人系统？</td>
</tr>
<tr>
<td width="300" nowrap><a href="../landscape/10-data.md">数据采集与治理</a></td>
<td width="760">怎样把分散的演示与运行经验变成可复用、可追溯的数据资产？</td>
</tr>
<tr>
<td width="300" nowrap><a href="../landscape/11-simulation.md">仿真与训练基础设施</a></td>
<td width="760">如何用可控实验加速研发，同时识别仿真无法替代的真实因素？</td>
</tr>
<tr>
<td width="300" nowrap><a href="../landscape/12-operations.md">评测、安全与部署运维</a></td>
<td width="760">怎样把单次任务效果转化为可测、可恢复、可持续运行的系统能力？</td>
</tr>
<tr>
<td width="300" nowrap><a href="../landscape/13-manufacturing.md">制造、集成与交付</a></td>
<td width="760">怎样把实验样机变成可制造、可维护且配置明确的交付物？</td>
</tr>
<tr>
<td width="300" nowrap><a href="../landscape/14-applications.md">应用与解决方案</a></td>
<td width="760">机器人服务于哪些工作流程，价值如何通过真实任务衡量？</td>
</tr>
</tbody>
</table>

<!-- landscape-links:end -->
