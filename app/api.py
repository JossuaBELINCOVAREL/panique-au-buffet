from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uuid
import random

from app.game import BuffetGame  # Assure-toi que BuffetGame est bien importé depuis app/game.py

app = FastAPI(title="Panique au Buffet - API")

# Stockage des parties en mémoire (simple dict pour dev/local)
games = {}

# -------------------------
# Modèles Pydantic
# -------------------------

class Card(BaseModel):
    name: str
    value: int
    effect: Optional[str] = None
    image: Optional[str] = None

class StartGameResponse(BaseModel):
    game_id: str
    available_cards: List[Card]
    player_score: int
    ia_score: int

class PlayTurnRequest(BaseModel):
    game_id: str
    player_choice_index: int  # 0, 1 ou 2

class PlayTurnResponse(BaseModel):
    player_card: Card
    ai_card: Card
    player_score: int
    ia_score: int
    remaining_deck_size: int
    message: Optional[str] = None

# -------------------------
# Routes
# -------------------------

@app.post("/start-game", response_model=StartGameResponse)
def start_game():
    game = BuffetGame()
    game_id = str(uuid.uuid4())
    games[game_id] = game

    cards = game.draw_cards()

    return StartGameResponse(
        game_id=game_id,
        available_cards=cards,
        player_score=game.player_score,
        ia_score=game.ia_score
    )

@app.post("/play-turn", response_model=PlayTurnResponse)
def play_turn(request: PlayTurnRequest):
    game = games.get(request.game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Partie non trouvée")

    # Vérifie que le choix est valide
    if not (0 <= request.player_choice_index < 3):
        raise HTTPException(status_code=400, detail="Index de carte invalide (doit être entre 0 et 2)")

    # Tire 3 cartes pour ce tour
    cards = game.current_cards.copy()
    if not cards or len(cards) < 3:
        raise HTTPException(status_code=400, detail="Aucune carte disponible pour ce tour. As-tu bien lancé la partie ?")

    # Le joueur choisit
    player_card = cards.pop(request.player_choice_index)

    # L'IA choisit parmi les deux restantes
    ai_card = game.choose_card(cards, "ai")

    # Appliquer effets éventuels
    game.apply_card_effect(player_card, ai_card, current_player="player")
    game.apply_card_effect(ai_card, player_card, current_player="ai")

    # Mise à jour des scores
    game.player_score += player_card["value"]
    game.ia_score += ai_card["value"]

    # Remettre la carte restante dans le deck
    if cards:
        game.deck.append(cards[0])
        random.shuffle(game.deck)

    message = f"Tu as joué {player_card['name']} ({player_card['value']}), IA a joué {ai_card['name']} ({ai_card['value']})"

    return PlayTurnResponse(
        player_card=player_card,
        ai_card=ai_card,
        player_score=game.player_score,
        ia_score=game.ia_score,
        remaining_deck_size=len(game.deck),
        message=message
    )
