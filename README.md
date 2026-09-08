<div align="center">

# 🤖 Awesome Embodied AI Papers

**A curated top-conference-oriented map of embodied AI research across VLN, VLA, WAM, planning, embodiment, and deployment.**

English | [Chinese](README.zh-CN.md)

[![Awesome](https://img.shields.io/badge/Awesome-Embodied%20AI-fc60a8?style=for-the-badge)](https://awesome.re)
[![Survey Entries](https://img.shields.io/badge/Survey%20Entries-767-0984e3?style=for-the-badge)](README.md)
[![Last Commit](https://img.shields.io/github/last-commit/neardws/awesome-embodied-ai-papers?style=for-the-badge&color=00b894)](https://github.com/neardws/awesome-embodied-ai-papers/commits)
[![Stars](https://img.shields.io/github/stars/neardws/awesome-embodied-ai-papers?style=for-the-badge&color=fdcb6e&logo=github)](https://github.com/neardws/awesome-embodied-ai-papers/stargazers)
[![Forks](https://img.shields.io/github/forks/neardws/awesome-embodied-ai-papers?style=for-the-badge&color=e17055&logo=github)](https://github.com/neardws/awesome-embodied-ai-papers/network/members)

Latest recorded resource audit: 2026-07-13 · Documentation reorganized: 2026-09-08

</div>


The main tables contain **767 categorized entries** across **6 directions and 29 subdirections**, plus **7 additional leads**. Counts refer to categorized rows, not globally deduplicated papers. Source and hardware verification dates remain documented on their respective pages.

> [!NOTE]
> Entries are scoped to reviewed public sources, including CCF-A venues and robotics flagship conferences such as ICRA/IROS.

> [!TIP]
> Missing papers or resources can be suggested through Issues or Pull Requests.

## Contents

- [Overall view, figures and trends](docs/en/overview.md)
- [Suggested reading order](docs/en/reading-order.md)
- [Sources and provenance](docs/en/sources.md)
- [Humanoid and biped hardware reference](docs/en/embodiment/hardware.md)
- [Additional source entries](docs/en/additional-sources.md)

## Direction index

<table width="1090">
<thead>
<tr>
<th width="240">Direction</th>
<th width="90" nowrap>Entries</th>
<th width="760">Subdirections</th>
</tr>
</thead>
<tbody>
<tr>
<td width="240"><a href="docs/en/vln/README.md">VLN / Large-scale Navigation</a></td>
<td width="90" nowrap>92</td>
<td width="760"><a href="docs/en/vln/continuous.md">Continuous VLN</a> · <a href="docs/en/vln/map-memory.md">Map Memory</a> · <a href="docs/en/vln/physically-executable.md">Physically Executable Navigation</a> · <a href="docs/en/vln/urban-open-world.md">Urban / Open-world Navigation</a> · <a href="docs/en/vln/on-device.md">Low-cost / On-device Navigation</a></td>
</tr>
<tr>
<td width="240"><a href="docs/en/vla/README.md">VLA / Manipulation Policies</a></td>
<td width="90" nowrap>251</td>
<td width="760"><a href="docs/en/vla/generalist.md">generalist VLA</a> · <a href="docs/en/vla/action-representation.md">action representation</a> · <a href="docs/en/vla/diffusion-flow.md">diffusion/flow policy</a> · <a href="docs/en/vla/3d-grounding.md">3D grounding</a> · <a href="docs/en/vla/online-rl.md">online/RL fine-tuning</a> · <a href="docs/en/vla/safety-robustness.md">Safety and Robustness</a></td>
</tr>
<tr>
<td width="240"><a href="docs/en/wam/README.md">WAM / World Models</a></td>
<td width="90" nowrap>70</td>
<td width="760"><a href="docs/en/wam/cascaded.md">cascaded WAM</a> · <a href="docs/en/wam/joint.md">joint WAM</a> · <a href="docs/en/wam/video-latent.md">video/latent world model</a> · <a href="docs/en/wam/for-vla.md">world model for VLA</a></td>
</tr>
<tr>
<td width="240"><a href="docs/en/planning/README.md">Agentic Planning / Reasoning and Planning</a></td>
<td width="90" nowrap>103</td>
<td width="760"><a href="docs/en/planning/task-decomposition.md">Task Decomposition</a> · <a href="docs/en/planning/memory.md">memory</a> · <a href="docs/en/planning/failure-monitor.md">failure monitor</a> · <a href="docs/en/planning/constraint-affordance.md">constraint / affordance planning</a> · <a href="docs/en/planning/self-improving.md">self-improving planning</a></td>
</tr>
<tr>
<td width="240"><a href="docs/en/embodiment/README.md">Embodiment Expansion / Dexterous Manipulation</a></td>
<td width="90" nowrap>146</td>
<td width="760"><a href="docs/en/embodiment/humanoid.md">humanoid</a> · <a href="docs/en/embodiment/bimanual.md">bimanual</a> · <a href="docs/en/embodiment/dexterous-hand.md">dexterous hand</a> · <a href="docs/en/embodiment/tactile-contact.md">tactile/contact-rich</a></td>
</tr>
<tr>
<td width="240"><a href="docs/en/deployment/README.md">Efficiency / Evaluation / Data</a></td>
<td width="90" nowrap>105</td>
<td width="760"><a href="docs/en/deployment/quantization-cache-tokenization.md">quantization/cache/tokenization</a> · <a href="docs/en/deployment/real-time.md">real-time execution</a> · <a href="docs/en/deployment/benchmarks-datasets.md">benchmark/dataset</a> · <a href="docs/en/deployment/sim2real.md">sim2real</a> · <a href="docs/en/deployment/safety-evaluation.md">safety evaluation</a></td>
</tr>
</tbody>
</table>

## Tag Legend

<table width="730">
<thead>
<tr>
<th width="110" nowrap>Tag</th>
<th width="620">Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td width="110" nowrap><code>VLN</code></td>
<td width="620">Large-scale navigation</td>
</tr>
<tr>
<td width="110" nowrap><code>VLA</code></td>
<td width="620">Vision-language-action manipulation policies</td>
</tr>
<tr>
<td width="110" nowrap><code>WAM</code></td>
<td width="620">World action models</td>
</tr>
<tr>
<td width="110" nowrap><code>Planning</code></td>
<td width="620">Task decomposition, memory, failure recovery, and constrained planning</td>
</tr>
<tr>
<td width="110" nowrap><code>Embodiment</code></td>
<td width="620">Humanoids, bimanual systems, dexterous hands, and tactile interaction</td>
</tr>
<tr>
<td width="110" nowrap><code>Deployment</code></td>
<td width="620">Efficiency, evaluation, data, sim2real, and safety</td>
</tr>
</tbody>
</table>


## Partial updates

Edit the relevant subdirection file and its same-path counterpart in the other language. Keep paper titles, venues, years, resource links and entry order aligned. Chinese pages retain official paper titles, proper names such as models, and necessary abbreviations; generic explanations use Chinese. See the [maintenance guide](CONTRIBUTING.md).
