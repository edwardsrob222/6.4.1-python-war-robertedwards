from random import shuffle, random
# Card, Deck, Player, and Game

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    #check if card is red or black
    def isBlackOrRed(self):
        if self.suit == "hearts" or self.suit == "diamonds":
            return "red"
        else:
            return "black"

    def isNumberCard(self):
        numberCards = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        for numberCard in numberCards:
            if self.value == numberCard:
                return True
            else:
                return False

    def isFaceCard(self):
        faceCards = [11, 12, 13]
        for faceCard in faceCards:
            if self.value == faceCard:
                return True
            else:
                return False

    def isAceCard(self):
        aceCards = [14]
        for aceCard in aceCards:
            if self.value == aceCard:
                return True
            else:
                return False




class Deck:
    def __init__(self):
        self.deck = []

    def isFullDeck(self):
        suits = ["clubs", "diamonds", "hearts", "spades"]
        for suit in suits:
            for value in range(1, 14):
                self.stack.append(card(suit, value))
# class Player:
#     def __init__(self):
#         self. =
#         self. =
#         print()
#
#
# class Game:
#     def __init__(self):
#         self. =
#         self. =
#         print()
