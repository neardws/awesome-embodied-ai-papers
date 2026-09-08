# 安全性与鲁棒性

[首页](../../../README.zh-CN.md) | [英文](../../en/vla/safety-robustness.md) | [方向目录](README.md)

共 7 篇。

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
<td width="120" nowrap>NeurIPS 2024</td>
<td width="320"><a href="https://proceedings.neurips.cc/paper_files/paper/2024/hash/d83fd70a31c64e020844ec80705ba87f-Abstract-Conference.html">Diffusion Policy Attacker: Crafting Adversarial Attacks for Diffusion-based Policies</a></td>
<td width="420">DPA 研究针对扩散式机器人策略的对抗攻击。</td>
<td width="230">扩散策略</td>
<td width="240">连续动作</td>
<td width="300">VLA / 安全性与鲁棒性</td>
<td width="260">扩散策略攻击</td>
<td width="240">对抗鲁棒性评测</td>
<td width="200">机器人策略基准</td>
<td width="360">评测扩散式机器人策略的攻击面。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2405.19424">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=OwinX7PI83">BEAT: Visual Backdoor Attacks on VLM-based Embodied Agents via Contrastive Trigger Learning</a></td>
<td width="420">BEAT 利用对比触发器学习，为基于视觉语言模型的具身智能体构造视觉后门攻击。</td>
<td width="230">视觉语言模型具身智能体</td>
<td width="240">策略动作</td>
<td width="300">VLA / 安全性与鲁棒性</td>
<td width="260">对比触发器学习</td>
<td width="240">后门攻击评测</td>
<td width="200">具身智能体基准</td>
<td width="360">揭示具身视觉语言模型智能体的视觉后门风险。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2510.27623">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICRA 2025</td>
<td width="320"><a href="https://ieeexplore.ieee.org/document/11128017/">Run-time Observation Interventions Make Vision-Language-Action Models More Visually Robust</a></td>
<td width="420">BYOVLA 在运行时识别并编辑任务无关视觉区域，提升 Octo/OpenVLA 对视觉干扰的鲁棒性。</td>
<td width="230">Octo / OpenVLA</td>
<td width="240">自回归 / 策略动作</td>
<td width="300">VLA / 安全性与鲁棒性</td>
<td width="260">运行时观测干预</td>
<td width="240">鲁棒 VLA 执行</td>
<td width="200">真实机器人操作</td>
<td width="360">降低真实部署中无关视觉扰动导致的 VLA 失败。</td>
<td width="110" nowrap><a href="https://ieeexplore.ieee.org/document/11128017/">论文</a></td>
<td width="110" nowrap><a href="https://aasherh.github.io/byovla/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/irom-princeton/byovla">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=cS6xizdYD5">On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations</a></td>
<td width="420">研究视觉语言动作模型对多模态扰动的鲁棒性研究对多模态扰动、对抗输入或分布偏移下的 VLA 鲁棒性。</td>
<td width="230">π0 / OpenVLA</td>
<td width="240">扩散 / 流</td>
<td width="300">VLA / 安全 / 安全鲁棒</td>
<td width="260">RobustVLA；覆盖 4 种模态的 17 种扰动</td>
<td width="240">流策略</td>
<td width="200">LIBERO + 真实 FR5</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=cS6xizdYD5">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2503.03480">SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning</a></td>
<td width="420">SafeVLA 通过约束强化学习让 VLA 策略满足安全约束。</td>
<td width="230">SPOC</td>
<td width="240">自回归</td>
<td width="300">VLA / 安全性与鲁棒性</td>
<td width="260">采用约束学习的 PPO</td>
<td width="240">同策略 / 无模型</td>
<td width="200">仿真 ✓（单任务）</td>
<td width="360">在部署前提升 VLA 策略的安全对齐。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2503.03480">论文</a></td>
<td width="110" nowrap><a href="https://sites.google.com/view/pku-safevla">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2505.16640">BadVLA: Towards Backdoor Attacks on Vision-Language-Action Models via Objective-Decoupled Optimization</a></td>
<td width="420">研究 BadVLA 如何对 VLA 注入后门触发并影响机器人动作输出。</td>
<td width="230">未指定具体基座 VLA</td>
<td width="240">自回归</td>
<td width="300">VLA / 安全鲁棒</td>
<td width="260">目标解耦后门攻击</td>
<td width="240">-</td>
<td width="200">-</td>
<td width="360">构造并评估针对 VLA 机器人策略的后门攻击。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2505.16640">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2411.13587">Exploring the Adversarial Vulnerabilities of Vision-Language-Action Models in Robotics</a></td>
<td width="420">研究机器人视觉语言动作模型的对抗脆弱性研究对多模态扰动、对抗输入或分布偏移下的 VLA 鲁棒性。</td>
<td width="230">未指定具体基座 VLA</td>
<td width="240">自回归</td>
<td width="300">VLA / 安全鲁棒</td>
<td width="260">UADA / UPA / TMA 对抗攻击</td>
<td width="240">三维落地策略/感知</td>
<td width="200">仿真 + 实体设置</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2411.13587">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">LIBERO + BridgeData V2 攻击资源</td>
</tr>
</tbody>
</table>
