# 联合世界动作模型

[首页](../../../README.zh-CN.md) | [英文](../../en/wam/joint.md) | [方向目录](README.md)

共 3 篇。

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
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=IvUM6UwYCJ">Empowering Multi-Robot Cooperation via Sequential World Models</a></td>
<td width="420">SeqWM 用自回归逐智能体世界模型降低多机器人联合动力学建模复杂度。</td>
<td width="220">联合世界动作模型</td>
<td width="280">按智能体顺序建模的世界模型</td>
<td width="260">多智能体强化学习动作</td>
<td width="360">多机器人协作/规划</td>
<td width="200">仿真 + 实机</td>
<td width="360">解决物理多机器人合作中联合动力学复杂、MBRL 难扩展的问题。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=IvUM6UwYCJ">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/zhaozijie2022/seqwm-marl">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/64447">Dual-Stream Diffusion for World-Model Augmented Vision-Language-Action Model</a></td>
<td width="420">DUST 用双流扩散 Transformer 分别建模视觉和动作并跨模态共享信息。</td>
<td width="220">联合世界动作模型</td>
<td width="280">视觉词元 + 动作词元</td>
<td width="260">扩散/流匹配动作词元</td>
<td width="360">世界模型增强 VLA</td>
<td width="200">RoboCasa, GR-1, Franka Research 3</td>
<td width="360">解决 VLA 中联合预测状态和动作时视觉-动作模态差异带来的训练困难。</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/64447">论文</a></td>
<td width="110" nowrap><a href="https://periphanes.github.io/dust/">项目</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2507.11296">Diffusion-Based Imaginative Coordination for Bimanual Manipulation</a></td>
<td width="420">通过联合视频和动作扩散预测提升双臂操作协调。</td>
<td width="220">联合世界动作模型</td>
<td width="280">多帧潜在未来状态</td>
<td width="260">扩散动作预测</td>
<td width="360">双臂协调</td>
<td width="200">ALOHA + RoboTwin + 实机</td>
<td width="360">解决双臂操作高维动作空间和复杂协同导致策略学习困难的问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2507.11296">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/return-sleep/Diffusion_based_imaginative_Coordination">代码</a></td>
<td width="240">-</td>
</tr>
</tbody>
</table>
