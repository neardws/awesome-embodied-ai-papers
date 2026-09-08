# 实时执行

[首页](../../../README.zh-CN.md) | [英文](../../en/deployment/real-time.md) | [方向目录](README.md)

共 6 篇。

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
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=INsLvSCJ4z">Time Optimal Execution of Action Chunk Policies Beyond Demonstration Speed</a></td>
<td width="420">将动作块策略的执行时间优化到超过示教速度，同时保持动作可行性。</td>
<td width="240">实时执行</td>
<td width="280">时间最优执行</td>
<td width="280">机器人部署/评测环境</td>
<td width="280">动作块策略执行</td>
<td width="220">-</td>
<td width="360">解决动作块策略执行受示教速度限制的问题。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=INsLvSCJ4z">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=mIeKe74W43">Mean Flow Policy with Instantaneous Velocity Constraint for One-step Action Generation</a></td>
<td width="420">在均值流策略中加入瞬时速度约束，实现一步动作生成与可执行控制。</td>
<td width="240">实时执行</td>
<td width="280">单步动作生成 + 速度约束</td>
<td width="280">机器人部署/评测环境</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">解决流策略多步采样慢和速度约束缺失的问题。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=mIeKe74W43">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=r0RGJ1j9on">Real-Time Robot Execution with Masked Action Chunking</a></td>
<td width="420">用掩码动作分块支持机器人实时执行，减少块推理和控制不匹配。</td>
<td width="240">实时执行</td>
<td width="280">掩码动作分块</td>
<td width="280">机器人部署/评测环境</td>
<td width="280">实时机器人执行</td>
<td width="220">-</td>
<td width="360">解决动作分块策略在实时闭环执行中的延迟问题。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=r0RGJ1j9on">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://www.physicalintelligence.company/download/real_time_chunking.pdf">Real-Time Execution of Action Chunking Flow Policies</a></td>
<td width="420">Physical Intelligence 提出动作分块流策略的实时执行机制。</td>
<td width="240">实时执行</td>
<td width="280">实时</td>
<td width="280">机器人部署/评测环境</td>
<td width="280">-</td>
<td width="220">项目</td>
<td width="360">解决流策略生成动作块后如何低延迟稳定执行的问题。</td>
<td width="110" nowrap><a href="https://www.physicalintelligence.company/download/real_time_chunking.pdf">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://www.arxiv.org/abs/2505.10646">Accelerating Visual-Policy Learning through Parallel Differentiable Simulation</a></td>
<td width="420">用并行可微仿真加速视觉策略学习和训练反馈。</td>
<td width="240">并行可微仿真</td>
<td width="280">实时</td>
<td width="280">仿真</td>
<td width="280">-</td>
<td width="220">项目</td>
<td width="360">解决视觉策略真实/串行仿真训练慢的问题。</td>
<td width="110" nowrap><a href="https://www.arxiv.org/abs/2505.10646">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2508.00697">On-Device Diffusion Transformer Policy for Efficient Robot Manipulation</a></td>
<td width="420">通过剪枝/蒸馏把扩散 Transformer 策略部署到端侧实时机器人操作。</td>
<td width="240">实时执行</td>
<td width="280">时延 + 剪枝/蒸馏</td>
<td width="280">端侧/移动机器人硬件</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">解决扩散 Transformer 策略 在端侧设备延迟过高的问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2508.00697">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
</tbody>
</table>
