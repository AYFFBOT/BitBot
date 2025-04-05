from api.odds_api import get_odds
from api.sofascore_api import get_form_score

def get_top_matches():
    matches = get_odds()
    top = []
    for match in matches:
        score = get_form_score(match["team1"], match["team2"])
        if score >= 60:
            top.append({
                "teams": f"{match['team1']} vs {match['team2']}",
                "odds": match['odds'],
                "score": score
            })
    return top