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
    if not game_instance:
        return jsonify({"error": "Aucune partie en cours."}), 400

    data = request.json
    chosen_name = data.get("card_name")
    cards = session.get("cards")

    if not cards or not chosen_name:
        return jsonify({"error": "Carte manquante ou session invalide"}), 400

    # Trouver la carte du joueur
    player_card = next((c for c in cards if c["name"] == chosen_name), None)
    if not player_card:
        return jsonify({"error": "Carte non trouvée"}), 400
    cards.remove(player_card)

    # IA choisit une autre carte parmi celles restantes
    ia_card = game_instance.choose_card(cards, player="ai")
    cards.remove(ia_card)
    remaining_card = cards[0]

    # Appliquer les effets si nécessaire
    game_instance.apply_card_effect(player_card, ia_card, current_player="player")
    game_instance.apply_card_effect(ia_card, player_card, current_player="ai")

    game_instance.player_score += player_card["value"]
    game_instance.ia_score += ia_card["value"]
    game_instance.turn += 1
    game_instance.player_starts = not game_instance.player_starts

    return jsonify({
        "turn": game_instance.turn,
        "player_card": player_card,
        "ia_card": ia_card,
        "remaining_card": remaining_card,
        "player_score": game_instance.player_score,
        "ia_score": game_instance.ia_score,
        "game_over": game_instance.turn > 7
    })

if __name__ == "__main__":
    app.run(debug=True)
