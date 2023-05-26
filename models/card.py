SUITS = ("diamonds", "coeurs", 'piques', "carreaux")
RANKS = (
    "deux",
    "trois",
    "quatre",
    "cinq",
    "six",
    "sept",
    "huit",
    "neuf",
    "dix",
    "valet",
    "reine",
    "roi",
    "ace"
)

class Card:
    """
    Card class.

    Has a suit and a rank.
    """
    def __init__(self, suit, rank):
        """
        Init the suit, rank, is_face_up and the scores.
        """
        self.suit = suit
        self.rank = rank
        self.is_face_up = False

        self.rank_score = RANKS.index(self.rank)
        self.suit_score = SUITS.index(self.suit)

    def __str__(self) -> str:
        """
        Used in print.
        """
        return f"{self.rank} de {self.suit}"
    
    def __repr__(self) -> str:
        """
        Used in print.
        """
        return str(self)
    
    def __lt__(self, other: "Card") -> bool:
        """
        Compares the score of the current card with the score of another card.
        """
        if self.rank_score != other.rank_score:
            return self.rank_score < other.rank_score
        
        return self.suit_score < other.suit_score

