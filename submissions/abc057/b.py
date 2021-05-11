import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, m = map(int, readline().split())
ab = [list(map(int, readline().split())) for _ in range(n)]
cd = [list(map(int, readline().split())) for _ in range(m)]
inf = float('inf')
for a, b in ab:
    cnt = inf
    ans = 0
    for i in range(m):
        v = abs(a - cd[i][0]) + abs(b - cd[i][1])
        if cnt > v:
            cnt = v
            ans = i + 1
    print(ans)
