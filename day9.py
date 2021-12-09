import logging
from functools import reduce
import RealInput


logging.basicConfig(level=logging.INFO)

# Inputs
tst_input = """2199943210
3987894921
9856789892
8767896789
9899965678"""
data_in = RealInput.RealInput.DAY9

# Turn into matrix. I don't know NP
input_as_matrix = [list(map(lambda a: int(a), list(x))) for x in data_in.splitlines()]
x_max = len(input_as_matrix[0])
y_max = len(input_as_matrix)


def exists_and_smaller(lol, x, y, ref):
    """Check if the item beside is smaller"""
    if x < 0 or y < 0 :
        return False
    if y >= len(lol):
        return False
    if x >= len(lol[y]):
        return False
    return ref >= lol[y][x]


low_points = []
for x in range(x_max):
    for y in range(y_max):
        logging.debug("{} {}".format(x, y))
        ref_point = input_as_matrix[y][x]
        if not (exists_and_smaller(input_as_matrix, x-1, y, ref_point) or
                exists_and_smaller(input_as_matrix, x+1, y, ref_point) or
                exists_and_smaller(input_as_matrix, x, y-1, ref_point) or
                exists_and_smaller(input_as_matrix, x, y+1, ref_point)):
            low_points.append(ref_point)


risk = reduce(lambda a, b: a + b, map(lambda x: x+1, low_points))
print(risk)
assert risk == 514, "wrong p1"
