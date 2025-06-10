import unittest
import sys
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

    def test_Edge_string_representation(self):
        test1 = Node("test7", 4)
        test2 = Node("test8", 4)
        front_edge = Edge(test1, test2, 66)
        back_edge = Edge(test2, test1, 66)

        # Check the string representation of the first edge
        self.assertEqual(f"Starting node: name=test7, elevation=4, data={sys.maxsize}, parent=None, "
                         f"Used in path=False, Is on open list=False, Ending node: name=test8, elevation=4, "
                         f"data={sys.maxsize}, parent=None, Used in path=False, Is on open list=False, Distance: 66",
                         str(front_edge))

        # Check the string representation of the second edge
        self.assertEqual(f"Starting node: name=test8, elevation=4, data={sys.maxsize}, parent=None, "
                         f"Used in path=False, Is on open list=False, Ending node: name=test7, elevation=4, "
                         f"data={sys.maxsize}, parent=None, Used in path=False, Is on open list=False, Distance: 66",
                         str(back_edge))


if __name__ == '__main__':
    unittest.main()
