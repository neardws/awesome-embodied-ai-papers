# 动作表示

[首页](../../../README.zh-CN.md) | [英文](../../en/vla/action-representation.md) | [方向目录](README.md)

共 30 篇。

<table width="3260">
<thead>
<tr>
<th width="120" nowrap>会议/年份</th>
<th width="320">论文/方法</th>
<th width="420">摘要</th>
<th width="230">基础 VLA</th>
<th width="240">动作</th>
<th width="300">训练/反馈</th>
<th width="260">算法</th>
<th width="240">策略/类型</th>
<th width="200">仿真/实机</th>
<th width="360">论文任务/目标</th>
<th width="110" nowrap>论文</th>
<th width="110" nowrap>项目</th>
<th width="110" nowrap>代码</th>
<th width="240">数据/基准</th>
</tr>
</thead>
<tbody>
<tr>
<td width="120" nowrap>ICML 2024</td>
<td width="320"><a href="https://proceedings.mlr.press/v235/he24o.html">DynSyn: Dynamical Synergistic Representation for Efficient Learning and Control in Overactuated Embodied Systems</a></td>
<td width="420">为高过驱动肌骨控制学习低维动态协同表示。</td>
<td width="230">-（非机器人肌骨模型）</td>
<td width="240">肌肉激励：MyoHand R39 / Arm-Locate R81，经学习的协同压缩</td>
<td width="300">MuJoCo + MyoSuite；约 5×10^5 帧提取协同；每任务约 3M 强化学习步、5 随机种子</td>
<td width="260">无监督动态协同表示 + 下游强化学习</td>
<td width="240">仅仿真的潜动作表示；不是实体机器人手硬件</td>
<td width="200">仅仿真</td>
<td width="360">控制 MS-HUMAN-700、Arm-Locate、MyoHand-Reorient100；论文报告回报/样本效率曲线，没有稳定可引用的抓取成功率</td>
<td width="110" nowrap><a href="https://proceedings.mlr.press/v235/he24o.html">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">MuJoCo/MyoSuite；100 种 MyoHand 物体几何</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=tv0Sz8A9Tc">Robotic Manipulation by Imitating Generated Videos Without Physical Demonstrations (RIGVid)</a></td>
<td width="420">无需物理示范或策略训练，把生成任务视频转为可执行机器人轨迹。</td>
<td width="230">Kling/Sora 视频生成器 + FoundationPose</td>
<td width="240">跟踪物体 6 自由度轨迹 → 重定向末端 6 自由度轨迹</td>
<td width="300">4 个任务；每任务/视频来源 10 条生成视频；无物理仿真器和机器人策略数据集</td>
<td width="260">视频筛选 + 物体跟踪 + 固定夹爪—物体变换重定向</td>
<td width="240">生成视频到动作表示；xArm7 与 ALOHA；普通夹爪</td>
<td width="200">仅实机；不是物理仿真到现实管线</td>
<td width="360">筛选后 Kling v1.6 四任务 100/80/90/70%；整体 85%，ReKep 50%；ALOHA 倒水 80%，xArm 100%</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=tv0Sz8A9Tc">论文</a></td>
<td width="110" nowrap><a href="https://rigvid-robot.github.io/">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">仅生成视频；无物理示范</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2022</td>
<td width="320"><a href="https://arxiv.org/abs/2203.06173">Real-World Robot Learning with Masked Visual Pre-training</a></td>
<td width="420">MVP 利用掩码视觉预训练支持真实机器人学习。</td>
<td width="230">掩码视觉预训练的真实机器人学习</td>
<td width="240">机器人动作</td>
<td width="300">VLA / 动作表示</td>
<td width="260">CoRL 机器人学习方法</td>
<td width="240">机器人策略</td>
<td width="200">机器人基准</td>
<td width="360">补充 CoRL VLA 研究覆盖。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2203.06173">论文</a></td>
<td width="110" nowrap><a href="https://tetexiao.com/projects/real-mvp">项目</a></td>
<td width="110" nowrap><a href="https://github.com/ir413/mvp">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2022</td>
<td width="320"><a href="https://arxiv.org/abs/2203.12601">R3M: A Universal Visual Representation for Robot Manipulation</a></td>
<td width="420">R3M 学习用于机器人操作的通用视觉表示。</td>
<td width="230">R3M</td>
<td width="240">机器人动作</td>
<td width="300">VLA / 动作表示</td>
<td width="260">CoRL 机器人学习方法</td>
<td width="240">机器人策略</td>
<td width="200">机器人基准</td>
<td width="360">补充 CoRL VLA 研究覆盖。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2203.12601">论文</a></td>
<td width="110" nowrap><a href="https://sites.google.com/view/robot-r3m/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/facebookresearch/r3m">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2023</td>
<td width="320"><a href="https://arxiv.org/abs/2306.10007">Robot Learning with Sensorimotor Pre-training</a></td>
<td width="420">RPT 利用感觉运动预训练支持下游机器人学习。</td>
<td width="230">感觉运动预训练的机器人学习</td>
<td width="240">机器人动作</td>
<td width="300">VLA / 动作表示</td>
<td width="260">CoRL 机器人学习方法</td>
<td width="240">机器人策略</td>
<td width="200">机器人基准</td>
<td width="360">补充 CoRL VLA 研究覆盖。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2306.10007">论文</a></td>
<td width="110" nowrap><a href="https://robotic-pretrained-transformer.github.io">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2024</td>
<td width="320"><a href="https://arxiv.org/abs/2407.20179">Theia: Distilling Diverse Vision Foundation Models for Robot Learning</a></td>
<td width="420">Theia 将多种视觉基础模型蒸馏为机器人学习表示。</td>
<td width="230">Theia</td>
<td width="240">机器人动作</td>
<td width="300">VLA / 动作表示</td>
<td width="260">CoRL 机器人学习方法</td>
<td width="240">机器人策略</td>
<td width="200">机器人基准</td>
<td width="360">补充 CoRL VLA 研究覆盖。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2407.20179">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2509.07962">TA-VLA: Elucidating the Design Space of Torque-aware Vision-Language-Action Models</a></td>
<td width="420">TA-VLA 研究 VLA 模型中考虑力矩的动作设计。</td>
<td width="230">TA-VLA</td>
<td width="240">机器人动作</td>
<td width="300">VLA / 动作表示</td>
<td width="260">CoRL 机器人学习方法</td>
<td width="240">机器人策略</td>
<td width="200">机器人基准</td>
<td width="360">补充 CoRL VLA 研究覆盖。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2509.07962">论文</a></td>
<td width="110" nowrap><a href="https://zzongzheng0918.github.io/Torque-Aware-VLA.github.io/">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2508.01600">CLASS: Contrastive Learning via Action Sequence Supervision for Robot Manipulation</a></td>
<td width="420">CLASS 使用动作序列监督，进行对比式机器人操作学习。</td>
<td width="230">CLASS</td>
<td width="240">机器人动作</td>
<td width="300">VLA / 动作表示</td>
<td width="260">CoRL 机器人学习方法</td>
<td width="240">机器人策略</td>
<td width="200">机器人基准</td>
<td width="360">补充 CoRL VLA 研究覆盖。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2508.01600">论文</a></td>
<td width="110" nowrap><a href="https://class-robot.github.io/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/sean1295/CLASS/tree/main">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2021</td>
<td width="320"><a href="https://arxiv.org/abs/2010.14406">Transporter Networks: Rearranging the Visual World for Robotic Manipulation</a></td>
<td width="420">Transporter Networks 通过空间搬运算子表示抓取放置操作。</td>
<td width="230">Transporter Networks</td>
<td width="240">机器人动作</td>
<td width="300">VLA / 动作表示</td>
<td width="260">CoRL 机器人学习方法</td>
<td width="240">机器人策略</td>
<td width="200">机器人基准</td>
<td width="360">补充 CoRL VLA 研究覆盖。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2010.14406">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2024</td>
<td width="320"><a href="https://arxiv.org/abs/2310.08576">Learning to Act from Actionless Videos through Dense Correspondences</a></td>
<td width="420">该工作利用稠密视觉对应关系，从无动作标注视频中学习动作表示。</td>
<td width="230">视频预训练</td>
<td width="240">潜在动作</td>
<td width="300">动作表示 / 预训练</td>
<td width="260">稠密对应关系学习</td>
<td width="240">视频到动作表示</td>
<td width="200">机器人操作基准</td>
<td width="360">在无动作标签条件下恢复可复用的动作结构。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2310.08576">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2024</td>
<td width="320"><a href="https://arxiv.org/abs/2402.07872">PIVOT: Iterative Visual Prompting Elicits Actionable Knowledge for VLMs</a></td>
<td width="420">PIVOT 通过迭代视觉提示，提取视觉语言模型中的空间与可执行知识。</td>
<td width="230">视觉语言模型</td>
<td width="240">可执行视觉提示</td>
<td width="300">动作表示 / 可供性</td>
<td width="260">迭代视觉提示</td>
<td width="240">视觉语言模型可供性推理</td>
<td width="200">空间动作基准</td>
<td width="360">从视觉语言模型中提取可执行的空间知识。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2402.07872">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=y5CaJb17Fn">villa-X: Enhancing Latent Action Modeling in Vision-Language-Action Models</a></td>
<td width="420">villa-X 学习并使用潜在动作作为 VLA 预训练中的运动抽象，可零样本生成潜在动作计划。</td>
<td width="230">ViLLA/villa-X</td>
<td width="240">潜在动作</td>
<td width="300">动作表示 / 动作表示/词元化</td>
<td width="260">用于 VLA 预训练的潜在动作建模</td>
<td width="240">视觉—语言—潜在动作</td>
<td width="200">SIMPLER + 两套实机设置</td>
<td width="360">潜在动作预训练</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=y5CaJb17Fn">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2410.11758">Latent Action Pretraining from Videos</a></td>
<td width="420">LAPA 先从视频中学习潜在动作抽象，再迁移到机器人动作生成。</td>
<td width="230">LAPA</td>
<td width="240">潜在动作</td>
<td width="300">动作表示 / 预训练</td>
<td width="260">潜在动作预训练</td>
<td width="240">视频到动作表示</td>
<td width="200">机器人操作基准</td>
<td width="360">从视频中学习可复用潜在动作，用于下游 VLA 策略。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2410.11758">论文</a></td>
<td width="110" nowrap><a href="https://latentactionpretraining.github.io/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/LatentActionPretraining/LAPA">代码</a></td>
<td width="240"><a href="https://huggingface.co/latent-action-pretraining/LAPA-7B-openx">Hugging Face</a></td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=IZHk6BXBST">Rodrigues Network for Learning Robot Actions</a></td>
<td width="420">RodriNet 将可学习 神经罗德里格斯算子 作为运动学结构先验注入动作网络。</td>
<td width="230">-</td>
<td width="240">运动学感知动作表示</td>
<td width="300">动作表示 / 动作表示/词元化</td>
<td width="260">神经 Rodrigues 算子 + RodriNet</td>
<td width="240">动作网络架构</td>
<td width="200">合成数据 + 模仿学习基准 + 手部重建</td>
<td width="360">机器人动作的运动学结构建模</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=IZHk6BXBST">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38937">Actor-Critic for Continuous Action Chunks: A Reinforcement Learning Framework for Long-Horizon Robotic Manipulation with Sparse Reward</a></td>
<td width="420">AC3 用演员—评论家直接学习连续动作块，并用成功轨迹非对称更新和块内 n 步回报稳定训练。</td>
<td width="230">-</td>
<td width="240">连续动作块</td>
<td width="300">强化学习 / 稀疏奖励</td>
<td width="260">AC3</td>
<td width="240">演员—评论家动作块策略</td>
<td width="200">BiGym + RLBench</td>
<td width="360">稀疏奖励长程连续动作块学习</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38937">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/60681">DyGRO-VLA: Cross-Task Scaling of Vision-Language-Action Models via Dynamic Grouped Residual Optimization</a></td>
<td width="420">DyGRO-VLA 先学习跨任务潜在表征，再用动态分组强化学习残差优化多任务 VLA。</td>
<td width="230">DyGRO-VLA</td>
<td width="240">残差策略优化</td>
<td width="300">强化学习/在线微调</td>
<td width="260">动态分组残差优化</td>
<td width="240">跨任务强化学习优化的 VLA</td>
<td width="200">LIBERO/RoboTwin2 + 实机</td>
<td width="360">跨任务 VLA 强化学习优化</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/60681">论文</a></td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/60681">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/61232">LARA: Latent Action Representation Alignment for Vision-Language-Action Models</a></td>
<td width="420">LARA 联合优化潜在动作模型与 VLA，使人类视频潜在动作更好对齐真实动作轨迹。</td>
<td width="230">LARA 插件</td>
<td width="240">潜在动作表示</td>
<td width="300">VLA / 动作表示/词元化</td>
<td width="260">LAM-VLA 表示对齐</td>
<td width="240">预训练/后训练增强</td>
<td width="200">3 个仿真基准 + 1 个实机基准</td>
<td width="360">潜在动作对齐</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/61232">论文</a></td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/61232">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/62908">From Noise to Intent: Anchoring Generative VLA Policies with Residual Bridges</a></td>
<td width="420">ResVLA 将生成动作从“噪声生成”改为“意图锚定后残差细化”，分离低频意图与高频局部动力学。</td>
<td width="230">ResVLA</td>
<td width="240">扩散 / 残差桥</td>
<td width="300">VLA / 动作表示/词元化</td>
<td width="260">低频意图锚点 + 高频残差扩散桥</td>
<td width="240">生成式 VLA 策略</td>
<td width="200">LIBERO/LIBERO-Plus</td>
<td width="360">生成式动作解码稳定性</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/62908">论文</a></td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/62908">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/65967">Demystifying Action Space Design for Robotic Manipulation Policies</a></td>
<td width="420">该文用 13k+ 真实轨迹展开和 500+ 模型系统分析绝对/增量、关节/任务空间动作设计的影响。</td>
<td width="230">-</td>
<td width="240">倾向使用增量动作</td>
<td width="300">动作表示 / 动作表示/词元化</td>
<td width="260">大规模动作空间实证研究</td>
<td width="240">动作空间设计研究</td>
<td width="200">真实双臂机器人</td>
<td width="360">动作空间设计准则</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/65967">论文</a></td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/65967">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/66520">FocalPolicy: Frequency-Optimized Chunking and Locally Anchored Flow Matching for Coherent Visuomotor Policy</a></td>
<td width="420">FocalPolicy 用频域优化分块和局部锚定流匹配提升长程动作块之间的连贯性。</td>
<td width="230">视觉运动策略</td>
<td width="240">扩散 / 流动作块</td>
<td width="300">流匹配 / 扩散与流策略</td>
<td width="260">频率优化分块 + 局部锚定流匹配</td>
<td width="240">流匹配视觉运动策略</td>
<td width="200">-</td>
<td width="360">跨动作块连贯性</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/66520">论文</a></td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/66520">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/62176">GeoMoLa: Geometry-Aware Motion Latents for Learning Robust Manipulation Policies</a></td>
<td width="420">GeoMoLa 通过预测点云随操作的四维几何变化来学习离散运动潜在编码。</td>
<td width="230">GeoMoLa</td>
<td width="240">离散运动潜在编码</td>
<td width="300">动作表示 / 动作表示/词元化</td>
<td width="260">几何感知点云演化目标</td>
<td width="240">运动潜在表示策略</td>
<td width="200">基准 + 实机</td>
<td width="360">几何感知动作潜变量</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/62176">论文</a></td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/62176">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2604.04161">Adaptive Action Chunking at Inference-time for Vision-Language-Action Models</a></td>
<td width="420">AAC 用动作熵在推理时动态选择动作块长度，平衡反应性和连续性。</td>
<td width="230">通用 VLA</td>
<td width="240">自适应动作块</td>
<td width="300">VLA / 动作表示/词元化</td>
<td width="260">基于动作熵的自适应动作分块</td>
<td width="240">推理时适应</td>
<td width="200">仿真 + 实机</td>
<td width="360">推理时自适应动作分块</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2604.04161">论文</a></td>
<td width="110" nowrap><a href="https://lance-lot.github.io/adaptive-chunking.github.io/">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2603.10158">Cross-Hand Latent Representation for Vision-Language-Action Models</a></td>
<td width="420">XL-VLA/DexLatent 学习跨不同灵巧手的潜在表示，使单一策略可迁移到多种手型。</td>
<td width="230">XL-VLA / DexLatent</td>
<td width="240">跨手型潜在表示</td>
<td width="300">VLA / 动作表示/词元化</td>
<td width="260">DexLatent</td>
<td width="240">跨本体灵巧 VLA</td>
<td width="200">-</td>
<td width="360">解决多指灵巧手之间动作空间不同、策略难跨手迁移的问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2603.10158">论文</a></td>
<td width="110" nowrap><a href="https://xl-vla.github.io/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/EmptyBlueBox/DexLatent">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2506.16685">Compliant Residual DAgger: Improving Real-World Contact-Rich Manipulation with Human Corrections</a></td>
<td width="420">CR-DAgger 用柔顺干预接口和力反馈残差策略，从人类增量修正中改进接触丰富操作。</td>
<td width="230">-</td>
<td width="240">增量动作修正 / 残差策略</td>
<td width="300">DAgger / 人类纠正</td>
<td width="260">柔顺残差 DAgger</td>
<td width="240">人在回路中的残差策略</td>
<td width="200">实机</td>
<td width="360">解决真实接触操作中 DAgger 修正数据难采、策略更新难稳定的问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2506.16685">论文</a></td>
<td width="110" nowrap><a href="https://compliant-residual-dagger.github.io/">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2510.25138">Learning Spatial-Aware Manipulation Ordering</a></td>
<td width="420">OrderMind 从空间上下文直接学习杂乱场景中各物体的操作优先级。</td>
<td width="230">OrderMind</td>
<td width="240">操作顺序优先级</td>
<td width="300">VLA / 动作表示/词元化</td>
<td width="260">空间图编码器 + 时间优先级结构化</td>
<td width="240">排序策略</td>
<td width="200">基准 + 实机</td>
<td width="360">解决杂乱环境中错误操作顺序导致碰撞或遮挡的问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2510.25138">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/yyxssm/OrderMind">代码</a></td>
<td width="240">操作排序基准</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2509.15607">PRIMT: Preference-based Reinforcement Learning with Multimodal Feedback and Trajectory Synthesis from Foundation Models</a></td>
<td width="420">PRIMT 用大语言模型/视觉语言模型多模态合成偏好反馈和轨迹合成来减少 PbRL 对人工反馈的依赖。</td>
<td width="230">-</td>
<td width="240">强化学习策略动作</td>
<td width="300">基于偏好的强化学习 / 多模态合成反馈</td>
<td width="260">PRIMT + 神经符号融合 + 轨迹合成</td>
<td width="240">基于偏好的强化学习框架</td>
<td width="200">2 个运动基准 + 6 个操作基准</td>
<td width="360">解决偏好强化学习中人工反馈多、查询歧义和信用分配难的问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2509.15607">论文</a></td>
<td width="110" nowrap><a href="https://primt25.github.io/">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2502.01218">Provable Ordering and Continuity in Vision-Language Pretraining for Generalizable Embodied Agents</a></td>
<td width="420">AcTOL 用帧间语义排序和局部布朗桥连续性约束学习有序连续的视觉语言表征。</td>
<td width="230">AcTOL 特征</td>
<td width="240">预训练表示</td>
<td width="300">VLA / 动作表示/词元化</td>
<td width="260">动作时间连贯性学习</td>
<td width="240">面向具身智能体的视觉语言预训练</td>
<td width="200">-</td>
<td width="360">有序连续视觉语言预训练</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2502.01218">论文</a></td>
<td width="110" nowrap><a href="https://actol-pretrain.github.io/">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2508.05941">Latent Policy Barrier: Learning Robust Visuomotor Policies by Staying In-Distribution</a></td>
<td width="420">LPB 将专家示教潜在嵌入作为隐式安全边界，推理时优化未来潜在表示保持在专家分布内。</td>
<td width="230">LPB</td>
<td width="240">扩散策略 + 潜在屏障修正</td>
<td width="300">动作表示 / 动作表示/词元化</td>
<td width="260">潜在策略屏障 + 动力学模型</td>
<td width="240">鲁棒视觉运动策略</td>
<td width="200">仿真 + 实机</td>
<td width="360">解决行为克隆视觉运动策略因协变量偏移而逐步偏离专家轨迹的问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2508.05941">论文</a></td>
<td width="110" nowrap><a href="https://project-latentpolicybarrier.github.io/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/zhanyisun/lpb">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2412.04445">Moto: Latent Motion Token as the Bridging Language for Robot Manipulation</a></td>
<td width="420">Moto 将视频转为潜在运动词元，并用 Moto-GPT 自回归预训练把视频运动知识迁移到机器人控制。</td>
<td width="230">Moto-GPT</td>
<td width="240">潜在运动词元</td>
<td width="300">VLA / 动作词元化 / 动作表示/词元化</td>
<td width="260">潜在运动词元化器 + Moto-GPT 自回归</td>
<td width="240">视频预训练运动词元策略</td>
<td width="200">-</td>
<td width="360">解决机器人缺少动作标注数据而视频数据中运动知识难直接利用的问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2412.04445">论文</a></td>
<td width="110" nowrap><a href="https://chenyi99.github.io/moto/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/TencentARC/Moto">代码</a></td>
<td width="240"><a href="https://huggingface.co/TencentARC/Moto">Hugging Face</a></td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2411.14519">Tra-MoE: Learning Trajectory Prediction Model from Multiple Domains for Adaptive Policy Conditioning</a></td>
<td width="420">Tra-MoE 从多域轨迹学习混合专家预测模型，用预测轨迹自适应调节策略条件。</td>
<td width="230">Tra-MoE</td>
<td width="240">轨迹预测 / 策略条件化</td>
<td width="300">动作表示 / 动作表示/词元化</td>
<td width="260">混合专家轨迹模型</td>
<td width="240">自适应策略条件化</td>
<td width="200">-</td>
<td width="360">多域轨迹预测与策略条件化</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2411.14519">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/MCG-NJU/Tra-MoE">代码</a></td>
<td width="240">-</td>
</tr>
</tbody>
</table>
