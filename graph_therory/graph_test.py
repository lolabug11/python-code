from graphTheoryClass import *
import json

with open('graph_therory/tests.json', "r") as f:
    tests = json.load(f)

passed = 0

for test in tests:
    g = Graph()

    # add vertices
    for v in test["vertices"]:
        g.add_vertex(v)

    # add edges
    for v1, v2 in test["edges"]:
        g.add_edge(v1, v2)

    # run test
    result = g.is_bipartite()
    expected = test["expected"]

    if result == expected:
        print(test["name"], "PASS")
        passed += 1
    else:
        print(test["name"], "FAIL", "| expected:", expected, "got:", result)
    print(g.adjacency_list)

print(f"\n{passed}/{len(tests)} tests passed")