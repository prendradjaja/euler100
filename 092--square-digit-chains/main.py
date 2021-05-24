cache = {1: 1, 89: 89}
def f(n):
    if n in cache:
        return cache[n]
    res = f(sum(d*d for d in digits(n)))
    cache[n] = res
    return res

def digits(n):
    while n:
        yield n % 10
        n //= 10

count = 0
for n in range(1, 10_000_000):
    if n % 100_000 == 0:
        print(f'{n / 1_000_000}M: {count}')
    if f(n) == 89:
        count += 1
print(count)
