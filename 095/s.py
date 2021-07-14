from functools import lru_cache

@lru_cache(maxsize=None)
def sum_proper_divisors(n):
    return sum(get_proper_divisors_unordered(n))

def get_proper_divisors_unordered(n):
    if n > 1:
        yield 1
    factor = 2
    while factor**2 < n:
        if n % factor == 0:
            yield factor
            yield n // factor
        factor += 1
    if factor**2 == n and n % factor == 0:
        yield factor

cache = {}
def chain_length(n, collector=None):
    if n % 1000 == 0:
        indent = '        ' if n > 500_000 else ''
        print('...', indent, f'{n:,}')
    if n in cache and collector is None:
        return cache[n]
    seen = {n}
    # print(sorted(seen))
    while sum_proper_divisors(n) not in seen:
        n = sum_proper_divisors(n)
        if n > 1_000_000:
            return -1
        if n == 1 or n == 0:
            return -1
        seen.add(n)
        # print(sorted(seen))
    result = len(seen)
    for each in seen:
        cache[each] = result
    if collector is not None:
        collector.extend(seen)
    return result

def azbycx(seq):
    '''
    >>> ''.join(azbycx('abcxyz'))
    >>> ''.join(azbycx('abcde'))
    '''
    lst = list(seq)
    i = 0
    j = len(lst) - 1
    while j > i:
        yield lst[i]
        yield lst[j]
        i += 1
        j -= 1
    if i == j:
        yield lst[i]

if __name__ == '__main__':
    # edge case behavior for n=1?
    limit = 1_000_000
    # limit = 100
    elem = max(azbycx(range(2, limit+1)), key=chain_length)
    chain = []
    # elem = 30
    chain_length(elem, chain)
    print('chain', chain)
    print('elem', elem)
    print('chain length', chain_length(elem))
    print('answer', min(chain))
