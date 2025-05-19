import json
import os

HISTORY_FILE = "history.json"

def save_result(palier, mise, gain, secure, confidence, bet_type):
    data = {
        "palier": palier,
        "mise": mise,
        "gain": gain,
        "secure": secure,
        "confidence": confidence,
        "bet": bet_type
    }
    history = []
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)
    history.append(data)
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f)

def get_stats():
    if not os.path.exists(HISTORY_FILE):
        return 0, 0, 0
    with open(HISTORY_FILE, "r") as f:
        history = json.load(f)
    return sum(d["mise"] for d in history), sum(d["gain"] for d in history), sum(d["secure"] for d in history)