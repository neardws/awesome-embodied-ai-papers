# 物理可执行导航

[首页](../../../README.zh-CN.md) | [英文](../../en/vln/physically-executable.md) | [方向目录](README.md)

共 7 篇。

<table width="3050">
<thead>
<tr>
<th width="120" nowrap>会议/年份</th>
<th width="320">论文/方法</th>
<th width="420">摘要</th>
<th width="220">任务类型</th>
<th width="240">环境</th>
<th width="260">地图/记忆</th>
<th width="300">训练/反馈</th>
<th width="240">仿真/实机/基准</th>
<th width="360">论文任务/目标</th>
<th width="110" nowrap>论文</th>
<th width="110" nowrap>项目</th>
<th width="110" nowrap>代码</th>
<th width="240">数据/基准</th>
</tr>
</thead>
<tbody>
<tr>
<td width="120" nowrap>CVPR 2024</td>
<td width="320"><a href="https://openaccess.thecvf.com/content/CVPR2024/html/Ehsani_SPOC_Imitating_Shortest_Paths_in_Simulation_Enables_Effective_Navigation_and_CVPR_2024_paper.html">SPOC: Imitating Shortest Paths in Simulation Enables Effective Navigation and Manipulation in the Real World</a></td>
<td width="420">SPOC 使用仿真最短路径训练具身智能体，并将其行为迁移到导航与操作任务。</td>
<td width="220">导航 + 操作</td>
<td width="240">物理具身环境</td>
<td width="260">隐式空间策略记忆</td>
<td width="300">基于最短路径的模仿学习</td>
<td width="240">仿真 + 实机</td>
<td width="360">将最短路径监督转化为物理可执行的具身行为。</td>
<td width="110" nowrap><a href="https://openaccess.thecvf.com/content/CVPR2024/papers/Ehsani_SPOC_Imitating_Shortest_Paths_in_Simulation_Enables_Effective_Navigation_and_CVPR_2024_paper.pdf">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38942">CorrectNav: Self-Correction Flywheel Empowers Vision-Language-Action Navigation Model</a></td>
<td width="420">CorrectNav 利用模型错误轨迹自动生成感知与动作自纠正数据，后训练 VLA 导航模型。</td>
<td width="220">VLA 导航自纠正</td>
<td width="240">移动机器人/移动操作</td>
<td width="260">-</td>
<td width="300">自纠正数据飞轮/后训练</td>
<td width="240">-</td>
<td width="360">让 VLA 导航模型偏离正确轨迹后能恢复。</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38942">论文</a></td>
<td width="110" nowrap><a href="https://correctnav.github.io/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/owlet914/CorrectNav">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/64257">SC$^{2}$-WM: A Self-Correcting World Model with Closed-Loop Feedback for Vision-and-Language Navigation in Continuous Environments</a></td>
<td width="420">SC2-WM 用世界模型前瞻产生内部反馈，在 VLN-CE 推理中闭环修正状态漂移和计划。</td>
<td width="220">世界模型导航</td>
<td width="240">移动机器人/移动操作</td>
<td width="260">世界模型前瞻/内部反馈</td>
<td width="300">闭环自纠正世界模型</td>
<td width="240">-</td>
<td width="360">解决连续 VLN 中开环执行无法检测和纠正内部状态漂移。</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/64257">论文</a></td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/64257">项目</a></td>
<td width="110" nowrap><a href="https://github.com/sunrise-ikun/SC2_WM">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2507.13019">Rethinking the Embodied Gap in Vision-and-Language Navigation: A Holistic Study of Physical and Visual Disparities</a></td>
<td width="420">VLN-PE 系统评估人形机器人、四足、轮式机器人上视觉和物理差异对 VLN 的影响。</td>
<td width="220">物理视觉语言导航评测</td>
<td width="240">人形/四足/轮式机器人</td>
<td width="260">-</td>
<td width="300">具身导航</td>
<td width="240">实体机器人设置</td>
<td width="360">衡量理想 VLN 假设到真实机器人执行之间的具身差距。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2507.13019">论文</a></td>
<td width="110" nowrap><a href="https://crystalsixone.github.io/vln_pe.github.io/">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2506.23468">NavMorph: A Self-Evolving World Model for Vision-and-Language Navigation in Continuous Environments</a></td>
<td width="420">NavMorph 用自演化世界模型和上下文演化记忆对 VLN-CE 环境动态进行前瞻建模和策略细化。</td>
<td width="220">世界模型导航</td>
<td width="240">移动机器人/移动操作</td>
<td width="260">上下文演化记忆</td>
<td width="300">自演化世界模型/强化学习</td>
<td width="240">-</td>
<td width="360">提升连续 VLN 在新环境和过程变化中的自适应规划。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2506.23468">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/Feliciaxyao/NavMorph">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://iccv.thecvf.com/virtual/2025/poster/299">3D Gaussian Map with Open-Set Semantic Grouping for Vision-Language Navigation</a></td>
<td width="420">该文用开放集语义分组将三维几何先验和开放语义统一进高斯地图。</td>
<td width="220">地图/记忆</td>
<td width="240">移动机器人/移动操作</td>
<td width="260">三维高斯地图 + 开放集语义分组</td>
<td width="300">三维表示</td>
<td width="240">-</td>
<td width="360">开放语义面向视觉语言导航的三维地图</td>
<td width="110" nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/299">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://iccv.thecvf.com/virtual/2025/poster/1792">monoVLN: Bridging the Observation Gap between Monocular and Panoramic Vision and Language Navigation</a></td>
<td width="420">monoVLN 用三维高斯泼溅补全单目 RGBD 观测缺失区域，缩小单目机器人和全景 VLN 设置的观测差距。</td>
<td width="220">单目视觉语言导航</td>
<td width="240">单目 RGBD 机器人</td>
<td width="260">三维高斯泼溅隐式局部补全</td>
<td width="300">具身导航</td>
<td width="240">-</td>
<td width="360">让只有单目相机的机器人执行原本依赖全景观测的 VLN。</td>
<td width="110" nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/1792">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
</tbody>
</table>
