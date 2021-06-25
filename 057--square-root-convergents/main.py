from math import gcd
import functools

@functools.lru_cache(maxsize=None)
def f(n):
    if n == 0:
        return (3, 2)
    else:
        a, b = f(n - 1)
        c, d = (a + 2*b, a + b)
        assert gcd(c, d) == 1  # It turns out this is true. Any nice way to prove it?
        return c, d

def count_digits(n):
    return len(str(n))

count = 0
for n in range(1000):
    numer, denom = f(n)
    if count_digits(numer) > count_digits(denom):
        count += 1
print(count)
