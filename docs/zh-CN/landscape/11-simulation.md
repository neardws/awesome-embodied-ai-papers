# 仿真与训练基础设施

[首页](../../../README.zh-CN.md) | [英文](../../en/landscape/11-simulation.md) | [全景目录](README.md)

如何用可控实验加速研发，同时识别仿真无法替代的真实因素？

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
<td width="240" nowrap><a id="11-01"></a>物理引擎与接触求解</td>
<td width="300">计算运动、碰撞与接触响应。</td>
<td width="320">可微物理、摩擦模型与数值稳定。</td>
<td width="320">求解速度、模型标定与资产兼容。</td>
<td width="340">接触误差、稳定性与仿真吞吐。</td>
</tr>
<tr>
<td width="240" nowrap><a id="11-02"></a>数字孪生与资产构建</td>
<td width="300">建立场景、机器人与物体的数字表示。</td>
<td width="320">重建、参数辨识与自动资产生成。</td>
<td width="320">资产质量、版本维护与现场一致性。</td>
<td width="340">几何动力学误差、制作成本与更新时间。</td>
</tr>
<tr>
<td width="240" nowrap><a id="11-03"></a>传感仿真与合成数据</td>
<td width="300">生成多模态观测及其标签。</td>
<td width="320">渲染真实性、触觉仿真与数据混合。</td>
<td width="320">生成流程、标注规范与域差评估。</td>
<td width="340">传感差异、标签质量与真实任务增益。</td>
</tr>
<tr>
<td width="240" nowrap><a id="11-04"></a>并行训练与实验管理</td>
<td width="300">提高策略训练和比较效率。</td>
<td width="320">分布式采样、优化稳定与可复现性。</td>
<td width="320">资源调度、检查点、成本与版本固定。</td>
<td width="340">训练预算、随机种子方差与复现实验。</td>
</tr>
<tr>
<td width="240" nowrap><a id="11-05"></a>领域随机化与迁移</td>
<td width="300">降低仿真与实机行为差异。</td>
<td width="320">自适应随机化、系统辨识与残差学习。</td>
<td width="320">真实校准、迁移测试与故障回退。</td>
<td width="340">真实任务成功率与迁移所需数据。</td>
</tr>
<tr>
<td width="240" nowrap><a id="11-06"></a>软件、硬件在环验证</td>
<td width="300">在上线前测试控制与通信链路。</td>
<td width="320">联合仿真、时序一致与边界覆盖。</td>
<td width="320">真实控制器接入、故障注入与回归测试。</td>
<td width="340">时序误差、故障覆盖与测试可重复性。</td>
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
<td width="280" nowrap><a href="https://mujoco.org/">MuJoCo / Google DeepMind</a></td>
<td width="300">企业支持的开源项目 / 物理仿真</td>
<td width="520">用于机器人和接触动力学研究的物理仿真器。</td>
<td width="360">代码或数据公开；本项目未复现</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://isaac-sim.github.io/IsaacLab/main/index.html">NVIDIA Isaac Lab</a></td>
<td width="300">企业与社区 / 训练框架</td>
<td width="520">面向机器人学习的仿真环境与训练工作流。</td>
<td width="360">代码或数据公开；本项目未复现</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://robotwin-platform.github.io/">RoboTwin 联合团队</a></td>
<td width="300">高校、研究院与企业 / 数据和评测</td>
<td width="520">双臂任务生成、领域随机化与统一评测资源。</td>
<td width="360">研究展示；代码或数据公开；本项目未复现</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://www.nvidia.com/en-us/industries/robotics/">NVIDIA 机器人平台</a></td>
<td width="300">企业 / 计算与开发平台</td>
<td width="520">训练、仿真、机器人软件加速和端侧推理的平台分工。</td>
<td width="360">产品或开发资料公开</td>
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

- [仿真到现实](../deployment/sim2real.md)
- [视频与潜在世界模型](../wam/video-latent.md)

来源核对日期：2026-09-08
