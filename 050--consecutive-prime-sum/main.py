from collections import OrderedDict, defaultdict
from pprint import pprint
import itertools

def main():
    # for p in primes_up_to(10**6):
    #     print(p)
    # return

    # nums = [1, 10, 100, 1000, 10000]
    # prefix_sums = get_prefix_sums(nums)
    # print(sum_range(prefix_sums, 1, 3), sum(nums[1:3]))
    # return

    # a b c d e
    # a b c d e

    n = 100000
    primes = primes_up_to(n)
    primes_set = set(primes)
    prefix_sums = get_prefix_sums(primes)
    count = len(primes)
    for stop in range(count + 1):
        for start in range(0, stop):
            my_sum = sum_range(prefix_sums, start, stop)
            if my_sum in primes_set and stop - start > 1:
                # print(stop - start, my_sum)
                pass





# 0 1 2 3 4
# sum(1:3)
# sum(:1)

def sum_range(prefix_sums, start, stop):
    return prefix_sums[stop] - prefix_sums[start]

def get_prefix_sums(lst):
    x = 0
    result = [x]
    for n in lst:
        x += n
        result.append(x)
    return result

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

main()
