import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import defaultdict
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
    return over // under


n, p = map(int, readline().split())
a = list(map(lambda x: int(x) % 2, readline().split()))
dict = defaultdict(int)
for aa in a:
    dict[aa] += 1
memo = 2 ** dict[0]
ans = 0
if p == 0:
    ans += memo
    m = 2
else:
    m = 1
for i in range(m, dict[1] + 1, 2):
    ans += nCr(dict[1], i) * memo
print(ans)
