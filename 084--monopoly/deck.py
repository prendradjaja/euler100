import random

class Deck:
    def __init__(self, cards):
        self.cards = cards[:]
        random.shuffle(self.cards)
        self.used = []

    def draw(self):
        if not self.cards:
            self.restart()
        card = self.cards.pop(0)
        self.used.append(card)
        return card

    def restart(self):
        # N.B.: Problem description doesn't mention re-shuffling deck after
        # it's exhausted, but probably we want to
        self.cards = self.used
        random.shuffle(self.cards)
        self.used = []
