"""Entry point."""

from models.deck import Deck
from controllers.base import Controller
from controllers.evaluate import CheckRankAndSuit
from views.base import PlayerView, BroadcastView, InternetStreamingView


def main():
    deck = Deck()
    view = PlayerView()
    views = (PlayerView(), BroadcastView(), InternetStreamingView())
    checker = CheckRankAndSuit()
    game = Controller(deck, view, views, checker)
    game.run()


if __name__ == "__main__":
    main()