import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from itertools import product

n, m, x = map(int, readline().split())
ca = [list(map(int, readline().split())) for _ in range(n)]
ans = float('inf')
for bit in product([0, 1], repeat=n):
    cnt = 0
    memo = [0] * m
    for i in range(n):
        if bit[i] == 1:
            cnt += ca[i][0]
            for j in range(m):
                memo[j] += ca[i][j + 1]
    for j in range(m):
        if memo[j] < x:
            break
    else:
        ans = min(ans, cnt)
if ans == float('inf'):
    ans = -1
print(ans)
