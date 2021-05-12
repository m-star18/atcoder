import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from math import pi

r, d = map(int, readline().split())
print(r ** 2 * pi ** 2 * d * 2)
