import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import deque

n, u, v = map(int, readline().split())
graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, readline().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(v):
    dist = [-1] * (n + 1)
    stack = deque([v])
    dist[v] = 0
    while stack:
        v = stack.popleft()
        memo = dist[v] + 1
        for w in graph[v]:
            if dist[w] >= 0:
                continue
            dist[w] = memo
            stack.append(w)
    return dist


U, V = dfs(u), dfs(v)
ans = 0
for x, y in zip(U[1:], V[1:]):
    if x < y:
        ans = max(ans, y - 1)
print(ans)
