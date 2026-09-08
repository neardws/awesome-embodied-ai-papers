# cascaded WAM

[Home](../../../README.md) | [中文](../../zh-CN/wam/cascaded.md) | [Direction index](README.md)

Total: 24 papers.

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
<td width="120" nowrap>ICRA 2025</td>
<td width="320"><a href="https://nvlabs.github.io/X-MOBILITY/">X-MOBILITY: End-To-End Generalizable Navigation via World Modeling</a></td>
<td width="420">X-MOBILITY uses an autoregressive latent world model to separate world dynamics learning from action policy learning for zero-shot sim-to-real navigation.</td>
<td width="220">navigation world model</td>
<td width="280">latent future state</td>
<td width="260">navigation action</td>
<td width="360">navigation policy imagination</td>
<td width="200">Sim + Real</td>
<td width="360">Improve end-to-end navigation generalization and sim-to-real transfer through world modeling.</td>
<td width="110" nowrap><a href="https://nvlabs.github.io/X-MOBILITY/">paper</a></td>
<td width="110" nowrap><a href="https://nvlabs.github.io/X-MOBILITY/">project</a></td>
<td width="110" nowrap><a href="https://github.com/NVlabs/X-MOBILITY">code</a></td>
<td width="240"><a href="https://github.com/NVlabs/X-MOBILITY">data</a></td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=748bHL2BAv">Ctrl-World: A Controllable Generative World Model for Robot Manipulation</a></td>
<td width="420">Build a controllable multi-view robotic world model, using imagined rollouts to evaluate and improve generalist robot policies.</td>
<td width="220">cascaded WAM</td>
<td width="280">Multi-view video world model</td>
<td width="260">frame-level action conditioning</td>
<td width="360">policy evaluation + synthetic improvement</td>
<td width="200">Real robot data/DROID</td>
<td width="360">Address the problem that real rollouts for generalist robot policies under new objects and new instructions are expensive and hard to scale.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=748bHL2BAv">paper</a></td>
<td width="110" nowrap><a href="https://ctrl-world.github.io/">project</a></td>
<td width="110" nowrap><a href="https://github.com/Robert-gyj/Ctrl-World">code</a></td>
<td width="240"><a href="https://huggingface.co/yjguo/Ctrl-World">hf</a></td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=0GNBqoYcAP">Context and Diversity Matter: The Emergence of In-Context Learning in World Models</a></td>
<td width="420">Study how world models identify or learn new environment dynamics from in-context examples.</td>
<td width="220">cascaded WAM</td>
<td width="280">environment dynamics/world-model latent</td>
<td width="260">-</td>
<td width="360">ICL dynamics prediction</td>
<td width="200">sim/analysis</td>
<td width="360">Address the poor adaptability of static world models when facing new environments or rare configurations.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=0GNBqoYcAP">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=4HZgkwVVFO">NeMo-map: Neural Implicit Flow Fields for Spatio-Temporal Motion Mapping</a></td>
<td width="420">Use neural implicit functions to continuously model site-specific spatiotemporal motion flow fields.</td>
<td width="220">spatio-temporal motion world model</td>
<td width="280">implicit neural flow field</td>
<td width="260">-</td>
<td width="360">motion mapping/navigation safety</td>
<td width="200">public motion datasets</td>
<td width="360">Address the high cost of discrete sampling and offline construction for dynamic motion maps in human environments.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=4HZgkwVVFO">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=8UZpmrxoLG">Astra: General Interactive World Model with Autoregressive Denoising</a></td>
<td width="420">Use an autoregressive denoising video model to generate long-horizon future worlds controllable by actions.</td>
<td width="220">cascaded WAM</td>
<td width="280">video world model</td>
<td width="260">action-aware adapter</td>
<td width="360">interactive future prediction</td>
<td width="200">robot + driving scenarios</td>
<td width="360">Address long-horizon future prediction from historical observations and actions in general scenarios.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=8UZpmrxoLG">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=LQD1MrnbxH">Test-Time Mixture of World Models for Embodied Agents in Dynamic Environments</a></td>
<td width="420">Dynamically route and combine multiple world models at test time to adapt to changing environments.</td>
<td width="220">cascaded WAM</td>
<td width="280">mixture of world models</td>
<td width="260">agent action/API</td>
<td width="360">test-time adaptation for embodied reasoning</td>
<td width="200">dynamic embodied env benchmarks</td>
<td width="360">Address insufficient world-model composition and continual adaptation for embodied agents in unseen dynamic environments.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=LQD1MrnbxH">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=MPabX9LEds">Learning Massively Multitask World Models for Continuous Control</a></td>
<td width="420">Newt pretrains and online-optimizes a language-conditioned world model across 200 continuous-control tasks.</td>
<td width="220">cascaded WAM</td>
<td width="280">language-conditioned multitask latent world model</td>
<td width="260">continuous control actions</td>
<td width="360">online RL pretraining/fine-tuning</td>
<td width="200">-</td>
<td width="360">Address poor scalability of online RL across multitask continuous control and multiple embodiments.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=MPabX9LEds">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">200-task benchmark</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=a1zfcaNTkM">ExoPredicator: Learning Abstract Models of Dynamic Worlds for Robot Planning</a></td>
<td width="420">Learn symbolic states and endogenous/exogenous causal processes for long-horizon robot planning.</td>
<td width="220">cascaded WAM</td>
<td width="280">abstract symbolic state + causal processes</td>
<td width="260">symbolic/endogenous actions</td>
<td width="360">long-horizon planning</td>
<td width="200">simulated tabletop</td>
<td width="360">Address concurrent environment changes and action effects in robot planning.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=a1zfcaNTkM">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=oBXfPyi47m">Efficient Reinforcement Learning by Guiding World Models with Non-Curated Data</a></td>
<td width="420">Use reward-free, cross-embodiment, mixed-quality offline data to guide world models and improve online RL sample efficiency.</td>
<td width="220">cascaded WAM</td>
<td width="280">world model from offline/online data</td>
<td width="260">visuomotor RL actions</td>
<td width="360">sample-efficient online RL</td>
<td width="200">72 visuomotor tasks/6 embodiments</td>
<td width="360">Address distribution shift that makes directly fine-tuning world models with uncurated offline data ineffective for improving RL.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=oBXfPyi47m">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=qmEyJadwHA">Object-Centric World Models from Few-Shot Annotations for Sample-Efficient Reinforcement Learning</a></td>
<td width="420">OC-STORM uses a small amount of annotations to extract object-centric representations and improve sample efficiency for pixel-based MBRL.</td>
<td width="220">cascaded WAM</td>
<td width="280">object-centric latent</td>
<td width="260">RL actions</td>
<td width="360">sample-efficient MBRL</td>
<td width="200">-</td>
<td width="360">Address low sample efficiency caused by pixel-level world models ignoring small but critical objects.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=qmEyJadwHA">paper</a></td>
<td width="110" nowrap><a href="https://oc-storm.weipuzhang.com">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">Atari 100k, Hollow Knight</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=w3w7WVG4ks">Building spatial world models from sparse transitional episodic memories</a></td>
<td width="420">ESWM builds spatial cognitive maps from sparse discrete episodic memories and predicts unobserved transitions.</td>
<td width="220">cascaded WAM</td>
<td width="280">episodic spatial latent map</td>
<td width="260">navigation transitions</td>
<td width="360">exploration/navigation planning</td>
<td width="200">simulated spatial environments</td>
<td width="360">Address the need for long continuous trajectories when building maps with spatial world models.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=w3w7WVG4ks">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=yDmb7xAfeb">World-In-World: World Models in a Closed-Loop World</a></td>
<td width="420">Provide a closed-loop platform to evaluate whether world models truly improve embodied task success.</td>
<td width="220">world model evaluation/closed-loop WAM</td>
<td width="280">heterogeneous WMs</td>
<td width="260">standardized action API</td>
<td width="360">closed-loop planning/evaluation</td>
<td width="200">-</td>
<td width="360">Address world-model evaluations biased toward open-loop visual quality and lacking closed-loop metrics for task success.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=yDmb7xAfeb">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">World-In-World benchmark</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=Patx6MRipw">ENACT: Evaluating Embodied Cognition with World Modeling of Egocentric Interaction</a></td>
<td width="420">ENACT uses egocentric interaction sequence reordering tasks to evaluate VLMs' forward and inverse world-modeling ability.</td>
<td width="220">world model evaluation</td>
<td width="280">egocentric state/action sequences</td>
<td width="260">inverse world modeling actions</td>
<td width="360">benchmark/evaluation</td>
<td width="200">-</td>
<td width="360">Address how to evaluate whether VLMs have embodied cognition and interactive world-modeling ability.</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=Patx6MRipw">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">ENACT</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/63978">Cross-Embodiment Robot Foundation World Models with Latent Actions</a></td>
<td width="420">LAC-WM trains a cross-embodiment robotic world model using a unified latent action space.</td>
<td width="220">cascaded WAM</td>
<td width="280">latent action-conditioned world model</td>
<td width="260">unified latent actions</td>
<td width="360">cross-embodiment adaptation</td>
<td width="200">dexterous manipulation benchmark</td>
<td width="360">Address poor generalization of world models to new embodiments caused by inconsistent action spaces across robots.</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/63978">paper</a></td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/63978">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/62480">DDP-WM: Disentangled Dynamics Prediction for Efficient World Models</a></td>
<td width="420">DDP-WM disentangles primary dynamics from background updates to improve real-time inference and planning efficiency in world models.</td>
<td width="220">cascaded WAM</td>
<td width="280">disentangled latent dynamics</td>
<td width="260">MPC/planner</td>
<td width="360">efficient planning</td>
<td width="200">navigation/tabletop/deformable benchmarks</td>
<td width="360">Address high computational cost and poor real-time deployability of dense Transformer world models.</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/62480">paper</a></td>
<td width="110" nowrap><a href="https://hcplab-sysu.github.io/DDP-WM">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/62543">RoboFlow4D: A Lightweight Flow World Model Toward Real-Time Flow-Guided Robotic Manipulation</a></td>
<td width="420">RoboFlow4D directly predicts multi-frame 3D flow and uses flow to guide real-time robotic manipulation.</td>
<td width="220">cascaded WAM</td>
<td width="280">multi-frame 3D flow</td>
<td width="260">flow-guided action policy</td>
<td width="360">real-time manipulation planning</td>
<td width="200">Sim + Real</td>
<td width="360">Address high overhead and poor real-time performance in modular predict-flow-plan pipelines for 3D manipulation.</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/62543">paper</a></td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/62543">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/64209">Learning Task-Sufficient World Models by Synergizing Agentic Exploration and Structured Modeling</a></td>
<td width="420">Learn task-sufficient and compact world-model representations through active exploration and structured modeling.</td>
<td width="220">cascaded WAM</td>
<td width="280">task-sufficient structured latent</td>
<td width="260">agentic exploration/actions</td>
<td width="360">sample-efficient control/generalization</td>
<td width="200">continuous control + manipulation benchmarks</td>
<td width="360">Address general visual/latent world models retaining too many control-irrelevant factors, hurting generalization efficiency.</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/64209">paper</a></td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/64209">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2509.15536">SAMPO: Scale-wise Autoregression with Motion PrOmpt for Generative World Models</a></td>
<td width="420">SAMPO combines scale-wise visual autoregression, causal next-frame modeling, and motion prompts to generate action-conditioned futures.</td>
<td width="220">cascaded WAM</td>
<td width="280">video tokens + motion prompt</td>
<td width="260">action-conditioned video prediction</td>
<td width="360">model-based control/video prediction</td>
<td width="200">robot/world-model benchmarks</td>
<td width="360">Address damaged spatial structure, inefficient decoding, and insufficient motion modeling in autoregressive world models.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2509.15536">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2505.05495">Learning 3D Persistent Embodied World Models</a></td>
<td width="420">Learn an embodied world model with explicit 3D memory to simulate long-horizon future observations more consistently.</td>
<td width="220">cascaded WAM</td>
<td width="280">RGB-D video + persistent 3D map</td>
<td width="260">future action-conditioned observation prediction</td>
<td width="360">planning/policy learning</td>
<td width="200">embodied applications</td>
<td width="360">Address lack of unobserved-scene memory and inconsistent long-horizon planning in video world models.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2505.05495">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2505.20425">OSVI-WM: One-Shot Visual Imitation for Unseen Tasks using World-Model-Guided Trajectory Generation</a></td>
<td width="420">Use a world model to generate latent states and action trajectories for one-shot visual imitation on unseen tasks.</td>
<td width="220">cascaded WAM</td>
<td width="280">latent states/trajectory</td>
<td width="260">decoded physical waypoints</td>
<td width="360">one-shot imitation</td>
<td width="200">2 sim benchmarks + 3 real robot platforms</td>
<td width="360">Address poor generalization of one-shot visual imitation to new tasks with different semantics or structures.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2505.20425">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/raktimgg/OSVI-WM">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2406.14540">IRASim: A Fine-Grained World Model for Robot Manipulation</a></td>
<td width="420">IRASim uses a frame-by-frame action-conditioned diffusion Transformer to generate fine-grained robot-object interaction videos.</td>
<td width="220">cascaded WAM</td>
<td width="280">action-conditioned video</td>
<td width="260">robot action trajectories/frame-level conditioning</td>
<td width="360">fine-grained manipulation simulation</td>
<td width="200">robot manipulation datasets</td>
<td width="360">Address the difficulty of precise action-visual frame alignment and fine-grained interaction prediction in robotic manipulation.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2406.14540">paper</a></td>
<td width="110" nowrap><a href="https://gen-irasim.github.io/">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://ziweiwangthu.github.io/data/GWM.pdf">GWM: Towards Scalable Gaussian World Models for Robotic Manipulation</a></td>
<td width="420">GWM uses 3D Gaussian primitives to predict future 3D scenes after robot actions.</td>
<td width="220">cascaded WAM</td>
<td width="280">3D Gaussian splats latent</td>
<td width="260">robot action-conditioned Gaussian propagation</td>
<td width="360">imitation representation + MBRL simulator</td>
<td width="200">Sim + Real</td>
<td width="360">Address lack of stable 3D geometric information in image world models, making it difficult to support policy training.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2507.07954">paper</a></td>
<td width="110" nowrap><a href="https://gaussian-world-model.github.io/">project</a></td>
<td width="110" nowrap><a href="https://github.com/Gaussian-World-Model/gaussianwm">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2503.16806">DyWA: Dynamics-adaptive World Action Model for Generalizable Non-prehensile Manipulation</a></td>
<td width="420">DyWA jointly predicts future states and adapts to dynamics changes, improving generalization for non-prehensile manipulation.</td>
<td width="220">cascaded WAM</td>
<td width="280">single-view point cloud + geometry/state/physics</td>
<td width="260">world action model</td>
<td width="360">non-prehensile manipulation</td>
<td width="200">Sim + Real</td>
<td width="360">Address generalization challenges in non-prehensile manipulation under varying object mass, table friction, and single-view partial observability.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2503.16806">paper</a></td>
<td width="110" nowrap><a href="https://pku-epic.github.io/DyWA/">project</a></td>
<td width="110" nowrap><a href="https://github.com/jiangranlv/DyWA">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://openreview.net/pdf?id=mnwlhvmKMN">Learning 4D Embodied World Models</a></td>
<td width="420">TesserAct predicts action-evolving 4D dynamic mesh worlds from images and language.</td>
<td width="220">cascaded WAM</td>
<td width="280">4D dynamic mesh</td>
<td width="260">inverse dynamics/policy execution</td>
<td width="360">4D prediction + policy learning</td>
<td width="200">dataset + embodied tasks</td>
<td width="360">Address lack of precise 3D geometry and temporal dynamics in 2D video world models, making inverse dynamics hard to learn.</td>
<td width="110" nowrap><a href="https://openreview.net/pdf?id=mnwlhvmKMN">paper</a> / <a href="https://arxiv.org/pdf/2504.20995">paper</a></td>
<td width="110" nowrap><a href="https://tesseractworld.github.io/">project</a></td>
<td width="110" nowrap><a href="https://github.com/UMass-Embodied-AGI/TesserAct">code</a></td>
<td width="240"><a href="https://huggingface.co/anyeZHY/tesseract">hf</a></td>
</tr>
</tbody>
</table>
