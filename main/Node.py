import sys
from main.DataTypeError import DataTypeError


class Node:
    def __init__(self, name, elevation):
        # The following is a fix to explicitly check that the 'name' parameter is of type 'str'
        if not isinstance(name, str):
            raise DataTypeError("Parameter 'name' should be of type 'str', but got a different type",
                                None, str, type(name))

        # Fix for the test that expected 'elevation' to be of type 'int', but got a different type.
        if not isinstance(elevation, int):
            raise DataTypeError("Parameter 'elevation' should be of type 'int', but got a different type",
                                None, int, type(elevation))

        self.name = name
        self.data = (sys.maxsize, self)
        self.parent = None
        self.edges = []
        self.used = False
        self.elevationZ = elevation
        self.isOnOpenList = False

    def add_edge(self, edge):
        self.edges.append(edge)

    """
    No need to test this function, it's a special function that is called during the dijkstra function execution
    under a specific circumstance; when the calculated distances are the same and the nodes need to be ordered in order
    for the calculated route to be efficient.
    """
    def __lt__(self, other):
        return self.name < other.name

    def __str__(self):
        return (f"name={self.name}, elevation={self.elevationZ}, data={self.data[0]}, parent={self.parent}," +
                f" Used in path={self.used}, Is on open list={self.isOnOpenList}")
