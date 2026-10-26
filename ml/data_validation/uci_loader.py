"""
Loads the UCI Online Retail dataset from data/raw/Online Retail.xlsx.

Source: UCI Machine Learning Repository — "Online Retail"
        (Daqing Chen, Sai Liang Sain, Kun Guo)
License/use: research & educational (see dataset page).
This module does NOT download — the file must be placed manually.

Rows ~541,909. Known issues handled downstream in clean_uci.py:
  - ~135,080 rows missing CustomerID
  - ~5,268 duplicate rows
  - InvoiceNo starting with 'C' = cancellation
  - Negative or zero Quantity / UnitPrice
"""
from pathlib import Path
import pandas as pd

RAW_PATH = Path("data/raw/Online Retail.xlsx")

EXPECTED_COLUMNS = [
    "InvoiceNo", "StockCode", "Description", "Quantity",
    "InvoiceDate", "UnitPrice", "CustomerID", "Country",
]

def load_raw() -> pd.DataFrame:
    if not RAW_PATH.exists():
        raise FileNotFoundError(
            f"Expected UCI file at {RAW_PATH}. "
            "Download 'Online Retail.xlsx' from the UCI ML Repository "
            "and place it in data/raw/."
        )
    df = pd.read_excel(RAW_PATH)
    missing = [c for c in EXPECTED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"UCI file missing expected columns: {missing}")
    return df

def schema_report(df: pd.DataFrame) -> dict:
    return {
        "rows": int(len(df)),
        "columns": list(df.columns),
        "missing_customer_id": int(df["CustomerID"].isna().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
        "cancellations": int(df["InvoiceNo"].astype(str).str.startswith("C").sum()),
        "negative_quantity": int((df["Quantity"] < 0).sum()),
        "nonpositive_unitprice": int((df["UnitPrice"] <= 0).sum()),
        "date_min": str(df["InvoiceDate"].min()),
        "date_max": str(df["InvoiceDate"].max()),
    }