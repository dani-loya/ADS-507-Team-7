# ADS-507-Team-7

## Goal: 
Investigate Airbnb locations and prices across San Diego using different zipcodes to have a clear data-driven insights on Airbnb activity and its impact on the different neighborhoods and locals. 
The automated data pipeline findings let us see the tourism across neghtborhoods. 


## Data pipeline is designed to perform automatically and be reproducible.
## Datasets loading:

### 1. San Diego Airbnb Listings 
Source: https://www.kaggle.com/datasets/thedevastator/san-diego-airbnb-listings-august-2019
Download the CSV and place it in:
`data/raw/airbnb_listings.csv`
Note: While the dataset covers the period 2008–2019, this project focuses on a subset from 2015 to 2019.

U.S. Census ACS demographic data
### 2. ACS DP05 (Demographic and Housing Estimates) 
Source: https://data.census.gov/
Download the DP05 table as CSV and place it in:
`data/raw/dp05_raw.csv`

### 3. ACS B01003 (Total Population)
Source: https://data.census.gov/
Download the B01003 table as CSV and place it in:
`data/raw/b01003_raw.csv`

## Data Cleaning:
Raw CSV files are cleaned and saved into a new processed folder. 
data/raw -> cleaned -> data/processed

## Schema


## Transformations
