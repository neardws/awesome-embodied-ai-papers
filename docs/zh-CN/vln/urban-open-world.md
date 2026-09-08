# 城市与开放世界导航

[首页](../../../README.zh-CN.md) | [英文](../../en/vln/urban-open-world.md) | [方向目录](README.md)

共 20 篇。

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
<td width="320"><a href="https://openaccess.thecvf.com/content/CVPR2024/html/Khanna_GOAT-Bench_A_Benchmark_for_Multi-Modal_Lifelong_Navigation_CVPR_2024_paper.html">GOAT-Bench: A Benchmark for Multi-Modal Lifelong Navigation</a></td>
<td width="420">GOAT-Bench 评测具有多模态目标和开放式物体/地点目标的终身导航。</td>
<td width="220">终身导航基准</td>
<td width="240">开放世界室内场景</td>
<td width="260">目标条件记忆</td>
<td width="300">基准评测</td>
<td width="240">GOAT-Bench</td>
<td width="360">评测超越单次指令回合的多模态终身导航。</td>
<td width="110" nowrap><a href="https://openaccess.thecvf.com/content/CVPR2024/papers/Khanna_GOAT-Bench_A_Benchmark_for_Multi-Modal_Lifelong_Navigation_CVPR_2024_paper.pdf">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ECCV 2024</td>
<td width="320"><a href="https://arxiv.org/pdf/2407.14758">DISCO: Embodied Navigation and Interaction via Differentiable Scene-Conditioned Options</a></td>
<td width="420">DISCO 学习场景条件选项策略，用于开放环境中的具身导航与交互。</td>
<td width="220">导航 + 交互</td>
<td width="240">开放具身场景</td>
<td width="260">场景条件选项策略</td>
<td width="300">选项策略学习</td>
<td width="240">具身交互基准</td>
<td width="360">通过可复用的场景条件选项策略，连接导航与交互。</td>
<td width="110" nowrap><a href="https://arxiv.org/pdf/2407.14758">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=88RKxlFUNY">AutoFly: Vision-Language-Action Model for UAV Autonomous Navigation in the Wild</a></td>
<td width="420">AutoFly 是端到端无人机 VLA 模型，用伪深度编码和两阶段训练支持野外连续规划与避障。</td>
<td width="220">开放环境</td>
<td width="240">无人机/城市环境</td>
<td width="260">-</td>
<td width="300">两阶段 VLA 训练</td>
<td width="240">仿真 + 真实无人机</td>
<td width="360">从显式路线跟随转向粗粒度指令下的自主无人机导航。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2602.09657">论文</a></td>
<td width="110" nowrap><a href="https://xiaolousun.github.io/AutoFly/">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=OKm3w71ymP">OpenFly: A Comprehensive Platform for Aerial Vision-Language Navigation</a></td>
<td width="420">OpenFly 集成 UE、GTA V、Google Earth 和三维高斯泼溅，生成大规模空中视觉语言导航数据和平台。</td>
<td width="220">空中视觉语言导航平台/基准</td>
<td width="240">无人机/城市环境</td>
<td width="260">-</td>
<td width="300">开放世界导航</td>
<td width="240">基准</td>
<td width="360">降低无人机 VLN 数据采集成本并提供空中导航评测平台。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=OKm3w71ymP">论文</a></td>
<td width="110" nowrap><a href="https://shailab-ipec.github.io/openfly/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/Eziotic/OpenFly">代码</a></td>
<td width="240"><a href="https://shailab-ipec.github.io/openfly/">data</a></td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=qSak1Hjfdq">All-day Multi-scenes Lifelong Vision-and-Language Navigation with Tucker Adaptation</a></td>
<td width="420">TuKA 将多场景多时间导航知识表示为 Tucker 分解适配器，缓解全天多场景 VLN 中遗忘。</td>
<td width="220">终身视觉语言导航</td>
<td width="240">无人机/城市环境</td>
<td width="260">-</td>
<td width="300">Tucker 适配/参数高效微调</td>
<td width="240">-</td>
<td width="360">全天多场景持续适应</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=qSak1Hjfdq">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=PaYo96rjij">Lifelong Embodied Navigation Learning</a></td>
<td width="420">Uni-Walker 用 DE-LoRA 分离共享和任务特定导航知识，支持多任务序列持续学习。</td>
<td width="220">终身具身导航</td>
<td width="240">无人机/城市环境</td>
<td width="260">-</td>
<td width="300">DE-LoRA 持续学习</td>
<td width="240">-</td>
<td width="360">导航技能持续学习</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=PaYo96rjij">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=hzf23XSDcs">CitySeeker: How Do VLMs Explore Embodied Urban Navigation with Implicit Human Needs?</a></td>
<td width="420">CitySeeker 用 8 城市 6440 条轨迹评测视觉语言模型是否能把“我渴了”等隐式需求转成城市导航目标。</td>
<td width="220">城市隐式需求导航基准</td>
<td width="240">无人机/城市环境</td>
<td width="260">-</td>
<td width="300">开放世界导航</td>
<td width="240">基准</td>
<td width="360">评测视觉语言模型在城市环境中理解隐式人类需求并找目标地点的能力。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=hzf23XSDcs">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">CitySeeker：6,440 条轨迹/8 座城市</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38878">AerialVLA: A Vision-Language-Action Model for Aerial Navigation with Online Dialogue</a></td>
<td width="420">AerialVLA 面向无人机视觉对话导航，支持主动询问和利用历史地标纠正路线。</td>
<td width="220">空中视觉对话导航</td>
<td width="240">无人机</td>
<td width="260">-</td>
<td width="300">在线对话 VLA</td>
<td width="240">-</td>
<td width="360">让无人机通过在线对话到达目标并主动修正导航。</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38878">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38885">History-Enhanced Two-Stage Transformer for Aerial Vision-and-Language Navigation</a></td>
<td width="420">HETT 先用历史网格地图粗定位目标，再用细粒度视觉分析优化无人机动作。</td>
<td width="220">开放环境</td>
<td width="240">大规模城市无人机</td>
<td width="260">历史网格地图</td>
<td width="300">由粗到细的两阶段 Transformer</td>
<td width="240">-</td>
<td width="360">平衡空中视觉语言导航中全局环境推理和局部场景理解。</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38885">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38897">RENEW: Risk- and Energy-Aware Navigation in Dynamic Waterways</a></td>
<td width="420">RENEW 为动态水流扰动下的 ASV 规划风险和能耗感知路径，并加入自适应安全约束。</td>
<td width="220">自主水面艇全局路径规划</td>
<td width="240">动态水道</td>
<td width="260">-</td>
<td width="300">风险/能耗感知规划</td>
<td width="240">-</td>
<td width="360">水域导航而非 VLN</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38897">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38898">Towards Autonomous UAV Visual Object Search in City Space: Benchmark and Agentic Methodology</a></td>
<td width="420">CityAVOS 提供 2420 个城市无人机视觉目标搜索任务，并用 PRPSearcher 做感知-推理-规划搜索。</td>
<td width="220">无人机视觉物体搜索基准</td>
<td width="240">无人机/城市环境</td>
<td width="260">三维认知/不确定性/动态语义地图</td>
<td width="300">开放世界导航</td>
<td width="240">基准</td>
<td width="360">让无人机在城市空间中自主搜索静态目标物体。</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38898">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">CityAVOS：2,420 项任务</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38916">UrbanNav: Learning Language-Guided Embodied Urban Navigation from Web-Scale Human Trajectories</a></td>
<td width="420">UrbanNav 用网页级城市步行视频和语言轨迹对齐，训练智能体按自由语言在城市中导航。</td>
<td width="220">语言引导城市导航</td>
<td width="240">地面城市机器人</td>
<td width="260">-</td>
<td width="300">开放世界导航</td>
<td width="240">-</td>
<td width="360">支持最后一公里机器人在陌生城市街景中按自然语言导航。</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38916">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/CASIA-IVA-Lab/UrbanNav">代码</a></td>
<td width="240"><a href="https://huggingface.co/datasets/Vigar001/UrbanNav">Hugging Face</a></td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38917">Autonomous Vehicle Path Planning by Searching with Differentiable Simulation</a></td>
<td width="420">DSS 用可微 Waymax 模拟器作为状态预测器和评论家，通过梯度搜索自动驾驶动作序列。</td>
<td width="220">自动驾驶路径规划</td>
<td width="240">Waymax/交通场景</td>
<td width="260">-</td>
<td width="300">可微仿真搜索</td>
<td width="240">-</td>
<td width="360">自动驾驶规划而非 VLN</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38917">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38920">Real-Time Path Planning for UAVs in Windy Environments Without Computational Fluid Dynamics</a></td>
<td width="420">GZS 无需 CFD，用点云局部拓扑和物理启发风风险建模进行实时无人机路径规划。</td>
<td width="220">无人机实时路径规划</td>
<td width="240">有风、杂乱的三维环境</td>
<td width="260">-</td>
<td width="300">零样本免训练规划</td>
<td width="240">-</td>
<td width="360">在有风扰和障碍的三维环境中做机载实时无人机规划。</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38920">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38938">ReflexDiffusion: Reflection-Enhanced Trajectory Planning for High-lateral-acceleration Scenarios in Autonomous Driving</a></td>
<td width="420">ReflexDiffusion 在扩散轨迹规划推理阶段加入反思式梯度调整，处理高横向加速度长尾场景。</td>
<td width="220">自动驾驶轨迹规划</td>
<td width="240">高横向加速度驾驶</td>
<td width="260">-</td>
<td width="300">推理阶段扩散反思</td>
<td width="240">-</td>
<td width="360">自动驾驶规划而非开放 VLN</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38938">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38941">Learning from Human Gaze: Human-like Robot Social Navigation in Dense Crowds</a></td>
<td width="420">GazeNav/Gaze2Nav 用人类眼动数据预测社交注意对象，并把该注意注入拥挤人群运动规划。</td>
<td width="220">社会导航</td>
<td width="240">密集人群</td>
<td width="260">注视/语义注意力</td>
<td width="300">开放世界导航</td>
<td width="240">GazeNav 数据集</td>
<td width="360">让机器人在密集人群中进行更像人的社交导航。</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38941">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/63554">Plan in Sandbox, Navigate in Open Worlds: Learning Physics-Grounded Abstracted Experience for Embodied Navigation</a></td>
<td width="420">SAGE 让智能体在物理落地的语义抽象沙盒中学习，再迁移到开放世界导航。</td>
<td width="220">开放环境</td>
<td width="240">移动机器人/移动操作</td>
<td width="260">-</td>
<td width="300">以物理为依据的抽象经验/强化学习</td>
<td width="240">-</td>
<td width="360">用抽象物理经验减少对逼真仿真的依赖并提升开放世界导航。</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/63554">论文</a></td>
<td width="110" nowrap><a href="https://frankzxshen.github.io/SAGE">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2510.20685">C-NAV: Towards Self-Evolving Continual Object Navigation in Open World</a></td>
<td width="420">C-Nav 提出持续物体目标导航基准，并用双路径抗遗忘机制学习新物体类别同时保留旧知识。</td>
<td width="220">持续物体目标导航基准</td>
<td width="240">移动机器人/移动操作</td>
<td width="260">-</td>
<td width="300">双路径抗遗忘/强化学习</td>
<td width="240">-</td>
<td width="360">在动态开放世界中持续学习新目标类别的物体导航。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2510.20685">论文</a></td>
<td width="110" nowrap><a href="https://bigtree765.github.io/C-Nav-project/">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2512.10046">SimWorld-Robotics: Synthesizing Photorealistic and Dynamic Urban Environments for Multimodal Robot Navigation and Collaboration</a></td>
<td width="420">SimWorld-Robotics 用 UE5 程序化生成动态城市，提供多模态指令导航和多机器人搜索协作基准。</td>
<td width="220">城市仿真基准</td>
<td width="240">无人车/城市环境</td>
<td width="260">-</td>
<td width="300">开放世界导航</td>
<td width="240">仿真/基准</td>
<td width="360">构建大规模逼真城市仿真以评测机器人开放环境导航和协作。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2512.10046">论文</a></td>
<td width="110" nowrap><a href="https://scai.cs.jhu.edu/projects/SimWorldRobotics/">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2408.15503">RoboSense: Large-scale Dataset and Benchmark for Egocentric Robot Perception and Navigation in Crowded and Unstructured Environments</a></td>
<td width="420">RoboSense 提供相机、激光雷达、鱼眼等多传感器第一视角数据，评测拥挤非结构环境中的感知和导航。</td>
<td width="220">评测/数据</td>
<td width="240">拥挤/非结构化第一视角机器人环境</td>
<td width="260">-</td>
<td width="300">开放世界导航</td>
<td width="240">基准</td>
<td width="360">建立面向移动机器人近场感知与导航的数据集和基准。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2408.15503">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/suhaisheng/RoboSense">代码</a></td>
<td width="240"><a href="https://huggingface.co/datasets/suhaisheng0527/RoboSense">Hugging Face</a></td>
</tr>
</tbody>
</table>
