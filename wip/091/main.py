from graphics import *

def main():
    win = GraphWin(width = 500, height = 400)
    h = 5
    w = 5
    m = max(h, w)
    padding = 0.1
    win.setCoords((0 - padding)*m, (0 - padding)*m, (1 + padding)*m, (1 + padding)*m)

    Grid(Point(0, 0), Point(w, h)).draw(win)
    (
        move(
            Polygon(Point(0.1, 0.1), Point(1.5, 0.5), Point(1.9, 1.9)),
            [
                [[0, 0], [2, 2]],
                [[1, 0], [3, 2]],
            ]
        )
        .draw(win)
    )

    win.getMouse()

class MultiGrid:
    def __init__(self, h, w, grids_per_row, win):
        self.h = h
        self.w = w
        self.grids_per_row = grids_per_row
        self.win = win

        self.padding = 10 # px

        total_padding = (1 + self.grids_per_row) * self.padding
        self.grid_width = (win.width - total_padding) / self.grids_per_row
        self.grid_height = self.h / self.w * self.grid_width

        self.row = 0
        self.col = 0

    def next_grid():
        self.col = (self.col + 1) % self.grids_per_row
        self.row += self.col == 0

    def add_shape(shape):
        pass




class Grid:
    def __init__(self, p1, p2, dx=1, dy=1):
        self.shapes = []
        for x in float_range(p1.x, p2.x+dx, dx):
            self.shapes.append(Line(Point(x, p1.y), Point(x, p2.y)))
        for y in float_range(p1.y, p2.y+dy, dy):
            self.shapes.append(Line(Point(p1.x, y), Point(p2.x, y)))

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
    elif isinstance(shape, Polygon):
        points = [move(point, boxes) for point in shape.points]
        return Polygon(*points)


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
