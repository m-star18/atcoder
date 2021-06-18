import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = read().rstrip().decode()
dp = [[0] * 13 for _ in range(len(s))]
mod = 10 ** 9 + 7
if s[0] == '?':
    dp[0] = 10 * [1] + [0] * 3
else:
    dp[0][int(s[0])] += 1
for i, ss in enumerate(s[1:]):
    if ss == '?':
        for j in range(13):
            for k in range(10):
                dp[i + 1][(j * 10 + k) % 13] += dp[i][j]
    else:
        for j in range(13):
            dp[i + 1][(int(ss) + j * 10) % 13] += dp[i][j]
    for j in range(13):
        dp[i + 1][j] %= mod
print(dp[-1][5])
