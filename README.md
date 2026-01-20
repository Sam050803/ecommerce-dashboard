# E-commerce Analytics Dashboard

[![Streamlit](https://img.shields.io/badge/Streamlit-Online-brightgreen)](https://4obfdhcbx64kebwc6cnt3v.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Deploy%C3%A9-success)](https://4obfdhcbx64kebwc6cnt3v.streamlit.app/)

Dashboard interactif Streamlit pour analyser les ventes d’un e-commerce britannique (Online Retail). Le projet couvre l’exploration, le nettoyage, l’analyse métier et la visualisation des insights clés.

## 🚀 Démo en ligne

Lien Streamlit Cloud : https://4obfdhcbx64kebwc6cnt3v.streamlit.app/

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

## � Dataset

**Online Retail Dataset** — e-commerce UK

- Période : 01/12/2010 → 09/12/2011
# E-commerce Analytics Dashboard

[![Streamlit](https://img.shields.io/badge/Streamlit-Live%20Demo-brightgreen)](https://4obfdhcbx64kebwc6cnt3v.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)

Un tableau de bord Streamlit pour analyser les ventes de l’Online Retail Dataset (UK, 2010–2011). Le projet couvre l’exploration, le nettoyage, l’analyse et la visualisation de métriques clés pour des décisions métier.

## Démo

- Application en ligne : https://4obfdhcbx64kebwc6cnt3v.streamlit.app/
- (Option) Démonstration vidéo : lien à ajouter (YouTube/LinkedIn). Vous pouvez enregistrer une courte capture avec QuickTime (macOS) ou un outil équivalent.

## Objectifs et périmètre

- Calcul et suivi des KPIs (CA, transactions, clients, panier moyen)
- Identification des pays/produits/clients les plus rentables
- Analyse temporelle (mensuelle, journalière, horaire)
- Filtrage interactif et export des données sélectionnées

## Fonctionnalités principales

- Filtres dynamiques (pays, période, montant minimum, top N)
- 7 graphiques interactifs (Plotly)
- Thème sombre optimisé pour la lisibilité
- Export CSV des données filtrées

## Dataset

Online Retail Dataset (UK e-commerce)

- Période : 01/12/2010 → 09/12/2011
- Lignes initiales : 541 909
- Produits uniques : 4 000+
- Pays couverts : 38
- Colonnes : InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country

Source : [Kaggle](https://www.kaggle.com/datasets/ulrikthygepedersen/online-retail-dataset)

## Installation

### Prérequis

- Python 3.8+
- pip ou conda

### Étapes

```bash
# Cloner le repository
git clone https://github.com/Sam050803/ecommerce-dashboard.git
cd ecommerce-dashboard

# Créer et activer l’environnement
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

## Structure du projet

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

## Insights clés (exemples)

- CA total ≈ £10.7M
- ~20k transactions uniques
- ~4.3k clients identifiés
- Panier moyen ≈ £536
- Pic de vente en novembre 2011
- Forte concentration sur UK

## Visualisations

- KPIs globales
- CA par pays (Top 10)
- Évolution mensuelle du CA
- Top produits par CA
- Top clients par CA
- Distribution des montants par transaction
- CA par jour de la semaine
- CA par heure

## Captures d’écran

Ajoutez vos captures pour illustrer le dashboard :

- [images/dashboard_overview.png](images/dashboard_overview.png)
- [images/dashboard_time.png](images/dashboard_time.png)
- [images/dashboard_export.png](images/dashboard_export.png)

## Déploiement

Déployé sur Streamlit Community Cloud. Pour reproduire :

1. Aller sur share.streamlit.io
2. Connecter votre compte GitHub
3. Créer une app et pointer vers ce dépôt et app.py

## État du projet

- [x] Exploration et nettoyage
- [x] Analyses et visualisations
- [x] Dashboard interactif
- [x] Déploiement Community Cloud

## Auteur

Seyyid-Aassuf — Développeur Data & IA

LinkedIn : https://www.linkedin.com/in/seyyid-aassuf-mamadou-96bb27374
GitHub : https://github.com/Sam050803

Dernière mise à jour : 21/01/2026
