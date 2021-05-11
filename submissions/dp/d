import sys
input = sys.stdin.readline

n, W = map(int, input().split())
dp = [[0 for i in range(W + 1)] for j in range(n + 1)]
wv = [[int(x) for x in input().split()] for _ in range(n)]

for i in range(n):
    for j in range(W + 1):
        if j - wv[i][0] >= 0:
            dp[i + 1][j] = max(dp[i][j - wv[i][0]] + wv[i][1], dp[i + 1][j])
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
print(max(dp[-1]))
