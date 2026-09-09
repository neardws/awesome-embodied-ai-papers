# 技术与产品细节库

[产品细节目录](README.md) | [英文](../../en/products/README.md) | [全景目录](../landscape/README.md)

本层包含 **170 条型号/产品族对照记录**、**312 段完整技术上下文**、**917 条原始展项关联**，覆盖 70 个来源分类。在全景之下恢复产品细节，不迁入展位名录和企业简介。

原资料核查日期为 **2026-09-05**，本次重组日期为 **2026-09-08**。展项关联不是去重后的商品型号，可能含系列、服务、概念、联合展项或冲突命名。尚未逐型号拆清的展项保留链接，不继承其他型号的参数。

<a href="catalog.md">检索全部原始产品与展项</a>

同时保留原有 236 个跨分类入口，复用同一份技术记录。

## 对照入口

<table width="1480">
<thead>
<tr>
<th width="300">板块</th>
<th width="140">相关记录数</th>
<th width="1040">专用比较字段</th>
</tr>
</thead>
<tbody>
<tr>
<td width="300"><a href="comparisons/01-bodies.md">整机与本体形态</a></td>
<td width="140">40</td>
<td width="1040">结构与配置 / 自由度 / 重量 / 负载与工况 / 电池与续航 / 传感配置 / 接口</td>
</tr>
<tr>
<td width="300"><a href="comparisons/02-actuation.md">执行与精密传动</a></td>
<td width="140">20</td>
<td width="1040">结构与配置 / 力矩与推力 / 供电与功率 / 精度与误差 / 接口 / 传感配置 / 防护与环境</td>
</tr>
<tr>
<td width="300"><a href="comparisons/03-end-effectors.md">末端与操作机构</a></td>
<td width="140">19</td>
<td width="1040">结构与配置 / 自由度 / 重量 / 接触与指尖力 / 负载与工况 / 传感配置 / 频率与同步 / 接口 / 仿真与数据支持</td>
</tr>
<tr>
<td width="300"><a href="comparisons/04-sensing.md">传感与交互硬件</a></td>
<td width="140">31</td>
<td width="1040">结构与配置 / 量程与视场 / 精度与误差 / 频率与同步 / 接口 / 功能与工作流程 / 防护与环境</td>
</tr>
<tr>
<td width="300"><a href="comparisons/05-compute.md">计算、通信与能源</a></td>
<td width="140">23</td>
<td width="1040">处理器与架构 / 算力与内存 / 供电与功率 / 电池与续航 / 接口</td>
</tr>
<tr>
<td width="300"><a href="comparisons/06-perception.md">感知、定位与空间表示</a></td>
<td width="140">1</td>
<td width="1040">功能与工作流程 / 传感配置 / 接口 / 精度与误差</td>
</tr>
<tr>
<td width="300"><a href="comparisons/07-control.md">运动控制与动作学习</a></td>
<td width="140">1</td>
<td width="1040">功能与工作流程 / 接口 / 精度与误差 / 报告的任务指标</td>
</tr>
<tr>
<td width="300"><a href="comparisons/08-models.md">机器人模型、推理与规划</a></td>
<td width="140">9</td>
<td width="1040">功能与工作流程 / 输入与数据 / 算力与内存 / 接口</td>
</tr>
<tr>
<td width="300"><a href="comparisons/09-systems.md">系统软件与集成平台</a></td>
<td width="140">3</td>
<td width="1040">功能与工作流程 / 输入与数据 / 接口</td>
</tr>
<tr>
<td width="300"><a href="comparisons/10-data.md">数据采集与治理</a></td>
<td width="140">17</td>
<td width="1040">结构与配置 / 输入与数据 / 传感配置 / 精度与误差 / 频率与同步 / 接口 / 功能与工作流程</td>
</tr>
<tr>
<td width="300"><a href="comparisons/11-simulation.md">仿真与训练基础设施</a></td>
<td width="140">4</td>
<td width="1040">功能与工作流程 / 输入与数据 / 算力与内存 / 接口</td>
</tr>
<tr>
<td width="300"><a href="comparisons/12-operations.md">评测、安全与部署运维</a></td>
<td width="140">2</td>
<td width="1040">功能与工作流程 / 报告的任务指标 / 接口</td>
</tr>
<tr>
<td width="300"><a href="comparisons/13-manufacturing.md">制造、集成与交付</a></td>
<td width="140">8</td>
<td width="1040">结构与配置 / 功能与工作流程 / 报告的任务指标 / 接口</td>
</tr>
<tr>
<td width="300"><a href="comparisons/14-applications.md">应用与解决方案</a></td>
<td width="140">14</td>
<td width="1040">功能与工作流程 / 结构与配置 / 报告的任务指标 / 防护与环境 / 电池与续航</td>
</tr>
</tbody>
</table>

## 细类独立专题页

<table width="1410">
<thead>
<tr>
<th width="360">细类</th>
<th width="300">所属板块</th>
<th width="150">对照记录数</th>
<th width="600">解决的问题</th>
</tr>
</thead>
<tbody>
<tr>
<td width="360"><a href="topics/01-01.md">双足与通用人形</a></td>
<td width="300">整机与本体形态</td>
<td width="150">10</td>
<td width="600">在人类尺度空间中移动并操作。</td>
</tr>
<tr>
<td width="360"><a href="topics/01-02.md">轮式双臂与移动操作</a></td>
<td width="300">整机与本体形态</td>
<td width="150">12</td>
<td width="600">把导航、站位和双臂操作连成任务。</td>
</tr>
<tr>
<td width="360"><a href="topics/01-03.md">四足与轮足</a></td>
<td width="300">整机与本体形态</td>
<td width="150">6</td>
<td width="600">在楼梯、坡面和不平地面移动。</td>
</tr>
<tr>
<td width="360"><a href="topics/01-04.md">固定工业与协作机械臂</a></td>
<td width="300">整机与本体形态</td>
<td width="150">2</td>
<td width="600">在受限工位完成重复或柔性操作。</td>
</tr>
<tr>
<td width="360"><a href="topics/01-05.md">小型开放与教学平台</a></td>
<td width="300">整机与本体形态</td>
<td width="150">5</td>
<td width="600">降低实验、教学和复现门槛。</td>
</tr>
<tr>
<td width="360"><a href="topics/01-06.md">专用、柔性与可穿戴本体</a></td>
<td width="300">整机与本体形态</td>
<td width="150">1</td>
<td width="600">适配狭窄、柔性或人体耦合任务。</td>
</tr>
<tr>
<td width="360"><a href="topics/01-07.md">移动底盘与模块化载体</a></td>
<td width="300">整机与本体形态</td>
<td width="150">2</td>
<td width="600">为感知、运输和操作提供移动载体。</td>
</tr>
<tr>
<td width="360"><a href="topics/01-08.md">固定半身与双臂平台</a></td>
<td width="300">整机与本体形态</td>
<td width="150">2</td>
<td width="600">在固定工位研究或执行双臂与上身操作。</td>
</tr>
<tr>
<td width="360"><a href="topics/02-01.md">电机与直接驱动</a></td>
<td width="300">执行与精密传动</td>
<td width="150">5</td>
<td width="600">提供可调的力矩与转速。</td>
</tr>
<tr>
<td width="360"><a href="topics/02-02.md">谐波、行星与摆线减速</a></td>
<td width="300">执行与精密传动</td>
<td width="150">2</td>
<td width="600">在体积约束下放大力矩。</td>
</tr>
<tr>
<td width="360"><a href="topics/02-03.md">丝杠与线性执行器</a></td>
<td width="300">执行与精密传动</td>
<td width="150">2</td>
<td width="600">产生直线推力与精密位移。</td>
</tr>
<tr>
<td width="360"><a href="topics/02-04.md">一体化关节模组</a></td>
<td width="300">执行与精密传动</td>
<td width="150">6</td>
<td width="600">把电机、传动、驱动与传感封装为关节。</td>
</tr>
<tr>
<td width="360"><a href="topics/02-05.md">伺服驱动与底层控制</a></td>
<td width="300">执行与精密传动</td>
<td width="150">5</td>
<td width="600">把电流、速度与位置指令稳定执行。</td>
</tr>
<tr>
<td width="360"><a href="topics/02-06.md">支承、制动与运动连接</a></td>
<td width="300">执行与精密传动</td>
<td width="150">2</td>
<td width="600">保障关节承载、停机保持与运动供能。</td>
</tr>
<tr>
<td width="360"><a href="topics/03-01.md">平行与自适应夹爪</a></td>
<td width="300">末端与操作机构</td>
<td width="150">0</td>
<td width="600">稳定夹持尺寸或形状不同的物体。</td>
</tr>
<tr>
<td width="360"><a href="topics/03-02.md">吸附、气动与柔性末端</a></td>
<td width="300">末端与操作机构</td>
<td width="150">1</td>
<td width="600">处理薄片、易损或不规则物体。</td>
</tr>
<tr>
<td width="360"><a href="topics/03-03.md">多指灵巧手</a></td>
<td width="300">末端与操作机构</td>
<td width="150">17</td>
<td width="600">在抓取后继续调整物体姿态。</td>
</tr>
<tr>
<td width="360"><a href="topics/03-04.md">绳驱、欠驱动与仿生结构</a></td>
<td width="300">末端与操作机构</td>
<td width="150">2</td>
<td width="600">降低手部重量与驱动数量。</td>
</tr>
<tr>
<td width="360"><a href="topics/03-05.md">工具快换与工艺末端</a></td>
<td width="300">末端与操作机构</td>
<td width="150">1</td>
<td width="600">在抓取、拧紧、加工等工序间切换。</td>
</tr>
<tr>
<td width="360"><a href="topics/03-06.md">双手与手臂协同</a></td>
<td width="300">末端与操作机构</td>
<td width="150">0</td>
<td width="600">共同支撑、交接或装配物体。</td>
</tr>
<tr>
<td width="360"><a href="topics/04-01.md">图像、深度与三维视觉</a></td>
<td width="300">传感与交互硬件</td>
<td width="150">5</td>
<td width="600">获取物体外观、形状与距离。</td>
</tr>
<tr>
<td width="360"><a href="topics/04-02.md">激光、雷达与测距</a></td>
<td width="300">传感与交互硬件</td>
<td width="150">4</td>
<td width="600">支持远距离或复杂环境测量。</td>
</tr>
<tr>
<td width="360"><a href="topics/04-03.md">惯性、编码器与本体反馈</a></td>
<td width="300">传感与交互硬件</td>
<td width="150">4</td>
<td width="600">估计机体姿态、关节位置和运动。</td>
</tr>
<tr>
<td width="360"><a href="topics/04-04.md">六维力与关节力矩</a></td>
<td width="300">传感与交互硬件</td>
<td width="150">7</td>
<td width="600">判断接触载荷及外力。</td>
</tr>
<tr>
<td width="360"><a href="topics/04-05.md">触觉阵列与电子皮肤</a></td>
<td width="300">传感与交互硬件</td>
<td width="150">8</td>
<td width="600">感知接触分布、滑移和局部几何。</td>
</tr>
<tr>
<td width="360"><a href="topics/04-06.md">动作捕捉、语音与人机交互</a></td>
<td width="300">传感与交互硬件</td>
<td width="150">2</td>
<td width="600">把人的动作和意图接入机器人。</td>
</tr>
<tr>
<td width="360"><a href="topics/04-07.md">环境与化学感知</a></td>
<td width="300">传感与交互硬件</td>
<td width="150">1</td>
<td width="600">识别气体、化学特征和环境变化。</td>
</tr>
<tr>
<td width="360"><a href="topics/05-01.md">推理芯片与异构加速</a></td>
<td width="300">计算、通信与能源</td>
<td width="150">7</td>
<td width="600">在设备上执行感知与策略模型。</td>
</tr>
<tr>
<td width="360"><a href="topics/05-02.md">边缘计算与域控制器</a></td>
<td width="300">计算、通信与能源</td>
<td width="150">8</td>
<td width="600">承载多传感、多模型与系统服务。</td>
</tr>
<tr>
<td width="360"><a href="topics/05-03.md">实时微控制与功率驱动</a></td>
<td width="300">计算、通信与能源</td>
<td width="150">7</td>
<td width="600">保持底层闭环与电机保护。</td>
</tr>
<tr>
<td width="360"><a href="topics/05-04.md">机内总线与工业网络</a></td>
<td width="300">计算、通信与能源</td>
<td width="150">0</td>
<td width="600">传送有时限的状态与指令。</td>
</tr>
<tr>
<td width="360"><a href="topics/05-05.md">无线、云边与远程连接</a></td>
<td width="300">计算、通信与能源</td>
<td width="150">0</td>
<td width="600">支持遥操作、更新和跨设备协作。</td>
</tr>
<tr>
<td width="360"><a href="topics/05-06.md">电池、电源与热管理</a></td>
<td width="300">计算、通信与能源</td>
<td width="150">6</td>
<td width="600">在持续任务中稳定供能。</td>
</tr>
<tr>
<td width="360"><a href="topics/06-01.md">目标识别与开放词汇感知</a></td>
<td width="300">感知、定位与空间表示</td>
<td width="150">0</td>
<td width="600">找到任务相关物体及其属性。</td>
</tr>
<tr>
<td width="360"><a href="topics/06-02.md">位姿、几何与可供性</a></td>
<td width="300">感知、定位与空间表示</td>
<td width="150">0</td>
<td width="600">定位可抓取、可接触和可操作部位。</td>
</tr>
<tr>
<td width="360"><a href="topics/06-03.md">定位建图与状态估计</a></td>
<td width="300">感知、定位与空间表示</td>
<td width="150">1</td>
<td width="600">维护机器人相对环境的位置。</td>
</tr>
<tr>
<td width="360"><a href="topics/06-04.md">三维重建与场景表征</a></td>
<td width="300">感知、定位与空间表示</td>
<td width="150">0</td>
<td width="600">构建可查询的空间模型。</td>
</tr>
<tr>
<td width="360"><a href="topics/06-05.md">语义地图与空间记忆</a></td>
<td width="300">感知、定位与空间表示</td>
<td width="150">0</td>
<td width="600">保留跨时刻、跨任务的场景知识。</td>
</tr>
<tr>
<td width="360"><a href="topics/06-06.md">主动感知与不确定性</a></td>
<td width="300">感知、定位与空间表示</td>
<td width="150">0</td>
<td width="600">决定下一步看哪里及何时重新观测。</td>
</tr>
<tr>
<td width="360"><a href="topics/07-01.md">运动学与轨迹规划</a></td>
<td width="300">运动控制与动作学习</td>
<td width="150">0</td>
<td width="600">寻找可达、无碰撞的动作路径。</td>
</tr>
<tr>
<td width="360"><a href="topics/07-02.md">模型预测与最优控制</a></td>
<td width="300">运动控制与动作学习</td>
<td width="150">0</td>
<td width="600">在动力学约束下滚动调整动作。</td>
</tr>
<tr>
<td width="360"><a href="topics/07-03.md">力控、阻抗与接触控制</a></td>
<td width="300">运动控制与动作学习</td>
<td width="150">0</td>
<td width="600">在接触中控制力与柔顺性。</td>
</tr>
<tr>
<td width="360"><a href="topics/07-04.md">腿式与全身协调控制</a></td>
<td width="300">运动控制与动作学习</td>
<td width="150">0</td>
<td width="600">协调平衡、行走、手臂与接触点。</td>
</tr>
<tr>
<td width="360"><a href="topics/07-05.md">模仿与扩散、流动作策略</a></td>
<td width="300">运动控制与动作学习</td>
<td width="150">1</td>
<td width="600">从示范学习多模态动作分布。</td>
</tr>
<tr>
<td width="360"><a href="topics/07-06.md">强化学习与在线适应</a></td>
<td width="300">运动控制与动作学习</td>
<td width="150">0</td>
<td width="600">通过反馈改进策略并适应变化。</td>
</tr>
<tr>
<td width="360"><a href="topics/08-01.md">视觉语言动作基础模型</a></td>
<td width="300">机器人模型、推理与规划</td>
<td width="150">4</td>
<td width="600">从多模态任务输入产生机器人动作。</td>
</tr>
<tr>
<td width="360"><a href="topics/08-02.md">世界模型与行动后果预测</a></td>
<td width="300">机器人模型、推理与规划</td>
<td width="150">5</td>
<td width="600">预测动作后的环境状态。</td>
</tr>
<tr>
<td width="360"><a href="topics/08-03.md">任务分解与技能规划</a></td>
<td width="300">机器人模型、推理与规划</td>
<td width="150">1</td>
<td width="600">把需求拆成有约束的可执行步骤。</td>
</tr>
<tr>
<td width="360"><a href="topics/08-04.md">长期记忆与个性化</a></td>
<td width="300">机器人模型、推理与规划</td>
<td width="150">0</td>
<td width="600">利用历史经验适应用户与环境。</td>
</tr>
<tr>
<td width="360"><a href="topics/08-05.md">失败监测与恢复</a></td>
<td width="300">机器人模型、推理与规划</td>
<td width="150">0</td>
<td width="600">识别偏离目标并重新组织行动。</td>
</tr>
<tr>
<td width="360"><a href="topics/08-06.md">分层智能体与混合系统</a></td>
<td width="300">机器人模型、推理与规划</td>
<td width="150">0</td>
<td width="600">连接慢推理、快速动作与传统控制。</td>
</tr>
<tr>
<td width="360"><a href="topics/09-01.md">操作系统与通信中间件</a></td>
<td width="300">系统软件与集成平台</td>
<td width="150">3</td>
<td width="600">组织进程、消息与分布式组件。</td>
</tr>
<tr>
<td width="360"><a href="topics/09-02.md">驱动、硬件抽象与控制接口</a></td>
<td width="300">系统软件与集成平台</td>
<td width="150">0</td>
<td width="600">统一传感读取与执行器命令。</td>
</tr>
<tr>
<td width="360"><a href="topics/09-03.md">导航与操作软件栈</a></td>
<td width="300">系统软件与集成平台</td>
<td width="150">0</td>
<td width="600">组合感知、规划与控制模块。</td>
</tr>
<tr>
<td width="360"><a href="topics/09-04.md">技能库、行为树与工作流</a></td>
<td width="300">系统软件与集成平台</td>
<td width="150">3</td>
<td width="600">表达任务顺序、并发与恢复。</td>
</tr>
<tr>
<td width="360"><a href="topics/09-05.md">开发、调试与可观测性</a></td>
<td width="300">系统软件与集成平台</td>
<td width="150">0</td>
<td width="600">解释系统运行中的数据与故障。</td>
</tr>
<tr>
<td width="360"><a href="topics/09-06.md">设施对接与多机协调</a></td>
<td width="300">系统软件与集成平台</td>
<td width="150">0</td>
<td width="600">让机器人与电梯、门禁、机队协同。</td>
</tr>
<tr>
<td width="360"><a href="topics/10-01.md">遥操作与示范采集</a></td>
<td width="300">数据采集与治理</td>
<td width="150">10</td>
<td width="600">获得包含观察和动作的训练轨迹。</td>
</tr>
<tr>
<td width="360"><a href="topics/10-02.md">人类视频与跨本体重定向</a></td>
<td width="300">数据采集与治理</td>
<td width="150">2</td>
<td width="600">利用不同身体产生的动作经验。</td>
</tr>
<tr>
<td width="360"><a href="topics/10-03.md">自动探索与失败采集</a></td>
<td width="300">数据采集与治理</td>
<td width="150">0</td>
<td width="600">补充困难状态与失败恢复数据。</td>
</tr>
<tr>
<td width="360"><a href="topics/10-04.md">多模态同步与标注</a></td>
<td width="300">数据采集与治理</td>
<td width="150">8</td>
<td width="600">对齐视觉、触觉、状态、动作和语言。</td>
</tr>
<tr>
<td width="360"><a href="topics/10-05.md">清洗、版本与数据质量</a></td>
<td width="300">数据采集与治理</td>
<td width="150">2</td>
<td width="600">避免泄漏、重复和质量漂移。</td>
</tr>
<tr>
<td width="360"><a href="topics/10-06.md">数据格式、共享与数据闭环</a></td>
<td width="300">数据采集与治理</td>
<td width="150">2</td>
<td width="600">让不同团队与机器人复用数据。</td>
</tr>
<tr>
<td width="360"><a href="topics/11-01.md">物理引擎与接触求解</a></td>
<td width="300">仿真与训练基础设施</td>
<td width="150">1</td>
<td width="600">计算运动、碰撞与接触响应。</td>
</tr>
<tr>
<td width="360"><a href="topics/11-02.md">数字孪生与资产构建</a></td>
<td width="300">仿真与训练基础设施</td>
<td width="150">1</td>
<td width="600">建立场景、机器人与物体的数字表示。</td>
</tr>
<tr>
<td width="360"><a href="topics/11-03.md">传感仿真与合成数据</a></td>
<td width="300">仿真与训练基础设施</td>
<td width="150">2</td>
<td width="600">生成多模态观测及其标签。</td>
</tr>
<tr>
<td width="360"><a href="topics/11-04.md">并行训练与实验管理</a></td>
<td width="300">仿真与训练基础设施</td>
<td width="150">0</td>
<td width="600">提高策略训练和比较效率。</td>
</tr>
<tr>
<td width="360"><a href="topics/11-05.md">领域随机化与迁移</a></td>
<td width="300">仿真与训练基础设施</td>
<td width="150">0</td>
<td width="600">降低仿真与实机行为差异。</td>
</tr>
<tr>
<td width="360"><a href="topics/11-06.md">软件、硬件在环验证</a></td>
<td width="300">仿真与训练基础设施</td>
<td width="150">0</td>
<td width="600">在上线前测试控制与通信链路。</td>
</tr>
<tr>
<td width="360"><a href="topics/12-01.md">能力基准与任务评测</a></td>
<td width="300">评测、安全与部署运维</td>
<td width="150">1</td>
<td width="600">以可比条件衡量能力。</td>
</tr>
<tr>
<td width="360"><a href="topics/12-02.md">可靠性与长时程测试</a></td>
<td width="300">评测、安全与部署运维</td>
<td width="150">0</td>
<td width="600">发现连续运行中的累积故障。</td>
</tr>
<tr>
<td width="360"><a href="topics/12-03.md">安全约束与系统防护</a></td>
<td width="300">评测、安全与部署运维</td>
<td width="150">0</td>
<td width="600">限制危险动作和失控传播。</td>
</tr>
<tr>
<td width="360"><a href="topics/12-04.md">端侧部署与模型更新</a></td>
<td width="300">评测、安全与部署运维</td>
<td width="150">1</td>
<td width="600">把模型稳定运行在目标设备上。</td>
</tr>
<tr>
<td width="360"><a href="topics/12-05.md">接管、诊断与恢复</a></td>
<td width="300">评测、安全与部署运维</td>
<td width="150">1</td>
<td width="600">在失败时维持可控运行。</td>
</tr>
<tr>
<td width="360"><a href="topics/12-06.md">机队、服务与运营指标</a></td>
<td width="300">评测、安全与部署运维</td>
<td width="150">0</td>
<td width="600">管理多机任务与长期服务。</td>
</tr>
<tr>
<td width="360"><a href="topics/13-01.md">结构材料与精密制造</a></td>
<td width="300">制造、集成与交付</td>
<td width="150">6</td>
<td width="600">实现强度、重量与尺寸要求。</td>
</tr>
<tr>
<td width="360"><a href="topics/13-02.md">增材制造与快速迭代</a></td>
<td width="300">制造、集成与交付</td>
<td width="150">1</td>
<td width="600">缩短设计验证与样件制造周期。</td>
</tr>
<tr>
<td width="360"><a href="topics/13-03.md">装配、标定与出厂测试</a></td>
<td width="300">制造、集成与交付</td>
<td width="150">0</td>
<td width="600">降低个体间性能差异。</td>
</tr>
<tr>
<td width="360"><a href="topics/13-04.md">供应链与配置管理</a></td>
<td width="300">制造、集成与交付</td>
<td width="150">0</td>
<td width="600">控制部件变化及其系统影响。</td>
</tr>
<tr>
<td width="360"><a href="topics/13-05.md">系统集成与工位改造</a></td>
<td width="300">制造、集成与交付</td>
<td width="150">0</td>
<td width="600">把机器人接入真实业务流程。</td>
</tr>
<tr>
<td width="360"><a href="topics/13-06.md">维护、培训与生命周期</a></td>
<td width="300">制造、集成与交付</td>
<td width="150">1</td>
<td width="600">保持设备与人员长期可用。</td>
</tr>
<tr>
<td width="360"><a href="topics/14-01.md">制造、装配与工艺操作</a></td>
<td width="300">应用与解决方案</td>
<td width="150">0</td>
<td width="600">完成取放、装配、检测与加工工序。</td>
</tr>
<tr>
<td width="360"><a href="topics/14-02.md">仓储物流与搬运配送</a></td>
<td width="300">应用与解决方案</td>
<td width="150">0</td>
<td width="600">连接存储、分拣、搬运与交付。</td>
</tr>
<tr>
<td width="360"><a href="topics/14-03.md">商业服务与楼宇作业</a></td>
<td width="300">应用与解决方案</td>
<td width="150">1</td>
<td width="600">完成清洁、配送、接待等日常服务。</td>
</tr>
<tr>
<td width="360"><a href="topics/14-04.md">家庭消费与陪伴</a></td>
<td width="300">应用与解决方案</td>
<td width="150">2</td>
<td width="600">适应非结构化家庭及不同用户。</td>
</tr>
<tr>
<td width="360"><a href="topics/14-05.md">能源、农业与特种作业</a></td>
<td width="300">应用与解决方案</td>
<td width="150">7</td>
<td width="600">在复杂或危险环境中感知和作业。</td>
</tr>
<tr>
<td width="360"><a href="topics/14-06.md">医疗、康复与辅助行动</a></td>
<td width="300">应用与解决方案</td>
<td width="150">4</td>
<td width="600">在人的身体与临床工作流中提供辅助。</td>
</tr>
</tbody>
</table>

## 完整来源分类资料

<table width="880">
<thead>
<tr>
<th width="540">来源分类</th>
<th width="160">技术上下文数</th>
<th width="180">展项关联数</th>
</tr>
</thead>
<tbody>
<tr>
<td width="540"><a href="references/01-01.md">双足与通用人形机器人</a></td>
<td width="160">36</td>
<td width="180">112</td>
</tr>
<tr>
<td width="540"><a href="references/01-02.md">轮式双臂与移动操作机器人</a></td>
<td width="160">25</td>
<td width="180">43</td>
</tr>
<tr>
<td width="540"><a href="references/01-03.md">四足与轮足机器人</a></td>
<td width="160">12</td>
<td width="180">35</td>
</tr>
<tr>
<td width="540"><a href="references/01-04.md">小型教学与开放机器人平台</a></td>
<td width="160">5</td>
<td width="180">17</td>
</tr>
<tr>
<td width="540"><a href="references/01-05.md">仿生与交互人形机器人</a></td>
<td width="160">6</td>
<td width="180">14</td>
</tr>
<tr>
<td width="540"><a href="references/01-06.md">具身方案与未明确形态平台</a></td>
<td width="160">3</td>
<td width="180">3</td>
</tr>
<tr>
<td width="540"><a href="references/02-01.md">工业机械臂与工业机器人</a></td>
<td width="160">3</td>
<td width="180">12</td>
</tr>
<tr>
<td width="540"><a href="references/02-02.md">协作机械臂与自适应力控</a></td>
<td width="160">4</td>
<td width="180">6</td>
</tr>
<tr>
<td width="540"><a href="references/02-03.md">桌面机械臂与教学机械臂</a></td>
<td width="160">1</td>
<td width="180">3</td>
</tr>
<tr>
<td width="540"><a href="references/02-04.md">焊接与柔性制造集成</a></td>
<td width="160">3</td>
<td width="180">1</td>
</tr>
<tr>
<td width="540"><a href="references/03-01.md">家用商用及户外清洁</a></td>
<td width="160">3</td>
<td width="180">2</td>
</tr>
<tr>
<td width="540"><a href="references/03-02.md">酒店餐饮与楼宇配送</a></td>
<td width="160">2</td>
<td width="180">17</td>
</tr>
<tr>
<td width="540"><a href="references/03-03.md">饮品制作与无人零售</a></td>
<td width="160">1</td>
<td width="180">5</td>
</tr>
<tr>
<td width="540"><a href="references/03-04.md">家庭陪伴与桌面交互</a></td>
<td width="160">4</td>
<td width="180">7</td>
</tr>
<tr>
<td width="540"><a href="references/03-05.md">导览接待与文旅服务</a></td>
<td width="160">4</td>
<td width="180">7</td>
</tr>
<tr>
<td width="540"><a href="references/03-06.md">移动充电服务</a></td>
<td width="160">1</td>
<td width="180">1</td>
</tr>
<tr>
<td width="540"><a href="references/04-01.md">仓储搬运与装卸机器人</a></td>
<td width="160">5</td>
<td width="180">9</td>
</tr>
<tr>
<td width="540"><a href="references/04-02.md">末端配送机器人</a></td>
<td width="160">2</td>
<td width="180">6</td>
</tr>
<tr>
<td width="540"><a href="references/04-03.md">移动底盘与自主导航载体</a></td>
<td width="160">4</td>
<td width="180">20</td>
</tr>
<tr>
<td width="540"><a href="references/04-04.md">消防排爆与应急救援</a></td>
<td width="160">3</td>
<td width="180">28</td>
</tr>
<tr>
<td width="540"><a href="references/04-05.md">能源工业与安防巡检</a></td>
<td width="160">6</td>
<td width="180">31</td>
</tr>
<tr>
<td width="540"><a href="references/04-06.md">爬壁与高危设施维护</a></td>
<td width="160">2</td>
<td width="180">10</td>
</tr>
<tr>
<td width="540"><a href="references/04-07.md">农业巡检与采摘作业</a></td>
<td width="160">1</td>
<td width="180">6</td>
</tr>
<tr>
<td width="540"><a href="references/05-01.md">手术机器人</a></td>
<td width="160">2</td>
<td width="180">2</td>
</tr>
<tr>
<td width="540"><a href="references/05-02.md">康复助残与轮椅机器人</a></td>
<td width="160">1</td>
<td width="180">3</td>
</tr>
<tr>
<td width="540"><a href="references/05-03.md">外骨骼与运动助力</a></td>
<td width="160">4</td>
<td width="180">15</td>
</tr>
<tr>
<td width="540"><a href="references/05-04.md">脑机接口与肌电仿生手</a></td>
<td width="160">4</td>
<td width="180">6</td>
</tr>
<tr>
<td width="540"><a href="references/06-01.md">灵巧手与仿生末端</a></td>
<td width="160">9</td>
<td width="180">45</td>
</tr>
<tr>
<td width="540"><a href="references/06-02.md">夹爪气动与工具快换</a></td>
<td width="160">3</td>
<td width="180">8</td>
</tr>
<tr>
<td width="540"><a href="references/06-03.md">一体化关节与执行模组</a></td>
<td width="160">14</td>
<td width="180">70</td>
</tr>
<tr>
<td width="540"><a href="references/06-04.md">无框微型与直驱电机</a></td>
<td width="160">10</td>
<td width="180">40</td>
</tr>
<tr>
<td width="540"><a href="references/06-05.md">伺服驱动与运动控制</a></td>
<td width="160">4</td>
<td width="180">8</td>
</tr>
<tr>
<td width="540"><a href="references/06-06.md">谐波减速器</a></td>
<td width="160">7</td>
<td width="180">16</td>
</tr>
<tr>
<td width="540"><a href="references/06-07.md">行星摆线与精密减速器</a></td>
<td width="160">4</td>
<td width="180">7</td>
</tr>
<tr>
<td width="540"><a href="references/06-08.md">丝杠与线性执行器</a></td>
<td width="160">5</td>
<td width="180">6</td>
</tr>
<tr>
<td width="540"><a href="references/06-09.md">轴承与精密支承</a></td>
<td width="160">7</td>
<td width="180">21</td>
</tr>
<tr>
<td width="540"><a href="references/06-10.md">制动器与离合器</a></td>
<td width="160">1</td>
<td width="180">3</td>
</tr>
<tr>
<td width="540"><a href="references/06-11.md">拖链电缆与线束</a></td>
<td width="160">2</td>
<td width="180">1</td>
</tr>
<tr>
<td width="540"><a href="references/06-12.md">密封与关节防护</a></td>
<td width="160">1</td>
<td width="180">10</td>
</tr>
<tr>
<td width="540"><a href="references/07-01.md">六维力与关节扭矩传感</a></td>
<td width="160">9</td>
<td width="180">51</td>
</tr>
<tr>
<td width="540"><a href="references/07-02.md">触觉与柔性电子皮肤</a></td>
<td width="160">12</td>
<td width="180">29</td>
</tr>
<tr>
<td width="540"><a href="references/07-03.md">深度相机与三维视觉</a></td>
<td width="160">3</td>
<td width="180">6</td>
</tr>
<tr>
<td width="540"><a href="references/07-04.md">激光雷达与测距</a></td>
<td width="160">5</td>
<td width="180">5</td>
</tr>
<tr>
<td width="540"><a href="references/07-05.md">惯性导航与姿态传感</a></td>
<td width="160">1</td>
<td width="180">0</td>
</tr>
<tr>
<td width="540"><a href="references/07-06.md">编码器与磁位置传感</a></td>
<td width="160">4</td>
<td width="180">4</td>
</tr>
<tr>
<td width="540"><a href="references/07-07.md">图像传感与视觉识别</a></td>
<td width="160">3</td>
<td width="180">6</td>
</tr>
<tr>
<td width="540"><a href="references/07-08.md">SLAM与空间感知模组</a></td>
<td width="160">4</td>
<td width="180">12</td>
</tr>
<tr>
<td width="540"><a href="references/07-09.md">光学动捕与三维动作感知</a></td>
<td width="160">1</td>
<td width="180">0</td>
</tr>
<tr>
<td width="540"><a href="references/08-01.md">AI芯片与异构计算</a></td>
<td width="160">4</td>
<td width="180">7</td>
</tr>
<tr>
<td width="540"><a href="references/08-02.md">边缘计算与机器人控制器</a></td>
<td width="160">6</td>
<td width="180">12</td>
</tr>
<tr>
<td width="540"><a href="references/08-03.md">MCU与功率半导体</a></td>
<td width="160">2</td>
<td width="180">0</td>
</tr>
<tr>
<td width="540"><a href="references/08-04.md">工业通信与无线连接</a></td>
<td width="160">2</td>
<td width="180">7</td>
</tr>
<tr>
<td width="540"><a href="references/08-05.md">电子元器件与传感芯片</a></td>
<td width="160">2</td>
<td width="180">1</td>
</tr>
<tr>
<td width="540"><a href="references/08-06.md">电池BMS与智能充电</a></td>
<td width="160">2</td>
<td width="180">11</td>
</tr>
<tr>
<td width="540"><a href="references/08-07.md">电源与功率驱动模块</a></td>
<td width="160">1</td>
<td width="180">2</td>
</tr>
<tr>
<td width="540"><a href="references/09-01.md">具身基础模型与行为策略</a></td>
<td width="160">2</td>
<td width="180">4</td>
</tr>
<tr>
<td width="540"><a href="references/09-02.md">世界模型与因果推理</a></td>
<td width="160">3</td>
<td width="180">9</td>
</tr>
<tr>
<td width="540"><a href="references/09-03.md">遥操作与数据采集工具链</a></td>
<td width="160">3</td>
<td width="180">3</td>
</tr>
<tr>
<td width="540"><a href="references/09-04.md">仿真合成数据与评测</a></td>
<td width="160">2</td>
<td width="180">9</td>
</tr>
<tr>
<td width="540"><a href="references/09-05.md">机器人操作系统与技能平台</a></td>
<td width="160">2</td>
<td width="180">4</td>
</tr>
<tr>
<td width="540"><a href="references/09-06.md">企业智能体与AI服务</a></td>
<td width="160">1</td>
<td width="180">0</td>
</tr>
<tr>
<td width="540"><a href="references/10-01.md">金属增材制造</a></td>
<td width="160">1</td>
<td width="180">1</td>
</tr>
<tr>
<td width="540"><a href="references/10-02.md">机床与精密加工装备</a></td>
<td width="160">1</td>
<td width="180">2</td>
</tr>
<tr>
<td width="540"><a href="references/10-03.md">本体ODM与精密制造</a></td>
<td width="160">2</td>
<td width="180">6</td>
</tr>
<tr>
<td width="540"><a href="references/10-04.md">粘接导热与功能材料</a></td>
<td width="160">2</td>
<td width="180">9</td>
</tr>
<tr>
<td width="540"><a href="references/10-05.md">显示与可穿戴交互设备</a></td>
<td width="160">1</td>
<td width="180">0</td>
</tr>
<tr>
<td width="540"><a href="references/11-01.md">高校研究院与科研团队</a></td>
<td width="160">6</td>
<td width="180">27</td>
</tr>
<tr>
<td width="540"><a href="references/11-02.md">创新中心中试与产业运营</a></td>
<td width="160">6</td>
<td width="180">17</td>
</tr>
<tr>
<td width="540"><a href="references/11-03.md">协会与联合展区</a></td>
<td width="160">4</td>
<td width="180">15</td>
</tr>
<tr>
<td width="540"><a href="references/11-04.md">人才培养与实训</a></td>
<td width="160">1</td>
<td width="180">2</td>
</tr>
</tbody>
</table>

## 归属与维护

型号字段按归档提要逐项归属；混合段落完整保留，包括型号冲突、未核实声明和缺失工况。HumanPlus 关联依据既有论文目录中明确出现的 RH56DFX；其他研究关联在没有单独证据时标为相关路线。

原展项索引的 Magic MA1 名称含垂直制表控制字符，本次恢复完整名称，保留原始写法并规范显示空白，未因控制字符丢弃展项。原文件哈希与恢复说明存入来源记录。
