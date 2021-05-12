import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from itertools import combinations

n = int(readline())
xy = [tuple(map(int, readline().split())) for _ in range(n)]
ans = 0
for a, b, c in combinations(xy, 3):
    s = abs((b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1]))
    if s != 0 and not s & 1:
        ans += 1
print(ans)
