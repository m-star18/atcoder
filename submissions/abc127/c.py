import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

import itertools

n, m = map(int, readline().split())
lr = [list(map(int, readline().split())) for i in range(m)]
memo = [0] * (n + 1)
for l, r in lr:
    memo[l - 1] += 1
    memo[r] -= 1
cumsum = list(itertools.accumulate(memo))
cnt = 0
for i in range(n):
    if cumsum[i] == m:
        cnt += 1
print(cnt)
