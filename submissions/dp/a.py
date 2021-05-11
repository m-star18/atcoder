import sys
input = sys.stdin.readline

n = int(input())
h = list(map(int, input().split()))
cnt = 0
dp = [0]*n
dp[1] = abs(h[1]-h[0])
for i in range(2, n):
    i_1 = dp[i-1] + abs(h[i]-h[i-1])
    i_2 = dp[i-2] + abs(h[i]-h[i-2])
    if i_1 > i_2:
        dp[i] = i_2
    else:
        dp[i] = i_1
print(dp[n-1])
