from graphics import *

def main():
    win = GraphWin(width = 500, height = 800)
    h = 5
    w = 5
    m = max(h, w)
    padding = 0.1
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
    mg = MultiGrid(3, 3, grids_per_row, win)
    for _ in range(9):
        mg.next_grid()
    mg.draw()

    win.getMouse()

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
                [] # shape
            ]
        ]

    def next_grid(self):
        if len(self.current_row()) == self.grids_per_row:
            self.rows.append([])
        self.current_row().append([])

    def current_row(self):
        return self.rows[-1]

    def current_grid(self):
        return self.current_row()[-1]

    def add_shape(self, shape):
        self.current_grid.append(shape)

    def draw(self):
        for r, row in enumerate(self.rows):
            for c, shapes in enumerate(row):
                x1 = self.padding + (self.grid_width + self.padding) * c
                x2 = self.padding + (self.grid_width + self.padding) * c + self.grid_width
                y1 = self.padding + (self.grid_height + self.padding) * r
                y2 = self.padding + (self.grid_height + self.padding) * r + self.grid_height
                # Rectangle(Point(x1, y1), Point(x2, y2)).draw(self.win)
                move(Grid(Point(0, 0), Point(self.w, self.h)), [
                    [[0, 0], [self.w, self.h]],
                    [[x1, y1], [x2, y2]],
                ]).draw(self.win)
                print(x1, y1)




class Grid:
    def __init__(self, p1, p2, dx=1, dy=1):
        self.shapes = []
        for x in float_range(p1.x, p2.x+dx, dx):
            self.shapes.append(Line(Point(x, p1.y), Point(x, p2.y)))
        for y in float_range(p1.y, p2.y+dy, dy):
            self.shapes.append(Line(Point(p1.x, y), Point(p2.x, y)))

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
        return type(shape)(p1, p2)
    elif isinstance(shape, Polygon):
        points = [move(point, boxes) for point in shape.points]
        return Polygon(*points)
    elif isinstance(shape, Grid):
        shapes = [move(shape, boxes) for shape in shape.shapes]
        # p1 = move(shape.p1, boxes)
        # p2 = move(shape.p2, boxes)
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
