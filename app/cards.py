# app/cards.py

import random

# Une carte = nom, valeur, effet spécial (facultatif), image (future illustration)
CARDS = [
    # Asiatique
    {"name": "Sushi Moisi", "value": -3, "effect": None, "image": "sushi_moisi.png"},
    {"name": "Soupe Disparue", "value": 0, "effect": None, "image": "soupe_disparue.png"},
    {"name": "Sesame Molletonné", "value": 2, "effect": "double_value", "image": "sesame_molletonne.png"},
    {"name": "Riz Collant", "value": -1, "effect": None, "image": "riz_collant.png"},
    {"name": "Pad Thai Acidulé", "value": -4, "effect": "double_value", "image": "pad_thai_acidule.png"},

    # Américain
    {"name": "Pizza Gluante", "value": -2, "effect": None, "image": "pizza_gluante.png"},
    {"name": "Hot-Dog Piquant", "value": 3, "effect": None, "image": "hot_dog_piquant.png"},
    {"name": "Cookie Mutant", "value": 2, "effect": None, "image": "cookie_mutant.png"},
    {"name": "Burger Brûlé", "value": -4, "effect": "reverse_sign", "image": "burger_brule.png"},
    {"name": "Tacos Surprise", "value": 5, "effect": "double_value", "image": "tacos_surprise.png"},
    {"name": "Chili Glacé", "value": -2, "effect": None, "image": "chili_glace.png"},
    {"name": "Nuggets Trop Cuits", "value": 1, "effect": None, "image": "nuggets_trop_cuits.png"},

    # Européen
    {"name": "Tarte Trop Acide", "value": -1, "effect": None, "image": "tarte_trop_acide.png"},
    {"name": "Glace Fantôme", "value": 0, "effect": "heal", "image": "glace_fantome.png"},
    {"name": "Fromage Miroir", "value": -1, "effect": None, "image": "fromage_miroir.png"},
    {"name": "Frites Friables", "value": 1, "effect": None, "image": "frites_friables.png"},
    {"name": "Salade Explosive", "value": -5, "effect": "reverse_sign", "image": "salade_explosive.png"},
    {"name": "Boulettes Rebelles", "value": 2, "effect": "swap_scores", "image": "boulettes_rebelles.png"},
    {"name": "Yaourt Hystérique", "value": 3, "effect": None, "image": "yaourt_hysterique.png"},
    {"name": "Pâtes Trop Salées", "value": 4, "effect": None, "image": "pates_trop_salees.png"},
    {"name": "Pain Élastique", "value": -2, "effect": "double_value", "image": "pain_elastique.png"},
    {"name": "Champignon Farceur", "value": -5, "effect": "swap_scores", "image": "champignon_farceur.png"},

    # Africain
    {"name": "Thiakry Vide", "value": 0, "effect": None, "image": "thiakry_vide.png"},
    {"name": "Brochette Cramée", "value": -3, "effect": None, "image": "brochette_cramee.png"},
    {"name": "Zebu Volant", "value": 0, "effect": "heal", "image": "zebu_volant.png"},
]

def get_deck():
    """Retourne une copie mélangée du paquet"""
    deck = CARDS.copy()
    random.shuffle(deck)
    return deck
