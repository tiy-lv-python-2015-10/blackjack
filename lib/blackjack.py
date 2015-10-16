import random


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    @property
    def value(self):
        if self.rank ==  'A':
            return 11
        elif self.rank in ['J', 'Q', 'K']:
            return 10
        else:
            return self.rank

    def __str__(self):
        return "{}-{}".format(self.rank, self.suit)


class Deck:
    """Create a deck of cards using class Card"""
    def __init__(self):
        self.cards = []
        for suit in ['Club', 'Diamond', 'Heart', 'Spade']:
            for rank in ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10,
                         'J', 'Q', 'K']:
                self.cards.append(Card(suit, rank))

    def __str__(self):
        return "Deck of cards"

    def shuffle(self):
        random.shuffle(self.cards)

    def initial_deal(self, dealer, player):
        """Deal 2 cards from deck to player and dealer

        :param dealer: of class Dealer type
        :param player: of class Player typ
        :return: None
        """
        self.shuffle()
        for x in range(2):
            dealer.hand.cards.append(self.cards.pop())
            player.hand.cards.append(self.cards.pop())

    def deal(self, player):
        player.hand.cards.append(self.cards.pop())
        print(player.hand.cards[-1], end=", ")
        print("Hand Total: {}".format(player.hand.value), end="   ")

class Hand:
    def __init__(self):
        self.cards = []

    @property
    def value(self):
        h_value = 0
        aces = 0
        for card in self.cards:
            h_value += card.value
            if card.rank == 'A':
                aces += 1
        if h_value > 21 and aces >= 1:
            while aces > 0:
                h_value -= 10
                aces -= 1
            if h_value < 11:
                h_value += 10
        return h_value

    def is_blackjack(self):
        if len(self.cards) == 2 and self.value == 21:
            return True

    def __str__(self):
        return "Your hand = {}".format(self.value)

class Player:
    def __init__(self, name):
        self.name = name
        self.bankroll = 100
        self.hand = Hand()
        self.bet = 0

    def bet_amount(self):
        while self.bet == 0:
            try:
                self.bet = int(input("How much do you want to bet?"))
                if self.bet > self.bankroll:
                    print("You don't have that much to bet!")
                    self.bet = 0
            except ValueError:
                print("Please only a number")

    def __str__(self):
        return self.name

    def show_hand(self):
        print("Your hand: ")
        for card in self.hand.cards:
            print(card, end=", ")
        print("Hand Total: {}".format(self.hand.value), end="   ")

    def stay(self):
        pass

    def show_bankroll(self):
        print("You have ${}".format(self.bankroll))


class Dealer:
    def __init__(self):
        self.hand = Hand()

    def show_up_card(self):
        print("Dealer up card: {} \n".format(self.hand.cards[0]))

    def reveal_down_card(self, deck):
        print("")
        print("Dealer hand: ")
        print(self.hand.cards[0], self.hand.cards[1], sep=", ", end=", ")
        print("Hand total: {}".format(self.hand.value), end="   ")
        while self.hand.value < 17:
            input("HIT ENTER for dealer hit")
            deck.deal(self)

    def payout(self, player):
        if self.hand.value > 21:
            print("Dealer Busts! You win!")
            input("Hit ENTER to continue")
            player.bankroll += player.bet
            player.show_bankroll()
        elif self.hand.value > player.hand.value:
            print("Sorry. You lose.")
            input("Hit ENTER to continue")
            player.bankroll -= player.bet
            player.show_bankroll()
        elif self.hand.value < player.hand.value:
            print("Congrats! You win!")
            input("Hit ENTER to continue")
            player.bankroll += player.bet
            player.show_bankroll()
        else:
            print("You tie!")
            input("Hit ENTER to continue")
            player.show_bankroll()


class Turn:
    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer

    def hit_or_stay(self, deck):
        self.player.show_hand()
        while(self.player.hand.value <= 21):
            turn = input("[H]it or [S]tay?").lower()
            if turn[0] == 'h':
                deck.deal(self.player)
                if self.player.hand.value > 21:
                    self.bust()
                    return False
            elif turn[0] == 's':
                return True

    def bust(self):
        print("Sorry you busted")
        print("Dealer Hand: {}, {}".format(self.dealer.hand.cards[0], self.dealer.hand.cards[1]))
        input("Hit ENTER to continue")
        self.player.bankroll -= self.player.bet
        self.player.show_bankroll()

class Game:

    def __init__(self, player):
        self.running = True
        self.player = player
        self.dealer = Dealer()

    def play_again(self):
        play = None
        while play is None:
            play = input("Would you like to play again? [Y]es or [N]o > ").lower()
            if play == 'y' or play == 'yes':
                self.player.hand.cards = []
                self.dealer.hand.cards = []
                self.player.bet = 0
                play = True
            elif play == 'n' or play == 'no':
                self.running = False
                play = False
            else:
                print("Only [Y]es or [N]o please")
                play = None

    def blackjack(self):
        if self.dealer.hand.is_blackjack() and self.player.hand.is_blackjack():
            self.display_hands()
            print("You both got BlackJack!")
            self.player.show_bankroll()
            self.play_again()
            return True
        elif self.dealer.hand.is_blackjack():
            self.display_hands()
            print("Dealer Blackjack! You lose")
            self.player.bankroll -= self.player.bet
            self.player.show_bankroll()
            self.play_again()
            return True
        elif self.player.hand.is_blackjack():
            self.display_hands()
            print("You got BlackJack!")
            self.player.bankroll += (self.player.bet * 1.5)
            self.player.show_bankroll()
            self.play_again()
            return True

    def display_hands(self):
        print("Player Hand: {}, {}".format(self.player.hand.cards[0], self.player.hand.cards[1]))
        print("Dealer Hand: {}, {}".format(self.dealer.hand.cards[0], self.dealer.hand.cards[1]))

    def start(self):
        print("Welcome to Blackjack {}! You start with ${}".format(self.player.name, self.player.bankroll))
        while self.running:
            if self.player.bankroll <= 0:
                print("You're broke. STOP GAMBLING!")
                self.running = False
            else:
                print("")
                new_deck = Deck()
                new_deck.shuffle()
                self.player.bet_amount()
                new_deck.initial_deal(self.dealer, self.player)
               # self.player.hand.cards = []
                #ace = Card('S', 'J')
                #ten = Card('H', 6)
                #self.player.hand.cards.extend([ace, ten])
                self.dealer.show_up_card()

                if not self.blackjack():
                    player_turn = Turn(Bob, self.dealer)
                    if player_turn.hit_or_stay(new_deck):
                        self.dealer.reveal_down_card(new_deck)
                        self.dealer.payout(self.player)
                        self.play_again()
                    else:
                        self.play_again()


if __name__ == '__main__':
    Bob = Player('Bob')
    new_game = Game(Bob)
    new_game.start()