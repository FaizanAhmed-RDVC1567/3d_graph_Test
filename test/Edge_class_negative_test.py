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
                         f"Received: {type("")}\nError Code: {""}")


if __name__ == '__main__':
    unittest.main()
