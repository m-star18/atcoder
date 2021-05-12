import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from math import floor

a, b, n = map(int, readline().split())
print(floor(a * min(b - 1, n) / b) - a * floor(min(b - 1, n) / b))
