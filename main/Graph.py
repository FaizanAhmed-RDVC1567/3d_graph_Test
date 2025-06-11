import collections
from heapq import heappush, heappop
from main.Edge import Edge


class Graph:
    """def __init__(self):"""
    def __str__(self):
        return ("A instance of a class that contains a network of interconnected Node objects, which use "
                "bi-directional Edge objects that show which nodes are connected to each other.\nContains "
                "two methods: 'add_edge' and the route-finding algorithm called 'dijkstra'.")

    def add_edge(self, node_start, node_end, distance):
        forwardEdge = Edge(node_start, node_end, distance)
        backwardEdge = Edge(node_end, node_start, distance)
        node_start.add_edge(forwardEdge)
        node_end.add_edge(backwardEdge)

    def dijkstra(self, beginning_node, ending_node):
        current_node = beginning_node
        open_list = []

        beginning_node.data = (0, beginning_node)
        heappush(open_list, beginning_node.data)

        while current_node != ending_node and len(open_list) > 0:
            for i in range(0, (len(current_node.edges))):
                # if current_node.edges[i].endNode.used == False  --> This is the old line
                if not current_node.edges[i].endNode.used:

                    # Here, an extra check is needed to prevent the same node being added twice
                    # if current_node.edges[i].endNode.isOnOpenList == False  --> This is the old line
                    if not current_node.edges[i].endNode.isOnOpenList:
                        heappush(open_list, current_node.edges[i].endNode.data)
                        current_node.edges[i].endNode.isOnOpenList = True

                # second part of checks to add the nodes needed, using distance checks
                if current_node.edges[i].endNode.data[0] > current_node.edges[i].distance + current_node.data[0]:
                    current_node.edges[i].endNode.parent = current_node
                    current_node.edges[i].endNode.data = (
                        current_node.edges[i].distance + current_node.data[0],
                        current_node.edges[i].endNode
                    )

            # At this point, the current node has been used by the algorithm, so we'll first set the 'used'
            # variable to True
            current_node.used = True

            # Now, we'll pop it out of the open list and then set the new current node to be used
            func_tuple = heappop(open_list)
            current_node = func_tuple[1]

            # Now, we just print out the used node's name:
            print(current_node.name)

        # This part of the function runs when the entire while loop has finished executing
        route = collections.deque([])
        while current_node is not None:
            route.appendleft(current_node.name) # Add to the left of the queue
            current_node = current_node.parent # This attribute gets set by the pathfinding algorithm above
        return route
