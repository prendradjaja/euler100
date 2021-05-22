import math

def main():
    grid = read_and_parse()

    transformations = [
        grid,
        transpose(grid),
        transpose(stagger(grid, True)),
        transpose(stagger(grid, False)),
    ]

    largest = 0
    for transformed_grid in transformations:
        for row in transformed_grid:
            for line in consecutives(row, 4):
                largest = max(largest, math.prod(line))
    print(largest)

def read_and_parse():
    x = (open('grid.txt')
        .read()
        .strip()
        .split('\n'))
    x = [[int(n) for n in row.split(' ')] for row in x]
    return x

def transpose(m):
    """
    >>> transpose([[1, 2, 3], [4, 5, 6]])
    [[1, 4], [2, 5], [3, 6]]
    """
    return [list(i) for i in zip(*m)]

def stagger(m, forward):
    """
    >>> for row in stagger([
    ...     [1, 2],
    ...     [3, 4],
    ...     [5, 6],
    ... ], True):
    ...     print(row)
    [0, 0, 1, 2]
    [0, 3, 4, 0]
    [5, 6, 0, 0]
    """
    m_width = len(m[0])
    m_height = len(m)
    out_width = m_width + m_height - 1

    if forward:
        x = list(reversed(m))
        x = stagger(x, False)
        return list(reversed(x))

    out = []
    for i, row in enumerate(m):
        before = [0] * i
        after = [0] * (out_width - m_width - i)
        out.append(before + row + after)
    return out

def consecutives(seq, n):
    """
    >>> [''.join(t) for t in consecutives('abcd', 2)]
    ['ab', 'bc', 'cd']
    """
    prevs = []
    for item in seq:
        prevs.append(item)
        if len(prevs) == n:
            yield tuple(prevs)
            prevs.pop(0)

main()
