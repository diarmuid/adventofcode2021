import RealInput
from collections import defaultdict, namedtuple
import re

Fold = namedtuple("Fold", ["direction", 'value'])

def exists(lol, x, y):
    try:
        res = lol[y][x]
    except:
        return 0
    else:
        return res


def countdots(lol:{int,int}):
    _c = 0
    for y in lol.values():
        _c += sum(y.values())

    return _c


def print_matrix(lol, maxx, maxy):
    PRINTSTR = {0: ".", 1: "#"}
    for y in range(maxy):
        for x in range(maxx):
            v = lol[y][x]
            print("{}".format(PRINTSTR[v]), end="")
        print("")


data_in = RealInput.RealInput.DAY13

input_as_matrix = defaultdict(dict)
folds = []
max_x = 0
max_y = 0
for l in data_in.splitlines(keepends=False):
    m = re.match(r"fold along ([xy])=(\d+)", l)
    if "," in l:
        x,y = map(lambda x: int(x), l.split(","))
        input_as_matrix[y][x] = 1
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
    elif m:
        folds.append(Fold(m.group(1), int(m.group(2))))
    elif l == "":
        pass
    else:
        raise Exception("Can't parse {}".format(l))


for i, fold in enumerate(folds):
    if fold.direction == "y":
        for y_fold in range(1, fold.value+1):
            for x in range(max_x+1):
                input_as_matrix[fold.value-y_fold][x] = exists(input_as_matrix, x, fold.value-y_fold) \
                                              or exists(input_as_matrix, x, fold.value+y_fold)
        for y_fold in range(fold.value, max_y+1):
            for x in range(max_x+1):
                try:
                    del(input_as_matrix[y_fold][x])
                except:
                    pass

        max_y = max_y // 2
    else:
        for x_fold in range(fold.value+1):
            for y in range(max_y+1):
                input_as_matrix[y][fold.value-x_fold] = exists(input_as_matrix, fold.value-x_fold, y) \
                                              or exists(input_as_matrix, fold.value+x_fold, y)
        for x_fold in range(fold.value, max_x+1):
            for y in range(max_y+1):
                try:
                    del(input_as_matrix[y][x_fold])
                except:
                    pass

        max_x = max_x // 2
    if i == 0:
        print("Part1=",countdots(input_as_matrix))
        assert countdots(input_as_matrix) == 675, "Wrong p1 test"
    #print("_------------{}----------------".format(i))
    #print_matrix(input_as_matrix, max_x, max_y)
print("Part2=",countdots(input_as_matrix))
print_matrix(input_as_matrix, max_x, max_y)
assert countdots(input_as_matrix) == 98, "Wrong P2"