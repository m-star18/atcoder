import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall
from itertools import permutations

n, m, r = map(int, readline().split())
rr = list(map(int, readline().split()))
graph = [[0] * n for _ in range(n)]
for i in range(m):
    a, b, c = map(int, readline().split())
    graph[a - 1][b - 1] = c
    graph[b - 1][a - 1] = c
cost = floyd_warshall(csr_matrix(graph))
ans = float('inf')
for bit in permutations(rr):
    cnt = 0
    for now, next in zip(bit, bit[1:]):
        cnt += cost[now - 1][next - 1]
    ans = min(cnt, ans)
print(int(ans))
