import sys
import math
input = sys.stdin.readline

n = int(input())
r = [0] * n
for i in range(n):
  r[i] = int(input())
r.sort(reverse=True)
ans = 0

for i in range(n):
  if i % 2 == 0:
    ans += r[i] ** 2
  else:
    ans -= r[i] ** 2
  
ans *= math.pi
print(ans)
