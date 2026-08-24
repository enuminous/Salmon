import unittest
from salmon import Node, Edge, SalmonTracer

class TestSalmon(unittest.TestCase):
    def test_single_origin(self):
        nodes = {"a":Node("a",1), "b":Node("b",2)}
        t = SalmonTracer(nodes,[Edge("a","b",1.0)])
        out = t.trace("b")
        self.assertEqual(out["origins"][0][0],"a")

    def test_weighted_origin(self):
        nodes = {"a":Node("a",1),"b":Node("b",1),"c":Node("c",2)}
        t = SalmonTracer(nodes,[Edge("a","c",0.8),Edge("b","c",0.2)])
        out = t.trace("c")
        self.assertGreater(out["origins"][0][1], out["origins"][1][1])

    def test_unresolved_origin(self):
        nodes = {"a":Node("a",1),"c":Node("c",2)}
        t = SalmonTracer(nodes,[Edge("a","c",0.6)])
        out = t.trace("c")
        self.assertGreater(out["unresolved_origin"],0)

if __name__ == "__main__":
    unittest.main()
