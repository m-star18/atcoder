import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

import itertools

n, k = map(int, readline().split())
memo = [i for i in range(n + 1)]
cumsum = list(itertools.accumulate(memo))
mod = 10 ** 9 + 7
if n < k:
    print(1)
    exit()
ans = 1
for i in range(k - 1, n):
    ans += (cumsum[-1] - cumsum[n - i - 1]) - cumsum[i]
    ans += 1
    ans %= mod
print(ans % mod)
