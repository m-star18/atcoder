import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

import numpy as np

n, m = map(int, readline().split())
a = np.array(readline().split(), dtype=np.int64)
b = np.array(readline().split(), dtype=np.int64)
a.sort()
b.sort()


def check(mid):
    memo = np.searchsorted(a, mid // b, side='right').sum()
    return memo >= m


left = 0
right = 10 ** 18
while left + 1 < right:
    mid = (left + right) // 2
    if check(mid):
        right = mid
    else:
        left = mid
print(right)
