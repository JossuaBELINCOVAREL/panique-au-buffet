from app.game import BuffetGame

def test_draw_cards_removes_three_cards():
    game = BuffetGame()
    initial_len = len(game.deck)
    drawn = game.draw_cards()
    assert len(drawn) == 3
    assert len(game.deck) == initial_len - 3

def test_calculate_score():
    game = BuffetGame()
    hand = [
        {"name": "Pizza Gluante", "value": -2},
        {"name": "Tacos Surprise", "value": +5},
        {"name": "Salade Explosive", "value": -5}
    ]
    score = game.calculate_score(hand)
    assert score == -2, f"Expected score -2, got {score}"

def test_ai_chooses_card_closest_to_zero():
    game = BuffetGame()
    cards = [
        {"name": "Salade Explosive", "value": -5},
        {"name": "Yaourt Hystérique", "value": +3},
        {"name": "Cookie Mutant", "value": +1}
    ]
    selected = game.choose_card(cards[:], player="ai")
    assert selected["value"] == +1, f"L'IA aurait dû choisir la carte la plus proche de 0"

def test_game_progression(monkeypatch):
    game = BuffetGame()
    game.deck = game.deck[:21]  # 7 tours max

    # Simule une saisie "1" à chaque tour
    monkeypatch.setattr("builtins.input", lambda _: "1")

    game.play_game()

    assert game.turn == 8  # Après 7 tours, on arrive à 8


