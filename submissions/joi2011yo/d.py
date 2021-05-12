import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, *a = map(int, read().split())
b = a.pop(-1)
dp = [0] * (21 * (n - 1))
dp[a.pop(0)] = 1
for i in range(n - 2):
    for j in range(21):
        p = j + a[i]
        m = j - a[i]
        if p <= 20:
            dp[21 * (i + 1) + p] += dp[21 * i + j]
        if m >= 0:
            dp[21 * (i + 1) + m] += dp[21 * i + j]
print(dp[21 * (n - 2) + b])
