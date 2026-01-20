# Résultats des analyses

Ce document présente les principaux enseignements tirés de l'analyse des données de ventes.

## Contexte

Nous avons analysé 530 104 transactions d'un commerce en ligne britannique, couvrant la période de décembre 2010 à décembre 2011. L'objectif était de mieux comprendre le comportement d'achat, identifier les produits et clients clés, et repérer les tendances temporelles.

---

## Indicateurs clés

| Métrique | Valeur |
|----------|--------|
| Chiffre d'affaires | 10 666 685 £ |
| Nombre de commandes | 19 960 |
| Clients uniques | 4 338 |
| Panier moyen | 534 £ |
| CA moyen par client | 2 459 £ |

Le panier moyen relativement élevé suggère une activité orientée B2B (vente en gros) plutôt qu'un commerce de détail classique.

---

## Répartition géographique

Sans surprise, le Royaume-Uni représente la quasi-totalité du chiffre d'affaires (environ 85 %). Les marchés européens comme les Pays-Bas, l'Irlande, l'Allemagne et la France arrivent ensuite, mais avec des volumes nettement plus modestes.

| Pays | CA (£) |
|------|--------|
| United Kingdom | 9 025 222 |
| Netherlands | 285 446 |
| EIRE | 283 454 |
| Germany | 228 867 |
| France | 209 715 |

Ces chiffres montrent qu'il y a probablement une marge de progression à l'international, notamment en travaillant sur les frais de livraison ou en proposant des offres dédiées.

---

## Produits les plus vendus

| Référence | Description | CA (£) | Quantité |
|-----------|-------------|--------|----------|
| DOT | DOTCOM POSTAGE | 206 249 | 706 |
| 22423 | REGENCY CAKESTAND 3 TIER | 174 485 | 13 879 |
| 23843 | PAPER CRAFT, LITTLE BIRDIE | 168 470 | 80 995 |
| 85123A | WHITE HANGING HEART T-LIGHT HOLDER | 104 519 | 37 660 |
| 47566 | PARTY BUNTING | 99 504 | 18 295 |

À noter : "DOTCOM POSTAGE" correspond aux frais de port facturés, ce n'est pas un produit à proprement parler. Les vrais best-sellers sont des articles de décoration et d'artisanat.

---

## Meilleurs clients

| Client | CA (£) | Commandes |
|--------|--------|-----------|
| 14646 | 280 206 | 73 |
| 18102 | 259 657 | 60 |
| 17450 | 194 551 | 46 |
| 16446 | 168 473 | 2 |
| 14911 | 143 825 | 201 |

Le client 14911 se distingue par sa fréquence d'achat exceptionnelle (201 commandes sur la période). À l'inverse, le client 16446 a généré un CA important en seulement 2 commandes, ce qui peut indiquer un achat ponctuel ou un profil de grossiste occasionnel.

---

## Évolution dans le temps

### Par mois

Le CA connaît une progression marquée à l'automne, avec un pic en novembre 2011 (environ 1,5 M£). Décembre affiche une baisse, ce qui peut s'expliquer par l'anticipation des commandes B2B avant les fêtes.

| Période | CA (£) |
|---------|--------|
| 2010-12 | 823 746 |
| 2011-01 | 691 365 |
| 2011-02 | 523 632 |
| 2011-09 | 1 058 590 |
| 2011-10 | 1 154 979 |
| 2011-11 | 1 509 496 |
| 2011-12 | 638 793 |

### Par jour de la semaine

Le jeudi et le mardi sont les jours les plus actifs. On remarque qu'aucune vente n'est enregistrée le samedi, ce qui indique probablement une fermeture des opérations ce jour-là.

| Jour | CA (£) |
|------|--------|
| Monday | 1 779 575 |
| Tuesday | 2 178 633 |
| Wednesday | 1 851 148 |
| Thursday | 2 203 161 |
| Friday | 1 840 340 |
| Saturday | 0 |
| Sunday | 813 828 |

### Par heure

L'essentiel de l'activité se concentre entre 10h et 15h, avec un pic autour de 10h et 12h. Les créneaux matinaux (avant 9h) et de fin de journée restent marginaux.

---

## Ce qu'on peut en retenir

1. **Clientèle B2B** : le panier moyen élevé et les quantités commandées pointent vers une activité de vente en gros.

2. **Dépendance au marché UK** : 85 % du CA provient du Royaume-Uni. L'expansion internationale pourrait être un levier de croissance.

3. **Saisonnalité marquée** : les mois de septembre à novembre concentrent les meilleures performances. Il serait pertinent de préparer les stocks et les campagnes marketing en amont.

4. **Concentration client** : quelques comptes génèrent une part significative du CA. Un programme de fidélisation ciblé pourrait sécuriser ce revenu.

5. **Samedi inactif** : à confirmer s'il s'agit d'une politique volontaire ou d'un manque à gagner.

---

## Prochaines étapes

- Segmenter les clients (analyse RFM) pour adapter les actions commerciales
- Analyser les retours produits (lignes avec quantités négatives)
- Construire un dashboard interactif pour suivre ces indicateurs
