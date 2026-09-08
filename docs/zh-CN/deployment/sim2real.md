# 仿真到现实

[首页](../../../README.zh-CN.md) | [英文](../../en/deployment/sim2real.md) | [方向目录](README.md)

共 20 篇。

<table width="3090">
<thead>
<tr>
<th width="120" nowrap>会议/年份</th>
<th width="320">论文/方法</th>
<th width="420">摘要</th>
<th width="240">对象类型</th>
<th width="280">效率指标</th>
<th width="280">平台/硬件</th>
<th width="280">覆盖任务</th>
<th width="220">开放资源状态</th>
<th width="360">论文任务/目标</th>
<th width="110" nowrap>论文</th>
<th width="110" nowrap>项目</th>
<th width="110" nowrap>代码</th>
<th width="240">数据/基准</th>
</tr>
</thead>
<tbody>
<tr>
<td width="120" nowrap>CoRL 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2505.03233">GraspVLA: a Grasping Foundation Model Pre-trained on Billion-scale Synthetic Action Data</a></td>
<td width="420">在合成动作数据上预训练语言条件闭环抓取 VLA，并迁移到真实机器人。</td>
<td width="240">开放词汇平行夹爪抓取</td>
<td width="280">SynGrasp-1B：10M 轨迹/~1B 帧；实机均值 84.7%；模型 5 Hz；5K 合成轨迹即可适配新本体/视角</td>
<td width="280">主平台：Franka Panda + 原装二指夹爪（手指加长 2 cm），前置 D435 + 侧置 D415i；适配：UR5e + Robotiq 2F-85</td>
<td width="280">语言条件闭环抓取与本体/视角适配</td>
<td width="220"><a href="https://pku-epic.github.io/GraspVLA-web/">项目</a> / <a href="https://github.com/PKU-EPIC/GraspVLA">代码</a></td>
<td width="360">用十亿级合成动作监督降低真实抓取数据需求；实机总体/语言/任意/透明成功率 93.3/93.3/93.3/86.6%</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2505.03233">论文</a></td>
<td width="110" nowrap><a href="https://pku-epic.github.io/GraspVLA-web/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/PKU-EPIC/GraspVLA">代码</a></td>
<td width="240">SynGrasp-1B；CuRobo 规划 + MuJoCo 物理验证 + Isaac Sim 渲染；LIBERO 评测</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://openaccess.thecvf.com/content/CVPR2025/html/Wang_MobileH2R_Learning_Generalizable_Human_to_Mobile_Robot_Handover_Exclusively_from_CVPR_2025_paper.html">MobileH2R: Learning Generalizable Human to Mobile Robot Handover Exclusively from Scalable and Diverse Synthetic Data</a></td>
<td width="420">完全使用可扩展合成人体动作与四维模仿学习，训练移动机器人从人类手中接物。</td>
<td width="240">移动操作 / 人到机器人交接</td>
<td width="280">100K+ 合成示范；每设置 30 次实机评测，简单/复杂成功率 80.0/63.3%，基线为 40.0/30.0%</td>
<td width="280">Galbot G1 移动底盘 + 单侧左 7 自由度臂 + 夹爪</td>
<td width="280">全身接近与从人类手中接物</td>
<td width="220"><a href="https://mobileh2r.github.io/">项目</a></td>
<td width="360">在不采集真实交接示范的情况下覆盖大工作空间；该方法不是双臂操作。</td>
<td width="110" nowrap><a href="https://openaccess.thecvf.com/content/CVPR2025/html/Wang_MobileH2R_Learning_Generalizable_Human_to_Mobile_Robot_Handover_Exclusively_from_CVPR_2025_paper.html">论文</a></td>
<td width="110" nowrap><a href="https://mobileh2r.github.io/">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">MobileH2R-Sim（PyBullet + Ray）；8,836 个 ShapeNet 物体</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2018</td>
<td width="320"><a href="https://scholar.google.com/scholar?q=Sim-to-Real+Reinforcement+Learning+for+Deformable+Object+Manipulation">Sim-to-Real Reinforcement Learning for Deformable Object Manipulation</a></td>
<td width="420">该工作将强化学习从仿真迁移到可变形物体操作。</td>
<td width="240">仿真到现实</td>
<td width="280">部署/评测覆盖</td>
<td width="280">机器人/仿真器平台</td>
<td width="280">具身机器人任务</td>
<td width="220">来源列出的资源</td>
<td width="360">补充 CoRL 部署/评测研究覆盖。</td>
<td width="110" nowrap><a href="https://scholar.google.com/scholar?q=Sim-to-Real+Reinforcement+Learning+for+Deformable+Object+Manipulation">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=W3Q2xvrZtx">PD$^{2}$GS: Part-Level Decoupling and Continuous Deformation of Articulated Objects via Gaussian Splatting</a></td>
<td width="420">用部件级解耦和连续形变高斯表示建模关节物体。</td>
<td width="240">关节物体高斯泼溅</td>
<td width="280">仿真到现实</td>
<td width="280">仿真/评测环境</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">解决关节物体在真实/仿真中可变形建模的问题。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=W3Q2xvrZtx">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=sWyX1BpeN4">Manipulation as in Simulation: Enabling Accurate Geometry Perception in Robots</a></td>
<td width="420">让机器人获得接近仿真的准确几何感知以提升真实操作。</td>
<td width="240">面向操作的几何感知</td>
<td width="280">仿真到现实</td>
<td width="280">仿真/评测环境</td>
<td width="280">真实机器人操作</td>
<td width="220">-</td>
<td width="360">解决真实机器人几何感知噪声导致仿真到现实操作差距的问题。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=sWyX1BpeN4">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=nAO9LcV7nE">Emergent Dexterity Via Diverse Resets and Large-Scale Reinforcement Learning</a></td>
<td width="420">通过多样化复位和大规模强化学习训练涌现灵巧操作能力。</td>
<td width="240">灵巧操作强化学习</td>
<td width="280">仿真到现实</td>
<td width="280">仿真 + 可能使用机器人手</td>
<td width="280">灵巧操作</td>
<td width="220">-</td>
<td width="360">解决灵巧操作策略从仿真训练到复杂状态恢复的问题。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=nAO9LcV7nE">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=H4SyKHjd4c">Sim2Real VLA: Zero-Shot Generalization of Synthesized Skills to Realistic Manipulation</a></td>
<td width="420">将合成技能训练的 VLA 零样本迁移到真实感操作环境。</td>
<td width="240">仿真到现实 VLA</td>
<td width="280">仿真到现实</td>
<td width="280">仿真/评测环境</td>
<td width="280">逼真操作</td>
<td width="220">-</td>
<td width="360">解决合成技能到真实机器人操作的泛化问题。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=H4SyKHjd4c">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=TmYcqOnxhN">Exo-Plore: Exploring Exoskeleton Control Space through Human-aligned Simulation</a></td>
<td width="420">用人体对齐仿真探索外骨骼控制空间。</td>
<td width="240">外骨骼控制</td>
<td width="280">仿真到现实</td>
<td width="280">与人体对齐的仿真/外骨骼</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">解决外骨骼控制策略难以安全高效探索的问题。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=TmYcqOnxhN">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=yn9dzttHvT">Latent Adaptation of Foundation Policies for Sim-to-Real Transfer</a></td>
<td width="420">在潜变量空间适配基础策略以完成仿真到现实迁移。</td>
<td width="240">潜在策略适配</td>
<td width="280">仿真到现实</td>
<td width="280">仿真/评测环境</td>
<td width="280">仿真到现实策略迁移</td>
<td width="220">-</td>
<td width="360">解决基础机器人策略在真实域分布偏移下性能下降的问题。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=yn9dzttHvT">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=OutljIofvS">RobotArena ∞: Scalable Robot Benchmarking via Real-to-Sim Translation</a></td>
<td width="420">通过现实到仿真翻译扩展真实机器人场景的可评测基准。</td>
<td width="240">现实到仿真基准</td>
<td width="280">仿真到现实</td>
<td width="280">仿真/评测环境</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">解决真实机器人基准扩展成本高的问题。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=OutljIofvS">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=xlr3NqxUqY">Contact-guided Real2Sim from Monocular Video with Planar Scene Primitives</a></td>
<td width="420">用接触线索和平面场景基元从单目视频重建 real2sim 场景。</td>
<td width="240">接触引导的现实到仿真迁移</td>
<td width="280">仿真到现实</td>
<td width="280">单目视频</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">解决单目视频转仿真缺少物理接触约束的问题。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=xlr3NqxUqY">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/66662">FlatLab: A Unified Methodology Framework and Simulation-Based Benchmark for Robotic Manipulation of Flat Objects</a></td>
<td width="420">提供统一方法框架和仿真基准，用于操作不同几何和材质的扁平物体。</td>
<td width="240">基准/数据集</td>
<td width="280">仿真到现实</td>
<td width="280">仿真/评测环境</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/66662">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2602.20871">GeCo-SRT: Geometry-aware Continual Adaptation for Robotic Cross-Task Sim-to-Real Transfer</a></td>
<td width="420">用几何感知持续适配支持跨任务仿真到现实迁移。</td>
<td width="240">持续仿真到现实适配</td>
<td width="280">仿真到现实</td>
<td width="280">仿真/评测环境</td>
<td width="280">-</td>
<td width="220">项目</td>
<td width="360">解决机器人策略跨任务真实迁移中几何差异和连续适配问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2602.20871">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2509.19626">EgoBridge: Domain Adaptation for Generalizable Imitation from Egocentric Human Data</a></td>
<td width="420">将第一视角人类数据做域适配，用于可泛化机器人模仿学习。</td>
<td width="240">人类到机器人领域适配</td>
<td width="280">仿真到现实</td>
<td width="280">机器人部署/评测环境</td>
<td width="280">-</td>
<td width="220">项目</td>
<td width="360">解决第一视角人类数据到机器人策略的域差距问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2509.19626">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://openreview.net/forum?id=284GWLFtjU">DEAL: Diffusion Evolution Adversarial Learning for Sim-to-Real Transfer</a></td>
<td width="420">结合扩散进化和对抗学习调节仿真器，缩小强化学习控制器的仿真到现实差距。</td>
<td width="240">基准/数据集</td>
<td width="280">基准/数据集</td>
<td width="280">仿真/评测环境</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">缩小仿真到真实差距</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=284GWLFtjU">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2509.18631">Generalizable Domain Adaptation for Sim-and-Real Policy Co-Training</a></td>
<td width="420">用仿真与实机策略联合训练提升跨域泛化。</td>
<td width="240">领域适配 / 联合训练</td>
<td width="280">仿真到现实</td>
<td width="280">机器人部署/评测环境</td>
<td width="280">-</td>
<td width="220">项目</td>
<td width="360">解决仿真和真实数据联合训练时域偏移影响策略泛化的问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2509.18631">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2505.22634">LabUtopia: High-Fidelity Simulation and Hierarchical Benchmark for Scientific Embodied Agents</a></td>
<td width="420">提供科学实验室高保真仿真、场景生成和分层基准。</td>
<td width="240">基准/数据集</td>
<td width="280">仿真到现实</td>
<td width="280">LabSim</td>
<td width="280">30 项实验室任务 / 200+ 个资源</td>
<td width="220">项目</td>
<td width="360">解决科学具身智能体缺少复杂实验流程仿真和评测的问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2505.22634">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2507.01152">SonoGym: High Performance Simulation for Challenging Surgical Tasks with Robotic Ultrasound</a></td>
<td width="420">提供可并行的机器人超声手术仿真环境和任务。</td>
<td width="240">基准/数据集</td>
<td width="280">仿真到现实</td>
<td width="280">机器人超声</td>
<td width="280">-</td>
<td width="220">代码</td>
<td width="360">解决机器人超声导航/重建缺少真实高效仿真训练环境的问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2507.01152">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/SonoGym/SonoGym">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2506.22756">RoboPearls: Editable Video Simulation for Robot Manipulation</a></td>
<td width="420">用三维高斯泼溅从示教视频构建可编辑、照片级机器人操作仿真。</td>
<td width="240">基准/数据集</td>
<td width="280">可编辑视频仿真</td>
<td width="280">仿真/评测环境</td>
<td width="280">-</td>
<td width="220">项目</td>
<td width="360">解决真实示教采集贵和传统仿真仿真到现实差距大的问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2506.22756">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2409.02920">RoboTwin: Dual-Arm Robot Benchmark with Generative Digital Twins (early version)</a></td>
<td width="420">用生成式数字孪生创建双臂操作数据和真实对齐评测平台。</td>
<td width="240">基准/数据集</td>
<td width="280">基准/数据集</td>
<td width="280">双臂机器人 / COBOT Magic</td>
<td width="280">-</td>
<td width="220">项目+代码+数据/基准</td>
<td width="360">解决双臂操作数据稀缺和仿真评测不对齐真实的问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2409.02920">论文</a></td>
<td width="110" nowrap><a href="https://robotwin-benchmark.github.io/early-version/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/RoboTwin-Platform/RoboTwin">代码</a></td>
<td width="240"><a href="https://huggingface.co/datasets/TianxingChen/RoboTwin">Hugging Face</a></td>
</tr>
</tbody>
</table>
