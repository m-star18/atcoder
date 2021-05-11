import math
import sys
input = sys.stdin.readline

n = int(input())
x, y = [0]*n, [0]*n
ans = [0]*n**2
c = 0
for i in range(n):
    x[i], y[i] = map(int, input().split())
for i in range(n-1):
    for j in range(n-i-1):
        ans[c] = math.sqrt((x[i+j+1]-x[i])**2 + (y[i+j+1]-y[i])**2)
        c += 1
print(max(ans))
