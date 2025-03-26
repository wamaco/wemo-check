"""
================================================================================
MATCHING ALGORITHMS CHEAT SHEET (Python)
================================================================================

This file contains implementations and walkthroughs of key algorithms used for:

    1. Maximum Bipartite Matching
    2. Stable Matching (Stable Marriage)
    3. Maximum Flow (for modeling matchings)
    4. Visualizing and Testing Matching Solutions

-------------------------
When to Use Each Algorithm:
-------------------------
- KUHNâ€™S ALGORITHM:
    - For bipartite graphs (e.g., matching jobs to workers)
    - DFS-based, relatively easy to implement
    - Time Complexity: O(n * e)

- HOPCROFT-KARP ALGORITHM:
    - Optimized for large bipartite graphs
    - Uses BFS + layered DFS
    - Time Complexity: O(âˆšn * e)

- EDMONDS-KARP (Max Flow):
    - For solving matching by modeling it as a flow network
    - More general, works even when Kuhn/Hopcroft isn't suitable
    - Time Complexity: O(V * E^2)

- GALE-SHAPLEY ALGORITHM:
    - Solves the Stable Marriage problem (matching with preferences)
    - Always returns a stable matching
    - Time Complexity: O(n^2)

================================================================================
"""


# ==============================================================================
# 1. KUHN'S ALGORITHM (Maximum Bipartite Matching)
# ==============================================================================
# Description:
#   Given a bipartite graph (L -> R), find the maximum number of matchings
#   such that no two matchings share a node.
#   Works by looking for "augmenting paths" via DFS.
#
# Use Cases:
#   - Assigning students to dorm rooms
#   - Matching people to tasks/jobs
#
# How It Works:
#   For each node in L, try to match it to a node in R.
#   If that node in R is already matched, see if we can
#   reassign its current match to someone else to free it up.
#
# Input:
#   adj = adjacency list { L-node: list of R-nodes it can connect to }
#   L, R = list of nodes in the left and right partitions
#
# Output:
#   Dictionary with R-nodes as keys and matched L-nodes as values
# ==============================================================================
 for Maximum Bipartite Matching
# Time: O(n * e)

def kuhn_maximum_matching(adj, L, R):
    match_to = {}

    def try_match(u, visited):
        for v in adj[u]:
            if v in visited:
                continue
            visited.add(v)
            if v not in match_to or try_match(match_to[v], visited):
                match_to[v] = u
                return True
        return False

    for u in L:
        visited = set()
        try_match(u, visited)

    return match_to


# ==============================================================================
# 3. EDMONDS-KARP ALGORITHM (Maximum Flow)
# ==============================================================================
# Description:
#   Finds the maximum flow in a directed graph using BFS.
#   In bipartite matching, each edge represents 1 unit of capacity.
#   Used to model matching problems as flow problems.
#
# Use Cases:
#   - When Kuhnâ€™s or Hopcroft-Karp doesnâ€™t fit the problem
#   - Any problem reducible to "maximum number of disjoint paths"
#
# Input:
#   capacity = capacity[u][v] = capacity of edge u â†’ v
#   s = source node
#   t = sink node
#
# Output:
#   Maximum flow value (equal to size of max matching)
# ==============================================================================
 (Max Flow)
# Time: O(V * E^2)

from collections import deque, defaultdict

def bfs(capacity, flow, s, t, parent):
    visited = set()
    queue = deque([s])
    visited.add(s)
    while queue:
        u = queue.popleft()
        for v in capacity[u]:
            if v not in visited and capacity[u][v] - flow[u][v] > 0:
                parent[v] = u
                visited.add(v)
                if v == t:
                    return True
                queue.append(v)
    return False

def edmonds_karp(capacity, s, t):
    flow = defaultdict(lambda: defaultdict(int))
    parent = {}
    max_flow = 0

    while bfs(capacity, flow, s, t, parent):
        path_flow = float('inf')
        v = t
        while v != s:
            u = parent[v]
            path_flow = min(path_flow, capacity[u][v] - flow[u][v])
            v = u
        v = t
        while v != s:
            u = parent[v]
            flow[u][v] += path_flow
            flow[v][u] -= path_flow
            v = u
        max_flow += path_flow
    return max_flow


# ==============================================================================
# 4. GALE-SHAPLEY ALGORITHM (Stable Marriage)
# ==============================================================================
# Description:
#   Matches 2 sets (L and R) based on preference rankings.
#   Ensures the resulting match is stable (no two would prefer each other over current partners).
#
# Input:
#   n = number of proposers/responders
#   preferences_L = preference list of proposers (L)
#   preferences_R = preference list of responders (R)
#
# Output:
#   List of matched pairs (L_index, R_index)
# ==============================================================================
 (Stable Marriage)
# Time: O(n^2)

def gale_shapley(n, preferences_L, preferences_R):
    free_L = list(range(n))
    next_proposal = [0] * n
    match_R = [-1] * n
    rank_R = [dict() for _ in range(n)]

    for r in range(n):
        for i, l in enumerate(preferences_R[r]):
            rank_R[r][l] = i

    while free_L:
        l = free_L.pop(0)
        r = preferences_L[l][next_proposal[l]]
        next_proposal[l] += 1
        if match_R[r] == -1:
            match_R[r] = l
        else:
            if rank_R[r][l] < rank_R[r][match_R[r]]:
                free_L.append(match_R[r])
                match_R[r] = l
            else:
                free_L.append(l)

    result = [(match_R[r], r) for r in range(n)]
    return result

# ======================================
# Walkthroughs, Sample Inputs, and Tips
# ======================================

# -------------------------------
# 1. KUHN'S ALGORITHM (Bipartite Matching)
# -------------------------------
# Problem: Match applicants to jobs.
# Sample Bipartite Graph:
# Applicants: ['A', 'B', 'C']
# Jobs: ['1', '2', '3']
# Edges (who can take which job):
# A - 1, 2
# B - 1
# C - 3

if __name__ == "__main__":
    print("=== KUHN'S ALGORITHM SAMPLE ===")
    L = ['A', 'B', 'C']
    R = ['1', '2', '3']
    adj = {
        'A': ['1', '2'],
        'B': ['1'],
        'C': ['3']
    }
    matches = kuhn_maximum_matching(adj, L, R)
    print("Matching result:", matches)
    print()

# -------------------------------
# 2. EDMONDS-KARP (Max Flow)
# -------------------------------
# Problem: Same bipartite graph modeled as flow:
# Nodes: s (source), t (sink), L nodes, R nodes
# Edges:
# s â†’ L nodes (capacity 1)
# L â†’ R (based on ability)
# R â†’ t (capacity 1)

    print("=== EDMONDS-KARP SAMPLE ===")
    from collections import defaultdict

    capacity = defaultdict(lambda: defaultdict(int))
    nodes_L = ['A', 'B', 'C']
    nodes_R = ['1', '2', '3']
    all_nodes = ['s'] + nodes_L + nodes_R + ['t']

    for l in nodes_L:
        capacity['s'][l] = 1
    capacity['A']['1'] = 1
    capacity['A']['2'] = 1
    capacity['B']['1'] = 1
    capacity['C']['3'] = 1
    for r in nodes_R:
        capacity[r]['t'] = 1

    maxflow = edmonds_karp(capacity, 's', 't')
    print("Maximum matching via max flow:", maxflow)
    print()

# -------------------------------
# 3. GALE-SHAPLEY (Stable Marriage)
# -------------------------------
# Problem: Stable matching between proposers and responders
# n = 3
# preferences_L: Each proposer's ranked preferences of responders
# preferences_R: Each responder's ranked preferences of proposers

    print("=== GALE-SHAPLEY SAMPLE ===")
    n = 3
    preferences_L = [
        [0, 1, 2],  # L0 prefers R0 > R1 > R2
        [1, 0, 2],  # L1 prefers R1 > R0 > R2
        [1, 2, 0]   # L2 prefers R1 > R2 > R0
    ]
    preferences_R = [
        [0, 1, 2],  # R0 prefers L0 > L1 > L2
        [2, 1, 0],  # R1 prefers L2 > L1 > L0
        [1, 0, 2]   # R2 prefers L1 > L0 > L2
    ]

    result = gale_shapley(n, preferences_L, preferences_R)
    print("Stable matching:", result)
    print()

# -------------------------------
# How to Modify for Specific Problems
# -------------------------------
# - For grid-based problems: Treat white cells as L and black cells as R, then create edges based on allowed movement.
# - For task assignment: L = workers, R = tasks. Build adj lists based on who can do what.
# - For max-flow on bipartite graphs: Always connect source â†’ L, L â†’ R, R â†’ sink.
# - For stable matching: Add preference matrices. You can switch sides (L proposes vs R proposes) by flipping input roles.

# ----------------------------------------
# Hopcroft-Karp Algorithm (Faster Bipartite Matching)
# Time: O(âˆšn * e)
# ----------------------------------------

from collections import deque

def hopcroft_karp(adj, L, R):
    pair_L = {u: None for u in L}
    pair_R = {v: None for v in R}
    dist = {}

    def bfs():
        queue = deque()
        for u in L:
            if pair_L[u] is None:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = float('inf')
        found = False
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                match_u = pair_R[v]
                if match_u is None:
                    found = True
                elif dist[match_u] == float('inf'):
                    dist[match_u] = dist[u] + 1
                    queue.append(match_u)
        return found

    def dfs(u):
        for v in adj[u]:
            match_u = pair_R[v]
            if match_u is None or (dist[match_u] == dist[u] + 1 and dfs(match_u)):
                pair_L[u] = v
                pair_R[v] = u
                return True
        dist[u] = float('inf')
        return False

    matching = 0
    while bfs():
        for u in L:
            if pair_L[u] is None and dfs(u):
                matching += 1

    return {pair_L[u]: u for u in L if pair_L[u] is not None}

# ----------------------------------------
# Simple Visualization for Matching Results
# ----------------------------------------

def print_matching(match_dict, title="Matching Result"):
    print(f"--- {title} ---")
    for right, left in match_dict.items():
        print(f"{left} -> {right}")
    print()