
import pandas as pd

insurance_map = {
    "Any Insurance": ["COV_HI"],  # already a summary flag
    "Private Insurance": ["DEPHI", "DEPRIV", "HELSE1", "HELSE2", "HELSE3"],
    "Public Insurance": ["CAID", "CARE", "CHAMP", "CH_HI", "CH_MC"],
    "Medicaid": ["CAID"],
    "Medicare": ["CARE"],
    "Military/TRICARE": ["CHAMP"],
    "Children’s Insurance": ["CH_HI", "CH_MC"],
    "Other Programs": ["HELSE1", "HELSE2", "HELSE3", "HELSE4"]
}

# Read SAS file into a DataFrame
df = pd.read_sas("Python/CPS_ASEC_health_insurance_cleaning/data/hlthins_sy2000_rev.sas7bdat", format="sas7bdat", encoding="latin1")

print(df.head())

value_map = {1: "Yes", 2: "No", 0: "N.I.U."}
for col in df.columns:
    if col in sum(insurance_map.values(), []):  # flatten the list
        df[col] = df[col].replace(value_map)

df["Public Insurance"] = df[insurance_map["Public Insurance"]].eq("Yes").any(axis=1)
df["Private Insurance"] = df[insurance_map["Private Insurance"]].eq("Yes").any(axis=1)


df.to_csv("Python/CPS_ASEC_health_insurance_cleaning/data/hlthins_sy2000_rev.csv", index=False)


