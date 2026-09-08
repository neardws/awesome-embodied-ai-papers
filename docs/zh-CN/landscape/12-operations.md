# 评测、安全与部署运维

[首页](../../../README.zh-CN.md) | [英文](../../en/landscape/12-operations.md) | [全景目录](README.md)

怎样把单次任务效果转化为可测、可恢复、可持续运行的系统能力？

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
<td width="240" nowrap><a id="12-01"></a>能力基准与任务评测</td>
<td width="300">以可比条件衡量能力。</td>
<td width="320">任务设计、泛化划分与统计显著性。</td>
<td width="320">现场任务映射、验收条件与回归集。</td>
<td width="340">成功率、覆盖、方差与失败分布。</td>
</tr>
<tr>
<td width="240" nowrap><a id="12-02"></a>可靠性与长时程测试</td>
<td width="300">发现连续运行中的累积故障。</td>
<td width="320">误差传播、鲁棒性与寿命建模。</td>
<td width="320">老化测试、任务中断与备件维护。</td>
<td width="340">运行时长、故障频率与恢复时间。</td>
</tr>
<tr>
<td width="240" nowrap><a id="12-03"></a>安全约束与系统防护</td>
<td width="300">限制危险动作和失控传播。</td>
<td width="320">安全控制、约束验证与风险感知。</td>
<td width="320">保护链路、急停、隔离与责任边界。</td>
<td width="340">约束违反、响应时间与验证覆盖。</td>
</tr>
<tr>
<td width="240" nowrap><a id="12-04"></a>端侧部署与模型更新</td>
<td width="300">把模型稳定运行在目标设备上。</td>
<td width="320">压缩、缓存、推理调度与在线适配。</td>
<td width="320">版本发布、灰度更新、回滚与兼容。</td>
<td width="340">端到端时延、资源占用与回归结果。</td>
</tr>
<tr>
<td width="240" nowrap><a id="12-05"></a>接管、诊断与恢复</td>
<td width="300">在失败时维持可控运行。</td>
<td width="320">异常检测、恢复策略与人机协同。</td>
<td width="320">报警、远程接管、故障定位与复位。</td>
<td width="340">介入次数、接管时延与恢复后完成率。</td>
</tr>
<tr>
<td width="240" nowrap><a id="12-06"></a>机队、服务与运营指标</td>
<td width="300">管理多机任务与长期服务。</td>
<td width="320">协作调度、队列与资源优化。</td>
<td width="320">工单、可用率、运维成本与设施对接。</td>
<td width="340">吞吐、利用率、每任务成本与停机。</td>
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
<td width="280" nowrap><a href="https://www.nist.gov/el/intelligent-systems-division-73500/robotic-grasping-and-manipulation-assembly">美国国家标准与技术研究院</a></td>
<td width="300">研究机构 / 测量与评测</td>
<td width="520">围绕抓取、操作与装配建立性能测量研究。</td>
<td width="360">研究展示</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://robotwin-platform.github.io/">RoboTwin 联合团队</a></td>
<td width="300">高校、研究院与企业 / 数据和评测</td>
<td width="520">双臂任务生成、领域随机化与统一评测资源。</td>
<td width="360">研究展示；代码或数据公开；本项目未复现</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://www.open-rmf.org/">Open-RMF 社区</a></td>
<td width="300">开源生态 / 多机协调</td>
<td width="520">机器人机队与设施交互的协调框架。</td>
<td width="360">代码或数据公开；本项目未复现</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://foxglove.dev/">Foxglove</a></td>
<td width="300">企业 / 数据与可观测性平台</td>
<td width="520">机器人数据记录、管理和可视化分析工具。</td>
<td width="360">产品或开发资料公开</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://investors.gxo.com/news-releases/news-release-details/gxo-signs-industry-first-multi-year-agreement-agility-robotics">GXO / Agility Robotics</a></td>
<td width="300">运营方与企业 / 物流部署</td>
<td width="520">运营方于 2024 年披露 Digit 的商业部署协议与物流场景。</td>
<td width="360">运营方披露现场部署</td>
</tr>
</tbody>
</table>

示例用于说明本板块中的部分实现，并非每个细类的完整名录或市场排名。公开资源未在本地复现；产品页不证明即时供货、接口互通或独立测试性能。[证据规则与来源](sources.md).

## 与其他环节的接口

将上表指标作为接口约定：写清配置、量纲、时序、失效行为和负责环节。部件能力不自动等于整机能力；把研究结果用于实际部署前，应对齐任务负载和适用工况。

## 关联论文方向

- [安全评测](../deployment/safety-evaluation.md)
- [实时执行](../deployment/real-time.md)

来源核对日期：2026-09-08
