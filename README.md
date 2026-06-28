# Embodied AI Frontier Survey

更新日期：2026-06-28

这个仓库用于调研具身智能的前沿方向。当前判断：不要把主线押在“再做一个更大的端到端 VLA”上，更值得跟的是 **agent 细粒度规划 + WAM/小策略/传统控制执行 + 端侧安全闭环**。

## 一句话结论

具身智能正在从“模型直接输出动作”转向“分层自主系统”：

```text
用户目标 / 环境状态
        -> 任务理解与细粒度规划 agent
        -> 世界模型 / WAM 做想象、验证、失败预测
        -> 技能库、小 VLA、diffusion policy、MPC 或传统控制执行
        -> 本地低延迟安全闭环
```

这条路线同时覆盖 VLN 的大范围规划、VLA/WAM 的操作动作、轻量化部署和未来单机器人自我决策。

## 读过的 GitHub 仓库

| 仓库 | 读到的核心内容 | 对本调研的用法 |
| --- | --- | --- |
| [Songwxuan/Embodied-AI-Paper-TopConf](https://github.com/Songwxuan/Embodied-AI-Paper-TopConf) | 按 CVPR、ICCV、NeurIPS、ICML、ICLR、RSS、CoRL、ICRA 等会议整理 embodied AI；反复出现 VLA、VLN、World Models、Planning and Reasoning、Navigation、Humanoid、Dexterous、Tactile、Benchmark/Dataset、Accelerating and Deploying。 | 用来确认近年顶会热点，不把具身智能只等同于机械臂 VLA。 |
| [jonyzhang2023/awesome-embodied-vla-va-vln](https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln) | 综合收录 survey、VLA/WAM、VLN、VA 和相关 multimodal learning；2025-2026 的 VLA/WAM 条目明显密集。 | 用作快速总览，观察社区关注点从 VLA 扩展到 WAM、memory、failure recovery、agentic robot。 |
| [OpenMOSS/Awesome-WAM](https://github.com/OpenMOSS/Awesome-WAM) | 把 WAM 分成 Cascaded WAM 和 Joint WAM；进一步分 explicit pixel / implicit latent、autoregressive / diffusion；还整理 world model for imitation learning、RL、evaluation、training data。 | 用来定义 WAM：不是普通 VLA，而是“预测世界 + 生成动作”的桥接层。 |
| [UCSB-AI/awesome-vision-language-navigation](https://github.com/UCSB-AI/awesome-vision-language-navigation) | VLN 按 datasets/benchmarks、evaluation、representation learning、action strategy、navigation planning、asking for help、data-centric learning、prior exploration 分类。 | 用来确认 VLN 的核心还是地图、记忆、规划、探索和纠错，不是低层动作生成。 |
| [DelinQu/awesome-vision-language-action-model](https://github.com/DelinQu/awesome-vision-language-action-model) | 仓库较小但里程碑清晰：RT-1、Diffusion Policy、ACT、RT-2、UniSim、Octo、OpenVLA、RDT-1B、GR-2、pi0、SpatialVLA；还列了 OXE 和 SimplerEnv。 | 用作 VLA 快速时间线。 |
| [yueen-ma/Awesome-VLA](https://github.com/yueen-ma/Awesome-VLA) | VLA survey 配套仓库；区分 generalized VLA 和 large VLA；按 components、world models、reasoning、policy steering、low-level policies、high-level task planners、本体方向整理。其数据文件当前约 395 个 VLA model 条目，2025 年条目最多。 | 用作 VLA taxonomy 主参考，尤其是“VLA 不只是大 VLM 接动作头”。 |

## 调研边界

- CCF-A 线索按 [CCF 人工智能推荐目录](https://www.ccf.org.cn/Academic_Evaluation/AI/) 优先看 AAAI、NeurIPS、ACL、CVPR、ICCV、ICML、IJCAI。
- ICLR、RSS、CoRL、ICRA、IROS 虽然不能简单写成 CCF-A，但对机器人和具身智能非常关键，单独保留。
- 本仓库只记录会改变研究判断的论文、项目和 benchmark，不做全量 awesome list。

## 方向判断

| 主线 | 核心问题 | 当前趋势 | 适合关注的本体 |
| --- | --- | --- | --- |
| VLN | 语言指令驱动的大范围导航和任务规划 | 从离散导航图走向连续环境、物理可执行、跨本体泛化、问询/纠错 | 人形、四足、无人机、无人车、轮式机器人 |
| VLA | 视觉、语言到动作的映射 | 从 RT-2/OpenVLA/pi0 这类大模型路线，扩展到 action tokenizer、diffusion policy、3D/触觉/力觉、多本体动作空间 | 机械臂、双臂、移动操作、灵巧手 |
| WAM | 同时预测未来世界状态和动作 | 从视频/latent world model 到 joint world-action generation，用于规划、验证和失败恢复 | 机械臂为主，正在扩展到双臂、灵巧手和移动操作 |
| Agentic Planning | 让 agent 做任务分解、技能选择、约束生成和重规划 | 规划和执行分离；agent 负责语义，小模型/传统方法负责动作 | 所有需要长程任务和失败恢复的机器人 |
| Lightweight Autonomy | 单机器人本地自决策 | 端侧小模型、量化、缓存、动作 tokenization、低延迟安全回路 | 真实部署机器人 |

## 细分分析

### 1. VLN：从导航 benchmark 到物理本体

VLN 的长期价值在“大范围规划”。经典任务如 [R2R](https://arxiv.org/abs/1711.07280)、[VLN-CE](https://arxiv.org/abs/2004.02857) 和 [VLN survey](https://arxiv.org/abs/2203.12667) 建立了任务和评价框架。

读完 VLN 仓库后，比较清楚的是：VLN 不是在做机械臂动作，而是在解决语言 grounding、地图/图表示、记忆、探索、导航规划、问询和纠错。它可以把本体先抽象成质点，但真正落地时必须考虑本体差异：人形能跨越障碍，四足能上楼梯，无人机有三维运动，无人车有道路规则。

优先跟踪：

- 连续环境 VLN，而不是只在离散 nav graph 上评测。
- 跨本体导航基础模型，如 humanoid、quadruped、drone、vehicle 的统一规划表示。
- 能处理动态障碍、安全约束、失败恢复的 VLN。

### 2. VLA：仍是主战场，但不能只看“大模型更大”

VLA 的代表工作包括 [RT-2](https://arxiv.org/abs/2307.15818)、[OpenVLA](https://arxiv.org/abs/2406.09246)、[Octo](https://arxiv.org/abs/2405.12213)、[pi0](https://arxiv.org/abs/2410.24164)。这些工作说明视觉-语言知识可以转成机器人动作。

但读完 VLA 仓库后，VLA 的真实分叉更多：

- **动作表示**：action chunking、vector quantization、FAST/action tokenizer。
- **策略形式**：transformer policy、diffusion policy、flow matching、hybrid autoregressive + diffusion。
- **感知输入**：RGB、depth、3D point/voxel、tactile、force。
- **本体扩展**：单臂、双臂、移动操作、人形、四足、灵巧手。
- **训练/部署**：post-training、RL fine-tuning、quantization、token cache、real-time decoding。

判断：VLA 适合做动作先验和技能执行器，但不应该默认承担完整任务规划。对真实系统来说，VLA 的问题不是“会不会说”，而是是否低延迟、可恢复、可解释、可跨本体迁移。

### 3. WAM：VLA 和规划之间的桥接层

[Awesome-WAM](https://github.com/OpenMOSS/Awesome-WAM) 的分类很有用：WAM 不只是“世界模型”或“动作模型”，而是把未来状态预测和动作生成放在同一框架中。

关键分类：

- **Cascaded WAM**：先想象未来状态，再从未来状态反推出动作。包括 pixel-space、geometric flow、latent representation 等。
- **Joint WAM**：世界和动作一起生成，包括 autoregressive 和 diffusion-based 路线。
- **World Model for VLA**：用于 imitation learning、reinforcement learning、policy evaluation。
- **Evaluation**：不仅看视觉质量，还要看物理常识、动作可行性、真实策略表现。

代表线索：

- [Video Language Planning](https://arxiv.org/abs/2310.10625)：用视频语言规划长程操作。
- [Latent Action Pretraining](https://arxiv.org/abs/2410.11758)：从视频中学习 latent action。
- [Video Prediction Policy](https://arxiv.org/abs/2412.14803)：用预测式视觉表征做策略。
- WorldVLA、RynnVLA、DreamZero、Unified Diffusion VLA 等新工作说明 WAM 正在和 VLA 合流。

判断：WAM 最适合做“规划后果验证”和“失败恢复”。它不一定要替代底层控制，而是给 agent 一个可预测、可检验的中间层。

### 4. Agentic Planning：最适合近期落地

从 [SayCan](https://arxiv.org/abs/2204.01691)、[Code as Policies](https://arxiv.org/abs/2209.07753)、[VoxPoser](https://voxposer.github.io/) 到 [ReKep](https://rekep-robot.github.io/)，一个清晰趋势是：让大模型做任务分解、约束生成、技能选择、失败解释；让底层小模型、技能库或传统控制器执行。

这个方向比单体 VLA 更适合真实机器人：

- 规划错、感知错、动作错可以分层定位。
- 可以复用已有运动规划、MPC、控制器和技能库。
- 数据需求低于端到端 VLA。
- 高层可以慢，底层必须快，符合真实系统约束。

风险是 agent 可能规划出不可执行动作，所以必须配 affordance、constraint checker、world model 或执行监控。

### 5. 轻量化：从“优化项”变成“部署前提”

VLA 列表里 2025 年高效化条目非常多：SmolVLA、TinyVLA、VLA-Adapter、BitVLA、ActQuant、token cache、early-exit、real-time decoding、FAST/action tokenizer。这说明轻量化已经不是附属方向。

轻量化要分三层看：

| 层级 | 应该轻量化什么 |
| --- | --- |
| 高层规划 | 用小模型、缓存、检索和结构化任务图减少反复大模型推理 |
| 动作生成 | action tokenizer、chunking、diffusion/flow policy 加速、策略蒸馏 |
| 安全闭环 | 本地传感、碰撞检测、力控/速度限制、紧急停止必须脱离云端 |

判断：未来单个机器人必须有本地自决策能力。云端大模型可以增强，但不能成为安全闭环的唯一依赖。

## 推荐研究路线

### 路线 A：Agentic Planning + WAM 验证 + 小策略执行

这是当前最推荐的路线。

目标：agent 把用户目标拆成可执行子任务；WAM 预测候选动作后果；小 VLA、diffusion policy、MPC 或传统控制器执行；失败后由监控模块触发重规划。

为什么值得做：

- 覆盖 VLN 的长程规划和 VLA/WAM 的动作层。
- 比端到端大 VLA 更容易调试和迁移。
- 更符合轻量化部署。
- 可以在机械臂任务上先验证，再扩展到移动操作、人形或四足。

### 路线 B：跨本体 VLN / Navigation Foundation Model

目标：统一语言任务表示和地图/记忆层，适配人形、四足、无人机、无人车等不同本体。

关键问题：

- 同一 high-level route 如何变成本体相关 motion constraint。
- 如何把语言目标、地图、可通行区域和动态障碍统一表示。
- 如何从失败中恢复，而不是只报告导航成功率。

### 路线 C：端侧轻量自主决策栈

目标：把大模型能力压成机器人本地可运行的分层系统。

关键问题：

- 小模型负责状态判断、技能选择、异常检测。
- 低层控制器负责实时执行和安全。
- 大模型只做离线知识、慢速规划或云端增强。
- 评价指标必须包含延迟、功耗、断网表现和失败恢复。

## 代表论文和项目矩阵

| 方向 | 工作 | 为什么重要 |
| --- | --- | --- |
| VLN | [R2R](https://arxiv.org/abs/1711.07280) | VLN 基础 benchmark。 |
| VLN | [VLN-CE](https://arxiv.org/abs/2004.02857) | 从离散图走向连续环境。 |
| VLN | [VLN Survey](https://arxiv.org/abs/2203.12667) | 建立 VLN 任务、方法、评价体系。 |
| VLA | [RT-1](https://arxiv.org/abs/2212.06817) | 大规模真实机器人控制数据和 transformer policy 的起点。 |
| VLA | [RT-2](https://arxiv.org/abs/2307.15818) | 把 web-scale VLM 知识迁移到机器人控制。 |
| VLA | [Open X-Embodiment / RT-X](https://arxiv.org/abs/2310.08864) | 跨机器人数据和模型泛化的重要基础。 |
| VLA | [Octo](https://arxiv.org/abs/2405.12213) | 开源 generalist robot policy。 |
| VLA | [OpenVLA](https://arxiv.org/abs/2406.09246) | 开源 large VLA baseline。 |
| VLA | [pi0](https://arxiv.org/abs/2410.24164) | VLA + flow matching 的代表。 |
| VLA | [TinyVLA](https://arxiv.org/abs/2409.12514) | 快速、数据高效的小型 VLA。 |
| VLA | [SmolVLA](https://arxiv.org/abs/2506.01844) | affordable/efficient robotics 方向。 |
| WAM | [World Action Models](https://arxiv.org/abs/2605.12090) | WAM taxonomy 主入口。 |
| WAM | [Video Language Planning](https://arxiv.org/abs/2310.10625) | 用视频语言做长程操作规划。 |
| WAM | [Latent Action Pretraining](https://arxiv.org/abs/2410.11758) | 从视频中学习 latent action，缓解动作数据稀缺。 |
| WAM | [Video Prediction Policy](https://arxiv.org/abs/2412.14803) | 预测式视觉表征做通用机器人策略。 |
| Agentic | [SayCan](https://arxiv.org/abs/2204.01691) | LLM 规划 + affordance 约束。 |
| Agentic | [Code as Policies](https://arxiv.org/abs/2209.07753) | LLM 生成可执行控制程序。 |
| Agentic | [VoxPoser](https://voxposer.github.io/) | 语言模型生成 3D value map，可接传统规划。 |
| Agentic | [ReKep](https://rekep-robot.github.io/) | 用关系关键点约束做可调试操作规划。 |
| Benchmark | [OXE](https://robotics-transformer-x.github.io/) | 跨本体机器人数据基础。 |
| Benchmark | [SimplerEnv](https://github.com/simpler-env/SimplerEnv) | real-to-sim 评测入口。 |

## 近期跟踪优先级

1. **WAM 是否真的提升泛化和失败恢复**：重点看 WAM 评测是否包含 action plausibility、real-device policy、failure recovery。
2. **Agentic planning 是否能落到真实执行**：重点看是否有 affordance、constraint、monitor，而不是只生成好看的任务步骤。
3. **VLN 是否走向物理可执行**：重点看连续环境、真实机器人、跨本体约束。
4. **VLA 是否轻量化和可部署**：重点看 latency、action tokenization、quantization、early exit、edge device。
5. **灵巧手和触觉是否进入主线**：VLA/WAM 目前以机械臂为主，灵巧手需要触觉、力控、接触建模。

## 后续更新规则

每次新增论文，只回答五个问题：

1. 它属于 VLN、VLA、WAM、agentic planning、lightweight autonomy 中哪一类？
2. 它的本体是什么：质点、轮式、四足、无人机、人形、机械臂、双臂、灵巧手？
3. 它解决的是规划、世界预测、动作生成、执行控制、失败恢复还是部署效率？
4. 它是否有真实机器人、代码、benchmark 或可复现实验？
5. 它是否支持“agent 规划 + 小模型/传统控制执行”的系统路线？

不满足这些问题的论文，暂时不收进主表。
