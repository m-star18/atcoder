import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 7)

import numpy as np

n, w = map(int, readline().split())
vw = [list(map(int, readline().split())) for i in range(n)]
if n <= 30:
    dp = [0]
    check = [0]
    for vv, ww in vw:
        for j in range(len(dp)):
            g = ww + check[j]
            v = vv + dp[j]
            if g > w:
                continue
            if g in check:
                index = check.index(g)
                dp[index] = min(dp[index], v)
            else:
                check.append(g)
                dp.append(v)
    print(max(dp))
elif all(vw[i][1] <= 1000 for i in range(n)):
    dp = np.zeros(n * 1000 + 1, dtype=np.int64)
    for vv, ww in vw:
        dp[ww:] = np.maximum(dp[ww:], dp[:-ww] + vv)
    print(dp[:w + 1].max())
else:
    dp = np.zeros(n * 1000 + 1, dtype=np.int64)
    dp[1:] = 10 ** 18
    for vv, ww in vw:
        dp[vv:] = np.minimum(dp[vv:], dp[:-vv] + ww)
    ans = (dp <= w).nonzero()[0]
    print(ans.max())
