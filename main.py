import telebot
from montante_engine import *
from paris_engine import recommend_bet
from history import save_result, get_stats
from live_stats import fetch_live_match_stats

API_TOKEN = "7898519368:AAFuC5CIQ52hzbfsf0HfhRpjz2k_Rd3RclU"
CHAT_ID = "5824074931"
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=["start"])
def start_handler(message):
    state = init_montante(100, 1.5)
    save_state(state)
    bot.send_message(message.chat.id, "📊 Montante initialisée avec 100€ sur une cote de 1.50.")

@bot.message_handler(commands=["next"])
def next_handler(message):
    state = load_state()
    if not state:
        bot.send_message(message.chat.id, "❌ Aucune montante en cours.")
        return
    analysis = calculate_next_step(state)
    msg = (
        f"📍 Palier {state['current_step']}\n"
        f"💸 Mise : {state['current_mise']}€\n"
        f"📈 Gain potentiel : {analysis['gain_net']}€\n"
        f"🔐 Sécurisation : {analysis['secure_now']}€\n"
        f"💰 Total sécurisé : {analysis['total_secured']}€\n"
        f"➡️ Mise prochaine : {analysis['next_mise']}€"
    )
    bot.send_message(message.chat.id, msg)

@bot.message_handler(commands=["win"])
def win_handler(message):
    state = load_state()
    analysis = calculate_next_step(state)
    state = update_state_on_win(state, analysis["next_mise"], analysis["secure_now"], analysis["total_secured"])
    save_state(state)
    bot.send_message(message.chat.id, "✅ Victoire enregistrée. Prochain palier prêt.")

@bot.message_handler(commands=["lose"])
def lose_handler(message):
    state = load_state()
    state = reset_montante(state)
    save_state(state)
    bot.send_message(message.chat.id, "❌ Défaite. Montante redémarrée.")

@bot.message_handler(commands=["status"])
def status_handler(message):
    state = load_state()
    if not state:
        bot.send_message(message.chat.id, "Aucune montante active.")
        return
    bot.send_message(message.chat.id,
        f"📍 Palier : {state['current_step']}\n"
        f"💸 Mise : {state['current_mise']}€\n"
        f"🔐 Sécurisé : {state['total_secured']}€")

@bot.message_handler(commands=["stats"])
def stats_handler(message):
    mise, gain, secure = get_stats()
    bot.send_message(message.chat.id,
        f"📊 Statistiques globales :\n"
        f"💸 Total misé : {mise}€\n"
        f"💰 Total gagné : {gain}€\n"
        f"🔐 Total sécurisé : {secure}€")

@bot.message_handler(commands=["recolive"])
def recolive_handler(message):
    state = load_state()
    match_data = fetch_live_match_stats()
    if not match_data:
        bot.send_message(message.chat.id, "❌ Aucun match live dispo.")
        return
    reco, conf = recommend_bet(match_data["stats"])
    analysis = calculate_next_step(state)
    save_result(state["current_step"], state["current_mise"], analysis["gain_net"], analysis["secure_now"], conf, reco)
    bot.send_message(message.chat.id,
        f"📊 Match : {match_data['match']} ({match_data['minute']}')\n"
        f"💡 Pari : {reco}\n"
        f"🔎 Confiance : {conf}%\n"
        f"💸 Mise : {state['current_mise']}€ | Gain : {analysis['gain_net']}€\n"
        f"🔐 Sécurisation : {analysis['secure_now']}€")

bot.polling()