class Graph:
    def __init__(self):
        self.graph = {}

    # Function to add an edge to the graph
    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    # Depth-Limited Search function
    def dls(self, start, goal, max_depth):
        return self.dls_util(start, goal, max_depth, 0)

    # Utility function to perform the search recursively
    def dls_util(self, node, goal, max_depth, current_depth):
        print(f"Visiting node: {node}, current depth: {current_depth}")

        if node == goal:
            return True

        if current_depth >= max_depth:
            return False

        if node not in self.graph:
            return False

        # Recursively search in the neighbors of the current node
        for neighbor in self.graph[node]:
            if self.dls_util(neighbor, goal, max_depth, current_depth + 1):
                return True

        return False

# Example usage:
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('B', 'E')
g.add_edge('C', 'F')
g.add_edge('D', 'G')
g.add_edge('E', 'H')

start = 'A'
goal = 'H'
max_depth = 3

# Run the DLS algorithm and print the result
if g.dls(start, goal, max_depth):
    print(f"Goal {goal} found within depth {max_depth}")
else:
    print(f"Goal {goal} not found within depth {max_depth}")
