# NYC Taxi & Weather Data Project (2024)

## Overview

This project analyzes how weather conditions (rain, snow, temperature) affect NYC Yellow Taxi activity from Jan–Jun 2024.

## Folder Structure

- `data/` — Raw downloaded files (excluded from Git)
- `download_taxi_data.py` — Script to fetch Yellow Taxi data
- `download_weather_data.py` — Script to fetch NOAA weather data
- `collect_clean_data.ipynb` — Jupyter notebook to clean, merge, and analyze

## How to Reproduce

1. Clone the repo
2. Run:
   ```bash
   python download_taxi_data.py
   python download_weather_data.py
   ```
3. Open `collect_clean_data.ipynb` to process and explore

## Dependencies

Install with:

```bash
pip install -r requirements.txt

```
