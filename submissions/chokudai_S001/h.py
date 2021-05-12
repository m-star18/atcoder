import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from bisect import bisect_left

n, *a = map(int, read().split())
inf = float('inf')
dp = [inf] * n
for aa in a:
    dp[bisect_left(dp, aa)] = aa
print(bisect_left(dp, inf))
