# 三维空间落地

[首页](../../../README.zh-CN.md) | [英文](../../en/vla/3d-grounding.md) | [方向目录](README.md)

共 41 篇。

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
<td width="120" nowrap>CoRL 2023</td>
<td width="320"><a href="https://arxiv.org/abs/2311.05779">Language-guided Robot Grasping: CLIP-based Referring Grasp Synthesis in Clutter (CROG)</a></td>
<td width="420">在杂乱场景中定位语言指代目标，并预测俯视二指抓取。</td>
<td width="230">CLIP 指代分割</td>
<td width="240">4 自由度抓取 [x,y,偏航角,宽度]</td>
<td width="300">OCID-VLG：1,763 个 RGB-D 场景、75K 抓取矩形、89.6K 语言—掩码—抓取样本；Gazebo + 实机</td>
<td width="260">联合语言分割与抓取生成</td>
<td width="240">语言落地 + 平行夹爪抓取；不是灵巧手控制</td>
<td width="200">Gazebo + 实机</td>
<td width="360">仿真落地/任务成功：孤立场景 76/62%，杂乱场景 60/42%；实机 65/23.9% 与 60/20%</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2311.05779">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/HilbertXu/CROG">代码</a></td>
<td width="240">OCID-VLG</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=RYwQ0xQcAh">Interaction-aware Representation Modeling With Co-Occurrence Consistency for Egocentric Hand-Object Parsing (InterFormer)</a></td>
<td width="420">从第一视角 RGB 解析手与交互物体，并减少不合理的手—物共现。</td>
<td width="230">-</td>
<td width="240">二维手/物分割掩码；仅感知</td>
<td width="300">EgoHOS：8,993 训练/1,124 验证/1,126 域内/500 分布外；mini-HOI4D：1,095 张图</td>
<td width="260">交互感知分割 + 共现一致性</td>
<td width="240">第一视角人—物交互落地；没有机器人、三维动作或控制</td>
<td width="200">离线真实图像；无仿真器</td>
<td width="360">EgoHOS 域内/分布外 mIoU 73.22/72.82%；mini-HOI4D 66.07%；交互错觉率 2.19→1.55%</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=RYwQ0xQcAh">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/yuggiehk/InterFormer">代码</a></td>
<td width="240">EgoHOS / mini-HOI4D</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38873">GRIM: Task-Oriented Grasping with Conditioning on Generative Examples</a></td>
<td width="420">检索任务导向抓取示例，并把功能抓取几何迁移到新场景物体。</td>
<td width="230">AnyGrasp 候选 + 生成/网页/人类示例</td>
<td width="240">6 自由度二指抓取位姿</td>
<td width="300">无物理训练；记忆 210 例（180 生成帧 + 15 网页 + 15 人类）；TaskGrasp 离线 + 实机</td>
<td width="260">手物重建 + 语义三维对齐/ICP + 抓取重排</td>
<td width="240">任务导向平行夹爪抓取检索</td>
<td width="200">离线基准 + 实机；无仿真器</td>
<td width="360">TaskGrasp 全部/留出物体/留出任务的平均精度均值 0.67/0.65/0.64；Kinova Gen3 Lite 实机 39/50 = 78%</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38873">论文</a></td>
<td width="110" nowrap><a href="https://grim-tog.github.io/">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">210 个样例的记忆库 / TaskGrasp</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38940">GraphGrasp: Lightweight and Efficient Graph-Guided 6-DoF Robotic Grasp Pose Estimation Network</a></td>
<td width="420">用图引导点云推理，在杂乱场景预测高效 6 自由度双接触抓取。</td>
<td width="230">-</td>
<td width="240">旋转 + 平移 + 平行夹爪开口宽度</td>
<td width="300">GraspNet-1Billion 的 RealSense 划分：190 场景×256 视角；输入 15K 点；无物理仿真器</td>
<td width="260">场景/物体/抓取图 + 力闭合与碰撞评分</td>
<td width="240">点云 6 自由度平行夹爪抓取估计</td>
<td width="200">离线基准 + 实机</td>
<td width="360">已见/相似/新物体平均精度 64.88/56.91/24.83；3.2M 参数；UR3 实机平均抓取成功 92.1%（试次数未披露）</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38940">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/BIT-robot-group/GraphGrasp">代码</a></td>
<td width="240">GraspNet-1Billion</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38957">Effective Robotic Cloth Grasping Through Suppressing False Discoveries</a></td>
<td width="420">抑制服装分割误发现，并结合深度褶皱定位可靠抓取点。</td>
<td width="230">-</td>
<td width="240">单 RGB-D 抓取点 + 垂直平行夹取</td>
<td width="300">无仿真；7 件服装；640 训练/440 验证 RGB 场景；50 次实机整堆收纳测试</td>
<td width="260">无监督 RGB 分割 + 误检抑制 + 深度褶皱抓点评分</td>
<td width="240">服装感知/抓取点落地；Baxter 夹爪，不是灵巧手</td>
<td width="200">仅实机</td>
<td width="360">分割 mFDR 0%；抓取/整堆收纳成功 94%；相对三种分割基线 +20/+14/+28 个百分点</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38957">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">7-服装 RGB-D 数据</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://cvpr.thecvf.com/virtual/2025/poster/32440">ZeroGrasp: Zero-Shot Shape Reconstruction Enabled Robotic Grasping</a></td>
<td width="420">联合单视图形状重建、遮挡/空间推理和 6 自由度抓取预测。</td>
<td width="230">ZeroGrasp 重建 + 抓取网络</td>
<td width="240">6 自由度 Robotiq 2F-85 平行夹爪抓取</td>
<td width="300">ZeroGrasp-11B arXiv 版：1M RGB-D、12K Objaverse-LVIS 物体、11.3B 物理有效抓取；Isaac Gym 标注/筛选</td>
<td width="260">三维形状重建 + 空间关系推理 + 抓取位姿估计</td>
<td width="240">零样本平行夹爪抓取；不是灵巧手控制</td>
<td width="200">Isaac Gym 标注验证 + 实机</td>
<td width="360">GraspNet 已见/相似/新物体平均精度 70.53/62.51/26.46；预训练+FT 72.43/65.45/28.49；实机 75%，基线 56.25%</td>
<td width="110" nowrap><a href="https://cvpr.thecvf.com/virtual/2025/poster/32440">论文</a></td>
<td width="110" nowrap><a href="https://sh8.io/#/zerograsp">项目</a></td>
<td width="110" nowrap><a href="https://github.com/sh8/ZeroGrasp">代码</a></td>
<td width="240">ZeroGrasp-11B（CVPR 页面为 8.9B；arXiv 为 11.3B 条标注）</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2023</td>
<td width="320"><a href="https://arxiv.org/abs/2308.07931">Distilled Feature Fields Enable Few-Shot Language-Guided Manipulation</a></td>
<td width="420">F3RM 利用蒸馏特征场，实现少样本语言引导操作。</td>
<td width="230">Distilled Feature Fields Enable Few-Shot Language-Guided Manipulation</td>
<td width="240">机器人动作</td>
<td width="300">VLA / 三维空间落地</td>
<td width="260">CoRL 机器人学习方法</td>
<td width="240">机器人策略</td>
<td width="200">机器人基准</td>
<td width="360">补充 CoRL VLA 研究覆盖。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2308.07931">论文</a></td>
<td width="110" nowrap><a href="https://f3rm.github.io">项目</a></td>
<td width="110" nowrap><a href="https://github.com/f3rm/f3rm">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2023</td>
<td width="320"><a href="https://arxiv.org/abs/2306.14896">RVT: Robotic View Transformer for 3D Object Manipulation</a></td>
<td width="420">RVT 利用视图 Transformer 表示完成三维物体操作。</td>
<td width="230">RVT</td>
<td width="240">机器人动作</td>
<td width="300">VLA / 三维空间落地</td>
<td width="260">CoRL 机器人学习方法</td>
<td width="240">机器人策略</td>
<td width="200">机器人基准</td>
<td width="360">补充 CoRL VLA 研究覆盖。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2306.14896">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2022</td>
<td width="320"><a href="https://arxiv.org/abs/2209.05451">Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation</a></td>
<td width="420">PerAct 利用 Perceiver 式三维表示完成多任务操作。</td>
<td width="230">Perceiver-Actor</td>
<td width="240">机器人动作</td>
<td width="300">VLA / 三维空间落地</td>
<td width="260">CoRL 机器人学习方法</td>
<td width="240">机器人策略</td>
<td width="200">机器人基准</td>
<td width="360">补充 CoRL VLA 研究覆盖。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2209.05451">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2023</td>
<td width="320"><a href="https://arxiv.org/abs/2306.17817">Act3D: 3D Feature Field Transformers for Multi-Task Robotic Manipulation</a></td>
<td width="420">Act3D 构建三维特征场 Transformer，用于多任务机器人操作。</td>
<td width="230">Act3D</td>
<td width="240">机器人动作</td>
<td width="300">VLA / 三维空间落地</td>
<td width="260">CoRL 机器人学习方法</td>
<td width="240">机器人策略</td>
<td width="200">机器人基准</td>
<td width="360">补充 CoRL VLA 研究覆盖。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2306.17817">论文</a></td>
<td width="110" nowrap><a href="https://act3d.github.io">项目</a></td>
<td width="110" nowrap><a href="https://github.com/zhouxian/act3d-chained-diffuser">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2024</td>
<td width="320"><a href="https://proceedings.mlr.press/v235/zhen24a.html">3D-VLA: A 3D Vision-Language-Action Generative World Model</a></td>
<td width="420">3D-VLA 为视觉语言动作操作构建三维生成式世界模型。</td>
<td width="230">三维 VLA</td>
<td width="240">三维落地动作</td>
<td width="300">三维空间落地 / 世界模型</td>
<td width="260">三维生成式世界建模</td>
<td width="240">三维 VLA 策略</td>
<td width="200">机器人操作基准</td>
<td width="360">利用三维世界表示为 VLA 动作生成提供空间依据。</td>
<td width="110" nowrap><a href="https://proceedings.mlr.press/v235/zhen24a/zhen24a.pdf">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>IROS 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2606.26800">SSI-Policy: Learning Structured Scene Interfaces for Vision-Language Robotic Manipulation</a></td>
<td width="420">SSI-Policy 用结构化场景接口连接视觉语言推理和低数据机器人操作策略学习。</td>
<td width="230">视觉语言策略</td>
<td width="240">连续动作</td>
<td width="300">三维空间落地 / 结构化场景接口</td>
<td width="260">场景接口策略学习</td>
<td width="240">结构化 VLA 策略</td>
<td width="200">真实机器人操作</td>
<td width="360">用结构化场景表示提升低数据机器人操作泛化。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2606.26800">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICRA 2025</td>
<td width="320"><a href="https://kalie-vlm.github.io/">KALIE: Fine-Tuning Vision-Language Models for Open-World Manipulation without Robot Data</a></td>
<td width="420">KALIE 用视觉语言模型预测语言条件点式可供性，通过合成数据支持开放世界机器人操作。</td>
<td width="230">视觉语言模型</td>
<td width="240">可供性点</td>
<td width="300">三维空间落地 / 可供性落地</td>
<td width="260">合成数据微调</td>
<td width="240">以可供性为条件的操作</td>
<td width="200">真实机器人操作</td>
<td width="360">不用真实机器人数据学习语言条件可供性。</td>
<td width="110" nowrap><a href="https://kalie-vlm.github.io/">论文</a></td>
<td width="110" nowrap><a href="https://kalie-vlm.github.io/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/gractang/kalie">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=7M6ryCABIc">PixelVLA: Advancing Pixel-level Understanding in Vision-Language-Action Model</a></td>
<td width="420">提出 PixelVLA，把三维几何、空间定位或可供性先验接入机器人感知与操作。</td>
<td width="230">未指定具体基座 VLA</td>
<td width="240">三维/空间落地</td>
<td width="300">三维表示 / 三维空间落地</td>
<td width="260">-</td>
<td width="240">三维落地策略/感知</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=7M6ryCABIc">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=eKhOrQWAVJ">Spatially Guided Training for Vision-Language-Action Model</a></td>
<td width="420">提出 Spatially Guided Training，把三维几何、空间定位或可供性先验接入机器人感知与操作。</td>
<td width="230">未指定具体基座 VLA</td>
<td width="240">三维/空间落地</td>
<td width="300">三维表示 / 三维空间落地</td>
<td width="260">三维/空间表示学习</td>
<td width="240">三维落地策略/感知</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=eKhOrQWAVJ">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=euMVC1DO4k">Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model</a></td>
<td width="420">提出 Spatial Forcing，把三维几何、空间定位或可供性先验接入机器人感知与操作。</td>
<td width="230">未指定具体基座 VLA</td>
<td width="240">三维/空间落地</td>
<td width="300">三维表示 / 三维空间落地</td>
<td width="260">三维/空间表示学习</td>
<td width="240">三维落地策略/感知</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=euMVC1DO4k">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=fzmittHfq3">From Spatial to Actions: Grounding Vision-Language-Action Model in Spatial Foundation Priors</a></td>
<td width="420">提出 From Spatial to Actions，把三维几何、空间定位或可供性先验接入机器人感知与操作。</td>
<td width="230">未指定具体基座 VLA</td>
<td width="240">三维/空间落地</td>
<td width="300">三维表示 / 三维空间落地</td>
<td width="260">三维/空间表示学习</td>
<td width="240">三维落地策略/感知</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=fzmittHfq3">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=18gC6pZVVc">Geometry-aware 4D Video Generation for Robot Manipulation</a></td>
<td width="420">提出几何感知四维视频生成，利用视频生成/预测或未来渲染学习机器人交互动态。</td>
<td width="230">-</td>
<td width="240">自回归</td>
<td width="300">三维表示 / 三维空间落地</td>
<td width="260">三维/空间表示学习</td>
<td width="240">三维落地策略/感知</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=18gC6pZVVc">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=WXFfMLyB6y">Generalizable Coarse-to-Fine Robot Manipulation via Language-Aligned 3D Keypoints</a></td>
<td width="420">提出 Generalizable Coarse-to-Fine Robot Manipulation，把三维几何、空间定位或可供性先验接入机器人感知与操作。</td>
<td width="230">-</td>
<td width="240">自回归</td>
<td width="300">三维表示 / 三维空间落地</td>
<td width="260">三维关键点落地</td>
<td width="240">三维落地策略/感知</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=WXFfMLyB6y">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=ggofj6tyr3">Geometry-aware Policy Imitation</a></td>
<td width="420">提出几何感知策略模仿，把三维几何、空间定位或可供性先验接入机器人感知与操作。</td>
<td width="230">-</td>
<td width="240">自回归</td>
<td width="300">三维表示 / 三维空间落地</td>
<td width="260">扩散策略</td>
<td width="240">扩散策略</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=ggofj6tyr3">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=qXfRXfAHOK">PA3FF:Learning Part-Aware Dense 3D Feature Field For Generalizable Articulated Object Manipulation</a></td>
<td width="420">提出 PA3FF，把三维几何、空间定位或可供性先验接入机器人感知与操作。</td>
<td width="230">-</td>
<td width="240">自回归</td>
<td width="300">三维表示 / 三维空间落地</td>
<td width="260">扩散策略</td>
<td width="240">扩散策略</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=qXfRXfAHOK">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=z8BN7KyaPl">RAVEN: End-to-end Equivariant Robot Learning with RGB Cameras</a></td>
<td width="420">提出 RAVEN，把三维几何、空间定位或可供性先验接入机器人感知与操作。</td>
<td width="230">-</td>
<td width="240">自回归</td>
<td width="300">三维表示 / 三维空间落地</td>
<td width="260">三维/空间表示学习</td>
<td width="240">三维落地策略/感知</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=z8BN7KyaPl">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=DE5ZJtR4bg">On the Generalization Capacities of MLLMs for Spatial Intelligence</a></td>
<td width="420">提出多模态大语言模型泛化能力研究，把三维几何、空间定位或可供性先验接入机器人感知与操作。</td>
<td width="230">-</td>
<td width="240">三维/空间落地</td>
<td width="300">三维表示 / 三维空间落地</td>
<td width="260">三维/空间表示学习</td>
<td width="240">三维落地策略/感知</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=DE5ZJtR4bg">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38921">ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver</a></td>
<td width="420">ReconVLA 通过重建目标注视区域来提升视觉-语言-动作机器人策略的视觉落地。</td>
<td width="230">未指定具体基座 VLA</td>
<td width="240">三维/空间落地</td>
<td width="300">三维表示 / 三维空间落地</td>
<td width="260">-</td>
<td width="240">三维落地策略/感知</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38921">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38939">Indoor Multi-View Radar Object Detection via 3D Bounding Box Diffusion</a></td>
<td width="420">REXO 将基于扩散的三维边界框引入多视角雷达感知，用于室内目标检测。</td>
<td width="230">-</td>
<td width="240">自回归 / 扩散 / 流</td>
<td width="300">三维表示 / 扩散与流策略</td>
<td width="260">扩散策略</td>
<td width="240">扩散策略</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38939">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38946">RaLD: Generating High-Resolution 3D Radar Point Clouds with Latent Diffusion</a></td>
<td width="420">RaLD 使用潜在扩散生成更密集、更高分辨率的三维雷达点云。</td>
<td width="230">-</td>
<td width="240">自回归 / 扩散 / 流</td>
<td width="300">三维表示 / 扩散与流策略</td>
<td width="260">扩散策略</td>
<td width="240">扩散策略</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38946">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38947">Grounding Actions in Camera Space: Observation-Centric Vision-Language-Action Policy</a></td>
<td width="420">OC-VLA 在相机坐标中预测动作，以降低 VLA 策略中的观测-动作空间不一致。</td>
<td width="230">未指定具体基座 VLA</td>
<td width="240">三维/空间落地</td>
<td width="300">三维表示 / 三维空间落地</td>
<td width="260">-</td>
<td width="240">三维落地策略/感知</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38947">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2510.24261">DynaRend: Learning 3D Dynamics via Masked Future Rendering for Robotic Manipulation</a></td>
<td width="420">提出 DynaRend，利用视频生成/预测或未来渲染学习机器人交互动态。</td>
<td width="230">-</td>
<td width="240">自回归</td>
<td width="300">三维表示 / 三维空间落地</td>
<td width="260">生成式动作建模</td>
<td width="240">三维落地策略/感知</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2510.24261">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://neurips.cc/virtual/2025/loc/san-diego/poster/118141">Building 3D Representations and Generating Motions From a Single Image via Video-Generation</a></td>
<td width="420">VGER 从单张 RGB 图像生成视频来构建三维场景表示，用于无碰撞运动生成。</td>
<td width="230">-</td>
<td width="240">-</td>
<td width="300">三维表示 / 三维空间落地</td>
<td width="260">-</td>
<td width="240">-</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://neurips.cc/virtual/2025/loc/san-diego/poster/118141">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2504.12636">A0: An Affordance-Aware Hierarchical Model for General Robotic Manipulation</a></td>
<td width="420">提出 A0，把三维几何、空间定位或可供性先验接入机器人感知与操作。</td>
<td width="230">-</td>
<td width="240">自回归</td>
<td width="300">VLA / 可供性 / 三维空间落地</td>
<td width="260">流匹配策略</td>
<td width="240">流策略</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2504.12636">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2408.10123v1">Learning Precise Affordances from Egocentric Videos for Robotic Manipulation</a></td>
<td width="420">提出从第一视角视频学习精确可供性，把三维几何、空间定位或可供性先验接入机器人感知与操作。</td>
<td width="230">-</td>
<td width="240">自回归</td>
<td width="300">可供性 / 三维空间落地</td>
<td width="260">可供性落地</td>
<td width="240">三维落地策略/感知</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2408.10123v1">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2412.04380">EmbodiedOcc: Embodied 3D Occupancy Prediction for Vision-based Online Scene Understanding</a></td>
<td width="420">提出 EmbodiedOcc，把三维几何、空间定位或可供性先验接入机器人感知与操作。</td>
<td width="230">-</td>
<td width="240">三维/空间落地</td>
<td width="300">三维表示 / 强化学习/在线微调</td>
<td width="260">三维/空间表示学习</td>
<td width="240">三维落地策略/感知</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2412.04380">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2504.08531">Embodied Image Captioning: Self-supervised Learning Agents for Spatially Coherent Image Descriptions</a></td>
<td width="420">提出 Embodied Image Captioning，把三维几何、空间定位或可供性先验接入机器人感知与操作。</td>
<td width="230">-</td>
<td width="240">自回归</td>
<td width="300">三维空间落地</td>
<td width="260">三维/空间表示学习</td>
<td width="240">三维落地策略/感知</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2504.08531">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2503.10745">Unifying 2D and 3D Vision-Language Understanding</a></td>
<td width="420">提出统一二维与三维视觉语言理解，把三维几何、空间定位或可供性先验接入机器人感知与操作。</td>
<td width="230">-</td>
<td width="240">三维/空间落地</td>
<td width="300">三维表示 / 三维空间落地</td>
<td width="260">-</td>
<td width="240">三维落地策略/感知</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2503.10745">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2505.04119">GAPrompt: Geometry-Aware Point Cloud Prompt for 3D Vision Model</a></td>
<td width="420">提出 GAPrompt，把三维几何、空间定位或可供性先验接入机器人感知与操作。</td>
<td width="230">-</td>
<td width="240">自回归</td>
<td width="300">三维表示 / 三维空间落地</td>
<td width="260">三维/空间表示学习</td>
<td width="240">三维落地策略/感知</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2505.04119">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2412.00174">SOLAMI: Social Vision-Language-Action Modeling for Immersive Interaction with 3D Autonomous Characters</a></td>
<td width="420">提出 SOLAMI，把三维几何、空间定位或可供性先验接入机器人感知与操作。</td>
<td width="230">未指定具体基座 VLA</td>
<td width="240">自回归</td>
<td width="300">VLA / 三维表示 / 三维空间落地</td>
<td width="260">-</td>
<td width="240">三维落地策略/感知</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2412.00174">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2501.03841">OmniManip: Towards General Robotic Manipulation via Object-Centric Interaction Primitives as Spatial Constraints</a></td>
<td width="420">提出 OmniManip，把三维几何、空间定位或可供性先验接入机器人感知与操作。</td>
<td width="230">未指定具体基座 VLA</td>
<td width="240">自回归</td>
<td width="300">VLA / 三维空间落地</td>
<td width="260">可供性落地</td>
<td width="240">三维落地策略/感知</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2501.03841">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/pdf/2504.21530">RoboGround: Robot Manipulation with Grounded Vision-Language Priors</a></td>
<td width="420">RoboGround 将视觉-语言落地掩码作为中间空间先验，用于可泛化的操作策略。</td>
<td width="230">-</td>
<td width="240">-</td>
<td width="300">VLA / 三维空间落地</td>
<td width="260">-</td>
<td width="240">-</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2406.18158">3D-MVP: 3D Multiview Pretraining for Robotic Manipulation</a></td>
<td width="420">提出 3D-MVP，把三维几何、空间定位或可供性先验接入机器人感知与操作。</td>
<td width="230">-</td>
<td width="240">三维/空间落地</td>
<td width="300">三维表示 / 三维空间落地</td>
<td width="260">生成式动作建模</td>
<td width="240">三维落地策略/感知</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2406.18158">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2503.07135">VidBot: Learning Generalizable 3D Actions from In-the-Wild 2D Human Videos for Zero-Shot Robotic Manipulation</a></td>
<td width="420">提出 VidBot，把三维几何、空间定位或可供性先验接入机器人感知与操作。</td>
<td width="230">-</td>
<td width="240">自回归</td>
<td width="300">三维表示 / 三维空间落地</td>
<td width="260">扩散策略</td>
<td width="240">扩散策略</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2503.07135">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2412.05507">AutoURDF: Unsupervised Robot Modeling from Point Cloud Frames Using Cluster Registration</a></td>
<td width="420">提出 AutoURDF，把三维几何、空间定位或可供性先验接入机器人感知与操作。</td>
<td width="230">-</td>
<td width="240">三维/空间落地</td>
<td width="300">三维空间落地</td>
<td width="260">三维/空间表示学习</td>
<td width="240">三维落地策略/感知</td>
<td width="200">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2412.05507">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
</tbody>
</table>
