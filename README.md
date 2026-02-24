
## Goal: 
Investigate Airbnb locations and prices across San Diego using different zipcodes to have a clear data-driven insights on Airbnb activity and its impact on the different neighborhoods and locals. 
The automated data pipeline findings let us see the tourism across neghtborhoods. 

## Datasets taken from: 

### 1. Airbnb Listings (San Diego) 
Source: <link to dataset>
Download the CSV and place it in:
`data/raw/listings (6).csv`

U.S. Census ACS demographic data
### 2. ACS DP05 (Demographic and Housing Estimates) 
Source: https://data.census.gov/
Download the DP05 table as CSV and place it in:
`data/raw/ACSDP5Y2019.DP05-Data.csv` 

### 3. ACS B01003 (Total Population)
Source: https://data.census.gov/
Download the B01003 table as CSV and place it in:
`data/raw/ACSDT5Y2019.B01003-Data.csv`

## Architecture Overview

1. Data source
   The project uses two primary storage layers to ensure reproducibility and clear lineage from raw -> processed -> database
   #### Local storage
   data/raw/ contains the original CSV files exactly as downloaded.
   data/processed/ contains cleaned and standardized versions of each dataset.

   #### AWS RDS MySQL database
   stores the final cleaned tables:
   airbnb_listings
   acs_dp05
   acs_b01003
   stores derived view:
   airbnb_density
   
2. Pipeline execution flow
   Pipeline is executed through: src/pipeline.py
   This script orchestrates the entire workflow. The entry point ensures the pipeline is fully reproducible.

   1. Load environment variables from .env
   2. Run cleaning scripts to standardize raw data
   3. Connect to AWS RDS using MySQL Connector
   4. Execute SQL schema creation
   5. Load cleaned data into RDS tables
   6. Run transformation SQL to create the airbnb_density view
   7. Print a final success message when all steps complete
  
3. Cleaning Layer (Python)
   Each dataset has its own cleaning script in src/:
   clean_airbnb.py
   clean_dp05.py
   clean_b01003.py
   These scripts perform:
   Column renaming
   Type conversions
   Missing value handling
   ZIP code extraction
   Standardization across datasets

The cleaned outputs are saved to data/processed/ and then loaded into the database.

4. Database Layer (SQL)
   All SQL logic is stored in the sql/ directory:
    create_schema.sql — Creates the database tables
    load_airbnb.sql — Loads cleaned Airbnb data
    load_acs_dp05.sql — Loads ACS demographic data
    load_acs_b01003.sql — Loads ACS population data
    transforms_density.sql — Creates the airbnb_density view using ZIP code joins
    The transformation setup uses: SUBSTRING(d.geo_id, -5)
      - This is use to extract ZIP codes from ACS GEOIDs and ensure consitent joins across the datasets.

5. Derived View:  airbnb_density
   The final output of the pipeline is a database view that combines
   Airbnb listing counts
   ACS population data
   ACS demographic data
   The view calculates:
   Total listings per ZIP code
   Population per ZIP code
   Listings per 1,000 residents (density metric)
   This view is the primary analytical product of the pipeline.

6. Repository Structure

   
7. Reproducibility and Deployment
   The pipeline is fully reproducible because:
   All code is version-controlled
   All SQL files are included
   All cleaning scripts are included
   requirements.txt specifies dependencies
   .env.example documents required environment variables
   The pipeline runs end‑to‑end with a single command:

Schema
Database → Reverse Engineer → Selected your RDS connection → Selected schema airbnb_project → Finished


