import sys
import math
input = sys.stdin.readline

q, h, s, d = map(int, input().split())
n = int(input())
ans = 0

if n >= 2:
  ans += min(8 * q, 4 * h, 2 * s, d) * math.floor(n / 2)

if n % 2 == 1:
  ans += min(4 * q, 2 * h, s)
  
print(ans)
