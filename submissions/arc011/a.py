import sys
import math
input = sys.stdin.readline

m, n, N = map(int, input().split())
ans = 0
memo = 0
for i in range(N):
    ans += N
    N += memo
    memo = N % m
    if N < m:
        break
    N = math.floor(N / m) * n
print(ans)
