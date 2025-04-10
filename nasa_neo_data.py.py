#Main libraries to fletch data from the NASA API
import requests
import pandas as pd
import json
from datetime import date, timedelta


# Replace with your API key
API_KEY = "6socNC5nPTWKsGuhC0L0j48ejJFtCxAnFMCl0Ofj"  # or your real key
BASE_URL = "https://api.nasa.gov/neo/rest/v1/feed"


# Set your date range (max 7 days per request)
start_date = date.today() - timedelta(days=3)
end_date = date.today()

params = {
    "start_date": start_date.isoformat(),
    "end_date": end_date.isoformat(),
    "api_key": API_KEY
}

# Make the request
response = requests.get(BASE_URL, params=params)

# Check status
if response.status_code == 200:
    data = response.json()
    print(" Data retrieved successfully!")
else:
    print(" Failed to fetch data:", response.status_code)

# Save raw data to file
with open("nasa_raw_data.json", "w") as f:
    json.dump(data, f)

# Preview top-level keys
print("\nTop-level keys:", data.keys())


# Preview keys
neo_data = data["near_earth_objects"]

# Flatten into a list of NEOs across all dates
records = []

for date_str, neos in neo_data.items():
    for neo in neos:
        for approach in neo["close_approach_data"]:
            records.append({
                "name": neo["name"],
                "close_approach_date": approach["close_approach_date"],
                "is_potentially_hazardous": neo["is_potentially_hazardous_asteroid"],
                "estimated_diameter_min_m": neo["estimated_diameter"]["meters"]["estimated_diameter_min"],
                "estimated_diameter_max_m": neo["estimated_diameter"]["meters"]["estimated_diameter_max"],
                "relative_velocity_kph": float(approach["relative_velocity"]["kilometers_per_hour"]),
                "miss_distance_km": float(approach["miss_distance"]["kilometers"]),
                "orbiting_body": approach["orbiting_body"]
            })

df = pd.DataFrame(records)
#change format date
df['close_approach_date']=pd.to_datetime(df['close_approach_date'])


# Save cleaned DataFrame to CSV
df.to_csv(r"C:\Users\Lau\Desktop\Proyectos\nasa_neo_data.csv", index=False, encoding="utf-8")

print(" CSV file saved successfully!")

from sqlalchemy import create_engine

try:
    engine = create_engine("postgresql+psycopg2://postgres:5287@localhost:5433/neo_nasa")
    with engine.connect() as conn:
        print(" Connected successfully!")
except Exception as e:
    print("Connection failed:")
    print(e)

try:
    df.to_sql("nasa_neo_data", engine, if_exists="append", index=False)
    print("✅ Data uploaded successfully!")
except Exception as e:
    print("❌ Failed to upload data:")
    print(e)
