import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, m = map(int, readline().split())
s = list(map(int, readline().split()))
t = list(map(int, readline().split()))
dp = [[0] * (n + 1) for _ in range(m + 1)]
cumsum = [[0] * (n + 1) for _ in range(m + 1)]
dp[0][0] = 1
mod = 10 ** 9 + 7
for i, tt in enumerate(t):
    i += 1
    for j, ss in enumerate(s):
        j += 1
        if tt == ss:
            dp[i][j] = cumsum[i - 1][j - 1] + 1
            dp[i][j] %= mod
        else:
            dp[i][j] = 0
        cumsum[i][j] = cumsum[i - 1][j] + cumsum[i][j - 1] - cumsum[i - 1][j - 1] + dp[i][j]
        cumsum[i][j] %= mod
print(cumsum[-1][-1] + 1)
