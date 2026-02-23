import pandas as pd

def clean_airbnb(path):
    df = pd.read_csv(path, low_memory=False)

    # Standardize column names to match SQL schema
    df = df.rename(columns={
        "id": "listing_id",
        "neighbourhood_cleansed": "neighbourhood",
        "zipcode": "zip_code",
        "nightly_price": "price"
    })

    # Clean ZIP codes
    df["zip_code"] = (
        df["zip_code"]
        .astype(str)
        .str.extract(r"(\d{5})")  # keep only valid 5-digit ZIPs
        .fillna("00000")
    )

    # Convert price to numeric
    df["price"] = (
        df["price"]
        .astype(str)
        .str.replace(r"[^0-9.]", "", regex=True)
    )
    df["price"] = pd.to_numeric(df["price"], errors="coerce")

    # Parse last_review as datetime
    df["last_review"] = pd.to_datetime(df["last_review"], errors="coerce")

    # Columns required by SQL
    keep = [
        "listing_id", "name", "host_id", "neighbourhood", "zip_code",
        "latitude", "longitude", "room_type", "price", "minimum_nights",
        "number_of_reviews", "last_review"
    ]

    # Select only the required columns
    df = df[keep]

    # *** CRITICAL FIX: remove duplicate columns AFTER selecting keep ***
    df = df.loc[:, ~df.columns.duplicated()]

    # Add missing SQL-required columns
    df["reviews_per_month"] = None
    df["availability_365"] = None
    df["data_year"] = 2024

    return df

if __name__ == "__main__":
    df = clean_airbnb("data/raw/listings (6).csv")
    df.to_csv("data/processed/airbnb_clean.csv", index=False)
