import pandas as pd

# Load raw DP05
df = pd.read_csv("data/raw/dp05_raw.csv")

# Keep only the columns you need
columns_to_keep = [
    "GEO_ID",
    "NAME",
    "DP05_0001E",  # Total population
    "DP05_0002E",  # Male
    "DP05_0003E",  # Female
]

df_clean = df[columns_to_keep].copy()

# Rename columns to match your SQL schema
df_clean.columns = [
    "geo_id",
    "name",
    "total_population",
    "male_population",
    "female_population"
]

# Save cleaned file
df_clean.to_csv("data/processed/acs_dp05_clean.csv", index=False)

print("Cleaned DP05 file created.")

