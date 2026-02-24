System of the project pipeline

1. Data extraction
Raw CSVs stored in data/raw/
Pipeline reads them directly
No manual preprocessing 

2. Data cleaning (Python)
Each cleaner script handles one dataset:
clean_airbnb.py
clean_dp05.py
clean_b01003.py
They:
Standardize column names
Parse dates
Extract ZIP codes
Remove invalid rows
Output cleaned CSVs to data/processed/

3. Database initialization (SQL)
create_schema.sql creates the database structure
02_create_tables.sql defines tables
Foreign keys and data types match the schema diagram

4. Data loading (SQL)
load_airbnb.sql
load_acs_dp05.sql
load_acs_b01003.sql
These scripts insert cleaned data into MySQL.

5. Transformations
transforms_density.sql joins the tables
Computes listings per 1,000 residents
Produces the final analytical table: airbnb_density

6. Orchestration (pipeline.py)
This script:
Runs all cleaners
Connects to MySQL
Executes all SQL scripts in order
Prints progress and success messages

