#!/usr/bin/env python3
"""Build bilingual landscape pages and diagrams from topic-sized source files."""
from pathlib import Path
from html import escape
import json
import re
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'sources/landscape'
LANGS = ('en', 'zh-CN')
INDEX = json.loads((BASE / 'index.json').read_text())
TOPICS = [json.loads((BASE / 'topics' / (name + '.json')).read_text()) for name in INDEX['topics']]
SOURCES = {s['id']: s for s in json.loads((BASE / 'sources.json').read_text())}
MANIFEST = json.loads((ROOT / 'docs/manifest.json').read_text())
DOMAIN_COUNT = len(TOPICS)
SUBCATEGORY_COUNT = sum(len(t['subcategories']) for t in TOPICS)
PAPER_NAMES = {sub['path']: sub['title'] for t in MANIFEST['tracks'] for sub in t['subdirections']}
PAPER_NAMES.update({t['id'] + '/README.md': t['title'] for t in MANIFEST['tracks']})
EVIDENCE = {
    'R': {'en': 'Research demonstration', 'zh-CN': '研究展示'},
    'O': {'en': 'Code or data public; not reproduced here', 'zh-CN': '代码或数据公开；本项目未复现'},
    'P': {'en': 'Product or developer documentation public', 'zh-CN': '产品或开发资料公开'},
    'F': {'en': 'Operator-disclosed field deployment', 'zh-CN': '运营方披露现场部署'},
}


def bi(en, zh, lang):
    return en if lang == 'en' else zh


def link(label, target):
    return f'<a href="{escape(target, quote=True)}">{escape(label)}</a>'


def table(headers, widths, rows):
    out = [f'<table width="{sum(widths)}">', '<thead>', '<tr>']
    out += [f'<th width="{w}"' + (' nowrap' if i == 0 else '') + f'>{escape(h)}</th>' for i, (h, w) in enumerate(zip(headers, widths))]
    out += ['</tr>', '</thead>', '<tbody>']
    for row in rows:
        assert len(row) == len(widths)
        out += ['<tr>'] + [f'<td width="{w}"' + (' nowrap' if i == 0 else '') + f'>{c}</td>' for i, (w, c) in enumerate(zip(widths, row))] + ['</tr>']
    return '\n'.join(out + ['</tbody>', '</table>']) + '\n'


def nav(lang, filename):
    home = '../../../README.md' if lang == 'en' else '../../../README.zh-CN.md'
    other = 'zh-CN' if lang == 'en' else 'en'
    return f'[{bi("Home", "首页", lang)}]({home}) | [{bi("中文", "英文", lang)}](../../{other}/landscape/{filename}) | [{bi("Landscape index", "全景目录", lang)}](README.md)\n'


def source_links(ids, lang):
    return ' · '.join(link(SOURCES[i]['name'][lang], SOURCES[i]['url']) for i in ids)


def category_table(lang, prefix=''):
    headers = bi(['Domain', 'Question', 'Subcategories', 'Representative entry points'], ['板块', '核心问题', '细类', '代表性入口'], lang)
    rows = []
    for t in TOPICS:
        children = ' · '.join(link(c['name'][lang], prefix + t['id'] + '.md#' + c['id']) for c in t['subcategories'])
        examples = ' · '.join(link(SOURCES[key]['name'][lang], prefix + 'sources.md#source-' + key) for key in t['sources'][:3])
        rows.append([link(t['title'][lang], prefix + t['id'] + '.md'), escape(t['question'][lang]), children, examples])
    return table(headers, [230, 360, 680, 360], rows)


def make_topic(t, lang):
    filename = t['id'] + '.md'
    out = f'# {t["title"][lang]}\n\n' + nav(lang, filename) + '\n' + t['question'][lang] + '\n\n'
    out += bi('This page distinguishes subcategory questions, research priorities and industrial delivery concerns. These are editorial comparison axes; the cited examples below have narrower, explicitly described scopes.\n\n',
              '本页区分细类问题、学术研究重点和产业交付重点。这些是编辑归纳的比较维度；下方代表性入口各有明确的能力与证据范围。\n\n', lang)
    out += '## ' + bi('Subcategories and problems', '细类与问题', lang) + '\n\n'
    rows = []
    for c in t['subcategories']:
        rows.append([f'<a id="{c["id"]}"></a>' + escape(c['name'][lang]), *[escape(c[k][lang]) for k in ('problem', 'research', 'industry', 'compare')]])
    out += table(bi(['Subcategory', 'Problem', 'Research focus', 'Industrial focus', 'Comparison criteria'],
                    ['细类', '解决的问题', '学界研究重点', '产业交付重点', '比较指标与接口'], lang), [240, 300, 320, 320, 340], rows)
    out += '\n## ' + bi('Research, platforms and industrial examples', '研究、平台与产业代表', lang) + '\n\n'
    rows = []
    for key in t['sources']:
        s = SOURCES[key]
        rows.append([link(s['name'][lang], s['url']), escape(s['role'][lang]), escape(s['scope'][lang]), bi('; ', '；', lang).join(escape(EVIDENCE[e][lang]) for e in s['evidence'])])
    out += table(bi(['Participant / project', 'Role', 'Documented contribution', 'Evidence status'], ['参与者或项目', '角色', '有来源的能力', '证据状态'], lang), [280, 300, 520, 360], rows)
    out += '\n' + bi('Examples illustrate parts of this domain, not every subcategory or a market ranking. Open resources have not been run locally; product pages do not establish availability, integration compatibility or independent performance. ',
                    '示例用于说明本板块中的部分实现，并非每个细类的完整名录或市场排名。公开资源未在本地复现；产品页不证明即时供货、接口互通或独立测试性能。', lang)
    out += f'[{bi("Evidence rules and sources", "证据规则与来源", lang)}](sources.md).\n'
    out += '\n## ' + bi('Interfaces with the wider system', '与其他环节的接口', lang) + '\n\n'
    out += bi('Read the comparison criteria above as interface contracts: specify the configuration, units, timing, failure behavior and responsible layer. A suitable component does not by itself demonstrate a working integrated robot. Compare the same workload and operating envelope before transferring a result between research and deployment.\n',
              '将上表指标作为接口约定：写清配置、量纲、时序、失效行为和负责环节。部件能力不自动等于整机能力；把研究结果用于实际部署前，应对齐任务负载和适用工况。\n', lang)
    out += '\n## ' + bi('Related research catalog', '关联论文方向', lang) + '\n\n'
    for p in t['papers']:
        out += f'- [{PAPER_NAMES[p][lang]}](../{p})\n'
    out += '\n' + bi('Source check: ', '来源核对日期：', lang) + INDEX['checked_on'] + '\n'
    return out


def wrapped(text, max_units):
    def units(s): return sum(2 if unicodedata.east_asian_width(c) in 'WF' else 1 for c in s)
    tokens = list(text) if re.search('[\u4e00-\u9fff]', text) else text.split(' ')
    sep = '' if re.search('[\u4e00-\u9fff]', text) else ' '
    lines, line = [], ''
    for token in tokens:
        candidate = line + (sep if line else '') + token
        if units(candidate) > max_units and line:
            lines.append(line); line = token
        else: line = candidate
    if line: lines.append(line)
    return lines


def figure(lang):
    w, h = 1600, 1050
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img">',
           '<title>' + bi('Embodied AI research and industry landscape', '具身智能学术与产业全景', lang) + '</title>',
           '<rect width="1600" height="1050" fill="#f8fafc"/>',
           '<style>text{font-family:"Arial","PingFang SC","Microsoft YaHei",sans-serif}</style>']
    def text(x,y,s,size=18,color='#1e293b',weight='400'):
        out.append(f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{color}">{escape(s)}</text>')
    def rect(x,y,width,height,fill,stroke='none',r=12):
        out.append(f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="{r}" fill="{fill}" stroke="{stroke}"/>')
    text(48,62,bi('Embodied AI: research and industry', '具身智能：学术与产业全景',lang),34,weight='700')
    text(48,99,bi(f'{DOMAIN_COUNT} domains · {SUBCATEGORY_COUNT} subcategories · hardware, software and delivery', f'{DOMAIN_COUNT} 个板块 · {SUBCATEGORY_COUNT} 个细类 · 硬件、软件与交付协同',lang),20,'#475569')
    text(48,130,bi('A taxonomy of capabilities and problems; not a market-share or maturity ranking.', '围绕能力与问题组织；布局不表示市场份额或成熟度排名。',lang),17,'#64748b')
    groups=[(TOPICS[:5],bi('Physical platforms','物理平台',lang),'#2563eb'),(TOPICS[5:9],bi('Software capabilities','软件能力',lang),'#0f766e'),(TOPICS[9:12],bi('Development & operations','研发与运营',lang),'#7c3aed'),(TOPICS[12:],bi('Manufacturing & applications','制造交付与应用',lang),'#c2410c')]
    for gi,(topics,title,color) in enumerate(groups):
        x=48+gi*380
        rect(x,168,360,570,'#ffffff','#dbe3ed')
        rect(x,168,360,7,color,r=3)
        text(x+18,205,title,20,color,'700')
        for ti,t in enumerate(topics):
            y=226+ti*98
            rect(x+14,y,332,86,'#f8fafc','#e2e8f0',8)
            text(x+26,y+25,t['id'][:2],13,color,'700')
            lines=wrapped(t['title'][lang],35)
            for li,line in enumerate(lines[:3]):text(x+26,y+47+li*17,line,16)
    rect(48,768,1500,104,'#eff6ff','#bfdbfe')
    text(70,800,bi('Research → methods, open artifacts and controlled evaluation', '学术研究 → 方法创新、开放成果与受控评测',lang),21,'#1d4ed8','700')
    text(70,838,bi('Industry → components, platforms, integration and operational evidence', '产业实践 → 部件产品、开发平台、系统集成与运行证据',lang),21,'#0f766e','700')
    rect(48,894,1500,78,'#ffffff','#cbd5e1')
    text(70,923,bi('Field problems and failure data feed back into models, hardware and evaluation.', '场景需求与失败数据反向推动模型、本体和评测改进。',lang),19)
    text(70,950,bi('Participants may span several layers. An example is not a claim of supply-chain compatibility.', '同一参与者可以跨多个环节；共同出现不代表供应关系或已验证兼容。',lang),17,'#64748b')
    text(48,1012,bi('Framework and selected source review: ','分类框架与选定来源核对：',lang)+INDEX['checked_on'],15,'#64748b')
    out.append('</svg>')
    return '\n'.join(out)+'\n'


def make_index(lang):
    out='# '+bi('Research and industry landscape','学术与产业全景',lang)+'\n\n'+nav(lang,'README.md')+'\n'
    out+=bi(f'Start with how embodied systems are built and used, then explore research methods, software and industrial implementations. This editorial framework contains **{DOMAIN_COUNT} domains and {SUBCATEGORY_COUNT} subcategories**. Robotics infrastructure and established automation are included where they support embodied systems; inclusion does not imply use of a foundation model.\n\n',
            f'先理解具身系统如何组成和使用，再进入研究方法、软件与产业实现。本版编辑框架包含 **{DOMAIN_COUNT} 个板块、{SUBCATEGORY_COUNT} 个细类**。与具身系统相关的机器人基础设施和既有自动化也纳入视野；纳入某类不代表其使用基础模型。\n\n',lang)
    asset='research-industry-landscape'+('.zh-CN' if lang=='zh-CN' else '')+'.svg'
    out+=f'![{bi("Research and industry map", "学术与产业全景图", lang)}](../../../figs/{asset})\n\n'
    out+=f'[{bi("Open full-size diagram", "查看全景大图", lang)}](../../../figs/{asset})\n\n'
    out+='## '+bi('Three connected views','三个相互关联的视角',lang)+'\n\n'
    out+=bi('1. **Technical structure:** bodies, components, perception, control, models, data, tools and operations.\n2. **Participants and deliverables:** academic teams, industrial research, open-source communities, component vendors, integrators and operators may occupy multiple domains.\n3. **Evidence and open gaps:** separate demonstrated methods, public resources, documented products and disclosed field cases; inspect what remains unresolved.\n\n',
            '1. **技术结构：** 本体、部件、感知、控制、模型、数据、工具与运营共同构成系统。\n2. **参与者与交付物：** 高校团队、企业研究、开源社区、部件商、集成商和运营方可以跨多个板块。\n3. **证据与瓶颈：** 区分方法演示、公开资源、产品资料和现场案例，进一步查看仍未解决的问题。\n\n',lang)
    out+='## '+bi('Domains and subcategories','板块与细类',lang)+'\n\n'+category_table(lang)
    out+='\n## '+bi('Connections across the system','跨环节联系',lang)+'\n\n'
    chains=[('Contact-rich manipulation','接触丰富操作',['03-end-effectors','04-sensing','07-control','10-data','12-operations']),('Long-horizon mobile work','长时程移动作业',['01-bodies','06-perception','08-models','09-systems','12-operations']),('Train-to-deploy loop','训练到部署闭环',['10-data','11-simulation','08-models','05-compute','12-operations']),('Prototype-to-delivery loop','样机到交付闭环',['01-bodies','02-actuation','13-manufacturing','14-applications','12-operations'])]
    rows=[]
    by_id={t['id']:t for t in TOPICS}
    for en,zh,ids in chains:rows.append([escape(bi(en,zh,lang)), ' → '.join(link(by_id[i]['title'][lang],i+'.md') for i in ids)])
    out+=table(bi(['System question','Connected domains'],['系统问题','关联环节'],lang),[300,1100],rows)
    out+='\n'+bi('Follow [progress and bottlenecks](progress.md), [evidence rules and sources](sources.md), or return to the [research-method map](../overview.md).\n',
                  '继续阅读[关键进展与共性瓶颈](progress.md)、[证据规则与来源](sources.md)，或进入[研究方法地图](../overview.md)。\n',lang)
    return out


def make_sources(lang):
    out='# '+bi('Landscape evidence and sources','全景证据与来源',lang)+'\n\n'+nav(lang,'sources.md')+'\n'
    out+=bi('The taxonomy and comparison questions are editorial synthesis. Representative capabilities are supported by the primary pages below, checked on **2026-09-08**. The check date is not a product release date or a blanket refresh of the legacy paper catalog. This is a selected ecosystem view, not a census or a market-share estimate.\n\n',
            '分类和比较问题属于编辑归纳；代表性能力以以下原始来源为依据，核对日期为 **2026-09-08**。核对日期不是产品发布日期，也不代表旧论文目录全部重新核验。本版为选定样本的生态视图，不是行业普查或市场份额估计。\n\n',lang)
    out+='## '+bi('Evidence states','证据状态',lang)+'\n\n'
    state_notes={
      'R':bi('A paper or project reports experiments; retain its tasks and conditions.','论文或项目报告了实验；保留其任务与条件。',lang),
      'O':bi('Code, data or documentation are accessible; this repository has not reproduced the result.','代码、数据或文档公开；本仓库未复现实验结果。',lang),
      'P':bi('A vendor documents a product or development platform; no stock, compatibility or independent performance claim follows.','厂商公开产品或开发平台资料；不据此推定现货、兼容或独立性能。',lang),
      'F':bi('An operator describes a field case; this does not establish audited uptime or general deployment readiness.','运营方披露现场案例；不等于经审计的可用率或普遍部署成熟度。',lang)}
    out+=table(bi(['Code','State','Interpretation'],['标记','状态','解释'],lang),[90,360,760],[[k,escape(EVIDENCE[k][lang]),escape(v)] for k,v in state_notes.items()])
    out+='\n'+bi('These are evidence types, not a linear technology-readiness score. Sustained-operation claims need dated operating duration, workload, interruptions, interventions and recovery records. Manufacturer claims, research measurements and editorial inferences remain distinct.\n\n',
                  '这些是证据类型，不是线性成熟度评分。持续运营判断需要注明时段、任务量、中断、介入与恢复记录。发布方声明、研究测量和编辑推断分别保留。\n\n',lang)
    out+='## '+bi('Primary source register','原始来源登记',lang)+'\n\n'
    out+=table(bi(['Source','Role','Scope of evidence','Checked'],['来源','角色','证据范围','核对日期'],lang),[310,320,600,140],[[f'<a id="source-{s["id"]}"></a>'+link(s['name'][lang],s['url']),escape(s['role'][lang]),escape(s['scope'][lang]),s['checked_on']] for s in SOURCES.values()])
    out+='\n## '+bi('Selection and provenance','选取与来源处理',lang)+'\n\n'
    out+=bi('The local WRC 2026 classified library was used to identify component and application categories, rather than importing exhibitor profiles. The paper catalog supplies research entry points; official project, vendor and operator pages supply the selected ecosystem examples. Broad areas with few named examples remain taxonomy coverage, not claims of comprehensive supplier coverage. A named example is only attributed the contribution in its source row.\n\nROS documentation returned an access-denied page during review, so the official ROS 2 repository was used. The LEAP Hand site yielded no readable body; its paper abstract was used. Failed or empty fetches are not counted as substantive evidence.\n',
            '本地世界机器人大会 2026 分类资料库用于发现部件和应用类别，未迁入展商档案。既有论文目录提供研究入口；官方项目、厂商与运营方页面提供选定的生态示例。部分大类的具名示例仍有限，分类覆盖不等于供应商覆盖完整；对每个示例只归属来源行明确列出的能力。\n\n本轮读取 ROS 文档遇到访问限制，改用官方 ROS 2 仓库；LEAP Hand 网站未返回可读正文，采用其论文摘要。失败或空白读取不计为实质证据。\n',lang)
    return out


def make_progress(lang):
    items = json.loads((BASE / 'progress.json').read_text())
    out = '# ' + bi('Progress and shared bottlenecks', '关键进展与共性瓶颈', lang) + '\n\n' + nav(lang, 'progress.md') + '\n'
    out += bi('The observations below synthesize the listed research and industrial examples. They are not market-size estimates, universal maturity claims or a ranking of companies. Each row connects a documented capability with the evidence still needed for deployment.\n\n',
              '以下观察归纳所列研究与产业示例，不是市场规模估计、普遍成熟度结论或企业排名。每行把已有能力与走向实际部署仍需要的证据连接起来。\n\n', lang)
    rows = [[escape(item[k][lang]) for k in ('theme', 'observed', 'gap', 'next')] + [source_links(item['sources'], lang)] for item in items]
    out += table(bi(['Theme', 'What the examples establish', 'Remaining gap', 'Next evidence to retain', 'Primary examples'],
                    ['主题', '示例已能说明什么', '仍未解决的问题', '下一步应保留的证据', '原始示例来源'], lang), [240, 440, 440, 440, 400], rows)
    out += '\n## ' + bi('Read academic and industrial progress together', '结合学术与产业理解进展', lang) + '\n\n'
    out += bi('Academic comparisons emphasize controlled tasks, baselines, ablations and generalization. Industrial delivery additionally needs integration, operating duration, recovery, serviceability and cost evidence. Companies also publish research, and universities also build hardware: assign roles to the actual contribution rather than the organization name.\n\n',
              '学术比较强调受控任务、基线、消融与泛化；产业交付还需要集成、运行时长、恢复、维护和成本证据。企业也开展研究，高校也开发硬件，应按实际贡献确定角色。\n\n', lang)
    out += bi('A meaningful bridge is a reproducible task specification: robot and end effector, sensing, action interface, data version, compute budget, operating conditions and failure accounting. Keep those boundaries when linking papers with products.\n',
              '两者之间可比较的桥梁是可复现任务规格：机器人与末端、感知配置、动作接口、数据版本、计算预算、工况和失败统计。关联论文与产品时，应保留这些边界。\n', lang)
    return out


def update_root(lang):
    path = ROOT / ('README.md' if lang == 'en' else 'README.zh-CN.md')
    text = path.read_text()
    text = text.replace('# 🤖 Awesome Embodied AI Papers', '# 🤖 Embodied AI: Research & Industry')
    text = text.replace('# 🤖 具身智能论文精选', '# 🤖 具身智能：学术与产业全景')
    text = re.sub(r'\*\*(?:A curated top-conference-oriented map[^\n]*|围绕 VLN、VLA、WAM[^\n]*)\*\*',
                  '**' + bi('A map of robot hardware, software, research, industrial implementations and open problems.',
                            '从机器人硬件、软件、学术研究到产业实现，理解细分类、关键能力与未解问题。', lang) + '**', text, count=1)
    text = re.sub(r'(?:Latest recorded resource audit:|最近一次已记录资源核查：)[^\n]+',
                  bi('Landscape source review: 2026-09-08 · Legacy paper and hardware evidence dates remain on topic pages.',
                     '全景来源核对：2026-09-08 · 原有论文与硬件证据日期保留在各主题页。', lang), text, count=1)
    asset = 'research-industry-landscape' + ('.zh-CN' if lang == 'zh-CN' else '') + '.svg'
    prefix = 'docs/' + lang + '/landscape/'
    block = '<!-- landscape:start -->\n\n'
    block += '## ' + bi('Research and industry at a glance', '学术与产业全景', lang) + '\n\n'
    block += bi(f'Explore **{DOMAIN_COUNT} domains and {SUBCATEGORY_COUNT} subcategories** through their problems, research priorities, industrial roles and comparison criteria. The landscape connects to the six research tracks below.\n\n',
                f'以 **{DOMAIN_COUNT} 个板块、{SUBCATEGORY_COUNT} 个细类**梳理问题、学术重点、产业角色与比较指标，并与下方六条论文研究方向关联。\n\n', lang)
    block += f'![{bi("Research and industry landscape", "学术与产业全景图", lang)}](figs/{asset})\n\n'
    block += f'[{bi("Open full-size diagram", "查看全景大图", lang)}](figs/{asset})\n\n'
    for file, en, zh in [('README.md','Full landscape and system connections','完整全景与跨环节联系'),('progress.md','Progress and shared bottlenecks','关键进展与共性瓶颈'),('sources.md','Participants, sources and evidence states','参与者、来源与证据状态')]:
        block += f'- [{bi(en,zh,lang)}]({prefix}{file})\n'
    block += '\n## ' + bi('Domain and subcategory overview', '细分类总览', lang) + '\n\n' + category_table(lang, prefix)
    block += '\n## ' + bi('Questions connecting research and deployment', '连接研究与产业的关键问题', lang) + '\n\n'
    block += bi('- **From demonstration to generalization:** align unseen tasks, environments, robot configurations and intervention budgets.\n- **From more data to useful data:** inspect action semantics, synchronization, provenance and evaluation leakage.\n- **From components to systems:** validate timing, interfaces, fault isolation and recovery across hardware and software.\n- **From a site case to sustained service:** retain operating duration, downtime, maintenance and full task cost.\n\n',
                '- **从演示到泛化：** 对齐未见任务、环境、机器人配置和人工介入预算。\n- **从更多数据到有效数据：** 检查动作语义、时间同步、来源和评测泄漏。\n- **从部件到系统：** 联合验证软硬件时序、接口、失效隔离和恢复。\n- **从现场案例到持续服务：** 保留运行时长、停机、维护和完整任务成本。\n\n', lang)
    block += f'[{bi("See the source-backed analysis", "查看有来源的进展分析", lang)}]({prefix}progress.md)\n\n<!-- landscape:end -->'
    if '<!-- landscape:start -->' in text:
        text = re.sub(r'<!-- landscape:start -->.*?<!-- landscape:end -->', lambda _: block, text, flags=re.S)
    else:
        text = text.replace('</div>', '</div>\n\n' + block, 1)
    text = text.replace('## Contents', '## Research reading guide').replace('## 内容导航', '## 论文阅读导航')
    text = text.replace('## Direction index', '## Research paper map').replace('## 方向目录', '## 论文研究地图')
    text = text.replace('Entries are scoped to reviewed public sources,', 'Paper entries are scoped to reviewed public sources,')
    text = text.replace('> 条目范围限定为已读公开来源中可核验的论文', '> 论文条目范围限定为已读公开来源中可核验的论文')
    path.write_text(text)


def update_research_links(lang):
    for track in MANIFEST['tracks']:
        path = ROOT / 'docs' / lang / track['id'] / 'README.md'
        related = [t for t in TOPICS if any(p.startswith(track['id'] + '/') for p in t['papers'])]
        block = '<!-- landscape-links:start -->\n\n## ' + bi('Research and industrial context', '学术与产业关联', lang) + '\n\n'
        block += bi('Explore the hardware, software and delivery questions connected with this research track.\n\n',
                    '从以下板块继续查看与本研究方向相关的硬件、软件和交付问题。\n\n', lang)
        block += table(bi(['Landscape domain', 'System question'], ['全景板块', '系统问题'], lang), [300, 760],
                       [[link(t['title'][lang], '../landscape/' + t['id'] + '.md'), escape(t['question'][lang])] for t in related])
        block += '\n<!-- landscape-links:end -->'
        text = path.read_text()
        if '<!-- landscape-links:start -->' in text:
            text = re.sub(r'<!-- landscape-links:start -->.*?<!-- landscape-links:end -->', lambda _: block, text, flags=re.S)
        else:
            text = text.rstrip() + '\n\n' + block + '\n'
        path.write_text(text)


def build():
    pages=['landscape/README.md','landscape/progress.md','landscape/sources.md']+[f'landscape/{t["id"]}.md' for t in TOPICS]
    for lang in LANGS:
        folder=ROOT/'docs'/lang/'landscape';folder.mkdir(parents=True,exist_ok=True)
        (folder/'README.md').write_text(make_index(lang))
        (folder/'sources.md').write_text(make_sources(lang))
        (folder/'progress.md').write_text(make_progress(lang))
        for t in TOPICS:(folder/(t['id']+'.md')).write_text(make_topic(t,lang))
        (ROOT/'figs'/('research-industry-landscape'+('.zh-CN' if lang=='zh-CN' else '')+'.svg')).write_text(figure(lang))
        update_root(lang)
        update_research_links(lang)
    MANIFEST['pages']=list(dict.fromkeys(MANIFEST['pages']+pages))
    MANIFEST['landscape']={'domains':len(TOPICS),'subcategories':sum(len(t['subcategories']) for t in TOPICS),'sources':len(SOURCES),'topics':INDEX['topics'],'checked_on':INDEX['checked_on']}
    (ROOT/'docs/manifest.json').write_text(json.dumps(MANIFEST,ensure_ascii=False,indent=2)+'\n')
    print(f'Built {len(TOPICS)} topic pairs and landscape indexes; {sum(len(t["subcategories"]) for t in TOPICS)} subcategories.')


if __name__=='__main__':
    build()
