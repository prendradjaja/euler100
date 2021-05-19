# A simple implementation of the Sieve of Eratosthenes

from collections import OrderedDict

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

max_n = 200_000 # found by trial and error
target_index = 10_000 # 10001st 0-indexed

print(primes_up_to(max_n)[target_index])
