import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, m = map(int, readline().split())
a = list(map(int, readline().split()))
memo = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
dp = [''] * (n + 1)
for aa in a:
    if memo[aa] <= n:
        dp[memo[aa]] = max(dp[memo[aa]], str(aa))
for i in range(n):
    if dp[i] == '':
        continue
    for aa in a:
        if i + memo[aa] <= n:
            v = str(aa) + dp[i]
            if len(dp[i + memo[aa]]) < len(v):
                dp[i + memo[aa]] = v
            else:
                dp[i + memo[aa]] = max(dp[i + memo[aa]], v)
print(dp[-1])
