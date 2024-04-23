# DO NOT CHANGE THIS FILE

from card_utility import RANKS
from card_utility import SUITS

class Card:
    def __init__(self, id):
        self.__id = id

    # Return the id of the card
    def get_id(self):
        return self.__id

    # Return the rank of the card
    def get_rank(self):
        return RANKS[self.__id % len(RANKS)]

    # Return the suit of the card
    def get_suit(self):
        return SUITS[self.__id // len(RANKS)]

    # This returns a string to print when printing this object
    def __repr__(self):
        return self.get_rank() + " of " + self.get_suit()