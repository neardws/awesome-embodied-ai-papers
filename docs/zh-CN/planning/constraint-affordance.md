# 约束与可供性规划

[首页](../../../README.zh-CN.md) | [英文](../../en/planning/constraint-affordance.md) | [方向目录](README.md)

共 11 篇。

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
<td width="120" nowrap>CoRL 2023</td>
<td width="320"><a href="https://arxiv.org/abs/2307.05973">VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models</a></td>
<td width="420">VoxPoser 根据语言模型组合三维价值地图，用于操作规划。</td>
<td width="240">任务分解</td>
<td width="260">语言/场景上下文</td>
<td width="300">执行反馈</td>
<td width="260">机器人动作接口</td>
<td width="260">具身基准</td>
<td width="360">补充 CoRL 规划研究覆盖。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2307.05973">论文</a></td>
<td width="110" nowrap><a href="https://voxposer.github.io">项目</a></td>
<td width="110" nowrap><a href="https://github.com/huangwl18/VoxPoser">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICRA 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2408.14769">Points2Plans: From Point Clouds to Long-Horizon Plans with Composable Relational Dynamics</a></td>
<td width="420">Points2Plans 从点云和语言指令出发，用关系动力学连接高层计划和连续参数规划。</td>
<td width="240">约束 / 可供性规划</td>
<td width="260">点云关系动力学</td>
<td width="300">可组合规划反馈</td>
<td width="260">连续参数规划器</td>
<td width="260">仿真 + 实机</td>
<td width="360">把语言计划落到可执行的三维关系动力学约束。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2408.14769">论文</a></td>
<td width="110" nowrap><a href="https://sites.google.com/stanford.edu/points2plans">项目</a></td>
<td width="110" nowrap><a href="https://github.com/yixuanhuang98/Points2Plans">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=enprG5H9aD">SLAP: Shortcut Learning for Abstract Planning</a></td>
<td width="420">SLAP 从已有 TAMP 选项中自动发现低层捷径选项策略。</td>
<td width="240">任务与运动规划选项策略/捷径学习</td>
<td width="260">-</td>
<td width="300">约束/可供性</td>
<td width="260">规划 / 可供性</td>
<td width="260">-</td>
<td width="360">解决 TAMP 抽象动作依赖人工定义、行为空间受限的问题。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=enprG5H9aD">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=kWCNhRdcDI">Natural Language PDDL (NL-PDDL) for Open-world Goal-oriented Commonsense Regression Planning in Embodied AI</a></td>
<td width="420">用自然语言 PDDL 做开放世界目标回归规划。</td>
<td width="240">常识回归规划</td>
<td width="260">NL-PDDL</td>
<td width="300">约束/可供性</td>
<td width="260">规划 / 可供性</td>
<td width="260">-</td>
<td width="360">解决开放世界中部分可观测和知识不完整下的长程因果规划。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=kWCNhRdcDI">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=refcXHU1Nh">SafeFlowMatcher: Safe and Fast Planning using Flow Matching with Control Barrier Functions</a></td>
<td width="420">将流匹配规划器与控制屏障函数结合，保证快速且安全。</td>
<td width="240">约束/可供性</td>
<td width="260">控制屏障函数安全约束</td>
<td width="300">预测纠正积分器</td>
<td width="260">VLA/动作</td>
<td width="260">-</td>
<td width="360">解决生成式路径规划缺少形式化安全约束的问题。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=refcXHU1Nh">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=bGPDviEtZ1">MoMaGen: Generating Demonstrations under Soft and Hard Constraints for Multi-Step Bimanual Mobile Manipulation</a></td>
<td width="420">在软硬约束下自动生成多步双臂移动操作示范。</td>
<td width="240">以约束为条件的示范生成</td>
<td width="260">-</td>
<td width="300">-</td>
<td width="260">规划 / 可供性</td>
<td width="260">-</td>
<td width="360">解决多步双臂移动操作示范采集成本高的问题。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=bGPDviEtZ1">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38907">A3D: Adaptive Affordance Assembly with Dual-Arm Manipulation</a></td>
<td width="420">学习双臂装配中的自适应可供性，并随物体和任务状态变化更新操作选择。</td>
<td width="240">约束/可供性</td>
<td width="260">-</td>
<td width="300">-</td>
<td width="260">规划 / 可供性</td>
<td width="260">-</td>
<td width="360">双臂自适应可供性装配</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38907">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38909">Affordance-Guided Coarse-to-Fine Exploration for Base Placement in Open-Vocabulary Mobile Manipulation</a></td>
<td width="420">用可供性先验引导移动操作底座放置，再通过由粗到细的可行性细化确定位置。</td>
<td width="240">由粗到细的底座放置</td>
<td width="260">可供性引导</td>
<td width="300">-</td>
<td width="260">规划 / 可供性</td>
<td width="260">-</td>
<td width="360">用可供性指导开放词汇移动操作中的底盘放置探索。</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38909">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38955">Gentle Manipulation Policy Learning via Demonstrations from VLM Planned Atomic Skills</a></td>
<td width="420">用视觉语言模型规划的原子技能作为示范，学习温和的长程操作策略。</td>
<td width="240">约束/可供性</td>
<td width="260">视觉语言模型规划的原子技能</td>
<td width="300">-</td>
<td width="260">VLA/动作</td>
<td width="260">-</td>
<td width="360">轻柔操作策略学习</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38955">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://openreview.net/forum?id=wr47LsSUjH">InstructFlow: Adaptive Symbolic Constraint-Guided Code Generation for Long-Horizon Planning</a></td>
<td width="420">InstructFlow 用符号反馈流把失败诱导出的约束注入指令图和代码生成。</td>
<td width="240">约束/可供性</td>
<td width="260">约束/可供性</td>
<td width="300">失败诊断 + 符号约束</td>
<td width="260">流匹配 / 规划 / 推理</td>
<td width="260">-</td>
<td width="360">解决大语言模型长程规划代码幻觉、物理不可行和失败恢复差的问题。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=wr47LsSUjH">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/chiht21/InstructFlow">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://iccv.thecvf.com/virtual/2025/poster/542">CoA-VLA: Improving Vision-Language-Action Models via Visual-Text Chain-of-Affordance</a></td>
<td width="420">用视觉-文本可供性链在测试时增强 VLA 推理。</td>
<td width="240">约束/可供性</td>
<td width="260">-</td>
<td width="300">测试时可供性推理</td>
<td width="260">VLA/动作</td>
<td width="260">-</td>
<td width="360">解决 VLA 自驱动可供性推理和鲁棒行动不足。</td>
<td width="110" nowrap><a href="https://openaccess.thecvf.com/content/ICCV2025/papers/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.pdf">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
</tbody>
</table>
