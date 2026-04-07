import requests
import pandas as pd

def fetch_weather(city, lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "daily": [
            "temperature_2m_max",
            "temperature_2m_min",
            "precipitation_sum",
        ],
        "timezone": "America/New_York",
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    daily = data.get("daily", {})

    df = pd.DataFrame({
        "city": city,
        "date": daily.get("time", []),
        "temperature_max": daily.get("temperature_2m_max", []),
        "temperature_min": daily.get("temperature_2m_min", []),
        "precipitation": daily.get("precipitation_sum", []),
    })

    return df

print(fetch_weather("Tallahassee", 30.455, -84.253334))