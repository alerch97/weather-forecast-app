import requests
import os

# secured api key in local env variable
API_KEY = os.environ.get("WEATHER_API")
UNIT = "metric"

def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&units={UNIT}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    filtered_data = filtered_data[:8*forecast_days]
    return filtered_data


if __name__ == "__main__":
    # testing
    print(get_data(place="Winterberg", forecast_days=3))