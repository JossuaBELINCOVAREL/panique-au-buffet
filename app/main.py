# app/main.py

from game import BuffetGame

if __name__ == "__main__":
    print("🍽️ Bienvenue dans Panique au Buffet !")
    game = BuffetGame()
    game.play_game()
