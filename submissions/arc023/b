import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

r, c, d = map(int, readline().split())
a = [list(map(int, readline().split())) for _ in range(r)]
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
dict = [[0] * c for _ in range(r)]
q = [(0, 0)]
cnt = 0
while q:
    qq = set()
    cnt += 1
    for y, x in q:
        for dy, dx in move:
            yy, xx = y + dy, x + dx
            if xx < 0 or yy < 0 or xx > c - 1 or yy > r - 1:
                continue
            if dict[yy][xx] > 0:
                continue
            dict[yy][xx] = cnt
            qq.add((yy, xx))
    q = qq
ans = 0
memo = d % 2
for i in range(r):
    for j in range(c):
        if dict[i][j] <= d and dict[i][j] % 2 == memo:
            if ans < a[i][j]:
                ans = a[i][j]
print(ans)
