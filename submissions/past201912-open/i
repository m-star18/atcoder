import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from itertools import product

n, m = map(int, readline().split())
inf = float('inf')
dp = [inf] * (2 ** n)
dp[0] = 0
for _ in range(m):
    s, c = readline().rstrip().decode().split()
    c = int(c)
    bit = [0] * n
    for i, ss in enumerate(s):
        if ss == 'Y':
            bit[i] = 1
    for i, v in enumerate(product([0, 1], repeat=n)):
        if dp[i] != inf:
            num = 0
            for index, (x, y) in enumerate(zip(v[::-1], bit)):
                if x == 1 or y == 1:
                    num += 2 ** index
            dp[num] = min(dp[num], dp[i] + c)
print(-1 if dp[-1] == inf else dp[-1])
