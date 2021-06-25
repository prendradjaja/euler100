import functools

@functools.lru_cache(maxsize=None)
def f(n):
    return sum(factorial(int(d)) for d in str(n))

def loop_length(n):
    seen = {n}
    n = f(n)
    while n not in seen:
        seen.add(n)
        n = f(n)
    return len(seen)

@functools.lru_cache(maxsize=None)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

answer = 0
for n in range(1000000):
    if loop_length(n) == 60:
        answer += 1
print(answer)
