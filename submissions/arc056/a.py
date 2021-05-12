import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from math import ceil

a, b, k, l = map(int, readline().split())
if a < b / l:
    print(a * k)
else:
    print(min(a * (k % l) + b * (k // l), b * ceil(k / l)))
