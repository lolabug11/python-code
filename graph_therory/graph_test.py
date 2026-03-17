from graphTheoryClass import *
import json

def run_tests():
    with open('graph_therory/tests.json', 'r') as f:
        tests = json.load(f)

    passed = 0

    for test in tests:
        g = Graph()

        # add vertices
        for v in test["vertices"]:
            g.add_vertex(v)

        # add edges
        for e in test["edges"]:
            g.add_edge(e[0], e[1])

        result = g.is_bipartite()
        expected = test["expected"]

        if result == expected:
            print(f"PASS: {test['name']}")
            passed += 1
        else:
            print(f"FAIL: {test['name']}")
            print(f"  expected: {expected}")
            print(f"  got:      {result}")

    print(f"\n{passed}/{len(tests)} tests passed")


run_tests()