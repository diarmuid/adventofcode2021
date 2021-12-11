import logging
from functools import reduce
import RealInput
from collections import namedtuple
from math import prod


logging.basicConfig(level=logging.INFO)

Pt = namedtuple('Pt', ["x", "y"])

# For debug
def matrix_to_str(lol:dict):
    for y in lol.values():
        logging.debug('\t'.join(map(str, y.values())))


#Similar to d7
def get_locality(lol: dict, pt: Pt):
    """Get the points in the locality of the specified point"""
    locality = set()
    for (x_dlt, y_dlt) in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]:
        try:
            _s = lol[pt.y + y_dlt][pt.x + x_dlt]
        except:
            pass
        else:
            locality.add(Pt(pt.x + x_dlt, pt.y + y_dlt))
    return locality


data_in = RealInput.RealInput.DAY11
input_as_matrix = {}

# There's defo a one line for this
for y, l in enumerate(data_in.splitlines()):
    if y not in input_as_matrix:
        input_as_matrix[y] = {}
    for x, v in enumerate(map(lambda a: int(a), list(l))):
        input_as_matrix[y][x] = v

x_max = len(input_as_matrix[0])
y_max = len(input_as_matrix)

simulate_steps = 100

flash_count = 0
all_flash = None
step = 0
simulate = True
while simulate:
    keep_iterating = True
    iteration_step = 0

    while keep_iterating:
        keep_iterating = False  # Unless we find more octupses to flash
        for _x in range(x_max):
            for _y in range(y_max):
                # First pass just increment everything
                if iteration_step == 0:
                    input_as_matrix[_y][_x] = (input_as_matrix[_y][_x] + 1)
                    keep_iterating = True
                # subsequent passes, increment anything touch a 10 or greater
                # And reduce the flashes to 0 so they won't have a further impact
                elif input_as_matrix[_y][_x] >= 10:
                    for pt in get_locality(input_as_matrix, Pt(_x,_y)):
                        if input_as_matrix[pt.y][pt.x] != 0:
                            input_as_matrix[pt.y][pt.x] = (input_as_matrix[pt.y][pt.x] + 1)
                    input_as_matrix[_y][_x] = 0
                    keep_iterating = True
        # Debug
        logging.debug("iteration {}".format(iteration_step))
        matrix_to_str(input_as_matrix)
        iteration_step += 1

    # Count the flashes in this step
    new_flashes = 0
    for _x in range(x_max):
        for _y in range(y_max):
            if input_as_matrix[_y][_x] == 0:
                flash_count += 1
    # P1 was after 100 steps
    if step == 99:
        print("p1=",flash_count)
        assert flash_count == 1675, "wrong p1"

    # Reduce the matriox
    sum_flashes = 0
    for y in input_as_matrix.values():
        sum_flashes += reduce(lambda a,b : a + b, list(y.values()))

    logging.debug("step={} flash={}".format(step+1, sum_flashes))
    # Exit 
    if sum_flashes == 0:
        print("P2={}".format(step+1))
        simulate = False
        assert step == 514, "wrong P2"

    logging.debug("Reduced. Step={} TotalFlas={}".format(step, flash_count))
    logging.debug(matrix_to_str(input_as_matrix))
    step += 1

