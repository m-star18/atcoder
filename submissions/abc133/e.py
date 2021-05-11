import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, k = map(int, readline().split())
graph = [[] for _ in range(n)]
for i in range(n - 1):
    x, y = map(int, readline().split())
    graph[x - 1].append(y - 1)
    graph[y - 1].append(x - 1)
ans = 1
mod = 10 ** 9 + 7


def dfs(now, par, num):
    global ans
    ans *= num
    ans %= mod
    num = k - 1
    if par != -1:
        num -= 1
    for next in graph[now]:
        if next != par:
            dfs(next, now, num)
            num -= 1


dfs(0, -1, k)
print(ans)
