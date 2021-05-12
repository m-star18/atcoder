import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import defaultdict

n = int(readline())
graph = [[] for i in range(n + 1)]
memo = defaultdict(int)
for i in range(2, n + 1):
    b = int(readline())
    graph[b].append(i)
for i in range(n, 0, -1):
    if not graph[i]:
        memo[i] = 1
    else:
        p = 1
        m = 10 ** 20
        for u in graph[i]:
            tmp = memo[u]
            p = max(p, tmp)
            m = min(m, tmp)
        memo[i] = 1 + p + m
print(memo[1])
