SELECT 
    name,
    close_approach_date,
	estimated_diameter_max_m,
    is_potentially_hazardous,
    relative_velocity_kph,
    miss_distance_km
FROM nasa_neo_data
WHERE close_approach_date >= CURRENT_DATE - INTERVAL '30 days'
ORDER BY estimated_diameter_max_m DESC
LIMIT 10;
