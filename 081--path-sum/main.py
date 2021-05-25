import sys
import functools

matrix = (open('input.txt')
    .read()
    .strip()
    .split('\n'))
matrix = [[int(n) for n in line.split(',')] for line in matrix]

height = len(matrix)
width = len(matrix[0])

@functools.lru_cache(maxsize=None)
def minpath(r, c):
    if (r, c) == (height - 1, width - 1):
        return matrix[r][c]
    else:
        return matrix[r][c] + min(
            minpath(r+1, c) if r+1 < height else float('inf'),
            minpath(r, c+1) if c+1 < width else float('inf'),
        )

print(minpath(0, 0))
