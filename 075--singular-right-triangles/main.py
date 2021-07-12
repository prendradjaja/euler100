from collections import Counter


def main():
    m_limit = 866  # Found by inspection
    p_limit = 1_500_000

    triples = pythagorean_triples(m_limit, p_limit)
    triples = unique(triples, key=lambda triple: tuple(sorted(triple)))

    counts = Counter()
    for triple in triples:
        p = sum(triple)
        counts[p] += 1

    print(sum(1 for i in range(1, p_limit+1) if counts[i] == 1))


def pythagorean_triples(m_limit, p_limit):
    for m, n in natural_pairs(m_limit):
        base_triple = euclid(m, n)
        base_p = sum(base_triple)
        for k in range(1, p_limit // base_p + 1):
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
