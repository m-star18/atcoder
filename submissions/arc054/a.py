import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

l, x, y, s, d = map(int, readline().split())
if d > s:
    h = l - d + s
    n = d - s
else:
    h = s - d
    n = l - s + d
if y > x:
    print(min(n / (y + x), h / (y - x)))
else:
    print(n / (y + x))
