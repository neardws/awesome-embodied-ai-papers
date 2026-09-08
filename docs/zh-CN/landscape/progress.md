# 关键进展与共性瓶颈

[首页](../../../README.zh-CN.md) | [英文](../../en/landscape/progress.md) | [全景目录](README.md)

以下观察归纳所列研究与产业示例，不是市场规模估计、普遍成熟度结论或企业排名。每行把已有能力与走向实际部署仍需要的证据连接起来。

<table width="1960">
<thead>
<tr>
<th width="240" nowrap>主题</th>
<th width="440">示例已能说明什么</th>
<th width="440">仍未解决的问题</th>
<th width="440">下一步应保留的证据</th>
<th width="400">原始示例来源</th>
</tr>
</thead>
<tbody>
<tr>
<td width="240" nowrap>可获得的本体与可复现研究</td>
<td width="440">开放本体、研究型机械臂和商业人形已有不同形式的设计或产品入口。</td>
<td width="440">可获得硬件仍不等于通用任务能力；个体差异、散热和维护会影响复现。</td>
<td width="440">在明确配置与任务上报告成功、故障、维修和重复试验。</td>
<td width="400"><a href="https://toddlerbot.github.io/">ToddlerBot（斯坦福大学）</a> · <a href="https://www.unitree.com/g1/">宇树 G1</a> · <a href="https://franka.de/franka-research-3">Franka Research 3</a></td>
</tr>
<tr>
<td width="240" nowrap>动作学习与基础策略</td>
<td width="440">扩散策略与视觉语言动作模型提供了可研究的动作生成路线。</td>
<td width="440">跨场景、长时程和真实异常恢复不能由单一演示证明。</td>
<td width="440">对齐训练数据、机器人配置、未见条件及人工介入预算。</td>
<td width="400"><a href="https://diffusion-policy.cs.columbia.edu/">Diffusion Policy 研究团队</a> · <a href="https://openvla.github.io/">OpenVLA 联合研究团队</a> · <a href="https://www.pi.website/blog/pi0">Physical Intelligence / π0</a></td>
</tr>
<tr>
<td width="240" nowrap>世界预测与可执行规划</td>
<td width="440">世界模型、语言技能规划和空间价值表示分别提供闭环中的不同能力。</td>
<td width="440">预测看起来合理，不代表动作满足物理约束或能可靠恢复。</td>
<td width="440">比较有无该模块时的任务收益、错误预测与失败恢复。</td>
<td width="400"><a href="https://danijar.com/project/daydreamer/">DayDreamer 研究团队</a> · <a href="https://say-can.github.io/">SayCan 研究团队</a> · <a href="https://voxposer.github.io/">VoxPoser 研究团队</a></td>
</tr>
<tr>
<td width="240" nowrap>数据工具链与跨本体复用</td>
<td width="440">多机构数据集、便携示教与开源工具链形成互补的数据入口。</td>
<td width="440">数据量无法替代动作语义、时间同步、授权和分布覆盖。</td>
<td width="440">记录数据版本、来源、隔离划分和新增真实任务收益。</td>
<td width="400"><a href="https://robotics-transformer-x.github.io/">Open X-Embodiment 协作组</a> · <a href="https://droid-dataset.github.io/">DROID 多机构团队</a> · <a href="https://umi-gripper.github.io/">UMI 研究团队</a> · <a href="https://huggingface.co/docs/lerobot/index">Hugging Face / LeRobot</a> · <a href="https://github.com/OpenDriveLab/AgiBot-World">AgiBot World / OpenDriveLab</a></td>
</tr>
<tr>
<td width="240" nowrap>仿真与评测基础设施</td>
<td width="440">物理引擎、训练框架与双臂任务生成工具支持更可控的实验。</td>
<td width="440">接触、传感与资产误差仍需真实验证；合成指标不能替代实机指标。</td>
<td width="440">固定仿真版本、随机化范围、真实校准与迁移测试条件。</td>
<td width="400"><a href="https://mujoco.org/">MuJoCo / Google DeepMind</a> · <a href="https://isaac-sim.github.io/IsaacLab/main/index.html">NVIDIA Isaac Lab</a> · <a href="https://robotwin-platform.github.io/">RoboTwin 联合团队</a> · <a href="https://www.lightwheel.ai/">光轮智能</a></td>
</tr>
<tr>
<td width="240" nowrap>硬件接触与触觉学习</td>
<td width="440">研究灵巧手、商品化末端和触觉器件提供不同接触能力。</td>
<td width="440">更多自由度或触点不自动带来更好的控制；还受耐久、标定和数据约束。</td>
<td width="440">比较感知增益、任务效果、控制延迟和更换维护成本。</td>
<td width="400"><a href="https://arxiv.org/abs/2309.06440">LEAP Hand 研究团队</a> · <a href="https://shadowrobot.com/dexterous-hand-series/">Shadow Robot 灵巧手</a> · <a href="https://www.gelsight.com/product/digit-tactile-sensor/">GelSight DIGIT</a> · <a href="https://www.inspire-robots.com/">因时机器人</a></td>
</tr>
<tr>
<td width="240" nowrap>软件接口与运营闭环</td>
<td width="440">控制、导航、操作、机队和数据工具分别覆盖系统集成环节。</td>
<td width="440">接口存在不等于系统互通；版本、时序、故障语义仍须逐项验证。</td>
<td width="440">保留部署配置、端到端测试、故障注入和回滚记录。</td>
<td width="400"><a href="https://github.com/ros-controls/ros2_control">ros2_control 社区</a> · <a href="https://moveit.ai/">MoveIt / PickNik</a> · <a href="https://docs.nav2.org/rolling/">Nav2 社区</a> · <a href="https://www.open-rmf.org/">Open-RMF 社区</a> · <a href="https://foxglove.dev/">Foxglove</a></td>
</tr>
<tr>
<td width="240" nowrap>现场价值与规模交付</td>
<td width="440">运营方披露的物流案例说明了具体任务与商业交付之间的连接。</td>
<td width="440">单个场地案例不能代表全行业成熟；维护、改造和停机成本须纳入。</td>
<td width="440">同时记录任务周期、可用时长、介入、故障恢复和完整成本。</td>
<td width="400"><a href="https://investors.gxo.com/news-releases/news-release-details/gxo-signs-industry-first-multi-year-agreement-agility-robotics">GXO / Agility Robotics</a> · <a href="https://www.protolabs.com/industries/robotics/">Protolabs</a> · <a href="https://www.nist.gov/el/intelligent-systems-division-73500/robotic-grasping-and-manipulation-assembly">美国国家标准与技术研究院</a></td>
</tr>
</tbody>
</table>

## 结合学术与产业理解进展

学术比较强调受控任务、基线、消融与泛化；产业交付还需要集成、运行时长、恢复、维护和成本证据。企业也开展研究，高校也开发硬件，应按实际贡献确定角色。

两者之间可比较的桥梁是可复现任务规格：机器人与末端、感知配置、动作接口、数据版本、计算预算、工况和失败统计。关联论文与产品时，应保留这些边界。
