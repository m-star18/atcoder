import sys
input = sys.stdin.readline

n = int(input())
a = [0] * n
b = [0] * n
c = [0] * n
for i in range(n):
    a[i], b[i], c[i] = list(map(int, input().split()))

dp = [[0 for i in range(3)] for j in range(n)]
dp[0][0] = a[0]
dp[0][1] = b[0]
dp[0][2] = c[0]

for i in range(1, n):
    dp[i][0] = a[i] + max(dp[i - 1][1], dp[i - 1][2])
    dp[i][1] = b[i] + max(dp[i - 1][0], dp[i - 1][2])
    dp[i][2] = c[i] + max(dp[i - 1][0], dp[i - 1][1])
print(max(dp[-1]))
