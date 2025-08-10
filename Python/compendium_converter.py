import pandas as pd

with open(r'Python\hyrule_compendium.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

tables = pd.read_html(html_content, attrs={'class': 'wikitable'})

print(f"Found {len(tables)} tables")

for i, table in enumerate(tables):
    print(f"\nTable {i+1} preview:")
    print(table.head(3))
