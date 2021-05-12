import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

import numpy as np

w = int(readline())
n, k = map(int, readline().split())
ab = [tuple(map(int, readline().split())) for _ in range(n)]
dp = np.zeros((k + 1, w + 1), dtype=np.int64)

for a, b in ab:
    for i in range(k, 0, -1):
        dp[i, a:] = np.maximum(dp[i, a:], dp[i - 1, :-a] + b)
print(dp.max())
