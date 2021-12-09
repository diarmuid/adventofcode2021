import logging
from functools import reduce
import RealInput
from collections import namedtuple

logging.basicConfig(level=logging.INFO)

# Inputs
tst_input = """2199943210
3987894921
9856789892
8767896789
9899965678"""
#data_in = RealInput.RealInput.DAY9
data_in = tst_input

# Turn into matrix. I don't know NP
input_as_matrix = [list(map(lambda a: int(a), list(x))) for x in data_in.splitlines()]
x_max = len(input_as_matrix[0])
y_max = len(input_as_matrix)
Pt = namedtuple('Pt', ["x", "y"])


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
low_point_coord = []
for _x in range(x_max):
    for _y in range(y_max):
        logging.debug("{} {}".format(_x, _y))
        ref_point = input_as_matrix[_y][_x]
        if not (exists_and_smaller(input_as_matrix, _x-1, _y, ref_point) or
                exists_and_smaller(input_as_matrix, _x+1, _y, ref_point) or
                exists_and_smaller(input_as_matrix, _x, _y-1, ref_point) or
                exists_and_smaller(input_as_matrix, _x, _y+1, ref_point)):
            low_points.append(ref_point)
            low_point_coord.append((_x, _y))


risk = reduce(lambda a, b: a + b, map(lambda x: x+1, low_points))
print(risk)
#assert risk == 514, "wrong p1"


def get_locality(lol, pt: Pt, level):
    locality = set()
    if 0 <= pt.x-level < len(lol[pt.y]):
        for offset in range(pt.y-level, pt.y+level+1):
            if 0 <= offset < len(lol):
                locality.add((pt.x-level, offset))
    if 0 <= pt.x+level < len(lol[pt.y]):
        for offset in range(pt.y-level, pt.y+level+1):
            if 0 <= offset < len(lol):
                locality.add((pt.x+level, offset))

    if 0 <= pt.y-level < len(lol):
        for offset in range(pt.x-level, pt.x+level+1):
            if 0 <= offset < len(lol[pt.y]):
                locality.add((offset, pt.y-level))

    if 0 <= pt.y+level < len(lol):
        for offset in range(pt.x-level, pt.x+level+1):
            if 0 <= offset < len(lol[pt.y]):
                locality.add((offset, pt.y+level))

    return locality


def filter_locality(lol, locality, ref_val) -> set:
    filtered = set()
    for (x, y) in locality:
        if lol[y][x] == 9:
            continue
        if lol[y][x] >= ref_val:
            continue
        filtered.add(Pt(x,y))
    return filtered


def recurse_filter(input_as_matrix, points_to_check: [Pt], results: set):
    _pt = points_to_check.pop()
    logging.debug(repr(_pt))
    local = get_locality(input_as_matrix, _pt, 1)
    filtered = filter_locality(input_as_matrix, local, input_as_matrix[_pt.x][_pt.y])
    results = set.union(filtered, results)
    points_to_check += filtered
    if len(points_to_check) == 0:
        return results
    else:
        return recurse_filter(input_as_matrix, points_to_check, results)


#print(low_point_coord)
#filter_locality(input_as_matrix, get_locality(input_as_matrix, Pt(4,1), 1), input_as_matrix[4][1])
#exit()
ref_points = [Pt(1, 0)]
basin = set()
basin = recurse_filter(input_as_matrix, ref_points, basin)
print(len(basin))
exit()
