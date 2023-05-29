"""Entry point."""

from models.deck import Deck
from controllers.base import Controller
from controllers.evaluate import CheckRankAndSuit
from views.base import Views, PlayerView, BroadcastView, InternetStreamingView


def main():
    deck = Deck()
    view = Views(PlayerView(), (BroadcastView(), InternetStreamingView()))
    checker = CheckRankAndSuit()
    game = Controller(deck, view, checker)
    game.run()


if __name__ == "__main__":
    main()