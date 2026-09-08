#!/usr/bin/env python3
"""Format paired documentation tables with explicit GitHub-compatible widths.

English column names define widths for both languages. Existing explicit widths
are retained. Archived source snapshots are intentionally outside this scope.
"""
from pathlib import Path
from html import escape
import re

ROOT = Path(__file__).resolve().parents[1]
TABLE = re.compile(r'<table\b[^>]*>.*?</table>', re.S)
CELLS = re.compile(r'<t[hd]\b([^>]*)>(.*?)</t[hd]>', re.S)
WIDTHS = {
    'Tag': 110, 'Direction': 240, 'Subdirection': 280, 'Entries': 90,
    'Subdirections': 760, 'Topic': 340, 'Trend': 680, 'Meaning': 620,
    'Takeaway': 620, 'Focus': 720, 'Source': 320, 'Use': 360,
    'Entry': 250, 'Date': 110, 'Resource': 200, 'Why Track': 460,
    'Venue/Year': 120, 'Paper/Method': 320, 'Abstract': 420,
    'Task Type': 220, 'Environment': 240, 'Map/Memory': 260,
    'Training/Feedback': 300, 'Sim/Real/Benchmark': 240,
    'Paper Task/Goal': 360, 'Paper': 110, 'Project': 110,
    'Code': 110, 'Data/Bench': 240, 'Base VLA': 230,
    'Action': 240, 'Algorithm': 260, 'Policy/Type': 240,
    'Sim/Real': 200, 'WAM Type': 220, 'State Representation': 280,
    'Action Interface': 260, 'Benchmark': 260,
    'Planning Granularity': 240, 'Tool/Memory': 260,
    'Feedback/Self-Improvement': 300, 'Execution Interface': 260,
    'Validation Environment': 260, 'Object Type': 240,
    'Efficiency Metric': 280, 'Platform/Hardware': 280,
    'Covered Tasks': 280, 'Open Resource Status': 220,
}
SHORT = {'Tag', 'Entries', 'Papers', 'Coverage', 'Date', 'Venue/Year', 'Venue'}


def inline(text):
    """Render the links, emphasis and inline code used by our compact indexes."""
    pattern = r'\[([^\]]+)\]\(([^)]+)\)|`([^`]+)`|\*\*([^*]+)\*\*'
    out, end = [], 0
    for m in re.finditer(pattern, text):
        out.append(escape(text[end:m.start()], quote=False))
        if m[1] is not None:
            out.append(f'<a href="{escape(m[2], quote=True)}">{escape(m[1], quote=False)}</a>')
        elif m[3] is not None:
            out.append(f'<code>{escape(m[3], quote=False)}</code>')
        else:
            out.append(f'<strong>{escape(m[4], quote=False)}</strong>')
        end = m.end()
    out.append(escape(text[end:], quote=False))
    return ''.join(out)


def convert_markdown(text):
    lines = text.splitlines(keepends=True)
    output, i = [], 0
    def cells(line):
        return [c.strip() for c in re.split(r'(?<!\\)\|', line.strip().strip('|'))]
    while i < len(lines):
        if (i + 1 < len(lines) and lines[i].lstrip().startswith('|')
                and all(re.fullmatch(r':?-{3,}:?', c) for c in cells(lines[i + 1]))):
            head = cells(lines[i])
            rows, j = [], i + 2
            while j < len(lines) and lines[j].lstrip().startswith('|'):
                row = cells(lines[j])
                if len(row) != len(head):
                    raise ValueError('Markdown table row has wrong column count')
                rows.append(row)
                j += 1
            table = '<table>\n<thead>\n<tr>\n'
            table += '\n'.join(f'<th>{inline(c)}</th>' for c in head)
            table += '\n</tr>\n</thead>\n<tbody>\n'
            for row in rows:
                table += '<tr>\n' + '\n'.join(f'<td>{inline(c)}</td>' for c in row) + '\n</tr>\n'
            output.append(table + '</tbody>\n</table>\n')
            i = j
        else:
            output.append(lines[i])
            i += 1
    return ''.join(output)


def layout(table):
    header = re.search(r'<thead>(.*?)</thead>', table, re.S)[1]
    widths, nowrap = [], []
    for attrs, name in CELLS.findall(header):
        name = re.sub(r'<[^>]+>', '', name)
        old = re.search(r'\bwidth="(\d+)"', attrs)
        if not old and name not in WIDTHS:
            raise ValueError(f'Add an explicit column width for {name!r}')
        width = int(old[1]) if old else WIDTHS[name]
        widths.append(width)
        nowrap.append(bool(re.search(r'\bnowrap\b', attrs)) if old else
                      name in SHORT or (name in {'Paper', 'Project', 'Code'} and width <= 120))
    return widths, nowrap


def format_table(table, widths, nowrap):
    rows = []
    for row in re.findall(r'<tr\b[^>]*>(.*?)</tr>', table, re.S):
        cells = CELLS.findall(row)
        if len(cells) != len(widths):
            raise ValueError('HTML table row has wrong column count')
        rows.append([content for _, content in cells])
    output = [f'<table width="{sum(widths)}">', '<thead>']
    for index, row in enumerate(rows):
        if index == 1:
            output += ['</thead>', '<tbody>']
        output.append('<tr>')
        for i, content in enumerate(row):
            tag = 'th' if index == 0 else 'td'
            attrs = f' width="{widths[i]}"' + (' nowrap' if nowrap[i] else '')
            output.append(f'<{tag}{attrs}>{content}</{tag}>')
        output.append('</tr>')
    if len(rows) == 1:
        output += ['</thead>', '<tbody>']
    output += ['</tbody>', '</table>']
    return '\n'.join(output)


def main():
    pairs = [(ROOT / 'README.md', ROOT / 'README.zh-CN.md')]
    pairs += [(p, ROOT / 'docs/zh-CN' / p.relative_to(ROOT / 'docs/en'))
              for p in sorted((ROOT / 'docs/en').rglob('*.md'))]
    total = 0
    pending = {}
    for en, zh in pairs:
        texts = [convert_markdown(p.read_text()) for p in (en, zh)]
        tables = [TABLE.findall(text) for text in texts]
        if len(tables[0]) != len(tables[1]):
            raise ValueError(f'Table count differs: {en}')
        specs = [layout(table) for table in tables[0]]
        for path, text in zip((en, zh), texts):
            it = iter(specs)
            pending[path] = TABLE.sub(lambda m: format_table(m[0], *next(it)), text)
        total += len(specs)
    for path, text in pending.items():
        if path.read_text() != text:
            path.write_text(text)
    print(f'Formatted {total} bilingual table pairs ({total * 2} tables).')


if __name__ == '__main__':
    main()
