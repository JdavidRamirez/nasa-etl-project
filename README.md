# Exploring the Universe: ETL with NASA's Near Earth Object API

This project extracts, transforms, and visualizes data from NASA's Near-Earth Object (NEO) API. It demonstrates how to build a real-world ETL (Extract, Transform, Load) pipeline using Python, PostgreSQL, and Looker Studio for interactive dashboards.

Note: The project isn't automated. It's a static project

##  Project Goals

-Fetch data on Near-Earth Objects from NASA's public API.
-Transform and clean the data into a structured format.
-Load the data into a PostgreSQL database.
-Query and analyze potentially hazardous asteroids.
-Create visual storytelling dashboards in Looker Studio.

## Tools Used

-Python: For extracting and transforming data.
-Pandas Library: Data manipulation.
-Requests Library:	API calls.
-SQLAlchemy Library: Database connection.
-PostgreSQL: Data storage.
-Looker Studio: Visualization and storytelling.
-Git & GitHub: Version control & documentation.

## What I did.

1. Extract:
 - Used NASA's NEO Feed API to collect data for the last 3 days.
 - Saved raw data to a .json file for backup.
2. Transform:
 -Parsed nested JSON to extract key attributes such as:
    - name: (String) The asteroid's official name or identifier provided by NASA. 
    - close_approach_date: (Date) The date when the asteroid makes its closest approach to Earth.
    - is_potentially_hazardous: (Boolean) Indicates if the asteroid is considered potentially dangerous to Earth (True or False).
    - estimated_diameter_min_m: (Float)	The smallest estimated diameter of the asteroid in meters.
    - estimated_diameter_max_m: (Float)	The biggest estimated diameter of the asteroid in meters.
    - relative_velocity_kph: (Float)	The speed at which the asteroid is moving relative to Earth, measured in kilometers per hour.
    - miss_distance_km: (Float)	The closest distance the asteroid will pass by Earth, measured in kilometers.
3. Query:
 - Built SQL queries to identify potentially hazardous asteroids, their closest distances, and approach speeds.
4. Visualize:
 - Uploaded SQL query output to Looker Studio.
 - Created a dashboard with:
    - Bar Chart: Top 10 Largest NEOs.
    - Table: Closest Approaches.
    - Scorecard: Largest asteroid
    - Scorecard: Only hazardous asteroid.
  
 ## Challenges faced

- JSON data from NASA's API was deeply nested.
- Required careful type conversions (e.g., float, datetime).
- Faced an error when uploading to PostgreSQL due to mismatched column names and delimiters.

##  Insights & Learnings

- ETL projects are the best option to organize and structure data paths.
- Conditional formatting and filters in dashboards help highlight risk.
- Storytelling improves clarity — titles, labels, and color matter!



               
  

