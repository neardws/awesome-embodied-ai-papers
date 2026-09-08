# 安全评测

[首页](../../../README.zh-CN.md) | [英文](../../en/deployment/safety-evaluation.md) | [方向目录](README.md)

共 13 篇。

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
<td width="120" nowrap>CoRL 2024</td>
<td width="320"><a href="https://scholar.google.com/scholar?q=DriveVLM%3A+The+Convergence+of+Autonomous+Driving+and+Large+Vision-Language+Models">DriveVLM: The Convergence of Autonomous Driving and Large Vision-Language Models</a></td>
<td width="420">DriveVLM 利用大型视觉语言模型研究自动驾驶。</td>
<td width="240">安全评测</td>
<td width="280">部署/评测覆盖</td>
<td width="280">机器人/仿真器平台</td>
<td width="280">具身机器人任务</td>
<td width="220">来源列出的资源</td>
<td width="360">补充 CoRL 部署/评测研究覆盖。</td>
<td width="110" nowrap><a href="https://scholar.google.com/scholar?q=DriveVLM%3A+The+Convergence+of+Autonomous+Driving+and+Large+Vision-Language+Models">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2025</td>
<td width="320"><a href="https://proceedings.iclr.cc/paper_files/paper/2025/file/5ab848771ff8c9c47aac4128e2ef9f4e-Paper-Conference.pdf">HASARD: A Benchmark for Vision-Based Safe Reinforcement Learning in Embodied Agents</a></td>
<td width="420">HASARD 评测具身智能体中基于视觉的安全强化学习。</td>
<td width="240">安全评测</td>
<td width="280">安全强化学习基准覆盖</td>
<td width="280">基准平台</td>
<td width="280">基于视觉的安全强化学习</td>
<td width="220">HASARD</td>
<td width="360">在具身视觉观测条件下评测安全强化学习智能体。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2503.08241">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2022</td>
<td width="320"><a href="https://openreview.net/forum?id=dwi57JI_-K&noteId=pfmgIWaQAoN">SafeBench: A Benchmarking Platform for Safety Evaluation of Autonomous Vehicles</a></td>
<td width="420">SafeBench 提供自动驾驶车辆安全评测基准平台。</td>
<td width="240">安全评测</td>
<td width="280">自动驾驶安全场景</td>
<td width="280">基准平台</td>
<td width="280">驾驶安全评测</td>
<td width="220">SafeBench</td>
<td width="360">评测自动驾驶场景中的安全风险。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2206.09682">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>IROS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2410.15185">Semantically Safe Robot Manipulation: From Semantic Scene Understanding to Motion Safeguards</a></td>
<td width="420">该文用大语言模型推理常识语义风险，并把语义风险映射为机器人操作安全过滤。</td>
<td width="240">语义安全层</td>
<td width="280">安全评测</td>
<td width="280">机器人操作安全</td>
<td width="280">语义场景理解 + 安全防护</td>
<td width="220">项目已提供</td>
<td width="360">将语义风险纳入机器人操作安全闭环。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2410.15185">论文</a></td>
<td width="110" nowrap><a href="https://utiasdsl.github.io/semantic-manipulation/">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=8s5jBVybhQ">Remotely Detectable Robot Policy Watermarking</a></td>
<td width="420">提出 CoNoCo，在远程视频/动捕观测中检测机器人策略水印且不影响动作分布。</td>
<td width="240">策略水印</td>
<td width="280">安全</td>
<td width="280">机器人部署/评测环境</td>
<td width="280">远程安全/来源检测</td>
<td width="220">-</td>
<td width="360">解决机器人策略知识产权和未授权使用的远程验证问题。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=8s5jBVybhQ">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=Gsrw1vxq1G">RoboMD: Uncovering Robot Vulnerabilities through Semantic Potential Fields</a></td>
<td width="420">RoboMD 在语义视觉嵌入势场中主动搜索脆弱区域，用于安全发现和再训练。</td>
<td width="240">漏洞发现</td>
<td width="280">安全</td>
<td width="280">机器人部署/评测环境</td>
<td width="280">操作鲁棒性</td>
<td width="220">-</td>
<td width="360">解决真实机器人漏洞测试昂贵且未知扰动难枚举的问题。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=Gsrw1vxq1G">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/60472">Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds</a></td>
<td width="420">融合多样点云输入和二维观测，提升 VLA 在仿真、传感器和真实域中的鲁棒性。</td>
<td width="240">基准/数据集</td>
<td width="280">基准/数据集</td>
<td width="280">机器人部署/评测环境</td>
<td width="280">评估鲁棒性和安全性</td>
<td width="220">-</td>
<td width="360">评估鲁棒性和安全性</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/60472">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/62679">PACT: Self-Evolving Physical Safety Alignment for Diffusion Policies in Embodied Manipulation</a></td>
<td width="420">用物理约束对齐后训练扩散策略，在无需示教或奖励的情况下减少安全违规。</td>
<td width="240">基准/数据集</td>
<td width="280">安全</td>
<td width="280">机器人部署/评测环境</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/62679">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/61584">SafeLab: An Interactive High-Fidelity Benchmark for Embodied Safety in Scientific Robotics</a></td>
<td width="420">提供高保真实验室仿真安全基准，包含安全任务、校准资产和专家轨迹。</td>
<td width="240">基准/数据集</td>
<td width="280">安全</td>
<td width="280">仿真/评测环境</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/61584">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/64080">Dismantling the Illusion of Vision-Language-Action Models Competence via Explicit Distributional Shifts</a></td>
<td width="420">提出 LIBERO-Gen，通过显式语义和环境分布偏移揭示 VLA 的脆弱性。</td>
<td width="240">基准/数据集</td>
<td width="280">基准/数据集</td>
<td width="280">机器人部署/评测环境</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/64080">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2510.13626">LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models</a></td>
<td width="420">通过七类扰动和 10,030 个任务系统揭示 VLA 鲁棒性缺陷。</td>
<td width="240">基准/数据集</td>
<td width="280">基准/数据集</td>
<td width="280">机器人部署/评测环境</td>
<td width="280">7 个扰动维度 / 10,030 项任务</td>
<td width="220">项目+代码+数据/基准</td>
<td width="360">解决 VLA 在标准基准上高分但对真实扰动脆弱的问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2510.13626">论文</a> / <a href="https://arxiv.org/pdf/2510.13626">论文</a></td>
<td width="110" nowrap><a href="https://sylvestf.github.io/LIBERO-plus/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/sylvestf/LIBERO-plus">代码</a></td>
<td width="240"><a href="https://huggingface.co/datasets/Sylvest/LIBERO-plus">Hugging Face</a></td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2506.05294">A Smooth Sea Never Made a Skilled SAILOR: Robust Imitation via Learning to Search</a></td>
<td width="420">SAILOR 从示教学习搜索、世界模型和奖励模型，使模仿策略能从错误状态恢复。</td>
<td width="240">基准/数据集</td>
<td width="280">安全</td>
<td width="280">机器人部署/评测环境</td>
<td width="280">12 项视觉操作任务</td>
<td width="220">项目</td>
<td width="360">解决行为克隆离开示教分布后不会恢复的问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2506.05294">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/arnavkj1995/SAILOR">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2506.23725">PAC Bench: Do Foundation Models Understand Prerequisites for Executing Manipulation Policies?</a></td>
<td width="420">PAC Bench 评估视觉语言模型是否理解物体属性、可供性和约束等操作前置条件。</td>
<td width="240">基准/数据集</td>
<td width="280">安全</td>
<td width="280">机器人部署/评测环境</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">解决基础模型高层机器人能力依赖的低层物理前提未被验证的问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2506.23725">论文</a></td>
<td width="110" nowrap><a href="https://pacbench.github.io/">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">30k 条标注 / 673 张图像 / 100 个场景 / 120 项仿真约束</td>
</tr>
</tbody>
</table>
