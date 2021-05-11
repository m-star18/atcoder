import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

import itertools
import numpy as np

n, m = map(int, readline().split())
xyz = np.array([tuple(map(int, readline().split())) for _ in range(n)], dtype=np.int64)
bit = list(itertools.product([-1, 1], repeat=3))
ans = 0
for check in bit:
    v = (xyz * check).sum(axis=1)
    v.sort()
    if m != 0:
        ans = max(ans, v[-m:].sum())
print(ans)
