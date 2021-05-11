import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, y = map(int, read().split())
for xx in range(n + 1):
    for yy in range(n + 1):
        v = 9 * xx + 4 * yy
        if v == y // 1000 - n:
            if n - xx - yy >= 0:
                print(xx, yy, n - xx - yy)
                exit()
print(-1, -1, -1)
