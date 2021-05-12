import sys
import math
input = sys.stdin.readline

x = int(input())

if 105 * math.floor(x / 100) >= x:
  ans = '1'
else:
  ans = '0'

print(ans)
