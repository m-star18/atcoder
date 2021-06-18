import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, m = map(int, readline().split())
cost = [[10 ** 9] * n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, readline().split())
    cost[a - 1][b - 1] = c
    cost[b - 1][a - 1] = c
for i in range(n):
    cost[i][i] = 0
for k in range(n):
    for i in range(n):
        for j in range(i + 1, n):
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
            cost[j][i] = cost[i][j]
k = int(readline())
for _ in range(k):
    x, y, z = map(int, readline().split())
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            cost[i][j] = min(cost[i][j], cost[i][x - 1] + cost[y - 1][j] + z, cost[i][y - 1] + cost[x - 1][j] + z)
            cost[j][i] = cost[i][j]
            ans += cost[i][j]
    print(ans)
