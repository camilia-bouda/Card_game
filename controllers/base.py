"""Define the main controller."""

from models.deck import Deck
from models.player import Player


class Controller():
    
    def __init__(self, deck : Deck(), view, check_strategy):
        # models
        self.players: list[Player] = []
        self.deck = deck

        # views
        self.view = view

        # check strategy
        self.check_strategy = check_strategy

    def get_players(self):
        """Get some players"""

        while len(self.players) < 2:  # nombre magique
            choices = []
            name = self.view.prompt_for_players()
            choices.append(name)
            if not any(choices):
                return
            for choice in choices:
                if choice:
                    name = choice
                    player = Player(name)
                    self.players.append(player)
    
    def start_game(self):
        """Shuffle the deck and makes the player draw a card"""

        self.deck.shuffle()
        for player in self.players:
            card = self.deck.draw_card()
            player.hand.append(card)
    
    def evaluate_game(self):
        return self.check_strategy.check(self.players)
    
    def rebuild_deck(self):
        for player in self.players:
            while player.hand:
                card = player.hand.pop()
                card.is_face_up = False
                self.deck.append(card)
            self.deck.shuffle()

    def run(self):
        self.get_players()

        running = True
        while running:
            self.start_game()
            for player in self.players:
                self.view.show_player_hand(player.name, player.hand)

            self.view.prompt_for_flip_cards()

            for player in self.players:
                for card in player.hand:
                    card.is_face_up = True
                self.view.show_player_hand(player.name, player.hand)

            self.view.show_winner(self.evaluate_game())

            running = self.view.prompt_for_new_game()
            if not running:
                return

            self.rebuild_deck()
