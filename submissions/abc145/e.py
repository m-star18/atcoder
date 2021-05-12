import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

import numpy as np

n, t = map(int, readline().split())
ab = sorted([tuple(map(int, readline().split())) for i in range(n)])
dp = np.zeros(t, dtype=int)
ans = 0
for a, b in ab:
    ans = max(ans, max(dp) + b)
    if a < t:
        dp[a:] = np.maximum(dp[a:], dp[:-a] + b)
print(ans)
