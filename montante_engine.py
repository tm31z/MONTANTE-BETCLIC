import json
import os

STATE_FILE = "montante_state.json"

def init_montante(start_bet, target_odds):
    return {
        "current_step": 1,
        "current_mise": start_bet,
        "start_bet": start_bet,
        "target_odds": target_odds,
        "total_secured": 0
    }

def calculate_next_step(state):
    gain = state["current_mise"] * (state["target_odds"] - 1)
    to_secure = 0
    if state["total_secured"] < state["start_bet"] and state["current_step"] >= 2:
        to_secure = min(gain, state["start_bet"] - state["total_secured"])
    to_secure += (gain - to_secure) * 0.25
    new_total = state["total_secured"] + to_secure
    new_mise = state["current_mise"] + gain - to_secure
    return {
        "next_mise": round(new_mise, 2),
        "secure_now": round(to_secure, 2),
        "gain_net": round(gain, 2),
        "total_secured": round(new_total, 2)
    }

def update_state_on_win(state, next_mise, secure_now, total_secured):
    state["current_step"] += 1
    state["current_mise"] = next_mise
    state["total_secured"] = total_secured
    return state

def reset_montante(state):
    state["current_step"] = 1
    state["current_mise"] = state["start_bet"]
    state["total_secured"] = 0
    return state

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f)

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    return None