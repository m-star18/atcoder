import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from copy import deepcopy

h, w = map(int, readline().split())
s = [readline().rstrip().decode() for _ in range(h)]
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
sg = []
memo = [[False] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if s[i][j] == '.':
            sg.append((i, j))
        else:
            memo[i][j] = True
ans = 0
for ss in sg:
    q = [ss]
    cnt = 0
    dist = deepcopy(memo)
    dist[ss[0]][ss[1]] = True
    while q:
        cnt += 1
        qq = []
        for y, x in q:
            for dy, dx in move:
                xx, yy = x + dx, y + dy
                if xx < 0 or yy > h - 1 or yy < 0 or xx > w - 1:
                    continue
                if dist[yy][xx]:
                    continue
                dist[yy][xx] = True
                qq.append((yy, xx))
        q = qq
    ans = max(ans, cnt - 1)
print(ans)
