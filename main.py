import random

class Deck:
    def __init__(self):
        self.cards = []
        self.suits = ['spades', 'clubs', 'hearts', 'diamonds']
        self.ranks = [
                {"rank":'2', "value":2},
                {"rank":'3', "value":3},
                {"rank":'4', "value":4},
                {"rank":'5', "value":5},
                {"rank":'6', "value":6},
                {"rank":'7', "value":7},
                {"rank":'8', "value":8},
                {"rank":'9', "value":9},
                {"rank":'10', "value":10},
                {"rank":'J', "value":10},
                {"rank":'Q', "value":10},
                {"rank":'K', "value":10},
                {"rank":'A', "value":11}
                ]

        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append([suit, rank])


    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self, number):
        cards_dealt = []
        
        for n in range(number):
            if len(self.cards) > 0:
                card = cards.pop(n)
                cards_dealt.append(card)
        return cards_dealt

deck1 = Deck()
deck2 = Deck()
deck2.shuffle()

print(deck1.cards)
print(deck2.cards)
