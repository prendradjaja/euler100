import collections

def main():
    # ties = []
    # for i, line in enumerate(open('./input.txt'), start=1):
    #     line = line.strip()
    #     cards = line.split()
    #     hands = cards[:5], cards[5:]
    #     hand1, hand2 = hands
    #     rank1, rank2 = (get_rank(h) for h in hands)
    #     if rank1 == rank2:
    #         ties.append((i, line, hand1, hand2, rank1, rank2))
    # print(len(ties), 'ties\n')
    # if ties:
    #     i, line, hand1, hand2, rank1, rank2 = ties[0]
    #     print(*ties[0], sep='\n')

    wins = 0
    for line in open('./input.txt'):
        cards = line.strip().split()
        hands = cards[:5], cards[5:]
        rank1, rank2 = (get_rank(h) for h in hands)

        # I only implemented the minimum sufficient tiebreaking logic to solve
        # the problem. If e.g. both players have four of a kind, the player
        # whose quad is of greater rank should win, but this is unimplemented.
        # These sorts of tiebreaks can be implemented in get_rank() similarly
        # to how Two of a Kind's tiebreak is implemented.
        assert rank1 != rank2, "Unimplemented comparison"

        if rank1 > rank2:
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

def get_rank(hand):
    """
    >>> get_rank('AS KS QS JS TS'.split())[1]
    'Royal Flush'
    >>> get_rank('KS QS JS TS 9S'.split())[1]
    'Straight Flush'
    >>> get_rank('8S 8C 8D 8H 3S'.split())[1]
    'Four of a Kind'
    >>> get_rank('8S 8C 8D 3H 3S'.split())[1]
    'Full House'
    >>> get_rank('2S QS JS TS 9S'.split())[1]
    'Flush'
    >>> get_rank('KD QS JS TS 9S'.split())[1]
    'Straight'
    >>> get_rank('8S 8C 8D 4H 3S'.split())[1]
    'Three of a Kind'
    >>> get_rank('8S 8C 4D 4H 3S'.split())[1]
    'Two Pairs'
    >>> get_rank('8S 8C 5D 4H 3S'.split())[1]
    'One Pair'
    >>> get_rank('8S 7C 5D 4H 3S'.split())[1]
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
    _ = (CountValuePair(count, value) for value, count in collections.Counter(get_value(card) for card in hand).items())
    return list(sorted(_, reverse=True))

if __name__ == '__main__':
    main()
