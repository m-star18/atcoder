import sys
import math
input = sys.stdin.readline

k, a, b = map(int, input().split())
if b > a and k + 1 > a:
    ans = max(k + 1, (b - a) * math.floor((k + 1 - a) / 2) + (k + 1 - a) % 2 + a)
else:
    ans = k + 1
print(ans)
