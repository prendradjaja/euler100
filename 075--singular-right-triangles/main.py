from collections import Counter


def main():
    m_limit = 866  # Found by inspection
    perimeter_limit = 1_500_000

    triples = pythagorean_triples(m_limit, perimeter_limit)
    triples = unique(triples, key=lambda triple: tuple(sorted(triple)))

    counts = Counter()
    for triple in triples:
        perimeter = sum(triple)
        counts[perimeter] += 1

    print(sum(1 for perimeter in counts
              if counts[perimeter] == 1))


def pythagorean_triples(m_limit, perimeter_limit):
    '''
    Generates Pythagorean triples with Euclid's formula for every pair (m, n)
    up to m_limit (inclusive). (m, n) are as described in euclid().

    Also generates multiples of these triples up to the given perimeter limit
    (inclusive).

    These triples are not guaranteed to be unique or in sorted order.

    An example for m_limit = 4, which corresponds to these (m, n) pairs:

        (2, 1),
        (3, 1), (3, 2),
        (4, 1), (4, 2), (4, 3)

    >>> list(pythagorean_triples(4, 50)) == [
    ...    # (m, n) = (2, 1)  ->  (a, b, c) = (3, 4, 5)
    ...    [3, 4, 5],
    ...    [6, 8, 10],
    ...    [9, 12, 15],
    ...    [12, 16, 20],
    ...
    ...    # (m, n) = (3, 1)  ->  (a, b, c) = (8, 6, 10)
    ...    [8, 6, 10],
    ...    [16, 12, 20],
    ...
    ...    # (m, n) = (3, 2)  ->  (a, b, c) = (5, 12, 13)
    ...    [5, 12, 13],
    ...
    ...    # (m, n) = (4, 1)  ->  (a, b, c) = (15, 8, 17)
    ...    [15, 8, 17],
    ...
    ...    # (m, n) = (4, 2)  ->  (a, b, c) = (12, 16, 20)
    ...    [12, 16, 20],
    ...
    ...    # (m, n) = (4, 3)  ->  (a, b, c) = (7, 24, 25), but this triple is
    ...    # excluded because its perimeter is already above 50.
    ... ]
    True
    '''
    for m, n in natural_pairs(m_limit):
        base_triple = euclid(m, n)
        perimeter = sum(base_triple)
        for k in range(1, perimeter_limit // perimeter + 1):
            triple = [x*k for x in base_triple]
            yield triple


def euclid(m, n):
    '''
    Euclid's formula for generating Pythagorean triples.
    https://en.wikipedia.org/w/index.php?title=Pythagorean_triple&oldid=1028947457#Generating_a_triple

    Given arbitrary integers (m, n) such that m > n > 0, the resulting triple
    (a, b, c) will be a Pythagorean triple.

    This formula generates every primitive triple ("primitive" = a, b, and c
    are coprime) and also some (not all) non-primitive triples.

    There are some simple rules (see Wikipedia) that determine whether a pair
    (m, n) will generate a primitive triple, but they're not relevant to this
    use case.

    >>> euclid(2, 1)
    [3, 4, 5]
    >>> euclid(3, 1)
    [8, 6, 10]
    >>> euclid(3, 2)
    [5, 12, 13]
    '''
    a = m**2 - n**2
    b = 2*m*n
    c = m**2 + n**2
    return [a, b, c]


def unique(seq, key):
    '''
    >>> identity = lambda x: x
    >>> list(unique('ABCAD', key=identity))
    ['A', 'B', 'C', 'D']
    '''
    seen = set()
    for elem in seq:
        keyed = key(elem)
        if keyed not in seen:
            seen.add(keyed)
            yield elem


def natural_pairs(m_limit):
    '''
    Generates all pairs of positive integers (m, n) up to m_limit such that
    m > n

    >>> list(natural_pairs(5)) == [
    ...     (2, 1),
    ...     (3, 1), (3, 2),
    ...     (4, 1), (4, 2), (4, 3),
    ...     (5, 1), (5, 2), (5, 3), (5, 4)
    ... ]
    True
    '''
    for m in range(1, m_limit + 1):
        for n in range(1, m):
            yield (m, n)


if __name__ == '__main__':
    main()
