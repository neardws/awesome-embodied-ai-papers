# 人形机器人

[首页](../../../README.zh-CN.md) | [英文](../../en/embodiment/humanoid.md) | [方向目录](README.md)

共 78 篇。下表是唯一的人形机器人论文主表：每篇均逐项核查主论文/官方项目材料，并明确区分真实机器人、仅仿真机器人模型和非机器人虚拟人体。CoRL 2024 论文按会议年份标注，即使 PMLR 正式卷在 2025 年出版。**“当前瓶颈”优先采用作者明确限制；没有局限小节时写可验证的实验边界。“未来趋势”是根据该限制做出的研究判断，不等同于作者原话。** 证据列分别记录仿真/训练栈、基准或数据集及其公开规模、训练算力与墙钟时间、训练流程，以及论文明确给出的量化细节。**“未披露”表示论文或官方实现没有报告该项，不会按惯例倒推；“不适用”仅用于方法确实不使用该资源或训练阶段的情况。若依据作者官方代码确认，会在单元格中明确限定。**

## Humanoid 资源审计：统计口径

统计快照日期：**2026-07-13**。以下频次按不同论文计数，不按字符串出现次数计数；同一篇论文可分别计入多个硬件、仿真器、数据集或训练阶段，但同一规范化项目在一篇论文中最多计 1 次。机器人机体、末端执行器、计算硬件、物理引擎、机器人学习框架和辅助工具分层统计。论文披露了具体型号时保留型号边界，例如 H1 与 H1-2 分开，Isaac Gym、Isaac Lab、Isaac Sim、MuJoCo、MJX 也互不合并。长尾行保留所有仅出现 1 篇的规范名称。下方 78 篇主表是所有计数的逐篇追溯账本。

### 机器人机体与平台使用情况

<table width="1620">
<thead>
<tr>
<th width="240" nowrap>规范化平台</th>
<th width="100">论文数</th>
<th width="280">主表评测类型分布</th>
<th width="500">平台信息</th>
<th width="500">计数边界</th>
</tr>
</thead>
<tbody>
<tr>
<td width="240" nowrap><a href="https://www.unitree.com/g1/">宇树 Unitree G1</a></td>
<td width="100">29</td>
<td width="280">3 篇仅仿真；2 篇实机；14 篇仿真+实机；10 篇仿真→实机</td>
<td width="500">紧凑型科研人形平台；各论文使用不同的 23/27/29 自由度控制或机体配置，并可搭配不同机器人手。</td>
<td width="500">统计所有明确 G1 机体或仿真模型；不合并 H1、H1-2 或未注明型号的宇树机器人手。</td>
</tr>
<tr>
<td width="240" nowrap><a href="https://www.unitree.com/h1/">宇树 Unitree H1</a></td>
<td width="100">15</td>
<td width="280">2 篇仅仿真；2 篇实机；4 篇仿真+实机；7 篇仿真→实机</td>
<td width="500">全尺寸人形平台，用于运动控制、全身控制、遥操作和操作；论文中的定制配置为 19–33 自由度。</td>
<td width="500">只统计 H1；明确标为 H1-2 的版本单列。</td>
</tr>
<tr>
<td width="240" nowrap><a href="https://www.fftai.com/products-gr1">傅利叶 Fourier GR-1</a></td>
<td width="100">6</td>
<td width="280">1 篇实机；3 篇仿真+实机；2 篇仿真→实机</td>
<td width="500">全尺寸 44 关节平台；入选论文主要用于遥操作、移动操作和跨本体评测。</td>
<td width="500">统计 GR-1 机体；Fourier 手和 Fourier N1 机体分别统计。</td>
</tr>
<tr>
<td width="240" nowrap><a href="https://arxiv.org/abs/1809.07279">Agility Cassie</a></td>
<td width="100">6</td>
<td width="280">2 篇仿真+实机；4 篇仿真→实机</td>
<td width="500">无手臂的欠驱动双足科研平台，主要用于步行、跳跃、地形适应和多双足协同。</td>
<td width="500">统计实体 Cassie 和明确命名的 Cassie 仿真器/模型。</td>
</tr>
<tr>
<td width="240" nowrap><a href="https://www.agilityrobotics.com/solutions/digit/spec-sheet">Agility Digit</a></td>
<td width="100">6</td>
<td width="280">4 篇仅仿真；2 篇仿真+实机</td>
<td width="500">带手臂的双足人形平台，用于导航、运动控制和词元化运动建模。</td>
<td width="500">Digit 与 Cassie 虽来自同一厂商体系，但不合并计数。</td>
</tr>
<tr>
<td width="240" nowrap><a href="https://www.booster.tech/open-source/">加速进化 Booster T1</a></td>
<td width="100">4</td>
<td width="280">4 篇仿真+实机</td>
<td width="500">面向开发者的人形平台，用于跨本体学习、预训练/微调和仿真到仿真对比。</td>
<td width="500">仅统计明确 T1；不与其他厂商同名的 N1 平台合并。</td>
</tr>
<tr>
<td width="240" nowrap><a href="https://www.unitree.com/h1/">宇树 Unitree H1-2</a></td>
<td width="100">2</td>
<td width="280">2 篇仿真+实机</td>
<td width="500">H1 系列的更高自由度版本，出现在跨人形运动控制和高动态模仿研究中。</td>
<td width="500">论文明确写出 H1-2，因此与 H1 分开。</td>
</tr>
<tr>
<td width="240" nowrap><a href="https://www.agibot.com/products/X2">智元 AgiBot X2</a></td>
<td width="100">2</td>
<td width="280">2 篇仿真+实机</td>
<td width="500">半尺寸双足平台，用于全身 VLA 和跨人形控制；其中一篇采用带 OmniPicker 的 X2 原型。</td>
<td width="500">这里只统计 X2 机体；OmniPicker 作为末端执行器单独计数。</td>
</tr>
<tr>
<td width="240" nowrap>长尾（每项 1 篇）</td>
<td width="100">14 项</td>
<td width="280">混合仅仿真 / 仿真+实机 / 仿真→实机</td>
<td width="500">Dobot Atom、Fourier N1、Noetix N1、JAXON、Rabbit、Walker2D、Berkeley Humanoid、Berkeley Humanoid Lite、ToddlerBot、星动纪元 XBot-S、XBot-L、HECTOR V2、Disney 双足角色、MIT Humanoid。</td>
<td width="500">每个规范化机体/模型只出现在 1 篇论文；不同厂商的同名 N1 不合并。</td>
</tr>
</tbody>
</table>

### 命名机器人手、腕部与夹爪使用情况

<table width="1420">
<thead>
<tr>
<th width="260" nowrap>规范化末端执行器</th>
<th width="100">论文数</th>
<th width="500">硬件信息</th>
<th width="560">计数边界</th>
</tr>
</thead>
<tbody>
<tr>
<td width="260" nowrap>因时 Inspire 手系列</td>
<td width="100">8</td>
<td width="500">论文中常见的 6 驱动灵巧手，装配于定制 H1、GR-1 或仿真 G1 配置。</td>
<td width="560">1 篇明确写出 RH56DFX，另 7 篇只写 Inspire 灵巧手(s)；汇总系列频次，同时保留型号不确定性。</td>
</tr>
<tr>
<td width="260" nowrap><a href="https://www.unitree.com/Dex3-1/">宇树 Dex3-1</a></td>
<td width="100">4</td>
<td width="500">7 驱动三指手，用于 G1 操作、遥操作和视觉仿真到现实。</td>
<td width="560">只统计明确 Dex3-1；通用 13 自由度宇树灵巧手模型保留在长尾。</td>
</tr>
<tr>
<td width="260" nowrap>长尾（每项 1 篇）</td>
<td width="100">7 项</td>
<td width="500">Shadow Hand、ROBOTERA XHAND、Fourier Hand、Robotiq 2F-85、OmniPicker、13 自由度宇树灵巧手模型、Damiao 腕部。</td>
<td width="560">未命名的夹爪钳口、并联或简单夹爪会在逐篇主表描述，但不提升为命名产品计数。</td>
</tr>
</tbody>
</table>

### 仿真与训练环境使用情况

<table width="1740">
<thead>
<tr>
<th width="250" nowrap>规范化环境</th>
<th width="100">论文数</th>
<th width="260">层级 / 开发方</th>
<th width="560">在入选论文中的用途</th>
<th width="570">计数边界</th>
</tr>
</thead>
<tbody>
<tr>
<td width="250" nowrap><a href="https://developer.nvidia.com/isaac-gym/download">NVIDIA Isaac Gym</a></td>
<td width="100">44</td>
<td width="260">GPU 物理/强化学习环境；NVIDIA</td>
<td width="560">大规模并行策略训练、动作模仿、运动控制、全身控制和仿真到现实源域训练。</td>
<td width="570">包含 Preview 4 和由作者官方代码确认的用法；不包含 Isaac Lab 与 Isaac Sim。</td>
</tr>
<tr>
<td width="250" nowrap><a href="https://mujoco.org/">MuJoCo</a></td>
<td width="100">22</td>
<td width="260">通用接触物理引擎；Google DeepMind</td>
<td width="560">双足主仿真、跨引擎验证、仿真到仿真测试和目标域评测。</td>
<td width="570">包含明确 MuJoCo 和 MuJoCo Playground；MJX 单独统计。</td>
</tr>
<tr>
<td width="250" nowrap><a href="https://developer.nvidia.com/isaac/lab">NVIDIA Isaac Lab</a></td>
<td width="100">6</td>
<td width="260">机器人学习框架；NVIDIA</td>
<td width="560">可扩展强化学习/模仿学习流程和更高保真机器人学习任务，通常运行于 Isaac Sim 栈。</td>
<td width="570">即使同一论文还写 Isaac Sim，也按框架层单独计数；不并入 Isaac Gym。</td>
</tr>
<tr>
<td width="250" nowrap><a href="https://developer.nvidia.com/isaac/sim/">NVIDIA Isaac Sim</a></td>
<td width="100">3</td>
<td width="260">机器人仿真/合成数据框架；NVIDIA</td>
<td width="560">跨引擎目标域评测、高保真仿真和源策略对齐。</td>
<td width="570">与 Isaac Lab、旧版 Isaac Gym 分开。</td>
</tr>
<tr>
<td width="250" nowrap><a href="https://mujoco.readthedocs.io/en/latest/mjx.html">MJX</a></td>
<td width="100">2</td>
<td width="260">JAX 加速 MuJoCo 实现；Google DeepMind</td>
<td width="560">HumanoidBench 和 ToddlerBot 的并行 PPO/强化学习执行。</td>
<td width="570">只有明确写出 MJX 才计数，不从普通 MuJoCo 用法倒推。</td>
</tr>
<tr>
<td width="250" nowrap><a href="https://github.com/google/brax">Brax</a></td>
<td width="100">2</td>
<td width="260">JAX 强化学习/训练库；Google</td>
<td width="560">微调/目标域仿真和面向加速器的强化学习训练。</td>
<td width="570">按训练/仿真层记录，不并入 MuJoCo 或 MJX。</td>
</tr>
<tr>
<td width="250" nowrap><a href="https://www.mathworks.com/products/simulink.html">MATLAB / Simulink</a></td>
<td width="100">2</td>
<td width="260">建模/控制环境；MathWorks</td>
<td width="560">高保真验证和基于模型的人形/双足控制。</td>
<td width="570">Simscape Multibody 和旧版 SimMechanics 作为命名子层保留在长尾。</td>
</tr>
<tr>
<td width="250" nowrap>Cassie 专用仿真器</td>
<td width="100">2</td>
<td width="260">平台专用仿真层</td>
<td width="560">Cassie 策略训练和踏脚石运动评测。</td>
<td width="570">其中 1 篇明确使用 Cassie MuJoCo，另 1 篇未披露底层物理引擎，因此同时保留封装层和引擎证据状态。</td>
</tr>
<tr>
<td width="250" nowrap>长尾（每项 1 篇）</td>
<td width="100">12 项</td>
<td width="260">混合引擎、框架与工具</td>
<td width="560">PyBullet、Gazebo、Legged Gym、Genesis、robosuite、Simscape Multibody、SimMechanics、Choreonoid、Hrpsys、GRUtopia、Agility 仿真器、自建多 Cassie 仿真。</td>
<td width="570">InfiniGen、Blender、PyVHACD 等辅助场景/碰撞工具在对应论文行单列，不作为主物理引擎统计。</td>
</tr>
<tr>
<td width="250" nowrap>底层引擎未披露</td>
<td width="100">7</td>
<td width="260">证据状态类别</td>
<td width="560">论文报告物理仿真或命名封装层，但未说明底层引擎。</td>
<td width="570">该类别可与平台专用仿真器重叠；不会按领域惯例补写引擎。</td>
</tr>
<tr>
<td width="250" nowrap>主流程未使用物理仿真</td>
<td width="100">8</td>
<td width="260">证据状态类别</td>
<td width="560">离线动作/姿态研究、纯真实数据采集、遥操作或纯真实控制。</td>
<td width="570">若主方法为仅实机，但补充实验使用仿真，仍会在逐篇行中注明。</td>
</tr>
</tbody>
</table>

### 基准与数据集使用情况

数据集计数同样为非互斥统计。若论文同时写出 AMASS 及其内部来源库，则分别统计两层名称，因为逐篇证据确实披露了两层。数据规模保留原始单位，不把动作小时、片段、轨迹、帧、任务或场景直接相加。

<table width="1740">
<thead>
<tr>
<th width="250" nowrap>规范化数据集 / 基准</th>
<th width="100">论文数</th>
<th width="420">公开或论文报告规模</th>
<th width="430">在入选论文中的用途</th>
<th width="540">计数边界</th>
</tr>
</thead>
<tbody>
<tr>
<td width="250" nowrap><a href="https://amass.is.tue.mpg.de/">AMASS</a></td>
<td width="100">21</td>
<td width="420">官网发布规模：超过 40 小时、300 多名受试者、11,000 多段动作。</td>
<td width="430">人体动作先验、重定向、策略跟踪、遥操作先验、扩散训练和分布外评测。</td>
<td width="540">只统计明确 AMASS；各论文实际子集从少量片段到约 14k 重定向序列不等，不用全库规模替代论文子集。</td>
</tr>
<tr>
<td width="250" nowrap>CMU 动作捕捉 / AMASS-CMU 子集</td>
<td width="100">10</td>
<td width="420">论文子集包括 175 段分布外动作、318 段运动/3,729.18 秒、780 段/13,383 秒或 1,919 段序列。</td>
<td width="430">姿态估计、运动模仿、表现性控制、评测和极端接触动作参考。</td>
<td width="540">通过 AMASS 使用 CMU 时可同时计入 AMASS；不同论文的子集规模不相加。</td>
</tr>
<tr>
<td width="250" nowrap><a href="https://github.com/EricGuo5513/HumanML3D">HumanML3D</a></td>
<td width="100">7</td>
<td width="420">官方仓库为 14,616 段动作、44,970 条描述；两篇论文行报告 14,646 段的预处理版本。</td>
<td width="430">文本到动作生成、扩散、语言条件运动控制和标注迁移。</td>
<td width="540">保留两种论文报告总数，不静默改成同一个数字。</td>
</tr>
<tr>
<td width="250" nowrap>OMOMO</td>
<td width="100">5</td>
<td width="420">一篇报告 15 类物体、约 10 小时；其他论文使用更小或合并子集，未重述全量规模。</td>
<td width="430">人—物交互、全身重排、遥操作和导航/伸手动作数据。</td>
<td width="540">只统计明确 OMOMO；规模按论文子集保留。</td>
</tr>
<tr>
<td width="250" nowrap>SAMP</td>
<td width="100">3</td>
<td width="420">一篇报告 100 分钟；另一篇报告 OMOMO+SAMP 合并子集 30 分钟。</td>
<td width="430">人—场景交互和物体重排动作先验。</td>
<td width="540">不会把合并的 30 分钟全部归到任一来源。</td>
</tr>
<tr>
<td width="250" nowrap>LAFAN1 / LAFAN</td>
<td width="100">3</td>
<td width="420">BFM-Zero 报告 40 段、每段数分钟的 LAFAN1 动作；其他论文未重述全库规模。</td>
<td width="430">运动正则、起身恢复和高动态参考动作。</td>
<td width="540">LAFAN 与 LAFAN1 规范为同一系列，逐篇主表保留原论文写法。</td>
</tr>
<tr>
<td width="250" nowrap>BMLrub</td>
<td width="100">3</td>
<td width="420">AMASS 来源子集；三篇论文均未重述绝对子集规模。</td>
<td width="430">稀疏跟踪姿态和逆运动学训练。</td>
<td width="540">可与 AMASS 重叠；只有明确写出 BMLrub 才计数。</td>
</tr>
<tr>
<td width="250" nowrap>HDM05</td>
<td width="100">2</td>
<td width="420">AMASS 来源子集；两篇论文报告 90/10 序列划分，但未给绝对数量。</td>
<td width="430">稀疏第一视角和 VR 全身姿态估计。</td>
<td width="540">可与 AMASS 重叠；只有明确写出 HDM05 才计数。</td>
</tr>
<tr>
<td width="250" nowrap>命名长尾（每项 1 篇）</td>
<td width="100">30 个标签</td>
<td width="420">若论文披露规模，均保留在对应逐篇行。</td>
<td width="430">TokenHSI 运动集、InterAct、BEHAVE、HODome、IMHD、HIMO、ScenePlan、PartNet、ScanNet、CIRCLE、KIT-ML、HumanAct12、UESTC、HPS、Humanoid Everyday、AgiBot World、HITR、MaskedMimic、MotionMillion、HDHM、跨本体基准、ALMI-X、LEGO-H、HumanoidBench、MPI、SFU 动作捕捉、CLONED、ADT、OmniH2O-6、DeepMimic/FLD 动作捕捉。</td>
<td width="540">程序化地形、未命名自采演示和未命名仿真缓冲区仍在逐篇行说明，但不会被杜撰成命名数据集。</td>
</tr>
</tbody>
</table>

### 训练算力与时间披露情况

<table width="1560">
<thead>
<tr>
<th width="340" nowrap>证据状态</th>
<th width="120">论文数</th>
<th width="140">覆盖率</th>
<th width="480">统计内容</th>
<th width="480">解释</th>
</tr>
</thead>
<tbody>
<tr>
<td width="340" nowrap>流程任一环节披露具体加速器</td>
<td width="120">33 / 78</td>
<td width="140">42.3%</td>
<td width="480">算力单元格出现明确 RTX/A 系列/H100/V100/L40S 等型号。</td>
<td width="480">可能只用于预处理、仿真基准或部署，不能自动当作训练 GPU。</td>
</tr>
<tr>
<td width="340" nowrap>明确披露训练加速器</td>
<td width="120">29 / 78</td>
<td width="140">37.2%</td>
<td width="480">具体型号明确用于策略/模型训练、微调或蒸馏。</td>
<td width="480">排除 HumanPlus 姿态处理 4090、OKAMI 重建 3090、Berkeley 仿真吞吐 A4500 和 Hand-Eye 部署 4090。</td>
</tr>
<tr>
<td width="340" nowrap>披露量化训练墙钟时间</td>
<td width="120">21 / 78</td>
<td width="140">26.9%</td>
<td width="480">报告训练、预训练、微调、搜索或策略学习的分钟、小时或天数。</td>
<td width="480">不把数据采集、控制器运行时、视频预处理和执行器耐久测试算作训练时间。</td>
</tr>
<tr>
<td width="340" nowrap>直接报告或可安全换算 GPU·小时</td>
<td width="120">17 / 78</td>
<td width="140">21.8%</td>
<td width="480">同时有加速器数量和墙钟时间，或论文直接给出 GPU·小时/GPU·天。</td>
<td width="480">换算值在逐篇行明确标注；区间和教师/学生阶段分别保留。</td>
</tr>
<tr>
<td width="340" nowrap>只披露步数 / 迭代 / 训练轮次，无墙钟</td>
<td width="120">25 / 78</td>
<td width="140">32.1%</td>
<td width="480">论文给出量化训练预算，但没有实际耗时。</td>
<td width="480">原样记录，不换算为小时。</td>
</tr>
<tr>
<td width="340" nowrap>训练算力不适用</td>
<td width="120">3 / 78</td>
<td width="140">3.8%</td>
<td width="480">方法没有学习模型训练。</td>
<td width="480">对应行记录在线控制器/求解器运行时：MPCC、运动动力学织构或基于模型的步行控制。</td>
</tr>
</tbody>
</table>

### 训练流程分布

以下为非互斥的阶段级统计：同一系统可能先预训练教师，再蒸馏学生，随后用强化学习微调，最后做系统辨识后部署。

<table width="1420">
<thead>
<tr>
<th width="360" nowrap>规范化流程阶段</th>
<th width="120">论文数</th>
<th width="940">本组论文中的典型流程</th>
</tr>
</thead>
<tbody>
<tr>
<td width="360" nowrap>强化学习</td>
<td width="120">58</td>
<td width="940">PPO/IPPO/SAC 类动作跟踪、运动控制、全身控制、教师策略或任务学习。</td>
</tr>
<tr>
<td width="360" nowrap>模仿学习 / 行为克隆 / DAgger</td>
<td width="120">27</td>
<td width="940">动作模仿、教师到学生迁移、遥操作演示、ACT/扩散策略行为克隆或在线数据聚合。</td>
</tr>
<tr>
<td width="360" nowrap>微调 / 适配</td>
<td width="120">23</td>
<td width="940">任务词元、残差/世界模型适配、难例微调、真实数据修正、目标地形续训或专家适配。</td>
</tr>
<tr>
<td width="360" nowrap>预训练 / 复用预训练模块</td>
<td width="120">21</td>
<td width="940">动作先验、基础策略、潜在动作/运动模型、特权策略或预训练扩散/VLA 组件先于任务阶段。</td>
</tr>
<tr>
<td width="360" nowrap>数据生成 / 采集 / 重定向</td>
<td width="120">20</td>
<td width="940">动作捕捉/视频重定向、仿真轨迹展开、轨迹优化、遥操作、对抗轨迹生成或现实到仿真采集。</td>
</tr>
<tr>
<td width="360" nowrap>蒸馏 / 教师—学生迁移</td>
<td width="120">15</td>
<td width="940">特权教师到可部署学生、多专家到通用策略，或理想参照感知到机载感知。</td>
</tr>
<tr>
<td width="360" nowrap>域随机化 / 系统辨识</td>
<td width="120">13</td>
<td width="940">动力学、接触、传感器随机化，显式现实到仿真标定，或部署前学习增量动作对齐。</td>
</tr>
<tr>
<td width="360" nowrap>监督学习</td>
<td width="120">7</td>
<td width="940">姿态/IK 预测、自动回归控制器、高度图感知、步态时序或其他有标签回归/分类阶段。</td>
</tr>
<tr>
<td width="360" nowrap>明确的后训练</td>
<td width="120">4</td>
<td width="940">已有行为/基础/通用策略再通过潜变量适配、对抗鲁棒训练、真实数据蒸馏或对齐仿真微调。</td>
</tr>
<tr>
<td width="360" nowrap>经典优化 / 无训练阶段</td>
<td width="120">6</td>
<td width="940">IK 修正、GP/RRT* 规划、MPCC、轨迹优化、运动动力学织构或 FROST/ALIP-MPC；其中 3 篇完全没有学习模型训练。</td>
</tr>
</tbody>
</table>

<table width="3345">
<thead>
<tr>
<th width="105" nowrap>会议/年份</th>
<th width="280">论文/方法</th>
<th width="210">方向/方法</th>
<th width="260">具体机器人/本体</th>
<th width="220">仿真/训练环境</th>
<th width="300">基准 / 数据集（规模）</th>
<th width="260">训练算力 / 耗时</th>
<th width="330">训练流程</th>
<th width="90">验证</th>
<th width="300">关键细节/指标</th>
<th width="330">解决问题</th>
<th width="330">当前瓶颈</th>
<th width="330">未来趋势（基于论文边界）</th>
</tr>
</thead>
<tbody>
<tr>
<td width="105" nowrap>CoRL 2024</td>
<td width="280"><a href="https://proceedings.mlr.press/v270/fu25a.html">HumanPlus: Humanoid Shadowing and Imitation from Humans</a></td>
<td width="210">人体动作重定向 + 低层模仿 + 高层视觉策略</td>
<td width="260">定制 Unitree H1（33 自由度）；双 Inspire RH56DFX 6 自由度手 + 1 自由度腕</td>
<td width="220">具体引擎未披露；PPO 低层策略在物理仿真训练</td>
<td width="300">AMASS（40 h 人体动作）；6 项真实任务，每项最多 40 条示范</td>
<td width="260">披露 RTX 4090 用于实时姿态处理；策略训练 GPU 数量和墙钟时间未披露</td>
<td width="330">强化学习 + 模仿学习：AMASS 重定向 → 仿真 PPO 影随策略 → 人体影随采集示范 → 监督行为克隆任务策略</td>
<td width="90">仿真→实机</td>
<td width="300">AMASS 40 h；低层 50 Hz / PD 1 kHz；姿态 25 fps、手部 10 fps</td>
<td width="330">把人体影随、技能模仿和自主视觉操作统一到全尺寸人形上</td>
<td width="330">机器人自由度不足；固定头部相机会遮手；姿态估计和重定向会丢失关节；未覆盖长程导航</td>
<td width="330">更高自由度本体、主动视角、稳健姿态估计，以及规模化人类示范与导航融合</td>
</tr>
<tr>
<td width="105" nowrap>CVPR 2025 Oral</td>
<td width="280"><a href="https://openaccess.thecvf.com/content/CVPR2025/html/Pan_TokenHSI_Unified_Synthesis_of_Physical_Human-Scene_Interactions_through_Task_Tokenization_CVPR_2025_paper.html">TokenHSI: Unified Synthesis of Physical Human-Scene Interactions through Task Tokenization</a></td>
<td width="210">任务词元化 + 物理强化学习控制</td>
<td width="260">Isaac Gym 中具有 32 维受控动作空间的物理人体；非机器人</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="300">TokenHSI 动作集：AMASS、OMOMO、SAMP 共 84 条序列；12 项 HSI 任务</td>
<td width="260">4096 环境；基础策略 50k 次迭代；GPU 型号和墙钟时间未披露</td>
<td width="330">强化学习 + 参数高效适配：PPO 训练统一基础技能 → 冻结共享策略 → 为组合与几何变化训练新任务词元化器/输出头</td>
<td width="90">仅仿真</td>
<td width="300">4096 并行环境；基础策略 50k PPO 次迭代；每任务 512 试验</td>
<td width="330">以统一任务表示生成多类物理可信的人体—场景交互</td>
<td width="330">依赖奖励工程；长时任务仍需人工指导</td>
<td width="330">自动奖励与任务规划，并把交互表示迁移到真实人形控制</td>
</tr>
<tr>
<td width="105" nowrap>CVPR 2025 Highlight</td>
<td width="280"><a href="https://openaccess.thecvf.com/content/CVPR2025/html/Xu_InterMimic_Towards_Universal_Whole-Body_Control_for_Physics-Based_Human-Object_Interactions_CVPR_2025_paper.html">InterMimic: Towards Universal Whole-Body Control for Physics-Based Human-Object Interactions</a></td>
<td width="210">接触感知的通用全身交互模仿</td>
<td width="260">SMPL/SMPL-X 物理人体；Unitree G1 + Inspire 手仅作下游仿真</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="300">InterAct 子集：OMOMO（15 个物体、约 10 h，主数据），以及 BEHAVE、HODome、IMHD、HIMO</td>
<td width="260">8192 环境；GPU 型号和墙钟时间未披露</td>
<td width="330">模仿学习 + 蒸馏 + 微调：训练 17 个受试者教师策略 → 在线 DAgger/行为克隆蒸馏 → PPO 微调通用学生策略</td>
<td width="90">仅仿真</td>
<td width="300">策略 30 Hz；OMOMO 约 10 h；17 个教师策略</td>
<td width="330">用一个控制框架复现多样人体—物体全身交互</td>
<td width="330">动作捕捉误差；G1 仿真简化自碰撞、接触奖励和手部耦合，不能证明实机迁移</td>
<td width="330">补全接触、执行器和手部模型，再进行真实人形验证</td>
</tr>
<tr>
<td width="105" nowrap>ICLR 2025 Spotlight</td>
<td width="280"><a href="https://openreview.net/forum?id=pZISppZSTv">CLoSD: Closing the Loop between Simulation and Diffusion for multi-task character control</a></td>
<td width="210">扩散动作规划 + 物理强化学习闭环控制</td>
<td width="260">PHC/SMPL 兼容虚拟人体；非机器人</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="300">HumanML3D（14,616 条动作 / 44,970 条文本）；AMASS 用于 PHC 跟踪先验</td>
<td width="260">DiP：1×RTX 3090、600k 扩散步；跟踪器：1×A100、62k PPO 训练轮次 + 4k 闭环微调训练轮次；墙钟时间未披露</td>
<td width="330">预训练 + 强化微调：训练文本—动作扩散规划器 → AMASS 上训练 PHC 跟踪器 → 闭环微调规划器与跟踪器的交互</td>
<td width="90">仅仿真</td>
<td width="300">3072 并行环境；10 步扩散；约 3500 帧/秒（RTX 3090）</td>
<td width="330">把文本驱动动作生成与可反馈的多任务物理控制闭环连接</td>
<td width="330">无视觉、外感知或地形图；中低层技能和固定反馈时域仍会产生伪影</td>
<td width="330">场景感知、分层长时规划和自适应控制时域</td>
</tr>
<tr>
<td width="105" nowrap>ICLR 2024</td>
<td width="280"><a href="https://proceedings.iclr.cc/paper_files/paper/2024/hash/6a6ecedac816a24f92ad1f444b1edcb0-Abstract-Conference.html">Unified Human-Scene Interaction via Prompted Chain-of-Contacts</a></td>
<td width="210">接触链提示 + 通用人体—场景策略</td>
<td width="260">Isaac Gym 通用物理人体；非机器人</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="300">ScenePlan：40 个 PartNet 训练对象；40 PartNet + 10 ScanNet 测试场景；1040 + 100 条计划；SAMP（100 min）与 CIRCLE 动作数据</td>
<td width="260">1×NVIDIA A100；8192 环境；墙钟时间未披露</td>
<td width="330">数据生成 + 强化学习：GPT 生成接触链计划 → PPO 训练单一 AMP 风格统一控制器 → 执行语言生成计划</td>
<td width="90">仅仿真</td>
<td width="300">40 个 PartNet 训练对象；40 PartNet + 10 ScanNet 测试场景；1040 + 100 交互计划</td>
<td width="330">用接触序列统一坐、躺、触碰等多类人体—场景交互</td>
<td width="330">对象固定；大语言模型只离线产生接触计划，缺少在线闭环</td>
<td width="330">可动物体、在线接触规划与真实人形的闭环执行</td>
</tr>
<tr>
<td width="105" nowrap>ICLR 2024</td>
<td width="280"><a href="https://openreview.net/forum?id=gd0lAEtWso">OmniControl: Control Any Joint at Any Time for Human Motion Generation</a></td>
<td width="210">时空关节约束的可控扩散生成</td>
<td width="260">HumanML3D 22 关节 / KIT-ML 21 关节人体骨架；非机器人</td>
<td width="220">未使用物理仿真；HumanML3D / KIT-ML 离线扩散</td>
<td width="300">HumanML3D（14,646 条动作）；KIT-ML（3911 条动作）</td>
<td width="260">1×RTX A5000、29 h（换算 29 GPU·小时）；250k 次迭代</td>
<td width="330">微调：从预训练 MDM 初始化 → 在空间条件下联合微调动作扩散与真实性引导分支</td>
<td width="90">离线基准</td>
<td width="300">14,646 / 3,911 条动作；196 帧序列；DDPM T=1000</td>
<td width="330">允许任意时刻对任意关节施加稀疏控制约束</td>
<td width="330">约 1000 步去噪；冲突约束会产生不自然动作；无动力学保证</td>
<td width="330">快速扩散、约束可行性检查与物理投影</td>
</tr>
<tr>
<td width="105" nowrap>ICCV 2023</td>
<td width="280"><a href="https://openaccess.thecvf.com/content/ICCV2023/html/Karunratanakul_Guided_Motion_Diffusion_for_Controllable_Human_Motion_Synthesis_ICCV_2023_paper.html">Guided Motion Diffusion for Controllable Human Motion Synthesis</a></td>
<td width="210">目标函数/分类器引导的动作扩散</td>
<td width="260">HumanML3D 人体骨架；非机器人</td>
<td width="220">未使用物理仿真；离线 DDPM</td>
<td width="300">HumanML3D（14,646 条动作 / 44,970 条文本标注）</td>
<td width="260">1×RTX 3090；轨迹模型 4.34 GPU·小时 + 动作模型 34.7 GPU·小时（论文合计约 39.04 GPU·小时）</td>
<td width="330">从零扩散训练：训练轨迹 DPM 与动作 DPM → 采样时施加稠密目标/分类器引导；无需任务专用重训</td>
<td width="90">离线基准</td>
<td width="300">1000 去噪步数；约 110 s/样本；RTX 3090</td>
<td width="330">不重训生成器即可按轨迹、位置等目标控制人体动作</td>
<td width="330">需要人工设计可微目标或训练专用分类器；无接触动力学</td>
<td width="330">统一场景、接触与物理约束的可组合引导</td>
</tr>
<tr>
<td width="105" nowrap>ICCV 2023 Oral</td>
<td width="280"><a href="https://openaccess.thecvf.com/content/ICCV2023/html/Yuan_PhysDiff_Physics-Guided_Human_Motion_Diffusion_Model_ICCV_2023_paper.html">PhysDiff: Physics-Guided Human Motion Diffusion Model</a></td>
<td width="210">扩散采样中的物理控制器投影</td>
<td width="260">Isaac Gym 中 SMPL 物理人体；非机器人</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="300">HumanML3D（14,616 条动作 / 44,970 条描述）；HumanAct12（约 1200 段片段、12 类）；UESTC（25k 样本、40 类）</td>
<td width="260">8192 环境；PPO 投影策略训练 4000 个训练轮次；GPU 型号和墙钟时间未披露</td>
<td width="330">预训练复用 + 强化学习：复用预训练动作扩散 → 在 HumanML3D/AMASS 划分上训练 PPO 动作模仿投影策略 → 去噪时插入物理投影</td>
<td width="90">仅仿真</td>
<td width="300">50 扩散步；4 次物理投影；51.6 s/动作（约 2.5× MDM）</td>
<td width="330">减少人体动作扩散中的脚滑、穿透和失衡</td>
<td width="330">物理投影使推理慢约 2–3 倍；仍是虚拟人体</td>
<td width="330">轻量或可学习的物理投影，并与机器人动力学共同训练</td>
</tr>
<tr>
<td width="105" nowrap>ECCV 2024</td>
<td width="280"><a href="https://siplab.org/projects/MANIKIN">MANIKIN: Biomechanically Accurate Neural Inverse Kinematics for Human Motion Estimation</a></td>
<td width="210">生物力学约束神经逆运动学</td>
<td width="260">生物力学 SMPL 人体；真实稀疏传感输入，非机器人</td>
<td width="220">未使用物理仿真；PyTorch 神经—解析 IK</td>
<td width="300">AMASS 的 CMU、BMLrub、MPI 子集；真实 VR 动作捕捉测试集；未重述子集规模</td>
<td width="260">论文写作 NVIDIA GeForce GTX 4090 GPU(s)；数量与墙钟时间未披露</td>
<td width="330">监督训练：由稀疏追踪器学习旋转角/体型预测 → 解析式生物力学 IK 精确重建末端位置</td>
<td width="90">真实传感器数据</td>
<td width="300">40 帧窗口；MANIKIN-S 580 FPS / L 30.5 / LN 0.81</td>
<td width="330">从稀疏观测恢复更符合关节活动范围的人体动作</td>
<td width="330">需要已知体型；坐姿、盘腿等稀疏观测仍有歧义</td>
<td width="330">免标定体型、时序不确定性建模和多模态观测</td>
</tr>
<tr>
<td width="105" nowrap>ECCV 2024</td>
<td width="280"><a href="https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/00248.pdf">EgoPoser: Robust Real-Time Egocentric Pose Estimation from Sparse and Intermittent Observations Everywhere</a></td>
<td width="210">稀疏、间歇头手观测的实时姿态估计</td>
<td width="260">SMPL-H 前 22 关节；MR 头显 + 控制器，非机器人</td>
<td width="220">未使用物理仿真；离线姿态估计</td>
<td width="300">AMASS CMU/BMLrub/HDM05（序列 90/10 划分）；HPS 用于野外测试；绝对规模未重述</td>
<td width="260">1×NVIDIA GeForce GTX 3090；训练墙钟时间未披露</td>
<td width="330">监督学习：从 AMASS 合成稀疏/间歇头手观测 → 训练 SlowFast 姿态/体型估计器 → 推理时流式处理真实传感姿态</td>
<td width="90">真实传感器数据</td>
<td width="300">80 帧输入；单 RTX 3090；推理 &gt;600 FPS</td>
<td width="330">在观测丢失和跨场景情况下恢复全身姿态</td>
<td width="330">默认同一楼层；无接触或物理一致性保证</td>
<td width="330">跨楼层全局定位、物理约束与更多可穿戴模态</td>
</tr>
<tr>
<td width="105" nowrap>ECCV 2022</td>
<td width="280"><a href="https://siplab.org/projects/AvatarPoser">AvatarPoser: Articulated Full-Body Pose Tracking from Sparse Motion Sensing</a></td>
<td width="210">头部和双手三点稀疏传感的 Transformer 姿态跟踪</td>
<td width="260">SMPL 22 关节虚拟人；Vive 头显/控制器，非机器人</td>
<td width="220">未使用物理仿真；离线姿态跟踪</td>
<td width="300">AMASS 的 CMU、BMLrub、HDM05 子集；未重述子集规模</td>
<td width="260">1×NVIDIA GeForce GTX 3090、约 2 h（换算约 2 GPU·小时）</td>
<td width="330">监督学习 + 经典优化：AMASS 上训练 Transformer 姿态跟踪器 → 推理时执行 5 步逆运动学手部修正</td>
<td width="90">真实传感器数据</td>
<td width="300">60 Hz；40 帧输入；最高 662 FPS；RTX 3090 训练约 2 h</td>
<td width="330">仅凭三个可穿戴设备实时重建全身姿态</td>
<td width="330">问题高度欠定；真实演示有限；无地面接触和动力学约束</td>
<td width="330">显式不确定性、多模态融合和接触物理约束</td>
</tr>
<tr>
<td width="105" nowrap>arXiv 2025</td>
<td width="280"><a href="https://arxiv.org/abs/2510.08807">Humanoid Everyday: A Comprehensive Robotic Dataset for Open-World Humanoid Manipulation</a></td>
<td width="210">大规模真实数据集与开放世界评测</td>
<td width="260">Unitree G1 29 自由度 + 双 Dex3-1；Unitree H1 27 自由度 + 双 6 自由度 Inspire 手</td>
<td width="220">未使用仿真采集；真实机器人数据与云端评测</td>
<td width="300">Humanoid Everyday：10,400 条轨迹、超过 3M 帧、260 项任务、7 类，每任务 40 个回合、30 Hz</td>
<td width="260">基线 GPU 型号、数量和训练时间未披露；数据采集使用第 11 代 Intel i7 笔记本</td>
<td width="330">模仿学习 / VLA 微调：遥操作采集多模态轨迹 → 训练 DP/DP3/ACT，或两阶段 VLA 微调（全量数据 → 类别/任务适配）→ 云端实机评测</td>
<td width="90">实机</td>
<td width="300">260×40 = 10,400 轨迹；30 Hz；控制延迟降至 2 ms</td>
<td width="330">提供 10.3k 轨迹、260 类任务，补齐人形开放世界操作的数据与评测缺口</td>
<td width="330">现有模仿学习在 28 维动作上仍弱；云端评测缺少自动复位</td>
<td width="330">触觉预训练、人形 VLA、自动复位与失败恢复</td>
</tr>
<tr>
<td width="105" nowrap>ICLR 2026</td>
<td width="280"><a href="https://openreview.net/forum?id=OCJmVjyzN7">WholeBodyVLA: Towards Unified Latent VLA for Whole-body Loco-manipulation Control</a></td>
<td width="210">无动作第一视角视频潜变量 VLA + 强化学习控制器</td>
<td width="260">智元 AgiBot X2 原型：双 7 自由度臂、OmniPicker 夹爪、双腿各 6 自由度、1 自由度腰、D435i</td>
<td width="220">MuJoCo 用于 X2 受控消融；LMO 训练引擎未单独披露</td>
<td width="300">约 300 h 自采第一视角行走视频；AgiBot World 操作数据；3 项任务 × 每项 50 条遥操作轨迹</td>
<td width="260">LAM/VLA：8×H100（30k/20k/10k 步）；LMO 强化学习：1×H100；墙钟时间未披露</td>
<td width="330">预训练 + LoRA 微调 + 强化学习：预训练行走/操作 LAM → 用潜标签预训练 Prismatic-7B VLA → 遥操作数据 LoRA 微调 → 固定 LMO 强化学习控制器执行下肢</td>
<td width="90">仿真+实机</td>
<td width="300">约 300 h 第一视角数据；VLA 约 10 Hz / LMO 50 Hz；8×H100 + 1×H100 强化学习</td>
<td width="330">把语言理解、目标感知、行走和操作压入统一潜空间</td>
<td width="330">长程和精细任务仍弱；微小站姿/朝向误差会破坏抓放；末端是夹爪而非灵巧手</td>
<td width="330">记忆与地图、主动感知、精确落脚，以及灵巧手/触觉接入</td>
</tr>
<tr>
<td width="105" nowrap>NeurIPS 2024</td>
<td width="280"><a href="https://proceedings.neurips.cc/paper_files/paper/2024/hash/215aeb07b5996c969c0123c3c6ee8f54-Abstract-Conference.html">HumanVLA: Towards Vision-Language Directed Object Rearrangement by Physical Humanoid</a></td>
<td width="210">状态强化学习/AMP 教师蒸馏为第一视角视觉—语言—动作学生</td>
<td width="260">Isaac Gym 物理人体：15 刚体、28 个 PD 驱动关节、球形手；无真实机器人</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="300">HITR：615 项任务（552 训练 / 63 测试），50 个静态 + 34 个可动物体；OMOMO + SAMP 动作数据共 30 min</td>
<td width="260">教师策略：8×Tesla V100、约 2 d（换算约 384 GPU·小时）；学生策略：2 GPUs、约 1 d（换算约 48 GPU·小时，型号未披露）</td>
<td width="330">强化学习 + 蒸馏：训练特权 PPO/AMP 重排教师策略 → DAgger 行为克隆第一视角视觉语言学生策略 → 在仿真部署学生策略</td>
<td width="90">仅仿真</td>
<td width="300">仿真 60 Hz / 策略 30 Hz；585 个环境；教师策略约 2 d（8×V100），学生策略 20k 训练轮次</td>
<td width="330">用第一视角视觉和语言替代特权物体/目标状态，完成通用房间物体重排</td>
<td width="330">球形手不能操作小物体；每次只移动一个物体；无显式记忆、规划、导航或多智能体模块</td>
<td width="330">灵巧手、长时多物体任务、显式记忆/规划/导航和真实人形迁移</td>
</tr>
<tr>
<td width="105" nowrap>ICLR 2026</td>
<td width="280"><a href="https://openreview.net/forum?id=aQWSEjcN9V">Endowing GPT-4 with a Humanoid Body: Building the Bridge Between Off-the-Shelf VLMs and the Physical World</a></td>
<td width="210">视觉语言模型指令编译器 + 扩散动作执行器（BiBo）</td>
<td width="260">Isaac Gym 中 PHC/CLoSD 虚拟人体；非真实机器人</td>
<td width="220">Isaac Gym Preview 4；InfiniGen/Blender 场景，PyVHACD 碰撞体</td>
<td width="300">HumanML3D：24,545 训练回合 / 66,633 描述文本；4646 测试回合 / 12,536 描述文本；100 个合成场景、73 个物体类</td>
<td width="260">CUDA 后端；GPU 型号/数量和训练时间未披露；执行器最多训练 3000 个训练轮次</td>
<td width="330">从零训练执行器、视觉语言模型不微调：HumanML3D 上训练条件动作扩散执行器 → 现成 GPT-4o 编译结构化命令 → 物理闭环执行</td>
<td width="90">仅仿真</td>
<td width="300">100 场景、73 物体类；24,545 训练回合；20 FPS；在线动作 &gt;20 Hz</td>
<td width="330">无需微调 GPT-4，即把自然语言拆成可执行的人形动作参数</td>
<td width="330">文本—动作数据小；无场景几何；只覆盖人体—场景交互</td>
<td width="330">更大动作语料、几何/手物体/人际交互和真实机器人闭环</td>
</tr>
<tr>
<td width="105" nowrap>ICLR 2026</td>
<td width="280"><a href="https://openreview.net/forum?id=3UE3Aatcjy">HWC-Loco: A Hierarchical Whole-Body Control Approach to Robust Humanoid Locomotion</a></td>
<td width="210">安全恢复与目标跟踪的分层鲁棒控制</td>
<td width="260">Unitree H1（19 自由度主实机）；Unitree G1（23 自由度跨本体）</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="300">CMU 动作捕捉行走子集：318 条序列、3729.18 s</td>
<td width="260">1×RTX 4090；目标策略约 10 h、恢复策略约 8 h、高层策略不足 6 h（单卡，换算 GPU·小时数值相同）</td>
<td width="330">强化学习：训练带人体动作对抗对齐的目标跟踪策略 → 训练极端状态恢复策略 → 冻结两者并训练高层选择器</td>
<td width="90">仿真+实机</td>
<td width="300">4096 环境；目标/恢复/高层约 10k/8k/6k 次迭代；仿真与实机 100 Hz</td>
<td width="330">在训练—部署失配和扰动下动态权衡行走目标与安全恢复</td>
<td width="330">层级切换离散；低层策略固定；扰动覆盖和 H1 自由度有限</td>
<td width="330">联合学习层级、对抗扰动和安全的移动操作</td>
</tr>
<tr>
<td width="105" nowrap>ICLR 2026</td>
<td width="280"><a href="https://openreview.net/forum?id=6T3wJQhvc3">Task Tokens: A Flexible Approach to Adapting Behavior Foundation Models</a></td>
<td width="210">冻结行为基础模型，仅学习任务词元化器/词元</td>
<td width="260">69 自由度 SMPL 虚拟人体；非机器人</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="300">在预训练 MaskedMimic 上评测 5 项下游任务；每随机种子约 120M 帧；基础 BFM 动作捕捉规模未重述</td>
<td width="260">每个随机种子使用 1×A100 或 V100、约 1–2 GPU·天（换算 24–48 GPU·小时）；共 5 个随机种子；4000 个训练轮次 / 1024 环境</td>
<td width="330">参数高效强化学习适配：冻结预训练 MaskedMimic BFM → PPO 训练约 200k 参数的任务编码器 → 学习词元与现有提示组合</td>
<td width="90">仅仿真</td>
<td width="300">仿真 120 Hz / 控制器 30 Hz；每随机种子 1024 环境；约 120M 帧</td>
<td width="330">以少量参数让行为基础模型适配新任务</td>
<td width="330">只验证一个基础模型；手部奖励/观测简化；每任务仍需编码器；无仿真到现实</td>
<td width="330">共享与可组合词元、持续学习、自动任务发现和实机适配</td>
</tr>
<tr>
<td width="105" nowrap>ICLR 2026</td>
<td width="280"><a href="https://openreview.net/forum?id=jkhl2oI0g5">BFM-Zero: A Promptable Behavioral Foundation Model for Humanoid Control Using Unsupervised Reinforcement Learning</a></td>
<td width="210">无监督 Forward-Backward 强化学习的可提示行为基础模型</td>
<td width="260">Unitree G1 29 自由度主实机；Booster T1 补充验证；不控制手指</td>
<td width="220">Isaac Lab 训练；MuJoCo 跨引擎测试</td>
<td width="300">LAFAN1：40 条数分钟动作作训练；AMASS-CMU：175 条分布外动作 + 10 个精选姿态作评测</td>
<td width="260">1024 环境；3M 梯度更新步；GPU 型号和墙钟时间未披露</td>
<td width="330">无监督预训练 + 可选后训练：带动作捕捉正则和域随机化的离策略 FB-CPR → 零样本提示 → CEM/轨迹优化作少样本潜变量适配</td>
<td width="90">仿真+实机</td>
<td width="300">仿真 200 Hz / 控制 50 Hz；1024 环境；约 192M 环境步</td>
<td width="330">用动作、目标或奖励提示同一策略完成多类全身技能</td>
<td width="330">能力受运动库覆盖限制；缺少在线自适应</td>
<td width="330">行为数据规模律、在线后训练和安全适应</td>
</tr>
<tr>
<td width="105" nowrap>ICLR 2026</td>
<td width="280"><a href="https://openreview.net/forum?id=k3Cyx3Uets">From Language to Locomotion: Retargeting-free Humanoid Control via Motion Latent Guidance</a></td>
<td width="210">语言条件动作潜变量 + 直接动作扩散（RoboGhost）</td>
<td width="260">Unitree G1，23 自由度 PD 目标；Orin NX；不控制手指</td>
<td width="220">Isaac Gym 训练；MuJoCo 跨引擎</td>
<td width="300">MotionMillion：50,378 条动作；使用未见 MotionMillion 潜变量作泛化测试</td>
<td width="260">GPU 型号/数量和训练墙钟时间未披露</td>
<td width="330">预训练 + 强化学习：从 MotionMillion 学习语言对齐动作潜变量 → 在动作潜变量引导下训练免重定向机器人策略 → MuJoCo 与真实 G1 迁移</td>
<td width="90">仿真+实机</td>
<td width="300">50,378 条动作；策略 50 Hz / 低层 500 Hz；隐式 5.84 s 对比 显式 17.85 s</td>
<td width="330">绕过人体动作解码和重定向，直接从语言潜变量产生机器人动作</td>
<td width="330">未见 MotionMillion 潜变量表现差；更大 DiT 增加实时延迟</td>
<td width="330">更快动作生成器与视觉、语音等多模态潜空间</td>
</tr>
<tr>
<td width="105" nowrap>ICLR 2026</td>
<td width="280"><a href="https://openreview.net/forum?id=NEOTsyyYH7">Towards Bridging the Gap between Large-Scale Pretraining and Efficient Finetuning for Humanoid Control</a></td>
<td width="210">大批量 SAC 预训练 + 模型辅助微调（LIFT）</td>
<td width="260">仿真：Booster T1（12/23 自由度）与 G1（29 自由度）；实机仅 T1 12 自由度双腿</td>
<td width="220">MuJoCo Playground 预训练；Brax 微调/目标仿真</td>
<td width="300">无命名公开训练数据集；评测 1024 个回合、每回合 1000 步；实机微调使用 80–590 s 交互数据</td>
<td width="260">1×RTX 4090；调参后 SAC 预训练约 0.5 h（换算约 0.5 GPU·小时）；超参数搜索约 10 h（换算约 10 GPU·小时）；实机微调墙钟时间为数小时</td>
<td width="330">预训练 + 基于模型的微调：大批量 SAC 预训练 → 物理信息世界模型预训练 → 交替执行确定性实机采集、世界模型更新和想象 SAC 轨迹生成</td>
<td width="90">仿真+实机</td>
<td width="300">评测 1024 个回合（每回合 1000 步）；单 RTX 4090 预训练 &lt;1 h；50 Hz；真机微调数据 80–590 s</td>
<td width="330">连接大规模离策略预训练与新环境中的样本高效适配</td>
<td width="330">依赖人工急停/复位、Vicon 高度、串行训练；IMU 漂移且仅本体感知</td>
<td width="330">自动复位与安全、异步微调，以及视觉/触觉反馈</td>
</tr>
<tr>
<td width="105" nowrap>AAAI 2026</td>
<td width="280"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38918">Coordinated Humanoid Robot Locomotion with Symmetry Equivariant Reinforcement Learning Policy</a></td>
<td width="210">对称等变强化学习策略（SE-Policy）</td>
<td width="260">Unitree G1，27 自由度机体；无手指控制</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="300">无命名公开基准/数据集；Unitree G1 速度跟踪任务</td>
<td width="260">RTX 4090、约 4 h、超过 5k 次迭代；GPU 数量未披露，不能计算 GPU·小时</td>
<td width="330">从零强化学习：将严格左右等变/不变结构写入 PPO 演员/评论家 → 域随机化仿真 → 零样本实机部署</td>
<td width="90">仿真+实机</td>
<td width="300">训练 &gt;5k 次迭代、约 4 h（RTX 4090）；控制频率未披露</td>
<td width="330">把左右对称结构显式写入策略以提高协调行走和迁移</td>
<td width="330">只验证单一对称 G1 速度跟踪；严格对称不适合非对称任务和负载</td>
<td width="330">条件式/近似对称、非对称操作和跨本体验证</td>
</tr>
<tr>
<td width="105" nowrap>AAAI 2026</td>
<td width="280"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38924">FARM: Frame-Accelerated Augmentation and Residual Mixture-of-Experts for Physics-Based High-Dynamic Humanoid Control</a></td>
<td width="210">帧加速增广 + 残差混合专家</td>
<td width="260">Isaac Lab 中未命名物理人体角色；非真实机器人</td>
<td width="220">NVIDIA Isaac Lab</td>
<td width="300">HDHM：3593 段片段、平均 9.4 s，来自 5 个来源；AMASS 训练/测试用于训练和评测</td>
<td width="260">1×RTX 4090；难样本微调 6 h（换算 6 GPU·小时），对照完整数据训练 35 h（换算 35 GPU·小时）</td>
<td width="330">微调：用冻结基础控制器挖掘 AMASS 失败样本 → 帧加速难样本 → 冻结主干网络，训练输出 MLP + 残差混合专家 → HDHM 零样本评测</td>
<td width="90">仅仿真</td>
<td width="300">统一 30 Hz；3593 段片段、平均 9.4 s；困难样本训练约 6 h（完整数据 35 h）</td>
<td width="330">扩充高动态动作数据并融合专家残差以提升跟踪</td>
<td width="330">源数据含穿透、漂浮、抖动等伪影；无实机验证</td>
<td width="330">清洗物理一致数据、接触感知增广与真实人形迁移</td>
</tr>
<tr>
<td width="105" nowrap>AAAI 2026</td>
<td width="280"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38949">Keep On Going: Learning Robust Humanoid Motion Skills via Selective Adversarial Training</a></td>
<td width="210">选择性对抗扰动训练</td>
<td width="260">Unitree G1；不控制手指</td>
<td width="220">Isaac Gym + Legged Gym</td>
<td width="300">无命名公开训练数据集；感知行走与全身控制任务组</td>
<td width="260">约 6k 攻击策略 / 10k 动作策略次迭代；GPU 型号和墙钟时间未披露</td>
<td width="330">后训练 / 对抗强化学习：以预训练动作策略初始化 → 交替优化选择性攻击策略与鲁棒动作策略 → 零样本实机部署</td>
<td width="90">仿真→实机</td>
<td width="300">策略 50 Hz；地形高度图 10 Hz；对抗训练约 6k/10k 次迭代</td>
<td width="330">在保持动作质量的同时提高技能受扰后的持续执行能力</td>
<td width="330">未覆盖环境交互型扰动；对抗强度与敏捷性有权衡</td>
<td width="330">接触级对抗器、自适应扰动预算和任务安全约束</td>
</tr>
<tr>
<td width="105" nowrap>AAAI 2026</td>
<td width="280"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38951">Towards Adaptive Humanoid Control via Multi-Behavior Distillation and Reinforced Fine-Tuning</a></td>
<td width="210">多行为蒸馏 + 实机强化微调</td>
<td width="260">Unitree G1，控制 20 自由度（不含腰）；无手指控制</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="300">重定向恢复动作捕捉 + LAFAN1 行走数据；数据规模未披露</td>
<td width="260">4096 环境；最终 10k 次迭代微调使用 2×RTX 4090；前期 10k 策略 + 4k 蒸馏的 GPU/耗时未披露</td>
<td width="330">蒸馏 + 强化微调：训练恢复与行走专用策略 → DAgger 多行为蒸馏 → 带行为专用价值网络的 PPO 多任务地形微调</td>
<td width="90">仿真→实机</td>
<td width="300">4096 环境；10k + 4k + 10k 次迭代；真机策略 50 Hz / PD 500 Hz</td>
<td width="330">把多种动作压入统一策略并在真实硬件上继续适配</td>
<td width="330">仅本体感知；行为和环境覆盖仍少</td>
<td width="330">外感知、更大统一技能库和安全在线适应</td>
</tr>
<tr>
<td width="105" nowrap>ICML 2026</td>
<td width="280"><a href="https://icml.cc/virtual/2026/poster/62003">Scalable and General Whole-Body Control for Cross-Humanoid Locomotion</a></td>
<td width="210">跨形态随机化的通用全身控制（XHugWBC）</td>
<td width="260">12 个仿真平台/13 配置；7 类实机：Booster T1、Fourier N1、Unitree G1（23/29 自由度）、AgiBot X2、Dobot Atom、Unitree H1-2；无统一手部控制</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="300">跨本体基准：12 个人形仿真平台 / 13 配置，7 类实机变体</td>
<td width="260">GPU 型号/数量和训练墙钟时间未披露</td>
<td width="330">通用策略预训练 + 可选微调：生成物理一致随机形态 → 训练单个结构感知 PPO 策略 → 零样本部署；通用权重可初始化单机微调</td>
<td width="90">仿真+实机</td>
<td width="300">12 类仿真 / 7 类真机；通用约专用的 85%；0.6 m/s×10 s×5 次/本体</td>
<td width="330">让同一全身行走控制框架跨多种人形形态迁移</td>
<td width="330">共享语义命令压缩各本体特性；动作范围和重定向仍依赖形态</td>
<td width="330">形态感知动作空间、免人工重定向和跨平台全身操作</td>
</tr>
<tr>
<td width="105" nowrap>ICML 2026</td>
<td width="280"><a href="https://openreview.net/forum?id=Gd2S0bJqNZ">Learning Transferable Interaction Primitives from Game Videos for Humanoid Locomotion</a></td>
<td width="210">游戏视频 VQ 交互原语 + 物理策略（TRIP）</td>
<td width="260">使用 PULSE 先验的通用仿真人体；非真实机器人</td>
<td width="220">物理引擎未披露；复用 PULSE 先验/编码器/解码器</td>
<td width="300">未标注游戏视频数据集，规模未披露；PULSE 动作先验基于 AMASS</td>
<td width="260">1536 并行环境；GPU 型号/数量和墙钟时间未披露</td>
<td width="330">预训练复用 + 强化学习：复用 PULSE 动作先验 → 从游戏视频学习 VQ 交互原语 → 对齐视频/地形上下文潜变量 → 训练物理策略选择原语</td>
<td width="90">仅仿真</td>
<td width="300">1536 并行环境；32×32×3 高度图，覆盖 2×2 m²</td>
<td width="330">从游戏视频抽取可复用原语并迁移到物理人体控制</td>
<td width="330">动作重建误差；任务主要是地形交互；无真实机器人迁移</td>
<td width="330">第一视角/深度输入、物体与工具交互，以及仿真到现实</td>
</tr>
<tr>
<td width="105" nowrap>CVPR 2026</td>
<td width="280"><a href="https://openaccess.thecvf.com/content/CVPR2026/html/He_VIRAL_Visual_Sim-to-Real_at_Scale_for_Humanoid_Loco-Manipulation_CVPR_2026_paper.html">VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation</a></td>
<td width="210">特权教师 + 视觉学生蒸馏 + DAgger/BC</td>
<td width="260">Unitree G1 29 自由度 + 双 7 自由度 Dex3-1 三指手 + RealSense D435i</td>
<td width="220">Isaac Lab（Isaac Sim 栈）；MuJoCo 跨引擎评测</td>
<td width="300">200 条遥操作仿真演示用于参考状态初始化；未使用真实世界训练数据</td>
<td width="260">教师：16× NVIDIA L40S；视觉学生：64× L40S；墙钟时间未披露</td>
<td width="330">预训练 + 强化学习 + 模仿/蒸馏：预训练 HOMIE WBC → 特权 PPO 教师 → DAgger/BC 视觉学生 → 域随机化与系统辨识 → 实机零样本部署</td>
<td width="90">仿真→实机</td>
<td width="300">教师策略 16×L40S / 学生策略 64×L40S；200 条仿真示范；实机 54/59 连续循环成功</td>
<td width="330">规模化训练并零样本部署视觉全身移动操作</td>
<td width="330">长尾物理/任务、奖励工程和手部仿真差距仍大；训练最高需 64 GPU</td>
<td width="330">仿真+真实模仿混合数据和人形视觉—触觉基础策略</td>
</tr>
<tr>
<td width="105" nowrap>NeurIPS 2025</td>
<td width="280"><a href="https://proceedings.neurips.cc/paper_files/paper/2025/hash/6b081a311e0b9c75590ba97b104a2ce3-Abstract-Conference.html">Adversarial Locomotion and Motion Imitation for Humanoid Policy Learning</a></td>
<td width="210">上下身对抗学习的运动—模仿协同（ALMI）</td>
<td width="260">Unitree H1-2（控制 21 自由度）；ROBOTERA XHAND 手指由 VR 重定向，非 ALMI 端到端学习</td>
<td width="220">Isaac Gym 训练；MuJoCo 数据生成/验证</td>
<td width="300">ALMI-X：&gt;8 万条 MuJoCo 轨迹，平均约 4 s / 200 步，由 AMASS 动作生成；CMU 动作捕捉评测集 1,122 段</td>
<td width="260">GPU 型号/数量未披露；三轮对抗迭代合计约 17 h</td>
<td width="330">强化学习 + 监督预训练：上下半身对抗式 PPO → 采集 ALMI-X → 监督训练自回归 Transformer 基础控制器</td>
<td width="90">仿真+实机</td>
<td width="300">4096 环境；&gt;80k 条轨迹；实机 50 Hz；CMU 评测 1122 段片段</td>
<td width="330">在稳定行走时跟踪多样上身和全身表达动作</td>
<td width="330">动态舞蹈较弱；把全部数据直接训练一个基础模型会降质且低效</td>
<td width="330">统一奖励与更强架构，并把手指/接触纳入端到端策略</td>
</tr>
<tr>
<td width="105" nowrap>NeurIPS 2025</td>
<td width="280"><a href="https://neurips.cc/virtual/2025/poster/117371">From Experts to a Generalist: Toward General Whole-Body Control for Humanoid Robots</a></td>
<td width="210">专家聚类、实机适配与通用策略蒸馏（BumbleBee）</td>
<td width="260">Unitree G1 29 自由度，控制 23 自由度（腕部不控制）</td>
<td width="220">Isaac Gym 训练；MuJoCo 跨引擎评测</td>
<td width="300">过滤后的 AMASS：8,179 条轨迹、6 个聚类；HumanML3D 提供文本标注；每簇每轮 20 个动作×8 次实机轨迹展开</td>
<td width="260">两台桌面机，每台 1× RTX 4090、64 GB 内存；墙钟时间未披露</td>
<td width="330">预训练 + 微调 + 后训练/蒸馏：通用 PPO 跟踪器 → 分簇专家 → 基于实机数据的增量动作细化 → DAgger 知识蒸馏为单一通才</td>
<td width="90">仿真+实机</td>
<td width="300">6 个运动簇；批大小 4096；每轮 20 个动作×8 实机轨迹展开</td>
<td width="330">缓解多种敏捷动作间冲突，把多专家压入一个全身控制器</td>
<td width="330">无 GPS/VIO 时参考漂移；专家—实机—蒸馏流水线复杂</td>
<td width="330">精确状态估计、在线反馈和更简单的统一后训练</td>
</tr>
<tr>
<td width="105" nowrap>NeurIPS 2025</td>
<td width="280"><a href="https://proceedings.neurips.cc/paper_files/paper/2025/hash/5a0e51901cff2b42d379ec7869603e91-Abstract-Conference.html">KungfuBot: Physics-Based Humanoid Whole-Body Control for Learning Highly-Dynamic Skills</a></td>
<td width="210">物理模仿 + 自适应跟踪课程</td>
<td width="260">Unitree G1，控制 23 自由度（腕部不控制）</td>
<td width="220">Isaac Gym 训练；MuJoCo 仿真到仿真</td>
<td width="300">13 段高动态参考动作，由 AMASS、LAFAN 与人体视频动作处理共同构建</td>
<td width="260">1× NVIDIA RTX 4090；每模型 27 h = 27 GPU·小时（换算）</td>
<td width="330">从零强化学习/动作模仿：视频与动作集处理 → IK 重定向和物理过滤 → 带自适应跟踪课程的非对称演员—评论家 PPO → 仿真到现实</td>
<td width="90">仿真→实机</td>
<td width="300">13 个高动态动作；3 随机种子×1000 个回合；单 RTX 4090 训练 27 h</td>
<td width="330">跟踪功夫、舞蹈等高速高动态人体动作</td>
<td width="330">未覆盖复杂地形/障碍；每个参考动作仍需独立策略</td>
<td width="330">感知条件、多技能统一策略与在线动作组合</td>
</tr>
<tr>
<td width="105" nowrap>CVPR 2025</td>
<td width="280"><a href="https://openaccess.thecvf.com/content/CVPR2025/html/Lin_Let_Humanoids_Hike_Integrative_Skill_Development_on_Complex_Trails_CVPR_2025_paper.html">Let Humanoids Hike! Integrative Skill Development on Complex Trails</a></td>
<td width="210">感知、落脚、平衡的集成式山径技能（LEGO-H）</td>
<td width="260">Isaac 中 Unitree H1 与 G1；下肢/腿部位置控制，无手部</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="300">LEGO-H Humanoid Hiking 基准：5 类程序化路线（RandomMix、Ditch、Hurdle、Gap、Forest）；无外部数据集</td>
<td width="260">1× NVIDIA A40；理想参照策略约 18 GPU·小时；统一策略约 2 GPU·天</td>
<td width="330">强化学习 + 特权蒸馏：PPO 训练理想参照运动策略 → 通过分层损失蒸馏为视觉条件 TC-ViTs 导航/运动策略</td>
<td width="90">仅仿真</td>
<td width="300">10-D 动作；策略 50 Hz；模拟深度 10±2 Hz；仅仿真</td>
<td width="330">集成复杂山径中的感知、行走和动态平衡</td>
<td width="330">原型只在仿真山径；主要足部接触；未评测公里级、能耗或真实户外</td>
<td width="330">真实户外长程、能效、全身接触和高层路径规划</td>
</tr>
<tr>
<td width="105" nowrap>RSS 2024</td>
<td width="280"><a href="https://www.roboticsproceedings.org/rss20/p107.html">Expressive Whole-Body Control for Humanoid Robots</a></td>
<td width="210">动作捕捉上身模仿 + 鲁棒速度跟踪（ExBody）</td>
<td width="260">Unitree H1，19 自由度；无灵巧手控制</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="300">CMU 动作捕捉子集：780 段 / 13,383 s（约 3.7 h）</td>
<td width="260">GPU 型号/数量及墙钟时间未披露；4,096 个并行环境</td>
<td width="330">强化学习动作模仿：筛选并重定向 CMU 动作捕捉 → 带参考状态初始化的目标条件 PPO → 域随机化 → H1 零样本部署</td>
<td width="90">仿真→实机</td>
<td width="300">4096 个环境；780 段动作捕捉片段 / 3.7 h；20 s 轨迹展开</td>
<td width="330">在人体—机器人形态不匹配下兼顾上身表达性和下肢稳定移动</td>
<td width="330">低自由度映射丢失动作信息；需从静止站姿启动，缺少自动恢复</td>
<td width="330">高保真重定向、自动初始化和跌倒恢复</td>
</tr>
<tr>
<td width="105" nowrap>RSS 2024</td>
<td width="280"><a href="https://www.roboticsproceedings.org/rss20/p061.html">HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation</a></td>
<td width="210">27 项全身运动—操作基准 + 分层强化学习</td>
<td width="260">主模型 Unitree H1 + 双 Shadow Hand；另含 G1、Digit、Robotiq 2F-85、13 自由度宇树灵巧手模型</td>
<td width="220">MuJoCo；MJX 用于并行到达任务 PPO</td>
<td width="300">HumanoidBench：27 项任务（15 项操作 + 12 项运动），时域 500–1,000，最多 61 个执行器、448 个触觉触觉单元</td>
<td width="260">GPU 型号/数量未披露；基线约 48 h；MJX 伸手预训练：单手 2B 步/36 h，双手 4B 步/60 h</td>
<td width="330">基准训练：训练 DreamerV3、TD-MPC2、SAC、PPO 平坦基线；分层版本先用 MJX PPO 预训练并冻结伸手策略，再训练高层策略</td>
<td width="90">仅仿真</td>
<td width="300">27 项任务（15 操作 + 12 运动）；最多 61 执行器；时域长度 500–1000；448 触觉单元</td>
<td width="330">提供可复现高维、长时、全身运动与操作统一评测</td>
<td width="330">论文基线只用状态观测；视觉/全身触觉未系统评测；环境真实度有限</td>
<td width="330">多模态基线、更真实数字孪生和标准化仿真到现实评测</td>
</tr>
<tr>
<td width="105" nowrap>CoRL 2025</td>
<td width="280"><a href="https://proceedings.mlr.press/v305/ze25a.html">TWIST: Teleoperated Whole-Body Imitation System</a></td>
<td width="210">动作捕捉重定向 + 强化学习/BC 单一全身控制器</td>
<td width="260">Unitree G1 29 自由度主实机；Booster T1 仅仿真到仿真；未披露独立灵巧手型号</td>
<td width="220">Isaac Gym 训练；MuJoCo 做 T1 仿真到仿真</td>
<td width="300">AMASS + OMOMO：&gt;15,000 段 / 约 42 h；自采动作捕捉：150 段 / 约 0.5 h；另有 50 段评测集</td>
<td width="260">GPU 型号/数量及墙钟时间未披露</td>
<td width="330">强化学习 + 行为克隆：离线/在线动作捕捉 → 重定向人形动作库 → 带未来特权帧和 BC 的统一 PPO 教师 → 实时遥操作</td>
<td width="90">仿真+实机</td>
<td width="300">15k 段片段≈42 h + 150 段片段≈0.5 h；遥操作/策略 50 Hz；PD 1 kHz</td>
<td width="330">以人体动作统一遥操作全身操作、腿部操作、行走和表达动作</td>
<td width="330">无第一视角视觉或触觉反馈；依赖不便携动作捕捉；硬件过热</td>
<td width="330">RGB 姿态替代动作捕捉，并用第一视角+触觉数据训练自主策略</td>
</tr>
<tr>
<td width="105" nowrap>RSS 2023</td>
<td width="280"><a href="https://www.roboticsproceedings.org/rss19/p052.html">Robust and Versatile Bipedal Jumping Control through Reinforcement Learning</a></td>
<td width="210">目标条件策略 + 多阶段强化学习</td>
<td width="260">Cassie 双足机器人</td>
<td width="220">MuJoCo</td>
<td width="300">无外部数据集；1 段原地跳参考动画与程序化采样的多轴跳跃目标</td>
<td width="260">GPU 型号/数量及墙钟时间未披露；PPO 三阶段分别 6k、12k、20k 次迭代，每次 65,536 个样本</td>
<td width="330">从零强化学习：单目标跳跃模仿 → 多目标微调 → 动力学随机化微调 → Cassie 零样本部署</td>
<td width="90">仿真→实机</td>
<td width="300">策略 33 Hz；PD 2 kHz；750 步≈23 s</td>
<td width="330">用同一策略完成多方向、多高度跳跃、落点控制与扰动恢复</td>
<td width="330">同一策略兼顾跳跃与静止时部分落地会振荡；缺少环境感知落点选择</td>
<td width="330">加入感知与任务规划，在非结构环境自主选择落点</td>
</tr>
<tr>
<td width="105" nowrap>CoRL 2024</td>
<td width="280"><a href="https://proceedings.mlr.press/v270/cui25a.html">Adapting Humanoid Locomotion over Challenging Terrain via Two-Phase Training</a></td>
<td width="210">两阶段强化学习 + 命令课程 + 状态估计</td>
<td width="260">自研 Noetix N1：18 自由度、0.95 m、23 kg；锁臂后控制 10 个腿关节</td>
<td width="220">Isaac Gym 训练；MuJoCo / PyBullet / Gazebo 跨引擎</td>
<td width="300">无外部数据集；程序化平地、台阶、斜坡和楼梯，以及地形/速度课程</td>
<td width="260">GPU 型号/数量及墙钟时间未披露；4,096 个环境；回合长度 3,000；每次更新训练 2 个训练轮次</td>
<td width="330">两阶段强化学习：较易地形上的参考步态 PPO → 去除模仿奖励并在更难地形继续课程强化学习、联合隐状态估计 → 域随机化 → 仿真到现实</td>
<td width="90">仿真→实机</td>
<td width="300">4096 个环境；控制器 100 Hz；PD 控制 1 kHz</td>
<td width="330">改善小型人形在复杂地面上的高速跟踪、振荡和迁移</td>
<td width="330">没有地形感知；跨机器人仍需复杂奖励、域随机化和时序调参</td>
<td width="330">感知与模仿结合，并降低跨平台调参成本</td>
</tr>
<tr>
<td width="105" nowrap>IROS 2022</td>
<td width="280"><a href="https://doi.org/10.1109/IROS47612.2022.9981091">Adapting Rapid Motor Adaptation for Bipedal Robots</a></td>
<td width="210">外部参数估计 + 基础策略再适配（A-RMA）</td>
<td width="260">Cassie，20 自由度 / 10 个驱动关节</td>
<td width="220">Cassie MuJoCo；MATLAB Simulink 高保真验证</td>
<td width="300">无外部数据集；HZD 生成参考步态，并程序化随机地形、动力学和命令</td>
<td width="260">GPU 型号/数量及墙钟时间未披露；适配模块 2,000 次迭代、PPO 微调 2,000 次迭代，批大小 65,536</td>
<td width="330">预训练 + 监督适配 + 强化学习微调：训练特权基础策略 → 从状态/动作历史回归外部参数 → 冻结适配器并用 PPO 微调基础策略 → 零样本部署</td>
<td width="90">仿真→实机</td>
<td width="300">策略 30 Hz；PD 2 kHz；2500 步≈83 s；适配历史约 2 s</td>
<td width="330">在线适应湿滑、软地面、木板和约 40 kg 拖载等动力学变化</td>
<td width="330">仅本体感知，是盲走控制器</td>
<td width="330">机载视觉与快速动力学适应融合</td>
</tr>
<tr>
<td width="105" nowrap>ICRA 2024</td>
<td width="280"><a href="https://doi.org/10.1109/ICRA57147.2024.10611621">Learning Vision-Based Bipedal Locomotion for Challenging Terrain</a></td>
<td width="210">深度历史 + 本体状态预测局部高度图</td>
<td width="260">Cassie + RealSense D455 + Jetson Orin Nano</td>
<td width="220">MuJoCo</td>
<td width="300">仿真生成高度图数据：30,000 个回合，含 848×480 深度图（缩放到 128×128）、机器人状态和真实局部高度图</td>
<td width="260">运动 PPO：双 Xeon Platinum 8280 的 80 个 CPU 核；高度图预测器 GPU/时间未披露</td>
<td width="330">强化学习 + 监督学习：训练高度图条件运动策略 → 生成仿真深度/高度图回合 → 监督训练两阶段高度图预测器 → 域随机化零样本迁移</td>
<td width="90">仿真→实机</td>
<td width="300">策略 50 Hz；PD 2 kHz；30k 个回合；D455 90 FPS / 高度图可 200 Hz</td>
<td width="330">让双足从视觉提前感知台阶、楼梯和随机块地形</td>
<td width="330">相机看不到脚下；足部碰撞是主要失败；高台阶会使支撑腿扭矩饱和</td>
<td width="330">更大/全向视野、不确定性感知和碰撞约束落脚规划</td>
</tr>
<tr>
<td width="105" nowrap>ICRA 2024</td>
<td width="280"><a href="https://doi.org/10.1109/ICRA57147.2024.10610449">HumanMimic: Learning Natural Locomotion and Transitions for Humanoid Robot via Wasserstein Adversarial Imitation</a></td>
<td width="210">Wasserstein 对抗模仿 + 统一动作重定向</td>
<td width="260">全尺寸 JAXON 人形机器人模型</td>
<td width="220">Isaac Gym 训练；Choreonoid + Hrpsys 高保真仿真到仿真</td>
<td width="300">42.6 s 参考集：站立 5.1 s、蹲走 8.0 s、正常走 14.2 s、跑步 15.3 s；来源包括 CMU/SFU 动作捕捉、人工设计和已有控制器</td>
<td width="260">1× NVIDIA RTX 3090 Ti；约 30 h = 约 30 GPU·小时（换算）</td>
<td width="330">强化学习对抗模仿：重定向混合参考动作 → PPO 策略 + 带软边界损失的 Wasserstein 评论家 → 高保真仿真到仿真评测</td>
<td width="90">仅仿真</td>
<td width="300">参考运动 42.6 s；单 RTX 3090 Ti 训练约 30 h；无实机</td>
<td width="330">从混合人体动作学习站立、抗推、蹲走、直腿走、跑和自然切换</td>
<td width="330">只在仿真/高保真仿真到仿真验证，尚无真机迁移</td>
<td width="330">迁移到真实全尺寸人形并加入感知驱动的技能切换</td>
</tr>
<tr>
<td width="105" nowrap>IROS 2022</td>
<td width="280"><a href="https://doi.org/10.1109/IROS47612.2022.9981884">Learning Dynamic Bipedal Walking Across Stepping Stones</a></td>
<td width="210">单步强化学习控制器 + 可达性预测器</td>
<td width="260">Cassie + 固定俯视 RealSense D435 + ArUco 标记</td>
<td width="220">Cassie 仿真器；底层物理引擎未披露</td>
<td width="300">8 种人工设计踏脚石基准；可达性模型数据由仿真生成，策略学习在约 50M 样本处比较</td>
<td width="260">GPU 型号/数量及墙钟时间未披露</td>
<td width="330">预训练 + 强化学习 + 监督学习：预训练动力学模块 → PPO 微调落脚策略 → 采集仿真落脚数据 → 训练可达性预测器 → 相机引导实机部署</td>
<td width="90">仿真+实机</td>
<td width="300">策略/时钟 40 Hz；PD 2 kHz；中期约 50M 个样本；8 组踏脚石模式</td>
<td width="330">闭环选择可实现落脚点并动态穿越踏脚石</td>
<td width="330">依赖外部相机和标记；视野主要覆盖下一步，缺少多步初态规划</td>
<td width="330">降阶规划、多步前瞻和机载自中心视觉</td>
</tr>
<tr>
<td width="105" nowrap>CoRL 2024</td>
<td width="280"><a href="https://proceedings.mlr.press/v270/pandit25a.html">Learning Decentralized Multi-Biped Control for Payload Transport</a></td>
<td width="210">共享去中心化多智能体强化学习</td>
<td width="260">实机 2/3 台 Cassie；仿真扩展至 10 台</td>
<td width="220">自建多 Cassie 物理仿真；底层引擎未披露</td>
<td width="300">无外部数据集；程序化 1–3 台 Cassie 载荷架构，500 步/10 s 回合；训练 N=1–3、测试 N=2–10</td>
<td width="260">GPU 型号/数量未披露；三机器人去中心化策略约 245 h 达峰值回报（集中式基线约 1,000 h）</td>
<td width="330">从零多智能体强化学习：生成随机载荷架构/命令/扰动回合 → 共享去中心化 IPPO → 跨机器人数量和构型零样本迁移</td>
<td width="90">仿真→实机</td>
<td width="300">500 步=10 s；训练 N=1–3、仿真测试 N=2–10；20–80 kg 载荷、0–100 N 扰动</td>
<td width="330">不同数量和队形双足无需重训即可协作搬运刚性载荷</td>
<td width="330">仅平地；实机最多 3 台；无相机；成本、故障点和队形外泛化受限</td>
<td width="330">粗糙地形、异构双足、分布式感知通信与容错</td>
</tr>
<tr>
<td width="105" nowrap>RSS 2025</td>
<td width="280"><a href="https://www.roboticsproceedings.org/rss21/p063.html">Learning Getting-Up Policies for Real-World Humanoid Robots</a></td>
<td width="210">两阶段课程：先发现、再平滑可部署起身动作</td>
<td width="260">Unitree G1</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="300">第二阶段姿态集：20k 个随机仰卧姿态；第一阶段从规范仰卧/俯卧起始并生成起身参考轨迹</td>
<td width="260">1× RTX 4090 或 L40S；4,096 个环境；第一阶段约 5B 仿真步、第二阶段 20k 步；墙钟时间未披露</td>
<td width="330">两阶段强化学习：弱约束下发现起身/翻身轨迹 → 放慢并插值轨迹 → 用完整碰撞和地形随机化训练强正则跟踪策略 → 仿真到现实</td>
<td width="90">仿真→实机</td>
<td width="300">仿真 1 kHz / 控制 50 Hz；4096 环境；阶段 I≈5B 采样步；实机 78.3% 对比 41.7%</td>
<td width="330">从仰卧/俯卧在平地、湿滑、可变形、坡地、草雪地可靠起身</td>
<td width="330">只覆盖仰卧和俯卧，未覆盖任意侧卧与杂乱接触</td>
<td width="330">任意跌倒姿态、接触感知和起身—行走连续闭环</td>
</tr>
<tr>
<td width="105" nowrap>IROS 2024</td>
<td width="280"><a href="https://doi.org/10.1109/IROS58592.2024.10802816">Bipedal Safe Navigation over Uncertain Rough Terrain: Unifying Terrain Mapping and Locomotion Stability</a></td>
<td width="210">GP 地形/偏差建模 + 分层安全导航规划</td>
<td width="260">Agility Digit（MuJoCo 模型）</td>
<td width="220">MuJoCo</td>
<td width="300">3 张 20×20 m 地形图（每张 2,500 点）；地形 GP 用 500 点初始化、每步接收 10 个样本；每个局部目标评估 3 条候选轨迹</td>
<td width="260">GPU 型号/数量及训练墙钟时间未披露</td>
<td width="330">经典优化 + GP 学习：离线拟合运动偏差 GP → 在线更新地形 GP → 运动可行性感知的全局/局部 RRT* 规划 → MuJoCo 评测</td>
<td width="90">仅仿真</td>
<td width="300">3 个 20×20 m 环境（每个 2,500 点）；500 个 GP 初始点、每步 10 点；每个局部目标评 3 条候选轨迹</td>
<td width="330">联合未知地形建图、运动偏差与动态可行落脚规划</td>
<td width="330">尚无硬件实验</td>
<td width="330">Digit 户外实机、机载建图、不确定性校准和安全落脚闭环</td>
</tr>
<tr>
<td width="105" nowrap>IROS 2023</td>
<td width="280"><a href="https://doi.org/10.1109/IROS55552.2023.10342209">Overtaking Moving Obstacles with Digit: Path Following for Bipedal Robots via Model Predictive Contouring Control</a></td>
<td width="210">模型预测轮廓控制联合速度、路径偏差和落脚</td>
<td width="260">Agility Digit</td>
<td width="220">MuJoCo</td>
<td width="300">不适用：无学习型基准或训练数据集；评测曲线路径跟踪和 1 个移动障碍超越案例</td>
<td width="260">不适用（无学习策略）；MPCC 以 15 Hz 运行，平均求解约 12 ms</td>
<td width="330">无需训练/经典优化：在线 MPCC 选择速度、路径进度与落脚点 → 轨迹生成器 → 低层 QP 跟踪</td>
<td width="90">仅仿真</td>
<td width="300">物理仿真 2 kHz；MPCC 15 Hz；低层 QP 400 Hz；时域长度 5；平均求解 12 ms</td>
<td width="330">让双足在线权衡路径忠实度与速度并超越移动障碍</td>
<td width="330">仅高保真仿真；未覆盖杂乱三维空间的完整安全走廊</td>
<td width="330">真实 Digit 验证并集成安全行走走廊</td>
</tr>
<tr>
<td width="105" nowrap>IROS 2023</td>
<td width="280"><a href="https://doi.org/10.1109/IROS55552.2023.10341263">Template Model Inspired Task Space Learning for Robust Bipedal Locomotion</a></td>
<td width="210">ALIP 启发高层强化学习 + 模型低层控制</td>
<td width="260">Rabbit、Walker2D、Digit（20 个驱动关节）</td>
<td width="220">MuJoCo</td>
<td width="300">无外部数据集；在 Rabbit、Walker2D、Digit 上生成仿真回合，最长 300 步 / 9 s</td>
<td width="260">GPU 型号/数量及墙钟时间未披露</td>
<td width="330">从零强化学习：训练受 ALIP 启发的高层 PPO 任务空间策略 → 生成摆脚/机体命令 → 模型低层控制器跟踪</td>
<td width="90">仅仿真</td>
<td width="300">低层 1 kHz；高层 33 Hz；300 步=9 s；三种本体均仅仿真</td>
<td width="330">以统一低维任务空间接口跨不同双足形态稳健行走</td>
<td width="330">三种本体均无硬件验证；任务主要是速度、斜坡和扰动</td>
<td width="330">Digit 实机以及平衡、楼梯、踏脚石等更广任务</td>
</tr>
<tr>
<td width="105" nowrap>RSS 2025</td>
<td width="280"><a href="https://www.roboticsproceedings.org/rss21/p070.html">HOMIE: Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit</a></td>
<td width="210">强化学习下肢 + 同构外骨骼双臂 + 动作手套</td>
<td width="260">Unitree G1 + 双 Dex3-1（每手 7 自由度）主实机；Fourier GR-1 仿真/外骨骼适配</td>
<td width="220">Isaac Gym 训练；Isaac Sim / Isaac Lab（GRUtopia）跨引擎</td>
<td width="300">不使用动作先验数据集；驾驶舱采集任务演示用于训练自主模仿策略，数量未披露</td>
<td width="260">1× NVIDIA RTX 4090；4,096 个环境；约 3 h = 约 3 GPU·小时（换算）</td>
<td width="330">从零强化学习 + 可选模仿：面向任意上身姿态的运动/下蹲课程 PPO → 零样本部署 → 驾驶舱演示 → 自主模仿策略</td>
<td width="90">仿真+实机</td>
<td width="300">4096 环境；单 RTX 4090≈3 h；运动策略 π_loco 为 50 Hz；D455≈30 Hz；模仿学习闭环 10 Hz</td>
<td width="330">以低成本驾驶舱高效遥操作大工作区、接触丰富的移动操作</td>
<td width="330">复杂地形可靠性、手套拇指人体工学、力反馈和腰部遥操作不足</td>
<td width="330">地形能力、力/触觉反馈、腰部控制和自主数据飞轮</td>
</tr>
<tr>
<td width="105" nowrap>RSS 2025</td>
<td width="280"><a href="https://www.roboticsproceedings.org/rss21/p061.html">AMO: Adaptive Motion Optimization for Hyper-Dexterous Humanoid Whole-Body Control</a></td>
<td width="210">轨迹优化 + 仿真到现实强化学习自适应器</td>
<td width="260">Unitree G1 29 自由度 + 双 Dex3-1（每手 7 自由度）+ 3 自由度主动头 + ZED Mini</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="300">混合 AMO 数据集：轨迹优化生成的下身动作，条件为采样躯干/运动命令，并融合 AMASS 手臂命令；规模未披露</td>
<td width="260">训练 GPU 型号/数量及墙钟时间未披露；4,096 个环境；Jetson Orin NX 以 50 Hz 部署</td>
<td width="330">数据生成 + 强化学习蒸馏 + 模仿：轨迹优化 → 训练 AMO 适配器 → 特权教师/学生下身强化学习 → 可选遥操作轨迹展开与 ACT 行为克隆</td>
<td width="90">仿真+实机</td>
<td width="300">每项 4096 环境×500 步；Orin NX 50 Hz 推理</td>
<td width="330">扩大蹲、弯、拾地物等全身操作工作区并适应分布外命令</td>
<td width="330">上下身解耦限制动态协调；手臂生成不感知基座状态</td>
<td width="330">平衡感知上身生成与统一全身接触控制</td>
</tr>
<tr>
<td width="105" nowrap>RSS 2025</td>
<td width="280"><a href="https://www.roboticsproceedings.org/rss21/p067.html">A Unified and General Humanoid Whole-Body Controller for Fine-Grained Locomotion</a></td>
<td width="210">通用命令空间 + 对称损失 + 干预训练（HugWBC）</td>
<td width="260">Unitree H1，19 自由度；无独立手指策略</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="300">无外部数据集；程序化采样运动、步态、机体姿态和上身干预命令</td>
<td width="260">1× NVIDIA RTX 4090；约 16 h = 约 16 GPU·小时（换算）</td>
<td width="330">从零强化学习：在统一命令空间用非对称演员—评论家 PPO → 对称损失与步态课程 → 上身干预课程 → H1 零样本部署</td>
<td width="90">仿真→实机</td>
<td width="300">控制 50 Hz；1000 步=20 s；单 RTX 4090≈16 h；4096 条轨迹的扰动评测</td>
<td width="330">一个控制器统一走、跑、站、跳、单脚跳和细粒度步态参数</td>
<td width="330">仍是低层 WBC；无自主高层规划；侧向命令和硬件磨损受 H1 限制</td>
<td width="330">跨人形部署并叠加任务级规划器</td>
</tr>
<tr>
<td width="105" nowrap>RSS 2025</td>
<td width="280"><a href="https://www.roboticsproceedings.org/rss21/p068.html">BeamDojo: Learning Agile Humanoid Locomotion on Sparse Footholds</a></td>
<td width="210">多边形足稀疏奖励 + 双评论家 + 两阶段强化学习</td>
<td width="260">Unitree G1，23 驱动自由度 + Orin NX + Livox Mid-360；无灵巧手</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="300">无外部数据集；5 类程序化稀疏落脚地形、8 个课程难度等级；15×15 局部高度图</td>
<td width="260">GPU 型号/数量及墙钟时间未披露；4,096 个并行机器人</td>
<td width="330">两阶段强化学习：平地动力学下使用任务地形感知、软落脚惩罚和双评论家 PPO → 在真实任务地形硬接触下微调 → 噪声激光雷达地图仿真到现实</td>
<td width="90">仿真→实机</td>
<td width="300">4096 机器人；策略 50 Hz / PD 控制 500 Hz；激光雷达地图 10 Hz；踏脚石 20 cm、最大间距 45 cm</td>
<td width="330">在平衡木和踏脚石上实现精确落脚与抗扰</td>
<td width="330">激光雷达里程计/地图漂移；动态支撑难仿真；极小踏脚石和大台阶性能陡降</td>
<td width="330">不确定性感知、动态支撑建模和更强步幅/平衡目标</td>
</tr>
<tr>
<td width="105" nowrap>CoRL 2024</td>
<td width="280"><a href="https://proceedings.mlr.press/v270/li25a.html">OKAMI: Teaching Humanoid Robots Manipulation Skills through Single Video Imitation</a></td>
<td width="210">单段 RGB-D 人类视频 + 物体感知重定向 + 闭环策略</td>
<td width="260">Fourier GR-1 + 双 Inspire 灵巧手（每手 6 驱动自由度）</td>
<td width="220">主方法不依赖仿真；robosuite 仅补充评测</td>
<td width="300">6 项任务各 1 段 RGB-D 人类演示；OKAMI 轨迹展开训练 ACT：撒盐用 50 条，Bagging 用 100 条轨迹</td>
<td width="260">人体重建：1× RTX 3090 24 GB，10-s/30-fps 视频约需 10 min；策略训练时间未披露</td>
<td width="330">数据生成 + 行为克隆：视觉语言模型/目标跟踪与人体重建 → 目标感知全身重定向 → 机器人轨迹展开 → ACT 闭环视觉运动策略</td>
<td width="90">仿真+实机</td>
<td width="300">每任务 1 段 RGB-D 视频；关节 400 Hz / 上层 40 Hz；10 s@30 fps 重建约 10 min</td>
<td width="330">无需遥操作，仅凭单视频教授双臂精细操作</td>
<td width="330">仅上半身桌面工作区；依赖 RGB-D；对大物体形变不够稳健</td>
<td width="330">互联网 RGB 视频、更强基础视觉模型和行走式全身操作</td>
</tr>
<tr>
<td width="105" nowrap>CoRL 2024</td>
<td width="280"><a href="https://proceedings.mlr.press/v270/cheng25b.html">Open-TeleVision: Teleoperation with Immersive Active Visual Feedback</a></td>
<td width="210">立体视觉回传 + 主动颈 + 手臂/手映射遥操作</td>
<td width="260">H1 + 双 Inspire 手 + 2 自由度颈；GR-1 + 钳口夹爪 + 3 自由度颈</td>
<td width="220">未使用物理仿真；真实 H1 / GR-1 数据与 ACT</td>
<td width="300">5 个任务/机器人数据集：H1/GR-1 罐子分拣各 10 条演示；罐子插入、叠毛巾、卸载各 20 条</td>
<td width="260">1× NVIDIA RTX 4090；ACT 使用批大小 45、训练 25k 次迭代；墙钟时间未披露</td>
<td width="330">模仿学习：沉浸式双目遥操作 → 采集真实演示 → 在 ACT 中微调 DINOv2 视觉特征 → 真实闭环评测</td>
<td width="90">实机</td>
<td width="300">系统 60 Hz；ACT 25k 次迭代 / 批大小 45；多数任务 20 条示范（分罐 10）</td>
<td width="330">提高长时精密人形操作的数据采集效率和可用性</td>
<td width="330">无触觉反馈和专家数据重标注；实验未使用下肢移动</td>
<td width="330">视觉—触觉闭环、移动全身遥操作和跨本体数据</td>
</tr>
<tr>
<td width="105" nowrap>CoRL 2024 Oral</td>
<td width="280"><a href="https://proceedings.mlr.press/v270/zhang25a.html">WoCoCo: Learning Whole-Body Humanoid Control with Sequential Contacts</a></td>
<td width="210">顺序接触阶段 + 通用奖励的端到端强化学习</td>
<td width="260">Unitree H1（由官方代码/项目佐证，正文未直接写型号）；另有 22 自由度恐龙仿真</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="300">无外部数据集；程序化生成接触阶段/任务目标回合，覆盖 4 项人形任务和 1 项 22 自由度恐龙任务</td>
<td width="260">GPU 型号/数量、并行环境数和墙钟时间均未披露</td>
<td width="330">从零强化学习：把任务分解为顺序接触阶段 → 任务无关好奇心/接触奖励 → 无随机化 PPO → 加入域随机化与正则继续训练 → 仿真到现实</td>
<td width="90">仿真+实机</td>
<td width="300">策略 50 Hz；PD 200 Hz；4-Hz Butterworth 低通；并行环境数未披露</td>
<td width="330">无需运动先验学习跑酷、搬箱、拍击和攀爬等长时多接触任务</td>
<td width="330">接触序列仍人工预设；不能预测失败；阶段切换依赖接触传感/人工观察</td>
<td width="330">失败预测、机载感知和大语言模型/采样式高层接触规划</td>
</tr>
<tr>
<td width="105" nowrap>ICRA 2025</td>
<td width="280"><a href="https://mobile-tv.github.io/">Mobile-TeleVision: Predictive Motion Priors for Humanoid Whole-Body Control</a></td>
<td width="210">上肢 IK/重定向 + 下肢强化学习 + CVAE 预测运动先验</td>
<td width="260">H1 + 双 6 自由度 Inspire 手 + 主动颈/双目；GR-1 仿真/跨本体</td>
<td width="220">具体引擎未披露；H1 / GR-1 仿真均有验证</td>
<td width="300">源自 AMASS 的人体动作数据；训练子集/规模未披露；桌面任务评测使用 20 条轨迹（约 30 分钟）</td>
<td width="260">GPU 与训练墙钟时间未披露</td>
<td width="330">预训练 + 强化学习：人体动作重定向 → 训练 CVAE 预测动作先验 → PPO 下肢策略；上肢采用 IK/重定向控制 → 实机部署</td>
<td width="90">仿真+实机</td>
<td width="300">H1 50 Hz / GR-1 100 Hz；1 s 窗口 50/100 帧；CVAE 潜在表示=64；20 条轨迹≈30 min</td>
<td width="330">兼顾高自由度上肢精确操作与稳健行走</td>
<td width="330">上下肢解耦限制敏捷性；硬件自由度和多输入带来操作者负担</td>
<td width="330">统一全身策略、低负担接口和预测先验与自主视觉策略融合</td>
</tr>
<tr>
<td width="105" nowrap>RSS 2025</td>
<td width="280"><a href="https://www.roboticsproceedings.org/rss21/p065.html">LangWBC: Language-directed Humanoid Whole-Body Control via End-to-end Learning</a></td>
<td width="210">强化学习教师→CVAE 学生，CLIP 文本直达关节动作</td>
<td width="260">Unitree G1，27 维关节动作；不控制手指</td>
<td width="220">具体物理引擎未披露</td>
<td width="300">HumanML3D 文本-动作数据集；实际重定向训练子集/规模未披露</td>
<td width="260">GPU 与墙钟时间未披露；学生策略使用 1,024 个环境、约 50 万条状态-动作缓冲，并报告 1 万次迭代结果</td>
<td width="330">强化学习 + 蒸馏：动作捕捉重定向 → PPO 动作跟踪教师 → DAgger/行为克隆的 CLIP 条件 CVAE 学生 → 零样本实机部署</td>
<td width="90">仿真+实机</td>
<td width="300">教师策略 50 Hz；27 维动作；15 条未见命令；1000 步稳定性评测</td>
<td width="330">无需中间轨迹，直接以语言驱动真实人形全身动作及平滑切换</td>
<td width="330">只有几十类动作；无视觉；任务仍以运动为主；VAE 带来仿真到现实差距</td>
<td width="330">语言—动作基础控制器、扩散动作生成和视觉条件移动操作</td>
</tr>
<tr>
<td width="105" nowrap>RSS 2025</td>
<td width="280"><a href="https://www.roboticsproceedings.org/rss21/p066.html">ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills</a></td>
<td width="210">真实轨迹学习残差动力学，再注入仿真微调</td>
<td width="260">Unitree G1，29/23 自由度配置；无手指控制</td>
<td width="220">Isaac Gym 源训练；Isaac Sim / Genesis / 真实世界为目标</td>
<td width="300">43 个视频动作用于仿真评测；真实后训练使用 100 段动作片段 + 10 分钟行走数据（完整 23 自由度残差模型估计需 &gt;400 段）</td>
<td width="260">GPU 与训练墙钟时间未披露</td>
<td width="330">预训练 + 后训练/微调：视频 → TRAM 重建/重定向 → PPO 跟踪策略 → 实机轨迹 → 残差动作模型 → 对齐仿真微调 → 去除残差模型部署</td>
<td width="90">仿真→实机</td>
<td width="300">43 个动作；三条迁移链；增量动作模型部署时移除</td>
<td width="330">缩小踢球、跳跃、舞蹈等高动态技能的仿真—真实动力学差距</td>
<td width="330">实机采数会过热/损坏；依赖动作捕捉；完整 23 自由度残差模型数据昂贵</td>
<td width="330">损伤感知策略、无动作捕捉对齐和少样本/在线适应</td>
</tr>
<tr>
<td width="105" nowrap>ICRA 2026</td>
<td width="280"><a href="https://loco-hmc.github.io/">HMC: Learning Heterogeneous Meta-Control for Contact-Rich Loco-Manipulation</a></td>
<td width="210">位置/阻抗/力位混合专家的连续混合专家路由</td>
<td width="260">Unitree G1，双 7 自由度臂 + D435i；无夹爪/机器人手，靠裸末端摩擦</td>
<td width="220">未使用仿真；仅实机模仿学习/控制</td>
<td width="300">真实位置控制示范与多专家示范；轨迹数/时长未披露；3 个接触丰富任务用于定量评测</td>
<td width="260">GPU 与训练墙钟时间未披露</td>
<td width="330">模仿预训练 + 微调：用位置控制数据预训练 Transformer 主干/位置专家 → 解冻全部专家头 → 在小规模多专家示范上行为克隆并学习软混合专家路由</td>
<td width="90">实机</td>
<td width="300">OpenTV 头手跟踪 50 Hz；力矩空间软路由；相对基线提升 &gt;50%</td>
<td width="330">在擦拭、拉抽屉、抬瓶等接触阶段自动切换精度、柔顺和施力</td>
<td width="330">控制专家和任务规模小；未覆盖长时任务级自主规划</td>
<td width="330">更多控制专家、力/触觉闭环与 VLA/任务规划器融合</td>
</tr>
<tr>
<td width="105" nowrap>ICRA 2026</td>
<td width="280"><a href="https://arxiv.org/abs/2412.13196">ExBody2: Advanced Expressive Humanoid Whole-Body Control</a></td>
<td width="210">数据筛选 + 通用/专用预训微调 + 蒸馏</td>
<td width="260">Unitree G1，23 维动作；Orin NX，50 Hz；无手指控制</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="300">CMU 动作捕捉：1,919 个序列；数据筛选消融使用 D50 与 D250 子集</td>
<td width="260">GPU 与训练墙钟时间未披露</td>
<td width="330">强化学习 + 蒸馏 + 微调：动作捕捉重定向 → PPO 教师/基础策略 → 过滤不可行动作 → 通用策略 → DAgger 学生 → 任务专家微调</td>
<td width="90">仿真+实机</td>
<td width="300">策略 50 Hz / 低层 500 Hz；通信延迟 18–30 ms；250 个动作×5 随机种子</td>
<td width="330">稳定复现长时舞蹈、侧步、拳击、蹲起等表达性动态动作</td>
<td width="330">通用策略不及专家精度；多专家难以无缝组合和切换</td>
<td width="330">动态专家路由与统一通用基础控制器</td>
</tr>
<tr>
<td width="105" nowrap>NeurIPS 2024 Spotlight</td>
<td width="280"><a href="https://papers.nips.cc/paper_files/paper/2024/file/90afd20dc776bc8849c31d61a0763a0b-Paper-Conference.pdf">Humanoid Locomotion as Next Token Prediction</a></td>
<td width="210">混合传感运动序列的因果 Transformer 自回归建模</td>
<td width="260">Agility Digit：1.6 m、45 kg、36 自由度（20 驱动）；无灵巧手操作</td>
<td width="220">Agility 自有模拟器采集轨迹；先验强化学习在 Isaac Gym 训练；全部仿真评测使用 MuJoCo</td>
<td width="300">1 万条神经策略轨迹×10 秒；两组各 1 万条模型控制器轨迹×10 秒；约 1,000 条 KIT/AMASS 动作捕捉轨迹；YouTube 视频数量未披露</td>
<td width="260">GPU 与训练墙钟时间未披露</td>
<td width="330">从零训练（离线自回归建模）：采集/重定向混合传感-动作轨迹 → 掩码缺失模态 → 联合训练因果 Transformer 做下一 Token 预测 → 零样本实机行走</td>
<td width="90">仿真+实机</td>
<td width="300">神经策略轨迹 10k×10 s（约 27.8 h），另含基于模型控制器轨迹 20k×10 s；Transformer 上下文=16</td>
<td width="330">统一神经策略、MPC、动作捕捉和视频数据，27 小时数据零样本实机行走</td>
<td width="330">鲁棒性仍落后强 MPC/强化学习；大规模视频动作提取和清洗成本高</td>
<td width="330">规模化人形传感运动基础模型和缺失模态预训练</td>
</tr>
<tr>
<td width="105" nowrap>RSS 2024</td>
<td width="280"><a href="https://www.roboticsproceedings.org/rss20/p058.html">Advancing Humanoid Locomotion: Mastering Challenging Terrains with Denoising World Model Learning</a></td>
<td width="210">去噪世界模型（DWL）+ 端到端强化学习</td>
<td width="260">星动纪元 XBot-S（1.2 m/38 kg/26 驱动）与 XBot-L（1.65 m/57 kg/54 驱动）</td>
<td width="220">Isaac Gym 训练；MuJoCo 状态估计/分析</td>
<td width="300">无命名外部数据集；程序化地形评测覆盖斜坡、楼梯、雪地及不平/可变形地面；训练样本数未披露</td>
<td width="260">GPU 与墙钟时间未披露；12,288 个环境，每次更新 2 个学习训练轮次，单回合 2,400 步</td>
<td width="330">从零训练（强化学习）：非对称 PPO 演员—评论家 + GRU 去噪世界模型/状态重建 + 域随机化 → 零样本实机部署</td>
<td width="90">仿真→实机</td>
<td width="300">策略 100 Hz / PD 控制 500 Hz；12 维动作；XBot-S / XBot-L 零样本实机</td>
<td width="330">同一策略零样本通过雪地、斜坡、楼梯和强不平/可变形地面</td>
<td width="330">只控双腿、手臂固定；仅本体感知，缺少前视地形</td>
<td width="330">视觉地形感知、状态去噪与全身任务控制一体化</td>
</tr>
<tr>
<td width="105" nowrap>RSS 2025</td>
<td width="280"><a href="https://www.roboticsproceedings.org/rss21/p069.html">Gait-Net-augmented Implicit Kino-dynamic MPC for Dynamic Variable-frequency Humanoid Locomotion over Discrete Terrains</a></td>
<td width="210">Gait-Net 步时预测 + 隐式运动动力学 MPC</td>
<td width="260">自研 HECTOR V2：24 自由度，每腿 5/每臂 4 驱动关节，腿长 44 cm</td>
<td width="220">MATLAB / Simulink + Simscape Multibody</td>
<td width="300">无命名公开数据集；评测报告 15 次仿真、合计 600 秒，并进行真实离散地形实验</td>
<td width="260">训练硬件与墙钟时间未披露</td>
<td width="330">监督学习 + 经典优化：生成变频步态样例 → 训练轻量 Gait-Net 预测步时 → 嵌入序列凸化运动动力学 MPC</td>
<td width="90">仿真+实机</td>
<td width="300">15 组仿真共 600 s；MPC 100 Hz / 低层 1 kHz；随机步时 150–400 ms</td>
<td width="330">联合自适应步频、落脚点和接触力以跨离散障碍/沟隙</td>
<td width="330">只对下一步施加地形约束；实机先验知道地形图</td>
<td width="330">多步可行域、机载在线感知和全尺寸长时域 MPC</td>
</tr>
<tr>
<td width="105" nowrap>CoRL 2024</td>
<td width="280"><a href="https://openreview.net/forum?id=fs7ia3FqUM">Humanoid Parkour Learning</a></td>
<td width="210">端到端视觉全身控制 + 分阶段强化学习</td>
<td width="260">Unitree H1</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="300">不使用动作先验数据集；10 类程序化地形/障碍；4 个最难任务进行真实成功率评测</td>
<td width="260">DAgger 视觉蒸馏使用 4× RTX 3090；墙钟时间未披露</td>
<td width="330">从零强化学习 + 蒸馏：分形地形步态预训练 → 特权观测跑酷强化学习/课程教师 → 四卡 DAgger 蒸馏深度视觉学生 → 零样本实机部署</td>
<td width="90">仿真→实机</td>
<td width="300">4096 机器人；10 类障碍；视觉 10 Hz / 策略 50 Hz / PD 控制 1 kHz</td>
<td width="330">单一视觉策略自主选择跳台、越沟、跨栏、楼梯等跑酷技能</td>
<td width="330">训练地形人工构建；未见地形需再训练；复杂上肢动作会干扰视觉</td>
<td width="330">程序化开放地形、实景快速适配和跑酷—操作联合训练</td>
</tr>
<tr>
<td width="105" nowrap>ICRA 2025</td>
<td width="280"><a href="https://ieeexplore.ieee.org/document/11128333">Learning Humanoid Locomotion with Perceptive Internal Model</a></td>
<td width="210">机器人中心高程图 + 感知内部模型（PIM）</td>
<td width="260">Unitree H1（每腿 5 自由度）与 Fourier GR-1（每腿 6 自由度）</td>
<td width="220">具体引擎未披露；训练使用真实地形高度</td>
<td width="300">无命名外部数据集；使用合成地形真值高度观测；在 H1 与 GR-1 的室内外地形及多传感器配置上评测</td>
<td width="260">1× RTX 4090，约 3 小时（换算：约 3 GPU·小时）</td>
<td width="330">从零训练（单阶段强化学习）：地形真值高度观测 → HIM/PPO 感知策略与域随机化 → 推理时使用激光雷达高程图 → 零样本部署</td>
<td width="90">仿真→实机</td>
<td width="300">单 RTX 4090 训练约 3 h；H1 与 GR-1、多传感配置实机</td>
<td width="330">以内部模型提升多本体、多传感配置下复杂静态地形行走</td>
<td width="330">依赖局部高程图和里程计；未覆盖动态障碍与长程导航</td>
<td width="330">原始多模态感知、动态障碍理解与全局导航融合</td>
</tr>
<tr>
<td width="105" nowrap>ICRA 2025</td>
<td width="280"><a href="https://ieeexplore.ieee.org/document/11127524">Berkeley Humanoid: A Research Platform for Learning-Based Control</a></td>
<td width="210">低成本本体—仿真共设计 + 极简强化学习</td>
<td width="260">自研 Berkeley Humanoid（论文阶段无臂）</td>
<td width="220">NVIDIA Isaac Lab</td>
<td width="300">无命名外部数据集；程序化随机行走地形及真实行走/跳跃硬件测试</td>
<td width="260">NVIDIA RTX A4500 仿真基准超过 9 万步/秒；实际训练 GPU 配额与墙钟时间未披露</td>
<td width="330">从零训练（强化学习）：极简 PPO 行走策略 + 轻量动力学/接触随机化 → 零样本实机迁移</td>
<td width="90">仿真→实机</td>
<td width="300">策略 50 Hz / 状态估计器 1 kHz / PD 控制 25 kHz；实机 364 m/10 min、96 m/5 min</td>
<td width="330">以易仿真硬件缩小仿真到现实，完成长距离、山径、推扰和单腿跳</td>
<td width="330">策略无历史，不能在线系统辨识；尚未验证双臂移动操作</td>
<td width="330">装配机械臂、在线适应和可规模真实世界学习</td>
</tr>
<tr>
<td width="105" nowrap>IROS 2023</td>
<td width="280"><a href="https://ieeexplore.ieee.org/document/10342091/">Exploring Kinodynamic Fabrics for Reactive Whole-Body Control of Underactuated Humanoid Robots</a></td>
<td width="210">带优先级 运动动力学织构 的 kHz 级全身控制</td>
<td width="260">Agility Robotics Digit</td>
<td width="220">MuJoCo</td>
<td width="300">无训练数据集；仿真/真实任务覆盖避障、搬箱/抛箱和行走</td>
<td width="260">不适用（无学习模型训练）；控制器运行时延 0.81–1.06 ms/次迭代</td>
<td width="330">无需训练 / 经典优化：定义任务 Fabric → 按优先级组合 → 在线求解期望关节加速度 → 执行全身控制</td>
<td width="90">仿真+实机</td>
<td width="300">每迭代 0.81–1.06 ms 对比 QP 12.60–13.05 ms；碰撞阈值 14 N 对比 7 N</td>
<td width="330">实时组合避障、搬箱、投掷和行走等多项全身任务</td>
<td width="330">对欠驱动混杂系统的收敛/稳定理论未完成，本身不保证平衡稳定</td>
<td width="330">与地形自适应 MPC 融合，兼顾反应性、操作和稳定性</td>
</tr>
<tr>
<td width="105" nowrap>IROS 2024</td>
<td width="280"><a href="https://ieeexplore.ieee.org/document/10802406/">Demonstrating a Robust Walking Algorithm for Underactuated Bipedal Robots in Non-flat, Non-stationary Environments</a></td>
<td width="210">变高度 ALIP-MPC + 虚拟约束 + 踝力矩</td>
<td width="260">Cassie，20 自由度</td>
<td width="220">SimMechanics；FROST 轨迹；CasADi 优化</td>
<td width="300">无学习数据集；3 条离线标称轨迹覆盖平地、上坡和下坡；硬件评测含受限落脚点和移动步道</td>
<td width="260">不适用（无学习模型训练）；MPC &lt;500 μs，横向落脚控制 &lt;5 μs</td>
<td width="330">无需训练 / 经典优化：离线生成 FROST 全阶轨迹 → 变高度 ALIP-MPC + 虚拟约束/踝关节力矩 → 实时硬件控制</td>
<td width="90">仿真+实机</td>
<td width="300">控制器 2 kHz；MPC &lt;500 μs；横向落脚控制 &lt;5 μs</td>
<td width="330">在连续变化坡面和运动地面上维持实时稳定行走</td>
<td width="330">仅 3 条离散名义轨迹覆盖坡度；MPC 卸载到第二台计算机</td>
<td width="330">连续地形参数化、感知驱动轨迹和全机载 MPC</td>
</tr>
<tr>
<td width="105" nowrap>CoRL 2024</td>
<td width="280"><a href="https://proceedings.mlr.press/v270/he25b.html">OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning</a></td>
<td width="210">统一运动学姿态接口 + 稀疏状态全身策略</td>
<td width="260">Unitree H1 + Damiao 腕 + 双 Inspire 手</td>
<td width="220">论文仅写物理仿真；作者官方实现为 Isaac Gym</td>
<td width="300">重定向/增广 AMASS：约 1.4 万个序列；OmniH2O-6：6 个任务、40 分钟、30 Hz 遥操作 RGB-D/控制数据</td>
<td width="260">训练 GPU 与墙钟时间未披露</td>
<td width="330">强化学习 + 蒸馏 + 模仿学习：AMASS 上训练特权动作模仿器 → DAgger 稀疏状态学生 → 真实遥操作/采数 → 用扩散策略从示范学习自主任务</td>
<td width="90">仿真→实机</td>
<td width="300">PD 控制 200 Hz / 策略 50 Hz；ZED 60 fps；端到端延迟 20 ms；6 任务约 40 min 实机示教</td>
<td width="330">用消费级头手跟踪实现灵巧全身遥操作，并收集自主任务数据</td>
<td width="330">自主学习只覆盖少量任务；依赖人体重定向和低驱动自由度手</td>
<td width="330">视觉—触觉自主学习、长时任务和更高自由度手</td>
</tr>
<tr>
<td width="105" nowrap>IROS 2024</td>
<td width="280"><a href="https://arxiv.org/abs/2403.04436">Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation</a></td>
<td width="210">单目人体姿态 + 实时重定向/模仿控制（H2O）</td>
<td width="260">Unitree H1，19 个机体自由度；无灵巧手任务</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="300">AMASS：40 小时 / 约 1.3 万个源动作 → 约 1 万个重定向动作 → 仿真到数据筛选后约 8,500 个本体可行动作</td>
<td width="260">GPU 与训练墙钟时间未披露</td>
<td width="330">强化学习：拟合/重定向 AMASS → PPO 特权模仿器筛除不可行动作 → 域随机化训练鲁棒目标条件 PPO 策略 → 零样本真实遥操作</td>
<td width="90">仿真→实机</td>
<td width="300">约 40 h AMASS；约 8.5k 清洗动作；策略 50 Hz / PD 控制 200 Hz；延迟随机化 20–60 ms</td>
<td width="330">用普通相机实时驱动全尺寸人形复现全身动作</td>
<td width="330">单目遮挡和姿态误差；只模仿动作，缺少物体/触觉闭环</td>
<td width="330">稳健多视角感知并扩展到交互式操作</td>
</tr>
<tr>
<td width="105" nowrap>ICRA 2025</td>
<td width="280"><a href="https://research.nvidia.com/labs/lpr/publication/he2025hover/">HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots</a></td>
<td width="210">多控制模式蒸馏到统一全身策略</td>
<td width="260">Unitree H1，19 自由度；不含手部接触控制</td>
<td width="220">NVIDIA Isaac Gym（原论文）</td>
<td width="300">重定向后的 AMASS 可行子集 Q̂；序列数未披露；真实跟踪评测使用 20 个站立动作</td>
<td width="260">GPU 与训练墙钟时间未披露</td>
<td width="330">强化学习 + 蒸馏：AMASS 重定向/过滤 → PPO 全动作特权教师 → 带模式/稀疏掩码的 DAgger 学生 → 零样本多模式实机控制</td>
<td width="90">仿真+实机</td>
<td width="300">15+ 控制模式；25 步历史；5 随机种子；20 个站立动作×5 次实机</td>
<td width="330">用统一低层接口无缝切换速度、位置、上身姿态等控制模式</td>
<td width="330">停留在状态/运动学命令层；无视觉、任务规划或手部接触</td>
<td width="330">标准化基础控制接口，上接视觉、触觉和任务策略</td>
</tr>
<tr>
<td width="105" nowrap>RSS 2025</td>
<td width="280"><a href="https://www.roboticsproceedings.org/rss21/p064.html">Learning Humanoid Standing-up Control across Diverse Postures</a></td>
<td width="210">多评论家 + 多地形课程的起身控制（HoST）</td>
<td width="260">Unitree G1</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="300">无外部数据集；4 类仿真地形（地面、平台、墙、斜坡）；每个地形/策略评测 1,250 回合</td>
<td width="260">GPU 与墙钟时间未披露；4,096 个环境、500 步回合，每次迭代每环境 50 步</td>
<td width="330">从零训练（强化学习）：多 评论家 PPO + 垂直拉力探索课程 + 动作边界课程/平滑正则 + 域随机化 → 直接实机迁移</td>
<td width="90">仿真→实机</td>
<td width="300">4096 环境；策略 50 Hz；PD 200 Hz 仿真 / 500 Hz 实机；实机报告 100% 成功</td>
<td width="330">从多种姿态在实验室和户外平滑、稳定起身</td>
<td width="330">专注起身，尚未形成任意跌倒检测—恢复—继续任务闭环</td>
<td width="330">与跌倒检测、接触识别和任务恢复统一</td>
</tr>
<tr>
<td width="105" nowrap>CoRL 2025 Oral</td>
<td width="280"><a href="https://openreview.net/forum?id=FCpYuGtN4j">HuB: Learning Extreme Humanoid Balance</a></td>
<td width="210">参考动作精化 + 平衡策略 + 仿真到现实鲁棒化</td>
<td width="260">Unitree G1</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="300">6 个视频动作（深蹲、哪吒姿势、燕式平衡、李小龙踢腿、单腿站立、高抬膝）；片段数/时长未披露</td>
<td width="260">GPU 与训练墙钟时间未披露</td>
<td width="330">强化学习 + 蒸馏：视频 → WHAM/SMPL 重定向与参考动作精修 → 平衡感知 PPO 教师 → DAgger 学生 → 鲁棒性训练 → 零样本实机部署</td>
<td width="90">仿真→实机</td>
<td width="300">29 自由度；25 步历史；每策略 100 个回合；实机 50 Hz、连续 10 次无重置</td>
<td width="330">复现极限准静态平衡动作并处理形态/动力学偏差</td>
<td width="330">主要是准静态平衡；仍受参考动作、传感和形态差异限制</td>
<td width="330">动态、多接触和操作中的平衡控制</td>
</tr>
<tr>
<td width="105" nowrap>CoRL 2025</td>
<td width="280"><a href="https://openreview.net/forum?id=H0EgeP3feg">Hand-Eye Autonomous Delivery: Learning Humanoid Navigation, Locomotion and Reaching</a></td>
<td width="210">眼/手目标的模块化导航—行走—到达（HEAD）</td>
<td width="260">Unitree G1；无抓取/手指控制</td>
<td width="220">Isaac Gym 训练；MuJoCo 仿真到仿真</td>
<td width="300">低层：AMASS+OMOMO，1,363 个片段 / 约 5 小时；导航：ADT 400 分钟、每房间 200 个人体片段（约 4 秒/条）、24 条实验室机器人训练片段（约 30 秒/条）</td>
<td width="260">训练 GPU/耗时未披露；全身控制配置训练 5 万训练轮次；RTX 4090 仅为部署算力</td>
<td width="330">混合模块化训练：单阶段对抗模仿强化学习低层控制器 + 人/机器人/ADT 数据训练 DINO/Transformer 导航 + 模型式伸手模块 → 集成实机部署</td>
<td width="90">仿真+实机</td>
<td width="300">策略 30 Hz / PD 控制 120 Hz；ADT≈400 min；24 个实机任务，成功率 71%</td>
<td width="330">从人体动作捕捉与自回归眼镜数据学习自主导航和到达</td>
<td width="330">只到达不抓取；精确站位困难；感知、规划、控制仍解耦</td>
<td width="330">闭环抓取、统一感知动作和长时配送</td>
</tr>
<tr>
<td width="105" nowrap>CoRL 2025</td>
<td width="280"><a href="https://proceedings.mlr.press/v305/li25h.html">CLONE: Closed-Loop Whole-Body Humanoid Teleoperation for Long-Horizon Tasks</a></td>
<td width="210">混合专家全身策略 + 激光雷达里程计闭环纠偏</td>
<td width="260">Unitree G1；头手 VR 接口，无手指模型</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="300">CLONED：345 个动作，由 149 个精选 AMASS 序列、14 个自采动作捕捉序列、动作编辑和程序化 6D 腕部目标增广构成</td>
<td width="260">教师：1× A800、约 24 小时（换算：约 24 GPU·小时）；学生：1× RTX 3090 Ti、约 48 小时（换算：约 48 GPU·小时）</td>
<td width="330">强化学习 + 蒸馏：PPO 特权教师（8,192 环境 / 100 万次迭代）→ DAgger 混合专家学生（4,096 环境 / 60 万次迭代）→ 激光雷达里程计闭环部署</td>
<td width="90">仿真+实机</td>
<td width="300">教师策略：8192 个环境 / 1M 次迭代；学生策略：4096 个环境 / 600k 次迭代；策略 50 Hz / 激光雷达 10 Hz / PD 控制 1 kHz</td>
<td width="330">减少长距离遥操作漂移并采集长时移动操作数据</td>
<td width="330">依赖 VR 头手接口；无手指、触觉和自主任务学习</td>
<td width="330">灵巧手/触觉、低负担接口和从遥操作到自主策略</td>
</tr>
<tr>
<td width="105" nowrap>CoRL 2025</td>
<td width="280"><a href="https://proceedings.mlr.press/v305/lin25c.html">Sim-to-Real Reinforcement Learning for Vision-Based Dexterous Manipulation on Humanoids</a></td>
<td width="210">特权强化学习 + 视觉策略蒸馏的灵巧操作</td>
<td width="260">Fourier GR-1 + 双 Fourier Hand（每手 6 主动 + 5 欠驱动自由度）；补充实验含 Inspire 手（6 主动 + 6 欠驱动）</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="300">3 任务基准（抓取并到达、抬箱、双手交接）；10 对象消融；每任务 &lt;30 秒任务感知初始化数据，真实到仿真标定 &lt;4 分钟</td>
<td width="260">GPU 与训练墙钟时间未披露</td>
<td width="330">强化学习 + 蒸馏：自动现实到仿真调参 → 接触/物体奖励训练任务专家 PPO → 筛选成功轨迹 → 用扩散策略蒸馏任务通才 → 视觉仿真到现实</td>
<td width="90">仿真→实机</td>
<td width="300">双 Fourier Hand：每手 6 主动 + 5 欠驱动自由度；感知/策略 5 Hz；3 个任务；标定 &lt;4 min</td>
<td width="330">在真实人形上完成对未见物体有泛化的视觉多指操作</td>
<td width="330">只覆盖 3 类任务；任务特定标定/奖励；头部/第三视角和手动力学有差距</td>
<td width="330">可规模视觉—触觉策略、通用对象表示和多任务后训练</td>
</tr>
<tr>
<td width="105" nowrap>CoRL 2025</td>
<td width="280"><a href="https://proceedings.mlr.press/v305/zhuang25b.html">Embrace Contacts: humanoid shadowing with full body ground contacts</a></td>
<td width="210">离散动作命令 + 随机全身接触策略</td>
<td width="260">Unitree G1</td>
<td width="220">NVIDIA Isaac Lab</td>
<td width="300">极端动作集：5 条参考、3 类动作——CMU 起身、KIT 爬行、3 条互联网舞蹈/武术视频动作</td>
<td width="260">1× RTX 4090D，约 72 小时，4,096 个机器人（换算：约 72 GPU·小时）</td>
<td width="330">从零训练（强化学习）：重定向 AMASS/互联网动作 → Transformer 指令编码器 + 多 评论家 PPO/优势混合 → 域随机化 → 零样本全身接触部署</td>
<td width="90">仿真→实机</td>
<td width="300">4096 机器人；RTX 4090D 训练约 72 h；G1 策略 50 Hz / PD 控制 1 kHz；高层命令为 rosbag 开环回放</td>
<td width="330">让脚手之外的躯干/肢体也能接地完成翻滚、坐起等影随</td>
<td width="330">刚体碰撞仿真、数据和奖励设计困难；命令离散且无任务感知</td>
<td width="330">学习接触模型、全身触觉和在线任务条件控制</td>
</tr>
<tr>
<td width="105" nowrap>RSS 2025</td>
<td width="280"><a href="https://www.roboticsproceedings.org/rss21/p062.html">Demonstrating Berkeley Humanoid Lite: An Open-source, Accessible, and Customizable 3D-printed Humanoid Robot</a></td>
<td width="210">低成本开源三维打印本体 + 仿真到现实控制</td>
<td width="260">自研 Berkeley Humanoid Lite：0.8 m、16 kg、22 机体自由度 + 简单夹爪</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="300">无命名学习基准；含行走策略与执行器/手臂评测，其中 60 小时为执行器耐久测试而非训练时间</td>
<td width="260">GPU 与训练墙钟时间未披露</td>
<td width="330">从零训练（强化学习）：PPO 行走 + 域随机化 → 零样本硬件迁移；独立 SteamVR/Pink IK 遥操作无需学习</td>
<td width="90">仿真+实机</td>
<td width="300">0.8 m / 16 kg / 22 自由度；硬件 &lt;$5k；策略 25 Hz；零样本实机；耐久 60 h</td>
<td width="330">把可复现、可维护的人形研究平台成本降至约 5,000 美元以内</td>
<td width="330">负载、精度和任务仍基础；无五指灵巧手</td>
<td width="330">社区复现、多机真实数据和模块化高性能末端</td>
</tr>
<tr>
<td width="105" nowrap>CoRL 2025</td>
<td width="280"><a href="https://proceedings.mlr.press/v305/shi25a.html">ToddlerBot: Open-Source ML-Compatible Humanoid Platform for Loco-Manipulation</a></td>
<td width="210">面向学习的开源本体、数字孪生与遥操作</td>
<td width="260">自研 ToddlerBot：0.56 m、3.4 kg、30 自由度 + 并联夹爪/柔顺掌</td>
<td width="220">MuJoCo / MJX；强化学习同时使用 Brax</td>
<td width="300">2 个操作任务各使用 60 条示范（采集约 20 分钟）；行走训练使用 3×10^8 个仿真时间步</td>
<td width="260">GPU 与墙钟时间未披露；PPO 使用 1,024 环境 / 3×10^8 时间步；扩散策略训练采用 100 个扩散步</td>
<td width="330">系统辨识 → PPO 行走策略零样本迁移；主从遥操作示范 → RGB 扩散策略 → 串联操作与行走技能</td>
<td width="90">仿真+实机</td>
<td width="300">3×10^8 步 / 1024 环境；30 自由度反馈 50 Hz；视觉策略 10 Hz、延迟 &lt;0.1 s</td>
<td width="330">统一低成本本体、零样本仿真到现实、数据采集和双机长时玩具整理</td>
<td width="330">玩具尺度、负载、速度和地形能力有限</td>
<td width="330">扩展开放数据、平台复现和更大尺度协作移动操作</td>
</tr>
<tr>
<td width="105" nowrap>RSS 2024</td>
<td width="280"><a href="https://www.roboticsproceedings.org/rss20/p103.html">Design and Control of a Bipedal Robotic Character</a></td>
<td width="210">动画引擎命令 + 强化学习表演控制</td>
<td width="260">Disney 自研双足角色：0.66 m、15.4 kg，双腿各 5 自由度 + 头部 4 自由度；无臂/手</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="300">艺术家制作参考：1 个站立策略、1 个行走策略及若干单动作情节策略；具体片段数/时长未披露</td>
<td width="260">每个策略：1× RTX 4090、约 2 天 / 10 万次迭代 / 每次迭代 8,192×24 样本（换算：约 48 GPU·小时）</td>
<td width="330">从零训练（强化学习）：艺术家动画/参考动作 → 分别训练 PPO 站立、行走和情节策略 → 冻结权重 → 动画引擎混合策略与艺术家指令</td>
<td width="90">仿真+实机</td>
<td width="300">策略 50 Hz / 执行器通信 600 Hz；100k 次迭代；8192×24 样本/迭代；约 10 h 实机无跌倒</td>
<td width="330">统一艺术家指定的表达动作与稳健动态移动</td>
<td width="330">依赖动画/操作者，面向娱乐表演；无自主感知和任务执行</td>
<td width="330">把表达性 HRI 与自主任务级移动结合</td>
</tr>
<tr>
<td width="105" nowrap>CoRL 2024</td>
<td width="280"><a href="https://proceedings.mlr.press/v270/zhao25a.html">Bi-Level Motion Imitation for Humanoid Robots</a></td>
<td width="210">策略与参考动作捕捉交替优化的双层模仿</td>
<td width="260">Isaac Gym 中高保真 MIT Humanoid 模型</td>
<td width="220">NVIDIA Isaac Gym</td>
<td width="300">DeepMimic/FLD 动作捕捉：13 个动作 × 每动作 10 条轨迹 × 每轨迹 240 步</td>
<td width="260">GPU 与墙钟时间未披露；SCAE 5,000 次迭代，PPO 策略最多 3,000 次迭代 / 4,096 环境，BMI 微调 50 次迭代</td>
<td width="330">预训练 + 双层微调：训练 SCAE 潜在动力学 → PPO 动作策略 → 交替优化解码器/参考动作与策略 → 仿真评测</td>
<td width="90">仅仿真</td>
<td width="300">18 维动作；13 个动作；策略 50 Hz；4096 环境；最大 3000 次迭代；仅仿真</td>
<td width="330">自动修改物理不可行动作，使模仿策略更可执行</td>
<td width="330">仅仿真；双层优化计算较重；动作覆盖有限</td>
<td width="330">在线可行重定向、更大动作库和真实本体验证</td>
</tr>
</tbody>
</table>

## 人形机器人研究方向凝练

<table width="1850">
<thead>
<tr>
<th width="190">研究方向</th>
<th width="300">代表论文</th>
<th width="280">典型本体 / 末端</th>
<th width="360">已取得进展</th>
<th width="360">共性瓶颈</th>
<th width="360">下一阶段趋势</th>
</tr>
</thead>
<tbody>
<tr>
<td width="190">复杂地形与敏捷运动</td>
<td width="300">DWL、Humanoid Parkour、PIM、BeamDojo、Cassie Jumping</td>
<td width="280">H1/G1、Cassie、Digit、XBot、HECTOR V2</td>
<td width="360">从盲走扩展到视觉落脚、跑酷、跳跃和稀疏支撑面</td>
<td width="360">地图漂移、未知地形泛化、能耗与硬件热/冲击约束</td>
<td width="360">原始多模态感知 + 在线适应 + 规划/控制联合学习</td>
</tr>
<tr>
<td width="190">全身模仿与表达运动</td>
<td width="300">HumanPlus、ExBody、TWIST、ALMI、KungfuBot、ExBody2</td>
<td width="280">H1/H1-2、G1、Booster T1</td>
<td width="360">人体动作可迁移为稳定行走、舞蹈和高动态技能</td>
<td width="360">形态/自由度不匹配、重定向误差、每技能策略和硬件损伤</td>
<td width="360">统一动作基础控制器、免重定向表示和损伤感知后训练</td>
</tr>
<tr>
<td width="190">平衡、起身与安全恢复</td>
<td width="300">HoST、Getting-Up、HuB、Keep On Going、HWC-Loco</td>
<td width="280">主要为 G1/H1</td>
<td width="360">已能在多地面起身、极限平衡并抵抗外扰</td>
<td width="360">初始跌倒姿态有限、失败不可预测、恢复后不能自动续接任务</td>
<td width="360">跌倒检测—接触识别—恢复—续作闭环与安全评论家</td>
</tr>
<tr>
<td width="190">遥操作与数据飞轮</td>
<td width="300">Open-TeleVision、Mobile-TeleVision、TWIST、CLONE、HOMIE、Humanoid Everyday</td>
<td width="280">H1/G1、GR-1、Dex3-1/Inspire</td>
<td width="360">从上身桌面遥操作扩展到全身长时移动操作与大规模数据集</td>
<td width="360">操作者负担、动作捕捉/VR 依赖、无力触觉、漂移与复位成本</td>
<td width="360">低负担多模态遥操作、视觉—触觉反馈和自动数据闭环</td>
</tr>
<tr>
<td width="190">移动操作与灵巧手</td>
<td width="300">WholeBodyVLA、OKAMI、AMO、VIRAL、Vision-Based Dexterous RL</td>
<td width="280">AgiBot X2、G1+Dex3-1、GR-1+Inspire</td>
<td width="360">行走、站位、双臂和多指操作开始在同一系统中协同</td>
<td width="360">手部仿真差距、精确站位、接触力和长时失败恢复</td>
<td width="360">触觉 VLA、接触感知世界模型、精确全身规划和自动恢复</td>
</tr>
<tr>
<td width="190">语言/视觉语言模型与通用策略</td>
<td width="300">HumanVLA、BiBo、LangWBC、RoboGhost、BFM-Zero、HEAD</td>
<td width="280">虚拟人体、G1</td>
<td width="360">语言可直接提示动作、目标、物体重排和部分导航/到达行为</td>
<td width="360">动作词表小、手部/接触模型弱、尚未覆盖真正长时抓取</td>
<td width="360">语言—视觉—触觉—动作统一模型与分层长时规划</td>
</tr>
<tr>
<td width="190">跨本体与开放平台</td>
<td width="300">XHugWBC、HumanoidBench、Berkeley Humanoid/Lite、ToddlerBot</td>
<td width="280">12+ 仿真本体和多类自研/商业平台</td>
<td width="360">开始形成跨形态控制、标准基准和低成本可复现硬件</td>
<td width="360">形态语义不一致、硬件差异大、仿真评测与实机能力脱节</td>
<td width="360">形态感知动作空间、统一协议、跨平台真实数据与评测</td>
</tr>
<tr>
<td width="190">人体动作/交互基础研究</td>
<td width="300">TokenHSI、InterMimic、CLoSD、UniHSI、OmniControl、PhysDiff</td>
<td width="280">SMPL/SMPL-X/PHC 等虚拟人体</td>
<td width="360">提供动作、接触、姿态和任务组合的上游表示</td>
<td width="360">多数不是机器人，缺少真实机器人执行器/手部模型、经标定接触动力学和仿真到现实验证</td>
<td width="360">把生成式人体先验接到真实人形动力学、接触与安全闭环</td>
</tr>
</tbody>
</table>
