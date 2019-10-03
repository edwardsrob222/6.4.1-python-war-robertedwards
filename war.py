from random import randint
# Card, Deck, Player, and Game

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        print()
    #check if card is red or black
    def isBlackOrRed(self):
        if self.suit == "hearts" or self.suit == "diamonds":
            return "red"
        else:
            return "black"

    def isFaceCard(self):
        faceCards = [11, 12, 13]
        for faceCard in faceCards:
            if self.value == faceCard:
                return True
            else:
                return False


class Deck:
    def __init__(self, ):
        self. =
        self. =
        print()


class Player:
    def __init__(self):
        self. =
        self. =
        print()


class Game:
    def __init__(self):
        self. =
        self. =
        print()
