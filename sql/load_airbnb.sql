USE airbnb_sd;

LOAD DATA LOCAL INFILE 'data/raw/airbnb_listings.csv'
INTO TABLE airbnb_listings
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(listing_id, name, zipcode, latitude, longitude, room_type, price,
 minimum_nights, number_of_reviews, last_review, reviews_per_month,
 calculated_host_listings_count, availability_365);

