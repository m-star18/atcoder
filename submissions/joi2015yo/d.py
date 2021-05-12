import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, m = map(int, readline().split())
d = [int(readline()) for _ in range(n)]
dp = [-1] * (n + 1)
dp[0] = 0
for i in range(m):
    c = int(readline())
    for j in range(n - 1, -1, -1):
        if dp[j] != -1:
            v = dp[j] + c * d[j]
            if dp[j + 1] == -1:
                dp[j + 1] = v
            elif dp[j + 1] > v:
                dp[j + 1] = v
print(dp[-1])
