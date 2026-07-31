#!/usr/bin/env python3
"""
Derive the `N` dict for 03_make_fig2_prisma.py from screening_log.csv.

Reads screening_log.csv (default: same folder as this script, or pass a path
as the first argument), tallies every count the PRISMA flow diagram needs,
and prints a copy-pasteable Python dict literal. The point is that the
diagram numbers come from the log -- not from a separate hand tally that can
drift out of sync with it.

Usage:
    python3 count_from_log.py [path/to/screening_log.csv]
"""

import csv
import sys
from collections import Counter
from pathlib import Path

TOPIC_SOURCES = {f"S{i}" for i in range(1, 12)}

FT_EXCLUSION_KEYS = {
    "not_methodological": "excl_ft_notmethod",
    "not_transferable":   "excl_ft_nottransf",
    "superseded":         "excl_ft_superseded",
    "unavailable":        "excl_ft_unavail",
}


def normalize_header(header):
    """Strip the parenthetical allowed-values hint the template header carries,
    e.g. 'curation_decision (retain/set_aside)' -> 'curation_decision'."""
    return header.split("(")[0].strip()


def load_rows(path):
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        header_map = {h: normalize_header(h) for h in reader.fieldnames}
        return [
            {header_map[k]: (v or "").strip() for k, v in raw.items()}
            for raw in reader
        ]


def is_true(value):
    return value.strip().upper() == "TRUE"


def tally(rows):
    n = {
        "db_core": 0, "db_topic": 0,
        "oth_texts": 0, "oth_citation": 0, "oth_standards": 0, "oth_team": 0,
        "duplicates": 0, "screened": 0, "excl_screen": 0,
        "fulltext": 0,
        "excl_ft_notmethod": 0, "excl_ft_nottransf": 0,
        "excl_ft_superseded": 0, "excl_ft_unavail": 0,
        "eligible": 0, "not_prioritised": 0,
        "included": 0, "cited_main": 0, "in_repo_tables": 0,
    }
    unrecognized_sources = Counter()
    unrecognized_ft_reasons = Counter()

    for row in rows:
        source = row.get("source", "")
        duplicate_of = row.get("duplicate_of", "")
        screen_ta = row.get("screen_ta_decision", "").lower()
        ft_decision = row.get("fulltext_decision", "").lower()
        ft_reason = row.get("fulltext_exclusion_reason", "")
        curation_decision = row.get("curation_decision", "").lower()

        # --- Identification: every row counts toward its raw source total,
        # duplicates included -- duplicates are subtracted out below, exactly
        # as the flow diagram does (identified minus duplicates = screened).
        if source == "core":
            n["db_core"] += 1
        elif source in TOPIC_SOURCES:
            n["db_topic"] += 1
        elif source == "texts":
            n["oth_texts"] += 1
        elif source == "citation_chasing":
            n["oth_citation"] += 1
        elif source == "standards":
            n["oth_standards"] += 1
        elif source == "team_corpus":
            n["oth_team"] += 1
        elif source:
            unrecognized_sources[source] += 1

        if duplicate_of:
            n["duplicates"] += 1
            continue

        n["screened"] += 1

        if screen_ta == "exclude":
            n["excl_screen"] += 1
            continue
        if screen_ta != "include":
            continue  # not yet screened

        n["fulltext"] += 1

        if ft_decision == "exclude":
            key = FT_EXCLUSION_KEYS.get(ft_reason)
            if key:
                n[key] += 1
            elif ft_reason:
                unrecognized_ft_reasons[ft_reason] += 1
            continue
        if ft_decision != "include":
            continue  # not yet assessed

        n["eligible"] += 1

        if curation_decision == "set_aside":
            n["not_prioritised"] += 1
            continue
        if curation_decision != "retain":
            continue  # not yet curated

        n["included"] += 1
        if is_true(row.get("cited_in_main_text", "")):
            n["cited_main"] += 1
        if is_true(row.get("in_repo_living_table", "")):
            n["in_repo_tables"] += 1

    return n, unrecognized_sources, unrecognized_ft_reasons


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent / "screening_log.csv"

    if not path.exists():
        print(f"No log found at {path}.")
        print("Copy screening_log_TEMPLATE.csv to screening_log.csv, fill it in, and re-run.")
        return

    rows = load_rows(path)
    if not rows:
        print(f"{path} exists but has no data rows yet.")
        return

    n, unrecognized_sources, unrecognized_ft_reasons = tally(rows)

    if unrecognized_sources:
        print(f"[warning] unrecognized 'source' values (not counted): "
              f"{dict(unrecognized_sources)}", file=sys.stderr)
    if unrecognized_ft_reasons:
        print(f"[warning] unrecognized 'fulltext_exclusion_reason' values "
              f"(not counted): {dict(unrecognized_ft_reasons)}", file=sys.stderr)

    print(f"# Derived from {path.name} -- {len(rows)} record(s) in the log.")
    print("# Paste this into the N dict at the top of 03_make_fig2_prisma.py")
    print("N = {")
    for key, value in n.items():
        print(f"    {key!r:22}: {value},")
    print("}")


if __name__ == "__main__":
    main()
