# Physically Executable Navigation

[Home](../../../README.md) | [中文](../../zh-CN/vln/physically-executable.md) | [Direction index](README.md)

Total: 7 papers.

<table width="3050">
<thead>
<tr>
<th width="120" nowrap>Venue/Year</th>
<th width="320">Paper/Method</th>
<th width="420">Abstract</th>
<th width="220">Task Type</th>
<th width="240">Environment</th>
<th width="260">Map/Memory</th>
<th width="300">Training/Feedback</th>
<th width="240">Sim/Real/Benchmark</th>
<th width="360">Paper Task/Goal</th>
<th width="110" nowrap>Paper</th>
<th width="110" nowrap>Project</th>
<th width="110" nowrap>Code</th>
<th width="240">Data/Bench</th>
</tr>
</thead>
<tbody>
<tr>
<td width="120" nowrap>CVPR 2024</td>
<td width="320"><a href="https://openaccess.thecvf.com/content/CVPR2024/html/Ehsani_SPOC_Imitating_Shortest_Paths_in_Simulation_Enables_Effective_Navigation_and_CVPR_2024_paper.html">SPOC: Imitating Shortest Paths in Simulation Enables Effective Navigation and Manipulation in the Real World</a></td>
<td width="420">SPOC trains embodied agents from simulated shortest paths and transfers the behavior to navigation and manipulation.</td>
<td width="220">Navigation + manipulation</td>
<td width="240">physical embodied environments</td>
<td width="260">implicit spatial policy memory</td>
<td width="300">imitation from shortest paths</td>
<td width="240">Sim + Real</td>
<td width="360">Convert shortest-path supervision into physically executable embodied behavior.</td>
<td width="110" nowrap><a href="https://openaccess.thecvf.com/content/CVPR2024/papers/Ehsani_SPOC_Imitating_Shortest_Paths_in_Simulation_Enables_Effective_Navigation_and_CVPR_2024_paper.pdf">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38942">CorrectNav: Self-Correction Flywheel Empowers Vision-Language-Action Navigation Model</a></td>
<td width="420">CorrectNav automatically generates perception and action self-correction data from model error trajectories, then post-trains VLA navigation models.</td>
<td width="220">VLA navigation self-correction</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">-</td>
<td width="300">self-correction flywheel/post-training</td>
<td width="240">-</td>
<td width="360">Enables VLA navigation models to recover after deviating from the correct trajectory.</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38942">paper</a></td>
<td width="110" nowrap><a href="https://correctnav.github.io/">project</a></td>
<td width="110" nowrap><a href="https://github.com/owlet914/CorrectNav">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/64257">SC$^{2}$-WM: A Self-Correcting World Model with Closed-Loop Feedback for Vision-and-Language Navigation in Continuous Environments</a></td>
<td width="420">SC2-WM uses world-model look-ahead to generate internal feedback, correcting state drift and plans in a closed loop during VLN-CE inference.</td>
<td width="220">World-model Navigation</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">world-model foresight/internal feedback</td>
<td width="300">closed-loop self-correcting world model</td>
<td width="240">-</td>
<td width="360">Addresses the inability of open-loop execution in continuous VLN to detect and correct internal state drift.</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/64257">paper</a></td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/64257">project</a></td>
<td width="110" nowrap><a href="https://github.com/sunrise-ikun/SC2_WM">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2507.13019">Rethinking the Embodied Gap in Vision-and-Language Navigation: A Holistic Study of Physical and Visual Disparities</a></td>
<td width="420">VLN-PE systematically evaluates how visual and physical differences across humanoid, quadruped, and wheeled robots affect VLN.</td>
<td width="220">physical VLN evaluation</td>
<td width="240">humanoid/quadruped/wheeled robots</td>
<td width="260">-</td>
<td width="300">embodied navigation</td>
<td width="240">physical robotic settings</td>
<td width="360">Measures the embodied gap between ideal VLN assumptions and real robot execution.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2507.13019">paper</a></td>
<td width="110" nowrap><a href="https://crystalsixone.github.io/vln_pe.github.io/">project</a></td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2506.23468">NavMorph: A Self-Evolving World Model for Vision-and-Language Navigation in Continuous Environments</a></td>
<td width="420">NavMorph uses a self-evolving world model and contextual evolving memory to model VLN-CE environment dynamics ahead of time and refine policies.</td>
<td width="220">World-model Navigation</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">contextual evolution memory</td>
<td width="300">self-evolving world model/RL</td>
<td width="240">-</td>
<td width="360">Improves adaptive planning for continuous VLN in new environments and process changes.</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2506.23468">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/Feliciaxyao/NavMorph">code</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://iccv.thecvf.com/virtual/2025/poster/299">3D Gaussian Map with Open-Set Semantic Grouping for Vision-Language Navigation</a></td>
<td width="420">This paper uses open-set semantic grouping to unify 3D geometric priors and open semantics in a Gaussian map.</td>
<td width="220">Map/memory</td>
<td width="240">mobile robot/mobile manipulation</td>
<td width="260">3D Gaussian map + open-set semantic grouping</td>
<td width="300">3D representation</td>
<td width="240">-</td>
<td width="360">Open-semantic 3D map for VLN</td>
<td width="110" nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/299">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://iccv.thecvf.com/virtual/2025/poster/1792">monoVLN: Bridging the Observation Gap between Monocular and Panoramic Vision and Language Navigation</a></td>
<td width="420">monoVLN uses 3DGS to complete missing regions in monocular RGBD observations, narrowing the observation gap between monocular robots and panoramic VLN settings.</td>
<td width="220">monocular VLN</td>
<td width="240">monocular RGBD robot</td>
<td width="260">3DGS implicit partial completion</td>
<td width="300">embodied navigation</td>
<td width="240">-</td>
<td width="360">Enables robots with only a monocular camera to perform VLN that originally relied on panoramic observations.</td>
<td width="110" nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/1792">paper</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
</tbody>
</table>
