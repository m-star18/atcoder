import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from operator import mul
from functools import reduce


def nCr(n, r):
    if n < r:
        return 0
    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under % mod


n, k = map(int, read().split())
mod = 10 ** 9 + 7
for i in range(1, k + 1):
    print(nCr(n - k + 1, i) * nCr(k - 1, i - 1) % mod)
