# Automated Data Pipeline

## Group 6 – CIS4930 SP26

### Team Members
| Name | ID | Role |
|---|---|---|
| Vanessa Campoe | VAC23A | Data Wrangler |
| Max Siska | MMS24I | Analyst |
| Mateo Linares Figueroa | ML22BZ | Visualization Designer |
| Vivianna Loredo | VL22J | Documentation / README Lead |

---

## Project Description

This pipeline automatically fetches 7-day daily weather forecasts for multiple Florida cities (Tallahassee, Miami, and Orlando) using the Open-Meteo API and saves the results to a local CSV file. The goal is to build up a timestamped historical record of forecasts — useful for local planning, comparing predicted vs. actual conditions, or studying seasonal weather trends over time. Each time the pipeline runs it appends a new batch of rows so the dataset grows without overwriting previous data.

---

## API Documentation

**Open-Meteo Forecast API**
- Docs: https://open-meteo.com/en/docs
- Free to use — no API key or account required
- Endpoint: `GET https://api.open-meteo.com/v1/forecast`
- Parameters used:
  - `latitude`, `longitude` — city coordinates
  - `daily=temperature_2m_max,temperature_2m_min,precipitation_sum` — fields returned per day
  - `timezone=America/New_York` — localizes dates to Eastern time

### API Constraints

| Constraint | Details |
|------------|---------|
| **Authentication** | None required — fully public API |
| **Rate Limit** | ~10,000 requests/day (generous for our use case) |
| **Pagination** | Not applicable — each request returns all 7 forecast days in one response |
| **Response Format** | JSON with nested `daily` object containing arrays for each weather variable |

We chose Open-Meteo because it requires no API key, has no sign-up process, and provides reliable global weather data, making it easy for all team members to run the pipeline immediately after cloning.

---

## Data Pipeline Goals

1. **Fetch a 7-day daily forecast for a given city** — call `fetch_weather(city, lat, lon)` which hits the Open-Meteo API and returns a DataFrame with one row per forecast day containing `temperature_max`, `temperature_min`, and `precipitation`.
2. **Accumulate results into a single CSV, adding new rows per run** — `save_to_csv()` appends each batch to `data/processed/weather.csv` and automatically creates the file (with headers) on the first run.
3. **Stamp every batch with a fetch timestamp** — a `fetched_at` column is added to every row so you can tell which pipeline run produced each record and compare forecasts made on different dates.
4. **Support reloading the stored data** — `load_csv()` reads the full accumulated CSV back into a DataFrame so downstream scripts or notebooks can analyze it without duplicating I/O logic.
5. **Run without credentials** — the pipeline uses Open-Meteo, a fully public API, so any team member can run it immediately after cloning the repo with no setup beyond `pip install`.

---

## How to Run

### Prerequisites

```bash
pip install requests pandas
```

### Running the Pipeline

From the `automated-data-pipeline/` directory:

```bash
python3 src/pipeline.py
```

### Example Output

```
Starting weather data pipeline...
Fetching forecasts for 3 cities...

Fetch: Tallahassee...
Fetch: Miami...
Fetch: Orlando...
Saved 21 record(s) to data/processed/weather.csv at 2026-04-08 18:08:28

Pipeline complete! Fetched 21 forecast records.
```

