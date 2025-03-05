class Node:
    def __init__(self, seq, i, j):
        self.i = i
        self.j = j
        if self.is_leaf():
            self.v = seq[i]
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
        self.v = min(self.l.v, self.r.v)

    def get(self, i, j):
        if i <= self.i and self.j <= j:
            return self.v
        elif self.j <= i or j <= self.i:
            return float('inf')
        else:
            return min(self.l.get(i, j), self.r.get(i, j))

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


if __name__ == '__main__':
    li = [5, 3, 1, 7, 4, 8]  # , 6, 2]
    rmq = RangeMin(li)  # segment tree for range sum query
    print(rmq.seq)

    queries = [(0, 3), (2, 3), (1, 5), (0, 6), (2, 6), (4, 6)]
    for l, r in queries:
        print(f'sum in [{l}, {r}) is {rmq.range_min(l, r)}')

    print('setting some values...')
    rmq.set(3, 6)
    rmq.set(1, 2)
    rmq.set(4, 5)
    rmq.set(5, 11)

    print(rmq.seq)

    for l, r in queries:
        print(f'sum in [{l}, {r}) is {rmq.range_min(l, r)}')