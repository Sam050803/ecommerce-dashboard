# E-commerce Dashboard

Analyse complète des données de ventes d'un commerce électronique britannique avec création d'un dashboard interactif.

## À propos

Ce projet analyse l'Online Retail Dataset de Kaggle, qui contient plus de 500 000 transactions d'une entreprise e-commerce basée au Royaume-Uni. L'objectif est d'explorer les données, les nettoyer et créer des visualisations interactives pour extraire des insights métier.

## Démarrage rapide

### Prérequis
- Python 3.8+
- pip ou conda

### Installation

```bash
# Cloner le repository
git clone <repository-url>
cd ecommerce-dashboard

# Créer l'environnement virtuel
python -m venv venv
source venv/bin/activate          # macOS/Linux
# ou
venv\Scripts\activate             # Windows

# Installer les dépendances
pip install -r requirements.txt
```

### Utilisation

**Nettoyer et préparer les données** :
```bash
python -m src.preprocessing
```

Cela génère `data/processed/clean_data.csv` contenant les données traitées et prêtes pour l'analyse.

**Générer les visualisations** :
```bash
python -m src.visualization
```

Cela crée 8 graphiques haute résolution dans le dossier `images/`.

**Explorez les données** :
Ouvrez les notebooks Jupyter dans le dossier `notebooks/` pour des analyses détaillées.

## Structure du projet

```
ecommerce-dashboard/
├── data/
│   ├── raw/                    # Données brutes (source Kaggle)
│   │   └── online_retail.csv
│   └── processed/              # Données nettoyées et traitées
│       └── clean_data.csv
├── images/                     # Graphiques et visualisations
│   ├── kpis_overview.png
│   ├── revenue_by_country.png
│   ├── revenue_by_month.png
│   ├── top_products.png
│   ├── top_customers.png
│   ├── transaction_distribution.png
│   ├── revenue_by_weekday.png
│   └── revenue_by_hour.png
├── notebooks/                  # Analyses Jupyter
│   ├── 01_exploration.ipynb    # Exploration et diagnostic initial
│   └── ...                     # Autres notebooks
├── src/
│   ├── __init__.py
│   ├── preprocessing.py        # Script de nettoyage des données
│   ├── analysis.py             # Analyses métier et KPIs
│   └── visualization.py        # Génération des graphiques
├── CLEANING.md                 # Documentation complète du nettoyage
├── ANALYSES.md                 # Synthèse des résultats et insights
├── requirements.txt            # Dépendances Python
└── README.md                   # Présentation et guide du projet
```

## Dataset

**Online Retail Dataset** - Commerce électronique britannique

- Période : 1er décembre 2010 - 9 décembre 2011 (13 mois)
- Nombre de transactions : 541 909 lignes initiales
- Produits uniques : 4 000+
- Pays couverts : 38
- Colonnes brutes : InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country

Source: [Kaggle](https://www.kaggle.com/datasets/ulrikthygepedersen/online-retail-dataset)

## Processus de nettoyage

Le script `src/preprocessing.py` effectue les transformations suivantes :

1. **Suppression des données invalides**
   - Transactions avec Quantity ≤ 0
   - Transactions avec UnitPrice ≤ 0

2. **Création de nouvelles colonnes**
   - TotalPrice = Quantity × UnitPrice
   - Features temporelles : Year, Month, Day, DayOfWeek, Hour

3. **Standardisation du texte**
   - Description et Country : suppression des espaces superflus, conversion en majuscules

**Résultat** : 530 104 lignes valides et 15 colonnes enrichies

Pour plus de détails, voir [CLEANING.md](CLEANING.md).

## Visualisations

Le script `src/visualization.py` génère 8 graphiques professionnels :

1. **KPIs Overview** : Vue d'ensemble des indicateurs clés (CA, transactions, clients, panier moyen)
2. **CA par pays** : Top 10 pays avec pourcentage UK
3. **Évolution mensuelle** : Courbe du CA avec annotation du pic novembre
4. **Top produits** : 10 produits les plus rentables (barres horizontales)
5. **Top clients** : 10 meilleurs clients avec nombre de commandes
6. **Distribution transactions** : Histogramme des montants par facture (médiane vs moyenne)
7. **CA par jour** : Performance par jour de semaine
8. **CA par heure** : Répartition horaire de l'activité

Tous les graphiques utilisent un formatage intelligent (M£, k£) et des annotations contextuelles.

## Questions métier adressées

- Quel est le chiffre d'affaires total ?
- Quels sont les 10 pays/produits/clients les plus rentables ?
- Comment évoluent les ventes dans le temps ?
- Existe-t-il une saisonnalité ?
- Quel est le panier moyen par commande ?
- Quels produits sont les plus retournés ?

## Technologies

- **Pandas** : manipulation et nettoyage de données
- **NumPy** : calculs numériques
- **Matplotlib/Seaborn** : visualisations statiques
- **Jupyter** : notebooks interactifs
- **Streamlit** : dashboard interactif (à venir)

## État du projet

- [x] Exploration initiale des données
- [x] Nettoyage et préparation
- [x] Analyses métier
- [x] Visualisations
- [ ] Dashboard interactif
- [ ] Déploiement

## Documentation

- [CLEANING.md](CLEANING.md) : processus de nettoyage des données
- [ANALYSES.md](ANALYSES.md) : résultats et insights des analyses
