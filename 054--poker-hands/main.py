import collections

def main():
    wins = 0
    for line in open('./input.txt'):
        cards = line.strip().split()
        hands = cards[:5], cards[5:]
        value1, value2 = (get_comparison_value(h) for h in hands)

        # I only implemented the minimum sufficient tiebreaking logic to solve
        # the given input. If e.g. both players have four of a kind, the
        # player whose quad is of greater rank should win, but this is
        # unimplemented. These sorts of tiebreaks can be implemented in
        # get_comparison_value() similarly to how Two of a Kind's tiebreak is
        # implemented.
        assert value1 != value2, "Unimplemented comparison"

        if value1 > value2:
            wins += 1
    print(wins)

def get_value(card):
    value = card[0]
    try:
        return int(value)
    except ValueError:
        return {
            'T': 10,
            'J': 11,
            'Q': 12,
            'K': 13,
            'A': 14,
        }[value]

def get_suit(card):
    return card[1]

def get_comparison_value(hand):
    """
    >>> get_comparison_value('AS KS QS JS TS'.split())[1]
    'Royal Flush'
    >>> get_comparison_value('KS QS JS TS 9S'.split())[1]
    'Straight Flush'
    >>> get_comparison_value('8S 8C 8D 8H 3S'.split())[1]
    'Four of a Kind'
    >>> get_comparison_value('8S 8C 8D 3H 3S'.split())[1]
    'Full House'
    >>> get_comparison_value('2S QS JS TS 9S'.split())[1]
    'Flush'
    >>> get_comparison_value('KD QS JS TS 9S'.split())[1]
    'Straight'
    >>> get_comparison_value('8S 8C 8D 4H 3S'.split())[1]
    'Three of a Kind'
    >>> get_comparison_value('8S 8C 4D 4H 3S'.split())[1]
    'Two Pairs'
    >>> get_comparison_value('8S 8C 5D 4H 3S'.split())[1]
    'One Pair'
    >>> get_comparison_value('8S 7C 5D 4H 3S'.split())[1]
    'High Card'
    """
    suits = set(get_suit(card) for card in hand)
    values = set(get_value(card) for card in hand)
    is_flush = len(suits) == 1
    is_straight = (len(values) == 5 and
        min(values) + 4 == max(values))
    kinds = get_kinds(hand)
    kind_counts = [k.count for k in kinds]

    if is_flush and values == {10, 11, 12, 13, 14}:
        result = (100, 'Royal Flush')
    elif is_flush and is_straight:
        result = (90, 'Straight Flush')
    elif kind_counts == [4, 1]:
        result = (80, 'Four of a Kind')
    elif kind_counts == [3, 2]:
        result = (70, 'Full House')
    elif is_flush:
        result = (60, 'Flush')
    elif is_straight:
        result = (50, 'Straight')
    elif kind_counts == [3, 1, 1]:
        result = (40, 'Three of a Kind')
    elif kind_counts == [2, 2, 1]:
        result = (30, 'Two Pairs')
    elif kind_counts == [2, 1, 1, 1]:
        result = (20, 'One Pair', kinds[0].value)
    else:
        assert kind_counts == [1]*5
        result = (10, 'High Card')
    return result + (max(values),)

CountValuePair = collections.namedtuple('CountValuePair', 'count value')

def get_kinds(hand):
    counts = collections.Counter(get_value(card) for card in hand).items()
    kinds = (CountValuePair(count, value) for value, count in counts)
    return list(sorted(kinds, reverse=True, key=lambda pair: pair.count))

if __name__ == '__main__':
    main()
