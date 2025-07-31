from flask import Flask, request, jsonify, session
from flask_cors import CORS
from app.game import BuffetGame

app = Flask(__name__)
app.secret_key = "panique-secret-key"
CORS(app)

# Crée un seul objet jeu pour la session actuelle
game_instance = None

@app.route("/start-game", methods=["GET"])
def start_game():
    global game_instance
    game_instance = BuffetGame()
    return jsonify({
        "message": "Nouvelle partie commencée !",
        "turn": game_instance.turn,
        "player_score": game_instance.player_score,
        "ia_score": game_instance.ia_score
    })

@app.route("/get-hand", methods=["GET"])
def get_hand():
    if not game_instance:
        return jsonify({"error": "Aucune partie en cours."}), 400

    try:
        cards = game_instance.draw_cards()
        session["cards"] = cards
        return jsonify(cards)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route("/play-turn", methods=["POST"])
def play_turn():
    if "deck" not in session or "hand" not in session:
        return jsonify({"error": "Session invalide"}), 400

    data = request.get_json()
    card_name = data.get("card_name")

    if not card_name:
        return jsonify({"error": "Nom de carte manquant"}), 400

    # Cherche la carte dans la main en fonction du nom
    hand = session["hand"]
    selected_card = next((card for card in hand if card["name"] == card_name), None)

    if not selected_card:
        return jsonify({"error": "Carte non trouvée dans la main"}), 400

    # Retirer la carte jouée de la main
    hand.remove(selected_card)
    session["hand"] = hand

    # Appliquer l'effet de la carte
    player_score = session.get("player_score", 0)
    ia_score = session.get("ia_score", 0)

    effect = selected_card.get("effect")
    value = selected_card.get("value", 0)

    if effect == "double_value":
        player_score += value * 2
    elif effect == "reverse_sign":
        player_score -= value
    elif effect == "swap_scores":
        player_score, ia_score = ia_score, player_score
    elif effect == "heal":
        player_score += 2  # ou une autre logique
    else:
        player_score += value

    # IA joue une carte au hasard
    deck = session["deck"]
    if deck:
        ia_card = deck.pop()
        ia_value = ia_card.get("value", 0)
        ia_effect = ia_card.get("effect")

        if ia_effect == "double_value":
            ia_score += ia_value * 2
        elif ia_effect == "reverse_sign":
            ia_score -= ia_value
        elif ia_effect == "swap_scores":
            ia_score, player_score = player_score, ia_score
        elif ia_effect == "heal":
            ia_score += 2
        else:
            ia_score += ia_value
    else:
        ia_card = None

    # Met à jour les données de session
    session["deck"] = deck
    session["player_score"] = player_score
    session["ia_score"] = ia_score
    session["turn"] = session.get("turn", 1) + 1

    return jsonify({
        "message": f"Carte jouée : {card_name}",
        "player_score": player_score,
        "ia_score": ia_score,
        "turn": session["turn"],
        "ia_card": ia_card,
        "remaining_hand": session["hand"]
    })

if __name__ == "__main__":
    app.run(debug=True)
