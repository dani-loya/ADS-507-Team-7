-- Create database
CREATE DATABASE IF NOT EXISTS airbnb_sd;
USE airbnb_sd;

-- Airbnb listings table
CREATE TABLE IF NOT EXISTS airbnb_listings (
    listing_id BIGINT PRIMARY KEY,
    name VARCHAR(255),
    host_id BIGINT,
    neighbourhood VARCHAR(255),
    zip_code VARCHAR(10),
    latitude DECIMAL(9,6),
    longitude DECIMAL(9,6),
    room_type VARCHAR(100),
    price DECIMAL(10,2),
    minimum_nights INT,
    number_of_reviews INT,
    last_review DATE,
    reviews_per_month DECIMAL(5,2),
    availability_365 INT,
    data_year INT
);

-- ACS DP05 table (matches cleaner)
CREATE TABLE IF NOT EXISTS acs_dp05 (
    geo_id VARCHAR(20),
    name VARCHAR(255),
    total_population INT,
    male_population INT,
    female_population INT
);

-- ACS B01003 table (matches cleaner)
CREATE TABLE IF NOT EXISTS acs_b01003 (
    geo_id VARCHAR(20),
    name VARCHAR(255),
    total_population INT
);
