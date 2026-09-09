# Bilingual consistency and localization audit

[Home](../../README.md) | [中文](../zh-CN/consistency-audit.md)

Baseline: `dfadfa5` (Audit humanoid training resources). Review date: 2026-09-08. This review compares repository content; it does not constitute a new external verification of every paper or product specification.

## Catalog consistency

- Both original READMEs contained 14,512 lines, 54 HTML tables and 958 table-body rows. All 958 rows per language remain in the split documents.
- The 767 main entries have matching official titles, venues/years, order and per-cell resource links. The seven additional source leads remain separate. No entry exists in only one language.
- The old badges said 707, whereas the six current direction totals are 92 + 251 + 70 + 103 + 146 + 105 = 767. Both root badges use 767 categorized entries. Figure counts remain explicitly labeled historical snapshots.
- The HumanPlus/OmniH2O hardware paragraph now says H1 in both languages. The Chinese lab-built biped specification now clearly says 12 total degrees of freedom, 6 per leg.
- Numerical comparisons covered measurement values, percentages, data sizes, training resources and counts. Thousands separators, k/M versus Chinese scale units, number words and reordered descriptions were reviewed as equivalent expressions, rather than treated as factual conflicts.
- The AgiBot source catalog intentionally retains the English and Chinese URLs of the same official documentation; this is an explicit checker exception.

## Chinese localization

- Revised 3,573 Chinese table cells, including full summaries, tasks, environments, methods, evaluation descriptions, limitations and resource labels. Generic English phrases in the Chinese prose, navigation and headings were translated.
- Official paper titles, model/platform/dataset names, venue names, necessary abbreviations, units, URLs and executable commands remain in their original form. English sentences are not retained merely because they were inherited from a source catalog.
- Preserved evidence boundaries such as not disclosed, simulation only, unverified deployment claims, author-stated limitations and inferred future directions. Translation does not upgrade these to demonstrated real-world results.
- Localized the four Chinese SVG figures referenced by the overview and regenerated their PNG counterparts. Full-size rendering was checked; historical statistics were not refreshed.

## Maintenance checks

The earlier reorganization produced 41 documentation pages per language; the landscape expansion brings this to 58, retaining six research indexes and 29 paper-topic files. The checker passed bilingual structure, identities, resource targets, counts and local links. It also checks common untranslated prose terms and root external targets to catch omissions and accidental URL edits.

Run `python3 scripts/check_docs.py` after paired edits. Automated checks complement human translation review; they do not prove every sentence's semantic equivalence or the availability of remote sources. See the [maintenance guide](../../CONTRIBUTING.md).

## Unified table formatting

The preceding formatting pass standardized 64 bilingual table pairs (128 tables) with explicit total and per-column widths, matching the Unitree biped reference style. Existing column widths are retained; formerly widthless tables receive field-specific widths. Compact Markdown indexes were converted to the same HTML structure. Header and body widths match in both languages.

The Chinese tactile-topic index previously displayed a dash instead of 28; it now matches the English index and the 28-entry main table. Other cell contents were preserved. Formatting is idempotent, and layout validation runs alongside content checks.

Representative indexes, VLA tables and embodiment tables were rendered locally in Chrome with GitHub Markdown CSS at 1280 px and 390 px viewport widths. Wide tables scrolled internally; the page itself did not overflow horizontally. This is local rendering validation, not a published GitHub preview.

## Research and industry landscape expansion

Added 17 bilingual page pairs: a landscape index, progress analysis, evidence register and 14 topic pages covering 84 subcategories. Each subcategory distinguishes its problem, academic focus, industrial delivery focus and comparison criteria. The selected examples cite 37 primary sources, with research, public-resource, product-documentation and field-case evidence distinguished.

The homepage now leads with the landscape diagram and domain index, then returns to the existing paper map. The six research indexes link back to related landscape domains. All 767 paper rows remain unchanged. At the landscape-only stage, the repository contained 104 bilingual table pairs (208 tables), with explicit column widths.

The 36 new or reorganized pages passed 72 local Chrome checks at desktop and narrow viewport widths using GitHub Markdown styling. No broken image or page-level horizontal overflow was found; subcategory navigation and bilingual switching passed. Both SVG diagrams were rendered and visually inspected. Sources were reviewed as scoped evidence, not independently reproduced experiments, commercial inventory or audited operational performance.

## Product and technical detail restoration

Restored 312 complete technical excerpts, original product/application wording, original tags and historical verification notes from the 2026-09-05 archive. All 917 source-published exhibit associations and 236 cross-category entry points are retained. The 57 contexts without structured exhibit lists remain searchable without inventing model records. Booth directories and company biographies were not imported as a new roster.

Added 170 manually attributed model/family comparison records with domain-specific fields, sources and conditions. Distinct models are kept separate; unresolved or mixed claims remain in their original context. The RH56DFX/HumanPlus association was checked in the primary PDF on page 4; other relationships remain related research routes unless use is documented.

Three missing distinctions—mobile bases, fixed upper-body platforms, and environmental/chemical sensing—extend the landscape from 84 to 87 subcategories. Added 86 bilingual detail-page pairs: 14 comparison pages, 70 evidence-category pages, a detail index and a full source-item index. There are now 144 documentation pages per language and 849 bilingual table pairs.

Validation preserved all 77 input-file hashes and every original technical excerpt and source-item name/URL. The Magic MA1 name contained a vertical-tab character: its full raw name is preserved and display whitespace normalized. Bilingual generation, local links, cross-references, paper-use evidence and table layouts pass the checker. Desktop/narrow rendering was checked across all 174 new/reorganized pages, with additional model-attribution and comparison-table checks. The 767 existing paper rows remain unchanged.
