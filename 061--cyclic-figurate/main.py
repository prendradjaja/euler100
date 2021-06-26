from collections import defaultdict
import itertools

poly_functions = {
    3: lambda n: int(n*(n+1)/2),
    4: lambda n: int(n**2),
    5: lambda n: int(n*(3*n-1)/2),
    6: lambda n: int(n*(2*n-1)),
    7: lambda n: int(n*(5*n-3)/2),
    8: lambda n: int(n*(3*n-2)),
}

def main():
    # grouped_figurates[n][p] = all the 4-digit n-gon-al numbers that start
    # with the two-digit prefix p
    #
    # e.g. grouped_figurates[4][10] = [1024, 1089]
    grouped_figurates = defaultdict(lambda: defaultdict(list))

    for n in four_digit_values(poly_functions[3]):
        grouped_figurates[3]['ANY'].append(n)

    for shape in range(4, 8+1):
        for n in four_digit_values(poly_functions[shape]):
            grouped_figurates[shape][prefix(n)].append(n)

    for shape_order in itertools.permutations([4, 5, 6, 7, 8]):
        shape_order = (3,) + shape_order
        for number_set in number_sets(shape_order, grouped_figurates, 'ANY'):
            if suffix(number_set[-1]) == prefix(number_set[0]):
                print(sum(number_set))

def four_digit_values(f):
    for n in itertools.count(start=1):
        num = f(n)
        if num > 9999:
            break
        elif num >= 1000:
            yield num

def prefix(n):
    return n // 100

def suffix(n):
    return n % 100

def number_sets(shape_order, grouped_figurates, prefix):
    '''
    Given a particular shape order and grouped_figurates dictionary, yield all
    possible ordered number sets that satisfy that shape order and the
    cyclicness condition (except that the last number does not necessarily
    "connect" to the first number).
    '''
    shape = shape_order[0]
    if len(shape_order) == 1:
        for z in grouped_figurates[shape][prefix]:
            yield (z,)
    else:
        for a in grouped_figurates[shape][prefix]:
            for xyz in number_sets(shape_order[1:], grouped_figurates, suffix(a)):
                yield (a, *xyz)

def product(*iterables):
    '''
    Not actually used for the solution, but this is an example of doing a
    variable-depth nested loop. I used this as a model to write number_sets().

    Equivalent to itertools.product, which is itself equivalent to:

    for a in iterables[0]:
        for b in iterables[1]:
            ...
                for y in iterables[-2]:
                    for z in iterables[-1]:
                        yield (a, b, ..., y, z)

    >>> for item in product([1,2], [3,4], [5,6]):
    ...     print(item)
    (1, 3, 5)
    (1, 3, 6)
    (1, 4, 5)
    (1, 4, 6)
    (2, 3, 5)
    (2, 3, 6)
    (2, 4, 5)
    (2, 4, 6)
    '''
    iterable = iterables[0]
    if len(iterables) == 1:
        for z in iterable:
            yield (z,)
    else:
        for a in iterable:
            for xyz in product(*iterables[1:]):
                yield (a, *xyz)

if __name__ == '__main__':
    main()
