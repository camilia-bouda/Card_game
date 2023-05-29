"""Entry point."""

from models.deck import Deck
from controllers.base import Controller, CheckRankAndSuit
from views.base import View


def main():
    deck = Deck()
    view = View()
    checker = CheckRankAndSuit()
    game = Controller(deck, view, checker)
    game.run()


if __name__ == "__main__":
    main()