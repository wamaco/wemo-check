# We import deque for an efficient queue implementation (used in Breadth-First Search)
from collections import deque

# dataclass is used to automatically generate special methods like __init__
from dataclasses import dataclass

# The Edge class represents a directed edge in our flow network.
# Each edge has a starting vertex (i), an ending vertex (j), a capacity (cap),
# the current flow through the edge (flow), and a pointer to the "back" edge (reverse edge).
@dataclass
class Edge:
    """Represents a directed edge from vertex i to j with a given capacity."""
    i: int        # The starting vertex of the edge
    j: int        # The ending vertex of the edge
    cap: int      # The maximum capacity of the edge
    flow: int = 0 # The current flow through the edge (initially 0)
    back: "Edge | None" = None  # A pointer to the reverse edge (will be set later)

    @property
    def is_saturated(self):
        """
        Returns True if the edge is 'saturated', meaning no additional flow can be pushed.
        This is when the residual capacity is zero.
        """
        return self.res == 0

    @property
    def res(self):
        """
        Returns the 'residual capacity' of the edge.
        This is the remaining capacity on the edge where additional flow can be added.
        """
        return self.cap - self.flow

    def add_flow(self, f):
        """
        Adds flow 'f' to this edge and subtracts the same amount from the reverse edge.
        This helps in 'undoing' the flow if needed in later steps.
        """
        # Increase flow on the forward edge
        self._add_flow(+f)
        # Decrease flow on the reverse edge (this effectively increases its capacity)
        self.back._add_flow(-f)

    def _add_flow(self, f):
        """
        A helper method to change the flow on this edge.
        It asserts that the new flow does not exceed the capacity.
        """
        # Check that the new flow does not exceed the capacity of the edge
        assert self.flow + f <= self.cap, "Flow cannot exceed capacity"
        self.flow += f

# The FlowNetwork class encapsulates our entire flow network and implements the
# Edmonds-Karp algorithm (a specific version of the Ford-Fulkerson method) for finding the maximum flow.
class FlowNetwork:
    def __init__(self, n, s, t):
        """
        Initializes a new flow network.
        
        Parameters:
        n (int): The number of vertices in the network.
        s (int): The source vertex from where the flow originates.
        t (int): The sink vertex where the flow is destined.
        """
        self.n = n      # Total number of vertices
        self.s = s      # Source vertex
        self.t = t      # Sink vertex
        # Create an adjacency list where each vertex has a list of edges.
        self.adj = [[] for _ in range(n)]
    
    def add_edge(self, i, j, cap):
        """
        Adds a directed edge from vertex i to vertex j with the given capacity.
        Also adds a reverse edge with zero capacity (for the residual graph).

        Parameters:
        i (int): The starting vertex.
        j (int): The ending vertex.
        cap (int): The capacity of the edge.
        """
        # Create the forward edge from i to j
        edge_ij = Edge(i, j, cap)
        # Create the reverse edge from j to i with zero capacity initially
        edge_ji = Edge(j, i, 0)

        # Add the forward edge to the adjacency list of vertex i
        self.adj[i].append(edge_ij)
        # Add the reverse edge to the adjacency list of vertex j
        self.adj[j].append(edge_ji)

        # Link the two edges to each other as reverse (back) edges.
        edge_ij.back = edge_ji
        edge_ji.back = edge_ij

    def find_augmenting_path(self):
        """
        Uses Breadth-First Search (BFS) to find an 'augmenting path' from the source (s) to the sink (t).
        An augmenting path is a path where additional flow can be pushed.

        Returns:
        A list of edges representing the path, or None if no such path exists.
        """
        # Initialize a queue for BFS and add the source vertex
        que = deque([self.s])
        # pedge will store the edge used to reach each vertex during BFS.
        # It is initialized with None (meaning unvisited) for each vertex.
        pedge = [None] * self.n
        # Mark the source as visited with a dummy value (True) since no edge is needed to reach itself.
        pedge[self.s] = True

        # Continue until there are no more vertices to explore in the queue
        while que:
            i = que.popleft()

            # If we reached the sink, backtrack to build the augmenting path.
            if i == self.t:
                path = []
                # Trace back from the sink to the source using the pedge array.
                while i != self.s:
                    # Add the edge that led to the current vertex
                    path.append(pedge[i])
                    # Move to the previous vertex in the path
                    i = pedge[i].i
                # The path is built in reverse order (from sink to source)
                return path

            # Iterate over all edges going out from vertex i.
            for edge in self.adj[i]:
                # Check if the edge has remaining capacity (not saturated)
                # and the destination vertex has not been visited yet.
                if not edge.is_saturated and pedge[edge.j] is None:
                    # Record that we reached vertex edge.j using the current edge.
                    pedge[edge.j] = edge
                    # Add the vertex to the queue for further exploration.
                    que.append(edge.j)

        # If no path was found, return None.
        return None

    def augment(self, path):
        """
        Augments the flow along the given path.
        It finds the minimum residual capacity along the path (bottleneck) and increases the flow along each edge by that amount.

        Parameters:
        path (list): A list of edges representing an augmenting path.

        Returns:
        delta (int): The amount of flow that was added along the path.
        """
        # Find the smallest available capacity along the path.
        delta = min(edge.res for edge in path)
        # Ensure that the bottleneck value is positive.
        assert delta > 0, "The augmenting flow must be positive."

        # For each edge in the path, add the flow delta.
        for edge in path:
            edge.add_flow(delta)

        return delta

    def max_flow(self):
        """
        Computes the maximum flow from the source to the sink using the Edmonds-Karp algorithm.
        It repeatedly finds an augmenting path and augments the flow until no more paths exist.

        Returns:
        max_flow_value (int): The total maximum flow from the source to the sink.
        """
        max_flow_value = 0

        # Keep finding paths until there is no available augmenting path.
        while (path := self.find_augmenting_path()) is not None:
            # Augment the flow along the found path and add the flow to max_flow_value.
            max_flow_value += self.augment(path)

        # Return the total maximum flow calculated.
        return max_flow_value

    def netflow(self, i):
        """
        Computes the net flow at a vertex (i.e., the sum of flows on all outgoing edges).
        This function can be used to verify flow conservation at each vertex.

        Parameters:
        i (int): The vertex for which to calculate the net flow.

        Returns:
        (int): The net flow at vertex i.
        """
        return sum(edge.flow for edge in self.adj[i])

def main():
    """
    Sets up a sample flow network and computes the maximum flow from the source (vertex 0)
    to the sink (vertex 3). The network has 4 vertices (0, 1, 2, 3) and several edges
    with very large capacities (10**100) to effectively simulate infinite capacity, except for
    one edge with a small capacity (1).
    """
    # Create a FlowNetwork with 4 vertices, source vertex 0, and sink vertex 3.
    f = FlowNetwork(4, 0, 3)

    # Add edges to the network.
    # The first two edges have a very high capacity.
    f.add_edge(0, 1, 10**100)
    f.add_edge(0, 2, 10**100)
    # This edge between vertex 1 and 2 has a low capacity, creating a bottleneck.
    f.add_edge(1, 2, 1)
    # More high capacity edges to the sink.
    f.add_edge(1, 3, 10**100)
    f.add_edge(2, 3, 10**100)

    # Calculate the maximum flow from the source to the sink.
    max_flow = f.max_flow()
    print("The maximum flow is:", max_flow)

# This ensures that the main() function is called when this script is run directly.
if __name__ == '__main__':
    main()