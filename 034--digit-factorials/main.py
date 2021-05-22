import functools

def main():
    results = []

    # An upper bound on these curious numbers.
    # TODO Formalize (Is this even right?)
    #
    # 9! = 362_880 (a six-digit number)
    #
    # So consider the six-digit number of only nines:
    #   curious_sum(999_999) = 9! * 6 = 2_177_280 (a seven-digit number)
    #
    # This is no longer a six-digit number. Now consider the seven-digit
    # number of only nines:
    #   curious_sum(9_999_999) = 9! * 7 = 2_540_160 (a seven-digit number)
    #
    # It is still a seven-digit number.
    #
    # So 9_999_999 is an upper bound on these curious numbers.
    max_n = 10_000_000

    for n in range(10, max_n):
        if n == curious_sum(n):
            results.append(n)
        if n % 100_000 == 0:
            print('\r', n, sep='', end='')
    print()
    print('Curious numbers found:', ', '.join(str(n) for n in results))
    print('Answer:', sum(results))

@functools.lru_cache(maxsize=None)
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def curious_sum(n):
    digits = [int(d) for d in str(n)]
    return sum(factorial(d) for d in digits)

main()
