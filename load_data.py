import pandas as pd
import sqlite3

# Load CSV
df = pd.read_csv("dataset/sales.csv", encoding="latin1")

# Create SQLite database
conn = sqlite3.connect("sales.db")

# Save data into SQL table
df.to_sql("sales", conn, if_exists="replace", index=False)

print("Database created successfully!")