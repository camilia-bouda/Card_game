# Création d'un jeu de cartes

## Objectif du projet
Projet simple


Code maintenable


## Spécificiations du jeu
* Créez un jeu de cartes standard de 52 cartes.
* Entrez des noms de joueurs. Limitez le nombre de joueurs à cinq.
* Battez les cartes.
* Distribuez une carte à chaque joueur (face vers le bas).
* Retournez les cartes de tous les joueurs, montrant quelle carte ils ont.
* Vérifiez quel joueur a la carte de plus haut rang : As > Roi > Reine > Valet > 10… > 2.
* En cas d’égalité, on départage les joueurs grâce à la couleur :
Trèfle > Pique > Cœur > Carreau.
* Montrez le nom et la carte du gagnant.
* Remettez toutes les cartes dans la pile.
* Retournez à l’étape du battage des cartes.

## MVC
### Modèle
Le modèle est constitué:
* d’un joueur
* d’une main
* d’une carte à jouer
* d’un jeu,
* d’un rang 
* d’une couleur

### Vue

### Controller

```mermaid
classDiagram
    direction LR
    class Card {
        +suit
        +rank
        +is_faced_up
        +rank_score
        +suit_score
    }
    class Deck { 
        +(shuffle)
        +(draw_card)
    }
    class Player {
        +name
        +hand
    }
    class Hand
    Card -- Deck
    Player -- Hand
    Hand -- Card