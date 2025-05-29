# app/cards.py

import random

# Une carte = nom, valeur, effet spécial (facultatif)
CARDS = [
    # Asiatique
    {"name": "Sushi Moisi", "value": -3, "effect": None},
    {"name": "Soupe Disparue", "value": 0, "effect": None},
    {"name": "Sesame Molletonné", "value": 2, "effect": "double_value"},
    {"name": "Riz Collant", "value": -1, "effect": None},
    {"name": "Pad Thai Acidulé", "value": -4, "effect": "double_value"},

    # Américain
    {"name": "Pizza Gluante", "value": -2, "effect": None},
    {"name": "Hot-Dog Piquant", "value": 3, "effect": None},
    {"name": "Cookie Mutant", "value": 2, "effect": None},
    {"name": "Burger Brûlé", "value": -4, "effect": "reverse_sign"},
    {"name": "Tacos Surprise", "value": 5, "effect": "double_value"},
    {"name": "Chili Glacé", "value": -2, "effect": None},
    {"name": "Nuggets Trop Cuits", "value": 1, "effect": None},

    # Européen
    {"name": "Tarte Trop Acide", "value": -1, "effect": None},
    {"name": "Glace Fantôme", "value": 0, "effect": "heal"},
    {"name": "Fromage Miroir", "value": -1, "effect": None},
    {"name": "Frites Friables", "value": 1, "effect": None},
    {"name": "Salade Explosive", "value": -5, "effect": "reverse_sign"},
    {"name": "Boulettes Rebelles", "value": 2, "effect": "swap_scores"},
    {"name": "Yaourt Hystérique", "value": 3, "effect": None},
    {"name": "Pâtes Trop Salées", "value": 4, "effect": None},
    {"name": "Pain Élastique", "value": -2, "effect": "double_value"},
    {"name": "Champignon Farceur", "value": -5, "effect": "swap_scores"},

    # Africain
    {"name": "Thiakry Vide", "value": 0, "effect": None},
    {"name": "Brochette Cramée", "value": -3, "effect": None},
    {"name": "Zebu Volant", "value": 0, "effect": "heal"},
    
]

def get_deck():
    """Retourne une copie mélangée du paquet"""
    deck = CARDS.copy()
    random.shuffle(deck)
    return deck
