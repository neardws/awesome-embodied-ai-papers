# 论文矩阵

更新日期：2026-06-28

## VLN / 大范围规划

| 工作 | 年份/来源 | 关注点 | 本仓库判断 |
| --- | --- | --- | --- |
| [R2R](https://arxiv.org/abs/1711.07280) | CVPR 2018 | 真实室内环境中的语言导航任务 | VLN 基础 benchmark，适合做历史起点 |
| [VLN-CE](https://arxiv.org/abs/2004.02857) | ECCV 2020 | 从离散导航图走向连续环境 | 重要，因为真实机器人不在离散图上移动 |
| [VLN Survey](https://arxiv.org/abs/2203.12667) | ACL 2022 | VLN 任务、方法、评价综述 | 建议先读，建立问题框架 |
| [NavFoM](https://openreview.net/forum?id=QNDX2YxMa6) | ICLR 2026 | 跨 humanoid、quadruped、drone、vehicle 的导航基础模型 | 和“多本体大范围规划”高度相关 |
| [VLN-PE](https://arxiv.org/abs/2507.13019) | ICCV 2025 | 真实物理具身环境中的 VLN | 优先关注，解决 VLN 物理落地缺口 |
| [AO-Planner](https://arxiv.org/abs/2501.18786) | AAAI 2025 | 用 foundation model 做 continuous VLN affordance planning | 连接 VLN 和 agentic planning |

## VLA / 操作动作模型

| 工作 | 年份/来源 | 关注点 | 本仓库判断 |
| --- | --- | --- | --- |
| [RT-2](https://arxiv.org/abs/2307.15818) | 2023 | 把 web-scale VLM 知识迁移到机器人动作 | VLA 代表起点 |
| [OpenVLA](https://arxiv.org/abs/2406.09246) | 2024 | 开源 generalist VLA | 适合作为开源 baseline |
| [Octo](https://arxiv.org/abs/2405.12213) | RSS 2024 | 开源通用机器人策略 | 适合看数据、策略和跨任务泛化 |
| [pi0](https://arxiv.org/abs/2410.24164) | 2024 | flow matching + 机器人基础模型 | 代表 VLA 与连续控制结合 |
| [VQ-VLA](https://arxiv.org/abs/2507.01016) | ICCV 2025 | vector-quantized action tokenizer | 说明动作表示/离散化仍是 VLA 核心问题 |
| [TinyVLA](https://arxiv.org/abs/2409.12514) | 2024 | 高效小型 VLA | 轻量化方向代表 |

## WAM / 世界动作模型

| 工作 | 年份/来源 | 关注点 | 本仓库判断 |
| --- | --- | --- | --- |
| [World Action Models](https://arxiv.org/abs/2605.12090) | 2026 | WAM taxonomy：世界预测 + 动作生成 | WAM 主入口 |
| [Video Language Planning](https://arxiv.org/abs/2310.10625) | ICLR 2024 | 视频语言规划 | 代表从未来视觉状态推动作 |
| [Latent Action Pretraining](https://arxiv.org/abs/2410.11758) | ICLR 2025 | 从视频学习 latent action | 解决动作标注稀缺问题 |
| [Video Prediction Policy](https://arxiv.org/abs/2412.14803) | ICML 2025 | 预测式视觉表征做机器人策略 | WAM/策略结合的重要线索 |
| [FAST](https://www.physicalintelligence.company/research/fast) | 2025 | 高效动作 tokenization | 和 WAM/VLA 的低延迟动作表示相关 |

## Agentic Planning / 细粒度规划

| 工作 | 年份/来源 | 关注点 | 本仓库判断 |
| --- | --- | --- | --- |
| [SayCan](https://arxiv.org/abs/2204.01691) | 2022 | LLM 规划 + affordance 约束 | agentic robotics 基础范式 |
| [Code as Policies](https://arxiv.org/abs/2209.07753) | 2022 | LLM 生成机器人控制代码 | 代表“规划变程序” |
| [VoxPoser](https://voxposer.github.io/) | CoRL 2023 | 语言模型生成 3D value maps | 能接传统规划/控制，适合真实系统 |
| [ReKep](https://rekep-robot.github.io/) | CoRL 2024 | 关系关键点约束 + 机器人操作 | 比纯 VLA 更结构化，可调试 |
| [Code-as-Monitor](https://arxiv.org/abs/2412.04455) | CVPR 2025 | 机器人失败检测与监控 | 对自我决策和失败恢复很重要 |

## Lightweight Autonomy / 端侧自决策

| 工作 | 年份/来源 | 关注点 | 本仓库判断 |
| --- | --- | --- | --- |
| [SmolVLA](https://huggingface.co/blog/smolvla) | 2025 | 小型高效 VLA | 代表端侧/低成本方向 |
| [TinyVLA](https://arxiv.org/abs/2409.12514) | 2024 | 高效 VLA 训练和推理 | 可作为轻量化 baseline |
| [FAST](https://www.physicalintelligence.company/research/fast) | 2025 | 高效动作 tokenization | 降低动作生成开销 |
| [Gemini Robotics On-Device](https://deepmind.google/models/gemini-robotics/gemini-robotics-on-device/) | 2025 | 本地机器人模型 | 说明产业界也在走端侧自治 |

## 暂不优先

| 类型 | 原因 |
| --- | --- |
| 只做仿真高分、不说明真实机器人约束的工作 | 对“单机器人自我决策”帮助有限 |
| 只做纯视觉生成、不落到动作执行的 world model | 可以作为 WAM 背景，但不是主线 |
| 只有闭源演示、无论文/代码/benchmark 的产品新闻 | 可跟踪，不作为核心证据 |
