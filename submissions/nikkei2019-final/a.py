import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

import numpy as np

n = int(readline())
a = np.array(readline().split(), dtype=np.int64)
v = np.zeros(n, dtype=np.int64)
ans = [0] * n
for i in range(n):
    v[:n - i] += a[i:]
    ans[i] = v[:n - i].max()
print(*ans, sep='\n')
