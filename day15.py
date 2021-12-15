from queue import PriorityQueue
import RealInput
import time

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        #self.edges[v][u] = weight

    def path_find(graph, start_vertex, end_vertex=None):
        D = {v: float("inf") for v in range(graph.v)}
        D[start_vertex] = 0

        pq = PriorityQueue()
        pq.put((0, start_vertex))

        while not pq.empty():
            (dist, current_vertex) = pq.get()

            graph.visited.append(current_vertex)

            for neighbor in range(graph.v):
                if graph.edges[current_vertex][neighbor] != -1:
                    distance = graph.edges[current_vertex][neighbor]
                    if neighbor not in graph.visited:
                        old_cost = D[neighbor]
                        new_cost = D[current_vertex] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, neighbor))
                            D[neighbor] = new_cost

        return D

def wrap(i):
    return ((i - 1) % 9) + 1

st = time.time()
data_in = RealInput.RealInput.DAY15
lines = [[int(c) for c in l.strip()] for l in data_in.splitlines(keepends=False)]
max_y = len(lines)
max_x = len(lines[0])

if True:  # Part 2
    lines = [[wrap(lines[y % max_y][x % max_x] + (x // max_x) + (y // max_y)) for x in range(max_x * 5)] for y in
             range(max_y * 5)]
    max_x = len(lines[0])
    max_y = len(lines)

cave = Graph(max_x*max_y)

point_idx = 0
edges_added = 0
for y in range(max_y):
    for x in range(max_x):
        _after = point_idx + 1
        _before = point_idx - 1
        _below = point_idx + max_x
        _above = point_idx - max_x
        if x < (max_x - 1):
            cave.add_edge(point_idx, _after, lines[y][x+1])
            edges_added += 1
        if y < (max_y - 1):
            cave.add_edge(point_idx, _below, lines[y+1][x])
            edges_added += 1
        if y > 0:
            cave.add_edge(point_idx, _above, lines[y-1][x])
            edges_added += 1
        if x < 0:
            cave.add_edge(point_idx, _before, lines[y][x-1])
            edges_added += 1
        point_idx += 1
print("{:.1f}".format(time.time() - st))

print("edges={}".format(edges_added))
start_node = 0
end_node = max_x * max_y - 1

D = cave.path_find(start_node)
end_dist = D[end_node]
#for vertex in range(len(D)):
#    print("Distance from vertex 0 to vertex", vertex, "is", D[vertex])
print("Distance from ", start_node," to end", end_node, "is", end_dist)
print("{:.1f}".format(time.time() - st))
assert end_dist==824, "Wrong p1"