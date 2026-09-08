# 制造、集成与交付

[首页](../../../README.zh-CN.md) | [英文](../../en/landscape/13-manufacturing.md) | [全景目录](README.md)

怎样把实验样机变成可制造、可维护且配置明确的交付物？

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
<td width="240" nowrap><a id="13-01"></a>结构材料与精密制造</td>
<td width="300">实现强度、重量与尺寸要求。</td>
<td width="320">轻量结构、材料设计与拓扑优化。</td>
<td width="320">加工能力、表面处理与公差控制。</td>
<td width="340">质量、公差、疲劳与材料批次。</td>
</tr>
<tr>
<td width="240" nowrap><a id="13-02"></a>增材制造与快速迭代</td>
<td width="300">缩短设计验证与样件制造周期。</td>
<td width="320">复杂结构、柔性器件与多材料设计。</td>
<td width="320">工艺选择、后处理与一致性。</td>
<td width="340">样件周期、强度方向性与返工率。</td>
</tr>
<tr>
<td width="240" nowrap><a id="13-03"></a>装配、标定与出厂测试</td>
<td width="300">降低个体间性能差异。</td>
<td width="320">自动标定、参数辨识与误差传播。</td>
<td width="320">装配工艺、检测工装与可追溯记录。</td>
<td width="340">标定残差、合格率与一致性。</td>
</tr>
<tr>
<td width="240" nowrap><a id="13-04"></a>供应链与配置管理</td>
<td width="300">控制部件变化及其系统影响。</td>
<td width="320">可替代设计与模块化架构。</td>
<td width="320">物料清单、替代件、版本与交期。</td>
<td width="340">配置可追溯性、替代验证与维护兼容。</td>
</tr>
<tr>
<td width="240" nowrap><a id="13-05"></a>系统集成与工位改造</td>
<td width="300">把机器人接入真实业务流程。</td>
<td width="320">任务建模、人机协作与混合自动化。</td>
<td width="320">工装、现场接口、调试与验收。</td>
<td width="340">改造时间、稳定节拍与异常处理。</td>
</tr>
<tr>
<td width="240" nowrap><a id="13-06"></a>维护、培训与生命周期</td>
<td width="300">保持设备与人员长期可用。</td>
<td width="320">预测维护、维修性设计与技能迁移。</td>
<td width="320">备件、培训、维修流程与版本支持。</td>
<td width="340">维修时间、维护成本与支持周期。</td>
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
<td width="280" nowrap><a href="https://www.protolabs.com/industries/robotics/">Protolabs</a></td>
<td width="300">企业 / 制造服务</td>
<td width="520">机器人零件的数控加工、增材制造与成型服务。</td>
<td width="360">产品或开发资料公开</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://www.harmonicdrive.net/products">Harmonic Drive</a></td>
<td width="300">企业 / 传动与执行器</td>
<td width="520">精密齿轮、旋转与直线执行器、伺服驱动产品类别。</td>
<td width="360">产品或开发资料公开</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://toddlerbot.github.io/">ToddlerBot（斯坦福大学）</a></td>
<td width="300">高校 / 开放本体研究</td>
<td width="520">公开本体设计、装配资料和运动操作研究。</td>
<td width="360">研究展示；代码或数据公开；本项目未复现</td>
</tr>
<tr>
<td width="280" nowrap><a href="https://www.nist.gov/el/intelligent-systems-division-73500/robotic-grasping-and-manipulation-assembly">美国国家标准与技术研究院</a></td>
<td width="300">研究机构 / 测量与评测</td>
<td width="520">围绕抓取、操作与装配建立性能测量研究。</td>
<td width="360">研究展示</td>
</tr>
</tbody>
</table>

示例用于说明本板块中的部分实现，并非每个细类的完整名录或市场排名。公开资源未在本地复现；产品页不证明即时供货、接口互通或独立测试性能。[证据规则与来源](sources.md).

## 与其他环节的接口

将上表指标作为接口约定：写清配置、量纲、时序、失效行为和负责环节。部件能力不自动等于整机能力；把研究结果用于实际部署前，应对齐任务负载和适用工况。

## 关联论文方向

- [仿真到现实](../deployment/sim2real.md)
- [人形与双足硬件参考](../embodiment/hardware.md)

来源核对日期：2026-09-08
