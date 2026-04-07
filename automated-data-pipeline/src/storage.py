import os
from datetime import datetime

import pandas as pd

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CSV_PATH = os.path.join(BASE_DIR, "data", "processed", "weather.csv")

# our 6 columns of data we want to save for each city and date, plus a timestamp to tell runs apart
COLUMNS = ["city", "date", "temperature_max", "temperature_min", "precipitation", "fetched_at"]


def save_to_csv(records):
    """
    Takes a list of dicts, one per city, and appends them to the CSV.
    Each dict should have a city, date, temperature_max, temperature_min, precipitation.
    A fetched_at timestamp is added automatically.

    Example:
        records = [
            {"city": "Tallahassee", "date": "2026-04-07", "temperature_max": 85,
             "temperature_min": 65, "precipitation": 0.2},
            {"city": "Miami", "date": "2026-04-07", "temperature_max": 90,
             "temperature_min": 75, "precipitation": 0.0},
        ]
    """
    if not records:
        print("No records to save.")
        return

    # adds a timestamp to each record so we can tell runs apart
    fetched_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cleaned_records = []
    for record in records:
        cleaned_record = {
            "city": record.get("city"),
            "date": record.get("date"),
            "temperature_max": record.get("temperature_max"),
            "temperature_min": record.get("temperature_min"),
            "precipitation": record.get("precipitation"),
            "fetched_at": fetched_at
        }
        cleaned_records.append(cleaned_record)

    # converts to DataFrame
    df = pd.DataFrame(cleaned_records, columns=COLUMNS)

    # confirms output folder exists
    os.makedirs(os.path.dirname(CSV_PATH), exist_ok=True)

    # if file doesn't exist yet write with header, otherwise append
    file_exists = os.path.isfile(CSV_PATH)
    df.to_csv(CSV_PATH, mode="a", header=not file_exists, index=False)

    print(f"Saved {len(df)} record(s) to {CSV_PATH} at {fetched_at}")


def load_csv():
    """
    Reads and returns the full CSV as a DataFrame.
    Returns None if the file doesn't exist yet.
    """
    if not os.path.isfile(CSV_PATH):
        print("No data file found yet. Run the pipeline first.")
        return None

    df = pd.read_csv(CSV_PATH)
    print(f"Loaded {len(df)} total row(s) from {CSV_PATH}")
    return df
