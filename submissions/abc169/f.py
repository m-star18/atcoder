import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, s, *a = map(int, read().split())
dp = [0] * (s + 1)
dp[0] = 1
mod = 998244353
for aa in a:
    for j in range(s, -1, -1):
        ss = j + aa
        if ss <= s:
            dp[ss] += dp[j]
            dp[ss] %= mod
        dp[j] *= 2
        dp[j] %= mod
print(dp[-1])
