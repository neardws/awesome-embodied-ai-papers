# Maintaining the bilingual catalog

[中文](CONTRIBUTING.zh-CN.md)

1. Find the topic in the root README. Edit `docs/en/<direction>/<topic>.md` and the matching `docs/zh-CN/<direction>/<topic>.md` together. These files are the source of truth; do not paste tables back into the root README.
2. Keep venue/year, official paper title, row order, resource URLs, quantitative claims and evidence boundaries aligned. Use Chinese for explanatory prose and labels; retain only official paper titles, proper model/platform/dataset names, venues, necessary abbreviations, units and commands. Language-specific official source URLs are allowed only when explicitly recorded in the checker.
3. For an added or removed entry, update the subdirection total, direction index and summary table, overview table, root README counts and badge, and `docs/manifest.json`. Counts are categorized entries, not globally unique papers. Keep the seven additional leads separate unless deliberately merging them.
4. For a new topic, add both language files and register the matching relative path in `docs/manifest.json`; update navigation in both languages. Use relative links to the matching language page and root README.
5. Run `python3 scripts/check_docs.py`. Review both rendered Markdown pages on GitHub, including tables, language switches and figures. The checker validates structure, paper identities, resource links, counts and local targets; it also catches common untranslated prose and accidental root URL edits, but cannot verify translation meaning or remote source claims.

Source snapshots under `sources/github/readmes/` remain archived inputs. Do not reorganize or translate them as project documentation. Historical figures are marked in the overview; update both language assets together when regenerating them. Preserve factual verification dates rather than replacing them with the editing date.

The initial reorganization and audit are recorded in [the audit report](docs/en/consistency-audit.md).

## Table layout

All documentation tables use the hardware-reference style: an explicit total width and matching widths on every header and data cell. Short metadata may use `nowrap`; titles, summaries and analysis wrap within their columns. GitHub supplies horizontal scrolling when a table exceeds the available width; no custom scrolling script is required.

Run `python3 scripts/format_tables.py` after editing table structure, then `python3 scripts/check_docs.py`. The formatter uses English field names to apply the same widths to both languages and preserves existing explicit widths. Add new field defaults to `WIDTHS` when needed. Keep the total width equal to the sum of the column widths. The checker rejects missing widths, mismatched bilingual layouts and new pipe tables. Archived source README snapshots are excluded.

## Landscape updates

The landscape is maintained by topic in `sources/landscape/topics/`. Update both language fields in the relevant JSON file, then run `python3 scripts/build_landscape.py` and `python3 scripts/check_docs.py`. The builder refreshes the paired topic pages, overview, diagram, homepage section and research cross-links. Avoid editing generated sections directly.

Maintain primary examples and their scoped claims in `sources/landscape/sources.json`, synthesis in `sources/landscape/progress.json`, and taxonomy order in `sources/landscape/index.json`. Each source needs a role, an exact URL, a check date and evidence states. Taxonomy changes must preserve stable subcategory anchors or provide a migration. Examples are not an exhibitor census, compatibility guarantee or market ranking.
