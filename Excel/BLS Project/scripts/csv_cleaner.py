import pandas as pd
import glob

path = 'Excel/BLS Project/data/'
all_files = glob.glob(path + "*.csv")

df_list = [pd.read_csv(file, encoding='utf-8') for file in all_files]
df = pd.concat(df_list, ignore_index=True)

print(df.head())
print(df.columns)

df.columns = df.columns.str.strip()

df['Year'] = df['Year'].astype(int)

columns_to_keep = ["Area Name", "Year", "Month", "Labor Force", "Employment", "Unemployment", "Unemployment Rate"]
df = df[columns_to_keep]

df = df[df["Year"] >= 2015] #Filter for last 10 years (2015-2025)

df.to_csv('Excel/BLS Project/data/cleaned_data.csv', index=False)
print("Data cleaned and saved to 'cleaned_data.csv'.")