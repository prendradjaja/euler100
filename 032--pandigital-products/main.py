import itertools
import functools

all_digits = '123456789'

def main():
    products = set()

    # For every possible ab * cd = efghi (where ab, cd, and efghi can be any
    # lengths, not just 2 and 5)
    for left_length in range(2, 9):
        for left_side in itertools.permutations(all_digits, left_length):
            for ab, cd in splits(left_side):

                efghi = set(all_digits) - set(ab) - set(cd)
                ab = digitcat(ab)
                cd = digitcat(cd)
                product = ab * cd
                product_string = str(product)

                # efghi = "expected"
                # product_string = "actual"
                if len(product_string) == len(efghi) and set(product_string) == efghi:
                    print(ab, '*', cd, '=', product_string)
                    products.add(product)

    print(sum(products))

def splits(lst):
    for i in range(1, len(lst)):
        yield lst[:i], lst[i:]

def digitcat(digits):
    """
    >>> digitcat(['1', '2'])
    12
    """
    return int(functools.reduce(lambda a, b: a + b, digits))

if __name__ == '__main__':
    main()
