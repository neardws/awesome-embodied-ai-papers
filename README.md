# Embodied AI Frontier Survey

English | [中文](README.zh-CN.md)

Updated: 2026-06-28

A curated research index for frontier directions in embodied AI. The complete CCF-A paper tables are maintained in the Chinese version: [README.zh-CN.md](README.zh-CN.md).

## Quick Access

- For the field map, read [Direction Overview](#direction-overview).
- For paper-level details, open [Full Chinese Tables](README.zh-CN.md#各方向详细表格).
- For the suggested reading sequence, jump to [Reading Order](#reading-order).
- For source traceability, see [Data Sources](#data-sources) and [`sources/github/readmes`](sources/github/readmes).

## Tag Legend

| Tag | Meaning |
| --- | --- |
| `VLN` | Large-scale navigation |
| `VLA` | Vision-language-action manipulation policies |
| `WAM` | World action models |
| `Planning` | Task decomposition, memory, failure recovery, and constrained planning |
| `Embodiment` | Humanoids, bimanual systems, dexterous hands, and tactile interaction |
| `Deployment` | Efficiency, evaluation, data, sim2real, and safety |

## Overall View

The current embodied AI frontier can be grouped into six tracks: large-scale VLN, VLA manipulation policies, WAM/world models, agentic planning, embodiment expansion, and deployment-oriented efficiency/evaluation/data.

The system direction worth tracking is:

```text
task understanding and fine-grained planning agent
        -> WAM / world model for imagination, verification, and failure prediction
        -> small VLA, diffusion policy, skill library, or classical controller
        -> local robot safety loop
```

The reason is straightforward: monolithic VLA models matter, but real robots also need interpretable planning, executable constraints, low-latency control, failure recovery, and on-device autonomy.

## Direction Overview

| Tag | Direction | Subdirections | CCF-A Entries | Takeaway |
| --- | --- | --- | ---: | --- |
| `VLN` | VLN / Large-scale navigation | Continuous VLN, map memory, executable navigation, urban/open-world navigation, low-cost/on-device navigation | 75 | Navigation is moving from discrete graphs toward continuous, executable, open-world, and lower-cost deployment settings. |
| `VLA` | VLA / Manipulation policy | Generalist VLA, action representation, diffusion/flow policy, 3D grounding, online/RL fine-tuning, robustness | 182 | VLA is the main track for manipulation, but the key work is in action representation, grounding, fine-tuning, and reliable control rather than simply adding an action head to a large model. |
| `WAM` | WAM / World model | Cascaded WAM, joint WAM, video/latent world model, world model for VLA, world model evaluation | 46 | World models are useful as an intermediate layer for imagination, verification, and recovery between planning and low-level control. |
| `Planning` | Agentic planning | Task decomposition, memory, failure monitoring, constraint/affordance planning, self-improving planning | 89 | Planning papers are closest to the practical architecture of agent planning plus smaller execution modules. |
| `Embodiment` | Embodiment expansion | Humanoid, bimanual, dexterous hand, tactile/contact-rich, grasping | 72 | Body form changes the action space, sensing needs, and control objective, so these papers are essential for moving beyond single-arm tabletop manipulation. |
| `Deployment` | Efficiency / evaluation / data | Quantization/cache/tokenization, real-time execution, benchmark/dataset, sim2real, safety evaluation | 79 | Deployment depends on fast inference, real-time execution, sim2real transfer, trustworthy benchmarks, and safety evaluation. |

## Full Chinese Tables

The full paper-level tables are in [README.zh-CN.md](README.zh-CN.md). They include paper title, abstract, project page, code, data/benchmark, source, and direction-specific fields such as Base VLA, Action, Algorithm, Policy/Type, Sim/Real, world-model state representation, planning interface, embodiment type, and efficiency metrics.

## Reading Order

1. Read the direction overview first to understand the six-track map.
2. Read VLA and Agentic Planning together, because planning quality and action execution are coupled.
3. Read WAM next as the bridge between planning and policy execution.
4. Read Embodiment and Deployment last to check what survives real robot constraints.

## Additional Source Entries

Archived source README snapshots are kept under [`sources/github/readmes`](sources/github/readmes). They are used as references, not copied wholesale.

## Data Sources

This repository keeps source metadata and archived GitHub README snapshots so table entries can be traced back to public paper pages, project pages, code repositories, datasets, and benchmark resources.
