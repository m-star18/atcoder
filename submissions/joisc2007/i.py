import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from bisect import bisect_left

n = int(readline())
inf = float('inf')
memo = [inf] * n
for _ in range(n):
    a = int(readline())
    memo[bisect_left(memo, a)] = a
print(bisect_left(memo, inf))
