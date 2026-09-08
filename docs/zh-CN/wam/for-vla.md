# 面向 VLA 的世界模型

[首页](../../../README.zh-CN.md) | [英文](../../en/wam/for-vla.md) | [方向目录](README.md)

共 10 篇。

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
<td width="120" nowrap>ECCV 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2602.10098">VLA-JEPA: Enhancing Vision-Language-Action Model with Latent World Model</a></td>
<td width="420">VLA-JEPA 用 JEPA 式潜在未来状态预测预训练 VLA，避免把未来帧泄漏进输入。</td>
<td width="220">面向 VLA 的潜在世界模型</td>
<td width="280">未来帧潜在目标</td>
<td width="260">潜在动作词元 + 动作头微调</td>
<td width="360">VLA 预训练/泛化</td>
<td width="200">LIBERO、LIBERO-Plus、SimplerEnv、真实 Franka</td>
<td width="360">解决视频预训练 VLA 中外观偏置、无关运动和信息泄漏问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2602.10098">论文</a></td>
<td width="110" nowrap><a href="https://ginwind.github.io/VLA-JEPA/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/ginwind/VLA-JEPA">代码</a></td>
<td width="240"><a href="https://huggingface.co/ginwind/VLA-JEPA">Hugging Face</a></td>
</tr>
<tr>
<td width="120" nowrap>ICRA 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2509.22643">VLA-Reasoner: Reinforcing Robotic Reasoning and Generalization with World Model</a></td>
<td width="420">VLA-Reasoner 用世界模型轨迹展开和在线 MCTS 为现有 VLA 加入测试时长程推理。</td>
<td width="220">面向 VLA 的世界模型</td>
<td width="280">预测未来状态</td>
<td width="260">VLA 候选动作</td>
<td width="360">测试时搜索与验证</td>
<td width="200">仿真 + 实机</td>
<td width="360">在动作执行前通过世界模型搜索未来结果。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2509.22643">论文</a></td>
<td width="110" nowrap><a href="https://vla-reasoner.github.io/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/wkguo/VLA-Reasoner">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICRA 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2503.10370">LUMOS: Language-Conditioned Imitation Learning with World Models</a></td>
<td width="420">LUMOS 在学习得到的世界模型潜在空间中离线练习语言条件长时程操作，再迁移到真机。</td>
<td width="220">面向 VLA 的世界模型</td>
<td width="280">潜在世界状态</td>
<td width="260">以语言为条件的动作</td>
<td width="360">离线练习 / 模仿学习</td>
<td width="200">仿真 + 实机</td>
<td width="360">用世界模型练习降低真实机器人数据需求。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2503.10370">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=fHLtSxDFKC">Genie Envisioner: A Unified World Foundation Platform for Robotic Manipulation</a></td>
<td width="420">GE 在视频生成框架内联合学习视觉表示和动作策略，支持跨本体操作。</td>
<td width="220">面向 VLA 的世界模型</td>
<td width="280">结构化视频潜在表示</td>
<td width="260">GE-Act 流匹配解码器/动作轨迹</td>
<td width="360">世界基础平台 + 策略推理</td>
<td width="200">-</td>
<td width="360">解决机器人操作中世界建模和动作策略分离、泛化监督成本高的问题。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=fHLtSxDFKC">论文</a></td>
<td width="110" nowrap><a href="https://genie-envisioner.github.io/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/AgibotTech/Genie-Envisioner-V1">代码</a></td>
<td width="240">&gt;1M 个操作回合 + 已发布基准</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=LQv9LU2Ufg">RIG: Synergizing Reasoning and Imagination in End-to-End Generalist Policy</a></td>
<td width="420">RIG 在端到端通用策略中联合学习推理、动作和下一图像想象。</td>
<td width="220">面向 VLA 的世界模型</td>
<td width="280">推理 + 下一帧图像/世界动力学</td>
<td width="260">结合想象结果的先推理后行动</td>
<td width="360">自纠正/测试时扩展</td>
<td width="200">通用具身策略基准</td>
<td width="360">解决具身智能体只具备推理或想象单一能力、系统式组合效率低的问题。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=LQv9LU2Ufg">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=qE2FyvRvuF">WMPO: World Model-based Policy Optimization for Vision-Language-Action Models</a></td>
<td width="420">WMPO 用像素级世界模型在想象中对 VLA 做同策略 GRPO。</td>
<td width="220">面向 VLA 的世界模型</td>
<td width="280">基于像素的想象轨迹</td>
<td width="260">VLA 策略动作/GRPO</td>
<td width="360">仅基于想象的策略优化</td>
<td width="200">仿真 + 实机</td>
<td width="360">解决 VLA 依赖专家示范、真实机器人强化学习采样成本高的问题。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=qE2FyvRvuF">论文</a></td>
<td width="110" nowrap><a href="https://wm-po.github.io/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/WM-PO/WMPO">代码</a></td>
<td width="240"><a href="https://huggingface.co/fangqi/WMPO">Hugging Face</a></td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=wPEIStHxYH">Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning</a></td>
<td width="420">Cosmos Policy 单阶段微调预训练视频模型，使其生成动作、未来状态和值以支持规划。</td>
<td width="220">面向 VLA 的世界模型 / 视频策略世界模型</td>
<td width="280">表示动作/状态/价值的视频模型潜在帧</td>
<td width="260">潜在帧动作生成 + 规划</td>
<td width="360">视觉运动控制/规划</td>
<td width="200">-</td>
<td width="360">解决视频模型用于机器人策略时需要复杂多阶段训练和额外动作架构的问题。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=wPEIStHxYH">论文</a></td>
<td width="110" nowrap><a href="https://research.nvidia.com/labs/dir/cosmos-policy/cosmos_policy_index.html">项目</a></td>
<td width="110" nowrap><a href="https://github.com/nvlabs/cosmos-policy">代码</a></td>
<td width="240">LIBERO、RoboCasa、真实双臂任务</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38925">WorldAgen: Unified State-Action Prediction with Test-Time World Model Training</a></td>
<td width="420">WorldAgen 用共享 Transformer 同时预测未来状态和动作，并在测试时训练世界模型适应新环境。</td>
<td width="220">面向 VLA 的世界模型</td>
<td width="280">历史状态动作轨迹</td>
<td width="260">智能体模型动作头 + 探索动作</td>
<td width="360">VLA 测试时适应</td>
<td width="200">仿真/基准</td>
<td width="360">解决 VLA 部署到新物体配置或动力学环境时静态预训练难泛化的问题。</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38925">论文</a></td>
<td width="110" nowrap><a href="https://worldagen.github.io/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/mll-lab-nu/WorldAgen">代码</a></td>
<td width="240">CALVIN, LIBERO</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/66169">VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model</a></td>
<td width="420">VLAW 用真实轨迹展开迭代提升动作条件视频世界模型，再生成合成数据改进 VLA。</td>
<td width="220">面向 VLA 的世界模型</td>
<td width="280">以动作为条件的视频世界模型</td>
<td width="260">VLA 动作 + 生成轨迹</td>
<td width="360">VLA 与世界模型迭代共同改进</td>
<td width="200">实机 + 合成轨迹</td>
<td width="360">解决真实轨迹展开昂贵且现有世界模型物理保真度不足以直接改进策略的问题。</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/66169">论文</a></td>
<td width="110" nowrap><a href="https://sites.google.com/view/vla-w">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2603.03195">Chain of World: World Model Thinking in Latent Motion</a></td>
<td width="420">CoWVLA 用视频 VAE 提取连续潜在运动链，并与离散动作预测联合微调。</td>
<td width="220">面向 VLA 的世界模型 / 潜在运动</td>
<td width="280">结构与运动潜在表示</td>
<td width="260">自回归动作序列解码器</td>
<td width="360">VLA 预训练/微调</td>
<td width="200">机器人仿真基准</td>
<td width="360">解决世界模型 VLA 重建冗余背景、潜在动作 VLA 缺少连续时序动力学的问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2603.03195">论文</a></td>
<td width="110" nowrap><a href="https://fx-hit.github.io/cowvla-io/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/fx-hit/CoWVLA">代码</a></td>
<td width="240"><a href="https://huggingface.co/hitfx/CoWVLA">Hugging Face</a></td>
</tr>
</tbody>
</table>
