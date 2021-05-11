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


def prime_decomposition(n):
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0:
            n //= i
            table.append(i)
        i += 1
    if n > 1:
        table.append(n)
    return table


n = int(readline())
table = []
for i in range(1, n + 1):
    table += prime_decomposition(i)
counter = list(Counter(table).values())
ans = [0, 0, 0, 0, 0]
for v in counter:
    if v >= 2:
        ans[0] += 1
        if v >= 4:
            ans[1] += 1
            if v >= 14:
                ans[2] += 1
                if v >= 24:
                    ans[3] += 1
                    if v >= 74:
                        ans[4] += 1
if n < 10:
    print(0)
    exit()
print(ans[4] + ans[3] * (ans[0] - 1) + ans[2] * (ans[1] - 1) + (ans[0] - 2) * cmb(ans[1], 2))
