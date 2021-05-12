import sys
import math
input = sys.stdin.readline

a, b = map(int, input().split())
ans = math.ceil(b / a)
print(ans)
