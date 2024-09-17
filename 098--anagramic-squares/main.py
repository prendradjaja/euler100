from collections import defaultdict

# 40ish pairs including one triple
# 30k squares
#
# CARE
#
# 1296
# 1234
#
# RACE
#
# 9216
# 4132
#
#
# CARER
# abcdc
# 12345
#
# 12343


def main():
    with open('input.txt') as f:
        data = f.readline()
        words = data.replace('"', '').split(',')

    anagrams = defaultdict(set)
    for word in words:
        key = ''.join(sorted(word))
        anagrams[key].add(word)

    anagram_sets = { k: v for k, v in anagrams.items() if len(v) > 1 }

    # for key in anagram_sets:
    #     print(len(anagram_sets[key]), key, anagram_sets[key])

    longest = max(len(key) for key in anagram_sets)

    squares = []
    n = 1
    while len(str(n ** 2)) < longest + 1:
        squares.append(n ** 2)
        n += 1

    pairs = #TODO
    print(max(something(word1, word2, squares) for word1, word2 in pairs))

def something(word1, word2, squares):
    matches = find_numbers_matching_shape(word1, squares)
    scrambled_shape = get_scrambled_shape(word1, word2)

    largest_match = -1
    for number1 in matches:
        number2 = get_scrambled_number(number1, get_shape(word1), scrambled_shape)

        squares_set = set(squares)  # could move this somewhere else, but even here is better than not at all
        if number2 in squares_set:
            largest_match = max(largest_match, number1, number2)

    return largest_match


def find_numbers_matching_shape(word, squares):
    # can optimize: don't do the whole listcomp (squares is sorted)
    same_length_squares = [...]  # TODO
    shape = get_shape(word)
    return [n for n in squares if matches_shape(n, shape)]


def get_shape(word):
    """
    >>> get_shape('CARE')
    'abcd'
    >>> get_shape('CARER')
    'abcdc'
    """
    # TODO
    pass


def matches_shape(number, shape):
    # TODO
    pass


def get_scrambled_shape(word1, word2):
    # TODO
    pass


def get_scrambled_number(number, shape, scrambled_shape):
    """
    >>> get_scrambled_number(1296, 'abcd', 'cbad')
    9216
    """
    # TODO
    return scrambled_number



if __name__ == '__main__':
    main()
