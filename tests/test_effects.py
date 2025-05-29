import pytest
from app.game import BuffetGame as Game

@pytest.fixture
def game():
    g = Game()
    g.player_score = 10
    g.ia_score = 5
    return g

def test_double_value(game):
    card = {"name": "Tacos Surprise", "value": 4, "effect": "double_value"}
    opponent = {"name": "Pizza Gluante", "value": -2, "effect": None}
    
    game.apply_card_effect(card, opponent, current_player="player")
    
    assert card["value"] == 8, "double_value doit doubler la valeur"

def test_swap_scores(game):
    card = {"name": "Boulettes Rebelles", "value": 2, "effect": "swap_scores"}
    opponent = {"name": "Frites Friables", "value": 1, "effect": None}
    
    game.apply_card_effect(card, opponent, current_player="player")
    
    assert game.player_score == 5
    assert game.ia_score == 10

def test_heal(game):
    card = {"name": "Zebu Volant", "value": 0, "effect": "heal"}
    opponent = {"name": "Glace Fantôme", "value": 0, "effect": None}
    
    game.apply_card_effect(card, opponent, current_player="player")
    
    assert game.player_score == 13, "heal doit ajouter 3 au score joueur"
