import requests
from bs4 import BeautifulSoup
import time

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def get_team_slug(name):
    name = name.lower().replace(" ", "-")
    return name

def get_form_score(team1, team2):
    try:
        score1 = fetch_team_form(get_team_slug(team1))
        score2 = fetch_team_form(get_team_slug(team2))
        score = round((score1 + (100 - score2)) / 2)
        return score
    except Exception as e:
        print(f"Ошибка формы: {e}")
        return 50

def fetch_team_form(team_slug):
    url = f"https://www.sofascore.com/team/{team_slug}/"
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        raise Exception("Не удалось получить данные команды")

    soup = BeautifulSoup(response.text, "html.parser")
    form_row = soup.find_all("div", class_="sc-cMljjf eAxjFz")

    recent_results = []
    for item in form_row:
        text = item.text.strip()
        if text in ["W", "D", "L"]:
            recent_results.append(text)
        if len(recent_results) == 5:
            break

    # Преобразуем форму в баллы: победа=3, ничья=1, поражение=0
    score = sum({"W": 3, "D": 1, "L": 0}.get(r, 0) for r in recent_results)
    return score * 100 // 15  # Приводим к процентам