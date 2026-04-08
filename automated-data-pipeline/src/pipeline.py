"""
Main pipeline script - orchestrates fetching weather data and saving to CSV.
Run with: python -m src.pipeline (from project root)
"""

from api_client import fetch_multiple_cities
from storage import save_to_csv

# Cities to fetch weather data for (can add more here)
CITIES = [
    {"name": "Tallahassee", "lat": 30.4383, "lon": -84.2807},
    {"name": "Miami", "lat": 25.7617, "lon": -80.1918},
    {"name": "Orlando", "lat": 28.5383, "lon": -81.3792},
]


def main():
    print("Starting weather data pipeline...")
    print(f"Fetching forecasts for {len(CITIES)} cities...\n")

    # Fetch weather data for all cities
    df = fetch_multiple_cities(CITIES)

    if df.empty:
        print("No data fetched. Check your connection or API status.")
        return

    # Convert DataFrame to list of dicts for storage
    records = df.to_dict("records")

    # Save to CSV (appends to existing data)
    save_to_csv(records)

    print(f"\nPipeline complete! Fetched {len(records)} forecast records.")


if __name__ == "__main__":
    main()
