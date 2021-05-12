import sys
import math
input = sys.stdin.readline

n = int(input())
ab = [list(map(int, input().split())) for i in range(n)]
ans = 0
for i in range(n):
    ans += ab[i][0] * ab[i][1]
print(math.floor(ans * 1.05))
