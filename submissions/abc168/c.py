import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from math import sqrt, cos, pi

a, b, h, m = map(int, read().split())
theat = abs(h * 30 - 6 * m + m / 2) * pi / 180
print(sqrt(a ** 2 + b ** 2 - 2 * a * b * cos(theat)))
