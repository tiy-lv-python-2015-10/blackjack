import random


class Card:
    """
    Responsibilities:
        * Has a suit (Heart, Clubs, Spades, Diamonds)
        * Has a value (Face cards =  10, Aces can be 1 or 11 depending on hand)

    Contributes:
        *Makes up the deck
        *Makes up the hand of the player and dealer
    """
    suit = ""
    rank = ""

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    @property
    def value(self):
        if self.rank == 'A':
            return 11
        elif self.rank in ['K', 'J', 'Q']:
            return 10
        else:
            return self.rank

    def __str__(self):
        return "{} of {}s".format(self.rank, self.suit)


class Deck:
    """
    Responsibilities:
        *Made up of cards
        *Contains 52 cards
        *Must be shuffled after every round

    Contributes:
        *Multiple decks make up shoe
        *Used in the game
    """
    my_random = 10

    def __init__(self):
        self.cards = []
        for suit in ['Heart', 'Clubs', 'Spades', 'Diamonds']:
            for rank in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        print("I am shuffling")
        random.shuffle(self.cards)

    def dealing(self):
        card1 = random.choice(self.cards)
        card2 = random.choice(self.cards)
        print(card1, card2)


class Player:
    """
    Responsibilities:
        *Places bets
        *chooses to hit or stand

    Contributes:
        *plays the game
        *cards make up hand
    """
    def __init__(self, *hand):
        self.cash = 100
        self.hand = hand
        self.hit_stand = ""

    def bets(self):
        if self.cash <= 10:
            print("You need money to play this game, punk")
        else:
            self.cash -= 10
            return self.cash

    def hit_or_stand(self, card_count):
        while True:
            hit_or_stand = input("Hit or Stand?")
            if hit_or_stand[0].lower == "h":
                print("Hit")
                self.hit_stand = hit_or_stand
            elif hit_or_stand[0].lower == "s":
                print("Stand")
                self.hit_stand = hit_or_stand
                break
            else:
                print("HIT or STAND!")
        return self.hit_stand

    def show_hand(self):
        print(self.hand)

class Dealer(Player):
    """
    Responsibilities:
        *deals cards
        *plays game like a player

    Contributes:
        *starts game
    """
    def hit_or_stand(self, card_count):
        if card_count < 17:
            self.hit_stand = "Hit"
        else:
            self.hit_stand = "Stand"
        return self.hit_stand

class Hand(Card):
    """
    responsibilities:
        * keeps track of hand amount
        *
    """
    card_count =

    def __init__(self):
        super.__init__(self)
        self.hand_value = 0

    def dealing(self):
        card1 = random.choice(self.cards)
        card2 = random.choice(self.cards)
        print(card1, card2)

    def hand_value(self):
        self.hand_value = self.value(self.card1) + self.value(self.card2)
class Game:
    """
    Responsibilities:

    """
    def __init__(self, p_hand, d_hand, cash):
        self.p_hand = p_hand
        self.d_hand = d_hand
        self. cash = cash


    def blackjack(self, p_hand, d_hand, cash):
        if d_hand < p_hand <= 21:
            self.cash = cash + 20
        elif d_hand == p_hand:
            self.cash = cash + 10
        else:
            return self.cash

if __name__ == '__main__':
