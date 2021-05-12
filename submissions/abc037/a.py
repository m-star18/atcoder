import sys
import math
input = sys.stdin.readline

a, b, c = map(int, input().split())
ans = math.floor(c / min(a, b))
print(ans)
