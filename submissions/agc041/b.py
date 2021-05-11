import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

import numpy as np

n, m, v, p = map(int, readline().split())
a = np.array(read().split(), np.int64)
a.sort()


def check(i):
    if n - i <= p:
        return True
    x = a[i] + m
    y = np.zeros(n, np.int64)
    y = x - a
    y = np.minimum(y, m)
    y[n - p + 1:] = m
    if (y < 0).any():
        return False
    y[i] = 0
    next = y.sum()
    return next >= m * (v - 1)


low = -1
high = n - 1
while low + 1 < high:
    mid = (low + high) // 2
    if check(mid):
        high = mid
    else:
        low = mid
print(n - high)
