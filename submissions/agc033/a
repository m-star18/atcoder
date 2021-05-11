import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import deque

h, w = map(int, readline().split())
a = [input() for i in range(h)]
q = []
dist = [[True] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if a[i][j] == '#':
            q.append((i, j))
            dist[i][j] = False
cnt = -1
while q:
    cnt += 1
    qq = deque()
    for y, x in q:
        if x + 1 < w and dist[y][x + 1]:
            dist[y][x + 1] = False
            qq.append((y, x + 1))
        if x - 1 >= 0 and dist[y][x - 1]:
            dist[y][x - 1] = False
            qq.append((y, x - 1))
        if y + 1 < h and dist[y + 1][x]:
            dist[y + 1][x] = False
            qq.append((y + 1, x))
        if y - 1 >= 0 and dist[y - 1][x]:
            dist[y - 1][x] = False
            qq.append((y - 1, x))
    q = qq
print(cnt)
