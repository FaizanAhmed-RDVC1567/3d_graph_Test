import unittest
from main.Node import Node
from main.DataTypeError import DataTypeError


class NodeNegativeTestCase(unittest.TestCase):
    def test_Node_wrong_first_parameter_type(self):
        with self.assertRaises(DataTypeError) as e_ndt:
            test_node1 = Node([], 8)
        self.assertEqual(str(e_ndt.exception),
                         f"Parameter 'name' should be of type 'str', but got a different type | "
                         f"Expected: {str}, Received: {type([])}\nError Code: {''}")

    def test_Node_wrong_elevation_parameter_type(self):
        with self.assertRaises(DataTypeError) as e_net:
            test_a = Node("testA", {})
        self.assertEqual(str(e_net.exception),
                         f"Parameter 'elevation' should be of type 'int', but got a different type | "
                         f"Expected: {int}, Received: {dict}\nError Code: {''}")


if __name__ == '__main__':
    unittest.main()
