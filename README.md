# Embodied AI Frontier Survey

本仓库用于跟踪具身智能的前沿方向，重点不是复刻论文大清单，而是把资料组织成可持续更新的研究判断框架。

更新日期：2026-06-28

## 方向判断

当前先按四条主线跟踪：

| 主线 | 核心问题 | 近期重点 | 备注 |
| --- | --- | --- | --- |
| VLN | 语言指令驱动的大范围导航和任务规划 | 地图/记忆、长程规划、连续环境、安全约束 | 通常把本体简化成质点或移动平台，适合人形、四足、无人机、无人车等 |
| VLA / WAM | 感知、语言和动作之间的闭环 | 机械臂操作、双臂、灵巧手、世界模型、动作先验 | WAM 在这里作为 VLA 之后的一个重要替代/增强范式，不简单等同于 VLA |
| Agentic Planning | 让 agent 做细粒度规划，让技能库、小模型或传统控制执行 | 任务分解、工具调用、技能选择、失败恢复 | 重点假设：比端到端大 VLA 更容易迁移和调试 |
| Lightweight Autonomy | 单机器人本地自决策能力 | 端侧推理、蒸馏、量化、边缘部署、低延迟安全回路 | 未来机器人不能完全依赖云端大模型 |

## 先看什么

- [2026-06-28 调研报告](docs/research-2026-06-28.md)：当前需求下的方向研判、技术路线和建议跟踪顺序。
- [论文矩阵](docs/paper-matrix.md)：按 VLN、VLA/WAM、agentic planning、轻量化整理的代表论文/项目。
- [方向地图](docs/frontier-map.md)：对 VLN、VLA/WAM、agentic planning、轻量化的细分。
- [论文和资料种子](docs/paper-seeds.md)：现有 GitHub 索引、近年顶会线索、代表性论文入口。

## 调研边界

- CCF-A 线索按 [CCF 人工智能推荐目录](https://www.ccf.org.cn/Academic_Evaluation/AI/) 优先看 AAAI、NeurIPS、ACL、CVPR、ICCV、ICML、IJCAI；ICLR、RSS、CoRL、ICRA 等虽然不都等同于 CCF-A，但对具身智能方向判断很关键，会单独保留。
- VLN 先看“大范围规划”，VLA/WAM 先看“操作动作生成”，两者都要关注是否能落到真实机器人。
- 只记录能改变方向判断的论文、代码、benchmark 或 survey，不追求全量收录。

## 更新方法

最省事的更新节奏：

1. 每月看一次 `paper-seeds.md` 里的现有 awesome list。
2. 每个季度补一次 CVPR/ICCV/NeurIPS/ICML/ICLR/RSS/CoRL/ICRA 的 embodied AI 论文。
3. 每次新增论文只回答三个问题：解决什么任务、依赖什么本体、是否更接近可部署自主机器人。

## 关键资料源

- [Songwxuan/Embodied-AI-Paper-TopConf](https://github.com/Songwxuan/Embodied-AI-Paper-TopConf)
- [jonyzhang2023/awesome-embodied-vla-va-vln](https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln)
- [OpenMOSS/Awesome-WAM](https://github.com/OpenMOSS/Awesome-WAM)
- [UCSB-AI/awesome-vision-language-navigation](https://github.com/UCSB-AI/awesome-vision-language-navigation)
- [DelinQu/awesome-vision-language-action-model](https://github.com/DelinQu/awesome-vision-language-action-model)
- [yueen-ma/Awesome-VLA](https://github.com/yueen-ma/Awesome-VLA)
