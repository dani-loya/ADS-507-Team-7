USE airbnb_sd;

LOAD DATA LOCAL INFILE 'data/processed/acs_dp05_clean.csv'
INTO TABLE acs_dp05
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(geo_id, zip_code, year, total_population, total_housing_units, median_age);
-- load ACS dp05

