import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import deque

n = int(readline())
a, b = map(lambda x: int(x) - 1, readline().split())
m = int(readline())
graph = [[] for _ in range(n)]
for i in range(m):
    x, y = map(lambda x: int(x) - 1, readline().split())
    graph[x].append(y)
    graph[y].append(x)
inf = float('inf')
mod = 10 ** 9 + 7
dict = [inf] * n
dict[a] = 0
cnt = [0] * n
cnt[a] = 1
q = deque([a])

while q:
    x = q.popleft()
    for next in graph[x]:
        if dict[x] + 1 <= dict[next]:
            cnt[next] += cnt[x]
            if dict[next] == inf:
                dict[next] = dict[x] + 1
                q.append(next)

print(cnt[b] % mod)
