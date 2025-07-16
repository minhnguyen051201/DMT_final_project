import os
import urllib.request

# Destination folder
folder = "data"
os.makedirs(folder, exist_ok=True)

# Weather file URL and name
url = "https://www.ncei.noaa.gov/data/global-hourly/access/2024/06806599999.csv"
filename = os.path.join(folder, "weather_laguardia_airport_2024.csv")

# Headers to mimic browser
headers = {"User-Agent": "Mozilla/5.0"}

# Download process
req = urllib.request.Request(url, headers=headers)

try:
    with urllib.request.urlopen(req) as response, open(filename, "wb") as out_file:
        out_file.write(response.read())
    print(f"✅ Weather file saved to: {os.path.abspath(filename)}")
except Exception as e:
    print(f"❌ Failed to download weather data: {e}")
