import sys


class Node:
    def __init__(self, name, elevation):
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
