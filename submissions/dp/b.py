import sys
input = sys.stdin.readline

n, k = map(int, input().split())
h = list(map(int, input().split()))
dp = [0] * n
dp_memo = [10 ** 4] * k

for i in range(1, n):
    for j in range(min(k, i)):
        dp_memo[j] = abs(h[i] - h[i - j - 1]) + dp[i - j - 1]
    dp[i] = min(dp_memo)
    dp_memo = [10 ** 4] * k

print(dp[n - 1])
