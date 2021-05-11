import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import deque

n, q = map(int, readline().split())
graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, readline().split())
    graph[a].append(b)
    graph[b].append(a)
cnt = [0] * (n + 1)
for i in range(q):
    p, x = map(int, readline().split())
    cnt[p] += x


def dfs(s):
    check = [False] * (n + 1)
    stack = deque([s])
    while stack:
        now = stack.pop()
        check[now] = True
        for nxt in graph[now]:
            if check[nxt]:
                continue
            stack.appendleft(nxt)
            cnt[nxt] += cnt[now]


dfs(1)
print(*cnt[1:])
