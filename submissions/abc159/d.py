import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import Counter, defaultdict
from operator import mul
from functools import reduce


def cmb(n, r):
    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


n, *a = map(int, read().split())
counter = list(Counter(a).items())
cnt = defaultdict(int)
memo = defaultdict(int)
for k, v in counter:
    if v > 1:
        cnt[k] = cmb(v, 2)
        if v > 2:
            memo[k] = cmb(v - 1, 2)
        else:
            memo[k] = 0
    else:
        cnt[k] = 0
        memo[k] = 0
ans = sum(cnt.values())
for aa in a:
    print(ans - cnt[aa] + memo[aa])
