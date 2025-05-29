from app.cards import get_deck

def test_deck_has_cards():
    deck = get_deck()
    assert isinstance(deck, list), "Deck should be a list"
    assert len(deck) > 0, "Deck should not be empty"
    assert all("name" in card and "value" in card for card in deck), "Each card must have name and value"