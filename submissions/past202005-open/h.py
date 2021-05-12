import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, l = map(int, readline().split())
x = list(map(int, readline().split()))
xx = [False] * (l + 4)
for dx in x:
    xx[dx] = True
t1, t2, t3 = map(int, readline().split())
dp = [float('inf')] * (l + 4)
dp[0] = 0
for i in range(l):
    dp[i + 1] = min(dp[i + 1], dp[i] + t1 + (t3 if xx[i + 1] else 0))
    v1 = dp[i] + t1 + t2
    v2 = dp[i] + t1 + t2 * 3
    if xx[i + 2]:
        v1 += t3
    if xx[i + 4]:
        v2 += t3
    dp[i + 2] = min(dp[i + 2], v1)
    dp[i + 4] = min(dp[i + 4], v2)
v1 = dp[l - 1] + 0.5 * t1 + 0.5 * t2
v2 = dp[l - 2] + 0.5 * t1 + 1.5 * t2
v3 = dp[l - 3] + 0.5 * t1 + 2.5 * t2
print(int(min(dp[l], v1, v2, v3)))
