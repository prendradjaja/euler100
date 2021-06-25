import math
import itertools

digits = '123456789'

def main():
    coefficients = range(-999, 999+1)
    a, b, length = max(
        (
            (a, b, count_quadratic_primes(a, b))
            for a, b
            in itertools.product(coefficients, repeat=2)
        ),
        key=lambda x: x[2]
    )
    print('Answer:', a * b)
    print()
    print('a:', a)
    print('b:', b)
    print('Number of primes generated:', count_quadratic_primes(a, b))

    print('''
It is rather unsatisfying that neither n^2 - 79n + 1601 nor the quadratic that
we found actually generates more distinct primes than Euler's does:''')

    print()
    print('a', 'b', '#primes', '#distinct', sep='\t')
    print('-'*33)

    for (a, b) in [
        (1, 41),
        (-79, 1601),
        (-61, 971),
    ]:
        print(
            a,
            b,
            count_quadratic_primes(a, b),
            len(set(quadratic_primes(a, b))),
            sep='\t'
        )

def count_quadratic_primes(a, b):
    return len(quadratic_primes(a, b))

def quadratic_primes(a, b):
    f = lambda n: n**2 + a*n + b
    result = []
    for n in itertools.count():
        if is_prime(f(n)):
            result.append(f(n))
        else:
            return result

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for m in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % m == 0:
            return False
    return True

main()
