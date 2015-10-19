""" Noted problems.
1. Allow only one split.
2. Allow double down on split, and check player bankroll to see if it can afford. But doesn't check if
 both splits are double down if player bankroll can afford
3. Doesn't allow splitting of tens if different rank
Clean up bust
"""


import random




class Card:
    """Standard Card Class"""
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

        :param dealer: of class Dealer
        :param player: of class Player
        :return: None
        """
        self.shuffle()
        for x in range(2):
            dealer.hand.cards.append(self.cards.pop())
            player.hand.cards.append(self.cards.pop())

    def deal(self, hand):
        """
        Deal one card to hand. Display card, and hand value.
        :param hand: hand of Hand class
        :return:None
        """
        hand.cards.append(self.cards.pop())
        print(hand.cards[-1], end=", ")
        print("Hand Total: {}".format(hand.value), end="   ")

    def deal_split(self, hand):
        """
        Deal one card to hand without display
        :param hand: hand of Hand class
        :return:
        """
        hand.cards.append(self.cards.pop())

class Shoe(Deck):
    """Compile 6 decks into one shoe"""
    def __init__(self):
        self.deck = []
        self.cards = []
        for suit in ['Club', 'Diamond', 'Heart', 'Spade']:
            for rank in ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10,
                         'J', 'Q', 'K']:
                self.deck.append(Card(suit, rank))
        for cd in self.deck:
            self.cards.extend([cd, cd, cd, cd, cd, cd])


class Hand:
    """Hand class with attributes list-cards, int-bet, bool-surrender, and value"""
    def __init__(self, bet=0):
        self.cards = []
        self.bet = bet
        self.surrender = False

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
            if h_value < 12:
                h_value += 10
        return h_value

    def bet_amount(self, player):
        """

        :param player: Request bet size from player
        :return:
        """
        while self.bet == 0:
            try:
                self.bet = int(input("How much do you want to bet?"))
                if self.bet > player.bankroll:
                    print("You don't have that much to bet!")
                    self.bet = 0
            except ValueError:
                print("Please only a number")

    def is_blackjack(self):
        """Checks for blackjack"""
        if len(self.cards) == 2 and self.value == 21:
            return True

    def show_hand(self):
        """shows hand"""
        for card in self.cards:
            print(card, end=", ")
        print("Hand Total: {}".format(self.value), end="   ")

    def __str__(self):
        doodle = ""
        for card in self.cards:
            doodle += " " + str(card)
        return doodle

class Player:
    """Player class with attributes string(name), int(bankroll), Hand-class(hand), list(hand_list)"""
    def __init__(self, name):
        self.name = name
        self.bankroll = 100
        self.hand = Hand()
        self.hand_list = []

    def __str__(self):
        return self.name

    def show_bankroll(self):
        print("")
        print("You have ${}".format(self.bankroll))
        print("")


class Dealer:
    """Class Dealer with attribute Hand-class(hand)"""
    def __init__(self):
        self.hand = Hand()

    def show_up_card(self, player):
        """
        Print dealer up card. If up card is 'A' Ace, offer insurance.
        :param player: Player
        :return:insurance bet amount, default=0
        """
        print("")
        print("Dealer up card: {} \n".format(self.hand.cards[0]))
        ins_bet = 0
        if self.hand.cards[0].rank == 'A':
            player.hand.show_hand()
            ins = input("Buy insurance? [Y]es or [N}o").lower()
            if ins == 'y'or ins == 'yes':
                ins_bet = player.hand.bet / 2
        return ins_bet

    def reveal_down_card(self, deck):
        """Show down card and deal until hand.value >= 17
        Bad Function Name.
        :param deck: Deck
        :return:None
        """
        print("")
        print("Dealer hand: ")
        print(self.hand.cards[0], self.hand.cards[1], sep=", ", end=", ")
        print("Hand total: {}".format(self.hand.value), end="   ")
        while self.hand.value < 17:
            input("HIT ENTER for dealer hit")
            deck.deal(self.hand)

    def payout(self, player, hand):
        """
        Compare player hand and self.hand to see who wins. Adjust player bankroll.
        See Blackjack rules if any confusion
        :param player: Player
        :param hand: Hand
        :return: None
        """
        if self.hand.value > 21:
            print("Dealer Busts! You win!")
            input("Hit ENTER to continue")
            player.bankroll += hand.bet
            print("")
            print("YOU WIN ${}".format(hand.bet))
            player.show_bankroll()
        else:
            if self.hand.value > hand.value:
                print("")
                print("You lose ${}".format(hand.bet))
                input("Hit ENTER to continue")
                player.bankroll -= hand.bet
                player.show_bankroll()
            elif self.hand.value < hand.value:
                print("Your hand beat the dealer!")
                input("Hit ENTER to continue")
                print("")
                print("YOU WIN ${}".format(hand.bet))
                player.bankroll += player.hand.bet
                player.show_bankroll()
            else:
                print("You tie.")
                input("Hit ENTER to continue")
                player.show_bankroll()

class Turn:
    """ Turn class that calls player and deck"""
    def __init__(self, player, deck):
        self.player = player
        self.deck = deck

    def hit_or_stay(self, hand, split_count=0):
        """
        Checks for split, offers double down or surrender on first two cards only.
        :param hand: Player Hand
        :param split_count: count how many splits have occured
        :return: None
        """
        print("YOUR HAND:")
        hand.show_hand()
        stand = False
        done_splitting = False
        """stand = False while hand is in progress. done_splitting = True when a split is in progress"""
        while not stand:
            if len(hand.cards) == 2 and hand.cards[0].rank == hand.cards[1].rank and split_count == 0:
                """if split is an option"""
                split_decision = input("Would you like to split?")
                if split_decision == 'y' or split_decision == 'yes' or split_decision == 's':
                    if hand.bet > (self.player.bankroll/2):
                        print("You don't have enough to split")
                    else:
                        self.split(hand, split_count)
                        done_splitting = True
                        stand = True
            if not done_splitting:
                """first turn"""
                if len(hand.cards) == 2:
                    turn = input("[H]it, [S]tay, [D]ouble Down, or [X]Surrender").lower()
                    if turn == 'd' or turn == 'double':
                        self.double_down(hand, split_count)
                        stand = True
                    elif turn == 'h' or turn == 'hit':
                        self.deck.deal(hand)
                        if hand.value > 21:
                            stand = True
                    elif turn == 's' or turn == 'stay':
                        print("Player stands.")
                        stand = True
                    elif turn == 'x' or turn == 'surrender':
                        hand.surrender = True
                        stand = True
                    else:
                        print("Try again.")
                else:
                    """2nd turn through end of turn executed here"""
                    turn = input("[H]it or [S]tay?").lower()
                    if turn == 'h' or turn == 'hit':
                        self.deck.deal(hand)
                        if hand.value > 21:
                            stand = True
                    elif turn == 's' or turn == 'stay':
                        print("Player stands.")
                        stand = True
                    else:
                        print("Try again.")

        if not done_splitting:
            self.player.hand_list.append(hand)


    def split(self, hand, split_count):
        """
        Splits hand and deals to both hands. Returns a split count
        :param hand: Hand to be split
        :param split_count: count how many splits have occured
        :return:
        """
        split_count += 1
        hand1 = hand
        hand2 = Hand(self.player.hand.bet)
        hand2.cards.append(hand.cards.pop(-1))
        print("HAND 1")
        self.deck.deal_split(hand1)
        self.hit_or_stay(hand1, split_count)
        print("HAND 2")
        self.deck.deal_split(hand2)
        self.hit_or_stay(hand2, split_count)

    def double_down(self, hand, split_count):
        """
        Double down. Adjust value of hand.bet, and deal hand one card.
        :param hand: Hand
        :param split_count: count how many splits have occured
        :return: None
        """
        if split_count > 0 and hand.bet > self.player.bankroll - (hand.bet * 2):
            print("You can only double for {}. You will double for this amount"
                  .format(self.player.bankroll - (hand.bet * 2)))
            hand.bet += (self.player.bankroll - hand.bet)
        elif hand.bet > (self.player.bankroll / 2):
            print("You can only double for {}. You will double for this amount"
                  .format(self.player.bankroll - hand.bet))
            hand.bet += (self.player.bankroll - hand.bet)
        else:
            hand.bet *= 2
        self.deck.deal(hand)

class Game:
    """Game class with attributes bool(running), bool(play_shoe), Player, and Dealer"""
    def __init__(self, player):
        self.running = True
        self.play_shoe = True
        self.player = player
        self.dealer = Dealer()

    def play_again(self):
        """Ask to play again. If yes, reset hands and bet amounts"""
        play = None
        while play is None:
            play = input("Would you like to play again? [Y]es or [N]o > ").lower()
            if play == 'y' or play == 'yes':
                self.player.hand.cards = []
                self.dealer.hand.cards = []
                self.player.hand.bet = 0
                self.player.hand_list = []
                self.player.hand.surrender = False
                play = True
            elif play == 'n' or play == 'no':
                self.running = False
                play = False
                self.play_shoe = False
            else:
                print("Only [Y]es or [N]o please")
                play = None

    def blackjack(self, insurance):
        """
        Check for blackjack. Pay insurance bet if there is one.
        :param insurance: int of insurance bet
        :return: bool of whether there is a blackjack
        """
        if self.dealer.hand.is_blackjack() and self.player.hand.is_blackjack():
            self.display_hands()
            print("You both got BlackJack!")
            if insurance > 0:
                self.player.bankroll += insurance * 2
                print("You lost ${}".format(insurance))
            self.player.show_bankroll()
            self.play_again()
            return True
        elif self.dealer.hand.is_blackjack():
            self.display_hands()
            print("Dealer Blackjack!")
            if insurance > 0:
                self.player.bankroll += insurance * 2
            self.player.bankroll -= self.player.hand.bet
            self.player.show_bankroll()
            self.play_again()
            return True
        elif self.player.hand.is_blackjack():
            self.display_hands()
            print("You got BlackJack!")
            if insurance > 0:
                self.player.bankroll -= insurance
                print("You got even money")
            self.player.bankroll += (self.player.hand.bet * 1.5)
            self.player.show_bankroll()
            self.play_again()
            return True

    def display_hands(self):
        """Not sure I even use this"""
        print("Player Hand: {}, {}".format(self.player.hand.cards[0], self.player.hand.cards[1]))
        print("Dealer Hand: {}, {}".format(self.dealer.hand.cards[0], self.dealer.hand.cards[1]))

    def start(self):
        """Game Here. Needs cleanup"""
        print("Welcome to Blackjack {}! You start with ${}".format(self.player.name, self.player.bankroll))
        is_split = False
        while self.running:
            if self.player.bankroll <= 0:
                print("You're broke. STOP GAMBLING!")
                self.running = False
            else:
                print("")
                new_shoe = Shoe()
                new_shoe.shuffle()
                while len(new_shoe.cards) > 26 and self.play_shoe:
                    if self.player.bankroll <= 0:
                        print("You're broke. STOP GAMBLING!")
                        self.running = False
                        self.play_shoe = False
                    else:
                        self.player.hand.bet_amount(self.player)
                        new_shoe.initial_deal(self.dealer, self.player)
                        #WRITE TESTS! WRITE TESTS!
                        #self.dealer.hand.cards = []
                        #ace = Card('Spade', 'A')
                        #ten = Card('Heart', 'A')
                        #self.dealer.hand.cards.extend([ace, ten])
                        #self.player.hand.cards = []
                        #jack = Card('Spade', 6)
                        #queen = Card('Heart', 6)
                        #self.player.hand.cards.extend([jack, queen])
                        insurance = self.dealer.show_up_card(self.player)
                        if not self.blackjack(insurance):
                            if insurance > 0:
                                self.player.bankroll -= insurance
                                print("You lost ${} for insurance".format(insurance))
                                self.player.show_bankroll()
                            player_turn = Turn(Bob, new_shoe)
                            player_turn.hit_or_stay(self.player.hand)

                            count = 0
                            surrender_count = 0
                            all_surrender = False
                            for hand in self.player.hand_list:
                                if hand.surrender:
                                    print(hand)
                                    print("You surrendered this hand. You lose ${}".format(hand.bet/2))
                                    print("DEALER HAND: {}, {}".format(self.dealer.hand.cards[0],
                                                                       self.dealer.hand.cards[1]))
                                    self.player.bankroll -= (hand.bet / 2)
                                    self.player.show_bankroll()
                                    surrender_count += 1
                                elif hand.value <= 21:
                                    count+= 1
                            if surrender_count == len(self.player.hand_list):
                                all_surrender = True

                            if count == 0 and not all_surrender:
                                for hand in self.player.hand_list:
                                    print("")
                                    print("You busted. You lose ${}".format(hand.bet))
                                    print("")
                                    print("Dealer Hand: {}, {}".format(self.dealer.hand.cards[0], self.dealer.hand.cards[1]))
                                    self.player.bankroll -= hand.bet
                                    self.player.show_bankroll()
                            if count > 0:
                                self.dealer.reveal_down_card(new_shoe)
                                for hand in self.player.hand_list:
                                    if not hand.surrender:
                                        if hand.value > 21:
                                            print(hand)
                                            print("This hand busted. You lose ${}".format(hand.bet))
                                            self.player.bankroll -= hand.bet
                                            self.player.show_bankroll()
                                        else:
                                            self.dealer.payout(self.player, hand)
                            self.play_again()


if __name__ == '__main__':
    Bob = Player('Bob')
    new_game = Game(Bob)
    new_game.start()