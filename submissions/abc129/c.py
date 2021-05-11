import sys
input = sys.stdin.readline


n, m = map(int, input().split())
a = [0] * m
dp = [0] * (n + 1)
mod = 10 ** 9 + 7
for i in range(m):
    a[i] = int(input())
a = set(a)
dp[:2] = 1, 1 if 1 not in a else 0

for i in range(2, n + 1):
    if i not in a:
        dp[i] = (dp[i - 1] + dp[i - 2]) % mod
print(dp[-1])
