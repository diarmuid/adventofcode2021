import RealInput
from collections import defaultdict

connections = defaultdict(list)
for line in RealInput.RealInput.DAY12.splitlines(keepends=False):
    _start, _end = line.split("-")
    connections[_start].append(_end)
    connections[_end].append(_start)


def recurse_edges(current: str, visited: set, doubleback=True):
    num_paths = 0
    for endpoint in connections[current]:
        if endpoint == "end":
            num_paths += 1
        elif not endpoint.islower():
            num_paths += recurse_edges(endpoint, visited, doubleback)
        elif endpoint != "start":
            _newvisited = visited.union({endpoint})
            if endpoint not in visited:
                num_paths += recurse_edges(endpoint, _newvisited, doubleback)
            elif not doubleback:
                num_paths += recurse_edges(endpoint, _newvisited, True)
    return num_paths


p1 = recurse_edges("start", set())
print("Part 1:", p1)
assert p1==3485, "Wrong p1"


p2 = recurse_edges("start", set(), False)
print("Part 2:", p2)
assert p2==85062, "Wrong p2"