import pandas as pd

def clean_airbnb(path):
    df = pd.read_csv(path)

    # Standardize ZIP code column names
    zip_cols = [c for c in df.columns if "zip" in c.lower()]
    if zip_cols:
        df.rename(columns={zip_cols[0]: "zipcode"}, inplace=True)

    # Standardize price column
    price_cols = [c for c in df.columns if "price" in c.lower()]
    if price_cols:
        df.rename(columns={price_cols[0]: "price"}, inplace=True)

    # Convert ZIP to string and pad
    df["zipcode"] = df["zipcode"].astype(str).str.zfill(5)

    # Keep only columns needed for SQL
    keep = ["id", "listing_id", "zipcode", "price", "latitude", "longitude"]
    existing = [c for c in keep if c in df.columns]
    df = df[existing]

    return df
