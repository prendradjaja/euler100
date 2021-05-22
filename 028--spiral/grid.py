# This file is the same as grid.py linked below, but with unused code manually removed.
# https://github.com/prendradjaja/advent-of-code-2020/blob/e9dfd99b7d0e02aa1c95eb4f1c732e8c3ddb6018/grid.py

""" Many of these methods work for n dimensions """
def _make_grid_library(names, rotdir):
    """
    names: e.g. RDLU corresponding to `dirs` below
    rotdir: Going forward in `names` (e.g. RDLU -- R to D) is a...
      - right turn: 1
      - left turn: -1
    """

    class clazz:  # Not really a class -- can I use a module instead?
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        tovec = { names[i]: vec for (i, vec) in enumerate(dirs) }

        @staticmethod
        def addvec(a, b):
            return tuple(x+y for x,y in zip(a,b))

        @staticmethod
        def rot(direction, rotation):
            assert rotation in ['L', 'R']
            # return clazz.dirs[(clazz.dirs.index(direction) + (rotdir if rotation == 'R' else -rotdir)) % 4]
            return clazz.rotvec(direction, rotation)

        @staticmethod
        def rotvec(vec, rotation):
            assert rotation in ['L', 'R']
            forward = (rotation == 'L') ^ (rotdir == 1)
            y, x = vec
            if forward:
                return (x, -y)
            else:
                return (-x, y)

    return clazz

gridcardinal = _make_grid_library('ESWN', 1)  # (y, x)! For working with array in source code, but using cardinal directions instead of RDLU
