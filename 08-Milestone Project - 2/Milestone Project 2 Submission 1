"""
BLACKJACK GAME: Code by numbers (aka copied)
"""

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        # return f"{self.rank} of {self.suit}"
        return "%s of %s" % (self.rank, self.suit)


class Deck:

    def __init__(self):
        self.deck = []

        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        current_deck = '\n'.join([x.__str__() for x in self.deck])
        return current_deck

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:
    def __init__(self, total=100):  # starting bet of 100
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("Enter bet amount: "))
        except ValueError:
            print("Please enter number!")
        else:
            if chips.bet > chips.total:
                print("Count your chips again...")
                continue
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_stand(deck, hand):
    global playing

    while True:
        x = input("Would you like to Hit or Stand? (h/s)")

        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False
        else:
            print("Try again.")
            continue
        break


def show_some(player, dealer):
    print(f"\nDealer's Hand:\n <card hidden>\n {dealer.cards[1]}.")
    print(f"\nPlayer's Hand:", *player.cards, sep='\n ')


def show_all(player, dealer):
    print(f"\nDealer's Hand:", *dealer.cards, sep='\n ')
    print(f"\nPlayer's Hand:", *player.cards, sep='\n ')


def player_busts(chips):
    print("Player busts!")
    chips.lose_bet()


def player_wins(chips):
    print("Player wins!")
    chips.win_bet()


def dealer_busts(chips):
    print("Dealer busts!")
    chips.win_bet()


def dealer_wins(chips):
    print("Dealer wins!")
    chips.lose_bet()


def push():
    print("Dealer and Player tie! It's a push.")


while True:
    print("Welcome to Blackjack!\n    Dealer hits to 17. Aces count as 1 or 11.\n    21 OR BUST!\n\n")

    # Create and shuffle deck
    deck = Deck()
    deck.shuffle()

    # Create and deal hands
    player_hand = Hand()
    dealer_hand = Hand()

    # Card 1
    player_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    # Card 2
    player_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Check if pot exists from previous hands or create a new one with 100
    try:
        player_chips = Chips(carry_pot)
    except NameError:
        player_chips = Chips()

    # Ask for bet
    take_bet(player_chips)

    # Card Reveal
    show_some(player_hand, dealer_hand)

    # for card in player_hand.cards:
    #     print(card)
    while playing:
        # Ask player for hit or stand
        hit_stand(deck, player_hand)

        show_some(player_hand, dealer_hand)

        # Check for player bust
        if player_hand.value > 21:
            player_busts(player_chips)
            break

    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        # Check win scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_chips)

        else:
            push()

    # scores
    print("Dealer score= " + str(dealer_hand.value))
    print("Player score= " + str(player_hand.value))

    # Post game pot
    print("\nPlayer pot stands at " + str(player_chips.total))

    # Ask new game
    new_game = input("Would you like to play another hand? (Y/N)")

    if new_game[0].lower() == 'y':
        playing = True
        carry_pot = player_chips.total
        continue
    else:
        print("Thanks for playing!")
        break
