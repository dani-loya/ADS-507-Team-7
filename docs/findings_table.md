# Airbnb Density and Pricing by ZIP Code (San Diego)

This table summarizes the merged dataset produced by our ETL pipeline. It includes population, total Airbnb listings, Airbnb density (listings per 1,000 residents), average nightly price, and review activity for each ZIP code in San Diego. These values come directly from the `airbnb_density` table and the joined Airbnb listings table in our AWS RDS database.

The table highlights clear geographic patterns in Airbnb activity across the city.

| ZIP Code | Population | Listings | Listings per 1,000 | Avg Price ($) | Avg Reviews/Month |
|----------|------------|----------|---------------------|----------------|--------------------|
| 92109 | 47,111 | 2,602 | 55.23 | 309.70 | 0.00 |
| 92101 | 41,159 | 1,999 | 48.57 | 212.35 | 0.00 |
| 92103 | 34,700 | 873 | 25.16 | 201.44 | 0.00 |
| 92107 | 31,223 | 751 | 24.05 | 239.21 | 0.00 |
| 92104 | 45,435 | 770 | 16.95 | 140.82 | 0.00 |
| 92102 | 44,010 | 673 | 15.29 | 167.69 | 0.00 |
| 92110 | 30,108 | 376 | 12.49 | 296.72 | 0.00 |
| 92108 | 22,280 | 264 | 11.85 | 167.05 | 0.00 |
| 92116 | 33,408 | 384 | 11.49 | 124.57 | 0.00 |
| 92106 | 20,155 | 218 | 10.82 | 283.96 | 0.00 |
| 92117 | 56,983 | 363 | 6.37 | 139.30 | 0.00 |
| 92122 | 48,071 | 251 | 5.22 | 140.72 | 0.00 |
| 92111 | 50,693 | 229 | 4.52 | 123.23 | 0.00 |
| 92115 | 64,343 | 268 | 4.17 | 110.60 | 0.00 |
| 92120 | 30,550 | 125 | 4.09 | 150.42 | 0.00 |
| 92121 | 4,729 | 19 | 4.02 | 119.21 | 0.00 |
| 92123 | 32,473 | 128 | 3.94 | 102.65 | 0.00 |
| 92130 | 56,134 | 215 | 3.83 | 255.61 | 0.00 |
| 92113 | 58,408 | 153 | 2.62 | 129.86 | 0.00 |
| 92105 | 73,623 | 163 | 2.21 | 105.28 | 0.00 |
| 92126 | 82,658 | 181 | 2.19 | 78.91 | 0.00 |
| 92114 | 68,851 | 124 | 1.80 | 80.90 | 0.00 |
| 92129 | 54,762 | 82 | 1.50 | 125.40 | 0.00 |
| 92131 | 34,727 | 50 | 1.44 | 194.16 | 0.00 |
| 92139 | 36,105 | 48 | 1.33 | 99.48 | 0.00 |
| 92119 | 24,831 | 31 | 1.25 | 163.74 | 0.00 |
| 92128 | 51,357 | 58 | 1.13 | 182.55 | 0.00 |
| 92124 | 32,600 | 35 | 1.07 | 151.63 | 0.00 |
| 92154 | 88,979 | 77 | 0.87 | 139.39 | 0.00 |
| 92127 | 49,935 | 39 | 0.78 | 241.33 | 0.00 |
| 92173 | 31,000 | 20 | 0.65 | 45.10 | 0.00 |
| 92118 | 22,548 | 1 | 0.04 | 250.00 | 0.00 |

## Interpretation

Coastal ZIP codes such as **92109**, **92101**, **92103**, and **92107** show the highest Airbnb density, reflecting strong tourism demand and smaller residential populations. Inland ZIP codes with large populations, such as **92105**, **92126**, and **92114**, show significantly lower Airbnb penetration. Pricing also tends to be higher in high‑density coastal areas, indicating a strong relationship between location desirability and Airbnb market behavior.

