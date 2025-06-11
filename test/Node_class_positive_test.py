import unittest
import sys
from main.Node import Node


class NodePositiveTestCase(unittest.TestCase):
    def test_Node_creation_with_data(self):
        test_a = Node("testA", 1)
        self.assertEqual(test_a.name, "testA")
        self.assertEqual(test_a.elevationZ, 1)

    def test_Node_attributes_set_to_False(self):
        test1 = Node("testA", 2)
        self.assertFalse(test1.used, False)
        self.assertFalse(test1.isOnOpenList, False)

    def test_Node_parent_attribute_is_None(self):
        test_b = Node("testB", 0)
        self.assertIsNone(test_b.parent, None)

    def test_Node_edges_list_is_empty(self):
        test_c = Node("testC", 3)
        self.assertListEqual(test_c.edges, [])

    def test_Node_data_attribute_first_element_uses_maxsize(self):
        test_d = Node("testD", -1)
        self.assertIs(test_d.data[0], sys.maxsize)

    def test_Node_string_representation(self):
        test_e = Node("testE", 9)
        self.assertEqual(str(test_e), f"name=testE, elevation=9, data={sys.maxsize}, parent=None, "
                                      f"Used in path=False, Is on open list=False")


if __name__ == '__main__':
    unittest.main()
