from itertools import combinations
from utils import make_adjacency_list, Edge

def bridges_articulation_points_and_bccs(n, edges):
    if any(edge.i == edge.j for edge in edges):
        raise NotImplementedError("self-loops not supported")

    adj = make_adjacency_list(n, edges)

    vis = [-1]*n
    low = [-1]*n
    time = 0

    def visit(i):
        nonlocal time
        assert vis[i] == -1
        vis[i] = time
        time += 1

    bridges = []
    artic_points = []
    edge_visited = [False]*len(edges)
    edge_stack = []
    bccs = []

    def extract_bcc(edge):
        while True:
            last_edge = edge_stack.pop()
            yield last_edge
            if last_edge == edge:
                return

    def dfs(i, parent_edge):
        visit(i)
        is_root = parent_edge is None
        low[i] = vis[i]
        found_isolated_child = False
        children = 0

        for j, *_, edge_idx, edge in adj[i]:
            if edge_visited[edge_idx]:
                continue

            edge_visited[edge_idx] = True

            if vis[j] == -1:
                edge_stack.append(edge)
                dfs(j, edge)
                low[i] = min(low[i], low[j])

                children += 1

                if low[j] > vis[i]:
                    bridges.append(edge)

                if low[j] >= vis[i]:
                    bccs.append(list(extract_bcc(edge)))
                    found_isolated_child = True

            elif edge is not parent_edge:
                edge_stack.append(edge)
                low[i] = min(low[i], vis[j])

        if not is_root and found_isolated_child or is_root and children >= 2:
            artic_points.append(i)

    if n > 0:
        dfs(0, None)

    return bridges, artic_points, bccs

def is_k_vertex_connected(n, edges, k):
    if k <= 1:
        return True

    for remove_set in combinations(range(n), k - 1):
        remaining_nodes = set(range(n)) - set(remove_set)
        subgraph_edges = [e for e in edges if e.i in remaining_nodes and e.j in remaining_nodes]
        adj = make_adjacency_list(n, subgraph_edges)
        
        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor, *_ in adj[node]:
                dfs(neighbor)

        start_node = next(iter(remaining_nodes), None)
        if start_node is None:
            return False

        dfs(start_node)

        if len(visited) != len(remaining_nodes):
            return False

    return True

def is_k_edge_connected(n, edges, k):
    if k <= 1:
        return True

    for remove_set in combinations(edges, k - 1):
        subgraph_edges = [e for e in edges if e not in remove_set]
        adj = make_adjacency_list(n, subgraph_edges)

        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor, *_ in adj[node]:
                dfs(neighbor)

        start_node = next(iter(range(n)), None)
        if start_node is None:
            return False

        dfs(start_node)

        if len(visited) != n:
            return False

    return True

if __name__ == '__main__':
    from pprint import pprint

    test_edges = [
        Edge(0, 1), Edge(1, 2), Edge(2, 3), Edge(3, 4), Edge(4, 0),
        Edge(1, 3), Edge(2, 4)
    ]

    print("Bridges, Articulation Points, BCCs:")
    pprint(bridges_articulation_points_and_bccs(5, test_edges))

    print("\nIs 2-vertex-connected?", is_k_vertex_connected(5, test_edges, 2))
    print("Is 3-vertex-connected?", is_k_vertex_connected(5, test_edges, 3))

    print("\nIs 2-edge-connected?", is_k_edge_connected(5, test_edges, 2))
    print("Is 3-edge-connected?", is_k_edge_connected(5, test_edges, 3))