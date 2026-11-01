"""
citation_chasing.py
===================

Stream B component B3: one round of backward and forward citation chasing from
the seed set in STREAM_B_PROTOCOL.md, via the OpenAlex API.

Backward = works in each seed's reference list. Forward = works citing each seed.
Every API request is logged (URL, UTC time, records returned) in
`b3_query_log.csv` so the retrieval can be reproduced or audited.

Usage:  python citation_chasing.py
Writes: b3_seeds.csv, b3_records.csv (one row per unique work, all seeds/directions
        that reached it), b3_query_log.csv
"""
from __future__ import annotations

import csv
import json
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
API = "https://api.openalex.org/works"
UA = {"User-Agent": "stream-b-citation-chasing/1.0"}
FIELDS = "id,doi,title,publication_year,type,authorships,primary_location,abstract_inverted_index,referenced_works,cited_by_count"

# Seed set approved 2026-11-01 (STREAM_B_PROTOCOL.md, B3). DOIs verified in OpenAlex.
SEEDS = {
    "kyle2020": "10.1111/cobi.13625",
    "whitehousetedd2021": "10.1111/cobi.13599",
    "wardropper2021": "10.1111/cobi.13747",
    "moon_blackman2014": "10.1111/cobi.12326",
    "moon2018": "10.1111/2041-210x.13126",
    "boateng2018": "10.3389/fpubh.2018.00149",
    "ghasemi2026": "10.1111/cobi.70326",
    "bennett2017": "10.1016/j.biocon.2016.10.006",
    "teel_manfredo2010": "10.1111/j.1523-1739.2009.01374.x",
    "eyster2025": "10.1111/cobi.14461",
}

query_log: list[dict] = []


def get(url: str) -> dict:
    for attempt in range(5):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                data = json.load(r)
            break
        except Exception as e:
            if attempt == 4:
                raise
            time.sleep(2 ** attempt)
    n = len(data.get("results", [])) if "results" in data else 1
    query_log.append({"utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "url": url, "records": n})
    time.sleep(0.25)
    return data


def paged(filter_: str):
    # Basic page paging (no API key needed; cursor paging now requires one). Max 10,000 results per filter.
    page = 1
    while True:
        q = urllib.parse.urlencode({"filter": filter_, "per-page": 200, "page": page, "select": FIELDS})
        d = get(f"{API}?{q}")
        yield from d["results"]
        if not d["results"] or page * 200 >= d["meta"]["count"]:
            break
        page += 1


def abstract(inv: dict | None) -> str:
    if not inv:
        return ""
    pos = {i: w for w, idx in inv.items() for i in idx}
    return " ".join(pos[i] for i in sorted(pos))


def flat(w: dict) -> dict:
    src = ((w.get("primary_location") or {}).get("source") or {})
    return {
        "openalex_id": w["id"].rsplit("/", 1)[-1],
        "doi": (w.get("doi") or "").replace("https://doi.org/", "").lower(),
        "title": w.get("title") or "",
        "year": w.get("publication_year") or "",
        "type": w.get("type") or "",
        "authors": "; ".join(a["author"]["display_name"] for a in (w.get("authorships") or [])[:10]),
        "venue": src.get("display_name") or "",
        "cited_by_count": w.get("cited_by_count", ""),
        "abstract": abstract(w.get("abstract_inverted_index")),
    }


def main():
    records: dict[str, dict] = {}
    seeds_out = []

    def add(w, seed, direction):
        r = records.setdefault(w["id"].rsplit("/", 1)[-1], {**flat(w), "reached_by": set()})
        r["reached_by"].add(f"{direction}:{seed}")

    for name, doi in SEEDS.items():
        s = get(f"{API}/doi:{doi}?select={FIELDS}")
        sid = s["id"].rsplit("/", 1)[-1]
        refs = [r.rsplit("/", 1)[-1] for r in s.get("referenced_works") or []]
        seeds_out.append({"seed": name, "openalex_id": sid, "doi": doi, "title": s["title"],
                          "year": s["publication_year"], "n_references": len(refs), "n_cited_by": s["cited_by_count"]})
        # Backward: fetch referenced works in batches of 50 ids.
        for i in range(0, len(refs), 50):
            for w in paged("openalex_id:" + "|".join(refs[i:i + 50])):
                add(w, name, "backward")
        # Forward: everything citing the seed.
        for w in paged(f"cites:{sid}"):
            add(w, name, "forward")
        print(f"{name}: refs={len(refs)} cited_by={s['cited_by_count']} running unique={len(records)}", flush=True)

    seed_ids = {s["openalex_id"] for s in seeds_out}
    with open(HERE / "b3_seeds.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(seeds_out[0].keys()))
        w.writeheader()
        w.writerows(seeds_out)
    rows = []
    for r in records.values():
        r = {**r, "reached_by": ";".join(sorted(r["reached_by"])), "is_seed": r["openalex_id"] in seed_ids}
        rows.append(r)
    with open(HERE / "b3_records.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    sys.path.insert(0, str(HERE.parent))
    from local_abstracts import split
    split(HERE / "b3_records.csv")  # abstracts stay in ../local_abstracts/ (not committed)
    with open(HERE / "b3_query_log.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["utc", "url", "records"])
        w.writeheader()
        w.writerows(query_log)
    print("unique records:", len(rows), "queries:", len(query_log))


if __name__ == "__main__":
    main()
