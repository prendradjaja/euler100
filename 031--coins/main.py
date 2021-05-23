import functools

coins = [1, 2, 5, 10, 20, 50, 100, 200]

@functools.lru_cache(maxsize=None)
def count(n, depth=0):
    if n == 0:
        return 1
    result = 0
    for coin in coins:
        if coin <= n:
            result += count(n - coin, depth+1)
    print('  ' * depth, n, result)
    return result

print(count(4))
