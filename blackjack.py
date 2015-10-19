import random


class Card:
    def __init__(self, rank, suit):
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
    my_random = 10

    def __init__(self):
        self.cards = []
        for suit in ['Heart', 'Clubs', 'Spades', 'Diamonds']:
            for rank in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        print("I am shuffling")
        random.shuffle(self.cards)

    def __str__(self):
        return str([card.__str__() for card in self.cards])


class Hand():
    def __init__(self, *cards):
        self.cards = []
        self.cards_in_hand = []
        self.value = 0

    def draw_from(self):
        print()
        card1 = self.cards.pop()
        card2 = self.cards.pop()
        self.cards_in_hand = [card1, card2]

    def return_to(self):
        for cards in self.cards_in_hand:
            self.deck.append(cards)
        self.cards_in_hand = []

    def __str__(self):
        return str(self.cards_in_hand)


class Player:
    def __init__(self, *hand):
        self.hand = hand
        self.hit_stand = ""

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


class Dealer(Player):
    def hit_or_stand(self, card_count):
        if card_count < 17:
            self.hit_stand = "Hit"
        else:
            self.hit_stand = "Stand"
        return self.hit_stand


class Game():
    def __init__(self, p_hand, d_hand, cash=100):
        self.p_hand = p_hand
        self.d_hand = d_hand
        self.cash = cash

    def blackjack(self, p_hand, d_hand, cash):
        if d_hand < p_hand <= 21:
            self.cash = cash + 20
        elif d_hand == p_hand:
            self.cash = cash + 10
        else:
            return self.cash


if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()
    print(deck)
    hand = Hand(deck)
    hand.draw_from()
    print(hand)
