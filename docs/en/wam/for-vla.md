# world model for VLA

[Home](../../../README.md) | [中文](../../zh-CN/wam/for-vla.md) | [Direction index](README.md)

Total: 10 papers.

<table width="3110">
<thead>
<tr>
<th width="120" nowrap>Venue/Year</th>
<th width="320">Paper/Method</th>
<th width="420">Abstract</th>
<th width="220">WAM Type</th>
<th width="280">State Representation</th>
<th width="260">Action Interface</th>
<th width="360">Use</th>
<th width="200">Sim/Real</th>
<th width="360">Paper Task/Goal</th>
<th width="110" nowrap>Paper</th>
<th width="110" nowrap>Project</th>
<th width="110" nowrap>Code</th>
<th width="240">Data/Bench</th>
</tr>
</thead>
<tbody>
<tr>
<td width="120" nowrap>ECCV 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2602.10098">VLA-JEPA: Enhancing Vision-Language-Action Model with Latent World Model</a></td>
<td width="420">VLA-JEPA uses JEPA-style latent future-state prediction to pretrain VLA policies without leaking future frames into the input.</td>
<td width="220">latent world model for VLA</td>
<td width="280">future-frame latent targets</td>
<td width="260">latent action tokens + action-head fine-tuning</td>
<td width="360">VLA pretraining/generalization</td>
<td width="200">LIBERO, LIBERO-Plus, SimplerEnv, real Franka</td>
<td width="360">Address appearance bias, nuisance motion, and information leakage in video-pretrained VLA policies.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2602.10098">paper</a></td>
<td width="110" nowrap><a href="https://ginwind.github.io/VLA-JEPA/">project</a></td>
<td width="110" nowrap><a href="https://github.com/ginwind/VLA-JEPA">code</a></td>
<td width="240"><a href="https://huggingface.co/ginwind/VLA-JEPA">hf</a></td>
</tr>
<tr>
<td width="120" nowrap>ICRA 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2509.22643">VLA-Reasoner: Reinforcing Robotic Reasoning and Generalization with World Model</a></td>
<td width="420">VLA-Reasoner adds test-time long-horizon reasoning to existing VLAs through world-model rollouts and online MCTS.</td>
<td width="220">world model for VLA</td>
<td width="280">predicted future states</td>
<td width="260">VLA action candidates</td>
<td width="360">test-time search and verification</td>
<td width="200">Sim + Real</td>
<td width="360">Search future outcomes with a world model before executing actions.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2509.22643">paper</a></td>
<td width="110" nowrap><a href="https://vla-reasoner.github.io/">project</a></td>
<td width="110" nowrap><a href="https://github.com/wkguo/VLA-Reasoner">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICRA 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2503.10370">LUMOS: Language-Conditioned Imitation Learning with World Models</a></td>
<td width="420">LUMOS practices language-conditioned long-horizon manipulation offline in a learned world-model latent space before transferring to real robots.</td>
<td width="220">world model for VLA</td>
<td width="280">latent world state</td>
<td width="260">language-conditioned action</td>
<td width="360">offline practice / imitation learning</td>
<td width="200">Sim + Real</td>
<td width="360">Use world-model practice to reduce real-robot data requirements.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2503.10370">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=fHLtSxDFKC">Genie Envisioner: A Unified World Foundation Platform for Robotic Manipulation</a></td>
<td width="420">GE jointly learns visual representations and action policies within a video generation framework, supporting cross-embodiment manipulation.</td>
<td width="220">world model for VLA</td>
<td width="280">structured video latent</td>
<td width="260">GE-Act flow-matching decoder/action trajectories</td>
<td width="360">world foundation platform + policy inference</td>
<td width="200">-</td>
<td width="360">Address the separation of world modeling and action policies in robotic manipulation, and the high cost of supervision for generalization.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=fHLtSxDFKC">paper</a></td>
<td width="110" nowrap><a href="https://genie-envisioner.github.io/">project</a></td>
<td width="110" nowrap><a href="https://github.com/AgibotTech/Genie-Envisioner-V1">code</a></td>
<td width="240">&gt;1M manipulation episodes + released benchmarks</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=LQv9LU2Ufg">RIG: Synergizing Reasoning and Imagination in End-to-End Generalist Policy</a></td>
<td width="420">RIG jointly learns reasoning, action, and next-image imagination in an end-to-end generalist policy.</td>
<td width="220">world model for VLA</td>
<td width="280">reasoning + next-image/world dynamics</td>
<td width="260">reason-then-act with imagined outcome</td>
<td width="360">self-correction/test-time scaling</td>
<td width="200">generalist embodied policy benchmarks</td>
<td width="360">Address embodied agents having only reasoning or imagination as a single capability and inefficient system-level composition.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=LQv9LU2Ufg">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=qE2FyvRvuF">WMPO: World Model-based Policy Optimization for Vision-Language-Action Models</a></td>
<td width="420">WMPO performs on-policy GRPO for VLA in imagination using a pixel-level world model.</td>
<td width="220">world model for VLA</td>
<td width="280">pixel-based imagined trajectories</td>
<td width="260">VLA policy actions/GRPO</td>
<td width="360">imagination-only policy optimization</td>
<td width="200">Sim + Real</td>
<td width="360">Address VLA reliance on expert demonstrations and the high sampling cost of real-robot RL.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=qE2FyvRvuF">paper</a></td>
<td width="110" nowrap><a href="https://wm-po.github.io/">project</a></td>
<td width="110" nowrap><a href="https://github.com/WM-PO/WMPO">code</a></td>
<td width="240"><a href="https://huggingface.co/fangqi/WMPO">hf</a></td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=wPEIStHxYH">Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning</a></td>
<td width="420">Cosmos Policy fine-tunes a pretrained video model in one stage so it generates actions, future states, and values for planning.</td>
<td width="220">world model for VLA / video-policy world model</td>
<td width="280">video model latent frames for actions/states/values</td>
<td width="260">latent-frame action generation + planning</td>
<td width="360">visuomotor control/planning</td>
<td width="200">-</td>
<td width="360">Address the need for complex multi-stage training and extra action architectures when using video models for robot policies.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=wPEIStHxYH">paper</a></td>
<td width="110" nowrap><a href="https://research.nvidia.com/labs/dir/cosmos-policy/cosmos_policy_index.html">project</a></td>
<td width="110" nowrap><a href="https://github.com/nvlabs/cosmos-policy">code</a></td>
<td width="240">LIBERO, RoboCasa, real bimanual tasks</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38925">WorldAgen: Unified State-Action Prediction with Test-Time World Model Training</a></td>
<td width="420">WorldAgen uses a shared Transformer to predict future states and actions simultaneously, and trains the world model at test time to adapt to new environments.</td>
<td width="220">world model for VLA</td>
<td width="280">past state-action trajectories</td>
<td width="260">agent-model action head + exploratory actions</td>
<td width="360">test-time adaptation for VLA</td>
<td width="200">Sim/Benchmark</td>
<td width="360">Address poor generalization when deploying VLA to new object configurations or dynamics environments under static pretraining.</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38925">paper</a></td>
<td width="110" nowrap><a href="https://worldagen.github.io/">project</a></td>
<td width="110" nowrap><a href="https://github.com/mll-lab-nu/WorldAgen">code</a></td>
<td width="240">CALVIN, LIBERO</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/66169">VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model</a></td>
<td width="420">VLAW iteratively improves an action-conditioned video world model with real rollouts, then generates synthetic data to improve VLA.</td>
<td width="220">world model for VLA</td>
<td width="280">action-conditioned video world model</td>
<td width="260">VLA actions + generated rollouts</td>
<td width="360">iterative VLA/world-model co-improvement</td>
<td width="200">Real + synthetic rollouts</td>
<td width="360">Address expensive real rollouts and insufficient physical fidelity of existing world models for directly improving policies.</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/66169">paper</a></td>
<td width="110" nowrap><a href="https://sites.google.com/view/vla-w">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2603.03195">Chain of World: World Model Thinking in Latent Motion</a></td>
<td width="420">CoWVLA uses a video VAE to extract continuous latent motion chains and jointly fine-tunes them with discrete action prediction.</td>
<td width="220">world model for VLA / latent motion</td>
<td width="280">structure and motion latents</td>
<td width="260">autoregressive action sequence decoder</td>
<td width="360">VLA pretraining/fine-tuning</td>
<td width="200">robot simulation benchmarks</td>
<td width="360">Address redundant background reconstruction in world-model VLA and lack of continuous temporal dynamics in latent-action VLA.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2603.03195">paper</a></td>
<td width="110" nowrap><a href="https://fx-hit.github.io/cowvla-io/">project</a></td>
<td width="110" nowrap><a href="https://github.com/fx-hit/CoWVLA">code</a></td>
<td width="240"><a href="https://huggingface.co/hitfx/CoWVLA">hf</a></td>
</tr>
</tbody>
</table>
