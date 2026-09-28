# Brand — Jolies Pièces

Sources de fabrication des visuels de marque. **Dossier interne, exclu du repo public** (`.gitignore`).

| Fichier | Rôle |
|---|---|
| `logo-source.png` | Logo fourni par Charlie le 2026-09-25 (Anton noir, deux lignes) |
| `logo-trace.svg` | Vectorisation potrace du logo, base des SVG de `static/images/` |
| `make_brand.py` | Génère favicons, icônes PWA, logo carré et image de partage `og-jolies-pieces.jpg` à partir du logo |
| `anton.ttf`, `yellowtail.ttf` | Polices Google Fonts (licence OFL) utilisées par le script |
| `credits-visuels.json` | Crédits Pexels des 15 visuels du thème (id, photographe, alt d'origine) |

Régénérer : `cd brand && python3 make_brand.py`

Les avatars des auteurs sont des SVG plats écrits directement dans `static/images/auteurs/`.
