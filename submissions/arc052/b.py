import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from math import pi

n, q = map(int, readline().split())
xrh = [tuple(map(int, readline().split())) for _ in range(n)]
for _ in range(q):
    a, b = map(int, readline().split())
    ans = 0
    for x, r, h in xrh:
        if a >= x + h or b <= x:
            continue
        ans += pow(r, 2) * h if a <= x else pow(r * (x + h - a) / h, 2) * (x + h - a)
        if b < x + h:
            ans -= pow(r * (x + h - b) / h, 2) * (x + h - b)
    print(ans * pi / 3)
