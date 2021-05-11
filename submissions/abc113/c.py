import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from bisect import bisect_left

n, m = map(int, readline().split())
py = [list(map(int, readline().split())) for _ in range(m)]
check = sorted(py)
idx = [0] * (n + 1)
memo = 0
for i, (p, _) in enumerate(check):
    if memo != p:
        idx[p] = i
        memo = p
for p, y in py:
    yy = str(bisect_left(check, [p, y]) - idx[p] + 1)
    p = str(p)
    print('0' * (6 - len(p)) + p + '0' * (6 - len(yy)) + yy)
