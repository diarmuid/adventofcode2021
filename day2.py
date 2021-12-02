import gzip
import operator
import re


# Mutable. I thought the part 2 was going to turn into multipke dimensions
class Position(object):
    def __init__(self, v, t):
        self.v = v
        self.t = t

    def __repr__(self):  # Just to make debug visible
        return "{:s}={:d}".format(self.t, self.v)


line_r = r"(\w+)\s+(\d+)"

with gzip.open("d2.txt.gz", 'rt') as f:
    all_lines = f.readlines()
    # Part 1
    horizontal = Position(0, "horizontal")
    vertical = Position(0, "vertical")
    move = {"forward": horizontal, "up": vertical, "down": vertical}
    mov_op = {"forward": operator.add, "up": operator.sub, "down": operator.add}
    for _line in all_lines:
        _match = re.match(line_r, _line.strip())
        if _match:
            _op = mov_op[_match.group(1)]
            _dir = move[_match.group(1)]
            _val = int(_match.group(2))
            _dir.v = _op(_dir.v, _val)
        else:
            raise Exception("Shouldn't be here")

    print("Part1 H={} V={} M={}".format(horizontal.v, vertical.v, horizontal.v * vertical.v))

    # Part 2
    horizontal = Position(0, "horizontal")
    vertical = Position(0, "vertical")
    aim = Position(0, "aim")
    move = {"forward": horizontal, "up": vertical, "down": vertical}
    movep2 = {"forward": horizontal, "up": aim, "down": aim}
    mov_op = {"forward": operator.add, "up": operator.sub, "down": operator.add}

    for _line in all_lines:
        _match = re.match(line_r, _line.strip())
        if _match:
            _op = mov_op[_match.group(1)]
            _dir = movep2[_match.group(1)]
            _val = int(_match.group(2))
            if _match.group(1) == "forward":
                vertical.v = vertical.v + aim.v * _val
            _dir.v = _op(_dir.v, _val)
        else:
            raise Exception("Shouldn't be here")

    print("Part2 H={} V={} M={}".format(horizontal.v, vertical.v, horizontal.v * vertical.v))