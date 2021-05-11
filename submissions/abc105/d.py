import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import defaultdict
from itertools import accumulate

n, m, *a = map(int, read().split())
dict = defaultdict(int)
ans = 0
for v in [0] + list(map(lambda x: int(x) % m, list(accumulate(a)))):
    ans += dict[v]
    dict[v] += 1
print(ans)
