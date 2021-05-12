import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

import itertools

n, k, *a = map(int, read().split())
cumsum = list(itertools.accumulate(a))
ans = cumsum[k - 1]
for i in range(n - k):
    ans += cumsum[i + k] - cumsum[i]
print(ans)
