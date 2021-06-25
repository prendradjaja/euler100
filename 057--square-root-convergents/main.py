from math import gcd
import functools

@functools.lru_cache(maxsize=None)
def f(n):
    if n == 0:
        return (3, 2)
    else:
        a, b = f(n - 1)
        a2, b2 = (a + 2*b, a + b)

        # We will never need to reduce the fraction. Why? At each iteration,
        # we compute the next fraction by: adding one, inverting one, and
        # adding one again. None of these steps can make an irreducible
        # fraction reducible.
        assert gcd(a2, b2) == 1

        return a2, b2

def count_digits(n):
    return len(str(n))

count = 0
for n in range(1000):
    numer, denom = f(n)
    if count_digits(numer) > count_digits(denom):
        count += 1
print(count)
