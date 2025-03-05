import random

from dataclasses import dataclass, field

from sample_graphs import G3_ud_edgelist as T1_el
from sample_graphs import T_ud_edgelist as T2_el


class Node:
    def __init__(self, seq, i, j):
        self.i = i
        self.j = j
        if self.is_leaf():
            self.v = seq[i]
            self.seqidx = i
            self.l = self.r = None
        else:
            m = (i + j) // 2
            self.l = Node(seq, i, m)
            self.r = Node(seq, m, j)
            self.combine()
        super().__init__()

    def is_leaf(self):
        return self.i + 1 == self.j

    def combine(self):
        assert not self.is_leaf()
        if self.l.v < self.r.v:
            self.v = self.l.v
            self.seqidx = self.l.seqidx
        else:
            self.v = self.r.v
            self.seqidx = self.r.seqidx
        # self.v = min(self.l.v, self.r.v)

    def get(self, i, j):
        if i <= self.i and self.j <= j:
            return (self.v, self.seqidx)
        elif self.j <= i or j <= self.i:
            return (float('inf'), -1)
        else:
            lv, li = self.l.get(i, j)
            rv, ri = self.r.get(i, j)
            if lv < rv:
                return (lv, li)
            else:
                return (rv, ri)

    def set(self, i, v):
        if self.i <= i < self.j:
            if self.is_leaf():
                self.v = v
            else:
                self.l.set(i, v)
                self.r.set(i, v)
                self.combine()


class RangeMin:
    def __init__(self, seq):
        self.root = Node(seq, 0, len(seq))
        self.seq = seq
        super().__init__()

    def range_min(self, i, j):
        return self.root.get(i, j)

    def set(self, i, v):
        self.root.set(i, v)
        self.seq[i] = v


@dataclass
class TreeNode:
    label: int
    v: int
    children: list["TreeNode"] = field(default_factory=list)
    depth: int = 1
    parent: "TreeNode | None" = None


def edgelist_to_adj(el):
    adj = {}
    for i, j in el:
        if i not in adj:
            adj[i] = []
        if j not in adj:
            adj[j] = []
        adj[i].append(j)
        adj[j].append(i)
    return adj


def get_rooted_tree(adj, i):
    n = len(adj)
    vis = [False] * n
    root = TreeNode(i, i)

    nodes = {}

    def _dfs(i, parent):
        vis[i] = True
        nodes[i] = parent
        for j in adj[i]:
            if not vis[j]:
                child = TreeNode(j, j)
                child.parent = parent
                child.depth = parent.depth + 1
                parent.children.append(child)
                _dfs(j, child)
    _dfs(i, root)
    root.parent = root
    return root, nodes


def euler_tour(root):
    tour = []
    labels = []
    def _euler_tour(root):
        root.index = len(tour) # use leftmost occurence as seq index
        tour.append(root.depth)
        labels.append(root.label)
        for node in root.children:
            _euler_tour(node)
            tour.append(root.depth)
            labels.append(root.label)
    _euler_tour(root)
    return tour, labels


root1, nodes1 = get_rooted_tree(edgelist_to_adj(T1_el), 6)
seq1, labels1 = euler_tour(root1)
print(seq1)
rm = RangeMin(seq1)
# Euler tour sequence generated in O(n) time
# (O(n) segtree setup + O(lg n) queries)

print('Compute LCA of u and v using range min')
for u in range(len(nodes1)):
    for v in range(u + 1, len(nodes1)):
        idx1 = nodes1[u].index
        idx2 = nodes1[v].index
        if idx1 > idx2:
            idx1, idx2 = idx2, idx1
        m, m_i = rm.range_min(idx1, idx2)
        print(f'LCA of {u} and {v} using RMQ is {labels1[m_i]} with depth {m}')