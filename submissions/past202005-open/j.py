import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from bisect import bisect_right

n, m = map(int, readline().split())
a = list(map(int, readline().split()))
memo = [0] * (n + 1)
for aa in a:
    idx = bisect_right(memo, aa - 1) - 1
    if idx != 0:
        memo[idx] = aa
        print(n - idx + 1)
    else:
        print(-1)
