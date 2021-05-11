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
        da[0][i] = da[0][i-1] + a[0][i]
    for i in range(1, h):
        cnt_w = 0
        for j in range(w):
            cnt_w += a[i][j]
            da[i][j] = da[i-1][j] + cnt_w
    return da


# da_calc(p,q,x,y):(p,q)~(x,y)の長方形の和
def da_calc(p, q, x, y):
    if p > x or q > y:
        return 0
    if p == 0 and q == 0:
        return da[x][y]
    if p == 0:
        return da[x][y] - da[x][q-1]
    if q == 0:
        return da[x][y] - da[p-1][y]
    return da[x][y] - da[p-1][y] - da[x][q-1] + da[p-1][q-1]


n, m, q = map(int, readline().split())
lr = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    l, r = map(int, readline().split())
    lr[l][r] += 1
da = da_generate(n + 1, n + 1, lr)
for _ in range(q):
    p, q = map(int, readline().split())
    print(da_calc(p, p, q, q))
