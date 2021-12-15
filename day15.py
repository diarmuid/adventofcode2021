from queue import PriorityQueue
import RealInput


class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight

    def path_find(graph, start_vertex):
        D = {v: float('inf') for v in range(graph.v)}
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


data_in = RealInput.RealInput.DAY15TST
max_y = len(data_in.splitlines(keepends=False))
max_x = len(list(data_in.splitlines(keepends=False)[0]))

cave = Graph(max_x*max_y)

input_matrix = [[] * max_x] * max_y
for y,l in enumerate(data_in.splitlines(keepends=False)):
    input_matrix[y] = list(map(lambda x: int(x), list(l)))

point_idx = 0
for y in range(max_y):
    for x in range(max_x):
        _adj = point_idx + 1
        _below = point_idx + max_x
        if x < (max_x-1):
            cave.add_edge(point_idx, _adj, input_matrix[y][x+1])
        if y < max_y-1:
            cave.add_edge(point_idx, _below, input_matrix[y+1][x])
        point_idx += 1

start_node = 0
end_node = max_x * max_y - 1
D = cave.path_find(start_node)
end_dist = D[end_node]
for vertex in range(len(D)):
    print("Distance from vertex 0 to vertex", vertex, "is", D[vertex])
print("Distance from ", start_node," to end", end_node, "is", end_dist)