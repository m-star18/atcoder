import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

w, h, n = map(int, readline().split())
xy = [list(map(int, readline().split())) for _ in range(n)]
cnt = 0
xx, yy = xy.pop(0)
for x, y in xy:
    if (xx <= x and yy <= y) or (xx >= x and yy >= y):
        cnt += max(abs(x - xx), abs(y - yy))
    else:
        cnt += abs(x - xx) + abs(y - yy)
    xx, yy = x, y
print(cnt)
