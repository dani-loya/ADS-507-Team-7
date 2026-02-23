#!/usr/bin/env python3

import mysql.connector
import os

from clean_airbnb import clean_airbnb
from clean_dp05 import *
from clean_b01003 import *

def get_connection():
    return mysql.connector.connect(
        host="airbnb-sd-db.c9uo2eu8w6nl.us-west-1.rds.amazonaws.com",
        port=3306,
        user="admin",
        password="Airbnb2026!",
        database="airbnb_project",
        allow_local_infile=True,
        client_flags=[mysql.connector.ClientFlag.LOCAL_FILES]
    )

# ---------------------------------------------------------
# CORRECT SQL EXECUTION FUNCTION (multi-statement support)
# ---------------------------------------------------------
def run_sql_file(cursor, filepath):
    print(f"Running: {filepath}")

    if not os.path.exists(filepath):
        print("FILE NOT FOUND:", filepath)
        return

    with open(filepath, "r") as file:
        sql = file.read()

    print("SQL length:", len(sql))

    try:
        for result in cursor.execute(sql, multi=True):
            pass
    except mysql.connector.Error as err:
        print(f"ERROR executing {filepath}: {err}")
# ---------------------------------------------------------

def main():
    # 1. CLEANING STEP
    df_airbnb = clean_airbnb("data/raw/listings (6).csv")
    df_airbnb.to_csv("data/processed/airbnb_clean.csv", index=False)

    # DP05 + B01003 cleaners run automatically on import
    import clean_dp05
    import clean_b01003

    # 2. CONNECT TO MYSQL
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("USE airbnb_project;")



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
