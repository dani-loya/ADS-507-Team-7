import mysql.connector
import os

from clean_airbnb import clean_airbnb
from clean_dp05 import *
from clean_b01003 import *

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        port=3307,
        user="root",
        password="Plmokn741",
        database="airbnb_sd",
        allow_local_infile=True
    )

def run_sql_file(cursor, filepath):
    print(f"Running: {filepath}")
    with open(filepath, "r") as file:
        sql_commands = file.read()
        for command in sql_commands.split(";"):
            command = command.strip()
            if command:
                cursor.execute(command)

def main():
    # 1. CLEANING STEP
    df_airbnb = clean_airbnb("data/raw/listings (6).csv")
    df_airbnb.to_csv("data/processed/airbnb_clean.csv", index=False)

    # DP05
    import clean_dp05
    # B01003
    import clean_b01003

    # 2. CONNECT TO MYSQL
    conn = get_connection()
    cursor = conn.cursor()

    # 3. CREATE SCHEMA
    run_sql_file(cursor, "sql/create_schema.sql")
    conn.commit()

    # 4. LOAD CLEANED DATA
    run_sql_file(cursor, "sql/load_airbnb.sql")
    conn.commit()

    run_sql_file(cursor, "sql/load_acs_dp05.sql")
    conn.commit()

    run_sql_file(cursor, "sql/load_acs_b01003.sql")
    conn.commit()

    # 5. TRANSFORMATIONS
    run_sql_file(cursor, "sql/transforms_density.sql")
    conn.commit()

    print("Pipeline completed successfully.")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
