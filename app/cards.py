# app/cards.py

import random

# Une carte = nom, valeur, effet spécial (facultatif)
CARDS = [
    {"name": "Sushi Moisi", "value": -3, "effect": None},
    {"name": "Pizza Gluante", "value": -2, "effect": None},
    {"name": "Tarte Trop Acide", "value": -1, "effect": None},
    {"name": "Hot-Dog Piquant", "value": 3, "effect": None},
    {"name": "Glace Fantôme", "value": 0, "effect": None},
    {"name": "Cookie Mutant", "value": 2, "effect": None},
    {"name": "Fromage Miroir", "value": -1, "effect": None},
    {"name": "Burger Brûlé", "value": -4, "effect": None},
    {"name": "Frites Friables", "value": 1, "effect": None},
    {"name": "Salade Explosive", "value": -5, "effect": None},
    {"name": "Tacos Surprise", "value": 5, "effect": None},
    {"name": "Chili Glacé", "value": -2, "effect": None},
    {"name": "Gâteau Vide", "value": 0, "effect": None},
    {"name": "Brochette Cramée", "value": -3, "effect": None},
    {"name": "Boulettes Rebelles", "value": 2, "effect": None},
    {"name": "Soupe Disparue", "value": 0, "effect": None},
    {"name": "Nuggets Trop Cuits", "value": 1, "effect": None},
    {"name": "Biscuit Molletonné", "value": 2, "effect": None},
    {"name": "Riz Collant", "value": -1, "effect": None},
    {"name": "Yaourt Hystérique", "value": 3, "effect": None},
    {"name": "Pâtes Trop Salées", "value": 4, "effect": None},
    {"name": "Bonbon Acidulé", "value": -4, "effect": None},
    {"name": "Pain Élastique", "value": -2, "effect": None},
    {"name": "Champignon Farceur", "value": -5, "effect": None},
    {"name": "Compote Volante", "value": 0, "effect": None},
]

def get_deck():
    """Retourne une copie mélangée du paquet"""
    deck = CARDS.copy()
    random.shuffle(deck)
    return deck
