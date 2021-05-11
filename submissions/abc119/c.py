import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from itertools import product
from collections import Counter

n, a, b, c, *l = map(int, read().split())
ans = float('inf')
for bit in product([0, 1, 2, 3], repeat=n):
    if 0 not in bit or 1 not in bit or 2 not in bit:
        continue
    counter = Counter()
    memo = 0
    for ll, num in zip(l, bit):
        if num == 3:
            continue
        if counter[num] != 0:
            memo += 10
        counter[num] += ll
    ans = min(ans, abs(counter[0] - a) + abs(counter[1] - b) + abs(counter[2] - c) + memo)
print(ans)
