# generate_db.py
import sqlite3
import pandas as pd
from pathlib import Path

# Paths
CSV_PATH = Path(__file__).parent / "earnings_final.csv"
DB_PATH = Path(__file__).parent / "stocks_earnings_dates" / "data" / "earnings.db"

# Make sure the folder exists
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

# Read CSV
df = pd.read_csv(CSV_PATH)

# Save to SQLite
with sqlite3.connect(DB_PATH) as conn:
    df.to_sql("earnings", conn, if_exists="replace", index=False)

print(f"✅ Database created at: {DB_PATH.resolve()}")
print(f"   Source CSV: {CSV_PATH.resolve()}")
print(f"   Rows written: {len(df)}")
