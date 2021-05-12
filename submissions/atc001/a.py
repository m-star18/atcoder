import sys
input = sys.stdin.readline


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)


n, q = map(int, input().split())
uf = UnionFind(n)
for i in range(q):
    p, a, b = map(int, input().split())
    if p == 0:
        uf.union(a, b)
    else:
        if uf.same(a, b):
            print('Yes')
        else:
            print('No')
