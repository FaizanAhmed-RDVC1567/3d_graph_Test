from main.Node import Node
from main.DataTypeError import DataTypeError

class Edge:
    def __init__(self, starting_node, ending_node, travel_distance):
        # explicitly check that 'starting_node' is of type 'Node'
        if not isinstance(starting_node, Node):
            raise DataTypeError(f"Parameter 'starting_node' should be of type 'Node', but got a different type", None, Node, type(starting_node))

        self.startNode = starting_node
        self.endNode = ending_node
        self.distance = travel_distance

    def __str__(self):
        return f"Starting node: {self.startNode}, Ending node: {self.endNode}, Distance: {self.distance}"