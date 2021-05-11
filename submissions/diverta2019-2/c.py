import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from bisect import bisect_right

n = int(readline())
a = list(map(int, readline().split()))
a.sort()
if a[0] <= 0 and a[-1] >= 0:
    print(sum(map(lambda x: abs(int(x)), a)))
    idx = bisect_right(a, 0)
    idx -= 1 if idx == n else 0
    x = a[0]
    y = a[idx]
    for aa in a[1:idx]:
        print(y, aa)
        y -= aa
    for aa in a[idx + 1:]:
        print(x, aa)
        x -= aa
    print(y, x)
else:
    if a[0] < 0:
        print(-sum(a) + 2 * a[-1])
        a = a[::-1]
    else:
        print(sum(a) - 2 * a[0])
    x = a[0]
    y = a[-1]
    for aa in a[1:-1]:
        print(x, aa)
        x -= aa
    if a[0] < 0:
        y, x = x, y
    print(y, x)
