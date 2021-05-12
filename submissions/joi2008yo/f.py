import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra

n, k = map(int, readline().split())
inf = float('inf')
memo_graph = [[inf] * (n + 1) for _ in range(n + 1)]
cost = memo_graph
for i in range(k):
    check = list(map(int, readline().split()))
    if check[0] == 0:
        if cost[check[1]][check[2]] == inf:
            print(-1)
        else:
            print(int(cost[check[1]][check[2]]))
    else:
        if memo_graph[check[1]][check[2]] > check[3]:
            memo_graph[check[1]][check[2]] = memo_graph[check[2]][check[1]] = check[3]
        graph = csr_matrix(memo_graph)
        cost = dijkstra(graph)
