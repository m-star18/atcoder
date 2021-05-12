import sys
import math
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
cnt = 0

for i in range(n):
    if a[i] != 0:
        cnt += 1

ans = math.ceil(sum(a) / cnt)
print(ans)
