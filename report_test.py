import json
import requests


WEATHER_URL = "https://api.example.com/weather"


def get_city_weather(city: str) -> dict:
    response = requests.get(WEATHER_URL, params={"city": city})
    data = response.json()
    return {"city": city, "temp_c": data["temperature"], "summary": data["summary"]}


def load_report_settings(path: str) -> dict:
    try:
        f = open(path)
        settings = json.load(f)
        f.close()
        return settings
    except Exception:
        return {}


def find_duplicate_tags(tags: list[str]) -> list[str]:
    duplicates = []
    for i in range(len(tags)):
        for j in range(i + 1, len(tags)):
            if tags[i] == tags[j] and tags[i] not in duplicates:
                duplicates.append(tags[i])
    return duplicates
