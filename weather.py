import requests


def get_coordinates(city):
    """Pobiera współrzędne miasta."""

    url = "https://geocoding-api.open-meteo.com/v1/search"

    response = requests.get(
        url,
        params={
            "name": city,
            "count": 1,
            "language": "pl",
            "format": "json",
        },
        timeout=10,
    )

    data = response.json()

    if "results" not in data:
        raise ValueError("Nie znaleziono miasta.")

    result = data["results"][0]

    return result["latitude"], result["longitude"], result["name"]


def get_weather(city):
    """Pobiera aktualną pogodę."""

    lat, lon, city_name = get_coordinates(city)

    url = "https://api.open-meteo.com/v1/forecast"

    response = requests.get(
        url,
        params={
            "latitude": lat,
            "longitude": lon,
            "current": [
                "temperature_2m",
                "relative_humidity_2m",
                "apparent_temperature",
                "pressure_msl",
                "wind_speed_10m",
                "weather_code",
            ],
        },
        timeout=10,
    )

    data = response.json()
    current = data["current"]

    return {
        "city": city_name,
        "temperature": current["temperature_2m"],
        "feels_like": current["apparent_temperature"],
        "humidity": current["relative_humidity_2m"],
        "pressure": current["pressure_msl"],
        "wind": current["wind_speed_10m"],
        "weather_code": current["weather_code"],
    }