# Progress and shared bottlenecks

[Home](../../../README.md) | [中文](../../zh-CN/landscape/progress.md) | [Landscape index](README.md)

The observations below synthesize the listed research and industrial examples. They are not market-size estimates, universal maturity claims or a ranking of companies. Each row connects a documented capability with the evidence still needed for deployment.

<table width="1960">
<thead>
<tr>
<th width="240" nowrap>Theme</th>
<th width="440">What the examples establish</th>
<th width="440">Remaining gap</th>
<th width="440">Next evidence to retain</th>
<th width="400">Primary examples</th>
</tr>
</thead>
<tbody>
<tr>
<td width="240" nowrap>Available bodies and reproducible research</td>
<td width="440">Open bodies, research arms and commercial humanoids expose different design or product entry points.</td>
<td width="440">Access to hardware does not establish general task capability; unit variation, heat and service affect reproduction.</td>
<td width="440">Report success, failures, repairs and repeated trials for explicit configurations and tasks.</td>
<td width="400"><a href="https://toddlerbot.github.io/">ToddlerBot (Stanford University)</a> · <a href="https://www.unitree.com/g1/">Unitree G1</a> · <a href="https://franka.de/franka-research-3">Franka Research 3</a></td>
</tr>
<tr>
<td width="240" nowrap>Action learning and foundation policies</td>
<td width="440">Diffusion policies and vision-language-action models provide concrete action-generation research routes.</td>
<td width="440">A single demonstration cannot establish cross-scene, long-horizon or real failure-recovery ability.</td>
<td width="440">Align training data, robot configurations, unseen conditions and intervention budgets.</td>
<td width="400"><a href="https://diffusion-policy.cs.columbia.edu/">Diffusion Policy research team</a> · <a href="https://openvla.github.io/">OpenVLA research collaboration</a> · <a href="https://www.pi.website/blog/pi0">Physical Intelligence / pi0</a></td>
</tr>
<tr>
<td width="240" nowrap>World prediction and executable planning</td>
<td width="440">World models, language-based skill planning and spatial value representations contribute different closed-loop capabilities.</td>
<td width="440">Plausible predictions do not establish physically constrained actions or reliable recovery.</td>
<td width="440">Compare task benefit, incorrect predictions and recovery with and without the module.</td>
<td width="400"><a href="https://danijar.com/project/daydreamer/">DayDreamer research team</a> · <a href="https://say-can.github.io/">SayCan research team</a> · <a href="https://voxposer.github.io/">VoxPoser research team</a></td>
</tr>
<tr>
<td width="240" nowrap>Data toolchains and cross-body reuse</td>
<td width="440">Multi-institution data, portable teaching and open toolchains provide complementary data entry points.</td>
<td width="440">Volume cannot substitute for action semantics, synchronization, permission and distribution coverage.</td>
<td width="440">Record versions, provenance, isolated splits and gains on new real tasks.</td>
<td width="400"><a href="https://robotics-transformer-x.github.io/">Open X-Embodiment collaboration</a> · <a href="https://droid-dataset.github.io/">DROID multi-institution team</a> · <a href="https://umi-gripper.github.io/">UMI research team</a> · <a href="https://huggingface.co/docs/lerobot/index">Hugging Face / LeRobot</a> · <a href="https://github.com/OpenDriveLab/AgiBot-World">AgiBot World / OpenDriveLab</a></td>
</tr>
<tr>
<td width="240" nowrap>Simulation and evaluation infrastructure</td>
<td width="440">Physics engines, training frameworks and bimanual task generation support more controlled experiments.</td>
<td width="440">Contact, sensor and asset errors still require physical validation; synthetic metrics do not replace real metrics.</td>
<td width="440">Pin simulator versions, randomization ranges, real calibration and transfer-test conditions.</td>
<td width="400"><a href="https://mujoco.org/">MuJoCo / Google DeepMind</a> · <a href="https://isaac-sim.github.io/IsaacLab/main/index.html">NVIDIA Isaac Lab</a> · <a href="https://robotwin-platform.github.io/">RoboTwin collaboration</a> · <a href="https://www.lightwheel.ai/">Lightwheel</a></td>
</tr>
<tr>
<td width="240" nowrap>Contact hardware and tactile learning</td>
<td width="440">Research hands, commercial end effectors and tactile devices provide different contact capabilities.</td>
<td width="440">More joints or taxels do not automatically improve control; durability, calibration and data remain constraints.</td>
<td width="440">Compare sensing benefit, task outcomes, control latency and replacement or service cost.</td>
<td width="400"><a href="https://arxiv.org/abs/2309.06440">LEAP Hand research team</a> · <a href="https://shadowrobot.com/dexterous-hand-series/">Shadow Robot dexterous hands</a> · <a href="https://www.gelsight.com/product/digit-tactile-sensor/">GelSight DIGIT</a> · <a href="https://www.inspire-robots.com/">Inspire Robots</a></td>
</tr>
<tr>
<td width="240" nowrap>Software interfaces and operational feedback</td>
<td width="440">Control, navigation, manipulation, fleet and data tools cover different integration layers.</td>
<td width="440">Interfaces do not establish interoperability; versions, timing and failure semantics need explicit verification.</td>
<td width="440">Retain deployment configurations, end-to-end tests, fault injection and rollback records.</td>
<td width="400"><a href="https://github.com/ros-controls/ros2_control">ros2_control community</a> · <a href="https://moveit.ai/">MoveIt / PickNik</a> · <a href="https://docs.nav2.org/rolling/">Nav2 community</a> · <a href="https://www.open-rmf.org/">Open-RMF community</a> · <a href="https://foxglove.dev/">Foxglove</a></td>
</tr>
<tr>
<td width="240" nowrap>Field value and scalable delivery</td>
<td width="440">An operator-disclosed logistics case connects a specific task with commercial delivery.</td>
<td width="440">One site does not represent industry-wide maturity; service, retrofit and downtime costs must be included.</td>
<td width="440">Record cycle time, availability duration, interventions, recovery and full cost together.</td>
<td width="400"><a href="https://investors.gxo.com/news-releases/news-release-details/gxo-signs-industry-first-multi-year-agreement-agility-robotics">GXO / Agility Robotics</a> · <a href="https://www.protolabs.com/industries/robotics/">Protolabs</a> · <a href="https://www.nist.gov/el/intelligent-systems-division-73500/robotic-grasping-and-manipulation-assembly">NIST</a></td>
</tr>
</tbody>
</table>

## Read academic and industrial progress together

Academic comparisons emphasize controlled tasks, baselines, ablations and generalization. Industrial delivery additionally needs integration, operating duration, recovery, serviceability and cost evidence. Companies also publish research, and universities also build hardware: assign roles to the actual contribution rather than the organization name.

A meaningful bridge is a reproducible task specification: robot and end effector, sensing, action interface, data version, compute budget, operating conditions and failure accounting. Keep those boundaries when linking papers with products.
