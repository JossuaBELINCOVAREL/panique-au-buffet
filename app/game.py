# app/game.py

import random
from cards import get_deck

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

    def play_turn(self):
        cards = self.draw_cards()

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
        print(f"Tu as choisi : {player_card['name']} ({player_card['value']:+})")

        # L'IA choisit une carte aléatoirement parmi les 2 restantes
        ia_card = cards.pop(random.randint(0, 1))
        print(f"L'IA a choisi : {ia_card['name']} ({ia_card['value']:+})")

        # La carte restante est remise dans le deck (et re-mélangée)
        self.deck.append(cards[0])  # il reste 1 carte dans `cards`
        random.shuffle(self.deck)

        # Mise à jour des scores
        self.player_score += player_card["value"]
        self.ia_score += ia_card["value"]


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
            self.turn += 1

        print("\n🎉 Fin de la partie !")
        print(f"Ton score : {self.player_score}")
        print(f"Score de l'IA : {self.ia_score}")

        player_diff = abs(self.player_score)
        ia_diff = abs(self.ia_score)

        if player_diff < ia_diff:
            print("🏆 Tu gagnes ! Tu es le roi du buffet 🍽️👑")
        elif player_diff > ia_diff:
            print("🤖 L'IA gagne ! Elle a mieux géré son assiette...")
        else:
            print("🤝 Égalité parfaite ! Vous avez le même appétit !")
        

