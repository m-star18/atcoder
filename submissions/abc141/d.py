import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

import heapq

n, m = map(int, readline().split())
a = list(map(lambda x: int(x)*(-1), readline().split()))
heapq.heapify(a)
for i in range(m):
    memo = heapq.heappop(a)
    heapq.heappush(a, (-memo // 2) * (-1))
print(-sum(a))
