import random

class Card:
    '''
    Card constructor
    Parameters: suit->string, value->string, card_value->int
    Return values: none
    '''
    def __init__(self, suit, value, card_value):
        self.suit = suit
        self.value = value
        self.card_value = card_value

class Deck:
    '''
    Deck constructor
    Parameters: num->int
    Return values: none
    '''
    def __init__(self, num=1):
        suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
        suit_values = {"Spades": "\u2664", "Hearts": "\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}
        cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        card_values = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10,
                        "Q": 10, "K": 10}

        dummy_deck = []

        for suit in suits:
            for card in cards:
                dummy_deck.append(Card(suit_values[suit], card, card_values[card]))

        self.deck = dummy_deck*num
        
    def hit(self):
        if len(self.deck) > 1:
            return self.deck.pop(0)
        
    def shuffle(self):
        if len(self.deck) > 1:
            random.shuffle(self.deck)

    def deck_size(self):
        return len(self.deck)

class Hand:
    def __init__(self, dealer=False):
        self.dealer = dealer
        self.hand = []
        self.value = 0

    def add_card(self, card):
        self.hand.append(card)

    def calculate_hand(self):
        self.value = 0
        has_ace = False
        for card in self.hand:
            if card.value == "A":
                has_ace = True
            self.value += card.card_value

        if has_ace and self.value > 21:
            self.value -= 10

    def get_hand_value(self):
        self.calculate_hand()
        return self.value

    def clear_hand(self):
        self.hand: []
        self.value = 0

    def check_hand_result(self):
        if self.value > 21:
            return "Bust!"
        elif self.value == 21:
            return "BlackJack!"
        return ""

'''
Prints the cards in a hand
Parameters: cards->list(card), hidden->bool
Return values: none
'''
def print_cards(cards, hidden):
    if not hidden:
        s = ""
        for card in cards:
            s = s + "\t ________________"
        # if hidden:
        #     s += "\t ________________"
        print(s)

        s = ""
        for card in cards:
            s = s + "\t|                |"
        # if hidden:
        #     s += "\t|                |"
        print(s)

        s = ""
        for card in cards:
            if card.value == '10':
                s = s + "\t|  {}            |".format(card.value)
            else:
                s = s + "\t|  {}             |".format(card.value)
        # if hidden:
        #     s += "\t|                |"
        print(s)

        s = ""
        for card in cards:
            s = s + "\t|                |"
        # if hidden:
        #     s += "\t|      * *       |"
        print(s)

        s = ""
        for card in cards:
            s = s + "\t|                |"
        # if hidden:
        #     s += "\t|    *     *     |"
        print(s)

        s = ""
        for card in cards:
            s = s + "\t|                |"
        # if hidden:
        #     s += "\t|   *       *    |"
        print(s)

        s = ""
        for card in cards:
            s = s + "\t|                |"
        # if hidden:
        #     s += "\t|   *       *    |"
        print(s)

        s = ""
        for card in cards:
            s = s + "\t|       {}        |".format(card.suit)
        # if hidden:
        #     s += "\t|          *     |"
        print(s)

        s = ""
        for card in cards:
            s = s + "\t|                |"
        # if hidden:
        #     s += "\t|         *      |"
        print(s)

        s = ""
        for card in cards:
            s = s + "\t|                |"
        # if hidden:
        #     s += "\t|        *       |"
        print(s)

        s = ""
        for card in cards:
            s = s + "\t|                |"
        # if hidden:
        #     s += "\t|                |"
        print(s)

        s = ""
        for card in cards:
            s = s + "\t|                |"
        # if hidden:
        #     s += "\t|                |"
        print(s)

        s = ""
        for card in cards:
            if card.value == '10':
                s = s + "\t|            {}  |".format(card.value)
            else:
                s = s + "\t|            {}   |".format(card.value)
        # if hidden:
        #     s += "\t|        *       |"
        print(s)

        s = ""
        for card in cards:
            s = s + "\t|________________|"
        # if hidden:
        #     s += "\t|________________|"
        print(s)
    else:
        s = ""
        s = s + "\t ________________"
        s += "\t ________________"
        print(s)

        s = ""
        s = s + "\t|                |"
        s += "\t|                |"
        print(s)

        s = ""
        if cards[0].value == '10':
            s = s + "\t|  {}            |".format(cards[0].value)
        else:
            s = s + "\t|  {}             |".format(cards[0].value)
        s += "\t|                |"
        print(s)

        s = ""
        s = s + "\t|                |"
        s += "\t|      * *       |"
        print(s)

        s = ""
        s = s + "\t|                |"
        s += "\t|    *     *     |"
        print(s)

        s = ""
        s = s + "\t|                |"
        s += "\t|   *       *    |"
        print(s)

        s = ""
        s = s + "\t|                |"
        s += "\t|   *       *    |"
        print(s)

        s = ""
        s = s + "\t|       {}        |".format(cards[0].suit)
        s += "\t|          *     |"
        print(s)

        s = ""
        s = s + "\t|                |"
        s += "\t|         *      |"
        print(s)

        s = ""
        s = s + "\t|                |"
        s += "\t|        *       |"
        print(s)

        s = ""
        s = s + "\t|                |"
        s += "\t|                |"
        print(s)

        s = ""
        s = s + "\t|                |"
        s += "\t|                |"
        print(s)

        s = ""
        if cards[0].value == '10':
            s = s + "\t|            {}  |".format(cards[0].value)
        else:
            s = s + "\t|            {}   |".format(cards[0].value)
        s += "\t|        *       |"
        print(s)

        s = ""
        s = s + "\t|________________|"
        s += "\t|________________|"
        print(s)

    print()

class Game:
    def __init__(self):
        self.deck = Deck(2)

    def play(self):
        playing = True
        self.deck.shuffle()
        while playing and self.deck.deck_size() > 4:
            self.player_hand = Hand()
            self.dealer_hand = Hand(True)

            player_blackjack = False
            player_bust = False
            dealer_blackjack = False
            dealer_bust = False

            # deals 2 cards
            for _ in range(2):
                self.player_hand.add_card(self.deck.hit())
                self.dealer_hand.add_card(self.deck.hit())

            # displays both hands
            print("Player hand:")
            print(f"Points: {self.player_hand.get_hand_value()}")
            if self.player_hand.get_hand_value() > 21:
                print("Bust!")
                player_bust = True
            elif self.player_hand.get_hand_value() == 21:
                print("BlackJack!")
                player_blackjack = True
            print_cards(self.player_hand.hand, False)
            print()
            print("Dealer hand:")
            print("Points: ???")
            print_cards(self.dealer_hand.hand, True)

            # if game over, deal a new hand
            # start the loop over again
            if player_bust or player_blackjack:
                play_again = input("Deal a new hand? (yes, y, no, n): ").lower()
                while play_again not in ["yes", "y", "no", "n"]:
                    print("Invalid input. Try again. ")
                    play_again = input("Deal a new hand? (yes, y, no, n): ").lower()
                if play_again in ["yes", "y"]:
                    playing = True
                    break
                else:
                    playing = False
                    break

            if not player_bust and not player_blackjack and playing:
                player_move = input("Hit or Stand? (hit, h, stand, s): ").lower()
                moves = ["hit", "h", "stand", "s"]

                # Player's turn
                while player_move not in moves:
                    print("Invalid input. Try again.")
                    player_move = input("Hit or Stand? (hit, h, stand, s): ").lower()

                while player_move in ["hit", "h"]:
                    self.player_hand.add_card(self.deck.hit())

                    print("Player hand:")
                    print(f"Points: {self.player_hand.get_hand_value()}")
                    print_cards(self.player_hand.hand, False)
                    if self.player_hand.get_hand_value() > 21:
                        print("Bust! You lose!")
                        player_bust = True
                        break
                    elif self.player_hand.get_hand_value() == 21:
                        print("BlackJack! You win!")
                        player_blackjack = True
                        break
                    print()
                    print("Dealer hand:")
                    print("Points: ???")
                    print_cards(self.dealer_hand.hand, True)
                    player_move = input("Hit or Stand? (hit, h, stand, s): ").lower()

                # Dealer's turn
                if player_move in ["stand", "s"]:
                    print("Player hand:")
                    print(f"Points: {self.player_hand.get_hand_value()}")
                    print_cards(self.player_hand.hand, False)

                    print()
                    print("Dealer hand:")
                    print(f"Points: {self.dealer_hand.get_hand_value()}")
                    print_cards(self.dealer_hand.hand, False)

                    while self.dealer_hand.get_hand_value() < 16:
                        self.dealer_hand.add_card(self.deck.hit())

                        print("Player hand:")
                        print(f"Points: {self.player_hand.get_hand_value()}")
                        print_cards(self.player_hand.hand, False)

                        print()
                        print("Dealer hand:")
                        print(f"Points: {self.dealer_hand.get_hand_value()}")
                        print_cards(self.dealer_hand.hand, False)

                    # Compare hands
                    if self.dealer_hand.get_hand_value() == 21:
                        print("Dealer wins!")
                    elif self.dealer_hand.get_hand_value() > 21:
                        print("Dealer bust! You win!")
                    elif self.dealer_hand.get_hand_value() > self.player_hand.get_hand_value():
                        print("Dealer wins!")
                    elif self.dealer_hand.get_hand_value() == self.player_hand.get_hand_value():
                        print("You tied with the dealer!")
                    else:
                        print("You win!")


                play_again = input("Deal a new hand? (yes, y, no, n): ").lower()
                while play_again not in ["yes", "y", "no", "n"]:
                    print("Invalid input. Try again. ")
                    play_again = input("Deal a new hand? (yes, y, no, n): ").lower()

                if play_again in ["yes", "y"]:
                    playing = True
                else:
                    playing = False

if __name__ == "__main__":
    game = Game()
    game.play()

# card1 = Card("\u2661", "A", 2)
# card2 = Card("\u2661", "2", 2)
# card_list = [card1, card2]
# print_cards(card_list, True)