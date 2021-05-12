import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

h, w = map(int, readline().split())
a = [list(map(int, readline().split())) for _ in range(h)]
dp = [[-1] * w for _ in range(h)]
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
mod = 10 ** 9 + 7


def check(i, j):
    if dp[i][j] != -1:
        return dp[i][j]
    cnt = 1
    for dy, dx in move:
        if 0 <= dy + i < h and 0 <= dx + j < w:
            if a[i][j] > a[i + dy][j + dx]:
                cnt += check(i + dy, j + dx)
                cnt %= mod
    dp[i][j] = cnt
    return cnt


for i in range(h):
    for j in range(w):
        check(i, j)
print(sum(sum(ans) % mod for ans in dp) % mod)
