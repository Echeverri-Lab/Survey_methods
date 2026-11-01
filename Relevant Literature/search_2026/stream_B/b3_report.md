# B3 citation chasing — run report

**Run:** 2026-11-01, OpenAlex API, one round of backward and forward chasing from 10 seeds (protocol approved 2026-11-01).
**Reproduce:** `python citation_chasing.py`. All 85 API requests are logged in `b3_query_log.csv`. Records: `b3_records.csv`. Seeds: `b3_seeds.csv`.

## Seeds

| Seed | References (backward) | Citing works (forward) |
|---|---|---|
| Kyle et al. 2020 | 56 | 26 |
| Whitehouse-Tedd et al. 2021 | 73 | 28 |
| Wardropper et al. 2021 | 59 | 124 |
| Moon & Blackman 2014 | 77 | 678 |
| Moon et al. 2018 | 49 | 152 |
| Boateng et al. 2018 | 122 | **5,827** |
| Ghasemi et al. 2026 | 73 | 3 |
| Bennett et al. 2017 | 278 | 1,261 |
| Teel & Manfredo 2010 | 25 | 408 |
| Eyster et al. 2025 | 103 | 5 |

Backward counts are works OpenAlex could resolve, which can be fewer than the seed's own reference list.

## Result

- **9,117 unique records.** A record reached from more than one seed or direction is counted once; `reached_by` lists every path.
- Already in the Stream A corpus (1,580): **25**. Already cited in the repository (legacy list): **22**.
- No abstract in OpenAlex: **1,497**. These are screened on title, with the full text checked if the title is ambiguous.
- Non-screenable document types (errata, retractions, editorials, book reviews, peer-review reports, etc.): **207**.
- **5,822 records (64%) were reached only as forward citations of Boateng et al. 2018**, a health-sciences scale-development primer. Most of these are likely empirical studies that apply its scale-development steps, not methodological guidance.

## Decision (2026-11-01): option B

Applied by `prescreen_b3.py` before any human screening:

| Outcome | Records |
|---|---|
| Excluded: unscreenable document type | 207 |
| Excluded: reached only via Boateng 2018, failed guidance rule | 5,193 |
| **To human title/abstract screening** | **3,717** |

Of the 3,717, 769 have no abstract, and 33 are already in Stream A or the legacy repository list.

## Options considered

Whether to screen the 5,822 Boateng-only records in full. The rule must be fixed **before** any screening, and stated in the Methods.

| Option | Records to screen (screenable) | Note |
|---|---|---|
| A. Screen everything | ~8,910 | Most defensible; large workload (about the size of Stream A). |
| B. For Boateng-only records, screen only document types *review / book / chapter* or titles containing a guidance term (*guideline, guidance, best practice, primer, tutorial, recommendation, checklist, framework, review, how to, step-by-step, standard*) | 3,155 + 562 = **~3,717** | Pre-screen rule applied by script and reported. Matches the eligibility criterion (methodological guidance). Some guidance papers with plain titles could be missed. |
| C. Drop Boateng et al. 2018 from the seed set | ~3,155 | Simplest, but changes an approved protocol after seeing the volume. Would need to be reported as a deviation. |

Option C changes the protocol after the data were seen, and Option A has a high cost. Option B keeps the full seed set and applies a transparent, prespecified rule.
