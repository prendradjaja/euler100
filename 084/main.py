import random
from collections import namedtuple, Counter
import re
import itertools


from deck import Deck
from data import cards, board


def main():
    counts = Counter()
    for location in itertools.islice(indices(), 1_000_000):
        counts[location] += 1
    total = sum(counts.values())
    for location, count in counts.most_common(5):
        percent = count / total * 100
        print(location, board[location], f'{percent:.3f}%', sep='\t')


def indices():
    g = Game()
    while True:
        yield g.location
        g.take_turn()


Square = namedtuple('Square', 'typename num')

def parse_square(square):
    '''
    >>> parse_square('C1')
    Square(typename='C', num=1)
    >>> parse_square('CH1')
    Square(typename='CH', num=1)
    >>> parse_square('JAIL')
    Square(typename='JAIL', num=None)
    >>> parse_square('G2J')
    Square(typename='G2J', num=None)
    '''
    if square == 'G2J':
        return Square('G2J', None)

    match = re.fullmatch(r'([A-Z]+)([0-9]*)', square)
    if match[2]:
        num = int(match[2])
    else:
        num = None
    return Square(match[1], num)


class Game:
    def __init__(self):
        self.location = 0
        self.doubles = 0
        self.decks = {}
        self.decks['CH'] = Deck(cards['CH'])
        self.decks['CC'] = Deck(cards['CC'])


    def take_turn(self):
        roll = self.roll()
        if roll == 'JAIL':
            self.location = board.index('JAIL')
        else:
            self.location += roll
            self.location %= len(board)

        square = board[self.location]
        if square == 'G2J':
            self.location = board.index('JAIL')
        elif square.startswith('CH') or square.startswith('CC'):
            deck = self.decks[square[:2]]
            card = deck.draw()
            if card is None:
                pass
            elif '*' in card:
                typename = card.split('*')[0]
                self.location = self.find_next_square_of_type(typename)
            elif '-' in card:
                offset = int(card.split('-')[1])
                self.location -= offset
                self.location %= len(board)
            else:
                self.location = board.index(card)


    def find_next_square_of_type(self, typename):
        '''
        >>> g = Game()
        >>> g.location = g.find_next_square_of_type('R')
        >>> board[g.location]
        'R1'
        >>> g.location = g.find_next_square_of_type('R')
        >>> board[g.location]
        'R2'
        >>> g.location = g.find_next_square_of_type('R')
        >>> g.location = g.find_next_square_of_type('R')
        >>> g.location = g.find_next_square_of_type('R')
        >>> board[g.location]
        'R1'
        '''
        location = self.location + 1
        while parse_square(board[location]).typename != typename:
            location += 1
            location %= len(board)
        return location


    def roll(self):
        DIE_SIDES = 6
        a = random.randint(1, DIE_SIDES)
        b = random.randint(1, DIE_SIDES)

        if a == b:
            self.doubles += 1
        else:
            self.doubles = 0

        if self.doubles == 3:
            self.doubles = 0
            return 'JAIL'
        else:
            return a + b


if __name__ == '__main__':
    main()
