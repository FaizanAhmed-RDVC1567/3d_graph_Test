import unittest
from main.Node import Node
from main.Edge import Edge
from main.DataTypeError import DataTypeError


class MyTestCase(unittest.TestCase):
    def test_Edge_wrong_first_parameter(self):
        #test1_node = Node("test1", 0)
        #test2_node = Node("test2", 0)
        #test1_edge = Edge("", test2_node, 40)
        #test2_edge = Edge(test2_node, test1_node, 40)
        with self.assertRaises(DataTypeError) as e_dt:
            test1_node = Node("test1", 0)
            test2_node = Node("test2", 0)
            test1_edge = Edge("", test2_node, 40)
            test2_edge = Edge(test2_node, test1_node, 40)
        self.assertEqual(str(e_dt.exception),
                         f"Parameter 'starting_node' should be of type 'Node', but got a different type | Expected: {Node}, "
                         f"Received: {type('')}\nError Code: {""}")

    def test_Edge_wrong_second_parameter(self):
        with self.assertRaises(DataTypeError) as edt:
            test1_node = Node("test1", 1)
            test2_node = Node("test2", 1)
            test_edge1 = Edge(test1_node, 1, 35)
        self.assertEqual(str(edt.exception),
                         f"Parameter 'ending_node' should be of type 'Node', but got a different type | Expected: {Node}, "
                         f"Received: {type(1)}\nError Code: """)

    def test_Edge_wrong_third_parameter(self):
        with self.assertRaises(DataTypeError) as e:
            test1 = Node("testA", 2)
            test2 = Node("testB", 2)
            test_edge = Edge(test1, test2, 0.5)
        self.assertEqual(str(e.exception),
                         f"Parameter 'travel_distance' should be of type 'int', but got a different type | Expected: {int}, "
                         f"Received: {type(0.5)}\nError Code: """)


if __name__ == '__main__':
    unittest.main()
