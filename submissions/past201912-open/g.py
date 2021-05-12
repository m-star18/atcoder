import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from itertools import product

n = int(readline())
a = [list(map(int, readline().split())) for _ in range(n - 1)]
ans = -float('inf')
for bit in product(range(3), repeat=n):
    memo = [[], [], []]
    cnt = 0
    for i in range(n):
        memo[bit[i]].append(i)
    for m in memo:
        for i, x in enumerate(m):
            for y in m[i + 1:]:
                cnt += a[x][y - x - 1]
    ans = max(ans, cnt)
print(ans)
