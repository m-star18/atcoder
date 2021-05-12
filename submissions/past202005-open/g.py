import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, x, y = map(int, readline().split())
q = [(250, 250)]
move = [(1, 1), (1, -1), (1, 0), (0, 1), (0, -1), (-1, 0)]
dist = [[False] * 501 for _ in range(501)]
for _ in range(n):
    xx, yy = map(int, readline().split())
    dist[yy + 250][xx + 250] = True
g = (y + 250, x + 250)
dist[250][250] = True
cnt = 0
while q:
    qq = []
    cnt += 1
    for y, x in q:
        for dy, dx in move:
            yy, xx = y + dy, x + dx
            if xx < 0 or yy < 0 or xx > 500 or yy > 500:
                continue
            if dist[yy][xx]:
                continue
            if (yy, xx) == g:
                print(cnt)
                exit()
            dist[yy][xx] = True
            qq.append((yy, xx))
    q = qq
print(-1)
