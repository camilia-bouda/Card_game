"""Define the main controller."""

from models.deck import Deck
from models.player import Player

class Controller():
    
    def __init__(self, deck : Deck(), view):
        #models
        self.players: list[Player()] = []
        self.deck = deck

        #view
        self.view = view

    def get_players(self):
        """Get some players"""

        while len(self.players) < 2:
            name = self.view.prompt_for_players()
            if not name:
                return
            player = Player(name)
            self.players.append(player)
    
    def start_game(self):
        """Shuffle the deck and makes the player draw a card"""

        self.deck.shuffle()
        for player in self.players:
            card = self.deck.draw_card()
            player.hand.append(card)
    
    def evaluate_game(self):
        last_player = self.players[0]
        best_candidate = self.players[0]

        for player in self.players[1:]:
            player_card = player.hand[0]
            best_candidate_card = best_candidate.hand[0]

            if player_card > best_candidate_card:
                best_candidate = player
            
            return best_candidate.name
    
    def rebuild_deck(self):
        for player in self.players:
            while player.hand:
                card = player.hand.pop()
                card.is_face_up = False
                self.deck.append(card)
            self.deck.shuffle()

    def run(self):
        """Run the game"""
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
            self.rebuild_deck()

