import itertools

digits = range(10)
primes = [2, 3, 5, 7, 11, 13, 17]

pandigitals = itertools.permutations(digits)

def ok(digits):
    for ((a,b,c), p) in zip(
        itertools.islice(consecutives(digits, 3), 1, None),
        primes
    ):
        abc = 100*a + 10*b + c
        if abc % p != 0:
            return False
    return True


def consecutives(seq, n=2):
    """
    >>> [''.join(t) for t in consecutives('abcd')]
    ['ab', 'bc', 'cd']
    >>> [''.join(t) for t in consecutives('abcd', 3)]
    ['abc', 'bcd']
    >>> [''.join(t) for t in consecutives('abcd', 5)]  # seq is too short
    []
    """
    prevs = []
    for item in seq:
        prevs.append(item)
        if len(prevs) == n:
            yield tuple(prevs)
            prevs.pop(0)

def digitcat(n):
    """
    >>> digitcat([1, 2])
    12
    """
    return int(''.join(str(d) for d in n))

total = 0
for n in pandigitals:
    if ok(n):
        total += digitcat(n)
print(total)
