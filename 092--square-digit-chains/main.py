import functools

@functools.lru_cache(maxsize=None)
def f(n):
    if n in [1, 89]:
        return n
    return f(sum(int(d)**2 for d in str(n)))

count = 0
for n in range(1, 10_000_000):
    if n % 100_000 == 0:
        print(f'{n / 1_000_000}M: {count}')
    if f(n) == 89:
        count += 1
print(count)
