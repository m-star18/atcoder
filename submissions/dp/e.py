import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

import numpy as np

n, w = map(int, readline().split())
wv = [list(map(int, readline().split())) for i in range(n)]
dp = np.full(n * 1000 + 1, w + 1, dtype=int)
dp[0] = 0
for x, y in wv:
    dp[y:] = np.minimum(dp[y:], dp[:-y] + x)
print(np.max(np.where(dp <= w)))
