# 级联世界动作模型

[首页](../../../README.zh-CN.md) | [英文](../../en/wam/cascaded.md) | [方向目录](README.md)

共 24 篇。

<table width="3110">
<thead>
<tr>
<th width="120" nowrap>会议/年份</th>
<th width="320">论文/方法</th>
<th width="420">摘要</th>
<th width="220">WAM 类型</th>
<th width="280">状态表示</th>
<th width="260">动作接口</th>
<th width="360">用途</th>
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
<td width="120" nowrap>ICRA 2025</td>
<td width="320"><a href="https://nvlabs.github.io/X-MOBILITY/">X-MOBILITY: End-To-End Generalizable Navigation via World Modeling</a></td>
<td width="420">X-MOBILITY 用自回归潜在世界模型解耦世界动态学习和动作策略，支持零样本仿真到现实迁移导航。</td>
<td width="220">导航世界模型</td>
<td width="280">潜在未来状态</td>
<td width="260">导航动作</td>
<td width="360">导航策略想象</td>
<td width="200">仿真 + 实机</td>
<td width="360">通过世界模型提升端到端导航泛化和仿真到现实。</td>
<td width="110" nowrap><a href="https://nvlabs.github.io/X-MOBILITY/">论文</a></td>
<td width="110" nowrap><a href="https://nvlabs.github.io/X-MOBILITY/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/NVlabs/X-MOBILITY">代码</a></td>
<td width="240"><a href="https://github.com/NVlabs/X-MOBILITY">data</a></td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=748bHL2BAv">Ctrl-World: A Controllable Generative World Model for Robot Manipulation</a></td>
<td width="420">构建可控多视角机器人世界模型，用想象轨迹展开评估并改进泛化机器人策略。</td>
<td width="220">级联世界动作模型</td>
<td width="280">多视角视频世界模型</td>
<td width="260">帧级动作条件化</td>
<td width="360">策略评测 + 合成改进</td>
<td width="200">真实机器人数据/DROID</td>
<td width="360">解决通用机器人策略在新物体和新指令下真实轨迹展开昂贵、难扩展的问题。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=748bHL2BAv">论文</a></td>
<td width="110" nowrap><a href="https://ctrl-world.github.io/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/Robert-gyj/Ctrl-World">代码</a></td>
<td width="240"><a href="https://huggingface.co/yjguo/Ctrl-World">Hugging Face</a></td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=0GNBqoYcAP">Context and Diversity Matter: The Emergence of In-Context Learning in World Models</a></td>
<td width="420">研究世界模型如何通过上下文样例识别或学习新环境动力学。</td>
<td width="220">级联世界动作模型</td>
<td width="280">环境动力学/世界模型潜在表示</td>
<td width="260">-</td>
<td width="360">上下文学习动力学预测</td>
<td width="200">仿真/分析</td>
<td width="360">解决静态世界模型遇到新环境或稀有配置时适应性差的问题。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=0GNBqoYcAP">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=4HZgkwVVFO">NeMo-map: Neural Implicit Flow Fields for Spatio-Temporal Motion Mapping</a></td>
<td width="420">用神经隐式函数连续建模场地特定的时空运动流场。</td>
<td width="220">时空运动世界模型</td>
<td width="280">隐式神经流场</td>
<td width="260">-</td>
<td width="360">运动映射/导航安全</td>
<td width="200">公开运动数据集</td>
<td width="360">解决人类环境中动态运动地图离散采样、离线构建成本高的问题。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=4HZgkwVVFO">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=8UZpmrxoLG">Astra: General Interactive World Model with Autoregressive Denoising</a></td>
<td width="420">用自回归去噪视频模型生成可动作控制的长时未来世界。</td>
<td width="220">级联世界动作模型</td>
<td width="280">视频世界模型</td>
<td width="260">动作感知适配器</td>
<td width="360">交互式未来预测</td>
<td width="200">机器人 + 驾驶场景</td>
<td width="360">解决通用场景中基于历史观测和动作预测长时未来的问题。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=8UZpmrxoLG">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=LQD1MrnbxH">Test-Time Mixture of World Models for Embodied Agents in Dynamic Environments</a></td>
<td width="420">在测试时动态路由和组合多个世界模型以适应变化环境。</td>
<td width="220">级联世界动作模型</td>
<td width="280">世界模型混合</td>
<td width="260">智能体动作/接口</td>
<td width="360">具身推理的测试时适应</td>
<td width="200">动态具身环境基准</td>
<td width="360">解决具身智能体在未见动态环境中世界模型组合和持续适应不足的问题。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=LQD1MrnbxH">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=MPabX9LEds">Learning Massively Multitask World Models for Continuous Control</a></td>
<td width="420">Newt 在 200 个连续控制任务上预训练并在线优化语言条件世界模型。</td>
<td width="220">级联世界动作模型</td>
<td width="280">以语言为条件的多任务潜在世界模型</td>
<td width="260">连续控制动作</td>
<td width="360">在线强化学习预训练/微调</td>
<td width="200">-</td>
<td width="360">解决连续控制多任务、多本体在线强化学习难扩展的问题。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=MPabX9LEds">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">200 项任务基准</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=a1zfcaNTkM">ExoPredicator: Learning Abstract Models of Dynamic Worlds for Robot Planning</a></td>
<td width="420">学习符号状态和内外生因果过程，用于长时机器人规划。</td>
<td width="220">级联世界动作模型</td>
<td width="280">抽象符号状态 + 因果过程</td>
<td width="260">符号/内生动作</td>
<td width="360">长时程规划</td>
<td width="200">仿真桌面</td>
<td width="360">解决机器人规划中环境自身变化与动作效果并发发生的问题。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=a1zfcaNTkM">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=oBXfPyi47m">Efficient Reinforcement Learning by Guiding World Models with Non-Curated Data</a></td>
<td width="420">利用无奖励、跨本体、混合质量离线数据引导世界模型以提升在线强化学习样本效率。</td>
<td width="220">级联世界动作模型</td>
<td width="280">从离线/在线数据学习的世界模型</td>
<td width="260">视觉运动强化学习动作</td>
<td width="360">样本高效在线强化学习</td>
<td width="200">72 项视觉运动任务/6 种本体</td>
<td width="360">解决非精筛离线数据直接微调世界模型因分布偏移难以提升强化学习的问题。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=oBXfPyi47m">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=qmEyJadwHA">Object-Centric World Models from Few-Shot Annotations for Sample-Efficient Reinforcement Learning</a></td>
<td width="420">OC-STORM 用少量标注提取对象中心表示，提升像素 MBRL 样本效率。</td>
<td width="220">级联世界动作模型</td>
<td width="280">以物体为中心的潜在表示</td>
<td width="260">强化学习动作</td>
<td width="360">样本高效基于模型的强化学习</td>
<td width="200">-</td>
<td width="360">解决像素级世界模型忽视小但关键对象导致样本效率低的问题。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=qmEyJadwHA">论文</a></td>
<td width="110" nowrap><a href="https://oc-storm.weipuzhang.com">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">Atari 100k, Hollow Knight</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=w3w7WVG4ks">Building spatial world models from sparse transitional episodic memories</a></td>
<td width="420">ESWM 从稀疏离散回合记忆构建空间认知地图并预测未观测转移。</td>
<td width="220">级联世界动作模型</td>
<td width="280">回合式空间潜在地图</td>
<td width="260">导航状态转移</td>
<td width="360">探索/导航规划</td>
<td width="200">仿真空间环境</td>
<td width="360">解决空间世界模型需要长连续轨迹才能建图的问题。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=w3w7WVG4ks">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=yDmb7xAfeb">World-In-World: World Models in a Closed-Loop World</a></td>
<td width="420">提供闭环平台评测世界模型是否真正提升具身任务成功。</td>
<td width="220">世界模型评测/闭环世界动作模型</td>
<td width="280">异构世界模型</td>
<td width="260">标准化动作接口</td>
<td width="360">闭环规划/评测</td>
<td width="200">-</td>
<td width="360">解决世界模型评测偏开环视觉质量、缺少任务成功闭环指标的问题。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=yDmb7xAfeb">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">World-In-World 基准</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=Patx6MRipw">ENACT: Evaluating Embodied Cognition with World Modeling of Egocentric Interaction</a></td>
<td width="420">ENACT 用自我中心交互序列重排任务评估视觉语言模型的前向和逆向世界建模能力。</td>
<td width="220">世界模型评测</td>
<td width="280">第一视角状态动作序列</td>
<td width="260">逆世界建模动作</td>
<td width="360">基准/评测</td>
<td width="200">-</td>
<td width="360">解决视觉语言模型是否具备具身认知和交互世界建模能力的评测问题。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=Patx6MRipw">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">ENACT</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/63978">Cross-Embodiment Robot Foundation World Models with Latent Actions</a></td>
<td width="420">LAC-WM 用统一潜在动作空间训练跨本体机器人世界模型。</td>
<td width="220">级联世界动作模型</td>
<td width="280">以潜在动作为条件的世界模型</td>
<td width="260">统一潜在动作</td>
<td width="360">跨本体适配</td>
<td width="200">灵巧操作基准</td>
<td width="360">解决不同机器人动作空间不一致导致世界模型难泛化到新本体的问题。</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/63978">论文</a></td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/63978">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/62480">DDP-WM: Disentangled Dynamics Prediction for Efficient World Models</a></td>
<td width="420">DDP-WM 将主动态与背景更新解耦，提升世界模型实时推理和规划效率。</td>
<td width="220">级联世界动作模型</td>
<td width="280">解耦潜在动力学</td>
<td width="260">模型预测控制/规划器</td>
<td width="360">高效规划</td>
<td width="200">导航/桌面/可变形物体基准</td>
<td width="360">解决稠密 Transformer 世界模型计算开销高、难实时部署的问题。</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/62480">论文</a></td>
<td width="110" nowrap><a href="https://hcplab-sysu.github.io/DDP-WM">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/62543">RoboFlow4D: A Lightweight Flow World Model Toward Real-Time Flow-Guided Robotic Manipulation</a></td>
<td width="420">RoboFlow4D 直接预测多帧三维流，用流引导实时机器人操作。</td>
<td width="220">级联世界动作模型</td>
<td width="280">多帧三维流</td>
<td width="260">流引导动作策略</td>
<td width="360">实时操作规划</td>
<td width="200">仿真 + 实机</td>
<td width="360">解决三维操作中模块化预测流规划管线开销高、实时性差的问题。</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/62543">论文</a></td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/62543">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/64209">Learning Task-Sufficient World Models by Synergizing Agentic Exploration and Structured Modeling</a></td>
<td width="420">通过主动探索和结构化建模学习任务充分且紧凑的世界模型表示。</td>
<td width="220">级联世界动作模型</td>
<td width="280">任务充分结构化潜在表示</td>
<td width="260">智能体探索/动作</td>
<td width="360">样本高效控制/泛化</td>
<td width="200">连续控制 + 操作基准</td>
<td width="360">解决通用视觉/隐空间世界模型保留太多控制无关因素、影响泛化效率的问题。</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/64209">论文</a></td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/64209">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2509.15536">SAMPO: Scale-wise Autoregression with Motion PrOmpt for Generative World Models</a></td>
<td width="420">SAMPO 结合尺度级视觉自回归、因果下一帧建模和运动提示生成动作条件未来。</td>
<td width="220">级联世界动作模型</td>
<td width="280">视频词元 + 运动提示</td>
<td width="260">以动作为条件的视频预测</td>
<td width="360">基于模型的控制/视频预测</td>
<td width="200">机器人/世界模型基准</td>
<td width="360">解决自回归世界模型空间结构破坏、解码低效、运动建模不足的问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2509.15536">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2505.05495">Learning 3D Persistent Embodied World Models</a></td>
<td width="420">学习带显式三维记忆的具身世界模型，以更一致地模拟长时未来观测。</td>
<td width="220">级联世界动作模型</td>
<td width="280">RGB-D 视频 + 持久三维地图</td>
<td width="260">以未来动作为条件的观测预测</td>
<td width="360">规划/策略学习</td>
<td width="200">具身应用</td>
<td width="360">解决视频世界模型缺少未观测场景记忆、长时规划不一致的问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2505.05495">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2505.20425">OSVI-WM: One-Shot Visual Imitation for Unseen Tasks using World-Model-Guided Trajectory Generation</a></td>
<td width="420">用世界模型生成潜在状态和动作轨迹，实现未见任务的一次视觉模仿。</td>
<td width="220">级联世界动作模型</td>
<td width="280">潜在状态/轨迹</td>
<td width="260">解码后的物理路径点</td>
<td width="360">单样本模仿</td>
<td width="200">2 个仿真基准 + 3 个真实机器人平台</td>
<td width="360">解决单样本视觉模仿对语义或结构不同的新任务泛化差的问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2505.20425">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/raktimgg/OSVI-WM">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2406.14540">IRASim: A Fine-Grained World Model for Robot Manipulation</a></td>
<td width="420">IRASim 用逐帧动作条件扩散 Transformer 生成细粒度机器人-物体交互视频。</td>
<td width="220">级联世界动作模型</td>
<td width="280">以动作为条件的视频</td>
<td width="260">机器人动作轨迹/帧级条件化</td>
<td width="360">精细操作仿真</td>
<td width="200">机器人操作数据集</td>
<td width="360">解决机器人操作中动作与视觉帧精确对齐、细粒度交互预测困难的问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2406.14540">论文</a></td>
<td width="110" nowrap><a href="https://gen-irasim.github.io/">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://ziweiwangthu.github.io/data/GWM.pdf">GWM: Towards Scalable Gaussian World Models for Robotic Manipulation</a></td>
<td width="420">GWM 用三维高斯基元预测机器人动作后的未来三维场景。</td>
<td width="220">级联世界动作模型</td>
<td width="280">三维高斯泼溅潜在表示</td>
<td width="260">以机器人动作为条件的高斯传播</td>
<td width="360">模仿表示 + 基于模型的强化学习仿真器</td>
<td width="200">仿真 + 实机</td>
<td width="360">解决图像世界模型缺少稳定三维几何信息、难支持策略训练的问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2507.07954">论文</a></td>
<td width="110" nowrap><a href="https://gaussian-world-model.github.io/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/Gaussian-World-Model/gaussianwm">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2503.16806">DyWA: Dynamics-adaptive World Action Model for Generalizable Non-prehensile Manipulation</a></td>
<td width="420">DyWA 联合预测未来状态并适应动力学变化，提升非抓取操作泛化。</td>
<td width="220">级联世界动作模型</td>
<td width="280">单视角点云 + 几何/状态/物理</td>
<td width="260">世界动作模型</td>
<td width="360">非抓持操作</td>
<td width="200">仿真 + 实机</td>
<td width="360">解决非抓取操作在不同物体质量、桌面摩擦和单视角部分可观测下泛化困难的问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2503.16806">论文</a></td>
<td width="110" nowrap><a href="https://pku-epic.github.io/DyWA/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/jiangranlv/DyWA">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://openreview.net/pdf?id=mnwlhvmKMN">Learning 4D Embodied World Models</a></td>
<td width="420">TesserAct 从图像和语言预测随动作演化的四维动态网格世界。</td>
<td width="220">级联世界动作模型</td>
<td width="280">四维动态网格</td>
<td width="260">逆动力学/策略执行</td>
<td width="360">四维预测 + 策略学习</td>
<td width="200">数据集 + 具身任务</td>
<td width="360">解决二维视频世界模型缺少精确三维几何和时间动态、难学逆动力学的问题。</td>
<td width="110" nowrap><a href="https://openreview.net/pdf?id=mnwlhvmKMN">论文</a> / <a href="https://arxiv.org/pdf/2504.20995">论文</a></td>
<td width="110" nowrap><a href="https://tesseractworld.github.io/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/UMass-Embodied-AGI/TesserAct">代码</a></td>
<td width="240"><a href="https://huggingface.co/anyeZHY/tesseract">Hugging Face</a></td>
</tr>
</tbody>
</table>
