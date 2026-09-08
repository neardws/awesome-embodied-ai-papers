# 基准与数据集

[首页](../../../README.zh-CN.md) | [英文](../../en/deployment/benchmarks-datasets.md) | [方向目录](README.md)

共 44 篇。

<table width="3090">
<thead>
<tr>
<th width="120" nowrap>会议/年份</th>
<th width="320">论文/方法</th>
<th width="420">摘要</th>
<th width="240">对象类型</th>
<th width="280">效率指标</th>
<th width="280">平台/硬件</th>
<th width="280">覆盖任务</th>
<th width="220">开放资源状态</th>
<th width="360">论文任务/目标</th>
<th width="110" nowrap>论文</th>
<th width="110" nowrap>项目</th>
<th width="110" nowrap>代码</th>
<th width="240">数据/基准</th>
</tr>
</thead>
<tbody>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2505.11709">EgoDex: Learning Dexterous Manipulation from Large-Scale Egocentric Video</a></td>
<td width="420">提供大规模第一视角人手—物体视频和未来手轨迹预测基准。</td>
<td width="240">人类第一视角灵巧 HOI 数据集</td>
<td width="280">829 h、338K 个回合、90M 1080p 帧、194 任务、约 2 TB；30 Hz</td>
<td width="280">Apple Vision Pro（visionOS 2/ARKit）；无机器人或仿真器</td>
<td width="280">194 类人类桌面交互；48-D 双手轨迹预测</td>
<td width="220"><a href="https://github.com/apple/ml-egodex">代码/数据</a></td>
<td width="360">2 s 预测中，EncDec+FM K=10 平均/最终误差 0.038/0.041 m；人类到机器人重定向只是未来工作，本文未验证</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2505.11709">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/apple/ml-egodex">代码</a></td>
<td width="240">EgoDex</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38894">Real Garment Benchmark (RGBench): A Comprehensive Benchmark for Robotic Garment Manipulation Featuring a High-Fidelity Scalable Simulator</a></td>
<td width="420">评测真实服装仿真保真度，并提供可扩展 FEM GPU 模拟器与服装资产。</td>
<td width="240">服装/柔性物体模拟器基准</td>
<td width="280">6K+ 个网格、10+ 材质/100+ 子类；最短步 2.7 ms；比 Isaac Sim 快 3–7×，20K 顶点时最高比 MuJoCo 快 65×</td>
<td width="280">双 AGILEX Piper 或双 JAKA K1 + DH PGC-50-35 夹爪；RealSense L515</td>
<td width="280">抓取、抛展、折叠；核心是模拟器保真度，不是学习策略</td>
<td width="220"><a href="https://rgbench.github.io/">项目</a> / <a href="https://github.com/hwk0809/RGBench">代码</a></td>
<td width="360">GarmentDynamics 平均仿真误差约降 20%；抓取/折叠倒角距离最高改善 35/58%</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38894">论文</a></td>
<td width="110" nowrap><a href="https://rgbench.github.io/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/hwk0809/RGBench">代码</a></td>
<td width="240">RGBench / GarmentDynamics；对比 MuJoCo、PyBullet、Isaac Sim</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2023</td>
<td width="320"><a href="https://scholar.google.com/scholar?q=Behavior-1K%3A+A+Benchmark+for+Embodied+AI+with+1%2C000+Everyday+Activities+and+Realistic+Simulation">Behavior-1K: A Benchmark for Embodied AI with 1,000 Everyday Activities and Realistic Simulation</a></td>
<td width="420">Behavior-1K 在逼真仿真环境中，以 1,000 项日常活动评测具身智能。</td>
<td width="240">基准/数据集</td>
<td width="280">部署/评测覆盖</td>
<td width="280">机器人/仿真器平台</td>
<td width="280">具身机器人任务</td>
<td width="220">来源列出的资源</td>
<td width="360">补充 CoRL 部署/评测研究覆盖。</td>
<td width="110" nowrap><a href="https://scholar.google.com/scholar?q=Behavior-1K%3A+A+Benchmark+for+Embodied+AI+with+1%2C000+Everyday+Activities+and+Realistic+Simulation">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2022</td>
<td width="320"><a href="https://scholar.google.com/scholar?q=iGibson+2.0%3A+Object-Centric+Simulation+for+Robot+Learning+of+Everyday+Household+Tasks">iGibson 2.0: Object-Centric Simulation for Robot Learning of Everyday Household Tasks</a></td>
<td width="420">iGibson 2.0 为家庭任务机器人学习提供以物体为中心的仿真。</td>
<td width="240">基准/数据集</td>
<td width="280">部署/评测覆盖</td>
<td width="280">机器人/仿真器平台</td>
<td width="280">具身机器人任务</td>
<td width="220">来源列出的资源</td>
<td width="360">补充 CoRL 部署/评测研究覆盖。</td>
<td width="110" nowrap><a href="https://scholar.google.com/scholar?q=iGibson+2.0%3A+Object-Centric+Simulation+for+Robot+Learning+of+Everyday+Household+Tasks">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CoRL 2017</td>
<td width="320"><a href="https://scholar.google.com/scholar?q=CARLA%3A+An+Open+Urban+Driving+Simulator">CARLA: An Open Urban Driving Simulator</a></td>
<td width="420">CARLA 是用于具身驾驶评测的开放城市驾驶仿真器。</td>
<td width="240">基准/数据集</td>
<td width="280">部署/评测覆盖</td>
<td width="280">机器人/仿真器平台</td>
<td width="280">具身机器人任务</td>
<td width="220">来源列出的资源</td>
<td width="360">补充 CoRL 部署/评测研究覆盖。</td>
<td width="110" nowrap><a href="https://scholar.google.com/scholar?q=CARLA%3A+An+Open+Urban+Driving+Simulator">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://openaccess.thecvf.com/content/ICCV2025/html/Zhong_UnrealZoo_Enriching_Photo-realistic_Virtual_Worlds_for_Embodied_AI_ICCV_2025_paper.html">UnrealZoo: Enriching Photo-realistic Virtual Worlds for Embodied AI</a></td>
<td width="420">UnrealZoo 扩展照片级逼真的虚拟世界，用于具身智能训练与评测。</td>
<td width="240">基准/数据集</td>
<td width="280">虚拟世界覆盖</td>
<td width="280">仿真平台</td>
<td width="280">具身导航与交互</td>
<td width="220">开放虚拟世界资源</td>
<td width="360">为具身智能提供更丰富的仿真环境。</td>
<td width="110" nowrap><a href="https://openaccess.thecvf.com/content/ICCV2025/papers/Zhong_UnrealZoo_Enriching_Photo-realistic_Virtual_Worlds_for_Embodied_AI_ICCV_2025_paper.pdf">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://openaccess.thecvf.com/content/CVPR2025/html/Chen_ActiveGAMER_Active_GAussian_Mapping_through_Efficient_Rendering_CVPR_2025_paper.html">ActiveGAMER: Active GAussian Mapping through Efficient Rendering</a></td>
<td width="420">ActiveGAMER 通过高效渲染进行主动高斯建图，支持具身场景理解。</td>
<td width="240">建图/评测</td>
<td width="280">建图效率</td>
<td width="280">高斯建图流程</td>
<td width="280">主动建图</td>
<td width="220">建图基准/资源</td>
<td width="360">提高具身智能体的主动建图效率。</td>
<td width="110" nowrap><a href="https://openaccess.thecvf.com/content/CVPR2025/papers/Chen_ActiveGAMER_Active_Gaussian_Mapping_through_Efficient_Rendering_CVPR_2025_paper.pdf">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2024</td>
<td width="320"><a href="https://openaccess.thecvf.com/content/CVPR2024/html/Yang_Holodeck_Language_Guided_Generation_of_3D_Embodied_AI_Environments_CVPR_2024_paper.html">Holodeck: Language Guided Generation of 3D Embodied AI Environments</a></td>
<td width="420">Holodeck 根据语言引导生成三维具身智能环境。</td>
<td width="240">基准/数据集</td>
<td width="280">三维环境多样性</td>
<td width="280">语言到环境生成器</td>
<td width="280">环境生成</td>
<td width="220">三维具身环境</td>
<td width="360">生成多样化三维场景，用于具身智能评测。</td>
<td width="110" nowrap><a href="https://openaccess.thecvf.com/content/CVPR2024/papers/Yang_Holodeck_Language_Guided_Generation_of_3D_Embodied_AI_Environments_CVPR_2024_paper.pdf">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2022</td>
<td width="320"><a href="https://proceedings.neurips.cc/paper_files/paper/2022/hash/27c546ab1e4f1d7d638e6a8dfbad9a07-Abstract-Conference.html">ProcTHOR: Large-Scale Embodied AI Using Procedural Generation</a></td>
<td width="420">ProcTHOR 通过程序化生成，创建大规模具身智能环境。</td>
<td width="240">基准/数据集</td>
<td width="280">程序化场景多样性</td>
<td width="280">AI2-THOR 环境生成</td>
<td width="280">导航与交互任务</td>
<td width="220">ProcTHOR</td>
<td width="360">利用生成房屋扩展具身智能评测。</td>
<td width="110" nowrap><a href="https://proceedings.neurips.cc/paper_files/paper/2022/file/27c546ab1e4f1d7d638e6a8dfbad9a07-Paper-Conference.pdf">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2024</td>
<td width="320"><a href="https://openaccess.thecvf.com/content/CVPR2024/html/Wang_EmbodiedScan_A_Holistic_Multi-Modal_3D_Perception_Suite_Towards_Embodied_AI_CVPR_2024_paper.html">EmbodiedScan: A Holistic Multi-Modal 3D Perception Suite Towards Embodied AI</a></td>
<td width="420">EmbodiedScan 为具身智能提供多模态三维感知套件。</td>
<td width="240">基准/数据集</td>
<td width="280">多模态三维感知覆盖</td>
<td width="280">数据集 + 基准</td>
<td width="280">三维感知任务</td>
<td width="220">EmbodiedScan</td>
<td width="360">评测具身智能体的整体三维感知。</td>
<td width="110" nowrap><a href="https://openaccess.thecvf.com/content/CVPR2024/papers/Wang_EmbodiedScan_A_Holistic_Multi-Modal_3D_Perception_Suite_Towards_Embodied_AI_CVPR_2024_paper.pdf">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ECCV 2024</td>
<td width="320"><a href="https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/01610.pdf">ReALFRED: An Embodied Instruction Following Benchmark in Photo-Realistic Environments</a></td>
<td width="420">ReALFRED 在照片级逼真环境中评测具身指令遵循。</td>
<td width="240">基准/数据集</td>
<td width="280">照片级逼真指令遵循覆盖</td>
<td width="280">基准</td>
<td width="280">指令遵循</td>
<td width="220">ReALFRED</td>
<td width="360">在逼真场景中评测具身指令遵循。</td>
<td width="110" nowrap><a href="https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/01610.pdf">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICRA 2026</td>
<td width="320"><a href="https://arxiv.org/abs/2509.14687">RealMirror: A Comprehensive, Open-Source Vision-Language-Action Platform for Embodied AI</a></td>
<td width="420">RealMirror 提供 VLA 数据采集、仿真、训练、评测和零样本仿真到现实迁移平台。</td>
<td width="240">VLA 平台 / 基准</td>
<td width="280">基准/数据集</td>
<td width="280">仿真/评测环境</td>
<td width="280">人形 VLA 研究</td>
<td width="220">项目/代码/模型已提供</td>
<td width="360">降低 VLA 数据、训练和评测门槛。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2509.14687">论文</a></td>
<td width="110" nowrap><a href="https://terminators2025.github.io/RealMirror.github.io/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/terminators2025/RealMirror">代码</a></td>
<td width="240"><a href="https://huggingface.co/zte-terminators/realmirror-model-ckpt">Hugging Face</a></td>
</tr>
<tr>
<td width="120" nowrap>IROS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2412.05313">lambda: A Benchmark for Data-Efficiency in Long-Horizon Indoor Mobile Manipulation Robotics</a></td>
<td width="420">λ 基准评测长程室内移动操作在数据效率、语言任务和多房间场景下的表现。</td>
<td width="240">基准/数据集</td>
<td width="280">数据效率</td>
<td width="280">室内移动操作基准</td>
<td width="280">长时程移动操作</td>
<td width="220">项目/代码/数据已提供</td>
<td width="360">补足长程移动操作数据效率评测。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2412.05313">论文</a></td>
<td width="110" nowrap><a href="https://lambdabenchmark.github.io/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/h2r/LAMBDA">代码</a></td>
<td width="240"><a href="https://github.com/h2r/LAMBDA">data</a></td>
</tr>
<tr>
<td width="120" nowrap>ICRA 2025</td>
<td width="320"><a href="https://github.com/BAAI-DCAI/SpatialBot">SpatialBot: Precise Spatial Understanding with Vision Language Models</a></td>
<td width="420">SpatialBot 面向视觉语言模型精确空间理解，提供本体数据、SpatialQA 和 SpatialBench。</td>
<td width="240">空间理解基准</td>
<td width="280">基准/数据集</td>
<td width="280">视觉语言模型空间推理</td>
<td width="280">具身空间问答</td>
<td width="220">模型/数据/基准已提供</td>
<td width="360">评测视觉语言模型是否具备可用于机器人操作的精确空间理解。</td>
<td width="110" nowrap><a href="https://github.com/BAAI-DCAI/SpatialBot">论文</a></td>
<td width="110" nowrap><a href="https://github.com/BAAI-DCAI/SpatialBot">项目</a></td>
<td width="110" nowrap><a href="https://github.com/BAAI-DCAI/SpatialBot">代码</a></td>
<td width="240"><a href="https://github.com/BAAI-DCAI/SpatialBot">data</a></td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=TRwQND3xpt">D2E: Scaling Vision-Action Pretraining on Desktop Data for Transfer to Embodied AI</a></td>
<td width="420">用桌面交互数据扩展视觉动作预训练并迁移到具身任务。</td>
<td width="240">桌面到具身数据集/预训练</td>
<td width="280">基准/数据集</td>
<td width="280">仿真/评测环境</td>
<td width="280">视觉动作迁移</td>
<td width="220">-</td>
<td width="360">解决机器人数据稀缺下如何利用桌面数据预训练的问题。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=TRwQND3xpt">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=PGUC3mmMoi">RoboInter: A Holistic Intermediate Representation Suite Towards Robotic Manipulation</a></td>
<td width="420">构建面向机器人操作的中间表示套件，用于统一理解、规划和动作评测。</td>
<td width="240">中间表示套件</td>
<td width="280">基准/数据集</td>
<td width="280">仿真/评测环境</td>
<td width="280">机器人操作</td>
<td width="220">-</td>
<td width="360">解决操作学习缺少可复用中间表示基准的问题。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=PGUC3mmMoi">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=UUE6HEtjhu">AutoBio: A Simulation and Benchmark for Robotic Automation in Digital Biology Laboratory</a></td>
<td width="420">提供数字生物实验室机器人自动化仿真与基准。</td>
<td width="240">基准/数据集</td>
<td width="280">基准/数据集</td>
<td width="280">数字生物实验室仿真</td>
<td width="280">实验室自动化</td>
<td width="220">-</td>
<td width="360">解决生物实验室自动化缺少仿真和评测环境的问题。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=UUE6HEtjhu">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=azj53PLJRL">Image Quality Assessment for Embodied AI</a></td>
<td width="420">研究具身 AI 观测图像质量评估及其对任务表现的影响。</td>
<td width="240">图像质量基准</td>
<td width="280">基准/数据集</td>
<td width="280">仿真/评测环境</td>
<td width="280">具身感知/评测</td>
<td width="220">-</td>
<td width="360">解决具身感知输入质量缺少任务相关评估的问题。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=azj53PLJRL">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICLR 2026</td>
<td width="320"><a href="https://openreview.net/forum?id=tQJYKwc3n4">RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots</a></td>
<td width="420">提供大规模家庭场景仿真框架训练和评测通用机器人。</td>
<td width="240">基准/数据集</td>
<td width="280">基准/数据集</td>
<td width="280">RoboCasa 仿真</td>
<td width="280">通用家庭机器人</td>
<td width="220">-</td>
<td width="360">解决通用机器人缺少多样、长期、可扩展仿真基准的问题。</td>
<td width="110" nowrap><a href="https://openreview.net/forum?id=tQJYKwc3n4">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38875">H-RDT: Human Manipulation Enhanced Bimanual Robotic Manipulation</a></td>
<td width="420">利用第一视角人类操作数据预训练扩散 Transformer 策略，提升双臂机器人操作能力。</td>
<td width="240">基准/数据集</td>
<td width="280">基准/数据集</td>
<td width="280">仿真/评测环境</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38875">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38883">PEOD: A Pixel-Aligned Event-RGB Benchmark for Object Detection Under Challenging Conditions</a></td>
<td width="420">提供高分辨率像素对齐 Event-RGB 目标检测基准，覆盖弱光、过曝和高速场景。</td>
<td width="240">基准/数据集</td>
<td width="280">基准/数据集</td>
<td width="280">仿真/评测环境</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38883">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38913">SIAM: Towards Generalizable Articulated Object Modeling via Single Robot-Object Interaction</a></td>
<td width="420">从单次机器人-物体交互推断关节物体的部件分割、运动学和 URDF 式模型。</td>
<td width="240">基准/数据集</td>
<td width="280">基准/数据集</td>
<td width="280">仿真/评测环境</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38913">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38923">VirtualEnv: A Platform for Embodied AI Research</a></td>
<td width="420">提供 Unreal Engine 5 仿真平台，用于在交互式具身任务中评测大语言模型/视觉语言模型智能体。</td>
<td width="240">基准/数据集</td>
<td width="280">基准/数据集</td>
<td width="280">仿真/评测环境</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38923">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>AAAI 2026</td>
<td width="320"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38930">Lifelong Language-Conditioned Robotic Manipulation Learning</a></td>
<td width="420">提出 SkillsCrafter，在持续学习语言条件操作技能时减少跨技能灾难性遗忘。</td>
<td width="240">基准/数据集</td>
<td width="280">基准/数据集</td>
<td width="280">仿真/评测环境</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38930">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/64411">AIR-VLA: Vision-Language-Action Systems for Aerial Manipulation</a></td>
<td width="420">构建空中操作系统的仿真、数据集和基准，用于评测 VLA/视觉语言模型能力。</td>
<td width="240">基准/数据集</td>
<td width="280">基准/数据集</td>
<td width="280">无人机/空中机器人</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/64411">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/63391">DLO-Lab: Benchmarking Deformable Linear Object Manipulations with Differentiable Physics</a></td>
<td width="420">提供可微物理仿真器和基准，用于柔性线状物体操作及仿真到现实研究。</td>
<td width="240">基准/数据集</td>
<td width="280">基准/数据集</td>
<td width="280">仿真/评测环境</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/63391">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/63416">ManiSoft: Towards Vision-Language Manipulation for Soft Robotics</a></td>
<td width="420">提供软体机械臂仿真基准，包含语言条件任务和专家轨迹，用于视觉语言操作研究。</td>
<td width="240">基准/数据集</td>
<td width="280">基准/数据集</td>
<td width="280">机器人部署/评测环境</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/63416">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2026</td>
<td width="320"><a href="https://icml.cc/virtual/2026/poster/64619">OXE-AugE: A Large-Scale Robot Augmentation of OXE for Scaling Cross-Embodiment Policy Learning</a></td>
<td width="420">用多样机器人本体扩展 Open X-Embodiment，以扩大跨本体策略学习规模。</td>
<td width="240">基准/数据集</td>
<td width="280">基准/数据集</td>
<td width="280">机器人部署/评测环境</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://icml.cc/virtual/2026/poster/64619">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2506.07961">BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models</a></td>
<td width="420">用输入输出对齐和 BridgeVLA 数据集提升视觉语言模型到三维操作策略学习效率。</td>
<td width="240">基准/数据集</td>
<td width="280">基准/数据集</td>
<td width="280">机器人部署/评测环境</td>
<td width="280">三维操作</td>
<td width="220">项目+代码+数据/基准</td>
<td width="360">解决视觉语言模型学习三维操作时输入输出空间不匹配的问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2506.07961">论文</a></td>
<td width="110" nowrap><a href="https://bridgevla.github.io/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/BridgeVLA/BridgeVLA">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2506.14763">RobotSmith: Generative Robotic Tool Design for Acquisition of Complex Manipulation Skills</a></td>
<td width="420">用生成式工具设计让机器人获得刚体、柔性和流体对象的复杂操作技能。</td>
<td width="240">基准/数据集</td>
<td width="280">基准/数据集</td>
<td width="280">机器人部署/评测环境</td>
<td width="280">工具设计操作</td>
<td width="220">项目+代码</td>
<td width="360">解决机器人需要专用工具才能完成复杂操作的问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2506.14763">论文</a></td>
<td width="110" nowrap><a href="https://umass-embodied-agi.github.io/RobotSmith/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/UMass-Embodied-AGI/RobotSmith">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2511.00940">URDF-Anything: Constructing Articulated Objects with 3D Multimodal Language Model</a></td>
<td width="420">用三维多模态语言模型从多模态输入构建关节物体 URDF。</td>
<td width="240">关节物体 URDF 构建</td>
<td width="280">基准/数据集</td>
<td width="280">机器人部署/评测环境</td>
<td width="280">用于仿真的三维物体建模</td>
<td width="220">-</td>
<td width="360">解决仿真/机器人交互中关节物体 URDF 构建成本高的问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2511.00940">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2506.08822">FreqPolicy: Efficient Flow-based Visuomotor Policy via Frequency Consistency</a></td>
<td width="420">用频率一致性约束提升基于流的视觉运动策略效率和稳定性。</td>
<td width="240">基准/数据集</td>
<td width="280">频率一致性</td>
<td width="280">机器人部署/评测环境</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">解决流策略在视觉运动控制中高频/低频动作不一致问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2506.08822">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://www.arxiv.org/pdf/2506.06677">RoboCerebra: A Large-scale Benchmark for Long-horizon Robotic Manipulation Evaluation</a></td>
<td width="420">提供长时程家庭机器人操作基准，评估规划、反思和记忆能力。</td>
<td width="240">基准/数据集</td>
<td width="280">基准/数据集</td>
<td width="280">仿真/评测环境</td>
<td width="280">100 种任务变体 / 1,000 条轨迹</td>
<td width="220">项目+代码+数据/基准</td>
<td width="360">解决长时程机器人操作缺少系统评测的问题。</td>
<td width="110" nowrap><a href="https://www.arxiv.org/pdf/2506.06677">论文</a> / <a href="https://arxiv.org/pdf/2506.06677">论文</a></td>
<td width="110" nowrap><a href="https://robocerebra.github.io/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/qiuboxiang/RoboCerebra">代码</a> / <a href="https://github.com/buaa-colalab/RoboCerebra">代码</a></td>
<td width="240"><a href="https://huggingface.co/datasets/qiukingballball/RoboCerebra">Hugging Face</a> / <a href="https://huggingface.co/datasets/qiukingballball/RoboCerebraBench">Hugging Face</a></td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://suturebot.github.io/static/SutureBot_NeurIPS_2025.pdf">SutureBot: A Precision Framework &amp; Benchmark For Autonomous End-to-End Suturing</a></td>
<td width="420">提供 dVRK 端到端自主缝合框架、数据集和精细评测基准。</td>
<td width="240">基准/数据集</td>
<td width="280">基准/数据集</td>
<td width="280">dVRK Si + 腕部相机/内窥镜</td>
<td width="280">-</td>
<td width="220">项目+代码+数据/基准</td>
<td width="360">解决机器人自主缝合缺少端到端基准和数据的问题。</td>
<td width="110" nowrap><a href="https://suturebot.github.io/static/SutureBot_NeurIPS_2025.pdf">论文</a></td>
<td width="110" nowrap><a href="https://suturebot.github.io/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/SutureBot/SutureBot/tree/ACT">代码</a></td>
<td width="240"><a href="https://huggingface.co/datasets/jchen396/SutureBot">Hugging Face</a></td>
</tr>
<tr>
<td width="120" nowrap>NeurIPS 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2503.08367">Embodied Crowd Counting</a></td>
<td width="420">定义具身人群计数任务，提供无人机仿真器、ECCD 数据集和零样本导航基线。</td>
<td width="240">基准/数据集</td>
<td width="280">基准/数据集</td>
<td width="280">机器人部署/评测环境</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2503.08367">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2412.06782">CARP: Visuomotor Policy Learning via Coarse-to-Fine Autoregressive Prediction</a></td>
<td width="420">通过粗到细自回归预测提升视觉运动策略学习。</td>
<td width="240">基准/数据集</td>
<td width="280">基准/数据集</td>
<td width="280">机器人部署/评测环境</td>
<td width="280">-</td>
<td width="220">项目</td>
<td width="360">解决连续机器人动作直接预测难、长时程误差累积的问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2412.06782">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2503.16408">RoboFactory: Exploring Embodied Agent Collaboration with Compositional Constraints</a></td>
<td width="420">构建带组合约束的多具身智能体协作仿真与数据集。</td>
<td width="240">基准/数据集</td>
<td width="280">基准/数据集</td>
<td width="280">仿真</td>
<td width="280">-</td>
<td width="220">项目+代码+数据/基准</td>
<td width="360">解决具身智能体协作任务中组合约束评测不足的问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2503.16408">论文</a></td>
<td width="110" nowrap><a href="https://iranqin.github.io/robofactory/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/MARS-EAI/RoboFactory">代码</a></td>
<td width="240"><a href="https://huggingface.co/datasets/FACEONG/RoboFactory_Dataset">Hugging Face</a></td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2504.10414">HUMOTO: A 4D Dataset of Mocap Human Object Interactions</a></td>
<td width="420">提供人体-物体交互的四维动捕数据集。</td>
<td width="240">四维动作捕捉人—物交互数据集</td>
<td width="280">基准/数据集</td>
<td width="280">仿真/评测环境</td>
<td width="280">-</td>
<td width="220">项目</td>
<td width="360">解决人体操作物体动态数据不足的问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2504.10414">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2412.07215">RoboTron-Mani: All-in-One Multimodal Large Model for Robotic Manipulation</a></td>
<td width="420">提出 RoboTron-Mani 模型及 RoboData，用多模态数据支持机器人操作。</td>
<td width="240">RoboTron-Mani + RoboData</td>
<td width="280">基准/数据集</td>
<td width="280">机器人部署/评测环境</td>
<td width="280">-</td>
<td width="220">代码+数据/基准</td>
<td width="360">解决机器人操作模型需要统一多模态训练和评测数据的问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2412.07215">论文</a> / <a href="https://arxiv.org/pdf/2412.07215">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap><a href="https://github.com/RoboUniview/RoboMM">代码</a></td>
<td width="240"><a href="https://huggingface.co/datasets/liufanfanlff/RoboData">Hugging Face</a></td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2503.11117">Beyond the Destination: A Novel Benchmark for Exploration-Aware Embodied Question Answering</a></td>
<td width="420">提出 EXPRESS-Bench，把探索轨迹和问答绑定评估具身问答。</td>
<td width="240">基准/数据集</td>
<td width="280">基准/数据集</td>
<td width="280">仿真/评测环境</td>
<td width="280">777 条轨迹 / 2,044 个问答对</td>
<td width="220">代码</td>
<td width="360">解决 EQA 只看目的地、不评估探索过程的问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2503.11117">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">EXPRESS-Bench</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://iccv.thecvf.com/virtual/2025/poster/1787">RobAVA: A Large-scale Dataset and Baseline Towards Video based Robotic Arm Action Understanding</a></td>
<td width="420">提供大规模视频数据集和基线，用于机器人臂动作理解。</td>
<td width="240">基准/数据集</td>
<td width="280">基准/数据集</td>
<td width="280">仿真/评测环境</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">提供训练/评测数据资源</td>
<td width="110" nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/1787">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICCV 2025</td>
<td width="320"><a href="https://iccv.thecvf.com/virtual/2025/poster/2215">RoboAnnotatorX: A Comprehensive and Universal Annotation Framework for Accurate Understanding of Long-horizon Robot Demonstration</a></td>
<td width="420">提供多模态标注框架，为长时程机器人示教生成丰富标签。</td>
<td width="240">基准/数据集</td>
<td width="280">基准/数据集</td>
<td width="280">机器人部署/评测环境</td>
<td width="280">-</td>
<td width="220">-</td>
<td width="360">-</td>
<td width="110" nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/2215">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>ICML 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2502.09560">EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents</a></td>
<td width="420">综合评测多模态大语言模型在视觉驱动具身智能体中的导航、交互和推理能力。</td>
<td width="240">基准/数据集</td>
<td width="280">基准/数据集</td>
<td width="280">仿真/评测环境</td>
<td width="280">1,128 项任务 / 4 个环境 / 6 个能力子集</td>
<td width="220">项目+代码</td>
<td width="360">解决多模态大模型具身能力缺少统一基准的问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2502.09560">论文</a></td>
<td width="110" nowrap><a href="https://embodiedbench.github.io/">项目</a></td>
<td width="110" nowrap><a href="https://github.com/EmbodiedBench/EmbodiedBench">代码</a></td>
<td width="240">-</td>
</tr>
<tr>
<td width="120" nowrap>CVPR 2025</td>
<td width="320"><a href="https://arxiv.org/abs/2411.18025">Pixel-aligned RGB-NIR Stereo Imaging and Dataset for Robot Vision</a></td>
<td width="420">提供像素对齐 RGB-NIR 双目成像系统和机器人视觉数据集。</td>
<td width="240">RGB-NIR 双目数据集</td>
<td width="280">基准/数据集</td>
<td width="280">仿真/评测环境</td>
<td width="280">机器人视觉</td>
<td width="220">-</td>
<td width="360">解决机器人视觉在可见光/NIR 融合下缺少对齐数据的问题。</td>
<td width="110" nowrap><a href="https://arxiv.org/abs/2411.18025">论文</a></td>
<td width="110" nowrap>-</td>
<td width="110" nowrap>-</td>
<td width="240">-</td>
</tr>
</tbody>
</table>
