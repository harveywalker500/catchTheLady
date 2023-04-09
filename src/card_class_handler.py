import random


class Card:
    """
    This class represents a playing card with a suit and a value.

    Attributes:
    suit (str): the suit of the card (e.g. "hearts", "diamonds", "clubs", "spades").
    value (str): the value of the card (e.g. "ace", "2", "3", ..., "10", "jack", "queen", "king").

    Methods:
    __str__: returns a string representation of the card in the format "value of suit".
    __repr__: returns a string representation of the card,
    which is the same as the string representation returned by __str__.
    """

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

    def __repr__(self):
        return self.__str__()


class CardProperties:
    """
    This is a class that represents a list of possible suits and values for a deck of cards.

    Attributes:
    suit_list (list): a list of possible suits for a card (e.g. "hearts", "diamonds", "clubs", "spades").
    value_list (list): a list of possible values for a card (e.g. "ace", "2", "3", ..., "10", "jack", "queen", "king").

    Methods:
    __init__: initializes a CardProperties instance with the specified suits and values.
    extract_suit_list_from_file: extracts a list of suits from a file.
    extract_value_list_from_file: extracts a list of values from a file.
    """
    suit_list = ["Hearts", "Diamonds", "Spades", "Clubs"]
    value_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "Ace"]

    def __init__(self, suits=None, values=None):
        if suits is not None:
            self.suit_list = suits
        else:
            self.suit_list = ["Hearts", "Diamonds", "Spades", "Clubs"]

        if values is not None:
            self.value_list = values
        else:
            self.value_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "Ace"]

    def extract_suit_list_from_file(self, filename):
        try:
            with open(filename, "r") as suit_list_file:
                self.suit_list = suit_list_file.readlines()
        except FileNotFoundError:
            print("ERROR: File not found.")

    def extract_value_list_from_file(self, filename):
        try:
            with open(filename, "r") as value_list_file:
                self.value_list = value_list_file.readlines()
        except FileNotFoundError:
            print("ERROR: File not found.")


class Deck:
    """
    This is a class that represents a deck of the Cards class.

    Attributes:
    deck (list): a list containing the cards in the deck.

    Methods:
    init: initializes a deck instance.
    str: returns a string representation of a deck instance.
    show_entire_card_deck: prints the entire deck of cards.
    """
    deck = []

    def __init__(self, nof_card_packs, shuffled, value_list, suit_list):
        for pack in range(nof_card_packs):
            self.deck += [Card(suit, value) for value in value_list for suit in suit_list]

        if shuffled is True:
            random.shuffle(self.deck)

    def __str__(self):
        return f"{len(self.deck)} cards in deck."

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self.deck)

    def __getitem__(self, index):
        return self.deck[index]

    def show_entire_card_deck(self):
        for i in range(len(self.deck)):
            print(self.deck[i])

    def draw_from_top(self, num_cards=1):
        drawn_cards = []
        for i in range(num_cards):
            if len(self.deck) > 0:
                drawn_cards.append(self.deck.pop(0))
            else:
                break
        return drawn_cards

    def draw_from_bottom(self, num_cards=1):
        drawn_cards = []
        for i in range(num_cards):
            if len(self.deck) > 0:
                drawn_cards.append(self.deck.pop(len(self.deck)))
            else:
                break
        return drawn_cards

    def show_top_card(self):
        return self.deck[0]

    def cut_deck(self):
        cut_point = random.randint(0, 25)
        cut_1 = []
        for i in range(cut_point):
            cut_1.append(self.deck[i])
            self.deck.pop(i)
        self.deck = self.deck + cut_1


class Player:
    def __init__(self):
        self.hand = []
        self.cards_won = []
        self.score = 0

    def __str__(self):
        return f"""Hand: {self.hand}, Score: {self.score}"""

    def __repr__(self):
        return self.__str__()

    def determine_score(self):
        for i in self.cards_won:
            match i.value:
                case "A":
                    self.score += 15
                case "K", "J", 10:
                    self.score += 10
                case "Q":
                    if i.suit == "S":
                        self.score += 30
                case _:
                    self.score += i
