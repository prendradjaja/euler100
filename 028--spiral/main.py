from grid import gridcardinal as grid
import itertools

def main():
    n = 1001
    bounded_spiral = itertools.islice(infinite_spiral(), n**2)
    total = 0
    for i, pos in enumerate(bounded_spiral, 1):
        r, c = pos
        if abs(r) == abs(c):
            total += i
    print(total)

def infinite_spiral():
    curr = (0, 0)
    direction = grid.tovec['E']
    size = 1
    yield curr
    while True:
        nextpos = grid.addvec(curr, direction)
        if not in_box(nextpos, size):
            direction = grid.rot(direction, 'R')
            if direction == grid.tovec['E']:
                size += 1
            continue
        curr = nextpos
        yield curr

def in_box(position, size):
    return max(abs(x) for x in position) <= size

main()
