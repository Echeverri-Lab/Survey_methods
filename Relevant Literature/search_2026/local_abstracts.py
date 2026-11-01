"""
local_abstracts.py
==================

Abstracts are kept out of the public repository: publisher abstracts are often
under copyright, and anyone can retrieve them again from the DOI or OpenAlex ID
in each record. Complete copies of every CSV with an `abstract` column are kept
in `local_abstracts/` (gitignored), and the committed CSVs carry no abstracts.

    python local_abstracts.py FILE.csv [...]   split: save full copy locally, strip the public file

Scripts that need abstracts use `full_copy()` or `lookup()`.
"""
from __future__ import annotations

import csv
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LOCAL = HERE / "local_abstracts"
csv.field_size_limit(10**8)


def split(path: Path) -> bool:
    """Save a full copy in local_abstracts/ and rewrite `path` without the abstract column."""
    path = Path(path)
    with open(path, encoding="utf-8", errors="replace") as f:
        reader = csv.DictReader(f)
        cols, rows = reader.fieldnames, list(reader)
    if "abstract" not in cols:
        return False
    LOCAL.mkdir(exist_ok=True)
    shutil.copyfile(path, LOCAL / path.name)
    keep = [c for c in cols if c != "abstract"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=keep, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    return True


def full_copy(path: Path) -> Path:
    """The local copy with abstracts if it exists, else the public file."""
    local = LOCAL / Path(path).name
    return local if local.exists() else Path(path)


def lookup(name: str, key: str) -> dict[str, str]:
    """Map `key` -> abstract from local_abstracts/<name>; empty if the local copy is absent."""
    local = LOCAL / name
    if not local.exists():
        return {}
    with open(local, encoding="utf-8", errors="replace") as f:
        return {r[key]: r.get("abstract", "") for r in csv.DictReader(f)}


if __name__ == "__main__":
    for p in sys.argv[1:]:
        print(("stripped " if split(Path(p)) else "no abstract column ") + p)
