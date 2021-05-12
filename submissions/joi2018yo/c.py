import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

h, w = map(int, readline().split())
a = [list(map(int, readline().split())) for _ in range(h)]


def check(i, j):
    cnt = 0
    for y in range(h):
        if i == y:
            continue
        for x in range(w):
            if j == x:
                continue
            cnt += a[y][x] * min(abs(x - j), abs(y - i))
    return cnt


ans = float('inf')
for i in range(h):
    for j in range(w):
        v = check(i, j)
        if v < ans:
            ans = v
print(ans)
