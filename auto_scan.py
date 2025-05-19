import time
import requests
from live_stats import fetch_live_match_stats
from paris_engine import recommend_bet
from montante_engine import load_state, calculate_next_step, save_state
from history import save_result
import telebot

API_TOKEN = "7898519368:AAFuC5CIQ52hzbfsf0HfhRpjz2k_Rd3RclU"
CHAT_ID = "5824074931"
bot = telebot.TeleBot(API_TOKEN)

def auto_scan():
    while True:
        state = load_state()
        if not state:
            time.sleep(60)
            continue

        match_data = fetch_live_match_stats()
        if not match_data:
            time.sleep(60)
            continue

        reco, conf = recommend_bet(match_data["stats"])
        if reco != "Aucun pari recommandé" and conf >= 75:
            analysis = calculate_next_step(state)
            save_result(
                state["current_step"],
                state["current_mise"],
                analysis["gain_net"],
                analysis["secure_now"],
                conf,
                reco
            )
            msg = (
                f"📡 Signal détecté en LIVE !\n\n"
                f"📊 Match : {match_data['match']} ({match_data['minute']}')\n"
                f"🏆 Compétition : {match_data['league']}\n"
                f"💡 Pari conseillé : {reco}\n"
                f"🔎 Confiance : {conf}%\n\n"
                f"💸 Mise : {state['current_mise']}€\n"
                f"📈 Gain potentiel : {analysis['gain_net']}€\n"
                f"🔐 Sécurisation : {analysis['secure_now']}€"
            )
            bot.send_message(CHAT_ID, msg)

        time.sleep(60)

if __name__ == "__main__":
    auto_scan()