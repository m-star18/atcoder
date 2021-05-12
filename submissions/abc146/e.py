import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import defaultdict
from itertools import accumulate

n, k = map(int, readline().split())
a = list(map(lambda x: int(x) - 1, readline().split()))
cumsum = [0] + list(map(lambda x: int(x) % k, list(accumulate(a))))
dict = defaultdict(int)
ans = 0
for i, v in enumerate(cumsum):
    ans += dict[v]
    dict[v] += 1
    if i >= k - 1:
        dict[cumsum[i - k + 1]] -= 1
print(ans)
