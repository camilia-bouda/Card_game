"""Define the main view."""

class Views:
    """Implement the other views."""

    def __init__(self, active_view, views):
        """Init the active view and the passives views."""
        self.active_view = active_view
        self.views = views

    def prompt_for_players(self):
        """Call the active view."""
        return self.active_view.prompt_for_players()

    def show_player_hand(self, name, hand):
        """Call the passive views."""
        for view in self.views:
            view.show_player_hand(name, hand)

    def prompt_for_flip_cards(self):
        """Call the active view."""
        return self.active_view.prompt_for_flip_cards()

    def show_winner(self, name):
        """Call the passive views."""
        for view in self.views:
            view.show_winner(name)

    def prompt_for_new_game(self):
        """Call the active view."""
        return self.active_view.prompt_for_new_game()


class PlayerView():

    def prompt_for_players(self):
        name = input("Entrez le nom du joueur :")
        if not name:
            return None
        return name
    
    def show_player_hand(self, name, hand):
        print(f"[Joueur {name}]:")
        for card in hand:
            if card.is_face_up:
                print(card)
            else:
                print("(carte face cachée)")
    
    def prompt_for_flip_cards(self):
        input("Prêt à retourner les cartes ?")
        return True
    
    def show_winner(self, name):
        """Show the winner."""
        print(f"Bravo {name} !")

    def prompt_for_new_game(self):
        """Request to replay."""
        print("Souhaitez vous refaire une partie ?")
        choice = input("Y/n: ")
        if choice == "n":
            return False
        return True


class BroadcastView():

    def prompt_for_players(self):
        return None
    
    def show_player_hand(self, name, hand):
        print(f"[Joueur {name}]:")
        for card in hand:
            if card.is_face_up:
                print(card)
            else:
                print("(carte face cachée)")
    
    def prompt_for_flip_cards(self):
        return True
    
    def show_winner(self, name):
        """Show the winner."""
        print(f"Bravo {name} !")

    def prompt_for_new_game(self):
        return True
    

class InternetStreamingView():

    def prompt_for_players(self):
        return None
    
    def show_player_hand(self, name, hand):
        print(f"[Joueur {name}]:")
        for card in hand:
            if card.is_face_up:
                print(card)
            else:
                print("(carte face cachée)")
    
    def prompt_for_flip_cards(self):
        return True
    
    def show_winner(self, name):
        """Show the winner."""
        print(f"Bravo {name} !")

    def prompt_for_new_game(self):
        return True