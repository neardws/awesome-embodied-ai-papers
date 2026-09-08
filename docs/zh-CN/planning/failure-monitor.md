# 失败监测

[首页](../../../README.zh-CN.md) | [英文](../../en/planning/failure-monitor.md) | [方向目录](README.md)

共 9 篇。

<table width="3110">
<thead>
<tr>
<th width="120" nowrap>会议/年份</th>
<th width="320">论文/方法</th>
<th width="420">摘要</th>
<th width="240">规划粒度</th>
<th width="260">工具/记忆</th>
<th width="300">反馈/自改进</th>
<th width="260">执行接口</th>
<th width="260">验证环境</th>
<th width="360">论文任务/目标</th>
<th width="110" nowrap>论文</th>
<th width="110" nowrap>项目</th>
<th width="110" nowrap>代码</th>
<th width="240">数据/基准</th>
</tr>
</thead>
<tbody>
<tr>
<td width="120" nowrap>ICRA 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2510.16281">Do What You Say: Grounding Language-Conditioned Robotic Actions with Vision-Language Models</a></td>
<td width="420">该方法运行时检查 VLA 文本推理和动作结果是否一致，再选择是否执行动作。</td>
<td width="240">失败监测</td>
<td width="260">视觉语言模型推理检查器</td>
<td width="300">推理动作一致性</td>
<td width="260">VLA 动作选择</td>
<td width="260">真实机器人操作</td>
<td width="360">检测“说的计划”和“做的动作”是否一致。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2510.16281">论文</a></td>
<td width="110" nowrap><a href="https://yilin-wu98.github.io/steering-reasoning-vla/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/NVlabs/actalign">代码</a></td>
<td width="240"><a href="https://github.com/NVlabs/actalign">data</a></td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=N22lDHYrXe">Experience-based Knowledge Correction for Robust Planning in Minecraft</a></td>
<td width="420">XENON 从经验中修正依赖图和行动知识，提高 Minecraft 长程规划鲁棒性。</td>
<td width="240">失败监控</td>
<td width="260">基于经验的知识纠正</td>
<td width="300">失败监控</td>
<td width="260">失败监测</td>
<td width="260">Minecraft</td>
<td width="360">解决大语言模型初始知识错误且难通过反馈修正的问题。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=N22lDHYrXe">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=WC6MJ5r5Bj">ReCAPA: Hierarchical Predictive Correction to Mitigate Cascading Failures</a></td>
<td width="420">ReCAPA 在动作、子目标、轨迹三层预测并校正偏差以抑制级联失败。</td>
<td width="240">失败监控</td>
<td width="260">-</td>
<td width="300">层级预测纠正</td>
<td width="260">失败监测</td>
<td width="260">-</td>
<td width="360">解决多步 VLA 执行中局部错误向后传播的问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2604.21232">论文</a></td>
<td width="110" nowrap><a href="https://sunandreas0437-svg.github.io/recapa-project-page/">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=jr9hGWQioP">Self-Refining Vision Language Model for Robotic Failure Detection and Reasoning</a></td>
<td width="420">ARMOR 将失败检测和自然语言原因解释建模为多轮自细化任务。</td>
<td width="240">失败监控</td>
<td width="260">-</td>
<td width="300">自我优化</td>
<td width="260">失败监测</td>
<td width="260">-</td>
<td width="360">解决真实机器人失败微妙、组合多且标注稀缺的问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2602.12405">论文</a></td>
<td width="110" nowrap><a href="https://sites.google.com/utexas.edu/armor">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/61750">Sentinel-VLA: A Metacognitive VLA Model with Active Status Monitoring for Dynamic Reasoning and Error Recovery</a></td>
<td width="420">加入主动状态监控，使 VLA 模型能发现执行问题并触发恢复推理。</td>
<td width="240">失败监控</td>
<td width="260">-</td>
<td width="300">失败监控</td>
<td width="260">VLA/动作</td>
<td width="260">-</td>
<td width="360">发现并修复执行失败</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/61750">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/63650">NeurVLA: Unleashing Failure-Handling Capability of Vision-Language-Action Models via Neural-Symbolic Reasoning</a></td>
<td width="420">用神经符号推理诊断失败，并提升 VLA 操作策略的恢复能力。</td>
<td width="240">失败监控</td>
<td width="260">-</td>
<td width="300">失败监控</td>
<td width="260">VLA/动作</td>
<td width="260">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/63650">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/64203">Can VLMs Diagnose and Recover from VLA Manipulation Faults?</a></td>
<td width="420">评估视觉语言模型是否能诊断操作故障，并为失败的 VLA 执行提供恢复指导。</td>
<td width="240">失败监控</td>
<td width="260">-</td>
<td width="300">失败监控</td>
<td width="260">VLA/动作</td>
<td width="260">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/64203">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2510.09459">Failure Prediction at Runtime for Generative Robot Policies</a></td>
<td width="420">FIPER 在无需失败数据的情况下预测生成式模仿策略运行时失败。</td>
<td width="240">失败监控</td>
<td width="260">-</td>
<td width="300">运行时失败预测</td>
<td width="260">失败监测</td>
<td width="260">-</td>
<td width="360">解决扩散/流操作策略部署时早期失败预测。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2510.09459">论文</a></td>
<td width="110" nowrap><a href="https://tum-lsy.github.io/fiper_website">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2412.04455">Code-as-Monitor: Constraint-aware Visual Programming for Reactive and Proactive Robotic Failure Detection</a></td>
<td width="420">用视觉语言模型生成约束监控代码，同时做反应式和预防式失败检测。</td>
<td width="240">失败监控</td>
<td width="260">视觉语言模型生成的监测代码 + 约束要素</td>
<td width="300">失败监控</td>
<td width="260">开环策略上的闭环监测</td>
<td width="260">CLIPort、OmniGibson、真实场景</td>
<td width="360">解决开集机器人失败的实时检测和预防。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2412.04455">论文</a></td>
<td width="110" nowrap><a href="https://zhoues.github.io/Code-as-Monitor/">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
</tbody>
</table>
