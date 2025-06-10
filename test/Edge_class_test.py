import unittest

from main.Node import Node
from main.Edge import Edge


class MyTestCase(unittest.TestCase):
    # def test_something(self):
        #self.assertEqual(True, False)  # add assertion here
    def test_Edge_creation_forward(self):
        test1 = Node("test1", 1)
        test2 = Node("test2", 1)
        forwardEdge = Edge(test1, test2, 20)
        backwardEdge = Edge(test2, test1, 20)
        test1.edges.append(forwardEdge)
        test2.edges.append(backwardEdge)
        self.assertTrue(forwardEdge, test1.edges[0])

    def test_Edge_creation_backward(self):
        test1 = Node("test3", 2)
        test2 = Node("test4", 2)
        forward_edge = Edge(test1, test2, 17)
        backward_edge = Edge(test2, test1, 17)
        test1.edges.append(forward_edge)
        test2.edges.append(backward_edge)
        self.assertEqual(backward_edge, test2.edges[0])

    def test_Edge_distance_check(self):
        test1 = Node("test5", 3)
        test2 = Node("test6", 3)
        forward_edge = Edge(test1, test2, 36)
        backward_edge = Edge(test2, test1, 36)
        test1.edges.append(forward_edge)
        test2.edges.append(backward_edge)
        self.assertEqual(test1.edges[0].distance, 36)
        self.assertEqual(test2.edges[0].distance, 36)


if __name__ == '__main__':
    unittest.main()
