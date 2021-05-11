import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall

h, w = map(int, readline().split())
memo_graph = [list(map(int, readline().split())) for _ in range(10)]
cost = floyd_warshall(csr_matrix(memo_graph))
ans = 0
for i in range(h):
    for a in list(map(int, readline().split())):
        if a != -1:
            ans += cost[a][1]
print(int(ans))
