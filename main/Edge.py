class Edge:
    def __init__(self, starting_node, ending_node, travel_distance):
        self.startNode = starting_node
        self.endNode = ending_node
        self.distance = travel_distance

    def __str__(self):
        return f"Starting node: {self.startNode}, Ending node: {self.endNode}, Distance: {self.distance}"