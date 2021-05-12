import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)


# da[i][j]:(0,0)~(i,j)の長方形の和
def da_generate(h, w, a):
    da = [[0] * w for j in range(h)]
    da[0][0] = a[0][0]
    for i in range(1, w):
        da[0][i] = da[0][i - 1] + a[0][i]
    for i in range(1, h):
        cnt_w = 0
        for j in range(w):
            cnt_w += a[i][j]
            da[i][j] = da[i - 1][j] + cnt_w
    return da


# da_calc(p,q,x,y):(p,q)~(x,y)の長方形の和
def da_calc(p, q, x, y):
    if p > x or q > y:
        return 0
    if p == 0 and q == 0:
        return da[x][y]
    if p == 0:
        return da[x][y] - da[x][q - 1]
    if q == 0:
        return da[x][y] - da[p - 1][y]
    return da[x][y] - da[p - 1][y] - da[x][q - 1] + da[p - 1][q - 1]


m, n = map(int, readline().split())
a, b = map(int, readline().split())
br = [list(map(int, readline().split())) for _ in range(n)]
inf = float('inf')
for i in range(n):
    for j in range(m):
        if br[i][j] == -1:
            br[i][j] = 10 ** 5
da = da_generate(n, m, br)
ans = inf
for i in range(n - b):
    for j in range(m - a):
        v = da_calc(i, j, i + b - 1, j + a - 1)
        if ans > v:
            ans = v
print(ans)
