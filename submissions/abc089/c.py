import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import Counter
from operator import mul
from functools import reduce


def cmb(n, r):
    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


n = int(readline())
s = []
check = ['M', 'A', 'R', 'C', 'H']
for i in range(n):
    ss = readline().rstrip().decode()
    if ss[0] in check:
        s.append(ss[0])
counter = list(Counter(s).values())
if len(counter) < 3:
    print(0)
    exit()
ans = cmb(sum(counter), 3)
for v in counter:
    if v >= 2:
        ans -= cmb(v, 2) * (len(s) - v)
        if v >= 3:
            ans -= cmb(v, 3)
print(ans)
