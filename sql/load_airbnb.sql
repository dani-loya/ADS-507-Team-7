USE airbnb_sd;

LOAD DATA INFILE '/var/lib/mysql-files/airbnb_clean.csv'
INTO TABLE airbnb_listings
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(listing_id, name, host_id, neighbourhood, zip_code, latitude, longitude,
 room_type, price, minimum_nights, number_of_reviews, last_review,
 reviews_per_month, availability_365, data_year);
