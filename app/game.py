# app/game.py

import random

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
        self.starting_player = random.choice(["player", "ai"])

    def draw_cards(self):
        if len(self.deck) < 3:
            raise ValueError("Plus assez de cartes pour tirer un tour complet.")
        return [self.deck.pop() for _ in range(3)]

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

        logger.info(f"Tour {self.turn} – Cartes tirées : {[card['name'] for card in cards]}")  # Log des cartes tirées

        print("\nCartes disponibles :")
        for idx, card in enumerate(cards, 1):
            print(f"{idx}. {card['name']} ({card['value']:+})")

        # Le joueur choisit une carte
        while True:
            try:
                choice = int(input("Choisis une carte (1-3) : "))
                if 1 <= choice <= 3:
                    break
                else:
                    print("Choix invalide. Entrer un nombre entre 1 et 3.")
            except ValueError:
                print("Entrée invalide. Utilise un chiffre.")

        player_card = cards.pop(choice - 1)
        print(f"🧍 Tu as choisi : {player_card['name']} ({player_card['value']:+})")

        # L'IA choisit une carte aléatoirement parmi les 2 restantes
        ia_card = cards.pop(random.randint(0, 1))
        print(f"🤖 L'IA a choisi : {ia_card['name']} ({ia_card['value']:+})")

        # 💥 Active les effets spéciaux
        self.apply_card_effect(player_card, ia_card, current_player="player")
        self.apply_card_effect(ia_card, player_card, current_player="ai")

        # Mise à jour des scores
        self.player_score += player_card["value"]
        self.ia_score += ia_card["value"]

        # print(f"✅ Score actuel — Toi: {self.player_score} | IA: {self.ia_score}")

        # La carte restante est remise dans le deck (et re-mélangée)
        self.deck.append(cards[0])  # il reste 1 carte dans `cards`
        random.shuffle(self.deck)

        self.turn += 1



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
        

