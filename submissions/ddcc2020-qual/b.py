import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

import itertools
import bisect

n = int(readline())
a = tuple(map(int, readline().split()))
cumsum = tuple(itertools.accumulate(a))
index = bisect.bisect(cumsum, sum(a) // 2)
ans = min(cumsum[n - 1] - cumsum[index - 1] * 2, cumsum[index] * 2 - cumsum[n - 1])
print(ans)
