import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)


n, k, *a = map(int, read().split())
dp = [False] * (k + 1)
for i in range(k + 1):
    for j in range(n):
        if i - a[j] >= 0:
            dp[i] |= not dp[i - a[j]]
if dp[k]:
    print('First')
else:
    print('Second')
