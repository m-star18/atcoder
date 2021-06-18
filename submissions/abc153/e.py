import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

h, n = map(int, readline().split())
ab = [list(map(int, readline().split())) for _ in range(n)]
inf = float('inf')
dp = [inf] * (h + 1)
dp[0] = 0
for a, b in ab:
    for j in range(h):
        if dp[j] != inf:
            if a + j > h:
                dp[-1] = min(dp[-1], dp[j] + b)
            else:
                dp[a + j] = min(dp[a + j], dp[j] + b)
print(dp[-1])
