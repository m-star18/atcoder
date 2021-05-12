import sys
import math
input = sys.stdin.readline

y = int(input())
m = int(input())
d = int(input())

if m <= 2:
  y -= 1
  m += 12

ans = 735369
ans -= 365 * y + math.floor(y / 4) - math.floor(y / 100) + math.floor(y / 400) + math.floor(306 * (m + 1) / 10) + d - 429
print(ans)
