import pandas as pd
import glob
import os

# Built-in mapping from CA area names to (County, Region)
AREA_TO_COUNTY_REGION = {
    "Anaheim-Santa Ana-Irvine, CA Met Div": ("Orange County", "Southern California"),
    "Los Angeles-Long Beach-Glendale, CA Met Div": ("Los Angeles County", "Southern California"),
    "San Diego-Carlsbad, CA MSA": ("San Diego County", "Southern California"),
    "Oxnard-Thousand Oaks-Ventura, CA MSA": ("Ventura County", "Southern California"),
    "Riverside-San Bernardino-Ontario, CA MSA": ("Riverside County; San Bernardino County", "Inland Empire"),
    "San Francisco-Redwood City-South San Francisco, CA Met Div": ("San Francisco County; San Mateo County", "Bay Area"),
    "Oakland-Hayward-Berkeley, CA Met Div": ("Alameda County; Contra Costa County", "Bay Area"),
    "San Jose-Sunnyvale-Santa Clara, CA MSA": ("Santa Clara County; San Benito County", "Bay Area"),
    "Vallejo-Fairfield, CA MSA": ("Solano County", "Bay Area"),
    "Napa, CA MSA": ("Napa County", "Bay Area"),
    "Santa Rosa-Petaluma, CA MSA": ("Sonoma County", "Bay Area"),
    "Santa Cruz-Watsonville, CA MSA": ("Santa Cruz County", "Central Coast"),
    "Salinas, CA MSA": ("Monterey County", "Central Coast"),
    "San Luis Obispo-Paso Robles-Arroyo Grande, CA MSA": ("San Luis Obispo County", "Central Coast"),
    "Santa Maria-Santa Barbara, CA MSA": ("Santa Barbara County", "Central Coast"),
    "Bakersfield, CA MSA": ("Kern County", "Central Valley"),
    "Fresno, CA MSA": ("Fresno County", "Central Valley"),
    "Hanford-Corcoran, CA MSA": ("Kings County", "Central Valley"),
    "Madera, CA MSA": ("Madera County", "Central Valley"),
    "Merced, CA MSA": ("Merced County", "Central Valley"),
    "Modesto, CA MSA": ("Stanislaus County", "Central Valley"),
    "Stockton-Lodi, CA MSA": ("San Joaquin County", "Central Valley"),
    "Visalia-Porterville, CA MSA": ("Tulare County", "Central Valley"),
    "Yuba City, CA MSA": ("Sutter County; Yuba County", "Northern California"),
    "Chico, CA MSA": ("Butte County", "Northern California"),
    "Redding, CA MSA": ("Shasta County", "Northern California"),
    "Sacramento-Roseville-Arden-Arcade, CA MSA": ("Sacramento County; Placer County; El Dorado County; Yolo County", "Northern California"),
}


def load_area_mapping(optional_csv_path: str) -> dict:
    mapping = dict(AREA_TO_COUNTY_REGION)
    if optional_csv_path and os.path.exists(optional_csv_path):
        try:
            custom_df = pd.read_csv(optional_csv_path)
            if {"Area Name", "County", "Region"}.issubset(set(custom_df.columns)):
                for _, row in custom_df.iterrows():
                    area = str(row["Area Name"]).strip()
                    county = str(row["County"]).strip()
                    region = str(row["Region"]).strip()
                    mapping[area] = (county, region)
        except Exception as e:
            print(f"Warning: Failed to read custom area mapping CSV at {optional_csv_path}: {e}")
    return mapping


def map_county_region(area_name: str, mapping: dict) -> tuple:
    if not isinstance(area_name, str):
        return ("Unknown", "Unknown")
    name = area_name.strip()
    if name in mapping:
        return mapping[name]
    # Try relaxed matching by removing known suffixes
    suffixes = [", CA Met Div", ", CA MSA", ", CA"]
    for suffix in suffixes:
        if name.endswith(suffix):
            trimmed = name[: -len(suffix)]
            for key in mapping.keys():
                if key.startswith(trimmed):
                    return mapping[key]
    return ("Unknown", "Unknown")


path = 'Excel/BLS Project/data/'
all_files = glob.glob(path + "*.csv")

df_list = [pd.read_csv(file, encoding='utf-8') for file in all_files]
df = pd.concat(df_list, ignore_index=True)

print(df.head())
print(df.columns)

df.columns = df.columns.str.strip()

# Robust conversion of Year to integer
# Coerce non-numeric to NaN, drop missing years, then convert
df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
df = df[df['Year'].notna()]
df['Year'] = df['Year'].astype(int)

columns_to_keep = ["Area Name", "Year", "Month", "Labor Force", "Employment", "Unemployment", "Unemployment Rate"]
df = df[columns_to_keep]

# Compute County and Region based on Area Name (using built-in and optional CSV mapping)
mapping_csv = 'Excel/BLS Project/data/area_to_county_region.csv'
area_mapping = load_area_mapping(mapping_csv)
df[["County", "Region"]] = df["Area Name"].apply(lambda n: pd.Series(map_county_region(n, area_mapping)))

df = df[df["Year"] >= 2015] #Filter for last 10 years (2015-2025)

df.to_csv('Excel/BLS Project/data/cleaned_data.csv', index=False)
print("Data cleaned and saved to 'cleaned_data.csv'.")