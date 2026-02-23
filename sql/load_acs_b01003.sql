-- load ACS B01003
USE airbnb_project;

LOAD DATA LOCAL INFILE 'data/processed/acs_b01003_clean.csv'
INTO TABLE acs_b01003
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(geo_id, name, total_population);

