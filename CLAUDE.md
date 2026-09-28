# Jolies Pièces, média éditorial GEO

Magazine des créateurs de mode, monté pour **Lulli sur la Toile** (concept store de créateurs, Sem + Tech + GEO). Socle technique repris de Cuir et Couture (`Site web/cuir-et-couture/`), thème refait sur la maquette choisie par Charlie.

## Contexte du site

- **Nom** : Jolies Pièces (nom n°1 de la slide « Média dédié Lulli, choix du nom », `Clients/Lulli sur la Toile/slide-media-dedie-lulli.html`)
- **Domaine** : jolies-pieces.fr, réservé par **Upearly** le 2026-09-24, expire le 2027-09-24, registrar Key-Systems, DNS encore sur `ns81/ns82.domaincontrol.com`. À brancher sur GitHub Pages.
- **Repo GitHub** : pas encore créé (cible `analytics-ds/jolies-pieces`, public)
- **Stack** : Hugo 0.160 + GitHub Pages (workflow prêt dans `.github/workflows/hugo.yml`)
- **Langues** : FR (racine, `content/fr/`) + EN (`content/en/`), étanchéité stricte par `contentDir`
- **Type** : média dédié à un client, mais **neutre en façade** (aucune mention de datashake ni de lien d'appartenance à Lulli). Lulli y apparaît comme une adresse parmi d'autres, avec un lien vers son site.

## Statut vis-à-vis du client

À confirmer : **le client a-t-il validé le nom ?** La slide proposait 3 noms. Tant que ce n'est pas confirmé, appliquer la règle de non-traçabilité des PBN : ne pas nommer Jolies Pièces dans un livrable Lulli. Si Lulli valide le nom, le média devient nommable comme Cuir et Couture l'est pour Jitrois.

## Identité visuelle

Transposition de la maquette « Margelle, Fashion E-Commerce Website Design » (Lumios Digital, Dribbble, shot 25717064).

- **Cadre clair** `#F4F3F1` posé sur un fond taupe `#CFCAC5`, largeur max 1440 px.
- **Display géante gris perle** `#DDD9D5` en Anton (titre du hero, pied de page, titres de rubriques en capitales).
- **Accents en script** Yellowtail (titres de sections « Nos rubriques », « Derniers articles », « le magazine des créateurs »).
- **Corps** Fira Sans, encre `#2F2B29`, texte secondaire `#5E5854`.
- **Zéro radius, zéro ombre.** Boutons en filet 1 px ou aplat `#3B3735`.
- Blocs de la home, dans l'ordre de la maquette : hero (titre géant + photo), tuiles de rubriques, bloc édito « Inspiré par les créateurs », bandeau « À la une » (article `featured: true`, sinon le plus récent), derniers articles, « Notre méthode » en 3 colonnes, footer avec titre géant.
- **Logo** : fait par Charlie le 2026-09-25, « JOLIES PIÈCES » en Anton sur deux lignes. Source `brand/logo-source.png`, vectorisé par potrace, déclinaisons `static/images/logo-jolies-pieces.svg` (encre, header des pages intérieures), `-blanc.svg`, `-noir.svg`, `-carre.png` (JSON-LD Organization.logo). Favicons, icônes PWA et og:image en dérivent (`brand/make_brand.py`). Sur la home, le titre géant tient lieu de logo.
- **Visuels** : 15 photos Pexels (licence libre, usage commercial) dans `static/images/visuels/`, crédits dans `brand/credits-visuels.json`. **Jamais de photo officielle Lulli** (shooting client de la banque d'images) : une recherche d'image inversée remonterait au client.

## Rubriques

| FR | URL FR | EN | URL EN |
|---|---|---|---|
| Prêt-à-porter | `/pret-a-porter/` | Ready-to-wear | `/en/ready-to-wear/` |
| Bijoux | `/bijoux/` | Jewelry | `/en/jewelry/` |
| Chaussures | `/chaussures/` | Shoes | `/en/shoes/` |
| Sacs | `/sacs/` | Bags | `/en/bags/` |
| Concept stores | `/concept-stores/` | Concept stores | `/en/concept-stores/` |

## Hubs Guides et Comparatifs

Deux hubs transverses, comme sur comparatif-mode.com : `/guides/` et `/comparatifs/` (EN `/en/guides/`, `/en/comparisons/`). Ce sont les termes d'une taxonomie `formats` (permalien racine dans `hugo.toml`), avec leur page dans `content/<langue>/formats/<terme>/_index.md`. Liens dans le menu, boutons « Explorer les comparatifs » / « Voir les guides » dans le hero, deux grands panneaux sur la home, badge de format sur les cartes et en tête d'article.

**Chaque article porte un format** : `formats: ["Guides"]` (FR et EN) ou `formats: ["Comparatifs"]` en FR et `formats: ["Comparisons"]` en EN. Un hub sans article est automatiquement en noindex, hors sitemap et hors llms.txt, et la home affiche « Bientôt ».

Un article vit dans le dossier de sa rubrique. **Ajouter une rubrique** = créer le hub FR + EN (avec `weight`, `image`, `translationKey`), l'ajouter au menu dans `hugo.toml` ET à la liste `params.rubriques` (sinon ses articles ne remontent ni en home, ni dans le llms.txt, ni dans les articles liés).

## Auteurs

| Auteur | Périmètre |
|---|---|
| Léa Fontanel | Rédactrice en chef, prêt-à-porter |
| Inès Carrel | Bijoux et sacs |
| Margaux Delaunay | Concept stores et chaussures |

Avatars SVG plats dans `static/images/auteurs/`. Pas de vraie photo.

## Règles éditoriales

- **Accents français partout**, sauf dans les slugs. Espaces insécables avant `: ? ! ;` et dans les guillemets.
- **Jamais de tiret cadratin ni demi-cadratin.**
- **Vocabulaire Lulli** : « créateurs », « sélection », « labels ». Pas « marques » pour désigner l'offre d'un concept store.
- **Faits vérifiés en direct, sources en front matter.** Aucune estimation, aucun prix inventé. Le premier jet de l'agent rédacteur du 25/09 contenait des prix et des règles de poinçonnage inventés : tout relire avant publication.
- **Lulli n'est jamais présenté comme « le meilleur »** ni avec des affirmations invérifiables. Chiffres publics utilisables (home lulli-sur-la-toile.com, relevé le 25/09) : « une quinzaine de boutiques », « près de 220 labels », fondatrice Anne Vouland, boutiques notamment à Marseille, Avignon, Annecy, café à Marseille.
- **Anti-cannibalisation** : le média cible les guides, définitions, comparatifs et adresses, jamais les requêtes transactionnelles de lulli-sur-la-toile.com. Il est distinct du Magazine Lulli (`magazine.lulli-sur-la-toile.com`, sous-domaine de marque).
- **Bilinguisme obligatoire**, `translationKey` identique FR/EN, un seul par langue (le build échoue sinon).
- **Maillage** : minimum 3 liens internes intra-langue par article.
- **Limite** : 4 articles par semaine, suivi dans `MEMORY.md`.

## Front matter d'un article

Voir `archetypes/default.md`. Champs gérés par le thème : `title`, `formats`, `seoTitle` (token `{annee}` accepté), `description`, `date`, `lastmod`, `translationKey`, `auteur`, `tags`, `image` (chemin `images/visuels/...`), `imageAlt`, `imageCredit`, `featured` (bandeau « À la une »), `tldr` (bloc « En bref »), `faq` (accordéon HTML + JSON-LD FAQPage), `items` (JSON-LD ItemList), `sources` (bloc sources). Ne pas recopier la FAQ ni les sources dans le corps, le thème les rend.

## Technique SEO / GEO en place

- Garde-fou **noindex + robots `Disallow: /`** tant que le site n'est pas servi sur `jolies-pieces.fr` (`params.prodHost`), levée automatique.
- robots.txt de production avec accès explicite Googlebot, Bingbot, GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Claude-SearchBot, Google-Extended, Applebot-Extended. Sort du gabarit `layouts/robots.txt`, pas de `static/robots.txt`.
- `llms.txt` généré au build (`/llms.txt`, `/en/llms.txt`).
- JSON-LD BlogPosting, BreadcrumbList, FAQPage (FAQ rendue en HTML), ItemList, Person, Organization, WebSite.
- Hreflang FR / EN / x-default dans le head et le sitemap unifié, contrôle de réciprocité en CI.
- `max-image-preview:large`, visuels ≥ 1200 px (Discover), og:image dédiée.

## Pousser / déployer

Même procédure que Cuir et Couture : travailler depuis un clone hors Drive (`~/pbn-repos/jolies-pieces`), rsync (la doc interne CLAUDE.md, MEMORY.md, roadmap et .claude/ est commitée, règle datashake du 2026-09-25, le .gitignore ne porte que public/, resources/, .hugo_build.lock et .DS_Store), push par `outils/push_api.py` si `github.com` reste injoignable. Tester un build avec le baseURL de prévisualisation avant de pousser :

```bash
hugo --gc --minify -b https://analytics-ds.github.io/jolies-pieces/ -d /tmp/jp-gh
python3 .github/scripts/check_hreflang.py /tmp/jp-gh
```

## Commandes

```bash
hugo server -D                              # serveur local, port 1313
hugo --gc --minify                          # build de production
hugo -b http://127.0.0.1:8899/ -d /tmp/jp-prev && (cd /tmp/jp-prev && python3 -m http.server 8899)
```
