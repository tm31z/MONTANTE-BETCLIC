# 🧠 Montante Betclic Bot (Telegram) — FULL AUTO

Ce bot Telegram est une **machine à cash automatisée** qui combine :
- Une stratégie de **montante intelligente** avec sécurisation
- Une **analyse en temps réel des matchs live**
- Un système de **recommandation de paris "safe"**
- Et un **scan automatique 24/24** pour ne rater aucune opportunité

---

## ⚙️ Fonctionnalités
- 📲 Commandes Telegram : `start`, `next`, `win`, `lose`, `status`, `stats`, `recolive`
- 🔁 Gestion automatique des paliers + sécurisation de gains
- 📡 Scan automatique des matchs live 24/24 (`auto_scan.py`)
- 💹 Historique détaillé de chaque pari (JSON)
- 📊 Analyse de stats réelles via API-Football
- ✅ Compatible Render, Railway, VPS

---

## 🛠️ Installation via GitHub + Render (RECOMMANDÉ)

### 1. Uploade tous les fichiers de ce ZIP dans un **repo GitHub**
Structure :
```
montante_betclic_bot/
├── main.py
├── auto_scan.py
├── montante_engine.py
├── paris_engine.py
├── history.py
├── live_stats.py
└── requirements.txt
```

### 2. Crée deux services sur [Render.com](https://render.com)

#### 🔹 Service 1 : Bot Telegram (commandes)
- **Start command** : `python main.py`
- **Build command** : `pip install -r requirements.txt`

#### 🔹 Service 2 : Scanner automatique
- **Start command** : `python auto_scan.py`
- **Build command** : `pip install -r requirements.txt`

---

## 🔐 Tokens à configurer (déjà intégrés ici)

- Token Telegram : intégré dans `main.py` et `auto_scan.py`
- Clé API-Football : intégrée dans `live_stats.py`
- ID Telegram perso : intégré dans `auto_scan.py` pour t’envoyer les alertes

---

## ✉️ Commandes Telegram disponibles

| Commande     | Description |
|--------------|-------------|
| `/start`     | Initialise la montante |
| `/next`      | Calcule le prochain palier (mise, sécurisation) |
| `/win`       | Enregistre une victoire et passe au palier suivant |
| `/lose`      | Réinitialise la montante après une perte |
| `/status`    | Affiche l’état actuel de la montante |
| `/stats`     | Affiche les stats cumulées |
| `/recolive`  | Analyse un match live et recommande un pari rentable |

---

## 📡 Fonctionnement du scan automatique (`auto_scan.py`)
- Tourne en boucle 24/24
- Analyse tous les matchs en live (ligues Betclic)
- Envoie une alerte Telegram dès qu’un pari "safe" est détecté

---

## 🤝 Contact
Bot initial développé et généré avec 💥 par OpenAI + réglages personnalisés.