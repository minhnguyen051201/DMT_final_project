# download_taxi_data_urllib.py
import os
import urllib.request

# Create destination folder
folder = "data"
os.makedirs(folder, exist_ok=True)

# Base URL and months
base_url = "https://d37ci6vzurychx.cloudfront.net/trip-data/"
months = ["01", "02", "03", "04", "05", "06"]

# Browser-like headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    " AppleWebKit/537.36 (KHTML, like Gecko)"
    " Chrome/114.0.0.0 Safari/537.36",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
}

# Download loop
for month in months:
    filename = f"yellow_tripdata_2024-{month}.parquet"
    url = base_url + filename
    file_path = os.path.join(folder, filename)

    print(f"📥 Downloading {filename} from {url}")
    req = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(req) as response, open(file_path, "wb") as out_file:
            out_file.write(response.read())
        print(f"✅ Success: Saved to {os.path.abspath(file_path)}")
    except Exception as e:
        print(f"❌ Error downloading {filename}: {e}")
