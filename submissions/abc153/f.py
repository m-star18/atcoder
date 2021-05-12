import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from math import ceil
from bisect import bisect_right

n, d, a = map(int, readline().split())
xh = [list(map(int, readline().split())) for i in range(n)]
xh.sort()
imos = [0] * (n + 1)
cnt = 0
ans = 0
x = []
for i in range(n):
    xh[i][1] = ceil(xh[i][1] / a)
    x.append(xh[i][0])
for i in range(n):
    cnt += imos[i]
    n_h = xh[i][1] - cnt
    if n_h > 0:
        cnt += n_h
        ans += n_h
        imos[bisect_right(x, x[i] + 2 * d)] -= n_h
print(ans)
