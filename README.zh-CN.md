<div align="center">

# 🤖 具身智能论文精选

**围绕 VLN、VLA、WAM、规划、本体扩展和部署评测整理的顶会具身智能研究地图。**

[英文](README.md) | 中文

[![精选](https://img.shields.io/badge/Awesome-Embodied%20AI-fc60a8?style=for-the-badge&label=%E7%B2%BE%E9%80%89&message=%E5%85%B7%E8%BA%AB%E6%99%BA%E8%83%BD)](https://awesome.re)
[![条目数](https://img.shields.io/badge/Survey%20Entries-767-0984e3?style=for-the-badge&label=%E6%9D%A1%E7%9B%AE%E6%95%B0)](README.zh-CN.md)
[![最近提交](https://img.shields.io/github/last-commit/neardws/awesome-embodied-ai-papers?style=for-the-badge&color=00b894&label=%E6%9C%80%E8%BF%91%E6%8F%90%E4%BA%A4)](https://github.com/neardws/awesome-embodied-ai-papers/commits)
[![星标](https://img.shields.io/github/stars/neardws/awesome-embodied-ai-papers?style=for-the-badge&color=fdcb6e&logo=github&label=%E6%98%9F%E6%A0%87)](https://github.com/neardws/awesome-embodied-ai-papers/stargazers)
[![分支](https://img.shields.io/github/forks/neardws/awesome-embodied-ai-papers?style=for-the-badge&color=e17055&logo=github&label=%E5%88%86%E6%94%AF)](https://github.com/neardws/awesome-embodied-ai-papers/network/members)

最近一次已记录资源核查：2026-07-13 · 文档整理：2026-09-08

</div>


主表共 **767 条分类条目**，覆盖 **6 个方向、29 个子方向**；另有 **7 条补充线索**。条目按分类表行计数，非跨方向去重论文数。来源和硬件核查日期见对应页面。

> [!NOTE]
> 条目范围限定为已读公开来源中可核验的论文，覆盖 CCF-A 会议以及 ICRA/IROS 等机器人传统强会。

> [!TIP]
> 如果有遗漏论文或资源，可以通过议题或合并请求补充。

## 内容导航

- [总体判断、图示与趋势](docs/zh-CN/overview.md)
- [重点阅读顺序](docs/zh-CN/reading-order.md)
- [数据来源与追溯](docs/zh-CN/sources.md)
- [人形与双足硬件参考](docs/zh-CN/embodiment/hardware.md)
- [源仓库补充条目](docs/zh-CN/additional-sources.md)

## 方向目录

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
