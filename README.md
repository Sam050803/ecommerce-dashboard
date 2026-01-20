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
├── notebooks/                  # Analyses Jupyter
│   ├── 01_exploration.ipynb    # Exploration et diagnostic initial
│   ├── 02_preprocessing.ipynb  # (À venir)
│   └── 03_analysis.ipynb       # (À venir)
├── src/
│   ├── __init__.py
│   └── preprocessing.py        # Script de nettoyage des données
├── CLEANING.md                 # Documentation complète du nettoyage
├── requirements.txt            # Dépendances Python
└── README.md
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

**Résultat** : 530 104 lignes valides et 14 colonnes enrichies

Pour plus de détails, voir [CLEANING.md](CLEANING.md).

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
- [ ] Analyses exploratoires détaillées
- [ ] Dashboard interactif
- [ ] Déploiement

## Documentation

Voir [CLEANING.md](CLEANING.md) pour la documentation complète du processus de nettoyage.
