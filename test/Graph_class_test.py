import unittest
from main.Graph import Graph


class GraphTestCase(unittest.TestCase):
    def test_Graph_string_rep(self):
        test_graph = Graph()
        self.assertEqual("A instance of a class that contains a network of interconnected Node objects, which use "
                         "bi-directional Edge objects that show which nodes are connected to each other.\nContains "
                         "two methods: 'add_edge' and the route-finding algorithm called 'dijkstra'.",
                         str(test_graph))


if __name__ == '__main__':
    unittest.main()
