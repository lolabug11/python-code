import json
from graphTheoryClass import*
def run_tests(graph_class, test_data):
    for test in test_data["tests"]:
        g = graph_class()
        
        for action in test["actions"]:
            method = action[0]
            args = action[1:]
            getattr(g, method)(*args)
        
        expected = test["expected"]
        results = {}

        if "vertex_count" in expected:
            results["vertex_count"] = g.vertex_count()

        if "edge_count" in expected:
            results["edge_count"] = g.edge_count()

        if "neighbors_A" in expected:
            results["neighbors_A"] = g.get_neighbors("A")

        if "neighbors_B" in expected:
            results["neighbors_B"] = g.get_neighbors("B")

        if "degree_A" in expected:
            results["degree_A"] = g.degree("A")

        if "degree_sequence" in expected:
            results["degree_sequence"] = g.degree_sequence()

        if "is_connected" in expected:
            results["is_connected"] = g.is_connected()

        if "BFS_A" in expected:
            results["BFS_A"] = g.BFS("A")

        if "DFS_A_length" in expected:
            results["DFS_A_length"] = len(g.iterable_DFS("A"))

        if "path_exists" in expected:
            results["path_exists"] = g.path_exists("A", "C")

        if "shortest_path" in expected:
            results["shortest_path"] = g.shortest_path_unweighted("A", "C")

        if "has_cycle" in expected:
            results["has_cycle"] = g.has_cycle()

        if "is_tree" in expected:
            results["is_tree"] = g.is_tree()

        if "is_bipartite" in expected:
            results["is_bipartite"] = g.is_bipartite()

        if "all_paths_count" in expected:
            paths = g.all_paths("A", "D")
            results["all_paths_count"] = len(paths)

        if results == expected:
            print(f"✅ {test['name']}")
        else:
            print(f"❌ {test['name']}")
            print("Expected:", expected)
            print("Got:", results)


# load JSON file
with open("graph_therory/tests.json", "r") as f:
    test_data = json.load(f)

# run tests
run_tests(Graph, test_data)
