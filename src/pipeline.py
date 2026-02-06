import mysql.connector
import os

# ETLT (Extract + Transform (Python) + Load(SQL) + Transform(SQL))
# Cleaning step (Extract+Transform)
from clean_airbnb import clean_airbnb

airbnb_path = "data/raw/airbnb_clean.csv"  # placeholder for 2022 data

df_airbnb = clean_airbnb(airbnb_path)
df_airbnb.to_csv("data/processed/airbnb_clean.csv", index=False)

# Connect to MySQL
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        port=3307,
        user="root",
        password="Plmokn741",
        database="airbnb_sd",
        allow_local_infile=True
    )

# Run a SQL file
def run_sql_file(cursor, filepath):
    print(f"Running: {filepath}")
    with open(filepath, "r") as file:
        sql_commands = file.read()
        for command in sql_commands.split(";"):
            command = command.strip()
            if command:
                cursor.execute(command)

# Main pipeline
def main():
    conn = get_connection()
    cursor = conn.cursor()

    # 1. Create schema
    run_sql_file(cursor, "sql/create_schema.sql")
    conn.commit()
    
# Loading step into MySQL
    # 2. Load Airbnb data
    run_sql_file(cursor, "sql/load_airbnb.sql")
    conn.commit()

    # 3. Load ACS DP05 data
    run_sql_file(cursor, "sql/load_acs_dp05.sql")
    conn.commit()

    # 4. Load ACS B01003 data
    run_sql_file(cursor, "sql/load_acs_b01003.sql")
    conn.commit()

#Transformation
    # 5. Create density view
    run_sql_file(cursor, "sql/transforms_density.sql")
    conn.commit()

    print("Pipeline completed successfully.")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()

