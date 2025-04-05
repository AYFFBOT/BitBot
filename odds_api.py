import requests

API_KEY = "ad361015b134e5da9b5f19379a775757"

def get_odds():
    url = "https://api.the-odds-api.com/v4/sports/soccer_epl/odds/"
    params = {
        "apiKey": API_KEY,
        "regions": "eu",
        "markets": "h2h",
        "oddsFormat": "decimal"
    }
    response = requests.get(url, params=params)
    data = response.json()

    matches = []
    for item in data:
        try:
            teams = item['teams']
            odds = item['bookmakers'][0]['markets'][0]['outcomes']
            avg_odds = sum([o['price'] for o in odds]) / len(odds)
            matches.append({
                "team1": teams[0],
                "team2": teams[1],
                "odds": round(avg_odds, 2)
            })
        except Exception:
            continue
    return matches
