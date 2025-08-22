
import pandas as pd

# Read SAS file into a DataFrame
df = pd.read_sas("Python/CPS_ASEC_health_insurance_cleaning/data/hlthins_sy2000_rev.sas7bdat", format="sas7bdat", encoding="latin1")

# Show first 5 rows
print(df.head())
