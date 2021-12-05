import re
import operator
import logging

logging.basicConfig(level=logging.INFO)

DIR_X = "x"
DIR_Y = "y"


class Line(object):
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def to_points(self, diagonal: bool) -> dict:
        """
        Return the points of the line
        :param diagonal: include 45 degree diagonals
        :return:
        """
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

        if diagonal and (self.x1 != self.x2 and self.y1 != self.y2):
            logging.debug("Adding a diagonal {}".format(self))
            if abs(self.x1 - self.x2) != abs(self.y1 - self.y2):
                raise Exception("Diagonals should have matching lengths. {}".format(repr(self)))
            delta = abs(self.x1 - self.x2)
            # Increasing or decreasing
            if self.x1 > self.x2:
                x_operator = operator.sub
            else:
                x_operator = operator.add
            if self.y1 > self.y2:
                y_operator = operator.sub
            else:
                y_operator = operator.add

            for offset in range(delta+1):
                x_point = x_operator(self.x1, offset)
                y_point = y_operator(self.y1, offset)
                #logging.debug("Diagonal x={} y={}".format(x_point, y_point))
                if x_point < 0 or y_point < 0:
                    raise Exception("Should not have negative points. Delta={} Line={}".format(delta, repr(self)))
                if x_point not in _points:
                    _points[x_point] = {}
                    _points[x_point][y_point] = 1
                else:
                    _points[x_point][y_point] += 1

        return _points

    def __repr__(self):
        return "X1={:3d} X2={:3d} Y1={:3d} Y2={:3d}".format(self.x1, self.x2, self.y1, self.y2)


class Matrix(object):
    """
    Matrix representation
    """
    def __init__(self) -> None:
        self._matrix = {}

    def add_line(self, line: Line, diagonal=False) -> bool:
        """
        Add a line to the matrix.
        :param line:
        :param diagonal: Treat diagonals as danger points
        :return:
        """
        line_points = line.to_points(diagonal)
        logging.debug("Adding Line {} to matrix {}".format(line, self))
        for x, ydir in line_points.items():
            if x not in self._matrix:
                self._matrix[x] = {}
            for y, val in ydir.items():
                if y not in self._matrix[x]:
                    self._matrix[x][y] = 0
                self._matrix[x][y] += val

        return True

    def get_danger(self, dangerval=2) -> int:
        """Find the danger points based on the number of lines intersecting"""
        _count = 0
        for x, ydir in self._matrix.items():
            for y, val in ydir.items():
                if val >= dangerval:
                    _count += 1

        return _count

    def __repr__(self):
        return "MatrixMax"


# All the lines in the file
alllines = []

#Read in the file and populate the list of lines
f = open("d5.txt")
for l in f.readlines():
    match = re.match(r"(\d+),(\d+)\s+->\s+(\d+),(\d+)", l.strip())
    if match:
        alllines.append(Line(int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4))))
    else:
        raise Exception("Did not match on {}".format(l))

#part 1 . Create the matrix, add the lines hor and vert only
matrix = Matrix()
for mline in alllines:
    matrix.add_line(mline)

print("Danger points={}".format(matrix.get_danger(2)))
assert matrix.get_danger(2) == 3990, "Wrong answer"

# part 2
matrixp = Matrix()
for mline in alllines:
    matrixp.add_line(mline, diagonal=True)

print("Danger points={}".format(matrixp.get_danger(2)))
assert matrixp.get_danger(2) == 21305, "Wrong answer"
