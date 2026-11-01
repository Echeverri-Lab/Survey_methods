"""
build_screening_log.py
======================

Creates `../screening_log.csv` (the single log for all review records, per
STREAM_B_PROTOCOL.md) and fills it with Stream B rows:

  B1 standards  — the fixed list of named standards and guidance documents
  B2 texts      — reviewer-nominated texts (syllabi and author nominations to be added)
  B3 citation_chasing — every record from b3_records.csv, flagged if it is a
                 seed, already in the Stream A corpus, or already cited in the repo
  B4 team_corpus — the author team's studies used as worked examples

Screening columns are left blank for the screeners. Re-running overwrites the
log, so run it only before screening starts.

Usage:  python build_screening_log.py <survey_corpus_v3_retained.csv>
"""
from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_stream_b import clean_doi, norm_title, title_guess  # noqa: E402

HERE = Path(__file__).resolve().parent
LOG = HERE.parent / "screening_log.csv"
csv.field_size_limit(10**8)

TEMPLATE_COLS = next(csv.reader(open(HERE.parent / "screening_log_TEMPLATE.csv", encoding="utf-8")))
COLS = TEMPLATE_COLS + ["openalex_id", "reached_by", "abstract"]
SRC, DUP = TEMPLATE_COLS[1], TEMPLATE_COLS[7]

B1 = [
    ("AAPOR", "Standard Definitions: Final Dispositions of Case Codes and Outcome Rates for Surveys (current edition)"),
    ("AAPOR", "Code of Professional Ethics and Practices"),
    ("AAPOR", "Transparency Initiative disclosure elements"),
    ("ESOMAR; WAPOR", "ESOMAR/WAPOR Guideline on Opinion Polls and Published Surveys"),
    ("EQUATOR Network", "Reporting guideline library: survey and qualitative research guidelines"),
    ("Appelbaum et al.", "Journal Article Reporting Standards for Quantitative Research in Psychology (JARS-Quant)"),
    ("Levitt et al.", "Journal Article Reporting Standards for Qualitative Research in Psychology (JARS-Qual)"),
    ("Eysenbach", "Checklist for Reporting Results of Internet E-Surveys (CHERRIES)"),
    ("Tong, Sainsbury, Craig", "Consolidated criteria for reporting qualitative research (COREQ)"),
    ("O'Brien et al.", "Standards for Reporting Qualitative Research (SRQR)"),
    ("Page et al.", "The PRISMA 2020 statement"),
    ("Tricco et al.", "PRISMA Extension for Scoping Reviews (PRISMA-ScR)"),
    ("Haddaway et al.", "ROSES: RepOrting standards for Systematic Evidence Syntheses"),
    ("Collaboration for Environmental Evidence", "Guidelines and Standards for Evidence Synthesis in Environmental Management"),
    ("Carroll et al.", "The CARE Principles for Indigenous Data Governance"),
    ("Wilkinson et al.", "The FAIR Guiding Principles for scientific data management and stewardship"),
    ("CIHR; NSERC; SSHRC", "Tri-Council Policy Statement: Ethical Conduct for Research Involving Humans (TCPS 2)"),
    ("US DHHS", "The Belmont Report; Federal Policy for the Protection of Human Subjects (Common Rule)"),
]
B2_REVIEWER = [
    ("Vaske, J. J.", 2019, "Survey research and analysis (2nd ed.)", "Sagamore-Venture"),
    ("Fink, A.", 2003, "How to assess and interpret survey psychometrics", "Sage"),
    ("Johnson, R. L.; Morgan, G. B.", 2016, "Survey scales: A guide to development, analysis, and reporting", "Guilford"),
    ("Ford, L. R.; Scandura, T. A. (Eds.)", 2023, "The SAGE handbook of survey development and application", "SAGE"),
    ("Lam, T. C. M.; Green, K. E.", 2023, "Survey development: A theory-driven mixed-method approach", "Taylor & Francis"),
    ("Irwing, P.; Booth, T.; Hughes, D. J. (Eds.)", 2018, "The Wiley handbook of psychometric testing", "Wiley"),
    ("Dillman, D. A.; Smyth, J. D.; Christian, L. M.", 2014, "Internet, phone, mail, and mixed-mode surveys: The tailored design method (4th ed.)", "Wiley"),
    ("Brown, T. A.", 2015, "Confirmatory factor analysis for applied research (2nd ed.)", "Guilford"),
]
B4_TEAM = [
    ("Boren, A.; Echeverri, A.", 2025, "Does psychic numbing apply to endangered species conservation? The case of the Peregrine Falcon in Berkeley, California", "10.3389/fcosc.2025.1490272"),
    ("Callahan, M. M. et al.", 2019, "Using the Phylo Card Game to advance biodiversity conservation in an era of Pokémon", "10.1057/s41599-019-0287-9"),
    ("Dayer, A. A. et al.", 2020, "Applying conservation social science to study the human dimensions of Neotropical bird conservation", "10.1093/condor/duaa021"),
    ("Dinat, D. et al.", 2019, "Eco-xenophobia among rural populations: The Great-tailed Grackle as a contested species in Guanacaste, Costa Rica", "10.1080/10871209.2019.1614239"),
    ("Echeverri, A.; Chan, K. M. A.; Zhao, J.", 2017, "How messaging shapes attitudes toward sea otters as a species at risk", "10.1080/10871209.2016.1272146"),
    ("Echeverri, A. et al.", 2019, "Iconic manakins and despicable grackles: Comparing cultural ecosystem services and disservices across stakeholders in Costa Rica", "10.1016/j.ecolind.2019.105454"),
    ("Echeverri, A. et al.", 2021, "Avian cultural services peak in tropical wet forests", "10.1111/conl.12763"),
    ("Langhans, K. E. et al.", 2025, "Watching from your own residence makes it more accessible: Identifying supports and barriers to participatory science", "10.5334/cstp.874"),
    ("Langhans, K. E. et al.", 2025, "Urban community gardens foster positive human-avian interactions across an income gradient in San Francisco", "10.1016/j.landurbplan.2025.105391"),
    ("Niesner, C. A.; Kelty, C.; Robins, S.", 2024, "The coyote in the cloud", "10.1177/25148486241229011"),
]


def blank(**kw):
    r = {c: "" for c in COLS}
    r.update(kw)
    return r


def main(streamA_csv):
    a_doi, a_title = {}, {}
    with open(streamA_csv, encoding="utf-8", errors="replace") as f:
        for r in csv.DictReader(f):
            key = "A:" + (r.get("wos_accession") or r.get("doi") or r["title"][:40])
            if r.get("doi"):
                a_doi[clean_doi(r["doi"])] = key
            a_title[norm_title(r["title"])] = key
    legacy_doi, legacy_title = {}, {}
    for r in csv.DictReader(open(HERE / "stream_b_reconciled.csv", encoding="utf-8")):
        if r["status"] == "merge_duplicate":
            continue
        key = "legacy:" + r["record_id"]
        if r["registry_doi"]:
            legacy_doi[clean_doi(r["registry_doi"])] = key
        t = norm_title(r["registry_title"] or title_guess(r["reference"]))
        if len(t) > 25:
            legacy_title[t] = key

    def dup_of(doi, title):
        t = norm_title(title)
        hits = [d.get(doi) for d in (a_doi, legacy_doi) if doi] + [d.get(t) for d in (a_title, legacy_title) if len(t) > 25]
        return ";".join(sorted({h for h in hits if h}))

    rows = []
    for i, (who, what) in enumerate(B1, 1):
        rows.append(blank(record_id=f"B1-{i:03d}", **{SRC: "standards"}, authors=who, title=what,
                          notes="Record version and date accessed when retrieved"))
    for i, (who, yr, what, pub) in enumerate(B2_REVIEWER, 1):
        rows.append(blank(record_id=f"B2-{i:03d}", **{SRC: "texts"}, authors=who, year=yr, title=what,
                          journal_or_publisher=pub, notes="Nominated by Reviewer 1 (ConBio 26-785)"))
    for i, (who, yr, what, doi) in enumerate(B4_TEAM, 1):
        rows.append(blank(record_id=f"B4-{i:03d}", **{SRC: "team_corpus"}, authors=who, year=yr, title=what, doi=doi,
                          **{DUP: dup_of(doi, what)}, notes="Worked example only; not counted as evidence"))
    sys.path.insert(0, str(HERE.parent))
    from local_abstracts import full_copy, split
    b3 = list(csv.DictReader(open(full_copy(HERE / "b3_records.csv"), encoding="utf-8")))
    for i, r in enumerate(sorted(b3, key=lambda r: r["openalex_id"]), 1):
        rows.append(blank(record_id=f"B3-{i:05d}", **{SRC: "citation_chasing"}, authors=r["authors"], year=r["year"],
                          title=r["title"], journal_or_publisher=r["venue"], doi=r["doi"],
                          **{DUP: dup_of(r["doi"], r["title"])}, openalex_id=r["openalex_id"],
                          reached_by=r["reached_by"], abstract=r.get("abstract", ""),
                          notes="Seed paper" if r["is_seed"] == "True" else ""))
    with open(LOG, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        w.writeheader()
        w.writerows(rows)

    split(LOG)  # abstracts stay in ../local_abstracts/ (not committed)
    b3rows = [r for r in rows if r[SRC] == "citation_chasing"]
    print("log rows:", Counter(r[SRC] for r in rows))
    print("B3 dup with Stream A:", sum("A:" in r[DUP] for r in b3rows),
          "| dup with legacy list:", sum("legacy:" in r[DUP] for r in b3rows),
          "| no abstract:", sum(not r["abstract"] for r in b3rows),
          "| seeds:", sum(r["notes"] == "Seed paper" for r in b3rows))
    fwd = Counter(); back = Counter(); only_boateng = 0
    for r in b3rows:
        via = r["reached_by"].split(";")
        for v in via:
            d, s = v.split(":")
            (fwd if d == "forward" else back)[s] += 1
        if via == ["forward:boateng2018"]:
            only_boateng += 1
    print("forward by seed:", dict(fwd))
    print("backward by seed:", dict(back))
    print("reached only as forward citation of Boateng 2018:", only_boateng)
    print("types:", Counter(r["type"] for r in b3))
    print("years:", sorted(Counter(r["year"] for r in b3).items())[-8:])


if __name__ == "__main__":
    main(sys.argv[1])
