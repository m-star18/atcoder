import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall

n, m = map(int, readline().split())
graph = [[float('inf')] * n for i in range(n)]
for i in range(m):
    a, b = map(int, readline().split())
    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1
cost = floyd_warshall(csr_matrix(graph))
for ans in cost:
    print(np.count_nonzero(ans == 2))
