import functools

coins = [200, 100, 50, 20, 10, 5, 2, 1]
# My intuition tells me to use this order, but I suppose it's not needed

@functools.lru_cache(maxsize=None)  # Not strictly needed for this size input
def count(n, coin_index=0):
    """
    Returns the number of ways to make n with only the given coin and smaller
    """
    if coin_index >= len(coins) or n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return (count(n - coins[coin_index], coin_index)
                + count(n, coin_index + 1))

print(count(200))
