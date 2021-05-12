import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from math import ceil

n = int(readline())
c = [int(readline()) for _ in range(n)] * 2
ans = 0
cnt = 1
memo = c[0]
for i in range(1, 2 * n):
    if memo == c[i]:
        cnt += 1
    else:
        v = ceil(cnt / 2)
        if ans < v:
            ans = v
        cnt = 1
        memo = c[i]
if cnt == 2 * n:
    print(-1)
else:
    print(ans)
