from collections import OrderedDict, defaultdict
from pprint import pprint
import itertools

def main():
    primes = primes_in_range(1000, 9999)

    buckets = defaultdict(list)
    for p in primes:
        buckets[''.join(sorted(str(p)))].append(p)

    buckets = { k:v for k,v in buckets.items() if len(v) >= 3 }

    for bucket in buckets.values():
        for a, b in itertools.combinations(bucket, 2):
            c = b + (b - a)
            if c in bucket:
                print(a, b, c, sep='')

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

# Both endpoints are inclusive
def primes_in_range(a, b):
    return [p for p in primes_up_to(b) if p >= a]

main()
