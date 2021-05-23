import sys
import functools

assert len(sys.argv) == 2, 'Input file path must be provided, e.g. ./main.py input1.txt'

tri = (open(sys.argv[1])
    .read()
    .strip()
    .split('\n'))
tri = [[int(n) for n in line.split(' ')] for line in tri]

@functools.lru_cache(maxsize=None)
def maxpath(r, c):
    if r == len(tri) - 1:
        return tri[r][c]
    else:
        return tri[r][c] + max(
            maxpath(r+1, c),
            maxpath(r+1, c+1)
        )

print(maxpath(0, 0))
