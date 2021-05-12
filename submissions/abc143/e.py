import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall

n, m, l = map(int, readline().split())
graph = [[0] * n for _ in range(n)]
inf = float('inf')
for i in range(m):
    a, b, c = map(int, readline().split())
    graph[a - 1][b - 1] = c
    graph[b - 1][a - 1] = c
cost = floyd_warshall(csr_matrix(graph))
cnt = [[0] * n for _ in range(n)]
for i, cost_i in enumerate(cost):
    for j, v in enumerate(cost_i):
        if l >= v:
            cnt[i][j] = 1
cnt = floyd_warshall(csr_matrix(cnt))
q = int(readline())
for _ in range(q):
    s, t = map(int, readline().split())
    if cnt[s - 1][t - 1] == inf:
        print(-1)
    else:
        print(int(cnt[s - 1][t - 1] - 1))
