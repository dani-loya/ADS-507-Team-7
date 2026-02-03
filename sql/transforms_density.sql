USE airbnb_sd;

-- Create a combined table with Airbnb + ACS data
CREATE OR REPLACE VIEW airbnb_density AS
SELECT
    a.zipcode,
    COUNT(a.listing_id) AS total_listings,
    d.total_population,
    d.total_housing_units,
    
    -- Listings per 1,000 residents
    (COUNT(a.listing_id) / d.total_population) * 1000 AS listings_per_1000_residents,
    
    -- Listings per 1,000 housing units
    (COUNT(a.listing_id) / d.total_housing_units) * 1000 AS listings_per_1000_housing_units

FROM airbnb_listings a
LEFT JOIN acs_dp05 d
    ON a.zipcode = d.zip_code
    AND d.year = 2023   -- You can change this year if needed

GROUP BY
    a.zipcode,
    d.total_population,
    d.total_housing_units;

