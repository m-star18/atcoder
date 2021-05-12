import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

import numpy as np

n, k = map(int, readline().split())
a = np.array(list(map(int, readline().split())), np.int64)
a = np.sort(a)
z = a[a == 0]
p = a[a > 0]
m = a[a < 0]


def check(mid):
    cnt = 0
    # 0以上のとき
    if mid >= 0:
        cnt += len(z) * n
    cnt += np.searchsorted(a, mid // p, side='right').sum()
    cnt += (n - np.searchsorted(a, (-mid - 1) // (-m), side='right')).sum()
    cnt -= np.count_nonzero(a * a <= mid)
    return cnt // 2


left = -10 ** 18
right = 10 ** 18
while left + 1 < right:
    mid = (left + right) // 2
    if check(mid) >= k:
        right = mid
    else:
        left = mid
print(right)
