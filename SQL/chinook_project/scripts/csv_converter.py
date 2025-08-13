import sqlite3
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

db_path = os.path.join(BASE_DIR, '../data/chinook.db')

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print("Connected to the database successfully.")

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print(f"Found {len(tables)} tables. Exporting to CSV...")

for table_name in tables:
    table_name = table_name[0]
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    csv_path = os.path.join(BASE_DIR, f'../data/csv/{table_name}.csv')
    df.to_csv(csv_path, index=False)
    print(f"Exported {table_name} to {csv_path}")

conn.close()
