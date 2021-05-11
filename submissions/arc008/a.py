import sys
import math
input = sys.stdin.readline

n = int(input())

n_f = math.floor(n / 10)

if n - n_f * 10 < 7:
  ans = (n - n_f * 10) * 15
else:
  ans = 100

ans += n_f * 100
print(ans)
