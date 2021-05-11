import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import deque

n = int(readline())
graph = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, readline().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
c = list(map(int, readline().split()))
c.sort()
print(sum(c[:-1]))
q = deque([0])
d = [-1] * n

while q:
    x = q.popleft()
    d[x] = c.pop()
    for next in graph[x]:
        if d[next] < 0:
            q.appendleft(next)

print(*d)
