# 通用 VLA

[首页](../../../README.zh-CN.md) | [英文](../../en/vla/generalist.md) | [方向目录](README.md)

共 80 篇。

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
<td width="120" nowrap>LangRob @ CoRL 2023</td>
<td width="320"><a href="https://openreview.net/forum?id=3mKb5iyZ2V">Reasoning Tuning Grasp: Adapting Multi-Modal Large Language Models for Robotic Grasping</a></td>
<td width="420">微调多模态大模型，使其推理并输出二指夹爪的数值平面抓取位姿。</td>
<td width="230">LLaVA-7B-v0 + CLIP ViT-L/14</td>
<td width="240">图像抓取点 [x,y] + 末端旋转角</td>
<td width="300">Cornell：885 张图/240 物体，含 74 类推理标注；LoRA；135 次实机评测</td>
<td width="260">经过推理微调的多模态大语言模型抓取预测</td>
<td width="240">平行夹爪抓取位姿视觉语言模型；不是灵巧手控制器</td>
<td width="200">离线基准 + 实机；无物理仿真器</td>
<td width="360">Cornell 图像/物体准确率 84.05±0.78/77.02±0.93%；实机 LoRA 113/135 = 83.7%</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=3mKb5iyZ2V">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">Cornell Grasp Dataset；27 个未见物体×5 姿态</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2022</td>
<td width="320"><a href="https://arxiv.org/abs/2109.12098">CLIPort: What and Where Pathways for Robotic Manipulation</a></td>
<td width="420">CLIPort 将 CLIP 语义与基于空间搬运的操作策略结合。</td>
<td width="230">CLIPort</td>
<td width="240">机器人动作</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">CoRL 机器人学习方法</td>
<td width="240">机器人策略</td>
<td width="200">机器人基准</td>
<td width="360">补充 CoRL VLA 研究覆盖。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2109.12098">论文</a></td>
<td width="110" nowrap><a href="https://cliport.github.io">项目</a></td>
<td width="110" nowrap><a href="https://github.com/cliport/cliport">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2024</td>
<td width="320"><a href="https://arxiv.org/abs/2406.09246">OpenVLA: An Open-Source Vision-Language-Action Model</a></td>
<td width="420">OpenVLA 是用于通用机器人操作的开源 VLA 模型。</td>
<td width="230">OpenVLA</td>
<td width="240">机器人动作</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">CoRL 机器人学习方法</td>
<td width="240">机器人策略</td>
<td width="200">机器人基准</td>
<td width="360">补充 CoRL VLA 研究覆盖。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2406.09246">论文</a></td>
<td width="110" nowrap><a href="https://openvla.github.io">项目</a></td>
<td width="110" nowrap><a href="https://github.com/openvla/openvla">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2023</td>
<td width="320"><a href="https://arxiv.org/abs/2307.15818">RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control</a></td>
<td width="420">RT-2 将网络规模的视觉语言知识迁移到机器人控制。</td>
<td width="230">RT-2</td>
<td width="240">机器人动作</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">CoRL 机器人学习方法</td>
<td width="240">机器人策略</td>
<td width="200">机器人基准</td>
<td width="360">补充 CoRL VLA 研究覆盖。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2307.15818">论文</a></td>
<td width="110" nowrap><a href="https://robotics-transformer2.github.io">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2508.19958">Long-VLA: Unleashing Long-Horizon Capability of Vision Language Action Model for Robot Manipulation</a></td>
<td width="420">Long-VLA 利用 VLA 策略处理长时程机器人操作。</td>
<td width="230">Long-VLA</td>
<td width="240">机器人动作</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">CoRL 机器人学习方法</td>
<td width="240">机器人策略</td>
<td width="200">机器人基准</td>
<td width="360">补充 CoRL VLA 研究覆盖。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2508.19958">论文</a></td>
<td width="110" nowrap><a href="https://long-vla.github.io/">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2021</td>
<td width="320"><a href="https://arxiv.org/abs/2202.02005">BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning</a></td>
<td width="420">BC-Z 研究机器人模仿学习中的零样本任务泛化。</td>
<td width="230">BC-Z</td>
<td width="240">机器人动作</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">CoRL 机器人学习方法</td>
<td width="240">机器人策略</td>
<td width="200">机器人基准</td>
<td width="360">补充 CoRL VLA 研究覆盖。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2202.02005">论文</a></td>
<td width="110" nowrap><a href="https://sites.google.com/view/bc-z/home">项目</a></td>
<td width="110" nowrap><a href="https://github.com/google-research/tensor2robot/tree/master/research/bcz">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2022</td>
<td width="320"><a href="https://arxiv.org/abs/2209.04899">Hiveformer: Instruction-driven history-aware policies for robotic manipulations</a></td>
<td width="420">Hiveformer 构建考虑历史信息、以指令为条件的机器人操作策略。</td>
<td width="230">Hiveformer</td>
<td width="240">机器人动作</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">CoRL 机器人学习方法</td>
<td width="240">机器人策略</td>
<td width="200">机器人基准</td>
<td width="360">补充 CoRL VLA 研究覆盖。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2209.04899">论文</a></td>
<td width="110" nowrap><a href="https://vlc-robot.github.io/hiveformer-corl/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/vlc-robot/hiveformer">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2023</td>
<td width="320"><a href="https://arxiv.org/abs/2303.00905">Open-World Object Manipulation using Pre-trained Vision-Language Models</a></td>
<td width="420">MOO 利用预训练视觉语言模型研究开放世界物体操作。</td>
<td width="230">Open-World Object Manipulation using Pre-trained Vision-Language Models</td>
<td width="240">机器人动作</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">CoRL 机器人学习方法</td>
<td width="240">机器人策略</td>
<td width="200">机器人基准</td>
<td width="360">补充 CoRL VLA 研究覆盖。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2303.00905">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2024</td>
<td width="320"><a href="https://arxiv.org/abs/2410.05273">HiRT: Enhancing Robotic Control with Hierarchical Robot Transformers</a></td>
<td width="420">HiRT 利用层级机器人 Transformer 改善机器人控制。</td>
<td width="230">HiRT</td>
<td width="240">机器人动作</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">CoRL 机器人学习方法</td>
<td width="240">机器人策略</td>
<td width="200">机器人基准</td>
<td width="360">补充 CoRL VLA 研究覆盖。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2410.05273">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2023</td>
<td width="320"><a href="https://arxiv.org/abs/2307.14535">Scaling Up and Distilling Down: Language-Guided Robot Skill Acquisition</a></td>
<td width="420">SUDD 扩展语言引导的机器人技能学习，并将其蒸馏为可执行策略。</td>
<td width="230">Scaling Up and Distilling Down</td>
<td width="240">机器人动作</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">CoRL 机器人学习方法</td>
<td width="240">机器人策略</td>
<td width="200">机器人基准</td>
<td width="360">补充 CoRL VLA 研究覆盖。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2307.14535">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/real-stanford/scalingup">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2024</td>
<td width="320"><a href="https://openaccess.thecvf.com/content/CVPR2024/html/Li_ManipLLM_Embodied_Multimodal_Large_Language_Model_for_Object-Centric_Robotic_Manipulation_CVPR_2024_paper.html">ManipLLM: Embodied Multimodal Large Language Model for Object-Centric Robotic Manipulation</a></td>
<td width="420">ManipLLM 将多模态语言推理落地到以物体为中心的机器人操作。</td>
<td width="230">多模态大语言模型</td>
<td width="240">机器人动作</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">以物体为中心的具身推理</td>
<td width="240">机器人操作策略</td>
<td width="200">仿真操作</td>
<td width="360">利用多模态大语言模型推理，实现以物体为中心的操作。</td>
<td width="110" nowrap><a href="https://openaccess.thecvf.com/content/CVPR2024/papers/Li_ManipLLM_Embodied_Multimodal_Large_Language_Model_for_Object-Centric_Robotic_Manipulation_CVPR_2024_paper.pdf">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2024</td>
<td width="320"><a href="https://proceedings.neurips.cc/paper_files/paper/2024/hash/62203a74e233e933b160711e791e1a02-Abstract-Conference.html">PEAC: Unsupervised Pre-training for Cross-Embodiment Reinforcement Learning</a></td>
<td width="420">PEAC 在不同本体间预训练策略，在下游机器人学习前改善迁移能力。</td>
<td width="230">跨本体策略</td>
<td width="240">机器人动作</td>
<td width="300">VLA / 跨本体</td>
<td width="260">无监督预训练</td>
<td width="240">通用机器人策略</td>
<td width="200">跨本体基准</td>
<td width="360">改善跨本体策略迁移。</td>
<td width="110" nowrap><a href="https://proceedings.neurips.cc/paper_files/paper/2024/file/62203a74e233e933b160711e791e1a02-Paper-Conference.pdf">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://openaccess.thecvf.com/content/ICCV2025/html/Chen_CombatVLA_An_Efficient_Vision-Language-Action_Model_for_Combat_Tasks_in_3D_ICCV_2025_paper.html">CombatVLA: An Efficient Vision-Language-Action Model for Combat Tasks in 3D Action Role-Playing Games</a></td>
<td width="420">CombatVLA 研究用于实时三维游戏战斗任务的高效 VLA 控制。</td>
<td width="230">CombatVLA</td>
<td width="240">游戏动作</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">高效 VLA 控制</td>
<td width="240">实时具身智能体</td>
<td width="200">三维游戏任务</td>
<td width="360">在快速三维交互任务中评测 VLA 式动作模型。</td>
<td width="110" nowrap><a href="https://openaccess.thecvf.com/content/ICCV2025/papers/Chen_CombatVLA_An_Efficient_Vision-Language-Action_Model_for_Combat_Tasks_in_3D_ICCV_2025_paper.pdf">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2024</td>
<td width="320"><a href="https://openreview.net/forum?id=lFYj0oibGR">Vision-Language Foundation Models as Effective Robot Imitators</a></td>
<td width="420">该工作将视觉语言基础模型适配为机器人模仿学习器，以学习操作策略。</td>
<td width="230">视觉语言基础模型</td>
<td width="240">机器人动作</td>
<td width="300">模仿学习</td>
<td width="260">视觉语言模型到策略的适配</td>
<td width="240">机器人模仿策略</td>
<td width="200">机器人操作基准</td>
<td width="360">将预训练视觉语言模型用作有效的机器人模仿学习器。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=lFYj0oibGR">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2023</td>
<td width="320"><a href="https://arxiv.org/abs/2311.01977">RT-Trajectory: Robotic Task Generalization via Hindsight Trajectory Sketches</a></td>
<td width="420">RT-Trajectory 利用回溯轨迹草图，改善机器人任务泛化。</td>
<td width="230">机器人策略</td>
<td width="240">轨迹草图</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">回溯轨迹条件化</td>
<td width="240">通用操作策略</td>
<td width="200">机器人操作任务</td>
<td width="360">通过轨迹草图监督改善任务泛化。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2311.01977">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2023</td>
<td width="320"><a href="https://openreview.net/forum?id=nkDMZ8yqBt">VIMA: General Robot Manipulation with Multimodal Prompts</a></td>
<td width="420">VIMA 将机器人操作建模为以多模态提示为条件的策略学习。</td>
<td width="230">VIMA</td>
<td width="240">操作动作</td>
<td width="300">多模态提示策略</td>
<td width="260">以提示为条件的模仿学习</td>
<td width="240">通用操作策略</td>
<td width="200">VIMA-Bench</td>
<td width="360">利用多模态提示指定多样化操作任务。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=nkDMZ8yqBt">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2025</td>
<td width="320"><a href="https://proceedings.iclr.cc/paper_files/paper/2025/hash/8667f264f88c7938a73a53ab01eb1327-Abstract-Conference.html">TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies</a></td>
<td width="420">TraceVLA 加入视觉轨迹提示，增强通用机器人策略的时空感知。</td>
<td width="230">通用 VLA</td>
<td width="240">机器人动作</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">视觉轨迹提示</td>
<td width="240">通用机器人策略</td>
<td width="200">机器人操作基准</td>
<td width="360">利用视觉轨迹增强机器人策略感知。</td>
<td width="110" nowrap><a href="https://proceedings.iclr.cc/paper_files/paper/2025/hash/8667f264f88c7938a73a53ab01eb1327-Abstract-Conference.html">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ECCV 2024</td>
<td width="320"><a href="https://openreview.net/forum?id=Sa7upAJOIN">QUAR-VLA: Vision-Language-Action Model for Quadruped Robots</a></td>
<td width="420">QUAR-VLA 将 VLA 式策略学习扩展到四足机器人控制。</td>
<td width="230">四足 VLA</td>
<td width="240">运动动作</td>
<td width="300">VLA / 四足机器人</td>
<td width="260">视觉语言动作控制</td>
<td width="240">四足策略</td>
<td width="200">四足机器人任务</td>
<td width="360">将 VLA 建模应用于四足具身控制。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=Sa7upAJOIN">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2508.05186">Learning to See and Act: Task-Aware Virtual View Exploration for Robotic Manipulation</a></td>
<td width="420">该工作利用任务感知的虚拟视角探索，改善操作中的感知与动作。</td>
<td width="230">机器人操作模型</td>
<td width="240">操作动作</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">虚拟视角探索</td>
<td width="240">机器人操作策略</td>
<td width="200">操作基准</td>
<td width="360">通过任务感知视角探索，改善操作策略的输入。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2508.05186">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>IROS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2409.12514">TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation</a></td>
<td width="420">TinyVLA 用小型 VLA 和扩散策略提升机器人操作的数据效率与推理速度。</td>
<td width="230">TinyVLA</td>
<td width="240">扩散动作</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">紧凑 VLA + 扩散策略</td>
<td width="240">数据高效 VLA</td>
<td width="200">真实机器人操作</td>
<td width="360">构建更小、更快的数据高效 VLA 操作策略。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2409.12514">论文</a></td>
<td width="110" nowrap><a href="https://tiny-vla.github.io/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/JayceWen/tinyvla">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2502.05485">HAMSTER: Hierarchical Action Models For Open-World Robot Manipulation</a></td>
<td width="420">HAMSTER 用分层动作模型连接开放世界操作中的高层决策和低层可执行机器人动作。</td>
<td width="230">HAMSTER</td>
<td width="240">层级动作</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">层级动作建模</td>
<td width="240">开放世界操作策略</td>
<td width="200">机器人操作基准</td>
<td width="360">构建带显式动作层级的开放世界机器人操作策略。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2502.05485">论文</a></td>
<td width="110" nowrap><a href="https://hamster-robot.github.io/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/liyi14/HAMSTER_beta">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2406.20095">LLaRA: Supercharging Robot Learning Data for Vision-Language Policy</a></td>
<td width="420">LLaRA 通过转换和增强机器人学习数据，提升视觉语言策略训练效果。</td>
<td width="230">LLaRA</td>
<td width="240">策略动作</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">用于视觉语言预训练/VLA 的机器人数据增强</td>
<td width="240">视觉语言策略</td>
<td width="200">机器人学习数据集</td>
<td width="360">用更强的语言对齐训练数据提升机器人策略学习。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2406.20095">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/LostXine/LLaRA">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=54U3XHf7qq">MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation</a></td>
<td width="420">提出带工作记忆与长期感知-认知记忆库的 VLA，使长时序操作能利用历史上下文生成动作。</td>
<td width="230">视觉语言模型 + 扩散动作专家</td>
<td width="240">扩散动作序列</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">认知—记忆—动作 + 感知认知记忆库</td>
<td width="240">以记忆为条件的 VLA</td>
<td width="200">仿真 + 实机</td>
<td width="360">长时序机器人操作中的历史记忆建模</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=54U3XHf7qq">论文</a></td>
<td width="110" nowrap><a href="https://shihao1895.github.io/MemoryVLA">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=DdrsHWobR1">Disentangled Robot Learning via Separate Forward and Inverse Dynamics Pretraining</a></td>
<td width="420">DeFI 将视觉前向动力学与逆动力学预训练解耦，再统一微调用于动作预测。</td>
<td width="230">DeFI</td>
<td width="240">潜在动作 / 逆动力学</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">GFDM + GIDM 解耦预训练</td>
<td width="240">正逆动力学 VLA</td>
<td width="200">仿真 + 实机</td>
<td width="360">解耦视频预测与动作预测以提升泛化</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=DdrsHWobR1">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=IBJtOltTbx">Hybrid Training for Vision-Language-Action Models</a></td>
<td width="420">HyT 让 VLA 从思维链推理轨迹中学习，但测试时可直接输出动作以保持快速推理。</td>
<td width="230">-</td>
<td width="240">自回归/直接动作</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">混合训练</td>
<td width="240">使用思维链训练的直接动作 VLA</td>
<td width="200">仿真 + 实机</td>
<td width="360">在保留推理收益的同时降低 VLA 推理延迟</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=IBJtOltTbx">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=LYyoRqf0Ij">End-to-end Listen, Look, Speak and Act</a></td>
<td width="420">ELLSA 用 SA-MoE 在单一架构中同时感知并生成视觉、文本、语音和动作。</td>
<td width="230">ELLSA</td>
<td width="240">多模态动作生成</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">SA-MoE</td>
<td width="240">全双工全模态 VLA</td>
<td width="200">语音交互 + 机器人基准</td>
<td width="360">端到端多模态交互与动作生成</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=LYyoRqf0Ij">论文</a></td>
<td width="110" nowrap><a href="https://anonymous.4open.science/r/LLSA-E821">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=OJh7oBCYhL">RoboOmni: Proactive Robot Manipulation in Omni-modal Context</a></td>
<td width="420">RoboOmni 从语音、环境声和视觉线索中主动推断意图并执行操作。</td>
<td width="230">全模态大语言模型</td>
<td width="240">执行器动作</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">感知器—思考器—说话器—执行器</td>
<td width="240">主动全模态 VLA</td>
<td width="200">-</td>
<td width="360">跨模态上下文中的主动机器人操作</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=OJh7oBCYhL">论文</a> / <a href="https://arxiv.org/pdf/2510.23763">论文</a></td>
<td width="110" nowrap><a href="https://openmoss.github.io/RoboOmni/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/OpenMOSS/RoboOmni">代码</a></td>
<td width="240"><a href="https://huggingface.co/OpenMOSS-Team/RoboOmni">Hugging Face</a> / <a href="https://huggingface.co/datasets/fnlp/OmniAction">Hugging Face</a></td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=PklMD8PwUy">Unified Vision-Language-Action Model</a></td>
<td width="420">UniVLA 将视觉、语言、动作统一为离散词元序列，并用世界模型后训练提升长程策略学习。</td>
<td width="230">UniVLA</td>
<td width="240">离散词元自回归</td>
<td width="300">VLA / 高效/轻量 VLA</td>
<td width="260">统一多模态词元建模 + 世界模型后训练</td>
<td width="240">自回归统一 VLA</td>
<td width="200">CALVIN/LIBERO/SimplerEnv + ALOHA 实机</td>
<td width="360">解决传统 VLA 过度依赖视觉语言模型语义、忽略视觉中的时序因果结构的问题。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=PklMD8PwUy">论文</a> / <a href="https://arxiv.org/abs/2503.10631">论文</a> / <a href="https://arxiv.org/abs/2506.19850">论文</a></td>
<td width="110" nowrap><a href="https://hybrid-vla.github.io/">项目</a> / <a href="https://robertwyq.github.io/univla.github.io/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/PKU-HMI-Lab/Hybrid-VLA">代码</a> / <a href="https://github.com/baaivision/UniVLA">代码</a></td>
<td width="240">CALVIN/LIBERO/SimplerEnv/ALOHA</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=T3i7Ifeatk">Align-Then-stEer: Adapting the Vision-Language Action Models through Unified Latent Guidance</a></td>
<td width="420">ATE 先对齐不同动作空间，再用统一潜空间指导扩散/流 VLA 适配新任务和新本体。</td>
<td width="230">预训练扩散/流 VLA</td>
<td width="240">潜在动作引导</td>
<td width="300">VLA / 高效/轻量 VLA</td>
<td width="260">Align-Then-stEer / 反向 KL 的 VAE 潜在对齐</td>
<td width="240">插件式适配</td>
<td width="200">仿真 + 实机</td>
<td width="360">解决预训练 VLA 下游适配时动作分布错配、数据和算力成本高的问题。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=T3i7Ifeatk">论文</a> / <a href="https://arxiv.org/abs/2509.02055">论文</a></td>
<td width="110" nowrap><a href="https://align-then-steer.github.io/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/TeleHuman/Align-Then-Steer">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=UD4Rw8MOEK">Verifier-free Test-Time Sampling for Vision Language Action Models</a></td>
<td width="420">MG-Select 用模型内部掩码参考动作分布的 KL 置信度在测试时选择动作候选。</td>
<td width="230">-</td>
<td width="240">自回归候选选择</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">MG-Select / 掩码分布引导选择</td>
<td width="240">无需验证器的测试时扩展</td>
<td width="200">仿真 + 实机</td>
<td width="360">无额外验证器的测试时动作选择</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=UD4Rw8MOEK">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=kt51kZH4aG">X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model</a></td>
<td width="420">X-VLA 用本体特定软提示和流匹配 Transformer 学习跨机器人平台的通用控制。</td>
<td width="230">X-VLA</td>
<td width="240">流匹配连续动作</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">本体专属软提示</td>
<td width="240">跨本体 VLA</td>
<td width="200">6 个仿真环境 + 3 个实机平台</td>
<td width="360">跨本体 VLA 训练与泛化</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=kt51kZH4aG">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=tc2UsBeODW">VLM4VLA: Revisiting Vision-Language-Models in Vision-Language-Action Models</a></td>
<td width="420">VLM4VLA 系统比较不同视觉语言模型作为 VLA 主干的迁移效果，指出通用视觉语言模型能力不能直接预测控制性能。</td>
<td width="230">VLM4VLA 最小适配器</td>
<td width="240">策略动作</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">最小视觉语言模型到 VLA 适配 + 具身能力消融</td>
<td width="240">基准/适配流程</td>
<td width="200">3 个基准</td>
<td width="360">评估视觉语言模型主干对 VLA 控制的真实贡献</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=tc2UsBeODW">论文</a></td>
<td width="110" nowrap><a href="https://cladernyjorn.github.io/VLM4VLA.github.io/">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=tsxwloasw5">Vision-Language-Action Instruction Tuning: From Understanding to Manipulation</a></td>
<td width="420">InstructVLA 用 VLA 指令微调同时保留视觉语言模型推理能力并提升精细操作性能。</td>
<td width="230">InstructVLA</td>
<td width="240">自回归/动作生成</td>
<td width="300">VLA / 强化学习/在线微调</td>
<td width="260">VLA-IT + 混合专家适配</td>
<td width="240">端到端指令微调 VLA</td>
<td width="200">-</td>
<td width="360">解决 VLA 在视觉语言理解与动作生成之间互相牺牲、且容易遗忘预训练能力的问题。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=tsxwloasw5">论文</a> / <a href="https://arxiv.org/abs/2507.17520">论文</a></td>
<td width="110" nowrap><a href="https://yangs03.github.io/InstructVLA_Home/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/InternRobotics/InstructVLA">代码</a></td>
<td width="240">650K 条 VLA-IT 数据集</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=KcJ9U0x6kO">HAMLET: Switch Your Vision-Language-Action Model into a History-Aware Policy</a></td>
<td width="420">HAMLET 用时刻词元和轻量记忆模块把只看当前帧的 VLA 改造成历史感知策略。</td>
<td width="230">GR00T N1.5 / 预训练 VLA</td>
<td width="240">历史感知动作预测</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">时刻词元 + 时间对比初始化 + 记忆模块</td>
<td width="240">历史感知 VLA 适配器</td>
<td width="200">RoboCasa/LIBERO + 实机</td>
<td width="360">长程历史依赖操作</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=KcJ9U0x6kO">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38902">DiTEA: Mixture-of-Experts for Vision-Language-Action Model in Robotic Manipulation</a></td>
<td width="420">DiTEA 在扩散 VLA 动作头中加入动作混合专家和任务指令门控以减轻多任务遗忘。</td>
<td width="230">基于扩散的 VLA</td>
<td width="240">扩散</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">扩散 Transformer 动作混合专家 + 任务指令门控</td>
<td width="240">混合专家 VLA</td>
<td width="200">仿真 + 实机</td>
<td width="360">多任务扩散 VLA 的指令跟随与抗遗忘</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38902">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38910">TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for Vision-Language-Action Models</a></td>
<td width="420">TTF-VLA 训练自由地融合历史与当前视觉词元，提升 VLA 在噪声和时序场景下的推理质量。</td>
<td width="230">OpenVLA / VLA-Cache</td>
<td width="240">词元级推理增强</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">时间词元融合 + 像素差异 + 注意力相关性</td>
<td width="240">免训练推理插件</td>
<td width="200">LIBERO + SimplerEnv + 实机</td>
<td width="360">时序视觉词元融合</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38910">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/62813">Being-H0: Vision-Language-Action Pretraining from Large-Scale Human Videos</a></td>
<td width="420">Being-H0 从大规模人手视频中进行物理指令调优和手部运动词元化，迁移到灵巧操作。</td>
<td width="230">Being-H0</td>
<td width="240">部位级运动词元 / 自回归</td>
<td width="300">VLA / 强化学习/在线微调</td>
<td width="260">物理指令微调 + 手部运动词元化</td>
<td width="240">灵巧 VLA</td>
<td width="200">人类视频预训练 + 真实机器人</td>
<td width="360">解决 VLA 依赖昂贵机器人示教、灵巧操作泛化不足的问题。</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/62813">论文</a> / <a href="https://arxiv.org/pdf/2507.15597">论文</a> / <a href="https://arxiv.org/abs/2507.15597">论文</a></td>
<td width="110" nowrap><a href="https://beingbeyond.github.io/Being-H0">项目</a> / <a href="https://beingbeyond.github.io/Being-H0/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/BeingBeyond/Being-H0">代码</a></td>
<td width="240">BeingBeyond h0_post_train 数据集</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/60980">RA-VLA: Retrieval-Augmented VLA for Test-Time Adaptation</a></td>
<td width="420">RA-VLA 用行为对齐检索和落地执行流程在无需训练的测试时适配新任务分布。</td>
<td width="230">RA-VLA</td>
<td width="240">基于检索的动作</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">行为对齐检索 + 落地执行</td>
<td width="240">测试时适应 VLA</td>
<td width="200">LIBERO + UR5e 实机</td>
<td width="360">训练自由测试时适配</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/60980">论文</a></td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/60980">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/62270">A Generalist Pair-wise Progress Critic Model for Vision-Language-Action Robots</a></td>
<td width="420">VLAC 将动作策略与成对任务进度评论家统一在自回归架构中，为强化学习提供内在奖励。</td>
<td width="230">VLAC</td>
<td width="240">自回归</td>
<td width="300">VLA / 强化学习/在线微调</td>
<td width="260">成对进度评论家 + 内在奖励强化学习</td>
<td width="240">动作评论家 VLA</td>
<td width="200">多样化任务 + 实机强化学习</td>
<td width="360">通用任务进度评估与动作生成</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/62270">论文</a></td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/62270">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/62528">Bring My Cup! Personalizing Vision-Language-Action Models with Visual Attentive Prompting</a></td>
<td width="420">VAP 用少量参考图像作为视觉记忆，对冻结 VLA 注入目标实例注意力以执行个性化指令。</td>
<td width="230">冻结 VLA</td>
<td width="240">视觉提示动作</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">视觉注意提示</td>
<td width="240">免训练个性化适配器</td>
<td width="200">Personalized-SIMPLER/Personalized-VLABench + 实机</td>
<td width="360">个性化对象操作</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/62528">论文</a></td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/62528">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">Personalized-SIMPLER</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/66596">From Abstraction to Instantiation: Learning Behavioral Representation for Vision-Language-Action Model</a></td>
<td width="420">BehaviorVLA 学习长时序行为表征，并按执行阶段解码为精确动作以增强分布外泛化。</td>
<td width="230">BehaviorVLA</td>
<td width="240">自回归 / 行为条件解码</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">VBE + PBD</td>
<td width="240">行为表示 VLA</td>
<td width="200">RoboTwin2/LIBERO/CALVIN + 真实仿真到现实迁移</td>
<td width="360">时序一致行为表征</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/66596">论文</a></td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/66596">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/61157">VLA-ATTC: Adaptive Test-Time Compute for VLA Models with Relative Action Critic Model</a></td>
<td width="420">VLA-ATTC 用不确定性触发测试时思考，并用相对动作评论家在候选动作中选择最优。</td>
<td width="230">PI0.5 / VLA</td>
<td width="240">候选动作选择</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">自适应测试时计算 + 相对动作评论家</td>
<td width="240">测试时计算 VLA</td>
<td width="200">LIBERO-LONG</td>
<td width="360">自适应测试时计算与动作选择</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/61157">论文</a></td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/61157">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/66066">SCALE: Self-uncertainty Conditioned Adaptive Looking and Execution for Vision-Language-Action Models</a></td>
<td width="420">SCALE 用 VLA 自身不确定性在单次前向中同时调节视觉感知和动作探索/利用。</td>
<td width="230">通用 VLA</td>
<td width="240">自适应执行</td>
<td width="300">VLA / 强化学习/在线微调</td>
<td width="260">以自身不确定性为条件的自适应观察/执行</td>
<td width="240">免训练单次前向推理策略</td>
<td width="200">仿真 + 实机</td>
<td width="360">训练自由测试时鲁棒执行</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/66066">论文</a></td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/66066">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/64826">XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations</a></td>
<td width="420">XR-1 学习统一的视觉-运动编码，用于在异构机器人、任务和演示数据上训练通用 VLA 策略。</td>
<td width="230">-</td>
<td width="240">自回归</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">-</td>
<td width="240">-</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/64826">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/66510">Escaping the Diversity Trap in Robotic Manipulation via Anchor-Centric Adaptation</a></td>
<td width="420">ACA 证明少量预算下盲目追求示教多样性会带来密度不足，并用锚点重复示教再扩展边界来适配。</td>
<td width="230">VLA 适配</td>
<td width="240">残差更新</td>
<td width="300">通用 VLA / 通用 VLA</td>
<td width="260">以锚点为中心的适配</td>
<td width="240">数据高效真实机器人适配</td>
<td width="200">实机</td>
<td width="360">低预算本体适配</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/66510">论文</a></td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/66510">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/63997">Embodied Interpretability: Linking Causal Understanding to Generalization in Vision-Language-Action Models</a></td>
<td width="420">该文用干预式掩码估计视觉区域对动作预测的因果影响，并用 NMR 预测泛化。</td>
<td width="230">-</td>
<td width="240">用于诊断，而非动作表示</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">ISS + NMR</td>
<td width="240">可解释性/诊断</td>
<td width="200">操作任务</td>
<td width="360">VLA 因果归因与泛化诊断</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/63997">论文</a></td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/63997">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2511.04555">Evo-1: Lightweight Vision-Language-Action Model with Preserved Semantic Alignment</a></td>
<td width="420">Evo-1 面向轻量 VLA，在压缩模型规模时保持语言-视觉语义对齐与操作能力。</td>
<td width="230">Evo-1</td>
<td width="240">-</td>
<td width="300">VLA / 高效/轻量 VLA</td>
<td width="260">-</td>
<td width="240">轻量 VLA</td>
<td width="200">-</td>
<td width="360">轻量化 VLA 语义对齐保持</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2511.04555">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/MINT-SJTU/Evo-1">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2512.09928">HiF-VLA: Hindsight, Insight and Foresight through Motion Representation for Vision-Language-Action Models</a></td>
<td width="420">HiF-VLA 用运动表征引入回溯、洞察、前瞻来增强 VLA 对动作过程的理解。</td>
<td width="230">HiF-VLA</td>
<td width="240">运动表示</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">回溯/洞察/前瞻运动建模</td>
<td width="240">-</td>
<td width="200">-</td>
<td width="360">运动表征增强 VLA</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2512.09928">论文</a></td>
<td width="110" nowrap><a href="https://hifvla.github.io/">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2603.12193">SaPaVe: Towards Active Perception and Manipulation in Vision-Language-Action Models for Robotics</a></td>
<td width="420">SaPaVe 将主动感知与操作结合，让 VLA 在不确定场景中能先看再做。</td>
<td width="230">SaPaVe</td>
<td width="240">自回归</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">主动感知 + 操作</td>
<td width="240">-</td>
<td width="200">-</td>
<td width="360">主动感知驱动操作</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2603.12193">论文</a></td>
<td width="110" nowrap><a href="https://lmzpai.github.io/SaPaVe">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2601.12796">Contact-Aware Neural Dynamics</a></td>
<td width="420">该文学习接触感知神经动力学，用于建模接触丰富操作中的状态变化。</td>
<td width="230">-</td>
<td width="240">自回归</td>
<td width="300">接触丰富动力学 / 机器人操作</td>
<td width="260">接触感知神经动力学</td>
<td width="240">动力学模型，非通用 VLA</td>
<td width="200">-</td>
<td width="360">接触感知动力学建模</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2601.12796">论文</a></td>
<td width="110" nowrap><a href="https://changwei-jing.github.io/neural-physics/">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2508.21046">CogVLA: Cognition-Aligned Vision-Language-Action Model via Instruction-Driven Routing &amp; Sparsification</a></td>
<td width="420">CogVLA 通过指令驱动路由与稀疏化减少 VLA 后训练开销并提升效率。</td>
<td width="230">CogVLA</td>
<td width="240">自回归</td>
<td width="300">VLA / 高效/轻量 VLA</td>
<td width="260">指令驱动路由 + 稀疏化</td>
<td width="240">高效 VLA</td>
<td width="200">-</td>
<td width="360">解决大基于视觉语言模型的 VLA 后训练和部署计算成本高的问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2508.21046">论文</a></td>
<td width="110" nowrap><a href="https://jiutian-vl.github.io/CogVLA-page/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/JiuTian-VL/CogVLA">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2505.15660">Exploring the Limits of Vision-Language-Action Manipulation in Cross-task Generalization</a></td>
<td width="420">该文系统评估 VLA 跨任务泛化边界，并提出 AGNOSTOS/X-ICM 相关方法提升泛化。</td>
<td width="230">AGNOSTOS / X-ICM</td>
<td width="240">-</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">-</td>
<td width="240">跨任务泛化研究</td>
<td width="200">-</td>
<td width="360">跨任务泛化边界评估</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2505.15660">论文</a> / <a href="https://arxiv.org/pdf/2505.15660">论文</a></td>
<td width="110" nowrap><a href="https://jiaming-zhou.github.io/AGNOSTOS/">项目</a> / <a href="https://jiaming-zhou.github.io/AGNOSTOS">项目</a></td>
<td width="110" nowrap><a href="https://github.com/jiaming-zhou/X-ICM">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2505.15517">Robo2VLM: Improving Visual Question Answering using Large-Scale Robot Manipulation Data</a></td>
<td width="420">Robo2VLM 用大规模机器人操作数据改进视觉语言模型/VQA 对物体状态和可操作性的理解。</td>
<td width="230">-</td>
<td width="240">自回归</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">-</td>
<td width="240">机器人数据增强的视觉语言模型/视觉问答，非动作策略</td>
<td width="200">-</td>
<td width="360">机器人操作数据增强视觉问答</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2505.15517">论文</a></td>
<td width="110" nowrap><a href="https://berkeleyautomation.github.io/robo2vlm/">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2506.22242">4D-VLA: Spatiotemporal Vision-Language-Action Pretraining with Cross-Scene Calibration</a></td>
<td width="420">4D-VLA 通过 RGB-D 时序、坐标对齐和记忆库采样缓解跨场景预训练中的状态/坐标混乱。</td>
<td width="230">4D-VLA</td>
<td width="240">自回归</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">四维时空预训练 + 跨场景校准 + 记忆库采样</td>
<td width="240">-</td>
<td width="200">仿真 + 实机</td>
<td width="360">解决多源机器人数据预训练中输入不完整导致动作分布发散的问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2506.22242">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/LogosRoboticsGroup/4D-VLA">代码</a></td>
<td width="240">MV-Bench</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2510.24194">Blindfolded Experts Generalize Better: Insights from Robotic Manipulation and Videogames</a></td>
<td width="420">该文研究减少视觉依赖的专家为什么在机器人操作和游戏中更能泛化。</td>
<td width="230">-</td>
<td width="240">-</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">盲视专家 / 减少观测分析</td>
<td width="240">泛化分析</td>
<td width="200">-</td>
<td width="360">视觉依赖与泛化关系</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2510.24194">论文</a></td>
<td width="110" nowrap><a href="https://sites.google.com/view/blindfoldedexperts/home">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2510.11321">HiMaCon: Discovering Hierarchical Manipulation Concepts from Unlabeled Multi-Modal Data</a></td>
<td width="420">HiMaCon 从无标注多模态数据中发现层级操作概念，用于结构化表示机器人技能。</td>
<td width="230">-</td>
<td width="240">自回归</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">层级操作概念发现</td>
<td width="240">概念表示</td>
<td width="200">已确认仿真/基准</td>
<td width="360">无标注层级操作概念发现</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2510.11321">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2505.23705">Knowledge Insulating Vision-Language-Action Models: Train Fast, Run Fast, Generalize Better</a></td>
<td width="420">该文通过知识隔离降低 VLA 训练和推理成本，同时提升泛化。</td>
<td width="230">-</td>
<td width="240">-</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">知识隔离</td>
<td width="240">高效/通用 VLA</td>
<td width="200">-</td>
<td width="360">快速训练、快速推理和泛化提升</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2505.23705">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://openreview.net/forum?id=3XuUnUEI7e">Diversifying Parallel Ergodic Search: A Signature Kernel Evolution Strategy</a></td>
<td width="420">该文用签名核演化策略增强并行遍历搜索的轨迹多样性和探索效率。</td>
<td width="230">-</td>
<td width="240">自回归</td>
<td width="300">通用 VLA / 通用 VLA</td>
<td width="260">签名核演化策略</td>
<td width="240">轨迹优化/搜索，非 VLA</td>
<td width="200">机器人基准</td>
<td width="360">多样化并行遍历搜索</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=3XuUnUEI7e">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://iccv.thecvf.com/virtual/2025/poster/1325">FedVLA: Federated Vision-Language-Action Learning with Dual Gating Mixture-of-Experts for Robotic Manipulation</a></td>
<td width="420">FedVLA 用联邦学习和双门控混合专家在多端机器人数据上训练 VLA。</td>
<td width="230">FedVLA</td>
<td width="240">自回归</td>
<td width="300">VLA / 高效/轻量 VLA</td>
<td width="260">联邦学习 + 双门控混合专家</td>
<td width="240">联邦 VLA</td>
<td width="200">-</td>
<td width="360">隐私/多客户端 VLA 学习</td>
<td width="110" nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/1325">论文</a> / <a href="https://arxiv.org/abs/2508.02190">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://iccv.thecvf.com/virtual/2025/poster/225">PASG: A Closed-Loop Framework for Automated Geometric Primitive Extraction and Semantic Anchoring in Robotic Manipulation</a></td>
<td width="420">PASG 自动抽取几何基元并用视觉语言模型语义锚定，连接几何可供性与任务语义。</td>
<td width="230">VLM/Qwen2.5VL-PA</td>
<td width="240">-</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">基元感知语义落地</td>
<td width="240">语义可供性落地框架</td>
<td width="200">基准</td>
<td width="360">几何基元与语义可供性锚定</td>
<td width="110" nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/225">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">空间语义推理基准</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2503.07087">iManip: Skill-Incremental Learning for Robotic Manipulation</a></td>
<td width="420">iManip 面向机器人操作的技能增量学习，在加入新技能时保持旧技能能力。</td>
<td width="230">-</td>
<td width="240">自回归</td>
<td width="300">通用 VLA / 通用 VLA</td>
<td width="260">增量技能学习</td>
<td width="240">技能增量操作</td>
<td width="200">-</td>
<td width="360">机器人技能增量学习</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2503.07087">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://iccv.thecvf.com/virtual/2025/poster/972">4D Visual Pre-training for Robot Learning</a></td>
<td width="420">FVP 将视觉预训练设为下一点云预测，用扩散模型提升真实机器人三维表征和模仿学习成功率。</td>
<td width="230">FVP + DP3</td>
<td width="240">三维策略支持</td>
<td width="300">通用 VLA / 通用 VLA</td>
<td width="260">下一帧点云预测扩散预训练</td>
<td width="240">四维视觉预训练</td>
<td width="200">真实操作</td>
<td width="360">四维/点云视觉预训练</td>
<td width="110" nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/972">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2502.19417">Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models</a></td>
<td width="420">Hi Robot 用层级 VLA 将开放式指令分解为高层规划和低层动作执行。</td>
<td width="230">层级 VLA</td>
<td width="240">自回归</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">层级策略/规划</td>
<td width="240">开放式指令遵循</td>
<td width="200">-</td>
<td width="360">开放式层级指令跟随</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2502.19417">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2025</td>
<td width="320"><a href="https://arxiv.org/pdf/2503.03734">OTTER: A Vision-Language-Action Model with Text-Aware Visual Feature Extraction</a></td>
<td width="420">OTTER 用文本感知视觉特征抽取让 VLA 更聚焦与语言目标相关的图像信息。</td>
<td width="230">OTTER</td>
<td width="240">自回归</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">文本感知视觉特征提取</td>
<td width="240">-</td>
<td width="200">-</td>
<td width="360">文本感知视觉特征抽取</td>
<td width="110" nowrap><a href="https://arxiv.org/pdf/2503.03734">论文</a></td>
<td width="110" nowrap><a href="https://ottervla.github.io/">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2501.18867">UP-VLA: A Unified Understanding and Prediction Model for Embodied Agent</a></td>
<td width="420">UP-VLA 统一理解与预测任务，让具身智能体同时具备语义理解和未来/动作预测能力。</td>
<td width="230">UP-VLA</td>
<td width="240">-</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">-</td>
<td width="240">统一理解预测模型</td>
<td width="200">-</td>
<td width="360">具身理解与预测统一建模</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2501.18867">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/CladernyJorn/UP-VLA">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2411.18825">ELEMENTAL: Interactive Learning from Demonstrations and Vision-Language Models for Reward Design in Robotics</a></td>
<td width="420">ELEMENTAL 结合示教交互和视觉语言模型生成/改进机器人奖励设计。</td>
<td width="230">-</td>
<td width="240">自回归</td>
<td width="300">交互式学习 / 奖励设计</td>
<td width="260">示范 + 视觉语言模型奖励设计</td>
<td width="240">奖励学习，非通用 VLA</td>
<td width="200">-</td>
<td width="360">交互式奖励设计</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2411.18825">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2410.22391">A Large Recurrent Action Model: xLSTM enables Fast Inference for Robotics Tasks</a></td>
<td width="420">LRAM 用 xLSTM 替代 Transformer 构建大动作模型，实现更快推理和长序列外推。</td>
<td width="230">LRAM</td>
<td width="240">序列动作模型</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">xLSTM 循环动作模型</td>
<td width="240">大型循环动作模型</td>
<td width="200">-</td>
<td width="360">解决 Transformer 大动作模型在机器人实时任务中推理慢的问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2410.22391">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/ml-jku/LRAM">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2025</td>
<td width="320"><a href="https://arxiv.org/pdf/2502.13142">Pre-training Auto-regressive Robotic Models with 4D Representations</a></td>
<td width="420">ARM4R 用四维表征预训练自回归机器人模型，增强时空理解与操作泛化。</td>
<td width="230">ARM4R</td>
<td width="240">自回归</td>
<td width="300">通用 VLA / 高效/轻量 VLA</td>
<td width="260">四维表示预训练</td>
<td width="240">-</td>
<td width="200">-</td>
<td width="360">四维表征自回归预训练</td>
<td width="110" nowrap><a href="https://arxiv.org/pdf/2502.13142">论文</a></td>
<td width="110" nowrap><a href="https://arm4r.github.io/">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2025</td>
<td width="320"><a href="https://www.arxiv.org/pdf/2506.03863">STAR: Learning Diverse Robot Skill Abstractions through Rotation-Augmented Vector Quantization</a></td>
<td width="420">STAR 用旋转增强残差技能量化和因果技能 Transformer 学习离散技能抽象与组合。</td>
<td width="230">-</td>
<td width="240">离散技能词元</td>
<td width="300">通用 VLA / 强化学习/在线微调</td>
<td width="260">RaRSQ + 因果技能 Transformer</td>
<td width="240">技能抽象</td>
<td width="200">LIBERO + 实机</td>
<td width="360">解决 VQ 类技能抽象码本坍塌和技能因果组合建模不足的问题。</td>
<td width="110" nowrap><a href="https://www.arxiv.org/pdf/2506.03863">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/iLearn-Lab/ICML25-STAR">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2501.10105">UniAct: Universal Actions For Enhanced Embodied Foundation Models</a></td>
<td width="420">UniAct 提出通用动作作为跨任务/跨本体的动作接口以增强具身基础模型。</td>
<td width="230">UniAct</td>
<td width="240">通用动作</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">通用动作表示</td>
<td width="240">-</td>
<td width="200">-</td>
<td width="360">通用动作表示</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2501.10105">论文</a></td>
<td width="110" nowrap><a href="https://2toinf.github.io/UniAct/">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2503.13446">MoManipVLA: Transferring Vision-language-action Models for General Mobile Manipulation</a></td>
<td width="420">MoManipVLA 将 VLA 迁移到移动操作场景，面向导航与机械臂协同的通用操作。</td>
<td width="230">MoManipVLA</td>
<td width="240">-</td>
<td width="300">VLA / 高效/轻量 VLA</td>
<td width="260">-</td>
<td width="240">移动操作 VLA 迁移</td>
<td width="200">-</td>
<td width="360">通用移动操作迁移</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2503.13446">论文</a></td>
<td width="110" nowrap><a href="https://gary3410.github.io/momanipVLA/">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2503.06960">A Data-Centric Revisit of Pre-Trained Vision Models for Robot Learning</a></td>
<td width="420">该文从数据中心角度重新评估预训练视觉模型对机器人学习的作用。</td>
<td width="230">-</td>
<td width="240">自回归</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">-</td>
<td width="240">以数据为中心的机器人视觉预训练研究</td>
<td width="200">-</td>
<td width="360">预训练视觉模型的数据因素评估</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2503.06960">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/CVMI-Lab/SlotMIM">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2504.00420">Think Small, Act Big: Primitive Prompt Learning for Lifelong Robot Manipulation</a></td>
<td width="420">PPL 通过可复用基元提示支持机器人终身学习中新技能的持续获取。</td>
<td width="230">-</td>
<td width="240">自回归</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">基元提示学习</td>
<td width="240">终身机器人操作</td>
<td width="200">仿真 + 实机</td>
<td width="360">可复用基元提示的终身学习</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2504.00420">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://cvpr.thecvf.com/virtual/2025/poster/32789">Phoenix: A Motion-based Self-Reflection Framework for Fine-grained Robotic Action Correction</a></td>
<td width="420">Phoenix 用运动指令连接多模态大语言模型语义反思和低层扩散策略，实现细粒度动作纠错。</td>
<td width="230">多模态大语言模型 + 运动条件扩散策略</td>
<td width="240">扩散修正</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">双过程运动调整 + 运动条件扩散策略</td>
<td width="240">自我反思/动作修正</td>
<td width="200">-</td>
<td width="360">细粒度机器人动作纠错</td>
<td width="110" nowrap><a href="https://cvpr.thecvf.com/virtual/2025/poster/32789">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2406.14235">Mitigating the Human-Robot Domain Discrepancy in Visual Pre-training for Robotic Manipulation</a></td>
<td width="420">该文缓解人类视频视觉预训练与机器人操作之间的域差异。</td>
<td width="230">-</td>
<td width="240">-</td>
<td width="300">VLA / 通用 VLA</td>
<td width="260">缓解人类与机器人领域差异</td>
<td width="240">面向操作的视觉预训练</td>
<td width="200">-</td>
<td width="360">人-机器人视觉预训练域差异</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2406.14235">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2505.02166">CrayonRobo: Object-Centric Prompt-Driven Vision-Language-Action Model for Robotic Manipulation</a></td>
<td width="420">CrayonRobo 用叠加在图像上的对象中心二维视觉提示表达接触位姿和运动方向，指导长程操作。</td>
<td width="230">-</td>
<td width="240">SE(3) 接触位姿 + 运动方向</td>
<td width="300">VLA / 高效/轻量 VLA</td>
<td width="260">以物体为中心的视觉语言提示</td>
<td width="240">-</td>
<td width="200">仿真 + 实机</td>
<td width="360">解决语言目标歧义、图像/视频目标过细且难表达动作约束的问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2505.02166">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/clorislili/CrayonRobo">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/html/2505.00693">Robotic Visual Instruction</a></td>
<td width="420">RoVI/VIEW 用手绘对象中心二维符号指令表达空间时序约束并转成三维操作动作。</td>
<td width="230">使用视觉语言模型的 VIEW 流程</td>
<td width="240">三维动作序列</td>
<td width="300">VLA / 强化学习/在线微调</td>
<td width="260">机器人视觉指令 + 视觉指令具身工作流</td>
<td width="240">-</td>
<td width="200">仿真 + 实机</td>
<td width="360">解决自然语言机器人指令空间精度不足、公共场景语音不便的问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/html/2505.00693">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">开源 RoVI 数据集</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2411.17662">RoboPEPP: Vision-Based Robot Pose and Joint Angle Estimation through Embedding Predictive Pre-Training</a></td>
<td width="420">RoboPEPP 用嵌入预测预训练从视觉估计机器人姿态和关节角。</td>
<td width="230">-</td>
<td width="240">-</td>
<td width="300">通用 VLA / 通用 VLA</td>
<td width="260">嵌入预测预训练</td>
<td width="240">机器人位姿/关节估计预训练，非通用 VLA</td>
<td width="200">-</td>
<td width="360">视觉机器人姿态与关节估计</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2411.17662">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2504.06961">Two by Two: Learning Multi-Task Pairwise Objects Assembly for Generalizable Robot Manipulation</a></td>
<td width="420">2BY2 构建日常成对物体装配数据集，并用两步 SE(3) 位姿估计完成多任务装配。</td>
<td width="230">-</td>
<td width="240">SE(3) 位姿</td>
<td width="300">通用 VLA / 通用 VLA</td>
<td width="260">利用等变特征的两步 SE(3) 位姿估计</td>
<td width="240">-</td>
<td width="200">-</td>
<td width="360">解决现有装配数据集偏几何碎片/工业零件、不能覆盖日常对象功能关系的问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2504.06961">论文</a></td>
<td width="110" nowrap><a href="https://tea-lab.github.io/TwoByTwo/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/TEA-Lab/TwoByTWo">代码</a></td>
<td width="240">2BY2 数据集</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2503.11269">Prof. Robot: Differentiable Robot Rendering Without Static and Self-Collisions</a></td>
<td width="420">Prof. Robot 提供避免静态和自碰撞的可微机器人渲染，用于机器人视觉/几何学习。</td>
<td width="230">-</td>
<td width="240">-</td>
<td width="300">通用 VLA / 通用 VLA</td>
<td width="260">无碰撞可微机器人渲染</td>
<td width="240">可微渲染/工具，非 VLA</td>
<td width="200">-</td>
<td width="360">可微机器人渲染</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2503.11269">论文</a></td>
<td width="110" nowrap><a href="https://www.qrcat.cn/prof-robot/">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
</tbody>
</table>
