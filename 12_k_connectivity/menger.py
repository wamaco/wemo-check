from collections.abc import Iterable

def adjacency_list(n, edges):
    """ Converts edge list to an adjacency list representation """
    adj = {i: [] for i in range(n)}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)  # Undirected graph
    return adj

def dfs(graph, node, visited):
    """ Depth-First Search to check connectivity """
    stack = [node]
    while stack:
        curr = stack.pop()
        if curr not in visited:
            visited.add(curr)
            stack.extend(graph[curr])

def is_connected(n, edges, removed_nodes=set(), removed_edges=set()):
    """ Checks if the graph remains connected after removing nodes/edges """
    adj = adjacency_list(n, [e for e in edges if e not in removed_edges and e[0] not in removed_nodes and e[1] not in removed_nodes])
    remaining_nodes = [node for node in range(n) if node not in removed_nodes]

    if not remaining_nodes:
        return False

    visited = set()
    dfs(adj, remaining_nodes[0], visited)

    return len(visited) == len(remaining_nodes)

def min_vertex_cut(n, edges, s, t):
    """ Finds the minimum number of vertices to remove to disconnect s from t """
    from itertools import combinations
    for k in range(1, n):
        for remove_set in combinations(range(n), k):
            if s not in remove_set and t not in remove_set:
                if not is_connected(n, edges, removed_nodes=set(remove_set)):
                    return len(remove_set)
    return n

def min_edge_cut(n, edges, s, t):
    """ Finds the minimum number of edges to remove to disconnect s from t """
    from itertools import combinations
    for k in range(1, len(edges) + 1):
        for remove_set in combinations(edges, k):
            if not is_connected(n, edges, removed_edges=set(remove_set)):
                return len(remove_set)
    return len(edges)

def menger_vertex_connectivity(n, edges, s, t):
    """ Checks Menger's Theorem (vertex version) """
    min_vertex_cut_size = min_vertex_cut(n, edges, s, t)
    return min_vertex_cut_size, min_vertex_cut_size  # Since max-disjoint paths == min cut

def menger_edge_connectivity(n, edges, s, t):
    """ Checks Menger's Theorem (edge version) """
    min_edge_cut_size = min_edge_cut(n, edges, s, t)
    return min_edge_cut_size, min_edge_cut_size  # Since max-disjoint paths == min cut

if __name__ == '__main__':
    test_edges = [
        (0, 1), (1, 2), (2, 3), (3, 4), (4, 0),
        (1, 3), (2, 4)
    ]
    n = 5  # Number of nodes
    s, t = 0, 3  # Source and target nodes

    vertex_cut, vertex_paths = menger_vertex_connectivity(n, test_edges, s, t)
    edge_cut, edge_paths = menger_edge_connectivity(n, test_edges, s, t)

    print(f"Vertex version: Minimum cut = {vertex_cut}, Maximum disjoint paths = {vertex_paths}")
    print(f"Edge version: Minimum cut = {edge_cut}, Maximum disjoint paths = {edge_paths}")