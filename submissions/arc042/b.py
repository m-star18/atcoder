import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from math import sqrt

x, y = map(int, readline().split())
n = int(readline())
xy = [list(map(int, readline().split())) for _ in range(n)]
xy.append(xy[0])
ans = float('inf')
for i in range(n):
    a = [x - xy[i][0], y - xy[i][1]]
    b = [xy[i + 1][0] - xy[i][0], xy[i + 1][1] - xy[i][1]]
    ans = min(ans, abs(a[0] * b[1] - a[1] * b[0]) / sqrt(b[0] ** 2 + b[1] ** 2))
print(ans)
