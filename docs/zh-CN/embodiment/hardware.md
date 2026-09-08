# 人形与双足硬件参考

[首页](../../../README.zh-CN.md) | [英文](../../en/embodiment/hardware.md) | [方向目录](README.md)

本节只保留硬件索引：宇树与智元双足型号、自研平台，以及人形机体与灵巧手/夹爪的组合方式。论文不再在这里另起一张表；会议、方法、具体本体、验证形态、解决问题、当前瓶颈和未来趋势，统一合入唯一的[人形机器人论文主表](humanoid.md)。以下参数核对至 **2026-07-10**。

> [!IMPORTANT]
> “机体自由度”默认不含可选末端，只有厂商明确给出整机总数时才把双手计入。双足表有意排除宇树 G1-D/R1-D/H2-D，以及智元 A2-W/G1/G2 等轮式或固定底座平台。论文主表中的 `Sim Only` 表示只使用对应机器人模型/URDF，并不代表完成了实机部署。

## 宇树双足型号与参数

<table width="1460">
<thead>
<tr>
<th width="170" nowrap>型号 / 定位</th>
<th width="150">身高 / 重量</th>
<th width="150">机体自由度</th>
<th width="300">关节、负载与速度</th>
<th width="170">电池 / 续航</th>
<th width="300">感知与算力</th>
<th width="220">灵巧手形态</th>
</tr>
</thead>
<tbody>
<tr>
<td width="170" nowrap><a href="https://www.unitree.com/h1/">H1</a><br>首款全尺寸通用人形</td>
<td width="150">约 180 cm / 47 kg</td>
<td width="150">官方总计 19；单腿 5、单臂 4（可扩展）</td>
<td width="300">膝约 360 N·m、髋约 220 N·m、踝约 59 N·m、臂约 75 N·m；标称 3.3 m/s</td>
<td width="170">15 Ah / 0.864 kWh，可快换；官网未给小时续航</td>
<td width="300">三维激光雷达 + 深度相机；i5 平台机 + i7 开发机，可选 i7/Orin NX</td>
<td width="220">选配；官网未指定标准手型</td>
</tr>
<tr>
<td width="170" nowrap><a href="https://www.unitree.com/h1/">H1-2</a><br>全身操作高自由度版</td>
<td width="150">约 178 cm / 70 kg</td>
<td width="150">27；单腿 6、单臂 7</td>
<td width="300">腿峰值 360 N·m；肩/肘约 120 N·m、腕约 30 N·m；单臂峰值约 21 kg、额定约 7 kg；速度 &lt;2 m/s</td>
<td width="170">15 Ah / 0.864 kWh，可快换</td>
<td width="300">三维激光雷达 + 深度相机；i5+i7，可选最多 3 块 Orin NX</td>
<td width="220">明确可选 Dex5-1 或其他灵巧手</td>
</tr>
<tr>
<td width="170" nowrap><a href="https://www.unitree.com/g1/">G1 / G1 EDU</a><br>紧凑型研究与教育平台</td>
<td width="150">132 cm / 约 35 kg、35 kg+</td>
<td width="150">23 / 23–43；单腿 6、单臂 5；EDU 可增加腰、腕和手</td>
<td width="300">膝最大 90 / 120 N·m；单臂约 2 / 3 kg；当前参数表未列速度</td>
<td width="170">9000 mAh 快拆电池；约 2 h</td>
<td width="300">深度相机 + 三维激光雷达；8 核 CPU，EDU 可选 Orin</td>
<td width="220">标准版无；EDU 可选单手 7 自由度 Dex3-1，并可增加每侧 2 自由度手腕</td>
</tr>
<tr>
<td width="170" nowrap><a href="https://www.unitree.com/R1/">R1 AIR / R1 / R1 EDU</a><br>超轻、低成本平台</td>
<td width="150">123 cm / 约 27、29、29 kg</td>
<td width="150">20 / 26 / 26–40；单腿均 6，单臂 4/5/5</td>
<td width="300">单臂负载约 2 kg；关节扭矩和移动速度未公开</td>
<td width="170">快拆锂电；约 1 h</td>
<td width="300">8 核处理器；AIR 单目、R1/EDU 双目；EDU 可选 Orin 40–100 TOPS</td>
<td width="220">仅 EDU 明确支持选配灵巧手</td>
</tr>
<tr>
<td width="170" nowrap><a href="https://www.unitree.com/H2/">H2 / H2 EDU</a><br>全尺寸仿生头人形</td>
<td width="150">182 cm / 约 70 kg</td>
<td width="150">31：单腿 6、单臂 7、腰 3、头 2</td>
<td width="300">臂关节峰值 120 N·m、腿关节峰值 360 N·m；单臂峰值约 15 kg、额定约 7 kg；速度未公开</td>
<td width="170">15 Ah / 0.972 kWh；约 3 h</td>
<td width="300">宽视场双目；H2 为 i5，EDU 增加 i7 并可选 Thor</td>
<td width="220">H2 无；H2 EDU 可选多种灵巧手</td>
</tr>
<tr>
<td width="170" nowrap><a href="https://www.unitree.com/H2plus/">H2 Plus</a><br>NVIDIA Isaac GR00T 全栈研究配置</td>
<td width="150">182 cm / 约 70 kg</td>
<td width="150">机体 31；配置双手后共 75</td>
<td width="300">臂/腿峰值 120/360 N·m；单臂峰值约 15 kg、额定约 7 kg</td>
<td width="170">0.972 kWh；约 3 h</td>
<td width="300">i5+i7 + Jetson T5000；官网详表为 2070 TFLOPS（FP4 稀疏精度）、128 GB 统一内存；头部双目，可选腕部相机</td>
<td width="220">双 SharpaWave 五指触觉手，每手 22 个主动自由度；整机因此为 75 自由度</td>
</tr>
</tbody>
</table>

口径提醒：R1 官网把“臂部关节力矩”一栏写成约 2 kg，但脚注明确描述的是臂负载，因此表中只按负载记录，扭矩视为未公开。H2 首页的“2070 TOPS”宣传语也不能与 H2 Plus 详表的“2070 TFLOPS（FP4 稀疏精度）”合并为同一指标。

## 智元双足型号与参数

<table width="1330">
<thead>
<tr>
<th width="170" nowrap>型号 / 状态</th>
<th width="150">身高 / 重量</th>
<th width="130">主动自由度</th>
<th width="110">速度</th>
<th width="180">续航</th>
<th width="350">负载、算力与感知</th>
<th width="240">手部形态</th>
</tr>
</thead>
<tbody>
<tr>
<td width="170" nowrap><a href="https://www.agibot.com/products/A2_Ultra">A2 Ultra</a><br>旗舰全尺寸双足</td>
<td width="150">169 cm / 约 69 kg</td>
<td width="130">40，已含双手：颈 2、单臂 7、单腿 6、单手 6</td>
<td width="110">最大 1.2 m/s</td>
<td width="180">14.4 Ah；站立约 3 h、行走 1.5 h+；直充/换电</td>
<td width="350">单臂约 2 kg；16 核 CPU + Jetson AGX Orin 64 GB；激光雷达、RGB-D、RGB、鱼眼</td>
<td width="240">标配单手 6 自由度原生灵巧手；官网未给触觉阵列数</td>
</tr>
<tr>
<td width="170" nowrap><a href="https://www.agibot.com/products/A2_Ultra">A2 Lite</a><br>表演/入门全尺寸双足</td>
<td width="150">169 cm / 约 64 kg</td>
<td width="130">23：颈 1、单臂 5、单腿 6；手不计入</td>
<td width="110">最大 0.8 m/s</td>
<td width="180">14.4 Ah；站立约 4.5 h、行走 1.5 h+</td>
<td width="350">单臂约 2 kg；16 核 CPU；无高算力板及激光雷达/RGB-D/RGB/鱼眼</td>
<td width="240">软质仿生假手，不是灵巧手</td>
</tr>
<tr>
<td width="170" nowrap><a href="https://www.agibot.com/products/A2_Max">A2 Max</a><br>官网标注即将发布</td>
<td width="150">175 cm / 85 kg</td>
<td width="130">67 总自由度 / 53 主动自由度；单手 19 总 / 12 主动</td>
<td width="110">1 m/s</td>
<td width="180">约 2 h，支持换电</td>
<td width="350">全工作空间搬运 40 kg；腿部推力 8800 N；双臂关节峰值 450 N·m</td>
<td width="240">工业五指灵巧手；未量产状态需与在售型号分开看</td>
</tr>
<tr>
<td width="170" nowrap><a href="https://www.agibot.com/products/A3">A3</a><br>2026 全尺寸双足</td>
<td width="150">173 cm / 55 kg</td>
<td width="130">机体 31，不含手：颈 2、单臂 7、腰 3、单腿 6</td>
<td width="110">日常最大 1.8 m/s；实验室 2.5 m/s；最高跑速 5 m/s</td>
<td width="180">1152 Wh；综合约 10 h，站立约 6 h、连续行走 &gt;4 h；可换电</td>
<td width="350">单臂 5 kg；RK3588×2；双目 RGB、GPS、UWB、肩部触摸</td>
<td width="240">标准为硅胶手/硅胶拳，无主动手指自由度，不是灵巧手</td>
</tr>
<tr>
<td width="170" nowrap><a href="https://www.agibot.com/products/X1">X1</a><br>中型全栈开源双足</td>
<td width="150">130 cm / 33 kg</td>
<td width="130">34</td>
<td width="110">最大 1 m/s</td>
<td width="180">约 2 h</td>
<td width="350">单臂 0.5 kg；官方当前页未统一公开算力/感知配置</td>
<td width="240">OmniPicker 自适应夹爪：30 N、120 mm 行程、0.7 s 开合；不是五指灵巧手</td>
</tr>
<tr>
<td width="170" nowrap><a href="https://www.agibot.com/products/X2">X2</a><br>半尺寸基础双足</td>
<td width="150">约 131 cm / 35 kg</td>
<td width="130">25：颈 0、单臂 5、腰 3、单腿 6</td>
<td width="110">典型 ≤0.8 m/s；最高 1.8 m/s；实验室 ≤2 m/s</td>
<td width="180">约 500 Wh；0.5 m/s 下约 2 h；可换电</td>
<td width="350">特定姿态最大 3 kg、全工作域 ≤1 kg；RK3588×2；交互 RGB，无激光雷达/RGB-D</td>
<td width="240">基础 X2 不支持 Ultra 专属 OmniHand/OmniPicker 选配</td>
</tr>
<tr>
<td width="170" nowrap><a href="https://www.agibot.com/products/X2">X2 Ultra</a><br>半尺寸高配双足</td>
<td width="150">约 131 cm / 39 kg</td>
<td width="130">30：颈 1、单臂 7、腰 3、单腿 6</td>
<td width="110">典型 ≤0.8 m/s；最高 1.8 m/s；实验室 ≤2 m/s</td>
<td width="180">约 500 Wh；0.5 m/s 下约 2 h；可换电/可选自动充电</td>
<td width="350">特定姿态最大 3 kg、全工作域 ≤1 kg；RK3588×2 + Orin NX 157 TOPS；激光雷达、RGB-D、前后 RGB</td>
<td width="240">可选 OmniHand 或 OmniPicker，均非标配</td>
</tr>
</tbody>
</table>

## 论文中的自研双足平台

这里把“自研”限定为作者团队设计/制造核心机械与电气平台，并在论文中完成实机验证；在商用 H1 上自行加腕和手的 HumanPlus/OmniH2O 不归入此表。

<table width="1400">
<thead>
<tr>
<th width="180" nowrap>平台 / 会议</th>
<th width="150">身高 / 重量</th>
<th width="130">主动自由度</th>
<th width="360">实测能力</th>
<th width="320">算力 / 传感</th>
<th width="260">手部与正确分类</th>
</tr>
</thead>
<tbody>
<tr>
<td width="180" nowrap><a href="https://hybrid-robotics.berkeley.edu/publications/ICRA2025_Berkeley_Humanoid.pdf">Berkeley Humanoid</a><br>ICRA 2025</td>
<td width="150">0.85 m / 16 kg</td>
<td width="130">实验机 12：每腿 6</td>
<td width="360">校园 10 min 行走 364 m；山径 5 min 行走 96 m；论文未给产品额定续航/负载</td>
<td width="320">Intel NUC、低成本 IMU、双电池；预留 RGB-D/激光雷达接口</td>
<td width="260">论文设计过双 4 自由度臂，但验证实机未安装手臂和手；属于自研双足运动平台</td>
</tr>
<tr>
<td width="180" nowrap><a href="https://lite.berkeley-humanoid.org/">Berkeley Humanoid Lite</a><br>RSS 2025</td>
<td width="150">0.8 m / 16 kg</td>
<td width="130">机体 22：双腿 12 + 双臂 10；夹爪另算</td>
<td width="360">6S 4000 mAh，约 30 min；展示行走、书写、积木与魔方遥操作</td>
<td width="320">Intel N95 迷你电脑 + 惯性测量单元；模块化三维打印摆线减速器；硬件成本 &lt;5,000 美元</td>
<td width="260">双 5 自由度臂 + 集成夹爪；不是五指灵巧手</td>
</tr>
<tr>
<td width="180" nowrap><a href="https://proceedings.mlr.press/v305/shi25a.html">ToddlerBot</a><br>CoRL 2025</td>
<td width="150">0.56 m / 3.4 kg</td>
<td width="130">机体 30：单臂 7、单腿 6、颈 2、腰 2；末端另算</td>
<td width="360">实测举起 1.484 kg；电池实践约 2 h；连续踏步 19 min 是热/控制测试，不等同电池续航</td>
<td width="320">Jetson Orin NX 16 GB、双鱼眼、IMU、双麦克风与扬声器；整机成本 &lt;6,000 美元</td>
<td width="260">快换并联夹爪或柔顺掌；不是五指灵巧手</td>
</tr>
</tbody>
</table>

## 人形机体与灵巧手的组合形态

<table width="1200">
<thead>
<tr>
<th width="200" nowrap>厂商 / 末端</th>
<th width="180">形态</th>
<th width="320">自由度与传感</th>
<th width="180">重量 / 力</th>
<th width="320">明确适配的人形机体</th>
</tr>
</thead>
<tbody>
<tr>
<td width="200" nowrap><a href="https://www.unitree.com/Dex2-5/">宇树 Dex2/5</a></td>
<td width="180">五指腱绳手，偏轻量抓取/手势</td>
<td width="320">10 个运动自由度、2 个主动自由度；官网未列触觉阵列</td>
<td width="180">365 g；最大抓取约 1.5 kg</td>
<td width="320">G1、R1</td>
</tr>
<tr>
<td width="200" nowrap><a href="https://www.unitree.com/Dex3-1/">宇树 Dex3-1</a></td>
<td width="180">三指力控手</td>
<td width="320">7 个主动自由度；可配 33 个触觉传感单元</td>
<td width="180">710 g；掌心向下抓取约 0.5 kg</td>
<td width="320">G1，尤其 G1 EDU/旗舰配置</td>
</tr>
<tr>
<td width="200" nowrap><a href="https://www.unitree.com/Dex5-1/">宇树 Dex5-1 / Dex5-1P</a></td>
<td width="180">五指高自由度手</td>
<td width="320">20 自由度（16 主动 + 4 耦合）；P 版每手 94 个压力传感单元</td>
<td width="180">约 1.1 kg；指尖力约 10 N</td>
<td width="320">H1-2 官网明确列为选配</td>
</tr>
<tr>
<td width="200" nowrap><a href="https://www.unitree.com/H2plus/">SharpaWave 双五指手</a></td>
<td width="180">H2 Plus 的高密度触觉研究配置</td>
<td width="320">每手 22 个主动自由度；每个指尖 &gt;1000 触觉像素</td>
<td width="180">每手 1.3 kg；握力 150 N、指尖力 20 N</td>
<td width="320">H2 Plus；机体 31 + 双手 44 = 整机 75 自由度</td>
</tr>
<tr>
<td width="200" nowrap><a href="https://www.agibot.com/products/OmniHand_O10">智元 OmniHand 2025</a></td>
<td width="180">五指交互/轻作业灵巧手</td>
<td width="320">10 主动 / 16 总自由度；触觉版 400+ 触点</td>
<td width="180">触觉版 ≤550 g；典型指尖力 5 N</td>
<td width="320">X2 Ultra 官方选配；A2 可另购改装，但不是 A2 原生 40 自由度的组成口径</td>
</tr>
<tr>
<td width="200" nowrap><a href="https://www.agibot.com/products/OmniHand_O12">智元 OmniHand Pro 2025</a></td>
<td width="180">五指专业操作手</td>
<td width="320">12 主动 / 19 总自由度；150+ 触点，指尖三轴力 + 掌部一轴力</td>
<td width="180">≤750 g；典型指尖力 20 N</td>
<td width="320">通用机器人/机械臂末端；当前未找到 A3/X1 的逐机型标配证据</td>
</tr>
<tr>
<td width="200" nowrap>智元 OmniPicker</td>
<td width="180">自适应二指夹爪，不是灵巧手</td>
<td width="320">120 mm 行程；0.7 s 开合</td>
<td width="180">0.43 kg；最大夹持力 30 N</td>
<td width="320">X1 官方配置；X2 Ultra 可选</td>
</tr>
</tbody>
</table>

两家的共同思路都是“可行走机体 + 可替换末端 + 视觉/触觉 + 高算力模块”，但产品分层不同：宇树通常在 EDU/高配版增加腕、手和触觉，H2 Plus 才把高密度触觉双手做成完整参考配置；智元 A2 Ultra 使用原生 6 自由度手，X2 Ultra 改为 OmniHand/OmniPicker 可选末端，A3 标准款仍是无主动手指的硅胶手。因此比较时必须同时写清楚机体版本、末端型号、主动/被动自由度和触觉是否标配。
