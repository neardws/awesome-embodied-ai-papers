# 触觉与接触丰富操作

[首页](../../../README.zh-CN.md) | [英文](../../en/embodiment/tactile-contact.md) | [方向目录](README.md)

共计 28 篇。

方向特有列分别标注传感规格、融合位置、反馈阶段/频率和触觉增益；“未披露”表示已核查的论文或官方项目源没有提供该细节。

<table width="3520">
<thead>
<tr>
<th width="100" nowrap>会议/年份</th>
<th width="260">论文/方法</th>
<th width="230">研究问题</th>
<th width="300">具体机器人 / 末端 / 传感器</th>
<th width="280">触觉信号规格</th>
<th width="220">接触 / 感知任务</th>
<th width="300">融合架构 / 位置</th>
<th width="220">闭环阶段 / 控制频率</th>
<th width="200">动作 / 控制接口</th>
<th width="330">仿真 / 训练环境 + 数据规模</th>
<th width="110">仿真 / 实机角色</th>
<th width="320">触觉增益 / 任务核心指标</th>
<th width="230">已解决 / 进展</th>
<th width="240">局限</th>
<th width="180">资源</th>
</tr>
</thead>
<tbody>
<tr>
<td width="100" nowrap>CoRL 2024</td>
<td width="260"><a href="https://arxiv.org/abs/2410.24091">3D-ViTac: Learning Fine-Grained Manipulation with Visuo-Tactile Sensing</a></td>
<td width="230">从空间对齐的视觉与触觉中学习精细操作。</td>
<td width="300">双主从机械臂；软鳍式二指夹爪；4 块自制 Velostat 触觉垫；多视角 RealSense RGB-D。</td>
<td width="280">4 块 16x16 触觉垫，共 1,024 点；每点 3 mm²；触觉 ROS 以 30 Hz 发布（传感器最高 32.2 FPS），同步示范为 10 Hz。</td>
<td width="220">4 项精细操作，包括蒸蛋、插入和取葡萄等。</td>
<td width="300">三维触觉点与 RGB-D 点云经 PointNet++ 编码，在扩散策略之前融合。</td>
<td width="220">闭环轨迹展开；策略频率未单独披露。触觉 ROS 以 30 Hz 发布（传感器最高 32.2 FPS），同步示范为 10 Hz。</td>
<td width="200">双从端机械臂和夹爪的关节/动作块。</td>
<td width="330">仅实机；4 项任务分别为 30/30/30/50 条示范；每项评测 20 次。</td>
<td width="110">仅实机</td>
<td width="320">4 项任务成功率 85/80/90/85%，仅 RGB 输入为 50/45/45/60%。</td>
<td width="230">把分布式触觉统一为三维点表示，用于精细策略学习。</td>
<td width="240">依赖定制双臂硬件，且评测仅覆盖 4 项任务。</td>
<td width="180"><a href="https://arxiv.org/abs/2410.24091">论文</a> / <a href="https://binghao-huang.github.io/3D-ViTac/">项目</a> / <a href="https://github.com/binghao-huang/3D-ViTac_Tactile_Hardware">硬件</a></td>
</tr>
<tr>
<td width="100" nowrap>CoRL 2022</td>
<td width="260"><a href="https://arxiv.org/abs/2210.14210">MidasTouch: Monte-Carlo Inference over Distributions across Sliding Touch</a></td>
<td width="230">在滑动接触过程中完成触觉传感器的全局物体表面定位。</td>
<td width="300">手持 DIGIT + OptiTrack；没有机器人执行操作。</td>
<td width="280">DIGIT 240x320 RGB 触觉图像；实采 30 Hz；在线推理约 10 Hz。</td>
<td width="220">YCB 物体上的滑动触觉定位。</td>
<td width="300">触觉图像转局部高度图和几何编码；粒子滤波随时间整合位姿假设。</td>
<td width="220">约 10 Hz 的在线状态估计闭环；没有机器人操作控制闭环。</td>
<td width="200">人手引导滑动；方法输出传感器位姿分布。</td>
<td width="330">TACTO：40 个 YCB x 5,000 次接触 = 20 万；YCB-Slide：50 条仿真 + 50 条真实序列。</td>
<td width="110">仿真训练 + 实机评测</td>
<td width="320">仿真/真实最终误差分别为 0.74 cm / 9.43° 和 1.97 cm / 21.48°。</td>
<td width="230">实现仅依赖触觉滑动观测的在线全局定位。</td>
<td width="240">依赖已知物体几何和人手滑动，并非闭环操作策略。</td>
<td width="180"><a href="https://arxiv.org/abs/2210.14210">论文</a> / <a href="https://suddhu.github.io/midastouch-tactile/">项目</a> / <a href="https://github.com/facebookresearch/MidasTouch">代码</a></td>
</tr>
<tr>
<td width="100" nowrap>CoRL 2022</td>
<td width="260"><a href="https://proceedings.mlr.press/v205/zhong23a.html">Touching a NeRF: Leveraging Neural Radiance Fields for Tactile Sensory Data Generation</a></td>
<td width="230">从视觉物体模型生成可用触觉观测，减少真实接触采集。</td>
<td width="300">Franka Panda + DIGIT + RealSense D415；OmniTact 只用于仿真迁移实验。</td>
<td width="280">DIGIT 光学触觉图像；398 次真实接触产生 19,900 帧；论文未单列采集频率。</td>
<td width="220">触觉图像生成与下游物体分类。</td>
<td width="300">每物体 NeRF 渲染 RGB-D，条件 GAN 将几何映射为触觉图像并增强分类器。</td>
<td width="220">无闭环控制；机器人接触只用于采集数据。</td>
<td width="200">脚本化末端接触；学习输出为触觉图像/类别。</td>
<td width="330">TACTO（PyBullet + PyRender）：27 个 YCB x 500 次接触；真实 9 物体、398 次接触、1.99 万帧。</td>
<td width="110">仿真增强 + 实机评测</td>
<td width="320">分类准确率在仿真中 85→96%，真实数据上 74→83%。</td>
<td width="230">利用 NeRF 几何合成能提升触觉感知的训练数据。</td>
<td width="240">每个物体都要训练 NeRF，只覆盖刚体，也没有学习接触控制。</td>
<td width="180"><a href="https://proceedings.mlr.press/v205/zhong23a.html">论文</a> / <a href="https://proceedings.mlr.press/v205/zhong23a/zhong23a.pdf">PDF</a></td>
</tr>
<tr>
<td width="100" nowrap>CoRL 2020 (PMLR 2021)</td>
<td width="260"><a href="https://arxiv.org/abs/2012.05205">Tactile object pose estimation from the first touch with geometric contact rendering</a></td>
<td width="230">用单次触觉压痕和少量真实数据估计物体位姿。</td>
<td width="300">固定 GelSlim + 四轴定位台；没有自主机器人策略。</td>
<td width="280">GelSlim 470x470、90 Hz；网络输入 200x200；渲染/接触深度范围 0–2 mm。</td>
<td width="220">首次接触的物体位姿估计。</td>
<td width="300">几何接触渲染器生成训练压痕，供纯触觉位姿估计器学习。</td>
<td width="220">否；一次接触后直接估计位姿。</td>
<td width="200">定位台按程序接触，随后前馈预测位姿。</td>
<td width="330">自研几何渲染器；每物体至少 150 次真实接触和 5k–20k 条仿真样本。</td>
<td width="110">仿真训练 + 实机评测</td>
<td width="320">销钉物体的平移中位误差为 4.8 mm；论文另报各物体位姿误差。</td>
<td width="230">证明几何合成接触可支持准确的首次触觉定位。</td>
<td width="240">需要逐物体训练和固定接触装置，不覆盖连续操作。</td>
<td width="180"><a href="https://arxiv.org/abs/2012.05205">论文</a> / <a href="https://proceedings.mlr.press/v155/villalonga21a.html">PMLR</a> / <a href="http://mcube.mit.edu/research/tactile_loc_first_touch.html">项目</a></td>
</tr>
<tr>
<td width="100" nowrap>CoRL 2022</td>
<td width="260"><a href="https://arxiv.org/abs/2210.01116">That Sounds Right: Auditory Self-Supervision for Dynamic Robot Manipulation</a></td>
<td width="230">把接触声音作为动态操作行为选择的自监督信号。</td>
<td width="300">UR10 机械臂 + 接触麦克风；没有触觉单元触觉阵列。</td>
<td width="280">4 秒音频以 44.1 kHz 采集并下采样到 11 kHz；接触事件是声学信号。</td>
<td width="220">根据目标声音选择动态接触行为。</td>
<td width="300">BYOL 风格音频编码器把目标声音映射到参数化运动基元。</td>
<td width="220">执行前只映射一次音频到基元；后续运动是开环。</td>
<td width="200">选择并执行参数化动态运动基元。</td>
<td width="330">无仿真；约 2.5 万条带同步接触声音的真实机器人行为。</td>
<td width="110">仅实机</td>
<td width="320">采用音频/轨迹 MSE 与 DTW 评测；论文没有报告操作成功率。</td>
<td width="230">无需人工语义标签即可用接触声音学习动态行为选择。</td>
<td width="240">声音是间接接触感知，执行阶段没有声音反馈闭环。</td>
<td width="180"><a href="https://arxiv.org/abs/2210.01116">论文</a> / <a href="https://audio-robot-learning.github.io">项目</a></td>
</tr>
<tr>
<td width="100" nowrap>ICLR 2026</td>
<td width="260"><a href="https://openreview.net/forum?id=dT3ZciXvNX">DexMove: Learning Tactile-Guided Non-Prehensile Manipulation with Dexterous Hands</a></td>
<td width="230">用稀缺触觉示范学习非抓取式物体移动。</td>
<td width="300">Franka Research 3 + Allegro Hand + RealSense D435i，并使用 R-Tac 衍生的人手/指尖触觉硬件。</td>
<td width="280">每指跟踪 33 个标记点的 4 向位移，30 FPS。</td>
<td width="220">不抓取地移动 6 种桌面物体，并演示整理/归类。</td>
<td width="300">TaFo-Net 编码触觉力线索，与视觉/本体状态在流策略中融合。</td>
<td width="220">实机策略以 30 Hz 闭环运行。</td>
<td width="200">FR3 + Allegro 的机械臂/手动作轨迹。</td>
<td width="330">MuJoCo：352 种布局、41.2 万接触配置；约 30 万帧人类触觉数据。</td>
<td width="110">仿真增强 + 实机执行</td>
<td width="320">6 种物体实机成功率 77.8%，比论文消融高 36.6 个百分点。</td>
<td width="230">结合筛选后的合成轨迹与真实触觉示范实现非抓取灵巧操作。</td>
<td width="240">证据只覆盖 6 种物体且依赖传感器校准，跨物体/手型尚未验证。</td>
<td width="180"><a href="https://openreview.net/forum?id=dT3ZciXvNX">论文</a> / <a href="https://peilin-666.github.io/projects/DexMove/">项目</a> / <a href="https://github.com/bigai-ai/PP-Tac/tree/main">传感器代码</a></td>
</tr>
<tr>
<td width="100" nowrap>ICLR 2026</td>
<td width="260"><a href="https://openreview.net/forum?id=ndilONnABZ">AnyTouch 2: General Optical Tactile Representation Learning For Dynamic Tactile Perception</a></td>
<td width="230">学习可跨光学触觉传感器和机器人任务迁移的动态表示。</td>
<td width="300">多传感器预训练；下游为 Piper + GelSight Mini/DIGIT，以及 xArm6 + GelSight Mini。</td>
<td width="280">动态光学触觉流多为 30 Hz；报告配置中的 GelSight Mini 为 18 Hz。</td>
<td width="220">抓取、擦白板、USB 插入和移动芯片。</td>
<td width="300">注意力池化器形成触觉特征，与视觉拼接后输入扩散策略。</td>
<td width="220">下游闭环策略 3 Hz。</td>
<td width="200">面向机械臂/夹爪的扩散策略动作块。</td>
<td width="330">IMPM + Blender 合成 1,118,896；真实 584,842；带力标签 722,436；合计 2,426,174。</td>
<td width="110">混合仿真/真实预训 + 实机控制</td>
<td width="320">报告任务成功率范围 0.25–0.85：不同传感器/设置下为 0.75/0.80、0.85/0.80、0.30/0.25 和 0.85。</td>
<td width="230">提升多个光学触觉传感器间的动态、力感知迁移。</td>
<td width="240">跨传感器表现仍不均衡，下游控制频率也只有 3 Hz。</td>
<td width="180"><a href="https://openreview.net/forum?id=ndilONnABZ">论文</a> / <a href="https://gewu-lab.github.io/AnyTouch2/">项目</a> / <a href="https://github.com/GeWu-Lab/AnyTouch2">代码</a> / <a href="https://huggingface.co/collections/BAAI/touchd">数据</a></td>
</tr>
<tr>
<td width="100" nowrap>ICLR 2026</td>
<td width="260"><a href="https://openreview.net/forum?id=hU2gT2Ucua">APPLE: Toward General Active Perception via Reinforcement Learning</a></td>
<td width="230">学习主动获取有信息量触觉观测的通用策略。</td>
<td width="300">无实体机器人；仿真 GelSight Mini 和 Myrmex 类触觉。</td>
<td width="280">Taxim GelSight Mini 观测为 32x32；MHSB Myrmex 为 16x16，并非二值接触。</td>
<td width="220">主动触觉分类/回归，包括 Tactile-MNIST。</td>
<td width="300">ViT 与探测位置输入时序 Transformer 策略/价值模型。</td>
<td width="220">闭环的是主动感知而非操作控制；交互频率未披露。</td>
<td width="200">强化学习智能体选择下一次探测/接触动作。</td>
<td width="330">仅仿真；Taxim 与 MHSB 任务分别训练 5M/10M 环境步。</td>
<td width="110">仅仿真</td>
<td width="320">Tactile-MNIST 两种设置最终准确率约 87/89%，随机探索为 74%。</td>
<td width="230">把主动信息采集策略推广到多类触觉感知任务。</td>
<td width="240">没有实体机器人、接触丰富操作或硬件仿真到现实评测。</td>
<td width="180"><a href="https://openreview.net/forum?id=hU2gT2Ucua">论文</a> / <a href="https://timschneider42.github.io/apple">项目</a></td>
</tr>
<tr>
<td width="100" nowrap>AAAI 2026</td>
<td width="260"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38882">STOLA: Self-Adaptive Touch-Language Framework for Tactile Commonsense Reasoning in Open-Ended Scenarios</a></td>
<td width="230">跨传感器和交互序列回答开放式触觉常识问题。</td>
<td width="300">无机器人；使用公开/自建数据中的 GelSight、GelSight Mini 离线图像与序列。</td>
<td width="280">单帧触觉图像和触觉时间序列；空间密度/采样频率因数据源而异，未统一。</td>
<td width="220">覆盖 8 种属性和 4 种交互特征的开放式触觉问答。</td>
<td width="300">触觉编码器和适配器条件化 Vicuna，混合专家层自适应触觉-语言推理。</td>
<td width="220">无机器人闭环；仅离线推理。</td>
<td width="200">根据触觉观测和提示生成自由文本。</td>
<td width="330">Touch100k + PHYSICLEAR + 5k 自建指令；TactileBench 含 600 个问答；无物理仿真。</td>
<td width="110">真实离线数据</td>
<td width="320">PHYSICLEAR 上 CIDEr 为 195.03；TactileBench 另报问答/推理指标。</td>
<td width="230">把触觉语言评测从固定标签扩展到开放常识推理。</td>
<td width="240">尚未在实时机器人操作中验证推理结果。</td>
<td width="180"><a href="https://arxiv.org/abs/2505.04201">论文</a> / <a href="https://cocacola-lab.github.io/SToLa-Page/">项目</a></td>
</tr>
<tr>
<td width="100" nowrap>AAAI 2026</td>
<td width="260"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38915">TouchFormer: A Robust Transformer-based Framework for Multimodal Material Perception</a></td>
<td width="230">在触觉、惯性或音频噪声/缺失时仍稳健识别材料。</td>
<td width="300">RealMan RM65-B + TESOLLO Gripper-3F + uSkin 指尖 + 12 自由度 IMU + 接触音频。</td>
<td width="280">uSkin 法向/摩擦力、12 自由度惯性特征和音频序列；采样频率未披露。</td>
<td width="220">材料分类和感知引导的分拣演示。</td>
<td width="300">自适应门控结合自注意力/交叉注意力融合触觉、IMU 与音频。</td>
<td width="220">无操作反馈闭环；分类器只用于选择材料/分拣行为。</td>
<td width="200">输出材料类别，随后执行预设分拣动作。</td>
<td width="330">LMTHM 报告 965 条样本、193 种材料；FISHM 用于真实多模态微调/评测。</td>
<td width="110">真实离线感知 + 实机演示</td>
<td width="320">两个主要设置的分类准确率为 91.47% / 89.54%。</td>
<td width="230">在模态噪声或缺失下保持材料感知，并完成机器人分拣演示。</td>
<td width="240">实机演示是感知选择，不是闭环接触或力控制。</td>
<td width="180"><a href="https://arxiv.org/abs/2511.19509">论文</a></td>
</tr>
<tr>
<td width="100" nowrap>AAAI 2026</td>
<td width="260"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38956">Collaborative Representation Learning for Alignment of Tactile, Language, and Vision Modalities</a></td>
<td width="230">对齐触觉、语言和视觉，同时抑制传感器特有偏差。</td>
<td width="300">无机器人；来自 8 个离线数据集的 GelSight、DIGIT、DuraGel、GelSight Mini 数据。</td>
<td width="280">8 个真实触觉图像数据集约含 9.3k/8.3k/7.2k/250k/4.5k/39k/39k/55k 样本。</td>
<td width="220">跨传感器材料识别，以及触觉-语言-视觉检索/对齐。</td>
<td width="300">OpenCLIP-L + 统一偏置适配器 + 对比目标对齐三种模态。</td>
<td width="220">无；仅离线表示学习和评测。</td>
<td width="200">只输出嵌入、检索结果和分类。</td>
<td width="330">8 个真实触觉数据集，包括 TAG、TacQuad；无物理仿真。</td>
<td width="110">真实离线数据</td>
<td width="320">报告设置中的跨传感器材料识别达到 55.59%。</td>
<td width="230">提升异构数据上的传感器无关触觉-语言-视觉对齐。</td>
<td width="240">没有实时机器人、操作或闭环传感反馈评测。</td>
<td width="180"><a href="https://arxiv.org/abs/2511.11512">论文</a> / <a href="https://ojs.aaai.org/index.php/AAAI/article/view/38956">AAAI</a></td>
</tr>
<tr>
<td width="100" nowrap>ICML 2026</td>
<td width="260"><a href="https://icml.cc/virtual/2026/poster/66793">Cross-Tactile Sensor Representation Learning</a></td>
<td width="230">在图像域差异明显的光学触觉传感器之间迁移表示。</td>
<td width="300">无机器人；使用对齐的合成传感器域和真实触觉数据。</td>
<td width="280">SITR 含 5 个传感器 x 10k = 50k 对齐仿真样本；TAG 约含 250k 真实样本，另有其他真实数据。</td>
<td width="220">跨传感器触觉识别和表示迁移。</td>
<td width="300">先在对齐合成数据上学习 跨传感器调制器，再用真实多模态触觉适配。</td>
<td width="220">无；仅离线预训练和评测。</td>
<td width="200">输出特征嵌入和下游分类。</td>
<td width="330">SITR 5 万对齐仿真样本 + TAG 25 万及其他真实触觉数据。</td>
<td width="110">仿真对齐 + 真实评测</td>
<td width="320">DIGIT↔GelSight Mini 迁移在报告对比中提高约 20 个百分点。</td>
<td width="230">用对齐仿真缩小不同触觉传感器外观的域差异。</td>
<td width="240">没有机器人控制或闭环操作验证。</td>
<td width="180"><a href="https://icml.cc/virtual/2026/poster/66793">论文</a></td>
</tr>
<tr>
<td width="100" nowrap>ICML 2026</td>
<td width="260"><a href="https://icml.cc/virtual/2026/poster/65669">Tabero: Learning Gentle Manipulation with Closed-Loop Force Feedback from Vision, Touch, and Language</a></td>
<td width="230">在维持任务成功率的同时执行语言指定的轻柔/用力操作。</td>
<td width="300">Isaac Lab/Isaac Sim 中的 Franka Panda 机械臂/手，双 GelSight 指尖。</td>
<td width="280">每个模拟 GelSight 为 320x240 RGB、11x9 标记点；双指尖各有三维力向量；20 Hz 同步。</td>
<td width="220">受语言力约束的轻柔/用力抓取与操作。</td>
<td width="300">触觉 TCN 和交叉注意力条件化 Pi0；低层导纳力位控制器执行命令。</td>
<td width="220">策略观测 20 Hz；低层导纳力位闭环的内部频率未披露。</td>
<td width="200">Pi0 输出运动/力目标，交给导纳控制器。</td>
<td width="330">Isaac Lab/Isaac Sim + Taxim；重放开源 LIBERO 轨迹，轨迹数未披露。</td>
<td width="110">仅仿真</td>
<td width="320">任务 A 成功率 0.87/0.79，同时平均抓力从 31.3 N 降到 8.5 N；平均降幅超过 70%。</td>
<td width="230">在基本保持成功率的同时加入语言条件化力反馈。</td>
<td width="240">尚未解决超轻柔状态，也没有实体部署。</td>
<td width="180"><a href="https://arxiv.org/abs/2605.27886">论文</a> / <a href="https://github.com/NathanWu7/Tabero">代码</a></td>
</tr>
<tr>
<td width="100" nowrap>NeurIPS 2025</td>
<td width="260"><a href="https://arxiv.org/abs/2505.22566">Universal Visuo-Tactile Video Understanding for Embodied Interaction</a></td>
<td width="230">跨触觉传感器联合理解动态触觉、视频与语言。</td>
<td width="300">无机器人；人工采集 GelSight Mini、DIGIT、Tac3D 视频。</td>
<td width="280">VTV150K 含 100 个物体、15 万帧和 3 类传感器，并带硬度/凸起/弹性/摩擦标签。</td>
<td width="220">触觉视频属性识别和触觉语言问答。</td>
<td width="300">VideoMAE 特征与流掩码条件化 Qwen 语言模型。</td>
<td width="220">无；仅离线视频理解。</td>
<td width="200">输出属性预测和语言答案，不输出机器人动作。</td>
<td width="330">无仿真；100 个物体 x 5 段视频，共 15 万真实帧。</td>
<td width="110">真实离线数据</td>
<td width="320">VTV-LLM 在报告理解基准上的平均分为 60.4。</td>
<td width="230">给出多传感器触觉视频语言数据集和通用视频模型。</td>
<td width="240">没有闭环操作或机器人硬件评测。</td>
<td width="180"><a href="https://arxiv.org/abs/2505.22566">论文</a> / <a href="https://github.com/IvanXie416/VTV-LLM">代码</a> / <a href="https://huggingface.co/datasets/Ivan416/VBTS_video">数据</a></td>
</tr>
<tr>
<td width="100" nowrap>NeurIPS 2025</td>
<td width="260"><a href="https://arxiv.org/abs/2510.21609">Enhancing Tactile-based Reinforcement Learning for Robotic Control</a></td>
<td width="230">让稀疏接触信号支持无视觉强化学习控制。</td>
<td width="300">仅 Isaac Lab：查找 用 Franka；弹跳/保定球 用固定 Shadow Dexterous Hand；没有 Allegro/ORCA 实机评测。</td>
<td width="280">查找 为 9-D 状态 + 2 个二值接触；Shadow 任务为 20-D 手状态 + 17 个连杆接触；物理 120 Hz、策略 60 Hz。</td>
<td width="220">找物体、颠球、旋转保定球，均不使用视觉。</td>
<td width="300">PPO 融合本体感知与稀疏接触，自监督辅助目标正则化策略编码器。</td>
<td width="220">仿真闭环控制 60 Hz，物理 120 Hz。</td>
<td width="200">PPO 连续电机动作；低层执行模式随任务而异。</td>
<td width="330">Isaac Lab RoTO 基准；仅仿真；各任务训练时长未统一披露。</td>
<td width="110">仅仿真</td>
<td width="320">查找 1.4 s 对比 1.9 s；弹跳 79 对比 69 次/10 s；保定球 17 对比 5 转。</td>
<td width="230">证明自监督可从极稀疏二值接触提升无视觉灵巧控制。</td>
<td width="240">没有真实触觉硬件、耐久性或仿真到现实结果。</td>
<td width="180"><a href="https://arxiv.org/abs/2510.21609">论文</a> / <a href="https://elle-miller.github.io/tactile_rl/">项目</a> / <a href="https://github.com/elle-miller/roto">代码</a></td>
</tr>
<tr>
<td width="100" nowrap>NeurIPS 2025</td>
<td width="260"><a href="https://taccel-simulator.github.io/assets/taccel-paper.pdf">Taccel: Scaling Up Vision-based Tactile Robotics via High-performance GPU Simulation</a></td>
<td width="230">扩展可变形光学触觉仿真，用于机器人学习。</td>
<td width="300">仿真光学触觉机器人；仿真到现实分类实验使用 Robotiq 2F-85 + GelSight。</td>
<td width="280">触觉图像随任务配置；双 GelSight 插销场景并行 4,096 环境；五指模型含 17 个凝胶表面。</td>
<td width="220">插销、触觉分类和多指抓取/操作。</td>
<td width="300">基于 Warp 的 ABD + IPC 仿真接触和触觉图像，策略/分类器读取渲染信号。</td>
<td width="220">仿真控制任务为闭环；论文未给统一控制频率。</td>
<td width="200">按任务使用强化学习电机动作或分类输出。</td>
<td width="330">Taccel GPU 仿真器；双 GelSight 插销为 4,096 环境、915 FPS；多手实验约 1.4 万次抓取。</td>
<td width="110">仿真为主 + 有限真实迁移</td>
<td width="320">真实分类准确率 70.94%；4 组抓取成功率 44.56/44.61/54.30/42.54%。</td>
<td width="230">提供高吞吐可变形触觉仿真及机器人/传感器接口。</td>
<td width="240">硬件迁移仍依赖具体任务和校准，仿真到现实证据有限。</td>
<td width="180"><a href="https://taccel-simulator.github.io/assets/taccel-paper.pdf">论文</a> / <a href="https://taccel-simulator.github.io/">项目</a> / <a href="https://github.com/Taccel-Simulator/Taccel">代码</a></td>
</tr>
<tr>
<td width="100" nowrap>NeurIPS 2025</td>
<td width="260"><a href="https://arxiv.org/abs/2511.16596">Toward Artificial Palpation: Representation Learning of Touch on Soft Bodies</a></td>
<td width="230">从触诊序列学习软体内部结构表示。</td>
<td width="300">Franka Emika Panda + 单个 XELA uSkin。</td>
<td width="280">30 个三轴力单元，85 Hz；采集时低层维持 3.8 N 目标力。</td>
<td width="220">自动探压/触诊、MRI 重建和变化检测。</td>
<td width="300">力与机器人位姿序列输入 MLP/GRU 表示模型。</td>
<td width="220">只有数据采集控制器闭合 3.8 N 力环；学习推理没有运动规划闭环。</td>
<td width="200">程序化探压位置 + 低层力调节。</td>
<td width="330">PalpationSim 二维 FEM；真实约 550 个仿体、6 万次探压、3,000 万瞬时读数。</td>
<td width="110">仿真 + 真实感知</td>
<td width="320">尺寸误差 23%，质心误差 2.4 mm，变化检测 F1 为 74.4%。</td>
<td width="230">把序列触觉用于软体重建，并发布仿真/真实数据。</td>
<td width="240">仿真器明确是简化模型；未解决传感器运动规划和临床验证。</td>
<td width="180"><a href="https://arxiv.org/abs/2511.16596">论文</a> / <a href="https://zoharri.github.io/artificial-palpation/">项目</a> / <a href="https://github.com/zoharri/ArtificialPalpation">代码</a> / <a href="https://zenodo.org/records/17608184">数据</a></td>
</tr>
<tr>
<td width="100" nowrap>NeurIPS 2025</td>
<td width="260"><a href="https://arxiv.org/abs/2507.15062v1">Touch in the Wild: Learning Fine-Grained Manipulation with a Portable Visuo-Tactile Gripper</a></td>
<td width="230">用便携设备采集野外触觉示范，并迁移到精细机器人策略。</td>
<td width="300">采集为手持软鳍触觉夹爪；部署为装同款夹爪的 xArm 850；视觉为 GoPro Hero 9。</td>
<td width="280">两块 12x32 合成 1x24x32 触觉图，2 mm²/触觉单元、23 Hz；GoPro 60 Hz。</td>
<td width="220">试管/铅笔插入、液体转移、擦白板。</td>
<td width="300">触觉 CNN 与视觉 ViT 经交叉注意力融合，再输入扩散策略。</td>
<td width="220">扩散策略闭环；策略频率未报告；触觉/视频流为 23/60 Hz。</td>
<td width="200">扩散策略输出机械臂/夹爪动作块。</td>
<td width="330">仅真实：260 万视觉触觉对、2,700+ 示范、43 项任务、12 个环境。</td>
<td width="110">真实采集 + 实机部署</td>
<td width="320">4 项任务成功率 0.85/0.85/0.90/0.70，仅视觉为 0.25/0.45/0.55/0.55。</td>
<td width="230">便携数据和触觉预训练提升数据效率及视觉退化下的鲁棒性。</td>
<td width="240">每个下游任务仍需在定制夹爪上训练策略。</td>
<td width="180"><a href="https://arxiv.org/abs/2507.15062v1">论文</a> / <a href="https://binghao-huang.github.io/touch_in_the_wild/">项目</a> / <a href="https://github.com/YolandaXinyueZhu/touch_in_the_wild">代码</a> / <a href="https://huggingface.co/datasets/binghaohuang-robot/touch_in_the_wild-dataset">数据</a></td>
</tr>
<tr>
<td width="100" nowrap>arXiv 2026</td>
<td width="260"><a href="https://arxiv.org/abs/2606.17055">T-Rex: Tactile-Reactive Dexterous Manipulation</a></td>
<td width="230">让双臂灵巧策略以高于视觉/动作主干的频率响应触觉。</td>
<td width="300">固定底座 Dexmate Vega-1（14 个臂关节）+ 双 Sharpa Wave（每手 22 自由度）+ ZED 相机。</td>
<td width="280">10 指均输出形变深度图和六轴力旋量；RGB/触觉/状态/动作以 30 Hz 记录。</td>
<td width="220">12 项需要精细力控和可变形物体处理的任务。</td>
<td width="300">时序触觉 VQ-VAE 输入三专家异步 MoT；触觉专家用于细化动作。</td>
<td width="220">动作专家约 5 Hz、触觉专家约 20 Hz、PID 300 Hz；示范同步为 30 Hz。</td>
<td width="200">触觉异步细化双臂/双手动作块，再由 PID 跟踪。</td>
<td width="330">仅真实：100 h、7,755 个回合、207 物体、22 运动基元；另用 22,889 h 人类视频预训。</td>
<td width="110">仅实机</td>
<td width="320">12 项任务平均成功率 65%，基线 35%，去除触觉后 42%。</td>
<td width="230">把慢速语义动作与快速触觉反应分开，实现双臂灵巧控制。</td>
<td width="240">触觉存在畸变/标定漂移，手掌也缺少密集触觉。</td>
<td width="180"><a href="https://arxiv.org/abs/2606.17055">论文</a> / <a href="https://tactile-rex.github.io/">项目</a></td>
</tr>
<tr>
<td width="100" nowrap>arXiv 2026</td>
<td width="260"><a href="https://arxiv.org/abs/2606.13102">FTP-1: A Generalist Foundation Tactile Policy Across Tactile Sensors for Contact-Rich Manipulation</a></td>
<td width="230">跨异构传感器格式和机器人本体训练统一触觉专家。</td>
<td width="300">5 套下游配置，覆盖 UniVTAC 仿真以及 Sharpa/Dexmate、Flexiv、Franka 实机平台。</td>
<td width="280">MTTS 覆盖 21 种传感器/26 个来源：7 种图像、5 种阵列、9 种状态触觉，映射到 24 个传感器槽位。</td>
<td width="220">跨已见/未见触觉硬件的通用接触丰富操作。</td>
<td width="300">3 亿参数触觉 Transformer 通过单向接口条件化动作专家。</td>
<td width="220">高层是触觉条件化闭环；未报告力伺服和控制频率。</td>
<td width="200">下游动作专家根据 FTP-1 特征输出机器人专用动作。</td>
<td width="330">约 3,000 h、26 个来源、21 种传感器；混合 UniVTAC 仿真和真实机器人数据。</td>
<td width="110">仿真 + 真实预训/评测</td>
<td width="320">仿真 66.66% 对比 49.16%；已见实机 62.5% 对比 45.3%；未见实机均值 46.6% 对比 15%。</td>
<td width="230">证明共享触觉预训练可迁移到多模态传感器及未见下游传感器。</td>
<td width="240">下游仍需微调，FTP-1 也不是通用力伺服控制器。</td>
<td width="180"><a href="https://arxiv.org/abs/2606.13102">论文</a> / <a href="https://ftp1-policy.github.io/">项目</a> / <a href="https://github.com/michaelyuancb/ftp1-policy">代码</a></td>
</tr>
<tr>
<td width="100" nowrap>ICRA 2026</td>
<td width="260"><a href="https://opendrivelab.com/FreeTacMan">FreeTacMan: Robot-free Visuo-Tactile Data Collection System for Contact-rich Manipulation</a></td>
<td width="230">摆脱机器人本体限制，规模化采集接触丰富示范。</td>
<td width="300">采集为手持双指 McTac；学习策略部署到 6 自由度 Piper 机械臂。</td>
<td width="280">McTac 相机 640x480@30 Hz；鱼眼 30 Hz；NOKOV 240 Hz；统一同步记录为 30 Hz。</td>
<td width="220">50 项接触丰富任务及其机器人策略迁移。</td>
<td width="300">ResNet 触觉特征先做 CLIP 风格预训练，触觉与视觉拼接后输入 ACT。</td>
<td width="220">Piper 上的 ACT 闭环策略；执行频率未披露。</td>
<td width="200">ACT 输出 Piper 机械臂/夹爪动作块。</td>
<td width="330">无仿真；50 项真实任务，300 万+视觉触觉对、1 万+轨迹。</td>
<td width="110">无机器人真实采集 + 实机部署</td>
<td width="320">总体成功率按报告消融阶梯为 21%→55%→71%，体现触觉数据/预训练增益。</td>
<td width="230">把触觉示范采集与特定机器人解耦，并提升策略迁移。</td>
<td width="240">控制结果主要集中在 Piper，策略频率和硬件泛化未充分披露。</td>
<td width="180"><a href="https://opendrivelab.com/FreeTacMan">项目</a> / <a href="https://github.com/OpenDriveLab/FreeTacMan">代码</a></td>
</tr>
<tr>
<td width="100" nowrap>ICRA 2026</td>
<td width="260"><a href="https://arxiv.org/abs/2602.11643">ViTaS: Visual Tactile Soft Fusion Contrastive Learning for Visuomotor Learning</a></td>
<td width="230">在不硬对齐特征的前提下预训练视觉触觉视觉运动策略。</td>
<td width="300">实机为 Galaxea-R1 + ZED 2 + 3D-ViTaC 夹爪；仿真含平行夹爪和五指手。</td>
<td width="280">仿真使用 32x32x3 触觉图，或 5 个 3x3x3 指尖阵列；实机 3D-ViTaC 为 16x16x1。</td>
<td width="220">5 个仿真环境中的 12 项任务，以及 3 项真实触觉任务。</td>
<td width="300">软融合对比学习后接 CVAE/PPO/扩散策略头。</td>
<td width="220">学习策略为闭环；执行频率未披露。</td>
<td width="200">强化学习用 PPO 电机动作；模仿学习用 CVAE/扩散动作分布。</td>
<td width="330">仿真：Gymnasium、robosuite、Insertion、Mobile Catching、Block Spinning 等 5 类环境共 12 任务；强化学习 3M 步，模仿学习每任务 50 条。实机 Galaxea-R1：每任务 100 条遥操作轨迹。</td>
<td width="110">仿真与实机分别训练/评测；不是仿真到现实</td>
<td width="320">仿真均值 91.4% 对比 71.5%；去触觉 92.5→60.9%；实机均值 46% 对比 DP 30%。</td>
<td width="230">软对比融合在强化学习、模仿学习和单独训练的实机策略中提升触觉视觉运动学习。</td>
<td width="240">真实评测仅 3 项任务，且依赖定制触觉硬件。</td>
<td width="180"><a href="https://arxiv.org/abs/2602.11643">论文</a> / <a href="https://skyrainwind.github.io/ViTaS/index.html">项目</a> / <a href="https://github.com/SkyRainWind/ViTaS">代码</a></td>
</tr>
<tr>
<td width="100" nowrap>ICRA 2026</td>
<td width="260"><a href="https://arxiv.org/abs/2510.06339">Vi-TacMan: Articulated Object Manipulation via Vision and Touch</a></td>
<td width="230">用视觉完成全局初始化，再用触觉精确执行铰接物体操作。</td>
<td width="300">Kinova Gen3 + 双自制 GelSight 风格夹爪垫 + RealSense Femto Bolt。</td>
<td width="280">基于标记点的光学触觉图像；配准触觉控制器 50 Hz。</td>
<td width="220">在视觉位姿/方向歧义下操作铰接物体。</td>
<td width="300">DINOv3/SAM2 给视觉抓取，PointNet/vMF 预测方向，触觉 Kabsch 配准细化执行。</td>
<td width="220">视觉只初始化一次抓取/方向，执行阶段改为 50 Hz 纯触觉闭环。</td>
<td width="200">由触觉配准输出笛卡尔方向/位姿修正。</td>
<td width="330">SAPIEN：385 物体、55,241 条视觉位移样本；真实 4 物体 x 5 视角；未报告触觉物理仿真器。</td>
<td width="110">仿真训练视觉模块 + 真实触觉执行</td>
<td width="320">未见物体方向误差 8.13°；实机仅定性展示，没有成功率。</td>
<td width="230">明确分工：视觉负责全局，触觉负责局部反馈。</td>
<td width="240">实机缺少量化成功率，且铰接物体覆盖很小。</td>
<td width="180"><a href="https://arxiv.org/abs/2510.06339">论文</a> / <a href="https://vi-tacman.github.io/">项目</a></td>
</tr>
<tr>
<td width="100" nowrap>CoRL 2025</td>
<td width="260"><a href="https://proceedings.mlr.press/v305/xu25e.html">exUMI: Extensible Robot Teaching System with Action-aware Task-agnostic Tactile Representation</a></td>
<td width="230">采集标定一致的触觉示范，并学习可复用的动作感知触觉特征。</td>
<td width="300">教学端：Meta Quest 3、旋转编码器、Orange Pi、双 9DTact；部署端：Flexiv Rizon 4 + Grav 夹爪 + GoPro。</td>
<td width="280">双 9DTact 灰度流缩放到 224x224；超过 100 万对齐帧，其中 48 万触觉帧/5 h。</td>
<td width="220">用可扩展 UMI 风格设备采集 4 项接触丰富技能。</td>
<td width="300">TPP 由 VAE、Transformer 和潜在扩散组成；触觉嵌入拼接到扩散策略。</td>
<td width="220">扩散策略以 10 Hz 闭环运行。</td>
<td width="200">扩散策略输出末端与夹爪动作块。</td>
<td width="330">仅真实：10 个环境、300+ 物体、100 万+对齐帧；48 万触觉帧/5 h。</td>
<td width="110">真实教学 + 实机部署</td>
<td width="320">每项 20 次评测，4 项任务的 TPP 成功率为 85/60/95/80%。</td>
<td width="230">提升触觉教学数据质量，并把任务无关表示迁移到策略。</td>
<td width="240">定制教学/部署栈仍需针对具体装置标定。</td>
<td width="180"><a href="https://proceedings.mlr.press/v305/xu25e.html">PMLR</a> / <a href="https://silicx.github.io/exUMI/">项目</a> / <a href="https://github.com/silicx/exUMI">代码</a></td>
</tr>
<tr>
<td width="100" nowrap>CoRL 2025</td>
<td width="260"><a href="https://proceedings.mlr.press/v305/wistreich25a.html">DexSkin: High-Coverage Conformable Robotic Skin for Learning Contact-Rich Manipulation</a></td>
<td width="230">给简单夹爪提供大覆盖触觉，用于学习接触丰富行为。</td>
<td width="300">Franka Panda + SSG-48 平行夹爪（双指均覆 DexSkin）+ RealSense D415。</td>
<td width="280">每指 60 个电容触觉单元，共 120；覆盖 294°；30 Hz；0–2.5 N，力 RMSE 0.086 N。</td>
<td width="220">受扰钢笔在手重定向、浆果操作和橡皮筋操作。</td>
<td width="300">标定后的触觉向量与视觉/本体感知在扩散策略和在线强化学习中融合。</td>
<td width="220">扩散策略 20 Hz 闭环；在线强化学习同样使用触觉条件。</td>
<td width="200">高覆盖指面接触条件化机械臂/夹爪动作。</td>
<td width="330">仅真实；扩散策略任务 50 条示范，另含标定、模型迁移和在线强化学习。</td>
<td width="110">仅实机</td>
<td width="320">钢笔扰动 19/20，去触觉为 0/20；浆果完整率 60%，对照 20%。</td>
<td width="230">证明大覆盖柔性皮肤可支持模型迁移和学习式反应行为。</td>
<td width="240">只在平行夹爪上评测，并非完整多指灵巧手。</td>
<td width="180"><a href="https://proceedings.mlr.press/v305/wistreich25a.html">PMLR</a> / <a href="https://dex-skin.github.io/">项目</a> / <a href="https://github.com/sdwistreich/dexskin">代码</a></td>
</tr>
<tr>
<td width="100" nowrap>RSS 2025</td>
<td width="260"><a href="https://arxiv.org/abs/2504.16649">PP-Tac: Paper Picking Using Tactile Feedback in Dexterous Robotic Hands</a></td>
<td width="230">用滑移感知指尖反馈夹取一张或多张纸。</td>
<td width="300">Franka Research 3 + 自制 16 自由度四指手 + 4 个 R-Tac 指尖。</td>
<td width="280">OV9281 640x480，最高 120 Hz，约 100 ms 延迟，2 mm 凝胶。</td>
<td width="220">纸张抓取、滑移检测、在线抓力调整和学习轨迹。</td>
<td width="300">触觉深度与 152-D 本体状态条件化扩散策略；检测到滑移后增加抓力。</td>
<td width="220">滑移触发的力反馈为闭环；扩散策略频率未披露。</td>
<td width="200">机械臂/16 自由度手动作序列，在线叠加抓力增量。</td>
<td width="330">生成 50 万条刚性抓取序列 x 100 帧用于训练；无触觉物理仿真；真实触觉评测。</td>
<td width="110">生成刚性序列 + 实机评测</td>
<td width="320">总体成功率 87.5%；准确取 1/3/5/7 张的成功率为 90/75/30/5%。</td>
<td width="230">把触觉深度、滑移检测、抓力调整和扩散控制用于纸张分离。</td>
<td width="240">任务很窄，纸张数增加后性能明显下降，传感也存在较大延迟。</td>
<td width="180"><a href="https://arxiv.org/abs/2504.16649">论文</a> / <a href="https://www.roboticsproceedings.org/rss21/p056.pdf">RSS</a> / <a href="https://peilin-666.github.io/projects/PP-Tac/">项目</a> / <a href="https://github.com/bigai-ai/PP-Tac">代码</a></td>
</tr>
<tr>
<td width="100" nowrap>ICRA 2026</td>
<td width="260"><a href="https://arxiv.org/abs/2509.23468">Multi-Modal Manipulation via Multi-Modal Policy Consensus</a></td>
<td width="230">避免早期特征拼接，在视觉、触觉或本体感知受损时保持鲁棒控制。</td>
<td width="300">UR5e + 双 RealSense D415（96x128）+ 夹爪双指 FlexiTac。</td>
<td width="280">每块 FlexiTac 为 12x32、2 mm 空间间距；采样频率未披露。</td>
<td width="220">4 项 RLBench 任务，以及真实遮挡抓取、勺子在手重定向和拼图插入/操作。</td>
<td width="300">每种模态训练 DDPM 得分专家，路由器在动作分布层做策略共识。</td>
<td width="220">闭环策略；执行频率未披露。</td>
<td width="200">面向机械臂/夹爪的共识扩散动作轨迹。</td>
<td width="330">RLBench：4 任务、200 示范、200 未见测试；真实示范三组为 80/60/50。</td>
<td width="110">仿真 + 实机评测</td>
<td width="320">仿真均值 0.66，特征拼接为 0.56；4 个真实设置为 0.65/0.75/0.58/0.45。</td>
<td width="230">在单一传感器失效时保留其他模态的有效动作意见。</td>
<td width="240">控制频率和部分低层硬件细节未披露，真实覆盖也较小。</td>
<td width="180"><a href="https://arxiv.org/abs/2509.23468">论文</a> / <a href="https://policyconsensus.github.io/">项目</a> / <a href="https://openreview.net/forum?id=CJDU8IvF3y">OpenReview</a></td>
</tr>
<tr>
<td width="100" nowrap>arXiv 2026</td>
<td width="260"><a href="https://arxiv.org/abs/2602.06001">Visuo-Tactile World Models for Robot Manipulation</a></td>
<td width="230">在遮挡和接触不确定性下预测动力学并规划真实机器人动作。</td>
<td width="300">Franka Panda + Allegro Hand + 4 个 DIGIT 360 指尖。</td>
<td width="280">触觉 30 FPS；视觉/动作轨迹块以 6 Hz 执行。</td>
<td width="220">真实机器人到达、推、到达推移、擦拭、堆叠。</td>
<td width="300">Cosmos 视觉与 Sparsh-X 触觉嵌入输入 12 层 Transformer 世界模型，CEM 搜索动作块。</td>
<td width="220">轨迹块内部不使用触觉反馈；以 6 Hz 开环执行，因此不是触觉伺服闭环。</td>
<td width="200">CEM 选择机械臂/手的开环动作块。</td>
<td width="330">仅真实：训练 124 条示范/11.2 万点；验证 26 条示范/1.7 万点。</td>
<td width="110">仅实机</td>
<td width="320">V-WM→VT-WM 成功率：到达 100→100、推 83→92、到达推移 69→93、擦拭 70→92、堆叠 75→83%。</td>
<td width="230">触觉提升物体持续性和接触动力学预测，从而改善模型规划。</td>
<td width="240">CEM 计算开销高、数据规模小，且每个动作块内部仍是开环。</td>
<td width="180"><a href="https://arxiv.org/abs/2602.06001">论文</a> / <a href="https://carolinahiguera.github.io/vtml/">项目</a></td>
</tr>
</tbody>
</table>
