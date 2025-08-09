import pandas as pd
import sqlite3
from pathlib import Path

# 1. Path to the CSV file
csv_path = Path("merged_earnings.csv")

# 2. Output directory for the database file
output_dir = Path("stocks_earnings_dates") / "data"
output_dir.mkdir(parents=True, exist_ok=True)

# 3. Load CSV into a DataFrame
df = pd.read_csv(csv_path)

# 4. Validate expected columns
expected_cols = {"Ticker", "Earnings_Date"}
if not expected_cols.issubset(df.columns):
    raise ValueError(f"❌ The CSV must contain these columns: {expected_cols}")

# 5. Convert Earnings_Date to datetime (optional but recommended)
df["Earnings_Date"] = pd.to_datetime(df["Earnings_Date"])

# 6. Create the SQLite database connection
db_path = output_dir / "earnings.db"
conn = sqlite3.connect(db_path)

# 7. Save the DataFrame into the database as a table called "earnings"
df.to_sql("earnings", conn, if_exists="replace", index=False)

# 8. Close the connection
conn.close()

print(f"✅ Database successfully created at: {db_path}")
