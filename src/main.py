from card_class_handler import *


# Sets up the card deck
def setup_imports():
    cardProperties = CardProperties()
    f_deck = Deck(1, True, cardProperties.value_list, cardProperties.suit_list)
    return f_deck


if __name__ == "__main__":
    deck = setup_imports()
    players = []
    for i in range(5):
        players.append(Player())
    print(players)
