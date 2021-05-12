import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

m = int(readline())
n = int(readline())
a = [list(map(int, readline().split())) for _ in range(n)]
ans = 0


def dfs(y, x, cnt):
    a[y][x] = 0
    v = cnt + 1
    for dy, dx in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        xx = x + dx
        yy = y + dy
        if 0 <= xx < m and 0 <= yy < n and a[yy][xx] == 1:
            cnt = max(dfs(yy, xx, v), cnt)
    a[y][x] = 1
    return cnt


for i, aa in enumerate(a):
    for j, check in enumerate(aa):
        if check == 1:
            ans = max(dfs(i, j, 1), ans)
print(ans)
