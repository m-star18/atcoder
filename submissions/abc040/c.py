import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dp = [0]*n
dp[1] = abs(a[1]-a[0])
for i in range(2, n):
    i_1 = dp[i-1] + abs(a[i]-a[i-1])
    i_2 = dp[i-2] + abs(a[i]-a[i-2])
    if i_1 > i_2:
        dp[i] = i_2
    else:
        dp[i] = i_1
print(dp[n-1])
