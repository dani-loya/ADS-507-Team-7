-- Section for SQL schema -- Create database
CREATE DATABASE IF NOT EXISTS airbnb_sd;
USE airbnb_sd;

-- Airbnb listings table
CREATE TABLE IF NOT EXISTS airbnb_listings (
    listing_id BIGINT PRIMARY KEY,
    name VARCHAR(255),
    zipcode VARCHAR(10),
    latitude DECIMAL(9,6),
    longitude DECIMAL(9,6),
    room_type VARCHAR(100),
    price DECIMAL(10,2),
    minimum_nights INT,
    number_of_reviews INT,
    last_review DATE,
    reviews_per_month DECIMAL(5,2),
    calculated_host_listings_count INT,
    availability_365 INT
);

-- ACS DP05 table (Demographic and Housing Estimates)
CREATE TABLE IF NOT EXISTS acs_dp05 (
    geo_id VARCHAR(20),
    zip_code VARCHAR(10),
    year INT,
    total_population INT,
    total_housing_units INT,
    median_age DECIMAL(5,2),
    PRIMARY KEY (zip_code, year)
);

-- ACS B01003 table (Total Population)
CREATE TABLE IF NOT EXISTS acs_b01003 (
    geo_id VARCHAR(20),
    zip_code VARCHAR(10),
    year INT,
    total_population INT,
    PRIMARY KEY (zip_code, year)
);

