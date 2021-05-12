import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

import numpy as np

n, m = map(int, readline().split())
a = np.array(read().split(), np.int64)
a.sort()


def check(mid):
    mid = np.searchsorted(a, mid - a)
    return n * n - mid.sum() >= m


left = 0
right = 10 ** 6
while left + 1 < right:
    mid = (left + right) // 2
    if check(mid):
        left = mid
    else:
        right = mid

mid = np.searchsorted(a, right - a)
cumsum = np.zeros(n + 1, np.int64)
cumsum[1:] = np.cumsum(a)
ans = (cumsum[-1] - cumsum[mid]).sum() + (a * (n - mid)).sum() + (m - n * n + mid.sum()) * left
print(ans)
