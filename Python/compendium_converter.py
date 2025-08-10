from bs4 import BeautifulSoup
import pandas as pd

with open(r'Python\hyrule_compendium.html') as f:
    soup = BeautifulSoup(f, 'html.parser')

tables_html = soup.find_all('table', class_='wikitable')
print(f"BeautifulSoup found {len(tables_html)} tables")

dfs = []
for idx, table in enumerate(tables_html):
    # Convert the single table HTML back to string and parse with pandas
    df = pd.read_html(str(table))[0]
    dfs.append(df)
    print(f"Table {idx+1} shape: {df.shape}")

# Now dfs is a list of DataFrames, one per table
