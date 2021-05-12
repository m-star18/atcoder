import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, a, *x = map(int, read().split())
dp = [[0] * max(sum(x) + 1, a * n + 1) for _ in range(n + 1)]
dp[0][0] = 1
ans = 0
for i in range(n):
    for k in range(n - 1, -1, -1):
        for j in range(sum(x)):
            if dp[k][j] != 0:
                dp[k + 1][j + x[i]] += dp[k][j]
for i in range(1, n + 1):
    ans += dp[i][a * i]
print(ans)
