#!/usr/bin/env python3
"""Render product comparisons and complete technical evidence from archived inputs.

No network calls. A source item is not necessarily a commercial SKU. Manually
attributed comparison facts never inherit a supplier's full paragraph.
"""
from pathlib import Path
from html import escape
import json
import re

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'sources/products'
CATEGORIES=json.loads((BASE/'categories.json').read_text())
CATEGORY_BY_ID={c['id']:c for c in CATEGORIES}
CONTEXTS={p.stem:json.loads(p.read_text()) for p in sorted((BASE/'contexts').glob('*.json'))}
ITEMS=json.loads((BASE/'items.json').read_text())
REVIEWS=json.loads((BASE/'reviews.json').read_text())
ITEM_BY_ID={x['id']:x for x in ITEMS}
INDEX=json.loads((ROOT/'sources/landscape/index.json').read_text())
TOPICS=[json.loads((ROOT/'sources/landscape/topics'/(i+'.json')).read_text()) for i in INDEX['topics']]
TOPIC_BY_PREFIX={t['id'][:2]:t for t in TOPICS}
SUBS={s['id']:s for t in TOPICS for s in t['subcategories']}
LABELS={
 'structure':('Structure / configuration','结构与配置'), 'dof':('Degrees of freedom','自由度'),
 'mass':('Mass','重量'), 'load':('Load and conditions','负载与工况'), 'energy':('Battery / endurance','电池与续航'),
 'sensing':('Sensing','传感配置'), 'compute':('Compute / memory','算力与内存'), 'interface':('Interfaces','接口'),
 'output':('Torque / thrust','力矩与推力'), 'power':('Supply / power','供电与功率'), 'precision':('Precision / error','精度与误差'),
 'force':('Contact / fingertip force','接触与指尖力'), 'frequency':('Rate / synchronization','频率与同步'),
 'range':('Range / field of view','量程与视场'), 'function':('Function / workflow','功能与工作流程'),
 'data':('Inputs / data','输入与数据'), 'processor':('Processor / architecture','处理器与架构'),
 'protection':('Protection / environment','防护与环境'), 'performance':('Reported task measure','报告的任务指标'),
 'simulation_data':('Simulation / data support','仿真与数据支持'),
 'limits':('Limits / unresolved issues','限制与待核实项')}
SCHEMAS={
 '01':['structure','dof','mass','load','energy','sensing','interface'],
 '02':['structure','output','power','precision','interface','sensing','protection'],
 '03':['structure','dof','mass','force','load','sensing','frequency','interface','simulation_data'],
 '04':['structure','range','precision','frequency','interface','function','protection'],
 '05':['processor','compute','power','energy','interface'],
 '06':['function','sensing','interface','precision'],
 '07':['function','interface','precision','performance'],
 '08':['function','data','compute','interface'],
 '09':['function','data','interface'],
 '10':['structure','data','sensing','precision','frequency','interface','function'],
 '11':['function','data','compute','interface'],
 '12':['function','performance','interface'],
 '13':['structure','function','performance','interface'],
 '14':['function','structure','performance','protection','energy']}


def tr(pair,lang):return pair[0] if lang=='en' else pair[1]
def a(label,url):return f'<a href="{escape(url,quote=True)}">{escape(label)}</a>'
def table(head,widths,rows,nowrap_headers=False):
 out=[f'<table width="{sum(widths)}">','<thead>','<tr>']
 out += [f'<th width="{w}"' + (' nowrap' if nowrap_headers else '') + f'>{escape(h)}</th>' for h,w in zip(head,widths)]
 out += ['</tr>','</thead>','<tbody>']
 for row in rows:
  assert len(row)==len(widths)
  out+=['<tr>']+[f'<td width="{w}">{x}</td>' for w,x in zip(widths,row)]+['</tr>']
 return '\n'.join(out+['</tbody>','</table>'])+'\n'


def nav(lang,file):
 depth=len(Path(file).parts)-1;up='../'*depth;other='zh-CN' if lang=='en' else 'en'
 return f'[{tr(("Product detail index","产品细节目录"),lang)}]({up}README.md) | [{tr(("中文","英文"),lang)}]({up}../../{other}/products/{file}) | [{tr(("Landscape","全景目录"),lang)}]({up}../landscape/README.md)\n'


def related_categories(sub_ids):
 return [c for c in CATEGORIES if set(c['related_subcategories']) & set(sub_ids)]


def source_ref(c,lang,prefix=''):
 return a(c['title'][lang],prefix+'references/'+c['id']+'.md')


def make_reference(c,lang):
 out='# '+c['title'][lang]+'\n\n'+nav(lang,'references/'+c['id']+'.md')+'\n'
 out+=tr(('These are source-classified technical excerpts and exhibit links, not supplier biographies. The original category organizes provenance; it does not establish each listed product\'s form or capability. Facts reflect the **2026-09-05 archive**, not a new live verification.\n\n',
          '本页保留按来源分类的技术摘录和展项链接，不收录企业简介或展位名录。原分类用于组织来源，不证明每个展项的形态或能力。事实沿用 **2026-09-05 归档**，不代表重新联网核验。\n\n'),lang)
 out+=tr(('Supplier and source-item names are retained as published. The English technical summary translates the archived claims; original product/application wording and issue notes remain visible as source transcription.\n\n',
          '供应主体和展项名称保留原始写法；技术摘录配有英文对照。原产品线、应用措辞和问题记录作为来源转录保留，不能据关联关系推定自研或供货。\n\n'),lang)
 out+='## '+tr(('Original comparison checklist','原资料比较字段'),lang)+'\n\n'+c['comparison_focus'][lang]+'\n\n'
 rows=[]
 for sid in c['contexts']:
  ctx=CONTEXTS[sid];reviews=[r for r in REVIEWS if r['source_id']==sid]
  rows.append([a(sid+' · '+ctx['supplier_as_published'],'#'+sid.lower()),str(len(ctx['item_ids'])),str(len(reviews))])
 out+=table(tr((['Technical context','Source items','Comparison records'],['技术上下文','原始展项数','对照记录数']),lang),[460,150,170],rows)
 cross=[ctx for ctx in CONTEXTS.values() if c['id'] in ctx['cross_source_categories']]
 if cross:
  out+='\n## '+tr(('Cross-category technical contexts','跨分类技术上下文'),lang)+'\n\n'
  out+=tr(('These links reuse the primary technical record; they do not add new products or establish compatibility.\n\n',
           '这些入口复用主技术记录，不新增产品计数，也不证明接口兼容。\n\n'),lang)
  out+=table(tr((['Technical context','Primary source category'],['技术上下文','原主分类']),lang),[600,420],
             [[a(x['id']+' · '+x['supplier_as_published'],x['source_category']+'.md#'+x['id'].lower()),escape(CATEGORY_BY_ID[x['source_category']]['title'][lang])] for x in cross])
 for sid in c['contexts']:
  ctx=CONTEXTS[sid]
  out+=f'\n<a id="{sid.lower()}"></a>\n\n## {sid} · {escape(ctx["supplier_as_published"])}\n\n'
  out+=ctx['technical'][lang]+'\n\n'+a(tr(('Original evidence','原始依据'),lang),ctx['source_url'])+'\n\n'
  evidence=tr(('Official search or alternate-source excerpt','官方搜索或替代来源摘录'),lang) if ctx['evidence']=='official_search_or_alternate' else tr(('Archived official-page excerpt','归档官方页面摘录'),lang)
  out+=tr(('Source review date: ','原来源核查日期：'),lang)+ctx['source_checked_on']+' · '+evidence+'\n\n'
  out+=tr(('**Attribution boundary:** the paragraph can discuss several models, series limits or unresolved names. Only the comparison records below carry manually attributed model-level fields.\n\n',
           '**归属边界：** 以上段落可能涉及多个型号、系列极值或待确认命名。只有下方型号对照记录中的字段经过逐项归属，不能把整段参数套用到每个展项。\n\n'),lang)
  own=[r for r in REVIEWS if r['source_id']==sid]
  if own:
   out+='### '+tr(('Model / family comparison records','型号与产品族对照'),lang)+'\n\n'
   for r in own:
    tid=TOPIC_BY_PREFIX[r['related_subcategories'][0][:2]]['id']
    out+='- '+a(r['model_as_reported'],'../comparisons/'+tid+'.md#'+r['id'])+'\n'
   out+='\n'
  out+='<details>\n<summary>'+tr(('Original source wording and extra links','原始措辞与补充链接'),lang)+'</summary>\n\n'
  rows=[[tr(('Original product-line wording','原表产品线'),lang),escape(ctx['original_product_line'])],
        [tr(('Original application wording','原表应用措辞'),lang),escape(ctx['original_application_wording'])],
        [tr(('Original tags','原表细分标签'),lang),escape(ctx['original_tags'])],
        [tr(('Historical verification wording; not upgraded','历史核验措辞；未升级状态'),lang),escape(ctx['original_verification_wording'])],
        [tr(('Archived review wording','原归档核查措辞'),lang),escape(ctx['original_review_wording'])]]
  if ctx['cross_source_categories']:
   rows.append([tr(('Original cross-category links','原交叉分类入口'),lang),'<br>'.join(a(CATEGORY_BY_ID[k]['title'][lang],k+'.md') for k in ctx['cross_source_categories'])])
  if ctx['original_issue_notes']:rows.append([tr(('Original issue notes','原始问题记录'),lang),'<br>'.join(escape(x) for x in ctx['original_issue_notes'])])
  rows.append([tr(('Source links in the original record','原记录来源链接'),lang),'<br>'.join(a(tr(('Source','来源'),lang)+' '+str(i+1),url) for i,url in enumerate(ctx['original_source_urls']))])
  out+=table(tr((['Field','Source transcription'],['字段','来源转录']),lang),[240,900],rows)+'\n</details>\n\n'
  out+='### '+tr(('Source-listed products / exhibits','来源列出的产品与展项'),lang)+'\n\n'
  if ctx['item_ids']:
   rows=[]
   for iid in ctx['item_ids']:
    item=ITEM_BY_ID[iid];rows.append([f'<a id="{iid}"></a>'+escape(item['display_name']),a(tr(('Original exhibit page','原始展项页'),lang),item['url'])])
   out+=table(tr((['Name as published','Source'],['原始名称','来源']),lang),[640,280],rows)
  else:out+=tr(('No structured exhibit-name list was supplied. The technical context above remains retained; no model was invented from it.\n',
                '原资料未提供结构化展项名称列表。仍保留上述技术上下文，不据此编造型号。\n'),lang)
 return out


def relation(r,lang):
 rel=r['research_relation']
 if rel['kind']=='documented_use':
  return a(rel['paper_title'],rel['paper_url'])+'<br>'+escape(rel['note'][lang])+'<br>'+a(tr(('Paper PDF page 4','论文PDF第4页'),lang),rel['primary_pdf']+'#page='+str(rel['primary_page']))+'<br>'+a(tr(('Catalog evidence','论文目录证据'),lang),'../../'+rel['catalog_path'])
 topic=TOPIC_BY_PREFIX[r['related_subcategories'][0][:2]]
 refs='<br>'.join(a(tr(('Research catalog','论文目录'),lang)+' '+str(i+1),'../../'+p) for i,p in enumerate(topic['papers']))
 return tr(('Related route; model use unconfirmed.','相关路线；未确认型号使用。'),lang)+'<br>'+refs


def comparison_row(r,keys,lang,first_occurrence):
 ctx=CONTEXTS[r['source_id']];facts=r['facts'];missing=tr(('Not disclosed','未披露'),lang)
 model=(f'<a id="{r["id"]}"></a>' if first_occurrence else '')+escape(r['model_as_reported'])
 values=[escape(facts[k][lang]) if k in facts else missing for k in keys]
 extra=[escape(tr(LABELS[k],lang))+': '+escape(v[lang]) for k,v in facts.items() if k not in keys and k!='limits']
 limits=escape(facts['limits'][lang]) if 'limits' in facts else tr(('See source conditions; unreported fields remain unknown.','参见来源条件；未报告字段仍为未知。'),lang)
 grade=tr(('Search or alternate-source excerpt','搜索或替代来源摘录'),lang) if ctx['evidence']=='official_search_or_alternate' else tr(('Archived official-page excerpt','归档官方页面摘录'),lang)
 refs=a(tr(('Technical context','完整技术上下文'),lang),'../references/'+ctx['source_category']+'.md#'+ctx['id'].lower())+'<br>'+a(tr(('Original evidence','原始依据'),lang),ctx['source_url'])+'<br>'+ctx['source_checked_on']+'<br>'+grade
 for iid in r.get('source_item_ids',[]):
  refs+='<br>'+a(tr(('Model exhibit source','型号展项来源'),lang),ITEM_BY_ID[iid]['url'])
 return [model,escape(ctx['supplier_as_published']),*values,'<br>'.join(extra) or '—',limits,relation(r,lang),refs]


def make_comparison(t,lang):
 out='# '+t['title'][lang]+' — '+tr(('technical and product comparisons','技术与产品对照'),lang)+'\n\n'+nav(lang,'comparisons/'+t['id']+'.md')+'\n'
 out+=tr(('Fields vary by technical domain. **Not disclosed** means absent from the archived text for this model, not unsupported by the product. Supplier names remain as published. Series maxima, passive/static loads, rates, and certification claims retain their conditions.\n\n',
          '按技术领域设置专用字段。**未披露**表示归档文本未给出该型号此项，不代表产品不支持。供应主体保留原始名称；系列极值、被动/静态载荷、频率和认证声明均保留条件。\n\n'),lang)
 out+=tr(('These are product/model/family comparison records, not verified procurement specifications. The same record may appear under several related subcategories; it is maintained once in source data. A shared technology route does not establish use in a paper.\n\n',
          '本页是产品、型号及产品族对照，不是已核实的采购规格。同一记录可在多个相关细类引用，源数据只维护一份。技术路线相关不等于论文使用该型号。\n\n'),lang)
 out+=tr(('Columns with no disclosed values in a comparison group are omitted; consult the complete source-category checklist for the remaining gaps.\n\n',
          '同组所有条目均未披露的列不展开，完整待补字段仍保留在来源分类页的比较字段中。\n\n'),lang)
 subids=[s['id'] for s in t['subcategories']];schema=SCHEMAS[t['id'][:2]];seen=set()
 for s in t['subcategories']:
  out+=f'\n<a id="sub-{s["id"]}"></a>\n\n## {s["name"][lang]}\n\n'
  out+=a(tr(('Open dedicated topic page','打开独立专题页'),lang),'../topics/'+s['id']+'.md')+'\n\n'
  rs=[r for r in REVIEWS if s['id'] in r['related_subcategories']]
  if rs:
   keys=[key for key in schema if any(key in r['facts'] for r in rs)]
   rows=[]
   for r in rs:
    rows.append(comparison_row(r,keys,lang,r['id'] not in seen));seen.add(r['id'])
   headers=[tr(('Model / family','型号与产品族'),lang),tr(('Supplier as published','来源主体'),lang)]+[tr(LABELS[k],lang) for k in keys]+[tr(('Other reported details','其他已报告细节'),lang),tr(LABELS['limits'],lang),tr(('Research relationship','研究关联'),lang),tr(('Evidence / date','依据与日期'),lang)]
   out+=table(headers,[240,280]+[240]*len(keys)+[320,360,380,260],rows,nowrap_headers=True)
  else:out+=tr(('No model-attributed comparison has been entered for this subcategory. Preserve the source context instead of spreading a mixed paragraph across products.\n',
               '此细类尚无可逐型号归属的对照条目，保留来源上下文，不把混合段落分摊给各产品。\n'),lang)
  cs=related_categories([s['id']])
  if cs:
   out+='\n'+tr(('Complete archived technical material: ','完整归档技术资料：'),lang)+' · '.join(source_ref(c,lang,'../') for c in cs)+'\n'
 out+='\n## '+tr(('Related research','关联研究'),lang)+'\n\n'
 out+=a(tr(('Return to the research and industry topic','返回学术与产业主题页'),lang),'../../landscape/'+t['id']+'.md')+'\n'
 return out


def make_subtopic(t,s,lang):
 out='# '+s['name'][lang]+'\n\n'+nav(lang,'topics/'+s['id']+'.md')+'\n'
 out+=a(t['title'][lang],'../comparisons/'+t['id']+'.md#sub-'+s['id'])+'\n\n'
 out+='## '+tr(('Problem and comparison criteria','问题与比较重点'),lang)+'\n\n'
 out+=table(tr((['Dimension','Focus'],['维度','重点']),lang),[220,900],
            [[tr((en,zh),lang),escape(s[k][lang])] for k,en,zh in [('problem','Problem','解决的问题'),('research','Academic research','学术研究'),('industry','Industrial delivery','产业交付'),('compare','Comparison criteria','比较指标')]])
 # Reuse the canonical comparison section without changing its relative-link depth.
 block=make_comparison(t,lang)
 marker=f'<a id="sub-{s["id"]}"></a>'
 section=block.split(marker,1)[1]
 section=re.split(r'\n<a id="sub-|\n## '+re.escape(tr(('Related research','关联研究'),lang)),section,1)[0]
 section=section.split('\n\n',2)[-1]
 section=re.sub(r'<a href="\.\./topics/[^\"]+">.*?</a>\n\n','',section,count=1)
 out+='\n## '+tr(('Model and technical comparisons','型号与技术对照'),lang)+'\n\n'+section.strip()+'\n'
 out+='\n## '+tr(('Sources and remaining gaps','来源与待补内容'),lang)+'\n\n'
 out+=tr(('The entries use archived evidence dated 2026-09-05. Missing fields remain unknown. Source-category links provide context and do not imply that every product in a source category belongs to this subcategory.\n\n',
          '条目沿用 2026-09-05 归档证据，缺失字段仍为未知。来源分类链接提供上下文，不表示其中每个产品都属于本细类。\n\n'),lang)
 out+=tr(('For the next update, record the exact model/configuration, the criteria above, operating conditions, interfaces, source date and unresolved contradictions. A new page does not count as a newly verified product.\n',
          '后续按具体型号与配置补充上述比较指标、工况、接口、来源日期和未解冲突。新增页面不计为新增已核验产品。\n'),lang)
 out+='\n## '+tr(('Related research','关联研究'),lang)+'\n\n'
 out+='\n'.join('- '+a(tr(('Research catalog','论文目录'),lang)+' '+str(i+1),'../../'+p) for i,p in enumerate(t['papers']))+'\n'
 return out


def make_index(lang):
 out='# '+tr(('Technical and product detail library','技术与产品细节库'),lang)+'\n\n'+nav(lang,'README.md')+'\n'
 out+=tr((f'This layer contains **{len(REVIEWS)} model/family comparison records**, **{len(CONTEXTS)} complete technical contexts**, and **{len(ITEMS)} source-item associations** across {len(CATEGORIES)} source categories. It restores product detail beneath the landscape, without importing booth directories or company biographies.\n\n',
          f'本层包含 **{len(REVIEWS)} 条型号/产品族对照记录**、**{len(CONTEXTS)} 段完整技术上下文**、**{len(ITEMS)} 条原始展项关联**，覆盖 {len(CATEGORIES)} 个来源分类。在全景之下恢复产品细节，不迁入展位名录和企业简介。\n\n'),lang)
 out+=tr(('The archive was reviewed on **2026-09-05** and reorganized here on **2026-09-08**. Exhibit associations are not deduplicated commercial models: they can include series, services, concepts, joint exhibits or conflicting names. Untyped items retain their source links without inheriting model-specific parameters.\n\n',
          '原资料核查日期为 **2026-09-05**，本次重组日期为 **2026-09-08**。展项关联不是去重后的商品型号，可能含系列、服务、概念、联合展项或冲突命名。尚未逐型号拆清的展项保留链接，不继承其他型号的参数。\n\n'),lang)
 out+=a(tr(('Search all source-listed products and exhibits','检索全部原始产品与展项'),lang),'catalog.md')+'\n\n'
 cross_count=sum(len(c['cross_source_categories']) for c in CONTEXTS.values())
 out+=tr((f'The {cross_count} original cross-category entry points are retained, reusing the same technical records.\n\n',
          f'同时保留原有 {cross_count} 个跨分类入口，复用同一份技术记录。\n\n'),lang)
 out+='## '+tr(('Comparison entry points','对照入口'),lang)+'\n\n'
 rows=[]
 for t in TOPICS:
  ids={s['id'] for s in t['subcategories']};n=sum(bool(ids&set(r['related_subcategories'])) for r in REVIEWS)
  rows.append([a(t['title'][lang],'comparisons/'+t['id']+'.md'),str(n),escape(' / '.join(tr(LABELS[k],lang) for k in SCHEMAS[t['id'][:2]]))])
 out+=table(tr((['Domain','Related records','Domain-specific fields'],['板块','相关记录数','专用比较字段']),lang),[300,140,1040],rows)
 out+='\n## '+tr(('Dedicated subcategory pages','细类独立专题页'),lang)+'\n\n'
 rows=[]
 for t in TOPICS:
  for s in t['subcategories']:
   count=sum(s['id'] in r['related_subcategories'] for r in REVIEWS)
   rows.append([a(s['name'][lang],'topics/'+s['id']+'.md'),escape(t['title'][lang]),str(count),escape(s['problem'][lang])])
 out+=table(tr((['Subcategory','Domain','Comparison records','Problem'],['细类','所属板块','对照记录数','解决的问题']),lang),[360,300,150,600],rows)
 out+='\n## '+tr(('Complete source-category archive','完整来源分类资料'),lang)+'\n\n'
 rows=[]
 for c in CATEGORIES:
  n=sum(len(CONTEXTS[i]['item_ids']) for i in c['contexts'])
  rows.append([source_ref(c,lang),str(len(c['contexts'])),str(n)])
 out+=table(tr((['Source category','Technical contexts','Exhibit associations'],['来源分类','技术上下文数','展项关联数']),lang),[540,160,180],rows)
 out+='\n## '+tr(('Attribution and maintenance','归属与维护'),lang)+'\n\n'
 out+=tr(('Model fields were manually attributed from archived excerpts. Shared paragraphs remain intact, including exact-model conflicts, unverified claims and missing conditions. The HumanPlus link explicitly names RH56DFX in the existing paper catalog; other research links are labeled related routes unless separate evidence is recorded.\n\nThe original Magic MA1 name contained a vertical-tab character. Its full name was recovered; raw spelling is retained and display whitespace normalized. No source item was discarded because of that control character. Archive hashes and recovery notes are stored in the provenance file.\n',
          '型号字段按归档提要逐项归属；混合段落完整保留，包括型号冲突、未核实声明和缺失工况。HumanPlus 关联依据既有论文目录中明确出现的 RH56DFX；其他研究关联在没有单独证据时标为相关路线。\n\n原展项索引的 Magic MA1 名称含垂直制表控制字符，本次恢复完整名称，保留原始写法并规范显示空白，未因控制字符丢弃展项。原文件哈希与恢复说明存入来源记录。\n'),lang)
 return out


def make_catalog(lang):
 out='# '+tr(('Source product and exhibit index','原始产品与展项索引'),lang)+'\n\n'+nav(lang,'catalog.md')+'\n'
 out+=tr((f'All {len(ITEMS)} source associations are retained. Use browser search for a model name, then open its technical context. Names are transcribed as published; an exhibit can be a series, service or concept rather than a unique commercial SKU.\n\n',
          f'保留全部 {len(ITEMS)} 条来源关联，可通过浏览器查找型号名称，再进入完整技术上下文。名称按来源转录；展项可能是系列、服务或概念，不等同唯一商品型号。\n\n'),lang)
 rows=[]
 for item in ITEMS:
  ctx=CONTEXTS[item['source_id']];base='references/'+ctx['source_category']+'.md'
  rows.append([a(item['display_name'],base+'#'+item['id']),a(ctx['id']+' · '+ctx['supplier_as_published'],base+'#'+ctx['id'].lower()),a(tr(('Original source','原始来源'),lang),item['url'])])
 out+=table(tr((['Name as published','Technical context / source entity','Source'],['来源名称','技术上下文与来源主体','来源']),lang),[520,500,180],rows)
 out+='\n## '+tr(('Contexts without structured exhibit names','未列结构化展项名称的技术资料'),lang)+'\n\n'
 out+=tr(('These are source contexts, not additional product counts. Original product-line wording remains searchable without inventing separate model records.\n\n',
          '以下计为来源技术上下文，不新增产品计数。保留原产品线措辞以便检索，不擅自拆成独立型号。\n\n'),lang)
 rows=[]
 for ctx in CONTEXTS.values():
  if ctx['item_ids']:continue
  rows.append([a(ctx['id']+' · '+ctx['supplier_as_published'],'references/'+ctx['source_category']+'.md#'+ctx['id'].lower()),escape(ctx['original_product_line']),a(tr(('Original source','原始来源'),lang),ctx['source_url'])])
 out+=table(tr((['Technical context','Original product-line wording','Source'],['技术上下文','原产品线措辞','来源']),lang),[420,700,160],rows)
 return out


def landscape_section(t,lang):
 ids=[s['id'] for s in t['subcategories']];rs=[r for r in REVIEWS if set(ids)&set(r['related_subcategories'])]
 out='\n## '+tr(('Technical and product details','技术与产品细节'),lang)+'\n\n'
 out+=a(tr((f'Open {len(rs)} related comparison records',f'查看 {len(rs)} 条相关对照记录'),lang),'../products/comparisons/'+t['id']+'.md')+'\n\n'
 out+=tr(('Compare model-specific values, conditions, interfaces, research relationships and source issues. Full source excerpts and original exhibit links remain available underneath.\n\n',
          '继续比较逐型号参数、工况、接口、研究关联和来源问题，并下钻查看完整技术摘录与原始展项链接。\n\n'),lang)
 cs=related_categories(ids)
 if cs:out+=' · '.join(a(c['title'][lang],'../products/references/'+c['id']+'.md') for c in cs)+'\n'
 return out


def build():
 manifest=json.loads((ROOT/'docs/manifest.json').read_text())
 paths=['products/README.md','products/catalog.md']+[f'products/references/{c["id"]}.md' for c in CATEGORIES]+[f'products/comparisons/{t["id"]}.md' for t in TOPICS]
 paths += [f'products/topics/{s["id"]}.md' for t in TOPICS for s in t['subcategories']]
 for lang in ['en','zh-CN']:
  folder=ROOT/'docs'/lang/'products';(folder/'references').mkdir(parents=True,exist_ok=True);(folder/'comparisons').mkdir(exist_ok=True)
  (folder/'topics').mkdir(exist_ok=True)
  (folder/'README.md').write_text(make_index(lang))
  (folder/'catalog.md').write_text(make_catalog(lang))
  for c in CATEGORIES:(folder/'references'/(c['id']+'.md')).write_text(make_reference(c,lang))
  for t in TOPICS:(folder/'comparisons'/(t['id']+'.md')).write_text(make_comparison(t,lang))
  for t in TOPICS:
   for s in t['subcategories']:(folder/'topics'/(s['id']+'.md')).write_text(make_subtopic(t,s,lang))
 manifest['pages']=list(dict.fromkeys(manifest['pages']+paths))
 manifest['products']={'contexts':len(CONTEXTS),'source_items':len(ITEMS),'comparisons':len(REVIEWS),'source_categories':len(CATEGORIES),'cross_references':sum(len(c['cross_source_categories']) for c in CONTEXTS.values()),'source_snapshot':'2026-09-05','import_date':'2026-09-08'}
 manifest['products']['dedicated_topics']=sum(len(t['subcategories']) for t in TOPICS)
 (ROOT/'docs/manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
 print(f'Built {len(paths)} product-detail page pairs; {len(REVIEWS)} comparisons, {len(CONTEXTS)} contexts, {len(ITEMS)} source items.')

if __name__=='__main__':build()
