import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from itertools import accumulate
from bisect import bisect_left

n, *a = map(int, read().split())
a.sort()
cumsum = list(accumulate(a))
index = bisect_left(cumsum, a[-1] / 2)
cnt = 0
for (bf, af) in zip(cumsum[:index], a[1:index + 1]):
    cnt += 1
    if bf * 2 < af:
        cnt = 0
print((n - index) + cnt)
