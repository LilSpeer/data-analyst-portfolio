import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.zeldadungeon.net/wiki/Tears_of_the_Kingdom_Materials'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'https://www.google.com/'
}

session = requests.Session()
session.headers.update(headers)
response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table',{'class': 'wikitable'})

headers = []
for th in table.find_all('th'):
    headers.append(th.text.strip())

print("Headers found:", headers)

rows = []
for tr in table.find_all('tr')[1:]:
    cells = tr.find_all('td')
    if len(cells) ==0:
        continue

    icon_tag = cells[0].find('img')
    icon_url = icon_tag['src'] if icon_tag else ''

    name = cells[1].text.strip() if len(cells) > 1 else ''

    description = cells[2].text.strip() if len(cells) > 2 else ''

    id_ = cells[3].text.strip() if len(cells) > 3 else ''

    rows.append({
        'Icon URL': icon_url,
        'Name': name,
        'Description': description,
        'ID': id_
    })

df = pd.DataFrame(rows)

df.to_csv('totk_materials.csv', index=False)
df.to_json('totk_materials.json', orient='records')

print("Scraping complete! Files saved: totk_materials.csv, totk_materials.json")