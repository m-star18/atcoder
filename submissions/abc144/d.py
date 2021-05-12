import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from math import atan, tan, pi

a, b, x = map(int, readline().split())


def max_v(si):
    si = si / 180 * pi
    if si < atan(b / a):
        area = a * b - a ** 2 * tan(si) / 2
    else:
        area = b * (b / tan(si) / 2)
    return area * a


low = 0
high = 90
while high - low > 1e-7:
    mid = (low + high) / 2
    if max_v(mid) <= x:
        high = mid
    else:
        low = mid
print((high + low) / 2)
