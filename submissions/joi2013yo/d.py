import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

d, n = map(int, readline().split())
t = [int(readline()) for _ in range(d)]
abc = [list(map(int, readline().split())) for _ in range(n)]
dp = [[0] * n for _ in range(d)]
ans = 0
for i, tt in enumerate(t[:-1]):
    for j, (a, b, c) in enumerate(abc):
        if a <= tt <= b:
            for k, (_, _, cc) in enumerate(abc):
                dp[i + 1][k] = max(dp[i][j] + abs(c - cc), dp[i + 1][k])
for j, (a, b, _) in enumerate(abc):
    if a <= t[-1] <= b:
        ans = max(ans, dp[-1][j])
print(ans)
