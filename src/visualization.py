from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# Style global pour tous les graphiques
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6) # Taille par défaut des figures
plt.rcParams["axes.titlesize"] = 16  # Taille du titre des axes
plt.rcParams["axes.labelsize"] = 13  # Taille des labels des axes

IMAGES_DIR = Path("images")
IMAGES_DIR.mkdir(parents=True, exist_ok=True)

DATA_PATH = Path("data/processed/clean_data.csv")

# Fonction utilitaire pour formater les montants
def format_currency(value):
    """Formate un montant en M£ ou k£"""
    if value >= 1_000_000:
        return f"{value/1_000_000:.1f}M£"
    elif value >= 1_000:
        return f"{value/1_000:.0f}k£"
    else:
        return f"{value:.0f}£"

def load_data(path: str | Path = DATA_PATH) -> pd.DataFrame:
    df = pd.read_csv(path, dtype={"InvoiceNo": str}, low_memory=False)
    if not pd.api.types.is_datetime64_any_dtype(df['InvoiceDate']):
        df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    return df
    
def plot_revenue_by_country(df: pd.DataFrame, top_n: int = 10, filename: str = "revenue_by_country.png"):
    data = (
        df.groupby('Country')['TotalPrice']
        .sum()
        .sort_values(ascending=False)
        .head(top_n)
        .reset_index()
    )
    
    # Calculer pourcentage UK
    total_ca = df['TotalPrice'].sum()
    uk_ca = data[data['Country'] == 'UNITED KINGDOM']['TotalPrice'].values[0] if len(data[data['Country'] == 'UNITED KINGDOM']) > 0 else 0
    uk_pct = (uk_ca / total_ca) * 100
    
    plt.figure()
    ax = sns.barplot(data=data, x='Country', y='TotalPrice', palette='Blues_d')
    ax.set_title(f'Top {top_n} Pays par CA\n(UK représente {uk_pct:.1f}% du CA total)', fontsize=14)
    ax.set_xlabel('Pays')
    ax.set_ylabel('Chiffre d\'Affaires (£)')
    
    # Formater les valeurs sur l'axe Y
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: format_currency(x)))
    
    plt.xticks(rotation=30, ha='right')
    plt.tight_layout()
    plt.savefig(IMAGES_DIR / filename, dpi=300, bbox_inches='tight')
    plt.close()
    
def plot_monthly_revenue(df: pd.DataFrame, filename: str = "revenue_by_month.png"):
    if "Period" not in df.columns:
        df["Period"] = df["InvoiceDate"].dt.to_period("M").astype(str)
    data = (
        df.groupby("Period")["TotalPrice"]
          .sum()
          .reset_index()
          .sort_values("Period")
    )
    
    # Identifier le mois pic
    max_month = data.loc[data['TotalPrice'].idxmax(), 'Period']
    max_value = data['TotalPrice'].max()
    
    plt.figure()
    ax = sns.lineplot(data=data, x="Period", y="TotalPrice", marker="o", linewidth=2.5, markersize=8)
    ax.set_title("Évolution mensuelle du CA\n(Pic en novembre 2011)", fontsize=14)
    ax.set_xlabel("Période (YYYY-MM)")
    ax.set_ylabel("Chiffre d'affaires (£)")
    
    # Formater l'axe Y
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: format_currency(x)))
    
    # Annoter le pic
    max_idx = data[data['Period'] == max_month].index[0]
    ax.annotate(f'Pic: {format_currency(max_value)}', 
                xy=(max_idx, max_value), 
                xytext=(max_idx-1, max_value*1.1),
                arrowprops=dict(arrowstyle='->', color='red'),
                fontsize=10, color='red')
    
    plt.xticks(rotation=45, ha="right")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig(IMAGES_DIR / filename, dpi=300, bbox_inches="tight")
    plt.close()
    
def plot_top_products(df: pd.DataFrame, top_n: int = 10, filename: str = "top_products.png"):
    data = (
        df.groupby(["StockCode", "Description"])["TotalPrice"]
          .sum()
          .reset_index()
          .sort_values("TotalPrice", ascending=False)
          .head(top_n)
    )
    plt.figure(figsize=(10, 7))
    ax = sns.barplot(data=data, y="Description", x="TotalPrice", palette="Greens_r")
    ax.set_title(f"Top {top_n} produits par CA", fontsize=14)
    ax.set_xlabel("Chiffre d'affaires (£)")
    ax.set_ylabel("Produit")
    
    # Formater l'axe X
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: format_currency(x)))
    
    plt.tight_layout()
    plt.savefig(IMAGES_DIR / filename, dpi=300, bbox_inches="tight")
    plt.close()
    
def plot_transaction_distribution(df: pd.DataFrame, filename: str = "transaction_distribution.png"):
    # Grouper par InvoiceNo pour avoir le montant total par facture (vraie transaction)
    transactions = df.groupby("InvoiceNo")["TotalPrice"].sum()
    mean_val = transactions.mean()
    median_val = transactions.median()
    
    # Calculer le 95e percentile pour limiter l'axe X intelligemment
    percentile_95 = transactions.quantile(0.95)
    
    plt.figure()
    ax = sns.histplot(transactions, bins=50, color="#4C72B0", alpha=0.8)
    ax.axvline(mean_val, color="red", linestyle="--", linewidth=2, label=f"Moyenne: {format_currency(mean_val)}")
    ax.axvline(median_val, color="orange", linestyle="-.", linewidth=2, label=f"Médiane: {format_currency(median_val)}")
    ax.set_title("Distribution des montants par transaction (facture)\n(Montant total par commande - 95% des transactions)", fontsize=14)
    ax.set_xlabel("Montant (£)")
    ax.set_ylabel("Fréquence")
    
    # Limiter l'axe X au 95e percentile pour mieux voir la distribution principale
    ax.set_xlim(0, min(25000, percentile_95 * 1.1))
    
    # Formater l'axe X
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: format_currency(x)))
    
    ax.legend()
    plt.tight_layout()
    plt.savefig(IMAGES_DIR / filename, dpi=300, bbox_inches="tight")
    plt.close() 
    
def plot_revenue_by_weekday(df: pd.DataFrame, filename: str = "revenue_by_weekday.png"):
    order = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
    data = (
        df.groupby("DayName")["TotalPrice"]
          .sum()
          .reset_index()
    )
    data["DayName"] = pd.Categorical(data["DayName"], categories=order, ordered=True)
    data = data.sort_values("DayName")
    
    plt.figure()
    ax = sns.barplot(data=data, x="DayName", y="TotalPrice", palette="Oranges")
    ax.set_title("CA par jour de la semaine\n(Samedi : 0£ - fermeture confirmée)", fontsize=14)
    ax.set_xlabel("Jour")
    ax.set_ylabel("Chiffre d'affaires (£)")
    
    # Formater l'axe Y
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: format_currency(x)))
    
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(IMAGES_DIR / filename, dpi=300, bbox_inches="tight")
    plt.close()
    
def plot_revenue_by_hour(df: pd.DataFrame, filename: str = "revenue_by_hour.png"):
    data = (
        df.groupby("Hour")["TotalPrice"]
          .sum()
          .reset_index()
          .sort_values("Hour")
    )
    plt.figure()
    ax = sns.barplot(data=data, x="Hour", y="TotalPrice", palette="Reds")
    ax.set_title("CA par heure de la journée\n(Pic d'activité : 10h-15h)", fontsize=14)
    ax.set_xlabel("Heure")
    ax.set_ylabel("Chiffre d'affaires (£)")
    
    # Formater l'axe Y
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: format_currency(x)))
    
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(IMAGES_DIR / filename, dpi=300, bbox_inches="tight")
    plt.close()

def plot_kpis(df: pd.DataFrame, filename: str = "kpis_overview.png"):
    """Affiche les KPIs principaux en grand format"""
    df_clients = df[df['CustomerID'].notna()]
    
    ca_total = df['TotalPrice'].sum()
    n_transactions = df['InvoiceNo'].nunique()
    n_clients = df_clients['CustomerID'].nunique()
    panier_moyen = ca_total / n_transactions if n_transactions > 0 else 0
    ca_par_client = ca_total / n_clients if n_clients > 0 else 0
    
    fig, axes = plt.subplots(2, 3, figsize=(14, 8))
    fig.suptitle("Indicateurs Clés de Performance (KPIs)", fontsize=18, fontweight='bold')
    
    kpis = [
        ("CA Total", ca_total, "#2E86AB", True),
        ("Transactions", n_transactions, "#A23B72", False),
        ("Clients", n_clients, "#F18F01", False),
        ("Panier Moyen", panier_moyen, "#C73E1D", True),
        ("CA / Client", ca_par_client, "#6A994E", True),
        ("Lignes traitées", len(df), "#BC4B51", False)
    ]
    
    for idx, (label, value, color, is_currency) in enumerate(kpis):
        row, col = idx // 3, idx % 3
        ax = axes[row, col]
        ax.axis('off')
        
        # Format selon type
        if is_currency:
            display_val = format_currency(value)
        else:
            display_val = f"{int(value):,}".replace(',', ' ')
        
        ax.text(0.5, 0.6, display_val, 
                ha='center', va='center', 
                fontsize=28, fontweight='bold', color=color)
        ax.text(0.5, 0.3, label, 
                ha='center', va='center', 
                fontsize=14, color='gray')
    
    plt.tight_layout()
    plt.savefig(IMAGES_DIR / filename, dpi=300, bbox_inches='tight')
    plt.close()

def plot_top_customers(df: pd.DataFrame, top_n: int = 10, filename: str = "top_customers.png"):
    """Graphique des meilleurs clients"""
    df_clients = df[df["CustomerID"].notna()]
    
    data = (
        df_clients.groupby("CustomerID")
        .agg(
            Revenue=("TotalPrice", "sum"),
            Transactions=("InvoiceNo", "nunique"),
        )
        .sort_values("Revenue", ascending=False)
        .head(top_n)
        .reset_index()
    )
    
    # Créer label avec ID + nb transactions
    data['Label'] = data.apply(lambda x: f"Client {int(x['CustomerID'])} ({int(x['Transactions'])} cmds)", axis=1)
    
    plt.figure(figsize=(10, 7))
    ax = sns.barplot(data=data, y="Label", x="Revenue", palette="Purples_r")
    ax.set_title(f"Top {top_n} clients par CA\n(avec nombre de commandes)", fontsize=14)
    ax.set_xlabel("Chiffre d'affaires (£)")
    ax.set_ylabel("Client")
    
    # Formater l'axe X
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: format_currency(x)))
    
    plt.tight_layout()
    plt.savefig(IMAGES_DIR / filename, dpi=300, bbox_inches="tight")
    plt.close()
    
def generate_all_charts():
    df = load_data()
    print("Génération des graphiques...")
    plot_kpis(df)
    print("✓ KPIs overview")
    plot_revenue_by_country(df)
    print("✓ CA par pays")
    plot_monthly_revenue(df)
    print("✓ Évolution mensuelle")
    plot_top_products(df)
    print("✓ Top produits")
    plot_top_customers(df)
    print("✓ Top clients")
    plot_transaction_distribution(df)
    print("✓ Distribution transactions")
    plot_revenue_by_weekday(df)
    print("✓ CA par jour")
    plot_revenue_by_hour(df)
    print("✓ CA par heure")
    print(f"\n🎉 8 graphiques enregistrés dans {IMAGES_DIR.resolve()}")
    
if __name__ == "__main__":
    generate_all_charts()