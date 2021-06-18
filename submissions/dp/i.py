import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
p = list(map(float, readline().split()))
dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 1
for i in range(n):
    for j in range(i + 1):
        dp[i + 1][j + 1] += dp[i][j] * p[i]
        dp[i + 1][j] += dp[i][j] * (1 - p[i])
print(sum(dp[-1][n // 2 + 1:]))
