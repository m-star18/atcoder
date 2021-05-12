import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, k = map(int, readline().split())
ab = [list(map(int, readline().split())) for _ in range(k)]
ab.sort()
mod = 10 ** 4
dp = [[[0] * 2 for _ in range(3)] for _ in range(n + 1)]
if ab[0][0] - 1 == 0:
    dp[0][ab[0][1]][0] = 1
else:
    for j in range(3):
        dp[1][j][0] = 1
for i in range(n):
    if ab:
        if ab[0][0] - 1 == i:
            _, b = ab.pop(0)
            b -= 1
            for j in range(3):
                if j == b:
                    dp[i + 1][b][1] += dp[i][b][0]
                else:
                    dp[i + 1][b][0] += dp[i][j][0] + dp[i][j][1]
            dp[i + 1][b][0] %= mod
            dp[i + 1][b][1] %= mod
            continue
    for j in range(3):
        for k in range(3):
            if j == k:
                dp[i + 1][j][1] += dp[i][j][0]
                dp[i + 1][j][1] %= mod
            else:
                dp[i + 1][j][0] += dp[i][k][0] + dp[i][k][1]
                dp[i + 1][j][0] %= mod
ans = 0
for i in range(3):
    ans += sum(dp[-1][i])
    ans %= mod
print(ans)
