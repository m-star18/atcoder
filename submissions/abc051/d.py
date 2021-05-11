import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall

n, m = map(int, readline().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
abc = [list(map(int, readline().split())) for _ in range(m)]
for a, b, c in abc:
    graph[a][b] = c
    graph[b][a] = c
cost = floyd_warshall(csr_matrix(graph))
cnt = 0
for a, b, c in abc:
    if cost[a][b] < c:
        cnt += 1
print(cnt)
