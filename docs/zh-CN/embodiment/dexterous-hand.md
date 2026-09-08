# 灵巧手

[首页](../../../README.zh-CN.md) | [英文](../../en/embodiment/dexterous-hand.md) | [方向目录](README.md)

共 28 篇。

下表采用灵巧手方向专用字段，分别核查具体硬件、技能/接触模式、触觉、动作/控制、仿真与数据规模、迁移路径、人类数据链和论文指标。“未披露”表示已核查的论文/项目来源没有给出该项；仿真接触标签不计作真实触觉硬件。

<table width="3380">
<thead>
<tr>
<th width="100" nowrap>会议</th>
<th width="260">论文</th>
<th width="230">研究问题</th>
<th width="230">解决进展</th>
<th width="240">当前局限</th>
<th width="280">具体手 / 机械臂 / 载体</th>
<th width="160">自由度 / 驱动</th>
<th width="220">技能 / 接触模式</th>
<th width="180">触觉配置</th>
<th width="210">动作空间 / 控制频率</th>
<th width="330">仿真 / 训练环境 + 数据规模</th>
<th width="240">仿真到现实 / 重定向路径</th>
<th width="220">遥操作 / 人类数据链</th>
<th width="300">核心指标</th>
<th width="180">资源</th>
</tr>
</thead>
<tbody>
<tr>
<td width="100" nowrap>CoRL 2023</td>
<td width="260"><a href="https://arxiv.org/abs/2309.09979">General In-hand Object Rotation with Vision and Touch</a></td>
<td width="230">让指尖手内旋转跨物体形状和指令轴泛化。</td>
<td width="230">RotateIt 融合视觉、低维触觉与本体感觉，并蒸馏成可直接上真机的闭环策略。</td>
<td width="240">仅使用离散接触位置而非完整触觉图像；物体须在手的机械范围内，冻结策略不能从部署经验继续学习。</td>
<td width="280">Allegro Hand；Intel RealSense D435；四个指尖全向视觉触觉传感器</td>
<td width="160">16 个手关节；位置控制</td>
<td width="220">绕 x/y/z 轴连续指尖手内旋转；多接触手指步态</td>
<td width="180">四个光学指尖传感器；策略只用 8 区接触位置，不输入原始触觉图像</td>
<td width="210">16 维关节目标 20 Hz；PD 力矩环 300 Hz</td>
<td width="330">Isaac Gym；物体来自 EGAD、Google Scanned Objects、YCB、ContactDB；15 个留出分布外物体；无人工示范</td>
<td width="240">特权 PPO 教师 → 视觉触觉 Transformer 蒸馏并随机化深度/物理 → 直接真机部署</td>
<td width="220">无</td>
<td width="300">真机 x 轴 ContactLoc 旋转奖励 102.36，无触觉为 79.37；分布外奖励下降 15.4%，仅本体感觉为 41.6%</td>
<td width="180"><a href="https://arxiv.org/abs/2309.09979">论文</a> / <a href="https://haozhi.io/rotateit/">项目</a> / <a href="https://proceedings.mlr.press/v229/qi23a.html">PMLR</a></td>
</tr>
<tr>
<td width="100" nowrap>CVPR 2025</td>
<td width="260"><a href="https://openaccess.thecvf.com/content/CVPR2025/html/Li_ManipTrans_Efficient_Dexterous_Bimanual_Manipulation_Transfer_via_Residual_Learning_CVPR_2025_paper.html">ManipTrans: Efficient Dexterous Bimanual Manipulation Transfer via Residual Learning</a></td>
<td width="230">把长时、接触密集的人类单手/双手操作轨迹迁移到异构机器人手。</td>
<td width="230">把形态层动作模仿与接触感知残差强化学习分开，并构建 DexManipNet。</td>
<td width="240">排除了可变形/过大物体的动作捕捉；真机只给出定性轨迹回放，没有量化闭环触觉控制。</td>
<td width="280">仿真：双 Shadow、MANO、Inspire、Allegro；真机：双 7 自由度 RealMan 机械臂 + 双升级 Inspire Hand</td>
<td width="160">仿真手 22/22/12/16 自由度；真机 Inspire 每手 6 自由度</td>
<td width="220">笔帽、拧瓶盖、关节物体及协同双手操作；接触力残差细化</td>
<td width="180">仿真用指尖接触力；真机 Inspire 含触觉传感器，但未报告其闭环使用</td>
<td width="210">每手 K 维关节 PD 目标 + 6 维腕部力；Isaac Gym 步长 1/60 s</td>
<td width="330">Isaac Gym，4,096 个并行环境；DexManipNet 含 61 任务、3.3K 个回合、1.2K 物体、1.34M 帧，其中约 600 条双手序列</td>
<td width="240">动作捕捉 → 手轨迹模仿 → 物体/接触残差强化学习；将仿真 12 自由度 Inspire 拟合为真机 6 自由度 Inspire 回放</td>
<td width="220">OakInk-V2 光学动作捕捉；FAOVR VR/HITL；GRAB 与 ARCTIC 序列</td>
<td width="300">单手/双手迁移 SR 58.1/39.5%，Retarget+Residual 为 47.8/13.9%；真机证据仅定性</td>
<td width="180"><a href="https://openaccess.thecvf.com/content/CVPR2025/papers/Li_ManipTrans_Efficient_Dexterous_Bimanual_Manipulation_Transfer_via_Residual_Learning_CVPR_2025_paper.pdf">论文</a> / <a href="https://openaccess.thecvf.com/content/CVPR2025/html/Li_ManipTrans_Efficient_Dexterous_Bimanual_Manipulation_Transfer_via_Residual_Learning_CVPR_2025_paper.html">CVF</a></td>
</tr>
<tr>
<td width="100" nowrap>ICCV 2025</td>
<td width="260"><a href="https://openaccess.thecvf.com/content/ICCV2025/html/He_DexVLG_Dexterous_Vision-Language-Grasp_Model_at_Scale_ICCV_2025_paper.html">DexVLG: Dexterous Vision-Language-Grasp Model at Scale</a></td>
<td width="230">从单视角 RGB-D 生成符合指令、面向部件的灵巧抓取。</td>
<td width="230">用 DexGraspNet 3.0 训练视觉语言模型与流匹配姿态头，并在真机执行语义抓取。</td>
<td width="240">悬浮手训练忽略机械臂工作空间；不安全样本须过滤，且缺少有效的候选姿态排序。</td>
<td width="280">UR10e 上的 ShadowHand；腕部 Intel RealSense D415</td>
<td width="160">22 个手关节角 + 6 维腕位姿</td>
<td width="220">静态功能抓取姿态；按部件、风格及可选手指接触模式条件化抬升</td>
<td width="180">无；接触模式是合成标签，不是触觉传感</td>
<td width="210">抓取 g = 平移 + SO(3) 旋转 + 22 关节角；运动规划执行；频率未披露</td>
<td width="330">DexGraspNet 3.0：174K 个 Objaverse 物体、170M 姿态-文本对；Isaac Gym 验证；Blender D415 渲染；64 张 RTX 4090 训练 230 个训练轮次</td>
<td width="240">合成姿态学习 → 单视角彩色点云推理 → 安全过滤与运动规划 → 真实 UR10e</td>
<td width="220">无人工示范；SAMesh 与 GPT-4o 生成部件语义/文本</td>
<td width="300">仿真已见/未见/SamPart3D 成功率 87.7/79.1/76.3%；真机简单物体成功率 80%、部件准确率 75%，试验次数未说明</td>
<td width="180"><a href="https://arxiv.org/pdf/2507.02747">论文</a> / <a href="https://jiaweihe.com/dexvlg">项目</a> / <a href="https://openaccess.thecvf.com/content/ICCV2025/html/He_DexVLG_Dexterous_Vision-Language-Grasp_Model_at_Scale_ICCV_2025_paper.html">CVF</a></td>
</tr>
<tr>
<td width="100" nowrap>ICCV 2025</td>
<td width="260"><a href="https://openaccess.thecvf.com/content/ICCV2025/html/Wang_DexH2R_A_Benchmark_for_Dynamic_Dexterous_Grasping_in_Human-to-Robot_Handover_ICCV_2025_paper.html">DexH2R: A Benchmark for Dynamic Dexterous Grasping in Human-to-Robot Handover</a></td>
<td width="230">为动态人到机器人的递物生成安全的接收手接近轨迹。</td>
<td width="230">发布真实多模态递物基准，对比自回归、二维扩散和三维扩散接近策略。</td>
<td width="240">这是单机械臂/右手从人类接物，不是机器人双手操作；Hard 模式成功率与安全率仍低。</td>
<td width="280">UR10e + 右 ShadowHand；12 台外部 RGB 相机、4 台 Azure Kinect、2 台腕部 RealSense D455</td>
<td width="160">硬件 24 自由度；模型状态用 22 关节 + 全局 SE(3)</td>
<td width="220">运动物体接收抓取；目标姿态准备、响应式接近、末端对齐</td>
<td width="180">未报告</td>
<td width="210">预测全局 SE(3) + 22 维关节状态的未来序列；控制频率未披露</td>
<td width="330">4,282 次真实递物 / 456K 帧、39 人、56 物体；划分 2,888/591/803；DexGraspNet 预训练与 Isaac Gym 稳定性筛选</td>
<td width="240">合成抓取预训练 + Isaac 稳定性过滤 → 真实数据微调 → 真实接收执行</td>
<td width="220">&lt;50 ms 手套遥操作采集机器人接收手动作；递物者仍为外部人类</td>
<td width="300">Easy MotionNet/DP3 成功率 71.1/66.3%；Hard 为 26.6/27.1%，安全率 15.4/33.7%</td>
<td width="180"><a href="https://openaccess.thecvf.com/content/ICCV2025/html/Wang_DexH2R_A_Benchmark_for_Dynamic_Dexterous_Grasping_in_Human-to-Robot_Handover_ICCV_2025_paper.html">论文</a> / <a href="https://dexh2r.github.io/">项目</a> / <a href="https://github.com/4DVLab/DexH2R">代码</a></td>
</tr>
<tr>
<td width="100" nowrap>IROS 2026</td>
<td width="260"><a href="https://arxiv.org/abs/2606.24450">NoContactNoWorries: Estimating Contact through Vision and Proprioception for In-Hand Dexterous Manipulation</a></td>
<td width="230">在腕部相机自遮挡下，不借助触觉硬件恢复指尖接触。</td>
<td width="230">从 RGB-D、实际/指令关节预测四路二值接触，并替代理想参照触觉执行闭环旋转。</td>
<td width="240">只建模固定指尖二值接触，没有稠密接触图、滑移、力分布或跨任务接触表示。</td>
<td width="280">LEAP Hand + 腕部 Intel RealSense D455；薄型 FSR 只用于真机评分</td>
<td width="160">16 维手状态/指令</td>
<td width="220">预测指尖接触驱动的手内旋转；多接触闭环控制</td>
<td width="180">四个 FSR 仅提供真值，策略推理/部署时移除</td>
<td width="210">相对关节目标 20 Hz；RGB-D 30 Hz；编译后预测延迟 8 ms</td>
<td width="330">Isaac Gym/PhysX；5 个训练几何 × 50 轨迹展开 × 15 s × 30 Hz，约 22.5K 标注帧；物理/感知随机化</td>
<td width="240">PhysX 二值接触监督 → 视觉-本体接触预测器 → 真机策略使用伪触觉</td>
<td width="220">无</td>
<td width="300">真机已见物体 F1 0.71–0.84，新物体物体 0.80/0.74；遮挡帧 完整模型 0.85，仅视觉 0.51</td>
<td width="180"><a href="https://arxiv.org/abs/2606.24450">论文</a> / <a href="https://soham2560.github.io/no-contact-no-worries/">项目</a></td>
</tr>
<tr>
<td width="100" nowrap>ICLR 2026</td>
<td width="260"><a href="https://openreview.net/forum?id=Bf4FeuW0Mr">DemoGrasp: Universal Dexterous Grasping from a Single Demonstration</a></td>
<td width="230">从一条成功种子轨迹学习通用闭环灵巧抓取。</td>
<td width="230">把腕部与手指动作编辑压成单步强化学习，再将成功轨迹展开蒸馏为视觉策略。</td>
<td width="240">单次编辑在整段回合内固定；虽有一定视觉重抓能力，但大执行偏差恢复仍受限。</td>
<td width="280">仿真：Shadow、Inspire、SVH、Allegro、DClaw、Panda 夹爪；真机：7 自由度 FR3 + Inspire + 双 RealSense D435i</td>
<td width="160">真机 Inspire：6 主动 + 6 被动关节</td>
<td width="220">桌面抓取/抬升，覆盖小、薄物体；允许必要的手指-桌面接触</td>
<td width="180">未报告</td>
<td width="210">强化学习编辑量 = 腕 SE(3) 变换 + 手关节增量；底层 60 Hz，视觉策略 3 Hz</td>
<td width="330">Isaac Gym；一条种子轨迹；在 3,200 个 DexGraspNet 物体或 175 个跨数据集物体训练；采样/BC 对照收集 35K 成功轨迹</td>
<td width="240">单条仿真示范 → 强化学习轨迹编辑器 → 渲染成功轨迹 → 流匹配视觉策略 → 真实 FR3</td>
<td width="220">种子可由遥操作或脚本生成；核心真机策略不依赖大规模人类数据</td>
<td width="300">视觉策略未见类别成功率 90.1%；真机 110 个未见物体总体 86.5%（普通 95.3%，小/薄 71.1%）</td>
<td width="180"><a href="https://openreview.net/forum?id=Bf4FeuW0Mr">论文</a> / <a href="https://beingbeyond.github.io/DemoGrasp/">项目</a> / <a href="https://github.com/BeingBeyond/DemoGrasp">代码</a></td>
</tr>
<tr>
<td width="100" nowrap>ICLR 2026</td>
<td width="260"><a href="https://openreview.net/forum?id=80vjyj5o7l">DexNDM: Closing the Reality Gap for Dexterous In-Hand Rotation via Joint-Wise Neural Dynamics Model</a></td>
<td width="230">缩小跨物体、旋转轴和腕姿态的空中手内旋转交互动力学差距。</td>
<td width="230">从自动负载交互学习逐关节真实动力学，并在仿真策略上训练残差补偿器。</td>
<td width="240">仍需大量真实转移数据；动力学模型未纳入物体形状和触觉反馈。</td>
<td width="280">7 自由度 Franka 机械臂 + LEAP Hand；Chaos Box 负载交互装置</td>
<td width="160">LEAP 16 自由度；位置控制</td>
<td width="220">多旋转轴、多腕姿态的无支撑空中旋转；快速变化的全手接触</td>
<td width="180">无；触觉融合为未来工作</td>
<td width="210">16 维相对关节目标，20 Hz</td>
<td width="330">Isaac Gym PPO 教师与 BC 策略；24K 条真实 Chaos Box 转移轨迹；Genesis/MuJoCo 跨仿真器测试</td>
<td width="240">仿真策略 → 自动真实负载转移 → 逐关节神经动力学 → 残差策略 → 真机</td>
<td width="220">核心旋转链路全自动；Meta Quest 3 机械臂遥操作仅用于下游应用演示</td>
<td width="300">代表性真机 x/y/z 旋转量 6.35/11.32/8.61 rad；跨仿真测试仍显示域敏感性</td>
<td width="180"><a href="https://arxiv.org/abs/2510.08556">论文</a> / <a href="https://meowuu7.github.io/DexNDM/">项目</a></td>
</tr>
<tr>
<td width="100" nowrap>ICLR 2026</td>
<td width="260"><a href="https://openreview.net/forum?id=Kt9tJeOwjy">RFS: Reinforcement learning with Residual flow steering for dexterous manipulation</a></td>
<td width="230">在不破坏预训练行为的前提下微调多模态流策略。</td>
<td width="230">用潜在流引导改变全局模式，并以有界残差动作完成局部修正。</td>
<td width="240">仍需仿真预训练和真实纠错示范；未见物体成功率低于已见。</td>
<td width="280">7 自由度 Franka 机械臂 + LEAP Hand；笛卡尔阻抗控制</td>
<td width="160">已核查论文未说明手部自由度</td>
<td width="220">六项仿真任务；真实抓取与抓取放置，包含接触敏感的手指修正</td>
<td width="180">真机无触觉硬件；仿真观测含二值指尖接触</td>
<td width="210">10 Hz；残差限制为笛卡尔平移 1.5 cm、手指运动 0.05 rad</td>
<td width="330">Isaac Lab；六任务各约 400 条 Vision Pro 示范；两个真机任务各 1,000 条仿真蒸馏示范；50 条真实 SpaceMouse 纠错</td>
<td width="240">Isaac Lab 状态强化学习 → 点云策略蒸馏/随机化 → 零样本真机 → 离线残差/流纠错</td>
<td width="220">Vision Pro 遥操作；SpaceMouse 提供有界纠错干预</td>
<td width="300">仿真平均 0.87；真机已见抓取/抓取放置 90/80%，未见 70/74%；未见零样本基线 40/30%</td>
<td width="180"><a href="https://arxiv.org/abs/2602.01789">论文</a> / <a href="https://weirdlabuw.github.io/rfs/">项目</a></td>
</tr>
<tr>
<td width="100" nowrap>ICLR 2026</td>
<td width="260"><a href="https://openreview.net/forum?id=NZDaMcpXZm">Learning to Grasp Anything By Playing with Random Toys</a></td>
<td width="230">从少量随机组合几何玩具中获得跨物体桌面抓取能力。</td>
<td width="230">LEGO 用检测池化学习物体中心特征，并把玩具数据泛化到夹爪与人形灵巧手的 YCB/日常物体。</td>
<td width="240">仍需每种本体单独采集示范；H1-2 成功率约 51%，部分试验还受 Inspire 拇指关节故障影响。</td>
<td width="280">仿真：Franka + 夹爪；真机：Panda + Robotiq 2F-85；Unitree H1-2 左 7 自由度臂 + Inspire RH56DFTP</td>
<td width="160">Franka 7+1；Inspire 6 主动自由度 / 12 联动关节</td>
<td width="220">桌面抓取抬升；从球体/长方体/圆柱/圆环玩具零样本泛化</td>
<td width="180">Inspire 集成压力传感器，但 LEGO 策略不使用触觉输入</td>
<td width="210">绝对关节/状态动作：Franka 8 维、H1-2 40 维；16 步历史 → 16 动作块；频率未披露</td>
<td width="330">ManiSkill/SAPIEN：250 个玩具、2,500 条仿真示范；真机 1,500 条 Franka 示范、500 条 H1-2 示范</td>
<td width="240">玩具域物体中心 BC → 按本体分别进行真实训练/评测；没有把仿真策略迁移到 H1-2</td>
<td width="220">ManiSkill 脚本/遥操作；Franka 用 Meta Quest 3；H1-2 用 Apple Vision Pro + Unitree XR Teleoperate</td>
<td width="300">仿真 YCB 80%；真实 Franka 66.67%；真实 H1-2 在 13 个物体上 50.77%（每物体 5 次）</td>
<td width="180"><a href="https://arxiv.org/abs/2510.12866">论文</a> / <a href="https://lego-grasp.github.io/">项目</a></td>
</tr>
<tr>
<td width="100" nowrap>ICLR 2026</td>
<td width="260"><a href="https://openreview.net/forum?id=cVX3VqO8BO">UniHM: Unified Dexterous Hand Manipulation with Vision Language Model</a></td>
<td width="230">跨手形态生成开放词汇、多步手-物交互。</td>
<td width="230">学习共享离散动作码本，再以物体中心物理约束细化解码轨迹。</td>
<td width="240">只用 RGB-D，不含触觉/力；接触建模简化，每种新手仍需形态专用编码器/解码器。</td>
<td width="280">重定向 Shadow、Allegro、SVH、LEAP、Panda（附录含 Ability）；真机 7 自由度 Franka + Panda/XHand/Inspire + ZED</td>
<td width="160">真机手：Panda 2、XHand 12、Inspire 6 自由度</td>
<td width="220">开放词汇抓取、抓取放置、拉推、开合交互序列</td>
<td width="180">无；接触来自几何/碰撞约束</td>
<td width="210">8,192 项 VQ 码本 → 手形态专用关节轨迹 → Gauss-Newton 细化；频率未披露</td>
<td width="330">DexYCB 582K 帧、OakInk-Image 230K 帧；80/20 已见/未见划分；SAPIEN 仅用于生成序列可视化/验证</td>
<td width="240">人类 HOI → 共享手词元 → 形态解码/重定向 → 物体轨迹条件化与物理细化 → 真机</td>
<td width="220">离线 DexYCB/OakInk 人类交互数据；无大规模真实机器人遥操作集</td>
<td width="300">真机已见的抓取/抓取放置/拉推/开合为 65/50/60/55%；未见为 60/35/55/45%</td>
<td width="180"><a href="https://arxiv.org/abs/2603.00732">论文</a> / <a href="https://unihm.github.io/">项目</a> / <a href="https://github.com/Zhenhao-Zhang/UniHM">代码</a></td>
</tr>
<tr>
<td width="100" nowrap>ICLR 2026</td>
<td width="260"><a href="https://openreview.net/forum?id=k8ovuXEQQu">House Of Dextra: Cross-Embodied Co-Design for Dexterous Hands</a></td>
<td width="230">联合搜索手形态和控制，同时避免逐候选训练的高成本。</td>
<td width="230">用图语法形态搜索与形态条件 PPO，并制造四种模块化手进行零样本真机部署。</td>
<td width="240">盲本体感觉限制物体状态估计；形态搜索仍依赖任务族，且论文未给出仿真器名称。</td>
<td width="280">生成式固定腕模块手；LEAP 基线；四种真实三维打印手，使用 Dynamixel XL330-M288-T 舵机</td>
<td width="160">3–5 指；每指 2–3 个驱动关节 / 3–4 个舵机</td>
<td width="220">盲手内旋转；仅仿真的抓取与翻转；通过编码器阻力隐式感知接触</td>
<td width="180">无；没有相机或触觉反馈</td>
<td width="210">掩码关节位置命令；闭环本体感觉；控制频率未披露</td>
<td width="330">仿真器未披露；2,000–8,000 个生成形态、50×40 次搜索评测、2,048 个并行随机环境；PPO</td>
<td width="240">跨本体协同搜索 → 域随机化盲策略 → 程序化制造 → PID 调参 → 零样本真机</td>
<td width="220">无</td>
<td width="300">最优三指手旋转 15/17 个未见物体；拟人手和四指手仅 3/17；最佳仿真搜索达 3.3 rad/s</td>
<td width="180"><a href="https://arxiv.org/abs/2512.03743">论文</a> / <a href="https://an-axolotl.github.io/HouseofDextra/">项目</a></td>
</tr>
<tr>
<td width="100" nowrap>ICLR 2026</td>
<td width="260"><a href="https://openreview.net/forum?id=wySMuWHmt4">Primary-Fine Decoupling for Action Generation in Robotic Imitation</a></td>
<td width="230">表示多模态示范，避免模式平均或时间上随机切换。</td>
<td width="230">PF-DAG 预测离散主要模式与连续精细动作，同时提升低/高自由度模仿。</td>
<td width="240">真实分布外物体位置和间歇触觉噪声仍会失败；多个基准也不是统一引擎。</td>
<td width="280">仿真：Adroit Shadow、DexArt Allegro、MetaWorld 夹爪；真机：xArm + 夹爪或 xArm + ROBOTERA XHand + RealSense L515</td>
<td width="160">真机：机械臂+夹爪 7+1；机械臂+XHand 7+12 自由度</td>
<td width="220">56 项抓取/操作任务；真机抓取立方体、放置玩具、擦桌子、触觉箱内放置</td>
<td width="180">XHand：5 指尖 × 120 触觉单元 × 三维力向量；夹爪任务无触觉</td>
<td width="210">30 Hz 绝对关节位置：8 维或 19 维</td>
<td width="330">56 个 Adroit/DexArt/MetaWorld 任务；Adroit/MetaWorld 每任务 10 条专家示范，DexArt 为 90 条；论文未给三套任务统一的引擎映射</td>
<td width="240">不主张仿真到现实；同一主要/精细架构在真实示范上单独训练</td>
<td width="220">xArm+夹爪用 GELLO；XHand 用 Meta Quest 3 手跟踪 + AnyTeleop 重定向</td>
<td width="300">56 任务总体成功率 79.6%；四项真机任务成功率 70/90/70/80%</td>
<td width="180"><a href="https://arxiv.org/abs/2602.21684">论文</a> / <a href="https://xiaohanlei.github.io/projects/PF-DAG/">项目</a> / <a href="https://github.com/XiaohanLei/PF-DAG">代码</a></td>
</tr>
<tr>
<td width="100" nowrap>ICLR 2026</td>
<td width="260"><a href="https://openreview.net/forum?id=13jshGCK9i">D-REX: Differentiable Real-to-Sim-to-Real Engine for Learning Dexterous Grasping</a></td>
<td width="230">为物体特定的力感知灵巧抓取构建数字孪生并辨识动力学。</td>
<td width="230">对重建的 MuJoCo 场景求导以辨识质量，并从重定向人类 RGB 视频学习策略。</td>
<td width="240">证据限于刚体和特定物体；附录对 LEAP 驱动方式表述不一致，小物体仍受位姿/网格误差和手指尺寸限制。</td>
<td width="280">7 自由度 Franka Panda + Allegro Hand 或 LEAP Hand；RealSense D435i 或 iPhone 采集</td>
<td width="160">两种手均为 16 个独立驱动自由度</td>
<td width="220">物体特定的抓取/抬升；位置与力感知接触控制</td>
<td width="180">无触觉阵列；以视觉位姿及电机电流/力矩限制作为力代理</td>
<td width="210">16 维关节目标 + 接触/力条件；控制频率未披露；单姿态推理约 0.5 s，不能视为控制频率</td>
<td width="330">MuJoCo 可微物理 + Brax 策略训练 + GradSim 重建；每场景约 300 张图像、每物体 200–300 个抓取姿态</td>
<td width="240">真实扫描 → 高斯/网格数字孪生 → 可微质量辨识 → 人类视频重定向 → 力感知仿真策略 → 真机</td>
<td width="220">人类 RGB 视频 → 手/物位姿提取 → Dex-Retargeting 机器人示范</td>
<td width="300">真实平均成功率 86%，基线为 75/76%；分布外三物体为 9/10、10/10、9/10</td>
<td width="180"><a href="https://arxiv.org/abs/2603.01151">论文</a> / <a href="https://drex.github.io/">项目</a> / <a href="https://github.com/louhz/D-rex">代码</a></td>
</tr>
<tr>
<td width="100" nowrap>AAAI 2026</td>
<td width="260"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38874">Dexterous Manipulation Transfer via Progressive Kinematic-Dynamic Alignment</a></td>
<td width="230">把人类操作视频迁移到不同灵巧手，同时维持稳定接触动力学。</td>
<td width="230">PKDA 结合运动学重定向、拇指引导预抓取、接触残差强化学习与腕轨迹规划。</td>
<td width="240">Allegro/LEAP 对小或细长物体仍困难；变化多接触仍是开放问题，真机结果仅定性。</td>
<td width="280">仿真：Adroit、Allegro、LEAP Hand；真机：UR10 机械臂 + LEAP Hand</td>
<td width="160">Adroit 24；Allegro/LEAP 16 自由度</td>
<td width="220">抓取、手内/关节物体操作、物体跟随；包含变化的指尖接触</td>
<td width="180">无触觉硬件；接触点/奖励来自视频估计与仿真</td>
<td width="210">动作前 6 维控制腕部，其余为手指关节；MuJoCo 控制 120 Hz</td>
<td width="330">MuJoCo；约 600 条 GRAB、40 条 TCDM、10 条 DexYCB、10 条 TACO、5 条自采轨迹</td>
<td width="240">视频感知 → 手重定向 → MuJoCo 残差强化学习/接触对齐 → 腕规划 → 真机开环回放</td>
<td width="220">离线人类视频/数据集；无在线遥操作</td>
<td width="300">Adroit/Allegro/LEAP 迁移成功率 77.5/72.5/67.5%；真实 LEAP 仅定性展示</td>
<td width="180"><a href="https://arxiv.org/abs/2511.10987">论文</a> / <a href="https://ojs.aaai.org/index.php/AAAI/article/view/38874">AAAI</a></td>
</tr>
<tr>
<td width="100" nowrap>AAAI 2026</td>
<td width="260"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38892">Learning Object-Centric Motion Priors from Human for Robotic Dexterous Manipulation</a></td>
<td width="230">从 HOI 数据学习可复用的物体中心运动先验，减少逐任务奖励设计。</td>
<td width="230">GPT-2 预测未来手-物体状态；物体跟随奖励引导 PPO 覆盖抓取、铰接、避障和跨手型任务。</td>
<td width="240">依赖 6 自由度物体位姿跟踪、标定重定向和逐手型系统辨识；接触只来自碰撞检测。</td>
<td width="280">双 xArm-7；每臂可装 PSYONIC Ability、ROBOTERA XHand1 或 Inspire 手；RealSense D435i</td>
<td width="160">每臂 7 自由度；论文未报手部自由度</td>
<td width="220">抓取/抬升、铰接物体旋转、无碰撞抓取、跨手型迁移</td>
<td width="180">无；仅 SAPIEN 碰撞接触</td>
<td width="210">末端增量位姿 + 手关节增量；频率未披露</td>
<td width="330">SAPIEN3 + OpenAI Gymnasium；1,024 并行环境；PPO 训练 1M 步；DexYCB 和 ARCTIC HOI 数据</td>
<td width="240">HOI 预测 → 本体专用重定向 → 系统辨识与域随机化 PPO → 真实零样本</td>
<td width="220">离线 DexYCB/ARCTIC 人-物数据；无在线遥操作</td>
<td width="300">抓取仿真/真实 84%/77%；铰接 66%/53%；避障抓取 66%/63%</td>
<td width="180"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38892">AAAI</a></td>
</tr>
<tr>
<td width="100" nowrap>AAAI 2026</td>
<td width="260"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38953">DexGraspVLA: A Vision-Language-Action Framework Towards General Dexterous Grasping</a></td>
<td width="230">让语言引导灵巧抓取泛化到未见物体、杂乱、光照与背景。</td>
<td width="230">预训练视觉语言模型规划目标框/掩码，DINOv2 条件 DiT 控制器执行抓取、长时程和非抓取式任务。</td>
<td width="240">仅真实单一臂手平台评估，无触觉；硬件代码未公开。</td>
<td width="280">7 自由度 RealMan RM75-6F + 6 自由度 PsiBot G0-R；腕部 D405C + 头部 D435</td>
<td width="160">共 13 自由度：臂 7 + 手 6</td>
<td width="220">杂乱抓取/抬升、多次尝试、长时程任务链、非抓取式操作</td>
<td width="180">无</td>
<td width="210">13-D 目标关节角；DiT 动作块 20 Hz</td>
<td width="330">仅真实：2,094 条成功抓取示范/36 物体；另有 1,029 条非抓取式示范/32 物体</td>
<td width="240">不适用：直接在真实平台训练与评估</td>
<td width="220">运动示教；规划器把语言/RGB 转为跨域掩码</td>
<td width="300">单次 90.8%；最多 3 次 96.9%；长时程 89.6%；非抓取式 84.7%</td>
<td width="180"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38953">论文</a> / <a href="https://dexgraspvla.github.io/">项目</a> / <a href="https://github.com/Psi-Robot/DexGraspVLA">代码</a></td>
</tr>
<tr>
<td width="100" nowrap>CVPR 2026</td>
<td width="260"><a href="https://arxiv.org/abs/2603.22264">UniDex: A Robot Foundation Suite for Universal Dexterous Hand Control from Egocentric Human Videos</a></td>
<td width="230">降低机器人示范成本，并统一异构灵巧手控制。</td>
<td width="230">UniDex-Dataset、82-D FAAS、UniDex-VLA 与 UniDex-Cap 组成完整的人类视频到机器人链路。</td>
<td width="240">仍需人工在环重定向和逐手型执行器映射；没有触觉/力反馈。</td>
<td width="280">数据：Allegro、Ability、Inspire、LEAP、OYMotion、Shadow、Wuji、XHand；真实 Franka + Inspire/Wuji/OYMotion + L515</td>
<td width="160">8 种手；6–24 主动自由度</td>
<td width="220">5 个工具使用/多阶段任务；保持接触的跨手型迁移</td>
<td width="180">无</td>
<td width="210">82-D FAAS 动作块；机器人控制频率未披露</td>
<td width="330">H2O、HOI4D、HOT3D、TACO 等第一视角数据：52K 轨迹/9M 帧；PyBullet IK；5 真实任务×50 示范</td>
<td width="240">指尖/接触对齐 + 人工修正 + 去人手点云；再由 FAAS 解码到各手型</td>
<td width="220">30 fps 人类视频；Apple Vision Pro/OpenTeleVision 和 UniDex-Cap 采下游示范</td>
<td width="300">平均进度 81%、成功率 76%；π0 为 38%/35%；零样本跨手成功率 60% 和 40%</td>
<td width="180"><a href="https://arxiv.org/abs/2603.22264">论文</a> / <a href="https://unidex-ai.github.io/">项目</a> / <a href="https://github.com/unidex-ai/UniDex">代码</a> / <a href="https://huggingface.co/UniDex-ai/UniDex">数据</a></td>
</tr>
<tr>
<td width="100" nowrap>NeurIPS 2025</td>
<td width="260"><a href="https://arxiv.org/abs/2511.01276">Contact Map Transfer with Conditional Diffusion Model for Generalizable Dexterous Grasp Generation</a></td>
<td width="230">无需逐抓取优化，为新物体生成稳定、任务条件化抓取。</td>
<td width="230">级联扩散从形状模板迁移接触图、部件图和方向图，再由鲁棒恢复优化手部位姿。</td>
<td width="240">依赖同类形状模板；无触觉反馈；自研人形和 Inspire 手具体型号未披露。</td>
<td width="280">仿真 ShadowHand；真实自研人形 + Inspire 手；ZED 头部相机 + 两个 RealSense</td>
<td width="160">Shadow：24 手参数 + 6-D 根位姿；真实手自由度未报</td>
<td width="220">基于物体接触图的静态任务条件化力量/功能抓取</td>
<td width="180">无；接触图是几何条件</td>
<td width="210">24-D 手配置 + SE(3) 手根位姿；执行频率未披露</td>
<td width="330">CapGrasp：约 1.8K 物体/约 50K 模板-新物体对；Isaac Gym 稳定性筛选/评估</td>
<td width="240">模板图迁移 + 抓取恢复；真实 Inspire 执行链路未单独说明</td>
<td width="220">无遥操作；模板/抓取数据均为离线</td>
<td width="300">已见/未见 SR 79.32%/74.14%；任务一致性 83.60%/79.28%；真实成功率 70%</td>
<td width="180"><a href="https://arxiv.org/abs/2511.01276">论文</a> / <a href="https://cmtdiffusion.github.io/">项目</a> / <a href="https://github.com/Yiyao-Ma/cmtdiffusion">代码</a></td>
</tr>
<tr>
<td width="100" nowrap>NeurIPS 2025</td>
<td width="260"><a href="https://arxiv.org/abs/2506.02489">Grasp2Grasp: Vision-Based Dexterous Grasp Translation via Schrödinger Bridges</a></td>
<td width="230">在人手和不同机器人手形态间迁移功能等价抓取。</td>
<td width="230">视觉条件薛定谔桥学习人类→Allegro、人类→Shadow、Shadow→Allegro 映射。</td>
<td width="240">新手型仍需目标域训练；仅仿真静态抓取，无触觉。</td>
<td width="280">仿真人手、Allegro Hand、Shadow Hand；无载体机械臂</td>
<td width="160">人手 20；Allegro 16；Shadow 22 + SE(3) 基座</td>
<td width="220">跨形态静态抓取迁移及稳定性/接触保持</td>
<td width="180">无</td>
<td width="210">生成手关节位姿 + SE(3) 基座位姿；无控制频率</td>
<td width="330">MultiGripperGrasp：30.4M 抓取、11 种手、345 物体；Warp Jacobian + Isaac Gym 稳定性测试</td>
<td width="240">仅仿真跨手型迁移；无真实迁移</td>
<td width="220">数据集中的人手抓取位姿；无遥操作</td>
<td width="300">三种跨手设置 SR 77.23%/45.15%/79.98%（均值 67.45%）；每抓取约 0.8 s</td>
<td width="180"><a href="https://arxiv.org/abs/2506.02489">论文</a> / <a href="https://grasp2grasp.github.io/">项目</a> / <a href="https://github.com/n3il666/grasp2grasp">代码</a></td>
</tr>
<tr>
<td width="100" nowrap>NeurIPS 2025</td>
<td width="260"><a href="https://arxiv.org/abs/2506.19212">Scaffolding Dexterous Manipulation with Vision-Language Models</a></td>
<td width="230">用视觉语言模型生成操作支架，替代逐任务奖励和人类示范。</td>
<td width="230">视觉语言模型提议关键点及腕部/物体轨迹；残差闭环强化学习跟踪轨迹并零样本迁移到硬件。</td>
<td width="240">视觉语言模型关键点和轨迹误差仍是主因；仅 3 个真实任务，无触觉/力反馈。</td>
<td width="280">16 自由度 Allegro + 7 自由度 KUKA LBR iiwa 14 + 桌面固定 ZED 1 双目相机</td>
<td width="160">共 23 自由度：臂 7 + 手 16</td>
<td width="220">语义放置、铰接开启、滑动/锤击、剪刀/钳子操作</td>
<td width="180">无</td>
<td width="210">腕部 SE(3) + 手指位置/残差；策略 60 Hz，物理 120 Hz</td>
<td width="330">ManiSkill3/ReplicaCAD；2,048 环境；8 任务；100 初态×20 轨迹展开×3 随机种子</td>
<td width="240">数字孪生 + 域随机化；低层策略完全在仿真训练</td>
<td width="220">无人类示范；视觉语言模型从单张 RGB-D 场景生成计划</td>
<td width="300">仿真均值 72%，迭代后 81%；真实放置/滑动/锤击 90%/85%/65%（各 20 次）</td>
<td width="180"><a href="https://arxiv.org/abs/2506.19212">论文</a> / <a href="https://sites.google.com/view/dexterous-vlm-scaffolding">项目</a> / <a href="https://github.com/vdebakker/vlm-scaffolding">代码</a></td>
</tr>
<tr>
<td width="100" nowrap>NeurIPS 2025</td>
<td width="260"><a href="https://arxiv.org/abs/2505.11032">DexGarmentLab: Dexterous Garment Manipulation Environment with Generalizable Policy</a></td>
<td width="230">提供可扩展的双手灵巧衣物任务、数据生成和仿真到真实策略。</td>
<td width="230">DexGarmentLab 提供衣物资产/15 个任务场景；HALO 结合可供性定位与形状自适应扩散轨迹。</td>
<td width="240">每次仅一件衣物；可变形仿真到现实、目标区域抓取和精确放置仍较弱。</td>
<td width="280">仿真：双 UR10e + ShadowHand。真实 A：双 RealMan RM75-6F + PsiBot G0-R + D435。真实 B：双 UR10e + ShadowHand + Azure Kinect</td>
<td width="160">仿真动作 60-D；真实 A 每侧臂 7 + 手 6 自由度</td>
<td width="220">双手抖开、折叠、悬挂、穿戴及衣物-环境交互</td>
<td width="180">无</td>
<td width="210">每侧 6-D 臂位姿 + 24 手关节；频率未披露</td>
<td width="330">Isaac Sim 4.5.0；2,500+ 衣物/8 类/15 任务；每任务 1 条种子示范扩为 100 条示范</td>
<td width="240">UR10e/Shadow 匹配数字孪生；每任务加 15 条真实示范后两项均升至 13/15</td>
<td width="220">Leap Motion 提供 1 条 ShadowHand 种子；自动执行扩充示范</td>
<td width="300">真实 A：13/15、13/15、11/15、14/15。真实 B 仅仿真：8/15、9/15；+15 真实：13/15、13/15</td>
<td width="180"><a href="https://arxiv.org/abs/2505.11032">论文</a> / <a href="https://wayrise.github.io/DexGarmentLab/">项目</a> / <a href="https://github.com/wayrise/DexGarmentLab">代码</a> / <a href="https://huggingface.co/datasets/wayrise/DexGarmentLab">数据</a></td>
</tr>
<tr>
<td width="100" nowrap>CVPR 2025</td>
<td width="260"><a href="https://arxiv.org/abs/2412.02699">UniGraspTransformer: Simplified Policy Distillation for Scalable Dexterous Robotic Grasping</a></td>
<td width="230">把数千个物体专用抓取专家蒸馏为单一可扩展策略。</td>
<td width="230">逐物体 PPO 教师生成轨迹；Transformer 学生完成状态/点云条件的已见与未见物体抓取。</td>
<td width="240">仅 ShadowHand 仿真；无真实迁移和触觉，状态版还假设可得物体状态。</td>
<td width="280">桌面上方悬浮仿真 Shadow Hand；无载体机械臂</td>
<td width="160">24 执行器：腕部 6 + 主动手指 18 自由度</td>
<td width="220">接近、包络抓取并抬升至目标高度</td>
<td width="180">无</td>
<td width="210">24-D：腕部力/力矩 6 + 手指关节位置 18；频率未报</td>
<td width="330">Isaac Gym 3.0；3,200 物体；3.2M 条成功轨迹，每条 200 步</td>
<td width="240">仅仿真；无仿真到现实链路</td>
<td width="220">无人类/遥操作数据</td>
<td width="300">状态版已见/同类未见/新类 91.2%/89.2%/88.3%；视觉版 88.9%/87.3%/86.8%</td>
<td width="180"><a href="https://arxiv.org/abs/2412.02699">论文</a> / <a href="https://dexhand.github.io/UniGraspTransformer/">项目</a> / <a href="https://github.com/microsoft/UniGraspTransformer">代码</a></td>
</tr>
<tr>
<td width="100" nowrap>CVPR 2025</td>
<td width="260"><a href="https://arxiv.org/abs/2503.08257">DexGrasp Anything: Towards Universal Robotic Dexterous Grasping with Physics Awareness</a></td>
<td width="230">为任意物体生成多样且物理稳定的灵巧抓取。</td>
<td width="230">物理感知扩散加入穿透/接触约束和大语言模型物体先验；DGA 扩至 3.40M 位姿。</td>
<td width="240">无触觉；真实 ShadowHand 仅定性测试，载体硬件和控制频率未披露。</td>
<td width="280">数据、Isaac Gym 评估及定性真实部署均用 ShadowHand；载体未报</td>
<td width="160">24-D 手位姿 + 全局旋转/平移</td>
<td width="220">静态通用抓取位姿生成与六方向稳定性</td>
<td width="180">无</td>
<td width="210">生成 q∈R24 及全局 R,t；无在线控制频率</td>
<td width="330">DGA：3.40M 位姿/15,698 物体；Isaac Gym 过滤/评估；真实+仿真来源</td>
<td width="240">GRAB 人手位姿重定向到 ShadowHand；真实预抓取执行沿用既有流程</td>
<td width="220">离线 GRAB 人体捕捉；无在线遥操作</td>
<td width="300">大语言模型版在 MultiDex 上 Suc.6/Suc.1 为 79.1%/98.1%；跨数据集 Suc.6 为 58.6%/53.4%</td>
<td width="180"><a href="https://arxiv.org/abs/2503.08257">论文</a> / <a href="https://dexgraspanything.github.io/">项目</a> / <a href="https://github.com/4DVLab/DexGrasp-Anything">代码</a> / <a href="https://huggingface.co/datasets/GaussionZhong/DexGrasp-Anything">数据</a></td>
</tr>
<tr>
<td width="100" nowrap>arXiv 2025 (v2 2026)</td>
<td width="260"><a href="https://arxiv.org/abs/2602.16710">EgoScale: Scaling Dexterous Manipulation with Diverse Egocentric Human Data</a></td>
<td width="230">把第一视角人类视频预训练扩展到高自由度灵巧操作和新本体。</td>
<td width="230">大规模人类预训练、对齐的人机中训练和少量机器人后训练支持单次适应与 G1 迁移。</td>
<td width="240">无仿真和触觉；数据需求大、频率未报，且未找到正式会议。</td>
<td width="280">Galaxea R1Pro：双 7 自由度臂 + 双 22 自由度 Sharpa Wave；迁移为 Unitree G1 + 7 自由度三指手；OAK 相机</td>
<td width="160">R1Pro 每侧臂 7 + 手 22；G1 手 7</td>
<td width="220">双手长时程灵巧操作、单次任务适应、跨本体工具/物体任务</td>
<td width="180">未报告</td>
<td width="210">每臂相对 SE(3) + 手关节；频率未披露</td>
<td width="330">仅真实：阶段 I 20,854 h/9,869 场景/6,015 任务/43,237 物体；阶段 II 50 h 人 + 4 h 机器人；后训练 100 条机器人示范</td>
<td width="240">人腕/手重定向到 Sharpa 空间；本体适配器对齐 G1 手及动作空间</td>
<td width="220">带动作标签的第一视角人类视频 + 对齐的人类/机器人自由交互数据</td>
<td width="300">R1Pro 完成度/成功率 .83/.56，对照无预训 .24/.02；G1 两任务 .83/.67 与 .88/.50</td>
<td width="180"><a href="https://arxiv.org/abs/2602.16710">论文</a> / <a href="https://research.nvidia.com/labs/gear/egoscale/">项目</a></td>
</tr>
<tr>
<td width="100" nowrap>CVPR 2026</td>
<td width="260"><a href="https://openaccess.thecvf.com/content/CVPR2026/papers/Jiang_Cross-Hand_Latent_Representation_for_Vision-Language-Action_Models_CVPR_2026_paper.pdf">Cross-Hand Latent Representation for Vision-Language-Action Models (XL-VLA)</a></td>
<td width="230">让不同关节结构的灵巧手共享同一 VLA 动作空间。</td>
<td width="230">共享 32-D 潜空间配合手型专用编码/解码器，支持四手型共训及零样本手型-任务组合。</td>
<td width="240">仍需逐手型适配器和示范；仅真实评估，无触觉。</td>
<td width="280">双 xArm7 搭配 Ability、Inspire、X-Hand1 或 Paxini DexH13；另测 Unitree G1 跨机器人</td>
<td width="160">Ability 12（6 个耦合关节）、Inspire 12（6）、XHand 12、Paxini 16（3）</td>
<td width="220">10 个双手灵巧任务；跨手轨迹回放/接触保持</td>
<td width="180">无</td>
<td width="210">64 帧绝对关节指令、20 Hz（3.2 s），编码为 32-D 潜变量</td>
<td width="330">仅真实：10 任务×4 手型×50 示范 = 2,000 条示范/约 2M 状态-动作对</td>
<td width="240">FK 约束共享潜空间直接解码至各手型；无仿真</td>
<td width="220">Apple Vision Pro + Bunny-VisionPro 遥操作</td>
<td width="300">均值 0.72，π0 为 0.32；Ability/Inspire/Paxini/XHand 为 .73/.68/.78/.70；G1 约 .825 对比 .525</td>
<td width="180"><a href="https://openaccess.thecvf.com/content/CVPR2026/papers/Jiang_Cross-Hand_Latent_Representation_for_Vision-Language-Action_Models_CVPR_2026_paper.pdf">论文</a> / <a href="https://xl-vla.github.io/">项目</a> / <a href="https://github.com/EmptyBlueBox/DexLatent">代码</a></td>
</tr>
<tr>
<td width="100" nowrap>ECCV 2026</td>
<td width="260"><a href="https://arxiv.org/abs/2512.13644">World Models for Learning Dexterous Hand-Object Interactions from Human Videos (DexWM)</a></td>
<td width="230">从人类视频学习灵巧交互动力学，用于目标条件机器人规划。</td>
<td width="230">稠密手关键点动作和手一致性损失让单个潜世界模型支持 CEM/MPC 及真实零样本抓取。</td>
<td width="240">默认 CEM 每回合规划 168 s；无触觉，RoboCasa 仅右侧手活动。</td>
<td width="280">RoboCasa：双 Franka + 双 Allegro，但仅右侧活动。真实：Franka Panda + Allegro 手</td>
<td width="160">规划器：臂 7 + 手 16 = 23 关节</td>
<td width="220">到达、抓取、放置；基于预测手-物运动的图像目标规划</td>
<td width="180">无</td>
<td width="210">世界动作 132-D MANO/相机关键点、5 Hz；规划输出 23-D 关节</td>
<td width="330">EgoDex 829 h + DROID 约 100 h 预训；RoboCasa 约 4 h 随机探索微调；无真实微调</td>
<td width="240">Allegro 映射到五指关键点空间；CEM/MPC 以关节目标零样本执行到真实</td>
<td width="220">EgoDex Vision Pro 人类视频 + DROID 机器人视频；RoboCasa 数据无需遥操作</td>
<td width="300">仿真到达/抓取/放置 72%/28%/58%，DP 为 16%/8%/0%；真实 10/12（83%）；默认规划 168 s</td>
<td width="180"><a href="https://arxiv.org/abs/2512.13644">论文</a> / <a href="https://raktimgg.github.io/dexwm/">项目</a></td>
</tr>
<tr>
<td width="100" nowrap>arXiv 2026</td>
<td width="260"><a href="https://arxiv.org/abs/2512.24210">GR-Dexter Technical Report</a></td>
<td width="230">在机器人数据稀缺下为 21 自由度仿人手构建双手 VLA。</td>
<td width="230">ByteDexter V2、整手遥操作及机器人/VL/跨本体/人类共训组成 56 自由度真实系统。</td>
<td width="240">技术报告，无公开代码/数据/软件开发工具包；报告的 VLA 未使用指尖触觉阵列。</td>
<td width="280">双 Franka Research 3 + 双 ByteDexter V2；Meta Quest 头显/控制器 + Manus Metagloves</td>
<td width="160">每手 21 机械/16 主动自由度；整机 56 机械自由度</td>
<td width="220">双手化妆台整理、长时程工具使用、泛化拾放</td>
<td width="180">每手 5 个高密度压阻式指尖法向力阵列；未作为策略输入</td>
<td width="210">88-D：臂关节/末端位姿 + 每侧 16 手关节 + 指尖位置；频率未报</td>
<td width="330">仅真实；每项自采约 20 h；ActionNet 约 140 h、OpenLoong 100K+、RoboMIND 107K 示范、人类视频 800+ h</td>
<td width="240">无仿真；相机标准化 + 指尖中心重定向把外部本体对齐至 ByteDexter</td>
<td width="220">Meta Quest + Manus 双手遥操作；第一视角人类轨迹</td>
<td width="300">化妆台基础/分布外 .97/.89，普通为 .96/.64；拾放基础/未见物体/未见指令 .93/.85/.83</td>
<td width="180"><a href="https://arxiv.org/abs/2512.24210">论文</a> / <a href="https://byte-dexter.github.io/gr-dexter/">项目</a></td>
</tr>
<tr>
<td width="100" nowrap>arXiv 2025</td>
<td width="260"><a href="https://arxiv.org/abs/2511.01177">Scaling Cross-Embodiment World Models for Dexterous Manipulation</a></td>
<td width="230">统一运动学与动作空间不兼容的不同手型的数据、动力学和规划。</td>
<td width="230">手/物粒子与位移动作让同一 GNN 世界模型共训仿真机器人和真实人手，再规划到未见硬件。</td>
<td width="240">仅测试推物和橡皮泥原语；无触觉、二值成功率或正式会议。</td>
<td width="280">仿真：Ability、Allegro、XHand、LEAP、Shadow + 第二种 Shadow 变体。真实：xArm7 + Ability 或 XHand + 4 个 RealSense</td>
<td width="160">各手 6/16/12/16/24 自由度</td>
<td width="220">刚体推物；橡皮泥 ThumbPinch、FingersPinch、PalmPress</td>
<td width="180">无</td>
<td width="210">手/物粒子 + 末端位移场；CEM；频率未报</td>
<td width="330">SAPIEN 刚体推物 + Rewarped 橡皮泥；每任务 100 条随机轨迹；每个人类原语 30 分钟</td>
<td width="240">FK 把关节映射到共享粒子；同一世界模型无需目标微调即可规划 Ability/XHand</td>
<td width="220">真实人手示范；无机器人遥操作</td>
<td width="300">共训 CD/EMD（×10⁻³）：Ability 6.95/4.92 对比 仅人类 7.15/5.23；XHand 6.85/4.78 对比 7.22/5.18</td>
<td width="180"><a href="https://arxiv.org/abs/2511.01177">论文</a></td>
</tr>
</tbody>
</table>
