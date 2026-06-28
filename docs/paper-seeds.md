# 论文和资料种子

这页只放起步入口。更完整的论文列表优先去已有仓库看，本仓库只保留会影响方向判断的线索。

## 现有 GitHub 索引

| 资料源 | 适合看什么 |
| --- | --- |
| [Embodied-AI-Paper-TopConf](https://github.com/Songwxuan/Embodied-AI-Paper-TopConf) | 近年 CVPR、ICCV、NeurIPS、ICML、ICLR、RSS、CoRL、ICRA 等顶会 embodied AI 论文 |
| [awesome-embodied-vla-va-vln](https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln) | VLA、视觉 agent、VLN 的综合入口 |
| [Awesome-WAM](https://github.com/OpenMOSS/Awesome-WAM) | World Action Model 的 taxonomy、benchmark 和论文博客 |
| [awesome-vision-language-navigation](https://github.com/UCSB-AI/awesome-vision-language-navigation) | VLN 的任务、数据集、方法和 survey |
| [awesome-vision-language-action-model](https://github.com/DelinQu/awesome-vision-language-action-model) | VLA 近期论文 |
| [Awesome-VLA](https://github.com/yueen-ma/Awesome-VLA) | VLA 论文和项目补充 |

## 代表性论文入口

| 方向 | 论文/项目 | 为什么先看 |
| --- | --- | --- |
| VLN | [Vision-and-Language Navigation: A Survey of Tasks, Methods, and Future Directions](https://arxiv.org/abs/2203.12667) | 先建立 VLN 的任务、数据集和评价框架 |
| VLN | [R2R: Vision-and-Language Navigation in Real Environments](https://arxiv.org/abs/1711.07280) | VLN 基础 benchmark |
| VLN | [VLN-CE: Beyond the Nav-Graph](https://arxiv.org/abs/2004.02857) | 从离散图走向连续环境 |
| VLA | [RT-2](https://arxiv.org/abs/2307.15818) | 早期高影响力 VLA 路线：把 web-scale VLM 知识迁移到机器人控制 |
| VLA | [OpenVLA](https://arxiv.org/abs/2406.09246) | 开源 generalist VLA 的重要入口 |
| VLA | [Octo](https://arxiv.org/abs/2405.12213) | 开源通用机器人策略，适合看数据和策略泛化 |
| VLA | [pi0](https://arxiv.org/abs/2410.24164) | VLA + flow matching 的通用机器人控制方向 |
| WAM | [World Action Models: The Next Frontier in Embodied AI](https://arxiv.org/abs/2605.12090) | WAM taxonomy 的直接入口 |
| WAM | [Video Language Planning](https://arxiv.org/abs/2310.10625) | 用视频/语言做长程操作规划 |
| WAM | [Latent Action Pretraining from Videos](https://arxiv.org/abs/2410.11758) | 从视频学习 latent action，连接视频世界模型和动作 |
| WAM | [Video Prediction Policy](https://arxiv.org/abs/2412.14803) | 用预测式视觉表征做机器人策略 |
| Agentic | [SayCan](https://arxiv.org/abs/2204.01691) | 用语言模型规划，高层选择由 affordance 约束 |
| Agentic | [Code as Policies](https://arxiv.org/abs/2209.07753) | 让 LLM 生成可执行控制程序 |
| Agentic | [VoxPoser](https://voxposer.github.io/) | 语言模型生成 3D value maps，底层仍可接传统规划/控制 |
| Agentic | [Demonstration-Free Robotic Control via LLM Agents](https://arxiv.org/abs/2601.20334) | 代表“agent 规划 + 无需大规模演示数据”的方向 |

## 近年顶会跟踪建议

优先从这些标签筛：

- `Vision-Language-Action Models`
- `Vision-Language-Navigation Models`
- `World Models`
- `Planning and Reasoning`
- `Humanoid`
- `Dexterous Manipulation`
- `Accelerating and Deploying`
- `Benchmark and Dataset`

判断一篇论文是否值得加入本仓库：

1. 是否能解释 VLN、VLA/WAM、agentic planning 或轻量化中的一个关键变化。
2. 是否有真实机器人或接近真实部署的证据。
3. 是否给出可复现代码、benchmark 或失败分析。
