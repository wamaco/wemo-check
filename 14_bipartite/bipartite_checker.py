"""
===============================================================================
BIPARTITE GRAPH DETECTOR (Python)
===============================================================================

This script provides a function to determine if a given undirected graph is
bipartite using BFS (Breadth-First Search).

A graph is bipartite if its nodes can be colored with two colors such that
no two adjacent nodes have the same color.

===============================================================================
"""

from collections import deque

def is_bipartite(graph):
    """
    Parameters:
        graph: dict
            Adjacency list representing the undirected graph

    Returns:
        bool: True if graph is bipartite, False otherwise
    """
    color = {}

    for start in graph:
        if start not in color:
            queue = deque([start])
            color[start] = 0  # Start coloring with 0
            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if v not in color:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        return False
    return True

# ==============================
# Sample Usage
# ==============================
if __name__ == "__main__":
    # Example 1: Bipartite graph
    graph1 = {
        0: [1, 3],
        1: [0, 2],
        2: [1, 3],
        3: [0, 2]
    }

    # Example 2: Non-bipartite graph (odd-length cycle)
    graph2 = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1]
    }

    print("Graph1 is bipartite?", is_bipartite(graph1))  # True
    print("Graph2 is bipartite?", is_bipartite(graph2))  # False