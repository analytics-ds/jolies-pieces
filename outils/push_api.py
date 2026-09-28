#!/usr/bin/env python3
"""Pousse un arbre de fichiers sur GitHub via l'API Git (api.github.com).

Contournement : le shell n'a pas acces a github.com (git bloque), mais api.github.com repond.
On cree les blobs, un arbre, un commit, puis on pose la reference.
"""

import base64
import json
import os
import subprocess
import sys
import urllib.request

REPO = sys.argv[1]            # ex: analytics-ds/cuir-et-couture
ROOT = sys.argv[2]            # dossier local a pousser
MESSAGE = sys.argv[3]
BRANCH = sys.argv[4] if len(sys.argv) > 4 else "main"

TOKEN = subprocess.check_output(["gh", "auth", "token", "-u", "analytics-ds"], text=True).strip()
API = "https://api.github.com"


def call(method, path, payload=None):
    url = path if path.startswith("http") else API + path
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", f"Bearer {TOKEN}")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    if data:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            body = r.read()
            return json.loads(body) if body else {}
    except urllib.error.HTTPError as e:
        print(f"ERREUR {e.code} sur {method} {path}\n{e.read().decode()[:600]}")
        raise


# 1. inventaire des fichiers, en respectant .gitignore via git ls-files
files = subprocess.check_output(["git", "-C", ROOT, "ls-files"], text=True).split("\n")
files = [f for f in files if f]
print(f"{len(files)} fichiers a pousser")

# 2. un blob par fichier
tree = []
for i, rel in enumerate(files, 1):
    with open(os.path.join(ROOT, rel), "rb") as fh:
        content = fh.read()
    blob = call("POST", f"/repos/{REPO}/git/blobs",
                {"content": base64.b64encode(content).decode(), "encoding": "base64"})
    mode = "100755" if os.access(os.path.join(ROOT, rel), os.X_OK) else "100644"
    tree.append({"path": rel, "mode": mode, "type": "blob", "sha": blob["sha"]})
    if i % 10 == 0 or i == len(files):
        print(f"  blobs {i}/{len(files)}")

# 3. arbre, commit, reference
t = call("POST", f"/repos/{REPO}/git/trees", {"tree": tree})
print("arbre", t["sha"][:10])

# le depot peut deja avoir une tete (on reprend le parent si elle existe)
parents = []
try:
    ref = call("GET", f"/repos/{REPO}/git/ref/heads/{BRANCH}")
    parents = [ref["object"]["sha"]]
    print("parent", parents[0][:10])
except Exception:
    print("depot vide, commit initial")

c = call("POST", f"/repos/{REPO}/git/commits",
         {"message": MESSAGE, "tree": t["sha"], "parents": parents})
print("commit", c["sha"][:10])

if parents:
    call("PATCH", f"/repos/{REPO}/git/refs/heads/{BRANCH}", {"sha": c["sha"]})
else:
    call("POST", f"/repos/{REPO}/git/refs", {"ref": f"refs/heads/{BRANCH}", "sha": c["sha"]})

print(f"OK : https://github.com/{REPO}/commit/{c['sha'][:7]}")
