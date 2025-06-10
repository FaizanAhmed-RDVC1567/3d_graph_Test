from main.Node import Node
from main.DataTypeError import DataTypeError

class Edge:
    def __init__(self, starting_node, ending_node, travel_distance):
        # explicitly check that 'starting_node' is of type 'Node'
        if not isinstance(starting_node, Node):
            raise DataTypeError(f"Parameter 'starting_node' should be of type 'Node', but got a different type", None, Node, type(starting_node))

        # Fix for the test that expected an instance of the class 'Node' but got a different data type
        if not isinstance(ending_node, Node):
            raise DataTypeError("Parameter 'ending_node' should be of type 'Node', but got a different type", None, Node,type(ending_node))

        # Fix for the test that expected 'travel_distance' to be of type 'int' but got a different type
        if not isinstance(travel_distance, int):
            raise DataTypeError("Parameter 'travel_distance' should be of type 'int', but got a different type", None, Node, type(travel_distance))

        self.startNode = starting_node
        self.endNode = ending_node
        self.distance = travel_distance

    def __str__(self):
        return f"Starting node: {self.startNode}, Ending node: {self.endNode}, Distance: {self.distance}"