from decimal import Decimal, getcontext


# Trial and error shows that this is the minimum precision required for the
# answer to stabilize. I wondered why it's not 101 or something like that, and
# I think it's because squaring doubles the number of digits of a number.
getcontext().prec = 103


def main():
    naturals = set(range(100))
    squares = set(n ** 2 for n in range(10))

    total = 0
    for n in naturals - squares:
        total += sqrt100digitsum(n)
        print(n, sqrt(n, 99))

    print('Answer:', total)


def sqrt(n, precision):
    '''
    precision = # of digits after the dot
    '''
    result = Decimal(0)
    unit = Decimal(1)
    for p in range(precision + 1):
        while result ** 2 < n:
            result += unit
        result -= unit
        unit /= Decimal(10)
    return result


def sqrt100digitsum(n):
    root = sqrt(n, 99)
    return sum(int(d) for d in str(root) if d != '.')


main()
