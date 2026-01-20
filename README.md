# E-commerce Analytics Dashboard

Dashboard interactif Streamlit pour analyser les ventes d’un e-commerce britannique (Online Retail). Le projet couvre l’exploration, le nettoyage, l’analyse métier et la visualisation des insights clés.

## 🚀 Démo en ligne

Lien Streamlit Cloud : à compléter après déploiement.

## 👀 Aperçu

Ce projet s’appuie sur l’Online Retail Dataset (Kaggle) contenant plus de 500 000 transactions réelles (2010–2011). L’objectif est de produire un tableau de bord décisionnel clair et actionnable.

Principales analyses :

- KPI globaux (CA, transactions, clients, panier moyen)
- Top pays / produits / clients
- Évolution temporelle et saisonnalité
- Répartition horaire et par jour

## ✨ Fonctionnalités du dashboard

- Filtres dynamiques (pays, période, montant minimum, top N)
- KPIs et comparaisons clés
- 7 graphiques interactifs Plotly
- Thème sombre optimisé lisibilité
- Export des données filtrées

## 📦 Dataset

**Online Retail Dataset** — e-commerce UK

- Période : 01/12/2010 → 09/12/2011
- Lignes initiales : 541 909
- Produits uniques : 4 000+
- Pays couverts : 38
- Colonnes : InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country

Source : [Kaggle](https://www.kaggle.com/datasets/ulrikthygepedersen/online-retail-dataset)

## ⚡ Démarrage rapide

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

### Lancer le dashboard

```bash
streamlit run app.py
```

### Générer les données nettoyées et graphiques (optionnel)

```bash
python -m src.preprocessing
python -m src.visualization
```

Les graphiques sont enregistrés dans le dossier [images/](images/) et les données nettoyées dans [data/processed/](data/processed/).

## 🗂️ Structure du projet

```
ecommerce-dashboard/
├── app.py                       # Dashboard Streamlit
├── data/
│   ├── raw/                     # Données brutes (non versionnées)
│   └── processed/               # Données nettoyées
│       ├── clean_data.csv       # Dataset complet (local)
│       └── clean_data_sample.csv# Sample pour déploiement
├── images/                      # Graphiques exportés
├── notebooks/                   # Analyses Jupyter
├── src/                         # Scripts de préparation/analyses
├── .streamlit/                  # Configuration Streamlit Cloud
├── ANALYSES.md
├── CLEANING.md
├── requirements.txt
└── README.md
```

## 📈 Insights clés (exemples)

- CA total ≈ £10.7M
- ~20k transactions uniques
- ~4.3k clients identifiés
- Panier moyen ≈ £536
- Pic de vente en novembre 2011
- Forte concentration sur UK

## 🧪 Visualisations générées

- KPIs globales
- CA par pays (Top 10)
- Évolution mensuelle du CA
- Top produits par CA
- Top clients par CA
- Distribution des montants par transaction
- CA par jour de la semaine
- CA par heure

## ☁️ Déploiement Streamlit Cloud

1. Aller sur [share.streamlit.io](https://share.streamlit.io)
2. Connecter GitHub
3. Créer une nouvelle app
4. Sélectionner ce repository et [app.py](app.py)

## ✅ État du projet

- [x] Exploration initiale
- [x] Nettoyage et préparation
- [x] Analyses métier
- [x] Visualisations
- [x] Dashboard interactif
- [ ] Déploiement Streamlit Cloud

## 📚 Documentation

- [CLEANING.md](CLEANING.md) : processus de nettoyage
- [ANALYSES.md](ANALYSES.md) : synthèse des analyses

## 👤 Auteur

Seyyid-Aassuf - Developpeur Data et IA

LinkedIn : https://www.linkedin.com/in/seyyid-aassuf-mamadou-96bb27374
GitHub : https://github.com/Sam050803
