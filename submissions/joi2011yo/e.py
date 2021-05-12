import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

h, w, n = map(int, readline().split())
xy = [input() for i in range(h)]
g = [[] for j in range(n + 1)]
check = [str(i) for i in range(n + 1)]
for i in range(h):
    for j in range(w):
        if xy[i][j] == 'S':
            g[0] = [i, j]
        elif xy[i][j] in check:
            g[check.index(xy[i][j])] = [i, j]
p = [(-1, 0), (1, 0), (0, -1), (0, 1)]
inf = float('inf')
cnt = 0
g[0] = tuple(g[0])
for i in range(n):
    g[i + 1] = tuple(g[i + 1])
    q = [g[i]]
    dist = [[inf] * w for _ in range(h)]
    dist[g[i][0]][g[i][1]] = 0
    while q:
        cnt += 1
        qq = []
        for x, y in q:
            for dx, dy in p:
                xx, yy = x + dx, y + dy
                if xx < 0 or xx > h - 1 or yy < 0 or yy > w - 1:
                    continue
                if xy[xx][yy] == 'X' or dist[xx][yy] != inf:
                    continue
                dist[xx][yy] = cnt
                qq.append((xx, yy))
        q = qq
        if g[i + 1] in q:
            break
print(cnt)
