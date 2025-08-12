import os
import sqlite3
print(sqlite3.sqlite_version)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

db_path = os.path.join(BASE_DIR, '../data/chinook.db')
queries_path = os.path.join(BASE_DIR, '../scripts/queries.sql')

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print("Connected to the database successfully.")

with open(queries_path, 'r') as file:
    sql_content = file.read()

queries = [q.strip() for q in sql_content.split(';') if q.strip()]

for i, query in enumerate(queries,start=1):
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)
    except sqlite3.Error as e:
        print(f"Error executing query {i}: {e}")

conn.close()