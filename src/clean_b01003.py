import pandas as pd

df = pd.read_csv("data/raw/b01003_raw.csv")

columns_to_keep = [
    "GEO_ID",
    "NAME",
    "B01003_001E"
]

df_clean = df[columns_to_keep].copy()

df_clean.columns = [
    "geo_id",
    "name",
    "total_population"
]

df_clean.to_csv("data/processed/acs_b01003_clean.csv", index=False)

print("Cleaned B01003 file created.")
