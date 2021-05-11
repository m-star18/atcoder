import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, k = map(int, readline().split())
xy = []
xx = []
yy = []
for _ in range(n):
    x, y = map(int, readline().split())
    xx.append(x)
    yy.append(y)
    xy.append((x, y))
xx.sort()
yy.sort()
ans = float('inf')
for i, ix in enumerate(xx):
    for jx in xx[i + 1:]:
        for j, iy in enumerate(yy):
            for jy in yy[j + 1:]:
                cnt = 0
                for x, y in xy:
                    if ix <= x <= jx and iy <= y <= jy:
                        cnt += 1
                if cnt >= k:
                    ans = min(ans, (jx - ix) * (jy - iy))
print(ans)
