import logging
from functools import reduce
import RealInput
from collections import namedtuple
from math import prod
from operator import add, sub


logging.basicConfig(level=logging.INFO)

# Inputs
tst_input = """2199943210
3987894921
9856789892
8767896789
9899965678"""
data_in = RealInput.RealInput.DAY9
#data_in = tst_input

X = 0
Y = 1
Pt = namedtuple('Pt', ["x", "y"])


class Mtix(object):
    def __init__(self, val, checked):
        self.val = val
        self.checked = checked


# Turn into matrix. I don't know NP
_input_as_matrix = [list(map(lambda a: int(a), list(x))) for x in data_in.splitlines()]
input_as_matrix = {}
for y,row in enumerate(_input_as_matrix):
    if y not in input_as_matrix:
        input_as_matrix[y] = {}
    for x, val in enumerate(row):
        input_as_matrix[y][x] = Mtix(val, False)

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
    return ref >= lol[y][x].val


low_points = []
low_point_coord = []
for _x in range(x_max):
    for _y in range(y_max):
        logging.debug("{} {}".format(_x, _y))
        ref_point = input_as_matrix[_y][_x].val
        if not (exists_and_smaller(input_as_matrix, _x-1, _y, ref_point) or
                exists_and_smaller(input_as_matrix, _x+1, _y, ref_point) or
                exists_and_smaller(input_as_matrix, _x, _y-1, ref_point) or
                exists_and_smaller(input_as_matrix, _x, _y+1, ref_point)):
            low_points.append(ref_point)
            low_point_coord.append(Pt(_x, _y))


risk = reduce(lambda a, b: a + b, map(lambda x: x+1, low_points))
print(risk)
#assert risk == 15, "wrong p1"
assert risk == 514, "wrong p1"


def get_locality(lol: dict, pt: Pt,):
    locality = set()
    for (x_dlt, y_dlt) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            try:
                _s = lol[pt.y + y_dlt][pt.x + x_dlt]
            except:
                pass
            else:
                locality.add(Pt(pt.x + x_dlt, pt.y + y_dlt))
    return locality


def filter_locality(lol, locality, ref_val) -> set:
    filtered = set()
    logging.debug(ref_val)
    for (x, y) in locality:
        if lol[y][x].checked is True:
            continue
        if lol[y][x].val == 9:
            continue
        if lol[y][x].val <= ref_val:
            continue
        filtered.add(Pt(x,y))
        #lol[y][x].checked = True
    return filtered


def recurse_filter(input_as_matrix, points_to_check: [Pt], results: set ):
    _pt = points_to_check.pop()
    logging.debug(repr(_pt))
    local = get_locality(input_as_matrix, _pt,)
    filtered = filter_locality(input_as_matrix, local, input_as_matrix[_pt.y][_pt.x].val)
    results = set.union(filtered, results)
    points_to_check += filtered
    if len(points_to_check) == 0:
        return results
    else:
        return recurse_filter(input_as_matrix, points_to_check, results)


#print(low_point_coord)
#filter_locality(input_as_matrix, get_locality(input_as_matrix, Pt(4,1), 1), input_as_matrix[4][1])
#exit()
basin_sizes = []
for ref_point in low_point_coord:
    basin = {ref_point}
    basin = recurse_filter(input_as_matrix, [ref_point], basin)
    #print("--{}--".format(ref_point))
    #print(basin)
    #print(len(basin))
    basin_sizes.append(len(basin))

sol2 = prod(sorted(basin_sizes)[-3:])
print(sol2)
