import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import numpy as np

n, k = map(int, readline().split())
a = np.array(readline().split(), np.int64)
f = np.array(readline().split(), np.int64)
a.sort()
f.sort()
f = f[::-1]
a_sum = a.sum()
left = - 1
right = 10 ** 12

while left + 1 < right:
    mid = (left + right) // 2
    if a_sum - np.minimum(a, mid // f).sum() <= k:
        right = mid
    else:
        left = mid

print(right)
