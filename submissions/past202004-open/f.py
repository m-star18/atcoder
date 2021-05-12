import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

import heapq

n = int(readline())
ab = [list(map(int, readline().split())) for _ in range(n)]
memo = [[] for _ in range(n)]
for a, b in ab:
    memo[a - 1].append(b * (-1))
ans = []
heapq.heapify(ans)
cnt = 0
for i in range(n):
    for v in memo[i]:
        heapq.heappush(ans, v)
    cnt -= heapq.heappop(ans)
    print(cnt)
