import unittest

from Node import Node
from Edge import Edge


class MyTestCase(unittest.TestCase):
    # def test_something(self):
        #self.assertEqual(True, False)  # add assertion here
    def test_Edge_creation(self):
        test1 = Node("test1", 1)
        test2 = Node("test2", 1)
        forwardEdge = Edge(test1, test2, 20)
        backwardEdge = Edge(test2, test1, 20)
        test1.edges.append(forwardEdge)
        test2.edges.append(backwardEdge)
        self.assertTrue(forwardEdge, test1.edges[0])


if __name__ == '__main__':
    unittest.main()
