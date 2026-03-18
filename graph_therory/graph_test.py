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
start_time= perf_counter()
g = build_stress_graph(200,200)
end_time = perf_counter()
graph_time = end_time - start_time
start_time = perf_counter()
for x in range(10):
    g.DFS("A")
    print(x)
end_time = perf_counter()
DFS_time = end_time - start_time
start_time = perf_counter()
for x in range(10):
    g.iterable_DFS("A")
    print(x)
end_time = perf_counter()
iterable_DFS_time = end_time - start_time
start_time = perf_counter()
for x in range(10):
    g.BFS("A")
    print(x)
end_time = perf_counter()
BFS_time = end_time - start_time
print(f'Graph time: {graph_time}\nDFS time:{DFS_time}\nIterable DFS time: {iterable_DFS_time}\nBFS time: {BFS_time}')