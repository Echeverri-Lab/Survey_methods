"""
apa_from_crossref.py
====================

Builds APA-style reference strings from Crossref records (by DOI), so corrected
repository citations come from registry metadata rather than being typed.

Usage:  python apa_from_crossref.py DOI [DOI ...]   -> prints one reference per DOI
"""
import json
import re
import sys
import urllib.parse
import urllib.request


def apa(doi):
    m = json.load(urllib.request.urlopen(urllib.request.Request(
        "https://api.crossref.org/works/" + urllib.parse.quote(doi), headers={"User-Agent": "repo-ref-fix/1.0"}), timeout=30))["message"]
    names = []
    for a in m.get("author", []):
        given = " ".join(p[0] + "." for p in a.get("given", "").replace("-", " ").split() if p)
        names.append(f"{a.get('family', '')}, {given}".strip(", "))
    if len(names) > 20:
        names = names[:19] + ["…", names[-1]]
    auth = ", ".join(names[:-1]) + (", & " if len(names) > 1 else "") + names[-1] if names else ""
    year = (m.get("issued", {}).get("date-parts") or [[""]])[0][0]
    title = re.sub(r"<[^>]+>|\s+", " ", (m.get("title") or [""])[0]).strip().rstrip(".")
    cont = (m.get("container-title") or [""])[0]
    vol, iss, pg = m.get("volume"), m.get("issue"), m.get("page") or m.get("article-number")
    src = f"*{cont}*" if cont else ""
    if vol:
        src += f", *{vol}*" + (f"({iss})" if iss else "")
    if pg:
        src += f", {pg}"
    return f"{auth} ({year}). {title}. {src}. https://doi.org/{m['DOI']}"


if __name__ == "__main__":
    for d in sys.argv[1:]:
        try:
            print(apa(d))
        except Exception as e:  # unregistered DOI, network error
            print(f"NOT FOUND {d}: {e}")
