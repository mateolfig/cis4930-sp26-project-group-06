# Weather Data Pipeline – Group 6

## Team Members
| Name | ID | Role |
|---|---|---|
| Vanessa Campoe | VAC23A | Data Wrangler |
| Max Siska | MMS24I | Analyst |
| Mateo Linares Figueroa | ML22BZ | Visualization Designer |
| Vivianna Loredo | VL22J | Documentation / README Lead |

---

## Project Description

This pipeline tracks daily weather conditions in Tallahassee and Miami for local planning and trend analysis. It automatically fetches high temperature, low temperature, and precipitation from a public weather API once per run and stores the results in a local CSV. Running it repeatedly builds up a timestamped historical record that can be loaded and analyzed without any manual data entry.

---

## API Documentation

- **Open-Meteo Forecast API** — https://open-meteo.com/en/docs
  - Free to use, no API key required
  - Endpoint: `GET https://api.open-meteo.com/v1/forecast`

---

## Data Pipeline Goals

1. Fetch daily high temperature, low temperature, and precipitation for Tallahassee and Miami once per run.
2. Accumulate results into a single CSV, adding new rows on each run without overwriting previous data.
3. Attach a `fetched_at` timestamp to every row so runs can be distinguished from each other.
4. Handle API failures gracefully and log a clear error message instead of crashing silently.
5. Keep the code modular — API calls, storage, and orchestration each live in their own file.
