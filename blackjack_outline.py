"""
I need to create a blackjack Game. In blackjack, the player plays against the dealer. A player can win in three
different ways.  The three ways are, the player gets 21 on his first two cards, the dealer gets a score higher than 21,
and if the player's score is higher than the dealer without going over 21. The dealer wins if the player goes over 21,
or if the dealer's hand is greater than the player's without going over 21.  In the beginning, the player is
dealt two cards. There is also one rule which states that if the dealer's hand is greater than or equal to 17, then he
can not hit anymore.  There is a point system that must be followed in the game of blackjack,  all cards have a point
value based off the numeric indication on the front.  The card's that don't follow this rule are ace's which could be 1
or 11, and face cards which all equal to 10.  It is also important to know what a deck of cards has; a deck of cards ha
s 52 cards, 13 unique cards, and 4 suits of those 13 unique cards.

Game(player1, player2=)
    The Game

    Responsibilities:

    * ask players if they want to hit or stand.
    *

    Collaborators:

    * Collected into a Deck.
    * Collected into a Hand for each player and a Hand for the dealer.



    def play_game
        def deal_two_cards_to_player
        def switch_players
Player
   The player

    Responsibilities:
    * Has to hit or stand

    Collaborators:
    * game takes the hit or stand response

    def hit
    def stand
    money

Dealer
    The dealer

    Responsibilities:
    * Has to hit, has to stand at 17 or greater

    Collaborators:
    * game takes the hit or stand response

    def hit
    def stand
    money
    shoe

Hand
    cards_in_hand

Card

    A playing card.

    Responsibilities:

    * Has a rank and a suit.
    * Has a point value. Aces point values depend on the Hand.

    Collaborators:

    * Collected into a Deck.
    * Collected into a Hand for each player and a Hand for the dealer.


    suit
    kind

Deck
    card_amount
    suits
    kinds



if __name__ == '__main__':
"""


