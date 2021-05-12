import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from math import ceil

h, w = map(int, readline().split())
s = [input() for i in range(h)]
dp = [[float('inf')] * w for j in range(h)]
if s[0][0] == '#':
    dp[0][0] = 1
else:
    dp[0][0] = 0
for i in range(h):
    for j in range(w):
        if w - 1 != j:
            cnt = 0
            if s[i][j + 1] != s[i][j]:
                cnt += 1
            dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + cnt)
        if h - 1 != i:
            cnt = 0
            if s[i + 1][j] != s[i][j]:
                cnt += 1
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + cnt)
print(ceil(dp[-1][-1] / 2))
