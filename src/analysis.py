from pathlib import Path
import pandas as pd

DATA_PATH = Path("data/processed/clean_data.csv")

def load_clean_data(path: str | Path = DATA_PATH) -> pd.DataFrame:
    path = Path(path)
    df = pd.read_csv(path, dtype={"InvoiceNo": str}, low_memory=False)
    # Vérifier que InvoiceDate est bien en datetime
    if not pd.api.types.is_datetime64_any_dtype(df['InvoiceDate']):
        df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    return df

def compute_kpis(df: pd.DataFrame) -> dict:
    # Filtre clients identifiés pour les métriques liées aux clients
    df_clients = df[df['CustomerID'].notna()]
    
    ca_total = df['TotalPrice'].sum()
    n_transactions = df['InvoiceNo'].nunique()
    n_clients = df_clients['CustomerID'].nunique()
    
    panier_moyen = ca_total / n_transactions if n_transactions > 0 else 0
    ca_par_client = ca_total / n_clients if n_clients > 0 else 0
    
    return {
        'CA Total': ca_total,
        'Nombre de Transactions': n_transactions,
        'Nombre de Clients': n_clients,
        'Panier Moyen': panier_moyen,
        'CA Moyen par Client': ca_par_client
    }

def revenue_by_country(df:pd.DataFrame, top_n:int=10) -> pd.DataFrame:
   
    # Grouper par pays, sommer le TotalPrice. trier par ordre décroissant, limiter top_n       
    result = (
        df.groupby('Country')['TotalPrice']
        .sum()
        .sort_values(ascending=False)
        .head(top_n)
        .reset_index()
    )
    result.columns = ['Country', 'Revenue']
    return result

def top_products(df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    
    # Grouper par StockCode, sommer TotalPrice et Quantity, trier par Revenue décroissant, limiter top_n
    result = (
        df.groupby("StockCode")                        
        .agg(
            Revenue=("TotalPrice", "sum"),             
            Quantity=("Quantity", "sum"),              
            Description=("Description", "first"),    
        )
        .sort_values("Revenue", ascending=False)       
        .head(top_n)                                   
        .reset_index()                                 
    )
    return result[["StockCode", "Description", "Revenue", "Quantity"]] 

def top_customers(df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    # Filtrer les clients identifiés (exclure CustomerID NaN)
    df_clients = df[df["CustomerID"].notna()]
    
    # Grouper par client, agréger les infos
    result = (
        df_clients.groupby("CustomerID")
        .agg(
            Revenue=("TotalPrice", "sum"),           # CA total du client
            Transactions=("InvoiceNo", "nunique"),   # Nombre de factures uniques
        )
        .sort_values("Revenue", ascending=False)
        .head(top_n)
        .reset_index()
    )
    return result

def revenue_by_month(df: pd.DataFrame) -> pd.DataFrame:
    # Agrégation nommée pour Year, Month → Revenue
    result = (
        df.groupby(['Year', 'Month'])
          .agg(Revenue=("TotalPrice", "sum"))
          .reset_index()
          .sort_values(['Year', 'Month'])
    )
    # Colonne 'Period' utile pour affichage/plot : format "YYYY-MM"
    result['Period'] = result['Year'].astype(int).astype(str) + '-' + result['Month'].astype(int).astype(str).str.zfill(2)
    return result

def revenue_by_day_of_week(df: pd.DataFrame) -> pd.DataFrame:
    # Agrégation DayOfWeek + DayName → Revenue (DayName vient du preprocessing)
    result = (
        df.groupby(['DayOfWeek', 'DayName'])
          .agg(Revenue=("TotalPrice", "sum"))
          .reset_index()
          .sort_values('DayOfWeek')
    )
    return result

def revenue_by_hour(df: pd.DataFrame) -> pd.DataFrame:
    # Agrégation nommée : Hour → Revenue
    result = (
        df.groupby('Hour')
          .agg(Revenue=("TotalPrice", "sum"))
          .reset_index()
          .sort_values('Hour')
    )
    return result

if __name__ == "__main__":
    df = load_clean_data()
    print(df.shape)
    print(df.head())
    
    kpis = compute_kpis(df)
    print(kpis)
    
    print("\nTop 10 Pays par CA:")
    print(revenue_by_country(df, top_n=10))
    
    print("\nTop 10 Produits par CA:")
    print(top_products(df, top_n=10))
    
    print("\nTop 10 Clients par CA:")
    print(top_customers(df, top_n=10))
    
    print("\nRevenu par mois:")
    print(revenue_by_month(df))
    
    print("\nRevenu par jour de la semaine:")
    print(revenue_by_day_of_week(df))
    
    print("\nRevenu par heure:")
    print(revenue_by_hour(df))