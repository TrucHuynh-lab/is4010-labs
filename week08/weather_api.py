
import requests


class WeatherAPI:
    def __init__(self, api_key, base_url="https://api.weatherapi.com/v1"):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")

    def get_current_weather(self, location):
        url = f"{self.base_url}/current.json"

        params = {
            "key": self.api_key,
            "q": location
        }

        try:
            response = requests.get(
                url,
                params=params,
                timeout=10
            )
            response.raise_for_status()
            return response.json()

        except (requests.RequestException, ValueError):
            return None

    def get_forecast(self, location, days=3):
        if not 1 <= days <= 3:
            raise ValueError("Forecast days must be between 1 and 3.")

        url = f"{self.base_url}/forecast.json"

        params = {
            "key": self.api_key,
            "q": location,
            "days": days
        }

        try:
            response = requests.get(
                url,
                params=params,
                timeout=10
            )
            response.raise_for_status()
            return response.json()

        except (requests.RequestException, ValueError):
            return None


def format_current_weather(data):
    city = data["location"]["name"]
    country = data["location"]["country"]
    temperature = data["current"]["temp_f"]
    condition = data["current"]["condition"]["text"]

    return f"{city}, {country}: {temperature}°F, {condition}"


def format_forecast(data):
    forecast_days = data["forecast"]["forecastday"]
    results = []

    for day in forecast_days:
        date = day["date"]
        high = day["day"]["maxtemp_f"]
        low = day["day"]["mintemp_f"]
        condition = day["day"]["condition"]["text"]

        results.append(
            f"{date}: high {high}°F, low {low}°F, {condition}"
        )

    return "\n".join(results)
