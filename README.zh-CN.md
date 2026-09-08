<div align="center">

# 🤖 具身智能：学术与产业全景

**从机器人硬件、软件、学术研究到产业实现，理解细分类、关键能力与未解问题。**

[英文](README.md) | 中文

[![精选](https://img.shields.io/badge/Awesome-Embodied%20AI-fc60a8?style=for-the-badge&label=%E7%B2%BE%E9%80%89&message=%E5%85%B7%E8%BA%AB%E6%99%BA%E8%83%BD)](https://awesome.re)
[![条目数](https://img.shields.io/badge/Survey%20Entries-767-0984e3?style=for-the-badge&label=%E6%9D%A1%E7%9B%AE%E6%95%B0)](README.zh-CN.md)
[![最近提交](https://img.shields.io/github/last-commit/neardws/awesome-embodied-ai-papers?style=for-the-badge&color=00b894&label=%E6%9C%80%E8%BF%91%E6%8F%90%E4%BA%A4)](https://github.com/neardws/awesome-embodied-ai-papers/commits)
[![星标](https://img.shields.io/github/stars/neardws/awesome-embodied-ai-papers?style=for-the-badge&color=fdcb6e&logo=github&label=%E6%98%9F%E6%A0%87)](https://github.com/neardws/awesome-embodied-ai-papers/stargazers)
[![分支](https://img.shields.io/github/forks/neardws/awesome-embodied-ai-papers?style=for-the-badge&color=e17055&logo=github&label=%E5%88%86%E6%94%AF)](https://github.com/neardws/awesome-embodied-ai-papers/network/members)

全景来源核对：2026-09-08 · 原有论文与硬件证据日期保留在各主题页。

</div>

<!-- landscape:start -->

## 学术与产业全景

以 **14 个板块、84 个细类**梳理问题、学术重点、产业角色与比较指标，并与下方六条论文研究方向关联。

![学术与产业全景图](figs/research-industry-landscape.zh-CN.svg)

[查看全景大图](figs/research-industry-landscape.zh-CN.svg)

- [完整全景与跨环节联系](docs/zh-CN/landscape/README.md)
- [关键进展与共性瓶颈](docs/zh-CN/landscape/progress.md)
- [参与者、来源与证据状态](docs/zh-CN/landscape/sources.md)

## 细分类总览

<table width="1630">
<thead>
<tr>
<th width="230" nowrap>板块</th>
<th width="360">核心问题</th>
<th width="680">细类</th>
<th width="360">代表性入口</th>
</tr>
</thead>
<tbody>
<tr>
<td width="230" nowrap><a href="docs/zh-CN/landscape/01-bodies.md">整机与本体形态</a></td>
<td width="360">什么身体适合什么任务，如何平衡可达空间、运动能力、成本与可靠性？</td>
<td width="680"><a href="docs/zh-CN/landscape/01-bodies.md#01-01">双足与通用人形</a> · <a href="docs/zh-CN/landscape/01-bodies.md#01-02">轮式双臂与移动操作</a> · <a href="docs/zh-CN/landscape/01-bodies.md#01-03">四足与轮足</a> · <a href="docs/zh-CN/landscape/01-bodies.md#01-04">固定工业与协作机械臂</a> · <a href="docs/zh-CN/landscape/01-bodies.md#01-05">小型开放与教学平台</a> · <a href="docs/zh-CN/landscape/01-bodies.md#01-06">专用、柔性与可穿戴本体</a></td>
<td width="360"><a href="docs/zh-CN/landscape/sources.md#source-toddler">ToddlerBot（斯坦福大学）</a> · <a href="docs/zh-CN/landscape/sources.md#source-unitree">宇树 G1</a> · <a href="docs/zh-CN/landscape/sources.md#source-franka">Franka Research 3</a></td>
</tr>
<tr>
<td width="230" nowrap><a href="docs/zh-CN/landscape/02-actuation.md">执行与精密传动</a></td>
<td width="360">怎样把电能变成可控的力与运动，并在冲击、温升和磨损下保持性能？</td>
<td width="680"><a href="docs/zh-CN/landscape/02-actuation.md#02-01">电机与直接驱动</a> · <a href="docs/zh-CN/landscape/02-actuation.md#02-02">谐波、行星与摆线减速</a> · <a href="docs/zh-CN/landscape/02-actuation.md#02-03">丝杠与线性执行器</a> · <a href="docs/zh-CN/landscape/02-actuation.md#02-04">一体化关节模组</a> · <a href="docs/zh-CN/landscape/02-actuation.md#02-05">伺服驱动与底层控制</a> · <a href="docs/zh-CN/landscape/02-actuation.md#02-06">支承、制动与运动连接</a></td>
<td width="360"><a href="docs/zh-CN/landscape/sources.md#source-harmonic">Harmonic Drive</a> · <a href="docs/zh-CN/landscape/sources.md#source-ti">德州仪器机器人设计资源</a> · <a href="docs/zh-CN/landscape/sources.md#source-toddler">ToddlerBot（斯坦福大学）</a></td>
</tr>
<tr>
<td width="230" nowrap><a href="docs/zh-CN/landscape/03-end-effectors.md">末端与操作机构</a></td>
<td width="360">如何根据物体与工艺选择接触方式，而非只增加手指数量？</td>
<td width="680"><a href="docs/zh-CN/landscape/03-end-effectors.md#03-01">平行与自适应夹爪</a> · <a href="docs/zh-CN/landscape/03-end-effectors.md#03-02">吸附、气动与柔性末端</a> · <a href="docs/zh-CN/landscape/03-end-effectors.md#03-03">多指灵巧手</a> · <a href="docs/zh-CN/landscape/03-end-effectors.md#03-04">绳驱、欠驱动与仿生结构</a> · <a href="docs/zh-CN/landscape/03-end-effectors.md#03-05">工具快换与工艺末端</a> · <a href="docs/zh-CN/landscape/03-end-effectors.md#03-06">双手与手臂协同</a></td>
<td width="360"><a href="docs/zh-CN/landscape/sources.md#source-leap">LEAP Hand 研究团队</a> · <a href="docs/zh-CN/landscape/sources.md#source-shadow">Shadow Robot 灵巧手</a> · <a href="docs/zh-CN/landscape/sources.md#source-franka">Franka Research 3</a></td>
</tr>
<tr>
<td width="230" nowrap><a href="docs/zh-CN/landscape/04-sensing.md">传感与交互硬件</a></td>
<td width="360">如何测量外部环境、身体状态与接触过程，并把多种信号对齐？</td>
<td width="680"><a href="docs/zh-CN/landscape/04-sensing.md#04-01">图像、深度与三维视觉</a> · <a href="docs/zh-CN/landscape/04-sensing.md#04-02">激光、雷达与测距</a> · <a href="docs/zh-CN/landscape/04-sensing.md#04-03">惯性、编码器与本体反馈</a> · <a href="docs/zh-CN/landscape/04-sensing.md#04-04">六维力与关节力矩</a> · <a href="docs/zh-CN/landscape/04-sensing.md#04-05">触觉阵列与电子皮肤</a> · <a href="docs/zh-CN/landscape/04-sensing.md#04-06">动作捕捉、语音与人机交互</a></td>
<td width="360"><a href="docs/zh-CN/landscape/sources.md#source-digit">GelSight DIGIT</a> · <a href="docs/zh-CN/landscape/sources.md#source-ati">ATI 六维力传感器</a> · <a href="docs/zh-CN/landscape/sources.md#source-unitree">宇树 G1</a></td>
</tr>
<tr>
<td width="230" nowrap><a href="docs/zh-CN/landscape/05-compute.md">计算、通信与能源</a></td>
<td width="360">怎样把高算力推理与确定性控制放进同一台机器人？</td>
<td width="680"><a href="docs/zh-CN/landscape/05-compute.md#05-01">推理芯片与异构加速</a> · <a href="docs/zh-CN/landscape/05-compute.md#05-02">边缘计算与域控制器</a> · <a href="docs/zh-CN/landscape/05-compute.md#05-03">实时微控制与功率驱动</a> · <a href="docs/zh-CN/landscape/05-compute.md#05-04">机内总线与工业网络</a> · <a href="docs/zh-CN/landscape/05-compute.md#05-05">无线、云边与远程连接</a> · <a href="docs/zh-CN/landscape/05-compute.md#05-06">电池、电源与热管理</a></td>
<td width="360"><a href="docs/zh-CN/landscape/sources.md#source-nvidia">NVIDIA 机器人平台</a> · <a href="docs/zh-CN/landscape/sources.md#source-ti">德州仪器机器人设计资源</a> · <a href="docs/zh-CN/landscape/sources.md#source-toddler">ToddlerBot（斯坦福大学）</a></td>
</tr>
<tr>
<td width="230" nowrap><a href="docs/zh-CN/landscape/06-perception.md">感知、定位与空间表示</a></td>
<td width="360">怎样把传感数据转换为可供导航、规划和操作使用的状态？</td>
<td width="680"><a href="docs/zh-CN/landscape/06-perception.md#06-01">目标识别与开放词汇感知</a> · <a href="docs/zh-CN/landscape/06-perception.md#06-02">位姿、几何与可供性</a> · <a href="docs/zh-CN/landscape/06-perception.md#06-03">定位建图与状态估计</a> · <a href="docs/zh-CN/landscape/06-perception.md#06-04">三维重建与场景表征</a> · <a href="docs/zh-CN/landscape/06-perception.md#06-05">语义地图与空间记忆</a> · <a href="docs/zh-CN/landscape/06-perception.md#06-06">主动感知与不确定性</a></td>
<td width="360"><a href="docs/zh-CN/landscape/sources.md#source-nav2">Nav2 社区</a> · <a href="docs/zh-CN/landscape/sources.md#source-rvt">RVT 研究团队</a> · <a href="docs/zh-CN/landscape/sources.md#source-voxposer">VoxPoser 研究团队</a></td>
</tr>
<tr>
<td width="230" nowrap><a href="docs/zh-CN/landscape/07-control.md">运动控制与动作学习</a></td>
<td width="360">如何把任务目标转成连续、稳定且符合动力学的动作？</td>
<td width="680"><a href="docs/zh-CN/landscape/07-control.md#07-01">运动学与轨迹规划</a> · <a href="docs/zh-CN/landscape/07-control.md#07-02">模型预测与最优控制</a> · <a href="docs/zh-CN/landscape/07-control.md#07-03">力控、阻抗与接触控制</a> · <a href="docs/zh-CN/landscape/07-control.md#07-04">腿式与全身协调控制</a> · <a href="docs/zh-CN/landscape/07-control.md#07-05">模仿与扩散、流动作策略</a> · <a href="docs/zh-CN/landscape/07-control.md#07-06">强化学习与在线适应</a></td>
<td width="360"><a href="docs/zh-CN/landscape/sources.md#source-moveit">MoveIt / PickNik</a> · <a href="docs/zh-CN/landscape/sources.md#source-control">ros2_control 社区</a> · <a href="docs/zh-CN/landscape/sources.md#source-diffusion">Diffusion Policy 研究团队</a></td>
</tr>
<tr>
<td width="230" nowrap><a href="docs/zh-CN/landscape/08-models.md">机器人模型、推理与规划</a></td>
<td width="360">怎样连接语言理解、世界预测、技能与执行反馈？</td>
<td width="680"><a href="docs/zh-CN/landscape/08-models.md#08-01">视觉语言动作基础模型</a> · <a href="docs/zh-CN/landscape/08-models.md#08-02">世界模型与行动后果预测</a> · <a href="docs/zh-CN/landscape/08-models.md#08-03">任务分解与技能规划</a> · <a href="docs/zh-CN/landscape/08-models.md#08-04">长期记忆与个性化</a> · <a href="docs/zh-CN/landscape/08-models.md#08-05">失败监测与恢复</a> · <a href="docs/zh-CN/landscape/08-models.md#08-06">分层智能体与混合系统</a></td>
<td width="360"><a href="docs/zh-CN/landscape/sources.md#source-openvla">OpenVLA 联合研究团队</a> · <a href="docs/zh-CN/landscape/sources.md#source-pi">Physical Intelligence / π0</a> · <a href="docs/zh-CN/landscape/sources.md#source-saycan">SayCan 研究团队</a></td>
</tr>
<tr>
<td width="230" nowrap><a href="docs/zh-CN/landscape/09-systems.md">系统软件与集成平台</a></td>
<td width="360">如何把异构设备、模型和技能组成可开发、可调试的机器人系统？</td>
<td width="680"><a href="docs/zh-CN/landscape/09-systems.md#09-01">操作系统与通信中间件</a> · <a href="docs/zh-CN/landscape/09-systems.md#09-02">驱动、硬件抽象与控制接口</a> · <a href="docs/zh-CN/landscape/09-systems.md#09-03">导航与操作软件栈</a> · <a href="docs/zh-CN/landscape/09-systems.md#09-04">技能库、行为树与工作流</a> · <a href="docs/zh-CN/landscape/09-systems.md#09-05">开发、调试与可观测性</a> · <a href="docs/zh-CN/landscape/09-systems.md#09-06">设施对接与多机协调</a></td>
<td width="360"><a href="docs/zh-CN/landscape/sources.md#source-ros">ROS 2 社区</a> · <a href="docs/zh-CN/landscape/sources.md#source-control">ros2_control 社区</a> · <a href="docs/zh-CN/landscape/sources.md#source-moveit">MoveIt / PickNik</a></td>
</tr>
<tr>
<td width="230" nowrap><a href="docs/zh-CN/landscape/10-data.md">数据采集与治理</a></td>
<td width="360">怎样把分散的演示与运行经验变成可复用、可追溯的数据资产？</td>
<td width="680"><a href="docs/zh-CN/landscape/10-data.md#10-01">遥操作与示范采集</a> · <a href="docs/zh-CN/landscape/10-data.md#10-02">人类视频与跨本体重定向</a> · <a href="docs/zh-CN/landscape/10-data.md#10-03">自动探索与失败采集</a> · <a href="docs/zh-CN/landscape/10-data.md#10-04">多模态同步与标注</a> · <a href="docs/zh-CN/landscape/10-data.md#10-05">清洗、版本与数据质量</a> · <a href="docs/zh-CN/landscape/10-data.md#10-06">数据格式、共享与数据闭环</a></td>
<td width="360"><a href="docs/zh-CN/landscape/sources.md#source-oxe">Open X-Embodiment 协作组</a> · <a href="docs/zh-CN/landscape/sources.md#source-droid">DROID 多机构团队</a> · <a href="docs/zh-CN/landscape/sources.md#source-umi">UMI 研究团队</a></td>
</tr>
<tr>
<td width="230" nowrap><a href="docs/zh-CN/landscape/11-simulation.md">仿真与训练基础设施</a></td>
<td width="360">如何用可控实验加速研发，同时识别仿真无法替代的真实因素？</td>
<td width="680"><a href="docs/zh-CN/landscape/11-simulation.md#11-01">物理引擎与接触求解</a> · <a href="docs/zh-CN/landscape/11-simulation.md#11-02">数字孪生与资产构建</a> · <a href="docs/zh-CN/landscape/11-simulation.md#11-03">传感仿真与合成数据</a> · <a href="docs/zh-CN/landscape/11-simulation.md#11-04">并行训练与实验管理</a> · <a href="docs/zh-CN/landscape/11-simulation.md#11-05">领域随机化与迁移</a> · <a href="docs/zh-CN/landscape/11-simulation.md#11-06">软件、硬件在环验证</a></td>
<td width="360"><a href="docs/zh-CN/landscape/sources.md#source-mujoco">MuJoCo / Google DeepMind</a> · <a href="docs/zh-CN/landscape/sources.md#source-isaac">NVIDIA Isaac Lab</a> · <a href="docs/zh-CN/landscape/sources.md#source-robotwin">RoboTwin 联合团队</a></td>
</tr>
<tr>
<td width="230" nowrap><a href="docs/zh-CN/landscape/12-operations.md">评测、安全与部署运维</a></td>
<td width="360">怎样把单次任务效果转化为可测、可恢复、可持续运行的系统能力？</td>
<td width="680"><a href="docs/zh-CN/landscape/12-operations.md#12-01">能力基准与任务评测</a> · <a href="docs/zh-CN/landscape/12-operations.md#12-02">可靠性与长时程测试</a> · <a href="docs/zh-CN/landscape/12-operations.md#12-03">安全约束与系统防护</a> · <a href="docs/zh-CN/landscape/12-operations.md#12-04">端侧部署与模型更新</a> · <a href="docs/zh-CN/landscape/12-operations.md#12-05">接管、诊断与恢复</a> · <a href="docs/zh-CN/landscape/12-operations.md#12-06">机队、服务与运营指标</a></td>
<td width="360"><a href="docs/zh-CN/landscape/sources.md#source-nist">美国国家标准与技术研究院</a> · <a href="docs/zh-CN/landscape/sources.md#source-robotwin">RoboTwin 联合团队</a> · <a href="docs/zh-CN/landscape/sources.md#source-rmf">Open-RMF 社区</a></td>
</tr>
<tr>
<td width="230" nowrap><a href="docs/zh-CN/landscape/13-manufacturing.md">制造、集成与交付</a></td>
<td width="360">怎样把实验样机变成可制造、可维护且配置明确的交付物？</td>
<td width="680"><a href="docs/zh-CN/landscape/13-manufacturing.md#13-01">结构材料与精密制造</a> · <a href="docs/zh-CN/landscape/13-manufacturing.md#13-02">增材制造与快速迭代</a> · <a href="docs/zh-CN/landscape/13-manufacturing.md#13-03">装配、标定与出厂测试</a> · <a href="docs/zh-CN/landscape/13-manufacturing.md#13-04">供应链与配置管理</a> · <a href="docs/zh-CN/landscape/13-manufacturing.md#13-05">系统集成与工位改造</a> · <a href="docs/zh-CN/landscape/13-manufacturing.md#13-06">维护、培训与生命周期</a></td>
<td width="360"><a href="docs/zh-CN/landscape/sources.md#source-protolabs">Protolabs</a> · <a href="docs/zh-CN/landscape/sources.md#source-harmonic">Harmonic Drive</a> · <a href="docs/zh-CN/landscape/sources.md#source-toddler">ToddlerBot（斯坦福大学）</a></td>
</tr>
<tr>
<td width="230" nowrap><a href="docs/zh-CN/landscape/14-applications.md">应用与解决方案</a></td>
<td width="360">机器人服务于哪些工作流程，价值如何通过真实任务衡量？</td>
<td width="680"><a href="docs/zh-CN/landscape/14-applications.md#14-01">制造、装配与工艺操作</a> · <a href="docs/zh-CN/landscape/14-applications.md#14-02">仓储物流与搬运配送</a> · <a href="docs/zh-CN/landscape/14-applications.md#14-03">商业服务与楼宇作业</a> · <a href="docs/zh-CN/landscape/14-applications.md#14-04">家庭消费与陪伴</a> · <a href="docs/zh-CN/landscape/14-applications.md#14-05">能源、农业与特种作业</a> · <a href="docs/zh-CN/landscape/14-applications.md#14-06">医疗、康复与辅助行动</a></td>
<td width="360"><a href="docs/zh-CN/landscape/sources.md#source-ur">Universal Robots</a> · <a href="docs/zh-CN/landscape/sources.md#source-gxo">GXO / Agility Robotics</a> · <a href="docs/zh-CN/landscape/sources.md#source-nist">美国国家标准与技术研究院</a></td>
</tr>
</tbody>
</table>

## 连接研究与产业的关键问题

- **从演示到泛化：** 对齐未见任务、环境、机器人配置和人工介入预算。
- **从更多数据到有效数据：** 检查动作语义、时间同步、来源和评测泄漏。
- **从部件到系统：** 联合验证软硬件时序、接口、失效隔离和恢复。
- **从现场案例到持续服务：** 保留运行时长、停机、维护和完整任务成本。

[查看有来源的进展分析](docs/zh-CN/landscape/progress.md)

<!-- landscape:end -->


主表共 **767 条分类条目**，覆盖 **6 个方向、29 个子方向**；另有 **7 条补充线索**。条目按分类表行计数，非跨方向去重论文数。来源和硬件核查日期见对应页面。

> [!NOTE]
> 论文条目范围限定为已读公开来源中可核验的论文，覆盖 CCF-A 会议以及 ICRA/IROS 等机器人传统强会。

> [!TIP]
> 如果有遗漏论文或资源，可以通过议题或合并请求补充。

## 论文阅读导航

- [总体判断、图示与趋势](docs/zh-CN/overview.md)
- [重点阅读顺序](docs/zh-CN/reading-order.md)
- [数据来源与追溯](docs/zh-CN/sources.md)
- [人形与双足硬件参考](docs/zh-CN/embodiment/hardware.md)
- [源仓库补充条目](docs/zh-CN/additional-sources.md)

## 论文研究地图

<table width="1090">
<thead>
<tr>
<th width="240">方向</th>
<th width="90" nowrap>条目数</th>
<th width="760">子方向</th>
</tr>
</thead>
<tbody>
<tr>
<td width="240"><a href="docs/zh-CN/vln/README.md">VLN / 大范围导航</a></td>
<td width="90" nowrap>92</td>
<td width="760"><a href="docs/zh-CN/vln/continuous.md">连续视觉语言导航</a> · <a href="docs/zh-CN/vln/map-memory.md">地图与记忆</a> · <a href="docs/zh-CN/vln/physically-executable.md">物理可执行导航</a> · <a href="docs/zh-CN/vln/urban-open-world.md">城市与开放世界导航</a> · <a href="docs/zh-CN/vln/on-device.md">低成本与端侧导航</a></td>
</tr>
<tr>
<td width="240"><a href="docs/zh-CN/vla/README.md">VLA / 操作策略</a></td>
<td width="90" nowrap>251</td>
<td width="760"><a href="docs/zh-CN/vla/generalist.md">通用 VLA</a> · <a href="docs/zh-CN/vla/action-representation.md">动作表示</a> · <a href="docs/zh-CN/vla/diffusion-flow.md">扩散与流策略</a> · <a href="docs/zh-CN/vla/3d-grounding.md">三维空间落地</a> · <a href="docs/zh-CN/vla/online-rl.md">在线与强化学习微调</a> · <a href="docs/zh-CN/vla/safety-robustness.md">安全性与鲁棒性</a></td>
</tr>
<tr>
<td width="240"><a href="docs/zh-CN/wam/README.md">WAM / 世界模型</a></td>
<td width="90" nowrap>70</td>
<td width="760"><a href="docs/zh-CN/wam/cascaded.md">级联世界动作模型</a> · <a href="docs/zh-CN/wam/joint.md">联合世界动作模型</a> · <a href="docs/zh-CN/wam/video-latent.md">视频与潜在世界模型</a> · <a href="docs/zh-CN/wam/for-vla.md">面向 VLA 的世界模型</a></td>
</tr>
<tr>
<td width="240"><a href="docs/zh-CN/planning/README.md">智能体规划 / 推理规划</a></td>
<td width="90" nowrap>103</td>
<td width="760"><a href="docs/zh-CN/planning/task-decomposition.md">任务分解</a> · <a href="docs/zh-CN/planning/memory.md">记忆</a> · <a href="docs/zh-CN/planning/failure-monitor.md">失败监测</a> · <a href="docs/zh-CN/planning/constraint-affordance.md">约束与可供性规划</a> · <a href="docs/zh-CN/planning/self-improving.md">自我改进规划</a></td>
</tr>
<tr>
<td width="240"><a href="docs/zh-CN/embodiment/README.md">本体扩展 / 灵巧操作</a></td>
<td width="90" nowrap>146</td>
<td width="760"><a href="docs/zh-CN/embodiment/humanoid.md">人形机器人</a> · <a href="docs/zh-CN/embodiment/bimanual.md">双臂操作</a> · <a href="docs/zh-CN/embodiment/dexterous-hand.md">灵巧手</a> · <a href="docs/zh-CN/embodiment/tactile-contact.md">触觉与接触丰富操作</a></td>
</tr>
<tr>
<td width="240"><a href="docs/zh-CN/deployment/README.md">轻量化 / 评测 / 数据</a></td>
<td width="90" nowrap>105</td>
<td width="760"><a href="docs/zh-CN/deployment/quantization-cache-tokenization.md">量化、缓存与词元化</a> · <a href="docs/zh-CN/deployment/real-time.md">实时执行</a> · <a href="docs/zh-CN/deployment/benchmarks-datasets.md">基准与数据集</a> · <a href="docs/zh-CN/deployment/sim2real.md">仿真到现实</a> · <a href="docs/zh-CN/deployment/safety-evaluation.md">安全评测</a></td>
</tr>
</tbody>
</table>

## 标签图例

<table width="730">
<thead>
<tr>
<th width="110" nowrap>标签</th>
<th width="620">含义</th>
</tr>
</thead>
<tbody>
<tr>
<td width="110" nowrap><code>VLN</code></td>
<td width="620">大范围导航</td>
</tr>
<tr>
<td width="110" nowrap><code>VLA</code></td>
<td width="620">视觉-语言-动作操作策略</td>
</tr>
<tr>
<td width="110" nowrap><code>WAM</code></td>
<td width="620">世界动作模型</td>
</tr>
<tr>
<td width="110" nowrap><code>规划</code></td>
<td width="620">任务分解、记忆、失败恢复、约束规划</td>
</tr>
<tr>
<td width="110" nowrap><code>本体扩展</code></td>
<td width="620">人形、双臂、灵巧手、触觉</td>
</tr>
<tr>
<td width="110" nowrap><code>部署</code></td>
<td width="620">轻量化、评测、数据、仿真到现实、安全</td>
</tr>
</tbody>
</table>


## 部分更新

直接修改对应子方向文件，并同步修改另一语言的同名文件。论文标题、会议、年份、资源链接和条目顺序应一致；中文仅保留论文官方标题、模型等专名及必要缩写，通用说明使用中文。详细流程见[维护指南](CONTRIBUTING.zh-CN.md)。
