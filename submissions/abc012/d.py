import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall

n, m = map(int, readline().split())
memo_graph = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    a, b, t = map(int, readline().split())
    memo_graph[a][b] = t
    memo_graph[b][a] = t
graph = csr_matrix(memo_graph)
cost = floyd_warshall(graph)
inf = float('inf')
ans = inf
for i in range(n + 1):
    memo = 0
    for j in range(n + 1):
        if cost[i][j] != inf and i != j:
            if cost[i][j] > memo:
                memo = cost[i][j]
    if ans > memo > 0:
        ans = memo
print(ans)
