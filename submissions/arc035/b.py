import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import Counter
from itertools import accumulate

n = int(readline())
t = sorted([int(readline()) for _ in range(n)])
print(sum(accumulate(t)))
mod = 10 ** 9 + 7
fact = [1]
ans = 1
for i in range(1, n + 1):
    fact.append(fact[-1] * i % mod)
for v in Counter(t).values():
    ans *= fact[v] % mod
print(ans % mod)
