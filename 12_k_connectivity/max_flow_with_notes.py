"""
Max-Flow Min-Cut Theorem Implementation

This script implements the Ford-Fulkerson algorithm to compute the maximum flow 
in a directed network flow graph. The Max-Flow Min-Cut theorem states that the 
maximum flow from a source to a sink is equal to the minimum cut capacity 
that separates the source from the sink.

Concepts Covered:
1. Max-Flow Min-Cut Theorem
2. Ford-Fulkerson Algorithm
3. BFS for Augmenting Paths
4. Applications: Image Segmentation, Open-Pit Mining

"""

import collections

class Graph:
    def __init__(self, vertices):
        """Initializes a graph with the given number of vertices."""
        self.V = vertices  # Number of vertices
        self.graph = [[0] * vertices for _ in range(vertices)]  # Adjacency matrix

    def add_edge(self, u, v, capacity):
        """Adds a directed edge from node u to node v with given capacity."""
        self.graph[u][v] = capacity

    def bfs(self, source, sink, parent):
        """Performs BFS to find an augmenting path in the residual graph."""
        visited = [False] * self.V
        queue = collections.deque([source])
        visited[source] = True

        while queue:
            u = queue.popleft()
            for v, capacity in enumerate(self.graph[u]):
                if not visited[v] and capacity > 0:  # Unvisited and has capacity left
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == sink:
                        return True  # Found path to sink
        return False

    def ford_fulkerson(self, source, sink):
        """Runs the Ford-Fulkerson method to compute maximum flow."""
        parent = [-1] * self.V
        max_flow = 0

        while self.bfs(source, sink, parent):
            # Find the maximum flow through the path found
            path_flow = float('Inf')
            v = sink
            while v != source:
                u = parent[v]
                path_flow = min(path_flow, self.graph[u][v])
                v = u

            # Update residual capacities of the edges and reverse edges
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow  # Reverse flow for backtracking
                v = u

            max_flow += path_flow  # Add path flow to overall flow

        return max_flow

# Example Usage
if __name__ == "__main__":
    """Example Graph to Demonstrate Max-Flow Calculation"""
    
    # Creating a graph with 6 nodes
    g = Graph(6)
    
    # Adding edges with capacities
    g.add_edge(0, 1, 16)
    g.add_edge(0, 2, 13)
    g.add_edge(1, 2, 10)
    g.add_edge(1, 3, 12)
    g.add_edge(2, 1, 4)
    g.add_edge(2, 4, 14)
    g.add_edge(3, 2, 9)
    g.add_edge(3, 5, 20)
    g.add_edge(4, 3, 7)
    g.add_edge(4, 5, 4)

    # Define source and sink nodes
    source, sink = 0, 5

    # Compute the maximum flow
    max_flow = g.ford_fulkerson(source, sink)
    
    # Print the result
    print(f"Maximum Flow in the network: {max_flow}")

"""
Understanding the Implementation:

1. **Graph Representation**:
   - The graph is represented using an adjacency matrix where each entry (u, v) holds the capacity of the edge from node u to node v.

2. **Ford-Fulkerson Algorithm**:
   - Uses BFS to find an augmenting path from source to sink.
   - Finds the bottleneck (minimum capacity along the path).
   - Updates residual capacities and allows reverse flow for backtracking.
   - Repeats until no more augmenting paths exist.

3. **Max-Flow Min-Cut Theorem**:
   - The computed max-flow value equals the total capacity of the smallest cut that separates the source from the sink.

Applications:
1. **Image Segmentation**: Partitioning images into meaningful regions by modeling pixels as a flow network.
2. **Open-Pit Mining**: Determining the most profitable excavation strategy by modeling excavation constraints using flow networks.

This implementation serves as an educational tool for understanding network flow concepts.
"""