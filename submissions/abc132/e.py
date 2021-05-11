import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import deque

n, m = map(int, readline().split())
graph = [[] for _ in range(n * 3)]
for i in range(m):
    u, v = map(int, readline().split())
    u -= 1
    v -= 1
    graph[u].append(v + n)
    graph[u + n].append(v + 2 * n)
    graph[u + 2 * n].append(v)
s, t = map(lambda x: int(x) - 1, readline().split())
inf = float('inf')
q = deque([s])
dist = [inf] * (3 * n)
dist[s] = 0

while q:
    now = q.popleft()
    for next in graph[now]:
        if dist[next] != inf:
            continue
        dist[next] = dist[now] + 1
        if next == t:
            print(dist[next] // 3)
            exit()
        q.append(next)
print(-1)
