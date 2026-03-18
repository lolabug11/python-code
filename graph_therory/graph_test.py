from graphTheoryClass import *
from time import *
def build_stress_graph(width=100, depth=100):
    g = Graph()

    root = "A"
    g.add_vertex(root)

    for i in range(width):
        branch = f"B{i}"
        g.add_edge(root, branch)

        prev = branch
        for j in range(depth):
            node = f"{branch}_{j}"
            g.add_edge(prev, node)
            prev = node

    return g
g = build_stress_graph(200,200)

start_time = perf_counter()
for _ in range(50):
    g.DFS("A")
end_time = perf_counter()
DFS_time = end_time - start_time
start_time = perf_counter()
for _ in range(50):
    g.iterable_DFS("A")
end_time = perf_counter()
iterable_DFS_time = end_time - start_time
start_time = perf_counter()
for _ in range(50):
    g.BFS("A")
end_time = perf_counter()
BFS_time = end_time - start_time
print(f'DFS time:{DFS_time}\nIterable DFS time: {iterable_DFS_time}\nBFS time: {BFS_time}')