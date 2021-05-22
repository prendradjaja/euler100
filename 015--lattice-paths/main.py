import functools

# TODO Can probably be further optimized: m and n are interchangeable
@functools.lru_cache(maxsize=None)
def paths(m, n):
    if m == 0 or n == 0:
        return 1
    return paths(m-1, n) + paths(m, n-1)

print(paths(20, 20))
