import requests
import os

# secured api key in local env variable
API_KEY = os.environ.get("WEATHER_API")

def get_data(place, forecast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    filtered_data = filtered_data[:8*forecast_days]

    match kind:
        case "Temperature":
            filtered_data = [dict["main"]["temp"] for dict in filtered_data]
        case "Sky":
            filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]

    return filtered_data


if __name__ == "__main__":
    # testing
    print(get_data(place="Tokyo", forecast_days=3, kind="Sky"))