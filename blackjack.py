class Player:
    def __init__(self, hand):
        self.money = 100
        self.bet = 10
        self.hand = hand

    def hit(self):
        
        #retrieve a a random card from the deck
        #return the card
        pass


class Dealer(Player):
    def __int__(self):
        super().__init__()
        self.money = 0
        self.bet = 0


class Card:
    def __init__(self,suit,rank, cards):
        self.suit = suit
        self.rank = rank
        self.cards = cards

    @property
    def value(self):
        if rank == 'A':
            return 11
        elif rank in ['K','J','Q']:
            return 10
        else:
            return rank


class Deck():
    def __int__(self):
        suits = ["Diamond", "Spade", "Heart", "Club"]
        ranks = [1,2,3,4,5,6,7,8,9,10, 'J', 'Q', 'K', 'A']
        self.cards = [Card(suit,rank) for rank in ranks for suit in suits]




class Hand:
    def __init__(self, card_amount):
        self.card_amount = card_amount


class Game:
    def __init__(self, player, dealer):
        player.self = player
        dealer.self = dealer

    def initial cards(self):
        #give two cards to a player
        #give two cards to a dealer


    def start_game(self):
        player.place_bet()
        initial_cards()
        no_winner = True
        while no_winner = True

            def did_player_win():
                if player card count is > 21 && dealer card count < 21
                    #player loses, game over
                    #no_winner = false

                elif player card count < 21 && dealer card count > 21
                    #player wins, game over
                    #no_winner = false

                elif player card count > dealer card count && dealer card count >= 17
                    #player wins, game over
                    #no_winner = false

                elif player_card_count == dealer card count && dealer card count >= 17
                    # no money lost or gained, game over
                    #no_winner = false

                else
                    if dealer card count < 17;
                        # make dealer hit
                        #add amount dealer hit to his total hand

                    #ask player if he wants to hit or stand
                    if player hits
                        #make player hit
                        #add a new card to his hand && loop back up to check the conditions above

                    elif player stands
                        #make player stand
                        #dont add a new card to his hand && loop bakc up to check the conditions above

        #display who won
        #Deduct money from player if player lost and add it to dealer
        #Add money to player and remove from dealer if player won

if __name__ == '__main__':
player1 = Player()
dealer1 = Dealer()
game1 = Game(player1, dealer1)
game1.start_game()




