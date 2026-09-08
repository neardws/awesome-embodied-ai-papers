# quantization/cache/tokenization

[Home](../../../README.md) | [中文](../../zh-CN/deployment/quantization-cache-tokenization.md) | [Direction index](README.md)

Total: 22 papers.

<table width="3090">
<thead>
<tr>
<th width="120" nowrap>Venue/Year</th>
<th width="320">Paper/Method</th>
<th width="420">Abstract</th>
<th width="240">Object Type</th>
<th width="280">Efficiency Metric</th>
<th width="280">Platform/Hardware</th>
<th width="280">Covered Tasks</th>
<th width="220">Open Resource Status</th>
<th width="360">Paper Task/Goal</th>
<th width="110" nowrap>Paper</th>
<th width="110" nowrap>Project</th>
<th width="110" nowrap>Code</th>
<th width="240">Data/Bench</th>
</tr>
</thead>
<tbody>
<tr>
<td width="120" nowrap>CoRL 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2509.23655">Focusing on What Matters: Object-Agent-centric Tokenization for Vision Language Action models</a></td>
<td width="420">This work studies object-agent-centric tokenization for efficient VLA models.</td>
<td width="240">quantization/cache/tokenization</td>
<td width="280">deployment/evaluation coverage</td>
<td width="280">robot/simulator platform</td>
<td width="280">embodied robot tasks</td>
<td width="220">source-listed resource</td>
<td width="360">Add CoRL deployment/evaluation coverage.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2509.23655">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2509.05614">SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning</a></td>
<td width="420">Uses action-aware self-speculative pruning to accelerate VLA inference while preserving action quality.</td>
<td width="240">compression/cache/tokenization</td>
<td width="280">self-speculative pruning</td>
<td width="280">robot deployment/evaluation environment</td>
<td width="280">VLA manipulation</td>
<td width="220">-</td>
<td width="360">Addresses redundant computation in VLA action generation.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2509.05614">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>EMNLP 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2507.22424">Spec-VLA: Speculative Decoding for Vision-Language-Action Models with Relaxed Acceptance</a></td>
<td width="420">Applies relaxed speculative decoding to accelerate VLA action generation.</td>
<td width="240">compression/cache/tokenization</td>
<td width="280">speculative decoding</td>
<td width="280">robot deployment/evaluation environment</td>
<td width="280">VLA manipulation</td>
<td width="220">-</td>
<td width="360">Addresses slow autoregressive VLA decoding during robot execution.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2507.22424">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2024</td>
<td width="320"><a href="https://arxiv.org/abs/2411.02359">DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution</a></td>
<td width="420">Uses dynamic inference to reduce multimodal VLA computation during robot execution.</td>
<td width="240">compression/cache/tokenization</td>
<td width="280">dynamic inference</td>
<td width="280">robot deployment/evaluation environment</td>
<td width="280">robot execution</td>
<td width="220">Code</td>
<td width="360">Addresses unnecessary computation in multimodal VLA inference.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2411.02359">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/yueyang130/DeeR-VLA">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2024</td>
<td width="320"><a href="https://arxiv.org/abs/2406.04339">RoboMamba: Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation</a></td>
<td width="420">Uses a Mamba/state-space architecture to make VLA robot reasoning and manipulation more efficient.</td>
<td width="240">efficient architecture</td>
<td width="280">state-space model backbone</td>
<td width="280">robot deployment/evaluation environment</td>
<td width="280">robot reasoning and manipulation</td>
<td width="220">Project+Code</td>
<td width="360">Addresses Transformer efficiency bottlenecks in VLA policies.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2406.04339">paper</a></td>
<td width="110" nowrap><a href="https://sites.google.com/view/robomamba-web">project</a></td>
<td width="110" nowrap><a href="https://github.com/lmzpai/roboMamba">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=E1K2Ph3LtS">MetaVLA: Unified Meta Co-Training for Efficient Embodied Adaptation</a></td>
<td width="420">Uses meta co-training to merge multi-task adaptation into low-cost post-training, reducing VLA fine-tuning compute and improving LIBERO generalization.</td>
<td width="240">compression/cache/tokenization</td>
<td width="280">meta co-training</td>
<td width="280">robot deployment/evaluation environment</td>
<td width="280">LIBERO manipulation</td>
<td width="220">Code planned</td>
<td width="360">Addresses the high cost and weak generalization of VLA task adaptation.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=E1K2Ph3LtS">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=RwdGIIjPlC">SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration</a></td>
<td width="420">Uses action-aware model scheduling and spatiotemporal semantic token pruning to speed up VLA in LIBERO/SimplerEnv without performance loss.</td>
<td width="240">compression/cache/tokenization</td>
<td width="280">model scheduling + token pruning</td>
<td width="280">robot deployment/evaluation environment</td>
<td width="280">LIBERO, SimplerEnv</td>
<td width="220">-</td>
<td width="360">Addresses temporal and visual redundancy in VLA sequential decision-making.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=RwdGIIjPlC">paper</a> / <a href="https://arxiv.org/abs/2506.12723">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=TpL2nXanru">QVLA: Not All Channels Are Equal in Vision-Language-Action Model&#x27;s Quantization</a></td>
<td width="420">Proposes action-sensitive per-channel mixed-bit quantization to compress VLA to low memory while preserving success rate.</td>
<td width="240">compression/cache/tokenization</td>
<td width="280">channel-wise action-centric quantization/pruning</td>
<td width="280">resource-constrained robot hardware</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">Addresses why LLM-style uniform quantization is unsuitable for accumulated robot action errors.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=TpL2nXanru">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=ea6j8k8Rnw">Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation</a></td>
<td width="420">Dynamically adjusts the visual token retention rate based on recent action trajectories to reduce inference latency for long-horizon VLA manipulation.</td>
<td width="240">compression/cache/tokenization</td>
<td width="280">action-aware dynamic visual token pruning</td>
<td width="280">robot deployment/evaluation environment</td>
<td width="280">LIBERO + real-world manipulation</td>
<td width="220">-</td>
<td width="360">Addresses the mismatch between fixed pruning and phase-dependent visual redundancy during manipulation.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=ea6j8k8Rnw">paper</a> / <a href="https://arxiv.org/abs/2509.22093">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=k6nTUFoqeT">FASTer: Toward Powerful and Efficient Autoregressive Vision–Language–Action Models with Learnable Action Tokenizer and Block-wise Decoding</a></td>
<td width="420">Uses a learnable action tokenizer and block-wise decoding to improve action compression, speed, and task performance in autoregressive VLA.</td>
<td width="240">compression/cache/tokenization</td>
<td width="280">learnable action tokenizer + block-wise decoding</td>
<td width="280">robot deployment/evaluation environment</td>
<td width="280">sim+real manipulation</td>
<td width="220">-</td>
<td width="360">Addresses the tradeoff between reconstruction quality and inference efficiency in action tokenization.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=k6nTUFoqeT">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38880">FT-NCFM: An Influence-Aware Data Distillation Framework for Efficient VLA Models</a></td>
<td width="420">Uses causal attribution and adversarial NCFM to distill high-value VLA data, allowing a small coreset to approach full-data training performance.</td>
<td width="240">compression/cache/tokenization</td>
<td width="280">data distillation</td>
<td width="280">robot deployment/evaluation environment</td>
<td width="280">-</td>
<td width="220">Code+Data planned</td>
<td width="360">Addresses the high training cost caused by VLA reliance on large-scale redundant data.</td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38903">CronusVLA: Towards Efficient and Robust Manipulation via Multi-Frame Vision-Language-Action Modeling</a></td>
<td width="420">CronusVLA improves VLA manipulation robustness through multi-frame historical feature aggregation while controlling multi-frame inference cost.</td>
<td width="240">compression/cache/tokenization</td>
<td width="280">tokenization</td>
<td width="280">robot deployment/evaluation environment</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">Addresses the inability of single-frame VLA to use historical observations and the high latency of directly inputting multiple frames.</td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38904">SemanticVLA: Semantic-Aligned Sparsification and Enhancement for Efficient Robotic Manipulation</a></td>
<td width="420">Improves VLA manipulation efficiency and success rate through semantically aligned visual sparsification, hierarchical fusion, and action coupling.</td>
<td width="240">compression/cache/tokenization</td>
<td width="280">semantic-aligned sparsification</td>
<td width="280">robot deployment/evaluation environment</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">Addresses how visual redundancy and shallow instruction-vision alignment affect robot manipulation.</td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/JiuTian-VL/SemanticVLA">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38931">VLA-Adapter: An Effective Paradigm for Tiny-Scale Vision-Language-Action Model</a></td>
<td width="420">Uses a small-scale VLA adaptation paradigm to preserve robot manipulation ability at smaller model sizes.</td>
<td width="240">compression/cache/tokenization</td>
<td width="280">tiny-scale VLA adapter</td>
<td width="280">robot deployment/evaluation environment</td>
<td width="280">-</td>
<td width="220">Project+Code</td>
<td width="360">Addresses how tiny-scale VLA can be effectively adapted to manipulation tasks.</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38931">paper</a> / <a href="https://arxiv.org/abs/2509.09372">paper</a></td>
<td width="110" nowrap><a href="https://vla-adapter.github.io/">project</a></td>
<td width="110" nowrap><a href="https://github.com/OpenHelix-Team/VLA-Adapter">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38945">MoLe-VLA: Dynamic Layer-skipping Vision Language Action Model via Mixture-of-Layers for Efficient Robot Manipulation</a></td>
<td width="420">Uses mixture-of-layers dynamic layer skipping to reduce VLA compute while preserving manipulation success rate.</td>
<td width="240">compression/cache/tokenization</td>
<td width="280">dynamic layer skipping / up to 5.6x compute reduction</td>
<td width="280">robot deployment/evaluation environment</td>
<td width="280">-</td>
<td width="220">Project+Code</td>
<td width="360">Addresses the fact that different samples/steps in VLA inference do not need to pass through all layers.</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38945">paper</a> / <a href="https://arxiv.org/abs/2503.20384">paper</a></td>
<td width="110" nowrap><a href="https://sites.google.com/view/mole-vla">project</a></td>
<td width="110" nowrap><a href="https://github.com/RoyZry98/MoLe-VLA-Pytorch/">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2602.20309">QuantVLA: Scale-Calibrated Post-Training Quantization for Vision-Language-Action Models</a></td>
<td width="420">Proposes training-free PTQ quantization for the VLA language backbone and DiT action head, significantly saving memory.</td>
<td width="240">compression/cache/tokenization</td>
<td width="280">PTQ</td>
<td width="280">compute/memory/power constrained deployment</td>
<td width="280">-</td>
<td width="220">Project+Code</td>
<td width="360">Addresses quantization for large VLA models under low-compute/low-power deployment.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2602.20309">paper</a></td>
<td width="110" nowrap><a href="https://quantvla.github.io/">project</a></td>
<td width="110" nowrap><a href="https://github.com/AIoT-MLSys-Lab/QuantVLA">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2506.06072">BEAST: Efficient Tokenization of B-Splines Encoded Action Sequences for Imitation Learning</a></td>
<td width="420">Encodes action sequences as fixed-length tokens with B-splines, avoiding separate tokenizer training and generating smooth high-frequency control.</td>
<td width="240">compression/cache/tokenization</td>
<td width="280">B-spline action tokenizer</td>
<td width="280">robot deployment/evaluation environment</td>
<td width="280">166 sim tasks + 8 real tasks</td>
<td width="220">-</td>
<td width="360">Addresses the cost of action-sequence tokenization in imitation learning and the need for trajectory smoothness.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2506.06072">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2503.14259">Quantization-Free Autoregressive Action Transformer</a></td>
<td width="420">Uses a continuous infinite-vocabulary Transformer to model actions directly, avoiding damage to action-space structure from discrete quantization.</td>
<td width="240">continuous autoregressive action modeling</td>
<td width="280">quantization-free continuous autoregressive action modeling</td>
<td width="280">robot deployment/evaluation environment</td>
<td width="280">Reduce model deployment cost.</td>
<td width="220">Code</td>
<td width="360">Addresses how discrete action codes limit continuous control in autoregressive imitation learning.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2503.14259">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2506.10100">EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models</a></td>
<td width="420">Achieves training-free VLA acceleration and compression through language-layer pruning, visual token selection, and diffusion feature caching.</td>
<td width="240">compression/cache/tokenization</td>
<td width="280">layer pruning + visual token selection + diffusion cache</td>
<td width="280">robot deployment/evaluation environment</td>
<td width="280">CogACT/SIMPLER</td>
<td width="220">-</td>
<td width="360">Addresses redundancy across language, vision, and action-head components in the VLA pipeline.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2506.10100">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2502.02175">VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching</a></td>
<td width="420">Adaptively reuses the KV cache of static visual tokens in adjacent frames to improve VLA control frequency.</td>
<td width="240">compression/cache/tokenization</td>
<td width="280">adaptive visual token KV caching</td>
<td width="280">robot deployment/evaluation environment</td>
<td width="280">LIBERO, SIMPLER, real robot</td>
<td width="220">Project+Code</td>
<td width="360">Addresses repeated per-frame visual computation in real-time robot control.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2502.02175">paper</a></td>
<td width="110" nowrap><a href="https://vla-cache.github.io/">project</a></td>
<td width="110" nowrap><a href="https://github.com/siyuhsu/vla-cache">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2507.01016">VQ-VLA: Improving Vision-Language-Action Models via Scaling Vector-Quantized Action Tokenizers</a></td>
<td width="420">Trains a VQ action tokenizer on large-scale synthetic/real trajectories to improve VLA inference speed and long-horizon action quality.</td>
<td width="240">compression/cache/tokenization</td>
<td width="280">vector-quantized action tokenizer</td>
<td width="280">robot deployment/evaluation environment</td>
<td width="280">-</td>
<td width="220">Project+Code</td>
<td width="360">Addresses insufficient data scale and weak generalization for action tokenizers.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2507.01016">paper</a></td>
<td width="110" nowrap><a href="https://xiaoxiao0406.github.io/vqvla.github.io">project</a> / <a href="https://xiaoxiao0406.github.io/vqvla.github.io/">project</a></td>
<td width="110" nowrap><a href="https://github.com/xiaoxiao0406/VQ-VLA">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2505.15304">Saliency-Aware Quantized Imitation Learning for Efficient Robotic Control</a></td>
<td width="420">Uses saliency-aware quantization to compress imitation learning policies, balancing efficient control and task performance.</td>
<td width="240">compression/cache/tokenization</td>
<td width="280">saliency-aware quantized imitation learning</td>
<td width="280">robot deployment/evaluation environment</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">Addresses the loss of key perception/action information when quantizing robot control policies.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2505.15304">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
</tbody>
</table>
