USE airbnb_sd;

USE airbnb_project;

LOAD DATA LOCAL INFILE 'data/processed/acs_dp05_clean.csv'
INTO TABLE acs_dp05
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(geo_id, name, total_population, male_population, female_population);


