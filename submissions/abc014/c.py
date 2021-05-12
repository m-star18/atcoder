import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

import itertools

n = int(readline())
table = [0] * (10 ** 6 + 2)
for i in range(n):
    a, b = map(int, readline().split())
    table[a] += 1
    table[b + 1] -= 1
cumsum = list(itertools.accumulate(table))
print(max(cumsum))
