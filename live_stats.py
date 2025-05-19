import requests

API_KEY = "17e5f7f67f4b253b10ee08500fbcdee0"
BETCLIC_COMPETITIONS = [
    61, 62, 135, 140, 78, 39, 2, 3, 5, 4, 71, 66, 94, 95, 88, 203
]

def fetch_live_match_stats():
    url = "https://v3.football.api-sports.io/fixtures?live=all"
    headers = {"x-apisports-key": API_KEY}
    res = requests.get(url, headers=headers)
    matches = res.json().get("response", [])
    for match in matches:
        if match["league"]["id"] not in BETCLIC_COMPETITIONS:
            continue
        try:
            stats_url = f"https://v3.football.api-sports.io/fixtures/statistics?fixture={match['fixture']['id']}"
            stats_res = requests.get(stats_url, headers=headers)
            stats_data = stats_res.json().get("response", [])

            team_stats = {}
            for stat in stats_data:
                team = stat["team"]["name"]
                team_stats[team] = {item["type"]: item["value"] for item in stat["statistics"]}

            home = match["teams"]["home"]["name"]
            away = match["teams"]["away"]["name"]
            minute = match["fixture"]["status"]["elapsed"]
            league = match["league"]["name"]

            return {
                "match": f"{home} vs {away}",
                "minute": minute,
                "league": league,
                "stats": {
                    "shots_on_target": team_stats[home].get("Shots on Goal", 0) + team_stats[away].get("Shots on Goal", 0),
                    "possession": int(team_stats[home].get("Ball Possession", "50%").strip('%')),
                    "xg": 1.6,
                    "dominant_team": home if team_stats[home].get("Shots on Goal", 0) > team_stats[away].get("Shots on Goal", 0) else away
                }
            }
        except:
            continue
    return None