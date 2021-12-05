import re


DIR_X = "x"
DIR_Y = "y"


class Line(object):
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def to_points(self) -> dict:
        _points = {}
        if self.x1 == self.x2:
            _points[self.x1] = {}
            if self.y2 > self.y1:
                for y in range(self.y1, self.y2+1):
                    _points[self.x1][y] = 1
            elif self.y1 > self.y2:
                for y in range(self.y2, self.y1+1):
                    _points[self.x1][y] = 1
            else:
                raise Exception("Did not expect this config(y) {}".format(repr(self)))
        elif self.y1 == self.y2:

            if self.x2 > self.x1:
                for x in range(self.x1, self.x2 + 1):
                    _points[x] = {}
                    _points[x][self.y1] = 1
            elif self.x1 > self.x2:
                for x in range(self.x2, self.x1 + 1):
                    _points[x] = {}
                    _points[x][self.y1] = 1
            else:
                raise Exception("Did not expect this config(x) {}".format(repr(self)))
        return _points

    def __repr__(self):
        return "X1={:3d} X2={:3d} Y1={:3d} Y2={:3d}".format(self.x1, self.x2, self.y1, self.y2)


class Matrix(object):
    def __init__(self, max_x: int, max_y: int) -> None:
        self._matrix = {}
        for x in range(max_x):
            self._matrix[x] = {}
            for y in range(max_y):
                self._matrix[x][y] = 0

    def add_line(self, line: Line) -> bool:
        """Add a line to the matrix"""
        line_points = line.to_points()
        for x, ydir in line_points.items():
            for y, val in ydir.items():
                self._matrix[x][y] += val

        return True

    def get_danger(self, dangerval=2) -> int:
        _count = 0
        for x, ydir in self._matrix.items():
            for y, val in ydir.items():
                if val >= dangerval:
                    _count += 1

        return _count


def max(lines: [Line], dir) -> int:
    """Get the max coordinates in  a list of lines"""
    _max = 0
    for l in lines:
        if dir == DIR_X and l.x2 > _max:
            _max = l.x2
        elif dir == DIR_Y and l.y2 > _max:
            _max = l.y2
    return _max


alllines = []

f = open("d5.txt")
for l in f.readlines():
    match = re.match(r"(\d+),(\d+)\s+->\s+(\d+),(\d+)", l.strip())
    if match:
        alllines.append(Line(int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4))))
    else:
        raise Exception("Did not match on {}".format(l))

max_x = max(alllines, DIR_X)
max_y = max(alllines, DIR_Y)

matrix = Matrix(max_x, max_y)
for mline in alllines:
    matrix.add_line(mline)

print("Danger points={}".format(matrix.get_danger(2)))