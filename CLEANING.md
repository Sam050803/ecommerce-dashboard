# Documentation du Nettoyage des Données

## Dataset source

- **Nom** : Online Retail Dataset
- **Source** : Kaggle
- **Période** : 01/12/2010 - 09/12/2011
- **Lignes initiales** : 541 909
- **Colonnes initiales** : 8

## Problèmes détectés

1. **Quantités négatives** : 10 624 lignes (retours ou erreurs)
2. **Prix invalides** : 2 517 lignes (UnitPrice ≤ 0)
3. **CustomerID manquants** : 135 080 lignes (25%)
4. **Descriptions manquantes** : 1 454 lignes
5. **Format de date** : InvoiceDate en texte
6. **Données non standardisées** : espaces, casse incohérente

## Actions de nettoyage

### 1. Suppression des transactions invalides

- Supprimé : Quantity ≤ 0 (retours, transactions sans sens)
- Supprimé : UnitPrice ≤ 0 (erreurs d'entrée)
- Conservé : CustomerID manquants (utilisés pour l'analyse globale du CA)

Lignes supprimées :
- Quantity < 0 : 10 624
- UnitPrice ≤ 0 : 2 517
- Total supprimé : 11 805 lignes (2.18%)

### 2. Création de nouvelles colonnes

- **TotalPrice** = Quantity × UnitPrice
  - Calcul du montant total par ligne de transaction
  - Utilisé pour les analyses de chiffre d'affaires

### 3. Conversion des types

- **InvoiceDate** : string → datetime
  - Format source : "2010-12-01T08:26:00.000000000"
  - Permet les opérations temporelles (groupby, filtering, tri)

### 4. Extraction de features temporelles

À partir de InvoiceDate, extraction de colonnes pour les analyses temporelles :

- **Year** : année (2010, 2011)
- **Month** : mois (1-12)
- **Day** : jour du mois (1-31)
- **DayOfWeek** : jour de la semaine (0=Lundi, 6=Dimanche)
- **Hour** : heure (0-23)

Utilité :
- Identifier les mois/jours/heures les plus rentables
- Détecter la saisonnalité
- Optimiser le calendrier commercial

### 5. Standardisation du texte

- **Description** : strip (suppression espaces) + uppercase (majuscules)
- **Country** : strip + uppercase

Raison :
- Élimine les doublons dus aux espaces ou variations de casse
- Exemple : "  White Mug  " vs "WHITE MUG" vs "white mug" = un seul produit

## Résultat final

- **Lignes finales** : 530 104 lignes
- **Lignes supprimées** : 11 805 lignes (-2.18%)
- **Colonnes finales** : 14 colonnes
- **Colonnes créées** : 6 nouvelles colonnes
  - TotalPrice, Year, Month, Day, DayOfWeek, Hour
- **Fichier de sortie** : `data/processed/clean_data.csv`

## Statistiques de nettoyage

```
Chargement des données brutes
  Lignes chargées : 541 909
  Colonnes chargées : 8

Avant nettoyage : 541 909 lignes
  - Quantity < 0 : 10 624
  - UnitPrice <= 0 : 2 517

Suppression des transactions invalides
  Après nettoyage : 530 104 lignes
  - Lignes conservées : 530 104 (97.82%)
  - Lignes supprimées : 11 805 (2.18%)

Enrichissement des données
  - Colonne TotalPrice calculée
  - Features temporelles extraites (5 colonnes)
  - Description et Country standardisées

Résultat final
  - Lignes : 530 104
  - Colonnes : 14 (8 initiales + 6 créées)
  - Fichier : data/processed/clean_data.csv
```

## Script de nettoyage

Le nettoyage est automatisé dans `src/preprocessing.py`.

Pour relancer le nettoyage :
```bash
python -m src.preprocessing
```

Output attendu :
```
Chargement : data/raw/online_retail.csv
Chargé 541909 lignes et 8 colonnes depuis data/raw/online_retail.csv
Avant nettoyage : 541909 lignes
  - Quantity < 0 : 10624
  - UnitPrice <= 0 : 2517
Après nettoyage : 530104 lignes
Sauvegardé 530104 lignes et 14 colonnes vers data/processed/clean_data.csv
```

## Colonnes du dataset nettoyé

| Colonne | Type | Description |
|---------|------|-------------|
| InvoiceNo | str | Numéro de facture unique |
| StockCode | str | Code produit |
| Description | str | Libellé du produit (nettoyé) |
| Quantity | int | Quantité commandée |
| InvoiceDate | datetime | Date et heure de la transaction |
| UnitPrice | float | Prix unitaire en livres sterling |
| CustomerID | float | Identifiant client (peut être NaN) |
| Country | str | Pays du client (nettoyé) |
| TotalPrice | float | Montant total (Quantity × UnitPrice) |
| Year | int | Année de la transaction |
| Month | int | Mois (1-12) |
| Day | int | Jour du mois (1-31) |
| DayOfWeek | int | Jour de la semaine (0=Lundi, 6=Dimanche) |
| Hour | int | Heure de la journée (0-23) |
