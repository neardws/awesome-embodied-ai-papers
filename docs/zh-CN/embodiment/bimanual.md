# 双臂操作

[首页](../../../README.zh-CN.md) | [英文](../../en/embodiment/bimanual.md) | [方向目录](README.md)

共 12 篇。逐篇核查后，DexH2R 已移入灵巧手：机器人接收端实际是单 UR10e + ShadowHand；MobileH2R 已移入仿真到现实：它控制移动底盘与单侧左臂，并非双机器人臂；SARM 则从灵巧手移入本表，因为其平台是双 YAM + 平行夹爪系统。

下表用方向特有字段区分具体双臂本体、臂间耦合、动作接口、仿真/数据角色与协调证据。“未披露”表示论文没有给出具体型号、引擎、频率或指标，不会根据相邻基准反推。

<table width="3040">
<thead>
<tr>
<th width="100" nowrap>会议/年份</th>
<th width="270">论文/方法</th>
<th width="260">解决问题/目标</th>
<th width="300">具体本体/末端</th>
<th width="180">传感/接触</th>
<th width="300">双臂耦合/任务分工</th>
<th width="200">控制/动作接口</th>
<th width="200">训练方法</th>
<th width="360">仿真/训练环境 + 数据规模</th>
<th width="110">仿真/实机角色</th>
<th width="330">协调/泛化指标</th>
<th width="250">证据边界</th>
<th width="180">资源</th>
</tr>
</thead>
<tbody>
<tr>
<td width="100" nowrap>ICLR 2025</td>
<td width="270"><a href="https://openreview.net/forum?id=yAzN4tz7oI">RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation</a></td>
<td width="260">在异构机器人数据上扩展语言条件双臂扩散策略，再用少量目标示范适配。</td>
<td width="300">AgileX Cobot Mobile ALOHA；双 6 自由度臂 + 两只 0–80 mm 平行夹爪。移动底盘只承载平台，不由策略控制。</td>
<td width="180">前视 RGB + 两个腕部 RGB 相机；双臂/夹爪本体状态；未报告触觉。</td>
<td width="300">单一扩散策略联合预测两臂与夹爪动作块；无固定主从臂。任务包含交接、折叠和指定左右手倒水。</td>
<td width="200">双 6 自由度臂与两夹爪的关节位置动作块。</td>
<td width="200">多本体扩散预训练，再在目标 ALOHA 上微调。</td>
<td width="360">没有统一仿真器。预训练含 46 个数据集、&gt;1M 轨迹、21 TB；目标 ALOHA 微调覆盖 300+ 任务、6K+ 轨迹、3M+ 帧。</td>
<td width="110">目标实机；预训练来源混合；不是仿真到现实管线</td>
<td width="330">综合评测 68.2%；交接 40%、折叠短裤 68%、机器狗 76%；两种指定手倒水设置总成功率 100%/87.5%。</td>
<td width="250">目标评测仅实机，多项长程任务仍低于 70%；移动底盘不在学习动作空间内。</td>
<td width="180"><a href="https://openreview.net/forum?id=yAzN4tz7oI">OpenReview</a> / <a href="https://arxiv.org/abs/2410.07864">arXiv</a></td>
</tr>
<tr>
<td width="100" nowrap>ICRA 2025</td>
<td width="270"><a href="https://dexmimicgen.github.io/">DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning</a></td>
<td width="260">从少量种子示范生成大规模双臂模仿数据，同时保持并行、协调和顺序约束。</td>
<td width="300">仿真：双 Franka Panda + 平行夹爪、双 Franka + 未命名灵巧手、Fourier GR-1 + 未命名灵巧手。实机：Fourier GR1 + 双 Inspire 6 自由度手。</td>
<td width="180">仿真状态/视觉；实机头部/外置 RealSense D435i RGB-D + 机器人状态。</td>
<td width="300">左右臂子任务队列编码并行执行、共享物体变换与同步完成，或显式顺序约束。</td>
<td width="200">以物体为中心变换生成双臂示范，再训练模仿策略。</td>
<td width="200">种子示范切分 + MimicGen 式自动生成 + 模仿学习。</td>
<td width="360">robosuite + MuJoCo：9 任务、60 条种子、每任务生成 1,000 条（主实验 9K；全文报告 21K）。BiGym：3×1,000。实机分罐：4 条种子 → 40 条成功数字孪生示范。</td>
<td width="110">以仿真为主；一个任务走现实到仿真再到现实</td>
<td width="330">仿真成功率：零件装配 80.7%、穿线 69.3%、搬运 83.3%、托盘举升 88.7%、罐体分类 97.3%。实机分罐 20 次：生成数据 90%，仅四条种子 0%。</td>
<td width="250">实机只验证一个任务；仿真灵巧手型号未命名。</td>
<td width="180"><a href="https://dexmimicgen.github.io/">论文/项目</a> / <a href="https://github.com/NVlabs/dexmimicgen/">代码</a></td>
</tr>
<tr>
<td width="100" nowrap>ICLR 2026</td>
<td width="270"><a href="https://openreview.net/forum?id=jG9W6nAwVz">TwinVLA: Data-Efficient Bimanual Manipulation with Twin Single-Arm Vision-Language-Action Models</a></td>
<td width="260">在缺少大规模双臂数据时复用单臂 VLA 预训练。</td>
<td width="300">实机自研 Anubis：双 6 自由度臂 + ALOHA 式透明平行夹爪；三轮底盘未使用。Tabletop-Sim 使用 ALOHA2 资产。</td>
<td width="180">共享第一视角 RGB；两腕各一台 RealSense D405；每臂本体状态。</td>
<td width="300">两个臂专属分支共享语言/第一视角输入；联合注意力交换跨臂词元，层级混合专家分别输出左右动作块。</td>
<td width="200">两个协调 VLA 分支分别产生左右臂动作块。</td>
<td width="200">复制 SingleVLA 权重，再以每目标任务 50 条双臂回合微调。</td>
<td width="360">SingleVLA：约 0.5M OXE 示范/~800 h。RoboTwin 2.0/SAPIEN：50 任务×50 条。Tabletop-Sim/dm_control：5×50。实机：每任务 50 条。</td>
<td width="110">预训练 + 独立仿真/实机评测；不是仿真到现实</td>
<td width="330">实机五任务均值 71.0%；RoboTwin 简单/困难 42.0/8.9%；Tabletop-Sim 简单/困难 75.8/42.9%。去掉联合注意力，实机下降 27.0 个百分点。</td>
<td width="250">没有双臂预训练；困难划分成功率低，每个目标任务仍需 50 条示范。</td>
<td width="180"><a href="https://openreview.net/forum?id=jG9W6nAwVz">论文</a> / <a href="https://jellyho.github.io/TwinVLA/">项目</a></td>
</tr>
<tr>
<td width="100" nowrap>ICLR 2026</td>
<td width="270"><a href="https://openreview.net/forum?id=he86smZzRk">VLBiMan: Vision-Language Anchored One-Shot Demonstration Enables Generalizable Bimanual Robotic Manipulation</a></td>
<td width="260">用一条拖动示范学习双臂技能，并泛化到物体、场景和动态干扰变化。</td>
<td width="300">主平台：双 Aubo-i5 6 自由度臂 + DH-Robotics 80 mm 平行夹爪。迁移平台：双 Rokae xMate CR73 + Jodell RG75-3004 75 mm 夹爪。</td>
<td width="180">Kingfisher R-6000 第三视角双目；无腕部相机、力或触觉传感器。</td>
<td width="300">分解每臂原子技能与臂间依赖；结合视觉语言模型锚点、IK 和碰撞约束，支持同步/异步执行。</td>
<td width="200">稀疏 6 自由度末端位姿路点 + 二值夹爪状态，通过 IK/控制接口回放；相机与状态记录为 10 Hz，执行频率未披露。</td>
<td width="200">每任务一条动觉种子 + 视觉语言模型落地 + 约束轨迹组合；不训练任务策略。</td>
<td width="360">无仿真器或策略训练集。主平台 10 任务，每任务一条种子，每设置 25 次；迁移平台 4 任务，每设置 20 次。</td>
<td width="110">仅实机</td>
<td width="330">主平台六任务：无干扰同物/新物 85.3/78.0%，有干扰 69.3/59.3%；跨本体 83.8/76.3% 与 70.0/58.8%。最大同步化缩短约 22% 执行时间。</td>
<td width="250">初始抓取执行占失败 45%，双臂协调占 21%；每任务证据仍只有一条种子。</td>
<td width="180"><a href="https://openreview.net/forum?id=he86smZzRk">论文</a></td>
</tr>
<tr>
<td width="100" nowrap>ICLR 2026</td>
<td width="270"><a href="https://openreview.net/forum?id=aemqAxScl9">SARM: Stage-Aware Reward Modeling for Long Horizon Robot Manipulation</a></td>
<td width="260">学习阶段感知奖励，对长时程双臂任务的示范进行筛选与重加权。</td>
<td width="300">双 YAM 机械臂 + 平行夹爪。正文称每臂 7 自由度，附录 A.2 与厂商规格称 6 自由度；夹爪型号未披露。</td>
<td width="180">顶部 + 两个腕部 RealSense D405；关节状态/动作；无触觉。</td>
<td width="300">联合双臂策略执行折衣与洗碗机卸载/交接；阶段标签建模进度，但未定义固定主从臂。</td>
<td width="200">双臂关节角命令；示范以 30 fps 记录；策略控制频率未披露。</td>
<td width="200">阶段感知奖励建模 + 基于 GELLO 示范的奖励感知行为克隆/筛选。</td>
<td width="360">主实验仅实机：共 200 h T 恤折叠数据，另用 20 h 子集；奖励模型使用 200 条稠密 + 500 条稀疏轨迹。MuJoCo/300 条示范只属于附录独立 DiffQL 抓取放置实验。</td>
<td width="110">主实验仅实机</td>
<td width="330">奖励示范均方误差 0.009，轨迹展开 Spearman ρ=0.94。RA-BC 折衣：简单 12/12、中等 10/12（83%）、困难 8/12（67%）；ReWiND 在中等/困难为 50%/25%。</td>
<td width="250">论文对机械臂自由度表述冲突；主长程系统没有仿真迁移，也不是灵巧手。</td>
<td width="180"><a href="https://openreview.net/forum?id=aemqAxScl9">论文</a> / <a href="https://qianzhong-chen.github.io/sarm.github.io/">项目</a> / <a href="https://github.com/xdofai/opensarm">代码</a></td>
</tr>
<tr>
<td width="100" nowrap>AAAI 2026</td>
<td width="270"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38926">LatentVLA: Taming Latent Space for Generalizable and Long-Horizon Bimanual Manipulation</a></td>
<td width="260">组织连续 VLA 潜动作空间，以支持长程双臂规划与泛化。</td>
<td width="300">论文未披露机器人、机械臂或末端品牌/型号；只明确 14-D 双臂本体状态/动作接口。</td>
<td width="180">语言 + 视觉 + 14-D 本体状态；相机和接触传感器型号未披露。</td>
<td width="300">TA-LAM 学习联合语言/动作潜空间，LADT 规划长动作序列；没有显式固定左右臂分工。</td>
<td width="200">专家头把联合潜计划解码为 14-D 双臂动作序列。</td>
<td width="200">多源潜空间预训练，再进行八任务双臂微调。</td>
<td width="360">52 个来源、&gt;2.5M 序列；AgiBot World Beta + LatentVLA-Dexterous 约 0.5M。八个实机任务新增 1,600 h。仿真评测：RoboTwin 1.0、SIMPLER、CALVIN；引擎/版本未披露。</td>
<td width="110">混合预训练；仿真 + 实机评测；不是单一仿真到现实管线</td>
<td width="330">实机八任务均值 63.8%，分布外 56%，20 条示范的少样本设置 61%；SIMPLER 65.7%；CALVIN 平均长度 3.52；RoboTwin 各任务 33.7–98.3%。</td>
<td width="250">实物硬件与基准引擎版本未披露；跨基准指标不能直接横比。</td>
<td width="180"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38926">文章</a> / <a href="https://ojs.aaai.org/index.php/AAAI/article/download/38926/42888">PDF</a></td>
</tr>
<tr>
<td width="100" nowrap>ICML 2026</td>
<td width="270"><a href="https://icml.cc/virtual/2026/poster/63277">DexMachina: Functional Retargeting for Bimanual Dexterous Manipulation</a></td>
<td width="260">在不同灵巧手形态间重定向人类双手操作，同时保持任务功能效果。</td>
<td width="300">两只浮动灵巧手，每只增加 6 自由度腕；核心实验使用 Inspire、Allegro、ROBOTERA XHand、SCHUNK 五指。没有机器人臂或实体硬件。</td>
<td width="180">特权物体状态、关节目标、指—物距离和接触力。</td>
<td width="300">单个基于状态的 PPO 策略联合控制双手；动作/接触奖励诱导任务相关分工，不做显式左右策略拆分。</td>
<td width="200">重定向腕部基座动作 + 策略残差腕/指动作。</td>
<td width="200">PPO + 任务/运动/接触奖励 + 逐步衰减的虚拟物体控制器课程。</td>
<td width="360">Genesis；ARCTIC 提供 5 个铰接物与 7 条人类双手片段（每任务一条）。通常 12K 并行环境、5 个随机种子、每检查点 20 个评测回合。</td>
<td width="110">仅仿真</td>
<td width="330">论文“成功”实际是铰接部件 ADD-AUC：Allegro 长程任务 83.0/81.1/87.1/75.4%；XHand 72.4/66.2/89.0/80.3%。</td>
<td width="250">无实机/仿真到现实；URDF 惯量与碰撞质量会影响迁移，ADD-AUC 也不是二值任务成功率。</td>
<td width="180"><a href="https://icml.cc/virtual/2026/poster/63277">ICML</a> / <a href="https://arxiv.org/abs/2505.24853">论文</a> / <a href="https://project-dexmachina.github.io/">项目</a></td>
</tr>
<tr>
<td width="100" nowrap>ICML 2026</td>
<td width="270"><a href="https://icml.cc/virtual/2026/poster/66358">DECO: Decoupled Multimodal Diffusion Transformer for Bimanual Dexterous Manipulation with a Plugin Tactile Adapter</a></td>
<td width="260">无需重训视觉—动作主干，为双臂人形扩散策略加入触觉反馈。</td>
<td width="300">Unitree H1-2 上半身：双臂共 14 自由度 + 双 Inspire RH56DFTP 手（每手 6 自由度）；自研主动双目头增加偏航/俯仰。</td>
<td width="180">双目视觉；每手 17 个触觉垫、两手共 1,062 个接触点，数值范围 0–4096。</td>
<td width="300">单一 28 关节动作块策略；按任务形成持盘/取放、持物/开盖或插头/插座同步对齐等分工，而非两套独立策略。</td>
<td width="200">28 个臂/手/头部关节动作；数据 30 Hz；动作块 32、执行块 16。</td>
<td width="200">解耦多模态扩散 Transformer + 触觉交叉注意力 LoRA 适配器。</td>
<td width="360">无仿真器。DECO-50 实机遥操作：4 场景、28 子任务、8,021 条成功轨迹、约 48.704 成功小时、约 5M 帧；实机轨迹展开 &gt;2,000。</td>
<td width="110">仅实机</td>
<td width="330">仅视觉均值 72.25%；触觉 DECO.p 82.50%（+10.25 个百分点）。接触密集 垃圾处理 + 装配 从 53.13% 升至 73.13%（+20 个百分点）；装配 总计 55/80。</td>
<td width="250">躯干与下身不由策略控制；只覆盖四类场景。正文 表 4 印为 55/100，但 表 1 与附录 表 14 支持 55/80。</td>
<td width="180"><a href="https://icml.cc/virtual/2026/poster/66358">ICML</a> / <a href="https://arxiv.org/abs/2602.05513">论文</a> / <a href="https://huggingface.co/datasets/BAAI-Humanoid/DECO-50">数据</a></td>
</tr>
<tr>
<td width="100" nowrap>ICML 2026</td>
<td width="270"><a href="https://icml.cc/virtual/2026/poster/62192">RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation</a></td>
<td width="260">跨任务与本体扩展双臂专家数据，并在强域随机化下评估策略鲁棒性。</td>
<td width="300">仿真配对：Aloha-AgileX、ARX-X5、Piper、Franka-Panda、UR5-WSG；只有 Panda/WSG 夹爪映射明确。实机：COBOT-Magic 双臂，夹爪型号未披露。</td>
<td width="180">基准使用视觉/状态观测；未报告统一触觉传感器。</td>
<td width="300">以物体为中心的技能接口标记左右臂，支持顺序交接、同步/并行执行和异构组合；无固定主臂。</td>
<td width="200">专家技能程序生成数据；基准评测 ACT/DP/DP3/RDT/π0 类学习策略。</td>
<td width="200">域随机化专家生成、鲁棒性预训练与策略基准评测。</td>
<td width="360">SAPIEN 3.0.0b1；50 任务、5 种本体、731 物体/147 类、&gt;100K 轨迹。标准基准每任务 50 条；鲁棒性 32×300；实机每任务 10 条 + 1K 随机化仿真。</td>
<td width="110">仿真 + 实机 + 基准</td>
<td width="330">自动采集均值 60.5%（基线 52.2%）。基准简单/困难：π0 46.4/16.3%，DP3 55.2/5.0%。合成增强令四个实机设置提升 13.5–33.0 个百分点（均值 24.4）。</td>
<td width="250">若干仿真夹爪映射和实机夹爪未披露；没有独立碰撞率、人工干预或协调率指标。</td>
<td width="180"><a href="https://arxiv.org/abs/2506.18088">论文</a> / <a href="https://robotwin-platform.github.io/">项目</a> / <a href="https://github.com/RoboTwin-Platform/RoboTwin">代码</a> / <a href="https://huggingface.co/datasets/TianxingChen/RoboTwin2.0">数据</a></td>
</tr>
<tr>
<td width="100" nowrap>ICCV 2025</td>
<td width="270"><a href="https://openaccess.thecvf.com/content/ICCV2025/html/Jiang_Rethinking_Bimanual_Robotic_Manipulation_Learning_with_Decoupled_Interaction_Framework_ICCV_2025_paper.html">Rethinking Bimanual Robotic Manipulation: Learning with Decoupled Interaction Framework</a></td>
<td width="260">避免在可独立学习的任务或阶段强制进行全量臂间耦合。</td>
<td width="300">仿真：RoboTwin 双臂本体，论文未命名机器人/夹爪。实机：AgileX Cobot Magic 双臂，夹爪型号未披露。</td>
<td width="180">单第三视角 RealSense L515 点云 + 每臂机器人状态；无触觉。</td>
<td width="300">每臂独立策略交换对侧状态特征；选择性交互模块预测尺度/偏置，随任务阶段调整耦合强度。</td>
<td width="200">每臂输入本臂点云 + 7-D 状态，并预测 7-D 动作。</td>
<td width="200">解耦模仿学习 + 选择性臂间特征调制。</td>
<td width="360">SAPIEN + RoboTwin：7 任务，通常每任务 50 条；另两任务测试 100/150/200 条。实机四任务使用 50 条高质量遥操作示范；论文未说明是总计还是每任务。</td>
<td width="110">仿真 + 实机</td>
<td width="330">仿真均值 0.789，DP3 为 0.554；协调/非协调 0.700/0.824，对应基线 0.465/0.590。实机 45/60 = 75%，DP3 为 27/60 = 45%。</td>
<td width="250">仿真机器人/夹爪与实机夹爪未明确；没有量化碰撞、人工干预或执行时间指标。</td>
<td width="180"><a href="https://openaccess.thecvf.com/content/ICCV2025/html/Jiang_Rethinking_Bimanual_Robotic_Manipulation_Learning_with_Decoupled_Interaction_Framework_ICCV_2025_paper.html">CVF</a> / <a href="https://arxiv.org/abs/2503.09186">arXiv</a></td>
</tr>
<tr>
<td width="100" nowrap>ICCV 2025</td>
<td width="270"><a href="https://openaccess.thecvf.com/content/ICCV2025/html/Lu_AnyBimanual_Transferring_Unimanual_Policy_for_General_Bimanual_Manipulation_ICCV_2025_paper.html">AnyBimanual: Transferring Unimanual Policy for General Bimanual Manipulation</a></td>
<td width="260">用少量双臂示范，把预训练单臂技能组合为通用语言条件双臂操作。</td>
<td width="300">仿真：双 7 自由度 Franka Panda + Panda 两指夹爪。实机：双 UR5e + Robotiq 2F-85 夹爪。</td>
<td width="180">RealSense L515 RGB-D → 共享三维体素场景；机器人状态；无触觉。</td>
<td width="300">两份单臂策略由 技能管理器 动态调度；视觉对齐器 为每臂分配软体素区域；无固定主从臂。</td>
<td width="200">按语言选择单臂技能基元，并组合为同步/异步双臂动作。</td>
<td width="200">在 18 个单臂任务预训练，再用双臂示范微调。</td>
<td width="360">RLBench2 + PyRep + CoppeliaSim 4.1：12 任务×每任务 20 或 100 条（240/1,200），每任务测试 100 个回合。实机：9×30=270 条；少样本为 9×5。</td>
<td width="110">仿真 + 实机</td>
<td width="330">仿真 100 条示范设置的均值 32.00%，PerAct2 为 14.67%（+17.33 个百分点）。实机 55/65 = 84.62%；每任务五条实机示范时为 53.33%。</td>
<td width="250">仿真成功率仍只有 32%，未报告碰撞/干预率。约 1.5 分钟是示范采集 + 关键帧提取，不是任务执行时间。</td>
<td width="180"><a href="https://openaccess.thecvf.com/content/ICCV2025/html/Lu_AnyBimanual_Transferring_Unimanual_Policy_for_General_Bimanual_Manipulation_ICCV_2025_paper.html">CVF</a> / <a href="https://anybimanual.github.io/">项目</a> / <a href="https://github.com/TengBoYu01/AnyBimanual">代码</a></td>
</tr>
<tr>
<td width="100" nowrap>CVPR 2025</td>
<td width="270"><a href="https://openaccess.thecvf.com/content/CVPR2025/html/Lv_Spatial-Temporal_Graph_Diffusion_Policy_with_Kinematic_Modeling_for_Bimanual_Robotic_CVPR_2025_paper.html">Spatial-Temporal Graph Diffusion Policy with Kinematic Modeling for Bimanual Robotic Manipulation (KStar Diffuser)</a></td>
<td width="260">让双臂扩散动作满足机器人结构和关节运动学，减少相互干涉与不可执行位姿。</td>
<td width="300">仿真：双 Franka Panda + 平行夹爪。实机：Cobot AgileX ALOHA 双 6 自由度臂；夹爪型号未披露。</td>
<td width="180">语言 + 多视角 RGB-D；未报告触觉。</td>
<td width="300">动态空间—时间图跨时间连接两臂关节；策略联合生成两条末端轨迹，不设固定主臂。</td>
<td width="200">两条 6-D 末端位姿轨迹 + 夹爪开闭；可微 FK 约束预测位姿。</td>
<td width="200">图条件扩散模仿学习 + 运动学正则。</td>
<td width="360">RLBench2（本文未重述底层引擎）：5 任务、每任务 20/100 条、100 试验×3 随机种子。实机 ALOHA：2 任务、每任务 100 条示范、每任务评测 15 次。</td>
<td width="110">仿真 + 实机</td>
<td width="330">100 条示范设置的仿真均值 68.2±2.1%；各任务 83.0/98.7/27.0/43.7/89.0%。实机 抬盘 66.7±5.3%、交接 19.7±5.3%，均值 43.1±17.8%。</td>
<td width="250">交接仍弱；论文正文与附录对 handover_item_easy 的左右臂顺序描述冲突，表中不自行消解。</td>
<td width="180"><a href="https://openaccess.thecvf.com/content/CVPR2025/html/Lv_Spatial-Temporal_Graph_Diffusion_Policy_with_Kinematic_Modeling_for_Bimanual_Robotic_CVPR_2025_paper.html">CVF</a> / <a href="https://arxiv.org/abs/2503.10743">arXiv</a></td>
</tr>
</tbody>
</table>

**灵巧手与触觉/接触丰富任务研究现状矩阵。**

<table width="1740">
<thead>
<tr>
<th width="160" nowrap>研究主题</th>
<th width="280">代表问题</th>
<th width="360">已解决/较成熟</th>
<th width="360">未解决/瓶颈</th>
<th width="280">代表论文</th>
<th width="300">需要的硬件能力</th>
</tr>
</thead>
<tbody>
<tr>
<td width="160" nowrap>通用灵巧抓取</td>
<td width="280">任意物体、语言条件抓取、任务导向抓取</td>
<td width="360">大规模仿真抓取、跨手型潜在动作和人类视频预训练已有较多基线</td>
<td width="360">真机泛化、物理可行性、接触可观测性仍不稳</td>
<td width="280">DexGraspVLA / XL-VLA / EgoScale / UniDex</td>
<td width="300">多指手、高自由度、视觉/力反馈</td>
</tr>
<tr>
<td width="160" nowrap>掌内操作</td>
<td width="280">旋转、重定位、非抓取移动</td>
<td width="360">仿真、少量真机任务和触觉反应式策略已有方法</td>
<td width="360">接触动力学现实差距、传感覆盖和长时稳定性</td>
<td width="280">DexNDM / NoContactNoWorries / T-Rex / PP-Tac</td>
<td width="300">灵巧手、本体感知、接触/触觉</td>
</tr>
<tr>
<td width="160" nowrap>跨手型迁移</td>
<td width="280">不同手型之间策略迁移</td>
<td width="360">潜在表示/动作重定向开始出现</td>
<td width="360">手型差异、自由度差异、数据不对齐</td>
<td width="280">UniDex / Grasp2Grasp / House of Dextra</td>
<td width="300">多型号手、统一动作表示</td>
</tr>
<tr>
<td width="160" nowrap>人类视频到机器人</td>
<td width="280">第一视角视频、Vision Pro、VR 数据转机器人轨迹</td>
<td width="360">第一视角视频和手部跟踪数据链已成热点</td>
<td width="360">人手到机器人手映射、接触缺失、真机微调成本</td>
<td width="280">EgoDex / UniDex</td>
<td width="300">VR/Vision Pro、手部追踪、遥操作</td>
</tr>
<tr>
<td width="160" nowrap>触觉表征</td>
<td width="280">光学触觉、跨传感器表征、触觉语言对齐</td>
<td width="360">单传感器、跨传感器和触觉基础模型表征已有进展</td>
<td width="360">跨传感器泛化、动态力信息、实时闭环</td>
<td width="280">AnyTouch 2 / FTP-1 / ViTaS / VTV-LLM</td>
<td width="300">光学触觉、力反馈、多模态同步</td>
</tr>
<tr>
<td width="160" nowrap>接触丰富操作</td>
<td width="280">插拔、滑动、布料、软体、轻柔操作</td>
<td width="360">特定任务已有策略、数据采集系统和触觉仿真器</td>
<td width="360">真实接触不确定性、传感器耐用性、任务覆盖和可迁移闭环控制</td>
<td width="280">Tabero / Taccel / Touch in the Wild / FreeTacMan / exUMI</td>
<td width="300">触觉阵列、力控机械臂、仿真模型</td>
</tr>
</tbody>
</table>

**硬件、仿真与基准现状。**

_当前表格提及次数按下方 28 篇灵巧手和 28 篇触觉/接触丰富操作论文逐行统计；它表示当前 README 覆盖情况，不等同于全领域引用或使用量排名。_

<table width="1460">
<thead>
<tr>
<th width="220">平台/组件</th>
<th width="120">当前表格提及次数</th>
<th width="300">典型用途</th>
<th width="220">官网/代码链接</th>
<th width="300">已观察到的仿真/软件开发工具包适配</th>
<th width="300">调研结论</th>
</tr>
</thead>
<tbody>
<tr>
<td width="220">Franka Emika Panda / Franka Research 3</td>
<td width="120">17</td>
<td width="300">灵巧手、触觉夹爪和抓取基线最常见搭载机械臂</td>
<td width="220"><a href="https://frankarobotics.github.io/docs/">FCI 文档</a> / <a href="https://github.com/frankarobotics/franka_ros2">franka_ros2</a> / <a href="https://github.com/frankarobotics/franka_description">模型</a></td>
<td width="300">真实机器人软件开发工具包/ROS2 和 URDF 模型公开度高；手部安装、触觉安装和仿真控制器通常是论文自建</td>
<td width="300">当前调研里最稳妥的机械臂基线，但它本身不是完整的灵巧手+触觉栈</td>
</tr>
<tr>
<td width="220">Intel RealSense RGB-D</td>
<td width="120">19</td>
<td width="300">外部 RGB-D 感知，用于位姿、点云和策略输入</td>
<td width="220"><a href="https://github.com/realsenseai/librealsense">librealsense</a></td>
<td width="300">真实平台软件开发工具包支持好；提供视觉/深度，不提供接触或力反馈</td>
<td width="300">低风险默认相机，但不能解决接触可观测性</td>
</tr>
<tr>
<td width="220">Allegro Hand</td>
<td width="120">15</td>
<td width="300">四指灵巧手，用于旋转、关节物体操作和跨手型迁移</td>
<td width="220"><a href="https://www.allegrohand.com/">官网</a> / <a href="https://github.com/simlabrobotics/allegro_hand_ros">ROS</a> / <a href="https://github.com/simlabrobotics/allegro_hand_ros_v4">ROS v4</a></td>
<td width="300">公开 ROS 栈，并反复出现在 Isaac Gym / MuJoCo / DexArt 使用场景；稠密触觉不是标配，通常单独加装</td>
<td width="300">触觉不是核心需求时，是成熟的灵巧手研究平台</td>
</tr>
<tr>
<td width="220">LEAP Hand</td>
<td width="120">10</td>
<td width="300">低成本 16 自由度灵巧手，用于掌内操作、重定向和仿真到现实</td>
<td width="220"><a href="https://github.com/leap-hand/LEAP_Hand_API">API</a> / <a href="https://github.com/leap-hand">GitHub 组织</a></td>
<td width="300">公开 Python/C++/ROS/ROS2 接口，同时能看到 Isaac Gym 和 Isaac Lab 仓库；触觉通常缺失或外接</td>
<td width="300">当前表格里低成本手中软件开发工具包+仿真公开证据最强</td>
</tr>
<tr>
<td width="220">Shadow Dexterous Hand</td>
<td width="120">14</td>
<td width="300">高自由度仿人手和基准本体</td>
<td width="220"><a href="https://shadowrobot.com/dexterous-hand-series/">官网</a> / <a href="https://robotics.farama.org/envs/adroit_hand/index.html">Adroit</a></td>
<td width="300">MuJoCo/Adroit 和 Isaac Gym 类仿真中很常见；真实硬件迁移成本和采购成本更高</td>
<td width="300">适合作为基准手型；采购应由高端仿人硬件需求支撑</td>
</tr>
<tr>
<td width="220">Inspire RH56 系列</td>
<td width="120">8</td>
<td width="300">商用灵巧手和人形机器人末端</td>
<td width="220"><a href="https://en.inspire-robots.com/product-category/the-dexterous-hands">官网</a> / <a href="https://support.unitree.com/home/en/G1_developer/inspire_dfx_dexterous_hand">Unitree G1 集成说明</a></td>
<td width="300">多篇论文使用 Inspire 系列资产或真机；公开仿真/ROS 证据不如 LEAP 或 Allegro 统一</td>
<td width="300">作为实验室默认平台前，需要确认具体型号、触觉选项、软件开发工具包和 ROS2 支持</td>
</tr>
<tr>
<td width="220">DIGIT / Digit 360 / OmniTact</td>
<td width="120">7</td>
<td width="300">光学触觉，用于触觉图像、触觉定位和触觉表征学习</td>
<td width="220"><a href="https://digit.ml/digit.html">DIGIT</a> / <a href="https://github.com/facebookresearch/digit-interface">接口</a> / <a href="https://github.com/facebookresearch/tacto">TACTO</a></td>
<td width="300">接口和 TACTO 仿真公开度较好；与灵巧手或闭环策略集成仍通常是自定义工作</td>
<td width="300">适合作为光学触觉研究入口，尤其适合表征和数据集方向</td>
</tr>
<tr>
<td width="220">GelSight / GelSight Mini</td>
<td width="120">9</td>
<td width="300">商用凝胶光学触觉传感器</td>
<td width="220"><a href="https://www.gelsight.com/gelsightmini/">官网</a> / <a href="https://github.com/gelsightinc/gsrobotics">SDK</a></td>
<td width="300">真实传感器生态较强；仿真通常依赖 TACTO/Taxim/TacEx/Taccel 类项目流程，而不是单一通用栈</td>
<td width="300">触觉传感器选择较稳，但安装、闭环延迟和标定需要项目级验证</td>
</tr>
<tr>
<td width="220">XHand / ROBOTERA</td>
<td width="120">6</td>
<td width="300">商用灵巧手，用于跨手型和真实机器人灵巧操作论文</td>
<td width="220"><a href="https://www.robotera.com/en/goods1/4.html">官网</a></td>
<td width="300">当前论文能看到使用案例，但未找到统一公开的软件开发工具包/ROS2 和可复用仿真资产包</td>
<td width="300">硬件有潜力，但若没有厂家软件开发工具包和仿真资产确认，平台风险较高</td>
</tr>
<tr>
<td width="220">xArm / UFACTORY</td>
<td width="120">6</td>
<td width="300">灵巧手和遥操作系统的搭载机械臂</td>
<td width="220"><a href="https://github.com/xArm-Developer/xarm_ros2">xarm_ros2</a> / <a href="https://github.com/xArm-developer/xarm_ros">xarm_ros</a></td>
<td width="300">公开 ROS/ROS2 包包含仿真模型和控制示范；灵巧手安装仍是自定义工程</td>
<td width="300">和已验证灵巧手搭配时，是成本较友好的机械臂候选</td>
</tr>
<tr>
<td width="220">Apple Vision Pro / Meta Quest / GELLO</td>
<td width="120">Vision Pro 5；Meta Quest 或 VR 6；GELLO 1</td>
<td width="300">人类示范、手部跟踪、VR 遥操作和重定向数据链</td>
<td width="220"><a href="https://developer.apple.com/documentation/visionos/tracking-and-visualizing-hand-movement">Apple 手部跟踪</a> / <a href="https://wuphilipp.github.io/gello_site/">GELLO</a> / <a href="https://github.com/wuphilipp/gello_software">GELLO 代码</a></td>
<td width="300">适合规模化动作数据；接触、力和人手到机器人手重定向仍是算法瓶颈</td>
<td width="300">这是数据采集栈，不能替代触觉或力反馈</td>
</tr>
<tr>
<td width="220">Robotiq 2F / 平行夹爪</td>
<td width="120">4</td>
<td width="300">非灵巧手论文里的抓取基线硬件</td>
<td width="220"><a href="https://robotiq.com/products/2f85-140-adaptive-robot-gripper">官网</a></td>
<td width="300">相比灵巧手更容易仿真和部署；不是多指操作平台</td>
<td width="300">适合作为基线，但不能算作灵巧手能力</td>
</tr>
<tr>
<td width="220">Sharpa Wave / Dexmate Vega-1</td>
<td width="120">3</td>
<td width="300">高自由度触觉灵巧手和双手触觉反应式机器人平台</td>
<td width="220"><a href="https://arxiv.org/abs/2602.16710">EgoScale</a> / <a href="https://arxiv.org/abs/2606.17055">T-Rex</a></td>
<td width="300">公开证据来自论文/项目描述；未找到可复用公开软件开发工具包/ROS2 或统一仿真资产</td>
<td width="300">触觉灵巧能力证据强，但在确认厂家资产和接口前集成风险仍高</td>
</tr>
<tr>
<td width="220">自研视觉触觉夹爪 / 触觉皮肤</td>
<td width="120">12</td>
<td width="300">无机器人触觉数据采集、便携触觉夹爪和大覆盖接触感知</td>
<td width="220"><a href="https://opendrivelab.com/FreeTacMan">FreeTacMan</a> / <a href="https://dex-skin.github.io/">DexSkin</a> / <a href="https://peilin-666.github.io/projects/PP-Tac/">PP-Tac</a></td>
<td width="300">多数系统有项目页或代码，但机械安装、标定和运行时集成都是项目自定义</td>
<td width="300">当前最适合扩充触觉数据覆盖，但还不是标准即插即用灵巧手栈</td>
</tr>
</tbody>
</table>

<table width="1440">
<thead>
<tr>
<th width="200">仿真器/框架</th>
<th width="120">当前表格提及次数</th>
<th width="300">典型用途</th>
<th width="220">官网/代码链接</th>
<th width="300">硬件适配情况</th>
<th width="300">开放缺口</th>
</tr>
</thead>
<tbody>
<tr>
<td width="200">Isaac Gym</td>
<td width="120">11</td>
<td width="300">大规模强化学习、抓取过滤和灵巧手策略训练</td>
<td width="220"><a href="https://developer.nvidia.com/isaac-gym">官网</a> / <a href="https://github.com/isaac-sim/IsaacGymEnvs">IsaacGymEnvs</a></td>
<td width="300">当前表格里 Allegro、LEAP、Shadow 和合成抓取流程最常见适配对象</td>
<td width="300">NVIDIA 已将 Isaac Gym 标为旧版；新项目需要评估迁移 Isaac Lab 的成本</td>
</tr>
<tr>
<td width="200">Isaac Lab / Isaac Sim</td>
<td width="120">4</td>
<td width="300">机器人学习、传感器仿真和触觉实验的继任栈</td>
<td width="220"><a href="https://developer.nvidia.com/isaac/lab">Isaac Lab</a> / <a href="https://github.com/isaac-sim/IsaacLab">代码</a> / <a href="https://github.com/isaac-sim/IsaacSim">Isaac Sim</a></td>
<td width="300">适合 Franka 类机械臂和新触觉仿真论文；Isaac Sim 支持从 URDF/MJCF/CAD 导入资产</td>
<td width="300">稠密触觉和灵巧手控制器仍常需要自定义集成</td>
</tr>
<tr>
<td width="200">MuJoCo / MJCF</td>
<td width="120">4</td>
<td width="300">接触丰富动力学、Adroit 类手部任务和可复现实验基准</td>
<td width="220"><a href="https://mujoco.org/">官网</a> / <a href="https://github.com/google-deepmind/mujoco">代码</a> / <a href="https://github.com/google-deepmind/mujoco_menagerie">Menagerie</a></td>
<td width="300">适合 Shadow/Adroit 和 MJCF 模型，也适合做紧凑可复现基准</td>
<td width="300">高保真光学触觉渲染和真实手驱动并非开箱即用</td>
</tr>
<tr>
<td width="200">SAPIEN / ManiSkill</td>
<td width="120">SAPIEN 5；ManiSkill 2</td>
<td width="300">关节物体、操作环境和任务/数据生成</td>
<td width="220"><a href="https://sapien.ucsd.edu/">SAPIEN</a> / <a href="https://github.com/haosulab/SAPIEN">SAPIEN 代码</a> / <a href="https://github.com/mani-skill/ManiSkill">ManiSkill</a></td>
<td width="300">关节物体和机器人资产生态较好；手型模型依赖各论文提供的 URDF/资产</td>
<td width="300">在真实灵巧手仿真到现实上不如机械臂/夹爪操作标准化</td>
</tr>
<tr>
<td width="200">Adroit / Gymnasium Robotics</td>
<td width="120">Adroit 2；Gymnasium 1</td>
<td width="300">Shadow Hand 加机械臂任务的灵巧操作基准</td>
<td width="220"><a href="https://robotics.farama.org/envs/adroit_hand/index.html">文档</a> / <a href="https://github.com/Farama-Foundation/Gymnasium-Robotics">代码</a></td>
<td width="300">Shadow Hand 基准适配强，适合算法比较</td>
<td width="300">不是采购或真实硬件软件开发工具包；任务覆盖比真实实验室操作窄</td>
</tr>
<tr>
<td width="200">DexArt / MetaWorld</td>
<td width="120">DexArt 1；MetaWorld 1</td>
<td width="300">关节物体灵巧操作和操作策略基准套件</td>
<td width="220"><a href="https://www.chenbao.tech/dexart/">DexArt</a> / <a href="https://github.com/Kami-code/dexart-release">DexArt 代码</a> / <a href="https://meta-world.github.io/">MetaWorld</a></td>
<td width="300">适合基准对比；硬件本体由各环境固定</td>
<td width="300">不同环境的观测/动作定义不一致，跨论文比较困难</td>
</tr>
<tr>
<td width="200">TACTO</td>
<td width="120">2</td>
<td width="300">面向 DIGIT、OmniTact 等视觉触觉传感器的触觉渲染</td>
<td width="220"><a href="https://github.com/facebookresearch/tacto">代码</a> / <a href="https://ai.meta.com/research/publications/tacto-a-fast-flexible-and-open-source-simulator-for-high-resolution-vision-based-tactile-sensors/">论文页</a></td>
<td width="300">适合触觉图像仿真和感知预训练；原始集成主要面向 PyBullet</td>
<td width="300">完整灵巧手闭环接触动力学仍需自定义</td>
</tr>
<tr>
<td width="200">Taccel</td>
<td width="120">1</td>
<td width="300">面向视觉触觉机器人的 GPU 触觉仿真</td>
<td width="220"><a href="https://taccel-simulator.github.io/index.html">文档</a> / <a href="https://github.com/Taccel-Simulator">GitHub</a></td>
<td width="300">支持 URDF 机器人加载、触觉传感器配置文件和高吞吐触觉仿真</td>
<td width="300">生态较新；真实传感器标定和大规模基准采用还在发展</td>
</tr>
<tr>
<td width="200">PalpationSim</td>
<td width="120">1</td>
<td width="300">软体触诊和触觉表征学习</td>
<td width="220"><a href="https://zoharri.github.io/artificial-palpation/">项目</a> / <a href="https://github.com/zoharri/ArtificialPalpation">代码</a></td>
<td width="300">更像任务特定触觉仿真，而不是通用灵巧手仿真器</td>
<td width="300">当前表格里跨论文复用证据有限</td>
</tr>
<tr>
<td width="200">RLBench / tactile_envs / 自定义触觉仿真</td>
<td width="120">3</td>
<td width="300">多模态策略共识、视觉触觉表征学习和关节物体触觉研究</td>
<td width="220"><a href="https://github.com/stepjam/RLBench">RLBench</a> / <a href="https://github.com/SkyRainWind/ViTaS">ViTaS 代码</a> / <a href="https://vi-tacman.github.io/">Vi-TacMan</a></td>
<td width="300">适合方法比较，但每项工作定义的触觉观测和机器人本体不同</td>
<td width="300">作为采购依据仍弱于共享真实灵巧手触觉基准</td>
</tr>
</tbody>
</table>

<table width="1280">
<thead>
<tr>
<th width="180" nowrap>硬件系列</th>
<th width="180">适配状态</th>
<th width="360">已找到的最佳匹配仿真/数据栈</th>
<th width="220">证据链接</th>
<th width="340">实践注意点</th>
</tr>
</thead>
<tbody>
<tr>
<td width="180" nowrap>Franka + 加装灵巧手或触觉夹爪</td>
<td width="180">官方机械臂；社区/自定义末端集成</td>
<td width="360">真实机器人使用 ROS2/libfranka；论文流程中常见 Isaac/MuJoCo/SAPIEN 资产</td>
<td width="220"><a href="https://frankarobotics.github.io/docs/">FCI 文档</a> / <a href="https://github.com/frankarobotics/franka_ros2">franka_ros2</a> / <a href="https://github.com/frankarobotics/franka_description">模型</a></td>
<td width="340">机械臂支持成熟，但每种手/传感器都需要机械安装、标定和控制器集成</td>
</tr>
<tr>
<td width="180" nowrap>LEAP Hand</td>
<td width="180">官方</td>
<td width="360">LEAP 接口、LEAP Isaac Gym、LEAP Isaac Lab、论文自建 MuJoCo/Isaac 环境</td>
<td width="220"><a href="https://github.com/leap-hand/LEAP_Hand_API">API</a> / <a href="https://github.com/leap-hand/LEAP_Hand_Sim">Isaac Gym 仿真</a> / <a href="https://github.com/leap-hand/LEAP_Hand_Isaac_Lab">Isaac Lab 仿真</a></td>
<td width="340">适合可复现实验手部控制；触觉不是默认手部栈的一部分</td>
</tr>
<tr>
<td width="180" nowrap>Allegro Hand</td>
<td width="180">官方/社区</td>
<td width="360">ROS 栈、Isaac Gym、MuJoCo、DexArt 类环境</td>
<td width="220"><a href="https://www.allegrohand.com/">官网</a> / <a href="https://github.com/simlabrobotics/allegro_hand_ros">ROS</a> / <a href="https://github.com/Kami-code/dexart-release">DexArt</a></td>
<td width="340">研究先例强；传感指尖或触觉阵列需要单独选型</td>
</tr>
<tr>
<td width="180" nowrap>Shadow Dexterous Hand</td>
<td width="180">社区基准；官方硬件</td>
<td width="360">MuJoCo/Adroit 和 Isaac Gym 抓取环境</td>
<td width="220"><a href="https://shadowrobot.com/dexterous-hand-series/">官网</a> / <a href="https://robotics.farama.org/envs/adroit_hand/index.html">Adroit 文档</a> / <a href="https://github.com/Farama-Foundation/Gymnasium-Robotics">Gymnasium Robotics</a></td>
<td width="340">基准兼容性强，但真实硬件采购和迁移负担高于 LEAP/Allegro</td>
</tr>
<tr>
<td width="180" nowrap>Inspire / XHand</td>
<td width="180">不明确</td>
<td width="360">论文自建资产、真实平台和人形机器人集成</td>
<td width="220"><a href="https://en.inspire-robots.com/product-category/the-dexterous-hands">Inspire</a> / <a href="https://support.unitree.com/home/en/G1_developer/inspire_dfx_dexterous_hand">Unitree G1 说明</a> / <a href="https://www.robotera.com/en/goods1/4.html">ROBOTERA</a></td>
<td width="340">不能默认兼容；应向厂家索要 URDF/MJCF、ROS2 驱动、低层控制频率和触觉接口</td>
</tr>
<tr>
<td width="180" nowrap>GelSight / DIGIT 光学触觉</td>
<td width="180">官方软件开发工具包；社区仿真</td>
<td width="360">真实软件开发工具包加 TACTO/Taccel/Taxim/TacEx 类触觉仿真流程</td>
<td width="220"><a href="https://digit.ml/digit.html">DIGIT</a> / <a href="https://github.com/facebookresearch/digit-interface">DIGIT 接口</a> / <a href="https://github.com/gelsightinc/gsrobotics">GelSight SDK</a> / <a href="https://github.com/facebookresearch/tacto">TACTO</a> / <a href="https://github.com/Taccel-Simulator">Taccel</a></td>
<td width="340">适合触觉表征；闭环操作取决于延迟、安装、标定和同步</td>
</tr>
<tr>
<td width="180" nowrap>Vision Pro / VR / GELLO 遥操作</td>
<td width="180">官方跟踪；社区遥操作</td>
<td width="360">手部跟踪、VR 控制器、GELLO 关节级遥操作和重定向流程</td>
<td width="220"><a href="https://developer.apple.com/documentation/visionos/tracking-and-visualizing-hand-movement">Apple 手部跟踪</a> / <a href="https://wuphilipp.github.io/gello_site/">GELLO</a> / <a href="https://github.com/wuphilipp/gello_software">GELLO 代码</a></td>
<td width="340">更擅长规模化动作采集，不擅长接触采集；接触和力标签仍需要触觉/力传感器</td>
</tr>
</tbody>
</table>

<table width="1380">
<thead>
<tr>
<th width="220" nowrap>基准 / 数据集</th>
<th width="300">主要范围</th>
<th width="300">硬件/仿真关联</th>
<th width="220">链接</th>
<th width="340">对本调研的用途</th>
</tr>
</thead>
<tbody>
<tr>
<td width="220" nowrap>Adroit</td>
<td width="300">Shadow Hand 的开门、敲钉、转笔、重定位等操作任务</td>
<td width="300">MuJoCo / Gymnasium Robotics</td>
<td width="220"><a href="https://robotics.farama.org/envs/adroit_hand/index.html">文档</a></td>
<td width="340">适合算法基准，但不是统一真实硬件数据集</td>
</tr>
<tr>
<td width="220" nowrap>DexArt</td>
<td width="300">关节物体上的灵巧操作</td>
<td width="300">基准环境和训练代码</td>
<td width="220"><a href="https://www.chenbao.tech/dexart/">项目</a> / <a href="https://github.com/Kami-code/dexart-release">代码</a></td>
<td width="340">适合关节物体灵巧操作；本体和任务定义受基准限定</td>
</tr>
<tr>
<td width="220" nowrap>GraspNet-1Billion</td>
<td width="300">大规模 6D 平行夹爪抓取检测</td>
<td width="300">RealSense/Kinect RGB-D 场景；平行夹爪抓取标签</td>
<td width="220"><a href="https://graspnet.net/">项目</a> / <a href="https://github.com/graspnet/graspnetAPI">API</a></td>
<td width="340">重要抓取基线，但不是灵巧手操作基准</td>
</tr>
<tr>
<td width="220" nowrap>DexYCB</td>
<td width="300">人手抓取、6D 物体位姿、手姿态和交接相关任务</td>
<td width="300">YCB 物体和多视角真实数据</td>
<td width="220"><a href="https://dex-ycb.github.io/">项目</a> / <a href="https://github.com/NVlabs/dex-ycb-toolkit">工具包</a></td>
<td width="340">适合人手-物体感知和抓取迁移，本身不是机器人控制基准</td>
</tr>
<tr>
<td width="220" nowrap>OakInk / OakInk2</td>
<td width="300">手-物交互、可供性和双手任务数据</td>
<td width="300">人类示范和物体/手部标注</td>
<td width="220"><a href="https://oakink.net/">OakInk</a> / <a href="https://github.com/oakink/OakInk2">OakInk2 代码</a></td>
<td width="340">适合做人到机器人先验；机器人本体重定向仍是额外工作</td>
</tr>
<tr>
<td width="220" nowrap>ARCTIC</td>
<td width="300">含动态接触的双手关节物体操作</td>
<td width="300">人类视频和三维手/物体网格</td>
<td width="220"><a href="https://arctic.is.tue.mpg.de/">项目</a> / <a href="https://github.com/zc-alexfan/arctic">代码</a></td>
<td width="340">接触丰富人类数据强，但不能直接作为机器人硬件基准</td>
</tr>
<tr>
<td width="220" nowrap>UniDex-Dataset</td>
<td width="300">跨多个灵巧手的第一视角视频衍生轨迹</td>
<td width="300">8 种灵巧手、重定向和机器人中心轨迹</td>
<td width="220"><a href="https://unidex-ai.github.io/">项目</a> / <a href="https://github.com/unidex-ai/UniDex">代码</a></td>
<td width="340">当前最接近跨手型标准化的尝试，但仍很新且依赖重定向</td>
</tr>
<tr>
<td width="220" nowrap>DexGraspNet / DexGrasp Anything</td>
<td width="300">大规模仿真灵巧抓取位姿</td>
<td width="300">ShadowHand 类抓取合成和物理过滤</td>
<td width="220"><a href="https://pku-epic.github.io/DexGraspNet/">DexGraspNet</a> / <a href="https://dexgraspanything.github.io/">DGA</a></td>
<td width="340">适合抓取生成；对长时程接触丰富控制覆盖不足</td>
</tr>
<tr>
<td width="220" nowrap>ZeroGrasp-11B</td>
<td width="300">形状重建加 6D 抓取标注</td>
<td width="300">RGB-D、Objaverse-LVIS、Franka/Robotiq 评测</td>
<td width="220"><a href="https://sh8.io/#/zerograsp">项目</a> / <a href="https://github.com/sh8/ZeroGrasp">代码</a></td>
<td width="340">是强抓取数据点，但面向平行夹爪而不是灵巧手控制</td>
</tr>
<tr>
<td width="220" nowrap>RoboTwin 2.0</td>
<td width="300">双臂操作数据生成和基准</td>
<td width="300">双臂配置的仿真基准</td>
<td width="220"><a href="https://robotwin-platform.github.io/">项目</a> / <a href="https://github.com/robotwin-Platform/robotwin">代码</a></td>
<td width="340">适合比较双臂配置；不是触觉优先，也未统一手型</td>
</tr>
<tr>
<td width="220" nowrap>MFR Benchmark</td>
<td width="300">多指灵巧操作任务</td>
<td width="300">Isaac Gym 中的 Allegro 手和可选机械臂配置</td>
<td width="220"><a href="https://github.com/UM-ARM-Lab/MFR_benchmark">代码</a></td>
<td width="340">如果实验室标准化 Allegro/Isaac Gym，可作为手部控制候选基准</td>
</tr>
<tr>
<td width="220" nowrap>YCB-Slide</td>
<td width="300">滑动触觉定位</td>
<td width="300">DIGIT 触觉图像和 YCB 物体</td>
<td width="220"><a href="https://suddhu.github.io/midastouch-tactile/">项目</a> / <a href="https://github.com/facebookresearch/MidasTouch">代码</a></td>
<td width="340">适合触觉定位基准，不是完整操作基准</td>
</tr>
<tr>
<td width="220" nowrap>ToucHD / AnyTouch 2 / Sparsh</td>
<td width="300">跨传感器和动态触觉的通用触觉表征学习</td>
<td width="300">GelSight、DIGIT、FastUMI、ToucHD 等触觉数据</td>
<td width="220"><a href="https://github.com/GeWu-Lab/AnyTouch2">AnyTouch 2</a> / <a href="https://github.com/facebookresearch/sparsh">Sparsh</a> / <a href="https://huggingface.co/datasets/BAAI/ToucHD-Sim">ToucHD-Sim</a></td>
<td width="340">适合表征预训练；下游机器人策略迁移仍需要任务数据</td>
</tr>
<tr>
<td width="220" nowrap>VTV150K / VTV-LLM</td>
<td width="300">视觉触觉视频理解和触觉问答</td>
<td width="300">GelSight Mini、DIGIT、Tac3D 视频帧</td>
<td width="220"><a href="https://github.com/IvanXie416/VTV-LLM">代码</a> / <a href="https://arxiv.org/abs/2505.22566">论文</a></td>
<td width="340">适合触觉语言基准，不是闭环操作基准</td>
</tr>
<tr>
<td width="220" nowrap>Touch in the Wild</td>
<td width="300">便携视觉触觉夹爪的精细操作示范</td>
<td width="300">自研触觉夹爪、GoPro 同步和 ROS2 触觉日志</td>
<td width="220"><a href="https://binghao-huang.github.io/touch_in_the_wild/">项目</a></td>
<td width="340">是当前表格里最接近触觉操作的数据集，但硬件是自研</td>
</tr>
<tr>
<td width="220" nowrap>T-Rex Dataset</td>
<td width="300">触觉同步的双手灵巧操作</td>
<td width="300">Dexmate Vega-1 + Sharpa Wave 手；同步 RGB、触觉信号、机器人状态、动作和语言</td>
<td width="220"><a href="https://arxiv.org/abs/2606.17055">论文</a> / <a href="https://tactile-reactive-dexterous.github.io/">项目</a></td>
<td width="340">重要触觉反应式数据集；依赖前需要确认公开可复用资产</td>
</tr>
<tr>
<td width="220" nowrap>FTP-1 Dataset / MTTS</td>
<td width="300">跨传感器触觉基础策略预训练</td>
<td width="300">26 个数据源、21 种触觉传感器，覆盖图像/阵列/状态触觉输入</td>
<td width="220"><a href="https://arxiv.org/abs/2606.13102">论文</a> / <a href="https://ftp1-policy.github.io/">项目</a></td>
<td width="340">是当前跨传感器触觉预训练的强证据；下游部署仍需目标传感器微调</td>
</tr>
<tr>
<td width="220" nowrap>FreeTacMan</td>
<td width="300">面向接触丰富操作的无机器人视觉触觉数据采集</td>
<td width="300">手持模块化视觉触觉夹爪；Piper/Franka 快换安装</td>
<td width="220"><a href="https://opendrivelab.com/FreeTacMan">项目</a> / <a href="https://github.com/OpenDriveLab/FreeTacMan">代码</a></td>
<td width="340">是强数据采集基准候选，但本身不是固定灵巧手策略基准</td>
</tr>
<tr>
<td width="220" nowrap>exUMI</td>
<td width="300">可扩展 UMI 式触觉机器人教学系统</td>
<td width="300">自回归动作捕捉、旋转编码器、模块化视觉触觉和自动标定</td>
<td width="220"><a href="https://proceedings.mlr.press/v305/xu25e.html">PMLR</a> / <a href="https://silicx.github.io/exUMI/">项目</a></td>
<td width="340">触觉教学系统证据强，但仍是自定义硬件，不是通用触觉手标准</td>
</tr>
<tr>
<td width="220" nowrap>Vi-TacMan 关节物体套件</td>
<td width="300">视觉到触觉的关节物体操作</td>
<td width="300">50,000+ 仿真物体，加真实 Kinova Gen3 + GelSight 型触觉实验</td>
<td width="220"><a href="https://arxiv.org/abs/2510.06339">论文</a> / <a href="https://vi-tacman.github.io/">项目</a></td>
<td width="340">适合触觉关节物体控制，但还不是完整长时程家庭操作基准</td>
</tr>
</tbody>
</table>
