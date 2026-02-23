USE airbnb_project;

CREATE OR REPLACE VIEW airbnb_density AS
SELECT
    a.zip_code,
    COUNT(a.listing_id) AS total_listings,
    d.total_population,
    (COUNT(a.listing_id) / d.total_population) * 1000 AS listings_per_1000_residents
FROM airbnb_listings a
LEFT JOIN acs_dp05 d
    ON a.zip_code = SUBSTRING(d.geo_id, -5)
GROUP BY
    a.zip_code,
    d.total_population;

