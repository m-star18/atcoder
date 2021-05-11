import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, ma, mb = map(int, readline().split())
inf = 40000
dp = [[[inf] * 401 for _ in range(401)] for _ in range(n + 1)]
ans = inf
dp[0][0][0] = 0
for i in range(n):
    a, b, c = map(int, readline().split())
    for j in range(401):
        for k in range(401):
            if dp[i][j][k] != inf:
                dp[i + 1][j + a][k + b] = min(dp[i + 1][j + a][k + b], dp[i][j][k] + c)
                dp[i + 1][j][k] = min(dp[i][j][k], dp[i + 1][j][k])
for i in range(1, 401):
    for j in range(1, 401):
        if i * mb == j * ma:
            if ans > dp[n][i][j]:
                ans = dp[n][i][j]
if ans == inf:
    ans = -1
print(ans)
