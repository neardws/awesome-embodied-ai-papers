# 数据采集与治理

[首页](../../../README.zh-CN.md) | [英文](../../en/landscape/10-data.md) | [全景目录](README.md)

怎样把分散的演示与运行经验变成可复用、可追溯的数据资产？

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
<td width="240" nowrap><a id="10-01"></a>遥操作与示范采集<br><a href="../products/topics/10-01.md">产品细节</a></td>
<td width="300">获得包含观察和动作的训练轨迹。</td>
<td width="320">低负担示教、纠正学习与延迟补偿。</td>
<td width="320">采集工位、操作培训、复位与质检。</td>
<td width="340">有效轨迹比例、每条成本与任务覆盖。</td>
</tr>
<tr>
<td width="240" nowrap><a id="10-02"></a>人类视频与跨本体重定向<br><a href="../products/topics/10-02.md">产品细节</a></td>
<td width="300">利用不同身体产生的动作经验。</td>
<td width="320">动作潜变量、运动对应与形态适配。</td>
<td width="320">标定、动作边界、工具与场景匹配。</td>
<td width="340">重定向误差与迁移后的任务表现。</td>
</tr>
<tr>
<td width="240" nowrap><a id="10-03"></a>自动探索与失败采集<br><a href="../products/topics/10-03.md">产品细节</a></td>
<td width="300">补充困难状态与失败恢复数据。</td>
<td width="320">主动学习、探索与数据选择。</td>
<td width="320">风险控制、人工接管与自动复位。</td>
<td width="340">新增覆盖、介入频率与有效失败样本。</td>
</tr>
<tr>
<td width="240" nowrap><a id="10-04"></a>多模态同步与标注<br><a href="../products/topics/10-04.md">产品细节</a></td>
<td width="300">对齐视觉、触觉、状态、动作和语言。</td>
<td width="320">弱监督、时序对齐与语义标注。</td>
<td width="320">时钟、校准、标注流程与一致性抽检。</td>
<td width="340">同步误差、标签一致性与缺失率。</td>
</tr>
<tr>
<td width="240" nowrap><a id="10-05"></a>清洗、版本与数据质量<br><a href="../products/topics/10-05.md">产品细节</a></td>
<td width="300">避免泄漏、重复和质量漂移。</td>
<td width="320">数据价值评估与分布诊断。</td>
<td width="320">版本追踪、回滚、质量门槛与许可。</td>
<td width="340">去重、训练测试隔离与可追溯性。</td>
</tr>
<tr>
<td width="240" nowrap><a id="10-06"></a>数据格式、共享与数据闭环<br><a href="../products/topics/10-06.md">产品细节</a></td>
<td width="300">让不同团队与机器人复用数据。</td>
<td width="320">统一表示、跨数据集训练与持续学习。</td>
<td width="320">格式转换、访问管理与运行数据回流。</td>
<td width="340">模式兼容、来源记录与迭代收益。</td>
</tr>
</tbody>
</table>

## 技术与产品细节

<a href="../products/comparisons/10-data.md">查看 17 条相关对照记录</a>

继续比较逐型号参数、工况、接口、研究关联和来源问题，并下钻查看完整技术摘录与原始展项链接。

<a href="../products/references/09-03.md">遥操作与数据采集工具链</a>

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
<td width="280" nowrap><a href="https://robotics-transformer-x.github.io/">Open X-Embodiment 协作组</a></td>
<td width="300">高校与企业 / 数据协作</td>
<td width="520">跨本体数据格式、数据集合与策略迁移研究。</td>
<td width="360">研究展示；代码或数据公开；本项目未复现</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://droid-dataset.github.io/">DROID 多机构团队</a></td>
<td width="300">研究协作 / 真实数据</td>
<td width="520">面向真实多样环境的机器人操作数据与采集方案。</td>
<td width="360">研究展示；代码或数据公开；本项目未复现</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://umi-gripper.github.io/">UMI 研究团队</a></td>
<td width="300">学术研究 / 数据工具</td>
<td width="520">便携示教接口与人类示范到机器人策略的研究。</td>
<td width="360">研究展示；代码或数据公开；本项目未复现</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://huggingface.co/docs/lerobot/index">Hugging Face / LeRobot</a></td>
<td width="300">企业与社区 / 学习工具链</td>
<td width="520">机器人数据、训练与真实设备接入的开源工具链。</td>
<td width="360">代码或数据公开；本项目未复现</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://github.com/OpenDriveLab/AgiBot-World">AgiBot World / OpenDriveLab</a></td>
<td width="300">学界与产业协作 / 数据和基础策略</td>
<td width="520">公开机器人操作数据、模型和开发资料。</td>
<td width="360">研究展示；代码或数据公开；本项目未复现</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://www.lightwheel.ai/">光轮智能</a></td>
<td width="300">企业 / 仿真、数据与评测</td>
<td width="520">公开仿真资产、第一视角数据和仿真评测平台介绍。</td>
<td width="360">产品或开发资料公开</td>
</tr>
</tbody>
</table>

示例用于说明本板块中的部分实现，并非每个细类的完整名录或市场排名。公开资源未在本地复现；产品页不证明即时供货、接口互通或独立测试性能。[证据规则与来源](sources.md).

## 与其他环节的接口

将上表指标作为接口约定：写清配置、量纲、时序、失效行为和负责环节。部件能力不自动等于整机能力；把研究结果用于实际部署前，应对齐任务负载和适用工况。

## 关联论文方向

- [基准与数据集](../deployment/benchmarks-datasets.md)
- [动作表示](../vla/action-representation.md)

来源核对日期：2026-09-08
