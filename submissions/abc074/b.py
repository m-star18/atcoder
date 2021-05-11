import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

import numpy as np

n = int(readline())
graph = np.array([list(map(int, readline().split())) for _ in range(n)])
inf = 10 ** 10
ans = 0
for i in range(n):
    graph[i][i] = inf
for i in range(n):
    for j in range(i + 1, n):
        v = np.min(graph[i] + graph[j])
        if graph[i][j] > v:
            print(-1)
            exit()
        elif graph[i][j] < v:
            ans += graph[i][j]
print(ans)
