import sys
import math
input = sys.stdin.readline

h, w = map(int, input().split())
ans = math.ceil(w / 2) * math.ceil(h / 2) + math.floor(w / 2) * math.floor(h / 2)
if h == 1 or w == 1:
    ans = 1
print(ans)
