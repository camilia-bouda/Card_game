import random
from .card import RANKS, SUITS, Card

class Deck(list):
    """Deck of cards"""
    def __init__(self):
        """Has cards."""
        for rank in RANKS:
            for suit in SUITS:
                card = Card(suit, rank)
                self.append(card)
        self.shuffle()

    def shuffle(self):
        """Shuffle the deck"""
        random.shuffle(self)
    
    def draw_card(self):
        """Draw the top card"""
        try:
            return self.pop()
        except IndexError:
            return None