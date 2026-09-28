# Jolies Pièces, état d'avancement

Dernière mise à jour : 2026-09-25

## Le projet en une phrase

Média éditorial GEO neutre sur les créateurs de mode (prêt-à-porter, bijoux, chaussures, sacs, concept stores), monté pour Lulli sur la Toile sur `jolies-pieces.fr`, bilingue FR + EN, Hugo + GitHub Pages. Doc complète dans `CLAUDE.md`.

## Ce qui est FAIT

**Socle et design (2026-09-25)**
- Site Hugo complet, thème maison `jolies-pieces` calé sur la maquette Margelle (Dribbble 25717064). Build sans erreur, 56 pages FR, 54 EN.
- Home dans l'ordre de la maquette, hubs de rubrique, article, pages institutionnelles, fiches et index auteurs. Contrôlé en capture desktop 1440 px et mobile 390 px, pas de scroll horizontal.
- 15 visuels Pexels WebP (1,8 Mo), favicons, icônes PWA, og:image, manifest.

**SEO / GEO**
- Garde-fou noindex + robots Disallow hors domaine final, vérifié sur un build en sous-chemin GitHub Pages.
- robots.txt de prod avec les crawlers IA autorisés explicitement, llms.txt FR et EN générés, sitemap unifié avec hreflang.
- JSON-LD valides sur toutes les pages (contrôle par parse), un seul H1 par page, titles 27 à 58 caractères, metas articles 133 à 154.
- Hreflang : 32 pages traduites, toutes réciproques.

**Contenu**
- 5 hubs FR + EN, 3 auteurs FR + EN, pages Le média, Contact, Mentions légales FR + EN.
- 3 articles bilingues : concept store (définition, 10 Corso Como, Colette, Merci, Lulli), plaqué or / vermeil / or massif (CGI art. 551 et annexe III art. 212 A), prêt-à-porter de créateur (Saint Laurent Rive Gauche 1966, FHCM 1945 et 1973). Premier jet par un agent, **réécrits intégralement** après contrôle (prix et règles de poinçonnage inventés, affirmations fausses sur Lulli).

## Ce qui RESTE

Priorité 1, avant mise en ligne
- [ ] **Confirmer que Lulli a validé le nom Jolies Pièces** (conditionne le droit de nommer le média dans les livrables).
- [ ] Valider le design avec Charlie (prévisualisation locale ou GitHub Pages).
- [ ] Compléter les mentions légales (éditeur réel, directeur de la publication, siège) et décider qui porte l'adresse `redaction@jolies-pieces.fr` (boîte à créer).

Priorité 2, mise en ligne
- [ ] Créer le repo `analytics-ds/jolies-pieces` (public), activer Pages en mode Actions, premier déploiement en prévisualisation noindex.
- [ ] Brancher le DNS de jolies-pieces.fr (4 A GitHub Pages) chez Key-Systems, créer `static/CNAME`, poser le custom domain par l'API avec le compte `analytics-ds`, basculer le baseURL du workflow.
- [ ] Propriété Search Console + soumission du sitemap.

Priorité 3, éditorial
- [ ] `roadmap.yaml` d'articles evergreen à partir des 105 prompts Lulli monitorés (clusters bijoux, chaussures, sacs, vêtement, local, comparatifs).
- [ ] Rubriques Chaussures et Sacs encore sans article.
- [ ] **Premier comparatif** pour ouvrir le hub Comparatifs (en noindex tant qu'il est vide).
- [ ] Brancher le média dans la skill `geo-run-lulli` comme levier actif (aujourd'hui noté « à venir »).
- [ ] Réseaux sociaux (Instagram, Pinterest) et `sameAs` dans `hugo.toml`.

## Prochaine action recommandée

Faire valider le design par Charlie, puis créer le repo et déployer la prévisualisation.

## Décisions clés

- **Socle repris de Cuir et Couture** (garde-fous hreflang, noindex auto, llms.txt), thème entièrement refait.
- **Photos Pexels uniquement**, jamais le shooting officiel Lulli, pour ne pas tracer le média jusqu'au client.
- **Rubriques = familles produit + concept stores.** Contrairement au Magazine Lulli (rubriques éditoriales), un média tiers neutre peut couvrir les familles produit sans recopier la boutique.
- **Pas de newsletter** dans le footer de la maquette : pas de backend, un faux formulaire serait trompeur. Remplacé par un lien d'écriture à la rédaction.

## Journal

- **2026-09-25** : hubs Guides et Comparatifs (taxonomie formats, menu, boutons hero, panneaux home). Comparatifs vide, donc noindex jusqu'au premier comparatif.
- **2026-09-25** : logo fourni par Charlie branché (header, favicons, icônes, og:image, JSON-LD).
- **2026-09-25** : création complète du site (design, thème, contenu, contrôles SEO/GEO). Pas encore de repo ni de déploiement.
