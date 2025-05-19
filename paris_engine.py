def generate_confidence(stats):
    score = 0
    if stats["shots_on_target"] > 5:
        score += 30
    if stats["possession"] > 55:
        score += 25
    if stats["xg"] > 1.5:
        score += 25
    if stats["dominant_team"]:
        score += 20
    return min(score, 100)

def recommend_bet(stats):
    confidence = generate_confidence(stats)
    if confidence >= 80:
        return "+0.5 but HT", confidence
    elif confidence >= 60:
        return "Prochaine équipe qui marque", confidence
    else:
        return "Aucun pari recommandé", confidence