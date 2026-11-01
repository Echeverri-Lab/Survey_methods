# stream_B — supplementary (bottom-up) search

> **Abstracts are not committed** (publisher copyright). Committed CSVs carry DOIs and OpenAlex IDs; full copies with abstracts are kept locally in `local_abstracts/` (gitignored; see `local_abstracts.py`).

Audit of the original Stream B list and the protocol for rebuilding it.

| File | What it is |
|---|---|
| `STREAM_B_PROTOCOL.md` | Draft protocol for the rebuilt Stream B (needs author approval) |
| `stream_b_summary.md` | What the original 242-entry list contains, and what that means for the manuscript |
| `stream_b_reconciled.csv` | One row per original entry: type, role, status, registry match, Stream A overlap, notes |
| `stream_b_log.csv` | Parsed original list with Stream A overlap flags (input to the steps below) |
| `stream_b_manual_codes.csv` | Hand-assigned document type, role, and flag for every entry (editable; re-run reconcile after changes) |
| `stream_b_verification.csv` | Crossref/OpenAlex check for every entry |
| `api_cache.json` | Cached API responses, so the check is reproducible |
| `b3_report.md` | Citation-chasing (B3) run report, and the open decision on the Boateng et al. 2018 forward set |
| `b3_seeds.csv`, `b3_records.csv`, `b3_query_log.csv` | B3 seeds, retrieved records (with abstracts), and every API request made |
| `citation_chasing.py` | Runs B3 |
| `flag_dual_sample.py` | Draws and flags the fixed 20% dual-screening sample (seed 2026) |
| `prescreen_b3.py` | Applies the automated B3 pre-screen (option B) to `../screening_log.csv` |
| `build_screening_log.py` | Creates `../screening_log.csv` with all Stream B rows (run once, before screening) |

## Re-running

```bash
python build_stream_b.py <master_reference_list_all_steps.md> <survey_corpus_v3_retained.csv> \
    <master_corpus_395_plus_repo.csv> <suggested_new_citations.md>
python verify_references.py
python reconcile_stream_b.py
```

The four inputs are in `../exports/` (e.g., `python build_stream_b.py ../exports/master_reference_list_all_steps.md ../exports/survey_corpus_v3_retained.csv ../exports/master_corpus_395_plus_repo.csv ../exports/suggested_new_citations.md`).

`apa_from_crossref.py DOI ...` prints APA references built from Crossref records; it was used to correct repository citations on 2026-11-01.
