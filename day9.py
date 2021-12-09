import logging
from functools import reduce
import RealInput
from collections import namedtuple
from math import prod


logging.basicConfig(level=logging.INFO)

# Inputs
data_in = RealInput.RealInput.DAY9

Pt = namedtuple('Pt', ["x", "y"])


def exists_and_smaller(lol, x, y, ref):
    """Check if the item beside is smaller"""
    try:
        res = ref >= lol[y][x]
    except:
        return False
    else:
        return res


# Turn into matrix. I don't know NP
input_as_matrix = {}

# There's defo a one line for this
for y, l in enumerate(data_in.splitlines()):
    if y not in input_as_matrix:
        input_as_matrix[y] = {}
    for x, v in enumerate(map(lambda a: int(a), list(l))):
        input_as_matrix[y][x] = v

x_max = len(input_as_matrix[0])
y_max = len(input_as_matrix)

# Part 1
low_points = []
low_point_coord = []  # For part 2
for _x in range(x_max):
    for _y in range(y_max):
        ref_point = input_as_matrix[_y][_x]
        if not (exists_and_smaller(input_as_matrix, _x-1, _y, ref_point) or
                exists_and_smaller(input_as_matrix, _x+1, _y, ref_point) or
                exists_and_smaller(input_as_matrix, _x, _y-1, ref_point) or
                exists_and_smaller(input_as_matrix, _x, _y+1, ref_point)):
            low_points.append(ref_point)
            low_point_coord.append(Pt(_x, _y))


risk = reduce(lambda a, b: a + b, map(lambda x: x+1, low_points))
print(risk)
assert risk == 514, "wrong p1"


# Part 2
def get_locality(lol: dict, pt: Pt):
    """Get the points in the locality of the specified point"""
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
    """Filter out the points that don't meet the criteria from the locality"""
    filtered = set()
    logging.debug(ref_val)
    for (x, y) in locality:
        if lol[y][x] == 9:
            continue
        if lol[y][x] <= ref_val:
            continue
        filtered.add(Pt(x,y))
    return filtered


def recurse_filter(input_as_matrix:dict, points_to_check: [Pt], results: set):
    """Recursively filter the points"""
    _pt = points_to_check.pop()
    local = get_locality(input_as_matrix, _pt,)
    filtered = filter_locality(input_as_matrix, local, input_as_matrix[_pt.y][_pt.x])
    results = set.union(filtered, results) # Add the filtered points to the results
    points_to_check += filtered  # More points to check
    if len(points_to_check) == 0: # All done
        return results
    else:
        return recurse_filter(input_as_matrix, points_to_check, results)


# Part 2
basin_sizes = []
for ref_point in low_point_coord:
    basin = {ref_point}  # Include the starting point
    basin = recurse_filter(input_as_matrix, [ref_point], basin)
    basin_sizes.append(len(basin))

sol2 = prod(sorted(basin_sizes)[-3:])
print(sol2)
assert sol2 == 1103130, "wrong p2"
