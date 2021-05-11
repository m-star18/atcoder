import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

h, w = map(int, readline().split())
a = [readline().rstrip().decode() for _ in range(h)]
dp = [[0] * w for _ in range(h)]
mod = 10 ** 9 + 7
dp[0][0] = 1

for i in range(h):
    for j in range(w):
        if a[i][j] != '#':
            if i != h - 1:
                if a[i + 1][j] != '#':
                    dp[i + 1][j] += dp[i][j]
                    dp[i + 1][j] %= mod
            if j != w - 1:
                if a[i][j + 1] != '#':
                    dp[i][j + 1] += dp[i][j]
                    dp[i][j + 1] %= mod
print(dp[-1][-1] % mod)
