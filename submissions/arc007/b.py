import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from copy import deepcopy

n, m = map(int, readline().split())
d = [int(input()) for i in range(m)]
ans = [i for i in range(n + 1)]
for check in d:
    memo = deepcopy(ans)
    index = ans.index(check)
    ans[index] = memo[0]
    ans[0] = memo[index]
for a in ans[1:]:
    print(a)
