import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

h, w, k = map(int, readline().split())
dp = [[0] * w for _ in range(h + 1)]
dp[0][0] = 1
mod = 10 ** 9 + 7
for i in range(h):
    for b in range(1 << (w - 1)):
        if '11' in bin(b):
            continue
        for j in range(w):
            if j and b & (1 << (j - 1)):
                dp[i + 1][j - 1] += dp[i][j]
            elif b & (1 << j):
                dp[i + 1][j + 1] += dp[i][j]
            else:
                dp[i + 1][j] += dp[i][j]
print(dp[-1][k - 1] % mod)
