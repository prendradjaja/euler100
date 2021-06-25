from collections import OrderedDict
from functools import reduce, lru_cache
import itertools

# A simple implementation of the Sieve of Eratosthenes
# n is inclusive
def primes_up_to(n):
    is_prime = OrderedDict((n, True) for n in range(2, n+1))
    i = 2
    while i <= n ** 0.5:
        for j in range(i*2, n+1, i):
            is_prime[j] = False
        # increment
        i += 1
        while not is_prime[i]:
            i += 1
    result = []
    for n in is_prime:
        if is_prime[n]:
            result.append(n)
    return result

cap = 10000
primes = primes_up_to(cap)
print('ready')

def main():
    example = {3, 7, 109, 673}
    # what = [3, 11, 17, 53]
    # print(ok([3, 7, 109, 673]))
    # return
    for i, idxs in enumerate(combos(3)):
        selected = [primes[idx] for idx in idxs]

        # if i % 100000 == 0:
        #     print(i // 1000, idxs[-1], primes[idxs[-1]])

        if ok(selected):
            print(selected)
            return
            # print(selected, '***' if set(selected) <= example else '')

        # if selected == [3, 7, 109, 673]:
        #     print(i)
        #     return

def ok(prime_set):
    for a, b in itertools.permutations(prime_set, 2):
        concatenation = intcat(a, b)
        # print(concatenation)
        if not is_prime(concatenation):
            return False
    return True

def combos(n):
    for z in itertools.count(start = n - 1):
        for abc in itertools.combinations(range(0, z), n - 1):
            yield (*abc, z)

def intcat(a, b):
    result = a * pow10(count_digits(b)) + b
    # expected = int(str(a) + str(b))
    # assert expected == result, (expected, result, a, b)
    return result

@lru_cache(maxsize=None)
def pow10(n):
    return 10 ** n

def count_digits(n):
    length = 0
    while n > 0:
        length += 1
        n //= 10
    return length



@lru_cache(maxsize=None)
def is_prime(n):
    # if n <= cap:
    #     return n in primes
    if n <= 1:
        return False
    for m in range(2, n):
        if n % m == 0:
            return False
    return True

main()
