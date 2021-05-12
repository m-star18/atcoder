import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import defaultdict

n, w = map(int, readline().split())
wv = [tuple(map(int, readline().split())) for i in range(n)]
dp = defaultdict(int)
dp[0] = 0

for ww, v in wv:
    for xw, xv in list(dp.items()):
        if ww + xw <= w:
            dp[ww + xw] = max(dp[ww + xw], v + xv)
print(max(dp.values()))
