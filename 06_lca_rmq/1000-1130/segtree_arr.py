class SegTreeArray:
    # range sum query
    def __init__(self, it):
        self.arr = [i for i in it]
        self.n = len(self.arr)

        self.k = len(format(self.n , 'b'))
        if self.n != 2 ** (self.k - 1):
            self.k += 1

        self.tree = [0] * (2 ** self.k - 1)
        self.arr += [0] * ((2 ** (self.k - 1)) - self.n)
        self._build(0, 0, 2 ** (self.k - 1))
        super().__init__()

    def _build(self, i, il, ir):
        # tree[i] = range sum on [il, ir)
        if il + 1 == ir:
            self.tree[i] = self.arr[il]
            return self.tree[i]
        m = (il + ir) // 2
        l_res = self._build(2 * i + 1, il, m)
        r_res = self._build(2 * i + 2, m, ir)
        self.tree[i] = l_res + r_res
        return self.tree[i]

    def get(self, l, r):
        # interval [l, r)
        def _get(i, il, ir):
            if r <= il or l >= ir:  # subtree range outside of [l, r)
                return 0
            elif l <= il and ir <= r:  # subtree range within [l, r)
                return self.tree[i]
            m = (il + ir) // 2
            l_sum = _get(2 * i + 1, il, m)
            r_sum = _get(2 * i + 2, m, ir)
            return l_sum + r_sum
        return _get(0, 0, len(self.arr))

    def set(self, j, v):
        # j is 0-based index, v is value
        assert 0 <= j < self.n
        self.arr[j] = v
        def _set(i, il, ir):
            if il + 1 == ir:
                self.tree[i] = v
                return
            m = (il + ir) // 2
            if j < m:
                _set(i * 2 + 1, il, m)
            else:
                _set(i * 2 + 2, m, ir)
            self.tree[i] = self.tree[i * 2 + 1] + self.tree[i * 2 + 2]
        _set(0, 0, len(self.arr))


if __name__ == '__main__':
    li = [5, 3, 1, 7, 4, 8]  # , 6, 2]
    rsq = SegTreeArray(li)  # segment tree for range sum query
    print(rsq.arr)

    queries = [(0, 3), (2, 3), (1, 5), (0, 6), (2, 6), (4, 6)]
    for l, r in queries:
        print(f'sum in [{l}, {r}) is {rsq.get(l, r)}')

    print('setting some values...')
    rsq.set(3, 6)
    rsq.set(1, 2)
    rsq.set(4, 5)
    rsq.set(5, 11)

    print(rsq.arr)

    for l, r in queries:
        print(f'sum in [{l}, {r}) is {rsq.get(l, r)}')
    # print(rsq.get(1, 1))