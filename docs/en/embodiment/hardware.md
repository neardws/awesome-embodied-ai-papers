# Humanoid & Biped Hardware Reference

[Home](../../../README.md) | [中文](../../zh-CN/embodiment/hardware.md) | [Direction index](README.md)

This section now serves only as a hardware index: Unitree and AgiBot biped models, lab-built platforms, and body-to-hand or body-to-gripper configurations. Papers are no longer duplicated in a separate table here. Venue, method, exact embodiment, evaluation setting, solved problem, current bottleneck, and future direction are consolidated into the single [humanoid paper master table](humanoid.md). Specifications were checked through **2026-07-10**.

> [!IMPORTANT]
> “Body DoF” excludes optional end effectors unless a vendor explicitly reports a complete-system total. The biped tables intentionally exclude wheeled or fixed-base systems such as Unitree G1-D/R1-D/H2-D and AgiBot A2-W/G1/G2. `Sim Only` in the paper table means that only a robot model or URDF was used; it does not imply physical deployment.

## Unitree biped models and specifications

<table width="1460">
<thead>
<tr>
<th width="170" nowrap>Model / role</th>
<th width="150">Height / weight</th>
<th width="150">Body DoF</th>
<th width="300">Joint, payload, and speed</th>
<th width="170">Battery / endurance</th>
<th width="300">Perception and compute</th>
<th width="220">Dexterous-hand form</th>
</tr>
</thead>
<tbody>
<tr>
<td width="170" nowrap><a href="https://www.unitree.com/h1/">H1</a><br>First full-size general humanoid</td>
<td width="150">About 180 cm / 47 kg</td>
<td width="150">Official total 19; 5 per leg and 4 per arm, expandable</td>
<td width="300">Knee about 360 N·m, hip 220 N·m, ankle 59 N·m, arm 75 N·m; listed speed 3.3 m/s</td>
<td width="170">15 Ah / 0.864 kWh, quick-release; no hourly endurance published</td>
<td width="300">3D LiDAR + depth camera; i5 platform PC + i7 development PC, optional i7/Orin NX</td>
<td width="220">Optional; no standard hand model specified</td>
</tr>
<tr>
<td width="170" nowrap><a href="https://www.unitree.com/h1/">H1-2</a><br>Higher-DoF whole-body manipulation version</td>
<td width="150">About 178 cm / 70 kg</td>
<td width="150">27; 6 per leg and 7 per arm</td>
<td width="300">Leg peak 360 N·m; shoulder/elbow about 120 N·m, wrist 30 N·m; arm payload about 21 kg peak / 7 kg rated; speed &lt;2 m/s</td>
<td width="170">15 Ah / 0.864 kWh, quick-release</td>
<td width="300">3D LiDAR + depth camera; i5+i7, with up to three optional Orin NX modules</td>
<td width="220">Dex5-1 or other dexterous hands explicitly optional</td>
</tr>
<tr>
<td width="170" nowrap><a href="https://www.unitree.com/g1/">G1 / G1 EDU</a><br>Compact research and education platform</td>
<td width="150">132 cm / about 35 kg, 35 kg+</td>
<td width="150">23 / 23–43; 6 per leg and 5 per arm; EDU can add waist, wrists, and hands</td>
<td width="300">Maximum knee torque 90 / 120 N·m; arm payload about 2 / 3 kg; current parameter table does not list speed</td>
<td width="170">9000 mAh quick-release battery; about 2 h</td>
<td width="300">Depth camera + 3D LiDAR; 8-core CPU, optional Orin on EDU</td>
<td width="220">None on base model; EDU can add a 7-DoF Dex3-1 per hand and 2-DoF wrists</td>
</tr>
<tr>
<td width="170" nowrap><a href="https://www.unitree.com/R1/">R1 AIR / R1 / R1 EDU</a><br>Ultra-light, lower-cost platform</td>
<td width="150">123 cm / about 27, 29, 29 kg</td>
<td width="150">20 / 26 / 26–40; 6 per leg and 4/5/5 per arm</td>
<td width="300">Arm payload about 2 kg; joint torque and mobility speed not published</td>
<td width="170">Quick-release lithium battery; about 1 h</td>
<td width="300">8-core processor; monocular on AIR, binocular on R1/EDU; optional 40–100 TOPS Orin on EDU</td>
<td width="220">Only EDU explicitly supports an optional dexterous hand</td>
</tr>
<tr>
<td width="170" nowrap><a href="https://www.unitree.com/H2/">H2 / H2 EDU</a><br>Full-size humanoid with a human-like head</td>
<td width="150">182 cm / about 70 kg</td>
<td width="150">31: 6 per leg, 7 per arm, 3 waist, 2 head</td>
<td width="300">Arm/leg peak torque 120/360 N·m; arm payload about 15 kg peak / 7 kg rated; speed not published</td>
<td width="170">15 Ah / 0.972 kWh; about 3 h</td>
<td width="300">Wide-FOV binocular camera; i5 on H2, additional i7 and optional Thor on EDU</td>
<td width="220">None on H2; multiple hand options on H2 EDU</td>
</tr>
<tr>
<td width="170" nowrap><a href="https://www.unitree.com/H2plus/">H2 Plus</a><br>NVIDIA Isaac GR00T full-stack research configuration</td>
<td width="150">182 cm / about 70 kg</td>
<td width="150">31 body DoF; 75 total with both hands</td>
<td width="300">Arm/leg peak torque 120/360 N·m; arm payload about 15 kg peak / 7 kg rated</td>
<td width="170">0.972 kWh; about 3 h</td>
<td width="300">i5+i7 + Jetson T5000; detailed page lists 2070 TFLOPS FP4 sparse and 128 GB unified memory; head stereo and optional wrist cameras</td>
<td width="220">Dual SharpaWave five-finger tactile hands, 22 active DoF each; 75 DoF system total</td>
</tr>
</tbody>
</table>

Scope notes: the R1 page labels a value of about 2 kg as “Arm Joint Torque,” but its footnote describes arm payload, so the table records payload and treats torque as unpublished. The H2 hero-page phrase “2070 TOPS” must also not be merged with the H2 Plus detailed specification of “2070 TFLOPS (FP4 sparse)” as if they were the same metric.

## AgiBot biped models and specifications

<table width="1330">
<thead>
<tr>
<th width="170" nowrap>Model / status</th>
<th width="150">Height / weight</th>
<th width="130">Active DoF</th>
<th width="110">Speed</th>
<th width="180">Endurance</th>
<th width="350">Payload, compute, and perception</th>
<th width="240">Hand form</th>
</tr>
</thead>
<tbody>
<tr>
<td width="170" nowrap><a href="https://www.agibot.com/products/A2_Ultra">A2 Ultra</a><br>Flagship full-size biped</td>
<td width="150">169 cm / about 69 kg</td>
<td width="130">40 including both hands: 2 neck, 7 per arm, 6 per leg, 6 per hand</td>
<td width="110">Up to 1.2 m/s</td>
<td width="180">14.4 Ah; about 3 h standing and 1.5 h+ walking; charging or battery swapping</td>
<td width="350">About 2 kg per arm; 16-core CPU + Jetson AGX Orin 64 GB; LiDAR, RGB-D, RGB, and fisheye cameras</td>
<td width="240">Native 6-DoF hand per side; no tactile-array count published</td>
</tr>
<tr>
<td width="170" nowrap><a href="https://www.agibot.com/products/A2_Ultra">A2 Lite</a><br>Entry/performance full-size biped</td>
<td width="150">169 cm / about 64 kg</td>
<td width="130">23: 1 neck, 5 per arm, 6 per leg; hands excluded</td>
<td width="110">Up to 0.8 m/s</td>
<td width="180">14.4 Ah; about 4.5 h standing and 1.5 h+ walking</td>
<td width="350">About 2 kg per arm; 16-core CPU; no high-performance board or LiDAR/RGB-D/RGB/fisheye suite</td>
<td width="240">Soft cosmetic hands, not dexterous hands</td>
</tr>
<tr>
<td width="170" nowrap><a href="https://www.agibot.com/products/A2_Max">A2 Max</a><br>Marked “Coming soon”</td>
<td width="150">175 cm / 85 kg</td>
<td width="130">67 total / 53 active; 19 total / 12 active per hand</td>
<td width="110">1 m/s</td>
<td width="180">About 2 h with battery swapping</td>
<td width="350">40 kg across the full workspace; 8800 N leg thrust; 450 N·m peak dual-arm joint torque</td>
<td width="240">Industrial five-finger hand; pre-release status must be kept separate from shipping products</td>
</tr>
<tr>
<td width="170" nowrap><a href="https://www.agibot.com/products/A3">A3</a><br>2026 full-size biped</td>
<td width="150">173 cm / 55 kg</td>
<td width="130">31 body DoF excluding hands: 2 neck, 7 per arm, 3 waist, 6 per leg</td>
<td width="110">Daily maximum 1.8 m/s; laboratory 2.5 m/s; maximum running speed 5 m/s</td>
<td width="180">1152 Wh; about 10 h mixed duty, 6 h standing, and &gt;4 h continuous walking; battery swapping</td>
<td width="350">5 kg per arm; RK3588×2; stereo RGB, GPS, UWB, and shoulder touch sensors</td>
<td width="240">Standard silicone hands/fists with no active finger DoF; not dexterous hands</td>
</tr>
<tr>
<td width="170" nowrap><a href="https://www.agibot.com/products/X1">X1</a><br>Mid-size full-stack open-source biped</td>
<td width="150">130 cm / 33 kg</td>
<td width="130">34</td>
<td width="110">Up to 1 m/s</td>
<td width="180">About 2 h</td>
<td width="350">0.5 kg per arm; current page does not publish one unified compute/perception configuration</td>
<td width="240">OmniPicker adaptive gripper: 30 N, 120 mm stroke, 0.7 s cycle; not a five-finger hand</td>
</tr>
<tr>
<td width="170" nowrap><a href="https://www.agibot.com/products/X2">X2</a><br>Half-size base biped</td>
<td width="150">About 131 cm / 35 kg</td>
<td width="130">25: 0 neck, 5 per arm, 3 waist, 6 per leg</td>
<td width="110">Typical ≤0.8 m/s; up to 1.8 m/s; laboratory ≤2 m/s</td>
<td width="180">About 500 Wh; about 2 h at 0.5 m/s; swappable battery</td>
<td width="350">3 kg in specified poses and ≤1 kg over the full workspace; RK3588×2; interaction RGB but no LiDAR/RGB-D</td>
<td width="240">Base X2 does not support the Ultra-only OmniHand/OmniPicker option</td>
</tr>
<tr>
<td width="170" nowrap><a href="https://www.agibot.com/products/X2">X2 Ultra</a><br>Half-size high-spec biped</td>
<td width="150">About 131 cm / 39 kg</td>
<td width="130">30: 1 neck, 7 per arm, 3 waist, 6 per leg</td>
<td width="110">Typical ≤0.8 m/s; up to 1.8 m/s; laboratory ≤2 m/s</td>
<td width="180">About 500 Wh; about 2 h at 0.5 m/s; swappable battery and optional charging dock</td>
<td width="350">3 kg in specified poses and ≤1 kg over the full workspace; RK3588×2 + Orin NX 157 TOPS; LiDAR, RGB-D, front/rear RGB</td>
<td width="240">Optional OmniHand or OmniPicker; neither is standard</td>
</tr>
</tbody>
</table>

## Lab-built biped platforms in papers

Here, “lab-built” means that the author team designed or manufactured the core mechanical and electrical platform and validated it on hardware. HumanPlus and OmniH2O therefore remain commercial H1 bodies with research-team wrist/hand integrations, rather than fully lab-built robots.

<table width="1400">
<thead>
<tr>
<th width="180" nowrap>Platform / venue</th>
<th width="150">Height / weight</th>
<th width="130">Active DoF</th>
<th width="360">Measured capability</th>
<th width="320">Compute / sensing</th>
<th width="260">Hand and correct classification</th>
</tr>
</thead>
<tbody>
<tr>
<td width="180" nowrap><a href="https://hybrid-robotics.berkeley.edu/publications/ICRA2025_Berkeley_Humanoid.pdf">Berkeley Humanoid</a><br>ICRA 2025</td>
<td width="150">0.85 m / 16 kg</td>
<td width="130">12 on the tested robot: 6 per leg</td>
<td width="360">364 m in a 10-minute campus walk and 96 m in a 5-minute trail test; no rated product endurance/payload</td>
<td width="320">Intel NUC, low-cost IMU, dual batteries; expansion interfaces for RGB-D/LiDAR</td>
<td width="260">The design discusses two 4-DoF arms, but the validated robot had no arms or hands; classify it as a lab-built biped locomotion platform</td>
</tr>
<tr>
<td width="180" nowrap><a href="https://lite.berkeley-humanoid.org/">Berkeley Humanoid Lite</a><br>RSS 2025</td>
<td width="150">0.8 m / 16 kg</td>
<td width="130">22 body DoF: 12 legs + 10 arms; grippers excluded</td>
<td width="360">6S 4000 mAh, about 30 minutes; demonstrates walking and teleoperated writing, block, and Rubik's-cube tasks</td>
<td width="320">Intel N95 mini PC + IMU; modular 3D-printed cycloidal gearboxes; hardware cost under $5,000</td>
<td width="260">Two 5-DoF arms with integrated grippers; not five-finger dexterous hands</td>
</tr>
<tr>
<td width="180" nowrap><a href="https://proceedings.mlr.press/v305/shi25a.html">ToddlerBot</a><br>CoRL 2025</td>
<td width="150">0.56 m / 3.4 kg</td>
<td width="130">30 body DoF: 7 per arm, 6 per leg, 2 neck, 2 waist; end effectors excluded</td>
<td width="360">Lifts 1.484 kg; practical battery duration about 2 h; the 19-minute continuous stepping test is a thermal/control test, not battery endurance</td>
<td width="320">Jetson Orin NX 16 GB, dual fisheye cameras, IMU, two microphones and speaker; system cost under $6,000</td>
<td width="260">Quick-change parallel gripper or compliant palm; not a five-finger dexterous hand</td>
</tr>
</tbody>
</table>

## Humanoid-body and dexterous-hand configurations

<table width="1200">
<thead>
<tr>
<th width="200" nowrap>Vendor / end effector</th>
<th width="180">Form</th>
<th width="320">DoF and sensing</th>
<th width="180">Weight / force</th>
<th width="320">Explicit humanoid compatibility</th>
</tr>
</thead>
<tbody>
<tr>
<td width="200" nowrap><a href="https://www.unitree.com/Dex2-5/">Unitree Dex2/5</a></td>
<td width="180">Five-finger tendon hand for lightweight grasping and gestures</td>
<td width="320">10 motion DoF, 2 active DoF; no tactile array listed</td>
<td width="180">365 g; maximum grasp about 1.5 kg</td>
<td width="320">G1 and R1</td>
</tr>
<tr>
<td width="200" nowrap><a href="https://www.unitree.com/Dex3-1/">Unitree Dex3-1</a></td>
<td width="180">Three-finger force-controlled hand</td>
<td width="320">7 active DoF; up to 33 tactile sensing elements</td>
<td width="180">710 g; about 0.5 kg palm-down grasp</td>
<td width="320">G1, especially G1 EDU/flagship configurations</td>
</tr>
<tr>
<td width="200" nowrap><a href="https://www.unitree.com/Dex5-1/">Unitree Dex5-1 / Dex5-1P</a></td>
<td width="180">High-DoF five-finger hand</td>
<td width="320">20 DoF (16 active + 4 coupled); 94 pressure elements per hand on P</td>
<td width="180">About 1.1 kg; fingertip force about 10 N</td>
<td width="320">Explicit option on H1-2</td>
</tr>
<tr>
<td width="200" nowrap><a href="https://www.unitree.com/H2plus/">Dual SharpaWave hands</a></td>
<td width="180">Dense-tactile H2 Plus research configuration</td>
<td width="320">22 active DoF per hand; &gt;1000 tactile pixels per fingertip</td>
<td width="180">1.3 kg per hand; 150 N grip force and 20 N fingertip force</td>
<td width="320">H2 Plus; 31 body + 44 hand DoF = 75 system DoF</td>
</tr>
<tr>
<td width="200" nowrap><a href="https://www.agibot.com/products/OmniHand_O10">AgiBot OmniHand 2025</a></td>
<td width="180">Five-finger interaction/light-duty dexterous hand</td>
<td width="320">10 active / 16 total DoF; 400+ taxels on the tactile version</td>
<td width="180">≤550 g tactile version; typical fingertip force 5 N</td>
<td width="320">Official option on X2 Ultra; sold as an A2 retrofit but not part of the native A2 40-DoF count</td>
</tr>
<tr>
<td width="200" nowrap><a href="https://www.agibot.com/products/OmniHand_O12">AgiBot OmniHand Pro 2025</a></td>
<td width="180">Five-finger professional manipulation hand</td>
<td width="320">12 active / 19 total DoF; 150+ taxels, 3-axis fingertip force and 1-axis palm force</td>
<td width="180">≤750 g; typical fingertip force 20 N</td>
<td width="320">General robot/arm end effector; no current per-model evidence that it is standard on A3 or X1</td>
</tr>
<tr>
<td width="200" nowrap>AgiBot OmniPicker</td>
<td width="180">Adaptive two-finger gripper, not a dexterous hand</td>
<td width="320">120 mm stroke; 0.7 s open/close cycle</td>
<td width="180">0.43 kg; maximum clamping force 30 N</td>
<td width="320">Official X1 configuration and optional X2 Ultra end effector</td>
</tr>
</tbody>
</table>

Both ecosystems use the general pattern “walking body + replaceable end effector + vision/touch + optional high-performance compute,” but their product tiers differ. Unitree typically adds wrists, hands, and tactile sensing on EDU or high-spec versions, with H2 Plus becoming the complete dense-tactile reference stack. AgiBot A2 Ultra uses a native 6-DoF hand, X2 Ultra exposes OmniHand/OmniPicker as options, and standard A3 still uses non-actuated silicone hands. Comparisons therefore need to name the body version, end-effector model, active versus passive DoF, and whether tactile sensing is standard or optional.
