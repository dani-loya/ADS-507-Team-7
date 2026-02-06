import pandas as pd

def clean_airbnb(path):
    df = pd.read_csv(path, low_memory=False)

    # Rename columns to match SQL schema
    df = df.rename(columns={
        "id": "listing_id",
        "neighbourhood_cleansed": "neighbourhood",
        "zipcode": "zip_code",
        "nightly_price": "price"
    })

    # Convert ZIP to string and pad
    df["zip_code"] = df["zip_code"].astype(str).str.zfill(5)

    # Columns required by SQL
    keep = [
        "listing_id", "name", "host_id", "neighbourhood", "zip_code",
        "latitude", "longitude", "room_type", "price", "minimum_nights",
        "number_of_reviews", "last_review"
    ]

    df = df[keep]

    # Add missing SQL-required columns
    df["reviews_per_month"] = None
    df["availability_365"] = None
    df["data_year"] = 2024

    return df

if __name__ == "__main__":
    df = clean_airbnb("data/raw/airbnb_raw.csv")
    df.to_csv("data/processed/airbnb_clean.csv", index=False)
