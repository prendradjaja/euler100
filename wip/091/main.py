from graphics import *
import math

def main():
    win = GraphWin(width = 500, height = 800)
    win.setCoords(0, 0, win.width, win.height)

    # Grid(Point(0, 0), Point(w, h)).draw(win)
    # (
    #     move(
    #         Polygon(Point(0.1, 0.1), Point(1.5, 0.5), Point(1.9, 1.9)),
    #         [
    #             [[0, 0], [2, 2]],
    #             [[1, 0], [3, 2]],
    #         ]
    #     )
    #     .draw(win)
    # )

    grids_per_row = 3
    w = 2
    h = 3
    grids_per_row = 10 // w
    mg = MultiGrid(w, h, grids_per_row, win)

    points = []
    for i in range(w):
        points.append(Point(i, 0))
    for i in range(h):
        points.append(Point(w, i))
    for i in range(w):
        points.append(Point(w-i, h))
    for i in range(h):
        points.append(Point(0, h-i))

    # for i,p in enumerate(points):
    #     print(i,p)

    for a in range(2, len(points)):
        for b in range(1, a):
            for c in range(0, b):
                pa = points[a]
                pb = points[b]
                pc = points[c]

                # if set([a, b, c]) == {0, 2, 6}:
                #     print(pa, pb, pc)
                #     print(is_triangle(pa, pb, pc),
                #         has_right_angle(pa, pb, pc),
                #         is_maximal(pa, pb, pc, w, h))
                #     mg.add_grid()
                #     mg.add_shape(Polygon(pa, pb, pc))

                if (is_triangle(pa, pb, pc)
                    and has_right_angle(pa, pb, pc)
                    and is_maximal(pa, pb, pc, w, h)
                ):
                    # print(a, b, c)
                    mg.add_grid()
                    mg.add_shape(Polygon(pa, pb, pc))

    # for _ in range(9):
    #     mg.add_grid()
    #     mg.add_shape(Polygon(Point(0.1, 0.1), Point(1.5, 0.5), Point(1.9, 1.9)))

    mg.draw()

    win.getMouse()

def slope(a, b):
    """ Returns inf for vertical slope """
    try:
        return (b.y - a.y) / (b.x - a.x)
    except ZeroDivisionError:
        return float('inf')

def is_triangle(a, b, c):
    m_ab = slope(a, b)
    m_bc = slope(b, c)
    return not slope_equals(m_ab, m_bc)

def has_right_angle(a, b, c):
    m_ab = slope(a, b)
    m_ac = slope(a, c)
    m_bc = slope(b, c)
    # print(m_ab, m_ac, m_bc,
        # '|', m_ac, rotate_90(m_bc))
    return (False
        or slope_equals(m_ab, rotate_90(m_ac))
        or slope_equals(m_ac, rotate_90(m_bc))
        or slope_equals(m_bc, rotate_90(m_ab))
    )

def is_maximal(a, b, c, w, h):
    xmax = max(a.x, b.x, c.x)
    xmin = min(a.x, b.x, c.x)
    ymax = max(a.y, b.y, c.y)
    ymin = min(a.y, b.y, c.y)
    return (True
        and float_equals(0, xmin)
        and float_equals(0, ymin)
        and float_equals(w, xmax)
        and float_equals(h, ymax)
    )

def slope_equals(m1, m2):
    if math.isinf(m1) and math.isinf(m2):
        return True
    else:
        return float_equals(m1, m2)

def rotate_90(m):
    """ Expects and returns inf for vertical slope """
    try:
        return -1/m
    except ZeroDivisionError:
        return float('inf')

def float_equals(a, b, epsilon=0.000001):
    return abs(a - b) < epsilon

class MultiGrid:
    def __init__(self, w, h, grids_per_row, win):
        self.w = w
        self.h = h
        self.grids_per_row = grids_per_row
        self.win = win

        self.padding = 10 # px

        total_padding = (1 + self.grids_per_row) * self.padding
        self.grid_width = (win.width - total_padding) / self.grids_per_row
        self.grid_height = self.h / self.w * self.grid_width

        self.rows = [
            [ # row
                # [] # shape
            ]
        ]

    def add_grid(self):
        if len(self.current_row()) == self.grids_per_row:
            self.rows.append([])
        self.current_row().append([])

    def current_row(self):
        return self.rows[-1]

    def current_grid(self):
        return self.current_row()[-1]

    def add_shape(self, shape):
        self.current_grid().append(shape)

    def draw(self):
        for r, row in enumerate(self.rows):
            for c, shapes in enumerate(row):
                x1 = self.padding + (self.grid_width + self.padding) * c
                x2 = self.padding + (self.grid_width + self.padding) * c + self.grid_width
                y1 = self.padding + (self.grid_height + self.padding) * r
                y2 = self.padding + (self.grid_height + self.padding) * r + self.grid_height
                boxes = [
                    [[0, 0], [self.w, self.h]],
                    [[x1, y1], [x2, y2]],
                ]
                move(Grid(Point(0, 0), Point(self.w, self.h)), boxes).draw(self.win)
                for shape in shapes:
                    move(shape, boxes).draw(self.win)




class Grid:
    def __init__(self, p1, p2, dx=1, dy=1):
        self.shapes = []
        for x in float_range(p1.x, p2.x+dx, dx):
            line = Line(Point(x, p1.y), Point(x, p2.y))
            line.setOutline('gray')
            self.shapes.append(line)
        for y in float_range(p1.y, p2.y+dy, dy):
            line = Line(Point(p1.x, y), Point(p2.x, y))
            line.setOutline('gray')
            self.shapes.append(line)

    @staticmethod
    def from_shapes(shapes):
        g = Grid(Point(0, 0), Point(1, 1))
        g.shapes = shapes
        return g

    def draw(self, win):
        for shape in self.shapes:
            shape.draw(win)

def float_range(start, stop, step=1):
    r = start
    i = 0
    while r < stop:
        yield r
        i += 1
        r = start + i * step

def move(shape, boxes):
    box1, box2 = boxes
    [[b1x1, b1y1], [b1x2, b1y2]] = box1
    [[b2x1, b2y1], [b2x2, b2y2]] = box2
    x = LinearEquation.from_points([b1x1, b2x1], [b1x2, b2x2])
    y = LinearEquation.from_points([b1y1, b2y1], [b1y2, b2y2])

    # TODO instead of creating new obj, try clone() methods -- would preserve config (fill etc)
    if isinstance(shape, Point):
        return Point(x(shape.x), y(shape.y))
    elif isinstance(shape, (Line, Rectangle)): # _BBox
        p1 = move(shape.p1, boxes)
        p2 = move(shape.p2, boxes)
        copy = shape.clone()
        copy.p1 = p1
        copy.p2 = p2
        return copy
    elif isinstance(shape, Polygon):
        points = [move(point, boxes) for point in shape.points]
        return Polygon(*points)
    elif isinstance(shape, Grid):
        shapes = [move(shape, boxes) for shape in shape.shapes]
        return Grid.from_shapes(shapes)
    else:
        raise Exception("Not implemented: move() for " + str(type(shape)))


class LinearEquation:
    def __init__(self, m, b):
        self.m = m
        self.b = b

    @staticmethod
    def from_points(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        m = (y2 - y1) / (x2 - x1)
        b = y1 - m * x1
        return LinearEquation(m, b)

    def __call__(self, x):
        return self.m * x + self.b

# def clear(win):
#     for item in win.items[:]:
#         item.undraw()

main()
