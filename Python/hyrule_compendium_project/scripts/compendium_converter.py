from bs4 import BeautifulSoup
import pandas as pd

with open(r'Python\hyrule_compendium.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

tables_html = soup.find_all('table', class_='wikitable')
BASE_URL = 'https://www.zeldadungeon.net'

dfs = []

for table_html in tables_html:
    rows = []
    headers = [th.get_text(strip=True) for th in table_html.find_all('th')]

    for tr in table_html.find_all('tr')[1:]: 
        cells = tr.find_all('td')
        if not cells:
            continue
        row = []
        for cell in cells:
            # Check if cell has an image
            img = cell.find('img')
            if img and img.has_attr('src'):
                relative_url = img['src']
                img_url = BASE_URL + relative_url
                row.append(img_url)
            else:
                # Just get the text content
                text = cell.get_text(strip=True)
                row.append(text)
        rows.append(row)

    df = pd.DataFrame(rows, columns=headers)
    dfs.append(df)

# Save all tables separately as csv
for i, df in enumerate(dfs, start=1):
    filename = f'compendium_table_{i}.csv'
    df.to_csv(filename, index=False)
    print(f"Saved {filename}")
