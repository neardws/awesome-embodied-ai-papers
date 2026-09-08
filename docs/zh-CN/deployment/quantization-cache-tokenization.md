# 量化、缓存与词元化

[首页](../../../README.zh-CN.md) | [英文](../../en/deployment/quantization-cache-tokenization.md) | [方向目录](README.md)

共 22 篇。

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
<td width="320"><a href="https://arxiv.org/abs/2509.23655">Focusing on What Matters: Object-Agent-centric Tokenization for Vision Language Action models</a></td>
<td width="420">该工作研究面向高效 VLA 模型、以物体和智能体为中心的词元化。</td>
<td width="240">量化/缓存/词元化</td>
<td width="280">部署/评测覆盖</td>
<td width="280">机器人/仿真器平台</td>
<td width="280">具身机器人任务</td>
<td width="220">来源列出的资源</td>
<td width="360">补充 CoRL 部署/评测研究覆盖。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2509.23655">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2509.05614">SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning</a></td>
<td width="420">用动作感知自推测剪枝加速 VLA 推理，同时尽量保持动作质量。</td>
<td width="240">压缩/缓存/词元化</td>
<td width="280">自推测剪枝</td>
<td width="280">机器人部署/评测环境</td>
<td width="280">VLA 操作</td>
<td width="220">-</td>
<td width="360">解决 VLA 动作生成中的冗余计算。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2509.05614">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>EMNLP 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2507.22424">Spec-VLA: Speculative Decoding for Vision-Language-Action Models with Relaxed Acceptance</a></td>
<td width="420">把宽松推测解码用于加速 VLA 动作生成。</td>
<td width="240">压缩/缓存/词元化</td>
<td width="280">推测解码</td>
<td width="280">机器人部署/评测环境</td>
<td width="280">VLA 操作</td>
<td width="220">-</td>
<td width="360">解决机器人执行中自回归 VLA 解码慢的问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2507.22424">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2024</td>
<td width="320"><a href="https://arxiv.org/abs/2411.02359">DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution</a></td>
<td width="420">通过动态推理减少机器人执行时的多模态 VLA 计算量。</td>
<td width="240">压缩/缓存/词元化</td>
<td width="280">动态推理</td>
<td width="280">机器人部署/评测环境</td>
<td width="280">机器人执行</td>
<td width="220">代码</td>
<td width="360">解决多模态 VLA 推理中的非必要计算。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2411.02359">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/yueyang130/DeeR-VLA">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2024</td>
<td width="320"><a href="https://arxiv.org/abs/2406.04339">RoboMamba: Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation</a></td>
<td width="420">用 Mamba/状态空间架构提升 VLA 机器人推理和操作效率。</td>
<td width="240">高效架构</td>
<td width="280">状态空间模型主干</td>
<td width="280">机器人部署/评测环境</td>
<td width="280">机器人推理与操作</td>
<td width="220">项目+代码</td>
<td width="360">解决 VLA 策略中的 Transformer 效率瓶颈。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2406.04339">论文</a></td>
<td width="110" nowrap><a href="https://sites.google.com/view/robomamba-web">项目</a></td>
<td width="110" nowrap><a href="https://github.com/lmzpai/roboMamba">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=E1K2Ph3LtS">MetaVLA: Unified Meta Co-Training for Efficient Embodied Adaptation</a></td>
<td width="420">用元协同训练把多任务适配合并到低成本后训练，降低 VLA 微调算力并提升 LIBERO 泛化。</td>
<td width="240">压缩/缓存/词元化</td>
<td width="280">元联合训练</td>
<td width="280">机器人部署/评测环境</td>
<td width="280">LIBERO 操作</td>
<td width="220">计划发布代码</td>
<td width="360">解决 VLA 任务适配成本高、泛化弱的问题。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=E1K2Ph3LtS">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=RwdGIIjPlC">SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration</a></td>
<td width="420">通过动作感知模型调度和时空语义词元剪枝，让 VLA 在 LIBERO/SimplerEnv 中加速且不降性能。</td>
<td width="240">压缩/缓存/词元化</td>
<td width="280">模型调度 + 词元剪枝</td>
<td width="280">机器人部署/评测环境</td>
<td width="280">LIBERO, SimplerEnv</td>
<td width="220">-</td>
<td width="360">解决 VLA 顺序决策中的时间和视觉冗余。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=RwdGIIjPlC">论文</a> / <a href="https://arxiv.org/abs/2506.12723">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=TpL2nXanru">QVLA: Not All Channels Are Equal in Vision-Language-Action Model&#x27;s Quantization</a></td>
<td width="420">提出动作敏感的逐通道混合位宽量化，把 VLA 压到低显存同时保持成功率。</td>
<td width="240">压缩/缓存/词元化</td>
<td width="280">逐通道动作中心量化/剪枝</td>
<td width="280">资源受限机器人硬件</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">解决大语言模型式统一量化不适合机器人动作误差累积的问题。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=TpL2nXanru">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=ea6j8k8Rnw">Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation</a></td>
<td width="420">根据最近动作轨迹动态调整视觉词元保留率，减少长时序 VLA 操作推理延迟。</td>
<td width="240">压缩/缓存/词元化</td>
<td width="280">动作感知动态视觉词元剪枝</td>
<td width="280">机器人部署/评测环境</td>
<td width="280">LIBERO + 真实操作</td>
<td width="220">-</td>
<td width="360">解决操作不同阶段视觉冗余不同但固定剪枝不适配的问题。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=ea6j8k8Rnw">论文</a> / <a href="https://arxiv.org/abs/2509.22093">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=k6nTUFoqeT">FASTer: Toward Powerful and Efficient Autoregressive Vision–Language–Action Models with Learnable Action Tokenizer and Block-wise Decoding</a></td>
<td width="420">用可学习动作词元化器和分块解码提升自回归 VLA 的动作压缩、速度和任务表现。</td>
<td width="240">压缩/缓存/词元化</td>
<td width="280">可学习动作词元化器 + 分块解码</td>
<td width="280">机器人部署/评测环境</td>
<td width="280">仿真 + 实机操作</td>
<td width="220">-</td>
<td width="360">解决动作词元化在重建质量和推理效率之间的折中。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=k6nTUFoqeT">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38880">FT-NCFM: An Influence-Aware Data Distillation Framework for Efficient VLA Models</a></td>
<td width="420">用因果归因和对抗式 NCFM 蒸馏高价值 VLA 数据，少量核心子集达到接近全量训练效果。</td>
<td width="240">压缩/缓存/词元化</td>
<td width="280">数据蒸馏</td>
<td width="280">机器人部署/评测环境</td>
<td width="280">-</td>
<td width="220">计划发布代码和数据</td>
<td width="360">解决 VLA 依赖大规模冗余数据导致训练成本高的问题。</td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38903">CronusVLA: Towards Efficient and Robust Manipulation via Multi-Frame Vision-Language-Action Modeling</a></td>
<td width="420">CronusVLA 以多帧历史特征聚合提升 VLA 操作鲁棒性，同时控制多帧推理开销。</td>
<td width="240">压缩/缓存/词元化</td>
<td width="280">词元化</td>
<td width="280">机器人部署/评测环境</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">解决单帧 VLA 无法利用历史观测且多帧直接输入延迟高的问题。</td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38904">SemanticVLA: Semantic-Aligned Sparsification and Enhancement for Efficient Robotic Manipulation</a></td>
<td width="420">通过语义对齐的视觉稀疏化、层级融合和动作耦合提升 VLA 操作效率与成功率。</td>
<td width="240">压缩/缓存/词元化</td>
<td width="280">语义对齐稀疏化</td>
<td width="280">机器人部署/评测环境</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">解决视觉冗余和浅层指令-视觉对齐影响机器人操作的问题。</td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/JiuTian-VL/SemanticVLA">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38931">VLA-Adapter: An Effective Paradigm for Tiny-Scale Vision-Language-Action Model</a></td>
<td width="420">用小规模 VLA 适配范式在较低模型规模下保持机器人操作能力。</td>
<td width="240">压缩/缓存/词元化</td>
<td width="280">微型 VLA 适配器</td>
<td width="280">机器人部署/评测环境</td>
<td width="280">-</td>
<td width="220">项目+代码</td>
<td width="360">解决微型 VLA 如何有效适配操作任务的问题。</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38931">论文</a> / <a href="https://arxiv.org/abs/2509.09372">论文</a></td>
<td width="110" nowrap><a href="https://vla-adapter.github.io/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/OpenHelix-Team/VLA-Adapter">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38945">MoLe-VLA: Dynamic Layer-skipping Vision Language Action Model via Mixture-of-Layers for Efficient Robot Manipulation</a></td>
<td width="420">用混合层动态跳层减少 VLA 计算量并保持操作成功率。</td>
<td width="240">压缩/缓存/词元化</td>
<td width="280">动态跳层 / 计算量最高压缩 5.6 倍</td>
<td width="280">机器人部署/评测环境</td>
<td width="280">-</td>
<td width="220">项目+代码</td>
<td width="360">解决 VLA 推理中不同样本/步骤不必经过全部层的问题。</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38945">论文</a> / <a href="https://arxiv.org/abs/2503.20384">论文</a></td>
<td width="110" nowrap><a href="https://sites.google.com/view/mole-vla">项目</a></td>
<td width="110" nowrap><a href="https://github.com/RoyZry98/MoLe-VLA-Pytorch/">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2602.20309">QuantVLA: Scale-Calibrated Post-Training Quantization for Vision-Language-Action Models</a></td>
<td width="420">提出免训练训练后量化量化 VLA 语言骨干和 DiT 动作头，显著节省内存。</td>
<td width="240">压缩/缓存/词元化</td>
<td width="280">训练后量化</td>
<td width="280">计算/内存/功耗受限部署</td>
<td width="280">-</td>
<td width="220">项目+代码</td>
<td width="360">解决 VLA 大模型在低算力/低功耗部署中的量化问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2602.20309">论文</a></td>
<td width="110" nowrap><a href="https://quantvla.github.io/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/AIoT-MLSys-Lab/QuantVLA">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2506.06072">BEAST: Efficient Tokenization of B-Splines Encoded Action Sequences for Imitation Learning</a></td>
<td width="420">用 B 样条编码动作序列为定长词元，免单独词元化器训练并生成平滑高频控制。</td>
<td width="240">压缩/缓存/词元化</td>
<td width="280">B 样条动作词元化器</td>
<td width="280">机器人部署/评测环境</td>
<td width="280">166 项仿真任务 + 8 项实机任务</td>
<td width="220">-</td>
<td width="360">解决模仿学习动作序列词元化成本和轨迹平滑性问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2506.06072">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2503.14259">Quantization-Free Autoregressive Action Transformer</a></td>
<td width="420">用连续无限词表 Transformer 直接建模动作，避免离散量化破坏动作空间结构。</td>
<td width="240">连续自回归动作建模</td>
<td width="280">无需量化的连续自回归动作建模</td>
<td width="280">机器人部署/评测环境</td>
<td width="280">降低模型部署成本</td>
<td width="220">代码</td>
<td width="360">解决自回归模仿学习中离散动作码限制连续控制的问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2503.14259">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2506.10100">EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models</a></td>
<td width="420">通过语言层剪枝、视觉词元选择和扩散特征缓存实现免训练 VLA 加速压缩。</td>
<td width="240">压缩/缓存/词元化</td>
<td width="280">层剪枝 + 视觉词元选择 + 扩散缓存</td>
<td width="280">机器人部署/评测环境</td>
<td width="280">CogACT/SIMPLER</td>
<td width="220">-</td>
<td width="360">解决 VLA 管线中语言、视觉和动作头多处冗余。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2506.10100">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2502.02175">VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching</a></td>
<td width="420">自适应复用相邻帧静态视觉词元的键值缓存，提高 VLA 控制频率。</td>
<td width="240">压缩/缓存/词元化</td>
<td width="280">自适应视觉词元键值缓存</td>
<td width="280">机器人部署/评测环境</td>
<td width="280">LIBERO、SIMPLER、真实机器人</td>
<td width="220">项目+代码</td>
<td width="360">解决实时机器人控制中逐帧重复视觉计算的问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2502.02175">论文</a></td>
<td width="110" nowrap><a href="https://vla-cache.github.io/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/siyuhsu/vla-cache">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2507.01016">VQ-VLA: Improving Vision-Language-Action Models via Scaling Vector-Quantized Action Tokenizers</a></td>
<td width="420">用大规模合成/真实轨迹训练 VQ 动作词元化器，提升 VLA 推理速度和长时程动作质量。</td>
<td width="240">压缩/缓存/词元化</td>
<td width="280">向量量化动作词元化器</td>
<td width="280">机器人部署/评测环境</td>
<td width="280">-</td>
<td width="220">项目+代码</td>
<td width="360">解决动作词元化器数据规模不足和泛化弱的问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2507.01016">论文</a></td>
<td width="110" nowrap><a href="https://xiaoxiao0406.github.io/vqvla.github.io">项目</a> / <a href="https://xiaoxiao0406.github.io/vqvla.github.io/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/xiaoxiao0406/VQ-VLA">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2505.15304">Saliency-Aware Quantized Imitation Learning for Efficient Robotic Control</a></td>
<td width="420">用显著性感知量化压缩模仿学习策略，在高效控制和任务性能之间折中。</td>
<td width="240">压缩/缓存/词元化</td>
<td width="280">显著性感知量化模仿学习</td>
<td width="280">机器人部署/评测环境</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">解决机器人控制策略量化时关键感知/动作信息易损失的问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2505.15304">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
</tbody>
</table>
