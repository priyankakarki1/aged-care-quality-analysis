create database aged_care_analysis;
use aged_care_analysis;
select * from star_ratings limit 10;

-- Query 1: Average star rating by state
SELECT 
    state_territory,
    ROUND(AVG(overall_star_rating), 2) AS avg_star_rating,
    COUNT(*) AS total_providers
FROM star_ratings
GROUP BY state_territory
ORDER BY avg_star_rating DESC;

-- Query 2: For-profit vs Not-for-profit vs Government comparison
SELECT 
    purpose,
    ROUND(AVG(overall_star_rating), 2) AS avg_rating,
    COUNT(*) AS total_providers
FROM star_ratings
GROUP BY purpose
ORDER BY avg_rating DESC;

-- Query 3: Large vs Medium vs Small facility comparison
SELECT 
    size,
    ROUND(AVG(overall_star_rating), 2) AS avg_rating,
    ROUND(AVG(staffing_rating), 2) AS avg_staffing,
    COUNT(*) AS total_providers
FROM star_ratings
GROUP BY size
ORDER BY avg_rating DESC;

-- Query 4b: Count of 5 star providers by state
SELECT 
    state_territory,
    COUNT(*) AS total_5_star_providers
FROM star_ratings
WHERE overall_star_rating = 5
ORDER BY total_5_star_providers DESC;

-- Query 5: Worst performing providers (1 and 2 star)
SELECT 
    state_territory,
    COUNT(*) AS total_poor_performers
FROM star_ratings
WHERE overall_star_rating <= 2
ORDER BY total_poor_performers DESC;

-- Query 6: Metro vs Rural quality comparison
SELECT 
    mmm_region,
    ROUND(AVG(overall_star_rating), 2) AS avg_rating,
    COUNT(*) AS total_providers
FROM star_ratings
GROUP BY mmm_region
ORDER BY avg_rating DESC;