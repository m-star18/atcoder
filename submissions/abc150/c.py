import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

import itertools

n = int(readline())
p = tuple(map(int, readline().split()))
q = tuple(map(int, readline().split()))
ans = list(itertools.permutations([(i + 1) for i in range(n)]))
print(abs(ans.index(p) - ans.index(q)))
