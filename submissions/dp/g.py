import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, m = map(int, readline().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    x, y = map(int, readline().split())
    graph[x].append(y)
dp = [-1] * (n + 1)


def check(v):
    if dp[v] != -1:
        return dp[v]
    if graph[v]:
        dp[v] = max(check(u) for u in graph[v]) + 1
    else:
        dp[v] = 0
    return dp[v]


print(max(check(v) for v in range(1, n + 1)))
