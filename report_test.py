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


def average_score(rows: list[dict]) -> float:
    total = 0
    for row in rows:
        total += int(row["score"])
    return total / len(rows)
def add_tag(tag: str, tags: list[str] = []) -> list[str]:
    if tag not in tags:
        tags.append(tag)
    return tags


def build_score_report(rows: list[dict], title: str) -> str:
    report = title + "\n"
    report = report + "=" * len(title) + "\n"
    for row in rows:
        name = row["name"].strip().title()
        score = int(row["score"])
        grade = "A" if score >= 90 else "B" if score >= 75 else "C" if score >= 50 else "F"
        report = report + f"{name}: {score} ({grade})\n"

    best = max(rows, key=lambda r: int(r["score"]))
    worst = min(rows, key=lambda r: int(r["score"]))
    avg = sum(int(r["score"]) for r in rows) / len(rows)

    report = report + f"\nBest: {best['name']} ({best['score']})\n"
    report = report + f"Worst: {worst['name']} ({worst['score']})\n"
    report = report + f"Average: {avg:.2f}\n"
    return report


def paginate(items: list, page: int, page_size: int) -> list:
    start = page * page_size
    end = start + page_size
    return items[start:end]