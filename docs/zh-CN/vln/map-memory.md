# 地图与记忆

[首页](../../../README.zh-CN.md) | [英文](../../en/vln/map-memory.md) | [方向目录](README.md)

共 23 篇。

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
<td width="120" nowrap>CoRL 2024</td>
<td width="320"><a href="https://arxiv.org/abs/2407.07775">Mobility VLA: Multimodal Instruction Navigation with Long-Context VLMs and Topological Graphs</a></td>
<td width="420">Mobility VLA 将长上下文视觉语言模型与拓扑图结合，用于指令导航。</td>
<td width="220">视觉语言导航</td>
<td width="240">具身导航</td>
<td width="260">语言/空间上下文</td>
<td width="300">CoRL 导航方法</td>
<td width="240">VLN / 具身导航基准</td>
<td width="360">补充 CoRL 导航研究覆盖。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2407.07775">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ACL 2024</td>
<td width="320"><a href="https://aclanthology.org/2024.acl-long.529/">MapGPT: Map-Guided Prompting for Unified Vision-and-Language Navigation</a></td>
<td width="420">MapGPT 通过地图引导的提示，将语言指令与空间导航决策联系起来。</td>
<td width="220">视觉语言导航</td>
<td width="240">室内视觉语言导航</td>
<td width="260">地图引导的提示记忆</td>
<td width="300">大语言模型提示 + 导航</td>
<td width="240">视觉语言导航基准</td>
<td width="360">利用显式地图为空间中的大语言模型导航决策提供依据。</td>
<td width="110" nowrap><a href="https://aclanthology.org/2024.acl-long.529.pdf">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2024</td>
<td width="320"><a href="https://openaccess.thecvf.com/content/CVPR2024/html/Zhao_OVER-NAV_Elevating_Iterative_Vision-and-Language_Navigation_with_Open-Vocabulary_Detection_and_StructurEd_CVPR_2024_paper.html">OVER-NAV: Elevating Iterative Vision-and-Language Navigation with Open-Vocabulary Detection and Structured Representation</a></td>
<td width="420">OVER-NAV 将开放词汇检测与结构化场景记忆结合，用于迭代式视觉语言导航。</td>
<td width="220">视觉语言导航</td>
<td width="240">室内视觉语言导航</td>
<td width="260">开放词汇结构化记忆</td>
<td width="300">迭代导航规划</td>
<td width="240">视觉语言导航基准</td>
<td width="360">利用开放词汇物体与场景结构，增强视觉语言导航的空间落地能力。</td>
<td width="110" nowrap><a href="https://openaccess.thecvf.com/content/CVPR2024/papers/Zhao_OVER-NAV_Elevating_Iterative_Vision-and-Language_Navigation_with_Open-Vocabulary_Detection_and_StructurEd_CVPR_2024_paper.pdf">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2024</td>
<td width="320"><a href="https://arxiv.org/abs/2403.14158">Volumetric Environment Representation for Vision-Language Navigation</a></td>
<td width="420">VER 构建体积场景表示，改善视觉语言导航的空间记忆与落地能力。</td>
<td width="220">视觉语言导航</td>
<td width="240">三维室内导航</td>
<td width="260">体积地图记忆</td>
<td width="300">三维表示学习</td>
<td width="240">视觉语言导航基准</td>
<td width="360">以体积表示可导航空间，支持语言引导导航。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2403.14158">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>IROS 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2606.25497">SAGE-Nav: Leveraging LLM Planning and Alignment Fusion for Hierarchical Scene Graph-Guided Navigation</a></td>
<td width="420">SAGE-Nav 结合大语言模型高层规划和层级场景图，引导物体目标导航。</td>
<td width="220">物体目标导航</td>
<td width="240">室内导航</td>
<td width="260">层级场景图</td>
<td width="300">大语言模型规划 + 对齐融合</td>
<td width="240">基准</td>
<td width="360">用场景图记忆把语言规划落到目标导航。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2606.25497">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>IROS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2503.02247">WMNav: Integrating Vision-Language Models into World Models for Object Goal Navigation</a></td>
<td width="420">WMNav 将视觉语言模型接入导航世界模型，预测未来状态并维护导航记忆以提升目标搜索。</td>
<td width="220">物体目标导航</td>
<td width="240">室内导航</td>
<td width="260">世界模型记忆</td>
<td width="300">视觉语言模型引导的世界模型</td>
<td width="240">基准</td>
<td width="360">用世界模型想象和反馈支持物体目标导航。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2503.02247">论文</a></td>
<td width="110" nowrap><a href="https://b0b8k1ng.github.io/WMNav/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/B0B8K1ng/WMNavigation">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=HB6KvsqcAn">Towards Physically Executable 3D Gaussian for Embodied Navigation</a></td>
<td width="420">SAGE-3D 将三维高斯泼溅升级为带对象语义和物理可执行性的导航环境表示。</td>
<td width="220">地图/记忆</td>
<td width="240">移动机器人/移动操作</td>
<td width="260">语义与物理对齐的三维高斯</td>
<td width="300">三维高斯泼溅环境构建</td>
<td width="240">-</td>
<td width="360">三维高斯泼溅可执行导航环境</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=HB6KvsqcAn">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=LPv59noPAy">Uncertainty-Aware Gaussian Map for Vision-Language Navigation</a></td>
<td width="420">该文构建语义 高斯地图 并显式编码几何、语义和外观不确定性以指导 VLN 动作。</td>
<td width="220">地图/记忆</td>
<td width="240">移动机器人/移动操作</td>
<td width="260">不确定性感知语义高斯地图</td>
<td width="300">利用不确定性信息的策略</td>
<td width="240">-</td>
<td width="360">在 VLN 决策中利用感知不确定性而不是忽略模糊观测。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=LPv59noPAy">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=RnuB0Nlbd5">JanusVLN: Decoupling Semantics and Spatiality with Dual Implicit Memory for Vision-Language Navigation</a></td>
<td width="420">JanusVLN 用双隐式记忆分别建模语义和空间信息，减少显式文本/帧记忆的冗余和空间损失。</td>
<td width="220">地图/记忆</td>
<td width="240">移动机器人/移动操作</td>
<td width="260">地图/记忆</td>
<td width="300">双重隐式神经记忆；键值缓存增量更新</td>
<td width="240">视觉语言导航基准</td>
<td width="360">解决基于多模态大语言模型的视觉语言导航中显式记忆膨胀和空间信息损失。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=RnuB0Nlbd5">论文</a></td>
<td width="110" nowrap><a href="https://miv-xjtu.github.io/JanusVLN.github.io/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/MIV-XJTU/JanusVLN">代码</a></td>
<td width="240"><a href="https://miv-xjtu.github.io/JanusVLN.github.io/">data</a></td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=li1vfqDzRD">Emergence of Spatial Representation in an Actor-Critic Agent with Hippocampus-Inspired Sequence Generator</a></td>
<td width="420">该文用海马体启发的序列生成器作为时间记忆缓冲，解释演员—评论家导航智能体中空间表征涌现。</td>
<td width="220">神经启发视觉导航/强化学习</td>
<td width="240">移动机器人/移动操作</td>
<td width="260">受海马体启发的时间序列记忆</td>
<td width="300">演员—评论家强化学习</td>
<td width="240">-</td>
<td width="360">研究连续迷宫视觉导航中空间表征如何由序列记忆机制产生。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=li1vfqDzRD">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=KcC5mwfGf0">GRL-SNAM: Geometric Reinforcement Learning with Differential Hamiltonians for Navigation and Mapping in Unknown Environments</a></td>
<td width="420">GRL-SNAM 用局部感知构造 Hamiltonian 能量景观，在未知环境中联合导航与映射而不建全局地图。</td>
<td width="220">同步导航与建图</td>
<td width="240">移动机器人/移动操作</td>
<td width="260">局部能量景观/无全局地图</td>
<td width="300">几何强化学习</td>
<td width="240">-</td>
<td width="360">做未知环境中的同步导航与映射。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=KcC5mwfGf0">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38884">RflyPano: A Panoramic Benchmark for Ultra-low Altitude UAV Localization Powered by RflySim</a></td>
<td width="420">RflyPano 是面向 120 米以下无人机视觉定位的全景数据集，基于 RflySim 四鱼眼相机生成。</td>
<td width="220">无人机定位基准</td>
<td width="240">超低空无人机 / RflySim 仿真</td>
<td width="260">评测/数据而非地图记忆</td>
<td width="300">定位</td>
<td width="240">基准</td>
<td width="360">提供低空无人机 GNSS 不可靠场景下的全景视觉定位基准。</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38884">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/DUNDAI1998/RflyPano">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38887">MHED-SLAM: Multi-Scale Hybrid Encoding-Based Decoupled SLAM</a></td>
<td width="420">MHED-SLAM 用多尺度混合编码和解耦几何/颜色建模提升 NeRF-SLAM 的建图和跟踪质量。</td>
<td width="220">同步定位与建图</td>
<td width="240">移动机器人/移动操作</td>
<td width="260">神经场景表示</td>
<td width="300">NeRF/TSDF 同步定位与建图</td>
<td width="240">-</td>
<td width="360">视觉同步定位与建图建图定位</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38887">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38893">LOG-Nav: Efficient Layout-Aware Object-Goal Navigation with Hierarchical Planning</a></td>
<td width="420">LOG-Nav 用全局拓扑布局地图和局部场景记忆进行层级规划，提升多房间 ObjectNav 效率。</td>
<td width="220">ObjectNav</td>
<td width="240">移动机器人/移动操作</td>
<td width="260">拓扑布局地图 + 局部场景记忆</td>
<td width="300">大语言模型层级规划/无高成本训练</td>
<td width="240">-</td>
<td width="360">让大语言模型智能体在复杂室内多房间环境中高效找物体。</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38893">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38899">PanoNav: Mapless Zero-Shot Object Navigation with Panoramic Scene Parsing and Dynamic Memory</a></td>
<td width="420">PanoNav 用仅 RGB 输入全景场景解析和动态记忆实现无地图零样本 ObjectNav。</td>
<td width="220">零样本物体目标导航</td>
<td width="240">移动机器人/移动操作</td>
<td width="260">动态记忆/无地图、仅 RGB 输入</td>
<td width="300">多模态大语言模型推理</td>
<td width="240">-</td>
<td width="360">在无深度、无预建图条件下进行零样本物体导航。</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38899">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38901">Lightweight Adaptive Topological Layout and Semantic Mapping in Vision-and-Language Navigation on Websites</a></td>
<td width="420">ATLAS 为网站 VLN 构建轻量自适应拓扑布局与语义图，提升网页导航准确率和推理速度。</td>
<td width="220">地图/记忆</td>
<td width="240">网页导航，不是物理机器人</td>
<td width="260">自适应拓扑布局 + 语义地图</td>
<td width="300">大语言模型网页导航</td>
<td width="240">-</td>
<td width="360">解决网页智能体在开放动态网页结构中的导航和问答。</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38901">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38929">Expand Your SCOPE: Semantic Cognition over Potential-Based Exploration for Embodied Visual Navigation</a></td>
<td width="420">SCOPE 用前沿边界和潜势探索建模局部观测与导航目标关系，做零样本视觉导航。</td>
<td width="220">零样本具身视觉导航</td>
<td width="240">移动机器人/移动操作</td>
<td width="260">基于前沿/势函数的语义记忆</td>
<td width="300">零样本框架</td>
<td width="240">-</td>
<td width="360">提升未知环境中目标导向探索的长程规划。</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38929">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38948">Agent Journey Beyond RGB: Hierarchical Semantic-Spatial Representation Enrichment for Vision-and-Language Navigation</a></td>
<td width="420">SUSA 用层级语义理解和空间感知融合非 RGB 表征，增强 VLN 中语义-空间落地。</td>
<td width="220">地图/记忆</td>
<td width="240">移动机器人/移动操作</td>
<td width="260">层级语义空间表示</td>
<td width="300">表示增强</td>
<td width="240">-</td>
<td width="360">解决第一视角视觉语言导航对多模态环境表示利用不足的问题。</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38948">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/64902">MapDream: Task-Driven Map Learning for Vision-Language Navigation</a></td>
<td width="420">MapDream 将地图构建视为任务驱动的 BEV 图像自回归生成，而非手工重建地图。</td>
<td width="220">地图/记忆</td>
<td width="240">移动机器人/移动操作</td>
<td width="260">学习得到的任务驱动鸟瞰图</td>
<td width="300">地图闭环中的自回归鸟瞰图合成</td>
<td width="240">-</td>
<td width="360">学习直接服务导航目标的地图表示。</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/64902">论文</a></td>
<td width="110" nowrap><a href="https://horizonrobotics.github.io/robot_lab/mapdream/">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2605.01736">GLMap: Multi-Scale Gaussian-Language Map for Zero-shot Embodied Navigation and Reasoning</a></td>
<td width="420">GLMap 用多尺度语义单元同时保存自然语言描述和三维高斯，实现零样本导航与推理。</td>
<td width="220">地图/记忆</td>
<td width="240">移动机器人/移动操作</td>
<td width="260">多尺度高斯语言地图</td>
<td width="300">零样本导航/推理</td>
<td width="240">-</td>
<td width="360">给大模型提供几何显式、语义多尺度的三维地图接口。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2605.01736">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/sx-zhang/GLMap">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2510.18546">EfficientNav: Towards On-Device Object-Goal Navigation with Navigation Map Caching and Retrieval</a></td>
<td width="420">EfficientNav 用导航地图缓存与检索降低本地小大语言模型做 ObjectNav 时的长提示和延迟。</td>
<td width="220">端侧物体目标导航</td>
<td width="240">移动机器人/移动操作</td>
<td width="260">导航地图缓存/检索</td>
<td width="300">小型大语言模型规划</td>
<td width="240">-</td>
<td width="360">在端侧设备上高效执行零样本 ObjectNav。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2510.18546">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/PKU-SEC-Lab/EfficientNav">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2507.04047">Move to Understand a 3D Scene: Bridging Visual Grounding and Exploration for Efficient and Versatile Embodied Navigation</a></td>
<td width="420">MTU3D 将主动探索和三维视觉语言落地结合，让智能体通过移动补全场景理解。</td>
<td width="220">主动三维场景理解/导航</td>
<td width="240">移动机器人/移动操作</td>
<td width="260">三维视觉语言主动感知</td>
<td width="300">三维表示</td>
<td width="240">-</td>
<td width="360">决定去哪里看以提升三维场景落地和导航效率。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2507.04047">论文</a></td>
<td width="110" nowrap><a href="https://mtu3d.github.io/">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://iccv.thecvf.com/virtual/2025/poster/944">NavQ: Learning a Q-Model for Foresighted Vision-and-Language Navigation</a></td>
<td width="420">NavQ 用大规模无标注轨迹训练 Q 模型，为候选动作估计未来可见信息以做前瞻决策。</td>
<td width="220">地图/记忆</td>
<td width="240">移动机器人/移动操作</td>
<td width="260">从轨迹数据学习具有前瞻性的 Q 特征</td>
<td width="300">基于无标签轨迹的 Q 学习</td>
<td width="240">-</td>
<td width="360">前瞻 VLN 决策</td>
<td width="110" nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/944">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
</tbody>
</table>
