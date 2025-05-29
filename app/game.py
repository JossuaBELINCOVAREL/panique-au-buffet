# app/game.py

import random

from app.effects import EFFECT_DESCRIPTIONS

from app.cards import get_deck

from logger.logger import setup_logger
logger = setup_logger()

class BuffetGame:
    def __init__(self):
        self.deck = get_deck()
        self.player_score = 0
        self.ia_score = 0
        self.player_hand = []
        self.ai_hand = []
        self.turn = 1
        # self.starting_player = random.choice(["player", "ai"])
        self.player_starts = True

    def draw_cards(self):
        if len(self.deck) < 3:
            raise ValueError("Plus assez de cartes pour tirer un tour complet.")
        return [self.deck.pop() for _ in range(3)]
    
    def get_player_choice(self, cards):
        while True:
            try:
                choice = int(input("Choisis une carte (1-3) : ")) - 1
                if 0 <= choice < len(cards):
                    return choice
                else:
                    print(f"❌ Choix invalide. Entrer un nombre entre 1 et {len(cards)}.")
            except ValueError:
                print("❌ Entrée invalide. Tape un nombre.")

    def choose_card(self, cards, player):
        if player == "player":
            print("\nCartes disponibles :")
            for i, card in enumerate(cards):
                print(f"{i + 1}. {card['name']} ({card['value']})")
            choice = int(input("Choisis une carte (1-3) : ")) - 1
            return cards.pop(choice)
        else:
            # IA choisit la carte avec la valeur qui l'approche de zéro
            best_card = min(cards, key=lambda c: abs(c["value"]))
            cards.remove(best_card)
            return best_card
        
    def apply_card_effect(self, card, opponent_card, current_player):
        effect = card.get("effect")
        if not effect:
            return

        logger.info(f"{current_player} active le pouvoir : {effect}")

        if effect == "double_value":
            card["value"] *= 2
        elif effect == "swap_scores":
            self.player_score, self.ia_score = self.ia_score, self.player_score
        elif effect == "heal" and current_player == "player":
            self.player_score += 3
        elif effect == "reverse_sign":
            card["value"] *= -1


    def play_turn(self):
        cards = self.draw_cards()

        logger.info(f"Tour {self.turn} – Cartes tirées : {[card['name'] for card in cards]}")

        print("\nCartes disponibles :")
        for idx, card in enumerate(cards, 1):
            effect = card.get("effect")
            effect_str = f" — Effet : {EFFECT_DESCRIPTIONS.get(effect)}" if effect else ""
            print(f"{idx}. {card['name']} ({card['value']:+}){effect_str}")

        # Choix selon qui commence
        if self.player_starts:
            choice = self.get_player_choice(cards)
            player_card = cards[choice]
            # Crée une liste sans la carte choisie
            remaining = [card for i, card in enumerate(cards) if i != choice]
            ia_card = self.choose_card(remaining, player="ai")
        else:
            ia_card = self.choose_card(cards.copy(), player="ai")
            # Supprime la carte de l'IA
            cards.remove(ia_card)
            choice = self.get_player_choice(cards)
            player_card = cards[choice]

        print(f"🧍 Tu as choisi : {player_card['name']} ({player_card['value']:+})")
        print(f"🤖 L'IA a choisi : {ia_card['name']} ({ia_card['value']:+})")

        self.apply_card_effect(player_card, ia_card, current_player="player")
        self.apply_card_effect(ia_card, player_card, current_player="ai")

        self.player_score += player_card["value"]
        self.ia_score += ia_card["value"]

        self.player_starts = not self.player_starts
        self.turn += 1

        # Replace la carte restante (si encore une)
        leftover = [card for card in cards if card not in (player_card, ia_card)]
        if leftover:
            self.deck.append(leftover[0])
            random.shuffle(self.deck)


    def calculate_score(self, hand):
        return sum(card["value"] for card in hand)

    def play_game(self):
        print("🍽️ Bienvenue dans Panique au Buffet !\n")
        while self.turn <= 7:
            print(f"\n🔄 Tour {self.turn}")
            if len(self.deck) < 3:
                print("❌ Plus assez de cartes pour continuer.")
                break
            self.play_turn()

        logger.info(f"Score final joueur : {self.player_score}, IA : {self.ia_score}") # Log du score final
        
        print("\n🎉 Fin de la partie !")
        print(f"Ton score : {self.player_score}")
        print(f"Score de l'IA : {self.ia_score}")

        player_diff = abs(self.player_score)
        ia_diff = abs(self.ia_score)

        if player_diff < ia_diff:
            print("🏆 Tu gagnes ! Tu es le roi du buffet 🍽️👑")
        elif player_diff > ia_diff:
            print("💀 Tu perds... L'IA domine le buffet.")
        else:
            print("🤝 Égalité parfaite ! Vous avez le même appétit !")
        

