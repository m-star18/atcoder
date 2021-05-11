import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

h, w = map(int, readline().split())
s = [input() for i in range(h)]
q = [(0, 0)]
g = (h - 1, w - 1)
test = [(0, 1), (0, -1), (1, 0), (-1, 0)]
inf = float('inf')
dist = [[inf] * w for _ in range(h)]
dist[0][0] = 0
cnt = 0
while 1:
    qq = []
    cnt += 1
    for y, x in q:
        for dy, dx in test:
            yy, xx = y + dy, x + dx
            if xx < 0 or yy < 0 or xx > w - 1 or yy > h - 1:
                continue
            if s[yy][xx] == '#' or dist[yy][xx] != inf:
                continue
            dist[yy][xx] = cnt
            qq.append((yy, xx))
    q = qq
    if g in q:
        break
    if q:
        continue
    else:
        print(-1)
        exit()
for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            cnt += 1
print(h * w - cnt - 1)
