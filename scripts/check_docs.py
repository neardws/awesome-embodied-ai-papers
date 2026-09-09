#!/usr/bin/env python3
"""Validate bilingual document structure, paper identities, counts and local links.

No dependencies. This checks structural parity, not translation semantics or
whether remote URLs are reachable. Archived source snapshots are not edited.
"""
from pathlib import Path
from html import unescape
import json
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
ERRORS = []


def require(condition, message):
    if not condition:
        ERRORS.append(message)


def plain(value):
    return unescape(re.sub(r'<[^>]+>', '', value)).strip()


def tables(text):
    result = []
    for table in re.findall(r'<table\b[^>]*>.*?</table>', text, re.S):
        headers = re.findall(r'<th\b[^>]*>(.*?)</th>', table, re.S)
        rows = [re.findall(r'<td\b[^>]*>(.*?)</td>', row, re.S)
                for row in re.findall(r'<tr\b[^>]*>(.*?)</tr>', table, re.S)]
        result.append((list(map(plain, headers)), [r for r in rows if r]))
    return result


def urls(value):
    # The sole intentional external language variant in the source catalog.
    return [unescape(u).replace('open.agibot.com/docs/en/', 'open.agibot.com/docs/')
            for u in re.findall(r'(?:href|src)="(https?://[^"]+)"', value)]


def external_links(text):
    """Compare targets as well as HTML links; badge display labels may differ."""
    return [unescape(url).replace('open.agibot.com/docs/en/', 'open.agibot.com/docs/')
            for url in re.findall(r'https?://[^\s\"<>\)]+', text)
            if not url.startswith('https://img.shields.io/')]


def check_chinese_prose(path, text):
    # Official linked titles, repository paths, code and method names stay intact.
    text = re.sub(r'```.*?```|`[^`]+`|<a\b[^>]*>.*?</a>', '', text, flags=re.S)
    text = re.sub(r'https?://[^\s\"<>\)]+|<[^>]+>|\]\([^)]*\)', '', text)
    text = text.replace('Streaming Flow Policy', '').replace('Diffusion Policy', '')
    leftovers = re.findall(
        r'(?<![A-Za-z0-9_-])(?:benchmark|dataset|rollouts?|DoF|Sim Only|'
        r'sim2real|action tokens?|tokenization|actor-critic|policy)(?![A-Za-z0-9_-])',
        text)
    require(not leftovers, f'{path.relative_to(ROOT)}: untranslated prose terms: {sorted(set(leftovers))}')


def paper_rows(text):
    # Audits and hardware tables coexist with paper tables in embodiment pages.
    return [row for headers, rows in tables(text)
            if headers and headers[0] in ('Venue/Year', '会议/年份', 'Venue', '会议')
            for row in rows]


def anchors(text):
    found = set(re.findall(r'(?:id|name)="([^"]+)"', text))
    used = {}
    for title in re.findall(r'^#{1,6} (.+)$', text, re.M):
        slug = re.sub(r'[^\w\- ]', '', plain(title).lower()).replace(' ', '-')
        n = used.get(slug, 0)
        used[slug] = n + 1
        found.add(slug + (f'-{n}' if n else ''))
    return found


def check_links(path, text):
    refs = re.findall(r'(?:href|src)="([^"]+)"', text)
    refs += re.findall(r'\]\(([^\s)]+)\)', text)
    for ref in refs:
        ref = unescape(ref)
        parsed = urlsplit(ref)
        if parsed.scheme or parsed.netloc:
            continue
        target = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
        require(target.exists(), f'{path.relative_to(ROOT)}: missing target {ref}')
        if target.is_file() and target.suffix == '.md' and parsed.fragment:
            require(unquote(parsed.fragment) in anchors(target.read_text()),
                    f'{path.relative_to(ROOT)}: missing anchor {ref}')


def check_table_layout(path, text):
    layouts = []
    require(not re.search(r'^\|.*\n\|[ :|\-]+\|', text, re.M),
            f'{path.relative_to(ROOT)}: use width-defined HTML tables, not pipe tables')
    for ti, table in enumerate(re.findall(r'<table\b[^>]*>.*?</table>', text, re.S)):
        widths = []
        header = re.search(r'<thead>(.*?)</thead>', table, re.S)
        if header is None:
            require(False, f'{path.relative_to(ROOT)} table {ti}: missing header')
            continue
        for attrs in re.findall(r'<th\b([^>]*)>', header[1]):
            width = re.search(r'\bwidth="([1-9]\d*)"', attrs)
            require(width is not None, f'{path.relative_to(ROOT)} table {ti}: missing column width')
            widths.append((int(width[1]) if width else 0, bool(re.search(r'\bnowrap\b', attrs))))
        table_width = re.match(r'<table\b[^>]*\bwidth="(\d+)"', table)
        require(table_width is not None and int(table_width[1]) == sum(w for w, _ in widths),
                f'{path.relative_to(ROOT)} table {ti}: total width must equal column sum')
        body_wrapping = None
        for ri, row in enumerate(re.findall(r'<tr\b[^>]*>(.*?)</tr>', table, re.S)):
            cells = re.findall(r'<t[hd]\b([^>]*)>', row)
            require(len(cells) == len(widths), f'{path.relative_to(ROOT)} table {ti} row {ri}: column count differs')
            if ri == 1:
                body_wrapping = [bool(re.search(r'\bnowrap\b', a)) for a in cells]
            for ci, (attrs, expected) in enumerate(zip(cells, widths)):
                width = re.search(r'\bwidth="(\d+)"', attrs)
                actual = (int(width[1]) if width else 0, bool(re.search(r'\bnowrap\b', attrs)))
                nowrap = expected[1] if ri == 0 else body_wrapping[ci]
                require(actual == (expected[0], nowrap), f'{path.relative_to(ROOT)} table {ti} row {ri} col {ci}: width/wrapping differs')
        layouts.append((widths, body_wrapping))
    return layouts


def check_landscape(manifest):
    """Check source completeness and exact bilingual generated-page parity."""
    if 'landscape' not in manifest:
        return
    import build_landscape as landscape
    config = manifest['landscape']
    topics = landscape.TOPICS
    sources = landscape.SOURCES
    require(len(topics) == config['domains'], 'Landscape domain count differs')
    children = [c for t in topics for c in t['subcategories']]
    require(len(children) == config['subcategories'], 'Landscape subcategory count differs')
    require(len({c['id'] for c in children}) == len(children), 'Duplicate landscape subcategory IDs')
    require(len(sources) == config['sources'], 'Landscape source count differs')
    require([t['id'] for t in topics] == config['topics'], 'Landscape topic order differs')
    source_rows = json.loads((ROOT / 'sources/landscape/sources.json').read_text())
    require(len(source_rows) == len(sources), 'Duplicate landscape source IDs')
    used = set()
    for t in topics:
        for key in t['sources']:
            require(key in sources, f'{t["id"]}: unknown source {key}')
            used.add(key)
        for row in t['subcategories']:
            for field in ('name', 'problem', 'research', 'industry', 'compare'):
                require(set(row[field]) == {'en', 'zh-CN'} and all(row[field].values()),
                        f'{row["id"]}: missing bilingual {field}')
        for lang in ('en', 'zh-CN'):
            path = ROOT / 'docs' / lang / 'landscape' / (t['id'] + '.md')
            require(path.read_text() == landscape.make_topic(t, lang), f'{path.relative_to(ROOT)}: regenerate from topic source')
    require(used == set(sources), 'Landscape contains unreferenced source records')
    for s in sources.values():
        require(s['checked_on'] == config['checked_on'], f'{s["id"]}: source review date differs')
        require(set(s['evidence']) <= set(landscape.EVIDENCE) and bool(s['evidence']), f'{s["id"]}: invalid evidence state')
        require(s['url'].startswith('https://'), f'{s["id"]}: expected HTTPS source')
    for lang in ('en', 'zh-CN'):
        for file, render in [('README.md', landscape.make_index), ('progress.md', landscape.make_progress), ('sources.md', landscape.make_sources)]:
            path = ROOT / 'docs' / lang / 'landscape' / file
            require(path.read_text() == render(lang), f'{path.relative_to(ROOT)}: generated content differs')
        asset = ROOT / 'figs' / ('research-industry-landscape' + ('.zh-CN' if lang == 'zh-CN' else '') + '.svg')
        require(asset.read_text() == landscape.figure(lang), f'{asset.name}: diagram differs from taxonomy')


def check_product_details(manifest):
    if 'products' not in manifest:
        return
    import build_products as products
    import hashlib
    config = manifest['products']
    require(len(products.CONTEXTS) == config['contexts'], 'Product technical-context count differs')
    require(len(products.ITEMS) == config['source_items'], 'Source-item count differs')
    require(len(products.REVIEWS) == config['comparisons'], 'Product comparison count differs')
    require(len(products.CATEGORIES) == config['source_categories'], 'Product source-category count differs')
    require(sum(len(c['cross_source_categories']) for c in products.CONTEXTS.values()) == config['cross_references'],
            'Product cross-reference count differs')
    require(len(products.ITEM_BY_ID) == len(products.ITEMS), 'Duplicate source-item IDs')
    require(len({r['id'] for r in products.REVIEWS}) == len(products.REVIEWS), 'Duplicate product comparison IDs')
    context_members = [sid for c in products.CATEGORIES for sid in c['contexts']]
    require(len(context_members) == len(set(context_members)) and set(context_members) == set(products.CONTEXTS),
            'Product contexts must each belong to exactly one source category')
    item_members = [iid for c in products.CONTEXTS.values() for iid in c['item_ids']]
    require(len(item_members) == len(set(item_members)) and set(item_members) == set(products.ITEM_BY_ID),
            'Every source item must be retained exactly once in its context')
    for c in products.CATEGORIES:
        require(set(c['related_subcategories']) <= set(products.SUBS), f'{c["id"]}: unknown related subcategory')
        require(set(c['comparison_focus']) == {'en', 'zh-CN'} and all(c['comparison_focus'].values()),
                f'{c["id"]}: missing original comparison checklist')
    for iid, item in products.ITEM_BY_ID.items():
        require(item['source_id'] in products.CONTEXTS, f'{iid}: missing technical context')
        require(iid in products.CONTEXTS[item['source_id']]['item_ids'], f'{iid}: context membership differs')
        require(item['display_name'] == re.sub(r'\s+', ' ', item['name_as_published']),
                f'{iid}: display normalization changed source wording')
    for sid, context in products.CONTEXTS.items():
        require(set(context['cross_source_categories']) <= set(products.CATEGORY_BY_ID)
                and len(context['cross_source_categories']) == len(set(context['cross_source_categories'])),
                f'{sid}: invalid cross-category links')
        require(set(context['technical']) == {'en', 'zh-CN'} and all(context['technical'].values()),
                f'{sid}: incomplete bilingual technical evidence')
        require(context['source_checked_on'] == config['source_snapshot'], f'{sid}: archive date changed')
        require(hashlib.sha256(context['technical']['zh-CN'].encode()).hexdigest() == context['source_technical_sha256'],
                f'{sid}: original technical excerpt changed')
    for review in products.REVIEWS:
        require(review['source_id'] in products.CONTEXTS, f'{review["id"]}: unknown source')
        require(bool(review['related_subcategories']) and set(review['related_subcategories']) <= set(products.SUBS),
                f'{review["id"]}: invalid detail routing')
        require(bool(review['facts']) and set(review['facts']) <= set(products.LABELS), f'{review["id"]}: unknown fact fields')
        for iid in review.get('source_item_ids', []):
            require(iid in products.ITEM_BY_ID and products.ITEM_BY_ID[iid]['source_id'] == review['source_id'],
                    f'{review["id"]}: model source item belongs to another context')
        for field, value in review['facts'].items():
            require(set(value) == {'en', 'zh-CN'} and all(value.values()), f'{review["id"]}: incomplete {field}')
        relation = review['research_relation']
        require(relation['kind'] in ('related_route', 'documented_use'), f'{review["id"]}: invalid research relation')
        if relation['kind'] == 'documented_use':
            require(bool(relation.get('primary_quote')) and relation.get('primary_page', 0) > 0
                    and bool(re.fullmatch(r'[0-9a-f]{64}', relation.get('primary_sha256', ''))),
                    f'{review["id"]}: missing primary paper verification record')
            rows = paper_rows((ROOT / 'docs/en' / relation['catalog_path']).read_text())
            matches = [r for r in rows if plain(r[1]) == relation['paper_title']]
            require(len(matches) == 1 and relation['quote'] in plain(' '.join(matches[0]))
                    and relation['paper_url'] in urls(matches[0][1]),
                    f'{review["id"]}: actual-use claim lacks matching catalog evidence')
    for lang in ('en', 'zh-CN'):
        folder = ROOT / 'docs' / lang / 'products'
        require((folder / 'README.md').read_text() == products.make_index(lang), f'{lang}: product index differs from source data')
        require((folder / 'catalog.md').read_text() == products.make_catalog(lang), f'{lang}: source-item catalog differs from source data')
        for c in products.CATEGORIES:
            require((folder / 'references' / (c['id'] + '.md')).read_text() == products.make_reference(c, lang),
                    f'{lang}/{c["id"]}: technical archive differs from source data')
        for topic in products.TOPICS:
            require((folder / 'comparisons' / (topic['id'] + '.md')).read_text() == products.make_comparison(topic, lang),
                    f'{lang}/{topic["id"]}: product comparison differs from source data')
            for sub in topic['subcategories']:
                require((folder / 'topics' / (sub['id'] + '.md')).read_text() == products.make_subtopic(topic, sub, lang),
                        f'{lang}/{sub["id"]}: dedicated topic differs from source data')
    require(sum(len(t['subcategories']) for t in products.TOPICS) == config['dedicated_topics'],
            'Dedicated product topic count differs')


def main():
    manifest = json.loads((ROOT / 'docs/manifest.json').read_text())
    paths = manifest['pages']
    require(len(paths) == len(set(paths)), 'Duplicate manifest paths')
    total = 0
    for lang in ('en', 'zh-CN'):
        actual = {str(p.relative_to(ROOT / 'docs' / lang))
                  for p in (ROOT / 'docs' / lang).rglob('*.md')}
        require(actual == set(paths), f'{lang}: manifest and files differ')
    for rel in paths:
        pair = [ROOT / 'docs' / lang / rel for lang in ('en', 'zh-CN')]
        if not all(p.exists() for p in pair):
            require(False, f'{rel}: missing bilingual counterpart')
            continue
        en, zh = [p.read_text() for p in pair]
        require(external_links(en) == external_links(zh), f'{rel}: external targets differ')
        check_chinese_prose(pair[1], zh)
        require(re.findall(r'^(#+) ', en, re.M) == re.findall(r'^(#+) ', zh, re.M),
                f'{rel}: heading structure differs')
        et, zt = tables(en), tables(zh)
        require(len(et) == len(zt), f'{rel}: table count differs')
        for ti, ((eh, er), (zhh, zr)) in enumerate(zip(et, zt)):
            require(len(eh) == len(zhh) and len(er) == len(zr), f'{rel} table {ti}: dimensions differ')
            for ri, (a, b) in enumerate(zip(er, zr)):
                require(len(a) == len(eh) and len(b) == len(zhh), f'{rel} table {ti} row {ri}: malformed row')
                for ci, (ac, bc) in enumerate(zip(a, b)):
                    require(urls(ac) == urls(bc), f'{rel} table {ti} row {ri} cell {ci}: resource links differ')
                    if re.fullmatch(r'\d+', plain(ac)):
                        require(plain(ac) == plain(bc), f'{rel} table {ti} row {ri} cell {ci}: numeric count differs')
        for ri, (a, b) in enumerate(zip(paper_rows(en), paper_rows(zh))):
            require([plain(c) for c in a[:2]] == [plain(c) for c in b[:2]],
                    f'{rel} paper {ri}: venue/year/title/order differs')
        for path, text in zip(pair, (en, zh)):
            require(text.count('<table') == text.count('</table>'), f'{rel}: unbalanced table tags')
            check_links(path, text)
        require(check_table_layout(pair[0], en) == check_table_layout(pair[1], zh),
                f'{rel}: bilingual column widths/wrapping differ')
    for track in manifest['tracks']:
        subtotal = 0
        for sub in track['subdirections']:
            if sub['count'] is None:
                continue
            for lang in ('en', 'zh-CN'):
                text = (ROOT / 'docs' / lang / sub['path']).read_text()
                actual = len(paper_rows(text))
                require(actual == sub['count'], f'{lang}/{sub["path"]}: expected {sub["count"]}, got {actual}')
                declared = re.search(r'(?:Total: |共(?:计)? )(\d+) (?:papers|篇)', text)
                require(declared is not None and int(declared[1]) == actual, f'{lang}/{sub["path"]}: stale declared total')
            subtotal += sub['count']
        total += subtotal
        for lang in ('en', 'zh-CN'):
            text = (ROOT / 'docs' / lang / track['id'] / 'README.md').read_text()
            declared = re.search(r'(?:Total: |共(?:计)? )(\d+) (?:papers|篇)', text)
            require(declared is not None and int(declared[1]) == subtotal, f'{lang}/{track["id"]}: stale direction total')
            summary = tables(text)[0][1]
            expected = [s['count'] for s in track['subdirections'] if s['count'] is not None]
            require([plain(row[1]) for row in summary] == list(map(str, expected)),
                    f'{lang}/{track["id"]}: stale subdirection summary')
            overview = (ROOT / 'docs' / lang / 'overview.md').read_text()
            overview_rows = next(rows for headers, rows in tables(overview)
                                 if headers[0] in ('Tag', '标签'))
            overview_row = next((row for row in overview_rows
                                 if plain(row[0]).lower() == track['id'] or
                                 plain(row[0]) == {'planning': '规划', 'embodiment': '本体扩展', 'deployment': '部署'}.get(track['id'])), None)
            require(overview_row is not None and plain(overview_row[3]) == str(subtotal),
                    f'{lang}/{track["id"]}: stale overview count')
            home = (ROOT / ('README.md' if lang == 'en' else 'README.zh-CN.md')).read_text()
            home_rows = next(rows for headers, rows in tables(home)
                             if len(headers) == 3 and headers[1] in ('Entries', '条目数'))
            home_row = next((row for row in home_rows
                             if f'href="docs/{lang}/{track["id"]}/README.md"' in row[0]), None)
            require(home_row is not None and plain(home_row[1]) == str(subtotal),
                    f'{lang}/{track["id"]}: stale root direction count')
    require(total == manifest['paper_entries'], 'Manifest total differs from paper rows')
    for lang in ('en', 'zh-CN'):
        extra = tables((ROOT / 'docs' / lang / 'additional-sources.md').read_text())
        require(sum(len(rows) for _, rows in extra) == manifest['additional_entries'], f'{lang}: additional total differs')
    for filename in ('README.md', 'README.zh-CN.md', 'CONTRIBUTING.md', 'CONTRIBUTING.zh-CN.md'):
        path = ROOT / filename
        text = path.read_text()
        check_links(path, text)
        check_table_layout(path, text)
        if 'zh-CN' in filename:
            check_chinese_prose(path, text)
        if filename.startswith('README'):
            require(f'Survey%20Entries-{total}-' in text, f'{filename}: stale badge')
    require(external_links((ROOT / 'README.md').read_text()) ==
            external_links((ROOT / 'README.zh-CN.md').read_text()),
            'Root README external targets differ')
    require(check_table_layout(ROOT / 'README.md', (ROOT / 'README.md').read_text()) ==
            check_table_layout(ROOT / 'README.zh-CN.md', (ROOT / 'README.zh-CN.md').read_text()),
            'Root README bilingual table layouts differ')
    check_landscape(manifest)
    check_product_details(manifest)
    if ERRORS:
        print('\n'.join(ERRORS))
        return 1
    print(f'OK: {len(paths)} bilingual page pairs; {total} main entries; {manifest["additional_entries"]} additional entries; local links valid.')
    print('Translation meaning and external URL availability require separate review.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
