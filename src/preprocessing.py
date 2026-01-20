import pandas as pd
from pathlib import Path

def load_raw_data(path: str | Path) -> pd.DataFrame:
    path = Path(path)
    df = pd.read_csv(path)
    print(f"Chargé {df.shape[0]} lignes et {df.shape[1]} colonnes depuis {path}")
    return df

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    print(f"Avant nettoyage : {df.shape[0]} lignes")
    print(f"  - Quantity < 0 : {(df['Quantity'] < 0).sum()}")
    print(f"  - UnitPrice <= 0 : {(df['UnitPrice'] <= 0).sum()}")
    
    #Supprimer les lignes avec Quantity négatif ou UnitPrice non positif
    df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
    
    # Créer une colonne TotalPrice
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
    print(f"  - TotalPrice calculé exemple : {df['TotalPrice'].head(3).values}")
    
    # Convertir InvoiceDate en datetime
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    print(f"  - InvoiceDate exemple : {df['InvoiceDate'].head(3).values}")
    
    # Extraire les features temporelles (année, mois, jour, jour de la semaine, heure)
    df['Year'] = df['InvoiceDate'].dt.year
    df['Month'] = df['InvoiceDate'].dt.month
    df['Day'] = df['InvoiceDate'].dt.day
    df['DayOfWeek'] = df['InvoiceDate'].dt.dayofweek
    df['Hour'] = df['InvoiceDate'].dt.hour
    print(f"  - Features temporelles extraites (Year, Month, Day, DayOfWeek, Hour)")
    
    print(f"Après nettoyage : {df.shape[0]} lignes")
    
    # Nettoyer la colonne Description
    df['Description'] = df['Description'].str.strip().str.upper()
    df['Country'] = df['Country'].str.strip().str.upper()
    print(f"  - Description et Country nettoyées (trim + uppercase)")
    print(f"Colonnes finales : {df.head(1).to_dict(orient='records')[0].keys()}")
    return df

def save_data(df: pd.DataFrame, path: str | Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    print(f"Sauvegardé {df.shape[0]} lignes et {df.shape[1]} colonnes vers {path}")

if __name__ == "__main__":
    raw_path = Path("data/raw/online_retail.csv")
    processed_path = Path("data/processed/clean_data.csv")
    print(f"Chargement : {raw_path}")
    df_raw = load_raw_data(raw_path)
    df_clean = clean_data(df_raw)
    save_data(df_clean, processed_path)