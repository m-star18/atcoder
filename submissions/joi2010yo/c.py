import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra

n = int(readline())
m = int(readline())
graph = [[float('inf') for _ in range(n)] for _ in range(n)]
for i in range(m):
    a, b = map(int, readline().split())
    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1
cost = dijkstra(csr_matrix(graph))
cnt = 0
for check in cost[0]:
    if 1 <= check <= 2:
        cnt += 1
print(cnt)
