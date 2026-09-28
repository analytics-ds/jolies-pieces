"""Controle de reciprocite des hreflang sur le site genere (dossier public/).

Lance par la CI apres `hugo`, avant le deploiement. Sort en erreur, et bloque donc
la mise en ligne, si une page :
  - ne se cite pas elle-meme dans ses hreflang,
  - pointe vers une page absente du build,
  - pointe vers une page qui ne la cite pas en retour,
  - a un x-default different de celui de ses traductions,
  - declare dans le sitemap des hreflang differents de ceux de son HTML.

Usage : python3 .github/scripts/check_hreflang.py public
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "public")
ALT = re.compile(r'<link rel="?alternate"? hreflang="?([\w-]+)"? href="?([^" >]+)')
CANON = re.compile(r'<link rel="?canonical"? href="?([^" >]+)')
REFRESH = re.compile(r'http-equiv="?refresh', re.I)


def alternates(html):
    return {lang: url for lang, url in ALT.findall(html)}


pages = {}
for f in ROOT.rglob("*.html"):
    html = f.read_text(errors="ignore")
    if REFRESH.search(html):  # pages de redirection generees par Hugo (/fr/, alias)
        continue
    canon = CANON.search(html)
    if canon:
        pages[canon.group(1)] = alternates(html)

errors = []
for url, alts in sorted(pages.items()):
    if not alts:
        continue
    langs = {k: v for k, v in alts.items() if k != "x-default"}
    if url not in langs.values():
        errors.append(f"{url} : ne se cite pas elle-meme")
    for lang, target in langs.items():
        if target == url:
            continue
        back = pages.get(target)
        if back is None:
            errors.append(f"{url} -> {target} ({lang}) : page cible absente du build")
        elif url not in [u for k, u in back.items() if k != "x-default"]:
            errors.append(f"{url} -> {target} ({lang}) : pas de lien retour")
        elif back.get("x-default") != alts.get("x-default"):
            errors.append(f"{url} et {target} : x-default differents")

sitemap = ROOT / "sitemap.xml"
if sitemap.exists():
    xml = sitemap.read_text()
    for block in re.findall(r"<url>(.*?)</url>", xml, re.S):
        loc = re.search(r"<loc>([^<]+)</loc>", block).group(1)
        sm = dict(re.findall(r'hreflang="([\w-]+)" href="([^"]+)"', block))
        html = pages.get(loc)
        if html is not None and sm != html:
            errors.append(f"sitemap {loc} : hreflang {sm} differents du HTML {html}")

checked = sum(1 for a in pages.values() if a)
if errors:
    print(f"hreflang : {len(errors)} erreur(s) sur {checked} pages traduites")
    print("\n".join("  - " + e for e in errors))
    sys.exit(1)
print(f"hreflang : OK, {checked} pages traduites, toutes reciproques")
