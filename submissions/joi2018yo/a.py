import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from math import ceil

n, a, b, c, d = map(int, readline().split())
print(min(ceil(n / a) * b, ceil(n / c) * d))
